"""One C2 spatial dictionary on the original R757 atlas, shared by all phase nodes."""
from types import SimpleNamespace
import numpy as np
import bent_shared_rim_fields as legacy
import r765_signed_ratio_closed_two_jets as physical
from r742_tilted_disk_two_jets import J,unary,cap_s7
prior=legacy.prior

def material_nodes(g,n,off):
    base=prior.qualified_nodes(g,n,off);old=g.original.profile_constants(32)
    top=old[1];bot=2*old[4]-top-1.3;b=physical.B
    a=[]
    for j,kind in [(0,1),(1,1),(2,1),(7,-1),(8,-1),(9,-1),(10,-1)]:
        for l,r in physical.intervals(kind):
            for edge,sign in ((l,1),(r,-1)):
                f=np.array([0.,.23,.5,.81,1.]) if off else np.array([0.,.38,.72,1.])
                for width in (physical.WIDTH,physical.BOUNDED_WIDTH):
                    a.extend((j+edge+sign*width*f)*b)
    v=np.asarray(a);v=np.r_[base,g.forward(top+v),g.forward(bot+v)]
    v=np.sort(v);return v[np.r_[True,np.diff(v)>3.e-12]]

class Mesh:
    def __init__(self,src,n,off):
        self.src=src;self.delay=src.delay;self.ar=src.ar;self.g=src.OLD
        g=self.g;r=self.delay;U=material_nodes(g,n[0],off)
        def levels(lo,hi,m):
            x=np.linspace(lo,hi,m)
            return np.r_[lo,.63*x[:-1]+.37*x[1:],hi] if off else x
        Y=np.unique(np.r_[levels(-r.HALF_WIDTH,r.HALF_WIDTH,n[1]),0.,-.36,.36])
        v0=levels(0,g.END_LENGTH,n[2]);b=r.SMALL_ANGLE
        # Include the small old v0 ramp and both sides of the true change of variable.
        fine=r.clock_at(np.array([0.,.000025,.00005,.00010,.000125,.00015,.000175,
                                 .0002,.00025,.00035,.0005,.0008,.001,g.END_LENGTH-.0005]))
        fractions=np.array([.15,.35,.55,.60,.70,.80,.88,.94,.97,.98,.99,.995,.998,.999,.9995,1.])
        low=np.zeros_like(fractions);high=low+.002
        for _ in range(48):
            mid=.5*(low+high)
            theta=g.disk.softened_angle(mid,g.END_LENGTH,g.END_BLEND,1/g.END_TURN)
            flag=theta<fractions*r.SMALL_ANGLE
            low=np.where(flag,mid,low);high=np.where(flag,high,mid)
        sharp=r.clock_at(.5*(low+high))
        V=np.unique(np.r_[levels(0,r.END_LENGTH,n[2]),r.clock_at(v0),fine,sharp,r.END_LENGTH])
        W=np.unique(np.r_[levels(0,1,n[3])[1:],.007,.035,.25,.5,.75,.99925,.9995,.99975,.99978,.99982,.999875,.99993,.99997,.99999])
        self.cases=[];self.center=np.array([g.CENTER_X,0.,0.]);self.polar=U
        F=[];lab=[];loc=[];sign=[];weight=[];start=0
        for label,z,sg in (("cylinder",Y,1),("end+",V,1),("end-",V,-1),("cap+",W,-1),
                           ("cap-",W,1),("cap-cartesian+",[0],-1),("cap-cartesian-",[0],1)):
            if "cartesian" in label:
                u=np.array([g.CENTER_X,g.CENTER_X-.012,g.CENTER_X+.012,g.CENTER_X,g.CENTER_X])
                v=np.array([0.,-.001,.001,-.00002,.00002])
                # This Cartesian patch also includes the proved interior bump disk.
                aa=np.linspace(0.,2*np.pi,max(12,n[3]),endpoint=False)+(.17 if off else 0.)
                rr=np.array([0.,.013,.025,.035,.04,.043])
                u=np.r_[u,(-.35+rr[:,None]*np.cos(aa)).ravel()]
                v=np.r_[v,(rr[:,None]*np.sin(aa)).ravel()]
            else:
                u,v=np.meshgrid(U,z,indexing="ij");u=u.ravel();v=v.ravel()
            ff=r.chart_jet(label,u,v,0.,bend=0.,rotate=False)
            stop=start+len(u);self.cases.append((label,u,v,slice(start,stop)));start=stop
            F.append(ff);loc.append(np.c_[u,v]);lab.extend([label]*len(u));sign.extend([sg]*len(u))
            weight.extend([np.sqrt((.008 if "cartesian" in label else 1.)/len(u))]*len(u))
        self.f0=np.concatenate(F);self.xy=np.concatenate(loc);self.g0=legacy.prior.metric(self.f0);self.lab=np.array(lab)
        self.sign=np.array(sign);self.weight=np.array(weight);self.cache={}
        self.fan_cache={};self.pose_cache={}
        self.roll=[next(j for label,u,v,j in self.cases if label=="end"+side) for side in ("+","-")]
    def name(self,i):
        return {"chart":str(self.lab[i]),"u":float(self.xy[i,0]),"v":float(self.xy[i,1]),"index":int(i)}

def slope_modes(s):
    # Return actual material jets in the regular input coordinates including
    # the Cartesian overlap, where s is obtained from the actual inverse map.
    g=physical.g
    unique,inv=np.unique(s.v,return_inverse=True)
    sh,old,live,ell,f=g.local(unique,32);m=g.original.profile_constants(32)
    P=2*m[4];top=m[1];bot=P-top-1.3
    a=old%P;e=np.sqrt(1+f[1]*f[1]);bp=-f[1]*f[2]/e**4
    names=[];out=[]
    for side,origin in (("upper",top),("lower",bot)):
        for j,kind in [(0,1),(1,1),(2,1),(7,-1),(8,-1),(9,-1),(10,-1)]:
            xi=(a-origin)/physical.B-j
            val=unary(s,xi[inv],(1/e/physical.B)[inv],(bp/physical.B)[inv])
            p=physical.window(val,kind);thin=physical.window(val,kind,physical.BOUNDED_WIDTH)
            for power,h in ((1,p),(4,p*p*p*p),(8,thin*thin*thin*thin)):
                out.append(h);names.append((side,j,power))
    return names,out

def local_table(chart,u,v,f0,cfg):
    if "cartesian" in chart:
        a,w=legacy.cartesian_material(prior.posjet(f0,0),prior.posjet(f0,2))
    else:
        a=J(np.asarray(u),s=1.);q=J(np.asarray(v),a=1.)
        w=q if "normal" in chart else 1-q
    angular,values=slope_modes(a)
    if chart.startswith("end"):
        x=q/physical.delay.END_LENGTH;env=64*x*x*x*(1-x)*(1-x)*(1-x)
        factors=[cap_s7(x),env]
        if cfg["cell_depth"]>=2:factors.append(env*(2*x-1))
        if cfg["cell_depth"]>=3:factors.append(env*(2*(2*x-1)*(2*x-1)-1))
    else:
        factors=[1-cap_s7(w/.65)]+[J(0.)]*cfg["cell_depth"]
    names=[];tab=np.empty((6,len(u),len(values)*len(factors)))
    for k,z in enumerate(factors):
        for i,p in enumerate(values):
            a0=z*p
            tab[:,:,k*len(values)+i]=np.broadcast_arrays(*a0.parts(),u)[:6]
            names.append(("signed-cell",k,angular[i]))
    return names,tab

def boundary(chart,u,v,f0,cfg):
    n,B=legacy.rim(chart,u,v,f0,cfg);q,D=local_table(chart,u,v,f0,cfg)
    return n+q,np.concatenate((B,D),axis=2)

def layout(cfg):
    a,b,c=legacy.layout(cfg)
    return a,b,c+42*(1+cfg["cell_depth"])

class Model(legacy.Model):
    def __init__(self,n,cfg,offset):
        self.mesh=Mesh(physical.paired.base,n,offset);m=self.mesh
        self.inner=prior.Basis(m,cfg)
        self.shared={};reuse={};rn=None
        for name,u,v,sl in m.cases:
            if name=="cylinder":continue
            key=name[:-1]
            if key not in reuse:reuse[key]=boundary(name,u,v,m.f0[sl],cfg)
            rn,B=reuse[key];self.shared[name]=(sl,B)
        self.names=list(self.inner.names)+rn
        self.width=len(self.names);self.n=6*self.width;self.cfg=cfg
        if layout(cfg)!=(self.inner.m,len(self.inner.capnames),len(rn)):
            raise ValueError("inconsistent coframe dictionary")
    def base(self,d,t):
        if not t:return self.mesh.f0.copy()
        return np.concatenate([physical.chart_jet(k,u,v,t,d) for k,u,v,sl in self.mesh.cases])
    def blocks(self):
        i=self.inner.width
        for name,u,v,sl in self.mesh.cases:
            if name=="cylinder":continue
            if name.startswith("end"):
                ids=np.arange(self.inner.m);old=self.inner.B
            else:
                ids=np.arange(self.inner.m,i);old=self.inner.caps[name][1]
            yield name,sl,np.r_[ids,np.arange(i,self.width)],old,self.shared[name][1]

def evaluate(d,cfg,z,chart,u,v,t):
    a,b=np.broadcast_arrays(np.asarray(u,float),np.asarray(v,float));sh=a.shape
    u=a.ravel();v=b.ravel();out=[]
    if chart=="cylinder":return physical.chart_jet(chart,a,b,t,d)
    rr,cc,jj=layout(cfg);co=z.reshape(2,rr+cc+jj,3)[0 if chart.endswith("+") else 1]
    for start in range(0,len(u),320):
        sl=slice(start,start+320);aa=u[sl];bb=v[sl]
        f=physical.chart_jet(chart,aa,bb,t,d)
        f0=physical.delay.chart_jet(chart,aa,bb,0.,bend=0.,rotate=False)
        if chart.startswith("end"):
            grid=SimpleNamespace(xy=np.c_[aa,bb],delay=physical.delay,g=physical.g,roll=[slice(None)])
            B=prior.Basis(grid,cfg).B;c=co[:rr]
        else:B=prior.cap_matrix(chart,bb,f0,cfg);c=co[rr:rr+cc]
        D=boundary(chart,aa,bb,f0,cfg)[1]
        out.append(f+(B@c+D@co[rr+cc:]).transpose(1,0,2))
    return np.concatenate(out).reshape(sh+(6,3))
