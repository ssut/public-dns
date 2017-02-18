def test_client_resolve_a(client):
    resp = client.resolve('google-public-dns-a.google.com')
    assert set(resp).intersection(['8.8.8.8'])


def test_client_resolve_a_roundrobin(client):
    resp = client.resolve('www.naver.com')
    assert len(resp) == 2


def test_client_resolve_ptr(client):
    resp = client.resolve('8.8.8.8', type='PTR')
    assert set(resp).intersection(['google-public-dns-a.google.com.'])
