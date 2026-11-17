#!/usr/bin/env python3
"""Canonical shared-two-jet C2 representative of a successful prefix checkpoint.

The checkpoint already stores a quintic Hermite reconstruction, not solve_bvp's
C1 cubic. To remove any ambiguity caused by independently rounded expanded
PPoly coefficients, this module interprets one binary64 value/first/second jet
per knot as the defining data. On each interval the mathematical representative
is the unique degree <=5 polynomial with those endpoint jets. Its C2 matching
is an algebraic identity; small numerical jumps are not used as a regularity
argument. Evaluation uses normalized Hermite residuals in long double.

The full Cartesian map also uses a shared-two-jet quintic for its mean height.
Its knot values come from Gauss integration of the mean Frenet velocity, and
its first/second knot jets from that velocity and its derivative. Thus the
final finite representation is C2 by algebra, without needing an unverified
interpolation across samples. This remains an OPEN prefix with a finite linear
terminal port.
"""
import os
for _k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[_k]='1'
import argparse, hashlib, importlib.util, inspect, json, math, time
from pathlib import Path
from types import SimpleNamespace
import numpy as np
from scipy.interpolate import PPoly

class SharedJetQuintic:
    """Exact model: common endpoint jets and the normalized Hermite basis.

    Jets have shape (3, nstate, nknots). Treat their finite float entries as
    exact real constants when defining the map. The evaluator is approximate.
    """
    def __init__(self, x, jets):
        self.x=np.asarray(x,dtype=float)
        self.jets=np.asarray(jets,dtype=float)
        if self.jets.ndim!=3 or self.jets.shape[0]!=3 or self.jets.shape[2]!=len(self.x):
            raise ValueError('Expected shared jets[3, state, knot].')
        if not np.all(np.diff(self.x)>0):
            raise ValueError('Strictly increasing knots required.')
        j=np.asarray(self.jets,dtype=np.longdouble);h=np.diff(self.x).astype(np.longdouble)[None,:]
        y,d,q=j
        e0=y[:,1:]-y[:,:-1]-h*d[:,:-1]-h*h*q[:,:-1]/2
        e1=d[:,1:]-d[:,:-1]-h*q[:,:-1]
        e2=q[:,1:]-q[:,:-1]
        self._normalized=np.stack((y[:,:-1],h*d[:,:-1],h*h*q[:,:-1]/2,
             10*e0-4*h*e1+h*h*e2/2,
             -15*e0+7*h*e1-h*h*e2,
             6*e0-3*h*e1+h*h*e2/2))
    @classmethod
    def from_ppoly(cls, pp):
        return cls(pp.x,np.stack([pp(pp.x,k) for k in range(3)]))
    def __call__(self, x, nu=0):
        if not 0<=nu<=5:raise ValueError('Only derivatives 0 through 5 are implemented.')
        inp=np.asarray(x,dtype=float);flat=inp.reshape(-1)
        if np.any(flat<self.x[0]) or np.any(flat>self.x[-1]):
            raise ValueError('No extrapolation is part of the representative.')
        i=np.clip(np.searchsorted(self.x,flat,side='right')-1,0,len(self.x)-2)
        h=(self.x[i+1]-self.x[i]).astype(np.longdouble)
        t=(flat.astype(np.longdouble)-self.x[i].astype(np.longdouble))/h
        c=self._normalized[:,:,i]
        v=np.zeros(c.shape[1:],dtype=np.longdouble)
        for degree in range(5,nu-1,-1):
            factor=math.factorial(degree)//math.factorial(degree-nu)
            v=v*t[None,:]+factor*c[degree]
        v/=h[None,:]**nu
        out=np.asarray(v,dtype=float)
        # The endpoint value of each of the first three jets is its one shared
        # datum. This is also exactly the endpoint identity of the Hermite basis.
        if nu<=2:
            k=np.searchsorted(self.x,flat,side='left')
            exact=(k<len(self.x)) & (self.x[np.minimum(k,len(self.x)-1)]==flat)
            out[:,exact]=self.jets[nu,:,k[exact]].T
        return out.reshape((out.shape[0],)+inp.shape)

def load_model(recovery,checkpoint,port_path,angular=1536):
    recovery=Path(recovery);checkpoint=Path(checkpoint);port_path=Path(port_path)
    source=recovery/'bundle/topics/visible-flexible-closed-surface'
    comp=recovery/'bundle/topics/visible-flex-larger-amplitude/computations'
    spec=importlib.util.spec_from_file_location('smallcut_numerical_c2',comp/'numerical-m2-prefix.py')
    mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)
    ad=mod.load(source);short=mod.source_module('smallcut_bridge_c2',comp/'root_short_bridge.py');short.install()
    from curve_stable_prefix_bvp import load_checkpoint
    r=load_checkpoint(checkpoint)
    if not r.get('solver_success'):raise ValueError('Successful checkpoint required.')
    port=json.loads(port_path.read_text());port['cut']['_prefix_bridge']=r['frozen_profile']['prefix_bridge']
    if port['parameters']!=r['physical_tail_parameters'] or port['cut']!=r['physical_tail_cut']:
        raise ValueError('Physical port mismatch.')
    _,BVP=ad.build_classes(r['chart'])
    obj=BVP(r['frozen_profile'],port,r['gauge_amplitude'],r['config']['modes'],angular,True,r['warp_reference_q'])
    par=np.array(r['parameters']);par[0]=math.log(r['actual_primary_amplitude']/obj.q)
    obj.initial(par);flow=obj.flow(par[0])
    old=PPoly.construct_fast(np.asarray(r['pp_coefficients']),np.asarray(r['mesh']),extrapolate=False,axis=1)
    rep=SharedJetQuintic.from_ppoly(old)
    sol=SimpleNamespace(x=rep.x,y=rep(rep.x),p=par,sol=rep)
    return r,obj,flow,sol,old,ad

def original_coefficient_jumps(pp):
    """Roundoff in expanded-polynomial joins; NOT a C2 acceptance test."""
    out=[];h=np.diff(pp.x).astype(np.longdouble);c=np.asarray(pp.c,dtype=np.longdouble)
    for nu in range(3):
        v=np.zeros(c.shape[1:],dtype=np.longdouble)
        for row in range(6-nu):
            degree=5-row
            factor=math.factorial(degree)//math.factorial(degree-nu)
            v=v*h[:,None]+factor*c[row]
        right=np.asarray(pp(pp.x[1:],nu),dtype=np.longdouble).T
        out.append(np.max(np.abs(v-right),axis=0))
    return np.array(out)

def build_mean(flow,sol,angular=1536,order=8):
    """Define a finite C2 mean coordinate from one shared two-jet per knot."""
    s=sol.x
    height=flow.height_integral(sol,s,angular,order)
    mu=np.empty(len(s));mup=np.empty(len(s));_,B1,B2=flow.basis(angular)
    for first in range(0,len(s),32):
        sl=slice(first,first+32);t=s[sl]
        fr,_,dW=flow.velocity_s(t,sol.sol(t),sol.sol(t,1),B1,B2)
        mu[sl]=np.mean(fr['V'][:,:,2],axis=1)
        mup[sl]=np.mean(dW[:,:,2],axis=1)
    return SharedJetQuintic(s,np.stack((height,mu,mup))[:,None,:])

def audit_explicit_mean(ad,obj,sol,angular):
    """Run the original tensor audit on the actual explicit C2 mean spline.

    Only the three mean coordinate evaluations change. No source file or
    metric/curvature formula is edited.
    """
    source=inspect.getsource(ad.audit)
    replacements=[
      ('hh=flow.height_integral(sol,ss,N,6)','hh=sol.mean_spline(ss)[0]'),
      ("np.mean(fr['V'][:,:,2],axis=1)[:,None]",'sol.mean_spline(s,1)[0,:,None]'),
      ('np.mean(dW[:,:,2],axis=1)[:,None]','sol.mean_spline(s,2)[0,:,None]')]
    for before,after in replacements:
        if source.count(before)!=1:raise ValueError('Unexpected upstream audit; refusing an adaptive replacement.')
        source=source.replace(before,after)
    namespace=dict(ad.__dict__);exec(compile(source,'<shared-jet-mean-audit>','exec'),namespace)
    return namespace['audit'](obj,sol,angular)

def endpoint(flow,sol,q,N=512,order=8):
    s=np.array([flow.end]);B,B1,B2=flow.basis(N)
    Y,Yp,Ypp=[sol.sol(s,k) for k in range(3)]
    fr,Xsp,dW=flow.velocity_s(s,Y,Yp,B1,B2);g=fr['geo']
    explicit=getattr(sol,'mean_spline',None)
    height=flow.height_integral(sol,s,N,order)[0] if explicit is None else explicit(s)[0,0]
    mean1=np.mean(fr['V'][:,:,2]) if explicit is None else explicit(s,1)[0,0]
    mean2=np.mean(dW[:,:,2]) if explicit is None else explicit(s,2)[0,0]
    X=(g['pos']+q*flow.values(Y,B))[0];X[:,2]+=height
    Xs=(g['s1']+q*flow.values(Yp,B))[0];Xs[:,2]+=mean1
    Xss=(g['s2']+q*flow.values(Ypp,B))[0];Xss[:,2]+=mean2
    return dict(theta=2*np.pi*np.arange(N)/N,X=X,Xs=Xs,Xss=Xss,
        Xtheta=fr['d'][0],Xthetatheta=fr['dd'][0],Xstheta=Xsp[0])

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--recovery',type=Path,required=True);p.add_argument('--checkpoint',type=Path,required=True)
    p.add_argument('--port',type=Path,required=True);p.add_argument('--output',type=Path,required=True)
    p.add_argument('--angular',type=int,default=1536);p.add_argument('--endpoint-angular',type=int,default=512)
    a=p.parse_args();beg=time.time()
    r,obj,flow,sol,old,ad=load_model(a.recovery,a.checkpoint,a.port,a.angular)
    js=original_coefficient_jumps(old)
    probes=np.unique(np.r_[sol.x,(sol.x[:-1]+sol.x[1:])/2])
    differences=[float(np.max(np.abs(sol.sol(probes,k)-old(probes,k)))) for k in range(3)]
    sol.mean_spline=build_mean(flow,sol,a.angular,8)
    audit=audit_explicit_mean(ad,obj,sol,a.angular)
    ep=endpoint(flow,sol,obj.q,a.endpoint_angular)
    oldsol=SimpleNamespace(x=old.x,y=old(old.x),p=sol.p,sol=old)
    oldep=endpoint(flow,oldsol,obj.q,a.endpoint_angular)
    a.output.parent.mkdir(parents=True,exist_ok=True)
    endpoint_path=a.output.with_name(a.output.stem+'-endpoint.npz')
    np.savez_compressed(endpoint_path,**ep)
    data_hash=hashlib.sha256(np.ascontiguousarray(sol.sol.x).tobytes()+np.ascontiguousarray(sol.sol.jets).tobytes()+np.ascontiguousarray(sol.mean_spline.jets).tobytes()).hexdigest()
    mean_errors=[0.,0.]
    _,B1,B2=flow.basis(a.angular)
    for first in range(0,len(probes),32):
        t=probes[first:first+32]
        fr,_,dW=flow.velocity_s(t,sol.sol(t),sol.sol(t,1),B1,B2)
        mean_errors[0]=max(mean_errors[0],float(np.max(np.abs(sol.mean_spline(t,1)[0]-np.mean(fr['V'][:,:,2],axis=1)))))
        mean_errors[1]=max(mean_errors[1],float(np.max(np.abs(sol.mean_spline(t,2)[0]-np.mean(dW[:,:,2],axis=1)))))
    out=dict(scope=__doc__,checkpoint_sha256=hashlib.sha256(a.checkpoint.read_bytes()).hexdigest(),
        script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),shared_jet_data_sha256=data_hash,
        polynomial_degree=5,knots=len(sol.x),state_count=sol.y.shape[0],
        c2_reason='Single shared 2-jet at every knot; unique quintic Hermite interpolation. Exact symbolic endpoint identities, not a small-jump criterion.',
        mean_coordinate='Shared-two-jet quintic: knot heights from segment Gauss quadrature; first and second knot derivatives from finite-angle mean W_z and dW_z. This finite mean spline is C2 algebraically.',
        mean_angular=a.angular,mean_gauss_order=8,
        mean_first_second_derivative_departure_at_probes=mean_errors,
        original_expanded_ppoly_max_join_roundoff=np.asarray(js.max(axis=1),float).tolist(),
        original_expanded_ppoly_cartesian_join_l1_bounds=np.asarray(obj.q*js.sum(axis=1),float).tolist(),
        shared_jet_vs_old_probe_derivative_max=differences,
        audit=audit,endpoint=dict(path=endpoint_path.name,sha256=hashlib.sha256(endpoint_path.read_bytes()).hexdigest(),
        angular=a.endpoint_angular,mean_X=ep['X'].mean(axis=0).tolist(),mean_Xs=ep['Xs'].mean(axis=0).tolist(),mean_Xss=ep['Xss'].mean(axis=0).tolist(),
        max_vector_changes={k:float(np.linalg.norm(ep[k]-oldep[k],axis=-1).max()) for k in ['X','Xs','Xss']}),seconds=time.time()-beg)
    a.output.write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(dict(event='c2_representative_audit',metric_l1=audit['metric_l1'],kappa=audit['kappa_sample'],root=audit['root_min'],
        derivative_changes=differences,endpoint_changes=out['endpoint']['max_vector_changes'],seconds=out['seconds'])),flush=True)
if __name__=='__main__':main()
