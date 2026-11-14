#!/usr/bin/env python3
"""Consume outer initial-law and inner complete-mean identities separately.

Author: geometry_audit (GPT-6 Astra Pro; AI-assisted), 2026-11-13.
The actual outer entry delegates geometry.main() to the unchanged inner
complete-mean producer. Consequently the saved geometry wrapper SHA is the
inner SHA, while the executed command and saved source_sha256 bind the outer
entry and its inlet hooks. This bridge verifies both layers and every saved
source-preparation record before invoking the unchanged full-field loader.
It does not alter a plan, field, report, mean rule, physical datum or LP row.
Only the actually available six zero-frontload q122 directions are allowed.
"""
import os
for _key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[_key]='1'
import argparse
import hashlib
import json
from pathlib import Path
import sys

HERE=Path(__file__).resolve().parent
EXPECTED={
    'root_geometry_minimax_initial_laws_controls.py':'ccdcc95d3e7dd2a1447714578e6976179f1b5c32d3495e13a074399872c31e57',
    'root_geometry_minimax_from_plan.py':'4fdd46bf198e573bd83a86195143caa86d7105d3847d4e12431d844c2111e213',
    'root_geometry_minimax_control_constraints.py':'7d5f91ca193ef9d6c02070b5c062f278ab29a01f070eb12b66c8c9dff701cc63',
    'root_actual_geometry_field_initial_laws.py':'7efa4f617321c5832b59b8ee4c451fc53838ddee61025581b6e5eeda459b1b09',
    'root_actual_geometry_field_complete_mean.py':'614a671b86dc1bacccf52d62311c51a7473c83072f9ce39e81ae3e421541dd86',
}
PLAN_SHA='240b5d5bd2bd51019296bab9c8eaa28d30de04e195cc2273a38c2d8c61cefab3'


def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def read(path):return json.loads(Path(path).read_text())


def main():
    parser=argparse.ArgumentParser(add_help=False,description=__doc__)
    parser.add_argument('--plan',type=Path,required=True)
    parser.add_argument('--out',type=Path,required=True)
    parser.add_argument('--bridge-out',type=Path,required=True)
    args,remaining=parser.parse_known_args()
    if args.out.exists() or args.bridge_out.exists():raise FileExistsError('Fresh bridged minimax outputs required')
    if sha(args.plan)!=PLAN_SHA:raise ValueError('This bridge is only for the actual immutable partial-six plan')
    for name,h in EXPECTED.items():
        if sha(HERE/name)!=h:raise ValueError('A frozen delegated-reader source changed: '+name)
    plan=read(args.plan)
    outer=HERE/'root_actual_geometry_field_initial_laws.py'
    inner=HERE/'root_actual_geometry_field_complete_mean.py'
    if (Path(plan['geometry_wrapper'])!=outer or len(plan['candidates'])!=13 or
        [r['name']for r in plan['directions']]!=['actual_q1','actual_q4','actual_c6','vu','descending_turn_curvature','start_acceleration']):
        raise ValueError('Only the same actual six directions and baseline are permitted')
    for path,wanted in plan['source_and_input_sha256'].items():
        if sha(path)!=wanted:raise ValueError('Original immutable plan identity changed: '+path)
    import root_actual_geometry_field_initial_laws as initial
    _,_,current_provenance=initial.prepare_entry()
    if (current_provenance['source_sha256']!=EXPECTED[outer.name] or
        current_provenance['complete_mean_original_source_sha256']!=EXPECTED[inner.name] or
        not current_provenance['exact_reverse_recovers_original_main']):
        raise ValueError('The actual outer-to-inner source delegation was not recovered')
    # The literal call is also pinned, so the two SHA labels are not inferred
    # merely from a coincidentally equal field or sample value.
    source=outer.read_text()
    if source.count('    import root_actual_geometry_field_complete_mean as geometry\n')!=1 or source.count('        geometry.main()\n')!=1:
        raise ValueError('The actual outer delegation changed')
    rows=[];checks=0
    for row in plan['candidates']:
        report,formal,field=map(read,(row['report'],row['resource'],row['field']))
        command=row['command'];actual_command=command[command.index('--')+1:]
        prefix=actual_command[actual_command.index('--out-prefix')+1]
        provenance_path=Path(prefix+'-initial-laws-geometry-source.json')
        provenance=read(provenance_path)
        if (formal['exitcode']!=0 or formal['command']!=actual_command or actual_command[1]!=str(outer) or
            report['source_sha256'].get(str(outer))!=EXPECTED[outer.name] or
            report['geometry_fields']['wrapper_sha256']!=EXPECTED[inner.name] or
            provenance!=current_provenance):
            raise ValueError('Executed outer, saved hook preparation or actual inner identity differs: '+row['name'])
        checks+=6
        for path,h in provenance['source_inputs'].items():
            if report['source_sha256'].get(path)!=h or sha(path)!=h:
                raise ValueError('A genuinely executed provider source is not bound: '+path)
            checks+=1
        if report['warm_profile'].get('initial_speed_frontload',0.)!=0. or report['warm_profile'].get('initial_speed_pulse',0.)!=0.:
            raise ValueError('This actual g0 bridge cannot certify a future nonzero inlet hook')
        if (not field['complete'] or field!=report['geometry_fields']['storage'] or
            field['shape']!=[3764,768,3] or not report['geometry_fields']['all_raw_nodes_and_modes_retained']):
            raise ValueError('The complete actual field metadata changed')
        checks+=2
        rows.append(dict(name=row['name'],report=row['report'],report_sha256=sha(row['report']),
                         resource=row['resource'],resource_sha256=sha(row['resource']),
                         field=row['field'],field_sha256=sha(row['field']),
                         source_preparation=str(provenance_path),source_preparation_sha256=sha(provenance_path),
                         actual_executed_outer_sha256=EXPECTED[outer.name],actual_saved_inner_sha256=EXPECTED[inner.name]))
    bridge=dict(schema='actual-initial-laws-outer-and-complete-mean-inner-reader-bridge-v1',scope=__doc__,
                source_sha256=sha(__file__),frozen_sources=EXPECTED,plan=str(args.plan),plan_sha256=PLAN_SHA,
                all_identity_gates=True,identity_gate_count=checks,fields=rows,
                partial_control_response_scope=plan['partial_control_response_scope'],
                geometry_data_recomputed=False,saved_source_identity_relabelled=False,
                original_reader_all_other_gates_preserved=True,complete_array_read_and_hash_check_delegated_to_original_loader=True,
                no_future_nonzero_frontload_or_vd_direction_included=True)
    args.bridge_out.parent.mkdir(parents=True,exist_ok=True)
    args.bridge_out.write_text(json.dumps(bridge,indent=2)+'\n')
    print(json.dumps(dict(event='actual_geometry_wrapper_bridge_verified',fields=len(rows),gates=checks,
                         path=str(args.bridge_out),sha256=sha(args.bridge_out))),flush=True)
    import root_geometry_minimax_initial_laws_controls as algorithm
    original_loader=algorithm.load_field
    observed={r['name']:r for r in rows}
    def checked_delegated_loader(row,original_plan,destination):
        old=observed[row['name']]
        for key in ('report','resource','field'):
            if sha(row[key])!=old[key+'_sha256']:raise ValueError('A verified field changed before full loading')
        if original_plan!=plan:raise ValueError('An unverified plan was substituted')
        internal_plan=dict(original_plan,geometry_wrapper=str(inner))
        return original_loader(row,internal_plan,destination)
    algorithm.load_field=checked_delegated_loader
    argv=sys.argv
    sys.argv=[argv[0],'--plan',str(args.plan),'--out',str(args.out),*remaining]
    try:algorithm.main()
    finally:algorithm.load_field=original_loader;sys.argv=argv
    result=read(args.out)
    result['actual_outer_inner_wrapper_bridge']=dict(path=str(args.bridge_out),sha256=sha(args.bridge_out),
        source_sha256=sha(__file__),all_identity_gates=True,identity_gate_count=checks,
        original_loader_and_all_LP_rows_unchanged=True,partial_six_scope=plan['partial_control_response_scope'])
    temporary=args.out.with_name(args.out.name+'.actual-wrapper-bridge.tmp')
    temporary.write_text(json.dumps(result,indent=2)+'\n');temporary.replace(args.out)
    print(json.dumps(dict(event='actual_partial_six_minimax_finished',path=str(args.out),sha256=sha(args.out))),flush=True)


if __name__=='__main__':main()
