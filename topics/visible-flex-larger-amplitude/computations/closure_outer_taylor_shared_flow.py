#!/usr/bin/env python3
"""Actual two-cell outer background flow in one fixed physical momentum gauge.

The cap/weight/chi identity is proved from the frozen source parameters.
The validated R65 Taylor recurrence is reused, with mu_star=mu11 in the
LINEAR COORDINATES only. The source w still uses each original mu_n.
No interface rho is applied in this global gauge. A shared dyadic B0 centre,
its true slope remainder, and both independent background basis columns
are retained. This is not a nonlinear outer boundary-value solution.

Author: exact_closure (GPT-6 Astra Pro, AI-assisted), 2026-11-12.
"""
import argparse
from fractions import Fraction
import json
from pathlib import Path
import resource
import time

from flint import arb, arb_series, ctx

from closure_real_head_source_enclosure import RealHead, exact_q, power2
from closure_projective_interval_column import ProjectiveColumn
from closure_real_linear_head_enclosure import peano_matrix, positive_scale_bounds
from closure_split_joint_io_v2 import digest, read_field, iter_array
from closure_taylor_cut_slope_v2 import (AnchoredHead, source_series, matrix_coefficients,
    rough_radius, monotone_parts, record, point_record, endpoint, ball, intersect,
    add_error, column_record, restore_column, save, EXPECTED_PROJECTIVE, EXPECTED_PB)


EXPECTED_TAYLOR = '8e150b6fe16c33da98043bc7ebe952abf123e2f7c8da8ebbfb10bfec700fb5ea'
EXPECTED_SOURCE = '97ff78a171b284cd8d5acc8dc233bcfe1f0b7c428ce2fbbd5b7104bd0ecb8c47'


def positive_chart(d):
    lo, hi = endpoint(d['lower']), endpoint(d['upper'])
    return lo > 0 or hi < 0


def generator_global(h, segment, xbase, span, rbase, order, sign, mode, mu_star):
    w, g = source_series(h, segment, xbase, span, order, sign)
    r = arb_series([rbase]+[g[k-1]/k for k in range(1, order+2)], prec=order+2)
    u, nu = mode*mode-4, arb(mode*mode*(mode*mode-1))/12
    a = h.sqrt12*mu_star*h.rc**(2*u)*g/(r**(8+2*u)*w)
    b = nu*h.sqrt12/(mu_star*h.rc**(2*u))*r**(6+2*u)*w*g
    return a, b, g


def taylor_global(h, segment, left, right, radius, modes, order, tol, mu_star):
    sign = segment['_monotone_sign']
    x0, span = exact_q(left), exact_q(right-left)
    xall = x0.union(exact_q(right))
    rr, _ = rough_radius(h, segment, left, right, radius)
    flows, worst = [], arb(0)
    for mode in modes:
        aa, bb, gc = generator_global(h, segment, x0, span, radius, order, sign, mode, mu_star)
        ai, bi, gi = generator_global(h, segment, xall, span, rr, order, sign, mode, mu_star)
        au, bu = abs(ai[0]).upper(), abs(bi[0]).upper()
        product = (au*bu).upper()
        if not product < arb(1)/4:
            raise ArithmeticError('Subdivide the positive local-flow majorant')
        denominator = 1-product
        major = [[1/denominator, au/denominator], [bu/denominator, 1/denominator]]
        identity = [[arb(1), arb(0)], [arb(0), arb(1)]]
        coeff = matrix_coefficients(aa, bb, order, identity)
        derivatives = matrix_coefficients(ai, bi, order+1, major, absolute=True)
        rem = derivatives[order+1]
        balance = (bu/au).sqrt()
        error = max(rem[0][0].upper(), rem[1][1].upper(),
            (rem[0][1]*balance).upper(), (rem[1][0]/balance).upper())
        if not error < tol:
            raise ArithmeticError('Subdivide the actual Taylor remainder')
        flows.append([[add_error(sum((c[i][j] for c in coeff), arb(0)), rem[i][j])
                       for j in range(2)] for i in range(2)])
        worst = max(worst, error)
    dr = sum((gc[k]/(k+1) for k in range(order)), arb(0))
    dr = add_error(dr, abs(gi[order]).upper()/(order+1))
    if not dr > 0:
        raise ArithmeticError('Subdivide a positive real-radius increment')
    return flows, intersect(radius+dr, rr), worst


def root_global(h, segment, left, right, radius, modes, mu_star):
    rr, dr = rough_radius(h, segment, left, right, radius)
    w = h.source_point(segment, exact_q(left).union(exact_q(right)))['w']
    flows, maximum = [], arb(0)
    for mode in modes:
        u, nu = mode*mode-4, arb(mode*mode*(mode*mode-1))/12
        a = abs(h.sqrt12*mu_star*h.rc**(2*u)*dr/(rr**(8+2*u)*w)).upper()
        b = abs(nu*h.sqrt12/(mu_star*h.rc**(2*u))*rr**(6+2*u)*w*dr).upper()
        flow, _, product = peano_matrix(arb(0).union(a), arb(0).union(b))
        flows.append(flow)
        maximum = max(maximum, product.upper())
    return flows, intersect(radius+arb(0).union(dr), rr), maximum


def raw_source_identity(ready, n):
    p = ready['rationalDeepModel']['physicalParameters']
    rows = {x['n']:x for x in ready['shallowSourceParameters']['cells']}
    row = rows[n]
    if (n not in (10, 11) or row['lengthScale'] != 1 or p['orientation'] != 1
            or p['capMode'] != 'cut-preserving' or p['protectCell'] != 160
            or p['capTransition'] != 2 or p['curvatureBound'] != 8
            or p.get('flatOuterThroughCell') is not None or p.get('rejoinR20At') is not None):
        raise ValueError('Unsupported exact outer source convention')
    if n < len(p.get('valleyControls', [])) and p['valleyControls'][n] != 0:
        raise ValueError('A nonzero valley correction cannot use the raw formula')
    for key in ('pulseCaps', 'valleyCaps', 'warpWeightLevels'):
        values = p.get(key, [])
        if n < len(values) and values[n] is not None:
            raise ValueError('A custom outer cap/warp value needs its full analytic expression')
    constants = ready['rationalDeepModel']['exactSourceConstants']
    delta = exact_q(Fraction(constants['delta0']))*power2(-n)
    mu = exact_q(p['epsilonScale'])*(arb(11)/4*delta.log()).exp()
    rc = exact_q(p['rCuff'])
    R, alpha = exact_q(row['R']), exact_q(row['alpha'])
    rho = (arb(11)/4*arb(2).log()).exp()
    levels = [arb(1), R/delta, delta/alpha, 1/delta, rho]
    max_level = max(x.upper() for x in levels)
    upper_w = (mu*max_level/rc**7).upper()
    raw_threshold = exact_q(p['slopeCap'])*(-exact_q(p['capTransition'])).exp()
    if not upper_w < raw_threshold:
        raise ArithmeticError('The entire raw source has not been proved below the cap threshold')
    return dict(cell=n, background_mu=record(mu), R=record(R), alpha=record(alpha),
        whole_cell_raw_w_upper=record(upper_w), cap_raw_threshold=record(raw_threshold),
        cap_strictly_inactive=True, valley_control_exact_zero=True, warp_weight_exact_one=True,
        chi_and_j0_exact_one=True, source_rule='RealHead formula; fixed raw table R/alpha, no replacement by R20 or R64')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ('ready', 'real-source', 'ports', 'slope', 'old-flow', 'out-prefix'):
        parser.add_argument('--'+name, required=True, type=Path)
    parser.add_argument('--order', type=int, default=24)
    parser.add_argument('--precision', type=int, default=256)
    parser.add_argument('--remainder-bits', type=int, default=100)
    parser.add_argument('--root-bits', type=int, default=160)
    parser.add_argument('--initial-parts', type=int, default=8)
    parser.add_argument('--rss-kib', type=int, default=40960)
    args = parser.parse_args()
    if args.order < 4 or args.precision < args.root_bits+32 or args.initial_parts < 1:
        raise ValueError('Unsafe Taylor order, series precision or root bracket precision')
    ctx.prec, ctx.cap, ctx.threads = args.precision, args.order+2, 1
    started = time.monotonic()
    out = Path(str(args.out_prefix)+'.json')
    if out.exists():
        raise FileExistsError('Use a new complete outer-flow prefix')
    taylor_path = Path(__file__).with_name('closure_taylor_cut_slope_v2.py')
    source_path = Path(__file__).with_name('closure_real_head_source_enclosure.py')
    if digest(taylor_path) != EXPECTED_TAYLOR or digest(source_path) != EXPECTED_SOURCE:
        raise ValueError('A validated local mathematical implementation changed')
    for name, expected in [('closure_projective_interval_column.py', EXPECTED_PROJECTIVE),
                           ('closure_real_linear_head_enclosure.py', EXPECTED_PB)]:
        if digest(Path(__file__).with_name(name)) != expected:
            raise ValueError('A shared projective/PB implementation changed')
    inputs = {str(getattr(args, k)):digest(getattr(args, k))
              for k in ('ready', 'real_source', 'ports', 'slope', 'old_flow')}
    source = dict(ports=read_field(args.real_source, 'ports'),
        checks=read_field(args.real_source, 'checks'), input_hashes=read_field(args.real_source, 'input_hashes'))
    slope = json.loads(args.slope.read_text())
    old = json.loads(args.old_flow.read_text())
    if (not all(source['checks'].values()) or not all(slope['gates'].values())
            or not old['finite_background_flow_complete'] or old['cells_completed'] != [11, 10]
            or slope['config']['modes'] != [2, 4]):
        raise ValueError('The original real source, true slope and actual outer flow are required')
    rh = inputs[str(args.ready)]
    if (rh not in source['input_hashes'].values() or rh not in slope['input_hashes'].values()
            or old['ready_sha256'] != rh or rh not in read_field(args.ports, 'input_hashes').values()):
        raise ValueError('The two sides of the interface use different frozen metric data')
    ready = dict(rationalDeepModel=read_field(args.ready, 'rationalDeepModel'),
                 shallowSourceParameters=read_field(args.ready, 'shallowSourceParameters'))
    identities = [raw_source_identity(ready, n) for n in (11, 10)]
    ports = {x['physical_node']:x for x in iter_array(args.ports, 'rows') if x['physical_node'] in (10, 11, 12)}
    for n in (10, 11):
        source['ports'][str(n)] = dict(radius=ports[n]['radius'])
    b = ball(source['ports']['12']['radius'])
    mu_star = ball(source['ports']['12']['mu'])
    if source['ports']['12']['normalization_cell'] != 11:
        raise ValueError('The unique outer momentum coordinate must be mu11')
    if not intersect(mu_star, ball(old['global_mu_star'])) > 0:
        raise ValueError('The old and new fixed global momentum scales differ')
    h = AnchoredHead(ready, source, 10, 12, args.precision//2, args.precision-32)
    del ready
    modes = [2, 4]
    slope_rows = {x['mode']:x for x in slope['rows']}
    vectors = []
    for mode in modes:
        scale = (b/h.rc)**(mode*mode-4)
        shat = endpoint(slope_rows[mode]['shared_exact_dyadic_slope'])
        vectors.append([ProjectiveColumn([1/scale, scale*shat]),
                        ProjectiveColumn([arb(1), arb(0)]),
                        ProjectiveColumn([arb(0), arb(1)])])
    radius = b
    counts = dict(taylor=0, root_brackets=0, rejected=0)
    worst = arb(0)
    cell_rows = []
    config = dict(cells=[11, 10], modes=modes, order=args.order, precision=args.precision,
        remainder_bits=args.remainder_bits, root_bits=args.root_bits, initial_parts=args.initial_parts,
        global_mu_star=record(mu_star), momentum_coordinate='p/mu11 across the entire outer range; no rho jump',
        input_hashes=inputs, entrypoint_sha256=digest(Path(__file__)),
        Taylor_source_sha256=EXPECTED_TAYLOR, real_source_sha256=EXPECTED_SOURCE)

    def guard():
        peak = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
        if peak > args.rss_kib:
            raise MemoryError('Observed owned RSS exceeded the stop threshold: '+str(peak))

    try:
        for n in (11, 10):
            for j in range(9):
                segment = h.cells[n]['segments'][j]
                radius = intersect(radius, segment['physical_inner_radius'])
                for left, right, sign in monotone_parts(segment, args.root_bits):
                    segment['_monotone_sign'] = sign
                    pieces = ([(left, right, 0)] if sign == 0 else
                        [(left+(right-left)*k/args.initial_parts,
                          left+(right-left)*(k+1)/args.initial_parts, 0)
                         for k in range(args.initial_parts)])
                    stack = list(reversed(pieces))
                    while stack:
                        a, c, level = stack.pop()
                        try:
                            flows, following, error = (root_global(h, segment, a, c, radius, modes, mu_star)
                                if sign == 0 else taylor_global(h, segment, a, c, radius, modes,
                                    args.order, power2(-args.remainder_bits), mu_star))
                            advanced = []
                            for group, flow in zip(vectors, flows):
                                group_next = []
                                for value in group:
                                    v = restore_column(column_record(value))
                                    v.advance(flow)
                                    group_next.append(v)
                                advanced.append(group_next)
                        except (ArithmeticError, ValueError, ZeroDivisionError) as error:
                            if sign == 0 or level >= 40:
                                raise ArithmeticError('Unresolved outer real flow at '+str((n, j, a, c, sign))+': '+str(error)) from error
                            midpoint = (a+c)/2
                            stack.extend([(midpoint, c, level+1), (a, midpoint, level+1)])
                            counts['rejected'] += 1
                            continue
                        radius, vectors = following, advanced
                        counts['root_brackets' if sign == 0 else 'taylor'] += 1
                        if sign != 0:
                            worst = max(worst, error)
                        guard()
                radius = intersect(radius, segment['physical_outer_radius'])
                checkpoint = dict(status='Complete actual outer segment; global mu11 gauge retained',
                    config=config, cell=n, segment=j, radius=record(radius),
                    columns=[[column_record(v) for v in group] for group in vectors],
                    counts=counts, greatest_balanced_Taylor_remainder=record(worst),
                    elapsed_seconds=time.monotonic()-started,
                    peak_RSS_KiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
                cp = Path(str(args.out_prefix)+f'-cell{n:03d}-seg{j}.json')
                if cp.exists():
                    raise FileExistsError('An actual completed outer segment would be overwritten')
                save(cp, checkpoint)
                print(json.dumps(dict(event='complete_outer_segment', cell=n, segment=j, counts=counts,
                    elapsed_seconds=time.monotonic()-started,
                    peak_RSS_KiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)), flush=True)
            radius = intersect(radius, ball(ports[n]['radius']))
            old_cell = next(x for x in old['cell_rows'] if x['cell'] == n)
            mode_rows = []
            for mode, group in zip(modes, vectors):
                u = mode*mode-4
                scale = (radius/h.rc)**u
                phi = [[group[j+1].component_bounds(i) for j in range(2)] for i in range(2)]
                phi_balls = [[x[0].union(x[1]) for x in row] for row in phi]
                A = (radius/b)**u*phi_balls[0][0]
                B = (radius*b/h.rc**2)**u*phi_balls[0][1]
                Qhat_pair = positive_scale_bounds(group[0].component_bounds(0), scale)
                Xihat_pair = positive_scale_bounds(group[0].component_bounds(1), 1/scale)
                Qhat = Qhat_pair[0].union(Qhat_pair[1])
                ds = ball(slope_rows[mode]['true_minus_shared_exact_slope'])
                actual_slope = ball(slope_rows[mode]['true_slope_mu_outer'])
                S = intersect(Qhat+B*ds, A+B*actual_slope)
                old_mode = next(x for x in old_cell['modes'] if x['mode'] == mode)
                S = intersect(S, ball(old_mode['b0_endpoint']['Q']))
                chart = not S.contains(0)
                if not chart:
                    raise ArithmeticError('The actual outer low-height Schur chart has not been proved nonzero')
                mode_rows.append(dict(mode=mode,
                    global_gauge_fundamental_matrix=[[dict(lower=point_record(x[0]), upper=point_record(x[1])) for x in row] for row in phi],
                    shared_exact_dyadic_slope=slope_rows[mode]['shared_exact_dyadic_slope'],
                    true_minus_shared_exact_slope=slope_rows[mode]['true_minus_shared_exact_slope'],
                    S0_affine_A=record(A), S0_affine_B=record(B),
                    S0_shared_centre_Q=record(Qhat), S0_true_Q=record(S),
                    S0_shared_centre_global_Xi=dict(lower=point_record(Xihat_pair[0]), upper=point_record(Xihat_pair[1])),
                    old_true_S0_Q=old_mode['b0_endpoint']['Q'],
                    S0_true_height=record(radius**4*S), height_chart_excludes_zero=chart,
                    exact_global_gauge_determinant=1,
                    column_states=[column_record(v) for v in group]))
            cell_rows.append(dict(cell=n, endpoint_physical_node=n, radius=record(radius), modes=mode_rows))
            save(Path(str(args.out_prefix)+f'-completed-cell{n:03d}.json'),
                dict(config=config, source_identity=next(x for x in identities if x['cell']==n), row=cell_rows[-1]))
        gates = dict(same_frozen_real_metric=True, both_cells_caps_proved_inactive=True,
            all_valley_and_warp_controls_retained=True, exact_physical_radius_anchors=True,
            global_mu11_without_interface_rescaling=True, all18_segments_complete=True,
            all_root_brackets_and_Taylor_remainders_paid=True, two_modes_and_two_basis_columns_complete=True,
            true_slope_variable_shared_in_all_S0_rows=True, all_true_S0_charts_nonzero=True,
            old_true_flow_intersections=True)
        result = dict(status='Validated actual outer11/10 signed background S0 and full two-mode basis flow',
            config=config, gates=gates, source_identity=identities, cell_rows=cell_rows,
            input_hashes=inputs, source_integrals=h.integral_count, counts=counts,
            greatest_balanced_Taylor_remainder=record(worst),
            source_units='For physical height forcing f_H in L_m H=f_H, v_r forcing=(r/rc)^u*r^4*w/(sqrt12*mu11)*f_H; v_x has another r_x. q forcing is0.',
            complete_outer_nonlinear_problem_paid=False, actual_forcing_kernel_paid=False,
            whole46_Schur_or_high_frequency_paid=False,
            elapsed_seconds=time.monotonic()-started,
            peak_RSS_KiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
        save(out, result)
        guard()
        print(json.dumps(dict(event='complete', path=str(out), gates=gates,
            rows=[dict(node=r['endpoint_physical_node'], mode=x['mode'], S0=str(ball(x['S0_true_Q'])))
                  for r in cell_rows for x in r['modes']],
            elapsed_seconds=time.monotonic()-started,
            peak_RSS_KiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)), flush=True)
    except Exception as error:
        save(Path(str(args.out_prefix)+'-failure.json'), dict(config=config,
            status='Actual outer interval attempt did not complete; no true singularity is inferred',
            error=repr(error), counts=counts, elapsed_seconds=time.monotonic()-started,
            peak_RSS_KiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss))
        raise


if __name__ == '__main__':
    main()
