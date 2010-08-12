from abjad import *
import py.test


def test_ParentageInterface__cut_01( ):
   '''Unspanned leaves can parentage-cut.'''

   t = Staff(macros.scale(4))
   note = t[1]
   note.parentage._cut( )

   r'''
   \new Staff {
           c'8
           e'8
           f'8
   }
   '''

   assert t.format == "\\new Staff {\n\tc'8\n\te'8\n\tf'8\n}"
   
   assert componenttools.is_well_formed_component(t)
   assert componenttools.is_well_formed_component(note)
   assert note.parentage.parent is None


def test_ParentageInterface__cut_02( ):
   '''Spanned leaves can parentage-cut.
      Spanners continue to attach to parentage-cut leaves.'''

   t = Voice([Container(macros.scale(4))])
   p = BeamSpanner(t.leaves)
   leaf = t.leaves[0]

   r'''
   \new Voice {
      {
         c'8 [
         d'8
         e'8
         f'8 ]
      }
   }
   '''

   leaf.parentage._cut( )
   assert not componenttools.is_well_formed_component(t)
   assert not componenttools.is_well_formed_component(leaf)

   t._music.insert(0, leaf)
   leaf.parentage._switch(t)

   r'''
   \new Voice {
           c'8 [
           {
                   d'8
                   e'8
                   f'8 ]
           }
   }
   '''

   assert componenttools.is_well_formed_component(t)
   assert componenttools.is_well_formed_component(leaf)
   assert t.format == "\\new Voice {\n\tc'8 [\n\t{\n\t\td'8\n\t\te'8\n\t\tf'8 ]\n\t}\n}"


def test_ParentageInterface__cut_03( ):
   '''Unspanned containers can parent-cut.'''

   t = Staff(Container(notetools.make_repeated_notes(2)) * 3)
   macros.diatonicize(t)
   sequential = t[1]

   r'''
   \new Staff {
           {
                   c'8
                   d'8
           }
           {
                   e'8
                   f'8
           }
           {
                   g'8
                   a'8
           }
   }
   '''
   
   sequential.parentage._cut( )

   r'''
   \new Staff {
           {
                   c'8
                   d'8
           }
           {
                   g'8
                   a'8
           }
   }
   '''

   assert t.format == "\\new Staff {\n\t{\n\t\tc'8\n\t\td'8\n\t}\n\t{\n\t\tg'8\n\t\ta'8\n\t}\n}"
   assert componenttools.is_well_formed_component(t)
   assert componenttools.is_well_formed_component(sequential)


def test_ParentageInterface__cut_04( ):
   '''Spanned containers parentage-cut successfully.
      Spanners continue to attach to parentage-cut containers.'''

   t = Voice([Container(FixedDurationTuplet((2, 8), macros.scale(3)) * 2)])
   tuplet = t[0][0]
   p = BeamSpanner(t[0][:])

   r'''
   \new Voice {
      {
         \times 2/3 {
            c'8 [
            d'8
            e'8
         }
         \times 2/3 {
            c'8
            d'8
            e'8 ]
         }
      }
   }
   '''

   tuplet.parentage._cut( )
   assert not componenttools.is_well_formed_component(t)
   assert not componenttools.is_well_formed_component(tuplet)

   t._music.insert(0, tuplet)
   tuplet.parentage._switch(t)
   
   r'''
   \new Voice {
      \times 2/3 {
         c'8 [
         d'8
         e'8
      }
      {
         \times 2/3 {
            c'8
            d'8
            e'8 ]
         }
      }
   }
   '''

   assert componenttools.is_well_formed_component(t)
   assert t.format == "\\new Voice {\n\t\\times 2/3 {\n\t\tc'8 [\n\t\td'8\n\t\te'8\n\t}\n\t{\n\t\t\\times 2/3 {\n\t\t\tc'8\n\t\t\td'8\n\t\t\te'8 ]\n\t\t}\n\t}\n}"
