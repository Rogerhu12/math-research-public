#!/usr/bin/env python3
"""Full R769 material sphere on the single R764 zero-phase metric; physical two-jets."""
from functools import lru_cache
import numpy as np
import r764_corrugated_pre_roll_and_movable_complete_caps as base
import r766_positive_boundary_curvature_and_exact_signed_ribbons as parent
from r742_tilted_disk_two_jets import J,unary,cap_s7,gather

old=base.old
m=base.m
E,L,B=base.E,base.L,base.HALF
PITCH=(.5,1.)
gate=base.gate

def clock_data(z,left,right,ramp):
    """Normalized integral, speed and its first two derivatives; endpoints genuine plateaus."""
    length=right-left;scale=length-ramp;t=np.clip(z-left,0.,length)
    a=np.clip(t/ramp,0.,1.);b=np.clip((length-t)/ramp,0.,1.)
    def prim(x):
        return x**5*(7+x*(-14+x*(10-2.5*x)))
    def smooth(x):
        return x**4*(35+x*(-84+x*(70-20*x)))
    rise=t<ramp;fall=t>length-ramp
    U=np.where(rise,ramp*prim(a),np.where(fall,scale-ramp*prim(b),t-ramp/2))
    speed=np.where(rise,smooth(a),np.where(fall,smooth(b),1.))
    ds=np.where(rise,140*(a*(1-a))**3/ramp,np.where(fall,-140*(b*(1-b))**3/ramp,0.))
    dds=np.where(rise,420*(a*(1-a))**2*(1-2*a)/ramp**2,
                 np.where(fall,420*(b*(1-b))**2*(1-2*b)/ramp**2,0.))
    return U/scale,speed/scale,ds/scale,dds/scale

def upper_basis(s,order):
    shape=s.shape;a=np.asarray(s,float).ravel()
    _,t,_,k,kp=old.data(a,0.,order,True)
    theta=np.arctan2(t[:,1],t[:,0]);A=np.pi/2
    lh,m0,m1,rtop,_,_,_,_,st,*_=m.constants(order)
    origin=m.LEFT_LENGTH/2+st-lh
    l0=origin+lh;l1=origin+m0;x0=l1+1.30;x1=l1+1.56
    right=origin+m1
    wc=np.zeros_like(a);wt=wc.copy();dc=np.zeros((len(a),3));dt=dc.copy()
    def assign(mask,arg,prime,left,right,ramp,c0,t0,c1,t1):
        h,b,db,ddb=clock_data(arg,left,right,ramp)
        wc[mask]=c0+c1*h;wt[mask]=t0+t1*h
        # beta_new=beta0+closure*wc+phase*wt; arg'=sign*k0.
        sg=1. if prime else -1.
        w=np.column_stack((-sg*b,-db*k[mask],-sg*ddb*k[mask]**2-db*kp[mask]))
        dc[mask]=c1*w;dt[mask]=t1*w
    mask=(a>l0)&(a<l1)
    assign(mask,A-theta[mask],True,.02,A-.02,.04,0.,0.,1.,0.)
    mask=(a>=l1)&(a<=x0);wc[mask]=1.
    mask=(a>x0)&(a<x1)
    assign(mask,theta[mask],False,.02,A-.02,.04,1.,0.,-1.,-1.)
    mask=(a>=x1)&(a<=right);wt[mask]=-1.
    mask=(a>right)&(a<origin+rtop)
    assign(mask,A-theta[mask],True,1.05,np.pi-.38,.14,0.,-1.,0.,1.)
    cols=np.column_stack((t,k,kp,wc,wt,dc,dt))
    return cols.reshape(shape+(cols.shape[-1],))

def tangents(z,ph,closure):
    return parent.rot(z[...,:2],z[...,4]*closure+z[...,5]*ph)

@lru_cache(maxsize=16)
def stations(order):
    grid=parent.cuts(order,0.)
    lh,m0,m1,rtop,_,_,_,_,st,*_=m.constants(order)
    org=m.LEFT_LENGTH/2+st-lh;A=np.pi/2;off=m.old.PLANAR_BLEND/2
    angles=[.02,.06,A-.06,A-.02]
    # Invert the actual material bend, including its two nonconstant-curvature ramps.
    more=[org+lh+off+.15*x for x in angles]
    for goal in angles:
        low,high=.30,.56
        for _ in range(54):
            mid=(low+high)/2
            if m.old.disk.beta(np.asarray(mid))<goal:low=mid
            else:high=mid
        more.append(org+m0+1+(low+high)/2)
    grid=np.unique(np.r_[grid,more]);grid=grid[np.r_[True,np.diff(grid)>1e-13]]
    n,w=m.old.disk.rule(order);width=np.diff(grid)
    z=upper_basis(grid[:-1,None]+width[:,None]*n,order)
    return grid,width,z,w

@lru_cache(maxsize=256)
def state(order,ph):
    grid,width,z,w=stations(order)
    def height(lam):
        return float(np.sum(width*(tangents(z,ph,lam)[...,1]@w)))
    low,high=0.,.45
    if ph:
        if height(low)>5e-13 or height(high)<0:
            raise ValueError("true whole upper closure failed its analytic bracket")
        for _ in range(57):
            mid=(low+high)/2
            if height(mid)>0:high=mid
            else:low=mid
    lam=(low+high)/2 if ph else 0.
    edges=width[:,None]*np.einsum("ink,n->ik",tangents(z,ph,lam),w)
    start=old.data(np.array([0.]),0.,order,True)[0][0]
    Q=start+np.vstack((np.zeros(2),np.cumsum(edges,axis=0)))
    anchor=m.grip_s(.55,order);j=np.argmin(abs(grid-anchor))
    wanted=old.data(np.array([anchor]),ph,order,True)[0][0]
    return grid,Q,lam,wanted-Q[j],(height(0.),height(.45),height(lam))

def curve(s,ph,order):
    sh=np.shape(s);u,ix=np.unique(np.asarray(s,float).ravel(),return_inverse=True)
    half=old.material(order,True)[-1];v=u%(2*half);lower=v>half
    a=np.where(lower,2*half-v,v)
    if not ph:
        q,t,n,k,kp=old.data(u,0.,order,True);r=np.ones_like(u);rs=r*0.;rss=rs
    else:
        grid,Q,lam,shift,_=state(order,ph);j=np.clip(np.searchsorted(grid,a,side="right")-1,0,len(grid)-2)
        span=a-grid[j];x,w=m.old.disk.rule(order);parts=[]
        for lo in range(0,len(u),384):
            sl=slice(lo,lo+384)
            z=upper_basis(grid[j[sl],None]+span[sl,None]*x,order)
            parts.append(np.einsum("ink,n->ik",tangents(z,ph,lam),w))
        q=Q[j]+span[:,None]*np.concatenate(parts)
        z=upper_basis(a,order);t=tangents(z,ph,lam)
        k0,kp0=z[:,2],z[:,3]
        aa,az,azz=(lam*z[:,6:9]+ph*z[:,9:12]).T
        aa=1+aa;r=1/aa;rs=-az*r*r;rss=2*az**2*r**3-azz*r*r
        k=k0*aa;kp=kp0*aa+k0*az
        q[lower,1]*=-1;t[lower,0]*=-1;kp[lower]*=-1;rs[lower]*=-1
        q+=shift;n=np.stack((-t[:,1],t[:,0]),axis=1)
    return tuple(z[ix].reshape(sh+z.shape[1:]) for z in (q,t,n,k,kp,r,rs,rss))

def section(s,ph,order):
    q,t,n,k,kp,r,rs,rss=curve(s.v,ph,order)
    return ([unary(s,q[:,j],t[:,j],-k*n[:,j]) for j in range(2)],
            [unary(s,n[:,j],k*t[:,j],kp*t[:,j]-k*k*n[:,j]) for j in range(2)],unary(s,r,rs,rss))

def angle(z,regular):
    if regular:
        a=m.old.disk.softened_angle(z,L,m.END_E,1/m.END_R)
        u=np.clip(np.minimum(z,L-z)/m.END_E,0.,1.)
        return a,m.old.disk.s5(u)/m.END_R
    a=np.pi*z/E
    return (base.EPS*np.sin(2*a)*np.sin(a)**2,
        (np.pi*base.EPS/E)*(2*np.cos(2*a)*np.sin(a)**2+np.sin(2*a)**2))

def velocity(r,z,regular):
    al,ap=angle(z,regular);si=np.sin(al);co=np.cos(al)
    if regular:
        h=np.sqrt(co*co+r*r*si*si)
        # Tangents P_v,D_v and their r,rr,v derivatives.
        p=co/h;d=r*si/h;b=r*si**2/h**2
        return ((p,-p*b,p*(3*b*b-si**2/h**2),-r*r*si*ap/h**3),
                (d,si*co**2/h**3,-3*r*si**3*co**2/h**5,r*co*ap/h**3))
    d=r*si;p=np.sqrt(1-d*d)
    return ((p,-r*si**2/p,-si**2/p**3,-r*r*si*co*ap/p),
            (d,si,np.zeros_like(d),r*co*ap))

def travel(r,v,regular,order):
    z=np.asarray(v.v);rr=r.v;x,w=m.old.disk.rule(order)
    cuts=(0.,m.END_E,L/2,L-m.END_E,L) if regular else (0.,E/4,E/2,3*E/4,E)
    sums=np.zeros((2,3,len(z)))
    for left,right in zip(cuts[:-1],cuts[1:]):
        span=np.clip(z-left,0.,right-left)
        data=velocity(rr[:,None],left+span[:,None]*x,regular)
        for j in range(2):
            for i in range(3):
                sums[j,i]+=span*(data[j][i]@w)
    if not regular:
        at=z==E;sums[1,:,at]=0.
    edge=velocity(rr,z,regular)
    def compose(j):
        f,fr,frr=sums[j]
        fv,frv,_,fvv=edge[j]
        return J(f,fr*r.s+fv*v.s,fr*r.a+fv*v.a,
            frr*r.s*r.s+2*frv*r.s*v.s+fvv*v.s*v.s+fr*r.ss+fv*v.ss,
            frr*r.s*r.a+frv*(r.s*v.a+r.a*v.s)+fvv*v.s*v.a+fr*r.sa+fv*v.sa,
            frr*r.a*r.a+2*frv*r.a*v.a+fvv*v.a*v.a+fr*r.aa+fv*v.aa)
    return compose(0),compose(1)

@lru_cache(maxsize=224)
def right_motion(order,ph):
    half=old.material(order,True)[-1];s=np.array([half])
    return curve(s,ph,order)[0][0]-old.data(s,0.,order,True)[0][0]

def block(chart,a,b,ph,order,pitch):
    if not ph:
        return base.chart_jet(chart,a,b,0.,order,.14,False)
    side=1 if chart.endswith("+") else -1
    s=J(a,s=1.);v=J(b,a=1.);q,n,r=section(s,ph,order)
    if chart=="cylinder":
        h=m.marks(s,v,order);out=(q[0]+h*n[0],v,q[1]+h*n[1])
    elif chart.startswith("preband"):
        p,d=travel(r,v,False,order);out=(q[0]-d*n[0],side*(B+p),q[1]-d*n[1])
    elif chart.startswith("round"):
        p0=travel(r,J(np.full(len(a),E)),False,order)[0]
        p,d=travel(1+pitch*(r-1),v,True,order)
        out=(q[0]-d*n[0],side*(B+p0+p),q[1]-d*n[1])
    else:
        raw=base.chart_jet(chart,a,b,0.,order,.14,False)
        tr=right_motion(order,ph);raw[:,0,0]+=tr[0];raw[:,0,2]+=tr[1]
        if chart.startswith("cap-cartesian"):
            return raw
        w=v if chart.startswith("cap-normal") else 1-v
        j,rho=old.collar_clock(w)
        # Entire real physical outer collar and the original chart overlap.
        # The deformation is zero on the whole rho<=.83 region, outside the polar/Cartesian overlap.
        fade=cap_s7((rho-.83)/.15)
        q0,n0=old.profile(s,0.,order,True)
        p0=travel(r,J(np.full(len(a),E)),False,order)[0]
        pr,dr=travel(1+pitch*(r-1),J(np.full(len(a),L)),True,order)
        pb,db=m.terminal(order)
        delta=[fade*(q[i]-(dr+j)*n[i]-q0[i]-tr[i]+(db+j)*n0[i]) for i in range(2)]
        dy=side*fade*(p0+pr-base.axial(order)-pb)
        out=tuple(J(*raw[:,:,i].T)+z for i,z in enumerate((delta[0],dy,delta[1])))
    return gather(out,len(a))

def chart_jet(chart,u,v,phase=0.,order=32,pitch=1.,rotate=True):
    m.old.disk._public();ph=float(phase)
    if not 0<=ph<=.90000000000001 or pitch not in PITCH:
        raise ValueError("R769 phase or registered angular response")
    a,b=np.broadcast_arrays(np.asarray(u,float),np.asarray(v,float));sh=a.shape
    a,b=a.ravel(),b.ravel()
    out=np.concatenate([block(chart,a[i:i+384],b[i:i+384],ph,order,pitch) for i in range(0,len(a),384)])
    if rotate:
        axis=np.asarray(m.axis(order));xz=out[:,:,[0,2]].copy();xz[:,0]-=axis
        xz=parent.rot(xz,ph);xz[:,0]+=axis;out[:,:,0]=xz[:,:,0];out[:,:,2]=xz[:,:,1]
    return out.reshape(sh+(6,3))
