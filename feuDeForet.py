import numpy as np
import matplotlib.pyplot as plt
import time

SIZE = 100

Grid = np.zeros((SIZE, SIZE))


# 0 = Ground
# 1 = ashes
# 2 = tree
# 3 = fire


#Init the forest
for i in range(SIZE):
    if i!=SIZE//2:
        for j in range(SIZE):
            if j != SIZE//2:
                if np.random.rand() > 0.5:
                    Grid[i,j] = 2
                    if np.random.rand() > 0.999:
                        Grid[i,j] = 3
        

def testNeighbourghood(i, j,M,condition, value):
    global Grid
    for k in range(3):
        for w in range(3):
            x = i+k-1
            y = j+w-1

            if x < 0:
                x = SIZE + x
            if x > SIZE-1:
                x = x-SIZE
            
            if y < 0:
                y = SIZE + y
            if y > SIZE-1:
                y = y-SIZE
            
            if Grid[x,y] == condition:
                M[x,y] = value

    return M
            

def iteration():
    global Grid
    NextGrid = Grid.copy()
    for i in range(SIZE):
        for j in range(SIZE):
            if Grid[i,j] == 3:
                NextGrid[i,j] = 1
                NextGrid = testNeighbourghood(i, j, NextGrid, 2, 3)

    Grid = NextGrid

for i in range(100):
    iteration()
    plt.imshow(Grid, cmap="Paired", norm=plt.Normalize(0,3))
    plt.pause(0.01)
plt.show()