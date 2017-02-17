from pytest import fixture


@fixture
def client():
    from publicdns.client import PublicDNS
    return PublicDNS()
