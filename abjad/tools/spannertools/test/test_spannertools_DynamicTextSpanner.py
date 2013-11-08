# -*- encoding: utf-8 -*-
from abjad import *


def test_spannertools_DynamicTextSpanner_01():

    voice = Voice("c'8 d'8 e'8 f'8")
    beam = Beam()
    attach(beam, voice[:])
    spanner = spannertools.DynamicTextSpanner(mark='f')
    attach(spanner, voice[:2])
    spanner = spannertools.DynamicTextSpanner(mark='p')
    attach(spanner, voice[2:])

    assert testtools.compare(
        voice,
        r'''
        \new Voice {
            c'8 [ \f
            d'8
            e'8 \p
            f'8 ]
        }
        '''
        )

    assert inspect(voice).is_well_formed()
