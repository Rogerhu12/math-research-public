#!/usr/bin/env python3
"""Build an actual nonaxisymmetric principal normal terminal condition.

For the sampled positive-Gauss reference field, impose the high cosine rows
of w_s-(f/g) w_phi+sqrt(e*g-f*f)/abs(g) |D_phi|w=0 on perturbations.
This is a principal boundary design, not an exact nonlinear stable manifold.
The interior finite Frenet equation is not changed or filtered.
"""
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[key]='1'
import argparse
import gzip
import hashlib
import importlib.util
import json
from fractions import Fraction
from pathlib import Path
import numpy as np

P=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('normal_terminal_driver',P/'geometry_20261114_r225_free_core_bvp.py')
driver=importlib.util.module_from_spec(spec);spec.loader.exec_module(driver)


def projector(q,s,y,first_mode):
    frame=q.frame(s,y);yp,ypp=driver.finite_second_derivative(q,s,y)
    V,dV,unused=q.jet(yp);acc=q.jet(ypp)[0];d,dd=frame['d'],frame['dd']
    normal=np.cross(V,d);area=np.linalg.norm(normal,axis=1);normal/=area[:,None]
    def normal_derivative(derivative):
        return (derivative-normal*np.einsum('ij,ij->i',normal,derivative)[:,None])/area[:,None]
    ns=normal_derivative(np.cross(acc,d)+np.cross(V,dV))
    nphi=normal_derivative(np.cross(dV,d)+np.cross(V,dd))
    e=np.einsum('ij,ij->i',acc,normal);f=np.einsum('ij,ij->i',dV,normal);g=np.einsum('ij,ij->i',dd,normal)
    det=e*g-f*f
    if np.any(det<=0)or np.any(g==0):
        raise ValueError('Principal elliptic boundary requires strictly positive sampled det II and nonzero II_phi_phi')
    flow=driver.BatchedFFTFlow(q)
    A=flow.jac(np.array([s]),y[:,None])[:,:,0]
    cosines=q.C[first_mode:q.M+1];raw=np.empty((q.M-first_mode+1,q.n))
    multiplier=np.arange(q.N//2+1)
    for j in range(q.n):
        direction=np.zeros(q.n);direction[j]=1
        delta,deltap,unused=q.jet(direction);delta_s=q.jet(A[:,j])[0]
        w=np.einsum('ij,ij->i',delta,normal)
        ws=np.einsum('ij,ij->i',delta_s,normal)+np.einsum('ij,ij->i',delta,ns)
        wphi=np.einsum('ij,ij->i',deltap,normal)+np.einsum('ij,ij->i',delta,nphi)
        absD=np.fft.irfft(multiplier*np.fft.rfft(w),n=q.N)
        trace=ws-(f/g)*wphi+(np.sqrt(det)/abs(g))*absD
        raw[:,j]=(2/q.N)*(cosines@trace)
    norms=np.linalg.norm(raw,axis=1)
    if np.any(norms==0):
        raise ValueError('A principal boundary row vanished')
    normalized=raw/norms[:,None]
    singular=np.linalg.svd(normalized,compute_uv=False)
    E=np.einsum('ij,ij->i',V,V);F=np.einsum('ij,ij->i',V,d);G=np.einsum('ij,ij->i',d,d)
    gauss=det/(E*G-F*F)
    info=dict(gauss_min=float(gauss.min()),gauss_max=float(gauss.max()),det_II_min=float(det.min()),
              II_phi_phi_min=float(g.min()),II_phi_phi_max=float(g.max()),
              principal_decay_min=float((np.sqrt(det)/abs(g)).min()),
              principal_decay_max=float((np.sqrt(det)/abs(g)).max()),
              normalized_row_singular_min=float(singular.min()),normalized_row_singular_max=float(singular.max()),
              normalized_row_condition=float(singular.max()/singular.min()),
              matrix_shape=list(normalized.shape))
    return normalized,norms,info


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--input',type=Path,required=True)
    p.add_argument('--station',type=float)
    p.add_argument('--fixed-modes',type=int,default=32)
    p.add_argument('--out',type=Path,required=True)
    args=p.parse_args()
    data=driver.fixed.read(args.input)
    controlled='augmented_states'in data
    ident=data['original_metric_identity']if controlled else data['metric_identity'];law=ident['law']
    c=np.array([float(Fraction(x))for x in ident['coefficients_rational']])
    M,N=(data['M'],data['N'])if controlled else (data['numerical_parameters']['M'],data['numerical_parameters']['N'])
    if not 0<args.fixed_modes<M:
        raise ValueError('Keep at least one and fewer than all core modes')
    index=-1 if args.station is None else int(np.argmin(abs(np.array(data['state_locations'])-args.station)))
    row=data['rows'][index];s=float(data['state_locations'][index])
    x=np.array(data['augmented_states'][index])if controlled else np.r_[row['a'],row['ap'],data['coefficient_states'][index]]
    if args.station is not None and abs(args.station-s)>1e-12:
        raise ValueError('The requested endpoint is not a saved actual station')
    q=driver.native.outward.FullCoreProbe(c,M,N,law['velocity'],law['length'],law['k0'])
    q.profile=lambda ignored:(float(x[0]),float(x[1]),row['app']);driver.fixed.fft.enable_fft(q)
    L,norms,info=projector(q,s,x[2:],args.fixed_modes+1)
    report=dict(scope=__doc__,M=M,N=N,first_mode=args.fixed_modes+1,station=s,
                original_metric_identity=ident,scalar_jet=[float(x[0]),float(x[1]),row['app']],
                reference_state=x[2:].tolist(),rows=L.tolist(),unnormalized_row_norms=norms.tolist(),
                diagnostics=info,reference_geometry=row,
                source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                input_sha256=hashlib.sha256(args.input.read_bytes()).hexdigest(),
                boundary_definition='L @ (y_end-reference_state) = 0, where L is fixed at the reference field.',
                new_interior_solution=False,exact_nonlinear_stable_manifold=False)
    args.out.parent.mkdir(parents=True,exist_ok=True)
    args.out.write_bytes(gzip.compress((json.dumps(report)+'\n').encode(),mtime=0))
    print(json.dumps(dict(output=str(args.out),station=s,diagnostics=info)),flush=True)


if __name__=='__main__':
    main()
