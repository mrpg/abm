import argparse
import os
import sys
import random
sys.path.append(os.path.dirname(os.path.realpath(__file__))) # hack (https://stackoverflow.com/a/49375740)

from farmer import *
from river import *
from helpers import *

parser = argparse.ArgumentParser()
parser.add_argument('alpha', type = float, help = 'alpha')
parser.add_argument('lambda_', type = float, help = 'lambda')
parser.add_argument('seed', nargs = '?', default = None, type = int, help = 'seed')

args = parser.parse_args()
rng = np.random.default_rng(args.seed)

r = River(1)

for _ in range(4):
    r.add_farmer(learn_model = "ReinforcementSimple",
                 learn_args = dict(alpha = args.alpha,
                                   lambda_ = args.lambda_,
                                   rng = rng))
