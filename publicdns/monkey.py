from socket import gaierror
from publicdns.client import PublicDNS
from publicdns.exceptions import NXDomain


client = PublicDNS()


def _gethostbyname(hostname):
    try:
        return client.resolve(hostname)[0]
    except NXDomain:
        raise gaierror('[Errno 8] nodename nor servname provided, or not known')


def patch_socket():
    module = __import__('socket')
    setattr(module, 'gethostbyname', _gethostbyname)