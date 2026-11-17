"""Exact radial/Laurent compiler for the finite principal map in R39.

The input coefficients are the literal finite binary64 data, interpreted
as exact real numbers.  Every new coefficient is formed with Fraction;
only the final enclosure is converted outward to binary64.  No FFT or
sampling constructs the radial principal, and no original map is changed.

This interface intentionally rejects a packet with a cut lift: that lift
needs its own recorded finite coefficient data before being compiled.
"""
from fractions import Fraction as F
import gzip
import hashlib
import json
import math
from pathlib import Path

import numpy as np

from certify_integral_remainder_budget import quintic
from interval_prefix_metric import rational_float, prefix_numerators


HERMITE = ((1, 0, 0, -10, 15, -6),
           (0, 1, 0, -6, 8, -3),
           (F(0), F(0), F(1, 2), F(-3, 2), F(3, 2), F(-1, 2)))


def ff(value):
    return F.from_float(float(value))


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def circle_laurent(e, degree):
    """e^(i psi) sum_[r=0]^degree [e/6*(z^-3-z^3)]^r/r!."""
    e, result = F(e), {}
    for r in range(degree+1):
        amplitude = (e/6)**r/math.factorial(r)
        for j in range(r+1):
            k = 1+3*(2*j-r)
            result[k] = result.get(k, F(0))+amplitude*math.comb(r, j)*(-1)**j
    return result


def cylindrical_projection(coefficients):
    """Literal source convention: r*cos + t*sin in rotating planar axes."""
    c = [ff(v) for v in coefficients]
    if (len(c)-1) % 3:
        raise ValueError('Expected the full 3*M+1 source projection')
    M = (len(c)-1)//3
    xy, height = {1: c[0]}, {0: F(0)}
    for j in range(1, M+1):
        r, t, z = c[j], c[M+j], c[2*M+j]
        xy[1+3*j], xy[1-3*j] = (r+t)/2, (r-t)/2
        height[3*j] = z
    return xy, height


def center_weight_powers(left, right, width, jet):
    """Exact local powers in t=(s-left)/(right-left); one shared span."""
    left, right, width = F(left), F(right), F(width)
    if left >= width:
        return [F(0)]*6
    if not 0 <= left < right <= width:
        raise ValueError('A common knot must split the center-width endpoint')
    a, d = left/width, (right-left)/width
    return [width**jet*sum((F(HERMITE[jet][j])*math.comb(j, k)*a**(j-k)*d**k
                            for j in range(k, 6)), F(0)) for k in range(6)]


class IntegralPrincipalCompiler:
    """On-demand exact coefficients for the auxiliary P, never for true X."""
    def __init__(self, data_path, audit_path, checkpoint_path, angular_path, principal_path,
                 circle_degree=16):
        self.paths = tuple(Path(p) for p in (data_path, audit_path, checkpoint_path, angular_path, principal_path))
        data, audit_path, checkpoint_path, angular_path, principal_path = self.paths
        self.data = {k: v.copy() for k, v in np.load(data).items()}
        self.principal = {k: v.copy() for k, v in np.load(principal_path).items()}
        self.audit = json.loads(audit_path.read_text())
        self.angular = json.loads(angular_path.read_text())
        self.checkpoint = json.load(gzip.open(checkpoint_path, 'rt'))
        assert sha(checkpoint_path) == self.audit['source']['checkpoint_sha256'] == self.angular['checkpoint_sha256']
        assert sha(data) == self.audit['packet_sha256'] == self.angular['packet_input_sha256']
        assert sha(principal_path) == self.angular['principal_output']['sha256']
        assert self.angular['observed_exit_code'] == 0 and self.angular['continuous_core_C1_remainder_certified']
        if self.audit['cut_numerical_identity'] is not None:
            raise ValueError('An actual cut lift requires additional finite coefficient input')
        self.knots = self.data['knots']
        self.old_pm, self.old_hm = self.data['planar_modes'], self.data['height_modes']
        assert np.all(np.diff(self.knots) > 0) and self.knots[0] == 0
        assert np.all((self.old_pm-1) % 3 == 0) and np.all(self.old_hm % 3 == 0)
        assert np.all(self.old_hm >= 0) and self.old_hm[0] == 0
        assert len(set(map(int, self.old_pm))) == len(self.old_pm)
        assert len(set(map(int, self.old_hm))) == len(self.old_hm)
        self.old_P = len(self.old_pm)
        assert self.data['jets'].shape == (3, self.old_P+len(self.old_hm), len(self.knots))
        assert self.data['reference_radial_jets'].shape == self.data['phase_jets'].shape == (3, 1, len(self.knots))
        assert all(np.all(np.isfinite(v)) for v in self.data.values())
        assert np.array_equal(self.data['reference_radial_jets'][:, 0, 0], [1., 0., 0.])
        assert self.data['phase_jets'][1, 0, 0] == 0
        argv = self.audit['argv']
        self.width = ff(argv[argv.index('--center-width')+1] if '--center-width' in argv else .04)
        assert np.any(self.knots == float(self.width))
        self.er = F(self.angular['reference_phase_exact'])
        self.ec, self.epp = map(ff, self.data['phase_jets'][[0, 2], 0, 0])
        assert self.er == ff(self.principal['reference_phase']) == ff(self.audit['definition']['theta0_e'])
        assert self.ec == ff(self.principal['center_phase']) == F(self.angular['center_phase_exact'])
        self.q_gauge = ff(self.checkpoint['gauge_amplitude'])
        self.q_actual = ff(self.checkpoint['actual_primary_amplitude'])
        self.circle_degree = int(circle_degree)
        assert self.circle_degree >= 1
        modes = self.principal['modes']
        G, T = self.principal['position_coefficients'], self.principal['tangent_coefficients']
        assert len(modes) == len(G) == len(T) and len(set(map(int, modes))) == len(modes)
        assert np.all((modes-1) % 3 == 0) and np.all(np.isfinite(G)) and np.all(np.isfinite(T))
        assert np.all(G.imag == 0) and np.all(T.real == 0)
        self.G = {int(k): ff(v.real) for k, v in zip(modes, G)}
        self.T_imag = {int(k): ff(v.imag) for k, v in zip(modes, T)}
        self.E = circle_laurent(self.er, self.circle_degree)
        self.Vxy, self.Vz = cylindrical_projection(self.data['reference_initial_projection'])
        self.bT = {}
        for k, t in self.T_imag.items():
            # b=-Epp sin(3psi)/3 has coefficients +/- i*Epp/6.
            self.bT[k+3] = self.bT.get(k+3, F(0))-self.epp*t/6
            self.bT[k-3] = self.bT.get(k-3, F(0))+self.epp*t/6
        pm = set(map(int, self.old_pm)) | set(self.G) | set(self.E) | set(self.Vxy) | set(self.bT)
        hm = set(map(int, self.old_hm)) | set(self.Vz) | {0}
        self.planar_modes = np.asarray(sorted(pm), dtype=np.int64)
        self.height_modes = np.asarray(sorted(hm), dtype=np.int64)
        self.P, self.C = len(pm), len(pm)+len(hm)
        self.planar_index = {int(k): j for j, k in enumerate(self.planar_modes)}
        self.height_index = {int(k): self.P+j for j, k in enumerate(self.height_modes)}
        self.old_indices = [self.planar_index[int(k)] for k in self.old_pm]+[
                            self.height_index[int(k)] for k in self.old_hm]
        def vector(xy=None, height=None):
            result = [F(0)]*self.C
            for key, value in (xy or {}).items():
                result[self.planar_index[key]] = value
            for key, value in (height or {}).items():
                result[self.height_index[key]] = value
            return result
        Gv, Ev, Vv, Bv, ez = vector(self.G), vector(self.E), vector(self.Vxy, self.Vz), vector(self.bT), vector(height={0: F(1)})
        centers = [[F(0)]*self.C for _ in range(3)]
        for j in range(3):
            for old, new in enumerate(self.old_indices):
                centers[j][new] = ff(self.data['jets'][j, old, 0])
        self.center_C = centers
        # P=C+f*H+h0*A0+h1*A1+h2*A2.  Gauge q multiplies the source
        # Fourier projection; actual q only enters the certified G and T.
        self.H = [g-e-self.q_gauge*v for g, e, v in zip(Gv, Ev, Vv)]
        self.A = [[e+self.q_gauge*v-c for e, v, c in zip(Ev, Vv, centers[0])],
                  [z-c for z, c in zip(ez, centers[1])],
                  [b-c for b, c in zip(Bv, centers[2])]]

    def span_exact(self, index):
        """Six power rows of exact rationals, planar first and cosine-height next."""
        if not 0 <= index < len(self.knots)-1:
            raise IndexError(index)
        left, right = map(ff, self.knots[index:index+2])
        out = [[F(0)]*self.C for _ in range(6)]
        for old, new in enumerate(self.old_indices):
            coefficients, h = quintic(self.knots[index], self.knots[index+1],
                                     self.data['jets'][:, old, index:index+2])
            for j, value in enumerate(coefficients):
                out[j][new] = value
        f, h = quintic(self.knots[index], self.knots[index+1],
                       self.data['reference_radial_jets'][:, 0, index:index+2])
        weights = [center_weight_powers(left, right, self.width, k) for k in range(3)]
        for j in range(6):
            for k in range(self.C):
                out[j][k] += f[j]*self.H[k]+sum((weights[r][j]*self.A[r][k] for r in range(3)), F(0))
        return tuple(tuple(row) for row in out), h

    def span_box(self, index):
        """Outward binary64 enclosures directly consumable by R31 algebra."""
        rows, h = self.span_exact(index)
        result = np.empty((2, 6, self.C))
        for j, row in enumerate(rows):
            for k, value in enumerate(row):
                result[:, j, k] = rational_float(value)
        return (result[0], result[1]), h

    def phase_box(self, index):
        coefficients, h = quintic(self.knots[index], self.knots[index+1],
                                  self.data['phase_jets'][:, 0, index:index+2])
        result = np.asarray([rational_float(v) for v in coefficients]).T[:, :, None]
        return (result[0], result[1]), h

    def metric_numerators(self, index, auxiliary_radius_box):
        """Exact finite A/B/C enclosures; caller still pays the true-radius error."""
        cartesian, h = self.span_box(index)
        phase, hp = self.phase_box(index)
        assert hp == h
        return prefix_numerators(cartesian, phase, auxiliary_radius_box, h,
                                 self.planar_modes, self.height_modes)

    def report(self):
        return dict(formula='P=C+f*(G_N-E_N-q_gauge*V_in)+h0*(E_N+q_gauge*V_in-C0)+h1*(ez-C1)+h2*(b*T_N-C2)',
            exact_literal_fraction_coefficients=True, source_map_changed=False,
            gauge_amplitude=str(self.q_gauge), actual_primary_amplitude=str(self.q_actual),
            center_width=str(self.width), circle_degree=self.circle_degree,
            reference_phase=str(self.er), center_phase=str(self.ec), center_phase_second=str(self.epp),
            shared_spans=len(self.knots)-1, planar_coefficients=self.P,
            height_coefficients=len(self.height_modes), maximum_absolute_planar_frequency=int(max(abs(self.planar_modes))),
            maximum_height_frequency=int(max(self.height_modes)), exact_C3=True,
            exact_planar_reflection=True, exact_height_reflection=True,
            radial_degree=5, cut_lift_included=False,
            inputs_sha256={str(p): sha(p) for p in self.paths},
            scope='An exact finite principal compiler. Principal metric, physical-radius transfer, core remainder and complete closed-map conditions must be combined separately.')
