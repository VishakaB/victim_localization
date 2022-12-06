#seq
#last update: sep 17

from pyibex import *
from codac import *
import math
import random
import time
import numpy as np
import pandas as pd
from scipy.spatial import distance
from sklearn.metrics import mean_squared_error

# =================== 0. Import data =========================================================================================================================================================
df = pd. read_excel (r'15kv2.xlsx', sheet_name='priority')
rows = df.shape[0]
columns = df.shape[1]
random.seed(100)
outdoor_los=False
outdoor_nlos=False
indoor_nlos= True
alpharssi = 0.8
alphatoa = 0.2
alphatheta  = math.pi/6

# =================== 0. Parameters, truth and data ==========================================================================================================================================
iteration_dt = 2#time for solving csp problem(sec)
benchmark_truth,benchmark_est, update_count,dist_arr = [],[],[],[]
all_er_mean,all_est_coor, all_pix_coor , all_contract_time,time_arr ,id_time_arr = [],[],[],[],[],[]
xgps_all,ygps_all,all_x_gps,all_gps_radius ={},{},{},{}
node_incoverage , time_contract,id_contract={},{},{}
past_bench_ids,id_arr,time_carr = [],[], []
id_error,id_update,id_updategsp={},{},{}
id_time_error,err_minmax,error_count={},{},{}
time_error,id_count,sol_ids  ={},{},{}
time_complexity,node_heading,node_xtruth={},{},{}
nodearr,emergarr,sol = [],[],[]
node_benchids,node_benchtruth,all_x_gpstheta={},{},{}
id_time_cdt,id_time_est_coord={},{}
bench_heading ,btruth, ntruth,ntruthaoa={},{}, {},{}

#initial gps estimate of each benchmark node 
#def gps_estimate(starting_row, last_row):
for i in range(1,rows):
    emerg_ids = df.loc[i][2] # emerg id
    x_ids = df.loc[i][3] # node id
    x1 = df.loc[i][4]
    x2 = df.loc[i][5]
    if xgps_all.get(x_ids) == None:
        #gps_radius = 6745.75/(3372.87**(float(df.loc[i][11]))*0.0001)#worst : 3000, best : 2m
        gps_radius = 1954.737/(997.368**(float(df.loc[i][11])))#worst : 1000, best : 2m
        #gps_radius = 180/(75**float(df.loc[i][11]))
        #gps_radius = 1/(1**float(df.loc[i][11]))
        angle = 0.01*random.randint(0,600)
        #gps_radius=0
        x_gps = gps_radius*np.cos(angle)+x1
        y_gps = gps_radius*np.sin(angle)+x2
        xgps_all[x_ids] = x_gps  
        e_radius = Interval(0,0.1)#distance based error
        if ygps_all.get(x_ids) == None:
            ygps_all[x_ids] = y_gps 
    #print('angle',angle,np.cos(angle),np.sin(angle),gps_radius,x1,x2,x_gps,y_gps)
    #e_g = Interval(random.uniform(-(50+gps_radius),-gps_radius),random.uniform(gps_radius,gps_radius+50))
    if (outdoor_los==True):
        e_g = Interval(random.randint(-100,-25),random.randint(25,100))
    elif (outdoor_nlos==True):
        e_g = Interval(random.randint(-500,-100),random.randint(100,500))
    elif (indoor_nlos==True):
        e_g = Interval(random.randint(-1000,0),random.randint(0,1000))
    #g1 = Interval(xgps_all[x_ids]+e_g)
    #g2 = Interval(ygps_all[x_ids]+e_g)
    g1 = Interval(xgps_all[x_ids])
    g2 = Interval(ygps_all[x_ids])
    eudist_xtruth = (x1,x2)
    eudist_est = (g1.mid(),g2.mid())
    eudist =  distance.euclidean(eudist_xtruth,eudist_est)
    xy_gps =IntervalVector([g1,g2])#gps locations of nodes 
    all_gps_radius[x_ids]= Interval(eudist+e_g)
    if all_x_gps.get(x_ids) == None:
        all_x_gps[x_ids]=xy_gps#estimated locations of nodes  #estimated locations of nodes 
        x11 = all_x_gps[x_ids][0].mid()
        x22 = all_x_gps[x_ids][1].mid()
        if (all_x_gps[x_ids][0].is_empty()):
            print('yes empty',x_ids,all_x_gps[x_ids][0])
        heading_gps = (math.pi)/3.14*math.atan2(x2,x1)
        if (heading_gps<0):
          heading_gps = heading_gps+2*math.pi
        e_h = Interval(heading_gps).inflate(0.01)
        node_heading[x_ids] = e_h
        gps_theta =  (math.pi)/3.14*math.atan2(x22-x2,x11-x1)
        if (gps_theta<0):
          gps_theta = gps_theta+2*math.pi
        all_x_gpstheta[x_ids] = gps_theta

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
  avg_error = (dst/len(act_arr))
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

def theta_limitsv2(theta_truth,outdoor_los,outdoor_nlos,indoor_nlos):
    if (outdoor_los==True):
        max_error_angle = math.pi/10
    elif (outdoor_nlos==True):
        max_error_angle = math.pi/8
    elif (indoor_nlos==True):
        max_error_angle = alphatheta#indoor nlos 30 degrees to one side

    #theta_truth=math.atan2(deltay,deltax)    
    #if (theta_truth<0):
        #theta_truth=theta_truth+2*math.pi # form anticlockwise angle 
    #observed angle by bench
    a_obs=theta_truth + random.random()*2*max_error_angle-max_error_angle#30 degree variation

    amin=a_obs-(max_error_angle)#theta error opening 
    amax=a_obs+(max_error_angle)

    return [Interval(amin,amax)]

def error_range(range,outdoor_los,outdoor_nlos,indoor_nlos):
    if (outdoor_los==True):
        e_y = range*Interval(random.randint(-200,-50),random.randint(50,200))
    elif (outdoor_nlos==True):
        e_y = range*Interval(random.randint(-1500,-200),random.randint(200,1500))
    elif (indoor_nlos==True):
        e_y = 0.5*range*Interval(random.randint(-2000,-0),random.randint(0,2000))
    return e_y

def error_range_toa(range,outdoor_los,outdoor_nlos,indoor_nlos):
    if (outdoor_los==True):
        e_y = range*Interval(random.randint(-150,-30),random.randint(30,150))
    elif (outdoor_nlos==True):
        e_y = range*Interval(random.randint(-1250,-150),random.randint(150,1250))
    elif (indoor_nlos==True):
        e_y = 0.5*range*Interval(np.random.uniform(-alphatoa,0),np.random.uniform(0,alphatoa))
    return e_y

def error_gps(gpsestimate,outdoor_los,outdoor_nlos,indoor_nlos):
    if (outdoor_los==True):
        e_g = Interval(random.randint(-100,-25),random.randint(25,100))
    elif (outdoor_nlos==True):
        e_g = Interval(random.randint(-500,-100),random.randint(100,500))
    elif (indoor_nlos==True):
        e_g = Interval(random.randint(-1000,0),random.randint(0,1000))
    return e_g

def toa_with_uncertainities(xtruth,b):
    v_obstoa = DataLoader.generate_static_observations(xtruth,b, False)
    for tt in v_obstoa: # for each gps:
        e_toa = error_range_toa(tt[0],outdoor_los,outdoor_nlos,indoor_nlos)
        tt[0]= tt[0]+e_toa#range
        tt[1].inflate(0.0) # bearing
    return v_obstoa
    
def collect_data(j,emergarr,all_x_gps):
    nodeid = df.loc[j][3]
    if (nodeid in nodearr):#nodearr has all unique nodes
        tuy=0
    else:    
        nodearr.append(int(nodeid))
    emerg_ids = df.loc[j][2] # emerg id
    if (emerg_ids in emergarr):#nodearr has all unique nodes
        tuy=0
    else:    
        emergarr.append(emerg_ids)
    x1 = df.loc[j][4]
    x2 = df.loc[j][5]
    x_truth= [df.loc[j][4],df.loc[j][5],math.atan2(x2,x1)] # (x,y,heading)#n1
    e_bs = Interval(random.randint(-2000,-1200),random.randint(1200,2000))
    x11 = Interval(x1+e_bs)
    x22 = Interval(x2+e_bs)
    ntruth[int(nodeid)] = [IntervalVector([x11,x22])]
    e_aoa = Interval(random.randint(-1000000000000,-0),random.randint(0,1000000000000))#uncertain error
    xaoa = Interval(x1+e_aoa)
    yaoa = Interval(x2+e_aoa)
    ntruthaoa[int(nodeid)]= [IntervalVector([xaoa,yaoa])]
    if (node_xtruth.get(nodeid)== None):#nodeid, truth location 
        node_xtruth[nodeid] = x_truth

    if (node_benchids.get(str(int(nodeid)))== None):
        node_benchids[str(int(nodeid))] = str(df.loc[j][6])
    else:
        lst0 = node_benchids[str(int(nodeid))]
        lst = (df.loc[j][6])
        node_benchids[str(int(nodeid))] = str(lst0)+';'+str(lst)
  
    #benchmark locations, b
    benchmark1_truth =  [df.loc[j][7],df.loc[j][8]] #benchmark locations
    benchids = node_benchids[str(int(nodeid))].split(';')
    #yy =benchids[len(benchids)-1] #last bench id
    yy = str(df.loc[j][6])
    if (outdoor_los==True):
        e_g = Interval(random.randint(-1200,-700),random.randint(700,1200))
    elif (outdoor_nlos==True):
        e_g = Interval(random.randint(-2700,-1200),random.randint(1200,2700))
    elif (indoor_nlos==True):
        e_g = Interval(random.randint(-3500,-1200),random.randint(1200,3500))
    ####################################################################################################
    bench1 = float(benchmark1_truth[0])
    bench2 = float(benchmark1_truth[1]) 
    bench_heading[yy] = Interval(math.atan2(float(benchmark1_truth[1]),float(benchmark1_truth[0]))).inflate(0.01)#heading measurement with 0.01 error
    #btruth[yy] = [float(benchmark1_truth[0]),float(benchmark1_truth[1]),bench_heading[yy].mid()]
    btruth[yy]= [bench1, bench2,math.atan2(bench2,bench1)] # (x,y,heading)#n1
    ####################################################################################################
    if (yy=="gNB"):
        bench1 = float(benchmark1_truth[0])
        bench2 = float(benchmark1_truth[1])
        e_bs = Interval(random.randint(-1,0),random.randint(0,1))
        b1 = Interval(bench1+e_bs)
        b2 = Interval(bench2+e_bs)#estimated locations of bench nodes 
        toa = float(df.loc[j][13]) #time of arrival
        node_incoverage[nodeid] = True
    elif yy in all_x_gps:
        b1 = all_x_gps[yy][0]#estimated locations of bench nodes 
        b2 = all_x_gps[yy][1]#estimated locations of bench nodes 
    else:
        bench1 = float(benchmark1_truth[0])
        bench2 = float(benchmark1_truth[1])
        #e_bs = Interval(random.randint(-3000,-1000),random.randint(1000,3000))
        e_bs = Interval(random.randint(-1,0),random.randint(0,1))
        b1 = Interval(bench1+e_g)
        b2 = Interval(bench2+e_g)#estimated locations of bench nodes 
    benchmark_est = [IntervalVector([b1,b2])]

    if (node_benchtruth.get(int(nodeid))== None):#nodeid, benchtruth location 
        node_benchtruth[int(nodeid)] = (benchmark_est)
    else:
        lst0 = node_benchtruth[int(nodeid)]
        lst = benchmark_est
        node_benchtruth[int(nodeid)] = (lst0+lst)   
    return node_benchids,node_benchtruth,node_heading,emergarr



def forward_tracking(node_ids,node_benchids,node_benchtruth,node_heading,time,emergarr,all_x_gps,all_gps_radius,all_x_gpstheta):
    for iter in node_ids:#for each node recorded till now      
            id =iter
            b = node_benchtruth[iter]#data stored in the order of nbnode index
            gps = all_x_gps[iter]   
            gps_radius = all_gps_radius[iter]
            #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
            benchids = node_benchids[str(iter)].split(';')
            if (b[0].is_empty()):
                yyy= 0
                print('vobs empty')
            else:
                cn = ContractorNetwork() 
                ben_dist=[]
                for i in range (0,len(b)): # for each range and bearing measurement
                      p = cn.create_dom(IntervalVector(2))     
                      alpha = cn.create_dom(Interval())
                      d = cn.create_dom(IntervalVector(2))
                      yy = benchids[i]
                      if (len(sol_ids) != 0 ):
                          if (yy !='gNB'):
                              #print('benchid in sol id', sol_ids.get(int(yy))!=None)
                              if (sol_ids.get(int(yy))!=None):
                                  b[i] = sol_ids[int(yy)]
                                  btruth[yy][0] = b[i][0].mid()
                                  btruth[yy][1] = b[i][1].mid()
                      v_obs = DataLoader.generate_static_observations(btruth[yy],ntruth[iter],False)#generate actual range, bearing values
                      
                    #if (node_incoverage.get(iter)==None):#out of coverage                         
                          #print(v_obs)
                          #print(iter, yy,v_obs)
                      for rg in v_obs: # for observation type:range#shifting the actual range to a point within interval of error
                        k = random.choice([-1, 1])*np.random.uniform(0,alpharssi)
                        e_y =rg[0]*Interval(k,k)#error depends on the distance by 0.01%
                        rg[0] = rg[0]+e_y#randomly choose whether it shift in positive direction or negative direction
                      # Adding uncertainties on the measurements
                      ben_dist.append(v_obs[0][0].mid())  
                      cn.add(ctc.dist, [p, b[i], v_obs[0][0]])# Distance constraint: relation between the state at t_i and the ith beacon position                          
                cn.add(ctc_circle,[p[0],p[1],gps[0],gps[1],gps_radius]) 
                contraction_dt = cn.contract()#csp solving time set to 2 sec
                sol.append(p)
                #print(p)
                #distribute 50 points uniformly in the rectangle created by p
                mcl_points = []
                post_mcl_points =[]
                filtered_mcl_points=[]
                benchids = node_benchids[str(iter)].split(';')
                for i in range(0,50):#50 partcles considered
                  X = np.random.uniform(p[0][0], p[0][1]);
                  Y = np.random.uniform(p[1][0], p[1][1]);
                  mcl_points.append((X,Y))
                dst   = 0 
                for ii in range (0, len(mcl_points)):
                    for jj in range (0,len(b)):
                      anchor_pos = (b[jj][0].mid(),b[jj][1].mid())
                      #print('mcl point ii',mcl_points[ii])
                      dst= distance.euclidean(mcl_points[ii],anchor_pos)#convert to meters
                      
                      yy = benchids[jj]
                      v_obs = DataLoader.generate_static_observations(btruth[yy],ntruth[iter],False)
                      #ben_radius = v_obs[0][0].mid()
                      
                      if (ben_dist[jj]> dst):#if rssi dist < distance between the mcl point and anchor position remove that point
                        post_mcl_points.append(mcl_points[ii])
                #print(filtered_mcl_points)
                import collections
                ctr = collections.Counter(post_mcl_points)
                #print(ctr)
                #filtering the partcles that satisfy the rssi constraints
                for kk in range(len(ctr)):
                    if (ctr[post_mcl_points[kk]]==len(b)):
                        filtered_mcl_points.append(post_mcl_points[kk])
                for ll in range(len(filtered_mcl_points)):
                  averagex = np.average(filtered_mcl_points[ll][0])
                  averagey = np.average(filtered_mcl_points[ll][1])
                additional_complexity = 50+len(mcl_points)*len(b)+len(ctr)+len(filtered_mcl_points)
                if (time_complexity.get(time) ==None):
                    time_complexity[time] =additional_complexity+len(b)
                    time_carr.append(float(time))
                else:
                    time_complexity[time] = len(b)+additional_complexity+time_complexity.get(time)
                if (len(filtered_mcl_points)>0):
                  mcl_p = (averagex,averagey)
                  if (math.isnan(time)==False and time_contract.get(time)== None):
                      time_contract[time] = contraction_dt#time taken to localize a device in this time
                  elif (math.isnan(time)==False):
                      time_contract[time] = contraction_dt+ time_contract.get(time)
                  sol_ids[int(iter)] = p
                  if iter in emergarr:#only emerg node ids
                        x1 = node_xtruth[iter][0]
                        x2 = node_xtruth[iter][1]
                        all_pix_coor.append([x1,x2])
                        all_est_coor.append([mcl_p])
                        er = mean_square_error(all_pix_coor,all_est_coor)
                        #if (er>20):
                            #print(iter, [x1,x2],p[0].mid(),p[1].mid())
                        all_er_mean.append(er)#MSE in m^2
                        key = str(iter)+';'+str(time)
                        id_time_error[key] = er
                        id_time_arr.append(key)
                        id_time_cdt[key] = contraction_dt
                        id_time_est_coord[key] = (mcl_p)
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

# =========== Defining contractors to deal with equations ==================================================================================================================================
# We use the predefined contractor ctc.dist, no need to build it
ctc_plus = CtcFunction(Function("a", "b", "c", "a+b-c")) # a+b=c
ctc_minus = CtcFunction(Function("a", "b", "c", "a-b-c")) # a-b=c#a=b
ctc_polarx = CtcFunction(Function("a", "b", "c","d","a-b-c*cos(d)"))
ctc_polary = CtcFunction(Function("a", "b", "c","d","a-b-c*sin(d)"))
ctc_dist = CtcFunction(Function("x[2]", "b[2]", "y","sqrt((x[0]-b[0])^2+(x[1]-b[1])^2)-y"))
ctc_polar = CtcPolar()
ctc_circle = CtcFunction(Function("px", "py", "xc","yc","r","(px-xc)^2+(py-yc)^2-r^2"))
ctc_taninverse =CtcFunction(Function("x[2]", "b[2]","h","t","atan2(x[1]-b[1],x[0]-b[0])-h-t"))
ctc_sinlimits = CtcFunction(Function("x[2]", "b[2]","t","(x[1]-b[1])/((x[0]-b[0])^2+(x[1]-b[1])^2)-t"))
# =========== Contractor network ===========================================================================================================================================================
cn = ContractorNetwork()
# =========== Time constraints =============================================================================================================================================================
thirty_min_lb = 0 
thirty_min_ub = 1800 
jj = 1#index where data starts
t_ub = 120#update upper bound#time interval of csp problem update(sec)
sliding_count = 0
next_tub_stop=t_ub

past_data_refresh=False
while thirty_min_lb <= thirty_min_ub:#while now is below the upper bound of time domain
    time_error_count =0
    if float(df.loc[jj][13])< next_tub_stop and float(df.loc[jj][13])<= t_ub:  
         node_benchids,node_benchtruth,node_heading,emergarr =collect_data(jj,emergarr,all_x_gps)#collect past window data
         if (jj<rows):  
            jj+=1# jj: global node index 
    else: 
         time_error_count =0
         if (float(df.loc[jj][13])>thirty_min_ub and past_data_refresh==True):#if time is above 1800 and current node considered>last refreshed node
            print('here 2')
            sol_with_ids = forward_tracking(nodearr,node_benchids,node_benchtruth,node_heading,df.loc[jj][13],emergarr,all_x_gps,all_gps_radius,all_x_gpstheta)
         elif (past_data_refresh==False):#if time is between 0 and 1800 and past data not refreshed
            print('here 1')
            sol_with_ids = forward_tracking(nodearr,node_benchids,node_benchtruth,node_heading,df.loc[jj][13],emergarr,all_x_gps,all_gps_radius,all_x_gpstheta)
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
            sol_ids={}
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

print(all_er_mean)

# =========== Export data ===============================================================================================================================================================
import xlwt
list1 = id_contract
list2 = all_er_mean
book = xlwt.Workbook(encoding="utf-8")

i =1
sheet1 = book.add_sheet("Sheet 1")  
for n in range(0,len(id_error)):
    i = i+1#row number
    gg = id_arr[n]
    h  = id_error[int(gg)]
    sheet1.write(i, 0, int(gg))
    sheet1.write(i, 1, h)

k= 1
sheet2 = book.add_sheet("Sheet 2")    
for n in range(0,len(time_error)):
    k = k+1#row number
    gg = time_arr[n]
    h=time_contract[gg]
    sheet2.write(k, 0, gg)
    sheet2.write(k, 1, h)

u = 1
sheet3 = book.add_sheet("Sheet 3")    
for n in range(0,len(time_error)):
    u = u+1#row number
    gg = time_arr[n]
    h=time_error[gg]
    m = error_count[gg]
    dg = h/m
    sheet3.write(u, 0, gg)
    sheet3.write(u, 1, h)
    sheet3.write(u, 2, dg)

y = 1
sheet4 = book.add_sheet("Sheet 4")    
for n in range(0,len(time_complexity)):
    y = y+1#row number
    gg = time_carr[n]
    h=time_complexity[gg]
    sheet4.write(y, 0, gg)
    sheet4.write(y, 1, h)

vu = 1
sheet6 = book.add_sheet("Sheet 6")    
for n in range(0,len(id_time_error)):
    vu = vu+1#row number
    gg = id_time_arr[n]
    h=id_time_error[gg]
    sheet6.write(vu, 0, gg)
    sheet6.write(vu, 1, h)

ve = 1
sheet7 = book.add_sheet("Sheet 7")    
for n in range(0,len(err_minmax)):
    ve = ve+1#row number
    gg = time_arr[n]
    h=err_minmax[gg]
    #split h by ;
    x = h.split(';')
    m = error_count[gg]
    #nb rows = error count
    for pl in range(0,m):
        sheet7.write(pl, ve, x[pl])
    sheet7.write(m+1, ve, gg)

kk= 1
sheet8 = book.add_sheet("Sheet 8")    
for n in range(0,len(id_contract)):
    kk = kk+1#row number
    gg = id_arr[n]
    h  = id_contract[gg]
    sheet8.write(kk, 0, int(gg))
    sheet8.write(kk, 1, h)

vuu = 1
sheet9 = book.add_sheet("Sheet 9")    
for n in range(0,len(id_time_cdt)):
    vuu = vuu+1#row number
    gg = id_time_arr[n]
    h=id_time_cdt[gg]
    sheet9.write(vuu, 0, gg)
    sheet9.write(vuu, 1, h)

vt = 1
sheet10 = book.add_sheet("Sheet 10")    
for n in range(0,len(id_time_est_coord)):
    vt = vt+1#row number
    gg = id_time_arr[n]
    x = gg.split(';')
    h=id_time_est_coord[gg]
    sheet10.write(vt, 0, gg)
    sheet10.write(vt, 1,str(h))
    sheet10.write(vt, 2, str(node_xtruth[float(x[0])]))

book.save("montecarlo apd v33.xls")