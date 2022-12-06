# Codac - Examples
# Static range-bearing localization
# ----------------------------------------------------------------------------
from pyibex import *
from codac import *
import math
import sys # only for checking if this example still works

# =================== 0. Parameters, truth and data ====================
# Truth (unknown pose)
x_est_m2 = [1,3,math.atan2(3,1)] # (x,y,heading)
x_est_m1 = [5,5,math.atan2(5,5)] # (x,y,heading)
x_est_m3 = [10,1,math.atan2(10,1)] # (x,y,heading)

# Creating random map of landmarks
map_area = IntervalVector(2, [-15,15])
v_map = DataLoader.generate_landmarks_boxes(map_area, nb_landmarks = 2)

# The following function generates a set of [range]x[bearing] values
v_obs = DataLoader.generate_static_observations(x_est_m2, v_map, False)

# We keep range-only observations from v_obs, and add uncertainties
v_range = []
for obs in v_obs:
  r = obs[0].inflate(0.6) # adding uncertainties: [-0.6,0.6]
  v_range.append(r)

# =============== 1. Defining domains for our variables ================
x = IntervalVector(2) # unknown position
heading = Interval(x_est_m2[2]).inflate(0.01) # measured heading

# =========== 2. Defining contractors to deal with equations ===========
ctc_plus = CtcFunction(Function("a", "b", "c", "a+b-c")) # a+b=c
ctc_minus = CtcFunction(Function("a", "b", "c", "a-b-c")) # a-b=c
ctc_circle = CtcFunction(Function("px", "py", "xc","yc","r","(px-xc)^2+(py-yc)^2-r^2"))

# =============== 3. Adding the contractors to a network ===============
#m2 localization
cn = ContractorNetwork()
gps = x_est_m2
gps_radius = 1

for i in range(0,len(v_range)):
  cn.add(ctc.dist, [x, v_map[i], v_range[i]])
cn.add(ctc_circle,[x[0],x[1],gps[0],gps[1],gps_radius]) 

# ======================= 4. Solving the problem =======================
cn.contract()
print(x)

#use the previous solution in the next localization
x_est_m2 = [x[0].mid(),x[1].mid(),math.atan2(x[1].mid(),x[0].mid())]

#m1 localization
# The following function generates a set of [range]x[bearing] values
v_obs = DataLoader.generate_static_observations(x_est_m1, v_map, False)

# We keep range-only observations from v_obs, and add uncertainties
v_range = []
for obs in v_obs:
  r = obs[0].inflate(1) # adding uncertainties: [-0.6,0.6]
  v_range.append(r)

x = IntervalVector(2) # unknown position
heading = Interval(x_est_m1[2]).inflate(0.01) # measured heading

gps = x_est_m1
gps_radius = 2

for i in range(0,len(v_range)):
  cn.add(ctc.dist, [x, v_map[i], v_range[i]])
cn.add(ctc_circle,[x[0],x[1],gps[0],gps[1],gps_radius]) 
cn.contract()

print(x.mid())

#use the previous solution in the next localization
x_est_m1 = [x[0].mid(),x[1].mid(),math.atan2(x[1].mid(),x[0].mid())]

#m3 localization
# The following function generates a set of [range]x[bearing] values
v_obs = DataLoader.generate_static_observations(x_est_m3, v_map, False)

# We keep range-only observations from v_obs, and add uncertainties
v_range = []
for obs in v_obs:
  r = obs[0].inflate(0.57) # adding uncertainties: [-0.6,0.6]
  v_range.append(r)

x = IntervalVector(2) # unknown position
heading = Interval(x_est_m3[2]).inflate(0.01) # measured heading

gps = x_est_m3
gps_radius = 1

for i in range(0,len(v_range)):
  cn.add(ctc.dist, [x, v_map[i], v_range[i]])
cn.add(ctc_circle,[x[0],x[1],gps[0],gps[1],gps_radius]) 
cn.contract()

print(x)