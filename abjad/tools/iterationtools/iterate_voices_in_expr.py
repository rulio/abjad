# -*- encoding: utf-8 -*-
from abjad.tools import scoretools


def iterate_voices_in_expr(expr, reverse=False, start=0, stop=None):
    r'''Iterate voices forward in `expr`:

    ::

        >>> voice_1 = Voice("c'8 d'8 e'8 f'8")
        >>> voice_2 = Voice("c'4 b4")
        >>> staff = Staff([voice_1, voice_2])
        >>> staff.is_simultaneous = True

    ..  doctest::

        >>> f(staff)
        \new Staff <<
            \new Voice {
                c'8
                d'8
                e'8
                f'8
            }
            \new Voice {
                c'4
                b4
            }
        >>

    ::

        >>> for voice in iterationtools.iterate_voices_in_expr(staff):
        ...     voice
        Voice{4}
        Voice{2}

    Iterate voices backward in `expr`:

    ::

    ::

        >>> for voice in iterationtools.iterate_voices_in_expr(
        ...     staff, reverse=True):
        ...     voice
        Voice{2}
        Voice{4}

    Returns generator.
    '''
    from abjad.tools import iterationtools

    return iterationtools.iterate_components_in_expr(
        expr,
        component_class=scoretools.Voice,
        reverse=reverse,
        start=start,
        stop=stop,
        )