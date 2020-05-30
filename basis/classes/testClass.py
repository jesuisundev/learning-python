from classes import *
from pprint import pprint as pp

a = Aircraft(
    "G-EUPT", 
    "747", 
    num_rows=20, 
    num_seat_per_row=6
)
f = Flight("AF2000", a)


pp(f._seating)

pp(f.allocate_seat("12F", "Toto"))

pp(f._seating)

pp(f.allocate_seat("12F", "Toto"))