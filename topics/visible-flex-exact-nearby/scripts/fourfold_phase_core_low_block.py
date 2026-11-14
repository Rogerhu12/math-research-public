#!/usr/bin/env python3
"""Actual R37 physical-core Fourier block, retaining both Cauchy channels.

This first runner is floating exploration of a specified exact affine graph.
It evaluates the genuine R37 coefficients (including its original zero-order
term and the complete ground-state-preserving correction). It does not claim
an interval ODE certificate, a tail Schur inverse, or a positive-cap solve.
No principal ray map or ideal Airy reflection is substituted for this block.
"""
from __future__ import annotations

import argparse
from fractions import Fraction
import hashlib
import json
from pathlib import Path
import time

import numpy as np
from scipy.integrate import solve_ivp
from scipy.linalg import solve

from fourfold_phase_symmetric_geometry import load_exact_object


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def dot(left, right):
    return np.sum(left*right, axis=-1)


def uniform_fields(geometry, radial, angles):
    """Same finite radial primitive, evaluated by exact Fourier folding.

    Floating only. The angular derivatives retain the exact tangent formula;
    they are not derivatives of the truncated primitive.
    """
    theta = np.arange(angles)*(np.pi/2)/angles
    data = geometry.radial_coefficients(np.array([radial]))
    pure = []
    indices = (np.asarray(geometry.frequency, dtype=int)//4) % angles
    for source in data['radial'][:3]:
        padded = np.zeros((angles, 3), dtype=complex)
        np.add.at(padded, indices, source[0])
        pure.append((angles*np.fft.ifft(padded, axis=0)).real)
    phase = data['phase'][:, 0]
    modes = 4*np.arange(1, geometry.modes+1)
    sine, cosine = np.sin(modes[:, None]*theta), np.cos(modes[:, None]*theta)
    b, g = phase[0].T@sine
    br, gr = phase[1].T@sine
    bt, gt = phase[0].T@(modes[:, None]*cosine)
    sb, cb, sg, cg = np.sin(b), np.cos(b), np.sin(g), np.cos(g)
    zero = np.zeros(angles)
    eh = np.stack((-sb, cb, zero), axis=-1)
    ep = np.stack((-cb, -sb, zero), axis=-1)
    ez = np.stack((zero, zero, np.ones(angles)), axis=-1)
    T = cg[:, None]*eh+sg[:, None]*ez
    eg = -sg[:, None]*eh+cg[:, None]*ez
    Tr = (cg*br)[:, None]*ep+gr[:, None]*eg
    Ttheta = (cg*(1+bt))[:, None]*ep+gt[:, None]*eg
    a, ar = data['mean'][:2, 0, 0]
    return pure[0], pure[1], a*T, pure[2], ar*T+a*Tr, a*Ttheta


def physical_coefficients(geometry, radial, angles):
    """Unnormalised divergence density A,d in R37, in the physical angle.

    nraw=(F_theta cross F_r).F_thetatheta is negative in this core.
    No positive-height division is used in the principal coefficients.
    At r=0, ell uses the exact removable F_z/r logarithmic derivative.
    """
    F, X, Y, Frr, Frt, Ftt = uniform_fields(geometry, radial, angles)
    cross = np.cross(Y, X)
    G, R2, support = dot(cross, cross), dot(F, F), dot(cross, F)
    l, m, n = [dot(cross, value) for value in (Frr, Frt, Ftt)]
    if np.min(G) <= 0 or np.min(R2) <= 0 or np.min(support) <= 0 or np.max(n) >= 0:
        raise ValueError('physical core area/support/N denominator failed')
    factor = R2/support**2
    a, b, c = -n*factor, m*factor, -l*factor
    K0 = float(geometry.radial_target_metric([radial])['K'][0])
    chat = -(m*m+K0*G*G)*factor/n
    omega = c-chat
    FX, FY = dot(F, X), dot(F, Y)
    d = (a*(dot(X, X)-FX*FX/R2)
         +2*b*(dot(X, Y)-FX*FY/R2)
         +c*(dot(Y, Y)-FY*FY/R2))/R2
    if radial == 0:
        if np.min(X[:, 2]) <= 0:
            raise ValueError('removable waist height derivative is not positive')
        ell = Frt[:, 2]/X[:, 2]-FY/R2
    else:
        if np.min(F[:, 2]/radial) <= 0:
            raise ValueError('F_z/r positivity failed')
        ell = Y[:, 2]/F[:, 2]-FY/R2
    return dict(a=a, b=b, c=chat, d0=d, omega=omega, ell=ell,
                tau=d+omega*ell*ell, sigma=omega*ell,
                Yz=F[:, 2]/np.sqrt(R2),
                Yz_r=X[:, 2]/np.sqrt(R2)-F[:, 2]*FX/R2**1.5,
                Yz_theta=Y[:, 2]/np.sqrt(R2)-F[:, 2]*FY/R2**1.5,
                K0=K0, a_min=float(np.min(a)), Nraw_max=float(np.max(n)),
                support_min=float(np.min(support)))


class CoreBlock:
    """Galerkin projection of the original second-order divergence equation.

    P_N(a w_r+b D w)=p. In particular A_N is inverted after projection;
    projecting the pointwise inverse a^-1 would define another finite block.
    """
    def __init__(self, object_path, modes, primitive_nodes=512, angles=1024):
        self.geometry, self.definition = load_exact_object(object_path, primitive_nodes)
        self.object_path = Path(object_path)
        self.modes, self.angles = int(modes), int(angles)
        if self.modes < 0 or angles <= 4*self.modes:
            raise ValueError('insufficient finite angular grid')
        self.indices = np.arange(-self.modes, self.modes+1)
        self.frequency = 4*self.indices
        self.count = len(self.indices)
        self.D = np.diag(1j*self.frequency)
        self.lag = self.indices[:, None]-self.indices[None, :]
        self.calls = 0
        self.minimum_a = np.inf
        self.maximum_generator_defect = 0.
        self.maximum_ground_projection_defect = 0.

    def fourier(self, values):
        coefficients = np.fft.fft(values)/self.angles
        # Exact conjugate symmetry of these real scalar coefficients is
        # enforced only in this floating finite representation.
        return (coefficients+np.conj(coefficients[(-np.arange(self.angles)) % self.angles]))/2

    def coefficients(self, radial):
        values = physical_coefficients(self.geometry, float(radial), self.angles)
        fourier = {name:self.fourier(values[name]) for name in ('a', 'b', 'c', 'tau', 'sigma')}
        scalar = {name:coeff[self.lag % self.angles] for name, coeff in fourier.items()}
        scalar['H'] = scalar.pop('tau')+4j*self.lag*scalar.pop('sigma')
        self.minimum_a = min(self.minimum_a, values['a_min'])
        return scalar, values

    def generator(self, radial):
        coefficients, values = self.coefficients(radial)
        A, B, C, H = [coefficients[name] for name in ('a', 'b', 'c', 'H')]
        if min(np.linalg.eigvalsh(A)) <= 0:
            raise ValueError('finite radial principal block is not positive')
        inverse = solve(A, np.eye(self.count), assume_a='her')
        F11 = -inverse@B@self.D
        F12 = inverse
        F21 = self.D@B@inverse@B@self.D-self.D@C@self.D-H
        F22 = -self.D@B@inverse
        matrix = np.block([[F11, F12], [F21, F22]])
        J = self.flux_form()
        self.maximum_generator_defect = max(self.maximum_generator_defect,
            float(np.linalg.norm(matrix.conj().T@J+J@matrix, 2)))
        self.calls += 1
        return matrix

    def flux_form(self):
        eye = np.eye(self.count)
        return np.block([[np.zeros_like(eye), eye], [-eye, np.zeros_like(eye)]])

    def exact_common_cuts(self, left, right):
        left, right = Fraction(left), Fraction(right)
        cuts = {left, right}
        for key, values in self.geometry.frozen.items():
            if key.endswith('_knots'):
                for x in values:
                    q = Fraction(float(x))
                    for value in (q, -q):
                        if left < value < right:
                            cuts.add(value)
        return sorted(cuts)

    def propagate(self, left, right, tolerance, checkpoint=None):
        n = 2*self.count
        cuts = self.exact_common_cuts(left, right)
        transfer = np.eye(n, dtype=complex)
        records = []
        for a, b in zip(cuts, cuts[1:]):
            af, bf = float(a), float(b)
            if not af < bf:
                # Exact near-coincident binary knots may have no binary64
                # interior. This is numerical exploration only, and no zero
                # length is silently treated as a rigorous radial cover.
                records.append(dict(left=str(a), right=str(b), numerical_width_zero=True))
                continue
            result = solve_ivp(lambda r, y:(self.generator(r)@y.reshape(n, n)).ravel(),
                               (af, bf), transfer.ravel(), method='DOP853',
                               rtol=tolerance, atol=tolerance/20)
            if not result.success:
                raise ValueError(result.message)
            transfer = result.y[:, -1].reshape(n, n)
            records.append(dict(left=str(a), right=str(b), calls=result.nfev,
                                accepted_steps=len(result.t)-1))
            if len(records) % 20 == 0 or b == cuts[-1]:
                if checkpoint is not None:
                    np.savez_compressed(checkpoint, transfer=transfer,
                        exact_position=np.array(str(b)),
                        completed_spans=np.array(json.dumps(records)))
                print(json.dumps(dict(progress='physical two-channel core',
                    completed_spans=len(records), total_spans=len(cuts)-1,
                    physical_r=str(b), calls=self.calls)), flush=True)
        return transfer, records


def core_DN(transfer, count):
    A, B = transfer[:count, :count], transfer[:count, count:]
    C, D = transfer[count:, :count], transfer[count:, count:]
    inverse = np.linalg.inv(B)
    # The two physical outward fluxes are -p(left), +p(right).
    return np.block([[inverse@A, -inverse],
                     [C-D@inverse@A, D@inverse]])


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--object', type=Path, default=Path(
        'data/phase_ring_continuation/type_fixed_step02_d5_exact_affine_step5_object.json'))
    parser.add_argument('--modes', type=int, default=4)
    parser.add_argument('--primitive-nodes', type=int, default=512)
    parser.add_argument('--angles', type=int, default=1024)
    parser.add_argument('--cut', type=Fraction, default=Fraction(1, 4))
    parser.add_argument('--tolerance', type=float, default=2e-10)
    parser.add_argument('--out', type=Path, required=True)
    args = parser.parse_args()
    wall, cpu = time.monotonic(), time.process_time()
    block = CoreBlock(args.object, args.modes, args.primitive_nodes, args.angles)
    identity = dict(object_path=str(args.object), object_sha256=sha(args.object),
        origin_inputs_sha256=block.definition['origin_inputs']['sha256'],
        direction_sha256=block.definition['direction']['sha256'],
        exact_delta_fraction=str(Fraction(int(block.definition['delta_fraction']['numerator']),
                                         int(block.definition['delta_fraction']['denominator']))))
    args.out.parent.mkdir(parents=True, exist_ok=True)
    transfer, steps = block.propagate(Fraction(0), args.cut, args.tolerance,
                                      args.out.with_suffix('.partial.npz'))
    n = block.count
    reflection = np.diag(np.r_[np.ones(n), -np.ones(n)])
    full = transfer@reflection@np.linalg.inv(transfer)@reflection
    dn = core_DN(full, n)
    J = block.flux_form()
    mean = args.modes
    nonmean = np.r_[np.arange(mean), np.arange(mean+1, n),
                    n+np.arange(mean), n+np.arange(mean+1, n)]
    means = np.array([mean, n+mean])
    snapshots = {}
    diagnostics = []
    for r in (0., float(args.cut)/2, float(args.cut)):
        matrices, values = block.coefficients(r)
        for key, value in matrices.items():
            snapshots[f'r{r.hex()}_{key}'] = value
        diagnostics.append(dict(radial_hex=r.hex(), a_min=values['a_min'],
            Nraw_max=values['Nraw_max'], support_min=values['support_min'], K0=values['K0'],
            A_minimum_eigenvalue=float(np.min(np.linalg.eigvalsh(matrices['a']))),
            mean_cross_norm=float(np.linalg.norm(matrices['H'][mean, np.arange(n) != mean]))))
    report = dict(kind='floating_actual_R37_full_two_channel_core_Galerkin_block',
        complete=True, rigorous_transfer=False, **identity,
        source_sha256=sha(__file__), dependency_sha256={name:sha(Path(__file__).with_name(name))
            for name in ('fourfold_phase_symmetric_geometry.py', 'fourfold_phase_geometry.py')},
        modes=args.modes, physical_frequencies=block.frequency.tolist(),
        primitive_nodes=args.primitive_nodes, angular_nodes=args.angles,
        exact_physical_cuts=[str(-args.cut), str(args.cut)],
        channel_order=['all retained heights w', 'all retained radial physical fluxes p'],
        angular_mean_retained=True, original_zero_order_retained=True,
        complete_ell_correction_retained=True, finite_A_inverted_after_projection=True,
        half_transfer_norm=float(np.linalg.norm(transfer, 2)),
        full_transfer_norm=float(np.linalg.norm(full, 2)),
        generator_flux_defect=block.maximum_generator_defect,
        half_transfer_flux_defect=float(np.linalg.norm(transfer.conj().T@J@transfer-J, 2)),
        full_transfer_flux_defect=float(np.linalg.norm(full.conj().T@J@full-J, 2)),
        core_DN_hermitian_defect=float(np.linalg.norm(dn-dn.conj().T, 2)),
        core_DN_singular_values=np.linalg.svd(dn, compute_uv=False).tolist(),
        core_DN_mean_cross_norm=float(np.linalg.norm(dn[np.ix_(means, nonmean)], 2)),
        radial_calls=block.calls, minimum_sampled_a=block.minimum_a,
        coefficient_snapshots=diagnostics, half_core_steps=steps,
        limitations=[
            'Infinite primitive, angular alias, floating arithmetic and radial ODE error are not certified by this exploration.',
            'This is the genuine two-channel core Galerkin model, not the full infinite-frequency Schur complement.',
            'The positive-cap DN, regular mean flux rows, canonical root frame and rigorous high-frequency feedback are separate matching inputs.',
            'No invertibility of the complete closed-surface operator or exact nonlinear family is asserted.'],
        CPU_seconds=time.process_time()-cpu, wall_seconds=time.monotonic()-wall)
    args.out.parent.mkdir(parents=True, exist_ok=True)
    array_path = args.out.with_suffix('.npz')
    np.savez_compressed(array_path, half_transfer=transfer, full_transfer=full,
                        core_DN=dn, frequencies=block.frequency, **snapshots)
    report['arrays'] = dict(path=str(array_path), sha256=sha(array_path), bytes=array_path.stat().st_size)
    args.out.write_text(json.dumps(report, indent=2)+'\n')
    print(json.dumps({key:report[key] for key in ('modes', 'radial_calls',
        'half_transfer_flux_defect', 'core_DN_hermitian_defect', 'core_DN_mean_cross_norm',
        'CPU_seconds', 'wall_seconds')}, indent=2), flush=True)


if __name__ == '__main__':
    main()
