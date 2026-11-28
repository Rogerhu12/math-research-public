#!/usr/bin/env python3
"""Portable complete design steps, each followed by independent diagnostics."""
from __future__ import annotations
import argparse,json,subprocess
from pathlib import Path

def main():
    ap=argparse.ArgumentParser()
    for k in ('scripts','work','prepared','state','observer','normal-audit'):
        ap.add_argument('--'+k,type=Path,required=True)
    ap.add_argument('--first',type=int,required=True);ap.add_argument('--stop',type=int,required=True)
    ap.add_argument('--tag',required=True);ap.add_argument('--boundary-pause-file',type=Path)
    args=ap.parse_args();w=args.work;state=args.state
    base=['--scripts',str(args.scripts),'--prepare-entry',str(w/'2ecf-polar-c2-g10-split-prepare.py'),
        '--prepared',str(args.prepared)]
    def run(prefix,command):
        command=['python3',str(w/'2ecf-polar-natural-process-receipt.py'),'--prefix',str(prefix),'--']+command
        print(json.dumps(dict(event='actual_design_child_start',command=command)),flush=True)
        subprocess.run(command,check=True)
    for number in range(args.first,args.stop):
        if args.boundary_pause_file and args.boundary_pause_file.exists():
            print(json.dumps(dict(event='requested_complete_step_boundary_pause',nextStep=number,state=str(state))),flush=True)
            return
        prefix=w/(args.tag+f'-step{number:02d}')
        run(prefix,['python3','-u',str(w/'2ecf-polar-log-radius-fast-normal-design-solve.py')]+base+
            ['--normal-audit',str(args.normal_audit),'--state',str(state),'--prefix',str(prefix),'--steps','1'])
        state=Path(str(prefix)+'-step01-state.json')
        row=json.loads(state.read_text())
        observation=Path(str(prefix)+'-G11')
        run(observation,['python3','-u',str(w/'2ecf-polar-c2-independent-g11-resume-observe.py'),'observe']+base+
            ['--state',str(state),'--observer',str(args.observer),'--output',str(observation)+'.json'])
        target=Path(str(prefix)+'-target-audit')
        run(target,['python3','-u',str(w/'2ecf-polar-log-radius-target-audit.py')]+base+
            ['--state',str(state),'--observer',str(args.observer),'--output',str(target)+'.json'])
        print(json.dumps(dict(event='actual_design_step_and_independent_checks_complete',number=number,
            ownAcceptedSteps=row['ownMetricDesignAcceptedSteps'],state=str(state))),flush=True)
        if not row['accepted']:raise RuntimeError('Actual rejected design step requires assessment')

if __name__=='__main__':main()
