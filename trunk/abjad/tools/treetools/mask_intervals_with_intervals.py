from abjad.tools.treetools.BoundedInterval import BoundedInterval
from abjad.tools.treetools.IntervalTree import IntervalTree
from abjad.tools.treetools.all_are_intervals_or_trees_or_empty \
   import all_are_intervals_or_trees_or_empty
from abjad.tools.treetools.compute_logical_not_of_intervals import compute_logical_not_of_intervals
from abjad.tools.treetools.split_intervals_at_rationals import split_intervals_at_rationals
from abjad.tools.treetools.get_all_unique_bounds_in_intervals import get_all_unique_bounds_in_intervals


def mask_intervals_with_intervals(masked_intervals, mask_intervals):
   '''Clip or remove all intervals in `masked_intervals` outside of the bounds
   defined in `mask_intervals`, while maintaining `masked_intervals`' payload contents ::

      abjad> a = BoundedInterval(0, 10, 'a')
      abjad> b = BoundedInterval(5, 15, 'b')
      abjad> tree = IntervalTree([a, b])
      abjad> mask = BoundedInterval(4, 11)
      abjad> mask_intervals_with_intervals(tree, mask)
      IntervalTree([
         BoundedInterval(4, 10, data = 'a'),
         BoundedInterval(5, 11, data = 'b')
      ])
   '''    

   assert all_are_intervals_or_trees_or_empty(masked_intervals)
   assert all_are_intervals_or_trees_or_empty(mask_intervals)
   masked_tree = IntervalTree(masked_intervals)
   mask_tree = IntervalTree(mask_intervals)
   not_mask_tree = compute_logical_not_of_intervals(mask_tree)

   if masked_tree.low < mask_tree.low:
      not_mask_tree = IntervalTree([not_mask_tree,
         BoundedInterval(masked_tree.low, mask_tree.low)])
   if mask_tree.high < masked_tree.high:
      not_mask_tree = IntervalTree([not_mask_tree, 
         BoundedInterval(mask_tree.high, masked_tree.high)])
   split_masked_tree = split_intervals_at_rationals(masked_tree, \
      get_all_unique_bounds_in_intervals(not_mask_tree))

   for interval in not_mask_tree:
      starts = set(split_masked_tree.find_intervals_starting_within_interval(interval))
      stops = set(split_masked_tree.find_intervals_stopping_within_interval(interval))
      intersection = set(starts).intersection(set(stops))
      split_masked_tree = IntervalTree(list(set(split_masked_tree).difference(intersection)))

   return split_masked_tree
