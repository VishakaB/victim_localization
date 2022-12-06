#ref:https://shantoroy.com/python/python-bar-chart-using-matplotlib/
from matplotlib import pyplot as plt
from matplotlib.pyplot import figure
import numpy as np
font = {'family' : 'Times New Roman',
        'weight' : 'bold',
        'size'   : 18}

plt.rc('font', **font)

figure(num=None, figsize=(14, 7))

t_1 = [161,
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
       17004]
t_3 = [414,
       2051,
       5013,
       9497,
       15633,
       22830,
       30895,
       40450,
       50331,
       62415,
       75647,
       90913,
       108717,
       128099,
       148647,
       169739,
       190266,
       210060]
t_2= [161,
       948,
       2483,
       5036,
       8751,
       13270,
       18422,
       24703,
       31247,
       39512,
       48589,
       59347,
       72290,
       86594,
       101954,
       117947,
       133797,
       149264]


Labels=[120,
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
        1863,
        1989,
        2120,
        2176]
y_pos=np.arange(len(Labels))
plt.bar(y_pos + 0, t_1,width=0.2, color = 'forestgreen' , label='test label-1')
plt.bar(y_pos + 0.2,t_2, width=0.2,color = 'navy',label = 'test label-2')
plt.bar(y_pos + 0.4, t_3,width=0.2, color = 'sandybrown' , label='test label-3')
#plt.bar(y_pos + 0.6, t_4,width=0.2, color = 'black' , label='test label-4')
plt.xticks(rotation=90)
plt.xticks(y_pos, Labels)
plt.yscale('log')
plt.legend(('test label-1','test label-2', 'test label-3', 'test label-4'))
plt.ylabel('Number in log10 scale')
plt.xlabel('Different X-Axis labels')
plt.title("Put a title here")
plt.show()
# plt.savefig('figure_name.pdf', dpi=300)