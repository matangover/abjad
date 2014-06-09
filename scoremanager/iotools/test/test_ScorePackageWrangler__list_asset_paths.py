# -*- encoding: utf-8 -*-
import os
from abjad import *
import scoremanager
session = scoremanager.iotools.Session(is_test=True)


def test_ScorePackageWrangler__list_asset_paths_01():
    r'''Lists example score packages.
    '''

    wrangler = scoremanager.iotools.ScorePackageWrangler(session=session)
    result = wrangler._list_asset_paths(
        abjad_library=False,
        example_score_packages=True,
        user_library=False,
        user_score_packages=False,
        )

    package_names = [
        'blue_example_score',
        'etude_example_score',
        'red_example_score',
        ]
    paths = []
    for package_name in package_names:
        path = os.path.join(
            wrangler._configuration.example_score_packages_directory,
            package_name,
            )
        paths.append(path)
    assert result == paths