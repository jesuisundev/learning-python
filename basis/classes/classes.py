"""
Class for aircraft
"""

class Flight:

    """
        - The first argument of __init___ must be self
        - __init__ is not a constructor, its a initializer
        - self is similar to this
        - _number => to avoid name clash, and same convention than JS
    """
    def __init__(self, number, aircraft):
        if not number[:2].isalpha():
            raise ValueError("Number %s need start with 2 alpha" % number)

        if not number.isupper():
            raise ValueError("Number %s is not full CAPS" % number)

        if not (number[2:].isdigit() and int(number[2:]) <= 9999):
            raise ValueError("Invalid number at the end")
        
        self._number = number
        self._aircraft = aircraft

        rows, seats = self._aircraft.seating_plan()
        self._seating  = [None] + [{letter: None for letter in seats} for _ in rows]

    def aircraft_model(self):
        return self._aircraft.model()

    def number(self):
        return self._number

    def airline(self):
        return self._number[:2]

    def allocate_seat(self, seat, passenger):
        """[summary]

        Arguments:
            seat {[type]} -- [description]
            passenger {[type]} -- [description]

        Returns:
            [type] -- [description]
        """
        rows, seat_letters = self._aircraft.seating_plan()

        letter = seat[-1]

        if letter not in seat_letters:
            raise ValueError("Invalid seat letter : %s" % letter)

        row_text = seat[:-1]

        try:
            row = int(row_text)
        except ValueError:
            raise ValueError("Invalid seat row : %s" % row_text)

        if row not in rows:
            raise ValueError("Invalid rown number: %s" % row)

        if self._seating[row][letter] is not None:
            raise ValueError("Seat already occupied")

        self._seating[row][letter] = passenger


class Aircraft:

    def __init__(self, registration, model, num_rows, num_seat_per_row):
        self._registration = registration
        self._model = model
        self._num_rows = num_rows
        self._num_seats_per_row = num_seat_per_row

    def registration(self):
        return self._registration

    def model(self):
        return self._model

    def seating_plan(self):
        return (range(1, self._num_rows +1), "ABCDEFGHJK"[:self._num_seats_per_row])