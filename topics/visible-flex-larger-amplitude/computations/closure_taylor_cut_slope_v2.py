#!/usr/bin/env python3
"""v2: explicit R22-column/R26-radius provenance chain; mathematical flow unchanged.

A rigorous finite Taylor column, compared to the SAME true tail by Wronskian.

This does not replace the infinite boundary condition by a finite Robin one.
The finite column starts with (Q,Xi)=(1,0) at an existing true radius port.
Its difference from the already certified true stable column is bounded by
the physical mu*determinant at that inner port. Only the chosen low modes
are refined. All old full-frequency/nonlinear results retain their scope.

Author: exact_closure (GPT-6 Astra Pro, AI-assisted), 2026-11-12.
"""
import argparse
from fractions import Fraction
import hashlib
import json
from pathlib import Path
import resource
import time

from flint import arb, arb_series, ctx

from closure_real_head_source_enclosure import RealHead, exact_q, power2
from closure_projective_interval_column import ProjectiveColumn
from closure_real_linear_head_enclosure import peano_matrix, positive_scale_bounds
from closure_split_joint_io_v2 import digest, iter_array, read_field


EXPECTED_SOURCE = '97ff78a171b284cd8d5acc8dc233bcfe1f0b7c428ce2fbbd5b7104bd0ecb8c47'
EXPECTED_PROJECTIVE = '45997a1d5be6326a1ebbe85ac4240ea7d9dde1c2fb6acdf832460dade89e4f97'
EXPECTED_PB = '1b8023b53eeca7a0ef28816a99b1b7d4a43f025c2482afae9e88db572e174b8e'


def endpoint(d):
    return arb((int(d['mantissa']), int(d['binary_exponent'])))


def ball(d):
    return endpoint(d['lower']).union(endpoint(d['upper']))


def point_record(x):
    a, b = x.man_exp()
    return dict(mantissa=str(a), binary_exponent=int(b))


def record(x):
    if not x.is_finite():
        raise ArithmeticError('A nonfinite interval cannot be a certificate')
    return dict(lower=point_record(x.lower()), upper=point_record(x.upper()))


def point_fraction(x):
    a, b = x.man_exp()
    return Fraction(int(a)) * Fraction(2) ** int(b)


def intersect(a, b):
    lo = max(a.lower(), b.lower())
    hi = min(a.upper(), b.upper())
    if lo > hi:
        raise ArithmeticError('Two enclosures of the same true quantity do not meet')
    return lo.union(hi)


def add_error(x, e):
    return x + (-e.upper()).union(e.upper())


def positive_lower(d):
    lo, hi = endpoint(d['lower']), endpoint(d['upper'])
    if lo > 0:
        return lo
    if hi < 0:
        return -hi
    raise ArithmeticError('The exact height chart has not been separated from zero')


def column_record(v):
    return dict(pivot=v.pivot, sign=v.sign, ratio=record(v.ratio),
                absolute_lower=point_record(v.absolute_lower),
                absolute_upper=point_record(v.absolute_upper))


def restore_column(d):
    v = ProjectiveColumn.__new__(ProjectiveColumn)
    v.pivot, v.sign = int(d['pivot']), int(d['sign'])
    v.ratio = ball(d['ratio'])
    v.absolute_lower = endpoint(d['absolute_lower'])
    v.absolute_upper = endpoint(d['absolute_upper'])
    if v.pivot not in (0, 1) or v.sign not in (-1, 1) or not v.absolute_lower > 0:
        raise ValueError('An exact projective checkpoint is malformed')
    return v


def save(path, data):
    path = Path(path)
    raw = (json.dumps(data, separators=(',', ':')) + '\n').encode()
    if len(raw) >= 1_000_000:
        raise ArithmeticError('The deliberately small slope certificate exceeded 1 MB')
    tmp = Path(str(path) + '.partial')
    tmp.write_bytes(raw)
    tmp.replace(path)


class AnchoredHead(RealHead):
    """Same RealHead methods, with an already certified exact inner radius.

    No deeper metric width is recomputed or suppressed. The radius at the
    chosen physical node is an input interval for the already defined metric.
    The original make_cell/free_width/source functions are inherited unchanged.
    """
    def __init__(self, ready, source_ledger, start, inner, rel_bits, abs_bits):
        self.ready = ready
        self.params = ready['rationalDeepModel']['physicalParameters']
        self.data = {x['n']: x for x in ready['shallowSourceParameters']['cells']}
        self.rc = exact_q(self.params['rCuff'])
        self.eps_phys = exact_q(self.params['epsilonScale'])
        self.eps = self.eps_phys / self.rc ** 7
        self.alpha = exact_q(ready['rationalDeepModel']['frozenWarpAlpha'])
        constants = ready['rationalDeepModel']['exactSourceConstants']
        self.d0 = exact_q(Fraction(constants['delta0']))
        self.c0 = exact_q(Fraction(constants['etaRatioAtN0']))
        self.a = arb(11) / 4
        self.sqrt12, self.log2 = arb(12).sqrt(), arb(2).log()
        self.rho = (self.a * self.log2).exp()
        self.start, self.far, self.exact_through = start, inner, inner - 1
        self.rel_tol, self.abs_tol = power2(-rel_bits), power2(-abs_bits)
        self.integral_count = 0
        self.cells, self.node_radii = {}, {}
        radius = ball(source_ledger['ports'][str(inner)]['radius'])
        self.node_radii[inner] = radius
        for n in range(inner - 1, start - 1, -1):
            cell = self.make_cell(n)
            cell['inner_radius'] = radius
            for segment in cell['segments']:
                segment['physical_inner_radius'] = radius
                radius += segment['width']
                segment['physical_outer_radius'] = radius
            cell['outer_radius'] = radius
            self.cells[n] = cell
            self.node_radii[n] = radius
        self.node_radii[start] = intersect(self.node_radii[start],
            ball(source_ledger['ports'][str(start)]['radius']))


def source_series(h, segment, xbase, span, order, sign):
    """Jets of w and scaled r_x at an arbitrary base point.

    xbase may be an interval over the full panel. The coefficients then
    enclose the derivatives at every base point in that panel. sign is the
    proved monotonicity sign of w_x; root brackets use a separate PB step.
    """
    x = arb_series([xbase, span], prec=order + 2)
    log_ro = segment['log_r0'] + segment['length'] * x / h.sqrt12
    ro = log_ro.exp()
    smooth = x*x*x*(10+x*(-15+6*x)) if segment['transition'] else arb_series([0], prec=order+2)
    dsmooth = 30*x*x*(1-x)*(1-x) if segment['transition'] else arb_series([0], prec=order+2)
    log_w = segment['log_mu'] + segment['log_p0'] + segment['log_jump'] * smooth - 7*log_ro
    w = log_w.exp()
    dlogw = segment['log_jump'] * dsmooth - 7*segment['length']/h.sqrt12
    invE = (1+w*w).inv()
    gx = sign*w*dlogw*invE*invE.sqrt()/8 + h.alpha*segment['length']*ro*invE/h.sqrt12
    return w, span*gx


def generator_series(h, segment, xbase, span, rbase, order, sign, mode):
    w, g = source_series(h, segment, xbase, span, order, sign)
    r = arb_series([rbase] + [g[k-1]/k for k in range(1, order+2)], prec=order+2)
    u, nu = mode*mode-4, arb(mode*mode*(mode*mode-1))/12
    mu = h.cells[segment['n']]['mu']
    a = h.sqrt12*mu*h.rc**(2*u)*g / (r**(8+2*u)*w)
    b = nu*h.sqrt12/(mu*h.rc**(2*u))*r**(6+2*u)*w*g
    return a, b, g


def matrix_coefficients(a, b, order, initial, absolute=False):
    """Exact coefficient recurrence or its componentwise derivative majorant."""
    coeff = [initial]
    for k in range(order):
        row = [[arb(0), arb(0)], [arb(0), arb(0)]]
        for j in range(k+1):
            aa, bb = (abs(a[j]).upper(), abs(b[j]).upper()) if absolute else (a[j], -b[j])
            for c in range(2):
                row[0][c] += aa*coeff[k-j][1][c]
                row[1][c] += bb*coeff[k-j][0][c]
        coeff.append([[x/(k+1) for x in row[i]] for i in range(2)])
    return coeff


def rough_radius(h, segment, left, right, radius):
    lo, hi = exact_q(left), exact_q(right)
    source = h.source_point(segment, lo.union(hi))
    w = source['w']
    E = 1+w*w
    g = abs(w*source['log_w_x'])/(8*E*E.sqrt()) + h.alpha*source['ro_x']/E
    if not g.is_finite() or not radius > 0 or not w > 0:
        raise ArithmeticError('The real source panel needs subdivision')
    width_upper = ((hi-lo)*abs(g).upper()).upper()
    rr = radius.lower().union((radius.upper()+width_upper).upper())
    rr = intersect(rr, segment['physical_inner_radius'].lower().union(segment['physical_outer_radius'].upper()))
    return rr, width_upper


def taylor_panel(h, segment, left, right, radius, modes, order, tol):
    sign = segment['_monotone_sign']
    x0, span = exact_q(left), exact_q(right-left)
    xall = x0.union(exact_q(right))
    rr, _ = rough_radius(h, segment, left, right, radius)
    flows = []
    worst = arb(0)
    for mode in modes:
        aa, bb, gc = generator_series(h, segment, x0, span, radius, order, sign, mode)
        ai, bi, gi = generator_series(h, segment, xall, span, rr, order, sign, mode)
        au, bu = abs(ai[0]).upper(), abs(bi[0]).upper()
        product = (au*bu).upper()
        if not product < arb(1)/4:
            raise ArithmeticError('Subdivide: the positive local-flow majorant is too large')
        denominator = 1-product
        major = [[1/denominator, au/denominator], [bu/denominator, 1/denominator]]
        identity = [[arb(1), arb(0)], [arb(0), arb(1)]]
        exact_coeffs = matrix_coefficients(aa, bb, order, identity)
        derivative_bounds = matrix_coefficients(ai, bi, order+1, major, absolute=True)
        remainder = derivative_bounds[order+1]
        balance = (bu/au).sqrt()
        local_error = max(remainder[0][0].upper(), remainder[1][1].upper(),
            (remainder[0][1]*balance).upper(), (remainder[1][0]/balance).upper())
        if not local_error < tol:
            raise ArithmeticError('Subdivide: the rigorous Taylor remainder is too large')
        flow = [[add_error(sum((c[i][j] for c in exact_coeffs), arb(0)), remainder[i][j])
                 for j in range(2)] for i in range(2)]
        if any(not x.is_finite() for row in flow for x in row):
            raise ArithmeticError('The Taylor coefficient enclosure is nonfinite')
        flows.append(flow)
        worst = max(worst, local_error)
    # Integrate the SAME exact radial derivative; this is not an independent
    # profile approximation. gi[p] is a derivative bound at every base point.
    dr = sum((gc[k]/(k+1) for k in range(order)), arb(0))
    dr = add_error(dr, abs(gi[order]).upper()/(order+1))
    if not dr > 0:
        raise ArithmeticError('Subdivide: the positive true radial increment was lost')
    following = intersect(radius+dr, rr)
    return flows, following, worst


def root_panel(h, segment, left, right, radius, modes):
    """A tiny critical-root bracket needs no analyticity of abs(w_x)."""
    rr, dr = rough_radius(h, segment, left, right, radius)
    source = h.source_point(segment, exact_q(left).union(exact_q(right)))
    w = source['w']
    flows = []
    worst = arb(0)
    for mode in modes:
        u, nu = mode*mode-4, arb(mode*mode*(mode*mode-1))/12
        mu = h.cells[segment['n']]['mu']
        au = abs(h.sqrt12*mu*h.rc**(2*u)*dr/(rr**(8+2*u)*w)).upper()
        bu = abs(nu*h.sqrt12/(mu*h.rc**(2*u))*rr**(6+2*u)*w*dr).upper()
        flow, _, product = peano_matrix(arb(0).union(au), arb(0).union(bu))
        flows.append(flow)
        worst = max(worst, product.upper())
    following = intersect(radius + arb(0).union(dr), rr)
    return flows, following, worst


def monotone_parts(segment, bits):
    if not segment['critical_points']:
        return [(Fraction(0), Fraction(1), -1)]
    brackets = []
    scale = 1 << bits
    for root in segment['critical_points']:
        lo, hi = point_fraction(root.lower()), point_fraction(root.upper())
        a = Fraction((lo*scale).__floor__()-1, scale)
        b = Fraction((hi*scale).__ceil__()+1, scale)
        brackets.append((a, b))
    (a, b), (c, d) = brackets
    if not 0 < a < b < c < d < 1:
        raise ArithmeticError('Critical roots have not been isolated in disjoint dyadic brackets')
    return [(Fraction(0), a, -1), (a, b, 0), (b, c, 1), (c, d, 0), (d, Fraction(1), -1)]


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--ready', required=True, type=Path)
    p.add_argument('--source-ledger', required=True, type=Path)
    p.add_argument('--columns', required=True, type=Path)
    p.add_argument('--out-prefix', required=True, type=Path)
    p.add_argument('--inner', type=int, default=16)
    p.add_argument('--cut', type=int, default=12)
    p.add_argument('--mode', action='append', type=int, default=[])
    p.add_argument('--order', type=int, default=24)
    p.add_argument('--precision', type=int, default=256)
    p.add_argument('--remainder-bits', type=int, default=100)
    p.add_argument('--root-bits', type=int, default=160)
    p.add_argument('--initial-parts', type=int, default=8)
    p.add_argument('--rss-kib', type=int, default=40960)
    p.add_argument('--resume', type=Path)
    args = p.parse_args()
    ctx.prec, ctx.cap, ctx.threads = args.precision, args.order+2, 1
    modes = args.mode or [2, 4]
    if (not 12 == args.cut < args.inner <= 24 or args.inner not in (16, 24)
            or any(m < 2 or m > 92 or m % 2 for m in modes)
            or len(set(modes)) != len(modes) or args.precision < args.root_bits+32
            or args.order < 4 or args.initial_parts < 1):
        raise ValueError('Unsupported scope or an unsafe Taylor/root precision choice')
    out = Path(str(args.out_prefix)+'.json')
    if out.exists():
        raise FileExistsError('A completed certificate must never be overwritten')
    started = time.monotonic()
    source_path = Path(__file__).with_name('closure_real_head_source_enclosure.py')
    projective_path = Path(__file__).with_name('closure_projective_interval_column.py')
    pb_path = Path(__file__).with_name('closure_real_linear_head_enclosure.py')
    if [digest(x) for x in (source_path, projective_path, pb_path)] != [EXPECTED_SOURCE, EXPECTED_PROJECTIVE, EXPECTED_PB]:
        raise ValueError('An inherited mathematical source changed')
    inputs = {str(q): digest(q) for q in (args.ready, args.source_ledger, args.columns)}
    source_ledger = dict(ports=read_field(args.source_ledger, 'ports'),
        checks=read_field(args.source_ledger, 'checks'), input_hashes=read_field(args.source_ledger, 'input_hashes'))
    if not all(source_ledger['checks'].values()) or inputs[str(args.ready)] not in source_ledger['input_hashes'].values():
        raise ValueError('The exact real-radius ledger does not certify this ready source')
    if read_field(args.columns, 'source_enclosure_sha256') != EXPECTED_SOURCE:
        raise ValueError('The true infinite linear comparison uses another source definition')
    column_inputs = read_field(args.columns, 'input_hashes')
    if inputs[str(args.ready)] not in column_inputs.values():
        raise ValueError('The true infinite linear columns use a different frozen ready source')
    old_ledgers = [Path(name) for name in column_inputs if 'ledger' in Path(name).name]
    if len(old_ledgers) != 1:
        raise ValueError('The true infinite column source ledger must be explicit')
    old_ledger = old_ledgers[0]
    if digest(old_ledger) != column_inputs[str(old_ledger)]:
        raise ValueError('The R22 paid source-parameter ledger changed')
    if not all(read_field(old_ledger, 'checks').values()):
        raise ValueError('The R22 source-parameter checks were not all paid')
    if inputs[str(args.ready)] not in read_field(old_ledger, 'input_hashes').values():
        raise ValueError('The R22 and R26 ledgers do not refer to the same frozen ready')
    inputs[str(old_ledger)] = column_inputs[str(old_ledger)]
    ready = dict(rationalDeepModel=read_field(args.ready, 'rationalDeepModel'),
                 shallowSourceParameters=read_field(args.ready, 'shallowSourceParameters'))
    config = dict(cut=args.cut, inner=args.inner, modes=modes, order=args.order,
        precision=args.precision, remainder_bits=args.remainder_bits, root_bits=args.root_bits,
        initial_parts=args.initial_parts, input_hashes=inputs,
        entrypoint_sha256=digest(Path(__file__)), source_sha256=EXPECTED_SOURCE,
        projective_sha256=EXPECTED_PROJECTIVE, peano_sha256=EXPECTED_PB)
    h = AnchoredHead(ready, source_ledger, args.cut, args.inner, args.precision//2, args.precision-32)
    del ready
    initial_radius = h.node_radii[args.inner]
    vectors = [ProjectiveColumn([(h.rc/initial_radius)**(m*m-4), arb(0)]) for m in modes]
    radius = initial_radius
    completed = -1
    counts = dict(taylor=0, root_brackets=0, rejected=0)
    greatest_remainder = arb(0)
    if args.resume:
        prior = json.loads(args.resume.read_text())
        if prior['config'] != config:
            raise ValueError('A resume checkpoint has different exact source or arithmetic parameters')
        vectors = [restore_column(x) for x in prior['columns']]
        radius, completed, counts = ball(prior['radius']), prior['completed_task'], prior['counts']
        greatest_remainder = ball(prior['greatest_balanced_Taylor_remainder'])
    tasks = [(n, j) for n in range(args.inner-1, args.cut-1, -1) for j in range(9)]

    def guard():
        rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
        if rss > args.rss_kib:
            raise MemoryError('Observed self peak RSS exceeded the declared stop threshold: '+str(rss))

    try:
        for task, (n, j) in enumerate(tasks):
            if task <= completed:
                continue
            if j == 0 and n < args.inner-1:
                for v in vectors:
                    v.multiply_component(1, 1/h.rho)
            segment = h.cells[n]['segments'][j]
            radius = intersect(radius, segment['physical_inner_radius'])
            for left, right, sign in monotone_parts(segment, args.root_bits):
                segment['_monotone_sign'] = sign
                if sign == 0:
                    pieces = [(left, right, 0)]
                else:
                    pieces = [(left+(right-left)*k/args.initial_parts,
                               left+(right-left)*(k+1)/args.initial_parts, 0)
                              for k in range(args.initial_parts)]
                stack = list(reversed(pieces))
                while stack:
                    a, b, level = stack.pop()
                    try:
                        flows, following, remainder = (root_panel(h, segment, a, b, radius, modes)
                            if sign == 0 else taylor_panel(h, segment, a, b, radius, modes, args.order, power2(-args.remainder_bits)))
                        following_columns = []
                        for old, flow in zip(vectors, flows):
                            v = restore_column(column_record(old))
                            v.advance(flow)
                            following_columns.append(v)
                    except (ArithmeticError, ValueError, ZeroDivisionError) as error:
                        if sign == 0 or level >= 40:
                            raise ArithmeticError('Unresolved local enclosure at '+str((n, j, a, b, sign))+': '+str(error)) from error
                        middle = (a+b)/2
                        stack.append((middle, b, level+1))
                        stack.append((a, middle, level+1))
                        counts['rejected'] += 1
                        continue
                    vectors, radius = following_columns, following
                    counts['root_brackets' if sign == 0 else 'taylor'] += 1
                    if sign != 0:
                        greatest_remainder = max(greatest_remainder, remainder)
                    guard()
            radius = intersect(radius, segment['physical_outer_radius'])
            checkpoint = dict(status='Complete exact finite-column source segment; infinite comparison pending',
                config=config, completed_task=task, cell=n, segment=j, radius=record(radius),
                columns=[column_record(v) for v in vectors], counts=counts,
                greatest_balanced_Taylor_remainder=record(greatest_remainder),
                elapsed_seconds=time.monotonic()-started,
                peak_RSS_KiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
            name = Path(str(args.out_prefix)+f'-cell{n:03d}-seg{j}.json')
            if name.exists():
                raise FileExistsError('A completed source segment would be overwritten')
            save(name, checkpoint)
            print(json.dumps(dict(event='complete_segment', cell=n, segment=j, counts=counts,
                elapsed_seconds=time.monotonic()-started,
                peak_RSS_KiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)), flush=True)
            guard()
        # The independently certified TRUE stable column enters only here.
        comparison = {}
        for group in read_field(args.columns, 'column_groups'):
            wanted = set(modes).intersection(group['modes'])
            if not wanted:
                continue
            path = Path(group['path'])
            if digest(path) != group['sha256']:
                raise ValueError('A true comparison-column group hash changed')
            inputs[str(path)] = group['sha256']
            ends = {x['mode']: x for x in read_field(path, 'endpoint_rows')}
            row = next(x for x in iter_array(path, 'cell_rows') if x['cell'] == args.inner)
            for x in row['linear_rows']:
                if x['mode'] in wanted:
                    gain_lower = positive_lower(ends[x['mode']]['Q_gain'])
                    comparison[x['mode']] = dict(mu=ball(row['mu']),
                        normalized_true_Xi_sup=(ball(x['column_Xi_sup']).upper()/gain_lower).upper(),
                        group_path=str(path), group_hash=group['sha256'])
        old_ends = {x['mode']: x for x in read_field(args.columns, 'endpoint_rows')}
        mu_outer = ball(source_ledger['ports'][str(args.cut)]['mu'])
        cut_radius = intersect(radius, ball(source_ledger['ports'][str(args.cut)]['radius']))
        results = []
        for mode, v in zip(modes, vectors):
            u = mode*mode-4
            scale = (cut_radius/h.rc)**u
            qlo, qhi = positive_scale_bounds(v.component_bounds(0), scale)
            gain_lower = qlo if qlo > 0 else (-qhi if qhi < 0 else arb(0))
            if not gain_lower > 0:
                raise ArithmeticError('The finite column is not in the shallow height chart')
            unit = v.unit()
            finite_slope = unit[1]/unit[0]/(h.rho*scale*scale)
            cp = comparison[mode]
            discrepancy = (cp['mu'].upper()/mu_outer.lower()*cp['normalized_true_Xi_sup']/gain_lower).upper()
            true_slope = add_error(finite_slope, discrepancy)
            old_slope = ball(old_ends[mode]['raw_worker_slope'])
            true_slope = intersect(true_slope, old_slope)
            shared = true_slope.mid()
            results.append(dict(mode=mode, finite_slope_mu_outer=record(finite_slope),
                normalized_true_inner_Xi_bound=record(cp['normalized_true_Xi_sup']),
                finite_Q_gain=dict(lower=point_record(qlo), upper=point_record(qhi)),
                Wronskian_true_minus_finite_slope_upper=record(discrepancy),
                true_slope_mu_outer=record(true_slope), old_true_slope_mu_outer=record(old_slope),
                shared_exact_dyadic_slope=point_record(shared),
                true_minus_shared_exact_slope=record(true_slope-shared),
                slope_width_improvement_log2=record(((old_slope.upper()-old_slope.lower())/
                    (true_slope.upper()-true_slope.lower())).log()/h.log2),
                comparison_column_group=cp['group_path']))
        gates = dict(same_frozen_real_metric=True, exact_inner_radius_anchor=True,
            all_requested_finite_segments_complete=True, rigorously_bounded_Taylor_remainders=True,
            all_critical_root_brackets_paid=True, exact_projective_columns_retained=True,
            all_finite_height_charts_nonzero=True, same_true_infinite_column_Wronskian=True,
            outer_mu_coordinate_correct=True, old_true_interval_intersection=True)
        result = dict(status='Validated true linear cut slope via finite Taylor column plus exact Wronskian comparison',
            config=config, gates=gates, input_hashes=inputs, cut_radius=record(cut_radius),
            initial_finite_column=dict(physical_node=args.inner, Q=1, Xi=0,
                normalization_cell=args.inner-1,
                interpretation='An arbitrary exact comparison column, never a replacement tail boundary condition'),
            rows=results, counts=counts, source_integrals=h.integral_count,
            greatest_balanced_Taylor_remainder=record(greatest_remainder),
            elapsed_seconds=time.monotonic()-started,
            peak_RSS_KiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
            limits=['Only the listed homogeneous linear slopes are refined; no new nonlinear or outer Schur claim.',
                'The shared dyadic slope is a common exact centre; its true remainder is retained on both sides.',
                'The mathematical positive-determinant flow, not an independent determinant interval test, justifies the projective endpoint propagation.',
                'The radius interval is the same exact metric source; source uncertainty is retained in every jet and derivative majorant.'])
        save(out, result)
        guard()
        print(json.dumps(dict(event='complete', path=str(out), gates=gates,
            slopes=[dict(mode=x['mode'], true=str(ball(x['true_slope_mu_outer'])),
                         gain_bits=str(ball(x['slope_width_improvement_log2']))) for x in results],
            peak_RSS_KiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)), flush=True)
    except Exception as error:
        save(Path(str(args.out_prefix)+'-failure.json'), dict(status='This new finite enclosure did not complete; no true singularity is inferred',
            config=config, error=repr(error), counts=counts,
            elapsed_seconds=time.monotonic()-started,
            peak_RSS_KiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss))
        raise


if __name__ == '__main__':
    main()
