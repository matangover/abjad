# -*- encoding: utf-8 -*-
from abjad import *
import scoremanager
score_manager = scoremanager.core.ScoreManager(is_test=True)


def test_DistributionFileWrangler_display_available_commands_01():
    
    input_ = 'red~example~score d ? q'
    score_manager._run(pending_input=input_)
    contents = score_manager._transcript.contents

    assert 'distribution files - available commands' in contents


def test_DistributionFileWrangler_display_available_commands_02():
    
    input_ = 'd ? q'
    score_manager._run(pending_input=input_)
    contents = score_manager._transcript.contents

    string = 'Score manager - distribution files - available commands'
    assert string in contents