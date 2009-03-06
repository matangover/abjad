from abjad import *
from abjad.tools import construct


def test_tie_chain_truncate_01( ):
   '''Keep and unspan first note in tie chain only.'''

   t = Staff(construct.notes(0, [(5, 16)]))

   r'''
   \new Staff {
      c'4 ~
      c'16
   }
   '''
   
   tie_chain_truncate(t[0].tie.chain)

   r'''
   \new Staff {
      c'4
   }
   '''

   assert check(t)
   assert t.format == "\\new Staff {\n\tc'4\n}"


def test_tie_chain_truncate_02( ):
   '''No effect on length-1 tie chains.'''

   t = Staff(run(1))

   tie_chain_truncate(t[0].tie.chain)

   r'''
   \new Staff {
      c'8
   }
   '''

   assert check(t)
   assert t.format == "\\new Staff {\n\tc'8\n}"
