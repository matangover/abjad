# -*- encoding: utf-8 -*-
from abjad import *
from abjad.tools import sequencetools
import pytest


def test_datastructuretools_CyclicList___getslice___01():

    cyclic_list = datastructuretools.CyclicList(range(3))

    assert cyclic_list[:2] == [0, 1]
    assert cyclic_list[:10] == [0, 1, 2, 0, 1, 2, 0, 1, 2, 0]
    assert cyclic_list[2:10] == [2, 0, 1, 2, 0, 1, 2, 0]
