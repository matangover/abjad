from abjad.helpers.tuplet_contents_fix import tuplet_contents_fix
from abjad.leaf.leaf import _Leaf
from abjad.rational.rational import Rational
from abjad.tools import durtools
from abjad.tools import leaftools
from abjad.tuplet.fd.tuplet import FixedDurationTuplet
from abjad.tuplet.fm.tuplet import FixedMultiplierTuplet


def tuplet_scale(tuplet, multiplier):
   '''Scale fixed-duration tuplet by multiplier.
      Preserve tuplet multiplier.
      Return tuplet.'''

   # check input
   if isinstance(tuplet, FixedMultiplierTuplet):
      raise NotImplemented
   elif not isinstance(tuplet, FixedDurationTuplet):
      raise ValueError('must be tuplet.')
   assert isinstance(multiplier, Rational)

   # find new target duration
   old_target_duration = tuplet.duration.target
   new_target_duration = multiplier * old_target_duration

   # change tuplet target duration
   tuplet.duration.target = new_target_duration

   # if multiplier is notehead assignable, scale contents graphically
   if durtools.is_assignable(multiplier):
      for component in tuplet[:]:
         if isinstance(component, _Leaf):
            leaftools.duration_scale(component, multiplier)

   # otherwise doctor up tuplet multiplier, if necessary
   elif not durtools.is_tuplet_multiplier(tuplet.duration.multiplier):
         tuplet_contents_fix(tuplet)

   # return tuplet
   return tuplet 
