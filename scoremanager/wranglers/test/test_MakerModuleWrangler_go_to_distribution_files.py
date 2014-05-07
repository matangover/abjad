# -*- encoding: utf-8 -*-
from abjad import *
import scoremanager
score_manager = scoremanager.core.ScoreManager(is_test=True)


def test_MakerModuleWrangler_go_to_distribution_files_01():
    r'''From makers directory to distribution directory.
    '''

    input_ = 'red~example~score k d q'
    score_manager._run(pending_input=input_)
    titles = [
        'Score manager - example scores',
        'Red Example Score (2013)',
        'Red Example Score (2013) - maker modules',
        'Red Example Score (2013) - distribution files',
        ]
    assert score_manager._transcript.titles == titles