from abjad.tools.pitchtools.list_named_chromatic_pitches_in_expr import list_named_chromatic_pitches_in_expr
from abjad.tools.pitchtools.NumberedChromaticPitchClass import NumberedChromaticPitchClass


def list_numbered_chromatic_pitch_classes_in_expr(expr):
   '''.. versionadded:: 1.1.2

   List numbered chromatic pitch-classes in `expr`::

      abjad> chord = Chord([13, 14, 15], (1, 4))
      abjad> pitchtools.list_numbered_chromatic_pitch_classes_in_expr(chord)
      (NumerciPitchClass(1), NumberedChromaticPitchClass(2), NumberedChromaticPitchClass(3))

   Works with notes, chords, defective chords.

   Return tuple or zero or more numbered chromatic pitch-classes.

   .. versionchanged:: 1.1.2
      renamed ``pitchtools.list_numeric_chromatic_pitch_classes_in_expr( )`` to
      ``pitchtools.list_numbered_chromatic_pitch_classes_in_expr( )``.
   '''

   pitches = list_named_chromatic_pitches_in_expr(expr)
   pitch_classes = [NumberedChromaticPitchClass(pitch) for pitch in pitches]
   pitch_classes = tuple(pitch_classes)
   return pitch_classes
