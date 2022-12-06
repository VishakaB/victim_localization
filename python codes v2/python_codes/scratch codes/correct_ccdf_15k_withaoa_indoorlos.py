import matplotlib.pyplot as plt
import numpy as np

from matplotlib import rc
from matplotlib.ticker import AutoMinorLocator

rc('mathtext', default='regular')
#from matplotlib.ticker import ScalarFormatter
#data
#15k average apd
from scipy.interpolate import make_interp_spline, BSpline
#success_rate_d = (0.71,0.63,0.59,0.48)
all = (17.03312805,
       17.39557953,
       17.6124021,
       17.82945424,
       18.06648873,
       18.15178667,
       18.1975177,
       18.22191664,
       18.28704594,
       18.30465408,
       18.35795958,
       18.38296366,
       18.41348326,
       18.4579864,
       18.49003009,
       18.55121342,
       18.62931425,
       18.66356367,18.88577)
ccdf = (0.9950930248,
        0.9606680997,
        0.8971845688,
        0.7800399722,
        0.5923394168,
        0.51583038,
        0.4743848542,
        0.4523569346,
        0.3944487054,
        0.3791307269,
        0.3339892935,
        0.3135699846,
        0.289404582,
        0.2558228814,
        0.2329671627,
        0.1926492454,
        0.1478515583,
        0.1306044071,0)
noaoa = (16.94226285,
           18.02181754,
           18.19400299,
           18.50939883,
           18.64383671,
           18.7897573,
           18.81946181,
           18.83852055,
           18.84198967,
           18.85606587,
           18.89067962,
           18.93886602,
           18.9829495,
           19.01721869,
           19.04214574,
           19.08142079,
           19.14469993,
           19.17796822,19.54
           )

ccdf2= (0.9994993008,
        0.8993550324,
        0.8307007401,
        0.6439556444,
        0.5471505079,
        0.4389921106,
        0.4172658349,
        0.4034535945,
        0.4009518222,
        0.3908433353,
        0.36631077,
        0.3330676988,
        0.3037560873,
        0.2817994005,
        0.266324493,
        0.2428467693,
        0.2075005264,
        0.1902065768,0)

onlycellular = (16.94226285,
                19.05227217,
                19.4938272,
                19.6323842,
                19.71877939,
                19.78336122,
                19.80917067,
                19.82721699,
                19.83709572,
                19.84136251,
                19.8413767,
                19.84357903,
                19.84394531,
                19.84941193,
                19.85260667,
                19.8563581,
                19.85832696,
                19.86719837,
                20.32)

ccdf3 = (0.9998701555,
         0.856948401,
         0.6255858219,
         0.5138078152,
         0.4429701865,
         0.3910642055,
         0.3707982825,
         0.3568343557,
         0.3492694723,
         0.346020289,
         0.3460095043,
         0.3443368436,
         0.3440589459,
         0.3399215415,
         0.3375124632,
         0.3346920848,
         0.3332155797,
         0.3265949326,
         0)

onlygps   =(17.05043074,
            23.45018936,
            26.55560268,
            26.8201401,
            26.89112323,
            26.92978173,
            26.95415865,
            26.97094941,
            26.98322365,
            26.99270009,
            27.02706692,
            27.05481799,
            27.07769709,
            27.09688434,
            27.11320701,
            27.12516312,
            27.18325146,
            27.20696058,
            27.72)

ccdf4 = (0.9999326055,
         0.8168026322,
         0.6592816593,
         0.5007131578,
         0.4570443326,
         0.4334446686,
         0.4186790936,
         0.4085735375,
         0.4012241312,
         0.3955736197,
         0.3752733349,
         0.3591264973,
         0.3459996608,
         0.3351311706,
         0.3259923034,
         0.319363543,
         0.2880034066,
         0.2756350208,
         0)
f, ax1 = plt.subplots()

ax1.set_ylim(-0.05, 1.25)  # most of the data
ax1.set_xlim(17.0, 28)  # most of the data
#ax1.plot(time, seq)

ax1.plot(onlygps, ccdf4,color="orange")
ax1.plot(onlycellular, ccdf3,color="black")
ax1.plot(noaoa, ccdf2,color="black")
ax1.plot(all, ccdf,color="black")
#ax1.set_xlim(0.1,81)

ax1.grid(color='gray', alpha=0.5, linestyle='dashed', linewidth=0.5)

#legend
#
#lns1 = ax1.plot(noaoa, ccdf2, color="black",  label='RSSI+TOA+AOA (15k UEs)')
lns1= ax1.plot(onlygps,ccdf4, color="orange", label='GPS (15k UEs)')
lns2 = ax1.plot(onlycellular,ccdf3, color="black",  label='RSSI+TOA+AOA (15k UEs)')
lns3 = ax1.plot(noaoa,ccdf2, color="purple", label='GPS+RSSI+TOA (15k UEs)')
lns4= ax1.plot(all,ccdf, color="blue", label='GPS+RSSI+TOA+AOA (15k UEs)')

lns = lns1+lns2+lns3+lns4
labs = [l.get_label() for l in lns]


#ax1.legend(lns2, labs, loc=1, fontsize=10)
#ax1.legend(loc=4, fontsize=10)
ax1.legend(loc=4, fontsize=18)
import matplotlib.font_manager as font_manager
font = font_manager.FontProperties(family='Arial',
                                   style='normal', size=12)
ax1.legend(prop=font)
ax1.set_title("CCDF of root mean squared error (Indoor NLOS)" , fontname="Arial", fontsize=14)

#ax2.set_xlabel("time (sec)",fontsize=14)
plt.xlabel(r"root mean squared error (m)",fontname="Arial",fontsize=14)
plt.ylabel(r"complementary cumulative distribution function (CCDF)",fontname="Arial",fontsize=14)
#ax2.set_ylabel(r"average messages per node (Dr)",fontsize=14)
d = .015  # how big to make the diagonal lines in axes coordinates
# arguments to pass to plot, just so we don't keep repeating them


# single vline with specific ymin and ymax
#ax2.vlines(x=39.25, ymin=25, ymax=150, colors='green', ls=':', lw=2, label='vline_single - partial height')

# place legend outside
#ax1.legend(loc=1)

for tick in ax1.get_xticklabels():
    tick.set_fontname("Arial")
for tick in ax1.get_yticklabels():
    tick.set_fontname("Arial")

ax1.tick_params(axis='both', which='major', labelsize=14)
plt.text(20.2,0.3,'# emergency devices: 340',fontsize=14,fontname="Arial")
plt.text(20.2,0.2,'emergency duration: 30 minutes',fontsize=14,fontname="Arial")

plt.show()
