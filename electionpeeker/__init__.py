import collections

from .sources import (
    aboriginal_highland, aboriginal_lowland, national, regional,
)


def count_party_seats():
    party_counts = collections.defaultdict(lambda: 0)
    sources = [aboriginal_highland, aboriginal_lowland, national, regional]
    for source in sources:
        for entity in source.crawl():
            party_counts[entity.party_name] += entity.seat_count
    return party_counts
