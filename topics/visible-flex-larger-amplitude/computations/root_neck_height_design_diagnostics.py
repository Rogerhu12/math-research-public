#!/usr/bin/env python3
"""Locate the height cost in an accepted candidate's actual background program.

This only instantiates the existing finite neck and terminal profile formulas.
It does not call their linear ODE screen, solve a BVP, differentiate a true
solution, or assert the perturbed background matches the prescribed core.
The controls are varied with all other physical profile entries fixed.
"""
from __future__ import annotations
import argparse
import gzip
import hashlib
import importlib.util
import json
import os
from pathlib import Path

for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[key]='1'


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--checkpoint',type=Path,required=True)
    ap.add_argument('--port',type=Path,required=True)
    ap.add_argument('--out',type=Path,required=True)
    args=ap.parse_args()
    if args.out.exists():raise FileExistsError('Use a fresh output')
    actual=json.loads(gzip.decompress(args.checkpoint.read_bytes()))
    if not actual['solver_success'] or actual.get('audit_pending',True):
        raise ValueError('Use a completed accepted physical baseline')
    path=Path(__file__).with_name('alternative-neck-provider.py')
    spec=importlib.util.spec_from_file_location('geometry_background_only',path)
    module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
    port=json.loads(args.port.read_text())
    cfg=actual['frozen_profile']

    def measure(profile):
        prefix=module.NeckPrefix(profile)
        bridge=module.NeckTerminalBridge(module.tagged_port(port,profile)['cut'])
        total=prefix.height+bridge.height
        return dict(background_height=total,background_length=prefix.end+bridge.end,
            background_height_is_not_true_prefix_height=True,
            segments=[dict(part=part,index=index,kind=segment['kind'],length=segment['length'],
                radius_change=segment['dr'],height_change=segment['dh'],height_fraction=segment['dh']/total,
                radius_start=segment['a0'],radius_end=segment['a1'])
                for part,program in [('prefix',prefix),('bridge',bridge)]
                for index,segment in enumerate(program.segments)])
    baseline=measure(cfg)
    directions=[('vu',.0002),('descending_turn_curvature',.0025),
                ('start_acceleration',.01),('vd',.001),('loop_curvature',.1),
                ('loop_ratio',.01),('loop_radius',.005),('loop_speed',.001)]
    trials=[]
    for key,step in directions:
        plus=measure({**cfg,key:cfg[key]+step})
        minus=measure({**cfg,key:cfg[key]-step})
        trials.append(dict(control=key,step=step,
            plus_height=plus['background_height'],minus_height=minus['background_height'],
            central_background_height_difference_per_step=(plus['background_height']-minus['background_height'])/2,
            central_background_height_derivative=(plus['background_height']-minus['background_height'])/(2*step),
            observed_second_difference=plus['background_height']+minus['background_height']-2*baseline['background_height'],
            low_core_constraints_held=False,true_solution_response_computed=False))
    result=dict(scope=__doc__,source_sha256=sha(__file__),checkpoint=str(args.checkpoint),
        checkpoint_sha256=sha(args.checkpoint),port=str(args.port),port_sha256=sha(args.port),
        original_provider_sha256=sha(path),
        provider_dependency_sha256={name:sha(Path(__file__).with_name(name)) for name in
            ('alternative-neck-flatturn.py','alternative-neck-program-search.py',
             'strong_angle_boost.py') if Path(__file__).with_name(name).exists()},
        actual_primary=actual['actual_primary_amplitude'],profile=cfg,
        accepted_prefix_height_sample=actual['summary']['height_max'],baseline=baseline,
        directions=trials,new_bvp_or_ode_or_tail_started=False,
        background_quadrature_is_floating_point=True,continuous_geometry_certified=False)
    args.out.parent.mkdir(parents=True,exist_ok=True)
    args.out.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(dict(out=str(args.out),sha256=sha(args.out),height=baseline['background_height'],
                         directions=trials)),flush=True)


if __name__=='__main__':
    main()
