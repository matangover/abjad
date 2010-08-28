from abjad import *


def test_marktools_get_effective_key_signature_01( ):
   '''Apply key signature mark.
   '''

   t = Staff(macros.scale(4))
   marktools.KeySignatureMark('c', 'major')(t)

   r'''
   \new Staff {
           \key c \major
           c'8
           d'8
           e'8
           f'8
   }
   '''

   assert marktools.get_effective_key_signature(t) == marktools.KeySignatureMark('c', 'major')
   assert componenttools.is_well_formed_component(t)
   assert t.format == "\\new Staff {\n\t\\key c \\major\n\tc'8\n\td'8\n\te'8\n\tf'8\n}"

   
def test_marktools_get_effective_key_signature_02( ):
   '''There is no default key signature.
   '''

   t = Staff(macros.scale(4))
   assert marktools.get_effective_key_signature(t) is None
