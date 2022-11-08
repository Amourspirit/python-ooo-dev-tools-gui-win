# coding: utf-8
import pytest
import tempfile
import os
import shutil
from pathlib import Path
from ooodev.utils.lo import Lo

# from ooodev.connect import connectors as mConnectors
from ooodev.conn.cache import Cache


@pytest.fixture(scope="session")
def tmp_path():
    result = Path(tempfile.mkdtemp())
    yield result
    if os.path.exists(result):
        shutil.rmtree(result, ignore_errors=True)


@pytest.fixture(scope="session")
def test_headless():
    return False


@pytest.fixture(scope="session")
def loader(tmp_path, test_headless):
    loader = Lo.load_office(connector=Lo.ConnectPipe(headless=test_headless), cache_obj=Cache(working_dir=tmp_path))
    # loader = Lo.load_office(connector=Lo.ConnectSocket(headless=True), cache_obj=Cache(working_dir=tmp_path))
    yield loader
    Lo.close_office()
