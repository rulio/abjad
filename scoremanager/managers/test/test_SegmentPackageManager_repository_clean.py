# -*- encoding: utf-8 -*-
import os
from abjad import *
import scoremanager
score_manager = scoremanager.core.ScoreManager(is_test=True)


def test_SegmentPackageManager_repository_clean_01():

    foo_path = os.path.join(
        score_manager._configuration.example_score_packages_directory,
        'red_example_score',
        'segments',
        'segment_01',
        'test_foo.txt',
        )

    with systemtools.FilesystemState(remove=[foo_path]):
        with open(foo_path, 'w') as file_pointer:
            file_pointer.write('')
        assert os.path.isfile(foo_path)
        input_ = 'red~example~score g A rcn y q'
        score_manager._run(pending_input=input_)
        assert not os.path.exists(foo_path)