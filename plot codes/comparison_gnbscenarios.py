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

allv3 = (138.9030,
147.3641,
148.9636,
152.9113667,
155.3202,
157.4228,
158.3342,
158.4237,
158.5496,
158.7623,
159.0832,
159.1234,
159.0449,
158.8147,
158.8673333)

min_apdallv3 = (31.67,
118.26,
139.89,
144.09,
150.28,
152.19,
154.83,
155.09,
155.21,
155.60,
156.14,
156.07,
156.17,
155.99,
156.17)

max_apdallv3 = (412.5542667,
154.8341,
150.5429,
155.7899,
155.8974,
158.5035,
158.7424,
158.7083,
158.6803,
158.7488333,
158.9601,
159.05,
158.8133,
158.5567667,
158.224)

allv2 = (163.9030,
150.3641,
154.8636,
157.7114,
158.3202,
158.6228,
159.0342,
159.1237,
159.2496,
159.4623,
159.7832,
159.8234,
159.7449,
159.5147,
159.5673)

min_apdallv2 = (120.47,
137.36,
145.69,
150.99,
153.18,
153.69,
154.33,
154.59,
154.71,
155.10,
155.64,
155.57,
155.67,
155.49,
155.67)

max_apdallv2 = (461.7542667,
194.8341,
170.7429,
164.3899,
164.3974,
164.2035,
164.4424,
164.4083,
164.3803,
164.4488333,
164.6601,
164.75,
164.5133,
164.2567667,
163.924)


f, ax1 = plt.subplots()

ax1.grid(color='gray', alpha=0.5, linestyle='dashed', linewidth=0.5)

#legend
lns3 = ax1.plot(time, all, color="navy", marker="o", markersize=7, label='gNB spread: Scenario 1 (15k UEs)')
lns4 = ax1.plot(time, allv2,color="saddlebrown",marker="d", markersize=7, label='gNB spread: Scenario 2 (15k UEs)')
lns5 = ax1.plot(time, allv3,color="darkcyan",marker="p", markersize=7, label='gNB spread: Scenario 3 (15k UEs)')

ax1.plot(time,min_apdall,linestyle='dotted',color="navy")
ax1.plot(time,max_apdall,linestyle='dotted',color="navy")
ax1.plot(time,min_apdallv2,linestyle='dotted',color="saddlebrown")
ax1.plot(time,max_apdallv2,linestyle='dotted',color="saddlebrown")
ax1.plot(time,min_apdallv3,linestyle='dashed',color="darkcyan")
ax1.plot(time,max_apdallv3,linestyle='dashed',color="darkcyan")

#ax1.plot(time,minonlycellular,linestyle='dotted',color="black")
#ax1.plot(time,maxonlycellular,linestyle='dotted',color="black")

plt.fill_between(time, min_apdall, max_apdall, alpha = .1,color = 'navy')
plt.fill_between(time, min_apdallv2, max_apdallv2, alpha = .3,color = 'saddlebrown')
plt.fill_between(time, min_apdallv3, max_apdallv3, alpha = .2,color = 'darkcyan')
#plt.fill_between(time, minonlycellular, maxonlycellular, alpha = .1,color = 'olive')
lns = lns3+lns4
labs = [l.get_label() for l in lns]

for i in range(len(time)):
    my_selected_date = time[i]
    lnv1 = ax1.vlines(my_selected_date, 0, max_apdall[i]+0.03, linestyles ="dashed", colors ="brown", alpha=0.5,linewidth=1)   # changed
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

ax1.set_ylim(125.0, 230.5)
ax1.set_xlim(121.0, 2108)  # most of the data
ax1.tick_params(axis='both', which='major', labelsize=14)
plt.text(1000,190,'# emergency devices: 340',fontsize=13,fontname="Arial")
plt.text(1000,183,'emergency duration: 30 mins',fontsize=13,fontname="Arial")
plt.xlabel(r"time (sec)",fontname="Arial",fontsize=14)
plt.ylabel(r"average distance error (m)",fontname="Arial",fontsize=14)
# ax1.set_title("Average distance error against time" , fontname="Arial", fontsize=14)
plt.show()
