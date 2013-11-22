# -*- encoding: utf-8 -*-
import pytest
from abjad import *


def test_agenttools_InspectionAgent_get_mark_01():

    note = Note("c'8")
    annotation = indicatortools.Annotation('special information')
    attach(annotation, note)

    assert inspect(note).get_indicator(indicatortools.Annotation) is annotation


def test_agenttools_InspectionAgent_get_mark_02():

    note = Note("c'8")

    statement = 'inspect(note).get_indicator(indicatortools.Annotation)'
    assert pytest.raises(Exception, statement)


def test_agenttools_InspectionAgent_get_mark_03():

    note = Note("c'8")
    annotation = indicatortools.Annotation('special information')
    attach(annotation, note)
    annotation = indicatortools.Annotation('more special information')
    attach(annotation, note)

    statement = 'inspect(note).get_indicator(indicatortools.Annotation)',
    assert pytest.raises(Exception, statement)


def test_agenttools_InspectionAgent_get_mark_04():

    note = Note("c'8")
    articulation = Articulation('staccato')
    attach(articulation, note)

    assert inspect(note).get_indicator(Articulation) is articulation


def test_agenttools_InspectionAgent_get_mark_05():

    note = Note("c'8")

    statement = 'inspect(note).get_indicator(Articulation)',
    assert pytest.raises(Exception, statement)


def test_agenttools_InspectionAgent_get_mark_06():

    note = Note("c'8")
    articulation = Articulation('staccato')
    attach(articulation, note)
    articulation = Articulation('marcato')
    attach(articulation, note)

    statement = 'inspect(note).get_indicator(Articulation)',
    assert pytest.raises(Exception, statement)


def test_agenttools_InspectionAgent_get_mark_07():

    note = Note("c'8")
    command = indicatortools.LilyPondCommand('stemUp')
    attach(command, note)

    assert inspect(note).get_indicator(indicatortools.LilyPondCommand) is command


def test_agenttools_InspectionAgent_get_mark_08():

    note = Note("c'8")

    statement = 'inspect(note).get_indicator(indicatortools.LilyPondCommand)'
    assert pytest.raises(Exception, statement)


def test_agenttools_InspectionAgent_get_mark_09():

    note = Note("c'8")
    command = indicatortools.LilyPondCommand('stemUp')
    attach(command, note)
    command = indicatortools.LilyPondCommand('slurUp')
    attach(command, note)

    statement = 'inspect(note).get_indicator(indicatortools.LilyPondCommand)'
    assert pytest.raises(Exception, statement)


def test_agenttools_InspectionAgent_get_mark_10():

    staff = Staff("c'8 d'8 e'8 f'8")
    slur = Slur()
    attach(slur, staff.select_leaves())
    command_1 = indicatortools.LilyPondCommand('slurDotted')
    attach(command_1, staff[0])
    command_2 = indicatortools.LilyPondCommand('slurUp')
    attach(command_2, staff[0])

    assert systemtools.TestManager.compare(
        staff,
        r'''
        \new Staff {
            \slurDotted
            \slurUp
            c'8 (
            d'8
            e'8
            f'8 )
        }
        '''
        )

    marks = inspect(staff[0]).get_indicators(indicatortools.LilyPondCommand)

    assert command_1 in marks
    assert command_2 in marks
    assert len(marks) == 2


def test_agenttools_InspectionAgent_get_mark_11():

    note = Note("c'8")
    comment = indicatortools.LilyPondComment('comment')
    attach(comment, note)

    indicator = inspect(note).get_indicator(indicatortools.LilyPondComment) 
    assert indicator is comment


def test_agenttools_InspectionAgent_get_mark_12():

    note = Note("c'8")

    statement = 'inspect(note).get_indicator(indicatortools.LilyPondComment)'
    assert pytest.raises(Exception, statement)


def test_agenttools_InspectionAgent_get_mark_13():

    note = Note("c'8")
    comment = indicatortools.LilyPondComment('comment')
    attach(comment, note)
    comment = indicatortools.LilyPondComment('another comment')
    attach(comment, note)

    statement = 'inspect(note).get_indicator(indicatortools.LilyPondComment)'
    assert pytest.raises(Exception, statement)


def test_agenttools_InspectionAgent_get_mark_14():

    note = Note("c'8")

    assert pytest.raises(Exception, 'inspect(note).get_indicator()')


def test_agenttools_InspectionAgent_get_mark_15():

    note = Note("c'4")
    stem_tremolo = indicatortools.StemTremolo(16)
    attach(stem_tremolo, note)
    stem_tremolo = inspect(note).get_indicator(indicatortools.StemTremolo)

    assert stem_tremolo is stem_tremolo


def test_agenttools_InspectionAgent_get_mark_16():

    staff = Staff("c'8 d'8 e'8 f'8")
    violin = instrumenttools.Violin()
    attach(violin, staff)

    wrapper = inspect(staff).get_indicator(instrumenttools.Instrument)

    assert wrapper.indicator is violin


def test_agenttools_InspectionAgent_get_mark_17():

    measure = Measure((4, 8), "c'8 d'8 e'8 f'8")
    wrapper = inspect(measure).get_indicator(TimeSignature)
    time_signature = wrapper.indicator

    assert time_signature == TimeSignature((4, 8))