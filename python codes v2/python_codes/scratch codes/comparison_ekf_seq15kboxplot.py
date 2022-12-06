import matplotlib.pyplot as plt
import numpy as np

seq = [[17.8092,
        4.0410,
        19.6653],
       [18.7266,
        18.2556,
        19.3739],
       [18.6051,
        18.0589,
        19.0557],
       [18.6467,
        18.5629,
        18.7566],
       [18.5307,
        18.4999,
        18.5684],
       [18.4732,
        18.4484,
        18.4985],
       [18.5234,
        18.5027,
        18.4797,
        18.4573],
       [18.3987,
        18.3636,
        18.4544],
       [18.3593],
       [18.7234,
        18.7092,
        18.7598],
       [18.7438,
        18.7224,
        18.7677],
       [18.7304,
        18.7111,
        18.6880,
        18.6913,
        18.6678],
       [18.8926,
        18.5902,
        19.2003],
       [19.1059,
        19.0835,
        19.0601,
        19.0373,
        19.0147],
       [19.1925,
        19.0177,
        19.2588]]
ekf=[[24.2255,
      23.2330,
      27.3264],
     [24.280,
      24.1331,
      24.4380],
     [24.4279,
      24.3158,
      24.5840],
     [24.5165,
      24.4562,
      24.6035],
     [24.5173,
      24.4737,
      24.5814],
     [24.5176,
      24.4834,
      24.5683],
     [24.5177,
      24.4896,
      24.5596],
     [24.5177,
      24.4939,
      24.5536],
     [24.5182,
      24.4975,
      24.5494],
     [24.5185,
      24.5002,
      24.5461],
     [24.5200,
      24.5036,
      24.5447],
     [24.5211,
      24.5063,
      24.5434],
     [24.5220,
      24.5085,
      24.5425],
     [24.5229,
      24.5104,
      24.5417],
     [24.5236,
      24.5121,
      24.5410],
     [24.5318,
      24.5171,
      24.5469]]

ticks = [120,
         240,
         360,
         516,
         662,
         740,
         874,
         1022,
         1081,
         1201,
         1320,
         1451,
         1562,
         1680,
         1863]

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

plt.xticks(range(0, len(ticks) * 2, 2), ticks)
plt.xlim(-2, len(ticks)*2)
plt.ylim(0, 30)
plt.tight_layout()
#plt.savefig('boxcompare.png')
plt.show()