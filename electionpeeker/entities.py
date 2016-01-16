class Person:

    def __init__(self, name, party):
        super().__init__()
        self._name = name
        self._party = party

    def __repr__(self):
        return '<{} of {}>'.format(self.name, self.party_name)

    @property
    def seat_count(self):
        return 1

    @property
    def name(self):
        return self._name

    @property
    def party_name(self):
        return self._party


class Party:

    def __init__(self, name, seat_count):
        super().__init__()
        self._name = name
        self._seat_count = seat_count

    def __repr__(self):
        return '<{} ({} seats)>'.format(self.party_name, self.seat_count)

    @property
    def seat_count(self):
        return self._seat_count

    @property
    def party_name(self):
        return self._name
