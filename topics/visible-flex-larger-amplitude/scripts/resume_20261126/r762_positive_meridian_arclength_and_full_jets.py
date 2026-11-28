#!/usr/bin/env python3
"""R762 positive transverse arclength gauges on the actual R760 cap, identity on both open collars."""
from functools import lru_cache
from math import factorial
import numpy as np
from scipy.interpolate import BSpline
from numpy.polynomial import Polynomial
import r760_cartesian_curved_crown_and_lower_rate_walls as geom
import solve_r760_curved_crown_middle_annuli as old


LEFT=1-old.WC
RIGHT=1-geom.WIDTH
SPAN=RIGHT-LEFT
GUARDS=(.04,.16,.84,.96)


def taylor_cutoff(cells):
    table=np.zeros((len(cells)-1,6))
    for i,(lo,hi) in enumerate(zip(cells[:-1],cells[1:])):
        mid=(lo+hi)/2;dz=hi-lo
        if mid<=GUARDS[0] or mid>=GUARDS[3]:
            continue
        if GUARDS[1]<=mid<=GUARDS[2]:
            table[i,0]=1.;continue
        if mid<GUARDS[1]:
            v=Polynomial([(lo-GUARDS[0])/(GUARDS[1]-GUARDS[0]),dz/(GUARDS[1]-GUARDS[0])])
        else:
            v=Polynomial([(GUARDS[3]-lo)/(GUARDS[3]-GUARDS[2]),-dz/(GUARDS[3]-GUARDS[2])])
        p=10*v**3-15*v**4+6*v**5
        table[i,:len(p.coef)]=p.coef
    return table


def greville(t):
    return (t[1:-3]+t[2:-2]+t[3:-1])/3


@lru_cache(maxsize=12)
def domain(order):
    ns,nr={16:(48,24),24:(96,40),32:(192,64)}[order]
    cut,extent,half=geom.material(order,True);P=2*half
    elbows=np.asarray(geom.clock_spec(True)[1])
    upper=np.r_[cut+elbows,cut-.30,cut-.20,cut-.10,geom.m.LEFT_LENGTH/2,half]
    # One common C2 speed proxy knot set is used at every phase in a level.
    sb=np.unique(np.r_[np.arange(ns)*P/ns,upper,P-upper,0.,P])
    sb=sb[(sb>=0)&(sb<=P)]
    near=1-np.array([geom.WIDTH,geom.WIDTH+geom.ROUND])
    cap=(1-geom.JOIN)*np.array([.82,.84,.86,.87,.92,.97,.98])
    special=(np.r_[near,cap]-LEFT)/SPAN
    vb=np.unique(np.r_[np.linspace(0,1,nr+1),special[(special>0)&(special<1)],GUARDS])
    # Coincident analytic anchors can differ by an ulp; drop only true
    # machine-neighbour duplicates before forming normalized polynomial cells.
    sb=sb[np.r_[True,np.diff(sb)>4e-14]];sb[-1]=P
    vb=vb[np.r_[True,np.diff(vb)>4e-14]];vb[-1]=1.
    st=np.r_[sb[-4:-1]-P,sb,sb[1:4]+P]
    vt=np.r_[np.zeros(3),vb,np.ones(3)]
    S=BSpline(st,np.eye(len(st)-4),3);V=BSpline(vt,np.eye(len(vt)-4),3)
    step=np.diff(vb)
    vc=np.stack([V(vb[:-1],nu=j)*(step**j/factorial(j))[:,None] for j in range(4)],axis=-1)
    return P,st,vt,S,vc,vb,step,taylor_cutoff(vb)


@lru_cache(maxsize=64)
def weights(order,side,phase):
    P,st,vt,*_=domain(order)
    su,vu=np.meshgrid(np.mod(greville(st),P),greville(vt),indexing="ij")
    name="cap"+("+" if side>0 else "-")
    angles=su.ravel();radius=LEFT+SPAN*vu.ravel()
    sample=np.empty(len(angles))
    for left in range(0,len(sample),512):
        sl=slice(left,left+512)
        jets=old.posed(name,angles[sl],radius[sl],phase,order,side)
        sample[sl]=SPAN*np.linalg.norm(jets[:,2],axis=1)
    speed=sample.reshape(su.shape)
    if np.any(~np.isfinite(speed)) or np.min(speed)<=0:
        raise ValueError("the physical reference speed is singular at a real cap Greville label")
    speed[-3:]=speed[:3]
    return speed


def coefficients(ss,phase,side,order):
    P,st,vt,S,vc,cells,width,cutoff=domain(order)
    Sd=np.stack([S(np.mod(ss,P),nu=d) for d in range(3)])
    def speed(ph):
        w=weights(order,side,ph)
        angular=Sd@w
        return np.einsum("dsn,cnj->dscj",angular,vc,optimize=True)
    A=speed(phase);A0=speed(0.)
    def multiply(poly):
        out=np.zeros(poly.shape[:-1]+(9,))
        for j in range(6):
            out[...,j:j+4]+=cutoff[None,None,:,j,None]*poly
        return out
    def integral(poly):
        return np.sum(np.sum(poly/np.arange(1,poly.shape[-1]+1),axis=-1)*width,axis=-1)
    I=integral(multiply(A));I0=integral(multiply(A0))
    scale=I[0]/I0[0]
    ds=(I[1]-scale*I0[1])/I0[0]
    dd=(I[2]-scale*I0[2]-2*ds*I0[1])/I0[0]
    ca=scale[None,:,None,None]*A0
    ca[1]+=ds[:,None,None]*A0[0]
    ca[2]+=dd[:,None,None]*A0[0]+2*ds[:,None,None]*A0[1]
    G=multiply(ca-A);G[...,:4]+=A
    def begins(poly):
        increments=np.sum(poly/np.arange(1,poly.shape[-1]+1),axis=-1)*width
        return np.concatenate((np.zeros(increments.shape[:-1]+(1,)),np.cumsum(increments,axis=-1)),axis=-1)
    return A,G,begins(A),begins(G),scale


def at(poly,prior,cells,ix,z,cell=None):
    k=np.clip(np.searchsorted(cells,z,side="right")-1,0,len(cells)-2) if cell is None else cell
    h=cells[k+1]-cells[k];t=(z-cells[k])/h
    Q=poly[:,ix,k,:];d=poly.shape[-1]
    powers=t[:,None]**np.arange(d)
    val=np.einsum("dnk,nk->dn",Q,powers)
    integral=prior[:,ix,k]+h*t*np.einsum("dnk,nk->dn",Q,powers/np.arange(1,d+1))
    deriv=np.einsum("nk,nk->n",Q[0,:,1:]*np.arange(1,d),powers[:,:-1])/h
    return val,integral,deriv


def map_jet(s,v,ph,order,side):
    s,v=np.broadcast_arrays(np.asarray(s,float),np.asarray(v,float))
    shape=v.shape;s=s.ravel();v=v.ravel();z=(v-LEFT)/SPAN
    live=(z>GUARDS[0])&(z<GUARDS[3])&(ph!=0.)
    ans=np.zeros((len(v),6));ans[:,0]=v;ans[:,2]=1.
    if not np.any(live):
        return ans.reshape(shape+(6,))
    ss,ix=np.unique(s[live],return_inverse=True);z=z[live]
    A,G,AI,GI,_=coefficients(ss,ph,side,order);cells=domain(order)[5]
    gv,gi,gz=at(G,GI,cells,ix,z)
    # Every A is strictly increasing. Locate its cell first; outside the
    # two real open guards both primitives have identical total length.
    cell=np.empty(len(z),dtype=int)
    for i in range(len(ss)):
        match=ix==i;cell[match]=np.clip(np.searchsorted(AI[0,i],gi[0,match],side="right")-1,0,len(cells)-2)
    low=cells[cell].copy();high=cells[cell+1].copy()
    sl=AI[0,ix,cell];sr=AI[0,ix,cell+1]
    x=low+(high-low)*np.clip((gi[0]-sl)/(sr-sl),0.,1.)
    for _ in range(52):
        av,ai,az=at(A,AI,cells,ix,x,cell)
        diff=ai[0]-gi[0]
        if np.all(np.abs(diff)<=2e-14*np.maximum(AI[0,ix,-1],1e-10)):
            break
        low=np.where(diff<0,x,low);high=np.where(diff>0,x,high)
        xn=x-diff/av[0]
        xn=np.where((xn>=low)&(xn<=high),xn,(low+high)/2)
        x=np.where(diff==0,x,xn)
    av,ai,az=at(A,AI,cells,ix,x,cell)
    xs=(gi[1]-ai[1])/av[0];xv=gv[0]/av[0]
    xss=(gi[2]-ai[2]-2*av[1]*xs-az*xs*xs)/av[0]
    xsv=(gv[1]-av[1]*xv-az*xs*xv)/av[0]
    xvv=(gz-az*xv*xv)/av[0]
    ans[live]=np.stack((LEFT+SPAN*x,SPAN*xs,xv,SPAN*xss,xsv,xvv/SPAN),axis=1)
    return ans.reshape(shape+(6,))


def posed(name,u,v,ph,order,side):
    if name not in ("cap+","cap-") or ph==0.:
        return old.posed(name,u,v,ph,order,side)
    u,v=np.broadcast_arrays(np.asarray(u,float),np.asarray(v,float));shape=u.shape
    u,v=u.ravel(),v.ravel()
    m=map_jet(u,v,ph,order,side);vp,ms,mv,mss,msv,mvv=(x[:,None] for x in m.T)
    j=old.posed(name,u,vp[:,0],ph,order,side)
    f,fs,fv,fss,fsv,fvv=np.moveaxis(j,1,0)
    g=np.stack((f,fs+ms*fv,mv*fv,fss+2*ms*fsv+ms**2*fvv+mss*fv,
         mv*fsv+ms*mv*fvv+msv*fv,mv**2*fvv+mvv*fv),axis=1)
    return g.reshape(shape+(6,3))
