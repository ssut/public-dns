from pytest import raises
from publicdns.exceptions import InvalidHTTPStatusCode


def test_client_invalid_status():
	from publicdns.client import PublicDNS
	client = PublicDNS(server='https://www.google.com')
	assert raises(InvalidHTTPStatusCode, client.resolve, 'www.google.com')


def test_client_resolve_a(client):
    resp = client.resolve('google-public-dns-a.google.com')
    assert set(resp).intersection(['8.8.8.8'])


def test_client_resolve_a_roundrobin(client):
    resp = client.resolve('www.naver.com')
    assert len(resp) == 1


def test_client_dns_error(client):
    from publicdns.exceptions import NXDomain
    with raises(NXDomain):
        client.resolve('domain.that.does.not.exist')


def test_client_resolve_ptr(client):
    resp = client.resolve('8.8.8.8', type='PTR')
    assert set(resp).intersection(['dns.google.'])
