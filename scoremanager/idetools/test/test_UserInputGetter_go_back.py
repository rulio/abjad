# -*- encoding: utf-8 -*-
from abjad import *
import scoremanager
ide = scoremanager.idetools.AbjadIDE(is_test=True)


def test_UserInputGetter_go_back_01():
    r'''Back works.
    '''

    input_ = 'red~example~score m tempo~inventory da 1 d b q'
    ide._run(input_=input_)

    titles = [
        'Abjad IDE - scores',
        'Red Example Score (2013)',
        'Red Example Score (2013) - materials',
        'Red Example Score (2013) - materials - tempo inventory',
        'Red Example Score (2013) - materials - tempo inventory (EDIT)',
        'Red Example Score (2013) - materials - tempo inventory - tempo (EDIT)',
        'Red Example Score (2013) - materials - tempo inventory - tempo (EDIT)',
        ]
    assert ide._transcript.titles == titles