# -*- encoding: utf-8 -*-
from abjad import *
import scoremanager
ide = scoremanager.idetools.AbjadIDE(is_test=True)


def test_BuildFileWrangler_open_music_pdf_01():

    input_ = 'red~example~score u mo q'
    ide._run(input_=input_)

    assert ide._session._attempted_to_open_file