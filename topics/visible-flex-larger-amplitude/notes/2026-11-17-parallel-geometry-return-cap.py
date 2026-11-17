#!/usr/bin/env python3
"""A fixed C2 outward semicircular return cap with a Cartesian top disk.

This generates a component with an open circular cuff, not a closed body.
The source must supply exactly matching planar two-jets at that cuff.  No
currently accepted finite tail is silently declared flat or glued by this
file.  Position integrals define the exact component; Gaussian quadrature
only evaluates them.  Optional OBJ output belongs outside the repository.
"""

from __future__ import annotations
import argparse
from dataclasses import dataclass
from fractions import Fraction
import hashlib
import json
import math
from pathlib import Path

import numpy as np


def smoothstep(t):
    return t*t*t*(10+t*(-15+6*t))


def smoothstep_primitive(t):
    return t**4*(2.5+t*(-3+t))


def polynomial_integral_powers(polynomial, maximum):
    power = [Fraction(1)]
    integrals = [Fraction(1)]
    for _ in range(maximum):
        product = [Fraction(0)]*(len(power)+len(polynomial)-1)
        for i, x in enumerate(power):
            for j, y in enumerate(polynomial):
                product[i+j] += x*y
        power = product
        integrals.append(sum(x/Fraction(i+1) for i, x in enumerate(power)))
    return integrals


def decimal_outward(value, digits, upper=False):
    scale = 10**digits
    numerator = value.numerator*scale
    integer = ((numerator+value.denominator-1)//value.denominator if upper
               else numerator//value.denominator)
    return str(integer//scale)+'.'+str(integer % scale).zfill(digits)


def sqrt_outward(value, digits, upper=False):
    scale = 10**digits
    integer = math.isqrt(value.numerator*scale*scale//value.denominator)
    if upper and integer*integer*value.denominator < value.numerator*scale*scale:
        integer += 1
    return Fraction(integer, scale)


@dataclass
class ReturnCap:
    R: float
    H: float
    radius: float
    ramp: float
    quadrature: int = 32

    def __post_init__(self):
        if not (self.R > 0 and self.H >= 0 and self.radius > 0
                and 0 < self.ramp < np.pi*self.radius and self.quadrature >= 8):
            raise ValueError('Need R,radius>0, H>=0, 0<ramp<pi*radius and quadrature>=8')
        self.length = np.pi*self.radius+self.ramp
        self.half_length = self.length/2
        self.ramp_angle = self.ramp/(2*self.radius)
        self.gauss_nodes, self.gauss_weights = np.polynomial.legendre.leggauss(self.quadrature)
        self.ramp_horizontal, self.ramp_vertical = self.ramp_integral(np.array([self.ramp]))
        self.ramp_horizontal = float(self.ramp_horizontal[0])
        self.ramp_vertical = float(self.ramp_vertical[0])
        # The entire constant-curvature middle piece lies on this one circle.
        self.circle_R = self.R+self.ramp_horizontal-self.radius*np.sin(self.ramp_angle)
        self.circle_H = self.H+self.ramp_vertical+self.radius*np.cos(self.ramp_angle)
        self.top_height = 2*self.circle_H-self.H
        self.radial_maximum = self.circle_R+self.radius

    def ramp_integral(self, s):
        s = np.asarray(s, dtype=float)
        t = s[:, None]*(self.gauss_nodes+1)/(2*self.ramp)
        theta = self.ramp/self.radius*smoothstep_primitive(t)
        dx = s/2*(np.cos(theta)@self.gauss_weights)
        dz = s/2*(np.sin(theta)@self.gauss_weights)
        return dx, dz

    def meridian(self, s):
        """Actual arclength 0/1/2 jets, using exact endpoint symmetry."""
        s = np.asarray(s, dtype=float)
        shape = s.shape
        ss = s.ravel()
        if np.any(ss < 0) or np.any(ss > self.length):
            raise ValueError('Meridian parameter is outside the fixed component')
        reflected = ss > self.half_length
        v = np.minimum(ss, self.length-ss)
        on_ramp = v < self.ramp
        angle = (v-self.ramp/2)/self.radius
        angle[on_ramp] = self.ramp/self.radius*smoothstep_primitive(v[on_ramp]/self.ramp)
        curvature = np.full_like(ss, 1/self.radius)
        curvature[on_ramp] *= smoothstep(v[on_ramp]/self.ramp)
        r = self.circle_R+self.radius*np.sin(angle)
        z = self.circle_H-self.radius*np.cos(angle)
        if np.any(on_ramp):
            dx, dz = self.ramp_integral(v[on_ramp])
            r[on_ramp] = self.R+dx
            z[on_ramp] = self.H+dz
        z[reflected] = 2*self.circle_H-z[reflected]
        angle[reflected] = np.pi-angle[reflected]
        cr, sr = np.cos(angle), np.sin(angle)
        # These values are exact in the mathematical definition, including
        # the flattened two-jets at both ends.  Avoid sin(pi) roundoff here.
        start, end = ss == 0, ss == self.length
        cr[start], sr[start], cr[end], sr[end] = 1., 0., -1., 0.
        r[start | end] = self.R
        z[start], z[end] = self.H, self.top_height
        curvature[start | end] = 0.
        values = dict(r=r, z=z, theta=angle, r_s=cr, z_s=sr,
                      r_ss=-curvature*sr, z_ss=curvature*cr, kappa=curvature)
        return {name: value.reshape(shape) for name, value in values.items()}

    def jet(self, s, beta, side=1):
        """Six Cartesian jets in meridian arclength and polar azimuth.

        A material chart beta=Phi(phi) is applied by the caller with
        F_phi=rho F_beta, F_phiphi=rho^2 F_betabeta+rho_phi F_beta.
        """
        if side not in (-1, 1):
            raise ValueError('side must be +1 or -1')
        s, beta = np.broadcast_arrays(np.asarray(s, float), np.asarray(beta, float))
        p = self.meridian(s)
        er = np.stack((np.cos(beta), np.sin(beta), np.zeros_like(beta)), axis=-1)
        et = np.stack((-np.sin(beta), np.cos(beta), np.zeros_like(beta)), axis=-1)
        ez = np.zeros_like(er); ez[..., 2] = side
        def scalar(v): return v[..., None]
        F = scalar(p['r'])*er+scalar(p['z'])*ez
        Fs = scalar(p['r_s'])*er+scalar(p['z_s'])*ez
        Fb = scalar(p['r'])*et
        Fss = scalar(p['r_ss'])*er+scalar(p['z_ss'])*ez
        Fsb = scalar(p['r_s'])*et
        Fbb = -scalar(p['r'])*er
        return dict(F=F, Fs=Fs, Fbeta=Fb, Fss=Fss, Fsbeta=Fsb, Fbetabeta=Fbb)

    def disk(self, x, y, side=1):
        """Regular Cartesian top-disk chart, including its single center."""
        x, y = np.broadcast_arrays(np.asarray(x, float), np.asarray(y, float))
        if np.any(x*x+y*y > self.R*self.R*(1+8*np.finfo(float).eps)):
            raise ValueError('Point is outside the disk')
        F = np.stack((x, y, np.full_like(x, side*self.top_height)), axis=-1)
        Fx, Fy = np.zeros_like(F), np.zeros_like(F)
        Fx[..., 0] = 1.; Fy[..., 1] = 1.
        return dict(F=F, Fx=Fx, Fy=Fy, Fxx=np.zeros_like(F),
                    Fxy=np.zeros_like(F), Fyy=np.zeros_like(F))

    def paired_diameter(self):
        """Diameters concern the two fixed caps, not an unexamined source.

        If R>top_height*tan(ramp_angle), the endpoint ramps have strictly
        increasing/decreasing norm.  The maximum is on the middle circle,
        hence the paired diameter is exactly 2*(norm(circle center)+radius).
        A universally valid analytic envelope is also returned.
        """
        condition_margin = self.R-self.top_height*np.tan(self.ramp_angle)
        rational_sufficient_margin = (self.R*(1-self.ramp_angle**2/2)
                                      -(self.H+2*self.radius+self.ramp)*self.ramp_angle)
        R, H, rho, delta = map(Fraction.from_float, (self.R, self.H, self.radius, self.ramp))
        u = delta/(2*rho)
        exact_margin = R*(1-u*u/2)-(H+2*rho+delta)*u
        return dict(
            universal_upper=2*(np.hypot(self.R, self.H+self.radius)+self.radius+self.ramp),
            exact_formula_when_endpoint_monotonicity_holds=(
                2*(np.hypot(self.circle_R, self.circle_H)+self.radius)
                if self.ramp_angle < np.pi/2 and condition_margin > 0 else None),
            endpoint_monotonicity_margin=condition_margin,
            rational_sufficient_margin=rational_sufficient_margin,
            exact_binary_parameter_sufficient_margin=str(exact_margin),
            exact_binary_parameter_condition=(delta < 3*rho and u < 1 and exact_margin > 0),
            exact_formula_scope='Exact integral-defined paired cap component only; displayed value uses Gaussian evaluation of two ramp integrals')

    def rational_diameter_enclosure(self, digits=24):
        """Outward rational bounds for the actual integral-defined diameter.

        The real parameters are the exact binary64 values supplied to this
        component.  Alternating Taylor bounds are integrated as rational
        polynomials; no floating quadrature enters this enclosure.
        """
        R, H, rho, delta = map(Fraction.from_float, (self.R, self.H, self.radius, self.ramp))
        u = delta/(2*rho)
        margin = R*(1-u*u/2)-(H+2*rho+delta)*u
        if not (delta < 3*rho and u < 1 and margin > 0):
            return dict(applicable=False, reason='The explicit rational endpoint-ramp condition did not pass')
        polynomial = [Fraction(0)]*7
        polynomial[4], polynomial[5], polynomial[6] = (delta/rho*Fraction(5, 2),
                                                       -3*delta/rho, delta/rho)
        integrals = polynomial_integral_powers(polynomial, 9)
        cos_low = sum((-1)**k*u**(2*k)/math.factorial(2*k) for k in range(4))
        cos_high = cos_low+u**8/math.factorial(8)
        sin_low = sum((-1)**k*u**(2*k+1)/math.factorial(2*k+1) for k in range(4))
        sin_high = sin_low+u**9/math.factorial(9)
        Ic_low = delta*sum((-1)**k*integrals[2*k]/math.factorial(2*k) for k in range(4))
        Ic_high = Ic_low+delta*integrals[8]/math.factorial(8)
        Is_low = delta*sum((-1)**k*integrals[2*k+1]/math.factorial(2*k+1) for k in range(4))
        Is_high = Is_low+delta*integrals[9]/math.factorial(9)
        Rc_low, Rc_high = R+Ic_low-rho*sin_high, R+Ic_high-rho*sin_low
        Zc_low, Zc_high = H+Is_low+rho*cos_low, H+Is_high+rho*cos_high
        assert Rc_low > 0 and Zc_low > 0
        low = 2*(sqrt_outward(Rc_low**2+Zc_low**2, digits)+rho)
        high = 2*(sqrt_outward(Rc_high**2+Zc_high**2, digits, True)+rho)
        return dict(applicable=True, diameter_lower=decimal_outward(low, digits),
                    diameter_upper=decimal_outward(high, digits, True),
                    rational_condition_margin=str(margin),
                    method='Integrated alternating cosine degree6/8 and sine degree7/9 bounds, exact Fractions, outward integer square root',
                    scope='Paired fixed-cap component for exact binary64 parameters; no source-body bound inferred')

    def mesh(self, meridian_cells=128, angles=128, disk_rings=32, side=1):
        if min(meridian_cells, angles) < 8 or disk_rings < 1:
            raise ValueError('Need >=8 meridian cells/angles and >=1 disk ring')
        s = np.unique(np.r_[np.linspace(0, self.length, meridian_cells+1),
                            self.ramp, self.length-self.ramp])
        p = self.meridian(s)
        radial = np.r_[p['r'], self.R*(1-np.arange(1, disk_rings)/disk_rings)]
        height = np.r_[p['z'], np.full(disk_rings-1, self.top_height)]
        beta = 2*np.pi*np.arange(angles)/angles
        vertices = np.stack((radial[:, None]*np.cos(beta), radial[:, None]*np.sin(beta),
                             np.broadcast_to(side*height[:, None], (len(radial), angles))), axis=2).reshape(-1, 3)
        center = len(vertices)
        vertices = np.vstack((vertices, [0., 0., side*self.top_height]))
        faces = []
        for i in range(len(radial)-1):
            for j in range(angles):
                j1 = (j+1) % angles
                a, b, c, d = i*angles+j, i*angles+j1, (i+1)*angles+j, (i+1)*angles+j1
                faces.extend(((a, b, c), (c, b, d)))
        for j in range(angles):
            faces.append(((len(radial)-1)*angles+j,
                          (len(radial)-1)*angles+(j+1) % angles, center))
        faces = np.asarray(faces, dtype=np.int64)
        if side < 0:
            faces = faces[:, [0, 2, 1]]
        return vertices, faces, dict(cuff_vertices=list(range(angles)),
                                     cuff_boundary_edges=angles, closed=False,
                                     orientation='outward for the intended returned-cap body')


def verification(cap):
    s = np.unique(np.r_[np.linspace(0, cap.length, 2049), cap.ramp, cap.length-cap.ramp])
    p, mirror = cap.meridian(s), cap.meridian(cap.length-s)
    beta = np.linspace(0, 2*np.pi, 17)[:-1]
    jet = cap.jet(s[:, None], beta[None, :])
    E = np.sum(jet['Fs']**2, axis=2)
    mixed = np.sum(jet['Fs']*jet['Fbeta'], axis=2)
    G = np.sum(jet['Fbeta']**2, axis=2)
    comparison = ReturnCap(cap.R, cap.H, cap.radius, cap.ramp, cap.quadrature+16)
    return dict(
        symmetry_r_error=float(np.max(abs(p['r']-mirror['r']))),
        symmetry_z_error=float(np.max(abs(p['z']+mirror['z']-2*cap.circle_H))),
        meridian_unit_speed_error=float(np.max(abs(E-1))),
        cross_gram_error=float(np.max(abs(mixed))),
        angular_gram_error=float(np.max(abs(G-p['r'][:, None]**2))),
        sampled_paired_diameter_lower=float(2*np.max(np.hypot(p['r'], p['z']))),
        sampled_meridian_curvature=float(np.max(p['kappa'])),
        sampled_azimuth_curvature=float(np.max(abs(p['z_s']/p['r']))),
        top_height_quadrature_difference=abs(comparison.top_height-cap.top_height),
        circle_center_quadrature_difference=float(np.hypot(comparison.circle_R-cap.circle_R,
                                                          comparison.circle_H-cap.circle_H)),
        source_cuff_gluing_checked=False, complete_source_reach_checked=False)


def main(args):
    cap = ReturnCap(args.R, args.H, args.radius, args.ramp, args.quadrature)
    report = dict(scope=__doc__, parameters=dict(R=args.R, H=args.H, radius=args.radius,
                                                ramp=args.ramp, quadrature=args.quadrature),
                  source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                  meridian_length=cap.length, circle_center=[cap.circle_R, cap.circle_H],
                  radial_maximum=cap.radial_maximum, top_height=cap.top_height,
                  cap_height_increment=cap.top_height-cap.H,
                  principal_curvature_upper=1/cap.radius,
                  convex_completion_reach_exact=cap.radius,
                  same_cap_normal_chord_radius=cap.radius,
                  opposite_cap_distance_lower=2*cap.H,
                  fixed_cap_pair_gate_at_radius=(cap.H >= cap.radius),
                  paired_cap_diameter=cap.paired_diameter(), verification=verification(cap),
                  rational_paired_cap_diameter=cap.rational_diameter_enclosure(),
                  source_seam_requirement='At r=R,z=+-H, exact matching planar position and two-jets; finite nonflat tail is not automatically glued',
                  full_body_closed=False, full_body_reach_certified=False)
    if args.obj:
        up, fu, meta = cap.mesh(args.meridian_cells, args.angles, args.disk_rings, 1)
        down, fd, _ = cap.mesh(args.meridian_cells, args.angles, args.disk_rings, -1)
        vertices = np.vstack((up, down)); faces = np.vstack((fu, fd+len(up)))
        lines = ['# two C2 return-cap components; two open cuff circles; no source body\n']
        lines.extend('v %.17g %.17g %.17g\n' % tuple(v) for v in vertices)
        lines.extend('f %d %d %d\n' % tuple(f+1) for f in faces)
        raw = ''.join(lines).encode()
        if len(raw) >= 5*1024*1024:
            raise ValueError('Requested OBJ exceeds 5 MB; reduce the display mesh')
        args.obj.write_bytes(raw)
        report['obj'] = dict(vertices=len(vertices), faces=len(faces), bytes=len(raw),
                             sha256=hashlib.sha256(raw).hexdigest(),
                             boundary_edges=2*meta['cuff_boundary_edges'], closed=False)
    if args.out:
        args.out.write_text(json.dumps(report, indent=2)+'\n')
    print(json.dumps(report, indent=2))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--R', type=float, required=True)
    parser.add_argument('--H', type=float, required=True)
    parser.add_argument('--radius', type=float, default=.145)
    parser.add_argument('--ramp', type=float, default=.002)
    parser.add_argument('--quadrature', type=int, default=32)
    parser.add_argument('--out', type=Path)
    parser.add_argument('--obj', type=Path)
    parser.add_argument('--meridian-cells', type=int, default=128)
    parser.add_argument('--angles', type=int, default=128)
    parser.add_argument('--disk-rings', type=int, default=32)
    main(parser.parse_args())
