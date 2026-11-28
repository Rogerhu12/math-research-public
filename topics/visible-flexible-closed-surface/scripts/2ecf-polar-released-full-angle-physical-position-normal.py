#!/usr/bin/env python3
"""Matrix-free damped Gauss-Newton for full independent XYZ/real Fourier channels on the actual released-cuff geometry."""
import argparse
import importlib.util
import json
import os
import sys
from pathlib import Path
for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):os.environ[k]='1'
import numpy as np
from scipy.sparse.linalg import LinearOperator,lsmr
from scipy.spatial import cKDTree
def module(p,n):
    sp=importlib.util.spec_from_file_location(n,p);m=importlib.util.module_from_spec(sp);sys.modules[n]=m;sp.loader.exec_module(m);return m
here=Path(__file__).parent
clock=module(here/'2ecf-polar-released-true-irregular-material-clock-observation.py','cartesian_full_clock')
c=clock.c;ext=c.ext;base=c.base
class XYZ:
    orders=clock.orders
    def __init__(self,s,u,b,T,n,m):
        self.B=c.spline(s,b,T,n);self.F=[];freq=np.arange(1,m+1)
        for d in range(3):
            theta=np.outer(u,freq)+d*np.pi/2
            self.F.append(np.c_[np.full(len(u),int(d==0)),np.cos(theta)*freq**d,np.sin(theta)*freq**d])
        self.shape=(3,self.B[0].shape[1],1+2*m)
        k=np.r_[0,freq,freq]
        self.scale=1/np.sqrt(1+(n/(T-b))**2+.8*k*k+.006*k**4)
        self.size=int(np.prod(self.shape));self.ns=len(s);self.nu=len(u)
    def apply(self,x):
        xx=np.asarray(x).reshape(self.shape);v=np.empty((self.ns,6,self.nu,3))
        for i,(s,u) in enumerate(self.orders):
            for d in range(3):v[:,i,:,d]=(self.B[s]@xx[d])@self.F[u].T
        return v
    def transpose(self,g):
        out=np.zeros(self.shape)
        for i,(s,u) in enumerate(self.orders):
            for d in range(3):out[d]+=self.B[s].T@(g[:,i,:,d]@self.F[u])
        return out.ravel()
    def pre(self,x):return (x.reshape(self.shape)*self.scale[None,None,:]).ravel()
class Far:
    def __init__(self,j,s,u,R):
        self.R=R;self.ns=len(s);self.nu=len(u);self.num=len(s)*len(u)
        p=j[:,0].reshape(-1,3);blocks=np.array_split(np.arange(len(s)),15);sv=np.repeat(s,len(u));pairs=[]
        for i,b in enumerate(blocks):
            ii=np.arange(b[0]*len(u),(b[-1]+1)*len(u));left=cKDTree(p[ii])
            for b2 in blocks[i+1:]:
                if s[b2[-1]]-s[b[0]]<.3:continue
                jj=np.arange(b2[0]*len(u),(b2[-1]+1)*len(u));nodes=left.sparse_distance_matrix(cKDTree(p[jj]),.235,output_type='coo_matrix')
                pi,pj=ii[nodes.row],jj[nodes.col];ok=(sv[pj]-sv[pi])>=.30
                if np.any(ok):pairs.append(np.c_[pi[ok],pj[ok]])
        out=np.concatenate(pairs);self.i=out[:,0];self.j=out[:,1]
    def values(self,j):
        p=j[:,0].reshape(-1,3);s=j[:,1].reshape(-1,3);u=j[:,2].reshape(-1,3);nn=np.cross(s,u);w=np.linalg.norm(nn,axis=1);n=nn/w[:,None]
        d=p[self.j]-p[self.i];dd=np.sum(d*d,axis=1);di=np.sum(n[self.i]*d,axis=1);dj=np.sum(n[self.j]*d,axis=1)
        val=np.stack([abs(di)-dd/(2*self.R),abs(dj)-dd/(2*self.R)],axis=-1)
        ratio=np.min(dd/(2*np.maximum(1e-13,np.maximum(abs(di),abs(dj)))))
        return val,float(ratio)
def warp(j,v,ds):
    ans=j.copy();s=v[:,None,None];ans[:,1]=j[:,1]/s;ans[:,4]=j[:,4]/s;ans[:,3]=(j[:,3]-ds[:,None,None]*j[:,1])/(s*s);return ans
def adjwarp(j,v,ds):
    s=v[:,None,None];j[:,1]=j[:,1]/s-ds[:,None,None]*j[:,3]/(s*s);j[:,3]/=s*s;j[:,4]/=s;return j
class Core:
    def __init__(self,a):
        self.a=a;m=clock.PhysicalField(a);self.m=m;b,S,T=m.b,m.S,m.T
        ns=np.linspace(b,T,a.radials);u=2*np.pi*(np.arange(a.angles)+.211)/a.angles
        self.s=ns;self.u=u
        r=c.target(a,ns,b,S,m.g);self.speed=np.ones_like(ns);self.der=np.zeros_like(ns)
        self.clock=base.read(a.clock) if a.clock else None
        identity=base.read(a.closed)['closedTrueTargetSHA256']
        if self.clock:
            assert self.clock['spatialSHA256']==base.sha(a.spatial)
            self.j=np.concatenate([m.compose(ns[i:i+7],u,self.clock) for i in range(0,len(ns),7)])
            B,D=c.spline(ns,b,T,self.clock['metricSpans'])[:2];alpha=np.array(self.clock['targetCoefficients']);r*=np.exp(B@alpha[1]);self.speed=np.exp(B@alpha[0]);self.der=D@alpha[0];identity=self.clock['newTargetSHA256']
        else:self.j=np.concatenate([m.grid(ns[i:i+7],u) for i in range(0,len(ns),7)])
        self.identity=identity;self.rad=r[:,None];self.basis=XYZ(ns,u,b,T,a.spans,a.modes)
        self.point=module(a.scripts/'6a65-cartesian-complete-stream.py','full_angle_phys_rows').point
        self.area=module(a.scripts/'6a65-geometry-area-ratio-power-two.py','full_angle_area')
        cfg0=base.read(a.prepared)['definition']['pointConfig'];orig=self.point.PointConfig
        class New(orig):
            def __post_init__(self):
                old={k:getattr(self,k) for k in self.__dataclass_fields__};old['height_maximum']=.0195;orig(**old)
        self.cfg=New(**dict(cfg0,true_cuff_height=.415+m.sol['raisedCuffDelta'],height_maximum=.635-(.415+m.sol['raisedCuffDelta'])))
        w=np.ones((len(ns),1));w[[0,-1]]=.5;w/=np.sum(w)*len(u)
        self.w=w;self.weights=dict(metric=w,curvature=w*a.curvature,geometry=w*a.geometry)
        self.A=m.ends.master.A
    def packets(self,raw):
        j=warp(raw,self.speed,self.der);p=self.point.PointLinearized(j.swapaxes(1,2),self.rad,self.cfg,self.weights);ar=self.area.AreaPacket(j,self.rad,self.w,.5)
        return p,ar
    def summary(self,z,far):
        raw=self.j+self.basis.apply(z);p,ar=self.packets(raw);num=len(self.s)*len(self.u)
        f,ratio=far.values(raw)
        x=raw[:,0];centers=np.stack([np.linalg.norm(x-np.array([0.,sgn*self.A,0.]),axis=-1) for sgn in (-1,1)])
        d=np.maximum(self.a.held_target-centers,0)
        hard=(self.a.far_weight*np.sum(np.maximum(f,0)**2)+self.a.held_weight*np.sum(d*d))/num
        return dict(merit=float(np.sum(p.residual**2)+np.sum(ar.residual**2)+hard),original=float(np.sum(p.residual**2)+np.sum(ar.residual**2)),peakMetric=float(np.max(abs(p.metric/np.array([1,np.sqrt(2),1])))),kappa=float(np.max(abs(p.curvature['eigenvalues']))),held=float(np.min(centers)),farNormalRatio=ratio,sampledClosedCapMaximum=float(np.max(x[...,2])),extraPhysical=float(hard))
    def linear(self,z,far):
        raw=self.j+self.basis.apply(z);p,ar=self.packets(raw);b=self.basis
        w=np.sqrt(self.a.held_weight/(b.ns*b.nu));P=raw[:,0];dirs=[];held=[]
        for sign in (-1,1):
            d=P-np.array([0,sign*self.A,0]);r=np.linalg.norm(d,axis=-1);ac=r<self.a.held_target;dirs.append(-w*(ac/r)[...,None]*d);held.append(w*np.maximum(self.a.held_target-r,0))
        # Differentiate all active actual remote normal-ball rows, retaining both endpoints.
        fw=np.sqrt(self.a.far_weight/(b.ns*b.nu));vals,ratio=far.values(raw)
        fi=[];fj=[];vs=[];normal=np.cross(raw[:,1],raw[:,2]).reshape(-1,3);wn=np.linalg.norm(normal,axis=1);normal/=wn[:,None]
        ss=raw[:,1].reshape(-1,3);uu=raw[:,2].reshape(-1,3);PP=P.reshape(-1,3)
        for side in (0,1):
            active=np.flatnonzero(vals[:,side]>0);i=far.i[active];jj=far.j[active];chosen=i if side==0 else jj
            d=PP[jj]-PP[i];n=normal[chosen];sgn=np.sign(np.sum(d*n,axis=1))
            bd=fw*(sgn[:,None]*n-d/self.a.far_radius);gn=fw*sgn[:,None]*d
            cn=(gn-n*np.sum(gn*n,axis=1)[:,None])/wn[chosen,None]
            fi.append((i,jj,chosen,bd,np.cross(uu[chosen],cn),np.cross(cn,ss[chosen])))
            vs.append(fw*vals[active,side])
        rr=np.concatenate([p.residual.ravel(),ar.residual.ravel(),*(v.ravel() for v in held),*vs])
        def jf(x):
            dv=b.apply(b.pre(x));jw=warp(dv,self.speed,self.der)
            ff=[p.jvp(jw.swapaxes(1,2)).ravel(),ar.jvp(jw[:,1],jw[:,2]).ravel()]
            ff.extend(np.sum(d*dv[:,0],axis=-1).ravel() for d in dirs)
            d0=dv[:,0].reshape(-1,3);ds=dv[:,1].reshape(-1,3);du=dv[:,2].reshape(-1,3)
            ff.extend(np.sum((d0[j]-d0[i])*bd+ds[h]*bs+du[h]*bu,axis=1) for i,j,h,bd,bs,bu in fi)
            return np.concatenate(ff)
        def jt(v):
            n=p.residual.size;N=ar.residual.size;g=p.vjp(v[:n].reshape(p.residual.shape)).swapaxes(1,2)
            gs,gu=ar.vjp(v[n:n+N].reshape(ar.residual.shape));g[:,1]+=gs;g[:,2]+=gu;g=adjwarp(g,self.speed,self.der)
            ofs=n+N
            for d in dirs:g[:,0]+=d*v[ofs:ofs+N].reshape(d.shape[:2])[...,None];ofs+=N
            for i,j,h,bd,bs,bu in fi:
                bb=v[ofs:ofs+len(i),None];ofs+=len(i)
                def collect(ind,vec):return np.stack([np.bincount(ind,weights=vec[:,k],minlength=N) for k in range(3)],axis=1).reshape(b.ns,b.nu,3)
                g[:,0]+=collect(j,bd*bb)-collect(i,bd*bb);g[:,1]+=collect(h,bs*bb);g[:,2]+=collect(h,bu*bb)
            return b.pre(b.transpose(g))
        return LinearOperator((len(rr),b.size),matvec=jf,rmatvec=jt,dtype=float),rr
def run(a):
    core=Core(a);b=core.basis;z=np.zeros(b.size)
    if a.start:
        old=base.read(a.start);assert old['targetSHA256']==core.identity and old['spans']==a.spans and old['modes']==a.modes and old['baseSpatialSHA256']==base.sha(a.spatial);z=np.array(old['coefficients'])
    hist=[];tries=[];rng=np.random.default_rng(881321)
    for step in range(a.steps):
        far=Far(core.j+b.apply(z),core.s,core.u,a.far_radius);before=core.summary(z,far);op,res=core.linear(z,far)
        if step==0:
            d=rng.normal(size=b.size);d/=np.linalg.norm(d);v=rng.normal(size=len(res));v/=np.linalg.norm(v)
            l=op.matvec(d)@v;r=d@op.rmatvec(v);ae=abs(l-r)/max(1e-12,abs(l),abs(r));assert ae<2e-8,(l,r,ae)
            h=1e-5;dz=b.pre(d);fm=core.summary(z-h*dz,far)['merit'];fp=core.summary(z+h*dz,far)['merit'];der=2*res@op.matvec(d);de=abs((fp-fm)/(2*h)-der)/max(1.,abs(der));assert de<1e-5,de
            baseline=before;aud=[float(ae),float(de)]
        lin=lsmr(op,-res,damp=a.damping,atol=1e-6,btol=1e-6,maxiter=a.linear_iterations)
        direction=b.pre(lin[0]);accepted=None;trial=[]
        for alpha in (1.,.5,.25,.125,.0625,.03125,.015625,.0078125,.00390625,.001953125):
            candidate=z+alpha*direction;own=core.summary(candidate,far);trial.append([alpha,own])
            if own['merit']<before['merit'] and own['kappa']<=a.kappa and own['held']>=a.held_gate and own['farNormalRatio']>=a.far_gate and own['sampledClosedCapMaximum']<.635:
                z=candidate;accepted=own;break
        tries.append(dict(step=step+1,linearIterations=int(lin[2]),normalResidual=float(lin[4]),trials=trial))
        print(step+1,int(lin[2]),alpha,accepted,flush=True)
        if accepted is None:break
        hist.append(accepted)
    out=dict(entrySHA256=base.sha(__file__),baseSpatialSHA256=base.sha(a.spatial),originalFieldSHA256=base.sha(a.field),clockSHA256=base.sha(a.clock) if a.clock else None,targetSHA256=core.identity,spans=a.spans,modes=a.modes,fullCosSinXYZ=True,physicalControls=b.size,grid=[a.radials,a.angles],ownNewAccepted=len(hist),originalFourteenRowsPerGridPoint=True,adjointAndPhysicalDerivative=aud,starting=baseline,history=hist,allTrials=tries,coefficients=z.tolist())
    base.stores(a.output,out)
if __name__=='__main__':
    p=argparse.ArgumentParser()
    for k in ('scripts','ramp','coast','prepared','independent','seed-design','donor','donor-field','frozen','state','field','spatial','closed','clock','start','output'):p.add_argument('--'+k,type=Path)
    for k,v in [('radials',145),('angles',112),('spans',36),('modes',20),('steps',5),('linear-iterations',80)]:p.add_argument('--'+k,type=int,default=v)
    for k,v in [('curvature',1.),('geometry',20.),('far-radius',.1005),('far-weight',12000.),('held-target',.6535),('held-weight',30000.),('kappa',10.38),('held-gate',.65),('far-gate',.0973),('damping',.004)]:p.add_argument('--'+k,type=float,default=v)
    run(p.parse_args())
