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

    print(f'initial,welfare_pi,welfare_liter,strat0,strat1,strat2,strat3')

    for replication in range(10000):
        r = River(1)

        for _ in range(4):
            r.add_farmer(learn_model = "ReinforcementSimple",
                         learn_args = dict(alpha = args.alpha,
                                           lambda_ = args.lambda_,
                                           rng = rng))

        runs = r.many_runs(5000) # TODO

        next_run = r.another_run()

        CSV_prep = [r.initial] + next_run['welfare'] + [str(g[0])+'+'+g[1].name for g in next_run['choices']]
        print(','.join(map(str, CSV_prep)), flush = True)
