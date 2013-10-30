# -*- encoding: utf-8 -*-
from abjad import *
from abjad.tools.marktools.TempoMark import TempoMark
from experimental import *


def test_TempoMarkInventoryEditor_run_01():

    editor = scoremanagertools.editors.TempoMarkInventoryEditor()
    editor._run(pending_user_input='q')
    assert editor.target == marktools.TempoMarkInventory([])


def test_TempoMarkInventoryEditor_run_02():

    editor = scoremanagertools.editors.TempoMarkInventoryEditor()
    editor._run(pending_user_input='add ((1, 4), 60) add ((1, 4), 72) add ((1, 4), 84) q')
    assert editor.target == marktools.TempoMarkInventory(
        [TempoMark(Duration(1, 4), 60), TempoMark(Duration(1, 4), 72), TempoMark(Duration(1, 4), 84)])
