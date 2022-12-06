#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt

c1,c2,c3,c4,c5  = np.loadtxt("output_mie_code.txt", skiprows=2, unpack=True)

fig = plt.figure()
ax = fig.add_subplot(111)

plt.plot(c1,c2,'k--')
yticks = [0, 1000, 10000, 100000]
ax.set_yticks(yticks)
plt.yscale('log')

plt.grid(True,which="both")

plt.xlabel(r"Scattering Angle $\Theta$ ($^\circ$)")
plt.ylabel(r"$P_{11}$")

plt.show()