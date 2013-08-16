# -*- encoding: utf-8 -*-
from abjad import *


def test_Container_pop_01():
    r'''Containers pop leaves correctly.
        Popped leaves detach from parent.
        Popped leaves withdraw from crossing spanners.
        Popped leaves carry covered spanners forward.'''

    voice = Voice("c'8 d'8 e'8 f'8")
    spannertools.SlurSpanner(voice[:])
    spannertools.BeamSpanner(voice[1])

    r'''
    \new Voice {
        c'8 (
        d'8 [ ]
        e'8
        f'8 )
    }
    '''

    result = voice.pop(1)

    r'''
    \new Voice {
        c'8 (
        e'8
        f'8 )
    }
    '''

    assert select(voice).is_well_formed()
    assert testtools.compare(
        voice,
        r'''
        \new Voice {
            c'8 (
            e'8
            f'8 )
        }
        '''
        )

    "Result is now d'8 [ ]"

    assert select(result).is_well_formed()
    assert result.lilypond_format == "d'8 [ ]"


def test_Container_pop_02():
    r'''Containers pop nested containers correctly.
        Popped containers detach from both parent and spanners.'''

    staff = Staff(Container(notetools.make_repeated_notes(2)) * 2)
    pitchtools.set_ascending_named_diatonic_pitches_on_tie_chains_in_expr(staff)
    beam = spannertools.BeamSpanner(staff[:])

    r'''
    \new Staff {
        {
            c'8 [
            d'8
        }
        {
            e'8
            f'8 ]
        }
    }
    '''

    sequential = staff.pop()

    r'''
    \new Staff {
        {
            c'8 [
            d'8 ]
        }
    }
    '''

    assert testtools.compare(
        staff,
        r'''
        \new Staff {
            {
                c'8 [
                d'8 ]
            }
        }
        '''
        )
    assert select(staff).is_well_formed()

    r'''
    {
        e'8
        f'8
    }
    '''

    assert testtools.compare(
        sequential,
        r'''
        {
            e'8
            f'8
        }
        '''
        )
    assert select(sequential).is_well_formed()
