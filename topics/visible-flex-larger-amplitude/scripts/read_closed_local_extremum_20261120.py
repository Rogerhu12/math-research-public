#!/usr/bin/env python3
"""Refine a single observed curvature peak in its actual quintic cell.

Numerical local optimization only. A discovered point is an additional
necessary-condition witness; no local or global maximum is certified.
All scalar geometry carriers are the same binary carriers as the solve.
"""
import argparse
import hashlib
import importlib.util
import json
from pathlib import Path
import sys

import numpy as np
from scipy.optimize import minimize


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


class LocalField:
    def __init__(self, dense, observed, data):
        self.weights = observed.hermite_weights
        self.o = dense.ClosedGram(data['mesh'], data['a_stages'],
            float(data['radius']), data['fixed_core_first3'],
            M=(data['qjets'].shape[-1]-2)//3, N=2, width=float(data['width']))
        x, self.affine = self.o.pack(data['qjets'], float(data['Hcap']), require_affine=True)
        self.jets, self.height, self.core = self.o.unpack(x)
        self.o.N = 1

    def fields(self, cell, u, phi):
        o = self.o
        h = o.mesh[cell+1]-o.mesh[cell]
        s = o.mesh[cell]+h*u
        y, v, acc = self.weights(h, u)@self.jets[cell:cell+2].reshape(6, o.n)
        o.cos = np.r_[1., np.cos(phi*o.freq)][None]
        o.sin = np.sin(phi*o.freq)[None]
        rho = 1.+o.cos[:, 1:]@(o.qfreq*self.core)
        rho_phi = -o.sin@(o.freq*o.qfreq*self.core)
        delta = o.sin@((o.qfreq/o.freq)*self.core)
        er = np.array([[np.cos(delta[0]), np.sin(delta[0]), 0.]])
        et = np.array([[-np.sin(delta[0]), np.cos(delta[0]), 0.]])
        chi, cp, cpp, f, fp, fpp = o._lift_scalar(float(s))
        F = o.synth(y)+f*er
        Fs = o.synth(v)+fp*er
        Fss = o.synth(acc)+fpp*er
        F[:, 2] += chi*self.height
        Fs[:, 2] += cp*self.height
        Fss[:, 2] += cpp*self.height
        Fphi = o.angular(y)+f*rho[:, None]*et
        Fsphi = o.angular(v)+fp*rho[:, None]*et
        Fphiphi = o.angular(y, order=2)+f*(rho_phi[:, None]*et-rho[:, None]**2*er)
        return {name:value[0] for name,value in dict(F=F, Fs=Fs,
            Fphi=Fphi, Fss=Fss, Fsphi=Fsphi, Fphiphi=Fphiphi).items()}

    def read(self, cell, u, phi):
        z = self.fields(cell, u, phi)
        v, d = z['Fs'], z['Fphi']
        cross = np.cross(v, d)
        area = np.linalg.norm(cross)
        n = cross/area
        E, F, G = v@v, v@d, d@d
        e, f, g = n@z['Fss'], n@z['Fsphi'], n@z['Fphiphi']
        trace = (e*G+g*E-2*f*F)/(area*area)
        gauss = (e*g-f*f)/(area*area)
        gap = np.sqrt(max(0., trace*trace-4*gauss))
        kappas = np.array([(trace-gap)/2, (trace+gap)/2])
        return dict(cell=int(cell), u=float(u), phi=float(phi),
            s=float(self.o.mesh[cell]+np.diff(self.o.mesh)[cell]*u),
            principal_curvatures=kappas.tolist(),
            maximum_absolute_principal_curvature=float(np.max(np.abs(kappas))),
            radius=float(np.linalg.norm(z['F'])), area=float(area))


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--repo', type=Path, required=True)
    p.add_argument('--bundle', type=Path, required=True)
    p.add_argument('--carrier', type=Path, required=True)
    p.add_argument('--stage', type=int, required=True)
    p.add_argument('--angle', type=int, required=True)
    p.add_argument('--angles', type=int, default=2048)
    p.add_argument('--diameter-point-lower', type=float, required=True)
    p.add_argument('--out', type=Path, required=True)
    a = p.parse_args()
    if a.out.exists():
        raise FileExistsError('Use a fresh readout path')
    topic = a.repo/'topics/visible-flex-larger-amplitude'
    dense_path = topic/'notes/2026-11-17-parallel-geometry-fullclosed-gram-operator.py'
    observed_path = topic/'scripts/resume_20261120/gauss_observed_closed_gram.py'
    dense = load('local_extremum_dense', dense_path)
    observed = load('local_extremum_observed', observed_path)
    with np.load(a.bundle, allow_pickle=False) as data:
        field = LocalField(dense, observed, data)
    with np.load(a.carrier, allow_pickle=False) as carrier:
        cell = int(carrier['observation_cells'][a.stage])
        u = float(carrier['observation_u'][a.stage])
    phi = 2*np.pi*a.angle/a.angles
    initial = field.read(cell, u, phi)
    objective = lambda x: -field.read(cell, x[0], x[1])['maximum_absolute_principal_curvature']
    result = minimize(objective, [u, phi], method='Nelder-Mead',
        bounds=((0., 1.), (0., np.pi/2)),
        options=dict(xatol=2.e-10, fatol=2.e-10, maxiter=300))
    final = field.read(cell, *result.x)
    record = dict(schema='closed-local-curvature-witness-v1',
        source_sha256=sha(__file__), bundle_sha256=sha(a.bundle),
        carrier_sha256=sha(a.carrier), dense_sha256=sha(dense_path),
        observed_sha256=sha(observed_path), initial_stage=a.stage,
        initial_angle=a.angle, affine=field.affine, initial=initial, final=final,
        optimizer=dict(method='Nelder-Mead', success=bool(result.success),
            message=str(result.message), iterations=int(result.nit), evaluations=int(result.nfev),
            xatol=2.e-10, fatol=2.e-10, maxiter=300),
        supplied_diameter_point_lower=a.diameter_point_lower,
        final_necessary_reach_product=.03*a.diameter_point_lower*
            final['maximum_absolute_principal_curvature'],
        continuous_upper_bound_certified=False, reach_certified=False,
        new_point_lower_witness_only=True)
    a.out.write_text(json.dumps(record, indent=2)+'\n')
    print(json.dumps(record), flush=True)


if __name__ == '__main__':
    main()
