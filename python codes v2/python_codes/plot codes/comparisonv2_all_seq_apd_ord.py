import matplotlib.pyplot as plt
import numpy as np
time =(120, 240, 360, 516, 662,740,874,1022,1081,1201,1320,1451,1562,1680,1863)
min_apd = (16.86498664,
           16.68448082,
           17.43947764,
           17.7424734,
           17.81345497,
           17.9596855,
           18.03441364,
           18.08911688,
           18.13897296,
           18.19703047,
           18.2356952,
           18.2542999,
           18.34830058,
           18.45179725,
           18.52348668)
max_apd = (19.02575048,
           19.30803381,
           19.04233058,
           18.87963287,
           18.84819282,
           18.85255666,
           18.85158675,
           18.85775036,
           18.86457275,
           18.90835522,
           18.94998561,
           18.97912953,
           18.98303105,
           18.99387118,
           19.00332008)
avg_apd = (17.71650462,
           18.06982981,
           18.29434945,
           18.35089066,
           18.36383395,
           18.41397702,
           18.44604205,
           18.4726579,
           18.49495025,
           18.5351204,
           18.55943181,
           18.57922933,
           18.62023253,
           18.65784974,
           18.69638646)

min_ord = (16.86498664,
           16.83654024,
           17.70095734,
           17.77535686,
           17.68499187,
           17.77616834,
           18.38214311,
           18.34501958,
           18.27054666,
           18.22015446,
           18.23808892,
           18.2402733,
           18.21623457,
           18.17989219,
           18.10597907)
max_ord = (19.02575048,
           18.80405207,
           19.17046114,
           19.4885671,
           19.38825972,
           19.21388005,
           19.10770932,
           18.98467192,
           18.85846709,
           18.76849452,
           18.75429213,
           18.67579744,
           18.79062816,
           18.73858342,
           18.72133095)
avg_ord = (17.71650462,
           18.12224526,
           18.54849816,
           18.84431548,
           18.78290899,
           18.72305479,
           18.64532894,
           18.57475283,
           18.57845779,
           18.58026168,
           18.59530946,
           18.60689829,
           18.64987276,
           18.65385946,
           18.65056)


min_seq= (15.92495504,
          16.61188813,
          17.57864638,
          18.05938255,
          18.1992312,
          18.20218252,
          18.16656719,
          18.2026077,
          18.30357079,
          18.31259434,
          18.30854163,
          18.26749568,
          18.2323047,
          18.21113767,
          18.43151952)
max_seq = (18.23400719,
           18.92732146,
           18.4973285,
           18.7753532,
           18.78287842,
           18.70937657,
           18.60456797,
           18.51845287,
           18.4290868,
           18.47157812,
           18.49290277,
           18.45915273,
           18.41989603,
           18.40361116,
           18.46485467)
avg_seq= (17.35721276,
          17.70479846,
          18.02888273,
          18.23044972,
          18.22902064,
          18.24439753,
          18.31183238,
          18.27105651,
          18.27687108,
          18.2770008,
          18.30329101,
          18.29441325,
          18.2876199,
          18.27863283,
          18.29812508)

f, ax1 = plt.subplots()
ax1.plot(time,min_apd,linestyle='dotted',color="navy", label='$MVLA_{all}$ min')
ax1.plot(time,avg_apd,linestyle='dotted',color="navy",marker='o', label='$MVLA_{all}$ mean')
ax1.plot(time,max_apd,linestyle='dashed',color="navy",label='$MVLA_{all}$ max')

ax1.plot(time,min_ord,linestyle='dotted',color="orchid", label='$MVLA_{recent}$ min')
ax1.plot(time,avg_ord,linestyle='dotted',color="orchid",marker='o', label='$MVLA_{recent}$ mean')
ax1.plot(time,max_ord,linestyle='dashed',color="orchid",label='$MVLA_{recent}$ max')

ax1.plot(time,min_seq,linestyle='dotted',color="green", label='$MVLA_{recent-seq}$ min')
ax1.plot(time,avg_seq,linestyle='dotted',color="green",marker='o', label='$MVLA_{recent-seq}$ mean')
ax1.plot(time,max_seq,linestyle='dashed',color="green",label='$MVLA_{recent-seq}$ max')


#fill between the upper and lower bands
plt.fill_between(time, min_apd, max_apd, alpha = .1,color = 'darkorchid')
plt.fill_between(time, min_ord, max_ord, alpha = .1,color = 'orchid')
plt.fill_between(time, min_seq, max_seq, alpha = .1,color = 'darkseagreen')
#add background grid for visual appeal
plt.grid(True, linestyle='dotted')
plt.legend()

for i in range(len(time)):
    my_selected_date = time[i]
    lnv1 = ax1.vlines(my_selected_date, 0, max_ord[i]+0.03, linestyles ="dashed", colors ="brown", alpha=0.5,linewidth=1)   # changed
    #lnv2 = ax1.vlines(my_selected_date, 2.51, ekf[i]+0.005, linestyles ="dashed", colors ="orange",alpha=0.9,linewidth=0.5)   # changed
ax1.axvline(x=time[0],ymin=0.0, ymax=0.03 ,label='localization update time',linestyle ="dashed", color ="brown", alpha=0.8,linewidth=0.5)
#ax1.legend(lns2, labs, loc=1, fontsize=10)
#ax1.legend(loc=4, fontsize=10)

import matplotlib.font_manager as font_manager
font = font_manager.FontProperties(family='Arial',
                                   style='normal', size=9)
ax1.legend(prop=font)
ax1.tick_params(axis='both', which='major', labelsize=14)
plt.text(205,7.0,'# emergency devices: 340',fontsize=14,fontname="Arial")
plt.text(200,5.5,'emergency duration: 30 mins',fontsize=14,fontname="Arial")
plt.text(200,3.0,'Technique:',fontsize=12,fontname="Arial")
plt.text(200,2.0,'GPS+RSSI+TOA+AOA',fontsize=12,fontname="Arial")

for tick in ax1.get_xticklabels():
    tick.set_fontname("Arial")
for tick in ax1.get_yticklabels():
    tick.set_fontname("Arial")

plt.xlabel(r"time (sec)",fontname="Arial",fontsize=14)
plt.ylabel(r"root mean square error (m)",fontname="Arial",fontsize=14)
ax1.set_title("Root mean squared error against time" , fontname="Arial", fontsize=14)
#ax2.set_ylabel(r"average messages per node (Dr)",fontsize=14)
d = .015  # how big to make the diagonal lines in axes coordinates
ax1.set_ylim(15, 20)  # most of the data
#ax1.set_xlim(100, 2000)  # most of the data
plt.show()