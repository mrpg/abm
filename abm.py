import argparse
import os
import sys
import random
sys.path.append(os.path.dirname(os.path.realpath(__file__))) # hack (https://stackoverflow.com/a/49375740)

from farmer import *
from river import *
from helpers import *

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('alpha', type = float, help = 'alpha')
    parser.add_argument('lambda_', type = float, help = 'lambda')
    parser.add_argument('seed', nargs = '?', default = None, type = int, help = 'seed')

    args = parser.parse_args()
    rng = np.random.default_rng(args.seed)

    print(f'welfare_pi,welfare_liter,'+','.join([f'p{k}i{i}A{j}' for k in range(0, 4) for i in range(0, 4) for j in range(1, 6)]))

    for replication in range(10000):
        r = River(1)

        for _ in range(4):
            r.add_farmer(learn_model = "ReinforcementSimple",
                         learn_args = dict(alpha = args.alpha,
                                           lambda_ = args.lambda_,
                                           rng = rng))

        runs = r.many_runs(250)

        CSV_prep = last_welfare(runs) + last_probabilities(r, 0) + last_probabilities(r, 1) + last_probabilities(r, 2) + last_probabilities(r, 3)
        print(','.join(map(str, CSV_prep)))
