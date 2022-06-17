#!/usr/bin/env bash

pids=""

for alpha in 0.05 0.1 0.2 0.5 0.75; do
    for lambda in 0 1 3 5 10 20; do
        outfile="data_${alpha}_${lambda}_out.csv"
        python3 abm.py "$alpha" "$lambda" "$(cat seed.txt)" > $outfile &
        pids="$pids $!"
    done
done

wait $pids
