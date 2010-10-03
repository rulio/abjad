from abjad import *


def test_NamedPitch__init_by_name_and_octave_01( ):
   '''Init by name and octave.'''

   p = pitchtools.NamedPitch('df', 5)
   assert p.diatonic_pitch_number == 8
   assert p.format == "df''"
   assert p.letter == 'd'
   assert p.name == 'df'
   assert p.number == 13
   assert p.octave == 5
   assert p.pitch_class == pitchtools.NumericPitchClass(1)
   assert p.ticks == "''"
