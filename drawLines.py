import numpy as np
import pylab as pl
from matplotlib import collections  as mc
import matplotlib.pyplot as plt

lines = [[(0, 5), (1, 1)], [(2, 3), (3, 3)], [(1, 2), (1, 3)]]
c = np.array([(1, 0, 0, 1), (0, 1, 0, 1), (0, 0, 1, 1)])

lc = mc.LineCollection(lines, colors=c, linewidths=2)
fig, ax = pl.subplots()
ax.add_collection(lc)
ax.autoscale()
ax.margins(0.1)
plt.show()
print "done"




def dr_line_maker():
    return 0


#WORK DAMNIT
path_world0 = np.full((rows - 1, columns - 1), 0)
path_world1 = np.full((rows - 1, columns - 1), 0)

path_nr = 1
for i in range(0,rows-1):
    for j in range(0,columns-1):
        #newpath
        if pass_through_rules(i, j, 0, crossWorld.world0) == 0:
            path_world0[i,j] = path_nr
            path_nr += 1
        #existing path dl
        elif pass_through_rules(i, j, 0, crossWorld.world0) == 1:
            path_world0[i,j] = path_world0[i-1,j+1]
        #existing path dr
        elif pass_through_rules(i, j, 0, crossWorld.world0) == 2:
            path_world0[i, j] = path_world0[i - 1, j - 1]
        #Bounce!
        elif bounce_h_rules(i,j,0,crossWorld.world0) == 1:
            path_world0[i,j] = path_world0[i,j-1]
        elif bounce_v_rules(i,j,0,crossWorld.world0) == 1:
            path_world0[i,j] = path_world0[i-1,j]
        else:
            path_world0[i,j] = 0