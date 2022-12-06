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

id13125= (20.6011306,
           20.49243328,
           20.5563235,
           20.53822144,
           20.50718957,
           20.48415561,
           20.46773733,
           20.45605132,
           20.44738929,
           20.45424273,
           20.46237234,
           20.4687627,
           20.46973195,
           20.47232211,20.47292925)
id14011 = (20.58627875,
           20.60829376,
           20.57923361,
           20.54299594,
           20.51584774,
           20.49603089,
           20.48150803,
           20.47047672,
           20.47945427,
           20.48497901,
           20.48461494,
           20.48617094,
           20.48561867,
           20.49047666,
           20.50648171
           )
id10121 = (20.49769568,
           20.49678942,
           20.47744638,
           20.46146994,
           20.44957494,
           20.44095792,
           20.43449919,
           20.447055,
           20.45551788,
           20.45762145,
           20.46125741,
           20.46249337,
           20.46701309,
           20.48349783,
           20.48075825)
time2 = (1201.829689,
         1320.745058,
         1451.173653,
         1562.6537,
         1680.858401,
         1863.265952,
         1989.468238,
         2120.810468,
         2176.312653)

id12658=(20.44709534,
         20.45837549,
         20.46579873,
         20.46704113,
         20.46994779,
         20.47056043,
         20.47471634,
         20.49101823,
         20.48826302)

f, ax1 = plt.subplots()

ax1.set_ylim(20.4, 20.7)  # most of the data

#ax1.plot(time, seq)
ax1.plot(time, id13125,linestyle='dashed',color="black")
ax1.plot(time, id14011,linestyle='dashed',color="black")
ax1.plot(time, id10121,linestyle='dashed',color="black")
ax1.plot(time2, id12658,linestyle='dashed',color="black")
#ax1.set_xlim(0.1,81)

ax1.grid(color='gray', alpha=0.5, linestyle='dashed', linewidth=0.5)

#legend
lns1 = ax1.plot(time, id13125, color="orange", label='UE1 (15k UEs)')
lns2 = ax1.plot(time, id14011, color="blue", marker="o", markersize=7, label='UE2 (15k UEs)')
lns3 = ax1.plot(time, id10121, color="purple", marker="o", markersize=7, label='UE 3 (15k UEs)')
lns4 = ax1.plot(time2, id12658, color="green", marker="o", markersize=7, label='UE 4 (15k UEs)')
lns = lns1+lns2+lns3+lns4
labs = [l.get_label() for l in lns]

for i in range(len(time)):
    my_selected_date = time[i]
    lnv1 = ax1.vlines(my_selected_date, 0, id13125[i]+0.03, linestyles ="dashed", colors ="brown", alpha=0.5,linewidth=0.5)   # changed
    #lnv2 = ax1.vlines(my_selected_date, 2.51, ekf[i]+0.005, linestyles ="dashed", colors ="orange",alpha=0.9,linewidth=0.5)   # changed
ax1.axvline(x=time[0],ymin=0.0, ymax=id13125[0]+0.03 ,label='localization update time',linestyle ="dashed", color ="brown", alpha=0.2,linewidth=0.5)
#ax1.legend(lns2, labs, loc=1, fontsize=10)
#ax1.legend(loc=4, fontsize=10)
ax1.legend(loc=4, fontsize=18)
import matplotlib.font_manager as font_manager
font = font_manager.FontProperties(family='Arial',
                                   style='normal', size=12)
ax1.legend(prop=font)
ax1.set_title("Specific node error variation against time (Indoor NLOS)" , fontname="Arial", fontsize=14)

#ax2.set_xlabel("time (sec)",fontsize=14)
plt.xlabel(r"time (sec)",fontname="Arial",fontsize=14)
plt.ylabel(r"root mean square error (m)",fontname="Arial",fontsize=14)
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
plt.text(1000,20.55,'# emergency devices: 340',fontsize=14,fontname="Arial")
plt.text(1000,20.53,'emergency duration: 30 mins',fontsize=14,fontname="Arial")
plt.show()
