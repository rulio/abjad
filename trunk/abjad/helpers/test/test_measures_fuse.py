from abjad import *


def test_measures_fuse_01( ):
   '''Fuse binary measures with different denominators.
      Helpers selects minimum of two denominators.
      Beams are OK because they attach to leaves rather than containers.'''

   t = Voice(measures_make([(1, 8), (2, 16)]))
   measures_populate(t, Rational(1, 16))
   pitchtools.diatonicize(t)
   Beam(t.leaves)

   r'''
   \new Voice {
         \time 1/8
         c'16 [
         d'16
         \time 2/16
         e'16
         f'16 ]
   }
   '''

   #measures_fuse(t[0], t[1])
   measures_fuse(t[:])

   r'''
   \new Voice {
         \time 2/8
         c'16 [
         d'16
         e'16
         f'16 ]
   }
   '''

   assert check.wf(t)
   assert t.format == "\\new Voice {\n\t\t\\time 2/8\n\t\tc'16 [\n\t\td'16\n\t\te'16\n\t\tf'16 ]\n}"


 
def test_measures_fuse_02( ):
   '''Fuse binary measures with different denominators.
      Helpers selects minimum of two denominators.
      Beams are OK because they attach to leaves rather than containers.'''

   t = Voice(measures_make([(1, 8), (2, 16)]))
   measures_populate(t, Rational(1, 16))
   pitchtools.diatonicize(t)
   Beam(t[0])

   r'''
   \new Voice {
         \time 1/8
         c'16 [
         d'16 ]
         \time 2/16
         e'16
         f'16
   }
   '''

   #measures_fuse(t[0], t[1])
   measures_fuse(t[:])

   r'''
   \new Voice {
         \time 2/8
         c'16 [
         d'16
         e'16
         f'16 ]
   }
   '''

   assert check.wf(t)
   assert t.format == "\\new Voice {\n\t\t\\time 2/8\n\t\tc'16 [\n\t\td'16\n\t\te'16\n\t\tf'16 ]\n}"


def test_measures_fuse_03( ):
   '''Fuse binary and nonbinary measures.
      Helpers selects least common multiple of denominators.
      Beams are OK because they attach to leaves rather than containers.'''

   m1 = RigidMeasure((1, 8), run(1))
   m2 = RigidMeasure((1, 12), run(1))
   t = Voice([m1, m2])
   pitchtools.diatonicize(t)
   Beam(t.leaves)

   r'''
   \new Voice {
                   \time 1/8
                   c'8 [
                   \time 1/12
                   \scaleDurations #'(2 . 3) {
                           d'8 ]
                   }
   }
   '''

   #measures_fuse(t[0], t[1])
   measures_fuse(t[:])

   r'''
   \new Voice {
                   \time 5/24
                   \scaleDurations #'(2 . 3) {
                           c'8. [
                           d'8 ]
                   }
   }
   '''

   assert check.wf(t)
   assert t.format == "\\new Voice {\n\t\t\\time 5/24\n\t\t\\scaleDurations #'(2 . 3) {\n\t\t\tc'8. [\n\t\t\td'8 ]\n\t\t}\n}"


def test_measures_fuse_04( ):
   '''Fusing empty list raises no excpetion but returns None.'''

   result = measures_fuse([ ])
   assert result is None


def test_measures_fuse_05( ):
   '''Fusing list of only one measure returns measure unaltered.'''

   t = RigidMeasure((3, 8), scale(3))
   new = measures_fuse([t])

   assert new is t


def test_measures_fuse_06( ):
   '''Fuse three measures.'''

   t = Voice(measures_make([(1, 8), (1, 8), (1, 8)]))
   measures_populate(t, Rational(1, 16))
   pitchtools.diatonicize(t)
   Beam(t.leaves)

   r'''
   \new Voice {
                   \time 1/8
                   c'16 [
                   d'16
                   \time 1/8
                   e'16
                   f'16
                   \time 1/8
                   g'16
                   a'16 ]
   }
   '''

   measures_fuse(t[:])

   r'''
   \new Voice {
                   \time 3/8
                   c'16 [
                   d'16
                   e'16
                   f'16
                   g'16
                   a'16 ]
   }
   '''

   assert check.wf(t)
   assert t.format == "\\new Voice {\n\t\t\\time 3/8\n\t\tc'16 [\n\t\td'16\n\t\te'16\n\t\tf'16\n\t\tg'16\n\t\ta'16 ]\n}"
