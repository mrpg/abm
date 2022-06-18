#!/usr/bin/env bash

python3 abm_strategies.py 0.05 20 "$(cat seed.txt)" > strategies.csv
grep -v welfare strategies.csv | cut -d, -f4- | sort | uniq -c | sort -rn | head
