# -*- encoding: utf-8 -*-
from abjad import *
import scoremanager
ide = scoremanager.idetools.AbjadIDE(is_test=True)


def test_SegmentPackageManager_pytest_01():

    input_ = 'red~example~score g A pt q'
    ide._run(input_=input_)
    transcript_contents = ide._transcript.contents

    strings = [
        'Running py.test ...',
        'No testable assets found.',
        ]

    for string in strings:
        assert string in transcript_contents