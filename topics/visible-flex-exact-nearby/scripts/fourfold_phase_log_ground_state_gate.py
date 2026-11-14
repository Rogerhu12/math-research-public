#!/usr/bin/env python3
"""Assemble an explicit real ground-state log gate from frozen core proofs."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import numpy as np

from fourfold_phase_root_interval import Box


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--inputs', type=Path, required=True)
    ap.add_argument('--scalar-certificate', type=Path, required=True)
    ap.add_argument('--core-certificate', type=Path, required=True)
    ap.add_argument('--out', type=Path, required=True)
    args = ap.parse_args()
    s = json.loads(args.scalar_certificate.read_text())
    c = json.loads(args.core_certificate.read_text())
    sha = hashlib.sha256(args.inputs.read_bytes()).hexdigest()
    if s['inputs_sha256'] != sha or c['configuration']['inputs_sha256'] != sha:
        raise ValueError('the two certificates must cover this same exact input')
    if s['radial_core'] != c['radial_core'] or not s['gate_passed'] or not c['complete']:
        raise ValueError('matching complete scalar and geometric cores required')
    cells = c['cells']
    if (cells[0]['radial_interval'][0] != 0
        or cells[-1]['radial_interval'][1] != c['radial_core'][1]
        or any(a['radial_interval'][1] != b['radial_interval'][0] for a,b in zip(cells,cells[1:]))):
        raise ValueError('geometric cell coverage has a gap')
    with np.load(args.inputs, allow_pickle=False) as f:
        highest_frequency = 4*f['phase_coefficients'].shape[1]
    arange = np.asarray(s['circumference_radius_derivative_ranges'])
    a0,a1,a2 = map(Box, np.maximum(abs(arange[:,0]),abs(arange[:,1])))
    g0,g1,g2 = map(Box,s['gamma_field_absolute_derivative_bounds'])
    qmin = Box(s['Fz_over_x_lower'])
    qmax = Box(s['Fx_vertical_upper'])  # Q=int_0^1 Fz,x(tx)dt.
    qt = Box(s['quotient_angular_Lipschitz_upper'])
    qx = Box(s['quotient_radial_Lipschitz_upper'])
    fmin = Box(c['support_lower'])      # |F| >= F dot nu > 0.
    fmax = Box(max(row['F_norm_upper'] for row in cells))
    fxmax = Box(max(row['Fx_norm_upper'] for row in cells))
    tx = Box(max(row['tangent_x_norm_upper'] for row in cells))
    tt = Box(max(row['tangent_theta_norm_upper'] for row in cells))
    # Gamma_theta is odd in x. This deliberately coarse coefficient bound
    # pays |Gamma_x,theta| <= highest_frequency * sum |gamma_k'(x)|.
    qtt = a0*highest_frequency*g1
    qxt = (a2*g0+2*a1*g1+a0*(g2+g0*g1*g1))/2
    ell = qt/qmin+a0/fmin
    ell_theta = qtt/qmin+qt*qt/(qmin*qmin)+3*a0*a0/(fmin*fmin)+a0*tt/fmin
    fx_theta = a1+a0*tx
    ell_x = qxt/qmin+qx*qt/(qmin*qmin)+3*fxmax*a0/(fmin*fmin)+fx_theta/fmin
    report = dict(kind='real_ground_state_log_gate_for_same_explicitly_symmetric_infinite_R33_core',
        inputs_sha256=sha, source_checkpoint_sha256=c['source_checkpoint_sha256'],
        source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        certificates_sha256={str(path):hashlib.sha256(path.read_bytes()).hexdigest()
            for path in [args.scalar_certificate,args.core_certificate]},
        dependency_sha256={'fourfold_phase_root_interval.py':hashlib.sha256(
            Path(__file__).with_name('fourfold_phase_root_interval.py').read_bytes()).hexdigest()},
        radial_core=c['radial_core'],
        Q_lower=float(qmin.lo), Q_upper=float(qmax.hi),
        F_norm_lower=float(fmin.lo),F_norm_upper=float(fmax.hi),
        G_lower=float((qmin/fmax).lo),G_upper=float((qmax/fmin).hi),
        ell_absolute_upper=float(ell.hi),ell_theta_absolute_upper=float(ell_theta.hi),
        ell_x_absolute_upper=float(ell_x.hi),
        quotient_theta2_absolute_upper=float(qtt.hi),quotient_x_theta_absolute_upper=float(qxt.hi),
        exact_definitions='Q=Fz/x by positive continuous extension; G=Q/|F|; uz=Fz/|F|=xG; ell=dtheta log(G)',
        exact_identity='(dtheta-ell) uz=0, including x=0',
        radial_regularity='F is C4 intersect W5,infinity; Q and ell are at least C3 intersect W4,infinity for every fixed finite angular derivative',
        limitations=['Real core only; no complex strip or parameter interval is paid by this report',
            'Does not define a new cap or solve the residual metric equation',
            'Explicit symmetrization and exact slope integration remain part of the object definition'])
    if report['G_lower'] <= 0:
        raise ValueError('ground state factor is not positive')
    args.out.parent.mkdir(parents=True,exist_ok=True)
    args.out.write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report,indent=2),flush=True)


if __name__=='__main__':
    main()
