# -*- encoding: utf-8 -*-
from abjad import *


def test_Chord_fingered_pitches_01():

    staff = Staff("<c''' e'''>4 <d''' fs'''>4")
    glockenspiel = instrumenttools.Glockenspiel()(staff)
    instrumenttools.transpose_from_sounding_pitch_to_written_pitch(staff)

    r'''
    \new Staff {
        \set Staff.instrumentName = \markup { Glockenspiel }
        \set Staff.shortInstrumentName = \markup { Gkspl. }
        <c' e'>4
        <d' fs'>4
    }
    '''

    assert staff[0].fingered_pitches == (
        pitchtools.NamedChromaticPitch("c'"), pitchtools.NamedChromaticPitch("e'"))
