#from abjad.tools.divide._tie_chain_arbitrarily import _tie_chain_arbitrarily
from abjad.tools.tietools._tie_chain_to_tuplet import _tie_chain_to_tuplet


def tie_chain_to_augmented_tuplet_with_proportions_and_avoid_dots(tie_chain, proportions):
   r'''.. versionadded:: 1.1.2

   Divide `tie_chain` into fixed-duration tuplet according to 
   arbitrary integer `proportions`.

   Interpret `proportions` as a ratio. That is, reduce integers
   in `proportions` relative to each other.

   Return non-trivial tuplet as augmentation.

   Where ``proportions[i] == 1`` for ``i < len(proportions)``, 
   do not allow tupletted notes to carry dots. ::

      abjad> staff = Staff([Note(0, (1, 8)), Note(0, (1, 16)), Note(0, (1, 16))])
      abjad> TieSpanner(staff[:2])
      TieSpanner(c'8, c'16)
      abjad> BeamSpanner(staff[:])
      BeamSpanner(c'8, c'16, c'16)
      abjad> tietools.tie_chain_to_augmented_tuplet_with_proportions_and_avoid_dots(staff[0].tie.chain, [1])
      FixedDurationTuplet(3/16, [c'8])
      abjad> f(t)
      \new Staff {
              \fraction \times 3/2 {
                      c'8 [
              }
              c'16 ]
      }

   ::

      abjad> staff = Staff([Note(0, (1, 8)), Note(0, (1, 16)), Note(0, (1, 16))])
      abjad> TieSpanner(staff[:2])
      TieSpanner(c'8, c'16)
      abjad> BeamSpanner(staff[:])
      BeamSpanner(c'8, c'16, c'16)
      abjad> tietools.tie_chain_to_augmented_tuplet_with_proportions_and_avoid_dots(staff[0].tie.chain, [1, 2])
      FixedDurationTuplet(3/16, [c'16, c'8])
      abjad> f(staff)
      \new Staff {
              {
                      c'16 [
                      c'8
              }
              c'16 ]
      }

   ::

      abjad> staff = Staff([Note(0, (1, 8)), Note(0, (1, 16)), Note(0, (1, 16))])
      abjad> TieSpanner(staff[:2])
      TieSpanner(c'8, c'16)
      abjad> BeamSpanner(staff[:])
      BeamSpanner(c'8, c'16, c'16)
      abjad> tietools.tie_chain_to_augmented_tuplet_with_proportions_and_avoid_dots(staff[0].tie.chain, [1, 2, 2])
      FixedDurationTuplet(3/16, [c'32, c'16, c'16])
      abjad> f(staff)
      \new Staff {
              \fraction \times 6/5 {
                      c'32 [
                      c'16
                      c'16
              }
              c'16 ]
      }

   .. versionchanged:: 1.1.2
      renamed ``divide.tie_chain_into_arbitrary_augmentation_undotted( )`` to
      ``tietools.tie_chain_to_augmented_tuplet_with_proportions_and_avoid_dots( )``.
   '''

   prolation, dotted = 'augmentation', False
   #return _tie_chain_arbitrarily(tie_chain, proportions, prolation, dotted)
   return _tie_chain_to_tuplet(tie_chain, proportions, prolation, dotted)
