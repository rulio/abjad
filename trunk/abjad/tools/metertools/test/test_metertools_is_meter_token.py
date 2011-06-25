from abjad import *
from abjad.tools import metertools


def test_metertools_is_meter_token_01( ):

   assert metertools.is_meter_token(contexttools.TimeSignatureMark(3, 8))
   assert metertools.is_meter_token(Duration(3, 8))
   assert metertools.is_meter_token((3, 8))


def test_metertools_is_meter_token_02( ):

   assert not metertools.is_meter_token('text')
