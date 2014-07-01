# -*- encoding: utf-8 -*-
from abjad import *
import scoremanager
ide = scoremanager.idetools.AbjadIDE(is_test=True)


def test_MaterialPackageWrangler_open_lilypond_log_01():
    r'''In score.
    '''

    input_ = 'red~example~score m ll q'
    ide._run(input_=input_)
    
    assert ide._session._attempted_to_open_file


def test_MaterialPackageWrangler_open_lilypond_log_02():
    r'''Out of score.
    '''

    input_ = 'M ll q'
    ide._run(input_=input_)
    
    assert ide._session._attempted_to_open_file