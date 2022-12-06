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
ord = {1: [16.9423,
           4.0410,
           19.1185],
         2: [18.5134,
             17.8048,
             19.2669],
         3: [18.7286,
             18.0576,
             19.1717],
         4: [18.8998,
             18.8469,
             19.0005],
         5: [18.8126,
             18.7870,
             18.8393],
         6: [18.7770,
             18.7511,
             18.8022],
         7: [18.7409,
             18.7075,
             18.7747],
         8: [18.6866,
             18.6624,
             18.7093
             ],
         9: [18.6748],
         10: [18.9069,
              18.6752,
              19.0769],
         11: [19.0012,
              18.9783,
              19.0202
              ],
         12:[18.9448,
             18.9134,
             18.9813],
       13:[19.1242,
           18.8256,
           19.3185],
       14:[19.2118,
           19.1661,
           19.2580],
       15:[19.2505,
           19.1231,
           19.3526]}

seq = {1:[17.8092,
          4.0410,
          19.6653],
       2:[18.7266,
          18.2556,
          19.3739],
       3:[18.6051,
          18.0589,
          19.0557],
       4:[18.6467,
          18.5629,
          18.7566],
       5:[18.5307,
          18.4999,
          18.5684],
       6:[18.4732,
          18.4484,
          18.4985],
       7:[18.5234,
          18.5027,
          18.4797,
          18.4573],
       8:[18.3987,
          18.3636,
          18.4544],
       9:[18.3593],
       10:[18.7234,
           18.7092,
           18.7598],
       11:[18.7438,
           18.7224,
           18.7677],
       12:[18.7304,
           18.7111,
           18.6880,
           18.6913,
           18.6678],
       13:[18.8926,
           18.5902,
           19.2003],
       14:[19.1059,
           19.0835,
           19.0601,
           19.0373,
           19.0147],
       15:[19.1925,
           19.0177,
           19.2588]}

apd={1:[17.0331,
        4.0410,
        18.5670],
     2:[17.6124,
        17.1975,
        18.0755],
     3:[17.3956,
        17.1572,
        17.9140],
     4:[17.8295,
        17.6514,
        18.1466],
     5:[18.0665,
        17.9144,
        18.2157],
     6:[18.1518,
        18.0382,
        18.2722],
     7:[18.1975,
        18.0956,
        18.2987],
     8:[18.2219,
        18.1293,
        18.3062],
     9:[18.2870,
        18.2215,
        18.3513],
     10:[18.3047,
         18.2363,
         18.3950],
     11:[18.3580,
         18.2923,
         18.4205],
     12:[18.3830,
         18.3250,
         18.4381],
     13:[18.4135,
         18.3645,
         18.4753],
     14:[18.4580,
         18.4095,
         18.5170],
     15:[18.4900,
         18.4430,
         18.5435]
     }


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
for k2, v2 in seq.items():
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

plt.xlabel("time (sec)")
plt.ylabel('RMSE (m)')
plt.title("Indoor NLOS (Total number of emergency devices localized=343)")
plt.grid(color='gray', alpha=1, linestyle='dashed', linewidth=0.5)
#plt.grid(b=True, which='major', color='k', linestyle='-')

#legend
lns1 = plt.errorbar(x, y, yerr=yerr,
                    lw=2,color="blue", marker="o", markersize=7, linestyle='dotted', label='ORD: GPS+RSSI+TOA+AOA (15k UEs)')
lns2 = plt.errorbar(x2, y2, yerr=yerr2, color="blue", marker="o", markersize=7, linestyle='dashed', label='SEQ: GPS+RSSI+TOA+AOA (15k UEs)')
lns3 = plt.errorbar(x3, y3, yerr=yerr3,  color="blue", marker="o", markersize=7, label='APD: GPS+RSSI+TOA+AOA (15k UEs)')
#lns3 = ax1.plot(time, seq, color="red", marker="o", markersize=7, label='Sequential (only recent data) (5000 UEs)')
#lns4 = ax1.plot(time, apd, color="black", marker="s", markersize=7, label='All previous data (100 UEs)',linestyle='dashed')

lns = lns1+lns2+lns3
#+lns2+lns4
#lns1++lns4
#abs = [l.get_label() for l in lns]
plt.legend(loc=4,fontsize=10)

plt.savefig('ml_results.png')
plt.show()