#!/usr/bin/env python3
"""Replay the stated cost-based stopping rule for the weak mean-LP input.

This only automates stopping a saved best iterate of the frozen optimizer;
it does not certify equality to a historical raw checkpoint. An optional
comparison is performed after generation and never supplies the initial
coefficients. Raw output and all inputs belong outside the repository.
"""
import argparse
import hashlib
import importlib.util
import json
from pathlib import Path
import numpy as np

SOURCE=Path(__file__).with_name('2026-11-17-parallel-model-direct-height-refined-grid.py')
EXPECTED='6fb6f84a8d05c8624df831f398f35a4958f29faa478d01375b970e47b90f816c'


class CheckpointReached(Exception):
    pass


def main(args):
    if hashlib.sha256(SOURCE.read_bytes()).hexdigest()!=EXPECTED:
        raise ValueError('Frozen refined-grid source differs')
    spec=importlib.util.spec_from_file_location('refined_checkpoint_source',SOURCE)
    module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
    original=module.RefinedGrid.save_design
    def save_at_cost(self,coefficients,cost,finished,optimizer=None):
        original(self,coefficients,cost,finished,optimizer)
        if cost<=args.stop_cost:
            report=json.loads(self.args.out.read_bytes())
            values=np.asarray(coefficients,dtype='<f8')
            replay=dict(stop_cost=args.stop_cost,reached_cost=float(cost),
                source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                input_sha256=hashlib.sha256(args.input.read_bytes()).hexdigest(),
                coefficient_binary_sha256=hashlib.sha256(values.tobytes()).hexdigest())
            if args.compare:
                old=np.asarray(json.loads(args.compare.read_bytes())['coefficients'])
                replay['comparison']=dict(equal=bool(np.array_equal(old,values)),
                    max_difference=float(np.max(abs(old-values))))
            report['checkpoint_replay']=replay
            self.args.out.write_text(json.dumps(report,indent=2)+'\n')
            print(json.dumps(dict(event='requested_best_checkpoint_saved',**replay)),flush=True)
            raise CheckpointReached
    module.RefinedGrid.save_design=save_at_cost
    stage=argparse.Namespace(input=args.input,out=args.out,iterations=400,
        critical_radii='[1.6883406815921667]',neighbors=8,
        curvature_limit=6.6,curvature_weight=.1,end_weight=3.,
        coupled_metric_height=False,mean_curvature_initialization=False,
        mean_curvature_radius=1.6,mean_speed_change=.005,
        cap_lift=.25,gauss=None,angles=None,cut_fraction=None)
    try:
        module.main(stage)
    except CheckpointReached:
        return
    raise RuntimeError('The declared finite budget did not reach the stated checkpoint cost')


if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--input',type=Path,required=True);p.add_argument('--out',type=Path,required=True)
    p.add_argument('--stop-cost',type=float,default=3.6060085164748892e-9)
    p.add_argument('--compare',type=Path)
    main(p.parse_args())
