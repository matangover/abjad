from abjad.helpers.is_tie_chain import _is_tie_chain


def tie_chain_truncate(tie_chain):
   '''Detach all leaves of tie chain after the first.
      Unspan and return length-1 tie chain.'''
   
   assert _is_tie_chain(tie_chain)

   for leaf in tie_chain[1:]:
      leaf.detach( )

   first = tie_chain[0]

   first.tie.unspan( )
   
   return first.tie.chain
