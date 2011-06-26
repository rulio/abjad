from abjad import Fraction
from abjad.tools.treetools import *
from abjad.tools.treetools._make_test_intervals import _make_test_intervals


def test_treetools_calculate_depth_centroid_of_intervals_in_interval_01( ):
   tree = IntervalTree(_make_test_intervals( ))
   interval = BoundedInterval(0, 10)
   depth_centroid = calculate_depth_centroid_of_intervals_in_interval(tree, interval)
   assert depth_centroid == Fraction(131, 18)


def test_treetools_calculate_depth_centroid_of_intervals_in_interval_02( ):
   tree = IntervalTree(_make_test_intervals( ))
   interval = BoundedInterval(-100, -10)
   depth_centroid = calculate_depth_centroid_of_intervals_in_interval(tree, interval)
   assert depth_centroid is None
