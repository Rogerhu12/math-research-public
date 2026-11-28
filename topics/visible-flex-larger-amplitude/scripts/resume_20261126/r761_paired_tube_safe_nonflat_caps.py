"""R761. Embedded paired-profile cap transport and genuine moving nonflat graphs.
chart_jet returns the physical material six-jet. All computations run on public Actions.
"""
from functools import lru_cache
import numpy as np
from scipy.integrate import solve_ivp
from scipy.spatial import cKDTree
import r759_paired_curvature_tracks as tr
from r742_tilted_disk_two_jets import J,unary,cap_s7,gather
g=tr.g;D=tr.delay
FLOW_BAND=.00035
HEIGHT_BAND=.00025

def response_integrand(x,theta,nr):
    p=tr.heading(x,1.,nr)[0];t=x/tr.ELL-np.minimum(np.floor(x/tr.ELL),tr.NCELL-1)
    fp=g.BOW*tr.ELL*g.shape(t,1);co=np.cos(theta*p);si=np.sin(theta*p)
    return np.stack((-p*(si+co*fp),p*(co-si*fp)),axis=-1)

@lru_cache(maxsize=96)
def response_integral(theta,nr,order):
    grid=tr.integration(theta,nr,order)[0]
    n,w=g.disk.rule(order);h=np.diff(grid)
    val=response_integrand(grid[:-1,None]+h[:,None]*n,theta,nr)
    return grid,np.vstack((np.zeros(2),np.cumsum(h[:,None]*np.einsum("nrc,r->nc",val,w),axis=0)))

def response(x,theta,nr,order):
    xx=np.clip(np.asarray(x).ravel(),0,tr.TRACK);grid,y=response_integral(theta,nr,order)
    i=np.clip(np.searchsorted(grid,xx,side="right")-1,0,len(grid)-2)
    n,w=g.disk.rule(order);h=xx-grid[i]
    return y[i]+h[:,None]*np.einsum("nrc,r->nc",response_integrand(grid[i,None]+h[:,None]*n,theta,nr),w)

def profile(s,theta,nr,order,velocity=False):
    if not velocity:return tr.profile(s,theta,nr,order)
    _,old,_,_,terms=g.local(s.v,order)
    _,m0,_,_,half,*_=g.original.profile_constants(order)
    P=2*half;a=old%P;lo=P-m0-tr.TRACK
    q,T,N,K,Kp=tr.coords(s.v,theta,nr,order)
    A=np.zeros(len(a));As=A.copy();Ass=A.copy();V=np.zeros_like(q)
    total=response_integral(theta,nr,order)[1][-1]
    V[(a<m0)|(a>lo+tr.TRACK)]=-total
    for start,sign in ((m0,1),(lo,-1)):
        take=(a>=start)&(a<=start+tr.TRACK);x=a[take]-start
        if not len(x):continue
        ang,ap,app=tr.heading(x,1.,nr)
        f1=terms[1][take];f2=terms[2][take];speed=np.sqrt(1+f1*f1)
        A[take]=ang;As[take]=ap/speed;Ass[take]=app/speed**2-ap*f1*f2/speed**4
        val=response(x,theta,nr,order)
        V[take]=val-total if sign==1 else -val
    Tt=A[:,None]*N;Nt=-A[:,None]*T;Kt=-As;Kst=-Ass
    Vss=-Kt[:,None]*N-K[:,None]*Nt
    Ns=Kt[:,None]*T+K[:,None]*Tt
    Nss=Kst[:,None]*T+Kp[:,None]*Tt-2*(K*Kt)[:,None]*N-(K*K)[:,None]*Nt
    return ([unary(s,V[:,i],Tt[:,i],Vss[:,i]) for i in range(2)],
            [unary(s,Nt[:,i],Ns[:,i],Nss[:,i]) for i in range(2)])

def normal(s,w,theta,nr,order,velocity=False):
    q,n=profile(s,theta,nr,order,velocity)
    dt=D.end_limits(order)[1]+w
    return tuple(q[i]-dt*n[i] for i in range(2))

def planar(X,Z,theta,nr,order,velocity=False):
    if not velocity:return tr.strip_map(X,Z,theta,nr,order)
    _,db=D.end_limits(order)
    take=(X.v>=-1.)&(X.v<=.30);xx=np.clip(X.v+1.,0.,tr.TRACK)
    for _ in range(8):
        t=xx/tr.ELL-np.minimum(np.floor(xx/tr.ELL),10)
        fp=g.BOW*tr.ELL*g.shape(t,1);fpp=g.BOW*g.shape(t,2);sp=np.sqrt(1+fp*fp)
        jac=1+db*fpp/sp**3
        xx=np.clip(xx-(xx+db*fp/sp-np.clip(X.v+1,0,tr.TRACK))/jac,0,tr.TRACK)
    t=xx/tr.ELL-np.minimum(np.floor(xx/tr.ELL),10)
    fp=g.BOW*tr.ELL*g.shape(t,1);fpp=g.BOW*g.shape(t,2);f3=g.BOW*g.shape(t,3)/tr.ELL
    sp=np.sqrt(1+fp*fp);jac=1+db*fpp/sp**3
    j2=db*(f3/sp**3-3*fp*fpp*fpp/sp**5)
    u=unary(X,xx,np.where(take,1/jac,0.),np.where(take,-j2/jac**3,0.))
    _,m0,_,_,half,*_=g.original.profile_constants(order)
    qa,na=profile(unary(u,g.forward(m0+xx,order),sp,fp*fpp/sp),theta,nr,order,True)
    qb,nb=profile(unary(u,g.forward(2*half-m0-xx,order),-sp,-fp*fpp/sp),theta,nr,order,True)
    hh=.17+g.BOW*tr.ELL**2*g.shape(t,0)-db/sp
    hp=fp+db*fp*fpp/sp**3;hpp=fpp+db*((fpp**2+fp*f3)/sp**3-3*(fp*fpp)**2/sp**5)
    L=(1+Z/unary(u,hh,hp,hpp))*.5
    total=response_integral(theta,nr,order)[1][-1]
    out=[]
    for i in range(2):
        val=L*(qa[i]-db*na[i])+(1-L)*(qb[i]-db*nb[i])
        rest=J(np.where(X.v< -1.,-total[i],0.))
        out.append(J(*(np.where(take,a,b) for a,b in zip(val.parts(),rest.parts()))))
    return tuple(out)

def solve2(f,h,fx,hx):
    det=f.s*h.a-f.a*h.s
    if np.any(abs(det)<1.e-11):raise ArithmeticError("nonregular collar-coordinate inversion")
    return (h.a*fx-f.a*hx)/det,(-h.s*fx+f.s*hx)/det

def inverse(fn,X,Z,start,width):
    s=np.asarray(start,float).copy();w=np.array(width,dtype=float,copy=True)
    for _ in range(10):
        f,h=fn(J(s,s=1.),J(w,a=1.))
        ds,dw=solve2(f,h,f.v-X.v,h.v-Z.v);s-=ds;w-=dw
        if max(np.max(abs(ds)),np.max(abs(dw)))<8.e-14:break
    f,h=fn(J(s,s=1.),J(w,a=1.))
    if max(np.max(abs(f.v-X.v)),np.max(abs(h.v-Z.v)))>3.e-10:
        raise ArithmeticError("collar coordinate inversion residual")
    si,wi=solve2(f,h,X.s,Z.s);sj,wj=solve2(f,h,X.a,Z.a)
    def second(ij,kl,xx,zz):
        a,b=ij;c,d=kl
        u=f.ss*a*c+f.sa*(a*d+b*c)+f.aa*b*d
        v=h.ss*a*c+h.sa*(a*d+b*c)+h.aa*b*d
        return solve2(f,h,xx-u,zz-v)
    p,q=second((si,wi),(si,wi),X.ss,Z.ss);r,t=second((si,wi),(sj,wj),X.sa,Z.sa)
    u,v=second((sj,wj),(sj,wj),X.aa,Z.aa)
    return J(s,si,sj,p,r,u),J(w,wi,wj,q,t,v)

def packed(v):
    a,b=v
    return np.stack(np.broadcast_arrays(*a.parts(),*b.parts())).reshape(12,-1)

@lru_cache(maxsize=12)
def tree(theta,nr,order):
    P=2*g.profile_constants(order)[4];s=np.arange(32768)*P/32768
    x,z=normal(J(s),J(0.),theta,nr,order)
    return cKDTree(np.c_[x.v,z.v]),s

def nearest(X,Z,theta,nr,order):
    kd,grid=tree(theta,nr,order)
    dist,i=kd.query(np.c_[X.v,Z.v]);return dist,grid[i]

def cut(x,mask):
    return J(*(np.broadcast_to(a,np.shape(x.v))[mask] for a in x.parts()))

def replace(x,mask,y):
    vals=[]
    for a,b in zip(x.parts(),y.parts()):
        z=np.broadcast_to(a,np.shape(x.v)).copy();z[mask]=b;vals.append(z)
    return J(*vals)

def move(X,Z,theta,nr,order):
    direct=planar(X,Z,theta,nr,order)
    dist,s=nearest(X,Z,0.,nr,order);near=dist<FLOW_BAND+.00050
    if not np.any(near):return direct
    ix=np.flatnonzero(near)
    a,w=inverse(lambda a,b:normal(a,b,0.,nr,order),cut(X,ix),cut(Z,ix),s[ix],s[ix]*0)
    live=w.v<FLOW_BAND;ix=ix[live]
    if not len(ix):return direct
    s0=a.v[live];w0=w.v[live];state=packed((cut(X,ix),cut(Z,ix)))
    def rhs(t,state):
        rows=state.reshape(12,-1);x=J(*rows[:6]);z=J(*rows[6:])
        def mapped(a,w):
            q=normal(a,w,0.,nr,order)
            return planar(*q,t,nr,order)
        aa,ww=inverse(mapped,x,z,s0,w0)
        ix0=normal(aa,ww,0.,nr,order)
        vb=planar(*ix0,t,nr,order,velocity=True)
        bb,dd=inverse(lambda a,w:normal(a,w,t,nr,order),x,z,aa.v,ww.v)
        vc=normal(bb,dd,t,nr,order,velocity=True)
        weight=1-cap_s7((ww-FLOW_BAND*.35)/(FLOW_BAND*.65))
        vel=[v+weight*(r-v) for v,r in zip(vb,vc)]
        return packed(vel).ravel()
    sol=solve_ivp(rhs,(0.,theta),state.ravel(),method="DOP853",rtol=2.e-9,atol=2.e-11)
    if not sol.success:raise ArithmeticError(sol.message)
    rr=sol.y[:,-1].reshape(12,-1)
    return replace(direct[0],ix,J(*rr[:6])),replace(direct[1],ix,J(*rr[6:]))

def crown(P,theta,nr,order):
    x,z=P
    dist,start=nearest(x,z,theta,nr,order)
    ids=np.flatnonzero(dist<HEIGHT_BAND+.00050)
    gate=J(np.ones(len(x.v)))
    if len(ids):
        _,ww=inverse(lambda a,b:normal(a,b,theta,nr,order),cut(x,ids),cut(z,ids),start[ids],start[ids]*0)
        gate=replace(gate,ids,cap_s7(ww/HEIGHT_BAND))
    # Median point integrates the rotated horizontal direction, without the corrugation f'.
    n,wt=g.disk.rule(order);grid=tr.integration(theta,nr,order)[0];h=np.diff(grid)
    mask=grid[:-1]>=tr.TRACK/2-1.e-14
    h=h[mask];u=grid[:-1][mask,None]+h[:,None]*n
    ang=tr.heading(u,theta,nr)[0]
    center=(.30-np.sum(h*(np.cos(ang)@wt)),-np.sum(h*(np.sin(ang)@wt)))
    radius=.12*np.cos(theta)-.08
    H=1-((x-center[0])*(x-center[0])+(z-center[1])*(z-center[1]))/(radius*radius)
    val=np.maximum(H.v,0.)
    return 1.e-8*(.1+.1*((x-g.CENTER_X)*(x-g.CENTER_X)+z*z))*gate+(.00035*(radius/.04)**2)*unary(H,val**4,4*val**3,12*val*val)

def chart_jet(chart,u,v,phase=0.,amplitude=.78,ramp_cells=2,order=32):
    g.disk._public()
    a,b=np.broadcast_arrays(np.asarray(u,float),np.asarray(v,float));sh=a.shape
    if not (0<=phase<=np.pi/2+2.e-14 and 0<=amplitude<=.81 and ramp_cells in (2,3)):
        raise ValueError("paired phase/amplitude/ramp outside R761")
    a=a.ravel();b=b.ravel()
    if not phase or not amplitude:
        return D.chart_jet(chart,a,b,0.,order=order,bend=0.,rotate=False).reshape(sh+(6,3))
    if chart=="cylinder" or chart.startswith("end"):
        return tr.field(chart,a,b,phase,amplitude,ramp_cells,(0.,)*6,order).reshape(sh+(6,3))
    X,_,Z=D.sphere_chart(chart,J(a,s=1.),J(b,a=1.),np.zeros(len(a)),order,"legacy")
    theta=amplitude*np.sin(phase);out=[]
    for lo in range(0,len(a),32):
        ii=np.arange(lo,min(len(a),lo+32));P=move(cut(X,ii),cut(Z,ii),theta,ramp_cells,order)
        sg=1 if chart.endswith("+") else -1
        y=sg*(D.HALF_WIDTH+D.end_limits(order)[0]+crown(P,theta,ramp_cells,order))
        out.append(gather((P[0],y,P[1]),len(ii)))
    return np.concatenate(out).reshape(sh+(6,3))
