#!/usr/bin/env python3
"""Explicit hypothetical constraints on an existing complete Schur model.

No live class, tail domain, source identity, actual field or finite goal is
modified. These small QPs do not evaluate F/J or create accepted states.
"""
import os
for name in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[name] = '1'
import argparse
import json
import time
from fractions import Fraction
from pathlib import Path
import numpy as np
from scipy.optimize import Bounds, LinearConstraint, minimize
from fd2d_gc_dyadic_grouped_search_context import NumericalContext, array_identity
from fd2d_gc_dyadic_stage_io import selected_normal, load_selected_normal, parent_factor_binding
from fd2d_gc_packet_checkpoint import load_actual_packet
from fd2d_gc_dyadic_saved_schur_search import normal_direction_quadratic
from fd2d_gc_archive_arrays import identity


def one_case(ctx, normal, packet, *, label, tail_upper, preserve_gap):
    problem = ctx.problem
    mapping = normal.mapping
    _, p = problem.unpack(ctx.vector)
    ps = np.asarray(packet['parameter_scale'])
    fs = np.asarray(packet['field_scale'])
    schur = np.asarray(packet['schur'])
    gradient = np.asarray(packet['gradient'])
    ts, ds = problem.tail_parameter_slice, problem.profile_parameter_slice
    lower = np.full(problem.parameter_count, -np.inf)
    upper = np.full(problem.parameter_count, np.inf)
    lower[ds], upper[ds] = -ctx.args.profile_box-p[ds], ctx.args.profile_box-p[ds]
    curvature = problem.seed + problem.core_basis @ p[:problem.K]
    cm = np.zeros((problem.work, problem.parameter_count))
    cm[:, :problem.K] = problem.core_basis * ps[None, :problem.K]
    constraints = [LinearConstraint(cm, ctx.args.central_floor-curvature,
                                  ctx.args.central_cap-curvature)]
    coefficients = problem.tail_control_box.coefficients_exact(p[ts])
    tm = np.zeros((128, problem.parameter_count))
    tm[:, ts] = problem.tail_control_box.matrix * ps[None, ts]
    tl = np.array([float(-v) for v in coefficients])
    tu = (np.full(128, np.inf) if tail_upper is None else
          np.array([float(tail_upper-v) for v in coefficients]))
    constraints.append(LinearConstraint(tm, tl, tu))
    dom = problem.profile_domain
    if dom is not None:
        pm = np.zeros((len(dom['lower']), problem.parameter_count))
        pm[:, ds] = dom['matrix'] * ps[None, ds]
        constraints.append(LinearConstraint(pm, dom['lower']-dom['matrix']@p[ds], np.inf))
    _, axes = problem.core(p[:problem.K])
    row = np.zeros((1, problem.parameter_count))
    row[0, :problem.K] = np.asarray(axes['gap_jacobian']) * ps[:problem.K]
    gap_target = problem.gap-float(axes['gap'])
    if preserve_gap:
        constraints.append(LinearConstraint(row, gap_target, gap_target))
    started = time.monotonic()
    answer = minimize(lambda z: .5*z@schur@z+gradient@z,
                      np.zeros(problem.parameter_count),
                      jac=lambda z: schur@z+gradient, method='SLSQP',
                      bounds=Bounds(lower/ps, upper/ps), constraints=constraints,
                      options=dict(ftol=1e-10, maxiter=1000))
    zp = answer.x
    solved = packet['solved']
    zf = -solved[:, 0]-solved[:, 1:]@zp
    direction = mapping.expand(fs*zf, ps*zp)
    info = normal_direction_quadratic(normal, direction)
    proposed = p+ps*zp
    local = problem.tail_control_box.coefficients_exact(proposed[ts])
    exact_ok = all(v >= 0 and (tail_upper is None or v <= tail_upper) for v in local)
    info.update(label=label, hypothetical_tail_upper=None if tail_upper is None else str(tail_upper),
                linear_gap_equality_preserved=preserve_gap,
                gap_residual_row_in_original_objective_preserved=True,
                optimizer_success=bool(answer.success), optimizer_status=int(answer.status),
                optimizer_message=str(answer.message), iterations=int(answer.nit),
                seconds=time.monotonic()-started, source=identity(__file__),
                unchanged_central_floor=float(ctx.args.central_floor),
                unchanged_central_cap=float(ctx.args.central_cap),
                proposed_central_min=float(np.min(curvature+cm@zp)),
                proposed_central_max=float(np.max(curvature+cm@zp)),
                proposed_linear_gap=float(axes['gap']+(row@zp)[0]),
                proposed_tail_local_min_exact=str(min(local)),
                proposed_tail_local_max_exact=str(max(local)),
                proposed_tail_exact_hypothetical_membership=exact_ok,
                local_lower_active_rows=sum(abs(float(v)) <= 1e-8 for v in local),
                local_upper_active_rows=(None if tail_upper is None else
                                        sum(abs(float(v-tail_upper)) <= 1e-8 for v in local)),
                activity_tolerance_is_not_domain_acceptance=True,
                proposed_parameters=proposed.tolist(),
                actual_projection_or_F_J_or_line_search_executed=False,
                usable_geometric_direction_claimed=False,
                field_and_normal_and_live_domain_modified=False)
    return info


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--request', type=Path, required=True)
    ap.add_argument('--out-prefix', type=Path, required=True)
    ap.add_argument('--factor-id', required=True)
    args = ap.parse_args()
    out = Path(str(args.out_prefix)+'-comparison.json')
    if out.exists(): raise FileExistsError(out)
    ctx = NumericalContext(args.request, args.out_prefix, install_caches=False)
    normal_manifest, normal_binding, normal_origin = selected_normal(ctx)
    saved_path = Path(ctx.request['cache_dir'])/'reduced-factors'/args.factor_id/'summary.json'
    saved = json.loads(saved_path.read_text())
    here = Path(__file__).resolve().parent
    expected = parent_factor_binding(ctx, normal_manifest, saved['damping'],
                                     here/Path(saved['solver_source']['path']).name,
                                     here/Path(saved['producer_source']['path']).name)
    if saved['binding'] != expected: raise ValueError('Wrong actual field/normal/Schur binding')
    manifest = saved['packet_manifest']
    actual = identity(manifest['path'])
    if (actual['sha256'], actual['bytes']) != (manifest['sha256'], manifest['bytes']):
        raise ValueError('Changed Schur packet')
    packet = load_actual_packet(manifest['path'], expected_binding=expected)
    normal = load_selected_normal(ctx.problem, normal_manifest, expected_binding=normal_binding)
    report = dict(schema='fd2d-hypothetical-same-Schur-tail-gap-comparison-v1',
                  request=identity(args.request), base_vector=array_identity(ctx.vector),
                  source=identity(__file__), normal_manifest=identity(normal_manifest),
                  saved_Schur=identity(saved_path), normal_origin=normal_origin,
                  actual_F_J_or_accepted_state_created=False, cases=[])
    for label, bound, gap in [('tail_upper_3over2', Fraction(3,2), True),
                              ('tail_no_upper', None, True),
                              ('no_linear_gap_equality', Fraction(6,5), False)]:
        item = one_case(ctx, normal, packet, label=label, tail_upper=bound, preserve_gap=gap)
        report['cases'].append(item)
        out.write_text(json.dumps(report, ensure_ascii=False, indent=2)+'\n')
        print(json.dumps({k: item[k] for k in ('label','linear_residual_norm',
              'proposed_linear_gap','optimizer_success','iterations','seconds')}), flush=True)
    report['complete'] = True
    out.write_text(json.dumps(report, ensure_ascii=False, indent=2)+'\n')


if __name__ == '__main__': main()
