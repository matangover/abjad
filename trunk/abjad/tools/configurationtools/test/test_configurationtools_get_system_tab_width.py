from abjad import *
from abjad.tools import configurationtools


def test_configurationtools_get_system_tab_width_01():

    assert configurationtools.get_system_tab_width() == 3
