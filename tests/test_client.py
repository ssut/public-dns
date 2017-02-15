import pytest
import ipaddress

from publicdns.client import PublicDNS

def test_client():
    client = PublicDNS()
    resp = client.resolve('google-public-dns-a.google.com')
    assert set(resp).intersection([ipaddress.IPv4Address('8.8.8.8')])


