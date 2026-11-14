#!/usr/bin/env python3
"""Prepare the saved plateau-point P1 injection and a separate R165 request.

This performs no residual, Jacobian, normal, QP, or nonlinear solve.  The
explicit new mesh and grouped cell rule never inherit v25 convergence.
"""
import os
for _name in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[_name]='1'
import argparse
import datetime
import json
from pathlib import Path
import numpy as np
from fd2d_gc_archive_arrays import identity,load_npz,save_npz
from fd2d_gc_physical_point_refinement import create_physical_point_refined_problem,checkpoint_arrays
from fd2d_gc_grouped_search_context import FINITE_RULE
from fd2d_gc_stage_io import atomic_json


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--parent-request',type=Path,required=True)
    ap.add_argument('--field',type=Path,required=True)
    ap.add_argument('--out-prefix',type=Path,required=True)
    ap.add_argument('--central-floor',type=float)
    args=ap.parse_args()
    request=json.loads(args.parent_request.read_text());settings=dict(request['settings'])
    field=load_npz(args.field);candidate=Path(settings['candidate']);candidate_id=identity(candidate)
    if str(field['candidate_sha256'])!=candidate_id['sha256']:
        raise ValueError('The actual field belongs to a different physical baseline candidate')
    proof_path=Path(settings['radius_packet']);proof=json.loads(proof_path.read_text())
    if not proof['passed'] or proof['candidate_sha256']!=candidate_id['sha256']:
        raise ValueError('The baseline radius packet does not bind this actual candidate')
    witness=dict(**identity(proof_path),candidate_sha256=proof['candidate_sha256'])
    problem=create_physical_point_refined_problem(candidate,saved_field=field,
        include_saved_gauss_plateau=True,physical_points=(),midpoint_cells=(),
        modes=int(field['modes']),max_step=settings['mesh_step'],gap=settings['gap'],
        reference_inlet=Path(settings['reference_inlet']),reference_cache=Path(settings['reference_cache']),
        reference_rim_fraction=settings['reference_rim_fraction'],minimum_active_n=settings['minimum_active_n'],
        mesh_relative_tolerance=settings['mesh_relative_tolerance'],base_lower_bound='4/5',
        base_lower_provenance=witness,radius_floor=settings['radius_floor'])
    vector,definition=problem.inject_saved_field(canonicalize_redundant=True)
    arrays=checkpoint_arrays(problem,vector,candidate_id['sha256'],refinement_definition=definition)
    if arrays['parameters'].dtype!=field['parameters'].dtype or arrays['parameters'].tobytes()!=field['parameters'].tobytes():
        raise ArithmeticError('The physical parameter vector must remain byte-identical during P1 injection')
    arrays['finite_radial_scheme']=np.array(FINITE_RULE)
    arrays['grouped_goal_preparation']=np.array(json.dumps(dict(schema='fd2d-explicit-R163-R165-preparation-v1',
        input=identity(args.field),parent_request=identity(args.parent_request),source=identity(__file__),
        actual_F_J_normal_QP_or_nonlinear_solve=False),sort_keys=True))
    initial_path=args.out_prefix.with_name(args.out_prefix.name+'-initial.npz')
    entity=save_npz(initial_path,**arrays)
    settings.update(warm_start=str(initial_path),modes=int(field['modes']),out_prefix=str(args.out_prefix),
        owner_stop_file='/tmp/'+args.out_prefix.name+'-stop',
        interior_cells=json.loads(str(arrays['finite_interior_rows_definition']))['cells'])
    if args.central_floor is not None:settings['central_floor']=float(args.central_floor)
    new_request=dict(schema='fd2d-recoverable-grouped-coast-step-v1',
        created_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
        run_prefix=str(args.out_prefix),cache_dir=str(args.out_prefix)+'-work',
        settings=settings,input_sha256=entity['sha256'],
        physical_parameters_preserved=True,finite_equations_changed_from25=True,
        finite_rule=FINITE_RULE,owner='numerical_recovery',strong_target_complete=False)
    request_path=args.out_prefix.with_name(args.out_prefix.name+'-request.json')
    if request_path.exists():raise FileExistsError(request_path)
    atomic_json(request_path,new_request)
    report=dict(schema='fd2d-actual-plateau-injection-and-R165-request-v1',completed=True,
        source=identity(__file__),input=identity(args.field),parent_request=identity(args.parent_request),
        candidate=candidate_id,initial=entity,request=identity(request_path),
        old_nodes=len(field['mesh']),new_nodes=problem.N,parameter_bytes_unchanged=True,
        definition=definition,new_finite_interior_rows_definition=json.loads(str(arrays['finite_interior_rows_definition'])),
        physical_g_changed=False,finite_goal_changed=True,actual_F_J_normal_QP_or_nonlinear_solve=False,
        finite_success=False,strong_target_complete=False)
    atomic_json(args.out_prefix.with_name(args.out_prefix.name+'-preparation-report.json'),report)
    print(json.dumps(dict(event='separate_grouped_goal_prepared',initial=entity,request=str(request_path),
        old_nodes=len(field['mesh']),new_nodes=problem.N)),flush=True)
    return 0


if __name__=='__main__':raise SystemExit(main())
