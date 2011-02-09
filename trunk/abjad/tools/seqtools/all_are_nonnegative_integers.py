from abjad.tools import mathtools


def all_are_nonnegative_integers(expr):
   '''.. versionadded:: 1.1.2

   True when `expr` is a sequence and all elements  in `expr` are nonnegative integers::

      abjad> seqtools.all_are_nonnegative_integers([0 1, 2, 99])
      True

   Otherwise false::

      abjad> seqtools.all_are_nonnegative_integers([0, 1, 2, -99])
      False

   Return boolean.
   '''

   try:
      return all([mathtools.is_nonnegative_integer(x) for x in expr])
   except TypeError:
      return False
