from httpx import Client
from ujson import loads as load_json

from publicdns import utils
from publicdns.exceptions import InvalidHTTPStatusCode
from publicdns.types import RR, StatusCode

DEFAULT_SERVER = 'https://dns.google.com/resolve'


class PublicDNS(object):

    default_headers = {
        'accept-encoding': 'gzip, deflate',
    }

    def __init__(self, server=DEFAULT_SERVER, edns_client_subnet='0.0.0.0/0'):
        self.server = server
        self.edns_client_subnet = edns_client_subnet

        self.session = Client(http2=True)

    def query(self, hostname, type='A', dnssec=True):
        assert utils.validate_hostname(hostname)
        assert utils.validate_rr_type(type)

        if (type in ('PTR', RR['PTR']) and
            not (hostname.endswith('.in-addr.arpa') or
                 hostname.endswith('.in-addr.arpa.'))):
            hostname = '%s.in-addr.arpa' % (hostname)

        params = self.build_params(hostname, type, dnssec)
        url = '%s?%s' % (self.server, params)
        resp = self.session.get(url, headers=PublicDNS.default_headers)
        if resp.status_code != 200:
            raise InvalidHTTPStatusCode(
                '{} {}: {}'.format(resp.status_code, resp.reason, url))
        body = resp.content
        try:
            json = load_json(body)
        except ValueError as e:
            raise InvalidHTTPStatusCode(e)
        obj = utils.populate_response(json)
        return obj

    def resolve(self, hostname, type='A', dnssec=True):
        resp = self.query(hostname, type, dnssec)
        if resp.status != StatusCode.NOERROR:
            raise utils.dns_exception(resp)
        data = [r.data for r in resp.answer
                if r.type in (type, RR[type]) and r.data]
        return data

    def build_params(self, hostname, type, dnssec):
        params = {
            'name': hostname,
            'type': type,
            'cd': int(not dnssec),
            'edns_client_subnet': self.edns_client_subnet,
        }
        return utils.build_qs(params)
