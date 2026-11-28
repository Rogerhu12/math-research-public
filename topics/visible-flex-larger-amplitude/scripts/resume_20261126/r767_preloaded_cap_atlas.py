"""Regular full disks, normal collars and their true two-jet material overlap for R767."""
from functools import lru_cache
import numpy as np
import r767_negative_track_profile as g
from r742_tilted_disk_two_jets import J,unary
OUTER_R=.092
OUTER_BLEND=.001
OUTER_L=OUTER_R*np.pi/2+OUTER_BLEND
LBRIDGE=.66
HALF_WIDTH=.13
PRELOAD=.02
SHORTEN=.18
SIDE_CUT=.01
RIGHT=1+g.HEAD_L/2
LEFT=2+1.5*g.HEAD_L

def root(x):
    q=np.sqrt(x.v)
    return unary(x,q,.5/q,-.25/q**3)

@lru_cache(maxsize=12)
def end_limits(order):
    p,d=g.smooth_curve(J(np.array([OUTER_L])),OUTER_L,OUTER_R,OUTER_BLEND,order)
    return float(p.v[0]),float(d.v[0])

def offset(s,d,order):
    q,n,T=g.section(s,0.,order)
    return [q[i]-d*n[i] for i in range(2)]

def projected(p,e):
    return e[0]*p[0]+e[1]*p[1]

@lru_cache(maxsize=12)
def data(order):
    db=end_limits(order)[1]
    q,T,N,k,kp=g.coordinates(np.array([LEFT,RIGHT]),0.,order)
    p=q-db*N;X=p@g.E;Z=p@g.N
    return float(X.mean()),float(np.diff(X)[0]/2),Z,db

def graph(x,side,order):
    C,R,_,db=data(order);X=C+R*x
    # Upper/lower graph inverses are monotone on these lifted intervals.
    lo=np.full(len(x),LEFT if side==1 else RIGHT)
    hi=np.full(len(x),RIGHT+g.P if side==1 else LEFT)
    s=(lo+hi)/2
    for _ in range(52):
        q,T,n,k,kp=g.coordinates(s,0.,order);p=q-db*n
        h=p@g.E-X;der=(1-db*k)*(T@g.E)
        close=np.abs(h)<3.e-14
        if np.all(close):break
        lo=np.where((side*h<0)&(~close),s,lo);hi=np.where((side*h>0)&(~close),s,hi)
        z=s-h/np.where(abs(der)>1.e-14,der,1.)
        s=np.where(close,s,np.where((z>lo)&(z<hi),z,.5*(lo+hi)))
    q,T,n,k,kp=g.coordinates(s,0.,order);p=q-db*n;c=T@g.E
    return p@g.N,R*(T@g.N)/c,-R*R*k/((1-db*k)*c**3)

def vertical(x,order):
    # Return mid-height and half-height/sqrt(1-x^2) with two x derivatives.
    C,R,Z,db=data(order);sh=np.shape(x.v);u,inv=np.unique(x.v,return_inverse=True)
    if np.any(abs(u)>1+2.e-9):raise ValueError("outside the normalized cap strip")
    mid=np.zeros((3,len(u)));fac=np.zeros_like(mid);q0=J(u,s=1.)
    near=abs(u)>.99
    for sign,idx in ((-1,0),(1,1)):
        mask=near&(u*sign>0)
        if not np.any(mask):continue
        w=J(u[mask],s=1.);rad=g.HEAD_R-db
        d=root(R*(2*rad-R*(1-sign*w))/(1+sign*w))
        mid[0,mask]=Z[idx];fac[:,mask]=np.broadcast_arrays(d.v,d.s,d.ss)
    use=~near
    if np.any(use):
        u0=u[use];a=graph(u0,1,order);b=graph(u0,-1,order);w=J(u0,s=1.)
        z1=unary(w,*a);z2=unary(w,*b);m=(z1+z2)*.5
        d=(z1-z2)*.5/root(1-w*w)
        mid[:,use]=np.broadcast_arrays(m.v,m.s,m.ss)
        fac[:,use]=np.broadcast_arrays(d.v,d.s,d.ss)
    def lift(a):return unary(x,*(v[inv].reshape(sh) for v in a))
    return lift(mid),lift(fac)

def disk_world(x,z,order=32):
    C,R,_,_=data(order);m,h=vertical(x,order);X=C+R*x;Z=m+h*z
    return [X*g.E[i]+Z*g.N[i] for i in range(2)]

def world_disk(p,order=32):
    C,R,_,_=data(order);x=(projected(p,g.E)-C)/R;m,h=vertical(x,order)
    return x,(projected(p,g.N)-m)/h

def boundary(s,order):
    return world_disk(offset(s,end_limits(order)[1],order),order)

def angle(x,z):
    # Clockwise positive angle; derivatives are local lifts through the branch.
    r=x*x+z*z
    p=(z.v*x.s-x.v*z.s)/r.v;q=(z.v*x.a-x.v*z.a)/r.v
    ss=(z.v*x.ss-x.v*z.ss-p*r.s)/r.v
    sa=(z.a*x.s+z.v*x.sa-x.a*z.s-x.v*z.sa-p*r.a)/r.v
    aa=(z.v*x.aa-x.v*z.aa-q*r.a)/r.v
    return J(np.mod(np.arctan2(-z.v,x.v),2*np.pi),p,q,ss,sa,aa)

@lru_cache(maxsize=12)
def grid(order):
    s=np.linspace(RIGHT,RIGHT+g.P,1025);x,z=boundary(J(s),order)
    a=np.unwrap(-np.arctan2(z.v,x.v));a-=a[0]
    return s,a

def normal_to_disk_material(s,w,order=32):
    """Input J's in any two variables; output J's (boundary label, disk radius)."""
    x,z=world_disk(offset(s,end_limits(order)[1]+w,order),order)
    r=root(x*x+z*z);q=angle(x,z);ss,aa=grid(order)
    y=np.interp(q.v,aa,ss)
    for _ in range(7):
        b=angle(*boundary(J(y,s=1.),order))
        dy=np.arctan2(np.sin(b.v-q.v),np.cos(b.v-q.v))/b.s;y-=dy
        if np.max(abs(dy))<1.e-13:break
    b=angle(*boundary(J(y,s=1.),order))
    return unary(q,np.mod(y,g.P),1/b.s,-b.ss/b.s**3),r

def cap_point(chart,a,b,order):
    if "cartesian" in chart:return [a,b]
    if "normal" in chart:return offset(a,end_limits(order)[1]+b,order)
    x,z=boundary(a,order)
    return disk_world(b*x,b*z,order)

def crown(p,order):
    q,T,n,k,kp=g.coordinates(np.array([RIGHT]),0.,order)
    c=q[0]-.127*n[0];w=1-((p[0]-c[0])*(p[0]-c[0])+(p[1]-c[1])*(p[1]-c[1]))/.012**2
    h=np.maximum(w.v,0.)
    return .00001*unary(w,h**4,4*h**3,12*h**2)
