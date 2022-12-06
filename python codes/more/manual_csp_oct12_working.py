# Codac - Examples
# Static range-bearing localization
# ----------------------------------------------------------------------------
from pyibex import *
from codac import *
import math
import random
import sys # only for checking if this example still works
btruth={}
benchids={}
ntruth = {}
sol_ids = {}
# =========== 2. Defining contractors to deal with equations ===========
ctc_plus = CtcFunction(Function("a", "b", "c", "a+b-c")) # a+b=c
ctc_minus = CtcFunction(Function("a", "b", "c", "a-b-c")) # a-b=c
ctc_circle = CtcFunction(Function("px", "py", "xc","yc","r","(px-xc)^2+(py-yc)^2-r^2"))

# =================== 0. Parameters, truth and data ====================
# Truth (unknown pose)
x_est_m2 = [1,3,math.atan2(3,1)] # (x,y,heading)#45 id
x_est_m1 = [5,5,math.atan2(5,5)] # (x,y,heading)#55 id
x_est_m3 = [10,1,math.atan2(10,1)] # (x,y,heading)#10 id

btruth['45']= [1,3,math.atan2(3,1)] # (x,y,heading)#n1
btruth['10']= [10, 1,math.atan2(1,10)] # (x,y,heading)#n1
btruth['55']= [5, 5,math.atan2(5,5)] # (x,y,heading)#n1

benchids['55'] = ['45','10']
benchids['45'] = ['55','10']
benchids['10'] = ['45','55']

x1 = 0.5
x2 = 2.5
x_truth= [x1,x2,math.atan2(x2,x1)] # (x,y,heading)#n1
e_bs = Interval(random.randint(-1,0),random.randint(0,1))
x11 = Interval(x1+e_bs)
x22 = Interval(x2+e_bs)
ntruth['45'] = [IntervalVector([x11,x22])]
x1 = 4.5
x2 = 6
x_truth= [4.5,6,math.atan2(6,4.5)] # (x,y,heading)#n1
e_bs = Interval(random.randint(-1,-0),random.randint(0,1))
x11 = Interval(x1+e_bs)
x22 = Interval(x2+e_bs)
ntruth['55'] = [IntervalVector([x11,x22])]
x1 = 9
x2 = 2
x_truth= [x1,x2,math.atan2(x2,x1)] # (x,y,heading)#n1
e_bs = Interval(random.randint(-1,-0),random.randint(0,1))
x11 = Interval(x1+e_bs)
x22 = Interval(x2+e_bs)
ntruth['10'] = [IntervalVector([x11,x22])]

# =============== 1. m2 ================
#m2 localization#45 
x = IntervalVector(2) # unknown position
heading = Interval(x_est_m2[2]).inflate(0.01) # measured heading
cn = ContractorNetwork()
gps = x_est_m2
gps_radius = 1

for  i in range (0,len(benchids['45'])):
  yy = benchids['45'][i]
  # The following function generates a set of [range]x[bearing] values
  v_obs = DataLoader.generate_static_observations(btruth[yy],ntruth['45'],False)
  for rg in v_obs: # We keep range-only observations from v_obs, and add uncertainties
      k = random.choice([-1, 1])*random.randrange(0,1)
      e_y = 0.5*rg[0]*Interval(k,k)#error depends on the distance by 0.01%
      rg[0] = rg[0]+e_y#randomly choose whether it shift in positive direction or negative direction
  #Adding uncertainties on the measurements 
  cn.add(ctc.dist, [x, ntruth[yy][0], v_obs[0][0]])
cn.add(ctc_circle,[x[0],x[1],gps[0],gps[1],gps_radius]) 
cn.contract()
print('m2',x)
sol_ids['45'] = x
#use the previous solution in the next localization
btruth['45'][0] =x[0].mid()
btruth['45'][1] =x[1].mid()
#print('45',btruth['45'] )

# ======================= 2. m1 =======================
#m1 localization#55
x = IntervalVector(2) # unknown position
heading = Interval(x_est_m1[2]).inflate(0.01) # measured heading
cn = ContractorNetwork()
gps = x_est_m1
gps_radius = 2
for  i in range (0,len(benchids['55'])):
  yy = benchids['55'][i]
  # The following function generates a set of [range]x[bearing] values
  v_obs = DataLoader.generate_static_observations(btruth[yy],ntruth['55'],False)
  for rg in v_obs: # We keep range-only observations from v_obs, and add uncertainties
      k = random.choice([-1, 1])*random.randrange(0,1)
      e_y = 0.5*rg[0]*Interval(k,k)#error depends on the distance by 0.01%
      rg[0] = rg[0]+e_y#randomly choose whether it shift in positive direction or negative direction
  #Adding uncertainties on the measurements 
  #print(ntruth[yy][0])
  cn.add(ctc.dist, [x, ntruth[yy][0], v_obs[0][0]])
cn.add(ctc_circle,[x[0],x[1],gps[0],gps[1],gps_radius]) 
cn.contract()
print('m1',x)
sol_ids['55'] = x
#use the previous solution in the next localization
btruth['55'][0] =x[0].mid()
btruth['55'][1] =x[1].mid()
#print('55',btruth['55'] )

# ======================= 3. m3 =======================
#m1 localization#55
x = IntervalVector(2) # unknown position
heading = Interval(x_est_m3[2]).inflate(0.01) # measured heading
cn = ContractorNetwork()
gps = x_est_m3
gps_radius = 1

for  i in range (0,len(benchids['10'])):
  yy = benchids['10'][i]
  # The following function generates a set of [range]x[bearing] values
  v_obs = DataLoader.generate_static_observations(btruth[yy],ntruth['10'],False)
  for rg in v_obs: # We keep range-only observations from v_obs, and add uncertainties
      k = random.choice([-1, 1])*random.randrange(0,1)
      e_y = 0.5*rg[0]*Interval(k,k)#error depends on the distance by 0.01%
      rg[0] = rg[0]+e_y#randomly choose whether it shift in positive direction or negative direction
  #Adding uncertainties on the measurements 
  #print(ntruth[yy][0])
  cn.add(ctc.dist, [x, ntruth[yy][0], v_obs[0][0]])
cn.add(ctc_circle,[x[0],x[1],gps[0],gps[1],gps_radius]) 
cn.contract()

print('m3',x)
sol_ids['10'] = x
#use the previous solution in the next localization
btruth['10'][0] =x[0].mid()
btruth['10'][1] =x[1].mid()
