#!/usr/bin/env python3
"""Build the original warm/BVP argv for an actually screened full-field guess.

This reads a completed compact design screen and the complete current
responses. The original accepted A inputs, full-flow tail predictor, BVP
unknowns, tolerances and final gates remain. Audited exact-old-H reuse flags
are deliberately absent because a nonzero warm response changes H.
"""
from __future__ import annotations
import argparse
import json
from pathlib import Path
import hashlib


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--template-plan',type=Path,required=True)
    parser.add_argument('--screen',type=Path,required=True)
    parser.add_argument('--response',type=Path,required=True)
    parser.add_argument('--work',type=Path,required=True)
    parser.add_argument('--prefix',required=True)
    parser.add_argument('--out',type=Path,required=True)
    parser.add_argument('--stage',choices=('warm','actual'),required=True)
    parser.add_argument('--candidate',type=int)
    parser.add_argument('--factor',type=float,default=1.)
    args=parser.parse_args()
    template,screen,response=[json.loads(path.read_text()) for path in (args.template_plan,args.screen,args.response)]
    if not screen.get('finished') or not response.get('finished') or response.get('new_solution'):
        raise ValueError('A completed screen and same-state response collection are required')
    candidates=screen['combined_warm_geometry']
    if args.candidate is None:
        viable=[(i,row) for i,row in enumerate(candidates) if row['finite_domain_passed']
            and row['summary']['kappa_times_size_proxy']<33.3333333333333
            and row['summary']['complete_core_axis_gap']>screen['baseline']['complete_core_axis_gap']]
        if not viable:raise ValueError('No finite screened positive-growth candidate meets the sample design budget')
        index,selected=max(viable,key=lambda pair:pair[1]['summary']['gap_over_size_proxy'])
    else:
        index=args.candidate;selected=candidates[index]
        if not selected['finite_domain_passed']:raise ValueError('The selected finite warm did not exist')
    if not 0<args.factor<=1:raise ValueError('Use a positive shortening factor no greater than one')
    steps={key:args.factor*value for key,value in selected['steps'].items()}
    rows={row['direction']:row for row in response['prescribed_low_core_responses']}
    rows.update({row['external_field']:row for row in response['additional_core_held_directions']})
    core=list(response['baseline']['core'])
    for name,weight in steps.items():
        for i,value in enumerate(rows[name]['core_derivative']):core[i]+=weight*value
    cmd=list(template['command'])
    # The template contains three physical target values.
    def delete(flag,count):
        while flag in cmd:
            i=cmd.index(flag);del cmd[i:i+count+1]
    for flag,count in (('--prepare-only',0),('--response-data',1),('--neutral-control-step',1),
            ('--initial-audited-tail-packet',1),('--initial-audited-tail-ready',1),
            ('--tail-warm-checkpoint',1),('--release-tail-worker-between-responses',0)):
        delete(flag,count)
    position=cmd.index('--target-core');cmd[position+1:position+4]=[repr(v) for v in core[:3]]
    for flag,value in (('--out-prefix',args.prefix),('--prefix-cache-directory',str(args.work/(Path(args.prefix).name+'-prefix-cache'))),('--max-nodes','6000')):
        cmd[cmd.index(flag)+1]=value
    cmd+=['--response-data',str(args.response)]
    for name,value in steps.items():
        if not name.startswith('actual_') and value!=0.:cmd+=['--neutral-control-step',name+'='+repr(value)]
    if args.stage=='warm':cmd+=['--inspect-warm-output',args.prefix+'-warm.json']
    target=cmd[2]
    cmd=cmd[:2]+['computations/root_20261114_threaded_entry.py','--radial-workers','4',
        '--parallel-run-record',str(Path(template['cwd'])/(args.prefix+'-parallel.json')),'--target-entry',target]+cmd[3:]
    record=dict(scope=__doc__,cwd=template['cwd'],command=cmd,stage=args.stage,
        selected_compact_candidate=index,shortening_factor=args.factor,physical_steps=steps,
        target_core=core[:3],predicted_complete_core=core,
        original_nonlinear_acceptance_gates_preserved=True,
        exact_old_H_audited_reuse_removed=True,
        original_complete_tail_flow_predictor_retained=True,
        inputs=[dict(file=str(path),sha256=hashlib.sha256(path.read_bytes()).hexdigest())
            for path in (args.template_plan,args.screen,args.response)],
        source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        executed=False,new_nonlinear_solution=False)
    args.out.write_text(json.dumps(record,indent=2)+'\n')
    print(json.dumps(dict(plan=str(args.out),stage=args.stage,candidate=index,target_core=core[:3])),flush=True)


if __name__=='__main__':main()
