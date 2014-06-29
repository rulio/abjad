# -*- encoding: utf-8 -*-
from abjad import *
import scoremanager
ide = scoremanager.idetools.AbjadIDE(is_test=True)


def test_ScorePackageWrangler_go_to_all_segments_01():
    r'''From all scores to all segments.
    '''

    input_ = 'G q'
    ide._run(input_=input_)
    titles = [
        'Abjad IDE - scores',
        'Abjad IDE - segments',
        ]
    assert ide._transcript.titles == titles