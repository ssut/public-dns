from collections import namedtuple

DNSResponse = namedtuple('DNSResponse', ['status', 'TC', 'RD', 'RA', 'AD', 'CD',
                                         'question', 'answer', 'authority',
                                         'additional', 'edns_client_subnet',
                                         'comment'])

DNSQuestion = namedtuple('DNSQuestion', ['name', 'type'])

DNSRR = namedtuple('DNSRR', ['name', 'type', 'TTL', 'data'])

