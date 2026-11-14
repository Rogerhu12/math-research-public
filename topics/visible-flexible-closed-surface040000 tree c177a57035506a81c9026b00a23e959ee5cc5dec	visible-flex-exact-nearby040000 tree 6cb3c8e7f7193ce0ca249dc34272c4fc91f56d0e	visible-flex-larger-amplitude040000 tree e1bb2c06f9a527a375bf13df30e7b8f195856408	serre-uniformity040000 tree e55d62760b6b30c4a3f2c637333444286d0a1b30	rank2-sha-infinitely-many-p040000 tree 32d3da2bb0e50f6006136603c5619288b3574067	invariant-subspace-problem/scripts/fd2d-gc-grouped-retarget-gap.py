#!/usr/bin/env python3
"""Change only one gap row of a same-state R165 baseline and unscaled normal.

No F/J is evaluated. Old files are immutable. The derived normal has an
explicit independent binding, and subsequent scaling/Schur/QP/F are new.
"""
import os
for _name in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[_name]='1'
import argparse,copy,datetime,json,traceback
from pathlib import Path
import numpy as np
from fd2d_gc_archive_arrays import identity
from fd2d_gc_grouped_search_context import NumericalContext,array_identity
from fd2d_gc_grouped_normal_tile_io import partition_context,merged_normal_binding
from fd2d_gc_stage_io import atomic_json,load_baseline
from fd2d_gc_normal_checkpoint import save_normal_checkpoint
from fd2d_gc_selected_normal_io import load_selected_normal
load_normal_checkpoint=load_selected_normal
from fd2d_gc_packet_checkpoint import save_actual_packet
from fd2d_gc_gap_row_retarget import gap_retarget_binding,replace_gap_row_in_place
from fd2d_gc_schur_stage_io import content
from fd2d_gc_bump_residual_locations import residual_locations


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--parent-request',type=Path,required=True)
    ap.add_argument('--out-prefix',type=Path,required=True)
    ap.add_argument('--new-gap',type=float,required=True)
    args=ap.parse_args()
    prefix=args.out_prefix
    parent=NumericalContext(args.parent_request,prefix.with_name(prefix.name+'-parent-context-read'),install_caches=False)
    oldroot,plan,common,baseline=partition_context(parent)
    oldmanifest=oldroot/'normal-partitioned'/'manifest.json'
    packet=load_baseline(parent)
    settings=dict(parent.request['settings']);settings.update(gap=args.new_gap,out_prefix=str(prefix),owner_stop_file='/tmp/'+prefix.name+'-stop')
    req=dict(parent.request,created_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
        run_prefix=str(prefix),cache_dir=str(prefix)+'-work',settings=settings,
        gap_retarget_origin=dict(parent_request=identity(args.parent_request),old_gap=parent.args.gap,new_gap=args.new_gap,
            rationale='R168/R169 D4 construction; all curvature guides and physical field arrays remain unchanged'),
        finite_goal_unchanged_from_parent=False)
    request=prefix.with_name(prefix.name+'-request.json')
    if request.exists():raise FileExistsError(request)
    atomic_json(request,req)
    ctx=NumericalContext(request,prefix.with_name(prefix.name+'-retarget'),install_caches=False)
    ctx.report.update(stage='same_state_one_gap_row_baseline_and_normal_replacement',stage_source=identity(__file__))
    ctx.save_report()
    try:
        expected=gap_retarget_binding(parent.binding,args.new_gap)
        if ctx.binding!=expected:raise ValueError('The new actual context changes more than the single gap goal')
        if array_identity(ctx.vector)!=array_identity(parent.vector):raise ValueError('Retarget changed the actual field vector')
        normal=load_normal_checkpoint(ctx.problem,oldmanifest,expected_binding=merged_normal_binding(common,plan))
        axes=packet['data']['axes'];actual_gap=float(axes['gap'])
        proof=replace_gap_row_in_place(normal,actual_gap=actual_gap,
            central_gap_gradient=axes['gap_jacobian'],old_binding=parent.binding,new_binding=ctx.binding)
        residual=packet['residual'];raw=packet['data']['original_residual']
        inside=2*ctx.problem.e*len(ctx.args.interior_cells)
        gap_index=len(raw)-inside-1
        old_value=(actual_gap-parent.args.gap)/parent.args.gap
        new_value=(actual_gap-args.new_gap)/args.new_gap
        if not 0<=gap_index<len(raw) or float(raw[gap_index])!=old_value or float(residual[gap_index])!=old_value:
            raise ValueError('The unique saved gap row is not at the proven original concatenation index')
        old_residual_id=array_identity(residual);old_raw_id=array_identity(raw)
        residual[gap_index]=new_value;raw[gap_index]=new_value
        packet['data']['previous_node_cell_residual_maximum']=float(np.max(abs(raw[:-inside] if inside else raw)))
        squared=float(residual@residual);difference=abs(squared-normal.residual_squared)
        # Only a floating sum reassociation bound; matrix/F identities above are exact SHA checks.
        scale=max(1.,squared,abs(normal.residual_squared))
        if difference>512*np.finfo(float).eps*scale:raise ArithmeticError('Derived normal and single-row actual value update disagree')
        root=Path(req['cache_dir'])
        value_manifest=save_actual_packet(packet,root/'baseline-values',binding=ctx.binding)
        transport=dict(schema='fd2d-durable-single-gap-derived-normal-binding-v1',finite_goal=ctx.binding,
            original_normal=content(oldmanifest),original_transport_binding=merged_normal_binding(common,plan),
            original_finite_goal=parent.binding,gap_replacement_source=content(Path(__file__).with_name('fd2d_gc_gap_row_retarget.py')),
            derivation_entry=content(__file__),actual_value_residual=array_identity(residual),gap_row_index=int(gap_index),
            old_target=float(parent.args.gap),new_target=float(args.new_gap))
        normal_manifest=save_normal_checkpoint(normal,root/'normal-gap-derived',binding=transport)
        reference=dict(schema='fd2d-explicit-derived-normal-reference-v1',finite_goal=ctx.binding,
            normal_manifest=identity(normal_manifest),transport_binding=transport,gap_row_replacement=proof,
            newly_assembled_tile_set_claimed=False)
        atomic_json(root/'normal-reference.json',reference)
        diagnostics=ctx.diag(ctx.vector,packet['data'])
        summary=dict(schema='fd2d-durable-actual-value-baseline-v1',binding=ctx.binding,
            value_packet_manifest=identity(value_manifest),actual_current_state=baseline['actual_current_state'],
            vector=array_identity(ctx.vector),residual=array_identity(residual),residual_squared=squared,
            objective_norm=float(np.linalg.norm(residual)),diagnostics=diagnostics,
            locations=residual_locations(ctx.problem,ctx.vector,packet['data'],packet['data']['codazzi_complement_result'],ctx.args.curvature_cap),
            stage_source=identity(__file__),recovered_complete_packet=True,actual_new_F_evaluations=0,
            single_gap_row_derived_from_actual_value=True,original_baseline=identity(oldroot/'baseline-summary.json'),
            finite_success=False,strong_target_complete=False)
        atomic_json(root/'baseline-summary.json',summary)
        original_norm=float(baseline['objective_norm'])
        comparison=dict(actual_state_sha256=ctx.report['warm_input']['sha256'],gap_row_index=int(gap_index),
            original_residual=old_residual_id,original_raw=old_raw_id,updated_residual=array_identity(residual),
            old_target=float(parent.args.gap),new_target=float(args.new_gap),actual_gap=actual_gap,
            old_gap_residual=old_value,new_gap_residual=new_value,
            original_objective_norm=original_norm,new_objective_norm=summary['objective_norm'],
            normal_residual_squared=float(normal.residual_squared),actual_residual_squared=squared,
            squared_difference=difference,curvature_guide=ctx.args.curvature_cap,
            central_cap=ctx.args.central_cap,central_floor=ctx.args.central_floor,
            node_curvature_merit_l2=diagnostics['curvature_merit']['residual_l2'],
            interior_curvature_merit_l2=diagnostics['interior_actual_constraints']['curvature_residual_l2'],
            full_field_J_or_F_recomputed=False,physical_g_or_field_changed=False,
            scaled_Schur_reused=False,strong_target_complete=False)
        atomic_json(root/'gap-comparison.json',comparison)
        ctx.save_report(completed=True,derived_normal=identity(normal_manifest),derived_reference=identity(root/'normal-reference.json'),
            value_packet_manifest=identity(value_manifest),comparison=comparison,gap_row_replacement=proof,
            actual_value_objective_evaluations=0)
        ctx.event('single_gap_goal_and_normal_closed',request=str(request),normal=str(normal_manifest),
            old_objective_norm=original_norm,new_objective_norm=summary['objective_norm'],gap_row_index=int(gap_index),
            normal_value_squared_difference=difference,actual_new_F_evaluations=0)
        return 0
    except Exception as exc:
        ctx.save_report(exception=dict(type=type(exc).__name__,message=str(exc),traceback=traceback.format_exc()))
        raise

if __name__=='__main__':raise SystemExit(main())
