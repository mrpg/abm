import matplotlib
import matplotlib.pyplot as plt

import scipy.stats

def profits(river, which = 0):
    return [g['endowment'] for g in river.farmers[which].learn.history]

def welfares(runs):
    return [run['welfare'][0] for run in runs]

def welfare_plot(runs):
    return plt.plot(range(len(runs)), welfares(runs))

def profit_plot(river, which = 0):
    pi = profits(river, which)
    return plt.plot(range(len(pi)), pi)

def mean(data):
    return sum(data)/len(data)
