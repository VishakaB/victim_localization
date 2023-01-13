import matplotlib.pyplot as plt
import numpy as np

from matplotlib import rc
from matplotlib.ticker import AutoMinorLocator

rc('mathtext', default='regular')
#from matplotlib.ticker import ScalarFormatter
#data
#15k average apd
time = (121.3333187,
        240.3017934,
        361.7600284,
        481.7971508,
        606.8551306,
        739.4784034,
        841.5119859,
        985.2494326,
        1082.049853,
        1211.674369,
        1324.038277,
        1568.091496,
        1688.091496,
        1801.94405,
        2108.409799)
#success_rate_d = (0.71,0.63,0.59,0.48)
onlygps = (216.9342,
           187.1696,
           191.4039,
           193.4143667,
           194.4959,
           195.3936,
           195.9721667,
           196.3446,
           196.6202,
           196.9657,
           197.2396,
           197.4619,
           198.0428,
           198.2224,
           198.5032)
noaoa = (182.2426,
         165.5483,
         171.9112,
         172.6430,
         173.1945,
         173.6592,
         173.9753,
         174.2993,
         174.5428,
         174.9150,
         175.3002,
         175.5316,
         175.8694,
         175.9139,
         176.1148
         )

all = (181.103,
       162.9641333,
       165.2636333,
       165.8113667,
       166.1202,
       166.1228,
       166.3342,
       166.3237,
       166.2496,
       166.3623,
       166.7832,
       166.9234,
       166.9449,
       166.9147,
       166.9673333
       )

min_apdall = (32.0711,
              151.5564667,
              160.0896333,
              162.3924,
              163.6816,
              164.2936,
              164.7305,
              164.9912,
              165.1145,
              165.4046,
              165.9426,
              166.0688,
              166.2667,
              166.2856667,
              166.5694)
max_apdall = (365.0542667,
              180.4341,
              171.4428667,
              169.5898667,
              168.8974,
              168.2035,
              168.0424,
              167.8083,
              167.5803,
              167.4488333,
              167.7601,
              167.9500,
              167.7133,
              167.6567667,
              167.4240)
minnoaoa =(32.0711,
           155.2067,
           165.8870,
           168.9590,
           170.5712,
           171.5870,
           172.2429,
           172.8884,
           173.3298,
           173.8783,
           174.3676,
           174.6145,
           175.1590,
           175.2543,
           175.6954)
maxnoaoa = (365.054,
            186.2092,
            177.8212,
            176.2845,
            175.9361,
            175.7142,
            175.7377,
            175.7538,
            175.8194,
            176.0011,
            176.3016,
            176.5223,
            176.6903,
            176.6198,
            176.5536)

minonlygps = (32.0711,
              172.3161,
              184.5655,
              189.3316,
              191.4908,
              193.0211,
              194.0093667,
              194.6720,
              195.1460,
              195.6536,
              196.0573,
              196.3862,
              197.1001,
              197.4343,
              198.0281)
maxonlygps = (467.5423,
              210.5822,
              199.4017,
              198.1361,
              198.0512,
              198.1296,
              198.1956,
              198.2168,
              198.2542,
              198.4203,
              198.5501,
              198.6543,
              199.1361,
              199.1483,
              199.0420)

f, ax1 = plt.subplots()

ax1.grid(color='gray', alpha=0.5, linestyle='dashed', linewidth=0.5)

#legend
lns1 = ax1.plot(time, onlygps, color="olive",marker="p", markersize=7, label='GPS (15k UEs)')
#lns2 = ax1.plot(time, onlycellular,color="black",marker="d", markersize=7,  label='RSSI+TOA+AOA (15k UEs)')
lns3 = ax1.plot(time, noaoa,color="chocolate",marker="*", markersize=7, label='GPS+RSSI+TOA (15k UEs)')
lns4 = ax1.plot(time, all, color="navy", marker="o", markersize=7, label='GPS+RSSI+TOA+AOA (15k UEs)')

ax1.plot(time,min_apdall,linestyle='dotted',color="navy")
ax1.plot(time,max_apdall,linestyle='dotted',color="navy")
ax1.plot(time,minonlygps,linestyle='dotted',color="olive")
ax1.plot(time,maxonlygps,linestyle='dotted',color="olive")
ax1.plot(time,minnoaoa,linestyle='dotted',color="chocolate")
ax1.plot(time,maxnoaoa,linestyle='dotted',color="chocolate")

#ax1.plot(time,minonlycellular,linestyle='dotted',color="black")
#ax1.plot(time,maxonlycellular,linestyle='dotted',color="black")

plt.fill_between(time, min_apdall, max_apdall, alpha = .1,color = 'navy')
plt.fill_between(time, minonlygps, maxonlygps, alpha = .1,color = 'olive')
plt.fill_between(time, minnoaoa, maxnoaoa, alpha = .1,color = 'chocolate')
#plt.fill_between(time, minonlycellular, maxonlycellular, alpha = .1,color = 'olive')
lns = lns1+lns3+lns4
labs = [l.get_label() for l in lns]

for i in range(len(time)):
    my_selected_date = time[i]
    lnv1 = ax1.vlines(my_selected_date, 0, onlygps[i]+0.03, linestyles ="dashed", colors ="brown", alpha=0.5,linewidth=1)   # changed
    #lnv2 = ax1.vlines(my_selected_date, 2.51, ekf[i]+0.005, linestyles ="dashed", colors ="orange",alpha=0.9,linewidth=0.5)   # changed
ax1.axvline(x=time[0],ymin=0.0, ymax=0.03 ,label='localization update time',linestyle ="dashed", color ="brown", alpha=1,linewidth=0.5)
#ax1.legend(lns2, labs, loc=1, fontsize=10)
#ax1.legend(loc=4, fontsize=10)
ax1.legend(loc=2, fontsize=10)
import matplotlib.font_manager as font_manager
font = font_manager.FontProperties(family='Arial',
                                   style='normal', size=12)
ax1.legend(prop=font)

d = .015  # how big to make the diagonal lines in axes coordinates

for tick in ax1.get_xticklabels():
    tick.set_fontname("Arial")
for tick in ax1.get_yticklabels():
    tick.set_fontname("Arial")

ax1.set_ylim(150.0, 230.5)
ax1.set_xlim(121.0, 2108)  # most of the data
ax1.tick_params(axis='both', which='major', labelsize=14)
plt.text(1000,190,'# emergency devices: 340',fontsize=13,fontname="Arial")
plt.text(1000,183,'emergency duration: 30 mins',fontsize=13,fontname="Arial")
plt.xlabel(r"time (sec)",fontname="Arial",fontsize=14)
plt.ylabel(r"average distance error (m)",fontname="Arial",fontsize=14)
# ax1.set_title("Average distance error against time" , fontname="Arial", fontsize=14)
plt.show()
