#!/usr/bin/env python3
"""Actual mixed-density, source-resolved middle Volterra geometry v3.

Source-origin v3 preserves every original physical Taylor/root transition and
all original V^2 results. It also accumulates the independent positive
materials s*V, |ell|*V, s, |ell|. These are linear geometric kernels;
each source origin retains signed two-column whole-field propagation;
the complete mixed-field domain and strip-transfer gates are NOT claimed
by producing them. The original v1 entry remains frozen and unchanged.

This NEW entry point reuses the frozen R87 physical Taylor integrator and
the exact R84/R90 local V identity. It computes a declared finite even
window (default 94,96); it does not assert the full middle band is done.
At every original source segment the inhomogeneous representation resets
to the identity, while the genuine signed flow and global initial columns
are retained. No head slope for modes above 92 is invented: both true
physical high initial components are an input, bounded from R78.

No result is claimed until this source actually runs. Existing output is
never overwritten. Author: exact_closure, GPT-6 Astra Pro (AI-assisted).
"""
import argparse
from fractions import Fraction
import json
from pathlib import Path
import resource
import time
import sys

_boot = argparse.ArgumentParser(add_help=False)
_boot.add_argument("--computations", type=Path, required=True)
_boot_args, _unused = _boot.parse_known_args()
sys.path.insert(0, str(_boot_args.computations))

from flint import arb, ctx
from closure_outer_physical_trace_flow import (
    EXPECTED as FLOW_EXPECTED, taylor_physical, root_physical,
    balanced_majorant)
from closure_outer_physical_green_geometry_recovered_v2 import (
    EXPECTED as GEOMETRY_EXPECTED, INPUT_SHA, whole_column, upper, point)
from closure_outer_whole_field_profiles import derivative_density
from closure_outer_taylor_shared_flow import raw_source_identity
from closure_projective_interval_column import ProjectiveColumn
from closure_real_head_source_enclosure import exact_q, power2
from closure_real_linear_head_enclosure import PositiveKernels
from closure_split_joint_io_v2 import (
    digest, read_field, iter_array, metadata_without_array)
from closure_taylor_cut_slope_v2 import (
    rough_radius, monotone_parts, record, ball, intersect,
    add_error, column_record, restore_column, save)
from tail_r33_middle_ordered_physical import SourceValues

EXPECTED = dict(FLOW_EXPECTED)
EXPECTED.update(GEOMETRY_EXPECTED)
EXPECTED.update({
    'closure_outer_middle_volterra_recovered_v1.py':
        '6655a72f38f89d6eb31ded7b78bd4b84f94c500653bbb8e6c3ca2611d6af2e31',
    'closure_outer_physical_trace_flow.py':
        'd919902557b3c5c17e6e68602ba86f3b3852207057c3a2ea1468b08ecae4cc5e',
    'closure_outer_physical_green_geometry_recovered_v2.py':
        'c48606c4e127fb0d3f27479eeed11bff3c5cb69139148633ea4f74a9e1f63829',
})
OTHER_INPUTS = {
    'head': '9e891098dd625f7418c48d91ee92db900bd7b0d1c44b2b69c1cdebbd8d03c930',
    'r91': 'badc734ef590c747d62fc75bd57ce2571bd89e8c522604b691406f469d47392f',
}
LABELS = ('radial', 'log_w', 'V1_radial', 'V1_log_w', 'V0_radial', 'V0_log_w')
MATERIAL_POWERS = (2, 1, 0)


def exact_fraction(d):
    return Fraction(int(d['numerator']), int(d['denominator']))


def max_positive(old, value):
    if not value.is_finite():
        raise ArithmeticError('A nonfinite positive bound is not a certificate')
    return max(old, value.upper())


def partial_for_modes(h, segment, left, right, radius, original, modes):
    """All true subinterval matrices, including every target inside a leaf.

The coefficient integral hull contains zero. The fixed balanced norm
remainder is q^2/(1-q). This is the same frozen R90 proof, with the maximum
declared physical mode replacing 92; no low-mode endpoint slope is used.
"""
    rr, _ = rough_radius(h, segment, left, right, radius)
    rr = intersect(rr, ball(original['radius']))
    xx = exact_q(left).union(exact_q(right))
    source = h.source_point(segment, xx)
    w = intersect(source['w'], ball(original['w']))
    ell = intersect(source['log_w_x'], ball(original['log_w_x']))
    E = 1+w*w
    rx = abs(w*ell)/(8*E*E.sqrt())+h.alpha*source['ro_x']/E
    rx = intersect(rx, ball(original['radius_x']))
    if not rr > 0 or not w > 0 or not rx > 0 or not w.upper() <= arb(1)/2:
        raise ArithmeticError('The same complete real background domain is unpaid')
    span = exact_q(right-left)
    ss, ee = span*rx/rr, span*ell
    dd = (ee-ss)/2
    B, q, _ = balanced_majorant(dd, ss, ee, max(modes))
    err = (q*q/(1-q)).upper()
    rem = [[err, (err/B).upper()], [(err*B).upper(), err]]
    boxes = []
    for m in modes:
        A = [[dd, -m*ss], [-m*ee, -dd]]
        boxes.append([
            [add_error(arb(1 if i == j else 0)+arb(0).union(A[i][j]),
                       rem[i][j]) for j in range(2)] for i in range(2)])
    return boxes, rr, w, (rr*w*w*w).sqrt()


def initial_pair():
    return [ProjectiveColumn([arb(1), arb(0)]),
            ProjectiveColumn([arb(0), arb(1)])]


def whole_matrix(columns, partial):
    # Each column keeps its shared signed projective scale.
    cols = [whole_column(col, partial) for col in columns]
    return [[cols[j][i] for j in range(2)] for i in range(2)]


def endpoint_matrix(columns):
    cols = [v.values() for v in columns]
    return [[cols[j][i] for j in range(2)] for i in range(2)]


def advance_pair(columns, transition):
    result = []
    for col in columns:
        c = restore_column(column_record(col))
        c.advance(transition)
        result.append(c)
    return result


def positive_vec(d):
    return [point(v) for v in d]


def unit_source_image(A, before, integrals):
    """Own-source and incoming positive boxes in Y coordinates.

A is the exact identity-normalized block flow enclosure. If
I0 >= integral |A00(s)| F(s) d(s) ds and
I1 >= integral |A01(s)| F(s) d(s) ds, then
A(r) A(s)^-1 e2 = (-A_i0(r) A01(s)+A_i1(r) A00(s))_i.
The exact determinant is one. No independently rounded determinant is
divided and no false cancellation of source signs is imposed.
"""
    return [
        (sum((abs(A[i][j]).upper()*before[j] for j in range(2)), arb(0))
         +abs(A[i][0]).upper()*integrals[1]
         +abs(A[i][1]).upper()*integrals[0]).upper()
        for i in range(2)]


def main():
    p = argparse.ArgumentParser(description=__doc__)
    for key in ('ready', 'physical-flow', 'physical-manifest',
                'source11', 'source10', 'head', 'r91', 'out-prefix'):
        p.add_argument('--'+key, type=Path, required=True)
    p.add_argument("--computations", type=Path, required=True)
    p.add_argument('--modes', default='94,96')
    p.add_argument('--precision', type=int, default=256)
    p.add_argument('--order', type=int, default=24)
    p.add_argument('--root-bits', type=int, default=160)
    p.add_argument('--remainder-bits', type=int, default=100)
    p.add_argument('--rss-kib', type=int, default=98304)
    p.add_argument('--resume', type=Path)
    p.add_argument('--prepare-only', action='store_true')
    a = p.parse_args()
    started = time.monotonic()
    if a.resume:
        raise ValueError("The new source-origin state requires a fresh prefix; old coarse resumes are not imported")
    if ':' in a.modes:
        first, last = map(int, a.modes.split(':'))
        modes = list(range(first, last+1, 2))
    else:
        modes = [int(x) for x in a.modes.split(',')]
    if (not modes or modes != sorted(set(modes))
            or any(m < 94 or m > 8190 or m % 2 for m in modes)
            or a.precision < a.root_bits+32 or a.order < 24
            or a.root_bits < 160 or a.remainder_bits < 100):
        raise ValueError('Keep a declared complete even middle subwindow and rigorous arithmetic')
    for suffix in ('.json', '-failure.json', '-prepared.json'):
        if Path(str(a.out_prefix)+suffix).exists():
            raise FileExistsError('Use a fresh middle-window prefix')
    a.out_prefix.parent.mkdir(parents=True, exist_ok=True)
    ctx.prec, ctx.cap, ctx.threads = a.precision, a.order+2, 1
    for name, wanted in EXPECTED.items():
        if digest(a.computations/name) != wanted:
            raise ValueError('Frozen source identity failed: '+name)
    hashes = {}
    for key in ('ready', 'physical_flow', 'physical_manifest', 'source11', 'source10'):
        path = getattr(a, key)
        got = digest(path)
        if got != INPUT_SHA[key]:
            raise ValueError('Frozen input identity failed: '+key)
        hashes[str(path)] = got
    for key, wanted in OTHER_INPUTS.items():
        path = getattr(a, key)
        got = digest(path)
        if got != wanted:
            raise ValueError('Frozen head/R91 identity failed: '+key)
        hashes[str(path)] = got
    flow = json.loads(a.physical_flow.read_text())
    manifest = json.loads(a.physical_manifest.read_text())
    head = json.loads(a.head.read_text())
    paid = json.loads(a.r91.read_text())
    if (not flow['all_gates'] or not all(flow['gates'].values())
            or not manifest['all9_gates'] or manifest['true_height_charts_paid'] != 92
            or not head['all_gates'] or not all(head['gates'].values())
            or not paid['all_gates'] or len(paid['gates']) != 28
            or not all(paid['gates'].values())):
        raise ValueError('The complete paid actual background/head/low-centre objects are required')
    V0 = Fraction(1, 1 << 40)
    low_local = exact_fraction(paid['actual_low_complete_wide'])/V0
    if not low_local < 12:
        raise ValueError('The actual same-V low centre is not below the stated twelve ball')
    known = {row['path']: row['sha256'] for row in manifest['files']}
    if known.get(str(a.physical_flow)) != hashes[str(a.physical_flow)]:
        raise ValueError('The registered actual R87 primary differs')
    docs = {11: json.loads(a.source11.read_text()),
            10: json.loads(a.source10.read_text())}
    for n, doc in docs.items():
        if (doc['cell'] != n or not doc['all_gates'] or not all(doc['gates'].values())
                or doc['tau'] != '1/64'
                or doc['original_candidate_modes'] != list(range(2, 41, 2))
                or doc['input_hashes'].get(str(a.ready)) != hashes[str(a.ready)]):
            raise ValueError('The exact original complete source/V identity changed')
    if not docs[10]['same_exact_candidate']:
        raise ValueError('The refined true moments are not the same candidate')
    order = [(n, j) for n in (11, 10) for j in range(9)]
    groups = {(n, g['segment']): g for n, doc in docs.items() for g in doc['groups']}
    if sorted(groups) != sorted(order):
        raise ValueError('All eighteen original source groups must be present')
    for g in groups.values():
        if digest(Path(g['path'])) != g['sha256']:
            raise ValueError('A true source group changed')
        hashes[g['path']] = g['sha256']
    stem = str(a.physical_flow)[:-5]
    anchors = {}
    for n, j in order:
        path = Path(stem+f'-completed-cell{n:03d}-segment{j}.json')
        got = digest(path)
        if known.get(str(path)) != got:
            raise ValueError('An actual physical-radius anchor changed')
        hashes[str(path)] = got
        anchors[n, j] = path
    ready = dict(rationalDeepModel=read_field(a.ready, 'rationalDeepModel'),
                 shallowSourceParameters=read_field(a.ready, 'shallowSourceParameters'))
    identities = [raw_source_identity(ready, n) for n in (11, 10)]
    h = SourceValues(ready)
    kernel = PositiveKernels(h, 12, 4)
    h.cells = {n: kernel.source_cell(n) for n in (11, 10)}
    del ready
    b = ball(flow['config']['true_cut_radius'])
    wb = ball(flow['config']['true_cut_w'])
    Fb = (b*wb*wb*wb).sqrt()
    config = dict(
        modes=modes, cells=[11, 10], precision=a.precision, order=a.order,
        root_bits=a.root_bits, remainder_bits=a.remainder_bits,
        source_strip='18/125', local_low_centre_bound=12, local_middle_test_radius=1,
        density_definitions={LABELS[2*i]: '(r_x/r) V^'+str(p)
                             for i, p in enumerate(MATERIAL_POWERS)} |
                            {LABELS[2*i+1]: '|w_x/w| V^'+str(p)
                             for i, p in enumerate(MATERIAL_POWERS)},
        mixed_density_kernel_scope='Linear exact-background kernels only; full mixed domain and strip transfer are separate R98 gates',
        complete_weak_source_cap_factor=216,
        complete_weak_derivative_factor=52,
        exact_low_local_bound={'numerator': str(low_local.numerator),
                               'denominator': str(low_local.denominator)},
        input_hashes=hashes, source_hashes=EXPECTED,
        entrypoint_sha256=digest(__file__),
        causal_block_reconstruction="NEW v3; exact signed columns for every source origin; physical output, V^2/V/1 source units",
        frozen_original_mixed_v2_sha256="a285a385d657e226ddcb7a080f86478b627e7406f970bb85b7ffc70a6c42feeb",
        real_background_identity=identities,
        no_new_high_linear_head_slope=True,
        no_outer_high_Dirichlet_constraint=True,
        coordinates='Y=sqrt(r*w^3)(P_sine,K_cosine), physical high IVP',
        nonlinear_claim='Only a declared finite-window conditional probe; no full middle/cut/full-PDE claim')
    def guard():
        rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
        if rss > a.rss_kib:
            raise MemoryError('Observed owned RSS above the declared stop threshold: '+str(rss))
    guard()
    if a.prepare_only:
        save(Path(str(a.out_prefix)+'-prepared.json'),
             dict(status='Prepared only; no new flow or numerical gate executed', config=config))
        return
    global_cols = [[ProjectiveColumn([Fb, arb(0)]),
                    ProjectiveColumn([arb(0), Fb])] for m in modes]
    # forcing_end[mode][density][physical trace0 component]
    forcing_end = [[[arb(0), arb(0)] for d in LABELS] for m in modes]
    source_max = [[[arb(0), arb(0)] for d in LABELS] for m in modes]
    initial_max = [[[arb(0), arb(0)] for input_component in range(2)] for m in modes]
    completed, completed_rows = [], []
    active_origins = [[] for m in modes]
    frozen_origin_integrals = [[] for m in modes]
    causal_rows = []
    running_Vhat = arb(0)
    counts = dict(original_panels=0, taylor=0, root_brackets=0, rejected=0)
    greatest, mean_max = arb(0), arb(0)
    if a.resume:
        old = json.loads(a.resume.read_text())
        if old['config'] != config:
            raise ValueError('Resume is another exact problem or source implementation')
        completed = [tuple(z) for z in old['completed_groups']]
        if completed != order[:len(completed)]:
            raise ValueError('Resume source order is not the true radial order')
        global_cols = [[restore_column(v) for v in row] for row in old['global_columns']]
        forcing_end = [[positive_vec(v) for v in row] for row in old['forcing_end']]
        source_max = [[positive_vec(v) for v in row] for row in old['source_component_max']]
        initial_max = [[positive_vec(v) for v in row] for row in old['initial_component_max']]
        completed_rows, counts = old['completed_rows'], old['counts']
        greatest, mean_max = point(old['greatest_remainder']), point(old['maximum_complete_mean_radius'])
    try:
        for gi, (n, j) in enumerate(order):
            if (n, j) in completed:
                continue
            end_anchor = metadata_without_array(anchors[n, j], 'cell_rows')
            if end_anchor['config'] != flow['config']:
                raise ValueError('A true physical anchor config differs')
            right_radius = ball(end_anchor['radius'])
            if gi == 0:
                left_radius = b
            else:
                prev = metadata_without_array(anchors[order[gi-1]], 'cell_rows')
                left_radius = ball(prev['radius'])
            segment = h.cells[n]['segments'][j]
            segment['physical_inner_radius'] = left_radius
            segment['physical_outer_radius'] = right_radius
            monotone = monotone_parts(segment, a.root_bits)
            local_cols = [initial_pair() for m in modes]
            for k in range(len(modes)):
                active_origins[k].append(initial_pair())
            group_source_max = [[[[arb(0), arb(0)] for ch in LABELS]
                                 for src in range(gi+1)] for m in modes]
            group_initial_max = [[[arb(0), arb(0)] for inc in range(2)] for m in modes]
            group_Vmin, group_Vmax = None, arb(0)
            group_Vhat_before = running_Vhat
            integrals = [[[arb(0), arb(0)] for d in LABELS] for m in modes]
            # Fixed incoming source enclosures; do not overwrite until block end.
            before = [[list(v) for v in row] for row in forcing_end]
            group_rows, previous_right = 0, Fraction(0)
            for original in iter_array(Path(groups[n, j]['path']), 'panels'):
                if original['panel'] != group_rows or original['segment'] != j:
                    raise ValueError('Original true source order differs')
                left, right = Fraction(original['x_left']), Fraction(original['x_right'])
                if left != previous_right or not left < right <= 1:
                    raise ValueError('Original source cover has a gap or overlap')
                previous_right = right
                V, _, _, _ = derivative_density(original, arb(17)/16, arb(1)/16, 92)
                if not V > 0 or not V <= power2(-40):
                    raise ArithmeticError('Exact local V domain failed')
                r, w, rx = (ball(original[k]) for k in ('radius', 'w', 'radius_x'))
                ell = ball(original['log_w_x'])
                if not (r > 0 and w > 0 and rx > 0 and w.upper() <= arb(1)/2):
                    raise ArithmeticError('Actual full source domain failed')
                group_Vmin = V if group_Vmin is None else min(group_Vmin, V)
                group_Vmax = max(group_Vmax, V)
                running_Vhat = max(running_Vhat, V)
                R = (13*V).upper()
                lead = (4*R*R+(arb(5)/4)*R).upper()
                if not R < arb(1)/64 or not lead < 1:
                    raise ArithmeticError('The complete mean/inverse work ball is unpaid')
                mean_max = max_positive(mean_max, R)
                ds = []
                for material_power in MATERIAL_POWERS:
                    vpower = V**material_power if material_power else arb(1)
                    ds.extend([((rx/r)*vpower).upper(), (abs(ell)*vpower).upper()])
                radius = ball(original['radius_left'])
                if group_rows == 0:
                    radius = intersect(radius, left_radius)
                parts = [(max(left, lo), min(right, hi), sign)
                         for lo, hi, sign in monotone if max(left, lo) < min(right, hi)]
                if not parts or parts[0][0] != left or parts[-1][1] != right:
                    raise ArithmeticError('The true root/source common refinement is incomplete')
                for lo, hi, sign in parts:
                    segment['_monotone_sign'] = sign
                    stack = [(lo, hi, 0)]
                    while stack:
                        aa, cc, level = stack.pop()
                        try:
                            args = (h, segment, aa, cc, radius, modes)
                            transitions, next_radius, error, q = (
                                root_physical(*args) if sign == 0 else
                                taylor_physical(*args, a.order, power2(-a.remainder_bits)))
                            partial, rr, ww, F = partial_for_modes(
                                h, segment, aa, cc, radius, original, modes)
                            local_whole = [whole_matrix(cols, T) for cols, T in zip(local_cols, partial)]
                            global_whole = [whole_matrix(cols, T) for cols, T in zip(global_cols, partial)]
                            next_local = [advance_pair(cols, T) for cols, T in zip(local_cols, transitions)]
                            next_global = [advance_pair(cols, T) for cols, T in zip(global_cols, transitions)]
                            origin_whole = [[whole_matrix(cols, partial[k]) for cols in active_origins[k]]
                                            for k in range(len(modes))]
                            next_origins = [[advance_pair(cols, transitions[k]) for cols in active_origins[k]]
                                            for k in range(len(modes))]
                        except (ArithmeticError, ValueError, ZeroDivisionError) as err:
                            if sign == 0 or level >= 40:
                                raise ArithmeticError('Unresolved true middle panel '+str((n,j,group_rows,aa,cc,sign))+': '+str(err)) from err
                            mid = (aa+cc)/2
                            stack.extend([(mid, cc, level+1), (aa, mid, level+1)])
                            counts['rejected'] += 1
                            continue
                        dx = exact_q(cc-aa)
                        denom = (F*V).lower()
                        if not denom > 0:
                            raise ArithmeticError('The true output physical/local divisor lost positivity')
                        for k, m in enumerate(modes):
                            A = local_whole[k]
                            for channel in range(len(LABELS)):
                                for col in range(2):
                                    mass = (abs(A[0][col]).upper()*F.upper()*ds[channel]*dx).upper()
                                    integrals[k][channel][col] = (integrals[k][channel][col]+mass).upper()
                                # A whole current subpanel is charged before taking target sup.
                                image = unit_source_image(A, before[k][channel], integrals[k][channel])
                                for comp in range(2):
                                    source_max[k][channel][comp] = max_positive(
                                        source_max[k][channel][comp], image[comp]/denom)
                            for inc in range(2):
                                for comp in range(2):
                                    initial_max[k][inc][comp] = max_positive(
                                        initial_max[k][inc][comp], abs(global_whole[k][comp][inc])/denom)
                        # Each old source integral is fixed. Only its genuinely signed
                        # two columns are advanced; no positive box is repeatedly transported.
                        for k, m in enumerate(modes):
                            for src in range(gi+1):
                                A_src = origin_whole[k][src]
                                Is = integrals[k] if src == gi else frozen_origin_integrals[k][src]
                                for ch in range(len(LABELS)):
                                    I0, I1 = Is[ch]
                                    for comp in range(2):
                                        mass = (abs(A_src[comp][0]).upper()*I1
                                                +abs(A_src[comp][1]).upper()*I0).upper()
                                        group_source_max[k][src][ch][comp] = max_positive(
                                            group_source_max[k][src][ch][comp], mass/F.lower())
                            for inc in range(2):
                                for comp in range(2):
                                    group_initial_max[k][inc][comp] = max_positive(
                                        group_initial_max[k][inc][comp],
                                        abs(global_whole[k][comp][inc])/F.lower())
                        local_cols, global_cols, radius = next_local, next_global, next_radius
                        active_origins = next_origins
                        counts['root_brackets' if sign == 0 else 'taylor'] += 1
                        greatest = max_positive(greatest, error)
                        guard()
                radius = intersect(radius, ball(original['radius_right']))
                group_rows += 1
                counts['original_panels'] += 1
            if previous_right != 1 or group_rows != groups[n,j]['panels']:
                raise ArithmeticError('The entire original source segment was not consumed')
            radius = intersect(radius, right_radius)
            endpoint_data = []
            for k, m in enumerate(modes):
                A = endpoint_matrix(local_cols[k])
                determinant = A[0][0]*A[1][1]-A[0][1]*A[1][0]
                if not determinant.contains(1):
                    raise ArithmeticError('The true local determinant-one identity failed')
                for channel in range(len(LABELS)):
                    forcing_end[k][channel] = unit_source_image(A, before[k][channel], integrals[k][channel])
                endpoint_data.append(dict(mode=m,
                    local_signed_matrix=[[record(v) for v in row] for row in A],
                    source_integral_uppers=[[upper(v,96) for v in pair] for pair in integrals[k]],
                    exact_determinant_one_intersects=True))
            causal_modes=[]
            for k,m in enumerate(modes):
                source_rows=[]
                for src in range(gi+1):
                    by_power=[]
                    for pi,power in enumerate(MATERIAL_POWERS):
                        comp=[sum((group_source_max[k][src][2*pi+ch][c]
                                  for ch in range(2)),arb(0)).upper() for c in range(2)]
                        by_power.append(dict(V_power=power,
                            P_sup=upper(((1+m)*comp[0]).upper(),96),
                            K_sup=upper(((1+m)*comp[1]).upper(),96),
                            physical_strong_output_row=upper(((1+m)*sum(comp,arb(0))).upper(),96),
                            radial_component_sup=[upper(((1+m)*v).upper(),96)
                                                  for v in group_source_max[k][src][2*pi]],
                            logw_component_sup=[upper(((1+m)*v).upper(),96)
                                                for v in group_source_max[k][src][2*pi+1]]))
                    source_rows.append(dict(source_cell=order[src][0],source_segment=order[src][1],
                                            density_rows=by_power))
                initcols=[sum(v,arb(0)).upper() for v in group_initial_max[k]]
                causal_modes.append(dict(mode=m,source_rows=source_rows,
                    initial_physical_strong_to_physical_strong=upper(max(initcols),96),
                    initial_separate_component_sups=[[upper(v,96) for v in pair]
                                                      for pair in group_initial_max[k]]))
                frozen_origin_integrals[k].append([[v for v in pair] for pair in integrals[k]])
            causal_rows.append(dict(target_cell=n,target_segment=j,
                original_panels=group_rows,V_min=upper(group_Vmin,96),V_max=upper(group_Vmax,96),
                Vhat_before=upper(group_Vhat_before,96),Vhat_after=upper(running_Vhat,96),
                modes=causal_modes,source_order_complete=True,
                physical_output_has_no_V_divisor=True))
            completed.append((n,j))
            completed_rows.append(dict(cell=n, segment=j, original_panels=group_rows,
                                       radius=record(radius), modes=endpoint_data))
            cp = dict(status='Complete true middle IVP source segment', config=config,
                completed_groups=completed, completed_rows=completed_rows,
                causal_block_rows=causal_rows,
                global_columns=[[column_record(v) for v in row] for row in global_cols],
                forcing_end=[[[upper(v,96) for v in pair] for pair in row] for row in forcing_end],
                source_component_max=[[[upper(v,96) for v in pair] for pair in row] for row in source_max],
                initial_component_max=[[[upper(v,96) for v in pair] for pair in row] for row in initial_max],
                greatest_remainder=upper(greatest,96), maximum_complete_mean_radius=upper(mean_max,96),
                counts=counts, elapsed_seconds=time.monotonic()-started,
                peak_RSS_KiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
            dest=Path(str(a.out_prefix)+f'-completed-cell{n:03d}-segment{j}.json')
            if dest.exists():
                raise FileExistsError('Do not overwrite a completed middle segment')
            save(dest,cp)
            print(json.dumps(dict(event='complete_actual_middle_segment',cell=n,segment=j,
                modes=modes,counts=counts,elapsed_seconds=cp['elapsed_seconds'],
                peak_RSS_KiB=cp['peak_RSS_KiB'])),flush=True)
        if completed != order or counts['original_panels'] != 10793:
            raise ArithmeticError('The actual complete two-cell cover is unpaid')
        rows=[]
        for k,m in enumerate(modes):
            component=[sum((source_max[k][ch][c] for ch in range(2)),arb(0)).upper() for c in range(2)]
            gamma=((1+m)*sum(component,arb(0))).upper()
            initial=max(sum(row,arb(0)).upper() for row in initial_max[k])
            mixed_rows=[]
            for pi, power in enumerate(MATERIAL_POWERS):
                by_component=[sum((source_max[k][2*pi+ch][c]
                                   for ch in range(2)), arb(0)).upper()
                              for c in range(2)]
                mixed_rows.append(dict(V_power=power,
                    source_Green_upper=upper(((1+m)*sum(by_component,arb(0))).upper(),96),
                    radial_source_Green_upper=upper(((1+m)*sum(source_max[k][2*pi],arb(0))).upper(),96),
                    log_w_source_Green_upper=upper(((1+m)*sum(source_max[k][2*pi+1],arb(0))).upper(),96),
                    source_units='source-x (s+|ell|) V^'+str(power),
                    output_units='same local-V strong norm; output (1+m) included',
                    constant_strip_only=True))
            rows.append(dict(mode=m,mixed_density_rows=mixed_rows,
                base_source_Green_upper=upper(gamma,96),
                radial_source_Green_upper=upper((1+m)*sum(source_max[k][0],arb(0)),96),
                log_w_source_Green_upper=upper((1+m)*sum(source_max[k][1],arb(0)),96),
                physical_initial_l1_to_field_upper=upper(initial,96)))
        gamma=max(point(row['base_source_Green_upper']) for row in rows)
        B=max(point(row['physical_initial_l1_to_field_upper']) for row in rows)
        band=head['complete_coarse_trace_rows']['head']['high_bands_value_upper']
        initial_head=(ball(band[0]) if max(modes)<=184 else
                      ball(band[1]) if min(modes)>=186 else ball(band[0])+ball(band[1]))
        image=(B*initial_head+216*gamma+52*gamma).upper()
        lip=(52*gamma).upper()
        gates=dict(all18_true_source_segments_complete=True,
            all10793_original_panels_covered=True,
            source_and_output_share_exact_R84_V=True,
            signed_physical_flow_and_determinant_one=True,
            complete_mean_and_quotient_domain_paid=True,
            whole_subpanel_targets_and_source_order_retained=True,
            separate_component_suprema_before_summing=True,
            no_high_DN_or_zero_high_Dirichlet_invented=True)
        result=dict(status='Complete actual finite-middle Volterra majorant; inspect mathematical probe gates',
            config=config,all_enclosure_gates=all(gates.values()),enclosure_gates=gates,
            declared_modes=modes,rows=rows,maximum_base_kernel=upper(gamma,96),
            complete_given_head_lift=upper((B*initial_head).upper(),96),
            fixed_low_window_image_upper=upper(image,96),
            fixed_low_window_lipschitz_upper=upper(lip,96),
            conditional_window_selfmap=bool(image<1),conditional_window_contraction=bool(lip<1),
            true_head_value_source='R78 complete high bands in tau_head > 18/125',
            all_modes94_to8190_computed=(modes==list(range(94,8191,2))),
            mixed_density_powers=[2,1,0],
            causal_block_rows=causal_rows,
            causal_block_output_units='physical strong Wiener, separate component radial sups, constant strip; no local V divisor',
            causal_block_source_units='source-x c*V^p fixed radial Fourier mass separately for each original source segment',
            all_source_origins_signed_until_output=True,
            mixed_density_high_strip_transfer_paid=False,
            mixed_density_full_field_domain_paid=False,
            full_middle_low_high_joint_solution_paid=False,cut_consistency_paid=False,
            full_outer_PDE_or_closed_family_claimed=False,
            counts=counts,input_hashes=hashes,elapsed_seconds=time.monotonic()-started,
            peak_RSS_KiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
        save(Path(str(a.out_prefix)+'.json'),result)
        guard()
        print(json.dumps(dict(event='actual_middle_window_complete',
            enclosure_gates=result['all_enclosure_gates'],
            conditional_selfmap=result['conditional_window_selfmap'],
            conditional_contraction=result['conditional_window_contraction'],
            modes=modes,elapsed_seconds=result['elapsed_seconds'],
            peak_RSS_KiB=result['peak_RSS_KiB'])),flush=True)
    except Exception as err:
        save(Path(str(a.out_prefix)+'-failure.json'),dict(
            status='Incomplete actual middle enclosure; no instability/nonexistence inferred',
            error=repr(err),config=config,completed_groups=completed,counts=counts,
            elapsed_seconds=time.monotonic()-started,
            peak_RSS_KiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss))
        raise

if __name__ == '__main__':
    main()
