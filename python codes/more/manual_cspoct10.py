import xpress as xp
import math
#TO INSTALL XPRESS: RUN 'pip install xpress'         
#initialization
nodeids_loc,nodeids_radius,benchids_node,benchids_dst,d,benchids_aoa,a={},{},{},{},{},{},{}
mx, my,gpsradius = {},{},{}
itercount=[]

nodeids = ['55','10','45']#ids

#positions
nodeids_loc['55'] =(5,5)
nodeids_loc['10'] =(10,1)
nodeids_loc['45'] =(1,3)


#gps radii
nodeids_radius['55'] =2
nodeids_radius['10'] =1
nodeids_radius['45'] =1

#benchmark ids
benchids_node['55'] = ('10','45')
benchids_node['10'] = ('45','55')
benchids_node['45'] = ('55','10')

benchids_dst['55'] = (5,4)
benchids_dst['10'] = (8,5)
benchids_dst['45'] = (4,8)

i = 0
for iter in nodeids:  #i is in the order of ids in nodeids
  mx[i] = nodeids_loc[iter][0]
  my[i] = nodeids_loc[iter][1]
  gpsradius[i] = nodeids_radius[iter]
  itercount.append(iter)
  i+=1
for i in S:#each node
  astar = []
  for kk in range(len(benchids_node[itercount[i]])):
     deltay=nodeids_loc[itercount[i]][1] - nodeids_loc[benchids_node[itercount[i]][kk]][1]#kkth bench node y
     deltax=nodeids_loc[itercount[i]][0] - nodeids_loc[benchids_node[itercount[i]][kk]][0]#kkth bench node y
     print(deltay)

     astar=math.atan2(deltay,deltax)  
     if (benchids_aoa.get(itercount[i])==None):
       benchids_aoa[itercount[i]] = astar
     else:
       lst0 =benchids_aoa[itercount[i]]
       lst1 = astar
       benchids_aoa[itercount[i]] = (lst0,lst1)

print('aoa bench',benchids_aoa)

N = 3#total nodes 
S = range(N)

x = [xp.var() for i in S]
y = [xp.var() for i in S]

#problem formulation
p = xp.problem()
for i in S:
  p.addVariable(x[i])#x and y coordinates
  p.addVariable(y[i])

import random
# polynomial constraint
for i in S:#each node
  p.addConstraint((x[i]-mx[i])**2+ (y[i]-my[i])**2<=gpsradius[i]) #own position gps

  #for each node, for the length of benchmarks=  nb distance constraints
  for kk in range(len(benchids_node[itercount[i]])):
     d[kk] = benchids_dst[itercount[i]][kk]#distance value set in benchid order #true distance
     print(d[kk])
     bxy = nodeids_loc[benchids_node[itercount[i]][kk]]
     alpharssi = 0.5*d[kk]*2#rssi error
     d[kk] = d[kk]+random.choice([-1, 1])*random.uniform(0,alpharssi)#estimated distance

     p.addConstraint(((x[i]-bxy[0])**2+(y[i]-bxy[1])**2)**0.5<=d[kk]*(1+alpharssi)) #distance constraint rssi
     p.addConstraint(((x[i]-bxy[0])**2+(y[i]-bxy[1])**2)**0.5>=d[kk]*(1-alpharssi)) #distance constraint rssi
     #add toa constraint#if incoverage
     
     #aoa constraint
     op=0.1#aoa error
     print(benchids_aoa[itercount[i]][kk])
     a[kk] = benchids_aoa[itercount[i]][kk]#in benchid order #true angle
     a[kk]=a[kk] + random.choice([-1, 1])*random.uniform(0,op)

     amin=a[kk]-op
     amax=a[kk]+op
     if amin>-3.14159 and amax<=3.14159 :
      yyy=0
      p.addConstraint((y[i]-bxy[1])/(x[i]-bxy[0])<=math.tan(amax))
      p.addConstraint((y[i]-bxy[1])/(x[i]-bxy[0])>=math.tan(amin))
     elif amin<=-3.14159 :
      print("x1-x2<0")
      p.addConstraint((y[i]-bxy[1])/((x[i]-bxy[0])**2+(y[i]-bxy[1])**2)<=math.sin(6.28318-amin))
      p.addConstraint((y[i]-bxy[1])/((x[i]-bxy[0])**2+(y[i]-bxy[1])**2)>=math.sin(amax))
      print("(y1-y2)/((x1-x2)^2+(y1-y2)^2)=<",math.sin(6.28318-amin))
      print("(y1-y2)/((x1-x2)^2+(y1-y2)^2)>=",math.sin(amax))
     elif amax>3.14159 :
      print("x1-x2<0 2")
      p.addConstraint((y[i]-bxy[1])/((x[i]-bxy[0])**2+(y[i]-bxy[1])**2)<=math.sin(amax-6.28318))
      p.addConstraint((y[i]-bxy[1])/((x[i]-bxy[0])**2+(y[i]-bxy[1])**2)>=math.sin(amin))
      print("(y1-y2)/((x1-x2)^2+(y1-y2)^2)>=",math.sin(amax-6.28318))
      print("(y1-y2)/((x1-x2)^2+(y1-y2)^2)<=",math.sin(amin))

#solving
p.setObjective(1)
p.solve()

print('solution: ', p.getSolution())