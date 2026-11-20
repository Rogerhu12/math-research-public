#!/usr/bin/env python3
"""One small independent energy/transpose check for the banded solver."""
import argparse
import hashlib
import importlib.util
import json
import sys
from pathlib import Path
import numpy as np


def load(path):
    name = 'polar_check_' + hashlib.sha256(Path(path).read_bytes()).hexdigest()[:16]
    spec = importlib.util.spec_from_file_location(name, path)
    result = importlib.util.module_from_spec(spec)
    sys.modules[name] = result
    spec.loader.exec_module(result)
    return result


def run(a):
    module, batch = load(a.source), load(a.batch)
    mesh = np.array([0., .13, .34, .72, 1.03, 1.31, 1.54, 1.8])
    times = np.empty(2*len(mesh)-1)
    times[::2] = mesh
    times[1::2] = (mesh[:-1]+mesh[1:])/2
    radius = .6
    scalar = 1-(1-radius)*times/mesh[-1]
    scalar[0], scalar[-1] = 1., radius
    o = batch.create(a.operator, mesh, scalar, radius, np.array([.003]),
                     M=3, N=64, width=.19, quarter=True, stage_block=5)
    eta = 2.e-5
    energy = module.FrozenCoreEnergy(o, regularization=eta)
    rng = np.random.default_rng(20261120)
    v, w = rng.normal(size=(2, o.free_size))
    v[:o.M-o.K] = 0.
    w[:o.M-o.K] = 0.
    Bv = energy.right_factor(v)
    BTw = energy.right_factor_transpose(w)
    adjoint = abs(Bv@w-v@BTw)/max(1., np.linalg.norm(Bv)*np.linalg.norm(w))
    # Independently interpolate scalar quintics by solving their endpoint
    # Vandermonde constraints.  Use eight Gauss nodes, not the solver's
    # five-point rows, to read its actual continuous derivative energy.
    C = np.array([[1,0,0,0,0,0],[0,1,0,0,0,0],[0,0,2,0,0,0],
                  [1,1,1,1,1,1],[0,1,2,3,4,5],[0,0,2,6,12,20]], dtype=float)
    gp, gw = np.polynomial.legendre.leggauss(8)
    def field_energy(direction):
        jets, H, _ = o.unpack(direction, tangent=True)
        Y, U = o._stage_pair(jets, 0, o.P)
        V, d = o._linear_fields(Y, U)
        V[:, :, 2] += o.lift_scalar[:, 1, None]*H
        sample = np.sum(o.multiplicity[None, :]*(np.sum(V*V, axis=2)
                          +np.sum(d*d, axis=2)/o.a[:, None]**2))
        continuous = 0.
        for i, h in enumerate(np.diff(mesh)):
            endpoints = jets[i:i+2].reshape(6, o.n).copy()
            endpoints[[1,4]] *= h
            endpoints[[2,5]] *= h*h
            coefficients = np.linalg.solve(C, endpoints)
            cuts = [0., 1.]
            breakpoint = (o.S-o.width-mesh[i])/h
            if 0 < breakpoint < 1:
                cuts.insert(1, breakpoint)
            for ul, ur in zip(cuts[:-1], cuts[1:]):
                for p, weight in zip(gp, gw):
                    u = ul+(ur-ul)*(p+1)/2
                    powers = np.array([0.,1.,2*u,3*u*u,4*u**3,5*u**4])/h
                    velocity = o.synth(powers@coefficients)
                    velocity[:, 2] += o._lift_scalar(float(mesh[i]+h*u))[1]*H
                    continuous += (ur-ul)*weight/2*np.sum(o.multiplicity*np.sum(velocity*velocity, axis=1))
        return float(sample+eta*continuous)
    actual_energy = field_energy(Bv)
    whiten = abs(actual_energy-v@v)/max(1., v@v)
    gjets, gh, _ = o.unpack(w, tangent=True)
    solution, H, diagnostics = energy.solve(gjets, gh)
    packed = energy.pack_direction(solution, H)
    inverse_via_factors = energy.right_factor(energy.right_factor_transpose(w))
    inverse_difference = np.linalg.norm(packed-inverse_via_factors)/max(1., np.linalg.norm(packed))
    report = dict(source_sha256=module.sha(a.source), operator_sha256=module.sha(a.operator),
                  batch_sha256=module.sha(a.batch), full_variables=o.free_size,
                  lower_band_width=5, local_regularization=eta,
                  transpose_relative_error=float(adjoint),
                  independent_energy_relative_error=float(whiten),
                  inverse_factor_relative_error=float(inverse_difference),
                  independent_energy=actual_energy, input_norm_squared=float(v@v),
                  solver=diagnostics)
    a.out.write_text(json.dumps(report, indent=2)+'\n')
    print(json.dumps(report), flush=True)
    if max(adjoint, whiten, inverse_difference) > 2.e-8:
        raise SystemExit('Banded physical-energy check failed')


if __name__ == '__main__':
    p = argparse.ArgumentParser(description=__doc__)
    for key in ('source','operator','batch','out'):
        p.add_argument('--'+key, type=Path, required=True)
    run(p.parse_args())
