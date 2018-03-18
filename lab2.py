import matplotlib.pyplot as plt
import matplotlib.patches as patches

fig = plt.figure()
ax = fig.add_subplot(111, aspect='equal')
ax.add_patch(
    patches.Circle(
        (0.5, 0.5),
        0.2,
        fill=False      # remove background
    )
)
# fig.savefig('circle.png', dpi=90, bbox_inches='tight')
plt.show()