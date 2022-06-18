# abm

<p align="center">
    <a href="https://github.com/psf/black"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>
</p>

A simple reinforcement learning model for the game of Farolfi & Erdlenbruch, 2020, ["A classroom experimental game to improve the understanding of asymmetric common-pool resource dilemmas in irrigation water management"](https://www.sciencedirect.com/science/article/abs/pii/S1477388020300268). Developed at the [2022 BESLab Summer School for Computational and Experimental Economics](https://www.upf.edu/web/beslab/summer-school-for-computational-and-experimental-economics) at [Universitat Pompeu Fabra](https://www.upf.edu/). Team members: [@GabrielBayle](https://github.com/GabrielBayle), [@gitcombat](https://github.com/gitcombat), [@mrpg](https://max.pm).

To run the central simulation,

```sh
python3 -i abm.py 0.05 20 1000 5000
```

The 1000 denotes the number of replications (the "outer loop") and 5000 the number of rounds (the "inner loop"). You may wish to reduce the number of replications. A random seed can be specified (our own seed is in `seed.txt`). To see usage,

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
