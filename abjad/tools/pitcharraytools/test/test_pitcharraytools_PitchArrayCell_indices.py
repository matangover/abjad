# -*- encoding: utf-8 -*-
from abjad import *
from abjad.tools import pitcharraytools
from abjad.tools.pitcharraytools import PitchArrayCell
import pytest


def test_pitcharraytools_PitchArrayCell_indices_01():

    array = pitcharraytools.PitchArray([[1, 2, 1], [2, 1, 1]])

    '''
    [] [      ] []
    [      ] [] []
    '''

    assert array[0].cells[0].indices == (0, (0,))
    assert array[0].cells[1].indices == (0, (1, 2))
    assert array[0].cells[2].indices == (0, (3,))

    assert array[1].cells[0].indices == (1, (0, 1))
    assert array[1].cells[1].indices == (1, (2,))
    assert array[1].cells[2].indices == (1, (3,))


def test_pitcharraytools_PitchArrayCell_indices_02():

    cell = PitchArrayCell([pitchtools.NamedPitch(1)])

    assert pytest.raises(IndexError, 'cell.indices')
