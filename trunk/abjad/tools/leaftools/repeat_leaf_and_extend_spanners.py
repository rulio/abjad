from abjad.tools.leaftools.Leaf import Leaf
from abjad.tools import componenttools


def repeat_leaf_and_extend_spanners(leaf, total = 1):
    r'''.. versionadded:: 1.1

    Repeat `leaf` and extend spanners::

        >>> staff = Staff("c'8 d'8 e'8 f'8")
        >>> beamtools.BeamSpanner(staff.leaves)
        BeamSpanner(c'8, d'8, e'8, f'8)
        >>> f(staff)
        \new Staff {
            c'8 [
            d'8
            e'8
            f'8 ]
        }

    ::

        >>> leaftools.repeat_leaf_and_extend_spanners(staff[0], total = 3)

    ::

        >>> f(staff)
        \new Staff {
            c'8 [
            c'8
            c'8
            d'8
            e'8
            f'8 ]
        }

    Preserve `leaf` written duration.

    Preserve parentage and spanners.

    Return none.

    .. versionchanged:: 2.0
        renamed ``leaftools.clone_and_splice_leaf()`` to
        ``leaftools.repeat_leaf_and_extend_spanners()``.
    '''

    componenttools.extend_in_parent_of_component_and_grow_spanners(
        leaf, componenttools.copy_components_and_remove_spanners([leaf], total - 1))
