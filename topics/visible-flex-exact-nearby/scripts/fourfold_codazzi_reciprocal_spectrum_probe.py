#!/usr/bin/env python3
"""Full saved-candidate spectrum diagnostic for reciprocal Codazzi variables.

This samples the complete finite B,C candidates, retains full sampled FFT
envelopes, and measures projection into the new U,V chart. It is a floating
diagnostic, not a continuous certificate or a new BVP solve.
"""
from __future__ import annotations
import argparse,gzip,json,time
from pathlib import Path
import numpy as np
from scipy.interpolate import PPoly
from flint import ctx
from fourfold_codazzi_reciprocal_polynomial_system import ReciprocalPolynomial
from fourfold_codazzi_compact_metric_fast_jacobian import FastCompactNormalized
from fourfold_codazzi_candidate_shards import load_candidate
from fourfold_phase_symmetric_geometry import load_exact_object
from fourfold_phase_codazzi_rotational_reference_probe import RotationalBodyTarget
from fourfold_codazzi_rotational_cap_jacobi_probe import RotationalGraftTarget
from fourfold_phase_local_correction_probe import sha


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--object',type=Path,default=Path('data/phase_ring_continuation/type_fixed_step02_d5_exact_affine_step5_object.json'))
    ap.add_argument('--candidate',type=Path,action='append',required=True)
    ap.add_argument('--angles',type=int,default=4096);ap.add_argument('--batch',type=int,default=8)
    ap.add_argument('--out',type=Path,required=True);args=ap.parse_args();started=time.monotonic()
    if args.out.exists():raise FileExistsError('preserve every actual reciprocal spectrum diagnostic')
    ctx.prec=192;ctx.cap=6;geometry,definition=load_exact_object(args.object,512)
    body=RotationalBodyTarget(geometry);graft=RotationalGraftTarget(geometry,args.object)
    radial=np.unique(np.r_[np.linspace(0.,.35,351),.239,.5,1.,1.5,3.,3.125]);N=args.angles
    kk=np.abs(np.fft.fftfreq(N,1/N));cutoffs=sorted({32,64,128,256,512,1024})
    output=[]
    for path in args.candidate:
        saved=load_candidate(path);meta=json.loads(str(saved['metadata']));m=int(meta['modes'])
        if (meta['object_sha256']!=sha(args.object) or meta['coordinates']!='B=alpha*b; C=Cref_nu+alpha*c'
            or N<=6*m):raise ValueError('complete original candidate and sufficient cubic angular grid required')
        old=FastCompactNormalized(geometry,m,N,body,graft)
        new=ReciprocalPolynomial(geometry,m,N,body,graft);new.all_base_cache=old.all_base_cache if hasattr(old,'all_base_cache') else {}
        old.all_base_cache=new.all_base_cache
        old.alpha=new.alpha=alpha=float(meta['amplitude']);p=np.array([float(meta['nu'])])
        if alpha<=0:raise ValueError('this complete transformed-candidate diagnostic requires positive amplitude')
        pp=PPoly(saved['piece_coefficients'],saved['radial_nodes'])
        names=('normalized_U','normalized_V','physical_A','physical_B','physical_C')
        envelopes={name:np.zeros(N//2+1) for name in names}
        spectral={name:{str(k):dict(tail_l1=0.,theta_derivative_tail_l1=0.,radial_of_tail_max=0.) for k in cutoffs if k<N//2} for name in names}
        maxima={k:dict(value=0.,r=0.,theta=0.) for k in (
            'old_physical_B_residual','old_physical_C_residual','new_projected_physical_B_residual',
            'new_projected_physical_C_residual','new_projected_normalized_finite_residual',
            'coordinate_projection_physical_B_error','coordinate_projection_physical_C_error',
            'new_polynomial_rhs_unretained_l1','new_polynomial_rhs_beyond_3M_roundoff_l1')}
        Cmin=np.inf;Cmax=-np.inf;vprojmin=np.inf;vprojmax=-np.inf
        def update(name,values,r):
            values=np.atleast_2d(abs(values));loc=np.unravel_index(np.argmax(values),values.shape);val=float(values[loc])
            if val>maxima[name]['value']:
                maxima[name]=dict(value=val,r=float(r[loc[-1]]),theta=float(new.theta[loc[0]]) if values.shape[0]==N else 0.)
        for start in range(0,len(radial),args.batch):
            r=radial[start:start+args.batch];y=pp(r).T;yr=pp(r,1).T
            t,b,c,C,A_delta=old.data(r,y,p);a,g,beta,K,ell,Cr,*_=t
            B=alpha*b;A=(K+B*B)/C;Cr_r=beta*(ell-1)*Cr
            br,cr=old.normalized_fields(yr);C_r=Cr_r+alpha*cr
            U=b/C;V=-c/(Cr*C)
            Ur=br/C-b*C_r/(C*C)
            Vr=-cr/(Cr*C)+c*Cr_r/(Cr*Cr*C)+c*C_r/(Cr*C*C)
            Bt=old.cos[1:].T@(old.frequency[:,None]*y[:m])
            ct=-old.sin.T@(old.frequency[:,None]*y[m+1:])
            At=2*alpha*b*Bt/C-(ell*Cr*Cr+alpha*alpha*b*b)*ct/(C*C)
            RB=alpha*(br-g*At+2*beta*b);RC=alpha*(cr-g*Bt-beta*(A_delta-c))
            update('old_physical_B_residual',RB,r);update('old_physical_C_residual',RC,r)
            for name,field in zip(names,(U,V,A,B,C)):
                ff=np.fft.fft(field,axis=0)/N;absf=abs(ff)
                envelopes[name]=np.maximum(envelopes[name],np.max(absf[:N//2+1],axis=1))
                for cutoff,row in spectral[name].items():
                    mask=kk>int(cutoff);tail=np.sum(absf[mask],axis=0);dt=np.sum(4*kk[mask,None]*absf[mask],axis=0)
                    loc=int(np.argmax(tail))
                    if tail[loc]>row['tail_l1']:row['tail_l1']=float(tail[loc]);row['radial_of_tail_max']=float(r[loc])
                    row['theta_derivative_tail_l1']=max(row['theta_derivative_tail_l1'],float(np.max(dt)))
            yn=new.project(U,V);ynr=new.project(Ur,Vr);fu,fv,z=new.physical_rhs(r,yn,p)
            unr,vnr=new.fields(ynr);resU=unr-fu;resV=vnr-fv;vn=z['v'];un=alpha*z['U']
            Rbn=alpha*(resU/vn-un*resV/(vn*vn));Rcn=-alpha*resV/(vn*vn)
            update('new_projected_physical_B_residual',Rbn,r);update('new_projected_physical_C_residual',Rcn,r)
            update('coordinate_projection_physical_B_error',un/vn-B,r)
            update('coordinate_projection_physical_C_error',1/vn-C,r)
            update('new_projected_normalized_finite_residual',ynr-new.project(fu,fv),r)
            fr=np.fft.fft(np.stack((fu,fv)),axis=1)/N
            update('new_polynomial_rhs_unretained_l1',np.sum(abs(fr[:,kk>m]),axis=1),r)
            update('new_polynomial_rhs_beyond_3M_roundoff_l1',np.sum(abs(fr[:,kk>3*m]),axis=1),r)
            Cmin=min(Cmin,float(np.min(C)));Cmax=max(Cmax,float(np.max(C)))
            vprojmin=min(vprojmin,float(np.min(vn)));vprojmax=max(vprojmax,float(np.max(vn)))
        item=dict(candidate=str(path),candidate_sha256=sha(path),metadata=meta,modes=m,
            angles=N,radial_samples=radial.tolist(),sampled_C_range=[Cmin,Cmax],
            sampled_projected_v_range=[vprojmin,vprojmax],projected_chart_sampled_negative=bool(vprojmax<0),
            maxima=maxima,spectral_tails=spectral,
            full_positive_index_sampled_Fourier_envelopes={k:v.tolist() for k,v in envelopes.items()},
            envelope_normalization='abs of complex FFT coefficient, quarter-period physical frequency 4*k; positive index only, both real signs represented by conjugacy',
            complete_original_finite_modes_used=True,original_finite_status_not_changed=True,
            transformed_projection_is_not_a_BVP_solution=True,continuous_PDE_certified=False)
        output.append(item)
        print(dict(candidate=path.name,C_range=item['sampled_C_range'],projected_v_range=item['sampled_projected_v_range'],
            old_B=maxima['old_physical_B_residual'],new_B=maxima['new_projected_physical_B_residual'],
            U_tail128=spectral['normalized_U'].get('128'),V_tail128=spectral['normalized_V'].get('128')),flush=True)
    result=dict(kind='actual_saved_full_candidates_reciprocal_spectrum_and_projection_diagnostic',complete=True,
        mathematical_certificate=False,source_sha256=sha(__file__),object_sha256=sha(args.object),
        system_sha256=sha(Path(__file__).with_name('fourfold_codazzi_reciprocal_polynomial_system.py')),
        candidates=output,wall_seconds=time.monotonic()-started,
        dependencies={name:sha(Path(__file__).with_name(name)) for name in (
            'fourfold_codazzi_compact_metric_fast_jacobian.py','fourfold_codazzi_compact_metric_branch_probe.py',
            'fourfold_codazzi_candidate_shards.py','fourfold_phase_symmetric_geometry.py',
            'fourfold_phase_codazzi_rotational_reference_probe.py','fourfold_codazzi_rotational_cap_jacobi_probe.py')})
    with gzip.GzipFile(filename=str(args.out),mode='wb',mtime=0) as stream:
        stream.write((json.dumps(result,indent=2,allow_nan=False)+'\n').encode())


if __name__=='__main__':main()
