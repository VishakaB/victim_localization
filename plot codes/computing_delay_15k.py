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
        1863.265952)
#success_rate_d = (0.71,0.63,0.59,0.48)
ord = (0.002,
       0.003,
       0.008,
       0.015,
       0.019,
       0.026,
       0.027,
       0.033,
       0.035,
       0.04,
       0.042,
       0.055,
       0.064,
       0.07,
       0.073)

apd = (0.002,
       0.023,
       0.04,
       0.052,
       0.071,
       0.093,
       0.117,
       0.149,
       0.184,
       0.224,
       0.272,
       0.334,
       0.401,
       0.483,
       0.567
)

seq_ord = (0.002,
           0.01,
           0.014,
           0.016,
           0.027,
           0.03,
           0.038,
           0.043,
           0.045,
           0.05,
           0.058,
           0.064,
           0.07,
           0.076,
           0.08)


#D_r = (0.19, 0.14, 0,.06, 0.03)
#D_r_1 = (36.75, 15.94, 10.13, 2.69)
#arrayY = (0.3,0.39,0.47,0.51,0.6,0.65,0.72,0.76,1)
#arrayD = (0.03, 0.06, 0.14, 0.19,  2.69, 10.13, 15.94, 36.75)
#noc10k = (1,50,100,300,500,800)
#success_rate_d = (0.9,0.7,0.62,0.48)
#success_rate_d10k = (1,0.95,0.84,0.66,0.58,0.5)
#success_rate10k = (1,0.77,0.64,0.5, 0.38, 0.3)
#D_r = (0.19, 0.14, 0.06, 0.03)
#D_r_1 = (36.75, 15.94, 10.13, 2.69)
#arrayY10k = (0.3,0.38,0.5,0.6,0.64,0.66,0.77,0.84,0.95,1)
#put labels to all data points



#success_rate_d = (0.79,0.74,0.57,0.43)
#success_rate_d15k = (1,0.98,0.75,0.69,0.55,0.43)
#success_rate15k = (1,0.98,0.51,0.48,0.32,0.28)
# Create a subplots and twin axes
f, ax1 = plt.subplots()

#ax1.set_xlim(0.1,81)

ax1.grid(color='gray', alpha=0.5, linestyle='dashed', linewidth=0.5)
#ax2.grid(color='gray', alpha=0.5, linestyle='dashed', linewidth=0.5)
#saving and showing fig


#legend
lns1 = ax1.plot(time, ord, color="orchid",  marker="p",linestyle='dotted', markersize=10,label='$MVLA_{recent}$ (15k UEs)')
lns2 = ax1.plot(time, seq_ord, color="forestgreen",linestyle='dashed', marker="*", markersize=7, label='$MVLA_{seq}$ (15k UEs)')
#lns3 = ax1.plot(time, seq, color="red", marker="o", markersize=7, label='Sequential (only recent data) (5000 UEs)')
lns3 = ax1.plot(time, apd, color="navy", marker="o", markersize=7, label='$MVLA_{all}$ (15k UEs)')

#lns3 = ax1.plot(noc, success_rate_d10k, color="black",linestyle='dashed', label='AM-HELP (1000 UEs)')
#lns4= ax1.plot(noc, success_rate10k, color="black", marker="*",linestyle='dashed', markersize=7, label='M-HELP (1000 UEs)')
#lns5 = ax1.plot(noc, success_rate_d15k, color="black",linestyle='dotted', label='AM-HELP (4000 UEs)')
#lns6= ax1.plot(noc, success_rate15k, color="black", marker="*",linestyle='dotted', markersize=7, label='M-HELP (4000 UEs)')
#lns3 = ax2.plot(time, D_r, color="black", marker="D", markersize=5, label='Dr: gNB = 8')
#lns4 = ax2.plot(time, D_r_1, color="black", marker="d", markersize=5, label='Dr : gNB = 1')
lns = lns1+lns2+lns3
#+lns4
#lns1++lns4
#
labs = [l.get_label() for l in lns]
#ax1.legend(lns, labs, loc=2, fontsize=10)


for i in range(len(time)):
    my_selected_date = time[i]
    lnv1 = ax1.vlines(my_selected_date, 0, apd[i]+0.03, linestyles ="dashed", colors ="brown", alpha=0.5,linewidth=0.5)   # changed
    #lnv2 = ax1.vlines(my_selected_date, 2.51, ekf[i]+0.005, linestyles ="dashed", colors ="orange",alpha=0.9,linewidth=0.5)   # changed
ax1.axvline(x=time[0],ymin=0, ymax=apd[0]+0.03 ,label='localization update time',linestyle ="dashed", color ="brown", alpha=0.2,linewidth=0.5)
#ax1.legend(lns2, labs, loc=1, fontsize=10)
#ax1.legend(loc=4, fontsize=10)
ax1.legend(loc=7, fontsize=10)
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
ax1.tick_params(axis='both', which='major', labelsize=14)
#ax1.set_yticks([0, 50, 100, 150])
plt.yscale('log')
from matplotlib import ticker
ax1.set_ylim(-100,1)
formatter = ticker.ScalarFormatter(useMathText=True)
formatter.set_scientific(True)
formatter.set_powerlimits((-1,1))
ax1.yaxis.set_major_formatter(formatter)
plt.text(1000,0.01,'# emergency devices: 340',fontsize=13,fontname="Arial")
plt.text(1000,0.006,'emergency duration: 30 mins',fontsize=13,fontname="Arial")
plt.xlabel(r"time (sec)",fontname="Arial",fontsize=14)
plt.ylabel(r"computing delay (sec)",fontname="Arial",fontsize=14)
ax1.set_title("Computing delay against time" , fontname="Arial", fontsize=14)
plt.show()
