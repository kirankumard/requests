from __future__ import annotations

import pytest


@pytest.fixture
def fx_001():
    return {"data": {"1": "a"}, "files": {"f": "b'x'"}}


@pytest.fixture
def fx_002():
    return {"files": {"1": "b'x'"}}


class TestPreparedRequest:
    
    def test_tc_001_encode_files(self, fx_001):
        pass
    
    def test_tc_002_encode_files(self, fx_002):
        pass
