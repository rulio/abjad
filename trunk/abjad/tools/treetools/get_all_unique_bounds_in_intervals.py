from abjad.tools.treetools.IntervalTree import IntervalTree
from abjad.tools.treetools.all_are_intervals_or_trees_or_empty \
   import all_are_intervals_or_trees_or_empty


def get_all_unique_bounds_in_intervals(intervals):
   '''Return all unique starting and ending boundaries in `intervals`.'''

   assert all_are_intervals_or_trees_or_empty(intervals)
   tree = IntervalTree(intervals)

   values = [ ]
   for interval in tree:
      if interval.low not in values:
         values.append(interval.low)
      if interval.high not in values:
         values.append(interval.high)
   return tuple(sorted(values))
