from abjad.helpers.bequeath import bequeath
from abjad.meter.meter import Meter
from abjad.rational.rational import Rational
from abjad.tools import containertools
from abjad.tools import iterate
from abjad.tools import mathtools


def measures_subsume(expr):
   r'''Subsume all measures in expr containing only top-level tuplet.
      Measures usually become nonbinary as as result of subsumption.

      Returns None because processes potentially many measures.

      t = RigidMeasure((2, 8), [FixedDurationTuplet((2, 8), scale(3))])
      measures_subsume(t)

      \time 3/12
      \scaleDurations #'(2 . 3) {
         c'8
         d'8
         e'8
      }
   '''

   from abjad.measure.measure import _Measure
   from abjad.tuplet.tuplet import _Tuplet
   for measure in iterate.naive(expr, _Measure): 
      if len(measure) == 1:
         if isinstance(measure[0], _Tuplet):
            tuplet = measure[0]
            tuplet_multiplier = tuplet.duration.multiplier
            tuplet_denominator = tuplet_multiplier._d
            reduced_denominator = mathtools.remove_powers_of_two(tuplet_denominator)
            meter = measure.meter.effective
            meter_rational = Rational(meter.numerator, meter.denominator)
            numerator = meter_rational._n * reduced_denominator
            denominator = meter_rational._d * reduced_denominator
            measure.meter.forced = Meter(numerator, denominator)
            meter_multiplier = measure.meter.effective.multiplier
            written_adjustment = tuplet_multiplier / meter_multiplier
            bequeath([tuplet], tuplet[:])
            containertools.contents_scale(measure, written_adjustment)
