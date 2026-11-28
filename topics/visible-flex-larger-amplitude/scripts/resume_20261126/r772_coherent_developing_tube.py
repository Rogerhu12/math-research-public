"""R772 coherent translation tube, complete two-jets in the axial cylinder, both rounded heads and both disks."""
from functools import lru_cache
import numpy as np
import r767_negative_track_profile as guard
from r742_tilted_disk_two_jets import J,unary,gather,trig
from r767_negative_track_profile import smooth_curve
from r767_preloaded_cap_atlas import root,angle
from r740_rolled_disk_seed import rule,softened_angle,s5
R=.27
SM=.001
FLAT=.14
QUARTER=R*np.pi/2+SM
BLOCK=FLAT+QUARTER
P=4*BLOCK
L=.09*np.pi/2+SM
HALF_WIDTH=.5
X0=.01
X1=1.67

@lru_cache(maxsize=12)
def side_height(order):
    p,d=smooth_curve(J(np.array([QUARTER])),QUARTER,R,SM,order)
    return FLAT/2+float(p.v[0])

def section(s,order=24):
    v=np.mod(s.v,P);b=np.floor(v/BLOCK).astype(int);x=v-b*BLOCK
    d=np.clip(x-FLAT,0.,QUARTER);alpha=softened_angle(d,QUARTER,SM,1/R)
    p,h=smooth_curve(J(d),QUARTER,R,SM,order)
    t=np.stack([np.cos(alpha),-np.sin(alpha)],axis=-1)
    n=np.stack([np.sin(alpha),np.cos(alpha)],axis=-1)
    pp=np.stack([-.5*FLAT+np.minimum(x,FLAT)+p.v,side_height(order)-h.v],axis=-1)
    si=np.array([0.,1.,0.,-1.])[b];co=np.array([1.,0.,-1.,0.])[b]
    def rot(vec):
        return (co*vec[...,0]+si*vec[...,1],-si*vec[...,0]+co*vec[...,1])
    pp,tt,nn=rot(pp),rot(t),rot(n)
    clock=np.clip(np.minimum(d,QUARTER-d)/SM,0.,1.)
    k=s5(clock)/R;kp=30*clock**2*(1-clock)**2*np.where(d<QUARTER/2,1.,-1.)/(SM*R)
    return ([unary(s,pp[i],tt[i],-k*nn[i]) for i in range(2)],
            [unary(s,nn[i],k*tt[i],kp*tt[i]-k*k*nn[i]) for i in range(2)])

def rate(x,t):
    y,dy,_=guard.clock(x)
    si=np.sin(2*np.pi*y);co=np.cos(2*np.pi*y)
    a=X0+(X1-X0)*np.sin(t)
    z=a*si*(1.5-.5*si*si);zp=a*(1.5-1.5*si*si)*co*2*np.pi*dy
    return np.arctan(z),zp/(1+z*z)

@lru_cache(maxsize=256)
def path_table(t,order):
    knots=np.array([0.,.06,.265,.5,.735,.94,1.]);n,w=rule(order)
    d=np.diff(knots);ang=rate(knots[:-1,None]+d[:,None]*n,t)[0]
    tab=np.vstack((np.zeros(2),np.cumsum(d[:,None]*np.c_[np.cos(ang)@w,np.sin(ang)@w],axis=0)))
    return knots,tab

def path(x,t,order):
    knots,tab=path_table(t,order);i=np.clip(np.searchsorted(knots,x.v,side="right")-1,0,len(knots)-2)
    h=x.v-knots[i];v,w=rule(order);ang=rate(knots[i,None]+h[:,None]*v,t)[0]
    q=tab[i]+h[:,None]*np.c_[np.cos(ang)@w,np.sin(ang)@w]
    z,k=rate(x.v,t);c=np.cos(z);s=np.sin(z)
    return unary(x,.5-tab[-1,0]+q[:,0],c,-k*s),unary(x,q[:,1],s,k*c)

@lru_cache(maxsize=12)
def end_limits(order):
    p,d=smooth_curve(J(np.array([L])),L,.09,SM,order)
    return float(p.v[0]),float(d.v[0])

def offset(s,d,order):
    c,n=section(s,order);return [p-d*z for p,z in zip(c,n)]

def profile_marks():
    return sorted(sum(([i*BLOCK+x for x in (0.,FLAT/2,FLAT,FLAT+SM,BLOCK-SM)] for i in range(4)),[]))

def axial_marks():return [-.5,-.44,-.235,0.,.235,.44,.5]

def chart_jet(chart,u,v,phase=0.,order=24,kind="coherent"):
    aa,bb=np.broadcast_arrays(np.asarray(u,float),np.asarray(v,float));sh=aa.shape
    s=J(aa.ravel(),s=1.);b=J(bb.ravel(),a=1.);sg=1 if chart.endswith("+") else -1
    if chart=="cylinder":
        c,n=section(s,order);ax,z=path(b+.5,float(phase),order)
        if kind=="coherent":out=(c[0],ax,c[1]+z)
        elif kind=="normal":out=(c[0]+z*n[0],ax,c[1]+z*n[1])
        else:raise ValueError(kind)
    else:
        pos=.5 if sg>0 else .5-path_table(float(phase),order)[1][-1,0]
        if chart.startswith("end"):
            pc,d=smooth_curve(b,L,.09,SM,order);p=offset(s,d,order);out=(p[0],pos+sg*pc,p[1])
        elif chart.startswith("cap"):
            pcap,db=end_limits(order)
            if "cartesian" in chart:p=[s,b]
            elif "normal" in chart:p=offset(s,db+b,order)
            else:p=[b*z for z in offset(s,db,order)]
            out=(p[0],J(np.full(len(s.v),pos+sg*pcap)),p[1])
        else:raise ValueError(chart)
    return gather(out,len(s.v)).reshape(sh+(6,3))

def disk_world(x,z,order=24):
    # The public Cartesian pole and disk coordinates are the actual section plane x,z.
    return [x,z]

def normal_to_disk_material(s,w,order=24):
    db=end_limits(order)[1];p=offset(s,db+w,order)
    # Convex positive radial support implies a strict angular derivative around the entire circle.
    q=angle(*p);base=angle(*offset(s,db,order));y=np.copy(s.v)
    for _ in range(10):
        lifted=angle(*offset(J(y,s=1.),db,order))
        dy=np.arctan2(np.sin(lifted.v-q.v),np.cos(lifted.v-q.v))/lifted.s;y-=dy
        if np.max(abs(dy))<6e-14:break
    lifted=angle(*offset(J(y,s=1.),db,order))
    label=unary(q,np.mod(y,P),1/lifted.s,-lifted.ss/lifted.s**3)
    rim=offset(label,db,order)
    return label,root(p[0]*p[0]+p[1]*p[1])/root(rim[0]*rim[0]+rim[1]*rim[1])
