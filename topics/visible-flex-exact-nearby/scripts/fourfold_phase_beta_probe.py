#!/usr/bin/env python3
"""Floating R50 finite-part phase probe for the explicitly symmetrized graph.

Frozen binary spline coefficients define real scalar functions. Physical
beta/radius are symmetrized evenly, gamma evenly after odd reflection, and
Z is the odd symmetrization of the EXACT integral of the stored slope.
This evaluator is floating, including its primitive and quadrature. It is
not an interval beta certificate or a completed scattering realization.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path

import numpy as np
from numpy.polynomial import Chebyshev, Polynomial
from numpy.polynomial.legendre import leggauss
from scipy.interpolate import BSpline
from scipy.optimize import brentq

from fourfold_phase_geometry import PhaseGeometry, tangent_radial_jets


def product_jets(a, b):
    return np.stack([sum(math.comb(j, k)*a[k]*b[j-k]
                         for k in range(j+1)) for j in range(len(a))])


class SymmetricFrozenGeometry(PhaseGeometry):
    """Same R33 definition as the directed sym root package, floating only."""
    def __init__(self, snapshot, quarter_nodes=256):
        with np.load(snapshot, allow_pickle=False) as saved:
            self.frozen = {key: saved[key].copy() for key in saved.files}
        f = self.frozen
        self.alpha = f['alpha']
        self.nodes = quarter_nodes
        self.modes = f['phase_coefficients'].shape[1]
        if self.nodes % 4 or self.nodes < 4*self.modes+8:
            raise ValueError('quarter nodes must be a multiple of four >=4M+8')
        self.frequency = 4*np.fft.fftfreq(self.nodes, 1/self.nodes)
        angles = np.arange(self.nodes)*(np.pi/2)/self.nodes
        self.sine = np.sin(4*np.arange(1, self.modes+1)[:, None]*angles)
        self.raw = BSpline(f['phase_knots'], f['phase_coefficients'], 5)
        self.base = BSpline(f['base_knots'], f['base_radius_coefficients'], int(f['base_degree']))
        self.radius = [self.base]+[BSpline(f[f'mean{j}_knots'],
                        f[f'mean{j}_radius_coefficients'], int(f[f'mean{j}_degree']))
                        for j in range(len(self.alpha))]
        self.shift = BSpline(f['shift_knots'], f['shift_coefficients'], int(f['shift_degree']))
        self.slopes = [BSpline(f[f'height{j}_slope_knots'],
                        f[f'height{j}_slope_coefficients'], int(f[f'height{j}_slope_degree']))
                        for j in range(len(self.alpha)+1)]
        self.amplitudes = np.r_[1., self.alpha]
        self._cache = {}
        self.directions = None

    def raw_physical_phase(self, x):
        raw = np.stack([self.raw(x, nu=j) for j in range(4)])
        base = np.stack([self.base(x, nu=j) for j in range(4)])[:, :, None]
        out = []
        for component, exponent in enumerate((3, 2)):
            field = raw[..., component]
            for _ in range(exponent):
                field = product_jets(field, base)
            out.append(field)
        return np.stack(out, axis=-1)

    def scalar_means(self, x):
        mean = np.zeros((4, len(x), 3))
        for j in range(4):
            parity = (-1)**j
            for amplitude, sp in zip(self.amplitudes, self.radius):
                mean[j, :, 0] += amplitude*.5*(sp(x, nu=j)+parity*sp(-x, nu=j))
            mean[j, :, 0] += .5*(self.shift(x, nu=j)+parity*self.shift(-x, nu=j))
            for amplitude, sp in zip(self.amplitudes, self.slopes):
                if j:
                    z = .5*(sp(x, nu=j-1)-parity*sp(-x, nu=j-1))
                else:
                    z = np.array([.5*(sp.integrate(0., float(v))-sp.integrate(0., -float(v)))
                                  for v in x])
                mean[j, :, 2] += amplitude*z
        return mean

    def radial_coefficients(self, x):
        x = np.atleast_1d(x)
        key = x.tobytes()
        if key in self._cache:
            return self._cache[key]
        reflection = ((-1.)**np.arange(4))[:, None, None, None]*np.array([1., -1.])
        phase = .5*(self.raw_physical_phase(x)+reflection*self.raw_physical_phase(-x))
        tangent, aux = tangent_radial_jets(phase, self.sine)
        primitive = self.primitive_coefficients(tangent)
        mean = self.scalar_means(x)
        radial = []
        for j in range(4):
            coef = sum(math.comb(j, k)*mean[k, :, 0, None, None]*primitive[j-k]
                       for k in range(j+1))
            coef[:, 0, 2] += mean[j, :, 2]
            radial.append(coef)
        value = dict(radial=radial, mean=mean, phase=phase, primitive=primitive, auxiliary=aux)
        if len(self._cache) >= 3:
            self._cache.pop(next(iter(self._cache)))
        self._cache[key] = value
        return value

    def radial_cuts(self, left, right):
        knots = [v for key, v in self.frozen.items() if key.endswith('_knots')]
        cuts = np.unique(np.concatenate([np.array([left, right])]+knots+[-v for v in knots]))
        return cuts[(cuts >= left)&(cuts <= right)]


def dot(a, b):
    return np.sum(a*b, axis=-1)


def phase_density(geometry, radial, angular_count=128, zero_order='ground-state'):
    radial = np.atleast_1d(radial)
    theta = np.arange(angular_count)*(np.pi/2)/angular_count
    x, angle = np.broadcast_arrays(radial[:, None], theta[None, :])
    F, X, Y, Frr, Frt, Ftt, *_ = geometry.paired_jets(x, angle)
    cross = np.cross(Y, X)
    cr = np.cross(Frt, X)+np.cross(Y, Frr)
    ct = np.cross(Ftt, X)+np.cross(Y, Frt)
    area2 = dot(cross, cross)
    radius2 = dot(F, F)
    support_raw = dot(cross, F)
    zeta = support_raw/np.sqrt(area2*radius2)
    lraw, mraw, nraw = [dot(cross, v) for v in (Frr, Frt, Ftt)]
    factor = zeta*zeta*area2
    a, b, c = -nraw/factor, mraw/factor, -lraw/factor
    curvature = (lraw*nraw-mraw*mraw)/area2**2
    target = geometry.radial_target_metric(radial)
    K = target['K'][:, None]
    Kp = -target['minus_K_x'][:, None]
    if np.any(K >= 0) or np.any(a <= 0) or np.any(zeta <= 0):
        raise ValueError('floating negative-core chart gate failed')
    logzr = dot(cr, F)/support_raw-dot(cross, cr)/area2-dot(F, X)/radius2
    logzt = dot(ct, F)/support_raw-dot(cross, ct)/area2-dot(F, Y)/radius2
    fr, ft = Kp/(2*K)-2*logzr, -2*logzt
    mu = np.sqrt(-K)/zeta**2
    omega = (curvature-K)/(zeta**4*a)
    chat = b*b/a+K/(zeta**4*a)
    U = F/np.sqrt(radius2)[..., None]
    Ur = (X-U*dot(U, X)[..., None])/np.sqrt(radius2)[..., None]
    Ut = (Y-U*dot(U, Y)[..., None])/np.sqrt(radius2)[..., None]
    d = a*dot(Ur, Ur)+2*b*dot(Ur, Ut)+c*dot(Ut, Ut)
    if zero_order == 'ground-state':
        if np.any(radial == 0) or np.any(F[..., 2]/x <= 0):
            raise ValueError('floating Fz/r gate failed; no division at zero is used')
        ell = Y[..., 2]/F[..., 2]-dot(F, Y)/radius2
    elif zero_order == 'unmodified-d':
        ell = np.zeros_like(a)
    else:
        raise ValueError(zero_order)
    zero_term = d+omega*(ell*ell+ell*ft)
    gradient_term = .25*(a*fr*fr+2*b*fr*ft+chat*ft*ft)
    density = (zero_term-gradient_term)/mu
    diagnostics = dict(minimum_a=float(a.min()), minimum_zeta=float(zeta.min()),
        minimum_area=float(np.sqrt(area2).min()), maximum_actual_N=float((nraw/np.sqrt(area2)).max()),
        minimum_Fz_over_r=float(np.min(F[..., 2]/x)),
        maximum_abs_omega=float(abs(omega).max()), minimum_K=float(K.min()), maximum_K=float(K.max()))
    return np.mean(density, axis=1), diagnostics


def integrate_bulk(geometry, right, gauss_order, angles, zero_order):
    cuts = geometry.radial_cuts(0., right)
    t, w = leggauss(gauss_order)
    points = (.5*(cuts[1:]+cuts[:-1])[:, None]+.5*np.diff(cuts)[:, None]*t).ravel()
    weights = (.5*np.diff(cuts)[:, None]*np.broadcast_to(w, (len(cuts)-1, len(w)))).ravel()
    total = 0.
    gates = []
    for first in range(0, len(points), 16):
        value, diagnostics = phase_density(geometry, points[first:first+16], angles, zero_order)
        total += float(np.dot(weights[first:first+16], value))
        gates.append(diagnostics)
    diag = {k:(max if k.startswith('maximum') else min)(g[k] for g in gates) for k in gates[0]}
    return total, dict(radial_cells=len(cuts)-1, quadrature_nodes=len(points), **diag)


def fit_collar(geometry, root, width, degree, angles, zero_order):
    # Values remain separated from the floating root. Exact interval/Taylor
    # evaluation at rho=0 must replace this extrapolation in a certificate.
    count = max(24, 3*(degree+1))
    nodes = np.cos((np.arange(count)+.5)*np.pi/count)
    rho = width*(.625+.375*nodes)  # [width/4,width]
    value, diagnostic = phase_density(geometry, root-rho, angles, zero_order)
    scaled = value*rho**2.5
    model = Chebyshev.fit(rho/width, scaled, degree, domain=[0., 1.]).convert(kind=Polynomial)
    coeff = model.coef
    factors = np.arange(len(coeff), dtype=float)-1.5
    finite_part = float(width**(-1.5)*np.sum(coeff/factors))
    check_rho = width*np.linspace(.25, 1., 37)
    check_value, _ = phase_density(geometry, root-check_rho, angles, zero_order)
    discrepancy = np.max(abs(model(check_rho/width)-check_value*check_rho**2.5))
    return finite_part, dict(width=width, degree=degree, fit_nodes=count,
        scaled_polynomial_coefficients=coeff.tolist(), g0=float(coeff[0]), g1=float(coeff[1]/width),
        scaled_off_grid_discrepancy=float(discrepancy),
        limitation='Floating polynomial extrapolation is diagnostic, not a root Taylor enclosure',
        **diagnostic)


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--frozen-inputs', type=Path, required=True)
    ap.add_argument('--quarter-nodes', type=int, default=256)
    ap.add_argument('--angles', type=int, default=128)
    ap.add_argument('--gauss', type=int, default=8)
    ap.add_argument('--collars', type=float, nargs='+', default=[1/2048, 1/4096])
    ap.add_argument('--fit-degrees', type=int, nargs='+', default=[5, 7])
    ap.add_argument('--zero-order', choices=['ground-state', 'unmodified-d'], default='ground-state')
    ap.add_argument('--out', type=Path, required=True)
    args = ap.parse_args()
    geometry = SymmetricFrozenGeometry(args.frozen_inputs, args.quarter_nodes)
    root = brentq(lambda x: float(geometry.radial_target_metric([x])['K'][0]),
                  .2383698, .2383701, xtol=5e-15)
    metadata = json.loads(str(geometry.frozen['metadata']))
    report = dict(kind='floating_full_R50_beta_finite_part_probe_not_certificate',
        frozen_inputs=str(args.frozen_inputs), frozen_sha256=hashlib.sha256(args.frozen_inputs.read_bytes()).hexdigest(),
        checkpoint_sha256=metadata['checkpoint_sha256'],
        script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        geometry_dependency_sha256=hashlib.sha256(Path(__file__).with_name('fourfold_phase_geometry.py').read_bytes()).hexdigest(),
        exact_object_definition='Physical beta and radius even averages; gamma odd average; Z odd average of exact integral of frozen slope, without Gaussian smoothing',
        zero_order=args.zero_order,
        zero_order_convention=('R37 ell=d_theta log(Fz/r)-d_theta log|F|, chi=1 throughout negative core'
            if args.zero_order=='ground-state' else 'principal-only R37 modification retaining original d; not ground-state cap compatible'),
        quarter_nodes=args.quarter_nodes, angular_quadrature_nodes=args.angles,
        gauss_order=args.gauss, finite_primitive_positive_root=root,
        full_phase_frequency='n=4j; beta is coefficient of 1/j',
        half_core_to_beta_factor=.5, runs=[],
        limitations=['Ordinary floating spline/trigonometric/FFT/ODE-free arithmetic and quadrature',
                     'Finite primitive differs from the exact infinite graph; no full beta tail or rounding certificate',
                     'Endpoint subtraction coefficients come from polynomial extrapolation, not directed Taylor bounds',
                     'Finite samples of chart/ground-state inequalities are not continuous certificates',
                     'R46 complete cap/strict/root network hypotheses and strong constants remain separate inputs',
                     'No exact metric, fixed cap, closed flexible family, visibility, or reach assertion'])
    for width in args.collars:
        if width <= 0 or width >= root:
            raise ValueError('invalid positive collar width')
        bulk, gates = integrate_bulk(geometry, root-width, args.gauss, args.angles, args.zero_order)
        for degree in args.fit_degrees:
            collar, detail = fit_collar(geometry, root, width, degree, args.angles, args.zero_order)
            row = dict(collar_width=width, fit_degree=degree, bulk_integral=bulk,
                       collar_finite_part=collar, beta_float=.5*(bulk+collar), bulk_diagnostics=gates,
                       collar_diagnostics=detail)
            report['runs'].append(row)
            args.out.parent.mkdir(parents=True, exist_ok=True)
            args.out.write_text(json.dumps(report, indent=2)+'\n')
            print(json.dumps({k:row[k] for k in ('collar_width','fit_degree','bulk_integral','collar_finite_part','beta_float')}), flush=True)
    report['finished']=True
    args.out.write_text(json.dumps(report, indent=2)+'\n')


if __name__ == '__main__':
    main()
