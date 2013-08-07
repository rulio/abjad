# -*- encoding: utf-8 -*-
from abjad import *
import py.test


def test_containertools_get_element_starting_at_exactly_offset_01():

    voice = Voice("c'8 d'8 e'8 f'8 g'8 a'8 b'8 c''8")
    duration = containertools.get_element_starting_at_exactly_offset(voice, Duration(6, 8))

    assert duration is voice[6]


def test_containertools_get_element_starting_at_exactly_offset_02():

    voice = Voice("c'8 d'8 e'8 f'8 g'8 a'8 b'8 c''8")

    assert py.test.raises(MissingComponentError, 'containertools.get_element_starting_at_exactly_offset(voice, Duration(15, 8))')
