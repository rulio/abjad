from abjad.components._Leaf import _Leaf
from abjad.tools.componenttools.component_to_score_root import component_to_score_root
from abjad.tools.componenttools.iterate_timeline_forward_in_expr import \
   iterate_timeline_forward_in_expr


def iterate_timeline_forward_from_component(expr, klass = _Leaf):
   r'''.. versionadded:: 1.1.2

   Iterate timeline forward from `component`::

      abjad> score = Score([ ])
      abjad> score.append(Staff(notetools.make_repeated_notes(4, Fraction(1, 4))))
      abjad> score.append(Staff(notetools.make_repeated_notes(4)))
      abjad> macros.diatonicize(score)
      abjad> f(score)
      \new Score <<
              \new Staff {
                      c'4
                      d'4
                      e'4
                      f'4
              }
              \new Staff {
                      g'8
                      a'8
                      b'8
                      c''8
              }
      >>
      abjad> for leaf in componenttools.iterate_timeline_forward_from_component(score[1][2]):
      ...     leaf
      ... 
      Note(b', 8)
      Note(c'', 8)
      Note(e', 4)
      Note(f', 4)

   .. todo:: optimize to avoid behind-the-scenes full-score traversal.
   '''

   root = component_to_score_root(expr)
   component_generator = iterate_timeline_forward_in_expr(root, klass = klass)

   yielded_expr = False
   for component in component_generator:
      if yielded_expr:
         yield component
      elif component is expr:
         yield component
         yielded_expr = True
