#!/usr/bin/env python3
"""Separate resolved and discarded angular residuals of an actual finite field.

Evaluations use existing shared-Hermite nodes and unchanged full exponentials.
This is a finite diagnostic, not a continuous certificate or a new solve.
"""
import os
for key in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[key] = '1'
import argparse, gzip, io, json
from pathlib import Path
import numpy as np
import fd2d_gc_native_log_field as native
from fd2d_gc_native_log_physical import PhysicalNativeLogField


class Reader:
    def __getattr__(self, name):
        return getattr(np, name)
    def load(self, path, *args, **kwargs):
        if isinstance(path, (str, Path)) and str(path).endswith('.gz'):
            return np.load(io.BytesIO(gzip.decompress(Path(path).read_bytes())), *args, **kwargs)
        return np.load(path, *args, **kwargs)


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--field', type=Path, required=True)
    p.add_argument('--out', type=Path, required=True)
    p.add_argument('--locations', type=float, nargs='+', required=True)
    p.add_argument('--points', type=int, default=2048)
    a = p.parse_args()
    if a.out.exists():
        raise FileExistsError(a.out)
    native.np = Reader(); model = PhysicalNativeLogField(a.field)
    xi = 2*np.pi*np.arange(a.points)/a.points; modes = 2*model.native.K
    rows = []
    def split(value):
        value = np.asarray(value, dtype=float)
        coeff = np.fft.rfft(value)/a.points
        low = coeff.copy(); low[modes+1:] = 0
        resolved = np.fft.irfft(low, n=a.points)*a.points
        return dict(maximum=float(abs(value).max()),
            resolved_maximum=float(abs(resolved).max()),
            discarded_maximum=float(abs(value-resolved).max()),
            resolved_coefficient_maximum=float(abs(coeff[:modes+1]).max()),
            discarded_coefficient_maximum=float(abs(coeff[modes+1:]).max()))
    for desired in a.locations:
        node = int(np.argmin(abs(model.native.nodes-desired)))
        x = float(model.native.nodes[node]); f = model.evaluate(x, xi)
        eta, zeta, ex, zx = [f[k][0] for k in ('eta', 'zeta', 'eta_xi', 'zeta_xi')]
        aa, ap, app, J = [f[k][0] for k in ('a', 'ap', 'app', 'J')]
        q, Ux = f['q'][0], f['Ux'][0]; c = ap/aa
        chi = -aa*app/(1-ap*ap); inv = np.exp(-eta)
        exact_eta = J*(inv*zx/(aa*q)+c*(zeta*zeta*inv*inv+chi*np.expm1(-2*eta)))+Ux*ex/q
        exact_zeta = J*(inv*(2*zeta*zx-(zeta*zeta+chi)*ex)/(aa*q)-c*(1+chi)*zeta)+Ux*zx/q
        rn = f['n_s_material'][0]-f['m_u'][0]/aa-c*(f['l'][0]-f['n'][0])
        rm = f['m_s_material'][0]-f['l_u'][0]/aa+2*c*f['m'][0]
        row = dict(requested_x=desired, actual_node=node, x=x,
            eta_velocity_residual=split(f['eta_x'][0]-exact_eta),
            zeta_velocity_residual=split(f['zeta_x'][0]-exact_zeta),
            physical_Rn_maximum=float(abs(rn).max()), physical_Rm_maximum=float(abs(rm).max()))
        rows.append(row)
    report = dict(schema='fd2d-native-spectral-residual-screen-v1',
        source=native.identity(__file__), actual_field=native.identity(a.field),
        defining_arrays=model.meta['actual_arrays'], maximum_frequency=modes,
        angular_points=a.points, same_actual_field=True, selected_native_nodes=True,
        continuous_certificate=False, new_solve=False, rows=rows)
    a.out.write_text(json.dumps(report, indent=2, allow_nan=False)+'\n')
    print(json.dumps(report, indent=2))


if __name__ == '__main__':
    main()
