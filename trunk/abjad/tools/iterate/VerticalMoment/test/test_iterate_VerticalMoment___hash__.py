from abjad import *


def test_VerticalMoment___hash___01( ):
   '''Vertical moments behave well when included in a set.'''

   t = Staff(construct.scale(4))
   vms = [ ]
   vms.extend(list(iterate.vertical_moments_forward_in(t)))
   vms.extend(list(iterate.vertical_moments_forward_in(t)))

   assert len(vms) == 8
   assert len(set(vms)) == 4
