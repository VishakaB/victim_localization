import matplotlib.pyplot as plt
import numpy as np
import matplotlib.font_manager
import matplotlib.font_manager as fontmanager
time =('100-300', '1000-2000', '2000-3000')

avg_seq= (18.62336991,22.45711697,21.91932224)
min_seq = (17.80918842,17.74479224,17.85090852)
max_seq= (19.19246775,23.29975537,22.72100787)

avg_apd = (167.1459,279.2657,265.8517)
min_apd = (155.0305889,269.4891,256.5260)
max_apd = (182.2004133,289.0626,278.8443)

avg_mcl = (515.7175,550.6138,551.4272)
min_mcl = (487.4678,535.7146,540.5275)
max_mcl = (521.3645,560.3701,552.6869)

f, ax1 = plt.subplots()

#ax1.plot(time,min_seq,linestyle='dotted',color="green", label='$MVLA_{recent-seq}$ min')
#ax1.plot(time,avg_seq,linestyle='dotted',color="green",marker='o', label='$MVLA_{recent-seq}$ mean')
#ax1.plot(time,max_seq,linestyle='dashed',color="green",label='$MVLA_{recent-seq}$ max')

ax1.plot(time,min_apd,linestyle='dotted',color="navy", label='$MVLA_{all}$ min (15k UEs)')
ax1.plot(time,avg_apd,linestyle='dotted',color="navy",marker='o', label='$MVLA_{all}$ mean (15k UEs)')
ax1.plot(time,max_apd,linestyle='dashed',color="navy",label='$MVLA_{all}$ max (15k UEs)')

ax1.plot(time,min_mcl,linestyle='dotted',color="saddlebrown", label='RSSI-MCL min  (15k UEs)')
ax1.plot(time,avg_mcl,linestyle='dotted',color="saddlebrown",marker='o', label='RSSI-MCL mean (15k UEs)')
ax1.plot(time,max_mcl,linestyle='dashed',color="saddlebrown",label='RSSI-MCL max (15k UEs)')

#fill between the upper and lower bands
plt.fill_between(time, min_mcl, max_mcl, alpha = .1,color = 'saddlebrown')
plt.fill_between(time, min_apd, max_apd, alpha = .1,color = 'navy')

#add background grid for visual appeal
plt.grid(True, linestyle='dotted')
plt.legend()

import matplotlib.font_manager as fontmanager

import matplotlib.font_manager as font_manager
font = font_manager.FontProperties(family='Arial',
                                   style='normal', size=12)
ax1.legend(prop=font)
plt.legend(fontsize=9) # using a size in points
ax1.tick_params(axis='both', which='major', labelsize=14)

plt.text(0.6,200.8,'emergency duration: 30 mins',fontsize=14,fontname="Arial")
#plt.text(0.6,155.0,'Technique: GPS+RSSI+TOA+AOA',fontsize=12,fontname="Arial")

for tick in ax1.get_xticklabels():
    tick.set_fontname("Arial")
for tick in ax1.get_yticklabels():
    tick.set_fontname("Arial")

plt.xlabel(r"number of emergency devices localized",fontname="Arial",fontsize=14)
plt.ylabel(r"average distance error (m)",fontname="Arial",fontsize=14)
# ax1.set_title("Average distance error against number of devices localized" , fontname="Arial", fontsize=14)
ax1.set_xlim(0, 2)  # most of the data
d = .015  # how big to make the diagonal lines in axes coordinates
ax1.set_ylim(140, 600)  # most of the data

plt.show()