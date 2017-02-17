import collections

DNSResponse = collections.namedtuple('DNSResponse', [
    'status',
    'TC', 'RD', 'RA', 'AD', 'CD',
    'question', 'answer', 'authority',
    'additional', 'edns_client_subnet',
    'comment'])

DNSQuestion = collections.namedtuple('DNSQuestion', ['name', 'type'])

DNSRR = collections.namedtuple('DNSRR', ['name', 'type', 'TTL', 'data'])
