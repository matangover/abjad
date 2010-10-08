from abjad.components._Leaf import _Leaf
from abjad.components.Note import Note
from abjad.tools import componenttools
from abjad.tools import markuptools
from abjad.tools import threadtools


def label_leaves_in_expr_with_melodic_diatonic_interval_classes(expr, markup_direction = 'up'):
   r""".. versionadded:: 1.1.2

   Label the melodic diatonic interval class of every leaf in `expr`. ::

      abjad> staff = Staff(notetools.make_notes([0, 25, 11, -4, -14, -13, 9, 10, 6, 5], [Fraction(1, 8)]))
      abjad> leaftools.label_leaves_in_expr_with_melodic_diatonic_inteval_classes(staff)
      abjad> f(staff)
      \new Staff {
              c'8 ^ \markup { +aug8 }
              cs'''8 ^ \markup { -M2 }
              b'8 ^ \markup { -aug2 }
              af8 ^ \markup { -m7 }
              bf,8 ^ \markup { aug1 }
              b,8 ^ \markup { +m7 }
              a'8 ^ \markup { +m2 }
              bf'8 ^ \markup { -dim4 }
              fs'8 ^ \markup { aug1 }
              f'8
      }
   """ 
   from abjad.tools import pitchtools

   for note in componenttools.iterate_components_forward_in_expr(expr, Note):
      thread_iterator = threadtools.iterate_thread_forward_from_component(note, _Leaf)
      try:
         thread_iterator.next( )
         next_leaf = thread_iterator.next( )
         if isinstance(next_leaf, Note):
            mdi = pitchtools.calculate_melodic_diatonic_interval_from_named_chromatic_pitch_to_named_chromatic_pitch(
               note, next_leaf)
            mdic = mdi.interval_class
            markuptools.Markup(mdic, markup_direction)(note)
      except StopIteration:
         pass
