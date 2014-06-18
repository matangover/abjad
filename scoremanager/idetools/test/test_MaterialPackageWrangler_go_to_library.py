# -*- encoding: utf-8 -*-
from abjad import *
import scoremanager
score_manager = scoremanager.idetools.AbjadIDE(is_test=True)


def test_MaterialPackageWrangler_go_to_library_01():
    r'''From score materials to library.
    '''

    input_ = 'red~example~score m ** q'
    score_manager._run(input_=input_)
    titles = [
        'Abjad IDE - scores',
        'Red Example Score (2013)',
        'Red Example Score (2013) - materials',
        'Abjad IDE',
        ]
    assert score_manager._transcript.titles == titles


def test_MaterialPackageWrangler_go_to_library_02():
    r'''From all materials to library.
    '''

    input_ = 'M ** q'
    score_manager._run(input_=input_)
    titles = [
        'Abjad IDE - scores',
        'Abjad IDE - materials',
        'Abjad IDE',
        ]
    assert score_manager._transcript.titles == titles