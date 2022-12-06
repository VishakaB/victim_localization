import matplotlib.pyplot as plt
import numpy as np

from matplotlib import rc
from matplotlib.ticker import AutoMinorLocator

rc('mathtext', default='regular')
#from matplotlib.ticker import ScalarFormatter
#data
#15k average apd
time = (120.3735852,
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
#success_rate_d = (0.71,0.63,0.59,0.48)
noaoa = (15.55673312,
         67.66186058,
         73.48032056,
         102.2243368,
         147.0463688,
         161.8714382,
         176.1862696,
         194.0903014,
         209.2607431,
         221.7326402,
         231.7090477,
         238.5009381,
         250.2496847,
         260.170653,
         267.5446546,
         269.9589754,
         208.7962793,
         208.5187704)
withaoa = (19.90199178,
           20.1276278,
           20.13571681,
           20.18670604,
           20.19379776,
           20.19819237,
           20.19773462,
           20.19306443,
           20.18829446,
           20.18434045,
           20.18236204,
           20.18480607,
           20.22707086,
           20.21920988,
           20.22297988,
           20.58258733,
           20.48503687,
           20.48558241
           )

f, ax1 = plt.subplots()

ax1.set_ylim(0, 300)  # most of the data
#ax1.set_xlim(0.1,81)

#ax1.set_yscale('log')
ax1.plot(time, noaoa,linestyle='dashed',color="black")
ax1.plot(time, withaoa,linestyle='dashed',color="black")


ax1.grid(color='gray', alpha=0.5, linestyle='dashed', linewidth=0.5)

#legend
lns1 = ax1.plot(time, noaoa, color="orange", label='without GPS (RSSI+TOA+AOA) (15k UEs)')
lns2 = ax1.plot(time, withaoa, color="blue", marker="o", markersize=7, label='with GPS (GPS+RSSI+TOA+AOA) (15k UEs)')

lns = lns1+lns2
labs = [l.get_label() for l in lns]

for i in range(len(time)):
    my_selected_date = time[i]
    lnv1 = ax1.vlines(my_selected_date, 0, noaoa[i]+0.03, linestyles ="dashed", colors ="brown", alpha=0.5,linewidth=0.5)   # changed
    #lnv2 = ax1.vlines(my_selected_date, 2.51, ekf[i]+0.005, linestyles ="dashed", colors ="orange",alpha=0.9,linewidth=0.5)   # changed
ax1.axvline(x=time[0],ymin=0.0, ymax=noaoa[0]+0.03 ,label='localization update time',linestyle ="dashed", color ="brown", alpha=0.2,linewidth=0.5)
#ax1.legend(lns2, labs, loc=1, fontsize=10)
#ax1.legend(loc=4, fontsize=10)
ax1.legend(loc="upper center", bbox_to_anchor=(0.5, 1.15), ncol=2, fontsize=12)
import matplotlib.font_manager as font_manager
font = font_manager.FontProperties(family='Arial',
                                   style='normal', size=12)
ax1.legend(prop=font)
ax1.set_title("root mean squared error against time (Indoor NLOS)" , fontname="Arial", fontsize=14)

#ax2.set_xlabel("time (sec)",fontsize=14)
plt.xlabel(r"time (sec)",fontname="Arial",fontsize=14)
plt.ylabel(r"root mean square error (m)",fontname="Arial",fontsize=14)
#ax2.set_ylabel(r"average messages per node (Dr)",fontsize=14)
d = .015  # how big to make the diagonal lines in axes coordinates
# arguments to pass to plot, just so we don't keep repeating them

for tick in ax1.get_xticklabels():
    tick.set_fontname("Arial")
for tick in ax1.get_yticklabels():
    tick.set_fontname("Arial")

ax1.tick_params(axis='both', which='major', labelsize=14)
plt.text(100,220.6,'# emergency devices: 340',fontsize=14,fontname="Arial")
plt.text(100,200.5,'emergency duration: 30 minutes',fontsize=14,fontname="Arial")
plt.show()
