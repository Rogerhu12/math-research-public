#!/usr/bin/env python3
"""Actual intrinsic-flow/JVP check and fixed-coordinate parameter layout.

Uses the previously saved, genuinely integrated v2 M63 state.  It compares
the smaller equations with that original implementation, computes one new
local stage and its analytic tangent, and measures the central parameter
projection conditioning in the balanced-oval coordinate.  No full BVP,
tail solve, complete new profile, or closed surface is claimed.
"""
from __future__ import annotations
import os
for _variable in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[_variable] = '1'
import argparse
import importlib.util
import json
from pathlib import Path
import sys
import time
import numpy as np
from scipy.linalg import svdvals
from fd2d_gc_intrinsic import IntrinsicGC, FixedNormalReference, identity

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent


def load_module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--out', type=Path, required=True)
    p.add_argument('--state-out', type=Path, required=True)
    p.add_argument('--candidate', type=Path, default=ROOT/'notes/2026-11-12-fd2d-ellipse-b05-frozen-candidate-v2.json')
    p.add_argument('--state', type=Path, default=ROOT/'notes/2026-11-12-fd2d-ellipse-v2-codazzi-hybrid-m63-state.npz')
    p.add_argument('--stage-length', type=float, default=.0003)
    args = p.parse_args()
    if args.out.exists() or args.state_out.exists():
        raise FileExistsError('Use unused report and state filenames')
    started = time.monotonic()
    legacy = load_module('fd2d_intrinsic_check_legacy', HERE/'fd2d-gc-ellipse-hybrid-flow.py')
    candidate = legacy.base.frozen.Candidate(json.loads(args.candidate.read_text()))
    source = np.load(args.state)
    modes, s = int(source['modes']), float(source['s'])
    old_state = source['state']
    shape_dimension = 2*(modes//2)+1
    work = (len(old_state)-shape_dimension)//12
    oversample = work//(2*(modes+1))
    if work*12+shape_dimension != len(old_state) or work != 2*oversample*(modes+1):
        raise ValueError('Saved hybrid layout is not an integral oversampling of the recorded modes')
    old = legacy.Hybrid(candidate, modes, oversample, 100000)
    old_nm = old.decode(old_state)[:, :2]
    flow = IntrinsicGC(candidate, modes, oversample)
    state = flow.encode(old_nm)
    old_rhs_nm = old.decode(old.rhs(s, old_state))[:, :2]
    rhs = flow.rhs(s, state)
    expected = flow.encode(old_rhs_nm)
    direction = np.cos(np.arange(flow.dimension)*1.723)/(1+np.arange(flow.dimension))
    direction /= np.linalg.norm(direction)
    actual_jvp = flow.jvp(s, state, direction)
    directional = []
    for epsilon in (1e-3, 1e-4, 1e-5, 1e-6):
        finite = (flow.rhs(s, state+epsilon*direction)-flow.rhs(s, state-epsilon*direction))/(2*epsilon)
        directional.append(dict(epsilon=epsilon, absolute_maximum_difference=float(abs(finite-actual_jvp).max()),
                                relative_l2_difference=float(np.linalg.norm(finite-actual_jvp)/np.linalg.norm(actual_jvp))))
    stage = flow.integrate_stage(s, s+args.stage_length, state, tangent=direction, max_step=.0001)
    epsilon = 1e-5
    plus = flow.integrate_stage(s, s+args.stage_length, state+epsilon*direction, max_step=.0001)
    minus = flow.integrate_stage(s, s+args.stage_length, state-epsilon*direction, max_step=.0001)
    finite_stage = (plus.state-minus.state)/(2*epsilon)
    tangent_difference = finite_stage-stage.tangent[:, 0]
    central_module = load_module('fd2d_intrinsic_check_balanced', HERE/'fd2d_balanced_oval_core.py')
    core = central_module.BalancedOvalCore()
    reference = FixedNormalReference(core)
    balanced = IntrinsicGC(candidate, 191, 2, reference=reference)
    central_state, central_projection = balanced.central_state(core)
    material = balanced.central_material_directions()
    angular, weighted_means = balanced.central_reference_directions()
    layout = []
    for name, matrix in [('material_u_cosines_projected_to_fixed_phi', material),
                         ('fixed_phi_cosines_minus_material_mean', angular)]:
        values = svdvals(matrix[:balanced.K+1])
        layout.append(dict(basis=name, parameters=matrix.shape[1], largest_singular_value=float(values[0]),
                           smallest_singular_value=float(values[-1]), condition=float(values[0]/values[-1]),
                           rank_at_relative_1e_minus12=int(np.sum(values>values[0]*1e-12)),
                           rank_at_relative_1e_minus8=int(np.sum(values>values[0]*1e-8))))
    material_mean_defect = np.mean(balanced.u_theta[:, None]*balanced.decode(angular)[:, 0], axis=0)
    monodromy = balanced.angular_monodromy(0., central_state)
    np.savez_compressed(args.state_out, s=stage.right, initial_s=s, state=stage.state,
                        tangent=stage.tangent, initial_state=state, initial_direction=direction,
                        modes=modes, balanced_modes=191, balanced_central_state=central_state,
                        reference_basis_means=weighted_means)
    report = dict(schema='fd2d-intrinsic-gc-local-comparison-v1', scope=__doc__,
        source=identity(__file__), provider=identity(HERE/'fd2d_gc_intrinsic.py'),
        original_flow=identity(HERE/'fd2d-gc-ellipse-flow.py'),
        original_adapter=identity(HERE/'fd2d-gc-ellipse-hybrid-flow.py'),
        central_provider=identity(HERE/'fd2d_balanced_oval_core.py'),
        common_coordinate_provider=identity(HERE/'fd2d_metric_curvature_core.py'),
        input_candidate=identity(args.candidate), input_state=identity(args.state),
        intrinsic_dimension=flow.dimension, original_hybrid_dimension=int(len(old_state)),
        original_state_conversion_error=float(abs(flow.decode(state)-old_nm).max()),
        original_projected_rhs_maximum_difference=float(abs(rhs-expected).max()),
        rhs_directional_checks=directional,
        local_stage=dict(left=stage.left, right=stage.right, rhs_calls=stage.rhs_calls, seconds=stage.seconds,
                         segments=stage.segments, finite_difference_epsilon=epsilon,
                         tangent_maximum_difference=float(abs(tangent_difference).max()),
                         tangent_relative_l2_difference=float(np.linalg.norm(tangent_difference)/np.linalg.norm(stage.tangent))),
        central_layout=layout, central_projection=central_projection,
        fixed_reference_basis_material_mean_defect=float(abs(material_mean_defect).max()),
        central_angular_monodromy=monodromy, output_state=identity(args.state_out),
        seconds=time.monotonic()-started, full_BVP_solved=False, new_tail_DN_solved=False,
        whole_profile_integrated=False, closed_surface=False)
    args.out.write_text(json.dumps(report, indent=2, allow_nan=False)+'\n')
    print(json.dumps({k:report[k] for k in ('intrinsic_dimension', 'original_hybrid_dimension',
          'original_projected_rhs_maximum_difference', 'rhs_directional_checks', 'local_stage',
          'central_layout', 'central_projection', 'fixed_reference_basis_material_mean_defect',
          'central_angular_monodromy', 'seconds')}, allow_nan=False), flush=True)


if __name__ == '__main__':
    main()
