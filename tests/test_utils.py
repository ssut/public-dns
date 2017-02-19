# coding=utf-8
"""unit tests for publicdns.utils
"""
from pytest import raises

from publicdns import exceptions as exc
from publicdns import utils


def test_get_netloc():
    url_http = 'http://www.google.com/'
    url_https = 'https://www.google.com/'
    assert utils.get_netloc(url_http) == 'www.google.com'
    assert utils.get_netloc(url_https) == 'www.google.com:443'


def test_build_qs():
    # while python 3.6 dict keywords become ordered, python 2.x doesn't.
    qs = utils.build_qs(dict(a=1, b=2, c='a'))
    assert 'a=1' in qs
    assert 'b=2' in qs
    assert 'c=a' in qs


def test_validate_hostname():
    assert raises(exc.InvalidHostname, utils.validate_hostname, '')
    assert raises(exc.InvalidHostname, utils.validate_hostname, '.' * 254)
    assert utils.validate_hostname(u'내도메인.한국')


def test_validate_rr_type():
    assert raises(exc.InvalidRRType, utils.validate_rr_type, 'EEE')
    assert raises(exc.InvalidRRType, utils.validate_rr_type, 65536)
    assert utils.validate_rr_type('A')
    assert utils.validate_rr_type(1)
