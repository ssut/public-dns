import requests
from hyper.contrib import HTTP20Adapter

DEFAULT_SERVER = 'https://dns.google.com/resolve'

class PublicDNS:
    def __init__(self, server=DEFAULT_SERVER, edns_client_subnet='0.0.0.0/0'):
        self.edns_client_subnet = edns_client_subnet

        self.session = requests.Session()
        self.session.mount(server, HTTP20Adapter())

    def resolve(self):
        pass


