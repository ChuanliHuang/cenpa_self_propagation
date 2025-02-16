import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import yaml
from itertools import chain
from bunch import bunchify


def density_evolution_map(df):
    densities = []
    for i, row in df.iterrows():
        density = row.sum() / config.simulation.lineage.nucleosome_num
        densities.append(density)
    plt.plot(densities)
    plt.xlabel('generation')
    plt.ylabel('density')
    plt.show()


def show_kymograph(df):
    x = []
    y = []
    for index, row in df.iterrows():
        row = row.to_numpy()
        if row.sum() != 0:
            x_coordinates = np.argwhere(row == 1).flatten().tolist()
            x.append(x_coordinates)
            # y_coordinates = [index * 20] * row.sum()
            y_coordinates = [index] * row.sum()
            y.append(y_coordinates)
        else:
            break
    x = list(chain.from_iterable(x))
    y = list(chain.from_iterable(y))
    binwidth = 1
    plt.hist2d(y, x,
               bins=[range(min(y), max(y) + binwidth + 1, binwidth), range(min(x), max(x) + binwidth + 1, binwidth)],
               cmap='gray')

    plt.ylabel('nucleosome position')
    plt.xlabel('generation')
    plt.show()


if __name__ == '__main__':
    with open("parameters.yaml") as f:
        config = yaml.load(f, Loader=yaml.Loader)
        config = bunchify(config)
    file_name = '/Users/kikawaryoku/PycharmProjects/project_cenp_a/local_only/master/states/lineage0.csv'
    _df = pd.read_csv(file_name, sep=',', header=None, dtype='int64')
    density_evolution_map(_df)
    show_kymograph(_df)