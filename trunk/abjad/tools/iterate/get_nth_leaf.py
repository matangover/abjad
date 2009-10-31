from abjad.leaf.leaf import _Leaf
from abjad.tools.iterate.get_nth_component import get_nth_component as \
   iterate_get_nth_component


def get_nth_leaf(expr, n = 0):
   r'''.. versionadded:: 1.1.2

   Return leaf `n` in `expr`. ::

      abjad> staff = Staff(RigidMeasure((2, 8), construct.run(2)) * 3)
      abjad> pitchtools.diatonicize(staff)
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
              {
                      \time 2/8
                      g'8
                      a'8
              }
      }

   ::

      abjad> for n in range(6):
      ...     iterate.get_nth_leaf(t, n)
      ... 
      Note(c', 8)
      Note(d', 8)
      Note(e', 8)
      Note(f', 8)
      Note(g', 8)
      Note(a', 8)

   Read backwards for negative values of `n`. ::

      abjad> iterate.get_nth_leaf(t, -1)
      Note(a', 8)
      
   .. note:: Because this function returns as soon as it finds instance
      `n` of `klasses`, it is more efficient to call
      ``iterate.get_nth_leaf(expr, 0)`` than ``expr.leaves[0]``.
      It is likewise more efficient to call
      ``iterate.get_nth_leaf(expr, -1)`` than ``expr.leaves[-1]``.

   .. todo:: implement ``iterate.yield_leaves(expr, i = 0, j = None)``
      as a generalization of, and companion to, this function.
   '''

   return iterate_get_nth_component(expr, _Leaf, n)
