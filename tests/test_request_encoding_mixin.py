from __future__ import annotations

import pytest
from requests.models import RequestEncodingMixin


class TestRequestEncodingMixin:

    def test_tc_001_encode_files(self):
        body, content_type = RequestEncodingMixin._encode_files(files={123: ('test.txt', b'content')}, data=None)
        assert isinstance(body, bytes)
        assert isinstance(content_type, str)

    def test_tc_002_encode_files(self):
        body, content_type = RequestEncodingMixin._encode_files(files={'file': ('test.txt', b'content')}, data={456: 'field_value'})
        assert isinstance(body, bytes)
        assert isinstance(content_type, str)

    def test_tc_003_encode_files(self):
        body, content_type = RequestEncodingMixin._encode_files(files={'file': ('test.txt', b'content')}, data={b'key': 'value'})
        assert isinstance(body, bytes)
        assert isinstance(content_type, str)

    def test_tc_004_encode_files(self):
        body, content_type = RequestEncodingMixin._encode_files(files=[(100, ('test.txt', b'content'))], data=[(object(), 'val')])
        assert isinstance(body, bytes)
        assert isinstance(content_type, str)
