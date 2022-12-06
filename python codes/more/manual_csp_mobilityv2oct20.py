from pyomo.environ import *
import numpy as np
import xpress as xp
import math
import random
import time
import pandas as pd
from scipy.spatial import distance
from sklearn.metrics import mean_squared_error
from numpy.linalg import inv
#TO INSTALL XPRESS: RUN 'pip install xpress'         
#initialization
nodeids_loc,nodeids_radius,benchids_node,benchids_dst,d,benchids_aoa,a={},{},{},{},{},{},{}
mx, my,gpsradius = {},{},{}
itercount=[]

#collect data
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

#benchmark distance
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

N = 3#total nodes 
S = range(N)

#benchmark aoa
for i in S:#each node
  astar = []
  for kk in range(len(benchids_node[itercount[i]])):
     deltay=nodeids_loc[itercount[i]][1] - nodeids_loc[benchids_node[itercount[i]][kk]][1]#kkth bench node y
     deltax=nodeids_loc[itercount[i]][0] - nodeids_loc[benchids_node[itercount[i]][kk]][0]#kkth bench node y

     astar=math.atan2(deltay,deltax)  
     if (benchids_aoa.get(itercount[i])==None):
       benchids_aoa[itercount[i]] = astar
     else:
       lst0 =benchids_aoa[itercount[i]]
       lst1 = astar
       benchids_aoa[itercount[i]] = (lst0,lst1)

x = [xp.var() for i in S]
y = [xp.var() for i in S]

#CSP formulation
p = xp.problem()
for i in S:
  p.addVariable(x[i])#x and y coordinates
  p.addVariable(y[i])


# enter data as numpy arrays
c = np.array([2,2,1])#weights

# set of column indices
J = range(len(c))

# create a model instance
model = ConcreteModel()

# create x and y variables in the model
model.x = Var(J,domain=Binary)

# add model constraints
model.constraints = ConstraintList()
model.constraints.add(sum(model.x[j] for j in J) <= sum(c))#total countr of contraints = 9
model.constraints.add(sum(model.x[j] for j in J) >= 1)#total countr of contraints = 9
#add the x to constraints in the CSP
#check whether the CSP problem gives a non empty solution when using the selected constraint set
#run csp algo 
#model.constraints.add((model.x[0]*x[0]-mx[0])**2+ (model.x[0]*y[0]-my[j])**2<=gpsradius[0])#own position gps

# add a model objective
model.objective = Objective(expr = sum(c[j]*model.x[j] for j in J), sense=minimize)

# create a solver
solver = SolverFactory('glpk')

# solve
solver.solve(model)

# print solutions
for j in J:
    print("x[", j, "] =", model.x[j].value)

model.constraints.display()

iter = 0
#run the csp here and check whether it gives none solution
# polynomial constraint
for j in J:#each node
  iter+=1
  if (model.x[j].value==1):  
    p.addConstraint((x[i]-mx[i])**2+ (y[i]-my[i])**2<=gpsradius[i]) #own position gps
    print('yes',iter)
