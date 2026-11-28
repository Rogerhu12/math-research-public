"""One broad physical normal swing per true R776 corner with its exact terminal chord."""
from functools import lru_cache
from math import factorial
import numpy as np
import r778_normal_periodic_closed_corrugation as corr
from r742_tilted_disk_two_jets import J,unary,gather,trig

a,g=corr.a,corr.g
WIDTH=.10

def pulse(d):
    z=d/g.QUARTER
    h=np.minimum(z,1-z)
    p,dp,_=g.guard.clock(h/WIDTH)
    r,dr,_=g.guard.clock((.5-h)/WIDTH)
    return np.where(z<.5,1.,-1.)*p*r,(dp*r-p*dr)/(WIDTH*g.QUARTER)

@lru_cache(maxsize=16)
def constants(order):
    w=WIDTH;u=g.guard.ROUND*w
    pos=np.array([0.,u,w-u,w,.5-w,.5-w+u,.5-u,.5])
    cut=np.unique(np.r_[g.QUARTER*pos,g.QUARTER*(1-pos),g.SM,g.QUARTER-g.SM])
    cut.sort();nodes,weights=g.rule(order);ds=np.diff(cut)
    x=(cut[:-1,None]+ds[:,None]*nodes).ravel();wt=(ds[:,None]*weights).ravel()
    th,k,_=a.bend(x);b,_=pulse(x)
    coeff=[]
    for power in range(1,34):
        if power%2:
            multiplier=(-1.)**((power-1)//2+1)*np.sin(th-np.pi/4)
        else:
            multiplier=(-1.)**(power//2+1)*np.cos(th-np.pi/4)
        v=(wt*multiplier)*(b**power)/float(factorial(power))
        coeff.append((np.sum(v),np.sum(k*v)))
    return cut,coeff

def gain(z0,delta,cq,order):
    coeff=constants(order)[1]
    def equation(h,z,d,c):
        y=h*d
        # Integrate the lost chord divided by delta, using its regular positive gain.
        r=0.
        for i in range(len(coeff)-1,-1,-1):
            f,k=coeff[i]
            term=f-z*k
            r=r*y+(term*c if not i%2 else term)
        return h*r-np.sqrt(2.)
    lo=np.zeros_like(z0.v)
    hi=np.minimum(512.,np.pi/(2*np.maximum(delta.v,1.e-300)))
    for _ in range(50):
        m=(lo+hi)*.5
        positive=equation(m,z0.v,delta.v,cq.v)>0
        lo,hi=np.where(positive,lo,m),np.where(positive,m,hi)
    hv=(lo+hi)*.5
    eq=equation(J(hv,s=1.),z0,delta,cq)
    dx=-eq.a/eq.s;dxx=-(eq.aa+2*eq.sa*dx+eq.ss*dx*dx)/eq.s
    return delta*J(hv,a=dx,aa=dxx)

def delta_tangent(s,rot,z0,dz,angle,cq,sq):
    al,k,kp=a.bend(s.v)
    cs,ss=trig(unary(s,rot+al,k,kp))
    zz=np.clip(np.minimum(s.v,g.QUARTER-s.v)/g.SM,0.,1.)
    kpp=60*zz*(1-zz)*(1-2*zz)/(g.R*g.SM*g.SM)
    K=unary(s,k,kp,kpp)
    b,db=pulse(s.v)
    c,v=trig(angle*unary(s,b,db,0.))
    w=1-z0*K;pt=w*(c-1)+K*dz;pn=w*v*cq
    return [pt*cs+pn*ss,w*v*sq,-pt*ss+pn*cs]

def add_corner(e,z0,dz,ang,cq,sq,order):
    q=np.mod(e.v,g.P);quad=np.floor(q/g.BLOCK).astype(int)
    d=np.clip(q-quad*g.BLOCK-g.FLAT,0.,g.QUARTER)
    cuts,_=constants(order);nodes,w=g.rule(order)
    def col(j):
        return J(j.v[:,None],a=np.broadcast_to(j.a,j.v.shape)[:,None],
                 aa=np.broadcast_to(j.aa,j.v.shape)[:,None])
    vv=[col(j) for j in (z0,dz,ang,cq,sq)]
    sums=np.zeros((3,3,len(q)))
    for left,right in zip(cuts[:-1],cuts[1:]):
        h=np.clip(d-left,0.,right-left)
        vals=delta_tangent(J(left+h[:,None]*nodes),quad[:,None]*np.pi/2,*vv)
        for i,v in enumerate(vals):
            for r,z in enumerate((v.v,v.a,v.aa)):
                sums[i,r]+=h*(np.broadcast_to(z,(len(q),order))@w)
    edge=delta_tangent(J(d,s=1.),quad*np.pi/2,z0,dz,ang,cq,sq)
    return [J(V[0],h.v,V[1],h.s,h.a,V[2]) for V,h in zip(sums,edge)]

def chart_jet(chart,u,v,phase=0.,order=20):
    f=a.chart_jet(chart,u,v,phase,order)
    if chart!="cylinder" or phase==0.:return f
    aa,bb=np.broadcast_arrays(np.asarray(u,float),np.asarray(v,float))
    out=f.reshape(-1,6,3).copy()
    for j in range(0,len(out),160):
        sl=slice(j,j+160);e=J(aa.ravel()[sl],s=1.);x=J(bb.ravel()[sl]+.5,a=1.)
        _,z0,dz=a.axial(x,float(phase),order)
        cq,sq=trig(corr.wave_jet(x,phase))
        ang=gain(z0,dz,cq,order)
        out[sl]+=gather(add_corner(e,z0,dz,ang,cq,sq,order),len(e.v))
    return out.reshape(f.shape)
