#!/usr/bin/env python3
"""Exact two-axis obstruction to all circle-preserving material relabelings.

For a fixed circle, the ratio of the largest/smallest normal radial speed
squared cannot be changed by (s,u) -> (phi(s),chi(s,u)).  A pair of positive
values P,Q therefore imposes metric error >= abs(P-Q)/(P+Q), against every
positive rotational target.  The two values here are computed from the
defining binary shared jets, with no floating trigonometry or target packets.

This checks a necessary condition only.  It neither constructs a new graph
nor excludes perturbing the graph or using diffeomorphisms that mix circles.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as Q
import gzip
import hashlib
import importlib.util
import io
import json
import math
from pathlib import Path
import time

import numpy as np

HERE = Path(__file__).resolve().parent


def module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def identity(path):
    path = Path(path).resolve()
    return dict(file=str(path), bytes=path.stat().st_size,
                sha256=hashlib.sha256(path.read_bytes()).hexdigest())


def safe_lower(value, digits=24):
    scale = 10**digits
    n = value.numerator*scale//value.denominator
    assert Q(n, scale) <= value < Q(n+1, scale)
    whole, tail = divmod(n, scale)
    return dict(exact=str(Q(n, scale)),
                decimal=f'{whole}.{tail:0{digits}d}')


def axis_jets(jets, node, modes, sign):
    y = [Q.from_float(float(v)) for v in jets[0, node]]
    d = [Q.from_float(float(v)) for v in jets[1, node]]
    rs = d[0]+sum((sign**j*d[j] for j in range(1, modes+1)), Q(0))
    zs = d[-1]+sum((sign**j*d[2*modes+j] for j in range(1, modes+1)), Q(0))
    angular = y[0]+sum((sign**j*(y[j]+3*j*y[modes+j])
                        for j in range(1, modes+1)), Q(0))
    if angular == 0:
        raise ValueError(f'The defining angular tangent vanishes at node {node}')
    p = rs*rs+zs*zs
    if p <= 0:
        raise ValueError(f'The defining normal radial speed vanishes at node {node}')
    return dict(radial_component=rs, height_component=zs,
                angular_tangent=angular, schur=p)


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--geometry', type=Path, required=True)
    ap.add_argument('--out', type=Path, required=True)
    ap.add_argument('--correction-width', type=float, default=.15)
    ap.add_argument('--node', type=int, action='append',
                    help='Optional selected native nodes; otherwise all before correction support')
    args = ap.parse_args()
    if args.out.exists():
        raise FileExistsError(args.out)
    if not math.isfinite(args.correction_width) or args.correction_width <= 0:
        raise ValueError('correction-width must be positive and finite')
    started = time.monotonic()
    storage_file = HERE/'78718-prefix-storage-v1.py'
    storage = module('fd2d_circle_axis_storage', storage_file)
    meta, payload, bindings = storage.read_payload(args.geometry, verify_arrays=True)
    if meta.get('representation') == 'exact-common-cut-prefix':
        raise ValueError('Supply the defining base, not the common-cut facade')
    with np.load(io.BytesIO(gzip.decompress(payload)), allow_pickle=False) as raw:
        mesh, jets = raw['mesh'], raw['jets']
    modes, nodes = int(meta['modes']), int(meta['nodes'])
    if mesh.shape != (nodes,) or jets.shape != (3, nodes, 3*modes+2):
        raise ValueError('Not the defining cylindrical Fourier shared-jet layout')
    if not np.isfinite(mesh).all() or not np.isfinite(jets).all() or not np.all(np.diff(mesh) > 0):
        raise ValueError('Invalid finite data')
    start = int(np.searchsorted(mesh, mesh[-1]-args.correction_width))
    selected = args.node if args.node is not None else range(1, start)
    worst, checked = None, 0
    for node in selected:
        if not 0 < node < start:
            raise ValueError('The selected node is not strictly before the conditional correction support')
        a, b = (axis_jets(jets, node, modes, sign) for sign in (1, -1))
        lower = abs(a['schur']-b['schur'])/(a['schur']+b['schur'])
        if worst is None or lower > worst['lower']:
            worst = dict(node=int(node), coordinate=Q.from_float(float(mesh[node])),
                         axes=(a,b), lower=lower,
                         unrestricted_optimal_scale=2/(a['schur']+b['schur']))
        checked += 1
    if worst is None:
        raise ValueError('No circle was checked')
    report = dict(
        schema='fd2d-circle-relabel-two-axis-schur-obstruction-v1',
        status='EXACT_FINITE_GRAPH_NECESSARY_CONDITION',
        geometry=identity(args.geometry), storage_reader=identity(storage_file),
        storage_bindings=bindings, script=identity(__file__),
        checkpoint_sha256=meta.get('checkpoint_sha256'),
        modes=modes, nodes=nodes, circles_checked=checked,
        witness=dict(node=worst['node'], coordinate_exact=str(worst['coordinate']),
            axes={name:{key:str(value) for key,value in row.items()}
                  for name,row in zip(('psi_zero','psi_pi_over_3'),worst['axes'])},
            target_normalized_metric_lower_exact=str(worst['lower']),
            safe_lower_decimal=safe_lower(worst['lower']),
            unrestricted_optimal_radial_scale_exact=str(worst['unrestricted_optimal_scale'])),
        exceeds_2e_minus9=worst['lower']>Q(1,500_000_000),
        relabeling_class='(s,u) -> (phi(s),chi(s,u)); phi a radial diffeomorphism and every chi(s,.) a circle diffeomorphism',
        target_class='Any fixed positive rotational metric zeta(s)^2 ds^2+a(s)^2 du^2',
        warp_handling='The Schur complement is unchanged by replacing psi with the physical material angle at fixed radial coordinate',
        exact_bridge_scale_cancels=True,
        common_support=dict(width_binary64_hex=args.correction_width.hex(), start_index=start,
            witness_before_support=True, actual_common_map_constructed=False,
            scope='Any actual common-cut extension using this same base and zero correction before the stated index inherits the pair'),
        conclusion_scope='A necessary lower bound for this finite graph under the stated relabeling class, not a nonexistence theorem for a new graph',
        solver_calls=0, ode_calls=0, new_graph=False, continuous_metric_upper=False,
        seconds=time.monotonic()-started)
    args.out.write_text(json.dumps(report,indent=2,sort_keys=True)+'\n')
    print(json.dumps(dict(output=str(args.out), witness_node=worst['node'],
        circles_checked=checked, lower=float(worst['lower']),
        safe_lower_decimal=report['witness']['safe_lower_decimal']['decimal'],
        exceeds_2e_minus9=report['exceeds_2e_minus9'],seconds=report['seconds']),sort_keys=True))


if __name__=='__main__':
    main()
