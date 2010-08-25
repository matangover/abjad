from abjad.core import _StrictComparator


class KeySignature(_StrictComparator):

   __slots__ = ('_tonic', '_mode')

   def __init__(self, tonic, mode):
      from abjad.tools import pitchtools
      from abjad.tools import tonalitytools
      tonic = pitchtools.NamedPitchClass(tonic)
      mode = tonalitytools.Mode(mode)
      #object.__setattr__(self, '_tonic', tonic)
      #object.__setattr__(self, '_mode', mode)
      self._tonic = tonic
      self._mode = mode

   ## OVERLOADS ##

   def __eq__(self, arg):
      if isinstance(arg, KeySignature):
         if self.tonic == arg.tonic:
            if self.mode == arg.mode:
               return True
      return False

   def __ne__(self, arg):
      return not self == arg

   def __repr__(self):
      return "%s('%s', '%s')" % (self.__class__.__name__, self.tonic, self.mode)

   def __str__(self):
      return '%s-%s' % (self.tonic, self.mode)

   ## PUBLIC ATTRIBUTES ##

   @property
   def format(self):
      return r'\key %s \%s' % (self.tonic, self.mode)

   @property
   def mode(self):
      '''Read-only mode.'''
      return self._mode

   @property
   def name(self):
      if self.mode.mode_name_string == 'major':
         tonic = self.tonic.name.upper( )   
      else:
         tonic = self.tonic.name
      return '%s %s' % (tonic, self.mode.mode_name_string)

   @property
   def tonic(self):
      '''Read-only tonic.'''
      return self._tonic
