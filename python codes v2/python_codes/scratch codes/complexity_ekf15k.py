import matplotlib.pyplot as plt
import numpy as np


seq = [[161,
        787,
        1535,
        2553,
        3719,
        4525,
        5158,
        6285,
        6548,
        8269,
        9081,
        10762,
        12947,
        14308,
        15364,
        16158,
        16639,
        17004]]
ekf=[[414,
      1201,
      2736,
      5289,
      9008,
      13533,
      18691,
      24976,
      31524,
      39793,
      48874,
      59636,
      72583,
      86891,
      102255,
      118413,
      135052,
      152056]]

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
#plt.yticks(range(1000,100000, 50000),[1000,10000,100000])
formatter = ticker.ScalarFormatter(useMathText=True)
plt.xticks(range(0, 2, 1), ticks)
plt.text(100,110000.0,'# emergency devices: 340',fontsize=13,fontname="Arial")
plt.text(100,50000.0,'emergency duration: 30 mins',fontsize=13,fontname="Arial")
plt.xlabel(r"Algorithm",fontname="Arial",fontsize=14)
plt.ylabel(r"algorithm complexity",fontname="Arial",fontsize=14)
plt.title("Complexity against algorithm" , fontname="Arial", fontsize=14)
plt.grid(color='gray', alpha=1.0, linestyle='dotted', linewidth=0.5)
plt.show()


