# -*- encoding: utf-8 -*-
import filecmp
import os
from abjad import *
import scoremanager
score_manager = scoremanager.iotools.AbjadIDE(is_test=True)


def test_BuildFileWrangler_generate_score_source_01():
    r'''Works when score source already exists.
    '''

    path = os.path.join(
        score_manager._configuration.example_score_packages_directory,
        'red_example_score',
        'build',
        'score.tex',
        )

    with systemtools.FilesystemState(keep=[path]):
        input_ = 'red~example~score u sg y q'
        score_manager._run(input_=input_)
        assert os.path.isfile(path)
        assert filecmp.cmp(path, path + '.backup')