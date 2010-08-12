from abjad import *


def test_LeafSpannerAggregator_clear_01( ):
   '''Clear a single spanner.'''

   t = Voice(macros.scale(4))
   p = BeamSpanner(t[ : ])

   r'''
   \new Voice {
      c'8 [
      d'8
      e'8
      f'8 ]
   }
   '''

   assert t.format == "\\new Voice {\n\tc'8 [\n\td'8\n\te'8\n\tf'8 ]\n}"

   t[0].spanners.clear( )

   r'''
   \new Voice {
      c'8
      d'8
      e'8
      f'8
   }
   '''

   assert t.format == "\\new Voice {\n\tc'8\n\td'8\n\te'8\n\tf'8\n}"


def test_LeafSpannerAggregator_clear_02( ):
   '''Clear multiple spanners.'''

   t = Voice(macros.scale(4))
   p1 = BeamSpanner(t[:])
   p2 = TrillSpanner(t[:])

   r'''
   \new Voice {
      c'8 [ \startTrillSpan
      d'8
      e'8
      f'8 ] \stopTrillSpan
   }
   '''

   assert t.format == "\\new Voice {\n\tc'8 [ \\startTrillSpan\n\td'8\n\te'8\n\tf'8 ] \\stopTrillSpan\n}"

   t[0].spanners.clear( )

   r'''
   \new Voice {
      c'8
      d'8
      e'8
      f'8
   }
   '''

   assert t.format == "\\new Voice {\n\tc'8\n\td'8\n\te'8\n\tf'8\n}"
