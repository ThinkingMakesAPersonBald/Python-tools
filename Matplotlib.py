'''
Author: xinhua.pei xinhua.pei@airudder.com
Date: 2022-08-10 20:48:19
LastEditors: xinhua.pei xinhua.pei@airudder.com
LastEditTime: 2022-08-11 12:43:40
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


# 可以吸附数据点的光标
import matplotlib.pyplot as plt
import numpy as np
 
 """
  A crosshair cursor that spans the axes and moves with mouse cursor.
 
  For the cursor to remain responsive you must keep a reference to it.
 
  Parameters
  ----------
  ax : `matplotlib.axes.Axes`
    The `~.axes.Axes` to attach the cursor to.
  horizOn : bool, default: True
    Whether to draw the horizontal line.
  vertOn : bool, default: True
    Whether to draw the vertical line.
  useblit : bool, default: False
    Use blitting for faster drawing if supported by the backend.
 
  Other Parameters
  ----------------
  **lineprops
    `.Line2D` properties that control the appearance of the lines.
    See also `~.Axes.axhline`.
 
  Examples
  --------
  See :doc:`/gallery/widgets/cursor`.
  """


class SnappingCursor:
  """
  A cross hair cursor that snaps to the data point of a line, which is
  closest to the *x* position of the cursor.
 
  For simplicity, this assumes that *x* values of the data are sorted.
  """
  def __init__(self, ax, line):
    self.ax = ax
    self.horizontal_line = ax.axhline(color='k', lw=0.8, ls='--')
    self.vertical_line = ax.axvline(color='k', lw=0.8, ls='--')
    self.x, self.y = line.get_data()
    self._last_index = None
    # text location in axes coords
    self.text = ax.text(0.72, 0.9, '', transform=ax.transAxes)
 
  def set_cross_hair_visible(self, visible):
    need_redraw = self.horizontal_line.get_visible() != visible
    self.horizontal_line.set_visible(visible)
    self.vertical_line.set_visible(visible)
    self.text.set_visible(visible)
    return need_redraw
 
  def on_mouse_move(self, event):
    if not event.inaxes:
      self._last_index = None
      need_redraw = self.set_cross_hair_visible(False)
      if need_redraw:
        self.ax.figure.canvas.draw()
    else:
      self.set_cross_hair_visible(True)
      x, y = event.xdata, event.ydata
      index = min(np.searchsorted(self.x, x), len(self.x) - 1)
      if index == self._last_index:
        return # still on the same data point. Nothing to do.
      self._last_index = index
      x = self.x[index]
      y = self.y[index]
      # update the line positions
      self.horizontal_line.set_ydata(y)
      self.vertical_line.set_xdata(x)
      self.text.set_text('x=%1.2f, y=%1.2f' % (x, y))
      self.ax.figure.canvas.draw()
 
x = np.arange(0, 1, 0.01)
y = np.sin(2 * 2 * np.pi * x)
 
fig, ax = plt.subplots()
ax.set_title('Snapping cursor')
line, = ax.plot(x, y, 'o')
snap_cursor = SnappingCursor(ax, line)
fig.canvas.mpl_connect('motion_notify_event', snap_cursor.on_mouse_move)
plt.show()