from publicdns.client import PublicDNS

client = PublicDNS()


def _gethostbyname(hostname):
    try:
        return client.resolve(hostname)[0]
    except Exception:
        return '0.0.0.0'


def patch_socket():
    module = __import__('socket')
    setattr(module, 'gethostbyname', _gethostbyname)
