# -*- encoding: utf-8 -*-
from abjad import *
import scoremanager
ide = scoremanager.idetools.AbjadIDE(is_test=True)


def test_MakerFileWrangler_go_to_previous_score_01():

    input_ = 'red~example~score k << q'
    ide._run(input_=input_)

    titles = [
        'Abjad IDE - scores',
        'Red Example Score (2013)',
        'Red Example Score (2013) - maker files',
        'Étude Example Score (2013)',
        ]
    assert ide._transcript.titles == titles


def test_MakerFileWrangler_go_to_previous_score_02():

    input_ = 'K << q'
    ide._run(input_=input_)

    titles = [
        'Abjad IDE - scores',
        'Abjad IDE - maker files',
        'Red Example Score (2013)',
        ]
    assert ide._transcript.titles == titles