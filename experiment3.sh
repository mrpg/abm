#!/usr/bin/env bash

python3 abm_stoch.py TODO TODO "$(cat seed.txt)" 1000 5000 > data_stoch.csv
