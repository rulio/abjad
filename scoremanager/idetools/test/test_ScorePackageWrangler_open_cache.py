# -*- encoding: utf-8 -*-
from abjad import *
import scoremanager


def test_ScorePackageWrangler_open_cache_01():

    ide = scoremanager.idetools.AbjadIDE(is_test=True)
    input_ = 'co q'
    ide._run(input_=input_)

    assert ide._session._attempted_to_open_file