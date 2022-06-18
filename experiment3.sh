#!/usr/bin/env bash

python3 abm_stoch.py 0.05 20 "$(cat seed.txt)" 1000 5000 > stochastic.csv
