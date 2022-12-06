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

ticks = ['SEQ','EKF']

def set_box_color(bp, color):
    plt.setp(bp['boxes'], color=color)
    plt.setp(bp['whiskers'], color=color)
    plt.setp(bp['caps'], color=color)
    plt.setp(bp['medians'], color=color)

plt.figure()

bpl = plt.boxplot(seq, positions=np.array(range(len(seq)))*2.0-0.4, sym='', widths=0.6)
bpr = plt.boxplot(ekf, positions=np.array(range(len(ekf)))*2.0+0.4, sym='', widths=0.6)
set_box_color(bpl, '#228B22') # colors are from http://colorbrewer2.org/
set_box_color(bpr, '#FF7F50')

# draw temporary red and blue lines and use them to create a legend
plt.plot([], c='#228B22', label='SEQ')
plt.plot([], c='#FF7F50', label='EKF')
#plt.legend()
plt.yscale('log')
from matplotlib import ticker
plt.tick_params(axis='both', which='major', labelsize=11)
#plt.yticks(range(0,10, 2),[0.01,0.01,1,10,100])
formatter = ticker.ScalarFormatter(useMathText=True)
plt.xticks(range(0, 2, 1), ticks)
plt.text(100,110000.0,'# emergency devices: 340',fontsize=13,fontname="Arial")
plt.text(100,50000.0,'emergency duration: 30 mins',fontsize=13,fontname="Arial")
plt.xlabel(r"Algorithm",fontname="Arial",fontsize=14)
plt.ylabel(r"computing delay (sec)",fontname="Arial",fontsize=14)
#plt.title("Computing delay against time" , fontname="Arial", fontsize=14)
plt.grid(color='gray', alpha=1.0, linestyle='dotted', linewidth=0.5)
plt.show()


