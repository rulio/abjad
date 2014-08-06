# -*- encoding: utf-8 -*-
from abjad.tools import indicatortools
from abjad.tools import mathtools
from abjad.tools import sequencetools
from abjad.tools.abctools.AbjadValueObject import AbjadValueObject


class MeasurewiseDivisionMaker(AbjadValueObject):
    r'''Measurewise division-maker.

    ..  container:: example

        ::

            >>> divisions = newmusicmakertools.DivisionMaker(
            ...     pattern=[(1, 4)],
            ...     )
            >>> hypermeasures = newmusicmakertools.HypermeasureSpecifier(
            ...     counts=[2],
            ...     cyclic=True,
            ...     )
            >>> maker = newmusicmakertools.MeasurewiseDivisionMaker(
            ...     division_maker=divisions,
            ...     hypermeasure_specifier=hypermeasures,
            ...     )

        ::

            >>> print(format(maker, 'storage'))
            newmusicmakertools.MeasurewiseDivisionMaker(
                division_maker=newmusicmakertools.DivisionMaker(
                    cyclic=True,
                    pattern=(
                        mathtools.NonreducedFraction(1, 4),
                        ),
                    remainder=Right,
                    ),
                hypermeasure_specifier=newmusicmakertools.HypermeasureSpecifier(
                    counts=(2,),
                    cyclic=True,
                    ),
                )

    Object model of a partially evaluated function that accepts measures (or
    time signatures) as input and returns nonreduced fractions as output.

    Follows the two-step configure-once / call-repeatly pattern established
    in the rhythm-makers.
    '''

    ### CLASS VARIABLES ###

    __slots__ = (
        '_division_maker',
        '_hypermeasure_specifier',
        )

    ### INITIALIZER ###

    def __init__(
        self,
        division_maker=None,
        hypermeasure_specifier=None,
        ):
        self._division_maker = division_maker
        self._hypermeasure_specifier = hypermeasure_specifier

    ### SPECIAL METHODS ###

    def __call__(self, measures=None):
        r'''Calls measurewise division-maker.

        ..  container:: example

            **Example 1.** Maker glues measures together two at a time. Maker
            fills resulting hypermeasures with ``1/4`` divisions. Maker
            positions remainders to the right of each hypermeasure:
            
            ::

                >>> divisions = newmusicmakertools.DivisionMaker(
                ...     pattern=[(1, 4)],
                ...     remainder=Right,
                ...     )
                >>> hypermeasures = newmusicmakertools.HypermeasureSpecifier(
                ...     counts=[2],
                ...     cyclic=True,
                ...     )
                >>> maker = newmusicmakertools.MeasurewiseDivisionMaker(
                ...     division_maker=divisions,
                ...     hypermeasure_specifier=hypermeasures,
                ...     )

            Example output:

            ::

                >>> measures = [(2, 8), (3, 8), (2, 8), (3, 8)]
                >>> lists = maker(measures)
                >>> for list_ in lists:
                ...     list_
                [NonreducedFraction(1, 4), NonreducedFraction(1, 4), NonreducedFraction(1, 8)]
                [NonreducedFraction(1, 4), NonreducedFraction(1, 4), NonreducedFraction(1, 8)]

            ::

                >>> measures = [(2, 8), (3, 8), (2, 8)]
                >>> lists = maker(measures)
                >>> for list_ in lists:
                ...     list_
                [NonreducedFraction(1, 4), NonreducedFraction(1, 4), NonreducedFraction(1, 8)]
                [NonreducedFraction(1, 4)]

            ::

                >>> measures = [(2, 8), (3, 8)]
                >>> lists = maker(measures)
                >>> for list_ in lists:
                ...     list_
                [NonreducedFraction(1, 4), NonreducedFraction(1, 4), NonreducedFraction(1, 8)]

            ::

                >>> measures = [(2, 8)]
                >>> lists = maker(measures)
                >>> for list_ in lists:
                ...     list_
                [NonreducedFraction(1, 4)]

            ::

                >>> measures = []
                >>> lists = maker(measures)
                >>> for list_ in lists:
                ...     list_

        ..  container:: example

            **Example 2.** As above but with remainders at left of each
            hypermeasure:

            ::

                >>> divisions = newmusicmakertools.DivisionMaker(
                ...     pattern=[(1, 4)],
                ...     remainder=Left,
                ...     )
                >>> hypermeasures = newmusicmakertools.HypermeasureSpecifier(
                ...     counts=[2],
                ...     cyclic=True,
                ...     )
                >>> maker = newmusicmakertools.MeasurewiseDivisionMaker(
                ...     division_maker=divisions,
                ...     hypermeasure_specifier=hypermeasures,
                ...     )

            Example output:

            ::

                >>> measures = [(2, 8), (3, 8), (2, 8), (3, 8)]
                >>> lists = maker(measures)
                >>> for list_ in lists:
                ...     list_
                [NonreducedFraction(1, 8), NonreducedFraction(1, 4), NonreducedFraction(1, 4)]
                [NonreducedFraction(1, 8), NonreducedFraction(1, 4), NonreducedFraction(1, 4)]


            ::

                >>> measures = [(2, 8), (3, 8), (2, 8)]
                >>> lists = maker(measures)
                >>> for list_ in lists:
                ...     list_
                [NonreducedFraction(1, 8), NonreducedFraction(1, 4), NonreducedFraction(1, 4)]
                [NonreducedFraction(1, 4)]

            ::

                >>> measures = [(2, 8), (3, 8)]
                >>> lists = maker(measures)
                >>> for list_ in lists:
                ...     list_
                [NonreducedFraction(1, 8), NonreducedFraction(1, 4), NonreducedFraction(1, 4)]

            ::

                >>> measures = [(2, 8)]
                >>> lists = maker(measures)
                >>> for list_ in lists:
                ...     list_
                [NonreducedFraction(1, 4)]

            ::

                >>> measures = []
                >>> lists = maker(measures)
                >>> for list_ in lists:
                ...     list_

        ..  container:: example

            **Example 3.** Similiar to the two makers above in that the maker
            here glues measures together two at a time. But the maker then
            fills resulting hypermeasures with ``2/8`` divisions instead of
            ``1/4`` divisions. Remainders at right of each hypermeasure.

            ::

                >>> divisions = newmusicmakertools.DivisionMaker(
                ...     pattern=[(2, 8)],
                ...     remainder=Right,
                ...     )
                >>> hypermeasures = newmusicmakertools.HypermeasureSpecifier(
                ...     counts=[2],
                ...     cyclic=True,
                ...     )
                >>> maker = newmusicmakertools.MeasurewiseDivisionMaker(
                ...     division_maker=divisions,
                ...     hypermeasure_specifier=hypermeasures,
                ...     )

            Example output:

            ::

                >>> measures = [(3, 8), (3, 8), (3, 8)]
                >>> lists = maker(measures)
                >>> for list_ in lists:
                ...     list_
                [NonreducedFraction(2, 8), NonreducedFraction(2, 8), NonreducedFraction(2, 8)]
                [NonreducedFraction(2, 8), NonreducedFraction(1, 8)]

            ::

                >>> measures = [(3, 8), (3, 8)]
                >>> lists = maker(measures)
                >>> for list_ in lists:
                ...     list_
                [NonreducedFraction(2, 8), NonreducedFraction(2, 8), NonreducedFraction(2, 8)]

            ::

                >>> measures = [(3, 8)]
                >>> lists = maker(measures)
                >>> for list_ in lists:
                ...     list_
                [NonreducedFraction(2, 8), NonreducedFraction(1, 8)]

            ::

                >>> measures = []
                >>> lists = maker(measures)
                >>> for list_ in lists:
                ...     list_

        ..  container:: example

            **Example 4.** As above but with remainders at left of each
            hypermeasure.

            ::

                >>> divisions = newmusicmakertools.DivisionMaker(
                ...     pattern=[(2, 8)],
                ...     remainder=Left,
                ...     )
                >>> hypermeasures = newmusicmakertools.HypermeasureSpecifier(
                ...     counts=[2],
                ...     cyclic=True,
                ...     )
                >>> maker = newmusicmakertools.MeasurewiseDivisionMaker(
                ...     division_maker=divisions,
                ...     hypermeasure_specifier=hypermeasures,
                ...     )

            Example output:

            ::

                >>> measures = [(3, 8), (3, 8), (3, 8)]
                >>> lists = maker(measures)
                >>> for list_ in lists:
                ...     list_
                [NonreducedFraction(2, 8), NonreducedFraction(2, 8), NonreducedFraction(2, 8)]
                [NonreducedFraction(1, 8), NonreducedFraction(2, 8)]

            ::

                >>> measures = [(3, 8), (3, 8)]
                >>> lists = maker(measures)
                >>> for list_ in lists:
                ...     list_
                [NonreducedFraction(2, 8), NonreducedFraction(2, 8), NonreducedFraction(2, 8)]

            ::

                >>> measures = [(3, 8)]
                >>> lists = maker(measures)
                >>> for list_ in lists:
                ...     list_
                [NonreducedFraction(1, 8), NonreducedFraction(2, 8)]

            ::

                >>> measures = []
                >>> lists = maker(measures)
                >>> for list_ in lists:
                ...     list_

        Returns nested list of nonreduced fractions.
        Output structured one list per hypermeasure.
        '''
        measures = measures or ()
        nonreduced_fractions = self._measures_to_nonreduced_fractions(
            measures)
        if self.hypermeasure_specifier is not None:
            parts = sequencetools.partition_sequence_by_counts(
                nonreduced_fractions,
                self.hypermeasure_specifier.counts,
                cyclic=self.hypermeasure_specifier.cyclic,
                overhang=True,
                )
            nonreduced_fractions = [sum(_) for _ in parts]
        division_lists = []
        for nonreduced_fraction in nonreduced_fractions:
            division_list = self.division_maker(nonreduced_fraction)
            division_lists.append(division_list)
        return division_lists

    ### PRIVATE METHODS ###

    def _measures_to_nonreduced_fractions(self, measures):
        nonreduced_fractions = []
        for measure in measures:
            if hasattr(measure, 'time_signature'):
                nonreduced_fraction = mathtools.NonreducedFraction(
                    measure.time_signature.pair
                    )
            else:
                nonreduced_fraction = mathtools.NonreducedFraction(measure)
            nonreduced_fractions.append(nonreduced_fraction)
        return nonreduced_fractions

    ### PUBLIC PROPERTIES ###

    @property
    def division_maker(self):
        r'''Gets division-maker bundled in measurewise division-maker.

        Returns division-maker.
        '''
        return self._division_maker

    @property
    def hypermeasure_specifier(self):
        r'''Gets hypermeasure specifier bundled in measurewise division-maker.

        Returns hypermeasure specifier or none.
        '''
        return self._hypermeasure_specifier