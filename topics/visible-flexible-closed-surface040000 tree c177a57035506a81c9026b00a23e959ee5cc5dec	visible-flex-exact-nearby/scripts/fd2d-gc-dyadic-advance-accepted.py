#!/usr/bin/env python3
"""Advance one R165 Newton input using its already evaluated actual value packet.

Only provenance changes: require identical numerical sources/finite rule,
all static saved arrays, the actual accepted-state SHA, and its exact packed
vector and residual SHA. No F/J evaluation or state projection is hidden.
"""
import os
for _name in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[_name]='1'
import argparse,datetime,json,traceback
from pathlib import Path
import numpy as np
from fd2d_gc_archive_arrays import identity,load_npz
from fd2d_gc_dyadic_grouped_search_context import NumericalContext,array_identity,FINITE_RULE
from fd2d_gc_packet_checkpoint import load_actual_packet,save_actual_packet
from fd2d_gc_stage_io import atomic_json


def exact_entity(description):
    actual=identity(description['path'])
    if any(actual[k]!=description[k] for k in ('bytes','sha256')):
        raise ValueError('Previously closed entity changed: '+description['path'])
    return Path(actual['path'])


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--parent-request',type=Path,required=True)
    ap.add_argument('--accepted-result',type=Path,required=True)
    ap.add_argument('--out-prefix',type=Path,required=True)
    args=ap.parse_args()
    result=json.loads(args.accepted_result.read_text())
    if result.get('accepted') is not True or result.get('actual_full_residual_evaluated') is not True:
        raise ValueError('Require a genuinely accepted complete actual F evaluation')
    parent=json.loads(args.parent_request.read_text());settings=dict(parent['settings'])
    field_path=exact_entity(result['accepted_state'])
    packet_path=exact_entity(result['accepted_value_packet'])
    old=load_npz(settings['warm_start']);new=load_npz(field_path)
    allowed_changed={'corrections','parameters','radial_mesh_rebind_definition','tail_search_domain_certificate','tail_domain_transport_diagnostics'}
    allowed_added={'radial_mesh_rebind_definition','finite_grouped_coast_rule_definition','tail_search_domain_kind','tail_search_domain_definition','tail_search_domain_certificate','tail_domain_transport_diagnostics'}
    allowed_removed={'full_gauss_nodes','codazzi_cells','omitted_codazzi_cells'}
    if not set(old)-set(new)<=allowed_removed or not set(new)-set(old)<=allowed_added:
        raise ValueError('Static field schema changed during the accepted transition')
    unchanged=[]
    for key in sorted(set(old)&set(new)-allowed_changed):
        if array_identity(old[key])!=array_identity(new[key]):
            raise ValueError('Static saved field array changed: '+key)
        unchanged.append(key)
    prefix=args.out_prefix
    request_path=prefix.with_name(prefix.name+'-request.json')
    if request_path.exists():raise FileExistsError(request_path)
    settings.update(warm_start=str(field_path),out_prefix=str(prefix),
        owner_stop_file='/tmp/'+prefix.name+'-stop')
    request=dict(parent,created_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
        run_prefix=str(prefix),cache_dir=str(prefix)+'-work',settings=settings,
        input_sha256=result['accepted_state']['sha256'],
        previous_actual_accepted_result=identity(args.accepted_result),
        finite_goal_unchanged_from_parent=True,new_actual_F_evaluations=0)
    atomic_json(request_path,request)
    ctx=NumericalContext(request_path,prefix.with_name(prefix.name+'-baseline-adoption'),install_caches=False)
    ctx.report.update(stage='same_actual_value_packet_from_accepted_state',stage_source=identity(__file__))
    ctx.save_report()
    try:
        old_binding=result['binding']
        keys=('schema','candidate_sha256','reference_inlet_sha256','mathematical_settings',
            'implementation_sources','context_source_sha256','base_context_source_sha256',
            'parent_objective_source_sha256','finite_rule','grouped_rule_definition',
            'original_grouped_context_source_sha256','tail_search_domain_definition',
            'domain_provider_source_sha256','finite_objective_unchanged_by_selected_domain')
        for key in keys:
            if old_binding[key]!=ctx.binding[key]:raise ValueError('Finite numerical goal changed: '+key)
        if ctx.report['initial_projection_change']!=0.:
            raise ValueError('Do not adopt an F packet after changing its actual vector')
        packet=load_actual_packet(packet_path,expected_binding=result['accepted_value_binding'])
        if result['accepted_value_binding']['original_context']!=old_binding:
            raise ValueError('Accepted value packet belongs to a different parent context')
        if result['accepted_value_binding']['accepted_state_sha256']!=result['accepted_state']['sha256']:
            raise ValueError('Accepted value packet is for another saved state')
        if array_identity(packet['vector'])!=array_identity(ctx.vector) or array_identity(packet['vector'])!=result['actual_trial_vector']:
            raise ValueError('Accepted value packet vector differs from the new exact input')
        if array_identity(packet['residual'])!=result['actual_residual']:
            raise ValueError('The already evaluated residual bytes changed')
        if 'finite_grouped_coast_rule_definition' not in new or json.loads(str(new['finite_grouped_coast_rule_definition']))!=ctx.report['grouped_rule_definition']:
            raise ValueError('Saved actual R165 rule differs')
        root=Path(request['cache_dir']);manifest=save_actual_packet(packet,root/'baseline-values',binding=ctx.binding)
        residual,data=packet['residual'],packet['data']
        summary=dict(schema='fd2d-durable-actual-value-baseline-v1',binding=ctx.binding,
            value_packet_manifest=identity(manifest),actual_current_state=result['accepted_state'],
            vector=array_identity(ctx.vector),residual=array_identity(residual),
            residual_squared=float(residual@residual),objective_norm=float(np.linalg.norm(residual)),
            diagnostics=ctx.diag(ctx.vector,data),locations=result['locations'],
            stage_source=identity(__file__),recovered_complete_packet=True,
            actual_new_F_evaluations=0,adopted_previously_evaluated_accepted_result=identity(args.accepted_result),
            unchanged_static_array_names=unchanged,finite_success=False,strong_target_complete=False)
        target=root/'baseline-summary.json';atomic_json(target,summary)
        ctx.save_report(completed=True,actual_baseline_summary=identity(target),
            value_packet_manifest=identity(manifest),initial=summary['diagnostics'],
            actual_value_objective_evaluations=0,adopted_actual_F_without_recalculation=True,
            unchanged_static_array_names=unchanged)
        ctx.event('accepted_actual_packet_adopted',request=str(request_path),
            objective_norm=summary['objective_norm'],manifest=str(manifest),actual_new_F_evaluations=0)
        return 0
    except Exception as exc:
        ctx.save_report(exception=dict(type=type(exc).__name__,message=str(exc),traceback=traceback.format_exc()))
        raise

if __name__=='__main__':raise SystemExit(main())
