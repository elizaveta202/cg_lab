import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation
from matplotlib.widgets import TextBox

fig = plt.figure()
fig.set_dpi(100)
fig.set_size_inches(8, 8)

Rb = 9
rm = 1

ax = plt.axes(xlim=(-Rb-1, Rb+1), ylim=(-Rb-1, Rb+1))
patch = plt.Circle((0, 0), rm, fill=False, fc='y')
main_circle = plt.Circle((0, 0), Rb, fill=False, fc='y')
ax.add_patch(main_circle)


def init():
    patch.center = (0, 0)
    ax.add_patch(patch)
    return patch,

def animate(i):
    x, y = patch.center
    x = (Rb-rm) * np.sin(np.radians(i))
    y = (Rb-rm) * np.cos(np.radians(i))
    patch.center = (x, y)
    return patch,

def animate2(i, Rb, rm):
    x, y = patch.center
    x = (Rb-rm) * np.sin(np.radians(i))
    y = (Rb-rm) * np.cos(np.radians(i))
    patch.center = (x, y)
    return patch,

anim = animation.FuncAnimation(fig, animate2,
                               fargs=(Rb, rm),
                               init_func=init,
                               frames=360,
                               interval=1,
                               blit=False)

def submit(text):
    Rb = int(text)
    print(Rb)
    main_circle.set_radius(Rb)
    plt.draw()

    anim.__init__(fig, animate2, fargs=(Rb, rm),
                            init_func=init,
                            frames=360,
                            interval=1,
                            blit=False)
    anim.frame_seq = anim.new_frame_seq()
    anim.event_source.start()

axbox = plt.axes([0.1, 0.05, 0.08, 0.08])
text_box = TextBox(axbox, 'R')
text_box.on_submit(submit)

plt.show()