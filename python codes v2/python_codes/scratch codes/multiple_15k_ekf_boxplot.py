import matplotlib.pyplot as plt
import numpy as np

# Simple data to display in various forms
x = np.linspace(0, 2 * np.pi, 400)
y = np.sin(x ** 2)

fig, axarr = plt.subplots(2, 2)
fig.suptitle("This Main Title is Nicely Formatted", fontsize=16)

axarr[0, 0].plot(x, y)
axarr[0, 0].set_title('Axis [0,0] Subtitle')
axarr[0, 1].scatter(x, y)
axarr[0, 1].set_title('Axis [0,1] Subtitle')
axarr[1, 0].plot(x, y ** 2)
axarr[1, 0].set_title('Axis [1,0] Subtitle')
axarr[1, 1].scatter(x, y ** 2)
axarr[1, 1].set_title('Axis [1,1] Subtitle')

# # Fine-tune figure; hide x ticks for top plots and y ticks for right plots
plt.setp([a.get_xticklabels() for a in axarr[0, :]], visible=False)
plt.setp([a.get_yticklabels() for a in axarr[:, 1]], visible=False)

# Tight layout often produces nice results
# but requires the title to be spaced accordingly
fig.tight_layout()
fig.subplots_adjust(top=0.88)

plt.show()