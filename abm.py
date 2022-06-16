import os
import sys
import random
sys.path.append(os.path.dirname(os.path.realpath(__file__))) # hack (https://stackoverflow.com/a/49375740)

from farmer import *
from river import *
from plots import *

if __name__ == '__main__':
    r = River(1)

    for _ in range(4):
        r.add_farmer()

    runs = r.many_runs(50000000)
