import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation

fig = plt.figure()
fig.set_dpi(100)
fig.set_size_inches(8, 8)

Rb = 9
rm = 1

ax = plt.axes(xlim=(-Rb-1, Rb+1), ylim=(-Rb-1, Rb+1))
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

# plt.xlim(Rb+1, Rb+1)
# plt.ylim(Rb+1, Rb+1)
plt.show()