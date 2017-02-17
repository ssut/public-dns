
def test_gethostbyname():
    from publicdns.monkey import patch_socket
    patch_socket()
    import socket
    assert socket.gethostbyname('google-public-dns-a.google.com')

