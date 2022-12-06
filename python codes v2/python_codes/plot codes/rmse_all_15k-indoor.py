import matplotlib.pyplot as plt
import numpy as np

from matplotlib import rc
from matplotlib.ticker import AutoMinorLocator

rc('mathtext', default='regular')
#from matplotlib.ticker import ScalarFormatter
#data
#15k average apd
time = (120.3735852,
        240.7824663,
        360.6113696,
        516.6123575,
        662.1859314,
        740.8104685,
        874.8063047,
        1022.24645,
        1081.829689,
        1201.829689,
        1320.745058,
        1451.173653,
        1562.6537,
        1680.858401,
        1863.265952,
        1989.468238,
        2120.810468,
        2176.312653)
#success_rate_d = (0.71,0.63,0.59,0.48)
onlygps = (27.66703926,
           28.17377356,
           27.64711892,
           27.44986354,
           27.32164037,
           27.24741697,
           27.19518126,
           27.17989621,
           27.16648431,
           27.15601035,
           27.15615428,
           27.16357475,
           27.16969123,
           27.17481988,
           27.14431044,
           27.80235218,
           27.18325146,
           27.20696058)
noaoa = (18.25039491,
         19.19220473,
         19.0748131,
         18.95641527,
         18.88909064,
         18.86893073,
         18.83296075,
         18.84960148,
         18.85674748,
         18.87539046,
         18.88999258,
         18.93108075,
         18.95835056,
         18.98870036,
         18.99354072,
         19.70913985,
         19.14384562,
         19.17683326
         )

all = (17.70983155,
       18.01606474,
       18.12094931,
       18.14972028,
       18.14717244,
       18.17288315,
       18.18733337,
       18.21655335,
       18.23880387,
       18.27599645,
       18.29598304,
       18.31440707,
       18.34469128,
       18.37740888,
       18.40781757,
       18.53918426,
       18.53918426,
       18.53918426
       )
onlycellular=(17.71650462,
              18.06982981,
              18.29435025,
              18.35087804,
              18.36357666,
              18.41197226,
              18.44417908,
              18.47262591,
              18.49454705,
              18.53344843,
              18.55837111,
              18.57979389,
              18.61973988,
              18.6574754,
              18.69671839,
              18.54519296,
              18.54519296,
              18.54519296


       )
min_apdall = (16.86498664,
              16.68448082,
              17.43947764,
              17.54620917,
              17.49718792,
              17.44960153,
              17.41120732,
              17.44823969,
              17.47036474,
              17.49862459,
              17.50563674,
              17.5199403,
              17.51806753,
              17.53608629,
              17.5421109,
              18.03918426,
              17.8,
              18.03)
max_apdall = (19.02575048,
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
              19.00332008,
              19.14560808,
              19.14560808,
              19.14560808)
minnoaoa =(16.94226285,
           17.85476953,
           17.60074887,
           17.54620917,
           17.49718792,
           17.45579991,
           17.42484707,
           17.45817937,
           17.4861806,
           17.51655519,
           17.52708952,
           17.54701174,
           17.5430924,
           17.56500077,
           17.57303603,
           19.0812769,
           19.14384562,
           19.17683326)
maxnoaoa = (20.11910953,
            21.70002713,
            21.42968743,
            20.8136378,
            20.52624729,
            20.36123497,
            20.25457337,
            20.24863542,
            20.2455413,
            20.25355033,
            20.25220861,
            20.30736448,
            20.34900979,
            20.38388163,
            20.3654404,
            20.3370028,
            19.14384562,
            19.17683326)

minonlygps = (24.35043074,
              26.45660775,
              26.10069686,
              25.95775514,
              25.86995541,
              25.81705428,
              25.78166376,
              25.79210178,
              25.79304904,
              25.79295903,
              25.79138627,
              25.79010454,
              25.78903991,
              25.78814153,
              25.77150038,
              27.12516312,
              27.18325146,
              27.20696058)
maxonlygps = (32.13773919,
              31.50911026,
              30.39047055,
              29.57169539,
              29.20384247,
              28.9954149,
              28.84972137,
              28.77663744,
              28.72318025,
              28.68237193,
              28.65000966,
              28.64580171,
              28.64233669,
              28.63943376,
              28.54822391,
              28.47954124,
              27.18325146,
              27.20696058)
minonlycellular=(16.86498664,
                 16.68448082,
                 17.43948155,
                 17.74246336,
                 17.81342803,
                 17.95966625,
                 18.03449466,
                 18.0892451,
                 18.13874384,
                 18.19656126,
                 18.23527214,
                 18.25374719,
                 18.34766326,
                 18.45113295,
                 18.52284169,
                 18.54519296,
                 18.54519296,
                 18.54519296)
maxonlycellular = (19.02575048,
                   19.30803381,
                   19.04232907,
                   18.87960994,
                   18.84741118,
                   18.85138193,
                   18.85006962,
                   18.85577502,
                   18.86183889,
                   18.90505825,
                   18.94664146,
                   18.97561924,
                   18.9770888,
                   18.98818863,
                   18.99994985,
                   18.54519296,
                   18.54519296,
                   18.54519296)
f, ax1 = plt.subplots()

ax1.grid(color='gray', alpha=0.5, linestyle='dashed', linewidth=0.5)

#legend
lns1 = ax1.plot(time, onlygps, color="darkcyan",marker="p", markersize=7, label='GPS (15k UEs)')
#lns2 = ax1.plot(time, onlycellular,color="black",marker="d", markersize=7,  label='RSSI+TOA+AOA (15k UEs)')
lns3 = ax1.plot(time, noaoa,color="chocolate",marker="*", markersize=7, label='GPS+RSSI+TOA (15k UEs)')
lns4 = ax1.plot(time, all, color="navy", marker="o", markersize=7, label='GPS+RSSI+TOA+AOA (15k UEs)')

ax1.plot(time,min_apdall,linestyle='dotted',color="navy")
ax1.plot(time,max_apdall,linestyle='dotted',color="navy")
ax1.plot(time,minonlygps,linestyle='dotted',color="darkcyan")
ax1.plot(time,maxonlygps,linestyle='dotted',color="darkcyan")
ax1.plot(time,minnoaoa,linestyle='dotted',color="chocolate")
ax1.plot(time,maxnoaoa,linestyle='dotted',color="chocolate")

#ax1.plot(time,minonlycellular,linestyle='dotted',color="black")
#ax1.plot(time,maxonlycellular,linestyle='dotted',color="black")

plt.fill_between(time, min_apdall, max_apdall, alpha = .1,color = 'navy')
plt.fill_between(time, minonlygps, maxonlygps, alpha = .1,color = 'darkcyan')
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
ax1.set_ylim(10.0, 38.5)  # most of the data
ax1.tick_params(axis='both', which='major', labelsize=14)
plt.text(100,14.0,'# emergency devices: 340',fontsize=13,fontname="Arial")
plt.text(100,12.0,'emergency duration: 30 mins',fontsize=13,fontname="Arial")
plt.xlabel(r"time (sec)",fontname="Arial",fontsize=14)
plt.ylabel(r"root mean square error (m)",fontname="Arial",fontsize=14)
ax1.set_title("Root mean squared error against time" , fontname="Arial", fontsize=14)
plt.show()
