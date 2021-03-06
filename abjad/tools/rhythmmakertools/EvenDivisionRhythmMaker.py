# -*- encoding: utf-8 -*-
import math
from abjad.tools import datastructuretools
from abjad.tools import durationtools
from abjad.tools import mathtools
from abjad.tools import scoretools
from abjad.tools import selectiontools
from abjad.tools.rhythmmakertools.RhythmMaker import RhythmMaker


class EvenDivisionRhythmMaker(RhythmMaker):
    r'''Even division rhythm-maker.

    Object model of a partially evaluated function that accepts a (possibly
    empty) list of divisions as input and returns a list of selections as
    output (structured one selection per input division).
    '''

    ### CLASS VARIABLES ###

    __slots__ = (
        '_denominators',
        '_extra_counts_per_division',
        )

    _human_readable_class_name = 'even division rhythm-maker'

    ### INITIALIZER ###

    def __init__(
        self,
        denominators=[8],
        extra_counts_per_division=None,
        beam_specifier=None,
        duration_spelling_specifier=None,
        tie_specifier=None,
        tuplet_spelling_specifier=None,
        ):
        RhythmMaker.__init__(
            self,
            beam_specifier=beam_specifier,
            duration_spelling_specifier=duration_spelling_specifier,
            tie_specifier=tie_specifier,
            tuplet_spelling_specifier=tuplet_spelling_specifier,
            )
        assert mathtools.all_are_nonnegative_integer_powers_of_two(
            denominators), repr(denominators)
        denominators = tuple(denominators)
        self._denominators = denominators
        if extra_counts_per_division is not None:
            assert mathtools.all_are_integer_equivalent_exprs(
                extra_counts_per_division), repr(extra_counts_per_division)
            extra_counts_per_division = [
                int(_) for _ in extra_counts_per_division
                ]
            extra_counts_per_division = tuple(extra_counts_per_division)
        self._extra_counts_per_division = extra_counts_per_division

    ### SPECIAL METHODS ###

    def __call__(self, divisions, seeds=None):
        r'''Calls even division rhythm-maker on `divisions`.

        ..  container:: example

                >>> maker = rhythmmakertools.EvenDivisionRhythmMaker(
                ...     denominators=[16, 16, 8],
                ...     extra_counts_per_division=[1, 0],
                ...     )

            ::

                >>> divisions = [(3, 8), (4, 8), (3, 8), (4, 8)]
                >>> selections = maker(divisions)

            ::

                >>> for selection in selections:
                ...     selection
                Selection(FixedDurationTuplet(Duration(3, 8), "c'16 c'16 c'16 c'16 c'16 c'16 c'16"),)
                Selection(FixedDurationTuplet(Duration(1, 2), "c'16 c'16 c'16 c'16 c'16 c'16 c'16 c'16"),)
                Selection(FixedDurationTuplet(Duration(3, 8), "c'8 c'8 c'8 c'8"),)
                Selection(FixedDurationTuplet(Duration(1, 2), "c'16 c'16 c'16 c'16 c'16 c'16 c'16 c'16"),)

            ::

                >>> lilypond_file = rhythmmakertools.make_lilypond_file(
                ...     selections,
                ...     divisions,
                ...     )
                >>> show(lilypond_file) # doctest: +SKIP

            ..  doctest::

                >>> staff = maker._get_rhythmic_staff(lilypond_file)
                >>> f(staff)
                \new RhythmicStaff {
                    {
                        \time 3/8
                        \tweak #'text #tuplet-number::calc-fraction-text
                        \times 6/7 {
                            c'16 [
                            c'16
                            c'16
                            c'16
                            c'16
                            c'16
                            c'16 ]
                        }
                    }
                    {
                        \time 4/8
                        {
                            c'16 [
                            c'16
                            c'16
                            c'16
                            c'16
                            c'16
                            c'16
                            c'16 ]
                        }
                    }
                    {
                        \time 3/8
                        \tweak #'text #tuplet-number::calc-fraction-text
                        \times 3/4 {
                            c'8 [
                            c'8
                            c'8
                            c'8 ]
                        }
                    }
                    {
                        \time 4/8
                        {
                            c'16 [
                            c'16
                            c'16
                            c'16
                            c'16
                            c'16
                            c'16
                            c'16 ]
                        }
                    }
                }

        Returns list of of selections.
        '''
        return RhythmMaker.__call__(
            self,
            divisions,
            seeds=seeds,
            )

    ### PRIVATE PROPERTIES ###

    @property
    def _attribute_manifest(self):
        from abjad.tools import rhythmmakertools
        from abjad.tools import systemtools
        from ide import idetools
        return systemtools.AttributeManifest(
            systemtools.AttributeDetail(
                name='denominators',
                command='d',
                editor=idetools.getters.get_positive_integer_powers_of_two,
                ),
            systemtools.AttributeDetail(
                name='extra_counts_per_division',
                command='ec',
                editor=idetools.getters.get_integers,
                ),
            systemtools.AttributeDetail(
                name='beam_specifier',
                command='bs',
                editor=rhythmmakertools.BeamSpecifier,
                ),
            systemtools.AttributeDetail(
                name='duration_spelling_specifier',
                command='ds',
                editor=rhythmmakertools.DurationSpellingSpecifier,
                ),
            systemtools.AttributeDetail(
                name='tie_specifier',
                command='ts',
                editor=rhythmmakertools.TieSpecifier,
                ),
            )

    ### PRIVATE METHODS ###

    def _make_music(self, divisions, seeds):
        #assert not seeds, repr(seeds)
        if seeds is None:
            seeds = 0
        selections = []
        divisions = [durationtools.Division(_) for _ in divisions]
        denominators = datastructuretools.CyclicTuple(self.denominators)
        extra_counts_per_division = self.extra_counts_per_division or (0,)
        extra_counts_per_division = datastructuretools.CyclicTuple(
            extra_counts_per_division
            )
        for i, division in enumerate(divisions, seeds):
            # not yet extended to work with non-power-of-two divisions
            assert mathtools.is_positive_integer_power_of_two(
                division.denominator), repr(division)
            denominator = denominators[i]
            extra_count = extra_counts_per_division[i]
            basic_duration = durationtools.Duration(1, denominator)
            unprolated_note_count = None
            if division < 2 * basic_duration:
                notes = scoretools.make_notes([0], [division])
            else:
                unprolated_note_count = division / basic_duration
                unprolated_note_count = int(unprolated_note_count)
                unprolated_note_count = unprolated_note_count or 1
                if 0 < extra_count:
                    modulus = unprolated_note_count
                    extra_count = extra_count % modulus
                elif extra_count < 0:
                    modulus = int(math.ceil(unprolated_note_count / 2.0))
                    extra_count = abs(extra_count) % modulus
                    extra_count *= -1
                note_count = unprolated_note_count + extra_count
                durations = note_count * [basic_duration]
                notes = scoretools.make_notes([0], durations)
                assert all(
                    _.written_duration.denominator == denominator
                    for _ in notes
                    )
            tuplet_duration = durationtools.Duration(division)
            tuplet = scoretools.FixedDurationTuplet(
                duration=tuplet_duration,
                music=notes,
                )
            if unprolated_note_count is not None:
                preferred_denominator = unprolated_note_count
                tuplet.preferred_denominator = preferred_denominator
            selection = selectiontools.Selection(tuplet)
            selections.append(selection)
        self._apply_beam_specifier(selections)
        return selections

    ### PUBLIC PROPERTIES ###

    @property
    def denominators(self):
        r'''Gets denominators of rhythm-maker.

        ..  container:: example

            **Example 1.** Fills divisions with 16th notes:

            ::


                >>> maker = rhythmmakertools.EvenDivisionRhythmMaker(
                ...     denominators=[16],
                ...     )

            ::

                >>> divisions = [(3, 16), (3, 8), (3, 4)]
                >>> selections = maker(divisions)
                >>> lilypond_file = rhythmmakertools.make_lilypond_file(
                ...     selections,
                ...     divisions,
                ...     )
                >>> show(lilypond_file) # doctest: +SKIP

            ..  doctest::

                >>> staff = maker._get_rhythmic_staff(lilypond_file)
                >>> f(staff)
                \new RhythmicStaff {
                    {
                        \time 3/16
                        {
                            c'16 [
                            c'16
                            c'16 ]
                        }
                    }
                    {
                        \time 3/8
                        {
                            c'16 [
                            c'16
                            c'16
                            c'16
                            c'16
                            c'16 ]
                        }
                    }
                    {
                        \time 3/4
                        {
                            c'16 [
                            c'16
                            c'16
                            c'16
                            c'16
                            c'16
                            c'16
                            c'16
                            c'16
                            c'16
                            c'16
                            c'16 ]
                        }
                    }
                }

        ..  container:: example

            **Example 2.** Fills divisions with 8th notes:

            ::


                >>> maker = rhythmmakertools.EvenDivisionRhythmMaker(
                ...     denominators=[8],
                ...     )

            ::

                >>> divisions = [(3, 16), (3, 8), (3, 4)]
                >>> selections = maker(divisions)
                >>> lilypond_file = rhythmmakertools.make_lilypond_file(
                ...     selections,
                ...     divisions,
                ...     )
                >>> show(lilypond_file) # doctest: +SKIP

            ..  doctest::

                >>> staff = maker._get_rhythmic_staff(lilypond_file)
                >>> f(staff)
                \new RhythmicStaff {
                    {
                        \time 3/16
                        {
                            c'8.
                        }
                    }
                    {
                        \time 3/8
                        {
                            c'8 [
                            c'8
                            c'8 ]
                        }
                    }
                    {
                        \time 3/4
                        {
                            c'8 [
                            c'8
                            c'8
                            c'8
                            c'8
                            c'8 ]
                        }
                    }
                }

            Divisions less than twice the duration of an eighth note are filled
            with a single attack.

        ..  container:: example

            **Example 3.** Fills divisions with quarter notes:

            ::


                >>> maker = rhythmmakertools.EvenDivisionRhythmMaker(
                ...     denominators=[4],
                ...     )

            ::

                >>> divisions = [(3, 16), (3, 8), (3, 4)]
                >>> selections = maker(divisions)
                >>> lilypond_file = rhythmmakertools.make_lilypond_file(
                ...     selections,
                ...     divisions,
                ...     )
                >>> show(lilypond_file) # doctest: +SKIP

            ..  doctest::

                >>> staff = maker._get_rhythmic_staff(lilypond_file)
                >>> f(staff)
                \new RhythmicStaff {
                    {
                        \time 3/16
                        {
                            c'8.
                        }
                    }
                    {
                        \time 3/8
                        {
                            c'4.
                        }
                    }
                    {
                        \time 3/4
                        {
                            c'4
                            c'4
                            c'4
                        }
                    }
                }

            Divisions less than twice the duration of a quarter note are filled
            with a single attack.

        ..  container:: example

            **Example 4.** Fills divisions with half notes:

            ::


                >>> maker = rhythmmakertools.EvenDivisionRhythmMaker(
                ...     denominators=[2],
                ...     )

            ::

                >>> divisions = [(3, 16), (3, 8), (3, 4)]
                >>> selections = maker(divisions)
                >>> lilypond_file = rhythmmakertools.make_lilypond_file(
                ...     selections,
                ...     divisions,
                ...     )
                >>> show(lilypond_file) # doctest: +SKIP

            ..  doctest::

                >>> staff = maker._get_rhythmic_staff(lilypond_file)
                >>> f(staff)
                \new RhythmicStaff {
                    {
                        \time 3/16
                        {
                            c'8.
                        }
                    }
                    {
                        \time 3/8
                        {
                            c'4.
                        }
                    }
                    {
                        \time 3/4
                        {
                            c'2.
                        }
                    }
                }

            Divisions less than twice the duration of a half note are filled
            with a single attack.

        Returns tuple of nonnegative integer powers of two.
        '''
        return self._denominators

    @property
    def extra_counts_per_division(self):
        r'''Gets extra counts per division of rhythm-maker.

        Treats overly large and overly small values of
        `extra_counts_per_division` modularly. Denote by
        `unprolated_note_count` the number of unprolated notes included in any
        division (as though `extra_counts_per_division` were set to zero). Then
        the actual number of extra counts included per division is given by two
        formulas:

        * The actual number of extra counts included per division is given by
          ``extra_counts_per_division % unprolated_note_count`` when
          `extra_counts_per_division` is positive.

        * The actual number of extra counts included per division is given by
          the formula
          ``extra_counts_per_division % ceiling(unprolated_note_count / 2)``
          when `extra_counts_per_division` is negative.

        These formulas ensure that:

        * even very large and very small values of
          `extra_counts_per_division` produce valid output, and that

        * the values given as the rhythm-maker's `denominators` are always
          respected. A very large value of `extra_counts_per_division`, for
          example, never causes a `16`-denominated division to result 32nd or
          64th note rhythms; `16`-denominated divisions always produce 16th
          note rhythms.

        ..  container:: example

            **Example -4.** Four missing counts per division:

            ::


                >>> maker = rhythmmakertools.EvenDivisionRhythmMaker(
                ...     denominators=[16],
                ...     extra_counts_per_division=[-4],
                ...     )

            ::

                >>> divisions = [(1, 16), (2, 16), (3, 16), (4, 16), (5, 16)]
                >>> selections = maker(divisions)
                >>> lilypond_file = rhythmmakertools.make_lilypond_file(
                ...     selections,
                ...     divisions,
                ...     )
                >>> show(lilypond_file) # doctest: +SKIP

            ..  doctest::

                >>> staff = maker._get_rhythmic_staff(lilypond_file)
                >>> f(staff)
                \new RhythmicStaff {
                    {
                        \time 1/16
                        {
                            c'16
                        }
                    }
                    {
                        \time 2/16
                        {
                            c'16 [
                            c'16 ]
                        }
                    }
                    {
                        \time 3/16
                        {
                            c'16 [
                            c'16
                            c'16 ]
                        }
                    }
                    {
                        \time 4/16
                        {
                            c'16 [
                            c'16
                            c'16
                            c'16 ]
                        }
                    }
                    {
                        \time 5/16
                        \tweak #'text #tuplet-number::calc-fraction-text
                        \times 5/4 {
                            c'16 [
                            c'16
                            c'16
                            c'16 ]
                        }
                    }
                }

        ..  container:: example

            **Example -3.** Three missing counts per division:

            ::


                >>> maker = rhythmmakertools.EvenDivisionRhythmMaker(
                ...     denominators=[16],
                ...     extra_counts_per_division=[-3],
                ...     )

            ::

                >>> divisions = [(1, 16), (2, 16), (3, 16), (4, 16), (5, 16)]
                >>> selections = maker(divisions)
                >>> lilypond_file = rhythmmakertools.make_lilypond_file(
                ...     selections,
                ...     divisions,
                ...     )
                >>> show(lilypond_file) # doctest: +SKIP

            ..  doctest::

                >>> staff = maker._get_rhythmic_staff(lilypond_file)
                >>> f(staff)
                \new RhythmicStaff {
                    {
                        \time 1/16
                        {
                            c'16
                        }
                    }
                    {
                        \time 2/16
                        {
                            c'16 [
                            c'16 ]
                        }
                    }
                    {
                        \time 3/16
                        \tweak #'text #tuplet-number::calc-fraction-text
                        \times 3/2 {
                            c'16 [
                            c'16 ]
                        }
                    }
                    {
                        \time 4/16
                        \tweak #'text #tuplet-number::calc-fraction-text
                        \times 4/3 {
                            c'16 [
                            c'16
                            c'16 ]
                        }
                    }
                    {
                        \time 5/16
                        {
                            c'16 [
                            c'16
                            c'16
                            c'16
                            c'16 ]
                        }
                    }
                }

        ..  container:: example

            **Example -2.** Two missing counts per division:

            ::


                >>> maker = rhythmmakertools.EvenDivisionRhythmMaker(
                ...     denominators=[16],
                ...     extra_counts_per_division=[-2],
                ...     )

            ::

                >>> divisions = [(1, 16), (2, 16), (3, 16), (4, 16), (5, 16)]
                >>> selections = maker(divisions)
                >>> lilypond_file = rhythmmakertools.make_lilypond_file(
                ...     selections,
                ...     divisions,
                ...     )
                >>> show(lilypond_file) # doctest: +SKIP

            ..  doctest::

                >>> staff = maker._get_rhythmic_staff(lilypond_file)
                >>> f(staff)
                \new RhythmicStaff {
                    {
                        \time 1/16
                        {
                            c'16
                        }
                    }
                    {
                        \time 2/16
                        {
                            c'16 [
                            c'16 ]
                        }
                    }
                    {
                        \time 3/16
                        {
                            c'16 [
                            c'16
                            c'16 ]
                        }
                    }
                    {
                        \time 4/16
                        {
                            c'16 [
                            c'16
                            c'16
                            c'16 ]
                        }
                    }
                    {
                        \time 5/16
                        \tweak #'text #tuplet-number::calc-fraction-text
                        \times 5/3 {
                            c'16 [
                            c'16
                            c'16 ]
                        }
                    }
                }

        ..  container:: example

            **Example -1.** One missing count per division:

            ::


                >>> maker = rhythmmakertools.EvenDivisionRhythmMaker(
                ...     denominators=[16],
                ...     extra_counts_per_division=[-1],
                ...     )

            ::

                >>> divisions = [(1, 16), (2, 16), (3, 16), (4, 16), (5, 16)]
                >>> selections = maker(divisions)
                >>> lilypond_file = rhythmmakertools.make_lilypond_file(
                ...     selections,
                ...     divisions,
                ...     )
                >>> show(lilypond_file) # doctest: +SKIP

            ..  doctest::

                >>> staff = maker._get_rhythmic_staff(lilypond_file)
                >>> f(staff)
                \new RhythmicStaff {
                    {
                        \time 1/16
                        {
                            c'16
                        }
                    }
                    {
                        \time 2/16
                        {
                            c'16 [
                            c'16 ]
                        }
                    }
                    {
                        \time 3/16
                        \tweak #'text #tuplet-number::calc-fraction-text
                        \times 3/2 {
                            c'16 [
                            c'16 ]
                        }
                    }
                    {
                        \time 4/16
                        \tweak #'text #tuplet-number::calc-fraction-text
                        \times 4/3 {
                            c'16 [
                            c'16
                            c'16 ]
                        }
                    }
                    {
                        \time 5/16
                        \tweak #'text #tuplet-number::calc-fraction-text
                        \times 5/4 {
                            c'16 [
                            c'16
                            c'16
                            c'16 ]
                        }
                    }
                }

        ..  container:: example

            **Example 0.** No extra counts per division:

            ::


                >>> maker = rhythmmakertools.EvenDivisionRhythmMaker(
                ...     denominators=[16],
                ...     extra_counts_per_division=None,
                ...     )

            ::

                >>> divisions = [(1, 16), (2, 16), (3, 16), (4, 16), (5, 16)]
                >>> selections = maker(divisions)
                >>> lilypond_file = rhythmmakertools.make_lilypond_file(
                ...     selections,
                ...     divisions,
                ...     )
                >>> show(lilypond_file) # doctest: +SKIP

            ..  doctest::

                >>> staff = maker._get_rhythmic_staff(lilypond_file)
                >>> f(staff)
                \new RhythmicStaff {
                    {
                        \time 1/16
                        {
                            c'16
                        }
                    }
                    {
                        \time 2/16
                        {
                            c'16 [
                            c'16 ]
                        }
                    }
                    {
                        \time 3/16
                        {
                            c'16 [
                            c'16
                            c'16 ]
                        }
                    }
                    {
                        \time 4/16
                        {
                            c'16 [
                            c'16
                            c'16
                            c'16 ]
                        }
                    }
                    {
                        \time 5/16
                        {
                            c'16 [
                            c'16
                            c'16
                            c'16
                            c'16 ]
                        }
                    }
                }

        ..  container:: example

            **Example 1.** One extra count per division:

            ::


                >>> maker = rhythmmakertools.EvenDivisionRhythmMaker(
                ...     denominators=[16],
                ...     extra_counts_per_division=[1],
                ...     )

            ::

                >>> divisions = [(1, 16), (2, 16), (3, 16), (4, 16), (5, 16)]
                >>> selections = maker(divisions)
                >>> lilypond_file = rhythmmakertools.make_lilypond_file(
                ...     selections,
                ...     divisions,
                ...     )
                >>> show(lilypond_file) # doctest: +SKIP

            ..  doctest::

                >>> staff = maker._get_rhythmic_staff(lilypond_file)
                >>> f(staff)
                \new RhythmicStaff {
                    {
                        \time 1/16
                        {
                            c'16
                        }
                    }
                    {
                        \time 2/16
                        \times 2/3 {
                            c'16 [
                            c'16
                            c'16 ]
                        }
                    }
                    {
                        \time 3/16
                        \tweak #'text #tuplet-number::calc-fraction-text
                        \times 3/4 {
                            c'16 [
                            c'16
                            c'16
                            c'16 ]
                        }
                    }
                    {
                        \time 4/16
                        \times 4/5 {
                            c'16 [
                            c'16
                            c'16
                            c'16
                            c'16 ]
                        }
                    }
                    {
                        \time 5/16
                        \tweak #'text #tuplet-number::calc-fraction-text
                        \times 5/6 {
                            c'16 [
                            c'16
                            c'16
                            c'16
                            c'16
                            c'16 ]
                        }
                    }
                }

        ..  container:: example

            **Example 2.** Two extra counts per division:

            ::


                >>> maker = rhythmmakertools.EvenDivisionRhythmMaker(
                ...     denominators=[16],
                ...     extra_counts_per_division=[2],
                ...     )

            ::

                >>> divisions = [(1, 16), (2, 16), (3, 16), (4, 16), (5, 16)]
                >>> selections = maker(divisions)
                >>> lilypond_file = rhythmmakertools.make_lilypond_file(
                ...     selections,
                ...     divisions,
                ...     )
                >>> show(lilypond_file) # doctest: +SKIP

            ..  doctest::

                >>> staff = maker._get_rhythmic_staff(lilypond_file)
                >>> f(staff)
                \new RhythmicStaff {
                    {
                        \time 1/16
                        {
                            c'16
                        }
                    }
                    {
                        \time 2/16
                        {
                            c'16 [
                            c'16 ]
                        }
                    }
                    {
                        \time 3/16
                        \tweak #'text #tuplet-number::calc-fraction-text
                        \times 3/5 {
                            c'16 [
                            c'16
                            c'16
                            c'16
                            c'16 ]
                        }
                    }
                    {
                        \time 4/16
                        \times 4/6 {
                            c'16 [
                            c'16
                            c'16
                            c'16
                            c'16
                            c'16 ]
                        }
                    }
                    {
                        \time 5/16
                        \tweak #'text #tuplet-number::calc-fraction-text
                        \times 5/7 {
                            c'16 [
                            c'16
                            c'16
                            c'16
                            c'16
                            c'16
                            c'16 ]
                        }
                    }
                }

        ..  container:: example

            **Example 3.** Three extra counts per division:

            ::


                >>> maker = rhythmmakertools.EvenDivisionRhythmMaker(
                ...     denominators=[16],
                ...     extra_counts_per_division=[3],
                ...     )

            ::

                >>> divisions = [(1, 16), (2, 16), (3, 16), (4, 16), (5, 16)]
                >>> selections = maker(divisions)
                >>> lilypond_file = rhythmmakertools.make_lilypond_file(
                ...     selections,
                ...     divisions,
                ...     )
                >>> show(lilypond_file) # doctest: +SKIP

            ..  doctest::

                >>> staff = maker._get_rhythmic_staff(lilypond_file)
                >>> f(staff)
                \new RhythmicStaff {
                    {
                        \time 1/16
                        {
                            c'16
                        }
                    }
                    {
                        \time 2/16
                        \times 2/3 {
                            c'16 [
                            c'16
                            c'16 ]
                        }
                    }
                    {
                        \time 3/16
                        {
                            c'16 [
                            c'16
                            c'16 ]
                        }
                    }
                    {
                        \time 4/16
                        \times 4/7 {
                            c'16 [
                            c'16
                            c'16
                            c'16
                            c'16
                            c'16
                            c'16 ]
                        }
                    }
                    {
                        \time 5/16
                        \tweak #'text #tuplet-number::calc-fraction-text
                        \times 5/8 {
                            c'16 [
                            c'16
                            c'16
                            c'16
                            c'16
                            c'16
                            c'16
                            c'16 ]
                        }
                    }
                }


        ..  container:: example

            **Example 4.** Four extra counts per division:

            ::


                >>> maker = rhythmmakertools.EvenDivisionRhythmMaker(
                ...     denominators=[16],
                ...     extra_counts_per_division=[4],
                ...     )

            ::

                >>> divisions = [(1, 16), (2, 16), (3, 16), (4, 16), (5, 16)]
                >>> selections = maker(divisions)
                >>> lilypond_file = rhythmmakertools.make_lilypond_file(
                ...     selections,
                ...     divisions,
                ...     )
                >>> show(lilypond_file) # doctest: +SKIP

            ..  doctest::

                >>> staff = maker._get_rhythmic_staff(lilypond_file)
                >>> f(staff)
                \new RhythmicStaff {
                    {
                        \time 1/16
                        {
                            c'16
                        }
                    }
                    {
                        \time 2/16
                        {
                            c'16 [
                            c'16 ]
                        }
                    }
                    {
                        \time 3/16
                        \tweak #'text #tuplet-number::calc-fraction-text
                        \times 3/4 {
                            c'16 [
                            c'16
                            c'16
                            c'16 ]
                        }
                    }
                    {
                        \time 4/16
                        {
                            c'16 [
                            c'16
                            c'16
                            c'16 ]
                        }
                    }
                    {
                        \time 5/16
                        \tweak #'text #tuplet-number::calc-fraction-text
                        \times 5/9 {
                            c'16 [
                            c'16
                            c'16
                            c'16
                            c'16
                            c'16
                            c'16
                            c'16
                            c'16 ]
                        }
                    }
                }

        Returns (possibly empty) tuple of integers or none.
        '''
        return self._extra_counts_per_division

    @property
    def tuplet_spelling_specifier(self):
        r'''Gets tuplet spelling specifier of even division rhythm-maker.

        ..  note:: note yet implemented.

        Returns tuplet spelling specifier or none.
        '''
        superclass = super(EvenDivisionRhythmMaker, self)
        return superclass.tuplet_spelling_specifier