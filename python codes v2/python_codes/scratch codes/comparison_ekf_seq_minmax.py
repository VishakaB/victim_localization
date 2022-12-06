import matplotlib.pyplot as plt
import numpy as np
time =(120, 240, 360, 516, 662,740,874,1022,1081,1201,1320,1451,1562,1680,1863)

min_seq= (4.0410, 18.2556, 18.0589, 18.5629, 18.4999, 18.4484, 18.4573, 18.3636, 18.3593, 18.7092, 18.7224, 18.6678, 18.5902, 19.0373, 19.0177)
max_seq = (19.6653, 19.3739, 19.0557, 18.7566, 18.5684, 18.4985, 18.5234, 18.4544, 18.3593, 18.7598, 18.7677, 18.7304, 19.2003, 19.0147, 19.2588)
avg_seq= (17.8092,18.7266,18.6051,18.6467,18.5307,18.4732,18.5027,18.3987,18.3593,18.7234,18.7438,18.7304,18.8926,19.0835,19.1925)

min_ekf = (23.2330, 24.1331, 24.3158, 24.4562, 24.4737, 24.5176, 24.4896, 24.4939, 24.4975, 24.5002, 24.5200, 24.5063, 24.5085, 24.5104, 24.5236 )
avg_ekf = (24.2255, 24.280, 24.4279, 24.5165, 24.5173, 24.5176, 24.5177, 24.5177, 24.5182, 24.5185, 24.5200, 24.5211, 24.5220, 24.5229, 24.5121)
max_ekf = (27.3264,24.4380, 24.5840, 24.6035 ,24.5814, 24.5683, 24.5596, 24.5536, 24.5494, 24.5461, 24.5447, 24.5434, 24.5425, 24.5417, 24.5410)

time2 =(120.0538738,240.3288625,360.1908036,482.7931902,600.077743,720.1311196,840.4899992,966.0963223,1112.081902,
        1229.799392,
        1339.817742,
        1444.086366,
        1561.165773,
        1691.058068,
        1815.031383)
avg_seq2= (17.3956,20.6911,21.8897,23.6345,24.3144,24.3823,24.8723,25.0126,25.2346,25.3869,25.3399,25.3465,25.3068,25.3417,25.3910)
min_seq2= (13.5890,19.9420,20.9792,22.9324,24.1332,24.1192,24.4409,24.9512,25.0170,25.3398,25.3195,25.3218,25.2840,25.3101,25.4312)
max_seq2 = (24.4580,21.3974,23.0931,24.3342,24.5577,24.5991,25.0954,25.0914,25.3888,25.4122,25.3598,25.3641,25.3381,25.3971,25.3922)

avg_ekf2 = (33.6219, 37.8080,42.0574,44.3079,45.8682,47.2854,48.6380,49.9432,51.1208,52.1564,52.9926,53.6721,54.2386,54.7279,55.2945)
min_ekf2 = (28.2602, 35.8645,40.6360,43.1401,44.8378,46.2814,47.7804, 49.1568,50.4643, 51.6122,52.5140,53.2623,53.8682,54.4005,55.0483)
max_ekf2 = (38.0818,39.7173,43.7880,45.4585,46.7289,48.1717,49.5071,50.7991,51.9287,52.8179,53.5527,54.1383,54.6563,55.0895,55.5020)

f, ax1 = plt.subplots()

ax1.plot(time,min_seq,linestyle='dotted',color="green", label='SEQ min (15k UEs)')
ax1.plot(time,avg_seq,linestyle='dotted',color="green",marker='o', label='SEQ mean (15 UEs)')
ax1.plot(time,max_seq,linestyle='dashed',color="green",label='SEQ max (15k UEs)')

ax1.plot(time,min_ekf,linestyle='dotted',color="coral", label='EKF min  (15k UEs)')
ax1.plot(time,avg_ekf,linestyle='dotted',color="coral",marker='o', label='EKF mean (15k UEs)')
ax1.plot(time,max_ekf,linestyle='dashed',color="coral",label='EKF max (15k UEs)')

#fill between the upper and lower bands
plt.fill_between(time, min_ekf, max_ekf, alpha = .1,color = 'peachpuff')
plt.fill_between(time, min_seq, max_seq, alpha = .1,color = 'darkseagreen')

ax1.plot(time,min_seq2,linestyle='dotted',color="green", label='SEQ min (15k UEs)')
ax1.plot(time,avg_seq2,linestyle='dotted',color="green",marker='o', label='SEQ mean (15 UEs)')
ax1.plot(time,max_seq2,linestyle='dashed',color="green",label='SEQ max (15k UEs)')

ax1.plot(time,min_ekf2,linestyle='dotted',color="coral", label='EKF min  (15k UEs)')
ax1.plot(time,avg_ekf2,linestyle='dotted',color="coral",marker='o', label='EKF mean (15k UEs)')
ax1.plot(time,max_ekf2,linestyle='dashed',color="coral",label='EKF max (15k UEs)')

plt.fill_between(time, min_ekf2, max_ekf2, alpha = .1,color = 'peachpuff')
plt.fill_between(time, min_seq2, max_seq2, alpha = .1,color = 'darkseagreen')
#add background grid for visual appeal
plt.grid(True, linestyle='dotted')
plt.legend()

for i in range(len(time)):
    my_selected_date = time[i]
    lnv1 = ax1.vlines(my_selected_date, 0, max_ekf2[i]+0.03, linestyles ="dashed", colors ="brown", alpha=0.5,linewidth=0.5)   # changed
    #lnv2 = ax1.vlines(my_selected_date, 2.51, ekf[i]+0.005, linestyles ="dashed", colors ="orange",alpha=0.9,linewidth=0.5)   # changed
ax1.axvline(x=time[0],ymin=0.0, ymax=max_ekf2[0]+0.03 ,label='localization update time',linestyle ="dashed", color ="brown", alpha=0.2,linewidth=0.5)
#ax1.legend(lns2, labs, loc=1, fontsize=10)
#ax1.legend(loc=4, fontsize=10)
ax1.legend(loc=2, fontsize=6)
import matplotlib.font_manager as font_manager
font = font_manager.FontProperties(family='Arial',
                                   style='normal', size=12)
ax1.legend(prop=font)
plt.legend(fontsize=8) # using a size in points
ax1.tick_params(axis='both', which='major', labelsize=14)
plt.text(300,8.7,'# emergency devices: 340',fontsize=14,fontname="Arial")
plt.text(300,5.8,'emergency duration: 30 mins',fontsize=14,fontname="Arial")
plt.text(300,3.0,'GPS+RSSI+TOA+AOA',fontsize=11,fontname="Arial")
for tick in ax1.get_xticklabels():
    tick.set_fontname("Arial")
for tick in ax1.get_yticklabels():
    tick.set_fontname("Arial")
#plt.yticks([0, 10, 50, 100])
plt.yticks(range(0, 80, 20), [0,10,50,80])
plt.xlabel(r"time (sec)",fontname="Arial",fontsize=14)
plt.ylabel(r"root mean square error (m)",fontname="Arial",fontsize=14)
ax1.set_title("Root mean squared error against time" , fontname="Arial", fontsize=14)
#ax2.set_ylabel(r"average messages per node (Dr)",fontsize=14)
d = .015  # how big to make the diagonal lines in axes coordinates
ax1.set_ylim(0, 100)  # most of the data
#plt.yscale('log')
plt.show()