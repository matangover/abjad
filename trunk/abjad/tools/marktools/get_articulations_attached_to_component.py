from abjad.tools.marktools.Articulation import Articulation


def get_articulations_attached_to_component(component):
   r'''.. versionadded:: 1.1.2

   Get articulations attached to `component`::

      abjad> staff = Staff(macros.scale(4))
      abjad> marktools.Articulation('staccato')(staff[0])
      abjad> marktools.Articulation('maracto')(staff[0])
      abjad> f(staff)
      \new Staff {
         %% comment 1
         %% comment 2
         c'8 (
         d'8
         e'8
         f'8 )
      }
      
   ::
      
      abjad> marktools.get_articulations_attached_to_component(staff[0]) 
      (Articulation('comment 1')(c'8), Articulation('comment 2')(c'8))

   Return tuple of zero or more marks.
   '''

   result = [ ]
   for mark in component._marks_for_which_component_functions_as_start_component:
      if isinstance(mark, Articulation):
         result.append(mark)

   result = tuple(result)
   return result
