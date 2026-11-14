#!/usr/bin/env python3
"""Verify the real thirteen-plus-four q122 fields before full-row consumption.

Author: geometry_audit (GPT-6 Astra Pro; AI-assisted), 2026-11-13.
All original thirteen commands, metadata and source identities are unchanged.
The four supplemental fields bind the corrected provider anchor explicitly.
The assembled response is selected by its explicit verified plan key, never
by rewriting the historical q1 field command. Every original loader and LP
gate remains; these are M28 finite design fields, not an M32 Jacobian.
"""
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[key]='1'
import argparse
import hashlib
import inspect
import json
from pathlib import Path
import sys

HERE=Path(__file__).resolve().parent
PLAN_SHA='0bfc0774122aa74cb10b242ffb964ef57db7e81526a56382f1333ca615f63ff1'
RESPONSE_SHA='5c83df392bb2e9ed75b767e0ed90fc85bfb83ae545945acb4177d200891937c0'
ORIGINAL_PLAN_SHA='240b5d5bd2bd51019296bab9c8eaa28d30de04e195cc2273a38c2d8c61cefab3'
ORIGINAL_BRIDGE_SHA='226e2e5d5c594ebb8665e09ad55dd721f031236e1f0b85528ef9f51d1efe07cf'
EXPECTED={
 'root_geometry_minimax_initial_laws_controls.py':'ccdcc95d3e7dd2a1447714578e6976179f1b5c32d3495e13a074399872c31e57',
 'root_geometry_minimax_from_plan.py':'4fdd46bf198e573bd83a86195143caa86d7105d3847d4e12431d844c2111e213',
 'root_actual_geometry_field_initial_laws.py':'7efa4f617321c5832b59b8ee4c451fc53838ddee61025581b6e5eeda459b1b09',
 'root_actual_geometry_field_anchor.py':'da6726c130503113a9483da2365cea70e59f22f26e09eb19b08ba57632229a77',
 'root_actual_geometry_field_complete_mean.py':'614a671b86dc1bacccf52d62311c51a7473c83072f9ce39e81ae3e421541dd86',
 'strong_monotone_initial_speed_anchor.py':'583af82cdd6bb672325844587d8aac67e47365ccb5152ac2eae543837adc0ffc',
 'strong_frontload_anchor_loader_adapter.py':'aa32079179e20a95493cd911185ea69e7df2b4d5b150a713597e9d2f9fd73c86',
}

def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def read(p):return json.loads(Path(p).read_text())

def verify(plan_path,out_path):
    """Return (original plan, frozen bridge, checked complete-field loader)."""
    plan_path,out_path=Path(plan_path),Path(out_path)
    if out_path.exists():raise FileExistsError('Fresh complete eight-field bridge required')
    if sha(plan_path)!=PLAN_SHA:raise ValueError('Require the actually prepared symmetric-vd plan')
    plan=read(plan_path);counts={}
    def check(name,ok):
        counts[name]=counts.get(name,0)+1
        if not ok:raise ArithmeticError(name)
    check('exact_original_working_directory',Path.cwd()==Path(plan['cwd']))
    for name,h in EXPECTED.items():check('frozen_delegated_source',sha(HERE/name)==h)
    for path,h in plan['source_and_input_sha256'].items():check('all_original_and_new_source_input_hashes',sha(path)==h)
    old_plan=read(plan['original_plan']);check('immutable_original_plan',sha(plan['original_plan'])==ORIGINAL_PLAN_SHA)
    inventory=read(plan['original_complete_field_inventory'])
    check('full_original_field_inventory',inventory['all_gates'] and inventory['total_fields']==13 and sha(plan['original_complete_field_inventory'])==plan['original_complete_field_inventory_sha256'])
    old_bridge_path=next(Path(k) for k,v in inventory['input_sha256'].items() if v==ORIGINAL_BRIDGE_SHA)
    old_bridge=read(old_bridge_path)
    check('actual_original_source_bridge',sha(old_bridge_path)==ORIGINAL_BRIDGE_SHA and old_bridge['all_identity_gates'] and old_bridge['plan_sha256']==ORIGINAL_PLAN_SHA)
    check('all_original_thirteen_commands_and_records_unchanged',plan['candidates'][:13]==old_plan['candidates'])
    names=[r['name'] for r in plan['directions']]
    check('all_eight_explicit_actual_controls',names==['actual_q1','actual_q4','actual_c6','vu','descending_turn_curvature','start_acceleration','initial_speed_frontload','vd'] and len(plan['candidates'])==17)
    check('actual_symmetric_new_steps',plan['directions'][-2]['step']==.01 and plan['directions'][-1]['step']==.001)
    response_path=Path(plan['assembled_response_file']);response=read(response_path)
    check('actual_complete_eight_response_identity',sha(response_path)==RESPONSE_SHA==plan['assembled_response_sha256'])
    first=old_plan['candidates'][1]['command'];old_response_path=Path(first[first.index('--response-data')+1]);old_response=read(old_response_path)
    check('same_baseline_and_original_six_combined_rows',response['baseline']==old_response['baseline'] and response['prescribed_low_core_responses']==old_response['prescribed_low_core_responses'] and response['additional_core_held_directions'][:3]==old_response['additional_core_held_directions'])
    check('partial_recovery_scope_preserved',response['partial_recovery'] and response['all_eight_external_full_and_half_gates_observed'] and not response['all_eight_combined_half_vectors_available'] and not response['complete_eight_combined_half_gate_claimed'] and not response['new_solution'])
    from strong_frontload_anchor_loader_adapter import build
    anchor=HERE/'root_actual_geometry_field_anchor.py';ns,unused=build('geometry',anchor)
    unused_entry,unused_main,expected_preparation=ns['prepare_entry']()
    old_observed={r['name']:r for r in old_bridge['fields']}
    output=[];total_chunks=0;total_bytes=0
    for index,row in enumerate(plan['candidates']):
        report,owned,field=map(read,(row['report'],row['resource'],row['field']))
        actual_command=row['command'][row['command'].index('--')+1:]
        prefix=actual_command[actual_command.index('--out-prefix')+1]
        prep_path=Path(prefix+'-initial-laws-geometry-source.json');preparation=read(prep_path)
        geom=report['geometry_fields']
        check('real_owned_complete_finite_field',owned['exitcode']==0 and report['finished'] and report['finite_domain_passed'] and report['worker_start_attempts']==0 and not report['nonlinear_solution'] and not report['true_new_H_tail_evaluated'])
        check('actual_historical_command_preserved',owned['command']==actual_command)
        check('saved_inner_geometry_identity',geom['wrapper_sha256']==EXPECTED['root_actual_geometry_field_complete_mean.py'])
        if index<13:
            original=old_observed[row['name']]
            for key in ('report','resource','field'):
                check('original_full_field_metadata_unchanged',sha(row[key])==original[key+'_sha256'])
            check('original_outer_preparation_unchanged',sha(prep_path)==original['source_preparation_sha256'] and actual_command[1]==str(HERE/'root_actual_geometry_field_initial_laws.py'))
            check('original_zero_frontload_field',report['warm_profile'].get('initial_speed_frontload',0.)==0.)
        else:
            check('new_actual_corrected_anchor_outer',actual_command[1]==str(anchor) and report['source_sha256'].get(str(anchor))==EXPECTED[anchor.name])
            check('actual_new_provider_preparation_equal',preparation==expected_preparation)
            for path,h in preparation['source_inputs'].items():
                check('every_actual_new_provider_source_bound',sha(path)==h and report['source_sha256'].get(path)==h)
            check('new_real_assembled_response_consumed',actual_command[actual_command.index('--response-data')+1]==str(response_path) and report['source_sha256'].get(str(response_path))==RESPONSE_SHA)
            check('new_real_neutral_step_matches',actual_command[actual_command.index('--neutral-control-step')+1]==row['direction']+'='+repr(row['step']))
            check('new_owned_wait4_observed',owned['wait4_observed'])
        check('all_original_raw_modes_grid_and_mean_retained',geom['grid_sha256']==sha(plan['grid']) and geom['shape']==[3764,768,3] and len(geom['actual_core'])==28 and geom['all_raw_nodes_and_modes_retained'] and geom['complete_mean_height'] and geom['mean_quadrature']['angular']==1360 and geom['mean_quadrature']['mean_height_first_second_same_angular_rule'])
        check('actual_complete_manifest_bound',field==geom['storage'] and field['complete'] and field['dtype']=='float64' and sha(row['field'])==geom['sha256'])
        cursor=0;size=0
        for chunk in field['chunks']:
            path=Path(row['field']).with_name(chunk['file'])
            check('contiguous_complete_chunk_coverage',chunk['start']==cursor and cursor<chunk['end']<=3764 and Path(chunk['file']).name==chunk['file'])
            check('every_complete_derived_array_hash_and_size',sha(path)==chunk['sha256'] and path.stat().st_size==chunk['bytes'])
            cursor=chunk['end'];size+=chunk['bytes'];total_chunks+=1
        check('complete_radial_end_and_saved_bytes',cursor==3764 and size==geom['bytes']);total_bytes+=size
        output.append(dict(name=row['name'],direction=row['direction'],step=row['step'],
            report=row['report'],report_sha256=sha(row['report']),resource=row['resource'],resource_sha256=sha(row['resource']),
            field=row['field'],field_sha256=sha(row['field']),source_preparation=str(prep_path),source_preparation_sha256=sha(prep_path),
            executed_outer=actual_command[1],saved_inner_sha256=geom['wrapper_sha256'],chunks=len(field['chunks']),compressed_bytes=size,
            wall_seconds=owned['wall_seconds'],peak_rss_kib=owned['peak_rss_kib'],
            scalar_finite_summaries={k:geom[k] for k in ('kappa_abs_max_sample','twice_radius_max_sample','height_abs_max_sample','horizontal_radius_max_sample','minimum_frenet_margin_sample')},
            full_core=geom['actual_core'],physical_profile=geom['physical_profile']))
    record=dict(schema='actual-q122-thirteen-plus-four-complete-field-reader-bridge-v1',scope=__doc__,
        all_identity_and_chunk_gates=True,gate_count=sum(counts.values()),gate_multiplicities=counts,
        source_sha256=sha(__file__),frozen_delegated_sources=EXPECTED,plan=str(plan_path),plan_sha256=PLAN_SHA,
        assembled_response_file=str(response_path),assembled_response_sha256=RESPONSE_SHA,
        original_thirteen_fields_retained_verbatim=True,fields=output,total_fields=17,total_chunks=total_chunks,
        total_compressed_derived_array_bytes=total_bytes,complete_mean_angular=1360,common_shape=[3764,768,3],
        partial_control_response_scope=plan['partial_control_response_scope'],
        explicit_symmetric_vd_rescale=plan['explicit_symmetric_vd_rescale'],
        old_M28_baseline_and_design_slopes_not_new_fine_M32_J=True,
        complete_array_read_delegated_to_original_loader_with_only_verified_outer_inner_identity_bridge=True,
        new_ODE_Node_Newton_or_geometry_calls=0,derived_arrays_scratch_only=True)
    out_path.write_text(json.dumps(record,indent=2)+'\n')
    from root_geometry_minimax_from_plan import load_field as original_loader
    observed={r['name']:r for r in output}
    def checked_loader(row,actual_plan,destination):
        if actual_plan!=plan:raise ValueError('Unverified complete-field plan substituted')
        old=observed[row['name']]
        for key in ('report','resource','field'):
            if sha(row[key])!=old[key+'_sha256']:raise ValueError('An actual verified field changed before loading')
        return original_loader(row,dict(actual_plan,geometry_wrapper=str(HERE/'root_actual_geometry_field_complete_mean.py')),destination)
    return plan,record,checked_loader

def main():
    p=argparse.ArgumentParser(add_help=False,description=__doc__)
    p.add_argument('--plan',type=Path,required=True);p.add_argument('--bridge-out',type=Path,required=True)
    p.add_argument('--out',type=Path);p.add_argument('--verify-only',action='store_true')
    a,remaining=p.parse_known_args()
    plan,record,loader=verify(a.plan,a.bridge_out)
    print(json.dumps(dict(event='actual_eight_geometry_bridge_verified',fields=17,gates=record['gate_count'],
        path=str(a.bridge_out),sha256=sha(a.bridge_out))),flush=True)
    if a.verify_only:return
    if a.out is None or a.out.exists():raise ValueError('Fresh minimax result path required')
    import root_geometry_minimax_initial_laws_controls as algorithm
    source=inspect.getsource(algorithm.main)
    before="    response_path=Path(candidate[candidate.index('--response-data')+1])"
    after="    response_path=Path(plan['assembled_response_file'])"
    if source.count(before)!=1:raise ValueError('Original response selection moved')
    changed=source.replace(before,after,1)
    if changed.replace(after,before,1)!=source:raise ValueError('Unexpected algorithm source change')
    ns=dict(algorithm.main.__globals__,load_field=loader)
    exec(compile(changed,'<actual-eight-field-response-selection-only>','exec'),ns)
    argv=sys.argv;sys.argv=[argv[0],'--plan',str(a.plan),'--out',str(a.out),*remaining]
    try:ns['main']()
    finally:sys.argv=argv
    result=read(a.out);result['actual_eight_source_and_response_bridge']=dict(path=str(a.bridge_out),sha256=sha(a.bridge_out),
        source_sha256=sha(__file__),all_identity_gates=True,gate_count=record['gate_count'],
        original_algorithm_main_sha256=hashlib.sha256(source.encode()).hexdigest(),
        response_selection_only_main_sha256=hashlib.sha256(changed.encode()).hexdigest(),
        original_all_geometry_LP_rows_and_loader_gates_unchanged=True,partial_scope=plan['partial_control_response_scope'])
    tmp=a.out.with_name(a.out.name+'.eight-source-bridge.tmp');tmp.write_text(json.dumps(result,indent=2)+'\n');tmp.replace(a.out)

if __name__=='__main__':main()
