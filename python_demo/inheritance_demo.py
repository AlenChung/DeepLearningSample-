import sys
import os
if os.path.abspath('../python code') not in sys.path:
    sys.path.insert(0, os.path.abspath('../python code'))

from transportations.Land import Car
from transportations.Sea import Boat

class My(Car, Boat):
    def __init__(self):
        pass


class My2(Boat, Car):
    def __init__(self):
        pass

print(4>>1)

m = My()
m.run(100)
print("My runs " + str(m.distance))

m2 = My2()
m2.run(100)
print("My2 runs " + str(m2.distance))