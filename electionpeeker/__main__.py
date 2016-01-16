import tabulate

from . import count_party_seats


def print_party_seats():
    party_seats = count_party_seats()
    table = [
        ('{:>4}'.format(count), '{:<32}'.format(name))
        for name, count in party_seats.items()
    ]
    print(tabulate.tabulate(table))
    print('{:>4}  TOTAL'.format(sum(party_seats.values())))


if __name__ == '__main__':
    print_party_seats()
