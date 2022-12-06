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
ord = (180.0141,
       162.6310,
       170.0076,
       176.5033,
       177.0551,
       176.8184,
       176.0824,
       175.1748,
       175.5720,
       175.9503,
       181.1312,
       183.1969,
       183.9480,
       183.8042,
       193.7156)
minord = (32.0711,
          147.9094,
          163.6497,
          174.0681,
          175.0151,
          175.6687,
          175.3165,
          172.6738,
          174.7073,
          175.1289,
          179.1329,
          181.9560,
          183.2473,
          183.4355,
          191.3137)
maxord = (365.0543,
          175.3282,
          176.0741,
          178.6675,
          178.7597,
          177.8305,
          177.0123,
          177.7847,
          176.1458,
          177.1459,
          182.6861,
          184.1149,
          184.3764,
          184.1679,
          195.6826)

seq = (180.3662333,
       162.7462333,
       168.8225667,
       175.2124,
       175.7454667,
       175.6172752,
       174.8981,
       174.0182333,
       174.4387,
       174.8269333,
       180.0232667,
       182.1174333,
       182.9424,
       182.8811,
       192.5188
         )
minseq = (32.0711,
          147.9851,
          162.2619333,
          172.7328667,
          173.7809,
          174.4708752,
          174.1333667,
          171.5137,
          173.5703,
          174.0075,
          178.023,
          180.8657667,
          182.1843,
          182.5145,
          190.1079)

maxseq = (365.0542667,
          175.6151333,
          174.9819,
          177.3866,
          177.4956667,
          176.6252085,
          175.8227333,
          176.6290667,
          175.0112,
          176.0245333,
          181.5826667,
          183.0281667,
          183.2912,
          182.7801,
          194.4813)

apd = (181.1030,
       162.9641333,
       165.2636,
       165.8114,
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
       166.9673
       )


minapd=(32.0711,
        151.5564667,
        160.0896,
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
        166.2857,
        166.5694)

maxapd = (365.0543,
          180.4341,
          171.4429,
          169.5899,
          168.8974,
          168.2035,
          168.0424,
          167.8083,
          167.5803,
          167.4488,
          167.7601,
          167.9500,
          167.7133,
          167.6568,
          167.4240)

f, ax1 = plt.subplots()

ax1.grid(color='gray', alpha=0.5, linestyle='dashed', linewidth=0.5)

#legend
lns1 = ax1.plot(time, ord, color="orchid",marker="p", markersize=7, label='$MVLA_{recent}$ (15k UEs)')
#lns2 = ax1.plot(time, onlycellular,color="black",marker="d", markersize=7,  label='RSSI+TOA+AOA (15k UEs)')
lns3 = ax1.plot(time, seq,color="olive",marker="*", markersize=7, label='GPS+RSSI+TOA (15k UEs)')
lns4 = ax1.plot(time, apd, color="navy", marker="o", markersize=7, label='GPS+RSSI+TOA+AOA (15k UEs)')

#ax1.plot(time,minapd,linestyle='dotted',color="navy")
#ax1.plot(time,maxapd,linestyle='dotted',color="navy")
#ax1.plot(time,minord,linestyle='dotted',color="orchid")
#ax1.plot(time,maxord,linestyle='dotted',color="orchid")
#ax1.plot(time,minseq,linestyle='dotted',color="olive")
#ax1.plot(time,maxseq,linestyle='dotted',color="olive")

#ax1.plot(time,minonlycellular,linestyle='dotted',color="black")
#ax1.plot(time,maxonlycellular,linestyle='dotted',color="black")

#plt.fill_between(time, minapd, maxapd, alpha = .1,color = 'navy')
#plt.fill_between(time, minord, maxord, alpha = .1,color = 'orchid')
#plt.fill_between(time, minseq, maxseq, alpha = .1,color = 'olive')
#plt.fill_between(time, minonlycellular, maxonlycellular, alpha = .1,color = 'olive')
lns = lns1+lns3+lns4
labs = [l.get_label() for l in lns]

for i in range(len(time)):
    my_selected_date = time[i]
    lnv1 = ax1.vlines(my_selected_date, 0, maxord[i]+0.03, linestyles ="dashed", colors ="brown", alpha=0.5,linewidth=1)   # changed
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

ax1.set_ylim(160.0, 195.5)  # most of the data
ax1.tick_params(axis='both', which='major', labelsize=14)
plt.text(500,300,'# emergency devices: 340',fontsize=13,fontname="Arial")
plt.text(500,250,'emergency duration: 30 mins',fontsize=13,fontname="Arial")
plt.xlabel(r"time (sec)",fontname="Arial",fontsize=14)
plt.ylabel(r"root mean square error (m)",fontname="Arial",fontsize=14)
ax1.set_title("Root mean squared error against time" , fontname="Arial", fontsize=14)
plt.show()
