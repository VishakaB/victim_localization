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
        1863.265952)
#success_rate_d = (0.71,0.63,0.59,0.48)

all = (17.70983155,
       18.01606474,
       18.12094931,
       18.14972028,
       18.14717244,
       18.17288315,
       18.18733337,
       18.21655335,
       18.23880387,
       18.27599645,
       18.29598304,
       18.31440707,
       18.34469128,
       18.37740888,
       18.40781757)

seqall  = (17.731965408,
           17.75860654,
           18.16478305,
           18.38045639,
           18.40853464,
           18.41359482,
           18.36328758,
           18.32117239,
           18.37005723,
           18.38610061,
           18.39210528,
           18.37026074,
           18.35544527,
           18.33700474,
           18.44818709)

ordall = (17.71650462,
          18.12224526,
          18.54849816,
          18.84431548,
          18.78290899,
          18.72305479,
          18.64532894,
          18.57475283,
          18.57845779,
          18.58026168,
          18.59530946,
          18.60689829,
          18.64987276,
          18.65385946,
          18.65056)

f, ax1 = plt.subplots()

ax1.set_ylim(17.5, 19.5)  # most of the data

#ax1.plot(time, seq)

#ax1.plot(time, nogps,linestyle='dashed',color="black")
#ax1.plot(time, nogps,linestyle='dashed',color="black")

#ax1.set_xlim(0.1,81)

ax1.grid(color='gray', alpha=0.5, linestyle='dashed', linewidth=0.5)

#legend
lns1 = ax1.plot(time, ordall,color="orchid", marker="o", markersize=7, linestyle='dotted', label='$MVLA_{recent}$ (15k UEs)')
lns2 = ax1.plot(time, seqall,color="forestgreen", marker="o", markersize=7, linestyle='dashed', label='$MVLA_{recents-seq}$ (15k UEs)')
lns3= ax1.plot(time, all, color="navy", marker="o", markersize=7, label='$MVLA_{all}$ (15k UEs)')


#lns4 = ax1.plot(time, nogps, color="brown", marker="o", markersize=7, label='RSSI+TOA+AOA (15k UEs)')

lns = lns1+lns2+lns3
labs = [l.get_label() for l in lns]

for i in range(len(time)):
    my_selected_date = time[i]
    lnv1 = ax1.vlines(my_selected_date, 0, ordall[i]+0.03, linestyles ="dashed", colors ="brown", alpha=0.5,linewidth=1)   # changed
    #lnv2 = ax1.vlines(my_selected_date, 2.51, ekf[i]+0.005, linestyles ="dashed", colors ="orange",alpha=0.9,linewidth=0.5)   # changed
ax1.axvline(x=time[0],ymin=0.0, ymax=0.03 ,label='localization update time',linestyle ="dashed", color ="brown", alpha=1,linewidth=0.5)
#ax1.legend(lns2, labs, loc=1, fontsize=10)
#ax1.legend(loc=4, fontsize=10)
ax1.legend(loc=2, fontsize=10)
import matplotlib.font_manager as font_manager
font = font_manager.FontProperties(family='Arial',
                                   style='normal', size=12)
ax1.legend(prop=font)


#ax2.set_xlabel("time (sec)",fontsize=14)

#ax2.set_ylabel(r"average messages per node (Dr)",fontsize=14)
d = .015  # how big to make the diagonal lines in axes coordinates
# arguments to pass to plot, just so we don't keep repeating them


# single vline with specific ymin and ymax
#ax2.vlines(x=39.25, ymin=25, ymax=150, colors='green', ls=':', lw=2, label='vline_single - partial height')

# place legend outside
#ax1.legend(loc=1)

for tick in ax1.get_xticklabels():
    tick.set_fontname("Arial")
for tick in ax1.get_yticklabels():
    tick.set_fontname("Arial")

ax1.tick_params(axis='both', which='major', labelsize=14)
plt.text(900,17.9,'Technique: GPS+RSSI+TOA+AOA',fontsize=12,fontname="Arial")
plt.text(900,17.75,'# emergency devices: 340',fontsize=13,fontname="Arial")
plt.text(900,17.550,'emergency duration: 30 mins',fontsize=13,fontname="Arial")
plt.xlabel(r"time (sec)",fontname="Arial",fontsize=14)
plt.ylabel(r"root mean square error (m)",fontname="Arial",fontsize=14)
ax1.set_title("Root mean squared error against time" , fontname="Arial", fontsize=14)
plt.show()
