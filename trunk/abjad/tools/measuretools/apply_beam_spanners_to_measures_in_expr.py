from abjad.spanners import BeamSpanner
from abjad.tools.measuretools.apply_beam_spanner_to_measure import apply_beam_spanner_to_measure
from abjad.tools.measuretools.iterate_measures_forward_in_expr import iterate_measures_forward_in_expr


def apply_beam_spanners_to_measures_in_expr(expr):
   r'''.. versionadded:: 1.1.1

   Apply beam spanners to measures in `expr`::

      abjad> staff = Staff(RigidMeasure((2, 8), notetools.make_repeated_notes(2)) * 2)
      abjad> macros.diatonicize(staff)
      abjad> f(staff)
      \new Staff {
         {
            \time 2/8
            c'8
            d'8
         }
         {
            \time 2/8
            e'8
            f'8
         }
      }
      
   ::
      
      abjad> measuretools.apply_beam_spanners_to_measures_in_expr(staff)
      [BeamSpanner(|2/8(2)|), BeamSpanner(|2/8(2)|)]
      
   ::
      
      abjad> f(staff)
      \new Staff {
         {
            \time 2/8
            c'8 [
            d'8 ]
         }
         {
            \time 2/8
            e'8 [
            f'8 ]
         }
      }

   Return list of beams created.

   .. versionchanged:: 1.1.2
      renamed ``measuretools.beam( )`` to
      ``measuretools.apply_beam_spanners_to_measures_in_expr( )``.

   .. versionchanged:: 1.1.2
      renamed ``measuretools.apply_beam_spanners_to_measures_in( )`` to
      ``measuretools.apply_beam_spanners_to_measures_in_expr( )``.
   '''

   ## init beams created
   beams_created = [ ]

   ## apply beam spanners to measures in expr
   for measure in iterate_measures_forward_in_expr(expr):
      beam = apply_beam_spanner_to_measure(measure)
      beams_created.append(beam)

   ## return beams created
   return beams_created
