import numbers
from abjad.tools import durationtools
from abjad.tools import sequencetools


def expr_to_timespan(expr):
    r'''.. versionadded:: 1.0

    Return `expr` unchanged when `expr` is timespan.

    Return ``expr.timespan`` when `expr` has timespan.

    Return timespan constant when `expr` has start- and stop-offsets::

        >>> staff = Staff("c'8 [ d'8 e'8 f'8 ]")

    ::

        >>> f(staff)
        \new Staff {
            c'8 [
            d'8
            e'8
            f'8 ]
        }

    ::

        >>> timetools.expr_to_timespan(staff[1])
        LiteralTimespan(start_offset=Offset(1, 8), stop_offset=Offset(1, 4))

    Return timespan constant when `expr` is a number::

        >>> timetools.expr_to_timespan(Fraction(7, 8))
        LiteralTimespan(start_offset=Offset(7, 8), stop_offset=Offset(7, 8))

    Return timespan constant when `expr` is an offset::

        >>> timetools.expr_to_timespan(durationtools.Offset(7, 8))
        LiteralTimespan(start_offset=Offset(7, 8), stop_offset=Offset(7, 8))

    Return timespan constant when `expr` is a pair::

        >>> timetools.expr_to_timespan(((1, 2), (3, 2)))
        LiteralTimespan(start_offset=Offset(1, 2), stop_offset=Offset(3, 2))

    Otherwise raise type error.
    '''
    from experimental import timetools

    if isinstance(expr, timetools.SymbolicTimespan):
        return expr
    if hasattr(expr, 'timespan'):
        return expr.timespan
    elif hasattr(expr, 'start_offset') and hasattr(expr, 'stop_offset'):
        return timetools.LiteralTimespan(start_offset=expr.start_offset, stop_offset=expr.stop_offset)
    elif isinstance(expr, numbers.Number):
        return timetools.LiteralTimespan(start_offset=expr, stop_offset=expr)
    elif sequencetools.is_pair(expr):
        start_offset, stop_offset = expr
        return timetools.LiteralTimespan(start_offset=start_offset, stop_offset=stop_offset)
    else:
        raise TypeError('can not change {!r} to timespan.'.format(expr))
