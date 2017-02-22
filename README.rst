=========
PublicDNS
=========

    .. image:: https://codeclimate.com/github/ssut/public-dns/badges/gpa.svg
       :target: https://codeclimate.com/github/ssut/public-dns
       :alt: Code Climate
    .. image:: https://travis-ci.org/ssut/public-dns.svg?branch=master
       :target: https://travis-ci.org/ssut/public-dns
    .. image:: https://coveralls.io/repos/github/ssut/public-dns/badge.svg?branch=master
       :target: https://coveralls.io/github/ssut/public-dns?branch=master
    .. image:: https://badge.fury.io/py/publicdns.svg
       :target: https://badge.fury.io/py/publicdns
    .. image:: https://img.shields.io/github/license/mashape/apistatus.svg
       :target: http://opensource.org/licenses/MIT

PublicDNS is a high-perfmrnace, secure, reliable python DNS client `over HTTP/2 and TLS`__.

__ https://developers.google.com/speed/public-dns/docs/dns-over-https

As written in Google DNS-over-HTTPS guide, this offers a variety of features as follows:

- support all RRs
- support DNSSEC validation
- support for IPv4 and IPv6
- support `edns-client-subnet`__
- can insure against `privacy concerns`__
    - ISPs will not able to track which DNS names you have queried

__ https://datatracker.ietf.org/doc/rfc7871/
__ https://https.cio.gov/everything/

Performance
===========

While tranditional DNS client does not support `put multiple questions into a single call`__,
PublicDNS has advantage that it's much faster when dealing with multiple questions, `a big advantage of HTTP/2`__.
Because Google servers also run over QUIC, this means that performance will be much better if it is implemented.

I recently benchmarked with a small amount of domains, take a look at the result:

    .. code-block:: console

       - dns.resolver
       100%|███| 100/100 [00:32<00:00, 3.97s/it]
       dns.resolver * 100 - took 32.5060371872969s
       - PublicDNS
       100%|███| 100/100 [00:13<00:00, 12.8it/s]
       PublicDNS * 100 - took 13.507565873209387s

Note that results will vary depend on the network since most dns servers use `IP Anycast`__. Further,
PublicDNS needs only one TCP connection as did in the benchmark, whereas traditional clients will need to establish
multiple TCP or UDP connections.

__ https://groups.google.com/d/msg/comp.protocols.dns.bind/uOWxNkm7AVg/wKtsmudkY1UJ
__ https://istlsfastyet.com/#faq
__ https://developers.google.com/speed/public-dns/faq#locations

Installation
============

Install PublicDNS using easy_setup or pip:

    .. code-block:: console

       pip install publicdns

Example
=======

    .. code-block:: python

       from publicdns.client import PublicDNS

       client = PublicDNS()
       result = client.query('www.google.com', 'A')
       ip = client.resolve('www.google.com')

To see more usage, just dive into the ``tests`` directory.

API
===

The public API is really simple, totaling only 2 API calls:

* ``query(host, type='A', dnssec=True)``: Do a DNS resolution of the given type for the given hostname. It returns an
  instance of ``publicdns.models.DNSResponse``.
* ``resolve(host, type='A', dnssec=True)``: Do a DNS resolution of the given type for the given hostname. While
  ``query()`` returns an instance of ``publicdns.models.DNSResponse``, ``resolve()`` only return a list of data
  like ``['8.8.8.8']``.


Patching
--------

Replace some functions of the standard socket object with publicdns's implementation.

    .. code-block:: python

       from publicdns.monkey import patch_socket
       patch_socket()

Documentation
=============

Until the project is properly documented you will have to rely on the source code. It is rather undocumented now, but
better documentation is under way. On the other hand, the code is quite extensively tested.

Query Limitation
----------------

Google can limit the number of API requests. Please follow `Rate-limiting queries`__ section.

__ https://developers.google.com/speed/public-dns/docs/security#rate_limit

Running tests
=============

PublicDNS has tests. These tests ensure that the code is in a working state. You have to install some external packages to run tests, listed in ``test_requirements.txt``:

    .. code-block:: console

       $ pip install -r test_requirements.txt

then:

    .. code-block:: console

       $ py.test

Alternatively, to run them in every supported Python version do:

    .. code-block:: console

       $ tox

Contributing
===========

1. Create an issue and describe your idea
2. Fork this repo
3. Create your feature branch (``git checkout -b my-new-feature``)
4. Run tests
5. Add a test for your feature
6. Run step 4 again
7. Commit your changes (``git commit -am 'Add some feature'``)
8. Publish the branch (``git push origin my-new-feature``)
9. Create a new Pull Request


License
=======

PublicDNS is released under the `MIT License`__.

__ http://www.opensource.org/licenses/MIT