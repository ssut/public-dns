import idna

from urllib.parse import urlencode
from collections import OrderedDict

def build_qs(params):
    return urlencode(params)

def validate_hostname(hostname):
    hostname = hostname.rstrip('.')

    if not(1 <= len(hostname) <= 253):
        return False

    for label in hostname.split('.'):
	if not(1 <= len(label) <= 63):
            return False
    try:
	hostname.encode('ascii')
    except UnicodeEncodeError:
        return validate_hostname(idna.encode(hostname))

    return True

