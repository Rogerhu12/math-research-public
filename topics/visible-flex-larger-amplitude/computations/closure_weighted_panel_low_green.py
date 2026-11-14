#!/usr/bin/env python3
"""Position-preserving real low Green caps on the R33 continuous strip.

All modal boundary conditions and the real background are unchanged.  The
new material panels are only used to enclose the same signed fundamental
columns, their pointwise physical weights, and ordered source integrals.
The output is a reusable Green ledger, not an invariant-box assertion.
Author: exact_closure (GPT-6 Astra Pro, AI-assisted), 2026-11-12.
"""
import argparse
import copy
from fractions import Fraction as Q
import gc
import gzip
import hashlib
import json
from pathlib import Path
import resource
import time

from flint import arb, ctx
from closure_real_head_source_enclosure import RealHead, exact_q, power2, ball_record
from closure_real_linear_head_enclosure import PositiveKernels, ideal_slope, peano_matrix, interval
from closure_real_head_green_enclosure import (load_json, ball, endpoint, mat, mv,
    inverse_unimodular, maximum, ceil_log2_upper)
from closure_projective_interval_column import ProjectiveColumn


def sha(raw): return hashlib.sha256(raw).hexdigest()


def upper(x): return abs(x).upper()


def small_record(x):
    r = ball_record(x)
    return {k: r[k] for k in ('lower', 'upper')}


def positive_min(a, b): return min(a.upper(), b.upper())


def seed_columns(data, selected, rc, rho, refined):
    """Keep the common projective amplitude in each independent cell seed."""
    all_seeds = {}
    group_hashes = {}
    for gr in data['column_groups']:
        path = Path(gr['path']); group, raw = load_json(path)
        if sha(raw) != gr['sha256']:
            raise ValueError('A true signed column group changed')
        group_hashes[str(path)] = sha(raw)
        rows = group['cell_rows']; by_cell = {r['cell']: r for r in rows}
        for j, m in enumerate(group['modes']):
            u = m*m-4; nu = arb(m*m*(m*m-1))/12
            gain = group['endpoint_rows'][j]['Q_gain']
            lo = endpoint(gain['lower']); hi = endpoint(gain['upper'])
            if not (lo > 0 or hi < 0):
                raise ArithmeticError('The true height chart contains zero')
            gain_lower = lo if lo > 0 else -hi
            rfar = ball(rows[-1]['r_inner']); scale = (rfar/rc)**u
            slope = ideal_slope(m, rho) + interval(-nu*power2(-60), nu*power2(-60))
            phi = ProjectiveColumn([1/scale, scale*slope])
            seeds = {}
            for n in range(224, min(selected)-1, -1):
                if n < 224: phi.multiply_component(1, 1/rho)
                lin = by_cell[n]['linear_rows'][j]
                if n in selected:
                    q = ball(lin['column_Q_sup']).upper()/gain_lower
                    xi = ball(lin['column_Xi_sup']).upper()/gain_lower
                    old = refined.get((m, n))
                    if old:
                        q = positive_min(q, ball(old['refined_phi_Q_sup']))
                        xi = positive_min(xi, ball(old['refined_phi_Xi_sup']))
                    seeds[n] = dict(phi=copy.copy(phi), phi_caps=(q, xi))
                if n > min(selected): phi.advance(mat(lin['gauge_matrix']))
            psi = ProjectiveColumn([arb(0), (ball(rows[0]['r_outer'])/rc)**u])
            for n in range(12, max(selected)+1):
                if n > 12: psi.multiply_component(1, rho)
                lin = by_cell[n]['linear_rows'][j]
                if n in selected:
                    r = ball(by_cell[n]['r_inner']).union(ball(by_cell[n]['r_outer']))
                    within = mv(mat(lin['gauge_backward_majorant']), psi.absolute_uppers())
                    q = upper((r/rc)**u)*within[0]
                    xi = upper((rc/r)**u)*within[1]
                    old = refined.get((m, n))
                    if old:
                        q = positive_min(q, ball(old['refined_psi_Q_sup']))
                        xi = positive_min(xi, ball(old['refined_psi_Xi_sup']))
                    seeds[n].update(psi=copy.copy(psi), psi_caps=(q, xi),
                        mu=ball(by_cell[n]['mu']), mu_ratio=ball(by_cell[n]['mu'])/ball(rows[0]['mu']))
                if n < max(selected): psi.advance(inverse_unimodular(mat(lin['gauge_matrix'])))
            all_seeds[m] = dict(gain_lower=gain_lower, cells=seeds)
        del group
    return all_seeds, group_hashes


def core_kernel(kernels, n, j, left, right, radius):
    """The R26 positive kernels, with a separately certified real radius.

    This is exactly PositiveKernels.kernels for cells12..23, except the
    independently proved panel radius replaces repeated radius quadrature.
    The physical free and curvature terms, including global warp alpha,
    are retained.  No numerical profile is substituted.
    """
    h = kernels.head; cell = kernels.source_cell(n); s = cell['segments'][j]
    af = kernels.scalar_integral(s, left, right, 'a')
    bf = kernels.scalar_integral(s, left, right, 'b')
    ca = h.sqrt12*cell['mu']/8*kernels.variation(s, left, right, 'a')
    cb = h.sqrt12/(8*cell['mu'])*kernels.variation(s, left, right, 'b')
    W = power2(21)*(arb(7)*cell['delta'].log()/4).exp()
    free = h.alpha*interval(1/(1+W*W), arb(1))
    return dict(r=radius, coreA=free*af+ca, coreB=free*bf+cb)


def prepare_cell(kernels, n, material, threshold):
    parents = []; total_pieces = 0; max_product = arb(0)
    for row in material['panels']:
        left = Q(*row['x_left']); right = Q(*row['x_right'])
        radius = ball(row['radius']); pieces = []
        stack = [(left, right, 0)]
        while stack:
            lo, hi, depth = stack.pop()
            kernel = core_kernel(kernels, n, row['segment'], lo, hi, radius)
            A, B = kernels.mode_integrals(kernel, 92)
            product = (A.upper()*B.upper()).upper()
            if product > threshold:
                if depth >= 30: raise ArithmeticError('The PB subdivision limit was reached')
                mid = (lo+hi)/2
                stack.append((mid, hi, depth+1)); stack.append((lo, mid, depth+1))
            else:
                pieces.append(kernel); max_product = maximum(max_product, product)
        parents.append(dict(radius=radius, w=ball(row['w']),
            tau=ball(row['tau_range']), J=ball(row['canonical_source_integral']).upper(),
            pieces=pieces))
        total_pieces += len(pieces)
    return parents, total_pieces, max_product


def column_panel_bounds(kernels, parents, mode, seed, gain_lower, forward):
    column = copy.copy(seed['phi' if forward else 'psi'])
    capq, capxi = seed['phi_caps' if forward else 'psi_caps']
    u = mode*mode-4; bounds = [None]*len(parents)
    indices = range(len(parents)) if forward else range(len(parents)-1, -1, -1)
    for i in indices:
        parent = parents[i]; qcap = arb(0); xcap = arb(0)
        pieces = parent['pieces'] if forward else reversed(parent['pieces'])
        for piece in pieces:
            A, B = kernels.mode_integrals(piece, mode); T, major, _ = peano_matrix(A, B)
            within = mv(major, column.absolute_uppers()); r = piece['r']
            q = upper((r/kernels.head.rc)**u)*within[0]
            xi = upper((kernels.head.rc/r)**u)*within[1]
            if forward: q /= gain_lower; xi /= gain_lower
            qcap = maximum(qcap, positive_min(q, capq))
            xcap = maximum(xcap, positive_min(xi, capxi))
            column.advance(T if forward else inverse_unimodular(T))
        bounds[i] = (qcap, xcap)
    return bounds


def physical_caps(parent, q, xi, mode, Xbar, B, a, mu, mu_bar):
    r = parent['radius']; w = parent['w']; root = arb(12).sqrt()
    al = a.lower(); au = a.upper(); D = root*mu_bar
    yl = al*r.lower()**7*w.lower(); yu = au*r.upper()**7*w.upper()
    tlo = (yl/(yl+D.upper())).lower()
    thi = (yu/(yu+D.lower())).upper()
    qfactor = thi/(Xbar.lower()*al)
    xfactor = (mu.upper()/mu_bar.lower())*(1-tlo)/Xbar.lower()
    weight = (mode*parent['tau'].upper()).exp().upper()
    p = ((1+mode)*B.upper()*mode*qfactor*q*weight).upper()
    kappa = ((1+mode)*(mode*mode*qfactor*q+xfactor*xi)*weight).upper()
    return p, kappa


def evaluate_mode(kernels, parents, mode, seed, gain_lower, density):
    Xbar = ball(density['canonical_total_envelope']); B = ball(density['B'])
    a = ball(density['Q_coefficient']); mu_bar = ball(density['mu_upper'])
    phi = column_panel_bounds(kernels, parents, mode, seed, gain_lower, True)
    psi = column_panel_bounds(kernels, parents, mode, seed, gain_lower, False)
    ph = []; ps = []; iphi = []; ipsi = []
    for panel, phq, psq in zip(parents, phi, psi):
        ph.append(physical_caps(panel, *phq, mode, Xbar, B, a, seed['mu'], mu_bar))
        ps.append(physical_caps(panel, *psq, mode, Xbar, B, a, seed['mu'], mu_bar))
        source_weight = panel['J']*(-mode*panel['tau'].lower()).exp().upper()
        iphi.append((source_weight*phq[0]).upper())
        ipsi.append((source_weight*psq[0]).upper())
    suffix = [arb(0)]*(len(parents)+1)
    for i in range(len(parents)-1, -1, -1): suffix[i] = (suffix[i+1]+ipsi[i]).upper()
    prefix = arb(0); pmax = arb(0); kmax = arb(0); witness = [None, None]
    for i in range(len(parents)):
        prefix = (prefix+iphi[i]).upper()
        p = ph[i][0]*suffix[i]+ps[i][0]*prefix
        k = ph[i][1]*suffix[i]+ps[i][1]*prefix
        if p > pmax: witness[0] = i
        if k > kmax: witness[1] = i
        pmax = maximum(pmax, p); kmax = maximum(kmax, k)
    diag = (seed['mu_ratio']*(pmax+kmax)).upper()
    return dict(mode=mode,
        phi_physical_p_sup=small_record(max(v[0] for v in ph)),
        phi_physical_kappa_sup=small_record(max(v[1] for v in ph)),
        psi_physical_p_sup=small_record(max(v[0] for v in ps)),
        psi_physical_kappa_sup=small_record(max(v[1] for v in ps)),
        weighted_phi_Q_source_integral=small_record(prefix),
        weighted_psi_Q_source_integral=small_record(suffix[0]),
        phi_Q_sup=small_record(max(v[0] for v in phi)),
        psi_Q_sup=small_record(max(v[0] for v in psi)),
        ordered_diagonal=small_record(diag), ordered_diagonal_log2_upper=ceil_log2_upper(diag),
        diagonal_component_witnesses=witness,
        normalized_phi_Q_gain_lower=small_record(gain_lower),
        mu_ratio=small_record(seed['mu_ratio']))


def main():
    p = argparse.ArgumentParser(description=__doc__)
    for name in ('columns', 'ordered', 'density', 'ready', 'panels-summary', 'out-prefix'):
        p.add_argument('--'+name, type=Path, required=True)
    p.add_argument('--first-cell', type=int, default=12)
    p.add_argument('--last-cell', type=int, default=13)
    p.add_argument('--only-mode', type=int)
    p.add_argument('--product-bits', type=int, default=20)
    args = p.parse_args(); ctx.prec = 192; started = time.monotonic()
    if not 12 <= args.first_cell <= args.last_cell <= 23: raise ValueError('Expected cells12..23')
    records = {}; input_hashes = {}
    for name in ('columns', 'ordered', 'density', 'ready', 'panels_summary'):
        path = getattr(args, name); records[name], raw = load_json(path); input_hashes[str(path)] = sha(raw)
    D = records['columns']; O = records['ordered']; P = records['density']; S = records['panels_summary']
    if D['modes'] != list(range(2, 93, 2)): raise ValueError('All46 true modal columns are required')
    if input_hashes[str(args.columns)] != O['input_hashes'].get(str(args.columns)):
        raise ValueError('The ordered source columns differ')
    for name in ('density', 'ready'):
        if input_hashes[str(getattr(args, name))] not in S['input_hashes'].values():
            raise ValueError('Panel source/density identity differs')
    if input_hashes[str(args.ready)] not in D['input_hashes'].values():
        raise ValueError('The real background differs')
    if not all(P['gates'].values()): raise ValueError('The source material has unpaid gates')
    selected = set(range(args.first_cell, args.last_cell+1)); modes = D['modes']
    if args.only_mode is not None:
        if args.only_mode not in modes: raise ValueError('Mode is outside the actual low46 window')
        modes = [args.only_mode]
    refined = {(r['mode'], c['cell']): c for r in O['mode_rows'] for c in r['refined_cells']}
    head = RealHead(records['ready'], start=12, far=159, exact_through=23)
    kernels = PositiveKernels(head, 225, 92)
    seeds, group_hashes = seed_columns(D, selected, head.rc, head.rho, refined)
    if not any(h in S['input_hashes'].values() for h in group_hashes.values()):
        raise ValueError('Panel radius anchors are not from these true column groups')
    density = {r['cell']: r for r in P['rows']}; material_refs = {r['cell']: r for r in S['cells']}
    source_names = [Path(__file__).name, 'closure_real_head_source_enclosure.py',
        'closure_real_linear_head_enclosure.py', 'closure_real_head_green_enclosure.py',
        'closure_projective_interval_column.py']
    source_hashes = {n: sha(Path(__file__).with_name(n).read_bytes()) for n in source_names}
    entries = []
    for n in sorted(selected):
        ref = material_refs[n]; material, raw = load_json(Path(ref['file']))
        if sha(raw) != ref['sha256']: raise ValueError('A source material panel package changed')
        for name in ('density', 'ready'):
            if input_hashes[str(getattr(args, name))] not in material['input_hashes'].values():
                raise ValueError('A panel package uses a different source or envelope')
        parents, piece_count, maxproduct = prepare_cell(kernels, n, material, power2(-args.product_bits))
        del material, raw; gc.collect()
        print(json.dumps(dict(event='prepared', cell=n, source_panels=len(parents),
            PB_pieces=piece_count, seconds=time.monotonic()-started,
            RSS_KiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)), flush=True)
        rows = []
        for m in modes:
            rows.append(evaluate_mode(kernels, parents, m, seeds[m]['cells'][n], seeds[m]['gain_lower'], density[n]))
            if m % 16 == 0 or m == modes[-1]:
                print(json.dumps(dict(event='mode', cell=n, mode=m,
                    diagonal_log2_upper=rows[-1]['ordered_diagonal_log2_upper'],
                    seconds=time.monotonic()-started)), flush=True)
        result = dict(status='Certified position-preserving modal Green data; no invariant-box assertion',
            cell=n, modes=modes, source_panels=len(parents), PB_pieces=piece_count,
            maximum_AB=ball_record(maxproduct), rows=rows,
            diagonal_maximum_log2_upper=max(r['ordered_diagonal_log2_upper'] for r in rows),
            state_norm='Separate p and kappa component suprema, weighted by (1+m) exp(tau(r)m) / V(r), with B on p.',
            source_norm='sup exp(tau(r)m)|f_m|/(c V^2/w); Jcan integrates its exact canonical density.',
            ordering='At target panel i, outer-source psi integrals use j>=i and inner-source phi integrals j<=i. The common panel is safely counted twice.',
            column_normalization='phi caps divide the exact nonzero cut-Q gain by its positive lower bound; psi has Qcut=0, Xi12cut=1.',
            input_hashes={**input_hashes, ref['file']: ref['sha256']},
            group_hashes=group_hashes, source_hashes=source_hashes,
            elapsed_seconds=time.monotonic()-started,
            peak_RSS_KiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
        payload = gzip.compress((json.dumps(result, separators=(',', ':'))+'\n').encode(), mtime=0)
        path = args.out_prefix.with_name(args.out_prefix.name+f'-cell{n:03d}.json.gz')
        if len(payload) >= 5_000_000: raise ArithmeticError('Repository file size cap exceeded')
        path.write_bytes(payload)
        entries.append(dict(cell=n, path=str(path), sha256=sha(payload), bytes=len(payload),
            source_panels=len(parents), PB_pieces=piece_count,
            diagonal_maximum_log2_upper=result['diagonal_maximum_log2_upper']))
        print(json.dumps(dict(event='cell', **entries[-1], seconds=time.monotonic()-started)), flush=True)
        del parents; kernels.release_cell(n); gc.collect()
    summary = dict(status='Completed weighted panel Green ledger', modes=modes, cells=entries,
        input_hashes=input_hashes, group_hashes=group_hashes, source_hashes=source_hashes,
        elapsed_seconds=time.monotonic()-started,
        peak_RSS_KiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    path = args.out_prefix.with_name(args.out_prefix.name+'-summary.json')
    path.write_text(json.dumps(summary, indent=2)+'\n')
    print(json.dumps(dict(event='done', output=str(path), seconds=summary['elapsed_seconds'],
        RSS_KiB=summary['peak_RSS_KiB'])), flush=True)


if __name__ == '__main__': main()
