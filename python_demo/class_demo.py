import sys
import os
if os.path.abspath('../python code') not in sys.path:
    sys.path.insert(0, os.path.abspath('../python code'))


from transportations.Land import Car
from transportations.Sea import Boat


c = Car("BMW", "320", "2000")
c.run(100)
print(c.distance)

c = None