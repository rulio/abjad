from abjad.tools.pitchtools._IntervalSegment import _IntervalSegment
from abjad.tools.pitchtools.DiatonicIntervalClass import DiatonicIntervalClass


class DiatonicIntervalClassSegment(_IntervalSegment):
   '''.. versionadded:: 1.1.2

   Ordered collection of diatonic interval classes::

      abjad> pitchtools.DiatonicIntervalClassSegment([('major', 2), ('major', 9), ('minor', -2), ('minor', -9)]) 
      DiatonicIntervalClassSegment(M2, M2, m2, m2)
   '''

   def __init__(self, diatonic_interval_class_tokens):
      for token in diatonic_interval_class_tokens:
         dic = DiatonicIntervalClass(token)
         self.append(dic)

   ## OVERLOADS ##

   def __copy__(self):
      return DiatonicIntervalClassSegment(self.intervals)

   ## PUBLIC ATTRIBUTES ##

   @property
   def is_tertian(self):
      '''True when all diatonic interval classes in segment are tertian:

      ::

         abjad> dics = pitchtools.DiatonicIntervalClassSegment([('major', 3), ('minor', 6), ('major', 6)])
         abjad> dics.is_tertian 
         True

      Otherwise false.
      '''
      for dic in self:
         if not dic.number == 3:
            return False
      return True
