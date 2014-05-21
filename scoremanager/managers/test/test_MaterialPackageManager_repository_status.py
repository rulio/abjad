# -*- encoding: utf-8 -*-
from abjad import *
import scoremanager
score_manager = scoremanager.core.ScoreManager(is_test=True)


def test_MaterialPackageManager_repository_status_01():
    r'''Works with Git.
    '''

    input_ = 'red~example~score m rst q'
    score_manager._run(pending_input=input_)
    string = 'On branch master'

    assert string in score_manager._transcript.titles
    assert score_manager._session.proceed_count == 0


def test_MaterialPackageManager_repository_status_02():
    r'''Works with Subversion.
    '''

    wrangler = score_manager._material_package_wrangler
    manager = wrangler._find_svn_manager()
    if not manager:
        return

    manager.repository_status()
    titles = manager._transcript.titles

    assert titles[0].endswith('...')
    assert len(titles) == 1
    assert score_manager._session.proceed_count == 0