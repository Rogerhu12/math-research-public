#!/usr/bin/env python3
"""Add true-material D3 position modes to a frozen R262 cut state, retaining its complete native-angle position field and fixed metric."""
import argparse,hashlib,importlib.util,json,os,sys
from pathlib import Path
for key in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','MKL_NUM_THREADS'):os.environ[key]='1'
import numpy as np
from scipy.interpolate import BSpline
from scipy.sparse.linalg import lsmr,LinearOperator

def module(path,name):
    spec=importlib.util.spec_from_file_location(name,path);m=importlib.util.module_from_spec(spec);sys.modules[name]=m;spec.loader.exec_module(m);return m
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def channels(m):
    return [('plane',j) for j in range(-m,m+1) if j%3==1]+[('height',j) for j in range(0,m+1,3)]

class Model:
    def __init__(self,ref,api,micro,src,geo,a,kn,oldkn,oldX,metric,nr,nu,shift):
        G=ref.cut_grid(api,micro,src,geo,a,kn,metric,nr,nu,shift)
        self.G=G;self.micro=micro
        self.B=api.Bvals(G.t*src.S,kn)
        old=api.Bvals(G.t*src.S,oldkn);mold=(oldX.shape[1]-2)//3
        self.base=G.base
        for i,(r,d) in enumerate(src.base.O):
            self.base[:,i]+=micro.fft_forward(old[r]@oldX,mold,nu,G.offset,d)
        self.Q=(1+G.M@np.asarray(metric['q']))[:,None]
        self.W=(1+G.M@np.asarray(metric['w']))[:,None];self.rho=G.rho
        if min(self.Q.min(),self.W.min())<=0:raise ValueError('Nonpositive frozen metric')
        pp,dd=[np.asarray(src.center.base.derivative(G.u,r),float) for r in (1,2)]
        v=np.linalg.norm(pp,axis=1);vv=np.sum(pp*dd,axis=1)/v;u=src.center.arc(G.u)
        self.u=u;self.ch=channels(a.material_modes)
        self.phi=np.zeros((3,3,len(self.ch),nu))
        for j,(tag,m) in enumerate(self.ch):
            co=np.cos(m*u);si=np.sin(m*u)
            if tag=='plane':
                for z,(p,p1) in enumerate(((co,-si),(si,co))):
                    self.phi[0,z,j]=p
                    self.phi[1,z,j]=m*v*p1
                    self.phi[2,z,j]=-(m*v)**2*p+m*vv*p1
            else:
                self.phi[0,2,j]=co
                self.phi[1,2,j]=-m*v*si
                self.phi[2,2,j]=-(m*v)**2*co-m*vv*si
        self.shape=(self.B[0].shape[1],len(self.ch));self.nvar=int(np.prod(self.shape))
        self.orders=src.base.O
    def forward_field(self,x,r,d):
        C=self.B[r]@x
        return np.stack([C@self.phi[d,j] for j in range(3)],axis=-1)
    def planes(self,v,d):
        return sum((v[:,:,j]@self.phi[d,j].T for j in range(3)))
    def first(self,x):
        return self.base[:,1]+self.forward_field(x,1,0),self.base[:,2]+self.forward_field(x,0,1)
    def metrics(self,x):
        v,u=self.first(x);z=self.Q;w=self.W;rho=self.rho
        e=np.sum(v*v,axis=-1)/z-1
        g=np.sum(u*u,axis=-1)/(rho*rho*w)-1
        f=np.sum(v*u,axis=-1)/(rho*np.sqrt(z*w))
        return v,u,np.stack((e,np.sqrt(2)*f,g)),abs(e+g)/2+np.hypot((e-g)/2,f)
    def report(self,x):
        J=self.base.copy()
        for i,(r,d) in enumerate(self.orders):J[:,i]+=self.forward_field(x,r,d)
        _,err,_=self.micro.gram(J,self.Q,self.W,self.rho)
        cur,ar=self.micro.curvature(J)
        normal=np.cross(J[:,2],J[:,1]);normal/=np.sqrt(ar)[...,None]
        sig=np.sum(normal*J[:,0],axis=-1)
        ix=np.unravel_index(np.argmax(err),err.shape);iy=np.unravel_index(np.argmax(cur),err.shape)
        return dict(peak=float(err[ix]),rms=float(np.mean(err**2)**.5),curvature=float(cur[iy]),
            worstMetric=[float(self.G.t[ix[0]]*self.G.source.S),float(self.G.u[ix[1]]),float(self.u[ix[1]])],
            worstCurvature=[float(self.G.t[iy[0]]*self.G.source.S),float(self.G.u[iy[1]]),float(self.u[iy[1]])],
            minimumSupport=float(sig.min()),minimumZs=float(J[:,1,:,2].min()),minimumArea=float(np.sqrt(ar).min()))
    def linear(self,x,power):
        v,u,res,err=self.metrics(x);weight=(np.maximum(.04,err/max(float(err.max()),1e-30))**power)/np.sqrt(err.size)
        z=self.Q;w=self.W;rho=self.rho;cross=np.sqrt(2)/(rho*np.sqrt(z*w))
        B0,B1=self.B[:2]
        diagonal=np.empty(self.shape)
        for j in range(len(self.ch)):
            h=self.phi[0,:,j].T;hp=self.phi[1,:,j].T
            av=np.sum(v*h[None],axis=-1)*2/z*weight
            au=np.sum(u*h[None],axis=-1)*cross*weight
            bv=np.sum(v*hp[None],axis=-1)*cross*weight
            bu=np.sum(u*hp[None],axis=-1)*2/(rho*rho*w)*weight
            diagonal[:,j]=(B1*B1).T@np.sum(av*av+au*au,axis=1)+(B0*B1).T@np.sum(2*au*bv,axis=1)+(B0*B0).T@np.sum(bv*bv+bu*bu,axis=1)
        scale=1/np.sqrt(np.maximum(1e-25,diagonal))
        def mv(x):
            y=x.reshape(self.shape)*scale;dv=self.forward_field(y,1,0);du=self.forward_field(y,0,1)
            e=2*np.sum(v*dv,axis=-1)/z
            f=cross*(np.sum(u*dv,axis=-1)+np.sum(v*du,axis=-1))
            g=2*np.sum(u*du,axis=-1)/(rho*rho*w)
            return (np.stack((e,f,g))*weight[None]).ravel()
        def tm(y):
            e,f,g=y.reshape(res.shape)*weight[None]
            av=(2*e/z)[...,None]*v+(f*cross)[...,None]*u
            au=(f*cross)[...,None]*v+(2*g/(rho*rho*w))[...,None]*u
            return (scale*(B1.T@self.planes(av,0)+B0.T@self.planes(au,1))).ravel()
        op=LinearOperator((res.size,self.nvar),matvec=mv,rmatvec=tm,dtype=float)
        return op,(res*weight[None]).ravel(),scale

def main():
    p=argparse.ArgumentParser()
    for key in ('scripts','work','physical-source','refinement-source','comparison','native-state','out'):
        p.add_argument('--'+key,type=Path,required=True)
    p.add_argument('--material-parent',type=Path);p.add_argument('--split',action='store_true')
    for key,d in (('material-modes',33),('angles',195),('test-angles',291),('radial',78),('test-radial',119),('steps',5),('iterations',130)):
        p.add_argument('--'+key,type=int,default=d)
    p.add_argument('--curvature-guide',type=float,default=8.69)
    a=p.parse_args()
    ref=module(a.refinement_source,'dense_true_cut_grid');api=module(a.physical_source,'true_cut_R262_source')
    micro=module(a.scripts/'2ecf-r262-small-input-full-xyz-positive-metric-v2.py','original_native_R262')
    geo=module(a.comparison,'true_threefold_angle')
    with np.load(a.native_state,allow_pickle=False) as z:
        ref.action_args(a,z)
        if 'heightDropEnd' in z:raise ValueError('Require the full-size cut branch')
        oldX=z['actualPhysicalXYZ'].copy();oldkn=z['knots'].copy();a.modes=int(z['modes']);a.spans=int(z['spans'])
        mk=z['metricKnots'].copy() if 'metricKnots' in z else oldkn;metric=dict(knots=mk.tolist(),q=z['metricQ'].tolist(),w=z['metricW'].tolist())
    geo.LOW=a.low;geo.HIGH=(geo.P-geo.LOW*(geo.L0+geo.TAU))/(geo.L1+geo.TAU)
    src=micro.Source(a);ch=channels(a.material_modes)
    if a.material_parent:
        with np.load(a.material_parent,allow_pickle=False) as z:
            if str(z['nativeStateSHA'])!=sha(a.native_state) or str(z['entrySHA'])!=sha(__file__):raise ValueError('Different native position or correction definition')
            kn=z['knots'].copy();C=z['materialCoefficients'].copy();cm=int(z['materialModes'])
            if cm>a.material_modes:raise ValueError('Old material modes not contained')
            cols=channels(cm);X=np.zeros((len(C),len(ch)))
            for j,k in enumerate(cols):X[:,ch.index(k)]=C[:,j]
    else:
        kn=oldkn.copy();X=np.zeros((len(kn)-12,len(ch)))
    if a.split:
        spline=BSpline(kn,np.pad(X,((3,3),(0,0))),5,axis=0)
        unique=np.unique(kn)
        for k in unique[:-1]+np.diff(unique)/2:spline=spline.insert_knot(k)
        kn=spline.t.copy();X=spline.c[3:-3].copy()
    G=Model(ref,api,micro,src,geo,a,kn,oldkn,oldX,metric,a.radial,a.angles,False)
    T=Model(ref,api,micro,src,geo,a,kn,oldkn,oldX,metric,a.test_radial,a.test_angles,True)
    init=G.report(X);ind0=T.report(X);hist=[]
    for j in range(a.steps):
        bef=G.report(X);_,_,_,e0=G.metrics(X);pwr=6
        val0=float(np.mean(e0**pwr)**(1/pwr));lin,r,scale=G.linear(X,.5 if j<2 else .9);best=None
        # Finite adjoint identity on the first actual linearization.
        if j==0:
            rng=np.random.default_rng(20261128);h=rng.standard_normal(G.nvar);v=rng.standard_normal(len(r))
            lhs=np.dot(lin@h,v);rhs=np.dot(h,lin.rmatvec(v))
            adjoint=float(abs(lhs-rhs)/max(1.,abs(lhs),abs(rhs)))
            if adjoint>1e-10:raise ArithmeticError('Material Jacobian transpose mismatch')
        for damp in (2e-6,5e-5,.001):
            dx=scale*lsmr(lin,-r,damp=damp,atol=2e-10,btol=2e-10,maxiter=a.iterations)[0].reshape(G.shape)
            for alpha in (1.,.5,.25,.125,.0625):
                y=X+alpha*dx;e=G.metrics(y)[3];pk=float(e.max());val=float(np.mean(e**pwr)**(1/pwr))
                if val>=val0 or pk>=bef['peak']:continue
                report=G.report(y)
                if report['curvature']>max(a.curvature_guide,bef['curvature']+1e-5):continue
                score=val+.15*pk
                if best is None or score<best[0]:best=(score,y,report,alpha,damp)
        if not best:break
        _,X,rep,alpha,damp=best;hist.append(dict(step=j+1,alpha=alpha,damping=damp,actual=rep));print('MATERIAL',j+1,rep,flush=True)
    state=a.out.with_suffix('.npz')
    with state.open('xb') as f:np.savez_compressed(f,nativeStateSHA=sha(a.native_state),entrySHA=sha(__file__),knots=kn,materialModes=a.material_modes,materialCoefficients=X)
    out=dict(schema='true-cut-fixed-metric-full-native-position-plus-physical-material-D3-modes-v1',entrySHA256=sha(__file__),nativeStateSHA256=sha(a.native_state),fieldSHA256=src.source_sha,materialParentSHA256=sha(a.material_parent) if a.material_parent else None,stateSHA256=sha(state),actualMetricVariables=0,materialPositionVariables=G.nvar,materialModes=a.material_modes,radialSpans=len(np.unique(kn))-1,initial=init,initialIndependent=ind0,training=G.report(X),independent=T.report(X),accepted=hist,adjointRelativeDifference=adjoint if a.steps else None,scope='All native Cartesian coefficients, both fixed radial metric functions, the true arcs, the nonzero operating phase, both ports, and the original tail are retained. The new physical position component uses only the true material arclength angle.')
    with a.out.open('x') as f:json.dump(out,f,indent=2);f.write('\n')
    print('END_MATERIAL',out['independent'],flush=True)
if __name__=='__main__':main()
