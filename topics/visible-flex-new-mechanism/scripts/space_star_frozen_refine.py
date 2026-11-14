#!/usr/bin/env python3
"""Refine continuous bounds for fixed, already screened two-mode flat cores.

The candidate parameters and material width do not change with subdivision.
This proves only local-core geometric bounds, never a completed closed surface.
"""
import argparse
from fractions import Fraction as R
import hashlib
import json
import os
from pathlib import Path
import time
from types import SimpleNamespace

from space_star_lift_design import continuous_certificate, load_planar


def exact_mix(a, b, specification):
    if specification == 'valley-zero':
        radius = 1-a+b
        third = 28*a-109*b-1
        return (9*radius+third)/(72*radius+2*third)
    if specification == 'tip-zero':
        radius = 1+a+b
        third = -1-28*a-109*b
        return -(9*radius+third)/(72*radius+2*third)
    return R(specification)


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--a', default='.65')
    p.add_argument('--b', default='.12')
    p.add_argument('--height', default='.30')
    p.add_argument('--mixes', default='.187,.20,valley-zero')
    p.add_argument('--widths', default='.005,.01')
    p.add_argument('--nodes', type=int, default=32768)
    p.add_argument('--planar-report', type=Path, required=True)
    p.add_argument('--out', type=Path, required=True)
    args = p.parse_args()
    if os.environ.get('GITHUB_ACTIONS') != 'true' or os.environ.get('GITHUB_REPOSITORY') != 'Rogerhu12/math-research-public':
        p.error('run continuous research certification in this public repository Actions')
    if args.nodes < 4096 or R(args.height) <= 0:
        p.error('need at least 4096 cells and a positive height')
    a, b, h = map(R, [args.a, args.b, args.height])
    geometry = SimpleNamespace(a=a, b=b)
    planar = load_planar(args.planar_report, args.a, args.b)
    result = dict(schema='space-star-frozen-two-mode-refinement-v1',
                  definition={k: str(v) if isinstance(v, Path) else v for k, v in vars(args).items()},
                  planar_source_sha256=hashlib.sha256(args.planar_report.read_bytes()).hexdigest(),
                  fixed_physical_candidates=True, optimization_performed=False,
                  method='per-cell lambda0/(1-w*abs(q_ell)); exact rational coefficients',
                  original_screen_run='43591099281', refinements=[], task_complete=False,
                  source_sha256={name: hashlib.sha256(Path(__file__).with_name(name).read_bytes()).hexdigest()
                     for name in ['space_star_frozen_refine.py', 'space_star_lift_design.py',
                                  'space_star_flat_core.py', 'star_core_geometry.py', 'folded_reference_geometry.py']})
    started = time.monotonic()
    for specification in args.mixes.split(','):
        mixture = exact_mix(a, b, specification)
        heights = [h, h*mixture]
        coefficients = [dict(numerator=str(x.numerator), denominator=str(x.denominator)) for x in heights]
        for width in args.widths.split(','):
            if R(width) <= 0:
                p.error('width must be positive')
            certificate = continuous_certificate(geometry, heights, width, planar, args.nodes)
            row = dict(mix_specification=specification,
                       exact_mix=dict(numerator=str(mixture.numerator), denominator=str(mixture.denominator)),
                       height_coefficients_exact_rational=coefficients, width=width,
                       continuous_certificate=certificate, elapsed_seconds=time.monotonic()-started)
            result['refinements'].append(row)
            result['elapsed_seconds'] = time.monotonic()-started
            args.out.parent.mkdir(parents=True, exist_ok=True)
            args.out.write_text(json.dumps(result, indent=2, allow_nan=False)+'\n')
            print(json.dumps(dict(mix=specification, width=width,
                immersion=certificate['whole_core_immersion_and_angular_closure_certified'],
                curvature_upper=certificate['whole_width_principal_curvature_upper'],
                curvature_budget=certificate['local_curvature_ceiling_sufficient_for_003_Dcore_budget'],
                witness_ratio=certificate['conditional_witness_over_core_D_lower'],
                seconds=result['elapsed_seconds'])), flush=True)


if __name__ == '__main__':
    main()
