"""R759 paired material tracks with a fixed right grip, two full rolls and two movable caps.
Public Actions evaluate the complete initial R757 metric and every physical two-jet.
"""
from functools import lru_cache
import numpy as np
import r757_curved_rectifying_closed_two_jets as base
from r742_tilted_disk_two_jets import J,unary,gather,cap_s7
delay=base.delay;g=base.OLD
TRACK=1.30
NCELL=11
ELL=TRACK/NCELL
EDGE=.025

def ramp(t):
    x=np.clip(t,0.,1.)
    return x**3*(10+x*(-15+6*x)),30*x*x*(1-x)**2

def iramp(t):
    x=np.clip(t,0.,1.)
    return x**4*(2.5-3*x+x*x)+np.maximum(t-1.,0.)

def subcell(t):
    v=np.zeros_like(t);d=v.copy();dd=v.copy()
    for a,b in ((0.,1/3),(2/3,1.)):
        # Positive plateau supported only where the original signed curvature is negative.
        x=(t-a)/EDGE;y=(t-(b-EDGE))/EDGE
        u,up=ramp(x);w,wp=ramp(y)
        v+=EDGE*(iramp(x)-iramp(y));d+=u-w;dd+=(up-wp)/EDGE
    return v,d,dd

def heading(x,angle,nr):
    # x is the original arclength from the upper-left track endpoint.
    x=np.clip(np.asarray(x,float),0.,TRACK)
    w=np.minimum(x,TRACK-x)/ELL
    k=np.floor(w).astype(int);frac=np.clip(w-k,0.,1.)
    v,d,dd=subcell(frac);m=2*(1/3-EDGE)
    live=w<nr
    f=np.where(live,(k+v/m)/nr,1.)
    sgn=np.where(x<TRACK/2,1.,-1.)
    return (angle*f,np.where(live,angle*sgn*d/(nr*m*ELL),0.),
            np.where(live,angle*dd/(nr*m*ELL**2),0.))

def offsets(x,angle,nr):
    # Delta derivatives in the OLD x-material label on the upper track.
    xx=np.clip(np.asarray(x,float),0.,TRACK);cell=np.minimum(np.floor(xx/ELL),NCELL-1)
    t=xx/ELL-cell;f1=g.BOW*ELL*g.shape(t,1);f2=g.BOW*g.shape(t,2)
    p,pp,_=heading(xx,angle,nr);co=np.cos(p);si=np.sin(p)
    delta1=np.stack((co-1-si*f1,si+(co-1)*f1),axis=-1)
    delta2=np.stack((-pp*(si+co*f1)-si*f2,pp*(co-si*f1)+(co-1)*f2),axis=-1)
    return delta1,delta2

@lru_cache(maxsize=96)
def integration(angle,nr,order):
    grid=np.unique(np.clip((np.arange(NCELL)[:,None]+np.array([0.,EDGE,1/3-EDGE,
             1/3,.5,2/3,2/3+EDGE,1-EDGE,1.]))*ELL,0.,TRACK))
    grid[0]=0.;grid[-1]=TRACK
    nodes,weights=g.disk.rule(order)
    h=np.diff(grid);xx=grid[:-1,None]+h[:,None]*nodes
    vals=offsets(xx,angle,nr)[0]
    integ=h[:,None]*np.einsum("nrc,r->nc",vals,weights)
    return grid,np.vstack((np.zeros(2),np.cumsum(integ,axis=0)))

def displacement(x,angle,nr,order):
    sh=np.shape(x);xx=np.clip(np.asarray(x).ravel(),0.,TRACK)
    grid,tab=integration(angle,nr,order);ids=np.clip(np.searchsorted(grid,xx,side="right")-1,0,len(grid)-2)
    nodes,weights=g.disk.rule(order);h=xx-grid[ids];yy=grid[ids,None]+h[:,None]*nodes
    val=tab[ids]+h[:,None]*np.einsum("nrc,r->nc",offsets(yy,angle,nr)[0],weights)
    return val.reshape(sh+(2,))

def coords(s,angle,nr,order):
    sh,old,live,ell,terms=g.local(s,order)
    lh,u0,u1,rt,half,*_=g.original.profile_constants(order);P=2*half
    a=old%P;bot=P-(u0+TRACK);top=(a>=u0)&(a<=u0+TRACK);low=(a>=bot)&(a<=bot+TRACK)
    tot=integration(angle,nr,order)[1][-1]
    left=(a<u0)|(a>bot+TRACK)
    Q,T,N,K,Kp=g.profile_coordinates(s,order)
    Q=Q.reshape(-1,2).copy();T=T.reshape(-1,2).copy();K=K.ravel().copy();Kp=Kp.ravel().copy()
    Q[left]-=tot
    for mask,x,sg in ((top,a-u0,1),(low,a-bot,-1)):
        if not np.any(mask):continue
        xx=x[mask];f1=terms[1][mask];f2=terms[2][mask]
        # On the reflected lower track old f' is differentiated in its increasing arclength.
        ang,d1,d2=heading(xx,angle,nr);speed=np.sqrt(1+f1*f1)
        aa=d1/speed;aaa=d2/(speed**2)-d1*f1*f2/speed**4
        DD=displacement(xx,angle,nr,order)
        Q[mask]+=DD-tot if sg==1 else -DD
        t=T[mask].copy();co=np.cos(ang);si=np.sin(ang)
        T[mask]=np.column_stack((co*t[:,0]-si*t[:,1],si*t[:,0]+co*t[:,1]))
        K[mask]-=aa;Kp[mask]-=aaa
    N=np.column_stack((-T[:,1],T[:,0]))
    return Q.reshape(sh+(2,)),T.reshape(sh+(2,)),N.reshape(sh+(2,)),K.reshape(sh),Kp.reshape(sh)

def profile(s,angle,nr,order):
    p,t,n,k,kp=coords(s.v,angle,nr,order)
    return ([unary(s,p[:,i],t[:,i],-k*n[:,i]) for i in range(2)],
            [unary(s,n[:,i],k*t[:,i],kp*t[:,i]-k*k*n[:,i]) for i in range(2)])

def pairpose(x,y,z,pose,t):
    if not any(pose):return x,y,z
    vec=np.asarray(pose[:3]);mag=np.linalg.norm(vec)
    P=(x-g.CENTER_X,y,z)
    if mag:
        a,b,c=vec/mag
        def cross(V):return (b*V[2]-c*V[1],c*V[0]-a*V[2],a*V[1]-b*V[0])
        v=cross(P);w=cross(v)
        P=tuple(pp+np.sin(t*mag)*vv+2*np.sin(t*mag/2)**2*ww for pp,vv,ww in zip(P,v,w))
    return P[0]+g.CENTER_X+t*pose[3],P[1]+t*pose[4],P[2]+t*pose[5]

def strip_map(X,Z,angle,nr,order):
    """Map the entire true fixed planar cap strip between its two terminal curves."""
    _,db=delay.end_limits(order);tot=integration(angle,nr,order)[1][-1]
    take=(X.v>=-1.)&(X.v<=.30)
    # Invert the common terminal x = -1+t+db f'/sqrt(1+f'^2).
    xx=np.clip(X.v+1.,0.,TRACK)
    for _ in range(8):
        t=xx/ELL-np.minimum(np.floor(xx/ELL),NCELL-1)
        fp=g.BOW*ELL*g.shape(t,1);fpp=g.BOW*g.shape(t,2);spd=np.sqrt(1+fp*fp)
        d=1+db*fpp/spd**3
        err=xx+db*fp/spd-np.clip(X.v+1.,0.,TRACK)
        xx=np.clip(xx-err/d,0.,TRACK)
    t=xx/ELL-np.minimum(np.floor(xx/ELL),NCELL-1)
    fp=g.BOW*ELL*g.shape(t,1);fpp=g.BOW*g.shape(t,2);f3=g.BOW*g.shape(t,3)/ELL
    sp=np.sqrt(1+fp*fp);d=1+db*fpp/sp**3
    d2=db*(f3/sp**3-3*fp*fpp*fpp/sp**5)
    old=unary(X,xx,np.where(take,1/d,0.),np.where(take,-d2/d**3,0.))
    m0=g.original.profile_constants(order)[1];period=2*g.original.profile_constants(order)[4]
    o=old.v
    def label(center,si):
        a=center+si*o
        return unary(old,g.forward(a,order),si*sp,si*fp*fpp/sp)
    st=label(m0,1.);sb=label(period-m0,-1.)
    qt,nt=profile(st,angle,nr,order);qb,nb=profile(sb,angle,nr,order)
    rho=g.BOW*ELL**2*g.shape(t,0)+.17-db/sp
    hp=fp+db*fp*fpp/sp**3
    hpp=fpp+db*((fpp*fpp+fp*f3)/sp**3-3*(fp*fpp)**2/sp**5)
    half=unary(old,rho,hp,hpp)
    lam=(1+Z/half)*.5
    cand=[lam*(qt[i]-db*nt[i])+(1-lam)*(qb[i]-db*nb[i]) for i in range(2)]
    # The exterior head pieces are respectively a rigid translation and identity.
    ret=[]
    for i,v in enumerate((X,Z)):
        move=np.where(X.v< -1.,-tot[i],0.);ex=v+move
        ret.append(J(*[np.where(take,p,q) for p,q in zip(cand[i].parts(),ex.parts())]))
    return ret

def field(chart,s,v,phase,amplitude,nr,pose,order=32):
    a=J(np.asarray(s,float).ravel(),s=1.);b=J(np.asarray(v,float).ravel(),a=1.)
    if phase==0.:
        return delay.chart_jet(chart,a.v,b.v,0.,order=order,bend=0.,rotate=False)
    angle=float(amplitude*np.sin(phase));time=np.sin(phase)
    sg=1 if chart.endswith("+") else -1
    if chart=="cylinder":
        q,n=profile(a,angle,nr,order);x,z=q;y=b
    elif chart.startswith("end"):
        q,n=profile(a,angle,nr,order);p,d=delay.end_offsets(b,order)
        x,z=[q[i]-d*n[i] for i in range(2)];y=sg*(delay.HALF_WIDTH+p)
        wt=cap_s7(b/delay.END_LENGTH)
        xp,yp,zp=pairpose(x,0.*x,z,pose,time)
        x,y,z=x+wt*(xp-x),y+wt*yp,z+wt*(zp-z)
    else:
        X,y0,Z=delay.sphere_chart(chart,a,b,np.zeros_like(a.v),order,"legacy")
        x,z=strip_map(X,Z,angle,nr,order)
        if "cartesian" not in chart:
            w=b if "normal" in chart else 1-b
            d,rho=delay.cap_leaf(w,order);d=d+delay.end_limits(order)[1]-g.original.end_limits(order)[1]
            q,n=profile(a,angle,nr,order)
            tx=g.CENTER_X+rho*(q[0]-d*n[0]-g.CENTER_X);tz=rho*(q[1]-d*n[1])
            gate=1-cap_s7(w/.03)
            x,z=x+gate*(tx-x),z+gate*(tz-z)
        yb=sg*(delay.HALF_WIDTH+delay.end_limits(order)[0])
        x,yy,z=pairpose(x,y0-yb,z,pose,time);y=yb+yy
    return gather((x,y,z),len(a.v))
