class InvalidHostname(Exception):
    pass


class InvalidRRType(Exception):
    pass


class InvalidHTTPStatusCode(Exception):
    pass


class DNSException(Exception):
    pass


class FormErr(DNSException):
    """DNS query format error
    """
    code = 1


class ServFail(DNSException):
    """Server failed to complete the DNS request
    """
    code = 2


class NXDomain(DNSException):
    """Domain name does not exist
    """
    code = 3


class NotImpl(DNSException):
    """Function not implemented
    """
    code = 4


class Refused(DNSException):
    """The server refused to answer for the reply
    """
    code = 5


class YXDomain(DNSException):
    """Name that should not exist, does exist
    """
    code = 6


class XRRSet(DNSException):
    """RRset that should not exist, does exist
    """
    code = 7


class NotAuth(DNSException):
    """Server not authoritative for the zone
    """
    code = 8


class NotZone(DNSException):
    """Name not in zone
    """
    code = 9


DNSExceptions = (
    FormErr,
    ServFail,
    NXDomain,
    NotImpl,
    Refused,
    YXDomain,
    XRRSet,
    NotAuth,
    NotZone,
)
