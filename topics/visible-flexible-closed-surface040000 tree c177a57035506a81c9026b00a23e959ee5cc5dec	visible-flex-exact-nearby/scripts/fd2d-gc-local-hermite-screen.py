#!/usr/bin/env python3
"""Define and screen one saved actual intrinsic stage, without reintegration.

The saved DOP853 stage has two endpoint states. Their reevaluated finite RHS
values are explicitly chosen as defining shared first jets of a NEW cubic
Hermite field. They are not mislabeled as the unavailable DOP853 interpolant
derivatives. This is a local representation/residual diagnostic only.
"""
from __future__ import annotations
import argparse
import importlib.util
import json
from pathlib import Path
import sys
import numpy as np
from fd2d_gc_shared_hermite_field import write_field,SharedHermiteGCField,codazzi_sample_residual,identity,LD
from fd2d_gc_intrinsic import IntrinsicGC

HERE=Path(__file__).resolve().parent;ROOT=HERE.parent


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--state',type=Path,default=ROOT/'notes/2026-11-12-fd2d-numerical-gc-intrinsic-local-02-state.npz')
    p.add_argument('--candidate',type=Path,default=ROOT/'notes/2026-11-12-fd2d-ellipse-b05-frozen-candidate-v2.json')
    p.add_argument('--oversample',type=int,default=3)
    p.add_argument('--field-dir',type=Path,required=True)
    p.add_argument('--out',type=Path,required=True)
    args=p.parse_args()
    if args.out.exists() or args.field_dir.exists():raise FileExistsError('Use unused local-field outputs')
    sp=importlib.util.spec_from_file_location('fd2d_actual_local_frozen',HERE/'fd2d_frozen_ellipse_candidate.py')
    frozen=importlib.util.module_from_spec(sp);sys.modules[sp.name]=frozen;sp.loader.exec_module(frozen)
    candidate=frozen.Candidate(json.loads(args.candidate.read_text()))
    with np.load(args.state,allow_pickle=False) as data:
        nodes=np.array([data['initial_s'].item(),data['s'].item()],dtype=float)
        values=np.stack((data['initial_state'],data['state']))
        modes=int(data['modes'])
    flow=IntrinsicGC(candidate,modes,args.oversample)
    first=np.stack([flow.rhs(s,y) for s,y in zip(nodes,values)])
    path=write_field(args.field_dir,nodes,values,first,
        chart=dict(kind='fixed_reference_ellipse_eccentric_angle',computational_angle='theta',
             material_map='u(theta)=original ellipse arclength/a0; independent of s and all shape parameters',
             provider=identity(HERE/'fd2d_metric_curvature_core.py'),U_s_exact='0'),
        target=dict(candidate=identity(args.candidate),provider=identity(HERE/'fd2d_frozen_ellipse_candidate.py')),
        provenance=dict(actual_state=identity(args.state),intrinsic_provider=identity(HERE/'fd2d_gc_intrinsic.py'),
             stage_reintegrated=False,source_kind='previously integrated actual local DOP853 endpoint states',
             finite_rhs_oversample=args.oversample,finite_rhs_angular_grid=flow.work),
        derivative_source='reevaluated actual finite projected RHS at the two saved states, intentionally defining this new Hermite field; not DOP853 dense-output jets',
        complete_target_prefix=False)
    field=SharedHermiteGCField(path)
    radial=np.linspace(nodes[0],nodes[-1],17)
    angles=np.arange(1024,dtype=LD)*2*np.arccos(LD(-1))/1024
    f=field.evaluate(radial,angles)
    aa,ap,app=candidate.profile(radial)
    coordinate=flow.reference.reference_coordinate(angles)
    residual=codazzi_sample_residual(f,aa,ap,app,coordinate['u_theta'])
    r=np.sqrt(residual['Rn']**2+residual['Rm']**2)
    endpoint=field.state(nodes);endpoint_first=field.state(nodes,1)
    report=dict(schema='fd2d-gc-actual-local-hermite-screen-v1',scope=__doc__,
        script=identity(__file__),field_provider=identity(HERE/'fd2d_gc_shared_hermite_field.py'),
        field=identity(path),radial_domain=nodes.tolist(),angle_count=len(angles),radial_sample_count=len(radial),
        actual_endpoint_value_representation_difference=float(np.max(abs(endpoint-values))),
        actual_endpoint_first_jet_representation_difference=float(np.max(abs(endpoint_first-first))),
        minimum_n_sample=float(np.min(f['n'])),maximum_Rn_sample=float(np.max(abs(residual['Rn']))),
        maximum_Rm_sample=float(np.max(abs(residual['Rm']))),maximum_residual_norm_sample=float(np.max(r)),
        cleared_numerator_Rn_difference=float(np.max(abs(residual['Rn']-residual['numerator_Rn']))),
        cleared_numerator_Rm_difference=float(np.max(abs(residual['Rm']-residual['numerator_Rm']))),
        initial_frame_compatibility_bound_provided=False,continuous_residual_certified=False,
        complete_target_prefix=False,closed_surface=False)
    args.out.write_text(json.dumps(report,indent=2,allow_nan=False)+'\n')
    print(json.dumps({k:report[k] for k in ('field','radial_domain','minimum_n_sample','maximum_Rn_sample',
          'maximum_Rm_sample','maximum_residual_norm_sample','cleared_numerator_Rn_difference','cleared_numerator_Rm_difference')}),flush=True)


if __name__=='__main__':main()
