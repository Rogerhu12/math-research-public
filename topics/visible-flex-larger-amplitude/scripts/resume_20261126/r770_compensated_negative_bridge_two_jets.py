"""R768/R770 fixed R767 metric. Two real meridian ends, non-even null moments and a three-vector endpoint corrector."""
from functools import lru_cache
import numpy as np
import r767_closed_meridian_bridge as old
import r767_negative_track_profile as g
import r767_preloaded_cap_atlas as cap
from r742_tilted_disk_two_jets import J,unary,trig,gather,cap_s7
L=cap.LBRIDGE
Y=cap.HALF_WIDTH
EP=.1
EDGE=.0005
SHORT=.40
entire,spread,integrate=old.entire,old.spread,old.integrate

def pulse(u):
    def cl(x):return unary(x,*g.clock(x.v))
    a=cl(u/EP)*cl((1-u)/EP)
    return a*a,trig(2*np.pi*cl(u))[1]

def envelope(u,a,b,d):
    def window(w):return cap_s7((w-a)/d)*cap_s7((b-w)/d)
    return window(u)+window(1-u)

def abscissae():
    a=np.array([0,EDGE,.006,.014,.06,.080,.088,EP*g.ROUND,EP*(1-g.ROUND),EP,
                .22,.31,.38,.44,.45,.46,.47,.5])
    return np.unique(np.r_[a,1-a])
@lru_cache(maxsize=12)
def rule(order):
    a=abscissae();n,w=g.old.rule(order);d=np.diff(a)
    x=(a[:-1,None]+d[:,None]*n).ravel();ww=(d[:,None]*w).ravel()
    p,b=pulse(J(x));return x,ww,p.v,b.v


def desired(s,t,order):
    h,y,shift=old.desired(s,t,order)
    return h,y-(SHORT-cap.SHORTEN)*np.sin(t)/L,shift
def means(Bx,Bz,G,order):
    _,w,p,b=rule(order);x=spread(Bx);z=spread(Bz);G=spread(G)
    k=(x*x+z*z)*(p*p);y=entire(G*(b*b),0)
    h=integrate(y*entire(k,1)*p,w)
    return (Bx*h,Bz*h,integrate(y*entire(k,0),w))

def solve_values(X,Yval,t,order):
    _,w,p,b=rule(order);N=len(X)
    if not t:return np.zeros(N),np.full(N,cap.PRELOAD**2)
    beta=np.minimum(1.40,X/.71);G=np.clip(2*(1-Yval-.5*beta**2*(w@(p*p)))/(w@(b*b)),0.0001,8.7)
    def scalars(pp,gg,ids):
        u=pp[:,None]*p;z=np.sqrt(np.maximum(gg,0.))[:,None]*b
        cc=np.cos(z);dg=-.5*b*b*np.sinc(z/np.pi)
        si=np.sin(u);co=np.cos(u)
        return ((si*cc)@w-X[ids],(co*cc)@w-Yval[ids],
                (p*co*cc)@w,(si*dg)@w,(-p*si*cc)@w,(co*dg)@w)
    ids=np.arange(N)
    for _ in range(18):
        f,h,a,b1,c,d=scalars(beta,G,ids);ok=(abs(f)+abs(h)<8.e-14)
        if np.all(ok):return beta,G
        det=a*d-c*b1
        beta=np.where(ok,beta,np.clip(beta-(d*f-b1*h)/det,0,np.pi/2))
        G=np.where(ok,G,np.clip(G-(-c*f+a*h)/det,0,np.pi**2))
    f,h,*_=scalars(beta,G,ids);ids=np.flatnonzero(abs(f)+abs(h)>=8.e-14)
    if not len(ids):return beta,G
    # Monotone continuation at fixed horizontal mean. If the requested X lies
    # above the current maximum, gamma is past the admissible endpoint.
    lo=np.zeros(len(ids));hi=np.full(len(ids),np.pi)
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


def kap(s,t,order):
    """One-sided curvature second derivatives, combined only in a C2 common quotient."""
    v=np.mod(s.v,g.P);k,kp=g.coordinates(v,t,order)[-2:];ks=np.zeros_like(v)
    def s5pp(x):
        z=np.clip(x,0,1)
        return 60*z*(1-z)*(1-2*z)
    def cpp(x):
        z=np.clip(x,0,1)
        return s5pp(np.minimum(z,1-z)/g.ROUND)/((1-g.ROUND)*g.ROUND**2)
    for i,(a,b) in enumerate(zip((0.,1.,1+g.HEAD_L,2+g.HEAD_L),(1.,1+g.HEAD_L,2+g.HEAD_L,g.P))):
        take=(v>=a)&(v<b);x=v[take]-a
        if i%2:
            ks[take]=s5pp(np.minimum(x,g.HEAD_L-x)/g.HEAD_BLEND)/(g.HEAD_R*g.HEAD_BLEND**2)
        else:
            ks[take]=-(8*np.pi**2*g.DELTA*np.cos(2*np.pi*x)
                           +((g.A-g.DELTA+t)*cpp(x/g.RAMP)+(g.B-g.DELTA-t)*cpp((x-1+g.RAMP)/g.RAMP))/g.RAMP**3)
    return unary(s,k,kp,ks)

def track_law(s,t):
    x=np.mod(s.v,g.P/2)
    def cl(x):return unary(x,*g.clock(x.v))
    w=unary(s,x,1.,0.)
    return g.ANGLE*np.sin(t)*(cl(w/g.RAMP)-cl((w-1+g.RAMP)/g.RAMP))

def solve_jets(M,r):
    """Batched implicit linear solve for value and both s derivatives."""
    shape=np.broadcast_shapes(*(np.shape(z.v) for row in M for z in row),*(np.shape(z.v) for z in r))
    def v(x,part):return np.broadcast_to(getattr(x,part),shape)
    def A(part):return np.stack([np.stack([v(z,part) for z in row],-1) for row in M],-2)
    def b(part):return np.stack([v(z,part) for z in r],-1)
    def sol(z):return np.linalg.solve(A("v"),z[...,None])[...,0]
    y=sol(b("v"));yp=sol(b("s")-(A("s")@y[...,None])[...,0])
    ypp=sol(b("ss")-(A("ss")@y[...,None])[...,0]-2*(A("s")@yp[...,None])[...,0])
    return [J(y[...,i],s=yp[...,i],ss=ypp[...,i]) for i in range(3)]

def chebs(x,n):
    a=J(1.+0.*x.v);b=x;out=[]
    for i in range(n):
        out.append(b);a,b=b,2*x*b-a
    return out

def angles(s,side,t,design):
    # Parameter tuple (common yaw, bulk yaw, first/second/third odd amplitude, harmonic).
    c,d,f0,f1,f2,m=design
    px=2*np.pi*s/g.P;co,si=trig(m*px+side*.34)
    h=np.sin(t)
    return h*(c+.35*d*si),h*d*co,[h*f0*(1+.22*co),h*f1*(1+.2*si),h*f2*(co+side*.35)]

def tau(p,k):
    v=p*p*k
    return [J(1.+0.*p.v),p*entire(v,1),p*p*entire(v,2)]

def proj(ctl,f,order):
    x,w,_,_=rule(order);u=J(x);p,b=pulse(u)
    bx,bz,G=[spread(y) for y in ctl];k=bx*bx+bz*bz
    ts=tau(p,k);env=envelope(u,.006,.088,.008)
    weight=env*b*b*entire(G*b*b,1)
    pol=chebs(2*(2*u-1)*(2*u-1)-1,len(f))
    ff=sum((spread(y)*v for y,v in zip(f,pol)),J(0.))
    M=[[integrate(weight*z*j,w) for j in ts] for z in ts]
    rhs=[integrate(weight*ff*z,w) for z in ts]
    return solve_jets(M,rhs)

def norm_components(values):
    return cap.root(sum((x*x for x in values),J(0.)))

def raw(u,data,edge=True):
    bx,bz,G,n,T,k0,kt,delta,yaw,bulk,f,c=data
    p,b=pulse(u);gam=cap.root(G);q=gam*b;alpha=yaw+bulk*envelope(u,.22,.47,.09)
    if edge:
        wl=1-cap_s7(u/EDGE);wr=1-cap_s7((1-u)/EDGE)
        # The regularized quotient tends to k0/kt at a nonzero curvature
        # station and to one at a common zero. The exact edge value multiplies b(0)=0.
        den=kt*kt+u*u
        den=J(*(np.where(den.v==0.,1.,den.v) if j==0 else v for j,v in enumerate(den.parts())))
        lam=1+kt*(k0-kt)/den
        si=trig(cap.PRELOAD*b)[1]*lam
        # Arc-sine is needed only in the tiny incoming strip.
        x=unary(si,np.arcsin(np.clip(si.v,-.5,.5)),
                1/np.sqrt(1-np.clip(si.v,-.5,.5)**2),
                np.clip(si.v,-.5,.5)/(1-np.clip(si.v,-.5,.5)**2)**1.5)
        q=q+wl*(x-q)+wr*(cap.PRELOAD*b-q)
        alpha=(1-wl-wr)*alpha-wr*delta
    co,si=trig(alpha)
    ts=tau(p,bx*bx+bz*bz)
    env=envelope(u,.006,.088,.008)
    cc=chebs(2*(2*u-1)*(2*u-1)-1,len(f))
    residual=sum((a*v for a,v in zip(f,cc)),J(0.))-sum((a*v for a,v in zip(c,ts)),J(0.))
    scale=cap.root(1+2*len(f)*sum((a*a for a in f),J(0.))+6*sum((a*a for a in c),J(0.)))
    z=.89*env*b*residual/scale
    zco=cap.root(1-z*z)
    ca,sa=co*zco-si*z,si*zco+co*z
    cq,sq=trig(q)
    point=[sq*(-ca*n[0]+sa*T[0]),cq,sq*(-ca*n[1]+sa*T[1])]
    axis=[bz,0.*bx,-bx];cr=old.cross(axis,point);cc=old.cross(axis,cr)
    return [point[i]+ts[1]*cr[i]+ts[2]*cc[i] for i in range(3)]

def lift_tree(tree,fn):
    return [lift_tree(a,fn) for a in tree] if isinstance(tree,(list,tuple)) else fn(tree)

def anchor(u):return envelope(u,.44,.47,.01)

def jac(tan,a,w):
    v=[x+w*y for x,y in zip(tan,a)];r=norm_components(v);vv=[x/r for x in v]
    D=[[w*((1. if i==j else 0.)-vv[i]*vv[j])/r for j in range(3)] for i in range(3)]
    return vv,D

def correction(data,order):
    n,wt=g.old.rule(order)
    # The undisturbed moment, including the odd projected part, is exactly the prescribed chord.
    ue=J(np.r_[EDGE*n,1-EDGE*n]);we=np.r_[EDGE*wt,EDGE*wt]
    dd=lift_tree(data,spread);ta=raw(ue,dd);tb=raw(ue,dd,False)
    rhs=[integrate(x-y,we) for x,y in zip(tb,ta)]
    cuts=np.array([.44,.45,.46,.47,.53,.54,.55,.56])
    pairs=[(l,r) for l,r in zip(cuts[:-1],cuts[1:]) if r-l<.02]
    u=J(np.concatenate([l+(r-l)*n for l,r in pairs]));wu=np.concatenate([(r-l)*wt for l,r in pairs])
    t=raw(u,dd);weight=anchor(u);a=[0.*x for x in rhs]
    # Newton in the full jet algebra, including the implicit first/second material derivatives.
    for _ in range(4):
        now,D=jac(t,[spread(z) for z in a],weight)
        f=[r-integrate(y-x,wu) for r,x,y in zip(rhs,t,now)]
        M=[[integrate(z,wu) for z in row] for row in D]
        step=solve_jets(M,f);a=[x+y for x,y in zip(a,step)]
    return a

def local_data(s,side,t,design,order):
    th=g.ANGLE*np.sin(t);q,n,T=g.section(s,th,order);ctl=controls(s,t,order)
    yaw,bulk,f=angles(s,side,t,design);c=proj(ctl,f,order)
    data=[*ctl,n,T,kap(s,0.,order),kap(s,th,order),track_law(s,t),yaw,bulk,f,c]
    return q,data,correction(data,order)

def velocity(u,data,a):
    v=raw(u,data);w=anchor(u)
    r=[x+w*y for x,y in zip(v,a)];length=norm_components(r)
    return [x/length for x in r]

@lru_cache(maxsize=36)
def table(keys,side,t,design,order):
    s=np.frombuffer(keys,dtype="<f8")
    q,data,a=local_data(J(s,s=1.),side,t,design,order)
    knots=abscissae();n,wt=g.old.rule(order);h=np.diff(knots)
    u=J((knots[:-1,None]+h[:,None]*n).ravel())
    dd,aa=lift_tree([data,a],spread);V=velocity(u,dd,aa)
    tab=np.zeros((len(s),len(knots),3,3))
    for i,z in enumerate(V):
        for j,v in enumerate((z.v,z.s,z.ss)):
            arr=np.broadcast_to(v,(len(s),len(u.v))).reshape(len(s),len(h),order)
            tab[:,1:,i,j]=np.cumsum(L*h*(arr@wt),axis=1)
    return q,data,a,tab

def bridge(sv,bv,side,t,design,order):
    un,inv=np.unique(sv,return_inverse=True)
    q,data,a,tab=table(np.asarray(un,dtype="<f8").tobytes(),side,t,tuple(design),order)
    def repeat(z):return J(*(np.broadcast_to(x,un.shape)[inv] for x in z.parts()))
    q,data,a=lift_tree([q,data,a],repeat);u=J(bv/L,a=1/L)
    f=velocity(u,data,a);kn=abscissae()
    idx=np.clip(np.searchsorted(kn,u.v,side="right")-1,0,len(kn)-2);d=u.v-kn[idx]
    n,wt=g.old.rule(order);uv=J(kn[idx,None]+d[:,None]*n)
    dd,aa=lift_tree([data,a],spread);V=velocity(uv,dd,aa);rows=tab[inv,idx].copy()
    for i,z in enumerate(V):
        for j,v in enumerate((z.v,z.s,z.ss)):
            rows[:,i,j]+=L*d*(np.broadcast_to(v,uv.v.shape)@wt)
    start=[q[0],J(np.full(len(sv),Y)),q[1]];take=[]
    for i in range(3):
        z=J(start[i].v+rows[:,i,0],start[i].s+rows[:,i,1],f[i].v,start[i].ss+rows[:,i,2],f[i].s,f[i].a)
        take.append(-z if i==1 and side<0 else z)
    return gather(take,len(sv))

def initial_bridge(sv,bv,side,order):
    u=bv/L;kn=old.abscissae();n,wt=g.old.rule(order)
    def ints(v):
        p,b=old.pulse(J(v));a=cap.PRELOAD*b.v
        return np.cos(a)@wt,np.sin(a)@wt
    h=np.diff(kn);co,si=ints(kn[:-1,None]+h[:,None]*n)
    j=np.clip(np.searchsorted(kn,u,side="right")-1,0,len(h)-1);d=u-kn[j]
    x,z=ints(kn[j,None]+d[:,None]*n)
    p,b=old.pulse(J(u,a=1./L));c,ss=trig(cap.PRELOAD*b)
    y=J(L*(np.r_[0.,np.cumsum(h*co)][j]+d*x),a=c.v,aa=c.a)
    off=J(L*(np.r_[0.,np.cumsum(h*si)][j]+d*z),a=ss.v,aa=ss.a)
    q,n,T=g.section(J(sv,s=1.),0.,order)
    return gather((q[0]-off*n[0],side*(Y+y),q[1]-off*n[1]),len(sv))

def chart_jet(chart,u,v,phase=0.,order=12,design=(0.,0.,0.,0.,0.,1)):
    aa,bb=np.broadcast_arrays(np.asarray(u,float),np.asarray(v,float));sh=aa.shape
    s=aa.ravel();b=bb.ravel();t=float(phase);side=1 if chart.endswith("+") else -1
    basechart=chart.replace("end-outer","end")
    if not chart.startswith("end"):
        z=old.chart_jet(basechart,aa,bb,t,order)
        if chart.startswith("cap"):z[...,0,1]-=side*(SHORT-cap.SHORTEN)*np.sin(t)
        return z
    out=np.empty((len(s),6,3));inside=(b<=L) if "outer" not in chart else np.zeros_like(b,dtype=bool)
    ix=np.flatnonzero(inside)
    if len(ix):
        labels,rev=np.unique(s[ix],return_inverse=True)
        for start in range(0,len(labels),24):
            sel=ix[(rev>=start)&(rev<start+24)]
            out[sel]=bridge(s[sel],b[sel],side,t,design,order) if t else initial_bridge(s[sel],b[sel],side,order)
    ix=np.flatnonzero(~inside)
    if len(ix):
        _,y,shift=desired(J(s[ix]),t,order);q,n,T=g.section(J(s[ix],s=1.),0.,order)
        p,d=g.smooth_curve(J(b[ix]-L,a=1.),cap.OUTER_L,cap.OUTER_R,cap.OUTER_BLEND,order)
        out[ix]=gather((q[0]-d*n[0]+shift[0],side*(Y+L*y+p),q[1]-d*n[1]+shift[1]),len(ix))
    return out.reshape(sh+(6,3))
