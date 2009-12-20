from abjad.markup import Markup
from abjad.spanners.text.spanner import TextSpanner


def solid_text_spanner_above_with_nib_at_right(left_text, components = None):
   r'''.. versionadded:: 1.1.2

   Span `components` with text spanner.
   Position spanner above staff and configure with `left_text`,
   solid line and downward-pointing nib at right. ::
   
      abjad> t = Staff(construct.scale(4))
      abjad> spanners.solid_text_spanner_above_with_nib_at_right('foo', t[:])
      abjad> f(t)
      \new Staff {
              \override TextSpanner #'bound-details #'left #'text = \markup { foo }
              \override TextSpanner #'bound-details #'right #'text = #(markup #:draw-line '(0 . 1))
              \override TextSpanner #'bound-details #'right-broken #'text = ##f
              \override TextSpanner #'dash-fraction = #1
              \override TextSpanner #'direction = #up
              c'8 \startTextSpan
              d'8
              e'8
              f'8 \stopTextSpan
              \revert TextSpanner #'direction
              \revert TextSpanner #'bound-details #'left #'text
              \revert TextSpanner #'dash-fraction
              \revert TextSpanner #'bound-details #'right #'text
              \revert TextSpanner #'bound-details #'right-broken #'text
      }
   '''

   text_spanner = TextSpanner(components) 
   left_text = Markup(left_text)
   text_spanner.bound_details__left__text = left_text
   right_text = Markup("(markup #:draw-line '(0 . -1))")
   right_text.style = 'scheme'
   text_spanner.bound_details__right__text = right_text
   text_spanner.bound_details__right_broken__text = False
   text_spanner.dash_fraction = 1
   text_spanner.direction = 'up'

   return text_spanner
