# -*- encoding: utf-8 -*-
from abjad import *


def test_scoretools_Note___repr___01():
    r'''Note repr is evaluable.
    '''

    note_1 = Note("c'4")
    note_2 = eval(repr(note_1))

    assert isinstance(note_1, Note)
    assert isinstance(note_2, Note)
    assert note_1.lilypond_format == note_2.lilypond_format
    assert note_1 is not note_2
