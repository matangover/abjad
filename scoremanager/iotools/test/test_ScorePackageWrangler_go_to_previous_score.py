# -*- encoding: utf-8 -*-
from abjad import *
import scoremanager


def test_ScorePackageWrangler_go_to_previous_score_01():

    score_manager = scoremanager.iotools.AbjadIDE(is_test=True)
    input_ = '<< << q'
    score_manager._run(input_=input_)
    titles = [
        'Abjad IDE - scores',
        'Red Example Score (2013)',
        'Étude Example Score (2013)',
        ]
    assert score_manager._transcript.titles == titles