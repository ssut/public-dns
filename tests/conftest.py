import pytest

from publicdns.client import PublicDNS

@pytest.fixture
def client():
    return PublicDNS()

