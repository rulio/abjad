from abjad.tools.timeintervaltools.TimeInterval import TimeInterval
from abjad.tools.timeintervaltools.TimeIntervalTree import TimeIntervalTree
from abjad.tools.timeintervaltools.all_are_intervals_or_trees_or_empty import all_are_intervals_or_trees_or_empty
from abjad.tools.timeintervaltools.compute_logical_not_of_intervals_in_interval import compute_logical_not_of_intervals_in_interval
from abjad.tools.timeintervaltools.compute_logical_or_of_intervals import compute_logical_or_of_intervals
from abjad.tools.timeintervaltools.get_all_unique_bounds_in_intervals import get_all_unique_bounds_in_intervals
from abjad.tools.timeintervaltools.split_intervals_at_rationals import split_intervals_at_rationals


def mask_intervals_with_intervals(masked_intervals, mask_intervals):
    '''Clip or remove all intervals in `masked_intervals` outside of the bounds
    defined in `mask_intervals`, while maintaining `masked_intervals`' payload contents ::

        >>> from abjad.tools import timeintervaltools
        >>> from abjad.tools.timeintervaltools import TimeInterval
        >>> from abjad.tools.timeintervaltools import TimeIntervalTree

    ::

        >>> a = TimeInterval(0, 10, {'a': 1})
        >>> b = TimeInterval(5, 15, {'b': 2})
        >>> tree = TimeIntervalTree([a, b])
        >>> mask = TimeInterval(4, 11)
        >>> timeintervaltools.mask_intervals_with_intervals(tree, mask)
        TimeIntervalTree([
            TimeInterval(Offset(4, 1), Offset(10, 1), {'a': 1}),
            TimeInterval(Offset(5, 1), Offset(11, 1), {'b': 2})
        ])

    Return interval tree.
    '''

    assert all_are_intervals_or_trees_or_empty(masked_intervals)
    assert all_are_intervals_or_trees_or_empty(mask_intervals)

    if isinstance(masked_intervals, TimeIntervalTree):
        masked_tree = masked_intervals
    else:
        masked_tree = TimeIntervalTree(masked_intervals)

    if isinstance(mask_intervals, TimeIntervalTree):
        mask_tree = mask_intervals
    else:
        mask_tree = TimeIntervalTree(mask_intervals)

    if not masked_tree or not mask_tree:
        return TimeIntervalTree([])

#   print 'masked: %d, %s | mask: %d, %s' % (len(masked_tree), get_all_unique_bounds_in_intervals(masked_tree), \
#      len(mask_tree), get_all_unique_bounds_in_intervals(mask_tree))

    start = min(mask_tree.start, masked_tree.start)
    stop = max(mask_tree.stop, masked_tree.stop)
    not_mask_tree = compute_logical_not_of_intervals_in_interval(mask_tree, TimeInterval(start, stop))

    if not not_mask_tree:
        return masked_tree

    not_mask_tree_bounds = get_all_unique_bounds_in_intervals(not_mask_tree)
    split_masked_tree = split_intervals_at_rationals(masked_tree, not_mask_tree_bounds)

    for interval in not_mask_tree:
        starts = set(split_masked_tree.find_intervals_starting_within_interval(interval))
        stops = set(split_masked_tree.find_intervals_stopping_within_interval(interval))
        intersection = set(starts).intersection(set(stops))
        split_masked_tree = TimeIntervalTree(list(set(split_masked_tree).difference(intersection)))

    return split_masked_tree
