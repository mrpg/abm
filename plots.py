import matplotlib
import matplotlib.pyplot as plt

def welfare_plot(runs):
    w = [run['welfare'][0] for run in runs]
    return plt.plot(range(len(runs)), w)

def profit_plot(river, which = 0):
    pi = [g['endowment'] for g in river.farmers[which].learn.history]
    return plt.plot(range(len(pi)), pi)
