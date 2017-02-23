from pytest import fixture, raises


@fixture
def patch_socket():
	from publicdns.monkey import patch_socket
	return patch_socket


def test_gethostbyname(patch_socket):
    patch_socket()
    import socket
    assert socket.gethostbyname('google-public-dns-a.google.com')


def test_gethostbyname_exception(patch_socket):
	patch_socket()
	import socket
	raises(socket.gaierror, socket.gethostbyname, '_')