from abjad.components._Leaf import _Leaf
import copy


class Chord(_Leaf):
   '''The Abjad model of a chord:

   ::

      abjad> Chord([4, 13, 17], (1, 4))
      Chord("ef' cs'' f''", '4')
   '''

   __slots__ = ('_note_heads', '_pitches', )

   def __init__(self, *args, **kwargs):
      from abjad.tools.chordtools._initialize_chord import _initialize_chord
      _initialize_chord(self, _Leaf, *args)
      self._initialize_keyword_values(**kwargs)

   ## OVERLOADS ##

   def __contains__(self, arg):
      from abjad.tools.notetools.NoteHead import NoteHead
      note_head = NoteHead(arg)
      return note_head in self.note_heads

   def __copy__(self, *args):
      new = type(self)(*self.__getnewargs__( ))
      if getattr(self, '_override', None) is not None:
         new._override = copy.copy(self.override)
      if getattr(self, '_set', None) is not None:
         new._set = copy.copy(self.set)
      return new

   #__deepcopy__ = __copy__

   def __delitem__(self, i):
      del(self._note_heads[i])

   def __eq__(self, arg):
      if _Leaf.__eq__(self, arg):
         if self.pitches == arg.pitches:
            return True
      return False

   def __getitem__(self, i):
      return self._note_heads[i]

   def __getnewargs__(self):
      result = [ ]
      result.append(self.pitches)
      result.append(self.duration.written)
      if self.duration.multiplier is not None:
         result.append(self.duration.multiplier)
      return tuple(result)

   def __len__(self):
      return len(self.note_heads)

   def __setitem__(self, i, arg):
      from abjad.tools.notetools.NoteHead import NoteHead
      if isinstance(arg, NoteHead):
         note_head = arg
      else:
         note_head = NoteHead(arg)
      note_head._client = self
      self._note_heads[i] = note_head
      self._note_heads.sort( )

   ## PRIVATE ATTRIBUTES ##

   @property
   def _compact_representation(self):
      return '<%s>%s' % (self._summary, self.duration)

   @property
   def _summary(self):
      '''Read-only string summary of noteh eads in chord.
      '''
      return ' '.join([str(x) for x in self])

   ## PUBLIC ATTRIBUTES ## 

   @apply
   def note_heads( ):
      def fget(self):
         '''Get read-only tuple of note heads in chord::

            abjad> chord = Chord([7, 12, 16], (1, 4))
            abjad> chord.note_heads
            (NoteHead(g'), NoteHead(c''), NoteHead(e''))
   
         Set chord note heads from any iterable::

            abjad> chord = Chord([7, 12, 16], (1, 4))
            abjad> chord.note_heads = [0, 2, 6]
            abjad> chord
            Chord(c' d' fs', 4)
         '''
         return tuple(self)
      def fset(self, note_head_tokens):
         self._note_heads = [ ]
         if isinstance(note_head_tokens, str):
            note_head_tokens = note_head_tokens.split( )
         self.extend(note_head_tokens)
      return property(**locals( ))

   @apply
   def pitches( ):
      def fget(self):
         '''Get read-only tuple of pitches in chord::

            abjad> chord = Chord([7, 12, 16], (1, 4))
            abjad> chord.pitches
            (NamedChromaticPitch(g, 4), NamedChromaticPitch(c, 5), NamedChromaticPitch(e, 5))

         Set chord pitches from any iterable::

            abjad> chord = Chord([7, 12, 16], (1, 4))
            abjad> chord.pitches = [0, 2, 6]
            abjad> chord
            Chord(c' d' fs', 4)
         '''
         return tuple([note_head.pitch for note_head in self])
      def fset(self, pitch_tokens):
         self.note_heads = pitch_tokens
      return property(**locals( ))

   ## PUBLIC METHODS ## 

   def append(self, note_head_token):
      '''Append `note_head_token` to chord::

         abjad> chord = Chord([4, 13, 17], (1, 4))
         abjad> chord
         Chord(e' cs'' f'', 4)

      ::

         abjad> chord.append(19)
         abjad> chord
         Chord(e' cs'' f'' g'', 4)

      Sort chord note heads automatically after append and return none.
      '''
      from abjad.tools.notetools.NoteHead import NoteHead
      if isinstance(note_head_token, NoteHead):
         note_head = note_head_token
      else:
         note_head = NoteHead(note_head_token)
      note_head._client = self
      self._note_heads.append(note_head)
      self._note_heads.sort( )

   def extend(self, note_head_tokens):
      '''Extend chord with `note_head_tokens`::

         abjad> chord = Chord([4, 13, 17], (1, 4))
         abjad> chord
         Chord(e' cs'' f'', 4)

      ::

         abjad> chord.extend([2, 12, 18])
         abjad> chord
         Chord(d' e' c'' cs'' f'' fs'', 4)

      Sort chord note heads automatically after extend and return none.
      '''
      for note_head_token in note_head_tokens:
         self.append(note_head_token)

   def pop(self, i = -1):
      '''Remove note head at index `i` in chord::

         abjad> chord = Chord([4, 13, 17], (1, 4))
         abjad> chord
         Chord(e' cs'' f'', 4)

      ::

         abjad> chord.pop(1)
         NoteHead(cs'')

      ::

         abjad> chord
         Chord(e' f'', 4)

      Return note head.
      '''
      note_head = self._note_heads.pop(i)
      note_head._client = None
      return note_head

   def remove(self, note_head):
      '''Remove `note_head` from chord::

         abjad> chord = Chord([4, 13, 17], (1, 4))
         abjad> chord
         Chord(e' cs'' f'', 4)

      ::

         abjad> chord.remove(chord[1])
         abjad> chord
         Chord(e' f'', 4)

      Return none.
      '''
      note_head._client = None
      self._note_heads.remove(note_head)
