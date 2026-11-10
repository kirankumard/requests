from __future__ import annotations

from http.cookiejar import DefaultCookiePolicy

import pytest

from requests.cookies import RequestsCookieJar, merge_cookies


@pytest.fixture
def target_jar_with_policy():
    policy = DefaultCookiePolicy(blocked_domains=["example.com"])
    jar = RequestsCookieJar()
    jar.policy = policy
    return jar


@pytest.fixture
def cookie_dict():
    return {"cookie_a": "val_a", "cookie_b": "val_b"}


@pytest.fixture
def source_jar():
    jar = RequestsCookieJar()
    jar.set("cookie_c", "val_c")
    return jar


@pytest.fixture
def invalid_cookiejar():
    return "not_a_cookie_jar"


def test_merge_cookies_dict_preserves_policy(target_jar_with_policy, cookie_dict):
    result = merge_cookies(target_jar_with_policy, cookie_dict)
    assert result.policy.blocked_domains == ("example.com",)
    assert result["cookie_a"] == "val_a"
    assert result["cookie_b"] == "val_b"


def test_merge_cookies_jar_preserves_policy(target_jar_with_policy, source_jar):
    result = merge_cookies(target_jar_with_policy, source_jar)
    assert result.policy.blocked_domains == ("example.com",)
    assert result["cookie_c"] == "val_c"


def test_merge_cookies_invalid_cookiejar_raises_valueerror(invalid_cookiejar):
    with pytest.raises(ValueError, match="You can only merge into CookieJar"):
        merge_cookies(invalid_cookiejar, {"cookie_a": "val_a"})
