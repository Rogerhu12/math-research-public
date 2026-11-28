"""Signed-curvature-ratio R757 roll development, with two matching whole cap jets.
All quadrature is evaluated on the real material. The source returns numerical six-jets.
"""
from functools import lru_cache
import numpy as np
import r763_translated_caps_and_shared_rim as previous
from r742_tilted_disk_two_jets import J,unary,gather,cap_s7
g=previous.g
delay=previous.delay
paired=previous.paired
tube=previous.tube
B=paired.ELL
WIDTH=.024
BOUNDED_WIDTH=.006
EPS=1.e-6
CAP_FADE=.19

def intervals(kind):
    return ((0.,1/3),(2/3,1.)) if kind==1 else ((1/3,2/3),)

def window(t,kind,width=WIDTH):
    z=J(0.)
    for left,right in intervals(kind):
        z=z+cap_s7((t-left)/width)*cap_s7((right-t)/width)
    return z

def cuts(kind,law="constant"):
    width=BOUNDED_WIDTH if law=="bounded" else WIDTH
    return np.unique(np.r_[0.,.5,1.,[v for a,b in intervals(kind) for v in (a,a+width,b-width,b)]])

def root_weight(t,law):
    if law=="constant":return J(np.ones_like(t.v))
    if law!="bounded":raise ValueError("unknown curvature ratio law")
    y=t.v
    fp=unary(t,g.BOW*B*g.shape(y,1),g.BOW*B*g.shape(y,2),g.BOW*B*g.shape(y,3))
    fpp=unary(t,g.BOW*g.shape(y,2),g.BOW*g.shape(y,3),g.BOW*g.shape(y,4))
    v=1+fp*fp;k=fpp*unary(v,v.v**-1.5,-1.5*v.v**-2.5,3.75*v.v**-3.5)
    v=k*k+EPS**2;q=EPS+unary(v,np.sqrt(v.v),.5/np.sqrt(v.v),-.25/v.v**1.5)
    return unary(q,1/np.sqrt(q.v),-.5/q.v**1.5,.75/q.v**2.5)

def rate(t,kind,law):
    x=J(t,s=1.);h=window(x,kind,BOUNDED_WIDTH if law=="bounded" else WIDTH).v
    r=root_weight(x,law).v
    fp=g.BOW*B*g.shape(t,1);fpp=g.BOW*g.shape(t,2)
    return kind*B*fpp/(1+fp*fp)*h**8*r*r

@lru_cache(maxsize=24)
def mass(kind,order,law):
    edges=cuts(kind,law);d=np.diff(edges);n,w=g.disk.rule(order)
    vals=rate(edges[:-1,None]+d[:,None]*n,kind,law)
    return edges,np.r_[0.,np.cumsum(d*(vals@w))]

def fraction(x,kind,order,law):
    x=np.asarray(x).ravel()
    edges,F=mass(kind,order,law);i=np.clip(np.searchsorted(edges,x,side="right")-1,0,len(edges)-2)
    d=x-edges[i];n,w=g.disk.rule(order)
    return (F[i]+d*(rate(edges[i,None]+d[:,None]*n,kind,law)@w))/F[-1]

def information(x,angle,rise,fall,order,law):
    xx=np.clip(np.asarray(x,float).ravel()/B,0,11);j=np.minimum(np.floor(xx).astype(int),10)
    a=xx-j;heading=np.full(len(a),angle);mu=J(np.zeros_like(a))
    root=J(np.zeros_like(a))
    for kind,num,take in ((1,rise,j<rise),(-1,fall,j>=11-fall)):
        if not np.any(take):continue
        t=a[take];fac=angle/(num*mass(kind,order,law)[1][-1])
        q=J(t,s=1/B);w=window(q,kind,BOUNDED_WIDTH if law=="bounded" else WIDTH)
        ww=w*w;w4=ww*ww*root_weight(q,law);v=fac*w4*w4
        # sqrt(1-lambda^2) without subtracting two nearby floating-point numbers.
        q=(2+v).v
        rr=np.sqrt(fac)*w4*unary(2+v,np.sqrt(q),.5/np.sqrt(q),-.25/q**1.5)/(1+v)
        mu=tube.replace(mu,take,v);root=tube.replace(root,take,rr)
        f=fraction(t,kind,order,law)
        heading[take]=angle*((j[take]+f)/num if kind==1 else (11-j[take]-f)/num)
    return heading,mu,root

def increment(x,theta,rise,fall,order,law):
    shape=np.shape(x);xx=np.asarray(x).ravel();a,m,r=information(xx,theta,rise,fall,order,law)
    t=xx/B-np.minimum(10,np.floor(xx/B));fp=g.BOW*B*g.shape(t,1)
    co=np.cos(a);si=np.sin(a)
    return np.column_stack((co-1-si*fp,si+(co-1)*fp)).reshape(shape+(2,))

@lru_cache(maxsize=160)
def primitive(theta,rise,fall,order,law):
    a=np.unique((np.arange(11)[:,None]+np.unique(np.r_[cuts(1,law),cuts(-1,law)]))*B)
    a[0]=0.;a[-1]=paired.TRACK;n,w=g.disk.rule(order);d=np.diff(a)
    val=increment(a[:-1,None]+d[:,None]*n,theta,rise,fall,order,law)
    return a,np.vstack((np.zeros(2),np.cumsum(d[:,None]*np.einsum("nqc,q->nc",val,w),axis=0)))

def shift(x,theta,rise,fall,order,law):
    edges,p=primitive(theta,rise,fall,order,law);i=np.clip(np.searchsorted(edges,x,side="right")-1,0,len(edges)-2)
    d=x-edges[i];n,w=g.disk.rule(order)
    return p[i]+d[:,None]*np.einsum("nqc,q->nc",increment(edges[i,None]+d[:,None]*n,theta,rise,fall,order,law),w)

def section(s,theta,rise,fall,order,law):
    us,inv=np.unique(s.v,return_inverse=True);_,old,live,ell,ff=g.local(us,order)
    Q,T,N,K,Ks=g.profile_coordinates(us,order)
    m=g.original.profile_constants(order);P=2*m[4];u0=m[1];bot=P-u0-paired.TRACK
    a=old%P;D=primitive(theta,rise,fall,order,law)[1][-1]
    Q[(a<u0)|(a>bot+paired.TRACK)]-=D
    lm=[np.ones_like(a),np.zeros_like(a),np.zeros_like(a)]
    zz=[np.zeros_like(a) for i in range(3)]
    for origin,side in ((u0,1),(bot,-1)):
        mask=(a>=origin)&(a<=origin+paired.TRACK)
        if not np.any(mask):continue
        x=a[mask]-origin;ang,mu,root=information(x,theta,rise,fall,order,law)
        disp=shift(x,theta,rise,fall,order,law)
        Q[mask]+=disp-D if side==1 else -disp
        co=np.cos(ang);si=np.sin(ang);t=T[mask].copy()
        T[mask]=np.column_stack((co*t[:,0]-si*t[:,1],si*t[:,0]+co*t[:,1]))
        speed=np.sqrt(1+ff[1][mask]**2);v2=ff[1][mask]*ff[2][mask]/speed
        Ks[mask]=(1+mu.v)*Ks[mask]+(mu.s/speed)*K[mask];K[mask]*=1+mu.v
        for dest,obj in ((lm,J(1.)/(1+mu)),(zz,root)):
            dest[0][mask]=obj.v;dest[1][mask]=obj.s/speed
            dest[2][mask]=obj.ss/speed**2-obj.s*v2/speed**3
    N=np.column_stack((-T[:,1],T[:,0]))
    def pack(a,b,c):return unary(s,a[inv],b[inv],c[inv])
    point=[pack(Q[:,i],T[:,i],-K*N[:,i]) for i in range(2)]
    normal=[pack(N[:,i],K*T[:,i],Ks*T[:,i]-K*K*N[:,i]) for i in range(2)]
    return point,normal,pack(*lm),pack(*zz)

@lru_cache(maxsize=4096)
def radial_rule(v,order):
    old=float(delay.original_parameter(np.array([v]))[0])
    end=g.END_LENGTH;h=g.END_BLEND;r=g.END_TURN
    a=np.unique(np.clip([0.,h/4,h/2,h,.001,end/2,end-.002,end-h,end-h/4,old],0,old))
    n,w=g.disk.rule(order);d=np.diff(a)
    x=(a[:-1,None]+d[:,None]*n).ravel()
    al=g.disk.softened_angle(x,end,h,1/r)
    k=g.disk.s5(np.clip(np.minimum(x,end-x)/h,0,1))/r
    weight=1+delay.EXTRA*4*np.maximum(1-al/delay.SMALL_ANGLE,0.)**3*k/delay.SMALL_ANGLE
    weight=weight*(d[:,None]*w).ravel()
    return weight,np.cos(al),np.sin(al)

def rise_height(z,v,p,order):
    # z depends on s alone. v is the independent physical v-jet on a roll
    # or the constant terminal value on a cap. First integrate at fixed v.
    vv=np.broadcast_to(v.v,np.shape(z.v));dv=np.zeros_like(vv);dz=dv.copy();dzz=dv.copy()
    for val in np.unique(vv):
        ii=np.flatnonzero((vv==val)&(z.v!=0.))
        if not len(ii):continue
        weight,c,s=radial_rule(float(val),order)
        for start in range(0,len(ii),256):
            ix=ii[start:start+256];a=z.v[ix,None];b=np.hypot(c,a*s)
            dv[ix]=((a*s)**2/(b+c))@weight
            dz[ix]=(a*s*s/b)@weight;dzz[ix]=((c/b)**2*s*s/b)@weight
    # The terminal clock has cos(alpha)=0 exactly in the defining formulas.
    x=delay.original_parameter(vv);L=g.END_LENGTH;h=g.END_BLEND;r=g.END_TURN
    alpha=g.disk.softened_angle(x,L,h,1/r);c=np.where(vv>=delay.END_LENGTH,0.,np.cos(alpha));sn=np.sin(alpha)
    k=g.disk.s5(np.clip(np.minimum(x,L-x)/h,0,1))/r
    k=k/(1+delay.EXTRA*4*np.maximum(1-alpha/delay.SMALL_ANGLE,0.)**3*k/delay.SMALL_ANGLE)
    H=np.hypot(c,z.v*sn);den=np.where(H>0.,H,1.)
    Hv=-(1-z.v*z.v)*sn*c*k/den;Hz=z.v*sn*sn/den
    # p already supplies the corresponding exact unmodified primitive and jets.
    f=(z*0)+unary(z,dv,dz,dzz)
    pdelta=H-c;pvv=Hv+sn*k
    return J(p.v+f.v,p.s+f.s+pdelta*v.s,p.a+f.a+pdelta*v.a,
             p.ss+f.ss+pvv*v.s*v.s+2*Hz*z.s*v.s+pdelta*v.ss,
             p.sa+f.sa+pvv*v.s*v.a+Hz*(z.s*v.a+z.a*v.s)+pdelta*v.sa,
             p.aa+f.aa+pvv*v.a*v.a+2*Hz*z.a*v.a+pdelta*v.aa)

def chart_jet(chart,u,v,phase=0.,design=None,order=32):
    design={} if design is None else design
    if design.get("cap","ratio")!="ratio":return previous.chart_jet(chart,u,v,phase,design,order)
    aa,bb=np.broadcast_arrays(np.asarray(u,float),np.asarray(v,float));sh=aa.shape
    s=J(aa.ravel(),s=1.);v=J(bb.ravel(),a=1.);t=float(phase)
    if not t:return delay.chart_jet(chart,s.v,v.v,0.,order,bend=0.,rotate=False).reshape(sh+(6,3))
    th=design.get("angle",.78)*np.sin(t);nu=design.get("rise",2);nd=design.get("fall",2)
    law=design.get("ratio_law","constant")
    if min(nu,nd)<1 or nu+nd>11 or th<0:raise ValueError("invalid signed-ratio track")
    sg=1 if chart.endswith("+") else -1
    pb,db=delay.end_limits(order)
    if chart=="cylinder" or chart.startswith("end"):
        q,n,l,z=section(s,th,nu,nd,order,law)
        if chart=="cylinder":X,Y,Z=q[0],v,q[1]
        else:
            p,d=delay.end_offsets(v,order)
            Y=sg*(delay.HALF_WIDTH+rise_height(z,v,p,order))
            X,Z=[q[i]-l*d*n[i] for i in (0,1)]
    else:
        X,Y,Z=delay.sphere_chart(chart,s,v,np.zeros_like(s.v),order,"legacy")
        if "cartesian" in chart:
            # This original regular core chart has w>.75. The named Cartesian
            # verification probes also lie beyond CAP_FADE; recover material w
            # when a Cartesian overlap is evaluated closer to the true rim.
            from bent_shared_rim_fields import cartesian_material
            a,w=cartesian_material(X,Z)
        else:a=s;w=v if "normal" in chart else 1-v
        D=primitive(th,nu,nd,order,law)[1][-1];delta=[-.5*D[0],-sg*design.get("shorten",.23)*np.sin(t),-.5*D[1]]
        X,Y,Z=X+delta[0],Y+delta[1],Z+delta[2]
        active=np.flatnonzero(w.v<CAP_FADE)
        if len(active):
            a=tube.cut(a,active);w=tube.cut(w,active)
            q,n,l,z=section(a,th,nu,nd,order,law);q0,n0=g.profile(a,order)
            const=J(np.full(len(active),delay.END_LENGTH));hp=rise_height(z,const,J(pb),order)
            weight=1-cap_s7(w/CAP_FADE);d=db+w
            diff=[q[i]-l*d*n[i]-q0[i]+d*n0[i] for i in (0,1)]
            increments=[diff[0],sg*(hp-pb+w*z),diff[1]]
            vals=[X,Y,Z]
            for i in range(3):
                vals[i]=tube.replace(vals[i],active,tube.cut(vals[i],active)+weight*(increments[i]-delta[i]))
            X,Y,Z=vals
    return gather((X,Y,Z),len(s.v)).reshape(sh+(6,3))
