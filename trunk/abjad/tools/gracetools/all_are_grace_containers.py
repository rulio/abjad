from abjad.tools.componenttools.all_are_components import all_are_components
from abjad.tools.gracetools.GraceContainer import GraceContainer


def all_are_grace_containers(expr):
    r'''.. versionadded:: 2.6

    True when `expr` is a sequence of Abjad grace containers::

        >>> graces = [gracetools.GraceContainer("<c' e' g'>4"), gracetools.GraceContainer("<c' f' a'>4")]
        >>> voice = Voice("c'8 d'8 e'8 f'8")
        >>> grace_notes = [Note("c'16"), Note("d'16")]
        >>> grace_container = gracetools.GraceContainer(grace_notes, kind='grace')
        >>> grace_container(voice[1])
        Note("d'8")

    ::

        >>> f(voice)
        \new Voice {
            c'8
            \grace {
                c'16
                d'16
            }
            d'8
            e'8
            f'8
        }

    ::

        >>> gracetools.all_are_grace_containers([grace_container])
        True

    True when `expr` is an empty sequence::

        >>> gracetools.all_are_grace_containers([])
        True

    Otherwise false::

        >>> gracetools.all_are_grace_containers('foo')
        False

    Return boolean.

    Function wraps ``componenttools.all_are_components()``.
    '''

    return all_are_components(expr, klasses=(GraceContainer,))
