#!/usr/bin/env python3
"""Start a new, explicit curvature-guidance objective from a true accepted field.

No value packet, normal, Schur factor or direction is reused under the new
goal. The physical field and all search bounds are copied without change.
"""
import argparse
import datetime
import json
from pathlib import Path
from fd2d_gc_archive_arrays import identity
from fd2d_gc_stage_io import atomic_json


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--parent-request',type=Path,required=True)
    parser.add_argument('--accepted-result',type=Path,required=True)
    parser.add_argument('--out-prefix',type=Path,required=True)
    parser.add_argument('--curvature-guide',type=float,required=True)
    parser.add_argument('--next-damping',type=float,required=True)
    args=parser.parse_args()
    if not 0<args.curvature_guide<1000/121 or not args.next_damping>0:
        raise ValueError('Use positive damping and a guide below the declared D4 curvature budget')
    parent=json.loads(args.parent_request.read_text())
    accepted=json.loads(args.accepted_result.read_text())
    if not accepted.get('accepted') or not accepted.get('actual_full_residual_evaluated'):
        raise ValueError('Require a saved complete actual accepted step')
    field=accepted['accepted_state'];actual=identity(field['path'])
    if any(actual[k]!=field[k] for k in ('bytes','sha256')):
        raise ValueError('The actual accepted field changed')
    settings=dict(parent['settings']);old_guide=settings['curvature_cap']
    destination=args.out_prefix.with_name(args.out_prefix.name+'-request.json')
    if destination.exists():raise FileExistsError(destination)
    settings.update(warm_start=str(Path(field['path']).resolve()),
        out_prefix=str(args.out_prefix),curvature_cap=args.curvature_guide,
        damping=args.next_damping,owner_stop_file='/tmp/'+args.out_prefix.name+'-stop')
    request=dict(parent,schema='fd2d-explicit-curvature-guidance-retarget-v1',
        created_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
        run_prefix=str(args.out_prefix),cache_dir=str(args.out_prefix)+'-work',
        settings=settings,input_sha256=actual['sha256'],
        previous_actual_accepted_result=identity(args.accepted_result),
        finite_goal_unchanged_from_parent=False,tail_domain_changed_only=False,
        new_actual_F_evaluations=0,
        curvature_guidance_retarget=dict(source=identity(__file__),
            parent_request=identity(args.parent_request),same_actual_field=actual,
            old_guide=old_guide,new_guide=args.curvature_guide,
            old_goal_actual_norm=accepted['objective_norm'],
            original_Gauss_Codazzi_gap_functions_unchanged=True,
            central_search_bounds_unchanged=True,tail_domain_unchanged=True,
            profile_search_bounds_unchanged=True,physical_g_unchanged_by_retarget=True,
            new_baseline_and_normal_required=True,old_norm_not_a_new_field_improvement=True,
            geometric_budget='R168 D<=4, required actual reach>=121/1000; guidance alone is not a certificate'))
    atomic_json(destination,request)
    report=dict(schema='fd2d-curvature-guidance-retarget-record-v1',
        request=identity(destination),field=actual,source=identity(__file__),
        completed=True,actual_F_J_or_matrix_operations=0,
        new_goal_is_not_old_finite_convergence=True)
    atomic_json(args.out_prefix.with_name(args.out_prefix.name+'-retarget-report.json'),report)
    print(json.dumps(report))


if __name__=='__main__':main()
