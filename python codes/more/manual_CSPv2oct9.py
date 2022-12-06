import xpress as xp
import math
#TO INSTALL XPRESS: RUN 'pip install xpress'         

nodeids_loc={}
mx, my = {},{}
#initialization
nodeids = ['55','10','45']
nodeids_loc['55'] =(5,5)
nodeids_loc['10'] =(1,3)
nodeids_loc['45'] =(10,1)

N = 3
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
for iter in nodeids:  
  mx[i] = nodeids_loc[iter][0]
  my[i] = nodeids_loc[iter][1]
  i+=1
    
# polynomial constraint
for i in S:
  print(i,mx)
  p.addConstraint(x[i]-mx[i] <= 2)
  p.addConstraint(y[i]-my[i] <= 2)

#solving
#p.setObjective(1)
p.solve()

print('solution: ', p.getSolution(x[0],y[0]))