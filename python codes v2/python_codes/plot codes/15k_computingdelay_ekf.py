import matplotlib.pyplot as plt
import numpy as np
time =('100-300', '1000-2000', '2000-3000')

min_seq= (0.004,0.008,0.017)
avg_seq = (0.042,0.26,0.36)
max_seq= (0.08,0.433,0.59)

min_apd = (0.01,0.012,0.019)
avg_apd = (0.29,2.5,3)
max_apd = (0.802,5.44,6.87)

min_ekf = (0.12,7.55,8.56)
avg_ekf = (25.1,216.68,272.13)
max_ekf = (70.6,376.27,460.13)

f, ax1 = plt.subplots()

ax1.plot(time,min_apd,linestyle='dotted',color="navy", label='$MVLA_{all}$ min (15k UEs)')
ax1.plot(time,avg_apd,linestyle='dotted',color="navy",marker='o', label='$MVLA_{all}$ mean (15 UEs)')
ax1.plot(time,max_apd,linestyle='dashed',color="navy",label='$MVLA_{all}$ max (15k UEs)')

ax1.plot(time,min_ekf,linestyle='dotted',color="saddlebrown", label='EKF min  (15k UEs)')
ax1.plot(time,avg_ekf,linestyle='dotted',color="saddlebrown",marker='o', label='EKF mean (15k UEs)')
ax1.plot(time,max_ekf,linestyle='dashed',color="saddlebrown",label='EKF max (15k UEs)')

#fill between the upper and lower bands
plt.fill_between(time, min_ekf, max_ekf, alpha = .1,color = 'saddlebrown')
plt.fill_between(time, min_apd, max_apd, alpha = .1,color = 'navy')

#add background grid for visual appeal
plt.grid(True, linestyle='dotted')

#ax1.legend(lns2, labs, loc=1, fontsize=10)
#ax1.legend(bbox_to_anchor=(0.05, 0), loc=3, borderaxespad=0.,  fontsize=8)
ax1.legend(loc='lower center', bbox_to_anchor= (0.0, 1.01), ncol=2,
          borderaxespad=0, frameon=False)
import matplotlib.font_manager as font_manager
font = font_manager.FontProperties(family='Arial',
                                   style='normal')
ax1.legend(prop=font)
plt.legend(fontsize=9) # using a size in points
ax1.tick_params(axis='both', which='major', labelsize=14)
for tick in ax1.get_xticklabels():
    tick.set_fontname("Arial")
for tick in ax1.get_yticklabels():
    tick.set_fontname("Arial")
#plt.yticks([0, 100000, 1200000, 1234614])
#plt.yticks(range(1, 1000000, 2000000), [1,1000,10000,100000,1000000])
plt.xlabel(r"number of emergency devices localized",fontname="Arial",fontsize=14)
plt.ylabel(r"computing delay (sec)",fontname="Arial",fontsize=14)
ax1.set_title("Computing delay against the number of localized devices" , fontname="Arial", fontsize=14)
#ax2.set_ylabel(r"average messages per node (Dr)",fontsize=14)
d = .015  # how big to make the diagonal lines in axes coordinates
plt.yscale('log')
#ax1.set_ylim(0.002, 1000)  # most of the data

from matplotlib import ticker
ax1.set_ylim(0.001,1000)
plt.yticks([0.001,0.01,0.1,1,10,100,1000])
formatter = ticker.ScalarFormatter(useMathText=True)
formatter.set_scientific(True)
formatter.set_powerlimits((-5,10))
ax1.yaxis.set_major_formatter(formatter)

plt.show()