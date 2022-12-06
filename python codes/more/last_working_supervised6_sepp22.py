#apd
#last update: sep 20
#5000 devices
from pyibex import *
from codac import *
import math
import random
import time
import numpy as np
import pandas as pd
from scipy.spatial import distance
from sklearn.metrics import mean_squared_error

# =================== 0. Import data ====================
df = pd. read_excel (r'15kv35.xlsx', sheet_name='Input')
rows = df.shape[0]
columns = df.shape[1]
random.seed(100)
outdoor_los=False
outdoor_nlos=False
indoor_nlos= True
no_aoa = True
toa_availability = False 

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
bench_heading ,btruth, ntruth,ntruthaoa={},{},{}, {}

#initial gps estimate of each benchmark node 
#def gps_estimate(starting_row, last_row):
for i in range(1,rows):
    emerg_ids = df.loc[i][2] # emerg id
    x_ids = df.loc[i][3] # node id
    x1 = df.loc[i][4]
    x2 = df.loc[i][5]
    if xgps_all.get(x_ids) == None:
        gps_radius = 3*1994.737/(997.368**float(df.loc[i][11]))#worst : 1000, best : 2m
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
        e_g = Interval(random.randint(-3000,0),random.randint(0,3000))
    #g1 = Interval(xgps_all[x_ids]+e_g)
    #g2 = Interval(ygps_all[x_ids]+e_g)
    #e_x = Interval(random.randint(-eudist*cos(),0),random.randint(0,eudist*cos()))
    #e_y = Interval(random.randint(-eudist*sin(),0),random.randint(0,eudist*sin()))
    e_cx = Interval(random.randint(-1000,0),random.randint(0,1000))
    e_cy = Interval(random.randint(-1000,0),random.randint(0,1000))
    g1 = Interval(xgps_all[x_ids]+e_cx)
    g2 = Interval(ygps_all[x_ids]+e_cy)
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
    a_obs = theta_truth +np.random.uniform(0, max_error_angle/2)
    amin=a_obs-(max_error_angle)#theta error opening 
    amax=a_obs+(max_error_angle)
    return [Interval(amin,amax)]

def theta_limitsv2(theta_truth,outdoor_los,outdoor_nlos,indoor_nlos):
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
    a_obs=theta_truth + random.random()*2*max_error_angle-max_error_angle#30 degree variation

    amin=a_obs-(max_error_angle)#theta error opening 
    amax=a_obs+(max_error_angle)

    return [Interval(amin,amax)]

def error_range(range,outdoor_los,outdoor_nlos,indoor_nlos):
    if (outdoor_los==True):
        e_y = 0.1*range*Interval(random.randint(-200,-50),random.randint(50,200))
    elif (outdoor_nlos==True):
        e_y = 0.1*range*Interval(random.randint(-1500,-200),random.randint(200,1500))
    elif (indoor_nlos==True):
        e_y = 0.1*range*Interval(random.randint(-3000,-1000),random.randint(1000,3000))
    return e_y

def error_range_toa(range,outdoor_los,outdoor_nlos,indoor_nlos):
    if (outdoor_los==True):
        e_y = 0.1*range*Interval(random.randint(-150,-30),random.randint(30,150))
    elif (outdoor_nlos==True):
        e_y = 0.1*range*Interval(random.randint(-1250,-150),random.randint(150,1250))
    elif (indoor_nlos==True):
        e_y = 0.1*range*Interval(random.randint(-15,-1),random.randint(1,15))
    return e_y

def error_gps(gpsestimate,outdoor_los,outdoor_nlos,indoor_nlos):
    if (outdoor_los==True):
        e_g = Interval(random.randint(-100,-25),random.randint(25,100))
    elif (outdoor_nlos==True):
        e_g = Interval(random.randint(-500,-100),random.randint(100,500))
    elif (indoor_nlos==True):
        e_g = Interval(random.randint(-3000,0),random.randint(0,3000))
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
    e_bs = Interval(random.randint(-1000,0),random.randint(0,1000))
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
        e_bs = Interval(random.randint(-1000,0),random.randint(0,1000))
        b1 = Interval(bench1+e_bs)
        b2 = Interval(bench2+e_bs)#estimated locations of bench nodes 
        toa = float(df.loc[j][13]) #time of arrival
        node_incoverage[nodeid] = True
    else:
        bench1 = float(benchmark1_truth[0])
        bench2 = float(benchmark1_truth[1])
        e_bs = Interval(random.randint(-1,0),random.randint(0,1))
        e_cx = Interval(random.randint(-1000,0),random.randint(0,1000))
        e_cy = Interval(random.randint(-1000,0),random.randint(0,1000))
        b1 = Interval(bench1+e_cx)
        b2 = Interval(bench2+e_cy)#estimated locations of bench nodes 
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
                if (time_complexity.get(time) ==None):
                    time_complexity[time] =len(b)
                    time_carr.append(float(time))
                else:
                    time_complexity[time] = len(b)+time_complexity.get(time)
                cn = ContractorNetwork() 
                
                for i in range (0,len(b)): # for each range and bearing measurement
                      p = cn.create_dom(IntervalVector(2))     
                      alpha = cn.create_dom(Interval())
                      d = cn.create_dom(IntervalVector(2))
                      yy = benchids[i]
                      v_obs = DataLoader.generate_static_observations(btruth[yy],ntruth[iter],False)#generate actual range, bearing values
                      for rg in v_obs: # for observation type:range#shifting the actual range to a point within interval of error
                        k = random.choice([-1, 1])*random.randrange(1000,1500)
                        e_y =0.1*rg[0]*Interval(k,k)#error depends on the distance by 0.01%
                        rg[0] = rg[0]+e_y#randomly choose whether it shift in positive direction or negative direction
                      # Adding uncertainties on the measurements
                      for hh in v_obs: # for each observation:
                        e_y = 0.1*hh[0]*Interval(random.randint(-2000,-1000),random.randint(1000,2000))################################################################################
                        hh[0]= hh[0]+e_y#range
                        hh[1].inflate(0.0) # bearing 
                        cn.add(ctc.dist, [p, b[i], v_obs[0][0]])# Distance constraint: relation between the state at t_i and the ith beacon position
                      if (node_incoverage.get(iter)!=None):#incoverage                        
                          v_obs_toa=toa_with_uncertainities(btruth[yy],ntruth[iter])   
                          for i in range (0,len(v_obs_toa)):
                                #toa based range measurements obtain & adding uncertainities
                                cn.add(ctc.dist, [p, b[i], v_obs_toa[i][0]])#toa based-range constraint
                          Y = (btruth[yy][0],btruth[yy][1])
                          X = (ntruth[iter][0][0].mid(),ntruth[iter][0][1].mid())
                          v_bangle = DataLoader.generate_static_observations(btruth[yy],ntruthaoa[iter],False)
                          heading = btruth[yy][2]
                          bangle = math.atan2(X[1]-Y[1],X[0]-Y[0])-heading
                          #print(bangle,(v_bangle[0][1].mid()))
                          a = theta_limits(v_bangle[0][1].mid(),outdoor_los,outdoor_nlos,indoor_nlos,btruth[yy][2])
                          theta_est =  IntervalVector(a)                         
                          #print('bangle',180/3.14*theta_est)
                          #theta_est = Interval(bangle-0.01,bangle+0.01)
                          #print('**',180/3.14*theta_est) 
                          amin = theta_est[0][0]
                          amax = theta_est[0][1] 
                          if amin>-3.14159 and amax<=3.14159:
                            #print("atan2(y1-y2,x1-x2)<=",amax)
                            #print("atan2(y1-y2,x1-x2)>=",amin)
                            theta_est=  IntervalVector([Interval(amin,amax)])
                            #print(theta_est)
                            cn.add(ctc_taninverse, [p,b[i],heading, theta_est])
                            #cn.add(ctc_plus, [theta_est, heading, alpha])#angle constraint#heading wrt bench
                            #cn.add(ctc_minus, [p,b[i], d])
                            #cn.add(ctc_polar, [d,v_bangle[0][0], alpha])
                          elif amin<=-3.14159 :
                            #print("x1-x2<0")
                            #print("(y1-y2)/((x1-x2)^2+(y1-y2)^2)=<",math.sin(6.28318+amin))
                            #print("(y1-y2)/((x1-x2)^2+(y1-y2)^2)>=",math.sin(amax))
                            sin_lb = math.sin(amax)
                            sin_ub = math.sin(6.28318+amin)
                            sin_limits = IntervalVector([Interval(sin_lb,sin_ub)])
                            #print('sin limits',sin_lb, sin_ub)
                            cn.add(ctc_sinlimits, [p,b[i], sin_limits])
                          elif amax>3.14159 :
                            #print("x1-x2<0")
                            #print("(y1-y2)/((x1-x2)^2+(y1-y2)^2)>=",math.sin(amax-6.28318))
                            #print("(y1-y2)/((x1-x2)^2+(y1-y2)^2)<=",math.sin(amin)) 
                            sin_lb = math.sin(amax-6.28318)
                            sin_ub = math.sin(amin)                            
                            #print("3",sin_lb,sin_ub)
                            if (sin_lb>sin_ub):
                              sin_limits = IntervalVector([Interval(sin_ub,sin_lb)])
                              cn.add(ctc_sinlimits, [p,b[i], sin_limits])  
                            else:
                              sin_limits = IntervalVector([Interval(sin_lb,sin_ub)])
                              cn.add(ctc_sinlimits, [p,b[i], sin_limits])  

                cn.add(ctc_circle,[p[0],p[1],gps[0],gps[1],gps_radius])   
                #print(iter)
                #print(cn)      
                contraction_dt = cn.contract()#csp solving time set to 2 sec
                sol.append(p)
                #print(p)
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

# =========== Defining contractors to deal with equations ==================================================================================================================================
# We use the predefined contractor ctc.dist, no need to build it
ctc_plus = CtcFunction(Function("a", "b", "c", "a+b-c")) # a+b=c
ctc_minus = CtcFunction(Function("a", "b", "c", "a-b-c")) # a-b=c#a=b
ctc_polarx = CtcFunction(Function("a", "b", "c","d","a-b-c*cos(d)"))
ctc_polary = CtcFunction(Function("a", "b", "c","d","a-b-c*sin(d)"))
ctc_dist = CtcFunction(Function("x[2]", "b[2]", "y","sqrt((x[0]-b[0])^2+(x[1]-b[1])^2)-y"))
ctc_polar = CtcPolar()
ctc_circle = CtcFunction(Function("px", "py", "xc","yc","r","sqrt((px-xc)^2+(py-yc)^2)-r"))
ctc_taninverse =CtcFunction(Function("x[2]", "b[2]","h","t","atan2(x[1]-b[1],x[0]-b[0])-h-t"))
ctc_sinlimits = CtcFunction(Function("x[2]", "b[2]","t","(x[1]-b[1])/((x[0]-b[0])^2+(x[1]-b[1])^2)-t"))
# =========== Contractor network ===========================================================================================================================================================
cn = ContractorNetwork()
# =========== Time constraints ===========

thirty_min_lb = 0 
thirty_min_ub = 1800 
jj = 1
t_ub = 120#update upper bound
sliding_count = 0
pp = 355
past_data_refresh=False
while thirty_min_lb <= thirty_min_ub:#while now is below the upper bound of time domain
    time_error_count =0
    #print('33',jj)
    if float(df.loc[jj][13])<= t_ub:  
         node_benchids,node_benchtruth,node_heading,emergarr =collect_data(jj,emergarr,all_x_gps)
         #print('node_bids',nodearr)
         if (jj<rows):  
            jj+=1# jj: global node index
    else: 
         time_error_count =0
         #sol_with_ids = forward_tracking(nodearr,node_benchids,node_benchtruth,node_theta,node_y,node_heading,df.loc[jj][13],emergarr,all_x_gps,all_gps_radius,all_x_gpstheta)
         if (float(df.loc[jj][13])>thirty_min_ub and past_data_refresh==True):#if time is above 1800 and current node considered>last refreshed node
            print('here 2')
            sol_with_ids = forward_tracking(nodearr,node_benchids,node_benchtruth,node_heading,df.loc[jj][13],emergarr,all_x_gps,all_gps_radius,all_x_gpstheta)
         elif (past_data_refresh==False):#if time is between 0 and 1800 and past data not refreshed
            print('here 1')
            sol_with_ids = forward_tracking(nodearr,node_benchids,node_benchtruth,node_heading,df.loc[jj][13],emergarr,all_x_gps,all_gps_radius,all_x_gpstheta)
         if (float(df.loc[jj][13])>thirty_min_ub):
            past_data_refresh=True
            pp ==jj#last node index before refreshing
            thirty_min_ub+=120#sliding window by 120
            thirty_min_lb+=120
            sliding_count +=1
            #all_x_gps,all_x_gpstheta,node_heading = gps_estimate(starting_row, jj)#initial gps estimate is also refreshed
            jj =1
            while (float(df.loc[jj][13])<thirty_min_lb ):    
                jj+=1  #setting starting data row related to 30 min lower bound
            t_ub = (sliding_count+1)*120#starting t_ub
            
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
         print('routinely update',jj) 
    if (jj==rows):#last data received from simulation
         break  
print(all_er_mean)

# =========== Export data ===========
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

book.save("apd all.xls")
