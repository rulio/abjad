from abjad.pitch.pitch import Pitch
from abjad.spanner.grobhandler import _GrobHandlerSpanner
from abjad.trill.format import _TrillSpannerFormatInterface


class Trill(_GrobHandlerSpanner):

   def __init__(self, music = None):
      _GrobHandlerSpanner.__init__(self, 'TrillSpanner', music)
      self._format = _TrillSpannerFormatInterface(self)
      self._pitch = None

   ## PUBLIC ATTRIBUTES ##

   @apply
   def pitch( ):
      def fget(self):
         return self._pitch
      def fset(self, expr):
         if expr == None:
            self._pitch = None
         elif isinstance(expr, (int, float, long)):
            self._pitch = Pitch(expr)
         elif isinstance(expr, Pitch):
            self._pitch = Pitch
         else:
            raise ValueError('can not set trill pitch.')
      return property(**locals( ))
