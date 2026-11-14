#!/usr/bin/env python3
"""Decompose the saved collocation residual by Fourier unknown.

Reconstructs the original cubic collocation interpolant from saved nodes
and the original RHS, then evaluates the same five-point Lobatto norm.
An optional m-squared scaling is evaluated diagnostically; no BVP is solved
and no conclusion about the effect of such scaling is assumed.
"""
import os
for name in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[name] = '1'
import argparse
import hashlib
import importlib.util
import json
from pathlib import Path
import numpy as np
from scipy.integrate._bvp import create_spline

HERE = Path(__file__).resolve().parent


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--source-root', type=Path, required=True)
    p.add_argument('--checkpoint', type=Path, required=True)
    p.add_argument('--linear-port', type=Path, required=True)
    p.add_argument('--out', type=Path, required=True)
    a = p.parse_args()
    spec = importlib.util.spec_from_file_location('spectrum_source', HERE/'db6f-prefix-flat-geometry-source.py')
    loader = importlib.util.module_from_spec(spec); spec.loader.exec_module(loader)
    rec, source, unused, saved = loader.source(a.checkpoint, a.linear_port, a.source_root)
    cfg = rec['config']
    obj = source.__class__(rec['frozen_profile'], source.port, rec['gauge_amplitude'],
                           cfg['modes'], cfg['angular'], True, rec['warp_reference_q'])
    par = saved.p
    physical = np.asarray(rec['mesh'])
    x = obj.inverse_chart(physical, par[0]); h = np.diff(x)
    y = saved.sol(physical)
    f = obj.fun(x, y, par)
    pp = create_spline(y, f, x, h)
    midpoint = x[:-1]+h/2
    fraction = np.sqrt(3/7)/2
    contributions = []
    frequencies = np.r_[0, np.tile(3*np.arange(1, obj.M+1), 3)]
    weights = 1+frequencies**2
    for z in (midpoint, midpoint+fraction*h, midpoint-fraction*h):
        rhs = obj.fun(z, pp(z), par)
        residual = pp(z, 1)-rhs
        contributions.append((residual/(1+abs(rhs)),
                              weights[:, None]*residual/(1+weights[:, None]*abs(rhs))))
    rows = []
    totals = {}
    for kind, side in [('original', 0), ('m_squared_unknown_scaling', 1)]:
        rm, rp, rn = [v[side] for v in contributions]
        bycomponent = np.sqrt(.5*(32/45*rm**2+49/90*(rp**2+rn**2)))
        rms = np.sqrt(np.sum(bycomponent**2, axis=0))
        i = int(np.argmax(rms))
        totals[kind] = dict(maximum=float(rms[i]),
                            physical_interval=[float(physical[i]), float(physical[i+1])])
        for component in range(obj.n):
            j = int(np.argmax(bycomponent[component]))
            axis = 'R0' if component == 0 else ('R', 'T', 'Z')[(component-1)//obj.M]
            rows.append(dict(norm=kind, component=component, axis=axis,
                             frequency=int(frequencies[component]),
                             maximum_rms=float(bycomponent[component, j]),
                             physical_interval=[float(physical[j]), float(physical[j+1])]))
    rows.sort(key=lambda r:(r['norm'], -r['maximum_rms']))
    out = dict(scope=__doc__, checkpoint=str(a.checkpoint),
               checkpoint_sha256=hashlib.sha256(a.checkpoint.read_bytes()).hexdigest(),
               script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
               saved_reported_rms=rec['max_rms_collocation_residual'],
               nodes=len(x), modes=obj.M, angular=obj.nt,
               hypothetical_weights='1+(3j)^2 on each nonmean cylindrical mode, R0 weight 1',
               totals=totals, component_rows=rows)
    a.out.write_text(json.dumps(out, indent=2)+'\n')
    print(json.dumps(dict(totals=totals, reported=out['saved_reported_rms'],
                         leading_components=[r for r in rows if r['norm']=='original'][:6])), flush=True)


if __name__ == '__main__':
    main()
