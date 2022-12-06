import matplotlib.pyplot as plt
import numpy as np

from matplotlib import rc
from matplotlib.ticker import AutoMinorLocator

rc('mathtext', default='regular')
#from matplotlib.ticker import ScalarFormatter
#data
#15k average apd
time = (1,2,3,4,5,6,7,8,9,10,11,12,13,14)
#success_rate_d = (0.71,0.63,0.59,0.48)

apd = (0.4363362767,	0.4312036777,	0.4049131111,	0.392865576,	0.4088113215,	0.4226709317,	0.4013775403,	0.3761452016,	0.3810867183,	0.3986258023,	0.3683381509,	0.3729631101,	0.3440961738,	0.35)
apdv2 =(0.4355889617,0.4050002999,0.4084523456,0.3914539909,0.3915902618,0.3937047904,0.4029627515,0.3793977105,0.3727034082,0.3998675998,0.3721665057,0.3586819422,0.3476453184,0.3451899363)
f, ax1 = plt.subplots()



ax1.grid(color='gray', alpha=0.5, linestyle='dashed', linewidth=0.5)

#legend
#lns1 = ax1.plot(time, ordall,color="orchid", marker="o", markersize=7, linestyle='dotted', label='$MVLA_{recent}$ (15k UEs)')
#lns2 = ax1.plot(time, seqall,color="forestgreen", marker="o", markersize=7, linestyle='dashed', label='$MVLA_{recents-seq}$ (15k UEs)')
lns3= ax1.plot(time, apd, color="navy", marker="o", markersize=7, label='# devices localized = 100-300')
lns4= ax1.plot(time, apdv2, color="navy", marker="o", linestyle ="dashed",markersize=7, label='# devices localized = 1000-2000')

#lns4 = ax1.plot(time, nogps, color="brown", marker="o", markersize=7, label='RSSI+TOA+AOA (15k UEs)')

lns = lns3
labs = [l.get_label() for l in lns]

for i in range(len(time)):
    my_selected_date = time[i]
    lnv1 = ax1.vlines(my_selected_date, 0, apd[i]+0.03, linestyles ="dashed", colors ="brown", alpha=0.5,linewidth=1)   # changed
    #lnv2 = ax1.vlines(my_selected_date, 2.51, ekf[i]+0.005, linestyles ="dashed", colors ="orange",alpha=0.9,linewidth=0.5)   # changed
ax1.axvline(x=time[0],ymin=0.0, ymax=0.03 ,label='localization update time',linestyle ="dashed", color ="brown", alpha=1,linewidth=0.5)
#ax1.legend(lns2, labs, loc=1, fontsize=10)
#ax1.legend(loc=4, fontsize=10)

import matplotlib.font_manager as font_manager
font = font_manager.FontProperties(family='Arial',
                                   style='normal', size=12)
ax1.legend(prop=font)

d = .015  # how big to make the diagonal lines in axes coordinates


for tick in ax1.get_xticklabels():
    tick.set_fontname("Arial")
for tick in ax1.get_yticklabels():
    tick.set_fontname("Arial")
ax1.set_ylim(0.33, 0.45)  # most of the data
ax1.tick_params(axis='both', which='major', labelsize=14)
plt.text(2,0.75,'Technique: GPS+RSSI+TOA+AOA',fontsize=12,fontname="Arial")
#plt.text(900,17.75,'# emergency devices: 340',fontsize=13,fontname="Arial")
plt.text(2,0.65,'emergency duration: 30 mins',fontsize=13,fontname="Arial")
plt.xlabel(r"number of updates",fontname="Arial",fontsize=14)
plt.ylabel(r"estimated area of localization/total network area",fontname="Arial",fontsize=14)
ax1.set_title("Area of localization per network area against number of updates" , fontname="Arial", fontsize=14)
plt.show()
