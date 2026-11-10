from __future__ import annotations

import pytest


@pytest.fixture
def fx_001():
    return {"policy_type": "DefaultCookiePolicy", "blocked_domains": ["example.com"]}


@pytest.fixture
def fx_002():
    return {"cookies": {"cookie_a": "val_a", "cookie_b": "val_b"}}


@pytest.fixture
def fx_003():
    return {"cookies": {"cookie_c": "val_c"}}


@pytest.fixture
def fx_004():
    return {"invalid_cookiejar": "not_a_cookie_jar"}


class Testmerge_cookies:
    
    def test_tc_001_merge_cookies(self, fx_001, fx_002):
        pass
    
    def test_tc_002_merge_cookies(self, fx_001, fx_003):
        pass
    
    def test_tc_003_merge_cookies(self, fx_004):
        pass
