RR = {
    'SIGZERO': 0,       # RFC2931 consider this a pseudo type
    'A': 1,       # RFC 1035, Section 3.4.1
    'NS': 2,       # RFC 1035, Section 3.3.11
    'MD': 3,       # RFC 1035, Section 3.3.4 (obsolete)
    'MF': 4,       # RFC 1035, Section 3.3.5 (obsolete)
    'CNAME': 5,       # RFC 1035, Section 3.3.1
    'SOA': 6,       # RFC 1035, Section 3.3.13
    'MB': 7,       # RFC 1035, Section 3.3.3
    'MG': 8,       # RFC 1035, Section 3.3.6
    'MR': 9,       # RFC 1035, Section 3.3.8
    'NULL': 10,      # RFC 1035, Section 3.3.10
    'WKS': 11,      # RFC 1035, Section 3.4.2 (deprecated)
    'PTR': 12,      # RFC 1035, Section 3.3.12
    'HINFO': 13,      # RFC 1035, Section 3.3.2
    'MINFO': 14,      # RFC 1035, Section 3.3.7
    'MX': 15,      # RFC 1035, Section 3.3.9
    'TXT': 16,      # RFC 1035, Section 3.3.14
    'RP': 17,      # RFC 1183, Section 2.2
    'AFSDB': 18,      # RFC 1183, Section 1
    'X25': 19,      # RFC 1183, Section 3.1
    'ISDN': 20,      # RFC 1183, Section 3.2
    'RT': 21,      # RFC 1183, Section 3.3
    'NSAP': 22,      # RFC 1706, Section 5
    'NSAP_PTR': 23,      # RFC 1348 (obsolete)
    'SIG': 24,      # RFC 2535, Section 4.1
    'KEY': 25,      # RFC 2535, Section 3.1
    'PX': 26,      # RFC 2163,
    'GPOS': 27,      # RFC 1712 (obsolete)
    'AAAA': 28,      # RFC 1886, Section 2.1
    'LOC': 29,      # RFC 1876
    'NXT': 30,      # RFC 2535, Section 5.2
    'EID': 31,      # draft-ietf-nimrod-dns-xx.txt
    'NIMLOC': 32,      # draft-ietf-nimrod-dns-xx.txt
    'SRV': 33,      # RFC 2052
    'ATMA': 34,      # ???
    'NAPTR': 35,      # RFC 2168
    'KX': 36,      # RFC 2230
    'CERT': 37,      # RFC 2538
    'DNAME': 39,      # RFC 2672
    'OPT': 41,      # RFC 2671
    'DS': 43,      # draft-ietf-dnsext-delegation-signer
    'SSHFP': 44,      # draft-ietf-secsh-dns (No RFC # yet at time of coding)
    'RRSIG': 46,      # draft-ietf-dnsext-dnssec-2535typecode-change
    'NSEC': 47,      # draft-ietf-dnsext-dnssec-2535typecode-change
    'DNSKEY': 48,      # draft-ietf-dnsext-dnssec-2535typecode-change
    'SPF': 99,      # RFC 4408
    'UINFO': 100,     # non-standard
    'UID': 101,     # non-standard
    'GID': 102,     # non-standard
    'UNSPEC': 103,     # non-standard
    'TKEY': 249,     # RFC 2930
    'TSIG': 250,     # RFC 2931
    'IXFR': 251,     # RFC 1995
    'AXFR': 252,     # RFC 1035
    'MAILB': 253,     # RFC 1035 (MB, MG, MR)
    'MAILA': 254,     # RFC 1035 (obsolete - see MX)
    'ANY': 255,     # RFC 1035
}


class StatusCode:
    (NOERROR, FORMERR, SERVFAIL, NXDOMAIN, NOTIME, REFUSED, YXDOMAIN,
     XRRSET, NOTAUTH, NOTZONE) = range(10)
