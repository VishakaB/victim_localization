import matplotlib.pyplot as plt
import numpy as np
time =('100-300', '1000-2000', '2000-3000')

avg_seq= (18.62336991,22.45711697,21.91932224)
min_seq = (17.80918842,17.74479224,17.85090852)
max_seq= (19.19246775,23.29975537,22.72100787)

avg_ekf = (42.83009142,43.92820304,43.80452747)
min_ekf = (33.32571637,32.47716209,32.62508046)
max_ekf = (47.90273175,46.65513684,46.40409082)

f, ax1 = plt.subplots()

ax1.plot(time,min_seq,linestyle='dotted',color="green", label='$MVLA_{recent-seq}$ min')
ax1.plot(time,avg_seq,linestyle='dotted',color="green",marker='o', label='$MVLA_{recent-seq}$ mean')
ax1.plot(time,max_seq,linestyle='dashed',color="green",label='$MVLA_{recent-seq}$ max')

ax1.plot(time,min_ekf,linestyle='dotted',color="saddlebrown", label='EKF min  (15k UEs)')
ax1.plot(time,avg_ekf,linestyle='dotted',color="saddlebrown",marker='o', label='EKF mean (15k UEs)')
ax1.plot(time,max_ekf,linestyle='dashed',color="saddlebrown",label='EKF max (15k UEs)')

#fill between the upper and lower bands
plt.fill_between(time, min_ekf, max_ekf, alpha = .1,color = 'saddlebrown')
plt.fill_between(time, min_seq, max_seq, alpha = .1,color = 'darkseagreen')


#add background grid for visual appeal
plt.grid(True, linestyle='dotted')
plt.legend()

#ax1.legend(lns2, labs, loc=1, fontsize=10)
#ax1.legend(loc=4, fontsize=10)
ax1.legend(loc=2, fontsize=14)
import matplotlib.font_manager as font_manager
font = font_manager.FontProperties(family='Arial',
                                   style='normal', size=12)
ax1.legend(prop=font)
plt.legend(fontsize=9) # using a size in points
ax1.tick_params(axis='both', which='major', labelsize=14)
plt.text(300,8.7,'# emergency devices: 340',fontsize=14,fontname="Arial")
plt.text(300,5.8,'emergency duration: 30 mins',fontsize=14,fontname="Arial")
plt.text(300,3.0,'GPS+RSSI+TOA+AOA',fontsize=11,fontname="Arial")
for tick in ax1.get_xticklabels():
    tick.set_fontname("Arial")
for tick in ax1.get_yticklabels():
    tick.set_fontname("Arial")
#plt.yticks([0, 10, 50, 100])
#plt.yticks(range(0, 80, 20), [0,10,50,80])
plt.xlabel(r"number of emergency devices localized",fontname="Arial",fontsize=14)
plt.ylabel(r"root mean square error (m)",fontname="Arial",fontsize=14)
ax1.set_title("Root mean squared error against number of devices localized" , fontname="Arial", fontsize=14)
#ax2.set_ylabel(r"average messages per node (Dr)",fontsize=14)
d = .015  # how big to make the diagonal lines in axes coordinates
ax1.set_ylim(12, 70)  # most of the data
#plt.yscale('log')
plt.show()