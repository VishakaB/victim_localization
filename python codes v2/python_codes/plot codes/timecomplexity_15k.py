import matplotlib.pyplot as plt
import numpy as np

from matplotlib import rc
from matplotlib.ticker import AutoMinorLocator

rc('mathtext', default='regular')
#from matplotlib.ticker import ScalarFormatter
#data
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
ord = (100,
       787,
       1535,
       2553,
       3719,
       4525,
       5158,
       6287,
       6550,
       8271,
       9083,
       10764,
       12949,
       14310,
       15366,
       16160,
       16641,
       17006)
seq_ord = (100,
           787,
           1535,
           2553,
           3719,
           4525,
           5158,
           6285,
           6548,
           8269,
           9081,
           10762,
           12947,
           14308,
           15364,
           16158,
           16639,
           17004
           )
apd = (
    100,
    948,
    2483,
    5036,
    8751,
    13270,
    18422,
    24703,
    31247,
    39512,
    48589,
    59347,
    72290,
    86594,
    101954,
    117947,
    133797,
    149264
)

ekf = (414,
       2051,
       5013,
       9497,
       15633,
       22830,
       30895,
       40450,
       50331,
       62415,
       75647,
       90913,
       108717,
       128099,
       148647,
       169739,
       190266,
       210060)


# Create a subplots and twin axes
f, ax1 = plt.subplots()

ax1.plot(time, ord, color="orchid")
#ax1.plot(time, seq)
ax1.plot(time, apd,linestyle='dashed',color="forestgreen")
ax1.plot(time, seq_ord,linestyle='dashed',color="blue")
#ax1.plot(time, ekf)
#ax1.plot(noc, success_rate_d10k,color="black",linestyle='dashed')
#ax1.plot(noc, success_rate10k,marker="*",color="black",linestyle='dashed')
#ax1.plot(noc, success_rate_d15k,color="black",linestyle='dotted')
#ax1.plot(noc, success_rate15k,marker="*",color="black",linestyle='dotted')
#ax1.set_ylim(-10,100000)


#limits


#ax1.set_xlim(0.1,81)

ax1.grid(color='gray', alpha=0.5, linestyle='dashed', linewidth=0.5)
#ax2.grid(color='gray', alpha=0.5, linestyle='dashed', linewidth=0.5)
#saving and showing fig


#legend
lns1 = ax1.plot(time, ord, color="orchid",  marker="o",linestyle='dotted', markersize=10,label='$MVLA_{recent}$ (15k UEs)')
lns2 = ax1.plot(time, seq_ord, color="forestgreen",linestyle='dashed', marker="o", markersize=7, label='$MVLA_{recent-seq} (15k UEs)$')
#lns3 = ax1.plot(time, seq, color="red", marker="o", markersize=7, label='Sequential (only recent data) (5000 UEs)')
lns3 = ax1.plot(time, apd, color="navy", marker="o", markersize=7, label='$MVLA_{all}$ (15k UEs)')
#lns4 = ax1.plot(time, ekf, color="sandybrown", marker="P", markersize=7, label='EKF (15k UEs)')

lns = lns1+lns2+lns3

#+lns4
#lns1++lns4
#
labs = [l.get_label() for l in lns]
ax1.legend(lns, labs, loc=2, fontsize=10)


for i in range(len(time)):
    my_selected_date = time[i]
    lnv1 = ax1.vlines(my_selected_date, -0.0, ekf[i]+0.03, linestyles ="dashed", colors ="brown", alpha=0.5,linewidth=1)   # changed
    #lnv2 = ax1.vlines(my_selected_date, 2.51, ekf[i]+0.005, linestyles ="dashed", colors ="orange",alpha=0.9,linewidth=0.5)   # changed
ax1.axvline(x=time[0],ymin=-0.0, ymax=0.03 ,label='localization update time',linestyle ="dashed", color ="brown", alpha=1,linewidth=0.5)
#ax1.legend(lns2, labs, loc=1, fontsize=10)
#ax1.legend(loc=4, fontsize=10)
ax1.legend(loc=2, fontsize=10)
import matplotlib.font_manager as font_manager
font = font_manager.FontProperties(family='Arial',
                                   style='normal', size=12)
ax1.legend(prop=font)

#+lns3+lns4+lns5+lns6
#+lns3+lns4

#labels

#ax2.set_ylabel(r"average messages per node (Dr)",fontsize=14)
ax1.tick_params(axis='both', which='major', labelsize=11)
for tick in ax1.get_xticklabels():
    tick.set_fontname("Arial")
for tick in ax1.get_yticklabels():
    tick.set_fontname("Arial")

ax1.tick_params(axis='both', which='major', labelsize=14)
plt.yscale('log')
from matplotlib import ticker
ax1.set_ylim(-100,400000)
formatter = ticker.ScalarFormatter(useMathText=True)
formatter.set_scientific(True)
formatter.set_powerlimits((-0,7))
ax1.yaxis.set_major_formatter(formatter)
plt.text(100,110000.0,'# emergency devices: 340',fontsize=13,fontname="Arial")
plt.text(100,50000.0,'emergency duration: 30 mins',fontsize=13,fontname="Arial")
plt.text(100,30000.0,'Technique:',fontsize=12,fontname="Arial")
plt.text(100,20000.0,'GPS+RSSI+TOA+AOA',fontsize=12,fontname="Arial")
plt.xlabel(r"time (sec)",fontname="Arial",fontsize=14)
plt.ylabel(r"algorithm complexity",fontname="Arial",fontsize=14)
ax1.set_title("Algorithm complexity against time" , fontname="Arial", fontsize=14)
plt.show()
