#!/usr/bin/env python3
"""R792 true position and six differentiated jets. Complete original center, two rolls and both cap disks."""
import numpy as np
from scipy.interpolate import BPoly
import r792_full_width_rectifying_center_shooting as rib
from r742_tilted_disk_two_jets import J,unary,cap_s7,gather
g=rib.g

def spline(p,j):
    a,b,c=(p(j.v,i) for i in range(3))
    if a.ndim==np.ndim(j.v):return unary(j,a,b,c)
    return tuple(unary(j,x,y,z) for x,y,z in zip(a.T,b.T,c.T))

def physical(x,a):return BPoly.from_derivatives(x,list(zip(*a)))

class Strip:
    def __init__(self,arc,x,ph):
        self.arc=arc;self.ph=ph;c=arc.ctrl;rr=arc.r;self.x=x
        R,d=arc.integrate(x)
        k,e,_,_=arc.curvatures(rr,arc.k0,x)
        aw,ew,_=c.words(x);ep=c.db(rr)@ew;epp=c.db2(rr)@ew
        t=np.einsum("ijk,ik->ij",R,arc.t0);n=np.einsum("ijk,ik->ij",R,arc.n0);b=R[:,:,1]
        from scipy.interpolate import BSpline
        self.eta=BSpline(c.b.t,c.b.c@ew,c.b.k,extrapolate=False)
        self.gamma=physical(rr,[arc.r0+d,t,k[:,None]*n])
        self.zero=physical(rr,[arc.r0,arc.t0,arc.k0[:,None]*arc.n0])
        self.ruler=physical(rr,[b+e[:,None]*t,ep[:,None]*t,epp[:,None]*t+(ep*k)[:,None]*n])
        goal=arc.goal(ph);self.incoming=np.zeros(3) if arc.side==0 else -goal
        # At each real end eta and its first two derivatives vanish on an open subinterval.
        # Cancel actual end values and TWO derivatives of both the constant and y-linear coefficients.
        length=arc.length;rp=np.array([0.,.24*length,.76*length,length]);z=np.zeros((3,3))
        fix0=[];fix1=[]
        for r,des in ((0.,np.zeros(3)),(length,goal)):
            aa=np.stack([self.zero(r,i)-self.gamma(r,i) for i in range(3)]);aa[0]+=des
            bb=-np.stack([self.ruler(r,i) for i in range(3)]);bb[0]+=rib.Y
            fix0.append(aa);fix1.append(bb)
        self.fix0=BPoly.from_derivatives(rp,[fix0[0],z,z,fix0[1]])
        self.fix1=BPoly.from_derivatives(rp,[fix1[0],z,z,fix1[1]])
        self.ext=min(.08,(1-g.B*c.bound(x))/(2*(1+c.bound(x))))
        self.prices={"endpoint_position_defect":np.linalg.norm(d[-1]-goal),"endpoint_rotation_frobenius":np.linalg.norm(R[-1]-rib.I),
                     "end_six_jet_affine_repair_max":float(np.max(abs(np.stack([fix0,fix1])))),
                     "maximum_eta_derivative_hull":c.bound(x),"full_width_D_lower":1-g.B*c.bound(x),
                     "actual_initial_arc_length":arc.length,"outward_extension":self.ext,
                     "arc_map_derivative_Bernstein_min":float(np.min(arc.rmap.derivative().c))}
    def correction(self,s,y):
        S=spline(self.arc.rmap,s)
        low=np.zeros_like(S.v);high=low+self.arc.length
        # The global derivative certificate gives unique roots for the entire registered width.
        r=np.clip(S.v,0,self.arc.length)
        for _ in range(7):
            e=self.eta(r);f=r+y.v*e-S.v;d=1+y.v*self.eta(r,1)
            low=np.where(f<0,r,low);high=np.where(f>0,r,high)
            h=r-f/d;r=np.where((h>=low)&(h<=high),h,(low+high)/2)
        mask=np.abs(r+y.v*self.eta(r)-S.v)>3e-14
        if np.any(mask):
            a,b=low[mask],high[mask];sv=S.v[mask];yv=y.v[mask]
            for _ in range(52):
                h=(a+b)/2;v=h+yv*self.eta(h)-sv
                a=np.where(v<0,h,a);b=np.where(v>=0,h,b)
            r[mask]=(a+b)/2
        e=self.eta(r);ep=self.eta(r,1);epp=self.eta(r,2);D=1+y.v*ep
        rs=(S.s-y.s*e)/D;ra=(S.a-y.a*e)/D
        def second(q,z,dt,du,yt,yu):
            return (q-z*e-ep*(yt*du+yu*dt)-y.v*epp*dt*du)/D
        R=J(r,rs,ra,second(S.ss,y.ss,rs,rs,y.s,y.s),second(S.sa,y.sa,rs,ra,y.s,y.a),second(S.aa,y.aa,ra,ra,y.a,y.a))
        p=spline(self.gamma,R);q=spline(self.zero,S);h=spline(self.ruler,R)
        a=spline(self.fix0,S);b=spline(self.fix1,S)
        return tuple(p[i]-q[i]+y*(h[i]-rib.Y[i])+a[i]+y*b[i]+self.incoming[i] for i in range(3))

class Sphere:
    def __init__(self,arcs,word,ph,order):
        self.ph=ph;self.o=order;self.arcs=arcs;self.strips=[Strip(z,x,ph) for z,x in zip(arcs,word)]
    def delta(self,s,y,strip):
        q,_=g.wall.parts(s,self.o);X0,G0,_,_=g.profile(q[0],0.,self.o)
        Xt,Gt,_,_=g.profile(q[0],self.ph,self.o);lo=g.lower_weight(q[1]);dy,dz=g.pose(self.ph,self.o)[4:6]
        v=strip.correction(s,y)
        return v[0]+X0-Xt,v[1]-dy*lo,v[2]+G0-Gt-dz*lo
    def evaluate(self,chart,a,b):
        rv=g.chart_jet(chart,a,b,self.ph,self.o)
        if not self.ph or chart.startswith("cap"):return rv
        a,b=np.broadcast_arrays(np.asarray(a,float),np.asarray(b,float))
        shape=a.shape;af=a.ravel();bf=b.ravel();f=rv.reshape(-1,6,3).copy();P,domains=rib.domain(self.o)
        labels=np.mod(af,P)
        for strip,(start,end) in zip(self.strips,domains):
            u=np.where(labels<start,labels+P,labels);mask=(u>=start)&(u<=end)
            if not np.any(mask):continue
            s=J(u[mask],s=1.);v=J(bf[mask],a=1.)
            if chart=="cylinder":
                y=v;gate=J(1.)
            else:
                sign=1 if chart.endswith("+") else -1;w=v+g.E if chart.startswith("round") else v
                h=strip.ext;k=np.tanh(w.v/h)
                y=sign*(g.B+unary(w,h*k,1-k*k,-2*k*(1-k*k)/h))
                gate=1-cap_s7(w/(g.E+g.OLD_L-.03))
            v=self.delta(s,y,strip);f[mask]+=gather(tuple(gate*z for z in v),np.sum(mask))
        return f.reshape(shape+(6,3))
