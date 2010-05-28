from abjad.rational import Rational
from abjad.score import Score
from abjad.staff import Staff
from abjad.tools import clone
from abjad.tools.construct.scale import scale



def scale_period(key_signature = None):
   r'''.. versionadded:: 1.1.2

   Construct one up-down period of scale according to `key_signature`::

      abjad> score = construct.scale_period(KeySignature('E', 'major'))
      abjad> f(score)
      \new Score \with {
              tempoWholesPerMinute = #(ly:make-moment 30 1)
      } <<
              \new Staff {
                      \key e \major
                      e'8
                      fs'8
                      gs'8
                      a'8
                      b'8
                      cs''8
                      ds''8
                      e''8
                      ds''8
                      cs''8
                      b'8
                      a'8
                      gs'8
                      fs'8
                      e'4
              }
      >>
   '''

   ascending_notes = scale(8, Rational(1, 8), key_signature)
   descending_notes = clone.unspan(ascending_notes[:-1])
   descending_notes.reverse( )
   notes = ascending_notes + descending_notes
   notes[-1].duration.written = Rational(1, 4)
   staff = Staff(notes)
   staff.key_signature.forced = key_signature
   score = Score([staff])
   score.tempo.tempo_wholes_per_minute = 30

   return score
