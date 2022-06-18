# abm

To run the central simulation,

```sh
python3 -i abm.py 0.05 20 10000 250
```

The 10000 denotes the number of replications (the "outer loop") and 250 the number of rounds (the "inner loop"). You may wish to reduce the number of replications. A random seed can be specified (our own seed is in `seed.txt`). To see usage,

```sh
python3 abm.py --help
```

Then, e.g.,

```python
mean(welfares(rounds))
```

`abm_profits.py` outputs profits per round and replication. `abm_stoch.py` introduces stochasticity of the initial inflow. `abm_strategies.py` extracts the gameplay from an additional 5,001st round.

There are also very simple tests in `simple/`.

Output from June 2022 is available in `data/2022-06-18.tar.bz2` that can be extracted with `tar` or 7-Zip. You can reproduce our plots using `data/plots.R`. You can also reproduce all data using the shell scripts in `experiment?.sh`. Except for floating-point specifics, everything should be identical to our runs.
