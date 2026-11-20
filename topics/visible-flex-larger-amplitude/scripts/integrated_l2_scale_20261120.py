#!/usr/bin/env python3
"""Positive quadrature scale for the existing complete DoubleIntegrated map.

No coordinates are dropped, and E/D are not set to zero.  This chooses a
different LM direction norm; it does not change the physical Gram target.
No residual, Jacobian, geometry audit, or nonlinear solve is evaluated.
This source was recovered after an unavailable-environment interruption;
no successful production preparation is claimed for this new source.
"""
import argparse
import hashlib
import importlib.util
import json
from pathlib import Path
import sys
import numpy as np


def coefficient_frequencies(problem):
    M = problem.M
    return np.r_[2*np.arange(M+1), 2*np.arange(1, M+1), 2*np.arange(M+1)].astype(float)


def make_scale(problem):
    """Return the positive scale vector in original DoubleIntegrated order.

    A[i,k] scale = 1 / sqrt(w_i * (1+nu_k**2)),
    E[i,k], D[i,k] scale = 1 / sqrt(h_i * (1+nu_k**2)),
    core[j] scale = 1/(1+nu_j**2), H scale = fixed lift width.
    Endpoint/fixed A slots retain the original map's definition.
    """
    q = problem
    h = np.diff(q.mesh)
    w = np.zeros(q.J, dtype=float)
    w[:-1] += h/2
    w[1:] += h/2
    nu = coefficient_frequencies(q)
    lam = np.sqrt(1.+nu*nu)
    A = 1./(np.sqrt(w[:, None])*lam[None, :])
    E = 1./(np.sqrt(h[:, None])*lam[None, :])
    D = E.copy()
    core = 1./(1.+q.freq[q.K:]**2)
    scale = np.r_[core, A[0, :2*q.M+1], A[1:-1].ravel(),
                  E.ravel(), D.ravel(), q.width]
    if scale.size != q.free_size+2*q.n or not np.all(np.isfinite(scale)) or not np.all(scale > 0):
        raise ValueError('The declared positive complete-coordinate scale is not defined')
    return scale


def create(problem, coordinate_module):
    """Use the published endpoint projector and lift/pullback unchanged."""
    return coordinate_module.DoubleIntegrated(problem, scale=make_scale(problem))


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    p = argparse.ArgumentParser(description=__doc__)
    for key in ('bundle', 'operator', 'implementation', 'coordinate-source', 'out'):
        p.add_argument('--'+key, type=Path, required=True)
    args = p.parse_args()
    if args.out.exists():
        raise ValueError('Do not overwrite the existing scale preparation report')
    m = load('integrated_l2_prepare_implementation', args.implementation)
    c = load('integrated_l2_prepare_coordinates', args.coordinate_source)
    data = np.load(args.bundle, allow_pickle=False)
    M = (data['qjets'].shape[-1]-2)//3
    q = m.create(args.operator, data['mesh'], data['a_stages'], float(data['radius']),
                 data['fixed_core_first3'], M=M, N=2048, width=float(data['width']),
                 quarter=True, stage_block=64)
    coordinates = create(q, c)
    metadata = coordinates.metadata()
    # Read only the original 2x2/4x4 Gram blocks.  Do not repeat the
    # previously published physical or lift/transpose probes.
    by_size = {}
    for size in (2, 4):
        groups = [g for g in coordinates.groups if len(g['indices']) == size]
        by_size[str(size)] = dict(
            count=len(groups),
            normalized_condition_min=min((g['normalized_condition'] for g in groups), default=None),
            normalized_condition_max=max((g['normalized_condition'] for g in groups), default=None))
    report = dict(schema='complete-double-integrated-positive-L2-scale-20261120-v1',
        source_sha256=sha(__file__), original_coordinate_source_sha256=sha(args.coordinate_source),
        implementation_sha256=sha(args.implementation), bundle_sha256=sha(args.bundle),
        M=M,J=q.J,full_N=q.full_N,quarter_N=q.N,metadata=metadata,gram_blocks=by_size,
        scale_formula='A=1/sqrt(w_i*(1+nu_k^2)); E=D=1/sqrt(h_i*(1+nu_k^2)); core=1/(1+nu_j^2); H=width',
        direction_norm_changed=True,physical_objective_changed=False,
        E_and_D_retained=True,nonlinear_solves=0,geometry_calls=0,
        old_transpose_probes_repeated=0,
        scope='One actual-mesh production scale preparation; not a convergence or continuous-geometry conclusion')
    args.out.write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report,indent=2))


if __name__ == '__main__':
    main()
