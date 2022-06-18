# abm

To run,

```sh
python3 -i abm.py 0.05 20 10000 250
```

The 10000 denotes the number of replications (the "outer loop") and 250 the number of rounds (the "inner loop").

Then, e.g.,

```python
mean(welfares(rounds))
```

To see usage,

```sh
python3 abm.py --help
```

There are also very simple tests in `simple/`.
