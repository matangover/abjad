import fractions
from abjad.tools import contexttools
from abjad.tools import durationtools


def tempo_scaled_rational_to_milliseconds(rational, tempo):
    '''Return the millisecond value of `rational` at `tempo`.

    ::

        >>> from experimental import *

    ::

        >>> from experimental.quantizationtools import tempo_scaled_rational_to_milliseconds
        >>> tempo = contexttools.TempoMark((1, 4), 60)
        >>> tempo_scaled_rational_to_milliseconds(Fraction(1, 4), tempo)
        Duration(1000, 1)

    Return a :py:class:`~abjad.tools.durationtools.Duration`.
    '''

    assert isinstance(rational, (int, fractions.Fraction))
    assert isinstance(tempo, contexttools.TempoMark)

    whole_note_duration = 1000 \
        * fractions.Fraction(tempo.duration.denominator, tempo.duration.numerator) \
        * fractions.Fraction(60, tempo.units_per_minute)

    return durationtools.Duration(rational * whole_note_duration)
