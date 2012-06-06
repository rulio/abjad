from abjad.tools.leaftools.Leaf import Leaf
from abjad.tools import durationtools


def copy_written_duration_and_multiplier_from_leaf_to_leaf(source_leaf, target_leaf):
    r'''.. versionadded:: 2.0

    Copy written duration and multiplier from `source_leaf` to `target_leaf`::

        >>> note = Note("c'4")
        >>> note.duration_multiplier = Duration(1, 2)
        >>> rest = Rest((1, 64))
        >>> leaftools.copy_written_duration_and_multiplier_from_leaf_to_leaf(note, rest)
        Rest('r4 * 1/2')

    Return `target_leaf`.
    '''

    # check source leaf type
    if not isinstance(source_leaf, Leaf):
        raise TypeError('must be leaf.')

    # check target leaf type
    if not isinstance(target_leaf, Leaf):
        raise TypeError('must be leaf.')

    # copy source leaf written duration and multiplier
    written = durationtools.Duration(source_leaf.written_duration)
    multiplier = durationtools.Duration(source_leaf.duration_multiplier)

    # set target leaf written duration and multiplier
    target_leaf.written_duration = written
    target_leaf.duration_multiplier = multiplier

    # return target leaf
    return target_leaf
