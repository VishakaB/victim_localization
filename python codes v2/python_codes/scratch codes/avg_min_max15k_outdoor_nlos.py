import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as plt
import numpy as np

from matplotlib import rc
from matplotlib.ticker import AutoMinorLocator

rc('mathtext', default='regular')
#refer:https://www.discoverbits.in/post/matplotlib-python-code-to-plot-errorbar-using-minimum-and-maximum-values/
# data for plot
#indoor NLOS ord 100 UEs
#5ktownv9
ord = {1: [1.2338,
           0.9405,
           1.4080],
         2: [1.3169,
             1.2553,
             1.3855],
         3: [1.4336,
             1.3782,
             1.4664],
         4: [1.4793,
             1.4674,
             1.4923],
         5: [1.4991,
             1.4895,
             1.5066],
         6: [1.5075,
             1.5095,
             1.5096,
             1.5090,
             1.5093],
         7: [1.5120,
             1.5077,
             1.5151],
         8: [1.5165,
             1.5136,
             1.5203
             ],
         9: [1.5226,
             1.5187,
             1.5340],
         10: [1.5336,
              1.5350],
         11: [1.5452,
              1.5336,
              1.5560
              ],
         12:[1.5545,
             1.5553,
             1.5566,
             1.5579]}

seq_ord = {1:[1.2494,
              0.9405,
              1.4306],
           2:[1.3874,
              1.2816,
              1.3946],
           3:[1.4488,
              1.3871,
              1.4956],
           4:[1.5136,
              1.4964,
              1.5301],
           5:[1.5421,
              1.5344,
              1.5429],
           6:[1.5441,
              1.5437,
              1.5444],
           7:[1.5468,
              1.5449,
              1.5489],
           8:[1.5506,
              1.5490,
              1.5533],
           9:[1.5653,
              1.5548,
              1.5695],
           10:[1.5671,
               1.5667],
           11:[1.5850,
               1.5727,
               1.5918
               ],
           12:[1.5938,
               1.5930,
               1.5949]
           }
apd={1:[1.1724,
        0.8495,
        1.3410],
     2:[1.1351,
        1.1055,
        1.1604],
     3:[1.1633,
        1.1440,
        1.1982],
     4:[1.1931,
        1.1791,
        1.2129],
     5:[1.2079,
        1.1971,
        1.2208],
     6:[1.2160,
        1.2069,
        1.2252],
     7:[1.2208,
        1.2133,
        1.2281],
     8:[ 1.2240,
         1.2173,
         1.2282],
     9:[1.2270,
        1.2213,
        1.2320],
     10:[1.2292,
         1.2241,
         1.2337],
     11:[1.2302,
         1.2327,
         1.2342],
     12:[1.2429,
         1.2301,
         1.2434]}
# plot error bar
x = []
y = []
yerr = []
for k, v in ord.items():
    u = (121.9352244,
         245.0565746,
         361.9471361,
         484.7443358,
         600.077743,
         720.1311196,
         840.4899992,
         977.9114601,
         1229.799392,
         1465.315692,
         1585.315692,
         2043.29332,
         2163.29332,
         2428.972382,
         2668.972382)
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
for k2, v2 in seq_ord.items():
    #print(u[k-1])
    gg = u[k2-1]
    x2.append(gg)
    y2.append(np.mean(v2))  # compute mean
    yerr2.append([np.mean(v2) - min(v2), max(v2) - np.mean(v2)])  # use max and min as upper and lower bound

yerr2 = np.transpose(yerr2)  # yerr should be 2xN matrix

#apd
x3 = []
y3 = []
yerr3 = []
for k3, v3 in apd.items():
    #print(u[k-1])
    gg = u[k3-1]
    x3.append(gg)
    y3.append(np.mean(v3))  # compute mean
    yerr3.append([np.mean(v3) - min(v3), max(v3) - np.mean(v3)])  # use max and min as upper and lower bound

yerr3 = np.transpose(yerr3)  # yerr should be 2xN matrix

plt.errorbar(x, y, yerr=yerr, color='goldenrod',
             lw=2,elinewidth=2)
plt.errorbar(x2, y2, yerr=yerr2, color='blue',marker='s', mfc='blue',
             ms=5,lw=2,elinewidth=2)
plt.errorbar(x3, y3, yerr=yerr3, color='black',marker='s', mfc='black',
             ms=5,lw=2,elinewidth=2)
plt.xlabel("time (sec)")
plt.ylabel('RMSE (m)')
plt.title("Outdoor NLOS (Total number of emergency devices localized=343)")
plt.grid(color='gray', alpha=1, linestyle='dashed', linewidth=0.5)
#plt.grid(b=True, which='major', color='k', linestyle='-')

#legend
lns1 = plt.errorbar(x, y, yerr=yerr, color='goldenrod',
                    ms=7,lw=2, label='Only recent data (15k UEs)',elinewidth=2)
lns2 = plt.errorbar(x2, y2, yerr=yerr2, color="blue", marker="o", label='Sequential (only recent data) (15k UEs)',
                    ms=7,lw=1,elinewidth=2)
lns3 = plt.errorbar(x3, y3, yerr=yerr3, color="black", marker="s", label='All previous data (15k UEs)',
                    ms=7,lw=1,elinewidth=2)
#lns3 = ax1.plot(time, seq, color="red", marker="o", markersize=7, label='Sequential (only recent data) (5000 UEs)')
#lns4 = ax1.plot(time, apd, color="black", marker="s", markersize=7, label='All previous data (100 UEs)',linestyle='dashed')

lns = lns1+lns2+lns3
#+lns2+lns4
#lns1++lns4
#abs = [l.get_label() for l in lns]
plt.legend(loc=4,fontsize=10)

plt.savefig('ml_results.png')
plt.show()