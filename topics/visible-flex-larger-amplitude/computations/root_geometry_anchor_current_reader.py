#!/usr/bin/env python3
"""Consume nineteen actual corrected-provider fields from one accepted M32 point.

Author: geometry_audit (GPT-6 Astra Pro; AI-assisted), 2026-11-13.
The original complete-array reader and full-row finite minimax remain unchanged.
The only reader bridge separates the actual outer provider entry from its saved
inner complete-mean SHA. No old field, interpolated old derivative, partial-six
response, or future accepted state is promoted into this current-point model.
"""
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[key]='1'
import argparse
import hashlib
import json
from pathlib import Path
import sys

from root_geometry_anchor_current_interfaces import (
    CONTROL_NAMES,FROZEN,HERE,check_sources,require_response,sha)

INNER='root_actual_geometry_field_complete_mean.py'
INNER_SHA='614a671b86dc1bacccf52d62311c51a7473c83072f9ce39e81ae3e421541dd86'


def read(path):return json.loads(Path(path).read_text())


def verify(plan_path,out_path):
    plan_path,out_path=Path(plan_path),Path(out_path)
    if out_path.exists():raise FileExistsError('A fresh current geometry bridge is required')
    check_sources()
    if sha(HERE/INNER)!=INNER_SHA:raise ValueError('The complete-mean producer changed')
    plan=read(plan_path)
    counts={}
    def check(name,ok):
        counts[name]=counts.get(name,0)+1
        if not ok:raise ArithmeticError(name)
    check('actual_plan_cwd',Path.cwd()==Path(plan['cwd']))
    check('complete_current_nine_control_plan',not plan['baseline_only'] and plan['modes']==32 and
          tuple(r['name'] for r in plan['directions'])==CONTROL_NAMES and len(plan['candidates'])==19)
    interface=plan['current_anchor_complete_geometry_interface']
    check('current_plan_adapter_bound',interface['schema']=='accepted-current-M32-nine-control-anchor-interface-v1' and
          interface['role']=='plan' and interface['exact_reverse_recovers_original_source'] and
          interface['adapter_source_sha256']==sha(HERE/'root_geometry_anchor_current_interfaces.py') and
          interface['entry_source_sha256']==sha(HERE/'root_actual_geometry_anchor_current_plan.py'))
    for path,h in plan['source_and_input_sha256'].items():
        check('actual_plan_source_and_input_hash',sha(path)==h)
    candidates={r['name']:r for r in plan['candidates']}
    check('complete_named_positive_and_negative_pairs',set(candidates)=={'baseline',*[n+s for n in CONTROL_NAMES for s in ('-plus','-minus')]})
    base_command=candidates['baseline']['command']
    q1_command=candidates['actual_q1-plus']['command']
    response_path=Path(q1_command[q1_command.index('--response-data')+1])
    response=read(response_path);require_response(response)
    response_rows={r['direction']:r for r in response['prescribed_low_core_responses']}
    response_rows.update({r['external_field']:r for r in response['additional_core_held_directions']})
    baseline_core=response['baseline']['core']
    check('all_current_core_entries',len(baseline_core)==32)
    grid=read(plan['grid']);radial=len(grid['numerical_t']);angular=grid['angular']
    check('complete_current_grid',grid['all_original_raw_nodes_evaluated'] and
          grid['all_original_raw_nodes_used_in_cubic'] and grid['original_raw_nodes']==response['nodes'] and
          radial>=response['nodes'] and angular>=768 and angular%768==0)
    check('actual_current_quintic_witness_present',any(w.get('same_accepted_baseline_physical_polynomial_witness') for w in grid['known_reference_witnesses']))
    from strong_frontload_anchor_loader_adapter import build
    outer=HERE/'root_actual_geometry_field_anchor.py'
    namespace,unused=build('geometry',outer)
    unused_entry,unused_main,expected_preparation=namespace['prepare_entry']()
    check('actual_uniform_outer_entry',plan['geometry_wrapper']==str(outer))
    observed=[];total_chunks=0;total_bytes=0
    for row in plan['candidates']:
        report,owned,field=map(read,(row['report'],row['resource'],row['field']))
        command=row['command'][row['command'].index('--')+1:]
        prefix=command[command.index('--out-prefix')+1]
        prep_path=Path(prefix+'-initial-laws-geometry-source.json')
        preparation=read(prep_path);geom=report['geometry_fields']
        check('owned_actual_completed_field',owned['exitcode']==0 and owned['wait4_observed'] and
              owned['termination_signal'] is None and owned['command']==command and
              report['finished'] and report['finite_domain_passed'] and report['worker_start_attempts']==0 and
              not report['nonlinear_solution'] and not report['true_new_H_tail_evaluated'])
        check('explicit_outer_and_inner_identity',command[1]==str(outer) and
              report['source_sha256'].get(str(outer))==FROZEN[outer.name] and
              geom['wrapper_sha256']==INNER_SHA and preparation==expected_preparation)
        for path,h in preparation['source_inputs'].items():
            check('every_actual_provider_source_bound',sha(path)==h and report['source_sha256'].get(path)==h)
        for flag in ('--actual-reference','--actual-reference-raw','--actual-reference-tail','--tail-config',
                     '--frozen-reference-ready','--frozen-calibration-ledger','--port','--source-topic'):
            check('same_current_physical_and_tail_inputs',command[command.index(flag)+1]==base_command[base_command.index(flag)+1])
        check('same_current_grid_and_complete_mean',geom['grid_sha256']==sha(plan['grid']) and
              geom['shape']==[radial,angular,3] and geom['all_raw_nodes_and_modes_retained'] and
              geom['complete_mean_height'] and geom['mean_quadrature']['angular']==1552 and
              geom['mean_quadrature']['mean_height_first_second_same_angular_rule'])
        if row['direction']:
            check('same_current_response_for_every_direction',command[command.index('--response-data')+1]==str(response_path) and
                  report['source_sha256'].get(str(response_path))==sha(response_path))
            direction=response_rows[row['direction']]
            expected_core=[c+row['step']*d for c,d in zip(baseline_core,direction['core_derivative'])]
            if row['direction'] in CONTROL_NAMES[3:]:
                check('same_neutral_physical_step',command[command.index('--neutral-control-step')+1]==row['direction']+'='+repr(row['step']))
        else:
            expected_core=baseline_core
            check('baseline_requires_no_response', '--response-data' not in command)
        check('all_32_original_current_core_entries_retained',len(geom['actual_core'])==32 and
              max(abs(x-y) for x,y in zip(geom['actual_core'],expected_core))<=3e-14)
        check('complete_storage_identity',field==geom['storage'] and field['complete'] and
              field['dtype']=='float64' and field['shape']==geom['shape'] and sha(row['field'])==geom['sha256'])
        cursor=0;size=0
        for chunk in field['chunks']:
            path=Path(row['field']).with_name(chunk['file'])
            check('complete_contiguous_chunks',chunk['start']==cursor and cursor<chunk['end']<=radial and Path(chunk['file']).name==chunk['file'])
            check('actual_full_chunk_identity',sha(path)==chunk['sha256'] and path.stat().st_size==chunk['bytes'])
            cursor=chunk['end'];size+=chunk['bytes'];total_chunks+=1
        check('full_current_radial_coverage',cursor==radial and size==geom['bytes']);total_bytes+=size
        observed.append(dict(name=row['name'],direction=row['direction'],step=row['step'],
            report=row['report'],report_sha256=sha(row['report']),resource=row['resource'],resource_sha256=sha(row['resource']),
            field=row['field'],field_sha256=sha(row['field']),source_preparation=str(prep_path),
            source_preparation_sha256=sha(prep_path),chunks=len(field['chunks']),compressed_bytes=size,
            wall_seconds=owned['wall_seconds'],peak_rss_kib=owned['peak_rss_kib']))
    record=dict(schema='actual-current-M32-nineteen-field-anchor-reader-bridge-v1',scope=__doc__,
        author='geometry_audit (GPT-6 Astra Pro; AI-assisted)',source_sha256=sha(__file__),
        all_identity_gates=True,gate_count=sum(counts.values()),gate_multiplicities=counts,
        plan=str(plan_path),plan_sha256=sha(plan_path),response_file=str(response_path),response_sha256=sha(response_path),
        full_response_scope='All nine current external full/half columns; all current combined observations preserved.',
        controls=list(CONTROL_NAMES),fields=observed,total_fields=19,total_chunks=total_chunks,
        total_compressed_derived_array_bytes=total_bytes,common_shape=[radial,angular,3],complete_mean_angular=1552,
        full_finite_row_count=5*radial*angular,original_complete_array_loader_unchanged=True,
        original_minimax_and_all_five_row_families_unchanged=True,old_coarse_or_stale_derivative_fields_used=False,
        new_ODE_Node_or_geometry_calls=0,continuous_geometry_or_new_solution_claimed=False,derived_arrays_scratch_only=True)
    out_path.parent.mkdir(parents=True,exist_ok=True)
    out_path.write_text(json.dumps(record,indent=2)+'\n')
    from root_geometry_minimax_from_plan import load_field as original_loader
    by_name={r['name']:r for r in observed}
    def checked_loader(row,original_plan,destination):
        if original_plan!=plan:raise ValueError('An unverified current plan was substituted')
        saved=by_name[row['name']]
        for key in ('report','resource','field'):
            if sha(row[key])!=saved[key+'_sha256']:raise ValueError('An actual field changed after identity verification')
        return original_loader(row,dict(original_plan,geometry_wrapper=str(HERE/INNER)),destination)
    return plan,record,checked_loader


def main():
    parser=argparse.ArgumentParser(add_help=False,description=__doc__)
    parser.add_argument('--plan',type=Path,required=True)
    parser.add_argument('--bridge-out',type=Path,required=True)
    parser.add_argument('--out',type=Path)
    parser.add_argument('--verify-only',action='store_true')
    args,rest=parser.parse_known_args()
    plan,record,loader=verify(args.plan,args.bridge_out)
    print(json.dumps(dict(event='actual_current_nineteen_geometry_bridge_verified',fields=19,
        gates=record['gate_count'],path=str(args.bridge_out),sha256=sha(args.bridge_out))),flush=True)
    if args.verify_only:return
    if args.out is None or args.out.exists():raise ValueError('A fresh finite minimax output is required')
    import root_geometry_minimax_initial_laws_controls as algorithm
    original_loader=algorithm.load_field;original_argv=sys.argv
    algorithm.load_field=loader
    sys.argv=[original_argv[0],'--plan',str(args.plan),'--out',str(args.out),*rest]
    try:algorithm.main()
    finally:algorithm.load_field=original_loader;sys.argv=original_argv
    result=read(args.out)
    result['actual_anchor_current_geometry_bridge']=dict(path=str(args.bridge_out),sha256=sha(args.bridge_out),
        source_sha256=sha(__file__),all_identity_gates=True,gate_count=record['gate_count'],
        controls=list(CONTROL_NAMES),original_algorithm_main_unchanged=True,
        current_M32_fields_only=True,old_coarse_or_stale_derivative_fields_used=False)
    tmp=args.out.with_name(args.out.name+'.current-anchor-bridge.tmp')
    tmp.write_text(json.dumps(result,indent=2)+'\n');tmp.replace(args.out)
    print(json.dumps(dict(event='actual_current_nine_minimax_finished',path=str(args.out),sha256=sha(args.out))),flush=True)


if __name__=='__main__':main()
