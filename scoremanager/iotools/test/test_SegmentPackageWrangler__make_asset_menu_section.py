# -*- encoding: utf-8 -*-
from abjad import *
import scoremanager


def test_SegmentPackageWrangler__make_asset_menu_section_01():
    r'''Omits score annotation when listing segments in score.
    '''

    score_manager = scoremanager.iotools.AbjadIDE(is_test=True)
    input_ = 'red~example~score g q'
    score_manager._run(input_=input_)
    contents = score_manager._transcript.contents

    string = 'Red Example Score (2013) - segments'
    assert string in contents
    assert 'A\n' in contents