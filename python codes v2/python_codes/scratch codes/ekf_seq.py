import matplotlib.pyplot as plt
import numpy as np

import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as plt
import numpy as np

from matplotlib import rc
from matplotlib.ticker import AutoMinorLocator

rc('mathtext', default='regular')
#refer:https://www.discoverbits.in/post/matplotlib-python-code-to-plot-errorbar-using-minimum-and-maximum-values/
# data for plot
#15KV35
#WITH OR WITHOUT AOA
#APD sep 20
no_gps = {1: [14.6026,
              8.4541,
              17.8765],

          }
with_aoa = {1:[19.4139,
               14.2331,
               21.5903],
            }

# plot error bar
x = []
y = []
yerr = []
for k, v in no_gps.items():
    u = (120.0)
    #print(u[k-1])
    gg = u[k-1]
    x.append(gg)
    y.append(np.mean(v))  # compute mean
    yerr.append([np.mean(v) - min(v), max(v) - np.mean(v)])  # use max and min as upper and lower bound

yerr = np.transpose(yerr)  # yerr should be 2xN matrix
#seq_ord
x2 = []
y2 = []
yerr2 = []
for k2, v2 in with_aoa.items():
    #print(u[k-1])
    gg = u[k2-1]
    x2.append(gg)
    y2.append(np.mean(v2))  # compute mean
    yerr2.append([np.mean(v2) - min(v2), max(v2) - np.mean(v2)])  # use max and min as upper and lower bound

yerr2 = np.transpose(yerr2)  # yerr should be 2xN matrix

plt.errorbar(x, y, yerr=yerr, color='goldenrod',
             lw=2,elinewidth=2)
plt.errorbar(x2, y2, yerr=yerr2, color='blue',marker='s', mfc='blue',
             ms=5,lw=2,elinewidth=2)
plt.xlabel("time (sec)")
plt.ylabel('RMSE (m)')
plt.title("Indoor NLOS (Total number of emergency devices localized=343)")
plt.grid(color='gray', alpha=1, linestyle='dashed', linewidth=0.5)
#plt.grid(b=True, which='major', color='k', linestyle='-')

#legend
lns1 = plt.errorbar(x, y, yerr=yerr, color='goldenrod',
                    ms=7,lw=2, label='with no GPS (15k UEs)',elinewidth=2)
lns2 = plt.errorbar(x2, y2, yerr=yerr2, color="blue", marker="o", label='with GPS (15k UEs)',
                    ms=7,lw=1,elinewidth=2)


#lns3 = ax1.plot(time, seq, color="red", marker="o", markersize=7, label='Sequential (only recent data) (5000 UEs)')
#lns4 = ax1.plot(time, apd, color="black", marker="s", markersize=7, label='All previous data (100 UEs)',linestyle='dashed')

lns = lns1+lns2
#+lns2+lns4
#lns1++lns4
#abs = [l.get_label() for l in lns]
plt.legend(loc=7,fontsize=10)

plt.savefig('ml_results.png')
plt.show()


