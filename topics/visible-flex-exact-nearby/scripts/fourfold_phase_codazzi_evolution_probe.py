#!/usr/bin/env python3
"""Dealiased two-field Gauss--Codazzi evolution and actual frame reconstruction.

Floating diagnostic only.  The complete physical mean is retained. Scalar
and frame nonlinearities are evaluated on a doubled grid before projection;
the Nyquist mode is omitted explicitly. Source/metric diagnostics use actual
derivatives of the reconstructed POSITION, not formally prescribed frame
jets. Every report separates finite projection defects, frame compatibility,
and denominator failures from the exact PDE identities.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import time
import numpy as np
from scipy.integrate import DOP853

from fourfold_phase_symmetric_geometry import load_exact_object
from fourfold_phase_core_low_block import uniform_fields
from fourfold_phase_local_correction_probe import (
    sha,dot,angular_derivative,scalar_target,source_and_geometry,correction_norms,
)


def scalar_derivative(v):
    f=4*np.fft.fftfreq(len(v),1/len(v))
    return np.fft.ifft(1j*f[:,None]*np.fft.fft(v,axis=0),axis=0).real


def resample(values,count):
    n=len(values);freq=np.fft.fftfreq(n,1/n).astype(int)
    c=np.fft.fft(values,axis=0)/n;out=np.zeros((count,values.shape[1]),complex)
    mask=(abs(freq)<min(n,count)//2)
    out[freq[mask]%count]=c[mask]
    return (count*np.fft.ifft(out,axis=0)).real


def normmax(v):return float(np.max(np.linalg.norm(v,axis=-1)))


class Evolution:
    # columns: m, n, F[3], X[3], Y[3], nu[3], in the rotating frame
    def __init__(self,geometry,angles,oversample):
        self.geometry=geometry;self.angles=angles;self.fine=angles*oversample
        self.calls=0

    def evaluate(self,r,y,diagnostics=False):
        state=y.reshape(self.angles,14);fine=resample(state,self.fine)
        t=scalar_target(self.geometry,float(r));rootE=np.sqrt(t['E']);a=t['a'];ap=t['a_x']
        m,n=fine[:,0],fine[:,1];F,X,Y,nu=[fine[:,j:j+3] for j in (2,5,8,11)]
        if np.min(abs(n))<1e-12:raise ValueError('angular second-form denominator n is unresolved near zero')
        ell=(t['K']+m*m)/n
        deriv=scalar_derivative(np.column_stack([m,ell]))
        full=np.zeros_like(fine)
        full[:,0]=rootE/a*deriv[:,1]-2*ap/a*m
        full[:,1]=rootE/a*deriv[:,0]+ap/a*(ell-n)
        full[:,2:5]=rootE*X
        full[:,5:8]=rootE*ell[:,None]*nu
        full[:,8:11]=rootE*m[:,None]*nu
        full[:,11:14]=-rootE*(ell[:,None]*X+m[:,None]*Y)
        result=resample(full,self.angles);self.calls+=1
        if not diagnostics:return result.ravel()
        projection_error=full-resample(result,self.fine)
        coeff=np.fft.fft(fine[:,:2],axis=0)/self.fine
        fmode=np.fft.fftfreq(self.fine,1/self.fine)
        ellc=np.fft.fft(ell)/self.fine
        data=dict(target=t,derivative=result,
            minimum_abs_n=float(np.min(abs(n))),n_min=float(np.min(n)),n_max=float(np.max(n)),
            maximum_abs_m=float(np.max(abs(m))),maximum_abs_ell=float(np.max(abs(ell))),
            characteristic_speed_max=float(np.max(rootE/a*(abs(m)+np.sqrt(max(0.,-t['K'])))/abs(n))),
            two_field_projection_defect=normmax(projection_error[:,:2]),
            frame_projection_defect=normmax(projection_error[:,5:14]),
            two_field_upper_half_coefficient_l1=float(np.sum(abs(coeff[abs(fmode)>=self.angles/4]))),
            ell_omitted_resolved_coefficient_l1=float(np.sum(abs(ellc[abs(fmode)>=self.angles/2]))))
        return data


def diagnose(evolution,r,y):
    ngrid=evolution.angles;state=y.reshape(ngrid,14)
    m,n=state[:,0],state[:,1];F,X,Y,nu=[state[:,j:j+3] for j in (2,5,8,11)]
    diag=evolution.evaluate(r,y,True);t=diag.pop('target');derivative=diag.pop('derivative')
    rootE=np.sqrt(t['E']);a=t['a'];ap=t['a_x']
    P=rootE*X;T=angular_derivative(F);M=angular_derivative(P);Q=angular_derivative(T)
    A=t['E_x']/(2*rootE)*X+rootE*derivative[:,5:8]
    updated=(F,P,T,A,M,Q);old=uniform_fields(evolution.geometry,float(r),ngrid)
    before=source_and_geometry(old,t);after=source_and_geometry(updated,t)
    V=tuple(x-o for x,o in zip(updated,old))
    frame=np.stack([X,Y,nu],axis=-1)
    orth=np.einsum('nki,nkj->nij',frame,frame)-np.eye(3)
    compatibility=[T-a*Y,
        angular_derivative(X)-(ap/rootE*Y+a*m[:,None]*nu),
        angular_derivative(Y)-(-ap/rootE*X+a*n[:,None]*nu),
        angular_derivative(nu)+a*(m[:,None]*X+n[:,None]*Y)]
    g=after['metric'];G=g[0][0]*g[1][1]-g[0][1]**2
    l2,m2,n2=[dot(after['normal'],z) for z in (A,M,Q)]
    mean=(g[1][1]*l2-2*g[0][1]*m2+g[0][0]*n2)/(2*G)
    principal=abs(mean)+np.sqrt(np.maximum(0.,mean**2-after['actual_K']))
    return dict(r=float(r),**diag,
        original_source_C0=float(np.max(abs(before['q']))),
        updated_source_C0=float(np.max(abs(after['q']))),
        updated_metric_defect_C0=float(np.max(after['metric_norm'])),
        updated_curvature_defect_C0=float(np.max(abs(after['actual_K']-after['K0']))),
        updated_absolute_principal_curvature_max=float(np.max(principal)),
        updated_support_min=float(after['support']),
        frame_orthogonality_defect=float(np.max(np.linalg.norm(orth,axis=(1,2)))),
        position_theta_compatibility=normmax(compatibility[0]),
        X_theta_compatibility=normmax(compatibility[1]),
        Y_theta_compatibility=normmax(compatibility[2]),
        normal_theta_compatibility=normmax(compatibility[3]),
        **correction_norms(V,before))


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--object',type=Path,default=Path('data/phase_ring_continuation/type_fixed_step02_d5_exact_affine_step5_object.json'))
    p.add_argument('--nodes',type=int,default=512);p.add_argument('--angles',type=int,default=512)
    p.add_argument('--oversample',type=int,default=2);p.add_argument('--right',type=float,default=.235)
    p.add_argument('--samples',type=int,default=236);p.add_argument('--rtol',type=float,default=3e-10)
    p.add_argument('--atol',type=float,default=3e-12);p.add_argument('--max-step',type=float,default=.00025)
    p.add_argument('--n-floor',type=float,default=.02);p.add_argument('--max-rhs',type=int,default=100000)
    p.add_argument('--out',type=Path,required=True);p.add_argument('--state',type=Path,required=True)
    args=p.parse_args();start=time.monotonic();last_progress=start
    geometry,definition=load_exact_object(args.object,args.nodes)
    F0,P0,T0,A0,M0,Q0=uniform_fields(geometry,0.,args.angles);t0=scalar_target(geometry,0.)
    X0=np.zeros_like(F0);X0[:,2]=1;Y0=T0/t0['a'];nu0=np.cross(Y0,X0)
    state=np.zeros((args.angles,14));state[:,1]=dot(nu0,Q0)/t0['a']**2
    state[:,2:5]=F0;state[:,5:8]=X0;state[:,8:11]=Y0;state[:,11:14]=nu0
    state=resample(state,args.angles);evolution=Evolution(geometry,args.angles,args.oversample)
    solver=DOP853(evolution.evaluate,0.,state.ravel(),args.right,rtol=args.rtol,atol=args.atol,max_step=args.max_step)
    sample_times=np.linspace(0.,args.right,args.samples);next_sample=1
    rows=[diagnose(evolution,0.,state.ravel())];status='running';exception=None
    try:
        while solver.status=='running':
            message=solver.step()
            if solver.status=='failed':status='integrator_failed: '+str(message);break
            dense=solver.dense_output()
            while next_sample<len(sample_times) and sample_times[next_sample]<=solver.t:
                rr=float(sample_times[next_sample]);rows.append(diagnose(evolution,rr,dense(rr)));next_sample+=1
            check=evolution.evaluate(solver.t,solver.y,True)
            if check['minimum_abs_n']<args.n_floor:
                status='angular_second_form_denominator_gate';break
            if evolution.calls>=args.max_rhs:
                status='diagnostic_rhs_limit';break
            now=time.monotonic()
            if now-last_progress>20:
                print({'r':solver.t,'rhs':evolution.calls,'n_min_abs':check['minimum_abs_n'],
                    'field_projection':check['two_field_projection_defect'],'elapsed':now-start},flush=True)
                last_progress=now
        if solver.status=='finished':status='finished'
    except Exception as exc:
        status='diagnostic_exception';exception=repr(exc)
    endpoint=solver.y.reshape(args.angles,14)
    if not rows or rows[-1]['r']!=float(solver.t):
        try:rows.append(diagnose(evolution,float(solver.t),solver.y))
        except Exception as exc:exception=(exception or '')+' endpoint diagnostics: '+repr(exc)
    np.savez_compressed(args.state,r=solver.t,state=endpoint,
        columns=np.array(['m','n','F0','F1','F2','X0','X1','X2','Y0','Y1','Y2','nu0','nu1','nu2']),
        metadata=np.array(json.dumps({'kind':'floating_dealiased_Codazzi_endpoint','object_sha256':sha(args.object),'source_sha256':sha(__file__)})))
    keys=[k for k in rows[0] if k!='r'];maxima={k:max(v[k] for v in rows) for k in keys}
    doc=dict(kind='floating_dealiased_two_field_Codazzi_with_position_reconstruction',complete=status=='finished',
        certified=False,status=status,exception=exception,source_sha256=sha(__file__),object_sha256=sha(args.object),
        dependency_sha256={s:sha(Path(__file__).with_name(s)) for s in ('fourfold_phase_local_correction_probe.py','fourfold_phase_symmetric_geometry.py','fourfold_phase_geometry.py','fourfold_phase_core_low_block.py')},
        origin_sha256=definition['origin_inputs']['sha256'],direction_sha256=definition['direction']['sha256'],
        exact_center_parameter=definition['delta_fraction'],primitive_nodes=args.nodes,angular_grid=args.angles,
        nonlinear_grid=args.angles*args.oversample,Nyquist_removed=True,mean_retained=True,original_target_fixed=True,
        whole_real_angular_circle=False,whole_parameter_interval=False,whole_radial_domain=False,
        method='DOP853, doubled-grid nonlinear evaluation and Fourier Galerkin projection',
        rtol=args.rtol,atol=args.atol,max_step=args.max_step,n_floor=args.n_floor,max_rhs=args.max_rhs,
        requested_radial_interval=[0.,args.right],finished_radial_interval=[0.,float(solver.t)],
        rhs_calls=evolution.calls,rows=rows,sampled_maxima=maxima,
        sampled_minimum_abs_n=min(v['minimum_abs_n'] for v in rows),
        sampled_support_min=min(v['updated_support_min'] for v in rows),
        endpoint_state_path=str(args.state),endpoint_state_sha256=sha(args.state),wall_seconds=time.monotonic()-start,
        limitations=['Floating arithmetic, time interpolation/integration error and infinite Fourier tails are not certified.',
            'Nonlinearities are sampled on a doubled grid, then projected; the listed projection defects are sampled diagnostics only.',
            'Auxiliary parameter is only its exact center; no whole-eta or continuous angular/radial enclosure.',
            'No cap, regular/mean return or global closure condition is imposed.'])
    args.out.write_text(json.dumps(doc,indent=2)+'\n')
    print({'status':status,'r':solver.t,'rhs':evolution.calls,'maxima':maxima,'min_n':doc['sampled_minimum_abs_n'],
        'wall_seconds':doc['wall_seconds'],'exception':exception},flush=True)


if __name__=='__main__':main()
