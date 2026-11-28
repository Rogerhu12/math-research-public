"""R776 metric, true low-frequency spatial seeds and phase-independent full-jet trial columns."""
import numpy as np
import r778_normal_periodic_closed_corrugation as ref
import bent_coherent_shear_fields as rich
import bent_short_normal_arc as swing
from collections import OrderedDict
from bent_spatial_ring_fields import apply,stack
from r742_tilted_disk_two_jets import J,trig,cap_s7,unary

g,a=ref.g,ref.a

def profile_breaks(design=None):
    u=[g.BLOCK*i+g.FLAT+v for i in range(4) for v in (.5*g.SM,g.QUARTER-.5*g.SM)]
    normal=(1,2) if design is None else ((design["harmonics"],) if design["profile"]=="normal" else (1,) if design["profile"] in ("short","arc") else ())
    for i in range(4):
        for freq in normal:
            for j in range(freq):
                for v in (0,.0125,.025,.475,.4875,.5,.5125,.525,.975,.9875,1.):
                    u.append(i*g.BLOCK+g.FLAT+g.QUARTER*(j+v)/freq)
    if design is None or design["profile"]=="swing":
        u.extend(i*g.BLOCK+g.FLAT+g.QUARTER*z for i in range(4) for z in (.006,.05,.094,.1,.4,.406,.45,.494,.506,.55,.594,.6,.9,.906,.95,.994))
    return np.unique(np.r_[g.profile_marks(),u])

def grid(ns,nv,order,ind=False):
    data=rich.grid(ns,nv,order,ind)
    for i,(chart,s,v) in enumerate(data):
        if chart!="cylinder":continue
        su=np.unique(s);vx=np.unique(np.r_[v,a.axial_marks()])
        ss,xx=np.meshgrid(su,vx,indexing="ij")
        # Also resolve both sides of all sharp clock and pulse joins at every axial lobe.
        extra=profile_breaks()
        extra_x=np.unique(np.r_[a.axial_marks(),-.375,-.25,-.125,0.,.125,.25,.375,
                        (-.405 if ind else -.41),(.343 if ind else .34)])
        es,ex=np.meshgrid(extra,extra_x,indexing="ij")
        both=np.unique(np.c_[np.r_[ss.ravel(),es.ravel()],np.r_[xx.ravel(),ex.ravel()]],axis=0)
        data[i]=(chart,both[:,0],both[:,1])
    return data

def target(chart,u,v,order):
    return a.chart_jet(chart,u,v,0.,order)

def base(chart,u,v,t,order,d):
    short=a.chart_jet(chart,u,v,t,order)
    if not t or chart!="cylinder" or not d["fraction"]:return short
    if d["profile"]=="swing":other=swing.chart_jet(chart,u,v,t,order)
    elif d["profile"]=="arc":other=a.chart_jet(chart,u,v,t,order,"arclength")
    elif d["profile"]=="normal":other=ref.chart_jet(chart,u,v,t,order,d["harmonics"])
    else:raise ValueError(d)
    return short+d["fraction"]*(other-short)

def names(level):
    n=level+1
    return (rich.names(level)+[("local",i,j,k) for i in range(4) for j in range(1,n+2)
                               for k in range(2)]+[("shape",i,j,0) for i in range(3) for j in range(n+1)])

def floor(t,order):
    return .5-4*a.quarter_table(float(t),order)[1][-1,0]-g.end_limits(order)[0]-.008*np.sin(t)

def basis(chart,u,v,F,keys,d,order=20):
    orig=[p for p in keys if p[0] not in ("local","shape")]
    B=rich.basis(chart,u,v,F,orig)
    N=len(u);extra=keys[len(orig):]
    if chart.endswith("+") or (d["heads"]=="both" and chart!="cylinder"):
        return np.zeros((N,6,len(keys)))
    if chart!="cylinder":
        return np.concatenate((B,np.zeros((N,6,len(extra)))),axis=2)
    x=J(v+.5,a=1.);e=np.mod(u,g.P);block=np.floor(e/g.BLOCK).astype(int)
    local=(e-block*g.BLOCK-g.FLAT)/g.QUARTER
    # The extra angular corrections and both axial end gates have vanishing complete two-jets.
    s=unary(J(u,s=1.),np.clip(local,0.,1.),np.where((local>0)&(local<1),1/g.QUARTER,0.),0.)
    if d["heads"]=="both":
        gate=cap_s7(x/.11);jg=J(*(np.broadcast_to(z,(N,))[:,None] for z in gate.parts()))
        B=stack(J(*B.transpose(1,0,2))*jg,N,len(orig))
    p=rich.cheb(2*x-1,max(key[2] for key in extra)+2)
    sin_ax=trig(np.pi*x)[1]
    sin_ang=trig(np.pi*s)[1]
    bell=sin_ax*sin_ax*sin_ax
    aperture=sin_ang*sin_ang*sin_ang
    # Columns from the same actual differential field include its narrow curvature shoulders.
    # In the short-start branch use the smooth deterministic n=1 direction as a free correction.
    cand=dict(d)
    if not cand["fraction"]:cand.update(profile="normal",harmonics=1,fraction=.06)
    diff=base(chart,u,v,np.pi/2,order,cand)-a.chart_jet(chart,u,v,np.pi/2,order)
    D=[J(*diff[:,:,i].T) for i in range(3)]
    rows=[]
    for typ,i,j,k in extra:
        if typ=="local":
            co,si=trig(j*np.pi*s)
            z=((block==i)*aperture)*bell*(si if k else co)
        else:z=D[i]*p[j]
        rows.append(np.stack(np.broadcast_arrays(*z.parts(),u)[:6],axis=1))
    return np.concatenate((B,np.stack(rows,axis=2)),axis=2)

_terminal_cache=OrderedDict()
_terminal_bytes=0

def terminal_basis(chart,u,v,d,order,keys):
    global _terminal_bytes
    tag=(chart,u.shape,v.shape,u.tobytes(),v.tobytes(),d["heads"],d["profile"],d["fraction"],
         d["harmonics"],order,tuple(keys))
    if tag in _terminal_cache:
        _terminal_cache.move_to_end(tag)
        return _terminal_cache[tag]
    B=basis(chart,u,v,target(chart,u,v,order),keys,d,order)
    if B.nbytes<=280_000_000:
        while _terminal_cache and _terminal_bytes+B.nbytes>280_000_000:
            _,item=_terminal_cache.popitem(last=False)
            _terminal_bytes-=item.nbytes
        _terminal_cache[tag]=B;_terminal_bytes+=B.nbytes
    return B

def image(chart,u,v,t,d,order,keys,Z):
    f=base(chart,u,v,t,order,d)
    if not t or chart.endswith("+") or (d["heads"]=="both" and chart!="cylinder"):return f
    B=terminal_basis(chart,u,v,d,order,keys)
    return apply(f,B,Z,floor(t,order),False)[0]
