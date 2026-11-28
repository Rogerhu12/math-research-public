"""Whole, shared material atlas and physical C2 fields for finite axial phases."""
from collections import OrderedDict
import numpy as np
from scipy.interpolate import BSpline
from bent_body_atlas import profile_nodes

def dot(a,b):
    return np.einsum("...i,...i->...",a,b)

def scalar(z):
    a=np.zeros((len(z),6));a[:,0]=z;return a

def mul(a,b):
    av,au,at,auu,aut,att=a.T;bv,bu,bt,buu,but,btt=b.T
    return np.column_stack([av*bv,au*bv+av*bu,at*bv+av*bt,auu*bv+2*au*bu+av*buu,
                     aut*bv+au*bt+at*bu+av*but,att*bv+2*at*bt+av*btt])

def unary(a,v,d,dd):
    return np.column_stack([v,d*a[:,1],d*a[:,2],dd*a[:,1]**2+d*a[:,3],
                         dd*a[:,1]*a[:,2]+d*a[:,4],dd*a[:,2]**2+d*a[:,5]])

def smooth(a):
    t=np.clip(a[:,0],0.,1.);p=t*(1-t)
    return unary(a,t**4*(35+t*(-84+t*(70-20*t))),140*p**3,420*p*p*(1-2*t))

def reciprocal(a):
    q=1/a[:,0];return unary(a,q,-q*q,2*q**3)

def cheb(a,n):
    tabs=[scalar(np.ones(len(a)))]
    if n:tabs.append(a)
    for _ in range(2,n+1):tabs.append(2*mul(a,tabs[-1])-tabs[-2])
    return tabs

def support_norm(f,sign,center):
    u,v=f[:,1],f[:,2];c=np.cross(u,v)*sign[:,None]
    area=np.sqrt(np.where(dot(c,c).real>1e-22,dot(c,c),1e-22))
    normal=c/area[:,None]
    return normal,area,dot(f[:,0]-center,normal)

def metric(f):
    return dot(f[:,1],f[:,1]),dot(f[:,1],f[:,2]),dot(f[:,2],f[:,2])

def whiten(t,g):
    e,f,h=g;h=np.where(h.real>1e-15,h,1.e-15);q=f/h;v=e-f*q
    v=np.where(v.real>1e-15,v,1e-15);i,j,k=t
    return np.column_stack([(i-2*q*j+q*q*k)/v,np.sqrt(2)*(j-q*k)/np.sqrt(v*h),k/h])

def opnorm(a):
    return abs(.5*(a[:,0]+a[:,2]))+np.sqrt((.5*(a[:,0]-a[:,2]))**2+.5*a[:,1]**2)

def properties(f,m):
    g=metric(f);n,area,sup=support_norm(f,m.sign,m.center)
    gram=whiten(tuple(a-b for a,b in zip(g,m.g0)),m.g0)
    curv=whiten([dot(n,f[:,i]) for i in (3,4,5)],g)
    H=.5*(curv[:,0]+curv[:,2])
    radius=np.sqrt((.5*(curv[:,0]-curv[:,2]))**2+.5*curv[:,1]**2+1e-20)
    return gram,np.sqrt(H**2+1e-20)+radius,sup,area,n

class Mesh:
    def __init__(self,src,counts,offset):
        self.src=src;self.ar=src.ar;g=src.ar.old;self.g=g
        u=profile_nodes(g,counts[0],offset)
        y0=np.linspace(-1.,1.,counts[1])
        if offset:y0=np.r_[y0[0],.61*y0[:-1]+.39*y0[1:],y0[-1]]
        y=np.unique(np.r_[y0,0.,-.70,.70,-.71,.71,-.83,.83,-.95,.95])
        L=g.END_LENGTH
        vr=np.linspace(0.,L,counts[2])
        if offset:vr=np.r_[0.,.61*vr[:-1]+.39*vr[1:],L]
        v=np.unique(np.r_[vr,.0001,.00025,.0005,.001,L-.0005,L-.00025])
        lam=np.linspace(0.,1.,counts[3])[1:]
        if offset:lam=np.r_[.37*lam[:-1]+.63*lam[1:],lam[0]*.69,1.]
        lam=np.unique(np.r_[lam,.007,.035,.25,.50,.75,.99925,.9995,.99975,.9999])
        self.cases=[];self.lab=[];self.sg=[];self.xy=[];self.w=[]
        center=np.array([g.CENTER_X,0.,0.]);self.center=center
        arr=[]
        for name,vv,sg in (("cylinder",y,1),("end+",v,1),("end-",v,-1),("cap+",lam,-1),("cap-",lam,1),
                        ("cap-cartesian+",[0.],-1),("cap-cartesian-",[0.],1)):
            if "cartesian" in name:
                aa=np.array([center[0],center[0]-.00002,center[0]+.00002]);bb=np.zeros(3)
            else:
                aa,bb=np.meshgrid(u,vv,indexing="ij");aa=aa.ravel();bb=bb.ravel()
            self.cases.append((name,aa,bb));self.xy.append(np.column_stack([aa,bb]));self.sg.append(np.full(len(aa),sg))
            self.lab.append(np.full(len(aa),name));self.w.append(np.full(len(aa),np.sqrt((.002 if "cartesian" in name else 1.)/len(aa))))
            arr.append(self.ar.chart_jet(name,aa,bb,0.,modes=self.ar.axial.ZERO_ENDS,rotate=False))
        self.f0=np.concatenate(arr);self.g0=metric(self.f0);self.lab=np.concatenate(self.lab)
        self.sign=np.concatenate(self.sg);self.xy=np.concatenate(self.xy);self.weight=np.concatenate(self.w)
        self.cache=OrderedDict()
    def at(self,d,t):
        key=(d["id"],float(t))
        if key in self.cache:
            self.cache.move_to_end(key);return self.cache[key]
        z=[]
        for chart,a,b in self.cases:
            if d["mode"]=="dev":
                v=self.src.chart_jet(chart,a,b,t,method=d["angle"],bend=d["bend"],
                               fade_start=d["fade"][0],fade_stop=d["fade"][1],rotate=False)
            else:
                func=self.ar.chart_jet if d["angle"]=="arc" else self.ar.legacy_chart_jet
                md=self.ar.CAP_ONLY if d["mode"]=="cap-only" else self.ar.REFERENCE
                v=func(chart,a,b,t,modes=md,rotate=False)
            z.append(v)
        value=np.concatenate(z);self.cache[key]=value
        if len(self.cache)>6:self.cache.popitem(last=False)
        return value
    def name(self,i):
        return {"chart":str(self.lab[i]),"u":float(self.xy[i,0]),"v":float(self.xy[i,1]),"index":int(i)}

class Basis:
    """Three independent physical channels. All spatial columns use the fixed original material."""
    def __init__(self,m,d,cfg):
        N=len(m.f0);one=scalar(np.ones(N));X,Y,Z=[m.f0[:,:,i].copy() for i in range(3)]
        j=scalar(m.xy[:,0]);j[:,1]=1.
        v=scalar(m.xy[:,1]);v[:,2]=1.
        absY=Y*np.where(Y[:,0]>=0,1.,-1.)[:,None]
        capplus=smooth((Y-1.025*one)/.06)
        dx=X-m.center[0]*one;r2=mul(dx,dx)+mul(Z,Z)
        # Point and tangent of the positive cap germ stay exactly fixed.
        germ=one-mul(capplus,.055**2*reciprocal(r2+.055**2*one))
        locked=smooth((absY-one)/.048)
        if d["central"]=="locked":
            window=locked
        else:
            s0=m.g.profile_constants(32)[2]+m.g.PLANAR_BLEND/2
            lo=s0+.15*.10;hi=s0+.15*1.05
            guard=mul(smooth((j-(lo-.09)*one)/.09),smooth(((hi+.09)*one-j)/.09))
            guard=mul(guard,one-smooth((absY-.70*one)/.15))
            guard[m.lab!="cylinder"]=0.
            window=one-guard
        extra_window=None
        if d["central"]=="expanded":
            extra_window=mul(window-locked,germ)
            window=locked
        window=mul(window,germ)
        td=cfg["degree"];capd=cfg["cap_degree"];md=cfg["roll_modes"]
        cx=cheb(X/1.3,max(td,capd));cz=cheb(Z/1.,max(td,capd));cy=cheb(Y/1.12,td)
        names=[];cols=[]
        def put(name,z):
            names.append(name);cols.append(z)
        for i in range(td+1):
            for k in range(td+1-i):
                xz=mul(cx[i],cz[k])
                for l in range(min(3,td-i-k)+1):
                    atom=mul(xz,cy[l])
                    put(("physical",i,l,k),mul(window,atom))
                    if extra_window is not None:
                        put(("extra_central",i,l,k),mul(extra_window,atom))
        for side in (-1,1):
            gate=mul(window,smooth((side*Y-.79*one)/.25))
            for i in range(capd+1):
                for k in range(capd+1-i):
                    put(("cap",side,i,k),mul(gate,mul(cx[i],cz[k])))
        baseperiod=2*m.g.profile_constants(32)[4]
        freq=[]
        for k in range(md+1):
            z=k*2*np.pi/baseperiod
            for ph in ([0.] if k==0 else [0.,np.pi/2]):
                q=z*m.xy[:,0]+ph
                freq.append(((k,int(ph>0)),unary(j,np.cos(q),-z*np.sin(q),-z*z*np.cos(q))))
        # Also retain the true rapid original turning-sector fields.
        _,T,normal,kk,kp=m.g.profile_coordinates(m.xy[:,0])
        for i in [0,1]:
            freq.append((("T",i),unary(j,T[:,i],-kk*normal[:,i],-kp*normal[:,i]-kk*kk*T[:,i])))
        nr=cfg["roll_spans"];L=m.g.END_LENGTH
        inherited=cfg.get("previous_roll_spaces",[]) if d["central"]=="expanded" else []
        for side in ("+","-"):
            use=(m.lab=="end"+side);w=np.clip(m.xy[use,1]/L,0.,1.)
            rb=[]
            for spans,maxmode in [*inherited,[nr,md]]:
                knots=np.r_[np.zeros(5),np.linspace(0.,1.,spans+1),np.ones(5)]
                n=len(knots)-6;sp=BSpline(knots,np.eye(n),5)
                for h in range(3,n-3):
                    vv=np.zeros((N,6))
                    for order,idx in [(0,0),(1,2),(2,5)]:
                        vv[use,idx]=sp(w,nu=order)[:,h]/L**order
                    rb.append((("spline",h,spans),vv,maxmode))
            # True C2 extra mode, zero first two jets at both ends.
            alpha=2.5
            r0=w**alpha*(1-w)**4
            r1=alpha*w**(alpha-1)*(1-w)**4-4*w**alpha*(1-w)**3
            r2=alpha*(alpha-1)*w**(alpha-2)*(1-w)**4-8*alpha*w**(alpha-1)*(1-w)**3+12*w**alpha*(1-w)**2
            vv=np.zeros((N,6));vv[use,0]=r0;vv[use,2]=r1/L;vv[use,5]=r2/L**2
            rb.append((("fractional",),vv,md))
            for h,rr,maxmode in rb:
                for k,ff in freq:
                    if k[0]=="T" or k[0]<=maxmode:put(("roll",side,h,k),mul(rr,ff))
        self.names=names;self.B=np.ascontiguousarray(np.stack(cols,axis=-1).transpose(1,0,2))
        self.m=len(names);self.n=3*self.m;self.cfg=cfg;self.exact_cloning=d["central"]=="expanded"
    def val(self,z):
        # B's storage order is (jet,point,mode).
        return (self.B@z.reshape(self.m,3)).transpose(1,0,2)
    def adj(self,v):
        return (self.B.reshape(-1,self.m).T@np.ascontiguousarray(v.transpose(1,0,2)).reshape(-1,3)).ravel()
    def project(self,oldnames,z):
        src=dict(zip(oldnames,z.reshape(-1,3)))
        ret=np.zeros((self.m,3))
        transforms={}
        for i,k in enumerate(self.names):
            if k in src:ret[i]=src[k];continue
            if self.exact_cloning:continue
            if k[0]!="roll" or k[2][0]!="spline":continue
            _,side,(_,h,newnr),angle=k
            rows=[(name[2][1],name[2][2],q) for name,q in src.items()
                  if name[0]=="roll" and name[1]==side and name[2][0]=="spline" and name[3]==angle]
            if not rows:continue
            oldnr=rows[0][1];key=(oldnr,newnr)
            if key not in transforms:
                t=np.linspace(0,1,10*max(key)+31)
                mats=[]
                for nn in key:
                    knots=np.r_[np.zeros(5),np.linspace(0.,1.,nn+1),np.ones(5)]
                    nd=len(knots)-6
                    mats.append(BSpline(knots,np.eye(nd),5)(t)[:,3:nd-3])
                transforms[key]=np.linalg.lstsq(mats[1],mats[0],rcond=1e-14)[0]
            ret[i]=sum(transforms[key][h-3,j-3]*q for j,_,q in rows)
        return ret.ravel()
