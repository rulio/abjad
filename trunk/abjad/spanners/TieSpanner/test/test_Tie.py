from abjad import *


def test_Tie_01( ):

   t = Voice(macros.scale(8))
   p = TieSpanner(t[4:6])

   assert len(p) == 2

   assert not t[0].tie.spanned
   assert not t[1].tie.spanned
   assert not t[2].tie.spanned
   assert not t[3].tie.spanned
   assert t[4].tie.spanned
   assert t[5].tie.spanned
   assert not t[6].tie.spanned
   assert not t[7].tie.spanned

   assert t[4].tie.spanner is t[5].tie.spanner
