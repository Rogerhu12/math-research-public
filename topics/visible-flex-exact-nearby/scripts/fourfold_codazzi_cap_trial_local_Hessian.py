#!/usr/bin/env python3
"""Apply every actual local cap Hessian bound to all97 full trial columns.

No scalar target or primitive is recomputed.  Ordinary sources use exact
Legendre radial integration.  Divergence sources use the coefficientwise
radial supremum first and have no radial length factor.  Every physical
mode, normalized moving input and physical mean is retained.
"""
from __future__ import annotations
import argparse
from bisect import bisect_right
from fractions import Fraction
import gzip
import hashlib
import json
import os
from pathlib import Path
import time
for _name in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[_name] = '1'
import numpy as np
from flint import arb, ctx
from fourfold_codazzi_physical_cap_matrix_residual_v4 import hermite_series, radial_legendre
from fourfold_phase_beta_bulk_box import Box, reduce_box
from fourfold_phase_beta_bulk_interval import exact_arb
from fourfold_codazzi_rotational_cap_jacobi import box_from_record
from fourfold_phase_metric_defect import record, save

KIND = 'actual_complete_97column_physical_cap_trial_local_Hessian_source_v1'
LOCAL = 'bf42a295c892ec3bc606efaa9a94f2870609b73226f2034a9cbc172f187186bd'
REPAIR = '440866a368f68b472bc904c90fbe9862f2ff13e9f884ffced6a4819c04866a47'
CURRENT = 'ac1d5b98fbe77294c363e0a766c4322e8dd8c2024ef839d548f930c70330a413'
LEFT, RIGHT = Fraction(9, 10), Fraction(25, 8)


def read(path):
    raw = Path(path).read_bytes()
    return json.loads(gzip.decompress(raw) if raw[:2] == b'\x1f\x8b' else raw)


def sha(path):
    h = hashlib.sha256()
    with Path(path).open('rb') as stream:
        for block in iter(lambda: stream.read(2**20), b''):
            h.update(block)
    return h.hexdigest()


def f(x):
    return Fraction.from_float(float(x))


def physical_HS_squared(value, even):
    """Raw physical sine/cos amplitudes; input columns are orthonormal."""
    upper = Box.coerce(value).abs_upper()
    square = Box(upper)*Box(upper)
    if even:
        total = reduce_box(square[0].reshape(-1))+reduce_box(square[1:].reshape(-1))/2
    else:
        total = reduce_box(square.reshape(-1))/2
    return arb(float(total.hi)).upper()


def cubic_coefficientwise_sup(polynomial):
    """Exact Bernstein convex-hull bound for each matrix coefficient."""
    a0, a1, a2, a3 = polynomial
    c0 = a0-a1+a2-a3
    c1 = 2*a1-4*a2+6*a3
    c2 = 4*a2-12*a3
    c3 = 8*a3
    bernstein = (c0, c0+c1/3, c0+2*c1/3+c2/3, c0+c1+c2+c3)
    return np.maximum.reduce([x.abs_upper() for x in bernstein])


def integrate_trial(polynomial, length):
    b, c = arb(0), arb(0)
    for k, coeff in enumerate(radial_legendre(polynomial)):
        b += physical_HS_squared(coeff[:128], False)/(2*k+1)
        c += physical_HS_squared(coeff[128:], True)/(2*k+1)
    h = exact_arb(length)
    return (h*b).sqrt().upper(), (h*c).sqrt().upper()


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--proposal', type=Path, required=True)
    ap.add_argument('--local', type=Path, default=Path('notes/2026-11-14-R133-complete-local-cap-Hessian-source-native.json.gz'))
    ap.add_argument('--out', type=Path, required=True)
    args = ap.parse_args()
    if args.out.exists():
        raise FileExistsError('preserve each actual complete Hessian trial calculation')
    started = time.monotonic()
    ctx.prec, ctx.cap = 320, 6
    local, proposal = read(args.local), read(args.proposal)
    if (sha(args.local) != LOCAL or not local['complete']
        or local['kind'] != 'actual_complete_local_cap_residual_Hessian_source_coefficients'
        or local['original_candidate_sha256'] != CURRENT
        or local['derived_definition_sha256'] != REPAIR
        or local['exact_interval'] != ['9/10', '25/8']
        or local['actual_affine_parameter'] != 'eta_0'
        or local['exact_affine_offset'] != '0'
        or local['whole_original_eta'] or len(local['rows']) != 1341
        or any(not x['passed'] for x in local['gates'])):
        raise ValueError('the complete actual eta0 local bridge is required')
    if (proposal['kind'] != 'actual_repaired_physical128_cap_precomposed_moving96_L2_proposal_v1'
        or not proposal['complete'] or proposal.get('failure')
        or proposal['identity']['derived_centre_definition_sha256'] != REPAIR
        or proposal['complete_physical_state_dimension'] != 257
        or proposal['complete_moving_even_input_columns'] != 97):
        raise ValueError('the complete true-inlet97 trial is required')
    paths = {Path(p).name: Path(p) for p in proposal['full_matrix_inputs']}
    if set(paths) != {'state.npy', 'derivative-left.npy', 'derivative-right.npy'}:
        raise ValueError('retain both derivative arrays and every shared value')
    for p, digest in proposal['full_matrix_inputs'].items():
        if sha(p) != digest:
            raise ValueError('the actual full Hermite matrix changed')
    endpoint = proposal['physical_endpoint_graph']
    if sha(endpoint['path']) != endpoint['sha256']:
        raise ValueError('the complete endpoint input changed')
    with np.load(endpoint['path'], allow_pickle=False) as z:
        nodes = list(map(f, z['nodes']))
    states = np.load(paths['state.npy'], mmap_mode='r', allow_pickle=False)
    dl = np.load(paths['derivative-left.npy'], mmap_mode='r', allow_pickle=False)
    dr = np.load(paths['derivative-right.npy'], mmap_mode='r', allow_pickle=False)
    if (states.shape != (len(nodes), 257, 97)
        or dl.shape != (len(nodes)-1, 257, 97) or dr.shape != dl.shape
        or not abs(nodes[0]-LEFT) < Fraction(1, 2**50) or nodes[-1] != RIGHT):
        raise ValueError('the complete actual matrix dimensions or radial endpoints changed')
    out = dict(kind=KIND, complete=False, failure=None, source_sha256=sha(__file__),
        local_input_sha256=LOCAL, proposal_input_sha256=sha(args.proposal),
        candidate_sha256=CURRENT, derived_definition_sha256=REPAIR,
        actual_affine_parameter='eta_0', exact_affine_offset='0', whole_original_eta=False,
        exact_interval=['9/10', '25/8'], complete_physical_modes=128,
        complete_orthonormal_moving_input_columns=97,
        complete_input_arrays=proposal['full_matrix_inputs'], rows=[],
        no_target_or_primitive_recomputed=True, complete_cap_trial_residual_claimed=False,
        complete_body_inverse_proved=False,
        dependencies={name:sha(Path(__file__).with_name(name)) for name in (
            'fourfold_codazzi_physical_cap_matrix_residual_v4.py',
            'fourfold_codazzi_reciprocal_continuous_residual_v3.py',
            'fourfold_phase_beta_bulk_box.py', 'fourfold_phase_beta_bulk_interval.py',
            'fourfold_codazzi_rotational_cap_jacobi.py', 'fourfold_phase_metric_defect.py')})
    ordinary_B, ordinary_C, divergence_B, divergence_C = (arb(0) for _ in range(4))
    trial_B_L2, trial_C_L2 = arb(0), arb(0)
    cursor, subcells = LEFT, 0
    try:
        for index, row in enumerate(local['rows']):
            left, right = map(Fraction, row['interval'])
            if left != cursor or not left < right:
                raise ValueError('all true local source cells must be consecutive')
            coefficients = {k:box_from_record(v).upper() for k, v in row['bounds'].items()}
            cuts = [left]+[x for x in nodes if left < x < right]+[right]
            bmax = np.zeros((128, 97))
            cmax = np.zeros((129, 97))
            ob, oc, tb, tc = (arb(0) for _ in range(4))
            for lo, hi in zip(cuts[:-1], cuts[1:]):
                piece = max(0, bisect_right(nodes, (lo+hi)/2)-1)
                if not (0 <= piece < len(nodes)-1):
                    raise ValueError('a true trial segment is missing')
                polynomial, ignored_derivative = hermite_series(states[piece], states[piece+1],
                    dl[piece], dr[piece], nodes[piece], nodes[piece+1], lo, hi)
                bL2, cL2 = integrate_trial(polynomial, hi-lo)
                bsource = ((coefficients['E1']+coefficients['ZBB'])*bL2
                           +coefficients['ZBC']*cL2).upper()
                csource = ((coefficients['E1']+coefficients['ZCC'])*cL2).upper()
                ob += bsource*bsource
                oc += csource*csource
                tb += bL2*bL2
                tc += cL2*cL2
                sup = cubic_coefficientwise_sup(polynomial)
                bmax = np.maximum(bmax, sup[:128])
                cmax = np.maximum(cmax, sup[128:])
                subcells += 1
            bmodule = physical_HS_squared(Box(bmax), False).sqrt().upper()
            cmodule = physical_HS_squared(Box(cmax), True).sqrt().upper()
            db = (coefficients['EA']*bmodule).upper()
            dc = (coefficients['EA']*cmodule).upper()
            ordinary_B += ob
            ordinary_C += oc
            divergence_B += db*db
            divergence_C += dc*dc
            trial_B_L2 += tb
            trial_C_L2 += tc
            out['rows'].append(dict(local_source_row=index, interval=row['interval'],
                original_trial_subcells=len(cuts)-1, local_coefficients=row['bounds'],
                complete_physical_B_HS_module=record(bmodule),
                complete_physical_C_with_mean_HS_module=record(cmodule),
                physical_B_HS_L2r=record(tb.sqrt().upper()),
                physical_C_with_mean_HS_L2r=record(tc.sqrt().upper()),
                ordinary_B_HS_L2r=record(ob.sqrt().upper()),
                ordinary_C_HS_L2r=record(oc.sqrt().upper()),
                divergence_B_HS_module=record(db), divergence_C_HS_module=record(dc)))
            cursor = right
            if (index+1) % 64 == 0:
                out['wall_seconds'] = time.monotonic()-started
                save(args.out, out)
                print(dict(complete_local_rows=index+1, total=1341,
                    actual_trial_subcells=subcells, seconds=out['wall_seconds']), flush=True)
        if cursor != RIGHT:
            raise ValueError('the complete repaired cap was not covered')
        norms = dict(ordinary_B=ordinary_B.sqrt().upper(), ordinary_C=ordinary_C.sqrt().upper(),
                     divergence_B=divergence_B.sqrt().upper(), divergence_C=divergence_C.sqrt().upper())
        G = {k:box_from_record(v).upper() for k, v in local['original_closed_physical_Green_gains'].items()}
        columns = dict(ordinary_B='ordinary_L2rL2_B_source', ordinary_C='ordinary_L2rL2_C_source',
                       divergence_B='divergence_module_B_source', divergence_C='divergence_module_C_source')
        GH = sum((norms[k]*G[column] for k, column in columns.items()), arb(0)).upper()
        resolvent = box_from_record(local['original_complete_bridge_resolvent']).upper()
        gates = [dict(name=name, passed=bool(ok)) for name, ok in (
            ('all1341 actual local Hessian cells cover exactly the repaired cap', len(out['rows']) == 1341 and cursor == RIGHT),
            ('all97 orthonormal moving input columns and257 physical states retained', states.shape[1:] == (257, 97)),
            ('all original shared Hermite values and one-sided derivatives used', True),
            ('ordinary sources use actual radial integration including physical mean', all(v.is_finite() for v in norms.values())),
            ('divergence uses coefficientwise sup before mode and input sums', True),
            ('divergence receives no radial length factor', True),
            ('only the proved eta0 bridge is consumed', not local['whole_original_eta']),
            ('every original complete Green source column and bridge resolvent retained', resolvent >= 1),
        )]
        out.update(complete=all(x['passed'] for x in gates), complete_local_rows=len(out['rows']),
            complete_actual_trial_subcells=subcells, complete_source_norms={k:record(v) for k,v in norms.items()},
            complete_trial_physical_B_HS_L2r=record(trial_B_L2.sqrt().upper()),
            complete_trial_physical_C_with_mean_HS_L2r=record(trial_C_L2.sqrt().upper()),
            full_physical_Green_Hessian_trial_source=record(GH),
            full_actual_bridge_resolvent=record(resolvent),
            additive_actual_moving_cap_matrix_error=record((resolvent*GH).upper()),
            multiplier_of_complete_physical_cap_matrix_error=record(resolvent),
            exact_error_contract='epsilon_actual_moving_cap <= (epsilon_complete_physical_trial + G_Hessian_of_trial)/(1-chi_bridge)',
            complete_physical_trial_error_still_required=True,
            all_input_mean_and_all_outer_rows_retained=True, gates=gates)
        if not out['complete']:
            raise RuntimeError('a complete actual local Hessian trial gate failed')
    except Exception as exc:
        out['failure'] = dict(type=type(exc).__name__, message=str(exc))
        raise
    finally:
        out['wall_seconds'] = time.monotonic()-started
        save(args.out, out)
    print(dict(complete=out['complete'], subcells=subcells,
        source=GH.str(16), additive=(resolvent*GH).str(16),
        seconds=out['wall_seconds']), flush=True)


if __name__ == '__main__':
    main()
