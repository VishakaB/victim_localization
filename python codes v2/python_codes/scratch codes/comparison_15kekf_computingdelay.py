import matplotlib.pyplot as plt
import numpy as np


seq = [[0.01,
        0.01,
        0.014,
        0.016,
        0.027,
        0.03,
        0.038,
        0.043,
        0.045,
        0.05,
        0.058,
        0.064,
        0.07,
        0.076,
        0.08]]
ekf=[[0.1216832,
      0.6067411,
      1.4782623,
      2.78046,
      4.5367281,
      6.88128,
      9.837157,
      13.3810099,
      16.7955174,
      20.783314,
      25.0712532,
      30.2667122,
      35.954631,
      42.5568378,
      49.6314424,
      56.6245882,
      64.0714547,
      70.5879609]]

ticks = [120]
plt.xticks(ticks)
def set_box_color(bp, color):
    plt.setp(bp['boxes'], color=color)
    plt.setp(bp['whiskers'], color=color)
    plt.setp(bp['caps'], color=color)
    plt.setp(bp['medians'], color=color)

plt.figure()

bpl = plt.boxplot(seq, positions=np.array(range(len(seq)))*2.0-0.4, sym='', widths=0.6)
bpr = plt.boxplot(ekf, positions=np.array(range(len(ekf)))*2.0+0.4, sym='', widths=0.6)
set_box_color(bpl, '#D7191C') # colors are from http://colorbrewer2.org/
set_box_color(bpr, '#2C7BB6')

# draw temporary red and blue lines and use them to create a legend
plt.plot([], c='#D7191C', label='Apples')
plt.plot([], c='#2C7BB6', label='Oranges')
plt.legend()
plt.yscale('log')
from matplotlib import ticker
#ax = plt.axes()
# Set ylim

# Set xlim
#ax.set_xlim(0, 100)
#ax.set_ylim(0, 100)
formatter = ticker.ScalarFormatter(useMathText=True)
#formatter.set_scientific(True)
#formatter.set_powerlimits((-3,7))
#ax.yaxis.set_major_formatter(formatter)
#plt.yticks([0, 10, 50, 100])
plt.xticks(range(0, len(ticks) * 2, 2), ticks)
plt.text(100,110000.0,'# emergency devices: 340',fontsize=13,fontname="Arial")
plt.text(100,50000.0,'emergency duration: 30 mins',fontsize=13,fontname="Arial")
plt.xlabel(r"time (sec)",fontname="Arial",fontsize=14)
plt.ylabel(r"algorithm complexity",fontname="Arial",fontsize=14)
plt.title("Algorithm complexity against time" , fontname="Arial", fontsize=14)
plt.show()
#plt.savefig('boxcompare.png')

plt.show()