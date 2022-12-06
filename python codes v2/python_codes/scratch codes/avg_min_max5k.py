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
ord = {1: [1.0046,
           0.7925,
           2.2502
           ],
         2: [0.7868,
             0.7537,
             0.8227],
         3: [0.8141,
             0.7660,
             0.8601],
         4: [0.8339,
             0.8150,
             0.8513],
         5: [0.8444,
             0.8308,
             0.8571],
         6: [0.8478,
             0.8350,
             0.8575],
         7: [0.8409,
             0.8301,
             0.8493],
         8: [0.8419,
             0.8376,
             0.8466],
         9: [0.8392,
             0.8365,
             0.8420],
         10: [0.8335,
              0.8313,
              0.8355],
         11: [0.8318,
              0.8325,
              0.8316,
              0.8372],
         12:[0.8534,
             0.8353,
             0.8654],
         13:[0.8600,
             0.8591,
             0.8592],
       14:[0.8582,
           0.8583,
           0.8573,
           0.8574],
       15:[0.8565,
           0.8558,
           0.8549,
           0.8542]}

seq_ord = {1:[1.2877,
              1.0186,
              3.1321],
           2:[1.0661,
              1.0149,
              1.1062],
           3:[1.0714,
              1.0177,
              1.1269],
           4:[1.0687,
              1.0465,
              1.1081],
           5:[1.0533,
              1.0409,
              1.0628],
           6:[1.0478,
              1.0331,
              1.0575],
           7:[1.0365,
              1.0283,
              1.0435],
           8:[1.0362,
              1.0317,
              1.0408],
           9:[1.0269,
              1.0235,
              1.0304],
           10:[1.0214,
               1.0198,
               1.0238],
           11:[1.0223,
               1.0230,
               1.0219,
               1.0206],
           12:[1.0250,
               1.0196,
               1.0298],
           13:[1.0233,
               1.0221,
               1.0209],
           14:[1.0199,
               1.0187,
               1.0177,
               1.0165],
           15:[1.0157,
               1.0146,
               1.0138,
               1.0127]
           }
apd={1:[1.3006,
        1.0368,
        2.8054],
     2:[1.1210,
        1.0865,
        1.2028],
     3:[1.1009,
        1.0839,
        1.1236],
     4:[1.1192,
        1.1052,
        1.1340],
     5:[1.1143,
        1.1041,
        1.1253],
     6:[ 1.1077,
         1.0990,
         1.1169],
     7:[1.0999,
        1.0929,
        1.1075],
     8:[1.0942,
        1.0878,
        1.1006],
     9:[1.0891,
        1.0840,
        1.0943],
     10:[1.0854,
         1.0812,
         1.0899],
     11:[1.0825,
         1.0787,
         1.0865],
     12:[1.0772,
         1.0714,
         1.0836
         ],
     13:[1.0686,
         1.0668,
         1.0714],
     14:[1.0648,
         1.0624,
         1.0669],
     15:[1.0621,
         1.0610,
         1.0627]}
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
plt.title("Outdoor LOS (Total number of emergency devices localized=300)")
plt.grid(color='gray', alpha=1, linestyle='dashed', linewidth=0.5)
#plt.grid(b=True, which='major', color='k', linestyle='-')

#legend
lns1 = plt.errorbar(x, y, yerr=yerr, color='goldenrod',
                    ms=7,lw=2, label='Only recent data (5000 UEs)',elinewidth=2)
lns2 = plt.errorbar(x2, y2, yerr=yerr2, color="blue", marker="o", label='Sequential (only recent data) (5000 UEs)',
                    ms=7,lw=1,elinewidth=2)
lns3 = plt.errorbar(x3, y3, yerr=yerr3, color="black", marker="s", label='All previous data (5000 UEs)',
                    ms=7,lw=1,elinewidth=2)
#lns3 = ax1.plot(time, seq, color="red", marker="o", markersize=7, label='Sequential (only recent data) (5000 UEs)')
#lns4 = ax1.plot(time, apd, color="black", marker="s", markersize=7, label='All previous data (100 UEs)',linestyle='dashed')

lns = lns1+lns2+lns3
#+lns2+lns4
#lns1++lns4
#abs = [l.get_label() for l in lns]
plt.legend(loc=1,fontsize=10)

plt.savefig('ml_results.png')
plt.show()