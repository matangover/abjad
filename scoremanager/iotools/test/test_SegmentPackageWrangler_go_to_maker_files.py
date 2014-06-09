# -*- encoding: utf-8 -*-
from abjad import *
import scoremanager
score_manager = scoremanager.iotools.AbjadIDE(is_test=True)


def test_SegmentPackageWrangler_go_to_maker_files_01():
    r'''From segments directory to makers directory.
    '''

    input_ = 'red~example~score g k q'
    score_manager._run(input_=input_)
    titles = [
        'Abjad IDE - scores',
        'Red Example Score (2013)',
        'Red Example Score (2013) - segments',
        'Red Example Score (2013) - maker files',
        ]
    assert score_manager._transcript.titles == titles