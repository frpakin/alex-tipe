# %%
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from DiamondSquare.src.hkb_diamondsquare import DiamondSquare as DS

def show_terrain_2D(terrain_array):
    sns.set()
    #f = plt.figure(figsize=(4, 4))
    sns.color_palette("magma", as_cmap=True)
    with sns.axes_style("ticks"):
        ax = sns.heatmap(terrain_array)

# %%
#make a height map of size 16x20, with values ranging from 1 to 100, with moderate roughness
map1 = DS.diamond_square(shape=(16,20),
                         min_height=1,
                         max_height=100,
                         roughness=0.75)
show_terrain_2D(map1)
# %%
#make a square height map with sides of length 120, that are VERY rough
map2 = DS.diamond_square(shape=(120,120),
                         min_height=1,
                         max_height=100,
                         roughness=0.99)
show_terrain_2D(map2)
# %%
#make a VERY smooth map with values from -10 to 10
map3 = DS.diamond_square(shape=(10,10),
                         min_height=-10,
                         max_height=10,
                         roughness=0.05)
show_terrain_2D(map3)
# %%
#make a smooth map with values from 0 to 10
map4 = DS.diamond_square(shape=(50,50), min_height=0, max_height=10, roughness=0.3)
show_terrain_2D(map4)
# %%
#The same in 3D
X = np.arange(0, 50, 1)
Y = np.arange(0, 50, 1)
X, Y = np.meshgrid(X, Y)
Z = map4

# Plot the surface
fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
fig.set_size_inches(6,6)
surf = ax.plot_surface(X, Y, Z, cmap= plt.get_cmap('magma'))
fig.colorbar(surf, ax = ax, shrink = 0.7, aspect = 7) 
ax.set(xticklabels=[],
       yticklabels=[],
       zticklabels=[])
plt.show()
# %%
