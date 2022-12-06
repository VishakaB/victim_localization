#ord
#last update: sep 17
import xpress as xp
import math
import random
import math
import random
import time
import numpy as np
import pandas as pd
from scipy.spatial import distance
from sklearn.metrics import mean_squared_error

# =================== 0. Import data =========================================================================================================================================================
df = pd. read_excel (r'15kv33.xlsx', sheet_name='priority')
rows = df.shape[0]
columns = df.shape[1]
random.seed(100)
outdoor_los=False
outdoor_nlos=False
indoor_nlos= True
rows = 500
# =================== 0. Parameters, truth and data ==========================================================================================================================================
nodeids_loc,nodeids_radius,benchids_node,benchids_dst,d,benchids_aoa,a={},{},{},{},{},{},{}
mx, my,gpsradius = {},{},{}
itercount=[]
xgps_all,ygps_all={},{}
nodeids_gps={}
node_incoverage={}

#initial gps estimate of each benchmark node 
#def gps_estimate(starting_row, last_row):
for i in range(1,rows):
    emerg_ids = df.loc[i][2] # emerg id
    x_ids = df.loc[i][3] # node id
    x1 = df.loc[i][4]
    x2 = df.loc[i][5]
    if xgps_all.get(x_ids) == None:
        gps_radius = 1994.737/(997.368**(float(df.loc[i][11])*0.001))#worst : 1000, best : 2m
        angle = 0.01*random.randint(0,600)
        x_gps = gps_radius*np.cos(angle)+x1
        y_gps = gps_radius*np.sin(angle)+x2
        xgps_all[x_ids] = x_gps  
        if ygps_all.get(x_ids) == None:
            ygps_all[x_ids] = y_gps 
    nodeids_gps[x_ids] = (x_gps,y_gps)
    nodeids_radius[x_ids] = gps_radius 

# =================== 0. Definitions ==================================================================================================================================================
def loc_area(x1,y1,x2,y2):
    area= abs(x1-x2)*abs(y1-y2)
    return area 

def mean_square_error(act_arr,est_arr):#vectors: estimated x1 y1 
  dst   = 0 
  for i in range (0, len(act_arr)):
      a = act_arr[i]
      b = est_arr[i]
      dst += distance.euclidean(a,b)#convert to meters
  avg_error = math.sqrt(dst/len(act_arr))
  return avg_error

def theta_limits(theta_truth,outdoor_los,outdoor_nlos,indoor_nlos,heading):
    if (outdoor_los==True):
        max_error_angle = math.pi/10
    elif (outdoor_nlos==True):
        max_error_angle = math.pi/8
    elif (indoor_nlos==True):
        max_error_angle = math.pi/6#indoor nlos 30 degrees to one side

    #theta_truth=math.atan2(deltay,deltax)    
    if (theta_truth<0):
        theta_truth=theta_truth+2*math.pi # form anticlockwise angle 
    #observed angle by bench
    #a_obs=theta_truth + random.random()*2*max_error_angle-max_error_angle+heading
    #random.random()*2*max_error_angle-max_error_angle#30 degree variation
    a_obs = theta_truth +np.random.uniform(0, max_error_angle)
    amin=a_obs-(max_error_angle)#theta error opening 
    amax=a_obs+(max_error_angle)
    return [Interval(amin,amax)]

def collect_data(j,emergarr,nodeids_gps,nodeids_radius):
    nodeid = df.loc[j][3]#str
    if (nodeid in nodearr):#nodearr has all unique nodes
        tuy=0
    else:    
        nodearr.append(nodeid)
    emerg_ids = df.loc[j][2] # emerg id
    if (emerg_ids in emergarr):#nodearr has all unique nodes
        tuy=0
    else:    
        emergarr.append(emerg_ids)
    x1 = df.loc[j][4]
    x2 = df.loc[j][5]
    x_truth= (df.loc[j][4],df.loc[j][5])# (x,y)

    if (nodeids_loc.get(nodeid)== None):#nodeid, truth location 
        nodeids_loc[nodeid] = x_truth

    yy = str(df.loc[j][6])
    if (benchids_node.get(nodeid)==None):
       benchids_node[nodeid] = yy
    else:
       lst0 =benchids_node[nodeid]
       lst1 = yy
       benchids_node[nodeid] = (lst0,lst1)

    benchmark1_truth =  [df.loc[j][7],df.loc[j][8]]
    if (yy=="gNB"):
        bench1 = float(benchmark1_truth[0])
        bench2 = float(benchmark1_truth[1])
        nodeids_gps['gNB'] = (bench1,bench2)
        node_incoverage[nodeid] = True
    elif yy in nodeids_gps:
        b1 = nodeids_gps[yy][0]#estimated locations of bench nodes 
        b2 = nodeids_gps[yy][1]#estimated locations of bench nodes 
    else:
        bench1 = float(benchmark1_truth[0])
        bench2 = float(benchmark1_truth[1])
        if xgps_all.get(nodeid) == None:
          gps_radius = 1994.737/(997.368**(float(df.loc[i][11])*0.001))#worst : 1000, best : 2m
          angle = 0.01*random.randint(0,600)
          x_gps = gps_radius*np.cos(angle)+bench1
          y_gps = gps_radius*np.sin(angle)+bench2
          xgps_all[x_ids] = x_gps  
          e_radius = Interval(0,0.1)#distance based error
          if ygps_all.get(nodeid) == None:
              ygps_all[nodeid] = y_gps 
          nodeids_gps[nodeid] = (x_gps,y_gps)
          nodeids_radius[nodeid] = gps_radius 
    return emergarr,nodearr,benchids_node,nodeids_gps,nodeids_radius

def forward_tracking(emergarr,nodearr,benchids_node,nodeids_gps,nodeids_radius,time):             
    N = len(nodearr)#total nodes 
    S = range(N)

    x = [xp.var() for i in S]
    y = [xp.var() for i in S]

    #CSP formulation
    p = xp.problem()
    for i in S:
      p.addVariable(x[i])#x and y coordinates
      p.addVariable(y[i])

    # polynomial constraint
    for i in S:#each node
      p.addConstraint((x[i]-mx[i])**2+ (y[i]-my[i])**2<=gpsradius[i]) #own position gps

      #for each node, for the length of benchmarks=  nb distance constraints
      for kk in range(len(benchids_node[itercount[i]])):
        d[kk] = benchids_dst[itercount[i]][kk]#distance value set in benchid order #true distance
        bxy = nodeids_loc[benchids_node[itercount[i]][kk]]
        alpharssi = 0.5*d[kk]*2#rssi error
        d[kk] = d[kk]+random.choice([-1, 1])*random.uniform(0,alpharssi)#estimated distance

        p.addConstraint(((x[i]-bxy[0])**2+(y[i]-bxy[1])**2)**0.5<=d[kk]*(1+alpharssi)) #distance constraint rssi
        p.addConstraint(((x[i]-bxy[0])**2+(y[i]-bxy[1])**2)**0.5>=d[kk]*(1-alpharssi)) #distance constraint rssi
        #add toa constraint#if incoverage
        
        #aoa constraint
        op=0.1#aoa error
        a[kk] = benchids_aoa[itercount[i]][kk]#in benchid order #true angle
        a[kk]=a[kk] + random.choice([-1, 1])*random.uniform(0,op)

        amin=a[kk]-op
        amax=a[kk]+op
        if amin>-3.14159 and amax<=3.14159 :
          yyy=0
          p.addConstraint((y[i]-bxy[1])/(x[i]-bxy[0])<=math.tan(amax))
          p.addConstraint((y[i]-bxy[1])/(x[i]-bxy[0])>=math.tan(amin))
        elif amin<=-3.14159 :
          p.addConstraint((y[i]-bxy[1])/((x[i]-bxy[0])**2+(y[i]-bxy[1])**2)<=math.sin(6.28318-amin))
          p.addConstraint((y[i]-bxy[1])/((x[i]-bxy[0])**2+(y[i]-bxy[1])**2)>=math.sin(amax))
        elif amax>3.14159 :
          p.addConstraint((y[i]-bxy[1])/((x[i]-bxy[0])**2+(y[i]-bxy[1])**2)<=math.sin(amax-6.28318))
          p.addConstraint((y[i]-bxy[1])/((x[i]-bxy[0])**2+(y[i]-bxy[1])**2)>=math.sin(amin))

    #solving
    p.setObjective(1)
    p.solve()

    if p.contains(node_xtruth[iter]):
        toff=0
    else:
        tgop=0
        #print('iter',iter)
    #err mean
    if (p[0].is_empty()):
        print('iter',iter)
        print('b',b)
        print('xtruth',node_xtruth[iter])
        print('p',p)
        print('yea',gps,id)
    else: 
        if (math.isnan(time)==False and time_contract.get(time)== None):
            time_contract[time] = contraction_dt#time taken to localize a device in this time
        elif (math.isnan(time)==False):
            time_contract[time] = contraction_dt+ time_contract.get(time)
        if iter in emergarr:#only emerg node ids
              x1 = node_xtruth[iter][0]
              x2 = node_xtruth[iter][1]
              all_pix_coor.append([x1,x2])
              all_est_coor.append([p[0].mid(),p[1].mid()])
              er = mean_square_error(all_pix_coor,all_est_coor)
              #if (er>20):
                  #print(iter, [x1,x2],p[0].mid(),p[1].mid())
              all_er_mean.append(er)#MSE in m^2
              key = str(iter)+';'+str(time)
              id_time_error[key] = er
              id_time_arr.append(key)
              id_time_cdt[key] = contraction_dt
              id_time_est_coord[key] = (p[0],p[1])
              if (id_error.get(iter)== None):
                  id_error[iter] = er
                  id_count[iter] = 1
                  id_arr.append(iter)
              else:
                  id_count[iter]= 1+id_count[iter]
                  id_error[iter] = (er+id_error.get(iter))/id_count[iter]
              if (math.isnan(time)==False and time_error.get(time)== None):
                  time_error[time] = er#only emerg device
                  error_count[time]= 1
                  time_arr.append(time)#use to identify the time
                  err_minmax[time] = str(er)
              elif (math.isnan(time)==False):
                  time_error[time] = er+time_error.get(time)#only emerg device
                  error_count[time]= 1+error_count.get(time)
                  err_minmax[time] = err_minmax.get(time)+';'+str(er)
              if (id_contract.get(iter)== None):
                  id_contract[iter] = contraction_dt
              else:
                  id_contract[iter] = contraction_dt+ id_contract.get(iter)                               
    return sol_ids

# =========== Time constraints =============================================================================================================================================================
thirty_min_lb = 0 
thirty_min_ub = 1800 
jj = 1#index where data starts
t_ub = 120#update upper bound#time interval of csp problem update(sec)
sliding_count = 0
next_tub_stop=t_ub
emergarr,nodearr=[],[]
j = 1

past_data_refresh=False
while thirty_min_lb <= thirty_min_ub:#while now is below the upper bound of time domain
    time_error_count =0
    if float(df.loc[jj][13])< next_tub_stop and float(df.loc[jj][13])<= t_ub:  
         emergarr,nodearr,node_benchids,nodeids_gps,nodeids_radius =collect_data(jj,emergarr,nodeids_gps,nodeids_radius)#collect past window data
         if (jj<rows):  
            jj+=1# jj: global node index 
    else: 
         time_error_count =0
         if (float(df.loc[jj][13])>thirty_min_ub and past_data_refresh==True):#if time is above 1800 and current node considered>last refreshed node
            print('here 2')
            sol_with_ids = forward_tracking(emergarr,nodearr,benchids_node,nodeids_gps,nodeids_radius,df.loc[jj][13])
         elif (past_data_refresh==False):#if time is between 0 and 1800 and past data not refreshed
            print('here 1')
            sol_with_ids = forward_tracking(emergarr,nodearr,benchids_node,nodeids_gps,nodeids_radius,df.loc[jj][13])
         if (float(df.loc[jj][13])>thirty_min_ub):           
            past_data_refresh=True
            #pp ==jj#last node index before refreshing
            thirty_min_ub+=120#sliding window by 120
            thirty_min_lb+=120
            sliding_count +=1
            jj =1
            while (float(df.loc[jj][13])<thirty_min_lb ):    
                jj+=1  #setting starting data row related to 30 min lower bound
            t_ub = (sliding_count+1)*120#starting t_ub
            past_tub_stop = t_ub#past localization stop tub
            next_tub_stop=past_tub_stop +120
            #clear previous input arr
            node_benchids = {}#data refresh
            node_benchtruth = {}
            node_y = {}
            node_theta = {}
            node_ids = {}
            nodearr = []
            emergarr =[]
            nodearr = []
         while (float(df.loc[jj][13])> t_ub):    
            t_ub+=120  
            next_tub_stop+=120
         print('routinely update',jj) 
         node_benchids = {}#data refresh
         node_benchtruth = {}
         node_y = {}
         node_theta = {}
         node_ids = {}
         nodearr = []
    if (jj==rows):#last data received from simulation
         break  
