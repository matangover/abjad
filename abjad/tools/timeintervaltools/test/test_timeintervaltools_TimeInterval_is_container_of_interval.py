# -*- encoding: utf-8 -*-
from abjad.tools.timeintervaltools import *
import pytest


def test_timeintervaltools_TimeInterval_is_container_of_interval_01():
    time_interval_1 = TimeInterval(-2, 2)
    time_interval_2 = TimeInterval(-7, -3)
    assert not time_interval_1.is_container_of_interval(time_interval_2)
    assert not time_interval_2.is_container_of_interval(time_interval_1)

def test_timeintervaltools_TimeInterval_is_container_of_interval_02():
    time_interval_1 = TimeInterval(-2, 2)
    time_interval_2 = TimeInterval(-6, -2)
    assert not time_interval_1.is_container_of_interval(time_interval_2)
    assert not time_interval_2.is_container_of_interval(time_interval_1)

def test_timeintervaltools_TimeInterval_is_container_of_interval_03():
    time_interval_1 = TimeInterval(-2, 2)
    time_interval_2 = TimeInterval(-4, 0)
    assert not time_interval_1.is_container_of_interval(time_interval_2)
    assert not time_interval_2.is_container_of_interval(time_interval_1)

def test_timeintervaltools_TimeInterval_is_container_of_interval_04():
    time_interval_1 = TimeInterval(-2, 2)
    time_interval_2 = TimeInterval(-2, 0)
    assert time_interval_1.is_container_of_interval(time_interval_2)
    assert not time_interval_2.is_container_of_interval(time_interval_1)

def test_timeintervaltools_TimeInterval_is_container_of_interval_05():
    time_interval_1 = TimeInterval(-2, 2)
    time_interval_2 = TimeInterval(-2, 2)
    assert time_interval_1.is_container_of_interval(time_interval_2)
    assert time_interval_2.is_container_of_interval(time_interval_1)

def test_timeintervaltools_TimeInterval_is_container_of_interval_06():
    time_interval_1 = TimeInterval(-2, 2)
    time_interval_2 = TimeInterval(-1, 1)
    assert time_interval_1.is_container_of_interval(time_interval_2)
    assert not time_interval_2.is_container_of_interval(time_interval_1)

def test_timeintervaltools_TimeInterval_is_container_of_interval_07():
    time_interval_1 = TimeInterval(-2, 2)
    time_interval_2 = TimeInterval(0, 2)
    assert time_interval_1.is_container_of_interval(time_interval_2)
    assert not time_interval_2.is_container_of_interval(time_interval_1)

def test_timeintervaltools_TimeInterval_is_container_of_interval_08():
    time_interval_1 = TimeInterval(-2, 2)
    time_interval_2 = TimeInterval(0, 4)
    assert not time_interval_1.is_container_of_interval(time_interval_2)
    assert not time_interval_2.is_container_of_interval(time_interval_1)

def test_timeintervaltools_TimeInterval_is_container_of_interval_09():
    time_interval_1 = TimeInterval(-2, 2)
    time_interval_2 = TimeInterval(2, 6)
    assert not time_interval_1.is_container_of_interval(time_interval_2)
    assert not time_interval_2.is_container_of_interval(time_interval_1)

def test_timeintervaltools_TimeInterval_is_container_of_interval_10():
    time_interval_1 = TimeInterval(-2, 2)
    time_interval_2 = TimeInterval(3, 7)
    assert not time_interval_1.is_container_of_interval(time_interval_2)
    assert not time_interval_2.is_container_of_interval(time_interval_1)
