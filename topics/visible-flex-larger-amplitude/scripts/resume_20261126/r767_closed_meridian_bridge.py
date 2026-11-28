"""R767 globally closed field. Independent even polarization fields preserve all meridian speeds and both rigid ends."""
from functools import lru_cache
from math import factorial
import numpy as np
from r742_tilted_disk_two_jets import J,unary,trig,gather
import r767_negative_track_profile as g
import r767_preloaded_cap_atlas as cap
L=cap.LBRIDGE
Y=cap.HALF_WIDTH
EP=.25

def pulse(u):
    def cl(x):return unary(x,*g.clock(x.v))
    p=cl(u/EP)*cl((1-u)/EP)
    b=trig(2*np.pi*cl(u))[1]
    return p,b

def abscissae():
    return np.unique(np.r_[0.,g.ROUND,1-g.ROUND,1.,EP,1-EP,
          EP*g.ROUND,EP*(1-g.ROUND),1-EP*g.ROUND,1-EP*(1-g.ROUND),.25,.5,.75])

@lru_cache(maxsize=12)
def rule(order):
    a=abscissae();n,w=g.old.rule(order);d=np.diff(a)
    x=(a[:-1,None]+d[:,None]*n).ravel();ww=(d[:,None]*w).ravel()
    p,b=pulse(J(x));return x,ww,p.v,b.v

@lru_cache(maxsize=12)
def axial0(order):
    x,w,p,b=rule(order);return L*float(w@np.cos(cap.PRELOAD*b))

@lru_cache(maxsize=32)
def pcoef(j):
    a=np.array([(-1.)**k/factorial(2*k+j) for k in range(16)])
    return a,np.polynomial.polynomial.polyder(a),np.polynomial.polynomial.polyder(a,2)

def entire(x,j):
    # cos(sqrt(x)), sinc(sqrt(x)), and (1-cos(sqrt(x)))/x, including two jets at zero.
    v,d,e=pcoef(j);fv=np.polynomial.polynomial.polyval
    return unary(x,fv(x.v,v),fv(x.v,d),fv(x.v,e))

def spread(a):
    return J(*(np.asarray(x)[...,None] for x in a.parts()))

def integrate(a,w):
    return J(*(np.sum(np.asarray(x)*w,axis=-1) for x in a.parts()))

def desired(s,t,order):
    theta=g.ANGLE*np.sin(t);q0,_,_=g.section(s,0.,order);qt,_,_=g.section(s,theta,order)
    shift=-.5*(g.track_integrator(theta,order)[1][-1]-g.track_integrator(0.,order)[1][-1])
    h=[(q0[i]-qt[i]+shift[i])/L for i in range(2)]
    z=(axial0(order)-cap.SHORTEN*np.sin(t))/L
    return h,J(np.full(np.shape(s.v),z)),shift

def means(Bx,Bz,G,order):
    _,w,p,b=rule(order);x=spread(Bx);z=spread(Bz);G=spread(G)
    k=(x*x+z*z)*(p*p);y=entire(G*(b*b),0)
    h=integrate(y*entire(k,1)*p,w)
    return (Bx*h,Bz*h,integrate(y*entire(k,0),w))

def solve_values(X,Yval,t,order):
    _,w,p,b=rule(order);N=len(X)
    if not t:return np.zeros(N),np.full(N,cap.PRELOAD**2)
    beta=np.minimum(1.40,X/.71);G=np.clip(2*(1-Yval-.5*beta**2*(w@(p*p)))/(w@(b*b)),0.0001,2.42)
    def scalars(pp,gg,ids):
        u=pp[:,None]*p;z=np.sqrt(np.maximum(gg,0.))[:,None]*b
        cc=np.cos(z);dg=-.5*b*b*np.sinc(z/np.pi)
        si=np.sin(u);co=np.cos(u)
        return ((si*cc)@w-X[ids],(co*cc)@w-Yval[ids],
                (p*co*cc)@w,(si*dg)@w,(-p*si*cc)@w,(co*dg)@w)
    ids=np.arange(N)
    for _ in range(14):
        f,h,a,b1,c,d=scalars(beta,G,ids);ok=(abs(f)+abs(h)<8.e-14)
        if np.all(ok):return beta,G
        det=a*d-c*b1
        beta=np.where(ok,beta,np.clip(beta-(d*f-b1*h)/det,0,np.pi/2))
        G=np.where(ok,G,np.clip(G-(-c*f+a*h)/det,0,(np.pi/2)**2))
    f,h,*_=scalars(beta,G,ids);ids=np.flatnonzero(abs(f)+abs(h)>=8.e-14)
    if not len(ids):return beta,G
    # Monotone continuation at fixed horizontal mean. If the requested X lies
    # above the current maximum, gamma is past the admissible endpoint.
    lo=np.zeros(len(ids));hi=np.full(len(ids),np.pi/2)
    for _ in range(48):
        gam=.5*(lo+hi);cg=np.cos(gam[:,None]*b)
        bl=np.zeros(len(ids));bh=np.full(len(ids),np.pi/2)
        for _ in range(47):
            bm=.5*(bl+bh);xx=(cg*np.sin(bm[:,None]*p))@w
            bl=np.where(xx<X[ids],bm,bl);bh=np.where(xx>=X[ids],bm,bh)
        be=.5*(bh+bl);yy=(cg*np.cos(be[:,None]*p))@w
        bad=((cg*np.sin((np.pi/2)*p))@w<X[ids])|(yy<Yval[ids])
        hi=np.where(bad,gam,hi);lo=np.where(~bad,gam,lo)
    beta[ids]=be;G[ids]=gam*gam
    f,h,*_=scalars(beta[ids],G[ids],ids)
    if np.max(abs(f)+abs(h))>5.e-11:raise ArithmeticError("R767 meridian endpoint root")
    return beta,G

def controls(s,t,order):
    u,inv=np.unique(s.v,return_inverse=True);a=J(u,s=1.);h,y,shift=desired(a,t,order)
    X=np.hypot(h[0].v,h[1].v);be,G=solve_values(X,y.v,t,order)
    _,w,p,b=rule(order);fac=(p*np.sinc(be[:,None]*p/np.pi)*np.cos(np.sqrt(G)[:,None]*b))@w
    vals=[h[0].v/fac,h[1].v/fac,G];D=np.empty((len(u),3,3))
    for k in range(3):
        v=means(*[J(x,s=float(i==k)) for i,x in enumerate(vals)],order)
        D[:,:,k]=np.stack(np.broadcast_arrays(*[z.s for z in v],u)[:3],axis=1)
    rhs=np.stack(np.broadcast_arrays(h[0].s,h[1].s,y.s,u)[:3],axis=1)
    vel=np.linalg.solve(D,rhs[:,:,None])[:,:,0]
    v=means(*[J(x,s=vel[:,i]) for i,x in enumerate(vals)],order)
    rhs=np.stack([np.broadcast_to(z.ss,np.shape(u))-w0.ss for z,w0 in zip((h[0],h[1],y),v)],axis=1)
    acc=np.linalg.solve(D,rhs[:,:,None])[:,:,0]
    return [unary(s,x[inv],vel[inv,i],acc[inv,i]) for i,x in enumerate(vals)]

def cross(a,b):
    return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])

def tangent(s,u,ctl,n,T,t,side,polarization,order):
    p,b=pulse(u);bx,bz,G=ctl
    # Positive G on the whole compact (s,t) set, including t=0.
    gamma=cap.root(G);cb,sb=trig(gamma*b)
    angle=J(0.)
    if polarization is not None:
        angle=.5*np.sin(t)*(polarization(side,s,u,t)+polarization(side,s,1-u,t))
    co,si=trig(angle);w=[sb*(-co*n[i]+si*T[i]) for i in range(2)]
    raw=[w[0],cb,w[1]];axis=[bz,0.*bx,-bx]
    cr=cross(axis,raw);cc=cross(axis,cr)
    v=p*p*(bx*bx+bz*bz);a=p*entire(v,1);b=p*p*entire(v,2)
    return [raw[i]+a*cr[i]+b*cc[i] for i in range(3)]

def bridge(sval,vval,t,side,field,order):
    s=J(sval,s=1.);u=J(vval/L,a=1/L);theta=g.ANGLE*np.sin(t)
    q,n,T=g.section(s,theta,order);ctl=controls(s,t,order)
    start=[q[0],J(np.full(len(sval),Y)),q[1]]
    f=tangent(s,u,ctl,n,T,t,side,field,order)
    # At fixed upper limit integrate the material s-jets and take the
    # transverse derivatives by the fundamental theorem of calculus.
    rows=[np.zeros((3,len(sval))) for _ in range(3)]
    knots=abscissae();nd,wt=g.old.rule(order)
    for l,r in zip(knots[:-1],knots[1:]):
        length=np.clip(u.v-l,0,r-l)
        ix=np.flatnonzero(length>0)
        if not len(ix):continue
        def jj(z):return J(*(np.broadcast_to(v,sval.shape)[ix,None] for v in z.parts()))
        uv=J(l+length[ix,None]*nd)
        vv=tangent(jj(s),uv,[jj(z) for z in ctl],[jj(z) for z in n],[jj(z) for z in T],t,side,field,order)
        for i,z in enumerate(vv):
            for j,part in enumerate((z.v,z.s,z.ss)):
                rows[i][j,ix]+=L*length[ix]*(np.broadcast_to(part,np.shape(uv.v))@wt)
    ans=[]
    for i in range(3):
        r=rows[i];z=f[i]
        part=J(start[i].v+r[0],start[i].s+r[1],z.v,start[i].ss+r[2],z.s,z.a)
        ans.append(-part if side<0 and i==1 else part)
    return gather(ans,len(sval))

def chart_jet(chart,u,v,phase=0.,order=32,polarization=None):
    aa,bb=np.broadcast_arrays(np.asarray(u,float),np.asarray(v,float));shape=aa.shape
    u=aa.ravel();v=bb.ravel();s=J(u,s=1.);b=J(v,a=1.);t=float(phase);theta=g.ANGLE*np.sin(t)
    side=1 if chart.endswith("+") else -1
    if chart=="cylinder":
        q,n,T=g.section(s,theta,order);f=gather((q[0],b,q[1]),len(u))
    else:
        shift=-.5*(g.track_integrator(theta,order)[1][-1]-g.track_integrator(0.,order)[1][-1])
        y0=Y+axial0(order)-cap.SHORTEN*np.sin(t)
        if chart.startswith("end"):
            f=np.empty((len(u),6,3));ii=np.flatnonzero(v<=L)
            for start in range(0,len(ii),96):
                ix=ii[start:start+96];f[ix]=bridge(u[ix],v[ix],t,side,polarization,order)
            ix=np.flatnonzero(v>L)
            if len(ix):
                q,n,T=g.section(J(u[ix],s=1.),0.,order)
                p,d=g.smooth_curve(J(v[ix]-L,a=1.),cap.OUTER_L,cap.OUTER_R,cap.OUTER_BLEND,order)
                f[ix]=gather((q[0]-d*n[0]+shift[0],side*(y0+p),q[1]-d*n[1]+shift[1]),len(ix))
        elif chart.startswith("cap"):
            p=cap.cap_point(chart,s,b,order);y=side*(y0+cap.end_limits(order)[0]+cap.crown(p,order))
            f=gather((p[0]+shift[0],y,p[1]+shift[1]),len(u))
        else:raise ValueError("unknown R767 chart")
    return f.reshape(shape+(6,3))
