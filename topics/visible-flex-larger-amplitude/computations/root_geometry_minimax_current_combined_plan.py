#!/usr/bin/env python3
"""Prepare one complete warm field from an explicit five/six-control choice.

All actual response fields are combined by the unchanged production warm
constructor.  This re-evaluates the geometry of the combined warm candidate,
not its linearized predicted geometry, and still does not solve a new BVP or
tail.  Selection is explicit so a size/curvature/amplitude tradeoff is visible.
"""
from __future__ import annotations
import argparse
import copy
import hashlib
import json
from pathlib import Path


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--plan',type=Path,required=True)
    ap.add_argument('--minimax',type=Path,required=True)
    ap.add_argument('--choice',type=int,required=True)
    ap.add_argument('--out-prefix',type=Path,required=True)
    args=ap.parse_args()
    plan=json.loads(args.plan.read_text())
    model=json.loads(args.minimax.read_text())
    if (model['plan_sha256']!=sha(args.plan)
            or model['source_sha256']!=sha(Path(__file__).with_name('root_geometry_minimax_current_controls.py'))
            or model['minimax_algorithm_source_sha256']!=sha(Path(__file__).with_name('root_geometry_minimax_variable_controls.py'))
            or model['stale_geometry_slopes_used'] or model['accepted_nonlinear_solution']
            or model['continuous_geometry_certified'] or model['actual_reach_certified']):
        raise ValueError('Require the completed current-baseline finite minimax identity')
    for item in model['inputs']:
        if sha(item['path'])!=item['sha256']:
            raise ValueError('A completed finite-model input changed: '+item['path'])
    for path,wanted in plan['source_and_input_sha256'].items():
        if sha(path)!=wanted:
            raise ValueError('A prepared source/input changed: '+path)
    if not 0<=args.choice<len(model['predictions']):
        raise ValueError('An explicit existing candidate index is required')
    selected=model['predictions'][args.choice]
    if not selected.get('success') or not selected.get('all_finite_rows_checked'):
        raise ValueError('The selected finite model did not pass all original rows')
    original_names=['actual_q1','actual_q4','actual_c6','vu','descending_turn_curvature']
    names=[d['name'] for d in plan['directions']]
    if names not in (original_names,original_names+['start_acceleration']):
        raise ValueError('All five original controls and optional sixth actual control must remain in order')
    if model['control_count']!=len(names) or selected['control_count']!=len(names):
        raise ValueError('The fitted current control count differs from the original complete plan')
    steps=selected['physical_steps']
    for index,direction in enumerate(plan['directions']):
        normalized=steps[direction['name']]/direction['step']
        if abs(normalized-selected['normalized_steps'][index])>1e-10:
            raise ValueError('The recorded normalized and physical design steps differ')
        if index and abs(normalized)>selected['other_control_trust_factor']+1e-10:
            raise ValueError('The selected control exceeds its recorded finite-model trust box')
    row=copy.deepcopy(next(r for r in plan['candidates'] if r['name']=='baseline'))
    command=row['command']
    response_path=Path(model['response_file'])
    if sha(response_path)!=model['response_sha256']:
        raise ValueError('The full actual response changed')
    response=json.loads(response_path.read_text())
    if '--response-data' in command:
        if command[command.index('--response-data')+1]!=str(response_path):
            raise ValueError('The baseline command names another actual response')
    else:
        command+=['--response-data',str(response_path)]
    response_rows={r['direction']:r for r in response['prescribed_low_core_responses']}
    response_rows.update({r['external_field']:r for r in response['additional_core_held_directions']})
    target=list(plan['baseline_core'])
    profile=dict(response['baseline']['profile'])
    for index,name in enumerate(names):
        step=steps[name]
        if index<3:
            target[index]+=step
        elif step:
            command+=['--neutral-control-step',name+'='+repr(step)]
        for key,derivative in response_rows[name]['physical_profile_derivative'].items():
            profile[key]+=step*derivative
    case=Path(str(args.out_prefix)+'-combined')
    out=Path(str(args.out_prefix)+'-plan.json')
    if out.exists() or list(case.parent.glob(case.name+'*')):
        raise FileExistsError('Use a fresh combined-candidate prefix')
    report,formal,field,log=[Path(str(case)+suffix) for suffix in
                          ('-screen.json','-resource.json','-field.json','-log.txt')]
    for flag,value in [('--out',formal),('--out-prefix',case),
                       ('--inspect-warm-output',report),('--geometry-array',field)]:
        command[command.index(flag)+1]=str(value)
    at=command.index('--target-core')+1
    command[at:at+3]=list(map(repr,target))
    row.update(name='combined',direction=None,step=None,expected_core=target,
        expected_profile=profile,command=command,report=str(report),resource=str(formal),
        field=str(field),log=str(log),complete_physical_steps=steps)
    hashes=dict(plan['source_and_input_sha256'])
    for path in (args.plan,args.minimax,Path(__file__)):
        hashes[str(path)]=sha(path)
    out.write_text(json.dumps(dict(scope=__doc__,prepared_only=True,executed=False,
        nonlinear_solution=False,new_tail_evaluation=False,cwd=plan['cwd'],
        grid=plan['grid'],geometry_wrapper=plan['geometry_wrapper'],
        source_and_input_sha256=hashes,baseline_core=plan['baseline_core'],modes=plan['modes'],
        directions=plan['directions'],candidates=[row],selected_minimax_candidate_index=args.choice,
        selected_minimax_candidate=selected,selection_rule='Explicit current-minimax candidate index.',
        limitations=plan['limitations']),indent=2)+'\n')
    print(json.dumps(dict(plan=str(out),sha256=sha(out),choice=args.choice,physical_steps=steps)),flush=True)


if __name__=='__main__':
    main()
