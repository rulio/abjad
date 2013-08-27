# -*- encoding: utf-8 -*-
import fractions
import math
from abjad.tools import durationtools
from abjad.tools import formattools
from abjad.tools import mathtools
from abjad.tools import sequencetools
from abjad.tools.containertools.Container import Container


class Tuplet(Container):
    r'''A tuplet.

    ..  container:: example

        ::

            >>> tuplet = Tuplet(Multiplier(2, 3), "c'8 d'8 e'8")
            >>> show(tuplet) # doctest: +SKIP

        ..  doctest::

            >>> f(tuplet)
            \times 2/3 {
                c'8
                d'8
                e'8
            }

    ..  container:: example

        ::

            >>> second_tuplet = Tuplet((4, 7), "g'4. ( a'16 )")
            >>> tuplet.insert(1, second_tuplet)
            >>> show(tuplet) # doctest: +SKIP

        ..  doctest::

            >>> f(tuplet)
            \times 2/3 {
                c'8
                \times 4/7 {
                    g'4. (
                    a'16 )
                }
                d'8
                e'8
            }


    ..  container:: example

        ::

            >>> third_tuplet = Tuplet((4, 5), [])
            >>> third_tuplet.extend("e''32 [ ef''32 d''32 cs''32 cqs''32 ]")
            >>> second_tuplet.insert(1, third_tuplet)
            >>> show(tuplet) # doctest: +SKIP

        ..  doctest::

            >>> f(tuplet)
            \times 2/3 {
                c'8
                \times 4/7 {
                    g'4. (
                    \times 4/5 {
                        e''32 [
                        ef''32
                        d''32
                        cs''32
                        cqs''32 ]
                    }
                    a'16 )
                }
                d'8
                e'8
            }

    '''

    ### CLASS VARIABLES ###

    __slots__ = (
        '_force_fraction',
        '_is_invisible',
        '_multiplier',
        '_preferred_denominator',
        '_signifier',
        )

    _is_counttime_component = True

    ### INITIALIZER ###

    def __init__(self, multiplier, music=None, **kwargs):
        Container.__init__(self, music)
        self.multiplier = multiplier
        self._force_fraction = None
        self._is_invisible = None
        self._preferred_denominator = None
        self._signifier = '*'
        self._initialize_keyword_values(**kwargs)

    ### SPECIAL METHODS ###

    def __getnewargs__(self):
        '''Gets new arguments.

        Returns tuple.
        '''
        return (self.multiplier, )

    def __repr__(self):
        '''Interpreter representation of tuplet.

        Returns string.
        '''
        return '%s(%s, [%s])' % (
            self._class_name,
            self.multiplier,
            self._summary,
            )

    def __str__(self):
        '''String representation of tuplet.

        Returns string.
        '''
        if 0 < len(self):
            return '{%s %s %s %s}' % (
                self._signifier,
                self._ratio_string,
                self._summary,
                self._signifier,
                )
        else:
            return '{%s %s %s}' % (
                self._signifier,
                self.multiplier,
                self._signifier,
                )

    ### PRIVATE PROPERTIES ###

    @property
    def _has_power_of_two_denominator(self):
        if self.multiplier:
            return mathtools.is_nonnegative_integer_power_of_two(
                self.multiplier.numerator)
        else:
            return True

    @property
    def _multiplier_fraction_string(self):
        if self.preferred_denominator is not None:
            inverse_multiplier = durationtools.Multiplier(
                self.multiplier.denominator, self.multiplier.numerator)
            nonreduced_fraction = \
                mathtools.NonreducedFraction(inverse_multiplier)
            nonreduced_fraction = nonreduced_fraction.with_denominator(
                self.preferred_denominator)
            d, n = nonreduced_fraction.pair
        else:
            n, d = self.multiplier.numerator, self.multiplier.denominator
        return '%s/%s' % (n, d)

    @property
    def _preprolated_duration(self):
        return self.multiplied_duration

    @property
    def _ratio_string(self):
        multiplier = self.multiplier
        if multiplier is not None:
            numerator = multiplier.numerator
            denominator = multiplier.denominator
            ratio_string = '{}:{}'.format(denominator, numerator)
            return ratio_string
        else:
            return None

    @property
    def _summary(self):
        if 0 < len(self):
            return ', '.join([str(x) for x in self._music])
        else:
            return ''

    ### PRIVATE METHODS ###

    def _fix(self):
        from abjad.tools import leaftools
        from abjad.tools import tuplettools
        if not isinstance(self, tuplettools.FixedDurationTuplet):
            return
        # find tuplet multiplier
        integer_exponent = int(math.log(self.multiplier, 2))
        leaf_multiplier = fractions.Fraction(2) ** integer_exponent
        # scale leaves in tuplet by power of two
        for component in self:
            if isinstance(component, leaftools.Leaf):
                old_written_duration = component.written_duration
                new_written_duration = leaf_multiplier * old_written_duration
                leaftools.set_leaf_duration(
                    component, new_written_duration)

    def _format_after_slot(self, format_contributions):
        r'''Tuple of format contributions to appear 
        immediately after self closing.
        '''
        result = []
        result.append(('grob reverts', 
            format_contributions.get('grob reverts', [])))
        result.append(('lilypond command marks',
            format_contributions.get(
                'after', {}).get('lilypond command marks', [])))
        result.append(('comments', 
            format_contributions.get('after', {}).get('comments', [])))
        return tuple(result)

    def _format_before_slot(self, format_contributions):
        result = []
        result.append(('comments', 
            format_contributions.get('before', {}).get('comments', [])))
        result.append(('lilypond command marks',
            format_contributions.get(
                'before', {}).get('lilypond command marks', [])))
        result.append(('grob overrides', 
            format_contributions.get('grob overrides', [])))
        return tuple(result)

    def _format_close_brackets_slot(self, format_contributions):
        r'''Tuple of format contributions used to 
        generate self closing.
        '''
        result = []
        if self.multiplier:
            result.append([('self_brackets', 'close'), '}'])
        return tuple(result)

    def _format_closing_slot(self, format_contributions):
        r'''Tuple of format contributions to appear 
        immediately before self closing.
        '''
        result = []
        result.append(('lilypond command marks',
            format_contributions.get(
                'closing', {}).get('lilypond command marks', [])))
        result.append(('comments', 
            format_contributions.get('closing', {}).get('comments', [])))
        return self._format_slot_contributions_with_indent(result)

    def _format_lilypond_fraction_command_string(self):
        if not self.is_invisible:
            if self.is_augmentation or \
                (not self._has_power_of_two_denominator) or \
                self.force_fraction:
                return r"\tweak #'text #tuplet-number::calc-fraction-text"
        return ''

    def _format_open_brackets_slot(self, format_contributions):
        result = []
        if self.multiplier:
            if self.is_invisible:
                multiplier = self.multiplier
                n, d = multiplier.numerator, multiplier.denominator
                contributor = (self, 'is_invisible')
                contributions = [r"\scaleDurations #'(%s . %s) {" % (n, d)]
                result.append([contributor, contributions])
            else:
                contributor = ('self_brackets', 'open')
                if self.multiplier != 1:
                    contributions = []
                    fraction_command_string = \
                        self._format_lilypond_fraction_command_string()
                    if fraction_command_string:
                        contributions.append(fraction_command_string)
                    contributions.append(r'\times {} {{'.format(
                        self._multiplier_fraction_string
                        ))
                else:
                    contributions = ['{']
                result.append([contributor, contributions])
        return tuple(result)

    def _format_opening_slot(self, format_contributions):
        result = []
        result.append(('comments', 
            format_contributions.get('opening', {}).get('comments', [])))
        result.append(('lilypond command marks',
            format_contributions.get(
                'opening', {}).get('lilypond command marks', [])))
        return self._format_slot_contributions_with_indent(result)

    ### PUBLIC PROPERTIES ###

    @apply
    def force_fraction():
        def fget(self):
            r'''Forced fraction formatting of tuplet.

            ..  container:: example

                **Example 1.** Get forced fraction formatting of tuplet:

                ::

                    >>> tuplet = Tuplet((2, 3), "c'8 d'8 e'8")
                    >>> show(tuplet) # doctest: +SKIP

                ..  doctest::

                    >>> f(tuplet)
                    \times 2/3 {
                        c'8
                        d'8
                        e'8
                    }


                ::
                    
                    >>> tuplet.force_fraction is None
                    True

            ..  container:: example

                **Example 2.** Set forced fraction formatting of tuplet:

                ::

                    >>> tuplet.force_fraction = True
                    >>> show(tuplet) # doctest: +SKIP

                ..  doctest::

                    >>> f(tuplet)
                    \tweak #'text #tuplet-number::calc-fraction-text
                    \times 2/3 {
                        c'8
                        d'8
                        e'8
                    }

            Returns boolean or none.
            '''
            return self._force_fraction
        def fset(self, arg):
            if isinstance(arg, (bool, type(None))):
                self._force_fraction = arg
            else:
                message = 'bad type for tuplet force fraction: "%s".'
                raise TypeError(message % arg)
        return property(**locals())

    @property
    def implied_prolation(self):
        r'''Implied prolation of tuplet.

        ..  container:: example

            ::

                >>> tuplet = Tuplet((2, 3), "c'8 d'8 e'8")
                >>> show(tuplet) # doctest: +SKIP

            ::

                >>> tuplet.implied_prolation
                Multiplier(2, 3)

        Defined equal to tuplet multiplier.

        Returns multiplier.
        '''
        return self.multiplier

    @property
    def is_augmentation(self):
        r'''True when tuplet multiplier is greater than ``1``.
        Otherwise false.

        ..  container:: example

            **Example 1.** Augmented tuplet:

            ::

                >>> tuplet = Tuplet((4, 3), "c'8 d'8 e'8")
                >>> show(tuplet) # doctest: +SKIP

            ::

                >>> tuplet.is_augmentation
                True

        ..  container:: example

            **Example 2.** Diminished tuplet:

            ::

                >>> tuplet = Tuplet((2, 3), "c'4 d'4 e'4")
                >>> show(tuplet) # doctest: +SKIP

            ::

                >>> tuplet.is_augmentation
                False

        ..  container:: example

            **Example 3.** Trivial tuplet:

            ::

                >>> tuplet = Tuplet((1, 1), "c'8. d'8. e'8.")
                >>> show(tuplet) # doctest: +SKIP

            ::

                >>> tuplet.is_augmentation
                False

        Returns boolean.
        '''
        if self.multiplier:
            return 1 < self.multiplier
        else:
            return False

    @property
    def is_diminution(self):
        r'''True when tuplet multiplier is less than ``1``.
        Otherwise false.

        ..  container:: example

            **Example 1.** Augmented tuplet:

            ::

                >>> tuplet = Tuplet((4, 3), "c'8 d'8 e'8")
                >>> show(tuplet) # doctest: +SKIP

            ::

                >>> tuplet.is_diminution
                False

        ..  container:: example

            **Example 2.** Diminished tuplet:

            ::

                >>> tuplet = Tuplet((2, 3), "c'4 d'4 e'4")
                >>> show(tuplet) # doctest: +SKIP

            ::

                >>> tuplet.is_diminution
                True

        ..  container:: example

            **Example 3.** Trivial tuplet:

            ::

                >>> tuplet = Tuplet((1, 1), "c'8. d'8. e'8.")
                >>> show(tuplet) # doctest: +SKIP

            ::

                >>> tuplet.is_diminution
                False

        Returns boolean.
        '''
        if self.multiplier:
            return self.multiplier < 1
        else:
            return False

    @apply
    def is_invisible():
        def fget(self):
            r'''Invisibility status of tuplet.

            ..  container:: example

                **Example.** Get tuplet invisibility status:

                ::

                    >>> tuplet = Tuplet((2, 3), "c'8 d'8 e'8")
                    >>> show(tuplet) # doctest: +SKIP

                ..  doctest::

                    >>> f(tuplet)
                    \times 2/3 {
                        c'8
                        d'8
                        e'8
                    }

                ::

                    >>> tuplet.is_invisible is None
                    True

            ..  container:: example

                **Example 2.** Set tuplet invisibility status:

                ::

                    >>> tuplet_1 = Tuplet((2, 3), "c'4 d'4 e'4")
                    >>> tuplet_2 = Tuplet((2, 3), "d'4 e'4 f'4")
                    >>> staff = Staff([tuplet_1, tuplet_2])
                    >>> show(staff) # doctest: +SKIP

                ..  doctest::

                    >>> f(staff)
                    \new Staff {
                        \times 2/3 {
                            c'4
                            d'4
                            e'4
                        }
                        \times 2/3 {
                            d'4
                            e'4
                            f'4
                        }
                    }
    
                ::

                    >>> staff[0].is_invisible = True
                    >>> show(staff) # doctest: +SKIP

                ..  doctest::

                    >>> f(staff)
                    \new Staff {
                        \scaleDurations #'(2 . 3) {
                            c'4
                            d'4
                            e'4
                        }
                        \times 2/3 {
                            d'4
                            e'4
                            f'4
                        }
                    }

            Hides tuplet bracket and tuplet number when true.

            Preserves tuplet duration when true.

            Returns boolean or none.
            '''
            return self._is_invisible
        def fset(self, arg):
            assert isinstance(arg, (bool, type(None)))
            self._is_invisible = arg
        return property(**locals())

    @property
    def is_trivial(self):
        r'''True when tuplet multiplier is equal to ``1``.
        Otherwise false:

        ::

            >>> tuplet = Tuplet((1, 1), "c'8 d'8 e'8")
            >>> tuplet.is_trivial
            True

        Return boolean.
        '''
        return self.multiplier == 1

    @property
    def lilypond_format(self):
        '''LilyPond format of tuplet.

        ..  container:: example

            ::

                >>> tuplet = Tuplet((2, 3), "c'8 d'8 e'8")
                >>> show(tuplet) # doctest: +SKIP

            ::

                >>> print tuplet.lilypond_format
                \times 2/3 {
                    c'8
                    d'8
                    e'8
                }

        Returns string.
        '''
        self._update_now(marks=True)
        return self._format_component()

    @property
    def multiplied_duration(self):
        r'''Multiplied duration of tuplet.

        ::

            >>> tuplet = Tuplet((2, 3), "c'8 d'8 e'8")
            >>> tuplet.multiplied_duration
            Duration(1, 4)

        Returns duration.
        '''
        return self.multiplier * self._contents_duration

    @apply
    def multiplier():
        def fget(self):
            r'''Tuplet multiplier.

            ..  container:: example

                **Example 1.** Get tuplet multiplier:

                    >>> tuplet = Tuplet((2, 3), "c'8 d'8 e'8")
                    >>> show(tuplet) # doctest: +SKIP

                ::

                    >>> tuplet.multiplier
                    Multiplier(2, 3)

            ..  container:: example

                **Example 2.** Set tuplet multiplier:

                    >>> tuplet.multiplier = Multiplier(4, 3)
                    >>> show(tuplet) # doctest: +SKIP

                ..  doctest::
                
                    >>> f(tuplet)
                    \tweak #'text #tuplet-number::calc-fraction-text
                    \times 4/3 {
                        c'8
                        d'8
                        e'8
                    }

            Returns multiplier.
            '''
            return self._multiplier
        def fset(self, expr):
            if isinstance(expr, (int, long, fractions.Fraction)):
                rational = durationtools.Multiplier(expr)
            elif isinstance(expr, tuple):
                rational = durationtools.Multiplier(expr)
            else:
                message = 'can not set tuplet multiplier: {!r}.'
                raise ValueError(message.format(expr))
            if 0 < rational:
                self._multiplier = rational
            else:
                message = 'tuplet multiplier must be positive: {!r}.'
                raise ValueError(message.format(expr))
        return property(**locals())

    @apply
    def preferred_denominator():
        def fget(self):
            r'''Preferred denominator of tuplet.

            ..  container:: example

                **Example 1.** Get preferred denominator of tuplet:

                ::

                    >>> tuplet = Tuplet((2, 3), "c'8 d'8 e'8")
                    >>> show(tuplet) # doctest: +SKIP

                ..  doctest::

                    >>> f(tuplet)
                    \times 2/3 {
                        c'8
                        d'8
                        e'8
                    }

                ::

                    >>> tuplet.preferred_denominator is None
                    True

            ..  container:: example

                **Example 2.** Set preferred denominator of tuplet:

                ::

                    >>> tuplet = Tuplet((2, 3), "c'8 d'8 e'8")
                    >>> show(tuplet) # doctest: +SKIP

                ..  doctest::

                    >>> f(tuplet)
                    \times 2/3 {
                        c'8
                        d'8
                        e'8
                    }

                    >>> tuplet.preferred_denominator = 4
                    >>> show(tuplet) # doctest: +SKIP

                ..  doctest::

                    >>> f(tuplet)
                    \times 4/6 {
                        c'8
                        d'8
                        e'8
                    }

            Returns positive integer or none.
            '''
            return self._preferred_denominator
        def fset(self, arg):
            if isinstance(arg, (int, long)):
                if not 0 < arg:
                    raise ValueError(arg)
            elif not isinstance(arg, type(None)):
                raise TypeError(arg)
            self._preferred_denominator = arg
        return property(**locals())

    ### PUBLIC METHODS ###

    def extract(self, scale_contents=False):
        r'''Extracts tuplet from score.

        ..  container:: example

            **Example 1.** Extract tuplet:

            ::

                >>> staff = Staff()
                >>> time_signature = contexttools.TimeSignatureMark((3, 4))
                >>> time_signature = time_signature.attach(staff)
                >>> staff.append(Tuplet((3, 2), "c'4 e'4"))
                >>> staff.append(Tuplet((3, 2), "d'4 f'4"))
                >>> hairpin = spannertools.HairpinSpanner([], 'p < f')
                >>> hairpin.attach(staff.select_leaves())
                >>> show(staff) # doctest: +SKIP

            ..  doctest::

                >>> f(staff)
                \new Staff {
                    \time 3/4
                    \tweak #'text #tuplet-number::calc-fraction-text
                    \times 3/2 {
                        c'4 \< \p
                        e'4
                    }
                    \tweak #'text #tuplet-number::calc-fraction-text
                    \times 3/2 {
                        d'4
                        f'4 \f
                    }
                }

            ::

                >>> empty_tuplet = staff[-1].extract()
                >>> empty_tuplet = staff[0].extract()
                >>> show(staff) # doctest: +SKIP

            ..  doctest::

                >>> f(staff)
                \new Staff {
                    \time 3/4
                    c'4 \< \p
                    e'4
                    d'4
                    f'4 \f
                }

        ..  container:: example

            **Example 2.** Scale tuplet contents and then extract tuplet:

            ::

                >>> staff = Staff()
                >>> time_signature = contexttools.TimeSignatureMark((3, 4))
                >>> time_signature = time_signature.attach(staff)
                >>> staff.append(Tuplet((3, 2), "c'4 e'4"))
                >>> staff.append(Tuplet((3, 2), "d'4 f'4"))
                >>> hairpin = spannertools.HairpinSpanner([], 'p < f')
                >>> hairpin.attach(staff.select_leaves())
                >>> show(staff) # doctest: +SKIP

            ..  doctest::

                >>> f(staff)
                \new Staff {
                    \time 3/4
                    \tweak #'text #tuplet-number::calc-fraction-text
                    \times 3/2 {
                        c'4 \< \p
                        e'4
                    }
                    \tweak #'text #tuplet-number::calc-fraction-text
                    \times 3/2 {
                        d'4
                        f'4 \f
                    }
                }

            ::

                >>> empty_tuplet = staff[-1].extract(scale_contents=True)
                >>> empty_tuplet = staff[0].extract(scale_contents=True)
                >>> show(staff) # doctest: +SKIP

            ..  doctest::

                >>> f(staff)
                \new Staff {
                    \time 3/4
                    c'4. \< \p
                    e'4.
                    d'4.
                    f'4. \f
                }

        Returns empty tuplet.
        '''
        from abjad.tools import containertools
        if scale_contents:
            containertools.scale_contents_of_container(
                self, self.multiplier)
        return super(Tuplet, self).extract()

    @staticmethod
    def from_duration_and_ratio(
        duration,
        proportions,
        avoid_dots=True,
        decrease_durations_monotonically=True,
        is_diminution=True,
        ):
        r'''Makes tuplet from `duration` and `proportions`.

        ..  container:: example

            **Example 1.** Make augmented tuplet from `duration` and 
            `proportions` and avoid dots.

            Make tupletted leaves strictly without dots when all 
            `proportions` equal ``1``:

            ::

                >>> tuplet = Tuplet.from_duration_and_ratio(
                ...     Duration(3, 16), 
                ...     [1, 1, 1, -1, -1], 
                ...     avoid_dots=True,
                ...     is_diminution=False,
                ...     )
                >>> measure = Measure((3, 16), [tuplet])
                >>> show(measure) # doctest: +SKIP

            ..  doctest::
               
                >>> f(measure)
                {
                    \time 3/16
                    \tweak #'text #tuplet-number::calc-fraction-text
                    \times 6/5 {
                        c'32
                        c'32
                        c'32
                        r32
                        r32
                    }
                }

            Allow tupletted leaves to return with dots when some `proportions` 
            do not equal ``1``:

            ::

                >>> tuplet = Tuplet.from_duration_and_ratio(
                ...     Duration(3, 16), 
                ...     [1, -2, -2, 3, 3], 
                ...     avoid_dots=True,
                ...     is_diminution=False,
                ...     )
                >>> measure = Measure((3, 16), [tuplet])
                >>> show(measure) # doctest: +SKIP

            ::

                >>> f(measure)
                {
                    \time 3/16
                    \tweak #'text #tuplet-number::calc-fraction-text
                    \times 12/11 {
                        c'64
                        r32
                        r32
                        c'32.
                        c'32.
                    }
                }

            Interpret nonassignable `proportions` according to
            `decrease_durations_monotonically`:

            ::

                >>> tuplet = Tuplet.from_duration_and_ratio(
                ...     Duration(3, 16), 
                ...     [5, -1, 5], 
                ...     avoid_dots=True,
                ...     decrease_durations_monotonically=False,
                ...     is_diminution=False,
                ...     )
                >>> measure = Measure((3, 16), [tuplet])
                >>> show(measure) # doctest: +SKIP

            ..  doctest::

                >>> f(measure)
                {
                    \time 3/16
                    \tweak #'text #tuplet-number::calc-fraction-text
                    \times 12/11 {
                        c'64 ~
                        c'16
                        r64
                        c'64 ~
                        c'16
                    }
                }

        ..  container:: example

            **Example 2.** Make augmented tuplet from `duration` and 
            `proportions` and encourage dots:

            ::

                >>> tuplet = Tuplet.from_duration_and_ratio(
                ...     Duration(3, 16), 
                ...     [1, 1, 1, -1, -1], 
                ...     avoid_dots=False,
                ...     is_diminution=False,
                ...     )
                >>> measure = Measure((3, 16), [tuplet])
                >>> show(measure) # doctest: +SKIP

            ..  doctest::

                >>> f(measure)
                {
                    \time 3/16
                    \tweak #'text #tuplet-number::calc-fraction-text
                    \times 8/5 {
                        c'64.
                        c'64.
                        c'64.
                        r64.
                        r64.
                    }
                }

            Interpret nonassignable `proportions` according to
            `decrease_durations_monotonically`:

            ::

                >>> tuplet = Tuplet.from_duration_and_ratio(
                ...     Duration(3, 16), 
                ...     [5, -1, 5], 
                ...     avoid_dots=False,
                ...     decrease_durations_monotonically=False,
                ...     is_diminution=False,
                ...     )
                >>> measure = Measure((3, 16), [tuplet])
                >>> show(measure) # doctest: +SKIP

            ..  doctest::

                >>> f(measure)
                {
                    \time 3/16
                    \tweak #'text #tuplet-number::calc-fraction-text
                    \times 16/11 {
                        c'32...
                        r128.
                        c'32...
                    }
                }

        ..  container:: example

            **Example 3.** Make diminished tuplet from `duration` and nonzero 
            integer `proportions`.

            Make tupletted leaves strictly without dots when all 
            `proportions` equal ``1``:

            ::

                >>> tuplet = Tuplet.from_duration_and_ratio(
                ...     Duration(3, 16), 
                ...     [1, 1, 1, -1, -1], 
                ...     avoid_dots=True,
                ...     is_diminution=True,
                ...     )
                >>> measure = Measure((3, 16), [tuplet])
                >>> show(measure) # doctest: +SKIP

            ..  doctest::

                >>> f(measure)
                {
                    \time 3/16
                    \tweak #'text #tuplet-number::calc-fraction-text
                    \times 3/5 {
                        c'16
                        c'16
                        c'16
                        r16
                        r16
                    }
                }

            Allow tupletted leaves to return with dots when some `proportions` 
            do not equal ``1``:

            ::

                >>> tuplet = Tuplet.from_duration_and_ratio(
                ...     Duration(3, 16), 
                ...     [1, -2, -2, 3, 3], 
                ...     avoid_dots=True,
                ...     is_diminution=True,
                ...     )
                >>> measure = Measure((3, 16), [tuplet])
                >>> show(measure) # doctest: +SKIP

            ..  doctest::

                >>> f(measure)
                {
                    \time 3/16
                    \tweak #'text #tuplet-number::calc-fraction-text
                    \times 6/11 {
                        c'32
                        r16
                        r16
                        c'16.
                        c'16.
                    }
                }

            Interpret nonassignable `proportions` according to
            `decrease_durations_monotonically`:

            ::

                >>> tuplet = Tuplet.from_duration_and_ratio(
                ...     Duration(3, 16), 
                ...     [5, -1, 5], 
                ...     avoid_dots=True,
                ...     decrease_durations_monotonically=False,
                ...     is_diminution=True,
                ...     )
                >>> measure = Measure((3, 16), [tuplet])
                >>> show(measure) # doctest: +SKIP

            ..  doctest::

                >>> f(measure)
                {
                    \time 3/16
                    \tweak #'text #tuplet-number::calc-fraction-text
                    \times 6/11 {
                        c'32 ~
                        c'8
                        r32
                        c'32 ~
                        c'8
                    }
                }

        ..  container:: example
        
            **Example 4.** Make diminished tuplet from `duration` and 
            `proportions` and encourage dots:

            ::

                >>> tuplet = Tuplet.from_duration_and_ratio(
                ...     Duration(3, 16), 
                ...     [1, 1, 1, -1, -1], 
                ...     avoid_dots=False,
                ...     is_diminution=True,
                ...     )
                >>> measure = Measure((3, 16), [tuplet])
                >>> show(measure) # doctest: +SKIP

            ..  doctest::

                >>> f(measure)
                {
                    \time 3/16
                    \times 4/5 {
                        c'32.
                        c'32.
                        c'32.
                        r32.
                        r32.
                    }
                }

            Interpret nonassignable `proportions` according to `direction`:

            ::

                >>> tuplet = Tuplet.from_duration_and_ratio(
                ...     Duration(3, 16), 
                ...     [5, -1, 5], 
                ...     avoid_dots=False,
                ...     decrease_durations_monotonically=False,
                ...     is_diminution=True,
                ...     )
                >>> measure = Measure((3, 16), [tuplet])
                >>> show(measure) # doctest: +SKIP

            ..  doctest::

                >>> f(measure)
                {
                    \time 3/16
                    \times 8/11 {
                        c'16...
                        r64.
                        c'16...
                    }
                }

        Reduces `proportions` relative to each other.

        Interprets negative `proportions` as rests.

        Returns fixed-duration tuplet.
        '''
        from abjad.tools import leaftools
        from abjad.tools import notetools
        from abjad.tools import resttools
        from abjad.tools import selectiontools
        from abjad.tools import tuplettools
        # coerce duration and proportions
        duration = durationtools.Duration(duration)
        proportions = mathtools.Ratio(proportions)
        # reduce proportions relative to each other
        proportions = \
            sequencetools.divide_sequence_elements_by_greatest_common_divisor(
                proportions)
        # find basic prolated duration of note in tuplet
        basic_prolated_duration = duration / mathtools.weight(proportions)
        # find basic written duration of note in tuplet
        if avoid_dots:
            basic_written_duration = \
                basic_prolated_duration.equal_or_greater_power_of_two
        else:
            basic_written_duration = \
                basic_prolated_duration.equal_or_greater_assignable
        # find written duration of each note in tuplet
        written_durations = [x * basic_written_duration for x in proportions]
        # make tuplet leaves
        try:
            notes = [
                notetools.Note(0, x) if 0 < x else resttools.Rest(abs(x)) 
                for x in written_durations
                ]
        except AssignabilityError:
            denominator = duration._denominator
            note_durations = [durationtools.Duration(x, denominator) 
                for x in proportions]
            pitches = [None if note_duration < 0 else 0 
                for note_duration in note_durations]
            leaf_durations = [abs(note_duration) 
                for note_duration in note_durations]
            notes = leaftools.make_leaves(
                pitches,
                leaf_durations,
                decrease_durations_monotonically=decrease_durations_monotonically,
                )
        # make tuplet
        tuplet = tuplettools.FixedDurationTuplet(duration, notes)
        # fix tuplet contents if necessary
        tuplet._fix()
        # change prolation if necessary
        if not tuplet.multiplier == 1:
            if is_diminution:
                if not tuplet.is_diminution:
                    tuplet.toggle_prolation()
            else:
                if tuplet.is_diminution:
                    tuplet.toggle_prolation()
        # return tuplet
        return tuplet

    @staticmethod
    def from_ratio_and_nonreduced_fraction(proportions, (n, d)):
        r'''Makes tuplet from `proportions` and nonreduced fraction `(n, d)`.

        ..  container:: example

            **Example 1.** Make container when no prolation is necessary:

            ::

                >>> ratio = [1]
                >>> tuplet = Tuplet.from_ratio_and_nonreduced_fraction(
                ...     [1],
                ...     (7, 16),
                ...     )
                >>> measure = Measure((7, 16), [tuplet])
                >>> show(measure) # doctest: +SKIP

            ..  doctest::

                >>> f(measure)
                {
                    \time 7/16
                    {
                        c'4..
                    }
                }

        ..  container:: example

            **Example 2.** Make fixed-duration tuplet when 
            prolation is necessary:

            ::

                >>> tuplet = Tuplet.from_ratio_and_nonreduced_fraction(
                ...     [1, 2],
                ...     (7, 16),
                ...     )
                >>> measure = Measure((7, 16), [tuplet])
                >>> show(measure) # doctest: +SKIP

            ..  doctest::

                >>> f(measure)
                {
                    \time 7/16
                    \tweak #'text #tuplet-number::calc-fraction-text
                    \times 7/6 {
                        c'8
                        c'4
                    }
                }

            ::

                >>> ratio = [1, 2, 4]
                >>> tuplet = Tuplet.from_ratio_and_nonreduced_fraction(
                ...     [1, 2, 4],
                ...     (7, 16),
                ...     )
                >>> measure = Measure((7, 16), [tuplet])
                >>> show(measure) # doctest: +SKIP

            ..  doctest::

                >>> f(measure)
                {
                    \time 7/16
                    {
                        c'16
                        c'8
                        c'4
                    }
                }

            ::

                >>> ratio = [1, 2, 4, 1]
                >>> tuplet = Tuplet.from_ratio_and_nonreduced_fraction(
                ...     [1, 2, 4, 1],
                ...     (7, 16),
                ...     )
                >>> measure = Measure((7, 16), [tuplet])
                >>> show(measure) # doctest: +SKIP

            ..  doctest::

                >>> f(measure)
                {
                    \time 7/16
                    \tweak #'text #tuplet-number::calc-fraction-text
                    \times 7/8 {
                        c'16
                        c'8
                        c'4
                        c'16
                    }
                }

            ::

                >>> ratio = [1, 2, 4, 1, 2]
                >>> tuplet = Tuplet.from_ratio_and_nonreduced_fraction(
                ...     [1, 2, 4, 1, 2],
                ...     (7, 16),
                ...     )
                >>> measure = Measure((7, 16), [tuplet])
                >>> show(measure) # doctest: +SKIP

            ..  doctest::

                >>> f(measure)
                {
                    \time 7/16
                    \tweak #'text #tuplet-number::calc-fraction-text
                    \times 7/10 {
                        c'16
                        c'8
                        c'4
                        c'16
                        c'8
                    }
                }

            ::

                >>> ratio = [1, 2, 4, 1, 2, 4]
                >>> tuplet = Tuplet.from_ratio_and_nonreduced_fraction(
                ...     [1, 2, 4, 1, 2, 4],
                ...     (7, 16),
                ...     )
                >>> measure = Measure((7, 16), [tuplet])
                >>> show(measure) # doctest: +SKIP

            ..  doctest::

                >>> f(measure)
                {
                    \time 7/16
                    \times 1/2 {
                        c'16
                        c'8
                        c'4
                        c'16
                        c'8
                        c'4
                    }
                }

        Interprets `d` as tuplet denominator.

        Returns tuplet or container.
        '''
        from abjad.tools import containertools
        from abjad.tools import notetools
        from abjad.tools import resttools
        from abjad.tools import tuplettools
        proportions = mathtools.NonreducedRatio(proportions)
        duration = durationtools.Duration(n, d)
        if len(proportions) == 1:
            if 0 < proportions[0]:
                try:
                    note = notetools.Note(0, duration)
                    return containertools.Container([note])
                except AssignabilityError:
                    notes = notetools.make_notes(0, duration)
                    return containertools.Container(notes)
            elif proportions[0] < 0:
                try:
                    rest = resttools.Rest(duration)
                    return containertools.Container([rest])
                except AssignabilityError:
                    rests = resttools.make_rests(duration)
                    return containertools.Container(rests)
            else:
                raise ValueError('no divide zero values.')
        if 1 < len(proportions):
            exponent = int(
                math.log(mathtools.weight(proportions), 2) - math.log(n, 2))
            denominator = int(d * 2 ** exponent)
            music = []
            for x in proportions:
                if not x:
                    raise ValueError('no divide zero values.')
                if 0 < x:
                    try:
                        note = notetools.Note(0, (x, denominator))
                        music.append(note)
                    except AssignabilityError:
                        notes = notetools.make_notes(0, (x, denominator))
                        music.extend(notes)
                else:
                    rests = resttools.Rest((-x, denominator))
                    music.append(rests)
            return tuplettools.FixedDurationTuplet(duration, music)

    def to_fixed_duration_tuplet(self):
        r'''Change tuplet to fixed-duration tuplet.

        ..  container:: example
        
            **Example:**

            ::

                >>> tuplet = Tuplet((2, 3), "c'8 d'8 e'8")
                >>> show(tuplet) # doctest: +SKIP

            ::

                >>> tuplet
                Tuplet(2/3, [c'8, d'8, e'8])

            ::

                >>> new_tuplet = tuplet.to_fixed_duration_tuplet()
                >>> show(new_tuplet) # doctest: +SKIP

            ::
                
                >>> new_tuplet
                FixedDurationTuplet(1/4, [c'8, d'8, e'8])

        Returns new tuplet.
        '''
        from abjad.tools import containertools
        from abjad.tools import tuplettools
        target_duration = self._preprolated_duration
        new_tuplet = tuplettools.FixedDurationTuplet(target_duration, [])
        containertools.move_parentage_children_and_spanners_from_components_to_empty_container(
            [self], new_tuplet)
        return new_tuplet

    def toggle_prolation(self):
        '''Changes augmented tuplets to diminished;
        changes diminished tuplets to augmented.

        ..  container:: example
        
            **Example 1.** Change augmented tuplet to diminished:

            ::

                >>> tuplet = Tuplet((4, 3), "c'8 d'8 e'8")
                >>> show(tuplet) # doctest: +SKIP

            ..  doctest::

                >>> f(tuplet)
                \tweak #'text #tuplet-number::calc-fraction-text
                \times 4/3 {
                    c'8
                    d'8
                    e'8
                }

            ::

                >>> tuplet.toggle_prolation()
                >>> show(tuplet) # doctest: +SKIP

            ..  doctest::

                >>> f(tuplet)
                \times 2/3 {
                    c'4
                    d'4
                    e'4
                }

            Multiplies the written duration of the leaves in tuplet
            by the least power of ``2`` necessary to diminshed tuplet.

        ..  container:: example

            **Example 2.** Change diminished tuplet to augmented:

            ::

                >>> tuplet = Tuplet((2, 3), "c'4 d'4 e'4")
                >>> show(tuplet) # doctest: +SKIP

            ..  doctest::

                >>> f(tuplet)
                \times 2/3 {
                    c'4
                    d'4
                    e'4
                }

            ::

                >>> tuplet.toggle_prolation()
                >>> show(tuplet) # doctest: +SKIP

            ..  doctest::

                >>> f(tuplet)
                \tweak #'text #tuplet-number::calc-fraction-text
                \times 4/3 {
                    c'8
                    d'8
                    e'8
                }

            Divides the written duration of the leaves in tuplet
            by the least power of ``2`` necessary to diminshed tuplet.

        Does not yet work with nested tuplets.

        Returns none.
        '''
        if self.is_diminution:
            while self.is_diminution:
                self.multiplier *= 2
                for leaf in self.select_leaves():
                    leaf.written_duration /= 2
        elif not self.is_diminution:
            while not self.is_diminution:
                self.multiplier /= 2
                for leaf in self.select_leaves():
                    leaf.written_duration *= 2
