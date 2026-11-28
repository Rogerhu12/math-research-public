"""R732 closed material ring, including both primary sheets and the two true U arcs."""
import hashlib
import numpy as np
from r688_actual_r664_window_collars import mollifier_cdf,quadrature
from r688_true_caps_and_reference_sections import sym_step
PARTS=((.205,.102,.100),(.846,.102,-.100),(.206,.100,.920),(.847,.100,-.920))

def angles(v,phase):
    v=np.asarray(v)
    return sum(a*(phase if i>=2 else 1.)*sym_step((abs(v)-c)/w) for i,(c,w,a) in enumerate(PARTS))

def line_k(v,phase):
    v=np.asarray(v);ans=np.zeros_like(v)
    for i,(c,w,a) in enumerate(PARTS):
        f=(abs(v)-c)/w
        ans+=a*(phase if i>=2 else 1.)*(mollifier_cdf((f-.001)/.0005)-mollifier_cdf((f-.999)/.0005))/(.998*w)
    return np.sign(v)*ans

class Line:
    def __init__(self,phase,order):
        self.phase=phase;self.order=order
        knots=[0.,1.]
        for c,w,_ in PARTS:knots.extend(c+w*np.array([0.,.0005,.0015,.9985,.9995,1.]))
        self.knots=np.unique(knots);self.prefix=[np.zeros(2)]
        for a,b in zip(self.knots,self.knots[1:]):
            self.prefix.append(self.prefix[-1]+self.inc(a,b))
        self.prefix=np.array(self.prefix);self.mid=np.array([-1.,0.])+self.prefix[-1]

    def inc(self,a,b):
        q,w=quadrature(self.order)
        o=(np.atleast_1d(b)-a)/2
        pos=a+o[:,None]*(1+q)
        th=angles(pos,self.phase)
        out=o[:,None]*np.column_stack((np.cos(th)@w,np.sin(th)@w))
        return out[0] if np.ndim(b)==0 else out

    def position(self,v):
        v=np.asarray(v);nodes,ix=np.unique(abs(v.ravel()),return_inverse=True)
        ids=np.minimum(np.searchsorted(self.knots,nodes,side='right')-1,len(self.knots)-2)
        out=np.empty((len(nodes),2))
        for i in np.unique(ids):
            use=ids==i;out[use]=self.prefix[i]+self.inc(self.knots[i],nodes[use])
        return self.mid+np.sign(v)[...,None]*out[ix].reshape(v.shape+(2,))

def curvature_derivative(v,phase,order):
    v=np.asarray(v); ans=np.zeros_like(v)
    q,wt=quadrature(order)
    norm=np.exp(-1/(1-q*q))@wt
    def bump(z):
        a=np.zeros_like(z); keep=abs(z)<1
        a[keep]=np.exp(-1/(1-z[keep]**2))/norm
        return a
    for i,(c,w,amp) in enumerate(PARTS):
        f=(abs(v)-c)/w
        ans+=amp*(phase if i>=2 else 1.)*(bump((f-.001)/.0005)-bump((f-.999)/.0005))/(.998*.0005*w*w)
    return ans


class Ring:
    """Oriented arclength on the upper line, far U, lower line and near U."""
    def __init__(self,phase,order):
        self.phase=phase
        self.order=order
        self.jet_cache={}
        self.line=Line(phase,order)
        self.split=np.array([0.,.0005,.0015,.9985,.9995,1.])
        inc=[self.turn_inc(a,b) for a,b in zip(self.split,self.split[1:])]
        self.prefix=np.r_[np.zeros((1,2)),np.cumsum(inc,axis=0)]
        self.LU=-.4/self.prefix[-1,1]
        self.length=4+2*self.LU
        self.origin=self.line.position(np.asarray(0.))

    def turn_inc(self,a,b):
        q,w=quadrature(self.order)
        z=(np.atleast_1d(b)-a)/2
        arg=a+z[:,None]*(1+q)
        th=-np.pi*sym_step(arg)
        val=z[:,None]*np.column_stack((np.cos(th)@w,np.sin(th)@w))
        return val[0] if np.ndim(b)==0 else val

    def turn_pos(self,u):
        u,ix=np.unique(u,return_inverse=True)
        ids=np.minimum(np.searchsorted(self.split,u,side='right')-1,4)
        P=np.empty((len(u),2))
        for i in np.unique(ids):
            j=ids==i
            P[j]=self.prefix[i]+self.turn_inc(self.split[i],u[j])
        return self.LU*P[ix]

    def label(self,s):
        d=np.mod(np.asarray(s),1.)*self.length
        kind=np.searchsorted(np.array([2.,2+self.LU,4+self.LU]),d,side='right')
        v=np.select([kind==0,kind==2,kind==1],[d-1,3+self.LU-d,1.],default=-1.)
        return d,kind,v

    def jets(self,s):
        """Position, tangent, left unit normal, signed curvature, arclength derivative."""
        s=np.asarray(s);shape=s.shape
        unique,inverse=np.unique(s.ravel(),return_inverse=True)
        key=hashlib.sha256(np.ascontiguousarray(unique,dtype='<f8').tobytes()).hexdigest()
        if key in self.jet_cache:
            return tuple(a[inverse].reshape(shape+a.shape[1:]) for a in self.jet_cache[key])
        d,kind,v=self.label(unique); N=len(d)
        yz=np.empty((N,2)); angle=np.empty(N); k=np.empty(N); ks=np.empty(N)
        for idx in (0,2):
            keep=kind==idx
            if not np.any(keep):continue
            V=v[keep]; sign=1 if idx==0 else -1
            yz[keep]=self.line.position(V)+np.array([0.,sign*.20])
            angle[keep]=angles(V,self.phase)+(0 if idx==0 else -np.pi)
            k[keep]=sign*line_k(V,self.phase)
            ks[keep]=curvature_derivative(V,self.phase,self.order)
        for idx in (1,3):
            keep=kind==idx
            if not np.any(keep):continue
            sign=1 if idx==1 else -1
            u=np.clip((d[keep]-(2. if idx==1 else 4+self.LU))/self.LU,0.,1.)
            yz[keep]=self.line.position(np.asarray(float(sign)))+sign*np.array([0.,.20])+sign*self.turn_pos(u)
            angle[keep]=-np.pi*sym_step(u)+(0 if idx==1 else -np.pi)
            k[keep]=-np.pi*(mollifier_cdf((u-.001)/.0005)-mollifier_cdf((u-.999)/.0005))/(.998*self.LU)
            q,w=quadrature(self.order); norm=np.exp(-1/(1-q*q))@w
            def kernel(z):return np.where(abs(z)<1,np.exp(-1/np.maximum(1-z*z,1.e-300))/norm,0.)
            ks[keep]=-np.pi*(kernel((u-.001)/.0005)-kernel((u-.999)/.0005))/(.998*.0005*self.LU**2)
        T=np.column_stack([np.cos(angle),np.sin(angle)])
        normal=np.column_stack([-np.sin(angle),np.cos(angle)])
        values=(yz,T,normal,k,ks)
        if len(self.jet_cache)>=12:self.jet_cache.pop(next(iter(self.jet_cache)))
        self.jet_cache[key]=values
        return tuple(a[inverse].reshape(shape+a.shape[1:]) for a in values)

    def angular_data(self,s):
        s=np.asarray(s);unique,inverse=np.unique(s.ravel(),return_inverse=True)
        d,kind,v=self.label(unique)
        keep=(kind==0)|(kind==2)
        delta=np.where(keep,angles(v,self.phase)-angles(v,0.),0.)
        dd=np.where(keep,np.where(kind==0,1.,-1.)*(line_k(v,self.phase)-line_k(v,0.))*self.length,0.)
        return delta[inverse].reshape(s.shape),dd[inverse].reshape(s.shape)

