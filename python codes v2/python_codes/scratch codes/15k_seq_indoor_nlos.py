import matplotlib.pyplot as plt
import numpy as np

from matplotlib import rc
from matplotlib.ticker import AutoMinorLocator

rc('mathtext', default='regular')
#from matplotlib.ticker import ScalarFormatter
#data
#15k average apd
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

seqonlycellular = (18.91319805,
                   19.67664152,
                   19.55987639,
                   19.59350714,
                   19.58527098,
                   19.64133493,
                   19.67547271,
                   19.70035996,
                   19.72084155,
                   19.71562251,
                   19.74590802,
                   19.75564133,
                   19.74709822,
                   19.72960223,
                   19.71232224)
seqnoaoa = (17.80918842,
            18.72656512,
            18.60513684,
            18.66820422,
            18.55549071,
            18.50425419,
            18.51694196,
            18.46043499,
            18.44008447,
            18.8301978,
            18.87567066,
            18.81429621,
            19.01600438,
            19.19154482,
            19.32663645)
seqonlygps = (24.35043074,
              26.45965764,
              26.47770315,
              26.99502853,
              26.83389007,
              26.94240032,
              27.2731122,
              27.38535422,
              27.43196861,
              27.70561804,
              28.07446796,
              28.07735357,
              28.16523911,
              28.31728592,
              28.4606571)

f, ax1 = plt.subplots()

ax1.set_ylim(11.8, 29.5)  # most of the data

#ax1.plot(time, seq)

#ax1.plot(time, nogps,linestyle='dashed',color="black")
#ax1.plot(time, nogps,linestyle='dashed',color="black")

#ax1.set_xlim(0.1,81)

ax1.grid(color='gray', alpha=0.5, linestyle='dashed', linewidth=0.5)

#legend
lns1 = ax1.plot(time2, seqonlygps, color="orange", label='GPS (15k UEs):SEQ')
lns2 = ax1.plot(time2, seqonlycellular,color="black",marker="d", markersize=7,  label='RSSI+TOA+AOA (15k UEs):SEQ')
lns3 = ax1.plot(time2, seqnoaoa,color="purple",marker="*", markersize=7, label='GPS+RSSI+TOA (15k UEs):SEQ')
lns4 = ax1.plot(time2, seqall, color="blue", marker="o", markersize=7, label='GPS+RSSI+TOA+AOA (15k UEs):SEQ')


#lns4 = ax1.plot(time, nogps, color="brown", marker="o", markersize=7, label='RSSI+TOA+AOA (15k UEs)')

lns = lns1+lns2+lns3
labs = [l.get_label() for l in lns]

for i in range(len(time2)):
    my_selected_date = time2[i]
    lnv1 = ax1.vlines(my_selected_date, 0, seqonlygps[i]+0.03, linestyles ="dashed", colors ="brown", alpha=0.5,linewidth=0.5)   # changed
    #lnv2 = ax1.vlines(my_selected_date, 2.51, ekf[i]+0.005, linestyles ="dashed", colors ="orange",alpha=0.9,linewidth=0.5)   # changed
ax1.axvline(x=time2[0],ymin=0.0, ymax=seqonlygps[0]+0.03 ,label='localization update time',linestyle ="dashed", color ="brown", alpha=0.2,linewidth=0.5)
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
plt.text(100,23.0,'# emergency devices: 340',fontsize=13,fontname="Arial")
plt.text(100,21.0,'emergency duration: 30 mins',fontsize=13,fontname="Arial")
plt.xlabel(r"time (sec)",fontname="Arial",fontsize=14)
plt.ylabel(r"root mean square error (m)",fontname="Arial",fontsize=14)
ax1.set_title("Root mean squared error against time" , fontname="Arial", fontsize=14)
plt.show()
