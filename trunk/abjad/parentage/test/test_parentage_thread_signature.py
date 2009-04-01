from abjad.component.component import _Component
from abjad import *
import py.test


def test_parentage_thread_signature_01( ):
   '''Return _ContainmentSignature giving the root and
      first voice, staff and score in the parentage of component.'''

   t = Container(run(4))
   t.insert(2, Container(Container(run(2)) * 2))
   t[2].parallel = True
   diatonicize(t)
   t.notehead.color = 'red'

   r'''{
           \override NoteHead #'color = #red
           c'8
           d'8
           <<
                   {
                           e'8
                           f'8
                   }
                   {
                           g'8
                           a'8
                   }
           >>
           b'8
           c''8
           \revert NoteHead #'color
   }'''

   '''All components here carry the exact same containment signature.'''

   signature = t.parentage._threadSignature

   for component in iterate(t, _Component):
      assert component.parentage._threadSignature == signature


def test_parentage_thread_signature_02( ):
   '''Return _ContainmentSignature giving the root and
      first voice, staff and score in the parentage of component.'''

   t = Voice(run(4))
   t.name = 'foo'
   t.insert(2, Container(Container(run(2)) * 2))
   t[2].parallel = True
   diatonicize(t)
   t.notehead.color = 'red'

   r'''\context Voice = "foo" \with {
           \override NoteHead #'color = #red
   } {
           c'8
           d'8
           <<
                   {
                           e'8
                           f'8
                   }
                   {
                           g'8
                           a'8
                   }
           >>
           b'8
           c''8
   }'''

   '''Again, all components here carry the exact same containment signature.'''

   signature = t.parentage._threadSignature

   for component in iterate(t, _Component):
      assert component.parentage._threadSignature == signature


def test_parentage_thread_signature_03( ):
   '''Return _ContainmentSignature giving the root and
      first voice, staff and score in the parentage of component.'''

   t = Voice(run(4))
   t.insert(2, Container(Container(run(2)) * 2))
   t[2].parallel = True
   diatonicize(t)
   t.notehead.color = 'red'

   r'''\new Voice \with {
           \override NoteHead #'color = #red
   } {
           c'8
           d'8
           <<
                   {
                           e'8
                           f'8
                   }
                   {
                           g'8
                           a'8
                   }
           >>
           b'8
           c''8
   }'''

   '''Again, all components here carry the exact same containment signature.'''

   containment = t.parentage._threadSignature

   for component in iterate(t, _Component):
      assert component.parentage._threadSignature == containment


def test_parentage_thread_signature_04( ):
   '''Return _ContainmentSignature giving the root and
      first voice, staff and score in the parentage of component.'''

   t = Voice(run(4))
   t.insert(2, Container(Voice(run(2)) * 2))
   t[2].parallel = True
   diatonicize(t)
   t.notehead.color = 'red'

   r'''\new Voice \with {
           \override NoteHead #'color = #red
   } {
           c'8
           d'8
           <<
                   \new Voice {
                           e'8
                           f'8
                   }
                   \new Voice {
                           g'8
                           a'8
                   }
           >>
           b'8
           c''8
   }'''

   signatures = [leaf.parentage._threadSignature for leaf in t.leaves]

   assert signatures[0] == signatures[1]
   assert signatures[0] != signatures[2]
   assert signatures[0] != signatures[4]
   assert signatures[0] == signatures[6]
   
   assert signatures[2] == signatures[3]
   assert signatures[2] != signatures[4]

      
def test_parentage_thread_signature_05( ):
   '''Return _ContainmentSignature giving the root and
      first voice, staff and score in parentage of component.'''

   t = Voice(run(4))
   t.name = 'foo'
   t.insert(2, Container(Voice(run(2)) * 2))
   t[2].parallel = True
   t[2][0].name = 'foo'
   diatonicize(t)
   t.notehead.color = 'red'

   r'''\context Voice = "foo" \with {
           \override NoteHead #'color = #red
   } {
           c'8
           d'8
           <<
                   \context Voice = "foo" {
                           e'8
                           f'8
                   }
                   \new Voice {
                           g'8
                           a'8
                   }
           >>
           b'8
           c''8
   }
   '''

   signatures = [leaf.parentage._threadSignature for leaf in t.leaves]

   signatures[0] == signatures[1]
   signatures[0] == signatures[2]
   signatures[0] != signatures[4]
   signatures[0] == signatures[6]

   signatures[2] == signatures[0]
   signatures[2] == signatures[3]
   signatures[2] == signatures[4]
   signatures[2] == signatures[6]

   signatures[4] != signatures[0]
   signatures[4] != signatures[2]
   signatures[4] == signatures[5]
   signatures[4] == signatures[6]


def test_parentage_thread_signature_06( ):
   '''Return _ContainmentSignature giving the root and
      first voice, staff and score in parentage of component.'''

   t = Container(Staff([Voice(scale(2))]) * 2)
   t[0].name = 'staff1'
   t[1].name = 'staff2'
   t[0][0].name = 'voicefoo'
   t[1][0].name = 'voicefoo'
   diatonicize(t)
   assert py.test.raises(ContiguityError, 'Beam(t.leaves)')
   Beam(t.leaves[:2])
   Beam(t.leaves[2:])

   r'''{
           \context Staff = "staff1" {
                   \context Voice = "voicefoo" {
                           c'8 [
                           d'8 ]
                   }
           }
           \context Staff = "staff2" {
                   \context Voice = "voicefoo" {
                           e'8 [
                           f'8 ]
                   }
           }
   }'''

   signatures = [leaf.parentage._threadSignature for leaf in t.leaves]

   signatures[0] == signatures[1]
   signatures[0] != signatures[2]

   signatures[2] != signatures[2]
   signatures[2] == signatures[3]

   
def test_parentage_thread_signature_07( ):
   '''Return _ContainmentSignature giving the root and
      first voice, staff and score in parentage of component.'''

   t = Container(run(2))
   t[1:1] = Container(Voice(run(1)) * 2) * 2
   t[1].parallel = True
   t[1][0].name = 'alto'
   t[1][1].name = 'soprano'
   t[2][0].name = 'alto'
   t[2][1].name = 'soprano'
   diatonicize(t)

   t[1][1][0].formatter.before.append(r"\override NoteHead #'color = #red")
   t[2][1][-1].formatter.after.append(r"\revert NoteHead #'color")

   r'''{
      c'8
      <<
         \context Voice = "alto" {
            d'8
         }
         \context Voice = "soprano" {
            \override NoteHead #'color = #red
            e'8
         }
      >>
      <<
         \context Voice = "alto" {
            f'8
         }
         \context Voice = "soprano" {
            g'8
            \revert NoteHead #'color
         }
      >>
      a'8
   }'''
   
   signatures = [leaf.parentage._threadSignature for leaf in t.leaves]

   signatures[0] != signatures[1]
   signatures[0] != signatures[2]
   signatures[0] != signatures[3]
   signatures[0] != signatures[4]
   signatures[0] == signatures[5]
   
   signatures[1] != signatures[0]
   signatures[1] != signatures[2]
   signatures[1] == signatures[3]
   signatures[1] != signatures[4]
   signatures[1] != signatures[5]
   
   signatures[2] != signatures[0]
   signatures[2] != signatures[1]
   signatures[2] != signatures[3]
   signatures[2] == signatures[4]
   signatures[2] != signatures[5]


def test_parentage_thread_signature_08( ):
   '''Unicorporated leaves carry different containment signatures.'''

   t1 = Note(0, (1, 8))
   t2 = Note(0, (1, 8))
  
   assert t1.parentage._threadSignature != t2.parentage._threadSignature


def test_parentage_thread_signature_09( ):
   '''Components here carry the same containment signature EXCEPT FOR root.
      Component containment signatures do not compare True.'''

   t1 = Staff([Voice([Note(0, (1, 8))])])
   t1.name = 'staff'
   t1[0].name = 'voice'

   t2 = Staff([Voice([Note(0, (1, 8))])])
   t2.name = 'staff'
   t2[0].name = 'voice'

   t1_leaf_signature = t1.leaves[0].parentage._threadSignature
   t2_leaf_signature = t2.leaves[0].parentage._threadSignature
   assert t1_leaf_signature != t2_leaf_signature


def test_parentage_thread_signature_10( ):
   '''Measure and leaves must carry same thread signature.'''

   t = Staff([DynamicMeasure(scale(2))] + run(2))
   diatonicize(t)

   r'''\new Staff {
         \time 1/4
         c'8
         d'8
      e'8
      f'8
   }'''

   assert t[0].parentage._threadSignature == t[-1].parentage._threadSignature
   assert t[0].parentage._threadSignature == t[0][0].parentage._threadSignature
   assert t[0][0].parentage._threadSignature == t[-1].parentage._threadSignature
