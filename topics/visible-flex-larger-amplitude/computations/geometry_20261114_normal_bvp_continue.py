#!/usr/bin/env python3
"""Prepare a genuine full-state continuation of an accepted normal BVP.

Append a C2 scalar turn segment with the same initial angular curvature,
predict only the new endpoint to second order, and build its nonaxisymmetric
principal terminal matrix. The predicted segment is not an accepted field.
The original complete accepted state supplies the warm prefix; no mode is
dropped. This program prepares files and argv, not a solved continuation.
"""
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[key]='1'
import argparse
import copy
import gzip
import hashlib
import importlib.util
import json
import sys
from fractions import Fraction
from pathlib import Path
import numpy as np

P=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('continued_normal_projector',P/'geometry_20261114_normal_terminal_projector.py')
normal=importlib.util.module_from_spec(spec);spec.loader.exec_module(normal)
base=normal.driver


def compressed(path,data):
    path.write_bytes(gzip.compress((json.dumps(data)+'\n').encode(),mtime=0))


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--input',type=Path,required=True)
    p.add_argument('--duration',type=float,default=.006)
    p.add_argument('--fixed-modes',type=int,default=32)
    p.add_argument('--jac-workers',type=int,default=1)
    p.add_argument('--tol',type=float,default=1e-6)
    p.add_argument('--max-nodes',type=int,default=640)
    p.add_argument('--out-prefix',type=Path,required=True)
    args=p.parse_args()
    data=base.fixed.read(args.input)
    if data['success']is not True:
        raise ValueError('Continuation requires an actually accepted BVP')
    M,N=data['M'],data['N'];s0=float(data['mesh'][-1]);duration=args.duration;s1=s0+duration
    if duration<=0:
        raise ValueError('Continue forward by a positive distance')
    original=data['fixed_scalar_profile'];old=base.fixed.FixedProfile(original['geometry'])
    a0,v0,u0=old.profile(s0);K=-u0/np.sqrt(1-v0*v0)
    if K<=0:
        raise ValueError('This continuation starts on a negative-acceleration turn')
    angle0=np.arcsin(v0);angle1=angle0-K*duration
    a1=a0+(np.cos(angle1)-np.cos(angle0))/K;v1=np.sin(angle1);u1=-K*np.cos(angle1)
    accepted_coefficients=np.array(data['core']['coefficients'])
    exact_coefficients=[str(Fraction(float(c)))for c in accepted_coefficients]
    core_identity=hashlib.sha256(json.dumps(exact_coefficients,separators=(',',':')).encode()).hexdigest()
    geometry=copy.deepcopy(original['geometry'])
    geometry['coefficients_rational']=exact_coefficients;geometry['core_sha256']=core_identity
    geometry['knots']=[r for r in geometry['knots']if r['s']<s0-1e-12]
    geometry['knots']+=[dict(s=s0,a=a0,ap=v0,app=u0),dict(s=s1,a=float(a1),ap=float(v1),app=float(u1))]
    scalar=base.fixed.FixedProfile(geometry)
    profile=dict(schema='r225-exact-C2-scalar-polynomial-profile-v1',geometry=geometry,
                 geometry_sha256=base.fixed.canonical_hash(geometry),
                 exact_coefficient_sha256=scalar.exact_coefficient_sha256,
                 exact_seam_checks=scalar.exact_seam_checks,
                 first_jet_float_correction=scalar.first_jet_float_correction,
                 definition='Exact-binary-rational nodal jets define the unique quintic per physical interval.',
                 scope='New scalar turn design, retaining the previous scalar prefix.')
    law=geometry['initial_law'];ident=dict(core_sha256=core_identity,coefficients_rational=exact_coefficients,law=law,end=s0)
    seed=dict(scope='Complete accepted finite BVP reshaped as a native warm seed; no predicted endpoint is included.',
              status='success',reached_s=s0,target_s=s0,metric_identity=ident,
              metric_identity_sha256=base.fixed.canonical_hash(ident),
              numerical_parameters=dict(M=M,N=N),fixed_metric_profile=geometry,
              state_locations=data['mesh'],coefficient_states=data['states'],rows=data['rows'],summary=data['summary'],
              accepted_BVP_sha256=hashlib.sha256(args.input.read_bytes()).hexdigest())
    q=base.native.outward.FullCoreProbe(accepted_coefficients,M,N,law['velocity'],law['length'],law['k0'])
    q.profile=scalar.profile;base.fixed.fft.enable_fft(q)
    y0=np.array(data['states'][-1]);yp,ypp=base.finite_second_derivative(q,s0,y0)
    predicted=y0+duration*yp+.5*duration**2*ypp
    L,norms,diagnostic=normal.projector(q,s1,predicted,args.fixed_modes+1)
    predicted_geometry=q.stats(s1,predicted)
    projector=dict(scope='Principal normal matrix at a Taylor2 predicted endpoint; not an actual continued trajectory.',
                   M=M,N=N,first_mode=args.fixed_modes+1,station=s1,original_metric_identity=ident,
                   scalar_jet=list(scalar.profile(s1)),reference_state=predicted.tolist(),rows=L.tolist(),
                   unnormalized_row_norms=norms.tolist(),diagnostics=diagnostic,reference_geometry=predicted_geometry,
                   exact_nonlinear_stable_manifold=False,new_interior_solution=False,
                   boundary_definition='L @ (y_end-predicted_reference) = 0, with L frozen before Newton.')
    args.out_prefix.parent.mkdir(parents=True,exist_ok=True)
    profile_path=Path(str(args.out_prefix)+'-profile.json');seed_path=Path(str(args.out_prefix)+'-seed.json.gz')
    projector_path=Path(str(args.out_prefix)+'-projector.json.gz');output_path=Path(str(args.out_prefix)+'-actual.json.gz')
    profile_path.write_text(json.dumps(profile,indent=2)+'\n');compressed(seed_path,seed);compressed(projector_path,projector)
    command=[sys.executable,'-u',str(P/'geometry_20261114_projected_core_bvp.py'),'--profile',str(profile_path),
             '--seed',str(seed_path),'--warm',str(args.input),'--M',str(M),'--N',str(N),
             '--fixed-modes',str(args.fixed_modes),'--end',repr(s1),'--base-step','.005','--extension-step','.001',
             '--seed-interpolation','hermite','--seed-predictor','taylor2','--terminal-projector',str(projector_path),
             '--linear-solver','separated-qr','--linear-workdir',str(args.out_prefix)+'-qr-blocks',
             '--jac-workers',str(args.jac_workers),'--jac-chunk','16','--tol',repr(args.tol),
             '--max-nodes',str(args.max_nodes),'--out',str(output_path)]
    plan=dict(scope=__doc__,executed=False,start=s0,end=s1,constant_angular_curvature=float(K),
              new_scalar_endpoint=list(scalar.profile(s1)),new_scalar_geometry_sha256=profile['geometry_sha256'],
              predicted_endpoint_geometry=predicted_geometry,terminal_diagnostics=diagnostic,
              source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              accepted_input_sha256=hashlib.sha256(args.input.read_bytes()).hexdigest(),command=command,
              prepared_source_hashes={f:hashlib.sha256((P/f).read_bytes()).hexdigest()for f in
                  ('geometry_20261114_projected_core_bvp.py','geometry_20261114_separated_qr_bvp.py',
                   'geometry_20261114_normal_terminal_projector.py')})
    Path(str(args.out_prefix)+'-plan.json').write_text(json.dumps(plan,indent=2)+'\n')
    print(json.dumps({k:plan[k]for k in ('start','end','constant_angular_curvature','new_scalar_endpoint','predicted_endpoint_geometry','terminal_diagnostics')}),flush=True)


if __name__=='__main__':
    main()
