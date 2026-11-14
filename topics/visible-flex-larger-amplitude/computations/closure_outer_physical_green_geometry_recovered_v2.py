#!/usr/bin/env python3
"""Recovered v2: all46 actual outer physical Green geometry.

This is a NEW reconstruction after the executor loss, not the unexecuted
local prepared file with an unknown final SHA. The mathematical inputs
are the published R87 true low46 flow and R84/R79 real source records.
The true metric, head columns, complete mean, and source positions stay
fixed. Output is geometry and nine explicit source densities, NOT a
claim that the whole nonlinear outer problem has been solved.

Working profiles are chunked gzip files. They are reproducible derived
data; the small complete primary/checkpoints record every hash.
Author: exact_closure, GPT-6 Astra Pro (AI-assisted), 2026-11-12.
"""
import argparse
from fractions import Fraction
import gzip
import json
from pathlib import Path
import resource
import struct
import tempfile
import time
import zlib

from flint import arb, ctx

from closure_outer_physical_trace_flow import (
    EXPECTED as PHYSICAL_EXPECTED, taylor_physical, root_physical,
    balanced_majorant)
from closure_outer_whole_field_profiles import derivative_density, scaled
from closure_outer_taylor_shared_flow import raw_source_identity
from closure_outer_two_cell_adjoint import compact_endpoint
from closure_projective_interval_column import ProjectiveColumn
from closure_real_head_source_enclosure import exact_q, power2
from closure_real_linear_head_enclosure import PositiveKernels
from closure_split_joint_io_v2 import (
    digest, read_field, iter_array, metadata_without_array)
from closure_taylor_cut_slope_v2 import (
    ball, record, intersect, rough_radius, monotone_parts,
    column_record, restore_column, add_error, save)
from tail_r33_middle_ordered_physical import SourceValues

MODES = list(range(2, 93, 2))
EXPECTED = dict(PHYSICAL_EXPECTED)
EXPECTED.update({
    'closure_outer_physical_trace_flow.py':
        'd919902557b3c5c17e6e68602ba86f3b3852207057c3a2ea1468b08ecae4cc5e',
    'closure_outer_whole_field_profiles.py':
        '88552242e5ace583f51093b3bd35dbb491f1eed1546a9d79437ec73e5b4c24d9',
    'closure_outer_two_cell_adjoint.py':
        '184667ec3f78b9d99d2a5fe28465c243ecee0e6ba4d4685199e72bd9bef0899a',
    'closure_split_joint_io_v2.py':
        '6cbcb8cf69a39d8df5d10be35a29b941b47fd66456364eb90fab7bbb22b386f0',
})
INPUT_SHA = {
    'ready': '563a99973230a7f15d1c1ba8537edae34bc02158a0cfff90160d37f57e3ab2f6',
    'physical_flow': 'd1078b0bd4795f99aaa87c32efe7577f6aef52e8909b8ac1460f058d39b317f3',
    'physical_manifest': 'c688c1a4412aa9ff55f8ce4d636cdca9adcb8eec65af16540dd8376e977ad6ed',
    'source11': 'f3d06071519f674de420a7fd66de45d14a8274bfb2089bd045bf0bfb2763cf83',
    'source10': 'bf4061ba1ca5295245165099d274b637630d16418a9e5283dd58898fb184e0c9',
    'response': '528fd51921f7cad71445d76669b44e60279c0fc31cddf9041f8ea5b1f7477962',
    'family': '17b1d776cdce044722db61c2981d64838d18fd66c6ef3fdd4c48fa183a9a3776',
}
# The family summary hash is checked through the supplied R74 primary
# ledger as well; a later textual summary reserialization must be made
# explicit with --family-sha256, never silently accepted.
DENSITIES = [
    dict(name='strong_local_rho_1_16', source_norm='W_tau_1',
         output_angular_factor=False, output_envelope='local_V'),
    dict(name='strong_local_rho_16', source_norm='W_tau_1',
         output_angular_factor=False, output_envelope='local_V'),
    dict(name='strong_candidate_cap', source_norm='W_tau_1',
         output_angular_factor=False, output_envelope='local_V'),
    dict(name='weak_local_rho_1_16', source_norm='W_tau_0',
         output_angular_factor=True, output_envelope='local_V'),
    dict(name='weak_local_rho_16', source_norm='W_tau_0',
         output_angular_factor=True, output_envelope='local_V'),
    dict(name='weak_candidate_cap', source_norm='W_tau_0',
         output_angular_factor=True, output_envelope='local_V'),
    dict(name='weak_uniform_rho_1_16', source_norm='W_tau_0',
         output_angular_factor=True, output_envelope='uniform_V0'),
    dict(name='weak_uniform_rho_1', source_norm='W_tau_0',
         output_angular_factor=True, output_envelope='uniform_V0'),
    dict(name='weak_uniform_rho_16', source_norm='W_tau_0',
         output_angular_factor=True, output_envelope='uniform_V0'),
]


def upper(x, bits=64):
    if not x.is_finite() or x.lower() < 0:
        raise ArithmeticError('A positive geometry bound must be finite and nonnegative')
    return compact_endpoint(x.upper(), 1, bits)


def point(d):
    return arb((int(d[0]), int(d[1])))


def compact(x, bits=80):
    if not x.is_finite():
        raise ArithmeticError('A nonfinite signed enclosure is not serializable')
    return [compact_endpoint(x.lower(), -1, bits),
            compact_endpoint(x.upper(), 1, bits)]


def expand(d):
    return point(d[0]).union(point(d[1]))


def inverse_one(T):
    # The exact matrix is a trace-zero flow, hence det(T_exact)=1.
    return [[T[1][1], -T[0][1]], [-T[1][0], T[0][0]]]


def matrix_record(T):
    return [[record(v) for v in row] for row in T]


def matrix_ball(T):
    return [[ball(v) for v in row] for row in T]


def whole_column(column, T):
    unit = column.unit()
    return [scaled(column, sum((T[i][j]*unit[j] for j in range(2)), arb(0)))
            for i in range(2)]


def partial_flow(h, segment, left, right, radius, original):
    """One box enclosing EVERY subinterval transfer inside this panel.

The first integral lies in the hull of zero and the full-length
coefficient interval. In a fixed balanced l1 norm the terms of degree
>=2 are bounded by q^2/(1-q). Exact determinant one gives the backward
box without division by an independently rounded determinant.
"""
    rr, unused = rough_radius(h, segment, left, right, radius)
    rr = intersect(rr, ball(original['radius']))
    xx = exact_q(left).union(exact_q(right))
    src = h.source_point(segment, xx)
    w = intersect(src['w'], ball(original['w']))
    ell = intersect(src['log_w_x'], ball(original['log_w_x']))
    E = 1+w*w
    rx = abs(w*ell)/(8*E*E.sqrt())+h.alpha*src['ro_x']/E
    rx = intersect(rx, ball(original['radius_x']))
    if not rr > 0 or not w > 0 or not rx > 0:
        raise ArithmeticError('A real positive source range was lost')
    span = exact_q(right-left)
    s, ell = span*rx/rr, span*ell
    d = (ell-s)/2
    B, q, unused = balanced_majorant(d, s, ell, 92)
    err = (q*q/(1-q)).upper()
    rem = [[err, (err/B).upper()], [(err*B).upper(), err]]
    result = []
    for m in MODES:
        M = [[d, -m*s], [-m*ell, -d]]
        result.append([
            [add_error(arb(1 if i == j else 0)+arb(0).union(M[i][j]),
                       rem[i][j]) for j in range(2)] for i in range(2)])
    return result, rr, w, (rr*w*w*w).sqrt()


def weak_density(g, V, sigma, rho, direction):
    """Complete weak source derivative W_tau,1 -> W_tau,0.

P,K are nonmean and |m|>=2. Thus ||P||0+||K||0<=R/3,
||K_theta-P||0,||K+P_theta||0<=R, and
Q=E*s*U^2+ell*(E*(K+P_theta)^2-w^2*(K^2+P^2)).
The full scalar mean root and full Wiener inverse are retained.
"""
    w, r, rx = (ball(g[k]) for k in ('w', 'radius', 'radius_x'))
    if not (w > 0 and r > 0 and rx > 0 and w.upper() <= arb(1)/2):
        raise ArithmeticError('The complete weak real source domain is unpaid')
    E = (1+w*w).upper()
    s, ell = (rx/r).upper(), abs(ball(g['log_w_x'])).upper()
    R = (sigma*V+rho*direction).upper()
    if not R < arb(1)/64:
        raise ArithmeticError('The complete weak mean domain is unpaid')
    c, dc = 4*R*R, 16*R*direction
    lead, dlead = c+E*R, dc+E*direction
    if not lead < 1:
        raise ArithmeticError('The full weak Wiener inverse is unpaid')
    A = E*s+(E+w*w/9)*ell
    Q, dQ = A*R*R, 2*A*R*direction
    mean = ell*(2*c*E*R+c*c)
    dmean = 2*ell*(dc*(E*R+c)+c*E*direction)
    cap = ((Q+mean)/(1-lead)).upper()
    derivative = ((dQ+dmean)/(1-lead)
                  +(Q+mean)*dlead/(1-lead)**2).upper()
    return derivative, cap, R, lead.upper()


def all_densities(g, sigma, V0):
    V, oldsmall, r1, l1 = derivative_density(g, sigma, arb(1)/16, 92)
    Vcheck, oldlarge, r2, l2 = derivative_density(g, sigma, arb(16), 92)
    if not V == Vcheck or not V > 0 or not V <= V0:
        raise ArithmeticError('The exact local/uniform physical norm identity failed')
    # Old complete candidate source cap, using the original strong bounds.
    w, r, rx = (ball(g[k]) for k in ('w', 'radius', 'radius_x'))
    E, s, ell = (1+w*w).upper(), (rx/r).upper(), abs(ball(g['log_w_x'])).upper()
    R, T, U = sigma*V, 40*sigma*V, 41*sigma*V
    c = 4*R*R
    lead = c+R+E*T
    if not R < arb(1)/64 or not lead < 1:
        raise ArithmeticError('The old candidate cap domain failed')
    q = E*s*U*U+E*ell*(R+T)**2
    mn = ell*(2*c*(R+E*T)+c*c)
    oldcap = ((q+mn)/(1-lead)).upper()
    ws = weak_density(g, V, sigma, arb(1)/16, V)
    wl = weak_density(g, V, sigma, arb(16), V)
    wc = weak_density(g, V, sigma, arb(0), V)
    uniforms = [weak_density(g, V, sigma, rho, V0)
                for rho in (arb(1)/16, arb(1), arb(16))]
    values = [oldsmall, oldlarge, oldcap, ws[0], wl[0], wc[1]]
    values.extend(z[0] for z in uniforms)
    mr = max([r1, r2, R, ws[2], wl[2], wc[2]]+[z[2] for z in uniforms])
    ml = max([l1, l2, lead, ws[3], wl[3], wc[3]]+[z[3] for z in uniforms])
    return V, [upper(v) for v in values], mr.upper(), ml.upper()


class ChunkWriter:
    def __init__(self, stem, cell, segment, limit):
        self.stem, self.cell, self.segment, self.limit = stem, cell, segment, limit
        self.handle = None
        self.count, self.number, self.total = 0, 0, 0
        self.chunks = []

    def open(self):
        path = Path(str(self.stem)+f'-cell{self.cell:03d}-segment{self.segment}'
                    +f'-geometry{self.number:03d}.json.gz')
        partial = Path(str(path)+'.partial')
        if path.exists() or partial.exists():
            raise FileExistsError('Use fresh reconstructed profile chunk names')
        self.path, self.partial = path, partial
        self.handle = gzip.open(partial, 'wt', compresslevel=9)
        header = dict(cell=self.cell, segment=self.segment, chunk=self.number,
                      reverse_radial_order=True,
                      mode_fields=['mode', 'phi_P_over_V', 'phi_K_over_V',
                                   'chi_P_over_V', 'chi_K_over_V', 'A_phi', 'A_chi'])
        self.handle.write(json.dumps(header, separators=(',', ':'))[:-1]+',"panels":[\n')
        self.count = 0

    def add(self, row):
        if self.handle is None:
            self.open()
        if self.count:
            self.handle.write(',\n')
        self.handle.write(json.dumps(row, separators=(',', ':')))
        self.count += 1
        self.total += 1
        if self.count >= self.limit:
            self.close()

    def close(self):
        if self.handle is None:
            return
        self.handle.write('\n]}\n')
        self.handle.close()
        self.handle = None
        if self.partial.stat().st_size > 5*1024*1024:
            raise ArithmeticError('A derived gzip chunk exceeds 5 MiB')
        self.partial.rename(self.path)
        self.chunks.append(dict(path=str(self.path), sha256=digest(self.path),
                                bytes=self.path.stat().st_size, subpanels=self.count))
        self.number += 1


def main():
    p = argparse.ArgumentParser(description=__doc__)
    for k in ('ready', 'physical-flow', 'physical-manifest', 'source11',
              'source10', 'response', 'family', 'out-prefix', 'work-dir'):
        p.add_argument('--'+k, type=Path, required=True)
    p.add_argument('--family-sha256', default=INPUT_SHA['family'])
    p.add_argument('--precision', type=int, default=256)
    p.add_argument('--order', type=int, default=24)
    p.add_argument('--root-bits', type=int, default=160)
    p.add_argument('--remainder-bits', type=int, default=100)
    p.add_argument('--rss-kib', type=int, default=40960)
    p.add_argument('--chunk-rows', type=int, default=128)
    p.add_argument('--resume', type=Path)
    p.add_argument('--prepare-only', action='store_true')
    a = p.parse_args()
    began = time.monotonic()
    if (a.precision < a.root_bits+32 or a.order < 24
            or a.root_bits < 160 or a.remainder_bits < 100
            or not 1 <= a.chunk_rows <= 128):
        raise ValueError('Retain the original certified arithmetic and bounded chunks')
    a.out_prefix.parent.mkdir(parents=True, exist_ok=True)
    a.work_dir.mkdir(parents=True, exist_ok=True)
    for suffix in ('.json', '-failure.json'):
        if Path(str(a.out_prefix)+suffix).exists():
            raise FileExistsError('A complete or failed reconstruction must not be overwritten')
    ctx.prec, ctx.cap, ctx.threads = a.precision, a.order+2, 1
    for name, expected in EXPECTED.items():
        if digest(Path(__file__).with_name(name)) != expected:
            raise ValueError('A frozen mathematical implementation changed: '+name)
    hashes = {}
    for key, expected in INPUT_SHA.items():
        path = getattr(a, key)
        value = digest(path)
        wanted = a.family_sha256 if key == 'family' else expected
        if value != wanted:
            raise ValueError('An explicit frozen input identity changed: '+key)
        hashes[str(path)] = value
    flow = json.loads(a.physical_flow.read_text())
    manifest = json.loads(a.physical_manifest.read_text())
    family = json.loads(a.family.read_text())
    if (not flow['all_gates'] or not all(flow['gates'].values())
            or flow['config']['modes'] != MODES
            or not manifest['all9_gates'] or manifest['true_height_charts_paid'] != 92
            or not family['all_gates'] or not all(family['gates'].values())):
        raise ValueError('Full R87 and R74 certificates are required')
    known = {r['path']: r['sha256'] for r in manifest['files']}
    if known.get(str(a.physical_flow)) != hashes[str(a.physical_flow)]:
        raise ValueError('The full physical primary is not its registered R87 object')
    if flow['input_hashes'].get(str(a.ready)) != hashes[str(a.ready)]:
        raise ValueError('The actual physical flow uses another true metric')
    source_docs = {11: json.loads(a.source11.read_text()),
                   10: json.loads(a.source10.read_text())}
    for n, d in source_docs.items():
        if (d['cell'] != n or not d['all_gates'] or not all(d['gates'].values())
                or d['tau'] != '1/64' or d['original_candidate_modes'] != list(range(2, 41, 2))
                or d['input_hashes'].get(str(a.response)) != hashes[str(a.response)]
                or d['input_hashes'].get(str(a.ready)) != hashes[str(a.ready)]):
            raise ValueError('The unchanged complete M20 candidate source identity failed')
    if not source_docs[10]['same_exact_candidate']:
        raise ValueError('The refined five moments must enclose the same candidate')
    forward_order = [(n, j) for n in (11, 10) for j in range(9)]
    reverse_order = list(reversed(forward_order))
    groups = {(n, g['segment']): g for n, d in source_docs.items() for g in d['groups']}
    if sorted(groups) != sorted(forward_order):
        raise ValueError('All original 18 source segments are required')
    for g in groups.values():
        if digest(Path(g['path'])) != g['sha256']:
            raise ValueError('A complete true source group changed')
        hashes[g['path']] = g['sha256']
    stem = str(a.physical_flow)[:-5]
    anchor_paths = {}
    for key in forward_order:
        n, j = key
        path = Path(stem+f'-completed-cell{n:03d}-segment{j}.json')
        value = digest(path)
        if known.get(str(path)) != value:
            raise ValueError('An actual R87 anchor changed')
        hashes[str(path)] = value
        anchor_paths[key] = path
    raw = read_field(a.response, 'checkpoint')['rawStates']
    if len(raw) != 13 or any(len(row) != 40 for row in raw):
        raise ValueError('Retain all original 20 modes and 13 physical nodes')
    axes = {r['mode']: r for r in family['parameter_axes']}
    if sorted(axes) != list(range(2, 41, 2)):
        raise ValueError('Retain all 20 original independent parameter axes')
    for m in axes:
        q = exact_q(Fraction.from_float(raw[12][m//2-1]))
        if not q == ball(axes[m]['exact_centre']):
            raise ValueError('The R74 family and actual complete height centre differ')
    Qout = {m: exact_q(Fraction.from_float(raw[10][m//2-1]))
            if m <= 40 else arb(0) for m in MODES}
    del raw
    ready = dict(rationalDeepModel=read_field(a.ready, 'rationalDeepModel'),
                 shallowSourceParameters=read_field(a.ready, 'shallowSourceParameters'))
    identities = [raw_source_identity(ready, n) for n in (11, 10)]
    h = SourceValues(ready)
    del ready
    positive = PositiveKernels(h, 12, 4)
    h.cells.update({n: positive.source_cell(n) for n in (11, 10)})
    b, wb = (ball(flow['config'][k]) for k in ('true_cut_radius', 'true_cut_w'))
    mu = ball(flow['config']['global_mu11'])
    Fb = (b*wb*wb*wb).sqrt()
    terminal = next(c for c in flow['cell_rows'] if c['cell'] == 10)
    R, wR = ball(terminal['radius']), ball(terminal['w'])
    terminal_rows = {r['mode']: r for r in terminal['modes']}
    W, S0, expected_chi_b = {}, {}, {}
    for m in MODES:
        row = terminal_rows[m]
        if not row['height_chart_excludes_zero']:
            raise ArithmeticError('The true low-mode chart is unpaid')
        col = restore_column(row['columns'][0])
        W[m] = col.values()[0]
        S0[m] = ball(row['S0_true_Q'])
        if W[m].contains(0) or S0[m].contains(0):
            raise ArithmeticError('The actual global Wronskian contains zero')
        matrix = [[ball(z) for z in r] for r in row['trace0_physical_fundamental_matrix']]
        expected_chi_b[m] = [-matrix[0][1], matrix[0][0]]
    sigma, V0 = arb(17)/16, power2(-40)
    config = dict(
        reconstruction='NEW recovered_v2; no byte-identity claim for lost prepared file',
        modes=MODES, cells=[11, 10], source_tau='1/64',
        precision=a.precision, order=a.order, root_bits=a.root_bits,
        remainder_bits=a.remainder_bits, chunk_rows=a.chunk_rows,
        parameter_sigma='17/16', uniform_envelope=[1, -40],
        actual_true_cut_radius=record(b), actual_true_cut_w=record(wb),
        global_mu11=record(mu), outer_radius=record(R), outer_w=record(wR),
        true_physical_Wronskians={str(m): record(W[m]) for m in MODES},
        actual_true_S0_Q={str(m): record(S0[m]) for m in MODES},
        actual_outer_Q={str(m): record(Qout[m]) for m in MODES},
        parameter_axes=family['parameter_axes'],
        source_hashes=EXPECTED, input_hashes=hashes,
        entrypoint_sha256=digest(__file__),
        densities=DENSITIES,
        physical_state='Y=sqrt(r*w^3)*(P_sine,K_cosine), exact trace zero',
        physical_source='N enters K_x, hence Y_2 source is sqrt(r*w^3)*N, no extra r_x',
        norm='sum of componentwise radial suprema, Fourier weight (1+|m|)*exp(|m|/64)',
        local_envelope='exact same upward80bit sqrt(original_complete_mean_bound/4) as R84',
        weak_output_requires_one_plus_mode=True,
        uniform_output_requires_local_V_over_V0=True,
        profiles_are_regenerable_derived_working_data=True)
    if a.prepare_only:
        plan = dict(status='Prepared only; no Green or density numerical gate claimed',
                    config=config, source_identity=identities,
                    whole_problem_complete=False, all_numeric_gates_executed=False)
        save(Path(str(a.out_prefix)+'-prepared.json'), plan)
        print(json.dumps(dict(event='physical46_green_prepared', all_numeric_gates_executed=False)), flush=True)
        return
    counts = dict(original_material=0, taylor=0, root_brackets=0, rejected=0)
    completed, profile_groups = [], []
    chi = [ProjectiveColumn([arb(0), arb(1)]) for m in MODES]
    max_remainder, max_mean, max_leading = arb(0), arb(0), arb(0)
    if a.resume:
        previous = json.loads(a.resume.read_text())
        if previous['config'] != config:
            raise ValueError('Recovery config differs from this same exact calculation')
        completed = [tuple(x) for x in previous['completed_groups']]
        if completed != reverse_order[:len(completed)]:
            raise ValueError('Recovery order is not the true reverse radial order')
        profile_groups, counts = previous['profile_groups'], previous['counts']
        chi = [restore_column(x) for x in previous['chi_at_left']]
        max_remainder = ball(previous['greatest_balanced_Taylor_remainder'])
        max_mean = ball(previous['maximum_mean_input_radius'])
        max_leading = ball(previous['maximum_leading_norm'])
        for g in profile_groups:
            for c in g['chunks']:
                if digest(Path(c['path'])) != c['sha256']:
                    raise ValueError('A complete recovered working chunk changed')
    def guard():
        peak = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
        if peak > a.rss_kib:
            raise MemoryError('Observed owned RSS exceeded the declared stop threshold: '+str(peak))
    def anchor(index):
        if index == 0:
            cols = []
            for m in MODES:
                slope = ball(flow['config']['actual_true_initial_slopes'][str(m)])
                P = -m*b**3/wb
                K = m*m*b**3/wb+h.sqrt12*mu*slope/(b**4*wb*wb)
                cols.append(ProjectiveColumn([Fb*P, Fb*K]))
            return cols, b
        key = forward_order[index-1]
        cp = metadata_without_array(anchor_paths[key], 'cell_rows')
        if cp['config'] != flow['config']:
            raise ValueError('A true physical anchor has another exact source')
        return [restore_column(row[0]) for row in cp['columns']], ball(cp['radius'])
    current_writer = None
    try:
        for n, j in reverse_order:
            if (n, j) in completed:
                continue
            gi = forward_order.index((n, j))
            phi, left_radius = anchor(gi)
            expected_phi, right_radius = anchor(gi+1)
            segment = h.cells[n]['segments'][j]
            segment['physical_inner_radius'] = left_radius
            segment['physical_outer_radius'] = right_radius
            monotone = monotone_parts(segment, a.root_bits)
            group = groups[n, j]
            source_path = Path(group['path'])
            original_count, subcount, previous_right = 0, 0, Fraction(0)
            with tempfile.TemporaryFile(mode='w+b', dir=a.work_dir) as spool:
                offsets = []
                for original in iter_array(source_path, 'panels'):
                    if original['panel'] != original_count or original['segment'] != j:
                        raise ValueError('Original true source positions changed')
                    left, right = Fraction(original['x_left']), Fraction(original['x_right'])
                    if left != previous_right or not left < right <= 1:
                        raise ValueError('Original material cover has a gap or overlap')
                    previous_right = right
                    V, densities, mr, ml = all_densities(original, sigma, V0)
                    max_mean, max_leading = max(max_mean, mr), max(max_leading, ml)
                    radius = ball(original['radius_left'])
                    if original_count == 0:
                        intersect(radius, left_radius)
                    parts = [(max(left, lo), min(right, hi), sign)
                             for lo, hi, sign in monotone if max(left, lo) < min(right, hi)]
                    if not parts or parts[0][0] != left or parts[-1][1] != right:
                        raise ArithmeticError('The source/root common refinement has a gap')
                    subindex = 0
                    for lo, hi, sign in parts:
                        segment['_monotone_sign'] = sign
                        stack = [(lo, hi, 0)]
                        while stack:
                            aa, cc, depth = stack.pop()
                            try:
                                args = (h, segment, aa, cc, radius, MODES)
                                T, next_radius, error, q = (
                                    root_physical(*args) if sign == 0 else
                                    taylor_physical(*args, a.order, power2(-a.remainder_bits)))
                                partial, rr, ww, F = partial_flow(
                                    h, segment, aa, cc, radius, original)
                                whole_phi, advanced = [], []
                                for k in range(len(MODES)):
                                    whole_phi.append(whole_column(phi[k], partial[k]))
                                    trial = restore_column(column_record(phi[k]))
                                    trial.advance(T[k])
                                    advanced.append(trial)
                            except (ArithmeticError, ValueError, ZeroDivisionError) as error0:
                                if sign == 0 or depth >= 40:
                                    raise ArithmeticError('Unresolved actual physical Green panel '+
                                        str((n, j, original_count, aa, cc, sign))+': '+str(error0)) from error0
                                mid = (aa+cc)/2
                                stack.extend([(mid, cc, depth+1), (aa, mid, depth+1)])
                                counts['rejected'] += 1
                                continue
                            payload = dict(
                                panel=original_count, subpanel=subindex,
                                x_left=str(aa), x_right=str(cc),
                                V=upper(V, 80), densities=densities,
                                F=record(F), partial=[matrix_record(t) for t in partial],
                                full=[matrix_record(t) for t in T],
                                phi=[[record(v) for v in vec] for vec in whole_phi])
                            packed = zlib.compress(json.dumps(payload, separators=(',', ':')).encode(), 1)
                            offsets.append(spool.tell())
                            spool.write(struct.pack('<I', len(packed)))
                            spool.write(packed)
                            phi, radius = advanced, next_radius
                            counts['root_brackets' if sign == 0 else 'taylor'] += 1
                            if sign:
                                max_remainder = max(max_remainder, error)
                            subindex += 1
                            subcount += 1
                            guard()
                    intersect(radius, ball(original['radius_right']))
                    original_count += 1
                    counts['original_material'] += 1
                if original_count != group['panels'] or previous_right != 1:
                    raise ValueError('A full true source segment was not processed')
                for k in range(len(MODES)):
                    for z in range(2):
                        intersect(phi[k].values()[z], expected_phi[k].values()[z])
                current_writer = ChunkWriter(
                    a.work_dir/a.out_prefix.name, n, j, a.chunk_rows)
                for offset in reversed(offsets):
                    spool.seek(offset)
                    length = struct.unpack('<I', spool.read(4))[0]
                    part = json.loads(zlib.decompress(spool.read(length)))
                    F, V = ball(part['F']), point(part['V'])
                    dx = exact_q(Fraction(part['x_right'])-Fraction(part['x_left']))
                    modes_row = []
                    for k, m in enumerate(MODES):
                        partial = matrix_ball(part['partial'][k])
                        whole_chi = whole_column(chi[k], inverse_one(partial))
                        whole_phi = [ball(v) for v in part['phi'][k]]
                        intersect(whole_phi[0]*whole_chi[1]-whole_phi[1]*whole_chi[0], W[m])
                        geometry = [upper((abs(v).upper()/F/V).upper())
                                    for vec in (whole_phi, whole_chi) for v in vec]
                        Aphi = upper((abs(whole_phi[0]).upper()*F.upper()*dx).upper())
                        Achi = upper((abs(whole_chi[0]).upper()*F.upper()*dx).upper())
                        modes_row.append([m]+geometry+[Aphi, Achi])
                        advanced_chi = restore_column(column_record(chi[k]))
                        advanced_chi.advance(inverse_one(matrix_ball(part['full'][k])))
                        chi[k] = advanced_chi
                    current_writer.add(dict(
                        panel=part['panel'], subpanel=part['subpanel'],
                        x_left=part['x_left'], x_right=part['x_right'],
                        local_V=part['V'], densities=part['densities'],
                        modes=modes_row))
                    guard()
                current_writer.close()
                profile_groups.append(dict(
                    cell=n, segment=j, original_panels=original_count, subpanels=subcount,
                    source_group_path=str(source_path), source_group_sha256=group['sha256'],
                    forward_anchor_intersects=True, pointwise_Wronskians_intersect=True,
                    chunks=current_writer.chunks))
                current_writer = None
            completed.append((n, j))
            cp = dict(
                status='Complete recovered true physical Green segment',
                config=config, completed_groups=completed, profile_groups=profile_groups,
                counts=counts, chi_at_left=[column_record(c) for c in chi],
                greatest_balanced_Taylor_remainder=record(max_remainder),
                maximum_mean_input_radius=record(max_mean), maximum_leading_norm=record(max_leading),
                elapsed_seconds=time.monotonic()-began,
                peak_RSS_KiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
            path = Path(str(a.out_prefix)+f'-completed-cell{n:03d}-segment{j}.json')
            if path.exists():
                raise FileExistsError('A complete geometry checkpoint would be overwritten')
            save(path, cp)
            print(json.dumps(dict(
                event='physical46_whole_field_group_complete', cell=n, segment=j,
                original_panels=original_count, subpanels=subcount,
                completed_groups=len(completed), elapsed_seconds=cp['elapsed_seconds'],
                peak_RSS_KiB=cp['peak_RSS_KiB'])), flush=True)
        if completed != reverse_order or counts['original_material'] != 10793:
            raise ValueError('The full18/10793 real source range is incomplete')
        for k, m in enumerate(MODES):
            for z in range(2):
                intersect(chi[k].values()[z], expected_chi_b[m][z])
        gates = dict(
            same_real_metric_full_source_and_all20_outer_heights=True,
            true_low46_head_slopes_no_finite_Robin_replacement=True,
            all18_segments_and10793_material_panels=True,
            signed_common_amplitudes_and_all46_Wronskians=True,
            both_physical_components_on_every_subinterval=True,
            exact_partial_inverse_and_all_Taylor_root_remainders=True,
            every_forward_anchor_and_final_backward_matrix_agree=True,
            complete_mean_and_pointwise_Wiener_inverse_all_nine_densities=True,
            weak_source_requires_one_angular_output_weight=True,
            uniform_norm_has_explicit_input_and_output_conversion=True)
        result = dict(
            status='Complete actual low46 whole-field geometry; ordered norm consumer required',
            config=config, all_gates=True, gates=gates, counts=counts,
            completed_groups=completed, profile_groups=profile_groups,
            chi_at_true_cut={str(m): [record(v) for v in chi[k].values()]
                             for k, m in enumerate(MODES)},
            source_identity=identities, input_hashes=hashes,
            greatest_balanced_Taylor_remainder=record(max_remainder),
            maximum_mean_input_radius=record(max_mean), maximum_leading_norm=record(max_leading),
            Green_formula='x<=r: chi(r)*phi1(x)*F(x)/W; x>r: phi(r)*chi1(x)*F(x)/W',
            all20_affine_outer_height_lift_retained=True,
            complete_outer_PDE_or_full_frequency_contraction_claimed=False,
            ordered_Green_norms_not_yet_consumed=True,
            derived_working_chunks_may_be_regenerated=True,
            elapsed_seconds=time.monotonic()-began,
            peak_RSS_KiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
        save(Path(str(a.out_prefix)+'.json'), result)
        guard()
        print(json.dumps(dict(event='physical46_whole_field_complete', all_gates=True,
            counts=counts, elapsed_seconds=result['elapsed_seconds'],
            peak_RSS_KiB=result['peak_RSS_KiB'])), flush=True)
    except Exception as error:
        if current_writer is not None and current_writer.handle is not None:
            current_writer.handle.close()
        save(Path(str(a.out_prefix)+'-failure.json'), dict(
            status='Incomplete reconstructed actual low46 geometry; no mathematical impossibility inferred',
            error=repr(error), config=config, completed_groups=completed,
            profile_groups=profile_groups, counts=counts,
            chi_at_left=[column_record(c) for c in chi],
            elapsed_seconds=time.monotonic()-began,
            peak_RSS_KiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss))
        raise


if __name__ == '__main__':
    main()
