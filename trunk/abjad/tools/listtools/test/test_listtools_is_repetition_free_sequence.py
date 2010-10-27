from abjad import *


def test_listtools_is_repetition_free_sequence_01( ):

   assert listtools.is_repetition_free_sequence(range(6))


def test_listtools_is_repetition_free_sequence_02( ):

   assert not listtools.is_repetition_free_sequence([0, 1, 2, 2, 4, 5])


def test_listtools_is_repetition_free_sequence_03( ):
   '''Empty iterable boundary case.'''

   assert listtools.is_repetition_free_sequence([ ])
