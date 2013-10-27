# -*- encoding: utf-8 -*-
from abjad import *


def test_contexttools_KeySignatureMark___eq___01():

    ks1 = contexttools.KeySignatureMark('g', 'major')
    ks2 = contexttools.KeySignatureMark('g', 'major')
    ks3 = contexttools.KeySignatureMark('g', 'minor')

    assert ks1 == ks2
    assert not ks2 == ks3
    assert not ks3 == ks1