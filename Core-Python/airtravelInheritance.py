class Flight:
    """A flight with a particular passenger aircraft"""

    def __init__(self, number, aircraft):
        if not number[:2].isalpha():
            raise ValueError(f"Not 2 initial letters in '{number}'")
        if not number[:2].isupper():
            raise ValueError(f"Not 2 initial Upper letters in '{number}'")
        if not [number[2:].isdigit() and int(number[2:]) <= 9999]:
            raise ValueError(f"Invalid number in '{number}'")

        self._number = number
        self._aircraft = aircraft
        rows, seats = self._aircraft.seating_plan()
        self._seating = [None] + [{letter: None for letter in seats} for _ in rows]

    def aircraft_model(self):
        return self._aircraft.model()

    def number(self):
        return self._number

    def airline(self):
        return self._number[:2]

    def allocate_seats(self, seat, passenger):
        """Allocate a seat to a passanger

        :arg
            seat: A seat designator such as '12C' or '21F'
            passenger: The passenger name

        :raises
            ValueError: If the seat is unavailable.
        """

        row, letter = self._parse_seat(seat)

        if self._seating[row][letter] is not None:
            raise ValueError(f'seat {seat} already occupied')

        self._seating[row][letter] = passenger

    def _parse_seat(self, seat):
        rows, seat_letters = self._aircraft.seating_plan()

        letter = seat[-1]
        if letter not in seat_letters:
            raise ValueError(f'invalid seat letter {letter}')

        row_text = seat[:-1]
        try:
            row = int(row_text)
        except ValueError:
            raise ValueError(f'Invalid seat row {row_text}')

        if row not in rows:
            raise ValueError(f'Invalid row number {row}')
        return row, letter

    def relocate_passenger(self, from_seat, to_seat):
        """Relocate a passenger to a different seat

        :arg
            from_seat: The existing seat designator for the passenger to be moved
            to_seat: The new seat designator
        """
        from_row, from_letter = self._parse_seat(from_seat)
        if self._seating[from_row][from_letter] is None:
            raise ValueError(f'No passenger to relocate in seat {from_seat}')

        to_row, to_letter = self._parse_seat(to_seat)
        if self._seating[to_row][to_letter] is not None:
            raise ValueError(f'Seat {to_seat} already occupied')

        self._seating[to_row][to_letter] = self._seating[from_row][from_letter]
        self._seating[from_row][from_letter] = None

    def num_available_seats(self):
        return sum(sum(1 for s in row.values() if s is None)
                   for row in self._seating
                   if row is not None)

    def make_boarding_cards(self, card_printer):
        for passenger, seat in sorted(self._passenger_seats()):
            card_printer(passenger, seat, self.number(), self.aircraft_model())

    def _passenger_seats(self):
        """An iterable series of passengers seating locations"""
        row_numbers, seat_letters = self._aircraft.seating_plan()
        for row in row_numbers:
            for letter in seat_letters:
                passenger = self._seating[row][letter]
                if passenger is not None:
                    yield passenger, f'{row}{letter}'


class Aircraft:
    def __init__(self, registration):
        self._registration = registration

    def registration(self):
        return self._registration

    def num_seats(self):
        rows, row_seats = self.seating_plan()
        return len(rows) * len(row_seats)


class AirbusA319(Aircraft):


    def model(self):
        return "Airbus A319"

    def seating_plan(self):
        return range(1, 23), "ABCDF"


class Boeing777(Aircraft):
    def __init__(self, registration):
        self._registration = registration

    def registration(self):
        return self._registration

    def model(self):
        return "Boeing777"

    def seating_plan(self):
        return range(1, 56), "ABCDFGHJK"


def make_flight():
    f = Flight(number="BA758",
               aircraft=Aircraft(registration="G-EUTP", model="Airbus 319", num_rows=22, num_seats_per_row=6))
    f.allocate_seats(seat='12C', passenger='jalejo')
    f.allocate_seats(seat='2C', passenger='beruba')
    f.allocate_seats(seat='1A', passenger='negro')
    f.allocate_seats(seat='5A', passenger='jaimeA')
    f.allocate_seats(seat='20A', passenger='JuanC')
    return f


def make_flights():
    a = Flight(number="BA759",
               aircraft=AirbusA319("G-EUPT"))
    a.allocate_seats(seat='12C', passenger='jalejo')
    a.allocate_seats(seat='2C', passenger='beruba')
    a.allocate_seats(seat='1A', passenger='negro')
    a.allocate_seats(seat='5A', passenger='jaimeA')
    a.allocate_seats(seat='20A', passenger='JuanC')

    b = Flight(number="AF72",
               aircraft=Boeing777("F-GSPS"))
    b.allocate_seats(seat='12C', passenger='jalejo')
    b.allocate_seats(seat='2C', passenger='beruba')
    b.allocate_seats(seat='1A', passenger='negro')
    b.allocate_seats(seat='5A', passenger='jaimeA')
    b.allocate_seats(seat='20A', passenger='JuanC')
    return a, b


def console_card_printer(passenger, seat, flight_number, aircraft):
    output = f'| Name: {passenger}' \
             f'  Flight: {flight_number}' \
             f'  Seat: {seat}' \
             f'  Aircraft: {aircraft}' \
             ' |'
    banner = '+' + '-' * (len(output) - 2) + '+'
    border = '|' + ' ' * (len(output) - 2) + '|'
    lines = [banner, border, output, border, banner]
    card = "\n".join(lines)
    print(card)
    print()
