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
       1535]#apd
t_2 = [414,
       2051,
       5013]#apd
t_3= [161,
      948,
      0.9946516008]#apd


Labels=['100-300',
        '1000-2000',
        '2000-3000']
y_pos=np.arange(len(Labels))
plt.bar(y_pos + 0, t_1,width=0.2, color = 'forestgreen' , label='test label-1')
plt.bar(y_pos + 0.2,t_2, width=0.2,color = 'navy',label = 'test label-2')
plt.bar(y_pos + 0.4, t_3,width=0.2, color = 'sandybrown' , label='test label-3')
#plt.bar(y_pos + 0.6, t_4,width=0.2, color = 'black' , label='test label-4')
plt.xticks()
plt.xticks(y_pos, Labels)
plt.yscale('log')
plt.legend(('test label-1','test label-2', 'test label-3', 'test label-4'))
plt.ylabel('Number of success contractions/ Total number of contractions')
plt.xlabel('Different X-Axis labels')
plt.title("Put a title here")
plt.show()
# plt.savefig('figure_name.pdf', dpi=300)