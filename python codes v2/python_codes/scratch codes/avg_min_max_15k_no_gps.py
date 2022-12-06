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
          2: [18.1023,
              16.4780,
              18.2078],
          3: [18.1847,
              17.4699,
              18.8690],
          4: [56.4192,
              18.4904,
              70.8551],
          5: [104.2781,
              61.4573,
              112.9595],
          6: [113.0247,
              99.0649,
              121.3934],
          7: [120.1106,
              110.1515,
              126.6790],
          8: [139.5590,
              118.6285,
              146.2720
              ],
          9: [153.3566,
              138.2840,
              159.1422],
          10: [162.2257,
               151.5395,
               167.3029],
          11: [166.0660,
               158.6023,
               170.9613
               ],
          12:[172.1849,
              165.0369,
              176.7763
              ],
          13:[184.8399,
              172.7193,
              188.3408],
          14:[195.9696,
              186.8311,
              198.7178],
          15:[205.6976,
              196.8658,
              208.5370],
          16:[206.2030,
              203.7579,
              209.6985],
          17:[208.7963,
              207.6485,
              209.9476],
          18:[208.5188,
              208.4121,
              208.6248]
          }

with_aoa = {1:[19.4139,
               14.2331,
               21.5903],
            2:[20.4717,
               19.9074,
               20.9601],
            3:[20.4159,
               20.0864,
               20.6148
               ],
            4:[20.5162,
               20.3656,
               20.6309],
            5:[20.5102,
               20.4074,
               20.5892],
            6:[20.4917,
               20.4287,
               20.5485],
            7:[20.4717,
               20.4196,
               20.5196],
            8:[20.4574,
               20.4129,
               20.4993
               ],
            9:[20.4471,
               20.4083,
               20.4843],
            10:[20.4395,
                20.4048,
                20.4730],
            11:[20.4497,
                20.4170,
                20.4817
                ],
            12:[20.4583,
                20.4290,
                20.4870],
            13:[20.4627,
                20.4388,
                20.4865],
            14:[20.4643,
                20.4422,
                20.4879],
            15:[20.4691,
                20.4519,
                20.4920],
            16:[20.4850,
                20.4686,
                20.5080
                ],
            17:[20.4850,
                20.4686,
                20.5080],
            18:[20.4850,
                20.4686,
                20.5080]
            }

# plot error bar
x = []
y = []
yerr = []
for k, v in no_gps.items():
    u = (120.3735852,
         240.7824663,
         360.6113696,
         516.6123575,
         662.1859314,
         740.8104685,
         874.8063047,
         1022.24645,
         1081.829689,
         1201.829689,
         1320.745058,
         1451.173653,
         1562.6537,
         1680.858401,
         1863.265952,
         1989.468238,
         2120.810468,
         2176.312653)
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