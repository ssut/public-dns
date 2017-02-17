import pytest


@pytest.fixture
def client():
    from publicdns.client import PublicDNS
    return PublicDNS()
