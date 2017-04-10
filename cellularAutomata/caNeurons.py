import numpy as np
import matplotlib.pyplot as plt 
import matplotlib.animation as animation
import random
plt.style.use('classic')

size = 100

#for stats
count = []
countOff = []
neigh = 0
neighs = []
refracts = []

#starting porportions
valsGrid = [1,0,-1]
pGrid = [.25,.5,.25]

# Static; Track the type of nrn, or if there is one: 1 excit, 0, struct, -1 inhib
# if 1, then this will cause surrounding cells to fire. If -1, then they will not fire
grid = np.random.choice(valsGrid, size*size, pGrid).reshape(size,size)

fireLog = np.zeros((size,size))
#print(fireLog)
for i in range(size):
    for j in range(size):
        if grid[i,j] == 1:
            fireLog[i,j] = 2
        elif grid[i,j] == -1:
            fireLog[i,j] = 1

x = grid
def numKin(array,typ,i,j,siz):
    eKin = 0
    iKin = 0  # variable to keep track of kin seen so far
    me = array[i][j]   # look in the mirror for a sec
    # check each of your neighbors
    for x in [-1,0,1]:
        ni = (i-x)%siz
        for y in [-1,0,1]:
            nj = (j-y)%siz
            #only look at the squares above and below and beside
            #if (abs(ni) + abs(nj)) > 1:
            if array[ni][nj] == 1 and typ[ni][nj] == 1:
              eKin += 1
            elif array[ni][nj] == 1 and typ[ni][nj] == -1:
              iKin += 1
    return eKin-1, iKin-1

def numberKin(array,i,j, siz):
    kin = 0  # variable to keep track of kin seen so far
    me = array[i][j]   # look in the mirror for a sec
    # check each of your neighbors
    for x in [-1,0,1]:
        ni = (i-x)%siz
        for y in [-1,0,1]:
            nj = (j-y)%siz
            #only look at the squares above and below and beside
            #if (abs(ni) + abs(nj)) > 1:
            if array[ni][nj] == 1:
                kin += 1
    return kin + 1


def step(data):
  global grid
  global fireLog
  global nType
  global neigh
  neigh = 0
  N = size
  newGrid = grid.copy()
  
  for i in range(size):
    for j in range(size):
        kin = numberKin(grid,i,j, size)
        
        if grid[i][j] == 1:
            newGrid[i][j] = -1
            fireLog[i][j] = 0
        elif grid[i][j] == -1:
            newGrid[i][j] = 0
        elif grid[i,j]== 0 and kin == 2: #or use two
            neigh +=1
            newGrid[i][j] = 1


  fire = 0
  off = 0
  refract = 0
  for i in range(size):
      for j in range(size):
        if grid[i][j] == 1:
            fire += 1
        elif grid[i][j] == 0:
            off += 1
        elif grid[i][j] == -1:
            refract += 1
            
  count.append(fire)
  countOff.append(off)
  refracts.append(refract)
    
  
  mat.set_data(newGrid)
  grid = newGrid
  neighs.append(neigh)
  return grid

# set up animation
#plt.matshow(nType,cmap=plt.cm.gray)
fig, ax = plt.subplots()
mat = ax.matshow(grid, cmap=plt.cm.gray)
ani = animation.FuncAnimation(fig,step, interval=100, save_count=50)
plt.show()

z = grid - x
c = 0
for i in range(size):
  for j in range(size):
    if z[i][j] == 0:
      c +=1

print(c, "cells changed")

plt.style.use('fivethirtyeight')
plt.title('Fire/Off Ratio')
plt.xlabel('Time')
plt.ylabel('Ratio')
rat = []
for on, off in zip(count, countOff):
    if off != 0:
        t = on/off
    else:
        t = 10000
    rat.append(t)
plt.plot(rat)
plt.show()


plt.style.use('fivethirtyeight')
plt.title('Cell Types')
plt.xlabel('Time')
plt.ylabel('Number Cells')

plt.plot(count, label='on')
plt.plot(countOff,label='off')
plt.plot(refracts,label='refract')
plt.legend()
plt.show()
