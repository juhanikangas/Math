from matplotlib import pyplot as plt, patches, ticker
import numpy as np
import math
def degs_to_rads(to_rad):
    rads = []
    for deg in to_rad:
        rads.append(np.radians(deg))
    return rads

fig = plt.figure(figsize=(6.4*3, 4.8*3))
ax = fig.subplots()

ymp = patches.Circle((0, 0), radius=1, fill=0)
ax.add_patch(ymp)

# Move left y-axis and bottom x-axis to center, passing through (0,0)
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('center')

# Eliminate upper and right axes
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

# Manually set the axis limits and ticks
ax.set_xlim(-1.2, 1.2)
ax.set_ylim(-1.2, 1.2)
ax.set_xticks([-1, -0.5, 0.5, 1])
ax.set_yticks([-1, -0.5, 0.5, 1])

# Customize the tick labels for π and π/2
ax.xaxis.set_major_formatter(ticker.FuncFormatter(lambda val, pos: f'{val}$/π$' if val != 0 else '0'))
ax.yaxis.set_major_formatter(ticker.FuncFormatter(lambda val, pos: f'{val}$/π$' if val != 0 else '0'))

ax.axis('equal')

pist_xy = np.array(degs_to_rads([30, 45, 60, 90, 120, 150, 180, 270]))

x = np.cos(pist_xy)
y = np.sin(pist_xy)

plt.scatter(x, y, color='red', marker='X', label='rad/deg')

plt.legend()

plt.show()
