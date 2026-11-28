"""Run-44 physical basis: true R757 material, coupled second jets at each of its two rims."""
from functools import lru_cache
from types import SimpleNamespace
import numpy as np
from r742_tilted_disk_two_jets import J,unary,trig,cap_s7
import r763_translated_caps_and_shared_rim as physical
import bent_curved_hard_end_fields as prior

def layout(cfg):
    rr=(cfg["radial_degree"]+cfg["turn_degree"]+4)*(2*cfg["roll_modes"]+6)
    cc=len(prior.cap_indices(cfg))
    jj=3*(2*cfg["rim_modes"]+3)
    return rr,cc,jj

@lru_cache(maxsize=1)
def polar_reference():
    g=physical.g;P=2*g.profile_constants(32)[4];s=np.linspace(0,P,8193)
    q,n=g.profile(J(s),32);dd=physical.delay.end_limits(32)[1]+.0005
    x=q[0].v-dd*n[0].v-g.CENTER_X;z=q[1].v-dd*n[1].v
    angles=np.unwrap(np.pi-np.arctan2(z,x));angles-=angles[0]
    return s,angles,np.hypot(x,z)

def cartesian_material(X,Z):
    # The auxiliary Cartesian probes at the old interior bump need the SAME
    # angular/radial rim modes as the polar chart. At the center their gate vanishes.
    g=physical.g;u0,a0,rr=polar_reference()
    dx=X.v-g.CENTER_X;dz=Z.v;r=np.hypot(dx,dz)
    angle=np.mod(np.pi-np.arctan2(dz,dx),2*np.pi)
    s=np.interp(angle,a0,u0);rho=r/np.interp(angle,a0,rr);w=1-.9995*rho
    use=(w<.68)&(r>1.e-4)
    A=J(np.zeros_like(r));B=J(np.ones_like(r))
    if np.any(use):
        ids=np.flatnonzero(use);D=physical.delay.end_limits(32)[1]+.0005
        def polar(a,b):
            q,n=g.profile(a,32);cc=(1-b)/.9995
            return g.CENTER_X+cc*(q[0]-D*n[0]-g.CENTER_X),cc*(q[1]-D*n[1])
        xi=physical.tube.cut(X,ids);zz=physical.tube.cut(Z,ids)
        a,b=physical.tube.inverse(polar,xi,zz,s[ids],w[ids])
        if np.any(b.v<.00075):raise ValueError("Cartesian chart outside its cap interior")
        A=physical.tube.replace(A,ids,a);B=physical.tube.replace(B,ids,b)
    return A,B

def rim(chart,u,v,ff,cfg):
    if "cartesian" in chart:
        a,w=cartesian_material(prior.posjet(ff,0),prior.posjet(ff,2));b=w
    else:
        a=J(np.asarray(u),s=1.);b=J(np.asarray(v),a=1.)
    D=physical.delay;L=D.END_LENGTH
    if chart.startswith("end"):
        r=b-L;gate=cap_s7(b/L)
    else:
        if "cartesian" not in chart:w=b if "normal" in chart else 1-b
        r=w;gate=1-cap_s7(w/.65)
    P=2*physical.g.profile_constants(32)[4];ang=[J(1.)];names=[("harmonic",0,0)]
    for k in range(1,cfg["rim_modes"]+1):
        ca,sa=trig((2*np.pi*k/P)*a)
        ang.extend((ca,sa));names.extend((("harmonic",k,0),("harmonic",k,1)))
    _,T,N,K,Ks=physical.g.profile_coordinates(a.v,32)
    for k in range(2):
        ang.append(unary(a,T[:,k],-K*N[:,k],-Ks*N[:,k]-K*K*T[:,k]))
        names.append(("tangent",k))
    rs=(gate,gate*r,gate*r*r*.5)
    table=np.empty((6,len(u),3*len(ang)))
    for i,p in enumerate(rs):
        for k,aa in enumerate(ang):
            col=p*aa;table[:,:,i*len(ang)+k]=np.broadcast_arrays(*col.parts(),u)[:6]
    return [("shared-rim",i,n) for i in range(3) for n in names],table

class Model:
    def __init__(self,n,cfg,offset):
        self.mesh=prior.Mesh(physical.paired.base,n,offset)
        self.inner=prior.Basis(self.mesh,cfg);m=self.mesh;b=self.inner
        self.shared={};rn=None
        for name,u,v,sl in m.cases:
            if name=="cylinder":continue
            rn,B=rim(name,u,v,m.f0[sl],cfg);self.shared[name]=(sl,B)
        self.names=list(b.names)+rn
        self.width=len(self.names);self.n=6*self.width;self.cfg=cfg
        rr,cc,jj=layout(cfg)
        if (rr,cc,jj)!=(b.m,len(b.capnames),len(rn)):raise ValueError("inconsistent physical dictionary")
    def val(self,z):
        c=np.asarray(z).reshape(2,self.width,3);i=self.inner.width
        f=self.inner.val(np.r_[np.zeros(prior.HARD),c[:,:i].ravel()])
        for name,(sl,B) in self.shared.items():
            side=0 if name.endswith("+") else 1
            f[sl]+=(B@c[side,i:]).transpose(1,0,2)
        return f
    def adj(self,grad):
        i=self.inner.width;out=np.zeros((2,self.width,3))
        out[:,:i]=self.inner.adj(grad).reshape(2,i,3)
        for name,(sl,B) in self.shared.items():
            side=0 if name.endswith("+") else 1
            out[side,i:]+=B.reshape(-1,self.width-i).T@grad[sl].transpose(1,0,2).reshape(-1,3)
        return out.ravel()
    def scale(self):
        w=np.array([.01,1,1,.001,.002,.001])[:,None]
        q=np.mean([np.sum(w*np.mean(B**2,axis=1),axis=0) for sl,B in self.shared.values()],axis=0)
        val=np.r_[self.inner.norm(),np.sqrt(q)]
        return np.tile(np.repeat(np.clip(.19/np.maximum(.03,val),.0015,2.),3),2)
    def project(self,names,z):
        old=np.asarray(z).reshape(2,len(names),3);by={s:i for i,s in enumerate(names)}
        new=np.zeros((2,self.width,3))
        for i,s in enumerate(self.names):
            if s in by:new[:,i]=old[:,by[s]]
        return new.ravel()
    def base(self,d,t):
        if not t:return self.mesh.f0.copy()
        f=[physical.chart_jet(k,u,v,t,d) for k,u,v,sl in self.mesh.cases]
        return np.concatenate(f)

def evaluate(d,cfg,z,chart,u,v,t):
    a,b=np.broadcast_arrays(np.asarray(u,float),np.asarray(v,float));sh=a.shape
    u=a.ravel();v=b.ravel();out=[]
    rr,cc,jj=layout(cfg);coeff=z.reshape(2,rr+cc+jj,3)[0 if chart.endswith("+") else 1]
    if chart=="cylinder":return physical.chart_jet(chart,a,b,t,d)
    for first in range(0,len(u),384):
        sl=slice(first,first+384);a=u[sl];b=v[sl]
        f=physical.chart_jet(chart,a,b,t,d);f0=physical.delay.chart_jet(chart,a,b,0.,bend=0.,rotate=False)
        if chart.startswith("end"):
            fake=SimpleNamespace(xy=np.c_[a,b],delay=physical.delay,g=physical.g,roll=[slice(None)])
            B=prior.Basis(fake,cfg).B;c=coeff[:rr]
        else:B=prior.cap_matrix(chart,b,f0,cfg);c=coeff[rr:rr+cc]
        f=f+(B@c).transpose(1,0,2)
        js=rim(chart,a,b,f0,cfg)[1]
        out.append(f+(js@coeff[rr+cc:]).transpose(1,0,2))
    return np.concatenate(out).reshape(sh+(6,3))
