from abjad import *


def test__SpannerOffsetInterface_stop_01( ):
   '''Return stop time of spanner in score.'''

   t = Voice(macros.scale(4))
   beam = BeamSpanner(t[1:3])
   glissando = GlissandoSpanner([t])

   r'''
   \new Voice {
           c'8 \glissando
           d'8 [ \glissando
           e'8 ] \glissando
           f'8
   }
   '''

   assert beam.offset.stop == Rational(3, 8)
   assert glissando.offset.stop == Rational(4, 8)
