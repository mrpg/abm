import os, sys
sys.path.append(os.path.dirname(os.path.realpath(__file__))) # hack (https://stackoverflow.com/a/49375740)

from farmer import *
from river import *

if __name__ == '__main__':
    r = River(10)

    for _ in range(4):
        r.add_farmer(1)
