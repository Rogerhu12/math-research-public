"""Three physical families on the R786 closed shell, with movable roll boundaries and R784 cap germs."""
from collections import OrderedDict
import numpy as np
import bent_circular_free_ring_fields as previous
import r781_round_three_lobe_spatial_rings as target_geometry
import r786_delayed_two_cap_roll_collars as geometry
import r784_first_nonlinear_cap_continuation as cauchy
from r742_tilted_disk_two_jets import J, cap_s7, trig, unary
from bent_coherent_shear_fields import cheb

apply=previous.apply
floor=previous.floor
target=previous.target
jetstack=previous.jetstack

def names(level):
    prior=previous.names(level)
    summits=[("summit",l,m,tr) for l in range(3) for m in range(1,level+4) for tr in range(2)]
    rolls=[("roll",side,m,tr) for side in range(2) for m in range(level+4)
           for tr in (range(1) if not m else range(2))]
    return prior+summits+rolls

def base(chart,u,v,t,order,d):
    field=geometry.chart_jet(chart,u,v,t,order,mode=d["profile"],m=d["m"],xi=d["xi"],mix=d["mix"])
    return cauchy.add_ninth_jet(field,chart,u,v,t,order)

def grid(ns,nv,order,independent=False):
    old=previous.grid(ns,nv,order,independent)
    # Existing whole grids and all clock/cap transition stations are retained.
    angles=geometry.angular_breaks(order)
    core=[.46,.48,.57,.67,.69]
    extra=np.unique(np.r_[angles,[geometry.R*((axis+s*x)%(2*np.pi)) for axis in np.arange(4)*np.pi/2
                                   for s in (-1.,1.) for x in core]])
    refined=[]
    for name,u,v in old:
        if name.startswith("end"):
            aa=np.unique(np.r_[u,extra])
            b=np.unique(np.r_[v,geometry.terminal_stations(np.pi/2),geometry.L-.001,
                       geometry.L-cauchy.HALF_BAND,geometry.L-1.5*cauchy.HALF_BAND])
            uu,vv=np.meshgrid(aa,b,indexing="ij")
            refined.append((name,uu.ravel(),vv.ravel()))
        else:refined.append((name,u,v))
    return refined

def anchor_gate(chart,u,v,F,d):
    if d["grip"]=="caps":
        if chart.startswith("cap"):return J(0.)
        if chart.startswith("end"):
            return cap_s7((geometry.L-J(v,a=1.)-geometry.THICKNESS)/.020)
        return J(1.)
    if d["grip"]=="paired-pads":
        X,Y,Z=[J(*F[:,:,i].T) for i in range(3)]
        y0=.5-6*target_geometry.half_table(0.,20)[1][-1,0]
        disk=1-cap_s7((X*X+Z*Z-.18**2)/(.255**2-.18**2))
        lower=cap_s7((y0-.038-Y)/.035)
        return 1-disk*lower
    return J(1.)

def basis(chart,u,v,F,keys,d,order=20):
    if d["grip"]=="caps" and chart.startswith("cap"):
        return np.zeros((len(u),6,len(keys)))
    parent_keys=[key for key in keys if key[0] not in ("summit","roll")]
    inherited=dict(d,grip="pad",cap_angle=0.)
    old=previous.basis(chart,u,v,F,parent_keys,inherited,order)
    if chart=="cylinder":
        x=J(v+.5,a=1.);th=J(u,s=1.)/geometry.R
    elif chart.startswith("end"):
        depth=geometry.L-J(v,a=1.);th=J(u,s=1.)/geometry.R
        b=J(v,a=1.)/geometry.L
        roll_window=cap_s7(b/.14)*cap_s7(depth/.014)
    extra=[]
    for tag,i,m,tr in keys[len(parent_keys):]:
        if tag=="summit" and chart=="cylinder":
            q=(x-(2*i+1)/6)/.146
            raw=1-q*q
            positive=unary(raw,np.maximum(raw.v,0.),(raw.v>0.).astype(float),np.zeros_like(raw.v))
            col=(positive**4)*trig(m*th)[tr]
        elif tag=="roll" and chart.startswith("end") and (chart[-1]=="+")==bool(i):
            col=roll_window*trig(m*th)[tr]
        else:col=J(0.)
        extra.append(jetstack(col,u))
    allrows=np.concatenate((old,np.stack(extra,axis=2)),axis=2)
    # Apply the one material mask to all derivative slots by the true product rule.
    z=jetstack(anchor_gate(chart,u,v,F,d),u)
    B=allrows
    return np.stack((z[:,0,None]*B[:,0],z[:,1,None]*B[:,0]+z[:,0,None]*B[:,1],
        z[:,2,None]*B[:,0]+z[:,0,None]*B[:,2],
        z[:,3,None]*B[:,0]+2*z[:,1,None]*B[:,1]+z[:,0,None]*B[:,3],
        z[:,4,None]*B[:,0]+z[:,1,None]*B[:,2]+z[:,2,None]*B[:,1]+z[:,0,None]*B[:,4],
        z[:,5,None]*B[:,0]+2*z[:,2,None]*B[:,2]+z[:,0,None]*B[:,5]),axis=1)

_cache=OrderedDict()
_cache_bytes=0

def cached_basis(chart,u,v,d,order,keys):
    global _cache_bytes
    tag=(chart,u.shape,v.shape,u.tobytes(),v.tobytes(),d["grip"],d["profile"],d["m"],
         d["xi"],d["mix"],order,tuple(keys))
    if tag in _cache:
        _cache.move_to_end(tag);return _cache[tag]
    B=basis(chart,u,v,target(chart,u,v,20),keys,d,20)
    if B.nbytes<280000000:
        while _cache and _cache_bytes+B.nbytes>280000000:
            _,item=_cache.popitem(last=False);_cache_bytes-=item.nbytes
        _cache[tag]=B;_cache_bytes+=B.nbytes
    return B

def image(chart,u,v,t,d,order,keys,Z):
    field=base(chart,u,v,t,order,d)
    if not t or (d["grip"]=="caps" and chart.startswith("cap")):return field
    return apply(field,cached_basis(chart,u,v,d,order,keys),Z,floor(t,order),False)[0]
