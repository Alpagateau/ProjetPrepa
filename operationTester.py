import matplotlib.pyplot as plt
import numpy as np


def showV(L):
    grid = np.zeros(1000)

    l = L.copy()
    for i in range(len(l)):
        grid[int(l[i])] = 1

    grid.shape = (10,100)
    plt.imshow(grid)
    plt.show()
