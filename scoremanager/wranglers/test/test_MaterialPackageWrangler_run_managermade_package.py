# -*- encoding: utf-8 -*-
import os
import shutil
from abjad import *
import scoremanager


def test_MaterialPackageWrangler_run_managermade_package_01():
    r'''Make managermade package. Delete package.
    '''

    score_manager = scoremanager.core.ScoreManager(is_test=True)
    path = os.path.join(
        score_manager._configuration.user_library_material_packages_directory_path,
        'testsargasso',
        )
    input_ = 'lmm nmm sargasso testsargasso default q'
    directory_entries = [
        '__init__.py', 
        '__metadata__.py',
        'user_input.py',
        ]

    assert not os.path.exists(path)
    try:
        score_manager._run(pending_user_input=input_)
        assert os.path.exists(path)
        session = scoremanager.core.Session(is_test=True)
        manager = scoremanager.managers.SargassoMeasureMaterialManager
        manager = manager(path=path, session=session)
        assert manager._list() == directory_entries
        input_ = 'lmm testsargasso rm remove q'
        score_manager._run(pending_user_input=input_)
    finally:
        if os.path.exists(path):
            shutil.rmtree(path)
    assert not os.path.exists(path)


def test_MaterialPackageWrangler_run_managermade_package_02():
    r'''Make score-resident managermade package. Delete package.
    '''

    score_manager = scoremanager.core.ScoreManager(is_test=True)
    path = os.path.join(
        score_manager._configuration.abjad_score_packages_directory_path,
        'red_example_score',
        'materials',
        'testsargasso',
        )
    input_ = 'red~example~score m nmm sargasso testsargasso default q'
    directory_entries = [
        '__init__.py', 
        '__metadata__.py',
        'user_input.py',
        ]

    assert not os.path.exists(path)
    try:
        score_manager._run(pending_user_input=input_)
        assert os.path.exists(path)
        session = scoremanager.core.Session(is_test=True)
        manager = scoremanager.managers.SargassoMeasureMaterialManager
        manager = manager(path=path, session=session)
        assert manager._list() == directory_entries
        input_ = 'red~example~score m testsargasso rm remove q'
        score_manager._run(pending_user_input=input_)
    finally:
        if os.path.exists(path):
            shutil.rmtree(path)
    assert not os.path.exists(path)


def test_MaterialPackageWrangler_run_managermade_package_03():
    r'''Make managermade package. Corrupt initializer.
    Verify invalid initializer. Remove package.
    '''

    score_manager = scoremanager.core.ScoreManager(is_test=True)
    path = os.path.join(
        score_manager._configuration.user_library_material_packages_directory_path,
        'testsargassomeasures',
        )
    input_ = 'lmm nmm sargasso testsargassomeasures'
    input_ += ' testsargassomeasures inbp boilerplate_exception.py default q'
    directory_entries = [
        '__init__.py', 
        '__metadata__.py',
        'user_input.py',
        ]

    assert not os.path.exists(path)
    try:
        score_manager._run(pending_user_input=input_)
        assert os.path.exists(path)
        session = scoremanager.core.Session(is_test=True)
        manager = scoremanager.managers.SargassoMeasureMaterialManager
        manager = manager(path=path, session=session)
        assert manager._list() == directory_entries
        assert manager._interpret_definition_module() is None
        assert manager._execute_output_module() is None
        input_ = 'lmm testsargassomeasures rm remove q'
        score_manager._run(pending_user_input=input_)
    finally:
        if os.path.exists(path):
            shutil.rmtree(path)
    assert not os.path.exists(path)


def test_MaterialPackageWrangler_run_managermade_package_04():
    r'''Make managermade package. Corrupt initializer. Restore initializer.
    Verify initializer. Remove package.
    '''

    score_manager = scoremanager.core.ScoreManager(is_test=True)
    path = os.path.join(
        score_manager._configuration.user_library_material_packages_directory_path,
        'testsargassomeasures',
        )
    input_ = 'lmm nmm sargasso testsargassomeasures'
    input_ += ' me inbp boilerplate_exception.py default'
    input_ += ' ins default q'
    directory_entries = [
        '__init__.py', 
        '__metadata__.py',
        'user_input.py',
        ]

    assert not os.path.exists(path)
    try:
        score_manager._run(pending_user_input=input_)
        assert os.path.exists(path)
        session = scoremanager.core.Session(is_test=True)
        manager = scoremanager.managers.SargassoMeasureMaterialManager
        manager = manager(path=path, session=session)
        assert manager._list() == directory_entries
        assert manager._interpret_definition_module() is None
        assert manager._execute_output_module() is None
        input_ = 'lmm testsargassomeasures rm remove q'
        score_manager._run(pending_user_input=input_)
    finally:
        if os.path.exists(path):
            shutil.rmtree(path)
    assert not os.path.exists(path)
