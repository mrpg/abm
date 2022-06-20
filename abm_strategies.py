import argparse
import os
import sys
import random

import numpy as np

from farmer import Farmer
from river import River
from learning.reinforcement import Reinforcement

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("alpha", type=float, help="alpha")
    parser.add_argument("lambda_", type=float, help="lambda")
    parser.add_argument("seed", nargs="?", default=None, type=int, help="seed")

    args = parser.parse_args()
    rng = np.random.default_rng(args.seed)

    print(f"initial,welfare_pi,welfare_liter,strat0,strat1,strat2,strat3")

    for replication in range(10000):
        r = River(1)

        for _ in range(4):
            r.add_farmer(
                learn_model=Reinforcement,
                learn_args=dict(alpha=args.alpha, lambda_=args.lambda_, rng=rng),
            )

        rounds = r.many_rounds(5000)

        next_round = r.another_round()

        CSV_prep = (
            [r.initial]
            + next_round["welfare"]
            + [str(g[0]) + "+" + g[1].name for g in next_round["choices"]]
        )
        print(",".join(map(str, CSV_prep)), flush=True)
