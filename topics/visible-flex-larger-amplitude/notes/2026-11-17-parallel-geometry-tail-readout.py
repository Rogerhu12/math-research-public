#!/usr/bin/env python3
"""Actual rho=1 angular geometry of an accepted finite tail interpolant.

The P coefficients are the stored cubic-Hermite interpolant.  Its actual
physical-r derivatives determine height-compatible nonconstant K, and a
literal angular mean equation determines the constant K.  The radial jet
of this same mean root is differentiated implicitly.  No PDE RHS replaces
an interpolant derivative.  All background and state breakpoints are split,
and both one-sided jets are read at their common endpoints.

This is a new readout candidate, not the old K field.  In particular, cubic
P is only C1, so its reconstructed geometry can have radial derivative
jumps.  Reported extrema and height quadratures are numerical evidence;
there is no closed-surface, C2, embedding, or reach certificate here.
"""

from __future__ import annotations
import argparse
import gzip
import hashlib
import importlib.util
import json
from pathlib import Path
import sys
import time

import numpy as np
from scipy.interpolate import CubicHermiteSpline

TOPIC = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(TOPIC / 'scripts'))
from parallel_20261117_dynamic_tail import Background


def piece_value(pp, points, references, order=0):
    """Use the right-hand polynomial at each atomic cell's left endpoint.

    References are those left endpoints, not rounded midpoints.  This also
    defines both one-sided endpoint jets when distinct knots differ by 1 ulp.
    """
    polynomial = pp.derivative(order)
    index = np.searchsorted(polynomial.x, references, side='right') - 1
    index = np.clip(index, 0, len(polynomial.x) - 2)
    delta = points - polynomial.x[index]
    shape = (len(points),) + (1,) * (polynomial.c.ndim - 2)
    value = np.zeros_like(polynomial.c[0, index])
    for coefficient in polynomial.c:
        value = value * delta.reshape(shape) + coefficient[index]
    return value


class HeightReader:
    def __init__(self, source, background, angles, height_source='p-derivative',
                 height_gauss=8, height_anchor=None):
        self.raw = source.read_bytes()
        self.data = json.loads(gzip.decompress(self.raw))
        if not self.data.get('success'):
            raise ValueError('An actually accepted finite field is required')
        self.bg = Background(background, self.data.get('coordinate', 'physical-r'))
        if self.bg.sha256 != self.data['background_sha256']:
            raise ValueError('The fixed background SHA changed')
        self.M, self.N = self.data['M'], angles
        if angles % 4 or angles <= 4*self.M:
            raise ValueError('Need N divisible by 4 and N > 4M')
        self.frequency = 2*np.arange(1, self.M+1)
        self.angle = 2*np.pi*np.arange(angles)/angles
        self.sin = np.sin(self.angle[:, None]*self.frequency)
        self.cos = np.cos(self.angle[:, None]*self.frequency)
        self.x = np.asarray(self.data['mesh'])
        self.state = CubicHermiteSpline(self.x, np.asarray(self.data['states']),
                                       np.asarray(self.data['rhs']), axis=0)
        self.breaks = np.unique(np.r_[self.x, self.bg.x])
        if self.breaks[0] != self.x[0] or self.breaks[-1] != self.x[-1]:
            raise ValueError('State and background domains must agree exactly')
        self.height_source = height_source
        self.height_gauss = height_gauss
        self.height_anchor = height_anchor or self.bg.data.get('shallow_at', 'right')
        self.height_quadrature = None
        if height_source == 'k-integral':
            self.prepare_height_primitive()

    def coefficient_height_velocity_x(self, points, references):
        old = piece_value(self.state, points, references)
        if self.bg.coordinate == 'source-index':
            r = piece_value(self.bg.radius, points, references)
            rx = piece_value(self.bg.radius, points, references, 1)
            index = np.searchsorted(self.bg.x, references, side='right')-1
            index = np.clip(index, 0, len(self.bg.x)-2)
            rref = self.bg.r[index]
        else:
            r, rx, rref = points, np.ones_like(points), references
        w = np.exp(piece_value(self.bg.spline, r, rref))
        return (w*rx)[:, None]*old[:, self.M:2*self.M]

    def integral_coefficients(self, left, right, order):
        nodes, weights = np.polynomial.legendre.leggauss(order)
        points = (left[:, None]+(right-left)[:, None]*(nodes+1)/2).ravel()
        reference = np.repeat(left, order)
        velocity = self.coefficient_height_velocity_x(points, reference).reshape(len(left), order, self.M)
        return ((right-left)/2)[:, None]*np.einsum('ijm,j->im', velocity, weights)

    def prepare_height_primitive(self):
        left, right = self.breaks[:-1], self.breaks[1:]
        low = self.integral_coefficients(left, right, self.height_gauss)
        high = self.integral_coefficients(left, right, self.height_gauss+4)
        x_anchor = self.breaks[0] if self.height_anchor == 'left' else self.breaks[-1]
        y_anchor = self.state(x_anchor)
        r_anchor = float(self.bg.radial(np.array([x_anchor]))[0][0])
        w_anchor = float(np.exp(self.bg.spline(r_anchor)))
        anchor = -r_anchor*w_anchor*y_anchor[:self.M]/self.frequency
        prefix = np.vstack((np.zeros(self.M), np.cumsum(low, axis=0)))
        prefix_high = np.vstack((np.zeros(self.M), np.cumsum(high, axis=0)))
        start = anchor if self.height_anchor == 'left' else anchor-prefix[-1]
        start_high = anchor if self.height_anchor == 'left' else anchor-prefix_high[-1]
        self.height_nodes = start+prefix
        self.height_quadrature = dict(
            definition='H_j(anchor) fixed from the original P; H_j,r = w K_j of the actual interpolant',
            anchor=self.height_anchor, gauss_order=self.height_gauss,
            comparison_gauss_order=self.height_gauss+4,
            max_primitive_node_difference=float(np.max(abs(start+prefix-start_high-prefix_high))),
            sum_cell_max_integral_difference=float(np.sum(np.max(abs(low-high), axis=1))),
            status='Quadrature comparison, not a rigorous integration error bound')

    def height_coefficients(self, points, references):
        index = np.searchsorted(self.breaks, references, side='right')-1
        index = np.clip(index, 0, len(self.breaks)-2)
        left = self.breaks[index]
        return self.height_nodes[index]+self.integral_coefficients(left, points, self.height_gauss)

    def mean_fields(self, P, T, K, z):
        E = 1+z
        A = 2*K+K*K+E*P*P
        S = 1-z*P*P
        D = 1-z*A
        y = 1+K
        L = y+E*T
        if np.min(S) <= 0 or np.min(D) <= 0 or np.min(y) <= 0 or np.min(L) <= 0:
            raise FloatingPointError('Height-compatible mean root leaves the positive branch')
        q = np.sqrt(D)
        NN = 1+z*y*T/S
        if np.min(NN) <= 0:
            raise FloatingPointError('Angular turn density is not positive')
        B = A/(q*(1+q))+y*T/(S*q)
        BP = E*P*NN/q**3+2*z*y*T*P/(S*S*q)
        Bz = (P*P/(q*(1+q))
              + A*(A+z*P*P)*(1+2*q)/(2*q**3*(1+q)**2)
              + y*T*((A+z*P*P)/(2*S*q**3)+P*P/(S*S*q)))
        C3 = (1+q+q*q)/(q**3*(1+q))
        BK1 = K+E*T+z*L*A*C3
        BT1 = K+z*y*(A/(1+q)+P*P*q)/(S*q)
        return dict(B=B, BP=BP, Bz=Bz, BK1=BK1, BT1=BT1,
                    S=S, D=D, L=L, N=NN, y=y)

    def evaluate(self, points, references):
        old = piece_value(self.state, points, references)
        old_x = piece_value(self.state, points, references, 1)
        old_xx = piece_value(self.state, points, references, 2)
        if self.bg.coordinate == 'source-index':
            r = piece_value(self.bg.radius, points, references)
            rx = piece_value(self.bg.radius, points, references, 1)
            rxx = piece_value(self.bg.radius, points, references, 2)
            # These two splines have corresponding knot intervals.  Selecting
            # log-w by a rounded r(midpoint) can choose the other side of a
            # knot when the atomic interval is only one floating-point ulp.
            bg_index = np.searchsorted(self.bg.x, references, side='right')-1
            bg_index = np.clip(bg_index, 0, len(self.bg.x)-2)
            rref = self.bg.r[bg_index]
        else:
            r, rx, rxx, rref = points, np.ones_like(points), np.zeros_like(points), references
        if np.min(rx) <= 0:
            raise ValueError('Physical radius must increase in the numerical coordinate')
        logw = piece_value(self.bg.spline, r, rref)
        ell = piece_value(self.bg.spline, r, rref, 1)
        ell_r = piece_value(self.bg.spline, r, rref, 2)
        w = np.exp(logw)
        p = old[:, :self.M]
        pr = old_x[:, :self.M]/rx[:, None]
        prr = (old_xx[:, :self.M]-pr*rxx[:, None])/rx[:, None]**2
        if self.height_source == 'k-integral':
            hc = self.height_coefficients(points, references)
            p = -self.frequency*hc/(r*w)[:, None]
            k = old[:, self.M:2*self.M]
            kr = old_x[:, self.M:2*self.M]/rx[:, None]
            pr = -self.frequency*k/r[:, None]-(1/r+ell)[:, None]*p
        else:
            k = -((1+r*ell)[:, None]*p+r[:, None]*pr)/self.frequency
            kr = -((2+r*ell)[:, None]*pr+(ell+r*ell_r)[:, None]*p
                   + r[:, None]*prr)/self.frequency
        P, T = p@self.sin.T, (p*self.frequency)@self.cos.T
        Pr, Tr = pr@self.sin.T, (pr*self.frequency)@self.cos.T
        Kbar, Krbar = k@self.cos.T, kr@self.cos.T
        z = w[:, None]**2
        c = old[:, -1].copy()
        iterations = 0
        for iterations in range(16):
            fields = self.mean_fields(P, T, Kbar+c[:, None], z)
            mean = np.mean(fields['B'], axis=1)
            mu = 1+c+np.mean(fields['BK1']-(Kbar+c[:, None])-(1+z)*T, axis=1)
            correction = mean/mu
            c -= correction
            if np.max(abs(correction)) < 2e-17:
                break
        else:
            raise FloatingPointError('Literal sampled height-compatible mean root did not converge')
        fields = self.mean_fields(P, T, Kbar+c[:, None], z)
        mu = 1+c+np.mean(fields['BK1']-(Kbar+c[:, None])-(1+z)*T, axis=1)
        zr = 2*w*w*ell
        cr = -np.mean(fields['BP']*Pr+fields['BK1']*Krbar
                      + fields['BT1']*Tr+fields['Bz']*zr[:, None], axis=1)/mu
        K, Kr = Kbar+c[:, None], Krbar+cr[:, None]
        hperp = (-(r*w)[:, None]*p/self.frequency)@self.cos.T
        hr = w[:, None]*(1+K)
        hrr = (w*ell)[:, None]*(1+K)+w[:, None]*Kr
        hphi = (r*w)[:, None]*P
        hphiphi = (r*w)[:, None]*T
        hrphi = -w[:, None]*((k*self.frequency)@self.sin.T)
        hrphiphi = -w[:, None]*((k*self.frequency**2)@self.cos.T)
        oldK = old[:, self.M:2*self.M]@self.cos.T+old[:, -1, None]
        oldKr = ((old_x[:, self.M:2*self.M]/rx[:, None])@self.cos.T
                 + (old_x[:, -1]/rx)[:, None])
        return dict(r=r, rx=rx, w=w, wr=w*ell, c=c, cr=cr,
                    hperp=hperp, hr=hr, hrr=hrr, h_phi=hphi,
                    h_phiphi=hphiphi, hr_phi=hrphi, hr_phiphi=hrphiphi,
                    height_mean_x=rx*w*(1+c),
                    delta_P=(p-old[:, :self.M])@self.sin.T,
                    delta_K=K-oldK, delta_Kr=Kr-oldKr,
                    delta_c=c-old[:, -1], delta_cr=cr-old_x[:, -1]/rx,
                    literal_mean=np.mean(fields['B'], axis=1),
                    root_iterations=iterations+1, fields=fields)


def load_helper(path):
    before = path.read_bytes()
    spec = importlib.util.spec_from_file_location('literal_angular_reconstruct', path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    if path.read_bytes() != before:
        raise RuntimeError('Angular helper changed while it was imported')
    return module.reconstruct_slice, hashlib.sha256(before).hexdigest()


def run(args):
    started = time.perf_counter()
    source_sha = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    reader = HeightReader(args.input, args.background, args.angles, args.height_source,
                          args.height_gauss, args.height_anchor)
    reconstruct, helper_sha = load_helper(args.helper)
    fractions = np.linspace(0, 1, args.subdivisions+1)
    vandermonde = np.vander(fractions, increasing=True)
    antiderivative = fractions[:, None]**np.arange(1, len(fractions)+1)/np.arange(1, len(fractions)+1)
    partial_weights = antiderivative@np.linalg.inv(vandermonde)
    simpson = np.ones(len(fractions)); simpson[1:-1:2] = 4; simpson[2:-1:2] = 2
    simpson /= 3*args.subdivisions
    maxima = {name: 0. for name in (
        'relative_gram_operator', 'relative_rr', 'relative_rphi', 'relative_phiphi',
        'sampled_height_compatible_mean', 'delta_P', 'delta_K', 'delta_Kr', 'delta_c', 'delta_cr',
        'height_Darboux_defect', 'literal_minus_curl_alpha_r', 'radial_error_identity_gap',
        'angular_density_gap', 'actual_radial_error', 'join_position_gap',
        'join_radial_derivative_jump')}
    minima = {name: float('inf') for name in ('S', 'D', 'L', 'N', 'y',
                                            'planar_curvature', 'radial_outward_speed')}
    xyz_min, xyz_max = np.full(3, np.inf), np.full(3, -np.inf)
    worst = {}
    current_height = args.height_origin
    simpson_height = args.height_origin
    height_quadrature_difference_sum = 0.
    previous_right = None
    points_count = 0
    root_iterations = 0
    breaks = reader.breaks
    if args.max_cells:
        breaks = breaks[:args.max_cells+1]
    for begin in range(0, len(breaks)-1, args.batch_cells):
        left = breaks[begin:min(begin+args.batch_cells, len(breaks)-1)]
        right = breaks[begin+1:min(begin+args.batch_cells, len(breaks)-1)+1]
        xx = (left[:, None]+(right-left)[:, None]*fractions).ravel()
        reference = np.repeat(left, len(fractions))
        data = reader.evaluate(xx, reference)
        root_iterations = max(root_iterations, data['root_iterations'])
        for name in ('delta_P', 'delta_K', 'delta_Kr', 'delta_c', 'delta_cr'):
            maxima[name] = max(maxima[name], float(np.max(abs(data[name]))))
        maxima['sampled_height_compatible_mean'] = max(maxima['sampled_height_compatible_mean'],
                                                       float(np.max(abs(data['literal_mean']))))
        for name in ('S', 'D', 'L', 'N', 'y'):
            minima[name] = min(minima[name], float(np.min(data['fields'][name])))
        for cell, (lo, hi) in enumerate(zip(left, right)):
            offset = cell*len(fractions)
            velocity = data['height_mean_x'][offset:offset+len(fractions)]
            mean_heights = current_height+(hi-lo)*(partial_weights@velocity)
            increment = mean_heights[-1]-current_height
            simp_increment = (hi-lo)*float(simpson@velocity)
            height_quadrature_difference_sum += abs(increment-simp_increment)
            simpson_height += simp_increment
            current_height = mean_heights[-1]
            for local, fraction in enumerate(fractions):
                i = offset+local
                fields = {name: data[name][i] for name in ('r', 'w', 'wr', 'hr', 'hrr',
                           'h_phi', 'h_phiphi', 'hr_phi', 'hr_phiphi')}
                geometry = reconstruct(h=data['hperp'][i]+mean_heights[local], **fields)
                metric = geometry['relative_op']
                if np.max(metric) > maxima['relative_gram_operator']:
                    j = int(np.argmax(metric))
                    maxima['relative_gram_operator'] = float(metric[j])
                    worst = dict(value=float(metric[j]), cell=begin+cell, fraction=float(fraction),
                                 x=float(xx[i]), r=float(data['r'][i]), phi=float(reader.angle[j]),
                                 relative_rr=float(geometry['relative_rr'][j]),
                                 relative_rphi=float(geometry['relative_rphi'][j]),
                                 relative_phiphi=float(geometry['relative_phiphi'][j]))
                for name in ('relative_rr', 'relative_rphi', 'relative_phiphi', 'height_Darboux_defect',
                             'literal_minus_curl_alpha_r', 'radial_error_identity_gap',
                             'angular_density_gap', 'actual_radial_error'):
                    maxima[name] = max(maxima[name], float(np.max(abs(geometry[name]))))
                for name in ('planar_curvature', 'radial_outward_speed'):
                    minima[name] = min(minima[name], float(np.min(geometry[name])))
                xyz_min = np.minimum(xyz_min, geometry['F'].min(axis=0))
                xyz_max = np.maximum(xyz_max, geometry['F'].max(axis=0))
                if local == 0 and previous_right is not None:
                    maxima['join_position_gap'] = max(maxima['join_position_gap'],
                        float(np.max(np.linalg.norm(geometry['F']-previous_right[0], axis=1))))
                    maxima['join_radial_derivative_jump'] = max(maxima['join_radial_derivative_jump'],
                        float(np.max(np.linalg.norm(geometry['Fr']-previous_right[1], axis=1))))
                if local == len(fractions)-1:
                    previous_right = (geometry['F'], geometry['Fr'])
                points_count += reader.N
    result = dict(scope=__doc__, source_sha256=source_sha, helper_sha256=helper_sha,
                  input_sha256=hashlib.sha256(reader.raw).hexdigest(),
                  background_sha256=reader.bg.sha256, M=reader.M, N=reader.N,
                  height_source=reader.height_source, height_coefficient_quadrature=reader.height_quadrature,
                  subdivisions=args.subdivisions, atomic_cells=len(breaks)-1,
                  full_radial_domain=not bool(args.max_cells), one_sided_endpoints=True,
                  sampled_angle_radial_points=points_count, max_root_iterations=root_iterations,
                  maxima=maxima, minima=minima, worst_metric=worst,
                  sampled_position_min=xyz_min.tolist(), sampled_position_max=xyz_max.tolist(),
                  mean_height=dict(origin=args.height_origin, end=float(current_height),
                                   total_increment=float(current_height-args.height_origin),
                                   simpson_end=float(simpson_height),
                                   absolute_cell_quadrature_difference_sum=float(height_quadrature_difference_sum),
                                   status='Two quadratures of the same exact mean primitive; difference is not a rigorous error bound'),
                  seconds=time.perf_counter()-started,
                  regularity='piecewise actual geometry; no C1/C2 seam claim',
                  closed_surface=False, reach_certificate=False)
    if args.out:
        args.out.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--input', type=Path, required=True)
    parser.add_argument('--background', type=Path, required=True)
    parser.add_argument('--out', type=Path)
    parser.add_argument('--helper', type=Path, default=Path(__file__).with_name('2026-11-17-parallel-model-angular-reconstruct.py'))
    parser.add_argument('--angles', type=int, default=512)
    parser.add_argument('--subdivisions', type=int, choices=(4, 8), default=4)
    parser.add_argument('--batch-cells', type=int, default=16)
    parser.add_argument('--max-cells', type=int, default=0, help='Explicit partial probe only; zero reads all cells')
    parser.add_argument('--height-origin', type=float, default=0.)
    parser.add_argument('--height-source', choices=('p-derivative', 'k-integral'), default='p-derivative')
    parser.add_argument('--height-gauss', type=int, default=8)
    parser.add_argument('--height-anchor', choices=('left', 'right'))
    run(parser.parse_args())
