# -*- encoding: utf-8 -*-
from abjad import *


def test_instrumenttools_EnglishHorn_sounding_pitch_of_written_middle_c_01():

    english_horn = instrumenttools.EnglishHorn()

    assert english_horn.sounding_pitch_of_written_middle_c == 'f'