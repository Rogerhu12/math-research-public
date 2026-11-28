"""Physical three-channel waist, end, shared-port and developed-cap trial fields for R791."""
from collections import OrderedDict
import numpy as np
from scipy.special import jv,jvp
import r791_prebent_lever_waist_two_jets as geom
import r783_four_developable_cap_flaps as flap
from r742_tilted_disk_two_jets import J,gather,trig,unary,cap_s7

def target(chart,u,v,order):return geom.chart_jet(chart,u,v,0.,order)

def encoded(chart,u,v,order):
    e=J(u,s=1.);w=J(v,a=1.);c,z=trig(e/geom.R)
    if chart=="cylinder":
        s=w+geom.SHIFT;r=geom.radius(s)
        return s,r*c,r*z,e/geom.R
    sg=1 if chart[-1]=="+" else -1;ring=geom.RIGHT if sg==1 else geom.LEFT
    if chart.startswith("end"):
        p,d=geom.smooth_curve(w,geom.L,geom.HEAD,geom.SM,order)
        return ring+sg*p,(geom.R-d)*c,(geom.R-d)*z,e/geom.R
    pb,db=geom.end_limits(order);s=J(np.full(len(u),ring+sg*pb))
    if "cartesian" in chart:return s,e,w,None
    if "normal" in chart:return s,(geom.R-db-w)*c,(geom.R-db-w)*z,e/geom.R
    return s,(geom.R-db)*w*c,(geom.R-db)*w*z,e/geom.R

def bessel(n,x):
    return unary(x,jv(n,x.v),jvp(n,x.v,1),jvp(n,x.v,2))

def spatial_section(angle,alpha,m,twist):
    c,z=trig(angle);j0=bessel(0,alpha)
    x=j0*c;y=J(np.zeros_like(angle.v));w=j0*z
    # All nonconstant angular primitives have zero mean.
    for n in range(1,13):
        j=bessel(n,alpha);k=n*m
        if n%2:
            a=(-1.)**((n-1)//2)*2/k
            y=y+a*j*trig(k*angle+n*twist)[1]
        else:
            a=(-1.)**(n//2)
            cp,sp=trig((1+k)*angle+n*twist)
            cm,sm=trig((1-k)*angle-n*twist)
            x=x+a*j*(cp/(1+k)+cm/(1-k))
            w=w+a*j*(sp/(1+k)+sm/(1-k))
    return x,y,w

def base(chart,u,v,t,order,d):
    if not t:return target(chart,u,v,order)
    u=np.asarray(u,float);v=np.asarray(v,float);s,xi,z,th=encoded(chart,u,v,order)
    if chart=="cylinder":
        c0,z0=trig(th);B=geom.BEND
        q0,q1,q2=geom.clock(s.v/B)
        swing=.55*np.sin(t)**2*unary(s,1-q0,-q1/B,-q2/B**2)
        slip_gate=cap_s7((s+.55)/.40)
        sm=s+d["slip"]*geom.WAIST*swing*c0*slip_gate
        if d["ring"]:
            envelope=cap_s7(s/.24)*cap_s7((B-s)/.24)
            alpha=d["ring"]*np.sin(t)**2*envelope
            twist=d["twist"]*(2*s/B-1.)
            xx,yy,zz=spatial_section(th,alpha,d["m"],twist)
            r=geom.radius(sm);coords=[r*xx,r*yy,r*zz]
        else:
            r=geom.radius(sm);coords=[r*c0,J(np.zeros_like(u)),r*z0]
        field=gather(geom.view(coords,sm,t,order),len(u))
    else:field=geom.chart_jet(chart,u,v,t,order)
    if not d["flap"]:return field
    x,y,z=[J(*field[:,:,i].T) for i in range(3)]
    # This material gate is one on the entire right cap and identically zero near the left witness.
    gate=cap_s7((s-geom.BEND)/.32)
    amp=d["flap"]*np.sin(t)**2
    dp,hp,_,_=flap.turn_jet(x,.045,amp,order)
    dm,hm,_,_=flap.turn_jet(-x,.045,amp,order)
    # Opposite wings lift in opposite axial directions, as for the world lever rotation.
    return gather([x+gate*(dp-dm),y+gate*(hp-hm),z],len(u))

def grid(ns,nv,order,ind=False):
    a,b=(.417,.283) if ind else (0.,0.)
    E=np.unique(np.r_[geom.profile_marks(),geom.P*(np.arange(ns)+a)/ns])
    s=np.unique(np.r_[geom.axial_marks(),-geom.HALF_WIDTH+2*geom.HALF_WIDTH*(np.arange(nv)+b)/nv,
            geom.HALF_WIDTH,geom.BEND*(np.arange(13)+(.29 if ind else 0.))/13-geom.SHIFT])
    end=np.unique(np.r_[0.,geom.SM/2,geom.SM,geom.L/2,geom.L-geom.SM,geom.L-geom.SM/2,geom.L,
                        geom.L*(np.arange(max(7,nv//2))+b)/max(7,nv//2)])
    pb,db=geom.end_limits(order);rb=geom.R-db
    r=np.unique(np.r_[.015,.035/rb,.045/rb,.125/rb,.28/rb,(np.arange(1,max(7,nv//2)+1)-b)/max(7,nv//2),1.])
    def mesh(t,w):
        ee,bb=np.meshgrid(t,w,indexing="ij");return ee.ravel(),bb.ravel()
    ans=[("cylinder",*mesh(E,s))]
    th=2*np.pi*(np.arange(24)+a)/24
    x=np.r_[0.,.025*np.cos(th),.165*np.cos(th),.285*np.cos(th),-.315,0.,0.]
    z=np.r_[0.,.025*np.sin(th),.165*np.sin(th),.285*np.sin(th),0.,.321,-.321]
    for sg in "+-":
        ans.extend([("end"+sg,*mesh(E,end)),("cap"+sg,*mesh(E,r)),
                    ("cap-normal"+sg,*mesh(E,[0.,.004,.015])),("cap-cartesian"+sg,x,z)])
    return ans

def names(level):
    n=level+2
    world=[("world",m,tr,i) for m in range(n+3) for tr in (range(1) if not m else range(2))
           for i in range(n+2) if i+m<=n+3]
    belt=[("waist",m,tr,j) for m in range(n+3) for tr in (range(1) if not m else range(2))
          for j in range(n+3) if j+m<=n+4]
    local=[("station",j,m,tr) for j in range(7) for m in range(n+1)
           for tr in (range(1) if not m else range(2))]
    rims=[("port",side,m,tr) for side in range(2) for m in range(n+2)
          for tr in (range(1) if not m else range(2))]
    caps=[("wing",i,k,tr) for i in range(4) for k in range(n) for tr in range(2)]
    return world+belt+local+rims+caps

def cheb(x,n):
    arr=[J(1.),x]
    while len(arr)<=n:arr.append(2*x*arr[-1]-arr[-2])
    return arr

def jetstack(f,u):return np.stack(np.broadcast_arrays(*f.parts(),u)[:6],axis=1)

def grip_gate(s,xi,d,order):
    pb,_=geom.end_limits(order);lo=geom.LEFT-pb;hi=geom.RIGHT+pb
    if d["grip"]=="two-caps":
        return cap_s7((s-lo)/.07)*cap_s7((hi-s)/.07)
    right=1-cap_s7((s-geom.RIGHT-.015)/.035)*(1-cap_s7((xi*xi-.035**2)/(.080**2-.035**2)))
    left_region=cap_s7((geom.LEFT-.025-s)/.035)
    if d["grip"]=="left-cap":return right*(1-left_region)
    exact_witness=1-cap_s7((xi+.315)/.035)
    return right*(1-left_region*exact_witness)

def basis(chart,u,v,F,keys,d,order=20):
    s,x,z,th=encoded(chart,u,v,order);gt=grip_gate(s,x,d,order)
    degree=max(12,max(max(k[1:]) for k in keys)+2);ky=cheb((s-geom.SHIFT)/1.56,degree)
    rx,rz=x/geom.R,z/geom.R;re=[J(1.)];im=[J(0.)]
    for n in range(degree):
        re.append(re[-1]*rx-im[-1]*rz);im.append(re[-2]*rz+im[-1]*rx)
    gate=cap_s7((s+.55)/.25)*cap_s7((geom.BEND+.55-s)/.25)
    if chart=="cylinder":
        cc=[trig(m*th) for m in range(degree+1)]
        poly=cheb((2*s/geom.BEND-1)/1.65,degree)
    loc=[]
    for j in range(7):
        a=1-((s-(geom.BEND*j/6))/.37)*((s-(geom.BEND*j/6))/.37)
        a=unary(a,np.maximum(a.v,0.),(a.v>0.).astype(float),np.zeros_like(a.v));sq=a*a
        loc.append(sq*sq)
    ports=[]
    for station in (0.,geom.BEND):
        a=s-station;v0=np.exp(-14*a.v*a.v)
        ports.append(unary(a,v0,-28*a.v*v0,(784*a.v*a.v-28)*v0))
    wings=[cap_s7((sign*var-.045)/.11) for var in (x,z) for sign in (1,-1)]
    rows=[]
    for tag,i,j,k in keys:
        if tag=="world":col=(im[i] if j else re[i])*ky[k]
        elif tag=="port":col=ports[i]*(im[j] if k else re[j])
        elif tag=="wing":col=wings[i]*ky[j]*(rx if k else rz)
        elif chart!="cylinder":col=J(0.)
        elif tag=="waist":col=gate*cc[i][j]*poly[k]
        else:col=gate*loc[i]*cc[j][k]
        rows.append(jetstack(col*gt,u))
    return np.stack(rows,axis=2)

def apply(f0,B,coef,floor,linear):
    # The moving left witness and fixed right grip are exact material masks.
    # No coordinate is clipped and no world-axis exponential floor is needed.
    F=f0+np.einsum("nrk,kd->nrd",B,coef)
    D=np.broadcast_to(B[:,:,:,None],B.shape+(3,)) if linear else None
    return F,D

def floor(t,order):return 0.

_cache=OrderedDict();_bytes=0

def image(chart,u,v,t,d,order,keys,coef):
    global _bytes
    f=base(chart,u,v,t,order,d)
    if not t:return f
    tag=(chart,u.shape,v.shape,u.tobytes(),v.tobytes(),d["grip"],tuple(keys))
    if tag in _cache:B=_cache[tag];_cache.move_to_end(tag)
    else:
        B=basis(chart,u,v,target(chart,u,v,20),keys,d,20)
        if B.nbytes<280000000:
            while _cache and _bytes+B.nbytes>280000000:
                _,x=_cache.popitem(last=False);_bytes-=x.nbytes
            _cache[tag]=B;_bytes+=B.nbytes
    return apply(f,B,coef,0.,False)[0]
