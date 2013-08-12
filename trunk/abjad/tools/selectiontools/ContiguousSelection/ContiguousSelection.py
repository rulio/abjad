# -*- encoding: utf-8 -*-
import itertools
import types
from abjad.tools.selectiontools.Selection import Selection


class ContiguousSelection(Selection):
    r'''A time-contiguous selection of components.
    '''

    ### INITIALIZER ###

    def __init__(self, music=None):
        if music is None:
            music = ()
        elif isinstance(music, (tuple, list)):
            music = tuple(music)
        elif isinstance(music, Selection):
            music = tuple(music)
        elif isinstance(music, types.GeneratorType):
            music = tuple(music)
        else:
            music = (music, )
        self._music = tuple(music)

    ### SPECIAL METHODS ###

    def __add__(self, expr):
        '''Add `expr` to slice selection.

        Return new slice selection.
        '''
        assert isinstance(expr, (type(self), list, tuple))
        if isinstance(expr, type(self)):
            music = self._music + expr._music
            return type(self)(music)
        # eventually remove this permissive branch 
        # and force the use of selections only
        elif isinstance(expr, (tuple, list)):
            music = self._music + tuple(expr)
        return type(self)(music)

    def __radd__(self, expr):
        '''Add slice selection to `expr`.

        Return new slice selection.
        '''
        assert isinstance(expr, (type(self), list, tuple))
        if isinstance(expr, type(self)):
            music = expr._music + self._music
            return type(self)(music)
        # eventually remove this permissive branch 
        # and force the use of selections only
        elif isinstance(expr, (tuple, list)):
            music = tuple(expr) + self._music
        return ContiguousSelection(music)

    ### PRIVATE PROPERTIES ###

    @property
    def _preprolated_duration(self):
        return sum(component._preprolated_duration for component in self)

    ### PRIVATE METHODS ###

    def _get_offset_lists(self):
        start_offsets, stop_offsets = [], []
        for component in self:
            start_offsets.append(component._get_timespan().start_offset)
            stop_offsets.append(component._get_timespan().stop_offset)
        return start_offsets, stop_offsets

    def _give_dominant_spanners_to_components(self, recipients):
        r'''Find all spanners dominating music.
        Insert each component in recipients into each dominant spanner.
        Remove music from each dominating spanner.
        Return none.
        Not composer-safe.
        '''
        from abjad.tools import componenttools
        from abjad.tools import spannertools
        assert componenttools.all_are_thread_contiguous_components(self)
        assert componenttools.all_are_thread_contiguous_components(recipients)
        receipt = spannertools.get_spanners_that_dominate_components(self)
        for spanner, index in receipt:
            for recipient in reversed(recipients):
                spanner._insert(index, recipient)
            for component in self:
                spanner._remove(component)

    def _set_parents(self, new_parent):
        r'''Not composer-safe.
        '''
        for component in self._music:
            component._set_parent(new_parent)

    def _withdraw_from_crossing_spanners(self):
        r'''Not composer-safe.
        '''
        from abjad.tools import componenttools
        from abjad.tools import iterationtools
        from abjad.tools import spannertools
        assert componenttools.all_are_thread_contiguous_components(self)
        crossing_spanners = \
            spannertools.get_spanners_that_cross_components(self)
        components_including_children = \
            list(iterationtools.iterate_components_in_expr(self))
        for crossing_spanner in list(crossing_spanners):
            spanner_components = crossing_spanner._components[:]
            for component in components_including_children:
                if component in spanner_components:
                    crossing_spanner._components.remove(component)
                    component._spanners.discard(crossing_spanner)

    ### PUBLIC METHODS ###

    def copy_and_detach_spanners(self, n=1):
        r'''Copies components in selection and removes spanners.

        Selection must be thread-contiguous.

        The steps taken by this function are as follows:

        * Withdraws components in selection from spanners.

        * Deep copies unspanned components in selection.

        * Reapplies spanners to components in selection.

        * Returns copied components.

        ..  container:: example
        
            **Example 1.** Copy selection one time:

            ::

                >>> voice = Voice("abj: | 2/4 c'4 ( d' || 2/4 e' f' ) |")
                >>> show(voice) # doctest: +SKIP

            ..  doctest::

                >>> f(voice)
                \new Voice {
                    {
                        \time 2/4
                        c'4 (
                        d'4
                    }
                    {
                        e'4
                        f'4 )
                    }
                }

            ::

                >>> selection = voice.select_leaves()[1:3]
                >>> result = selection.copy_and_detach_spanners()
                >>> new_voice = Voice(result)
                >>> show(new_voice) # doctest: +SKIP

            ..  doctest::

                >>> f(new_voice)
                \new Voice {
                    d'4
                    e'4
                }

            ::

                >>> new_voice[0] is voice[0]
                False

        ..  container:: example

            **Example 2.** Copy selection multiple times:

            ::

                >>> selection = voice.select_leaves()[1:3]
                >>> new_selection = selection.copy_and_detach_spanners(n=2)
                >>> new_voice = Voice(new_selection)
                >>> show(new_voice) # doctest: +SKIP

            ..  doctest::

                >>> f(new_voice)
                \new Voice {
                    d'4
                    e'4
                    d'4
                    e'4
                }

        Returns contiguous selection.
        '''

#        from abjad.tools import selectiontools
#        assert self._all_are_thread_contiguous_components()
#        if n < 1:
#            return type(self)()
#        result = []
#        for component in self:
#            new = \
#                component._copy_with_children_and_marks_but_without_spanners()
#            result.append(new)
#        for i in range(n - 1):
#            result += self.copy_and_detach_spanners()
#        result = type(self)(result)
#        return result

        # TODO: use the following wrapper instead of the implementation above
        from abjad.tools import componenttools
        from abjad.tools import spannertools
        result = componenttools.copy_components_and_fracture_crossing_spanners(
            self, n=n)
        spannertools.detach_spanners_attached_to_components_in_expr(result)
        result = type(self)(result)
        return result
        
    def get_duration(self, in_seconds=False):
        r'''Gets duration of contiguous selection.

        Returns duration.
        '''
        return sum(
            component._get_duration(in_seconds=in_seconds) 
            for component in self
            )

    def get_timespan(self, in_seconds=False):
        r'''Gets timespan of contiguous selection.

        Returns timespan.
        '''
        from abjad.tools import timespantools
        if in_seconds:
            raise NotImplementedError
        start_offset = min(x._get_timespan().start_offset for x in self)
        stop_offset = max(x._get_timespan().stop_offset for x in self)
        return timespantools.Timespan(start_offset, stop_offset)

    def group_by(self, predicate):
        '''Groups components in contiguous selection by `predicate`.

        Returns list of tuples.
        '''
        result = []
        grouper = itertools.groupby(self, predicate)
        for label, generator in grouper:
            selection = tuple(generator)
            result.append(selection)
        return result
