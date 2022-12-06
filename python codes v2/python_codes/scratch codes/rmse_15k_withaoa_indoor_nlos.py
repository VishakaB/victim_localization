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
noaoa = (26.55103869,
         27.69885244,
         27.44388822,
         27.64887809,
         27.6742002,
         27.81840486,
         27.87601696,
         27.7896875,
         27.73399408,
         27.77952508,
         27.82436123,
         27.85759423,
         27.90181065,
         27.93196233,
         27.92843934,
         27.90978783,
         27.95822668,
         27.9605148)
withaoa = (21.7301146,
           21.71013535,
           21.86305647,
           22.57047476,
           22.84445022,
           23.04210261,
           23.22941819,
           23.28162739,
           23.2432507,
           23.00343857,
           22.92303148,
           22.9314785,
           22.89889114,
           22.89393436,
           22.75232355,
           22.69911687,
           22.74152541,
           22.76599396,
           )

f, ax1 = plt.subplots()

ax1.set_ylim(20.75, 28.75)  # most of the data

#ax1.plot(time, seq)
ax1.plot(time, noaoa,linestyle='dashed',color="black")
ax1.plot(time, withaoa,linestyle='dashed',color="black")

#ax1.set_xlim(0.1,81)

ax1.grid(color='gray', alpha=0.5, linestyle='dashed', linewidth=0.5)

#legend
lns1 = ax1.plot(time, noaoa, color="orange", label='without AOA (15k UEs)')
lns2 = ax1.plot(time, withaoa, color="blue", marker="o", markersize=7, label='with AOA (15k UEs)')

lns = lns1+lns2
labs = [l.get_label() for l in lns]

for i in range(len(time)):
    my_selected_date = time[i]
    lnv1 = ax1.vlines(my_selected_date, 0, noaoa[i]+0.03, linestyles ="dashed", colors ="brown", alpha=0.5,linewidth=0.5)   # changed
    #lnv2 = ax1.vlines(my_selected_date, 2.51, ekf[i]+0.005, linestyles ="dashed", colors ="orange",alpha=0.9,linewidth=0.5)   # changed
ax1.axvline(x=time[0],ymin=0.0, ymax=noaoa[0]+0.03 ,label='localization update time',linestyle ="dashed", color ="brown", alpha=0.2,linewidth=0.5)
#ax1.legend(lns2, labs, loc=1, fontsize=10)
#ax1.legend(loc=4, fontsize=10)
ax1.legend(loc=4, fontsize=18)
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
plt.text(100,25.6,'# emergency devices: 340',fontsize=14,fontname="Arial")
plt.text(100,25.0,'emergency duration: 30 minutes',fontsize=14,fontname="Arial")
plt.show()
