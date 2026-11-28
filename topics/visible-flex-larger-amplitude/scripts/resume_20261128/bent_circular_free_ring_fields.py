"""R781 material dictionaries on the actual circle, both rounded caps and two Cartesian disk charts."""
from collections import OrderedDict
import numpy as np
import r781_round_three_lobe_spatial_rings as ref
from r742_tilted_disk_two_jets import J,trig,unary,cap_s7
from bent_spatial_ring_fields import apply
import bent_circular_cap_field as cap
from bent_coherent_shear_fields import cheb

def names(level):
    n=level+1
    world=[("world",m,tr,j) for m in range(n+3) for tr in (range(1) if not m else range(2))
            for j in range(n+2) if m+j<=n+3]
    tube=[("tube",m,tr,j) for m in range(n+4) for tr in (range(1) if not m else range(2))
            for j in range(n+3) if m+j<=n+4]
    # One low-frequency set for every individual positive and negative axial wave.
    lobes=[("lobe",i,m,tr) for i in range(6) for m in range(n+2)
           for tr in (range(1) if not m else range(2))]
    lips=[("rim",side,j,p) for side in range(2) for j in range(n+2) for p in range(3)]
    physical=[("field",i,j,0) for i in range(3) for j in range(n+1)]
    sectors=[("sector",i,j,k) for i in range(4) for j in range(n+1) for k in range(2)]
    return world+tube+lobes+lips+physical+sectors

def target(chart,u,v,order):
    return ref.chart_jet(chart,u,v,0.,order)

def base(chart,u,v,t,order,d):
    F=ref.chart_jet(chart,u,v,t,order,mode=d["profile"],m=d["m"],xi=d["xi"],mix=d["mix"])
    return cap.transform(F,t,d["cap_angle"],order)

def floor(t,order):
    return .5-6*ref.half_table(float(t),order)[1][-1,0]-ref.end_limits(order)[0]-.008*np.sin(t)

def grid(ns,nv,order,ind=False):
    a,b=(.417,.283) if ind else (0.,0.)
    angle=np.unique(np.r_[ref.profile_marks(),ref.P*(np.arange(ns)+a)/ns,
                     ref.P*np.arange(24)/24])
    wave=np.unique(np.r_[ref.axial_marks(),(np.arange(nv)+b)/nv-.5,.5,
              (np.arange(12)+(.317 if ind else .5))/12-.5])
    e=np.unique(np.r_[0.,ref.SM/2,ref.SM,ref.L/2,ref.L-ref.SM,ref.L-ref.SM/2,ref.L,
              ref.L*(np.arange(max(6,nv//2))+b)/max(6,nv//2)])
    r=np.unique(np.r_[.02,.18/(ref.R-ref.end_limits(order)[1]),
              .255/(ref.R-ref.end_limits(order)[1]),(np.arange(1,max(6,nv//2)+1)-b)/max(6,nv//2),1.])
    def mesh(u,v):
        s,x=np.meshgrid(u,v,indexing="ij");return s.ravel(),x.ravel()
    ans=[("cylinder",*mesh(angle,wave))]
    th=2*np.pi*(np.arange(24)+a)/24
    x=np.r_[0.,.025*np.cos(th),.15*np.cos(th),.20*np.cos(th),.28*np.cos(th)]
    z=np.r_[0.,.025*np.sin(th),.15*np.sin(th),.20*np.sin(th),.28*np.sin(th)]
    for sg in "+-":
        ans.extend([("end"+sg,*mesh(angle,e)),("cap"+sg,*mesh(angle,r)),
          ("cap-normal"+sg,*mesh(angle,[0.,.003,.01])),("cap-cartesian"+sg,x,z)])
    return ans

def cardinal(z):
    t=abs(z.v);sg=np.sign(z.v)
    a=t<1;b=(t>=1)&(t<2)
    val=np.where(a,(4-6*t*t+3*t**3)/6,np.where(b,(2-t)**3/6,0.))
    der=sg*np.where(a,(-12*t+9*t*t)/6,np.where(b,-.5*(2-t)**2,0.))
    d2=np.where(a,-2+3*t,np.where(b,2-t,0.))
    return unary(z,val,der,d2)

def jetstack(j,u):
    return np.stack(np.broadcast_arrays(*j.parts(),u)[:6],axis=1)

def basis(chart,u,v,F,keys,d,order=20):
    N=len(u);K=len(keys)
    X,Y,Z=[J(*F[:,:,i].T) for i in range(3)]
    if d["grip"]=="heads" and chart!="cylinder":return np.zeros((N,6,K))
    if d["grip"]=="left-and-pad" and chart.endswith("-"):return np.zeros((N,6,K))
    ini=.5-6*ref.half_table(0.,order)[1][-1,0]
    rad2=X*X+Z*Z
    # This is a C^2 material mask on the exact target, including the full central disk r<=.18.
    if d["grip"]=="heads":gate=J(1.)
    else:
        pad=1-cap_s7((rad2-.18**2)/(.255**2-.18**2))
        cap_layer=cap_s7((Y-.538)/.035)
        gate=1-pad*cap_layer
        if d["grip"]=="left-and-pad":gate=gate*cap_s7((Y-ini)/.075)
    degree=max(8,max(max(k[1:]) for k in keys)+2)
    py=cheb((Y+.02)*1.7,degree)
    xx,zz=X/ref.R,Z/ref.R
    real=[J(1.)];imag=[J(0.)]
    for m in range(degree):
        real.append(real[-1]*xx-imag[-1]*zz)
        imag.append(real[-2]*zz+imag[-1]*xx)
    sectors=[cap_s7((np.cos(i*np.pi/2)*X+np.sin(i*np.pi/2)*Z-.18)/.14) for i in range(4)]
    rom=[]
    for yy in (ini,.5):
        delta=Y-yy;v0=np.exp(-38*delta.v**2)
        gb=unary(delta,v0,-76*delta.v*v0,(76**2*delta.v**2-76)*v0)
        rom.append([gb,gb*delta,gb*delta*delta])
    if chart=="cylinder":
        x=J(v+.5,a=1.);th=J(u,s=1.)/ref.R
        window=cap_s7(x/.068)*cap_s7((1-x)/.068)
        if d["grip"]=="heads":gate=window
        cs=[trig(m*th) for m in range(degree+1)]
        px=cheb(2*x-1,degree)
        lobes=[cardinal(8*(x-(i+.5)/6))*window for i in range(6)]
        selected=dict(d)
        if d["profile"]!="ring" or not d["mix"]:
            selected.update(profile="ring",m=2,xi=.03,mix=.18)
        # Domain-specific seed difference vanishes through both cylinder/roll rims.
        selected["cap_angle"]=0.
        v1=base(chart,u,v,np.pi/2,order,selected)
        v0=ref.chart_jet(chart,u,v,np.pi/2,order,mode="balanced",xi=selected["xi"])
        geom=[J(*(v1-v0)[:,:,i].T) for i in range(3)]
    rows=[]
    for tag,i,j,k in keys:
        if tag=="world":col=(imag[i] if j else real[i])*py[k]
        elif tag=="rim":col=rom[i][k]*(imag[j] if k==2 else real[j])
        elif tag=="sector":col=sectors[i]*py[j]*(zz if k else xx)
        elif chart!="cylinder":col=J(0.)
        elif tag=="tube":col=window*cs[i][j]*px[k]
        elif tag=="lobe":col=lobes[i]*cs[j][k]
        else:col=geom[i]*px[j]
        rows.append(jetstack(gate*col,u))
    return np.stack(rows,axis=2)

_cache=OrderedDict()
_bytes=0

def cached_basis(chart,u,v,d,order,keys):
    global _bytes
    tag=(chart,u.shape,v.shape,u.tobytes(),v.tobytes(),d["grip"],d["profile"],d["m"],d["xi"],d["mix"],d["cap_angle"],order,tuple(keys))
    if tag in _cache:
        _cache.move_to_end(tag);return _cache[tag]
    B=basis(chart,u,v,target(chart,u,v,order),keys,d,order)
    if B.nbytes<280_000_000:
        while _cache and _bytes+B.nbytes>280_000_000:
            _,q=_cache.popitem(last=False);_bytes-=q.nbytes
        _cache[tag]=B;_bytes+=B.nbytes
    return B

def image(chart,u,v,t,d,order,keys,Z):
    f=base(chart,u,v,t,order,d)
    if not t or (d["grip"]=="heads" and chart!="cylinder") or (d["grip"]=="left-and-pad" and chart.endswith("-")):
        return f
    return apply(f,cached_basis(chart,u,v,d,order,keys),Z,floor(t,order),False)[0]
