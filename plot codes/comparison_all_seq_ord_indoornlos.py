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

all = (17.03312805,
       17.6124021,
       17.39557953,
       17.82945424,
       18.06648873,
       18.15178667,
       18.1975177,
       18.22191664,
       18.28704594,
       18.30465408,
       18.35795958,
       18.38296366,
       18.41348326,
       18.4579864,
       18.49003009
       )

time2 = (120.3735852,
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

seqall  = (17.80918842,
           18.72656512,
           18.60513684,
           18.64671357,
           18.53066768,
           18.47320797,
           18.49078567,
           18.39865287,
           18.35926677,
           18.7234257,
           18.74383441,
           18.69771562,
           18.89261576,
           19.06030452,
           19.19246775)

ordall = (16.94226285,
          18.51343328,
          18.72860452,
          18.89978794,
          18.81256121,
          18.77699846,
          18.74086643,
          18.68658557,
          18.67483337,
          18.90694166,
          19.00115967,
          18.94475647,
          19.12421778,
          19.21183504,
          19.25051218)


f, ax1 = plt.subplots()

ax1.set_ylim(16.8, 19.5)  # most of the data

#ax1.plot(time, seq)

#ax1.plot(time, nogps,linestyle='dashed',color="black")
#ax1.plot(time, nogps,linestyle='dashed',color="black")

#ax1.set_xlim(0.1,81)

ax1.grid(color='gray', alpha=0.5, linestyle='dashed', linewidth=0.5)

#legend
lns1 = ax1.plot(time2, ordall,color="orchid", marker="o", markersize=7, linestyle='dotted', label='$MVLA_{recent}$ (15k UEs)')
lns2 = ax1.plot(time2, seqall,color="forestgreen", marker="o", markersize=7, linestyle='dashed', label='$MVLA_{recents-seq}$ (15k UEs)')
lns3= ax1.plot(time2, all, color="navy", marker="o", markersize=7, label='$MVLA_{all}$ (15k UEs)')


#lns4 = ax1.plot(time, nogps, color="brown", marker="o", markersize=7, label='RSSI+TOA+AOA (15k UEs)')

lns = lns1+lns2+lns3
labs = [l.get_label() for l in lns]

for i in range(len(time2)):
    my_selected_date = time2[i]
    lnv1 = ax1.vlines(my_selected_date, 0, ordall[i]+0.03, linestyles ="dashed", colors ="brown", alpha=0.5,linewidth=1)   # changed
    #lnv2 = ax1.vlines(my_selected_date, 2.51, ekf[i]+0.005, linestyles ="dashed", colors ="orange",alpha=0.9,linewidth=0.5)   # changed
ax1.axvline(x=time2[0],ymin=0.0, ymax=0.03 ,label='localization update time',linestyle ="dashed", color ="brown", alpha=1,linewidth=0.5)
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
plt.text(250,19.35,'Technique: GPS+RSSI+TOA+AOA',fontsize=12,fontname="Arial")
plt.text(250,19.2,'# emergency devices: 340',fontsize=13,fontname="Arial")
plt.text(250,19.0,'emergency duration: 30 mins',fontsize=13,fontname="Arial")
plt.xlabel(r"time (sec)",fontname="Arial",fontsize=14)
plt.ylabel(r"root mean square error (m)",fontname="Arial",fontsize=14)
# ax1.set_title("Root mean squared error against time" , fontname="Arial", fontsize=14)
plt.show()
