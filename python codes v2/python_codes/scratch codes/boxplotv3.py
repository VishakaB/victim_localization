import numpy as np
import matplotlib.pyplot as plt

# --- Your data, e.g. results per algorithm:
data1 = [5,5,4,3,3,5]
data2 = [6,6,4,6,8,5]
data3 = [7,8,4,5,8,2]
data4 = [6,9,3,6,8,4]
data6 = [17,8,4,5,8,1]
data7 = [6,19,3,6,1,1]


# --- Combining your data:
data_group1 = [data1, data2, data6]
data_group2 = [data3, data4, data7]
data_group3 = [data1, data1, data1]
data_group4 = [data2, data2, data2]
data_group5 = [data2, data2, data2]

data_groups = [data_group1, data_group2, data_group3] #, data_group4] #, data_group5]

# --- Labels for your data:
labels_list = ['a','b', 'c']
width       = 0.3
xlocations  = range(len(data_group1))

symbol      = 'r+'
ymin        = min ( [ val  for dg in data_groups  for data in dg for val in data ] )
ymax        = max ( [ val  for dg in data_groups  for data in dg for val in data ])

ax = plt.gca()
ax.set_ylim(ymin,ymax)

ax.grid(True, linestyle='dotted')
ax.set_axisbelow(True)

plt.xlabel('X axis label')
plt.ylabel('Y axis label')
plt.title('title')

space = len(data_groups)/2
offset = len(data_groups)/2

plt.xticks(range(0, len(labels_list) * 2, 2), labels_list)
ax.set_xticks( xlocations )
#ax.set_xticklabels(range(0, len(labels_list) * 2, 2), labels_list)
# --- Offset the positions per group:

group_positions = []
for num, dg in enumerate(data_groups):
    _off = (0 - space + (0.5+num))
    print(_off)
    group_positions.append([x-_off*(width+0.01) for x in xlocations])

for dg, pos in zip(data_groups, group_positions):
    plt.boxplot(dg,
               sym=symbol,
               #            labels=['']*len(labels_list),
               labels=['']*len(labels_list),
               positions=pos,
               widths=width,
               #           notch=False,
               #           vert=True,
               #           whis=1.5,
               #           bootstrap=None,
               #           usermedians=None,
               #           conf_intervals=None,
               #           patch_artist=False,
               )



plt.show()