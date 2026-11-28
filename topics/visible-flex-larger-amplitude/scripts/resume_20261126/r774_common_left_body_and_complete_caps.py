#!/usr/bin/env python3
"""Whole R774 center, two end-cap poses, and every complete signed meridian on the R764 metric."""
from functools import lru_cache
import numpy as np
import r769_closed_turn_redistribution_and_complete_rolls as oldgeom
import r771_convex_complete_meridian_coordinates as convex
from r742_tilted_disk_two_jets import J,unary,cap_s7,gather

base,old,m=oldgeom.base,oldgeom.old,oldgeom.m
E,L,B,T=oldgeom.E,oldgeom.L,oldgeom.B,convex.T
BRANCHES={"left":(0.,0.),"common":(.12,.42)}
A=np.pi/2

def main_angles(a,ph,order,gamma):
    arr=np.asarray(a,float);sh=arr.shape;s=arr.ravel()
    _,t,_,k,kp=old.data(s,0.,order,True)
    beta=np.arctan2(t[:,1],t[:,0]);k0=k.copy()
    lh,m0,m1,rtop,_,_,_,_,st,*_=m.constants(order)
    off=m.LEFT_LENGTH/2+st-lh;neg=(s>off+m0+1.30)&(s<off+m0+1.56)
    h,w,dw,_=oldgeom.clock_data(beta[neg],.617,A-.005,.012)
    beta[neg]-=ph*h
    k[neg]=k0[neg]*(1-ph*w);kp[neg]=kp[neg]*(1-ph*w)+ph*dw*k0[neg]**2
    b=(s>=off+m0+1.56)&(s<=off+m1);beta[b]-=ph
    u=(s>off+m1)&(s<off+rtop)
    x=A-beta[u];h,w,dw,_=oldgeom.clock_data(x,.98,2.00,.02)
    beta[u]-=ph*(1-h)
    k[u]=k0[u]*(1-ph*w);kp[u]=kp[u]*(1-ph*w)-ph*dw*k0[u]**2
    cut,_,_=old.material(order,True);wall=s>=cut
    az,ap,app=old.heading(s[wall]-cut,True)
    beta[wall]=-A+gamma*az;k[wall]=-gamma*ap;kp[wall]=-gamma*app
    return np.column_stack((np.cos(beta),np.sin(beta),k,kp)).reshape(sh+(4,))

@lru_cache(maxsize=12)
def stations(order):
    grid=oldgeom.parent.cuts(order,0.)
    lh,m0,m1,_,_,_,_,_,st,*_=m.constants(order)
    off=m.LEFT_LENGTH/2+st-lh;more=[]
    for goal in (.617,.629,A-.017,A-.005):
        low,high=.30,.56
        for _ in range(54):
            mid=(low+high)/2
            if m.old.disk.beta(np.asarray(mid))<goal:low=mid
            else:high=mid
        more.append(off+m0+1+(low+high)/2)
    grid=np.unique(np.r_[grid,more,off+m1+.0005+.15*np.array([.98,1.,1.98,2.])])
    return grid[np.r_[True,np.diff(grid)>1e-13]]

@lru_cache(maxsize=128)
def state(order,ph):
    grid=stations(order);x,w=m.old.disk.rule(order);ds=np.diff(grid);u=grid[:-1,None]+ds[:,None]*x
    gamma0=old.amplitude(0.,order,True);cut=old.material(order,True)[0]
    nonwall=grid[1:]<=cut+1e-13
    orig=main_angles(u,0.,order,gamma0);moved=main_angles(u,ph,order,gamma0)
    change=float(np.sum(ds[nonwall]*((moved[nonwall,:,1]-orig[nonwall,:,1])@w)))
    wanted=old.PRE_CUT+change
    def height(g):
        return float(old.integral(np.asarray(old.PRE_HALF),g,order,True)[0])
    lo,hi=gamma0,1.397
    if ph and (height(lo)<wanted-1e-12 or height(hi)>wanted+1e-12):
        raise ValueError("true right wall outside its proven closure bracket")
    if ph:
        for _ in range(55):
            mid=(lo+hi)/2
            if height(mid)>wanted:lo=mid
            else:hi=mid
        gamma=(lo+hi)/2
    else:gamma=gamma0
    z=main_angles(u,ph,order,gamma);d=ds[:,None]*np.einsum("ink,n->ik",z[:,:,:2],w)
    start=old.data(np.array([0.]),0.,order,True)[0][0]
    Q=start+np.vstack((np.zeros(2),np.cumsum(d,axis=0)))
    anchor=m.grip_s(.55,order);j=np.argmin(abs(grid-anchor))
    sh=old.data(np.asarray([anchor]),ph,order,True)[0][0]-Q[j]
    return grid,Q,gamma,sh,[gamma0,gamma,change,wanted,height(gamma),float(Q[-1,1])]

def curve(s,ph,order):
    sh=np.shape(s);ss,ix=np.unique(np.asarray(s,float).ravel(),return_inverse=True)
    if not ph:
        return tuple(z[ix].reshape(sh+z.shape[1:]) for z in old.data(ss,0.,order,True))
    grid,Q,g,tr,_=state(order,ph);half=old.material(order,True)[-1]
    a=ss%(2*half);low=a>half;a=np.where(low,2*half-a,a)
    j=np.clip(np.searchsorted(grid,a,side="right")-1,0,len(grid)-2)
    ds=a-grid[j];x,w=m.old.disk.rule(order);inc=[]
    for lo in range(0,len(a),256):
        sl=slice(lo,lo+256);t=main_angles(grid[j[sl],None]+ds[sl,None]*x,ph,order,g)
        inc.append(np.einsum("ink,n->ik",t[:,:,:2],w))
    q=Q[j]+ds[:,None]*np.concatenate(inc);h=main_angles(a,ph,order,g);t=h[:,:2].copy()
    q[low,1]*=-1;q+=tr;t[low,0]*=-1;h[low,3]*=-1
    n=np.stack((-t[:,1],t[:,0]),axis=-1)
    return tuple(z[ix].reshape(sh+z.shape[1:]) for z in (q,t,n,h[:,2],h[:,3]))

def section(s,ph,order):
    q,t,n,k,kp=curve(s.v,ph,order)
    return ([unary(s,q[:,i],t[:,i],-k*n[:,i]) for i in range(2)],
            [unary(s,n[:,i],k*t[:,i],kp*t[:,i]-k*k*n[:,i]) for i in range(2)])

def cap_shift(order,ph,mode):
    dx,e=BRANCHES[mode];shift=state(order,ph)[3].copy() if ph else np.zeros(2)
    shift[0]+=dx*ph/.90;return shift,e*ph/.90

def target(s,ph,order,mode,details=False):
    q,_=section(s,ph,order);qo,no=old.profile(s,0.,order,True)
    tr,ret=cap_shift(order,ph,mode);pb,db=m.terminal(order);b=base.axial(order)+pb-ret
    c=[qo[j]+tr[j]-db*no[j]-q[j] for j in range(2)]
    R=np.sqrt((T-.005)**2-b*b);guard=R-.001 if mode=="common" else .90*R
    sq=c[0]*c[0]+c[1]*c[1];num=np.sqrt(np.maximum(sq.v,guard*guard));active=sq.v>guard*guard
    if details:
        raw=np.sqrt(np.maximum(0.,sq.v));return np.column_stack((np.hypot(raw,b)-T,raw-guard))
    r=unary(sq,num,np.where(active,.5/num,0.),np.where(active,-.25/num**3,0.))
    v=r-guard;z=v/(R-guard);p=1+z*z*z*z
    factor=(guard+v*unary(p,p.v**(-.25),-.25*p.v**(-1.25),.3125*p.v**(-2.25)))/r
    c=[x*factor for x in c];one=np.ones_like(s.v)
    vals=(c[0]*no[1]-c[1]*no[0],J(one*b),-c[0]*no[0]-c[1]*no[1])
    return np.stack([np.stack([x+0.*one for x in j.parts()],axis=-1) for j in vals],axis=1)

CACHE={}
def params(s,ph,order,mode):
    key=(ph,order,mode);mem=CACHE.setdefault(key,{})
    a,ix=np.unique(np.mod(s,2*old.material(order,True)[-1]),return_inverse=True)
    todo=np.array([float(z) for z in a if float(z) not in mem])
    u,w=convex.quadrature(order)
    for j in range(0,len(todo),64):
        x=todo[j:j+64];D=target(J(x,s=1.),ph,order,mode);z=np.zeros((len(x),1,2))
        p,H,err,_,_=convex.moment(D[:,:,0],z,u,w);U,M,c=convex.evaluate(p,z,u)
        ps=np.linalg.solve(H,D[:,:,1,None])[...,0]
        Q=convex.contracted(U,c,ps[:,None,:]);r2=D[:,:,3]-np.einsum("q,nqj->nj",w,Q)
        pss=np.linalg.solve(H,r2[...,None])[...,0]
        for i,k in enumerate(x):
            mem[float(k)]=(p[i],ps[i],pss[i],np.r_[err[i],np.linalg.eigvalsh(H[i])[0]])
    return tuple(np.stack([mem[float(z)][j] for z in a])[ix] for j in range(4))

def travel(s,v,ph,order,mode):
    p,ps,pss,_=params(s.v,ph,order,mode);z=np.zeros((len(p),1,2))
    n,w=m.old.disk.rule(order);summ=np.zeros((3,len(p),3))
    for a,b in zip(convex.CUTS[:-1],convex.CUTS[1:]):
        d=np.clip(v.v-a,0.,b-a)
        if np.any(d):
            rec=convex.virtual(a+d[:,None]*n,p,ps,pss,z,z,z)
            for j in range(3):summ[j]+=d[:,None]*np.einsum("q,nqj->nj",w,rec[j])
    U,Us,_,Uv=convex.virtual(v.v[:,None],p,ps,pss,z,z,z)
    return [J(summ[0,:,j],summ[1,:,j],U[:,0,j]*v.a,summ[2,:,j],Us[:,0,j]*v.a,
              Uv[:,0,j]*v.a*v.a+U[:,0,j]*v.aa) for j in range(3)]

def block(chart,a,b,ph,order,mode):
    if not ph:return base.chart_jet(chart,a,b,0.,order,.14,False)
    s=J(a,s=1.);v=J(b,a=1.);side=1 if chart.endswith("+") else -1
    q,n=section(s,ph,order)
    if chart=="cylinder":
        h=m.marks(s,v,order)
        return gather((q[0]+h*n[0],v,q[1]+h*n[1]),len(a))
    tr,ret=cap_shift(order,ph,mode)
    cap=chart.startswith("cap")
    if cap:
        raw=base.chart_jet(chart,a,b,0.,order,.14,False)
        raw[:,0,0]+=tr[0];raw[:,0,2]+=tr[1];raw[:,0,1]-=side*ret
        if chart.startswith("cap-cartesian"):return raw
    q0,n0=old.profile(s,0.,order,True);t0=[n0[1],-n0[0]];pb,db=m.terminal(order)
    u=J(np.full(len(a),T)) if cap else (v+E if chart.startswith("round") else v)
    A,Y,D=travel(s,u,ph,order,mode)
    f=[q[i]+A*t0[i]-D*n0[i] for i in range(2)]
    if not cap:return gather((f[0],side*(B+Y),f[1]),len(a))
    cv=v if chart.startswith("cap-normal") else 1-v
    _,rho=old.collar_clock(cv);h=cap_s7((rho-.83)/.15)
    dx=[h*(f[i]-q0[i]-tr[i]+db*n0[i]) for i in range(2)]
    dy=side*h*(Y-base.axial(order)-pb+ret)
    return gather(tuple(J(*raw[:,:,i].T)+z for i,z in enumerate((dx[0],dy,dx[1]))),len(a))

def chart_jet(chart,s,v,ph,order,mode,rotate=False):
    m.old.disk._public()
    if mode not in BRANCHES or not 0<=ph<=.90000000000001:raise ValueError("R774 registered complete field")
    a,b=np.broadcast_arrays(np.asarray(s,float),np.asarray(v,float));sh=a.shape;a,b=a.ravel(),b.ravel()
    j=np.concatenate([block(chart,a[i:i+192],b[i:i+192],float(ph),order,mode) for i in range(0,len(a),192)])
    if rotate:
        ax=np.asarray(m.axis(order));q=j[:,:,[0,2]].copy();q[:,0]-=ax;q=oldgeom.parent.rot(q,ph);q[:,0]+=ax
        j[:,:,0]=q[:,:,0];j[:,:,2]=q[:,:,1]
    return j.reshape(sh+(6,3))
