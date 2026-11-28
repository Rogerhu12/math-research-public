#!/usr/bin/env python3
"""Real complete fixed-g steps, each followed by independent G11.

The original-g and frozen-designed-g epochs have separate entries, states,
targets, and counters. A boundary request is honored only between complete
scientific steps and their returned independent observations.
"""
from __future__ import annotations
import argparse
import json
from pathlib import Path
import subprocess


def main():
    ap=argparse.ArgumentParser()
    for key in ('scripts','work','prepared','state','observer','normal-audit'):
        ap.add_argument('--'+key,type=Path,required=True)
    ap.add_argument('--mode',choices=('original','frozen-designed'),required=True)
    ap.add_argument('--frozen-target',type=Path)
    ap.add_argument('--first',type=int,required=True)
    ap.add_argument('--stop',type=int,required=True)
    ap.add_argument('--tag',required=True)
    ap.add_argument('--initial-damping',type=float,default=1e-4)
    ap.add_argument('--boundary-pause-file',type=Path)
    args=ap.parse_args();w=args.work;state=args.state
    if args.mode=='frozen-designed' and args.frozen_target is None:
        raise ValueError('An explicit immutable designed target is required')
    if args.mode=='original' and args.frozen_target is not None:
        raise ValueError('The original-g epoch cannot consume a designed target')
    base=['--scripts',str(args.scripts),'--prepare-entry',str(w/'2ecf-polar-c2-g10-split-prepare.py'),
        '--prepared',str(args.prepared)]
    if args.mode=='original':
        solve=w/'2ecf-polar-c2-g10-fast-solve.py'
        observe=[str(w/'2ecf-polar-c2-independent-g11-resume-observe.py'),'observe']
        target=[];counter='ownExtendedAcceptedSteps'
    else:
        solve=w/'2ecf-polar-frozen-designed-g-solve.py'
        observe=[str(w/'2ecf-polar-frozen-designed-g-observe.py')]
        target=['--frozen-target',str(args.frozen_target)];counter='ownFrozenMetricAcceptedSteps'
    def run(prefix,command):
        cmd=['python3',str(w/'2ecf-polar-natural-process-receipt.py'),'--prefix',str(prefix),'--']+command
        print(json.dumps(dict(event='actual_fixed_metric_child_start',mode=args.mode,command=cmd)),flush=True)
        subprocess.run(cmd,check=True)
    for number in range(args.first,args.stop):
        if args.boundary_pause_file and args.boundary_pause_file.exists():
            print(json.dumps(dict(event='requested_complete_step_boundary_pause',nextStep=number,state=str(state))),flush=True)
            return
        prefix=w/(args.tag+f'-step{number:02d}')
        run(prefix,['python3','-u',str(solve)]+base+target+
            ['--normal-audit',str(args.normal_audit),'--state',str(state),'--prefix',str(prefix),
             '--steps','1','--initial-damping',str(args.initial_damping)])
        state=Path(str(prefix)+'-step01-state.json');row=json.loads(state.read_text())
        observation=Path(str(prefix)+'-G11')
        run(observation,['python3','-u']+observe+base+target+
            ['--state',str(state),'--observer',str(args.observer),'--output',str(observation)+'.json'])
        print(json.dumps(dict(event='actual_fixed_metric_step_and_independent_observation_complete',
            mode=args.mode,number=number,ownAcceptedSteps=row[counter],state=str(state))),flush=True)
        if not row['accepted']:
            raise RuntimeError('A returned rejected scientific step requires explicit assessment')


if __name__=='__main__':main()
