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
ord = {1: [1.1288,
           0.8485,
           1.2637],
         2: [1.1062,
             1.0606,
             1.1531],
         3: [1.1385,
             1.1228,
             1.1534],
         4: [1.1307,
             1.1264,
             1.1352],
         5: [1.1294,
             1.1254,
             1.1338],
         6: [1.1289,
             1.1261,
             1.1309],
         7: [1.1336,
             1.1282,
             1.1370],
         8: [1.1320,
             1.1307,
             1.1344
             ],
         9: [1.1317,
             1.1282,
             1.1360],
         10: [1.1275,
              1.1262],
         11: [1.1287,
              1.1212,
              1.1419],
         12:[1.1405,
             1.1398,
             1.1386,
             1.1380]}

seq_ord = {1:[1.1213,
              0.8485,
              1.2637],
           2:[1.0984,
              1.0493,
              1.1481],
           3:[1.1371,
              1.1238,
              1.1487],
           4:[1.1444,
              1.1357,
              1.1520],
           5:[1.1488,
              1.1426,
              1.1533],
           6:[1.1421,
              1.1421,
              1.1468,
              1.1466,
              1.1454],
           7:[1.1514,
              1.1484,
              1.1532],
           8:[1.1477,
              1.1459,
              1.1496],
           9:[1.1448,
              1.1435,
              1.1528],
           10:[1.1423,
               1.1410],
           11:[1.1511,
               1.1400,
               1.1637
               ],
           12:[1.1587,
               1.1571,
               1.1603]
           }
apd={1:[1.1299,
        0.8004,
        1.3148],
     2:[1.0876,
        1.0559,
        1.1378],
     3:[1.1099,
        1.0934,
        1.1282],
     4:[1.1192,
        1.1088,
        1.1305],
     5:[1.1228,
        1.1154,
        1.1310],
     6:[1.1248,
        1.1187,
        1.1314],
     7:[1.1259,
        1.1209,
        1.1314],
     8:[ 1.1278,
         1.1220,
         1.1312],
     9:[1.1256,
        1.1217,
        1.1267],
     10:[1.1247,
        1.1212,
        1.1282],
     11:[1.1246,
        1.1215,
        1.1278],
     12:[1.1261,
         1.1235,
         1.1287]}
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
plt.title("Outdoor LOS (Total number of emergency devices localized=343)")
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
plt.legend(loc=1,fontsize=10)

plt.savefig('ml_results.png')
plt.show()