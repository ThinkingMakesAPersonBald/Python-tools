'''
Author: xinhua.pei xinhua.pei@airudder.com
Date: 2022-08-10 20:48:19
LastEditors: xinhua.pei xinhua.pei@airudder.com
LastEditTime: 2022-08-10 21:07:02
FilePath: /Python-tools/Matplotlib.py
Description: 

Copyright (c) 2022 by xinhua.pei xinhua.pei@airudder.com, All Rights Reserved. 
'''
import matplotlib.pyplot as plt
import numpy as np

# # Data for plotting
# t = np.arange(0.0, 2.0, 0.01)
# s = 1 + np.sin(2 * np.pi * t)

# fig, ax = plt.subplots()
# ax.plot(t, s)

# ax.set(xlabel='time (s)', 
#     ylabel='voltage (mV)',
#     title='About as simple as it gets, folks')

# ax.grid()

# fig.savefig("test.png")
# plt.show()

from matplotlib.widgets import Cursor
import numpy as np
import matplotlib.pyplot as plt


# Fixing random state for reproducibility
np.random.seed(19680801)

fig, ax = plt.subplots(figsize=(8, 6))

x, y = 4*(np.random.rand(2, 100) - .5)
ax.plot(x, y, 'o')
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)

# Set useblit=True on most backends for enhanced performance.
cursor = Cursor(ax, useblit=True, color='red', linewidth=2)

plt.show()