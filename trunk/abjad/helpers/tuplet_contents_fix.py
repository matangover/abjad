from abjad.tools import mathtools
from abjad.helpers.leaf_duration_change import leaf_duration_change
from abjad.leaf.leaf import _Leaf
from abjad.rational.rational import Rational
from abjad.tuplet.fd.tuplet import FixedDurationTuplet
from abjad.tuplet.fm.tuplet import FixedMultiplierTuplet
import math


def tuplet_contents_fix(tuplet):
   '''Scale tuplet contents by power of two
      if tuplet multiplier less than 1/2 or greater than 2.
   
      Return tuplet.'''

   # check input
   if isinstance(tuplet, FixedMultiplierTuplet):
      raise NotImplemented
   elif not isinstance(tuplet, FixedDurationTuplet):
      raise ValueError('must be tuplet.')

   # find tuplet multiplier
   integer_exponent = mathtools.chop(math.log(tuplet.duration.multiplier, 2))
   leaf_multiplier = Rational(2) ** integer_exponent

   # scale leaves in tuplet by power of two
   for component in tuplet[:]:
      if isinstance(component, _Leaf):
         old_written_duration = component.duration.written
         new_written_duration = leaf_multiplier * old_written_duration
         leaf_duration_change(component, new_written_duration)

   return tuplet
