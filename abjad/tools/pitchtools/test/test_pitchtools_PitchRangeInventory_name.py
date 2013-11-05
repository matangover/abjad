# -*- encoding: utf-8 -*-
from abjad import *
import pytest


def test_pitchtools_PitchRangeInventory_name_01():

    inventory = pitchtools.PitchRangeInventory(['[A0, C8]'])
    assert inventory.name is None

    inventory.name = 'blue inventory'
    assert inventory.name == 'blue inventory'


def test_pitchtools_PitchRangeInventory_name_02():

    inventory = pitchtools.PitchRangeInventory(['[A0, C8]'])
    assert pytest.raises(Exception, 'inventory.name = 99')
