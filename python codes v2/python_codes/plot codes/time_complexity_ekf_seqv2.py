import matplotlib.pyplot as plt
import numpy as np
time =('100-300', '1000-2000', '2000-3000')

min_seq= (161,956,1117)
avg_seq = (8433,49157,60923.64286)
max_seq= (17004,78245,96005)

min_apd= (235,956,1117)
avg_apd = (36278,230791,252501)
max_apd= (129792,627186,702603)

min_ekf = (414,16986,19848)
avg_ekf = (75645,539693,666684)
max_ekf = (210060,844922,1034614)

f, ax1 = plt.subplots()

#ax1.plot(time,min_seq,linestyle='dotted',color="green", label='$MVLA_{recent-seq}$ min (15k UEs)')
#ax1.plot(time,avg_seq,linestyle='dotted',color="green",marker='o', label='$MVLA_{recent-seq}$ mean (15 UEs)')
#ax1.plot(time,max_seq,linestyle='dashed',color="green",label='$MVLA_{recent-seq}$ max (15k UEs)')

ax1.plot(time,min_apd,linestyle='dotted',color="navy", label='$MVLA_{all}$ min (15k UEs)')
ax1.plot(time,avg_apd,linestyle='dotted',color="navy",marker='o', label='$MVLA_{all}$ mean (15 UEs)')
ax1.plot(time,max_apd,linestyle='dashed',color="navy",label='$MVLA_{all}$ max (15k UEs)')

ax1.plot(time,min_ekf,linestyle='dotted',color="saddlebrown", label='EKF min  (15k UEs)')
ax1.plot(time,avg_ekf,linestyle='dotted',color="saddlebrown",marker='o', label='EKF mean (15k UEs)')
ax1.plot(time,max_ekf,linestyle='dashed',color="saddlebrown",label='EKF max (15k UEs)')

#fill between the upper and lower bands
plt.fill_between(time, min_ekf, max_ekf, alpha = .1,color = 'saddlebrown')
#plt.fill_between(time, min_seq, max_seq, alpha = .1,color = 'darkseagreen')
plt.fill_between(time, min_apd, max_apd, alpha = .1,color = 'navy')
#add background grid for visual appeal
plt.grid(True, linestyle='dotted')

#ax1.legend(lns2, labs, loc=1, fontsize=10)
#ax1.legend(loc=4, fontsize=10)
ax1.legend(loc=2, fontsize=14)
import matplotlib.font_manager as font_manager
font = font_manager.FontProperties(family='Arial',
                                   style='normal', size=10)
ax1.legend(prop=font)
plt.legend(fontsize=10) # using a size in points
ax1.tick_params(axis='both', which='major', labelsize=14)
plt.text(300,8.7,'# emergency devices: 340',fontsize=14,fontname="Arial")
plt.text(300,5.8,'emergency duration: 30 mins',fontsize=14,fontname="Arial")
plt.text(300,3.0,'GPS+RSSI+TOA+AOA',fontsize=11,fontname="Arial")
for tick in ax1.get_xticklabels():
    tick.set_fontname("Arial")
for tick in ax1.get_yticklabels():
    tick.set_fontname("Arial")
#plt.yticks([0, 100000, 1200000, 1234614])
#plt.yticks(range(1, 1000000, 2000000), [1,1000,10000,100000,1000000])
plt.xlabel(r"number of emergency devices localized",fontname="Arial",fontsize=14)
plt.ylabel(r"algorthm complexity",fontname="Arial",fontsize=14)
ax1.set_title("Algorthm complexity against the number of localized devices" , fontname="Arial", fontsize=14)
#ax2.set_ylabel(r"average messages per node (Dr)",fontsize=14)
d = .015  # how big to make the diagonal lines in axes coordinates
plt.yscale('log')
ax1.set_ylim(10, 1234614)  # most of the data
from matplotlib import ticker
ax1.set_ylim(-1000,1234614)
formatter = ticker.ScalarFormatter(useMathText=True)
#formatter.set_scientific(True)
formatter.set_powerlimits((-5,10))
ax1.yaxis.set_major_formatter(formatter)

plt.show()
plt.show()