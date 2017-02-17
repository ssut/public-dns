from __future__ import unicode_literals

from idna import encode as encode_idna
from six.moves.urllib.parse import urlencode, urlparse

from publicdns._compat import PY3
from publicdns.exceptions import DNSExceptions
from publicdns.exceptions import InvalidHostname, InvalidRRType
from publicdns.models import (
    DNSRR, DNSResponse, DNSQuestion
)
from publicdns.types import RR


def get_netloc(url):
    o = urlparse(url)
    if o.scheme == 'https':
        return '%s:443' % (o.netloc)
    else:
        return o.netloc


def build_qs(params):
    return urlencode(params)


def validate_hostname(hostname):
    hostname = hostname.rstrip('.')

    if not(1 <= len(hostname) <= 253):
        raise InvalidHostname
    for label in hostname.split('.'):
        if not(1 <= len(label) <= 63):
            raise InvalidHostname
    try:
        hostname.encode('ascii')
    except UnicodeEncodeError:
        hostname = encode_idna(hostname)
        if PY3:
            hostname = hostname.decode()
        return validate_hostname(hostname)

    return True


def validate_rr_type(rr):
    if isinstance(rr, int) and not (1 <= rr <= 65535):
        raise InvalidRRType

    canonicals = RR.keys()
    if rr.upper() not in canonicals:
        raise InvalidRRType

    return True


def populate_response(json):
    questions = json.get('Question', [])
    records = {}

    questions = [DNSQuestion(
        name=q.get('name', ''),
        type=q.get('type', ''))
        for q in questions]
    for name in ('Answer', 'Authority', 'Additional'):
        record = [DNSRR(
            name=r.get('name', ''),
            type=r.get('type', ''),
            TTL=r.get('TTL', ''),
            data=r.get('data', ''))
            for r in json.get(name, [])]
        records[name] = record

    resp = DNSResponse(
        status=int(json['Status']),
        TC=bool(json['TC']),
        RD=bool(json['RD']),
        RA=bool(json['RA']),
        AD=bool(json['AD']),
        CD=bool(json['CD']),
        question=questions,
        answer=records['Answer'],
        authority=records['Authority'],
        additional=records['Additional'],
        edns_client_subnet=json.get('edns_client_subnet', None),
        comment=json.get('comment', ''))
    return resp


def dns_exception(resp):
    code = resp.status
    assert 1 <= code <= 9

    exception = DNSExceptions[code - 1]
    status = resp.comment or exception.__doc__
    return exception(status)
