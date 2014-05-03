# -*- encoding: utf-8 -*-
import pytest
pytest.skip('make me work')
import os
import shutil
from abjad import *
import scoremanager
score_manager = scoremanager.core.ScoreManager(is_test=True)


def test_SegmentPackageWrangler_make_package_01():
    r'''Makes score package.
    '''

    path = os.path.join(
        score_manager._configuration.user_score_packages_directory_path,
        'example_score',
        )
    directory_entries = [
        '__init__.py',
        '__metadata__.py',
        'build',
        'distribution',
        'makers',
        'materials',
        'segments',
        'stylesheets',
        ]

    assert not os.path.exists(path)
    try:
        input_ = 'new example~score q'
        score_manager._run(pending_user_input=input_)
        assert os.path.exists(path)
        session = scoremanager.core.Session(is_test=True)
        manager = scoremanager.managers.ScorePackageManager
        manager = manager(path=path, session=session)
        assert manager._list() == directory_entries
    finally:
        if os.path.exists(path):
            shutil.rmtree(path)
    assert not os.path.exists(path)