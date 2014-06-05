# -*- encoding: utf-8 -*-
import os
import shutil
from abjad import *
import scoremanager
score_manager = scoremanager.core.AbjadIDE(is_test=True)


def test_SegmentPackageManager_check_package_01():
    r'''Displays problems only.
    '''

    segment_directory = os.path.join(
        score_manager._configuration.example_score_packages_directory,
        'red_example_score',
        'segments',
        'segment_02',
        )
    versions_directory = os.path.join(segment_directory, 'versions')
    initializer = os.path.join(segment_directory, '__init__.py')

    with systemtools.FilesystemState(keep=[versions_directory, initializer]):
        os.remove(initializer)
        shutil.rmtree(versions_directory)
        input_ = 'red~example~score g B ck y q'
        score_manager._run(input_=input_)
        contents = score_manager._transcript.contents

    lines = [
        '1 of 1 required directory missing:',
        '1 of 2 required files missing:',
        ]
    for line in lines:
        assert line in contents
    assert 'optional directories' not in contents
    assert 'optional files' not in contents


def test_SegmentPackageManager_check_package_02():
    r'''Displays everything.
    '''

    segment_directory = os.path.join(
        score_manager._configuration.example_score_packages_directory,
        'red_example_score',
        'segments',
        'segment_02',
        )
    versions_directory = os.path.join(segment_directory, 'versions')
    initializer = os.path.join(segment_directory, '__init__.py')

    with systemtools.FilesystemState(keep=[versions_directory, initializer]):
        os.remove(initializer)
        shutil.rmtree(versions_directory)
        input_ = 'red~example~score g B ck n q'
        score_manager._run(input_=input_)
        contents = score_manager._transcript.contents

    lines = [
        '1 of 1 required directory missing:',
        '1 of 2 required files found:',
        '1 of 2 required files missing:',
        '4 optional files found:',
        ]
    for line in lines:
        assert line in contents