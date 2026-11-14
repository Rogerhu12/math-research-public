#!/usr/bin/env python3
"""R139 exact native l,m,n propagation on a fixed positive-slope K=0 coast.

The formula solves Gauss-Codazzi for arbitrary smooth periodic positive
inlet n and arbitrary m before the ruling focus.  It does not assert that
an arbitrary inlet angular frame/position has trivial monodromy.  The
bundled saved-data reader is bound to the new34 base metric, delta=0.
"""
from __future__ import annotations
import os
for _key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[_key]='1'
import argparse,hashlib,json,time
from pathlib import Path
import numpy as np
from scipy import fft
from fd2d_k0_ruling_coast import ruling_coordinates
from fd2d_balanced_curvature_core import FixedBalancedGeometry


def digest(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def native_from_inlet(a_c,v,sigma,data):
    """Return l,m,n and native first s/u jets at one incoming material label."""
    n0,m0,nt0,mt0,ntt0,mtt0=(np.asarray(data[k]) for k in ('n','m','n_u','m_u','n_uu','m_uu'))
    if np.any(n0<=0):raise ValueError('Positive inlet n is required')
    k=m0/n0;kt=mt0/n0-m0*nt0/n0**2
    ktt=mtt0/n0-m0*ntt0/n0**2-2*mt0*nt0/n0**2+2*m0*nt0**2/n0**3
    c=ruling_coordinates(a_c,v,sigma,k,kt,ktt)
    r0=a_c/v;r=r0+sigma;Q=c['A'];D=c['D'];w=c['w'];B=v*(1+k*k)-kt
    n=a_c*n0*Q*Q/(D*r*r);ratio=k*r0/Q;m=n*ratio;l=n*ratio*ratio
    Qs=(1+k*k)*c['raw_w_s']
    Qt=2*k*kt*w+(1+k*k)*c['raw_w_t']
    Ds=B*c['raw_w_s'];Dt=B*c['raw_w_t']+w*(2*v*k*kt-ktt)
    ns_label=n*(2*Qs/Q-Ds/D-2/r)
    nt=n*(nt0/n0+2*Qt/Q-Dt/D)
    ratio_s=-ratio*Qs/Q;ratio_t=r0*kt/Q-ratio*Qt/Q
    ms_label=ns_label*ratio+n*ratio_s;mt=nt*ratio+n*ratio_t
    lt=nt*ratio*ratio+2*n*ratio*ratio_t
    ns=ns_label+nt*c['inlet_t_s'];ms=ms_label+mt*c['inlet_t_s']
    nu=nt*c['inlet_t_u'];mu=mt*c['inlet_t_u'];lu=lt*c['inlet_t_u']
    radius=a_c+v*sigma;connection=v/radius
    return dict(l=l,m=m,n=n,n_s=ns,m_s=ms,n_u=nu,m_u=mu,l_u=lu,
        material_u=np.asarray(data['u'])+c['material_shift'],inlet_u=np.asarray(data['u']),
        D=D,Q=Q,ruling_w=w,new_ratio=ratio,
        gauss_residual=l*n-m*m,
        codazzi_m=ms-lu/radius+2*connection*m,
        codazzi_n=ns-mu/radius-connection*(l-n),
        nonzero_curvature=l+n,scalar_radius=radius,
        exact_formula=True,global_position_compatibility_inferred=False)


class SavedNativeCoast:
    """Evaluate the actual finite inlet Fourier functions in fixed material u."""
    def __init__(self,inlet_path,geometry=None):
        self.path=Path(inlet_path);p=np.load(self.path,allow_pickle=False)
        self.a,self.v,self.length=(float(p[k]) for k in ('a','v','coast_length'))
        self.entry_s=float(p['entry_s']);self.candidate_sha256=str(p['candidate_sha256'].item())
        self.n=np.asarray(p['n_phi_cos'],np.longdouble);self.m=np.asarray(p['m_phi_sin'],np.longdouble)
        self.f=np.asarray(p['frequencies'],np.longdouble)
        self.geometry=geometry or FixedBalancedGeometry();self.inverse_input_error=0.

    def inlet(self,u):
        u=np.asarray(u,np.longdouble);phi=self.geometry.normal_angle(u)
        C=np.cos(phi[...,None]*self.f);S=np.sin(phi[...,None]*self.f)
        n=C@self.n;m=S[...,1:]@self.m
        np1=-S@(self.f*self.n);mp1=C[...,1:]@(self.f[1:]*self.m)
        np2=-C@(self.f*self.f*self.n);mp2=-S[...,1:]@(self.f[1:]**2*self.m)
        chart=self.geometry.material_coordinate(phi);h,hp=chart['u_phi'],chart['u_phi_phi']
        self.inverse_input_error=max(self.inverse_input_error,float(np.max(abs(chart['u']-u))))
        return dict(u=u,n=n,m=m,n_u=np1/h,m_u=mp1/h,
            n_uu=(np2-hp*np1/h)/(h*h),m_uu=(mp2-hp*mp1/h)/(h*h))

    def evaluate(self,sigma,u,tolerance=2e-13,max_iterations=60):
        sigma=float(sigma)
        if not 0<=sigma<=self.length:raise ValueError('Outside the frozen physical coast')
        target=np.asarray(u,np.longdouble)
        if sigma==0:
            out=native_from_inlet(self.a,self.v,sigma,self.inlet(target));out['inverse_iterations']=0;return out
        width=np.pi/(2*self.v)+1e-8;lo=target-width;hi=target+width;t=target.copy()
        for iteration in range(max_iterations):
            data=self.inlet(t);n,m=data['n'],data['m'];k=m/n
            kt=data['m_u']/n-m*data['n_u']/n**2
            coordinates=ruling_coordinates(self.a,self.v,sigma,k,kt,np.zeros_like(k))
            residual=t+coordinates['material_shift']-target;done=abs(residual)<=tolerance
            if np.all(done):
                out=native_from_inlet(self.a,self.v,sigma,data)
                out['inverse_iterations']=iteration+1;return out
            lo=np.where(residual<0,t,lo);hi=np.where(residual>0,t,hi)
            trial=t-residual/coordinates['U_t']
            t=np.where(done,t,np.where((trial<=lo)|(trial>=hi),(lo+hi)/2,trial))
        raise RuntimeError('Native material inverse did not reach its explicit tolerance')


def main():
    ap=argparse.ArgumentParser(description=__doc__);root=Path(__file__).resolve().parent.parent
    ap.add_argument('--inlet',type=Path,default=root/'notes/2026-11-12-fd2d-peak-spacer-ruling-consumer-01-inlet.npz')
    ap.add_argument('--cartesian-endpoint',type=Path,default=root/'notes/2026-11-12-fd2d-peak-spacer-ruling-consumer-01-endpoint.npz')
    ap.add_argument('--work',type=int,default=768);ap.add_argument('--radial-nodes',type=int,default=9)
    ap.add_argument('--stem',type=Path,required=True);args=ap.parse_args()
    if list(args.stem.parent.glob(args.stem.name+'*')):raise FileExistsError('Use a new native-field output stem')
    start=time.monotonic();coast=SavedNativeCoast(args.inlet)
    phi=np.arange(args.work,dtype=np.longdouble)*(2*np.arccos(np.longdouble(-1))/args.work)
    u=coast.geometry.material_coordinate(phi)['u'];rows=[];fields=[];ns=[];ms=[]
    for sigma in np.linspace(0,coast.length,args.radial_nodes):
        q=coast.evaluate(float(sigma),u);field=np.stack((q['l'],q['m'],q['n']),axis=-1)
        fields.append(np.asarray(field,float));ns.append(np.asarray(q['n_s'],float));ms.append(np.asarray(q['m_s'],float))
        rows.append(dict(sigma=float(sigma),physical_s=coast.entry_s+float(sigma),
            D_min=float(np.min(q['D'])),n_min=float(np.min(q['n'])),curvature_max=float(np.max(q['nonzero_curvature'])),
            gauss_residual=float(np.max(abs(q['gauss_residual']))),codazzi_m=float(np.max(abs(q['codazzi_m']))),
            codazzi_n=float(np.max(abs(q['codazzi_n']))),material_inverse_residual=float(np.max(abs(q['material_u']-u))),
            inverse_iterations=q['inverse_iterations']))
    fields=np.asarray(fields);raw=fft.rfft(fields,axis=1,norm='forward');projection=[]
    for mode in (15,31,63,95,191):
        small=raw.copy();small[:,mode+1:]=0
        reconstructed=fft.irfft(small,n=args.work,axis=1,norm='forward')
        projection.append(dict(maximum_mode=mode,value_projection_error_max=float(np.max(abs(fields-reconstructed))),
            component_errors=np.max(abs(fields-reconstructed),axis=(0,1)).tolist(),
            scope='Only a finite-value projection diagnostic, not a solved finite BVP or discarded-equation certificate.'))
    comparison=None
    if args.cartesian_endpoint.exists():
        previous=np.load(args.cartesian_endpoint,allow_pickle=False)
        if len(previous['phi'])==args.work:
            comparison={key:float(np.max(abs(fields[-1,:,j]-previous[key]))) for j,key in enumerate(('l','m','n'))}
    arrays=args.stem.with_name(args.stem.name+'-field.npz')
    np.savez_compressed(arrays,phi=np.asarray(phi,float),material_u=np.asarray(u,float),
        physical_s=coast.entry_s+np.linspace(0,coast.length,args.radial_nodes),lmn=fields,
        n_s=np.asarray(ns),m_s=np.asarray(ms),candidate_sha256=coast.candidate_sha256,
        inlet_sha256=digest(args.inlet),definition='Analytic native K=0 GC field, same new34 base physical g, delta=0 only')
    report=dict(schema='fd2d-R139-native-flat-coast-GC-v1',actual_execution=True,
        source_sha256=digest(__file__),inlet_sha256=digest(args.inlet),candidate_sha256=coast.candidate_sha256,
        dependencies={name:digest(root/'scripts'/name) for name in ('fd2d_k0_ruling_coast.py','fd2d_balanced_curvature_core.py')},
        physical_metric_scope='Frozen new34 base candidate, delta=0 only; no reuse as an exact solution on modified radial-bump metrics.',
        exact_formula='Q=sqrt(rhoc^2+(1+k^2)*(rho^2-rhoc^2)); knew=k*rhoc/Q; nnew=ac*nc*Q^2/(D*rho^2); mnew=nnew*knew; lnew=nnew*knew^2.',
        a_c=coast.a,v=coast.v,coast_length=coast.length,angular_work=args.work,rows=rows,
        maximum_gauss_residual=max(r['gauss_residual'] for r in rows),
        maximum_codazzi_residual=max(max(r['codazzi_m'],r['codazzi_n']) for r in rows),
        material_provider_input_inverse_error=coast.inverse_input_error,
        finite_projection_diagnostics=projection,actual_cartesian_II_difference=comparison,
        global_position_compatibility_or_monodromy_certified=False,continuous_metric_certificate=False,
        arrays_file=arrays.name,arrays_sha256=digest(arrays),seconds=time.monotonic()-start)
    path=args.stem.with_name(args.stem.name+'-report.json');path.write_text(json.dumps(report,indent=2,allow_nan=False)+'\n')
    print(json.dumps(dict(report=str(path),sha256=digest(path),seconds=report['seconds'],
        gauss=report['maximum_gauss_residual'],codazzi=report['maximum_codazzi_residual'],
        cartesian_II_difference=comparison,projection=projection),allow_nan=False))


if __name__=='__main__':main()
