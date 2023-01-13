import matplotlib.pyplot as plt
import numpy as np

from matplotlib import rc
from matplotlib.ticker import AutoMinorLocator
import matplotlib.font_manager as font_manager

rc('mathtext', default='regular')

time = (1,3,5,7,10)

proposed = (247.8,217.8166667,213.2833333,206.95,198.16)
rssimcl = (265.6,244.4666667,236.7,234.6,232.4)

f, ax1 = plt.subplots()

ax1.grid(color='gray', alpha=0.5, linestyle='dashed', linewidth=0.5)

#legend
lns1 = ax1.plot(time, proposed, color="navy",marker="p", markersize=7, label=r'${MVLA}_{all} (15k UEs)$')
lns2 = ax1.plot(time, rssimcl ,color="saddlebrown",marker="d",linestyle='dashed', markersize=7,  label=r'${RSSI-MCL} (15k UEs)$')
lns = lns1+lns2
labs = [l.get_label() for l in lns]

ax1.legend(loc=2, fontsize=10)

font = font_manager.FontProperties(family='Arial', style='normal', size=12)
ax1.legend(prop=font)

d = .015  # how big to make the diagonal lines in axes coordinates
ax1.set_xticks(time)
for tick in ax1.get_xticklabels():
    tick.set_fontname("Arial")
for tick in ax1.get_yticklabels():
    tick.set_fontname("Arial")
ax1.set_ylim(190.0, 270)  # most of the data
ax1.set_xlim(1, 10)  # most of the data
ax1.tick_params(axis='both', which='major', labelsize=14)
plt.text(1.5,200.0,'# emergency devices: 340',fontsize=13,fontname="Arial")
plt.text(1.5,205.0,'emergency duration: 30 mins',fontsize=13,fontname="Arial")
plt.xlabel(r"number of functioning gNBs",fontname="Arial",fontsize=14)
plt.ylabel(r"average distance error (m)",fontname="Arial",fontsize=14)
#ax1.set_title("Average distance error against time", fontname="Arial", fontsize=14)
plt.show()
