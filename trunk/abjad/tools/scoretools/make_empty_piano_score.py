from abjad.components import Score
from abjad.components import Staff
from abjad.tools import contexttools
from abjad.tools.scoretools.PianoStaff import PianoStaff


def make_empty_piano_score( ):
   r'''.. versionadded:: 1.1.1
   
   Make empty piano score::

      abjad> score, treble, bass = scoretools.make_empty_piano_score( )

   ::

      abjad> f(score)
      \new Score <<
         \new PianoStaff <<
            \new Staff {
               \clef "treble"
            }
            \new Staff {
               \clef "bass"
            }
         >>
      >>

   Return score, treble staff, bass staff.

   .. versionchanged:: 1.1.2
      renamed ``scoretools.make_piano_staff( )`` to
      ``scoretools.make_empty_piano_score( )``.
   '''

   ## make treble staff
   treble_staff = Staff([ ])
   treble_staff.name = 'treble'
   contexttools.ClefMark('treble')(treble_staff)

   ## make bass staff
   bass_staff = Staff([ ])
   bass_staff.name = 'bass'
   contexttools.ClefMark('bass')(bass_staff)

   ## make piano staff and score
   piano_staff = PianoStaff([treble_staff, bass_staff])
   score = Score([ ])
   score.append(piano_staff)

   ## return score, treble staff, bass staff
   return score, treble_staff, bass_staff
