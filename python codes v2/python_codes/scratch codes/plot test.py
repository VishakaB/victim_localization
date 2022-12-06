import matplotlib.pyplot as plt
import numpy as np
time =(120, 240, 360, 516, 662,740,874,1022,1081,1201,1320,1451,1562,1680,1863)
min_apd = ( 4.0410, 17.1975, 17.1572, 17.6514, 17.9144, 18.0382, 18.0956, 18.1293, 18.2215, 18.2363, 18.2923, 18.3250, 18.3645, 18.4095, 18.4430)
max_apd = (18.5670, 18.0755, 17.9140, 18.1466, 18.2157, 18.2722, 18.2987, 18.3062, 18.3513, 18.3950, 18.4205, 18.4381, 18.4753, 18.5170, 18.5435)
avg_apd = (17.0331, 17.6124, 17.3956, 17.8295, 18.0665, 18.1518, 18.1975, 18.2219, 18.2870, 18.3047, 18.3580, 18.3830, 18.4135, 18.4580, 18.4900)

min_ord = (4.0410, 17.8048, 18.0576, 18.8469, 18.7870, 18.7511, 18.7075, 18.6624, 18.6748, 18.6752, 18.9783, 18.9134, 18.8256, 19.1661, 19.1231)
max_ord = (19.1185, 19.2669, 19.1717, 19.0005, 18.8393, 18.8022, 18.7747, 18.7093, 18.6748, 19.0769, 19.0202, 18.9813, 19.3185, 19.2580, 19.3526)
avg_ord = (16.9423,18.5134,18.7286,18.8998,18.8126,18.7770,18.7409,18.6866,18.6748,18.9069,19.0012,18.9448,19.1242,19.2118,19.2505)



min_seq= (4.0410, 18.2556, 18.0589, 18.5629, 18.4999, 18.4484, 18.4573, 18.3636, 18.3593, 18.7092, 18.7224, 18.6678, 18.5902, 19.0373, 19.0177)
max_seq = (19.6653, 19.3739, 19.0557, 18.7566, 18.5684, 18.4985, 18.5234, 18.4544, 18.3593, 18.7598, 18.7677, 18.7304, 19.2003, 19.0147, 19.2588)
avg_seq= (17.8092,18.7266,18.6051,18.6467,18.5307,18.4732,18.5027,18.3987,18.3593,18.7234,18.7438,18.7304,18.8926,19.0835,19.1925)

f, ax1 = plt.subplots()
ax1.plot(time,min_apd,linestyle='dotted',color="blue", label='APD min')
ax1.plot(time,avg_apd,linestyle='dotted',color="blue",marker='o', label='APD mean')
ax1.plot(time,max_apd,linestyle='dashed',color="blue",label='APD max')

ax1.plot(time,min_ord,linestyle='dotted',color="orchid", label='ORD min')
ax1.plot(time,avg_ord,linestyle='dotted',color="orchid",marker='o', label='ORD mean')
ax1.plot(time,max_ord,linestyle='dashed',color="orchid",label='ORD max')

ax1.plot(time,min_seq,linestyle='dotted',color="green", label='SEQ min')
ax1.plot(time,avg_seq,linestyle='dotted',color="green",marker='o', label='SEQ mean')
ax1.plot(time,max_seq,linestyle='dashed',color="green",label='SEQ max')


#fill between the upper and lower bands
plt.fill_between(time, min_apd, max_apd, alpha = .1,color = 'darkorchid')
plt.fill_between(time, min_ord, max_ord, alpha = .1,color = 'orchid')
plt.fill_between(time, min_seq, max_seq, alpha = .1,color = 'darkseagreen')
#add background grid for visual appeal
plt.grid(True, linestyle='dotted')
plt.legend()

for i in range(len(time)):
    my_selected_date = time[i]
    lnv1 = ax1.vlines(my_selected_date, 0, max_ord[i]+0.03, linestyles ="dashed", colors ="brown", alpha=0.5,linewidth=0.5)   # changed
    #lnv2 = ax1.vlines(my_selected_date, 2.51, ekf[i]+0.005, linestyles ="dashed", colors ="orange",alpha=0.9,linewidth=0.5)   # changed
ax1.axvline(x=time[0],ymin=0.0, ymax=max_ord[0]+0.03 ,label='localization update time',linestyle ="dashed", color ="brown", alpha=0.2,linewidth=0.5)
#ax1.legend(lns2, labs, loc=1, fontsize=10)
#ax1.legend(loc=4, fontsize=10)
ax1.legend(loc=2, fontsize=10)
import matplotlib.font_manager as font_manager
font = font_manager.FontProperties(family='Arial',
                                   style='normal', size=12)
ax1.legend(prop=font)
ax1.tick_params(axis='both', which='major', labelsize=14)
plt.text(155,4.6,'# emergency devices: 340',fontsize=14,fontname="Arial")
plt.text(100,2.5,'emergency duration: 30 mins',fontsize=14,fontname="Arial")
plt.text(100,1.0,'GPS+RSSI+TOA+AOA',fontsize=11,fontname="Arial")
for tick in ax1.get_xticklabels():
    tick.set_fontname("Arial")
for tick in ax1.get_yticklabels():
    tick.set_fontname("Arial")

plt.xlabel(r"time (sec)",fontname="Arial",fontsize=14)
plt.ylabel(r"root mean square error (m)",fontname="Arial",fontsize=14)
ax1.set_title("Root mean squared error against time (Indoor NLOS)" , fontname="Arial", fontsize=14)
#ax2.set_ylabel(r"average messages per node (Dr)",fontsize=14)
d = .015  # how big to make the diagonal lines in axes coordinates
ax1.set_ylim(0, 21.5)  # most of the data

plt.show()