# -*- encoding: utf-8 -*-
from abjad.tools import datastructuretools
from abjad.tools import durationtools
from abjad.tools.abctools import AbjadValueObject


class MetricAccentKernel(AbjadValueObject):
    r'''A metric accent kernel.

    ..  container:: example

        ::

            >>> hierarchy = metertools.Meter((7, 8))
            >>> kernel = hierarchy.generate_offset_kernel_to_denominator(8)
            >>> kernel
            MetricAccentKernel(
                {
                    Offset(0, 1): Multiplier(3, 14),
                    Offset(1, 8): Multiplier(1, 14),
                    Offset(1, 4): Multiplier(1, 14),
                    Offset(3, 8): Multiplier(1, 7),
                    Offset(1, 2): Multiplier(1, 14),
                    Offset(5, 8): Multiplier(1, 7),
                    Offset(3, 4): Multiplier(1, 14),
                    Offset(7, 8): Multiplier(3, 14),
                    }
                )

    Call the kernel against an expression from which offsets can be counted
    to receive an impulse-response:

    ..  container:: example

        ::

            >>> offsets = [(0, 8), (1, 8), (1, 8), (3, 8)]
            >>> kernel(offsets)
            0.5

    '''

    ### CLASS VARIABLES ###

    __slots__ = (
        '_kernel',
        '_offsets',
        )

    ### INITIALIZER ###

    def __init__(self, kernel=None):
        kernel = kernel or {}
        assert isinstance(kernel, dict)
        #assert 1 < len(kernel)
        for key, value in kernel.items():
            assert isinstance(key, durationtools.Offset)
            assert isinstance(value, durationtools.Multiplier)
        self._kernel = kernel.copy()
        self._offsets = tuple(sorted(self._kernel))

    ### SPECIAL METHODS ###

    def __call__(self, expr):
        r'''Calls metrical accent kernal on `expr`.

        Returns float.
        '''
        offset_count = self.count_offsets_in_expr(expr)
        response = 0.
        for offset, count in offset_count.items():
            if offset in self._kernel:
                response += (self._kernel[offset] * count)
        return float(response)

    def __eq__(self, expr):
        r'''Is true when `expr` is a metrical accent kernal with a kernal equal
        to that of this metrical accent kernel. Otherwise false.

        Returns boolean.
        '''
        if type(self) == type(expr):
            if self._kernel == expr._kernel:
                return True
        return False

    def __hash__(self):
        r'''Hashes metric accent kernel.

        Required to be explicitely re-defined on Python 3 if __eq__ changes.

        Returns integer.
        '''
        return super(MetricAccentKernel, self).__hash__()

    ### PRIVATE PROPERTIES ###

    @property
    def _repr_specification(self):
        return self._storage_format_specification

    @property
    def _storage_format_specification(self):
        from abjad.tools import systemtools
        positional_argument_values = (
            self.kernel,
            )
        return systemtools.StorageFormatSpecification(
            self,
            keyword_argument_names=(),
            positional_argument_values=positional_argument_values,
            )

    ### PUBLIC METHODS ###

    @staticmethod
    def count_offsets_in_expr(expr):
        r'''Count offsets in `expr`.

        ..  container:: example

            **Example 1:**

            ::

                >>> score = Score()
                >>> score.append(Staff("c'4. d'8 e'2"))
                >>> score.append(Staff(r'\clef bass c4 b,4 a,2'))

            ..  doctest::

                >>> print(format(score))
                \new Score <<
                    \new Staff {
                        c'4.
                        d'8
                        e'2
                    }
                    \new Staff {
                        \clef "bass"
                        c4
                        b,4
                        a,2
                    }
                >>

            ::

                >>> show(score) # doctest: +SKIP

            ::

                >>> MetricAccentKernel = metertools.MetricAccentKernel
                >>> leaves = score.select_leaves(
                ...     allow_discontiguous_leaves=True)
                >>> counter = MetricAccentKernel.count_offsets_in_expr(leaves)
                >>> for offset, count in sorted(counter.items()):
                ...     offset, count
                ...
                (Offset(0, 1), 2)
                (Offset(1, 4), 2)
                (Offset(3, 8), 2)
                (Offset(1, 2), 4)
                (Offset(1, 1), 2)

        ..  container:: example

            **Example 2:**

            ::

                >>> a = timespantools.Timespan(0, 10)
                >>> b = timespantools.Timespan(5, 15)
                >>> c = timespantools.Timespan(15, 20)

            ::

                >>> counter = MetricAccentKernel.count_offsets_in_expr((a, b, c))
                >>> for offset, count in sorted(counter.items()):
                ...     offset, count
                ...
                (Offset(0, 1), 1)
                (Offset(5, 1), 1)
                (Offset(10, 1), 1)
                (Offset(15, 1), 2)
                (Offset(20, 1), 1)

        Returns counter.
        '''
        if isinstance(expr, datastructuretools.TypedCounter):
            if expr.item_class is durationtools.Offset:
                return expr
        counter = datastructuretools.TypedCounter(
            item_class=durationtools.Offset,
            )
        for x in expr:
            if hasattr(x, 'start_offset') and hasattr(x, 'stop_offset'):
                counter[x.start_offset] += 1
                counter[x.stop_offset] += 1
            elif hasattr(x, '_get_timespan'):
                counter[x._get_timespan().start_offset] += 1
                counter[x._get_timespan().stop_offset] += 1
            else:
                offset = durationtools.Offset(x)
                counter[offset] += 1
        return counter

    ### PUBLIC PROPERTIES ###

    @property
    def duration(self):
        r'''Gets duration.
        '''
        return durationtools.Duration(self._offsets[-1])

    @property
    def kernel(self):
        r'''The kernel datastructure.

        Returns dict.
        '''
        return self._kernel.copy()
