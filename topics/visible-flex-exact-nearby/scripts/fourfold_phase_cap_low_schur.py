#!/usr/bin/env python3
"""Finite positive-cap Schur model with its real regular mean flux retained.

Floating exploration of the actual R74 grounded form in physical theta.
The body, natural C4 graft and true infinite exterior Robin enclosure are
kept distinct. No ideal Ai cap or boundary condition at r=3 is introduced.
The finite quadrature/Galerkin error is not certified by this runner.
"""
from __future__ import annotations

import argparse
from fractions import Fraction
import hashlib
import json
import math
from pathlib import Path
import time

import numpy as np
from numpy.polynomial import Polynomial as Poly
from numpy.polynomial.legendre import leggauss
from scipy.linalg import solve

from fourfold_phase_geometry import tangent_radial_jets
from fourfold_phase_symmetric_geometry import load_exact_object
from fourfold_phase_finite_tail_DN import finite_tail_entries
from fourfold_phase_core_low_block import dot
from flint import arb, ctx


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def trunc(poly, degree=4):
    return Poly(poly.coef[:degree+1])


def reciprocal_power(series, power, degree=4):
    constant = series.coef[0]
    q = series/constant-1
    output, term = Poly([1.]), Poly([1.])
    for j in range(1, degree+1):
        term = trunc(term*q, degree)
        output += (-1)**j*math.comb(power+j-1, j)*term
    return trunc(output/constant**power, degree)


def logarithm_series(series, degree=4):
    constant = series.coef[0]
    q = series/constant-1
    output, term = Poly([np.log(constant)]), Poly([1.])
    for j in range(1, degree+1):
        term = trunc(term*q, degree)
        output += (-1)**(j+1)*term/j
    return trunc(output, degree)


class ActualCapGeometry:
    def __init__(self, object_path, primitive_nodes):
        self.base, self.definition = load_exact_object(object_path, primitive_nodes)
        self.nodes, self.modes = self.base.nodes, self.base.modes
        self.sine, self.frequency = self.base.sine, self.base.frequency
        self.length = 1/8
        entrance = self.base.profile_jets(np.array([3.]), 4)
        phase, mean = entrance['phase'][:, 0], entrance['mean'][:, 0]
        a = Poly([mean[j, 0]/math.factorial(j) for j in range(5)])
        zprime = Poly([mean[j+1, 2]/math.factorial(j) for j in range(4)])
        loga = logarithm_series(a)
        c = trunc(zprime*reciprocal_power(a, 2), 3)
        s = Poly([0, 1])
        u = s/self.length
        self.chi = (1-u)**5*(1+5*u+15*u**2+35*u**3+70*u**4)
        self.loga = Poly(loga.coef[:2])+self.chi*Poly(np.r_[0., 0., loga.coef[2:]])
        self.c = Poly([c.coef[0]])+self.chi*Poly(np.r_[0., c.coef[1:]])
        self.z0 = mean[0, 2]
        self.phase_polynomials = []
        for component, power in enumerate((3, 2)):
            inverse = reciprocal_power(a, power)
            self.phase_polynomials.append([self.chi*trunc(
                Poly([phase[j, k, component]/math.factorial(j) for j in range(5)])*inverse)
                for k in range(self.modes)])
        self.gauss_x, self.gauss_w = leggauss(24)
        self._last = None

    def profile(self, radial):
        if radial <= 3:
            data = self.base.profile_jets(np.array([radial]), 3)
            return data['phase'], data['mean']
        if radial > 25/8:
            raise ValueError('the finite positive body ends at the actual graft endpoint')
        s = radial-3
        l = [self.loga.deriv(j)(s) for j in range(4)]
        a0 = np.exp(l[0])
        radius = np.array([a0, a0*l[1], a0*(l[2]+l[1]**2),
                           a0*(l[3]+3*l[1]*l[2]+l[1]**3)])
        c = [self.c.deriv(j)(s) for j in range(3)]
        qnodes = (self.gauss_x+1)*s/2
        z = self.z0+s/2*np.dot(self.gauss_w, np.exp(2*self.loga(qnodes))*self.c(qnodes))
        height = np.array([z, a0*a0*c[0], a0*a0*(2*l[1]*c[0]+c[1]),
            a0*a0*((2*l[2]+4*l[1]**2)*c[0]+4*l[1]*c[1]+c[2])])
        phase = np.zeros((4, 1, self.modes, 2))
        for component, power in enumerate((3, 2)):
            for k, polynomial in enumerate(self.phase_polynomials[component]):
                q = [polynomial.deriv(j)(s) for j in range(4)]
                phase[:, 0, k, component] = a0**power*np.array([
                    q[0], q[1]+power*l[1]*q[0],
                    q[2]+2*power*l[1]*q[1]+(power*l[2]+power**2*l[1]**2)*q[0],
                    q[3]+3*power*l[1]*q[2]+(3*power*l[2]+3*power**2*l[1]**2)*q[1]
                    +(power*l[3]+3*power**2*l[1]*l[2]+power**3*l[1]**3)*q[0]])
        mean = np.zeros((4, 1, 3))
        mean[:, 0, 0], mean[:, 0, 2] = radius, height
        return phase, mean

    def data(self, radial):
        if self._last is not None and radial == self._last[0]:
            return self._last[1]
        phase, mean = self.profile(radial)
        tangent, _ = tangent_radial_jets(phase, self.sine)
        # Subtract the exact circular tangent BEFORE the DFT, including the
        # tiny zeroth tangential component by half-angle identities.
        b, g = phase[0, 0].T@self.sine
        cmb, cmg = -2*np.sin(b/2)**2, -2*np.sin(g/2)**2
        tangent[0, 0, :, 1] = cmb+cmg+cmb*cmg
        primitive = self.base.primitive_coefficients(tangent)
        difference = []
        full = []
        for j in range(4):
            value = sum(math.comb(j, k)*mean[k, :, 0, None, None]*primitive[j-k]
                        for k in range(j+1))
            difference.append(value.copy())
            value[:, 0, 0] += mean[j, :, 0]
            value[:, 0, 2] += mean[j, :, 2]
            full.append(value)
        a, ar, arr = mean[:3, 0, 0]
        zr, zrr = mean[1:3, 0, 2]
        dx, ddx = difference[1][0], difference[2][0]
        e0 = 2*ar*dx[0, 0].real+np.sum(abs(dx)**2)
        e1 = (2*arr*dx[0, 0].real+2*ar*ddx[0, 0].real
              +2*np.real(np.sum(dx*np.conj(ddx))))
        E = ar*ar+zr*zr+e0
        K = (2*zr*(ar*zrr-arr*zr)+ar*e1-2*arr*e0)/(2*a*E*E)
        data = dict(phase=phase, mean=mean, radial=full, difference=difference, K=K)
        self._last = radial, data
        return data

    def coefficients(self, radial, angles):
        data = self.data(radial)
        theta = np.arange(angles)*np.pi/(2*angles)
        indices = (np.asarray(self.frequency, dtype=int)//4) % angles
        pure = []
        for source in data['radial'][:3]:
            padded = np.zeros((angles, 3), complex)
            np.add.at(padded, indices, source[0])
            pure.append((angles*np.fft.ifft(padded, axis=0)).real)
        phase = data['phase'][:, 0]
        frequency = 4*np.arange(1, self.modes+1)
        sine, cosine = np.sin(frequency[:, None]*theta), np.cos(frequency[:, None]*theta)
        b, g = phase[0].T@sine
        br, gr = phase[1].T@sine
        bt, gt = phase[0].T@(frequency[:, None]*cosine)
        sb, cb, sg, cg = np.sin(b), np.cos(b), np.sin(g), np.cos(g)
        zero = np.zeros(angles)
        eh, ep, ez = [np.stack(row, axis=-1) for row in
                      ((-sb, cb, zero), (-cb, -sb, zero), (zero, zero, np.ones(angles)))]
        T, eg = cg[:, None]*eh+sg[:, None]*ez, -sg[:, None]*eh+cg[:, None]*ez
        Tr, Tt = (cg*br)[:, None]*ep+gr[:, None]*eg, (cg*(1+bt))[:, None]*ep+gt[:, None]*eg
        a, ar = data['mean'][:2, 0, 0]
        F, X, _ = pure
        Ft, Frt, Ftt = a*T, ar*T+a*Tr, a*Tt
        cross = np.cross(Ft, X)
        G, support = dot(cross, cross), dot(F, cross)
        m, n = dot(cross, Frt), dot(cross, Ftt)
        factor = F[:, 2]**2/support**2
        A, B = -n*factor, m*factor
        C = -(m*m+data['K']*G*G)*factor/n
        eigen_lower = (A+C-np.sqrt((A-C)**2+4*B*B))/2
        if not data['K'] > 0 or np.min(eigen_lower) <= 0:
            raise ValueError('sampled actual grounded positive form failed')
        return A, B, C, data['K'], float(np.min(eigen_lower))


def block_condense(diagonal, off):
    """Exact algebra on the finite block-tridiagonal matrix (floating solve)."""
    first = diagonal[0].copy()
    link = off[0].copy()
    current = diagonal[1].copy()
    for node in range(1, len(diagonal)-1):
        inv_link = solve(current, link.conj().T, assume_a='her')
        inv_next = solve(current, off[node], assume_a='her')
        first -= link@inv_link
        link = -link@inv_next
        current = diagonal[node+1]-off[node].conj().T@inv_next
    return np.block([[first, link], [link.conj().T, current]])


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--object', type=Path, default=Path(
        'data/phase_ring_continuation/type_fixed_step02_d5_exact_affine_step5_object.json'))
    parser.add_argument('--modes', type=int, default=4)
    parser.add_argument('--primitive-nodes', type=int, default=512)
    parser.add_argument('--angles', type=int, default=512)
    parser.add_argument('--radial-elements', type=int, default=80)
    parser.add_argument('--gauss-order', type=int, default=4)
    parser.add_argument('--out', type=Path, required=True)
    args = parser.parse_args()
    wall, cpu = time.monotonic(), time.process_time()
    ctx.prec = 256
    geometry = ActualCapGeometry(args.object, args.primitive_nodes)
    tail = finite_tail_entries(Path('notes/2026-11-12-positive-family-natural-graft.json'),
        Path('notes/2026-11-12-actual-exterior-robin-certificate.json'),
        Path('notes/2026-11-12-common-core-exterior-parameter-interval.json'), args.modes)
    delta_record = geometry.definition['delta_fraction']
    delta = Fraction(int(delta_record['numerator']), int(delta_record['denominator']))
    exterior_interval = list(map(Fraction, tail['exact_parameter_interval']))
    if not exterior_interval[0] <= delta <= exterior_interval[1]:
        raise ValueError('the cap point is not contained in the actual tail certificate')
    indices = np.arange(-args.modes, args.modes+1)
    n, lag, D = len(indices), indices[:, None]-indices[None, :], np.diag(4j*indices)
    # Small physical core collar, body and actual finite graft are all kept.
    mesh = np.unique(np.r_[np.linspace(.25, .6, max(12, args.radial_elements//3)+1),
        np.linspace(.6, 3., args.radial_elements+1), np.linspace(3., 25/8, 9)])
    exact_knots = {Fraction(float(x)) for key, values in geometry.base.frozen.items()
                   if key.endswith('_knots') for x in values}
    exact_knots |= {-x for x in exact_knots}
    gx, gw = leggauss(args.gauss_order)
    diagonal = [np.zeros((n, n), complex) for _ in mesh]
    off = [np.zeros((n, n), complex) for _ in mesh[:-1]]
    minimum_eigen, minimum_K, calls = np.inf, np.inf, 0
    for cell, (left, right) in enumerate(zip(mesh, mesh[1:])):
        h = right-left
        cuts = sorted({Fraction(float(left)), Fraction(float(right))}
                      |{q for q in exact_knots if left < q < right})
        local = np.zeros((2, 2, n, n), complex)
        for exact_left, exact_right in zip(cuts, cuts[1:]):
            a, b = float(exact_left), float(exact_right)
            width = float(exact_right-exact_left)
            if width <= 0:
                continue
            for node, weight in zip((a+b)/2+width*gx/2, width*gw/2):
                aa, bb, cc, K, positive = geometry.coefficients(node, args.angles)
                minimum_eigen, minimum_K = min(minimum_eigen, positive), min(minimum_K, K)
                matrices = []
                for value in (aa, bb, cc):
                    coeff = np.fft.fft(value)/args.angles
                    matrices.append(coeff[lag % args.angles])
                A, B, C = matrices
                shape = np.array([(right-node)/h, (node-left)/h])
                derivative = np.array([-1/h, 1/h])
                for i in range(2):
                    for j in range(2):
                        local[i, j] += weight*(derivative[i]*derivative[j]*A
                            +derivative[i]*shape[j]*B@D
                            -shape[i]*derivative[j]*D@B-shape[i]*shape[j]*D@C@D)
                calls += 1
        diagonal[cell] += local[0, 0]
        diagonal[cell+1] += local[1, 1]
        off[cell] += local[0, 1]
        if (cell+1) % 30 == 0:
            print(json.dumps(dict(progress='actual grounded cap quadrature',
                elements=cell+1, total=len(mesh)-1, coefficient_calls=calls)), flush=True)
    gamma_mid = np.zeros(n)
    gamma_radius = np.zeros(n)
    for j, frequency in enumerate(indices):
        if frequency:
            value = arb(tail['entries'][abs(frequency)-1]['true_Robin']['ball'])
            gamma_mid[j], gamma_radius[j] = float(value.mid()), float(value.rad())
    diagonal[-1] += np.diag(gamma_mid)
    two_port = block_condense(diagonal, off)
    retained = np.r_[np.arange(n), n+args.modes]
    eliminated = n+np.flatnonzero(indices)
    augmented = (two_port[np.ix_(retained, retained)]
        -two_port[np.ix_(retained, eliminated)]@solve(two_port[np.ix_(eliminated, eliminated)],
            two_port[np.ix_(eliminated, retained)], assume_a='her'))
    constant = np.zeros(n+1); constant[args.modes] = constant[-1] = 1
    report = dict(kind='floating_actual_full_positive_cap_Galerkin_Schur_with_regular_mean',
        complete=True, rigorous_cap_DN=False, source_sha256=sha(__file__),
        object_path=str(args.object), object_sha256=sha(args.object), exact_delta_fraction=str(delta),
        origin_inputs_sha256=geometry.definition['origin_inputs']['sha256'],
        direction_sha256=geometry.definition['direction']['sha256'],
        actual_tail_input_sha256=tail['input_sha256'], modes=args.modes,
        physical_frequencies=(4*indices).tolist(), physical_radial_interval=['1/4', '25/8'],
        body_then_natural_graft=True, actual_infinite_exterior_retained=True,
        angular_coordinate='physical theta, no uncharged angular shear',
        root_slot='grounded U=w/Yz at physical regular core cut r=1/4',
        final_slots=['all retained left grounded heights', 'physical regular mean xi'],
        output_slots=['all retained left grounded outward conormals', 'physical regular mean flux lambda'],
        regular_mean_index=n, mean_not_eliminated=True,
        primitive_nodes=args.primitive_nodes, angular_nodes=args.angles,
        radial_elements=len(mesh)-1, radial_gauss_order=args.gauss_order, coefficient_calls=calls,
        sampled_grounded_matrix_lower=minimum_eigen, sampled_target_curvature_lower=minimum_K,
        actual_tail_chosen_midpoints=gamma_mid.tolist(), actual_tail_interval_radii=gamma_radius.tolist(),
        augmented_Hermitian_defect=float(np.linalg.norm(augmented-augmented.conj().T, 2)),
        augmented_constant_kernel_residual=float(np.linalg.norm(augmented@constant)),
        augmented_eigenvalues=np.linalg.eigvalsh(augmented).tolist(),
        actual_regular_mean_row= [[float(x.real), float(x.imag)] for x in augmented[-1]],
        regular_mean_pivot_from_left_constant=[float(augmented[-1, args.modes].real),
                                               float(augmented[-1, args.modes].imag)],
        limitations=['Primitive/angle alias, radial quadrature, floating solve and finite Galerkin errors are not certified here.',
            'The true infinite-tail entries are independently enclosed; choosing their midpoints is not silently identified with the true tail.',
            'The regular mean xi and its actual output lambda remain separate finite slots.',
            'Core-to-cap multiplication by Yz and physical flux shear remain required matching maps.',
            'No final high-frequency cutoff, infinite Schur inverse, or nonlinear solution is asserted.'],
        CPU_seconds=time.process_time()-cpu, wall_seconds=time.monotonic()-wall)
    args.out.parent.mkdir(parents=True, exist_ok=True)
    arrays = args.out.with_suffix('.npz')
    np.savez_compressed(arrays, mesh=mesh, two_port=two_port, augmented_DN=augmented,
        diagonal=np.asarray(diagonal), off=np.asarray(off), frequencies=4*indices)
    report['arrays'] = dict(path=str(arrays), sha256=sha(arrays), bytes=arrays.stat().st_size)
    args.out.write_text(json.dumps(report, indent=2)+'\n')
    print(json.dumps({key:report[key] for key in ('modes','radial_elements','coefficient_calls',
        'sampled_target_curvature_lower','augmented_Hermitian_defect',
        'augmented_constant_kernel_residual','regular_mean_pivot_from_left_constant',
        'CPU_seconds','wall_seconds')},indent=2),flush=True)


if __name__ == '__main__':
    main()
