import xpress as xp
import math
#TO INSTALL XPRESS: RUN 'pip install xpress'         
#initialization
nodeids_loc,nodeids_radius,benchids_node,benchids_dst,d={},{},{},{},{}
mx, my,gpsradius = {},{},{}
itercount=[]

nodeids = ['55','10','45']#ids

#positions
nodeids_loc['55'] =(5,5)
nodeids_loc['45'] =(1,3)
nodeids_loc['10'] =(10,1)

#gps radii
nodeids_radius['55'] =2
nodeids_radius['45'] =1
nodeids_radius['10'] =1

#benchmark ids
benchids_node['55'] = ('10','45')
benchids_node['45'] = ('55','10')
benchids_node['10'] = ('45','55')

benchids_dst['55'] = (5,4)
benchids_dst['45'] = (4,8)
benchids_dst['10'] = (8,5)

N = 3#total nodes 
S = range(N)

x = [xp.var() for i in S]
y = [xp.var() for i in S]

print (x)

#problem formulation
p = xp.problem()
for i in S:
  p.addVariable(x[i])#x and y coordinates
  p.addVariable(y[i])

i = 0
for iter in nodeids:  #i is in the order of ids in nodeids
  mx[i] = nodeids_loc[iter][0]
  my[i] = nodeids_loc[iter][1]
  gpsradius[i] = nodeids_radius[iter]
  itercount.append(iter)
  i+=1

# polynomial constraint
for i in S:#each node
  p.addConstraint((x[i]-mx[i])**2+ (y[i]-my[i])**2<=gpsradius[i]) #own position gps

  #for each node, for the length of benchmarks=  nb distance constraints
  for kk in range(len(benchids_node[itercount[i]])):
     d[kk] = benchids_dst[itercount[i]][kk]#distance value set in benchid order 
     print(d[kk])
     bxy = nodeids_loc[benchids_node[itercount[i]][kk]]
     p.addConstraint(((x[i]-bxy[0])**2+(y[i]-bxy[1])**2)**0.5<=d[kk]+2) #distance constraint rssi
     p.addConstraint(((x[i]-bxy[0])**2+(y[i]-bxy[1])**2)**0.5>=d[kk]-2) #distance constraint rssi

#solving
p.setObjective(1)
p.solve()

print('solution: ', p.getSolution(x[2],y[2]))