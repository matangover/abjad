# -*- encoding: utf-8 -*-
import os
from abjad import *
import scoremanager
score_manager = scoremanager.core.ScoreManager(is_test=True)


def test_MakerFileWrangler_invoke_shell_01():
    r'''Outside of score package.
    '''

    input_ = 'k !pwd q'
    score_manager._run(pending_input=input_)

    path = os.path.join(
        score_manager._configuration.score_manager_directory_path,
        )
    string = '\n{}\n'.format(path)
    assert string in score_manager._transcript.contents


def test_MakerFileWrangler_invoke_shell_02():
    r'''Inside score package.
    '''

    input_ = 'red~example~score k !pwd q'
    score_manager._run(pending_input=input_)

    path = os.path.join(
        score_manager._configuration.example_score_packages_directory_path,
        'red_example_score',
        'makers',
        )
    string = '\n{}\n'.format(path)
    assert string in score_manager._transcript.contents