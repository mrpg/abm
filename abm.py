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
    parser.add_argument('alpha', default = 0.1, type = float, help = 'alpha')
    parser.add_argument('lambda_', default = 5, type = float, help = 'lambda')

    args = parser.parse_args()

    for replication in range(1):
        r = River(1)

        for _ in range(4):
            r.add_farmer(learn_model = "ReinforcementSimple",
                         learn_args = dict(alpha = args.alpha,
                                           lambda_ = args.lambda_))

        runs = r.many_runs(200)

        CSV_prep = last_welfare(runs) + last_probabilities(r, 0) + last_probabilities(r, 1) + last_probabilities(r, 2) + last_probabilities(r, 3)
        print(','.join(map(str, CSV_prep)), flush = True)
