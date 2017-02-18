from concurrent.futures import ThreadPoolExecutor, as_completed
import os.path
import sys
import timeit

from dns import resolver as dns_resolver
from tqdm import tqdm


def main():
    sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
    from publicdns.client import PublicDNS

    domains = []
    filename = os.path.join(os.path.dirname(__file__), 'google_domains.txt')
    with open(filename, 'r') as f:
        domains = f.read().split('\n')
    size = len(domains)

    tqdmargs = {
        'total': 100,
        'unit': 'it',
        'unit_scale': True,
        'leave': True,
    }

    with ThreadPoolExecutor(max_workers=2) as pool:
        print('- dns.resolver')
        started = timeit.default_timer()
        resolver = dns_resolver.Resolver()
        resolver.nameservers = ['8.8.8.8', '8.8.4.4']
        futures = [pool.submit(resolver.query, domains[i % size], 'A')
                   for i in range(100)]
        for _ in tqdm(as_completed(futures), **tqdmargs):
            pass
        elapsed = timeit.default_timer() - started
        print('dns.resolver * 100 - took {}s'.format(elapsed))

    with ThreadPoolExecutor(max_workers=2) as pool:
        print('- PublicDNS')
        started = timeit.default_timer()
        client = PublicDNS()
        futures = [pool.submit(client.query, domains[i % size], 'A')
                   for i in range(100)]
        for _ in tqdm(as_completed(futures), **tqdmargs):
            pass
        elapsed = timeit.default_timer() - started
        print('\nPublicDNS * 100 - took {}s'.format(elapsed))


if __name__ == '__main__':
    main()
