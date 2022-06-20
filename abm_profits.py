import argparse
import os
import sys
import random

import numpy as np

from farmer import Farmer
from river import River
from learning.reinforcement import Reinforcement
from helpers import *

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("alpha", type=float, help="alpha")
    parser.add_argument("lambda_", type=float, help="lambda")
    parser.add_argument("seed", nargs="?", default=None, type=int, help="seed")

    args = parser.parse_args()
    rng = np.random.default_rng(args.seed)

    print(f"replication,round,pi1,pi2,pi3,pi4")

    for replication in range(1000):
        r = River(1)

        for _ in range(4):
            r.add_farmer(
                learn_model=Reinforcement,
                learn_args=dict(alpha=args.alpha, lambda_=args.lambda_, rng=rng),
            )

        rounds = r.many_rounds(5000)

        for j, (pi1, pi2, pi3, pi4) in enumerate(
            zip(
                profits(r, which=0),
                profits(r, which=1),
                profits(r, which=2),
                profits(r, which=3),
            )
        ):
            print(f"{replication},{j},{pi1},{pi2},{pi3},{pi4}")
