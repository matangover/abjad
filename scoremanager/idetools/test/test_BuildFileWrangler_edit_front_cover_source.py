# -*- encoding: utf-8 -*-
from abjad import *
import scoremanager
score_manager = scoremanager.idetools.AbjadIDE(is_test=True)


def test_BuildFileWrangler_edit_front_cover_source_01():

    input_ = 'red~example~score u fce q'
    score_manager._run(input_=input_)

    assert score_manager._session._attempted_to_open_file