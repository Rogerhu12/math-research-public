#!/usr/bin/env python3
"""Read-only decomposition of the known global-Z Hermite warm correction.

The defined comparison map is saved_warm minus the recorded exact Hermite
increment. It is not silently identified with the unavailable affine source:
the preparer rounded each coefficient and recorded a separate rounding bound.
No parameters, input coefficients or active solver states are changed.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as Q
import gzip
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import time

for key in ("OPENBLAS_NUM_THREADS","OMP_NUM_THREADS","MKL_NUM_THREADS"):
    os.environ[key]="1"
import numpy as np

HERE=Path(__file__).resolve().parent


def identity(path):
    path=Path(path).resolve(); raw=path.read_bytes()
    return dict(path=str(path),bytes=len(raw),sha256=hashlib.sha256(raw).hexdigest())


def rational(row):
    return Q(int(row['numerator']),int(row['denominator']))


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--checkpoint',type=Path,required=True)
    ap.add_argument('--preparation',type=Path,required=True)
    ap.add_argument('--bound-diagnostic',type=Path,required=True)
    ap.add_argument('--linear-port',type=Path,required=True)
    ap.add_argument('--source-root',type=Path,required=True)
    ap.add_argument('--out',type=Path,required=True)
    args=ap.parse_args()
    if args.out.exists(): raise FileExistsError(args.out)
    start=time.monotonic()
    small=json.loads(gzip.decompress(args.checkpoint.read_bytes()))
    prep=json.loads(args.preparation.read_text())
    old=json.loads(args.bound_diagnostic.read_text())
    if small['solver_success'] or small['status']!='UNSOLVED_Z_ONLY_HERMITE_INITIAL_GUESS':
        raise ValueError('Only the declared unsolved warm is studied')
    cp_id=identity(args.checkpoint)
    if cp_id['sha256']!=prep['new_warm']['sha256']:
        raise ValueError('Preparation binds a different warm')
    locations=np.asarray(old['physical_radial_points'],float)
    if len(locations)!=42: raise ValueError('Unexpected shared diagnostic locations')
    inputs=[cp_id,identity(args.preparation),identity(args.bound_diagnostic),identity(args.linear_port)]
    for part in small['pp_coefficient_chunks']:
        row=identity(args.checkpoint.parent/part['file'])
        if any(row[k]!=part[k] for k in ('sha256','bytes')): raise ValueError('Changed PP part')
        inputs.append(row)
    path=HERE/'db6f-prefix-flat-geometry-source.py'
    spec=importlib.util.spec_from_file_location('hermite_source_loader',path)
    loader=importlib.util.module_from_spec(spec); spec.loader.exec_module(loader)
    rec,obj,flow,sol=loader.source(args.checkpoint,args.linear_port,args.source_root)
    m=obj.M; n=4096
    if m!=15: raise ValueError('Expected M15')
    delta_exact=[rational(x) for x in prep['exact_delta_Z']]
    delta=np.asarray([float(x) for x in delta_exact])
    L=float(rec['meridian_length']); t=locations/L
    beta=t**3*(10+t*(-15+6*t))
    beta_prime=30*t*t*(1-t)**2/L
    y=sol.sol(locations)
    b,b1,b2=flow.basis(n)
    fr=flow.frame(locations,obj.q*y,b1,b2)
    d=fr['d']; rho=fr['geo']['rho']; a=flow.profile(locations)[0]
    psi=2*np.pi*np.arange(n)/n
    jj=np.arange(1,m+1)
    h=obj.q*np.sum(delta[:,None]*np.cos(3*jj[:,None]*psi),axis=0)
    h_psi=-obj.q*np.sum((3*jj*delta)[:,None]*np.sin(3*jj[:,None]*psi),axis=0)
    dz=beta[:,None]*h_psi[None,:]
    den=a[:,None]**2*rho**2
    dbase=d.copy(); dbase[:,:,2]-=dz
    warm_g=np.sum(d*d,axis=2)/den-1
    base_g=np.sum(dbase*dbase,axis=2)/den-1
    linear=2*dz*dbase[:,:,2]/den
    quadratic=dz*dz/den
    def l1(x): return np.sum(np.abs(np.fft.fft(x,axis=1)/n),axis=1)
    wl,bl,ll,ql,dl=map(l1,(warm_g,base_g,linear,quadratic,linear+quadratic))
    rows=[]
    for i,s in enumerate(locations):
        j=int(np.argmax(np.abs(warm_g[i])))
        rows.append(dict(s=float(s),beta=float(beta[i]),warm_G_FFT_l1=float(wl[i]),
                         dehermited_G_FFT_l1=float(bl[i]),linear_change_FFT_l1=float(ll[i]),
                         quadratic_change_FFT_l1=float(ql[i]),total_change_FFT_l1=float(dl[i]),
                         maximum_warm_absolute_sample=float(abs(warm_g[i,j])),
                         witness_psi=float(psi[j]),witness_signed_warm_G=float(warm_g[i,j]),
                         witness_signed_dehermited_G=float(base_g[i,j]),
                         witness_linear_change=float(linear[i,j]),witness_quadratic_change=float(quadratic[i,j])))
    worst=int(np.argmax(wl)); worst_base=int(np.argmax(bl))
    oldrow=old['diagnostics'][0]['saved_interpolant']['rows']
    oldnorm=np.asarray([r['G_over_a2_error_FFT_l1'] for r in oldrow])
    if len(oldnorm)!=len(wl): raise ValueError('Original row mismatch')
    rr=rational(prep['maximum_coefficient_rounding_error'])
    # General coefficient-rounding control, not a claim of exact equality to
    # the unavailable affine coefficients. Values are local h=s-left.
    span=float(np.max(np.diff(rec['mesh'])))
    per_state_value_round=float(rr)*sum(span**k for k in range(6))
    angular_round=obj.q*3*m*(m+1)/2*per_state_value_round
    report=dict(schema='78718-warm-Hermite-angular-metric-decomposition-v1',scope=__doc__,
                inputs=inputs,script=identity(__file__),source_loader=identity(path),
                original_affine_source_identity=rec['source_affine_checkpoint'],
                actual_affine_source_file_read=False,checkpoint_solver_success=False,
                angular_samples=n,radial_points=len(locations),rows=rows,
                max_warm_G_FFT_l1=float(wl[worst]),worst_warm_row=rows[worst],
                max_dehermited_G_FFT_l1=float(bl[worst_base]),worst_dehermited_s=float(locations[worst_base]),
                max_identity_residual_sample=float(np.max(np.abs(warm_g-base_g-linear-quadratic))),
                N2048_original_vs_N4096_G_l1_max_difference=float(np.max(np.abs(wl-oldnorm))),
                physical_height_increment_Fourier_l1=float(obj.q*np.sum(np.abs(delta))),
                physical_angular_derivative_increment_Fourier_l1=float(obj.q*np.sum(3*jj*np.abs(delta))),
                maximum_global_beta_prime=float(np.max(beta_prime)),
                source_coefficient_rounding_bound_exact=str(rr),
                old_affine_difference_bound_formula='each Z state value <= round_bound * sum_{k=0}^5 (s-left)^k',
                floating_uniform_Z_angular_round_bound=angular_round,
                continuous_bound=False,new_candidate=False,BVP_calls=0,tail_calls=0,flow_integrations=0,
                seconds=time.monotonic()-start)
    args.out.write_text(json.dumps(report,indent=2,sort_keys=True)+'\n')
    print(json.dumps(dict(output=identity(args.out),max_warm_G=report['max_warm_G_FFT_l1'],
                         max_dehermited_G=report['max_dehermited_G_FFT_l1'],
                         worst=report['worst_warm_row'],height_l1=report['physical_height_increment_Fourier_l1'],
                         derivative_l1=report['physical_angular_derivative_increment_Fourier_l1'],
                         identity_roundoff=report['max_identity_residual_sample'],
                         z_angular_round_bound=angular_round,seconds=report['seconds']),sort_keys=True))


if __name__=='__main__': main()
