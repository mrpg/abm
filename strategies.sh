#!/usr/bin/env bash

python3 abm_strategies.py 0.05 20 "$(cat seed.txt)" > strategies.csv
cut -d, -f4- < strategies.csv | sort | uniq -c | sort -rn
