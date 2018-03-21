import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation

fig = plt.figure()
fig.set_dpi(100)
fig.set_size_inches(7, 6.5)

Rb = 3
rm = 1

ax = plt.axes(xlim=(-5, 5), ylim=(-5, 5))
patch = plt.Circle((0, 0), rm, fill=False, fc='y')
main_circle = plt.Circle((0, 0), Rb, fill=False, fc='y')

def init():
    patch.center = (0, 0)
    ax.add_patch(patch)
    ax.add_patch(main_circle)
    return patch,

def animate(i):
    x, y = patch.center
    x = (Rb-rm) * np.sin(np.radians(i))
    y = (Rb-rm) * np.cos(np.radians(i))
    patch.center = (x, y)
    return patch,

anim = animation.FuncAnimation(fig, animate,
                               init_func=init,
                               frames=360,
                               interval=1,
                               blit=True)

plt.show()