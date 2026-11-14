#!/usr/bin/env python3
"""Independent Cartesian-jet checks of three finite-tail audit formulas.

This exercises algebra and conservative bounds on explicit analytic maps.
It is not a certificate for any supplied physical-background packet.
"""
import os
for key in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[key] = '1'
import argparse
from fractions import Fraction as Q
import hashlib
import importlib.util
import json
import math
from pathlib import Path
import sys
import numpy as np

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
path = HERE/'db6f-audit-tail-metric-curvature.py'
spec = importlib.util.spec_from_file_location('tail_formula_review_target', path)
audit = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = audit
spec.loader.exec_module(audit)
I, P = audit.I, audit.P


class Jet:
    """Value and all first/second derivatives in two Cartesian parameters."""
    def __init__(self, value, gradient=None, hessian=None):
        self.v = float(value)
        self.d = np.zeros(2) if gradient is None else np.array(gradient, float)
        self.h = np.zeros((2, 2)) if hessian is None else np.array(hessian, float)

    @staticmethod
    def get(a):
        return a if isinstance(a, Jet) else Jet(a)

    def __add__(self, b):
        b = Jet.get(b)
        return Jet(self.v+b.v, self.d+b.d, self.h+b.h)

    __radd__ = __add__

    def __neg__(self):
        return Jet(-self.v, -self.d, -self.h)

    def __sub__(self, b):
        return self+-Jet.get(b)

    def __mul__(self, b):
        b = Jet.get(b)
        return Jet(self.v*b.v, self.d*b.v+self.v*b.d,
                   self.h*b.v+self.v*b.h+np.outer(self.d, b.d)+np.outer(b.d, self.d))

    __rmul__ = __mul__

    def power(self, n):
        result = Jet(1)
        for _ in range(n):
            result = result*self
        return result

    def sin(self):
        return Jet(math.sin(self.v), math.cos(self.v)*self.d,
                   math.cos(self.v)*self.h-math.sin(self.v)*np.outer(self.d, self.d))

    def cos(self):
        return Jet(math.cos(self.v), -math.sin(self.v)*self.d,
                   -math.sin(self.v)*self.h-math.cos(self.v)*np.outer(self.d, self.d))


def derivative(c, n):
    result = list(c)
    for _ in range(n):
        result = [(j+1)*result[j+1] for j in range(len(result)-1)] or [Q(0)]
    return result


def local_coefficients(c, left, length):
    out = [Q(0) for _ in c]
    for j, z in enumerate(c):
        for k in range(j+1):
            out[k] += z*math.comb(j, k)*left**(j-k)*length**k
    return out


def scalar(c, left, length):
    c = local_coefficients(c, left, length)
    return P(audit.intervals(c)[:, None])


def field(terms, left, length, order, sine=False):
    # Terms are exact physical-r polynomial amplitudes of cos(3k theta)
    # or sin(3k theta). No audited cylindrical differentiation is reused.
    M = max(terms, default=0)
    d = max((len(derivative(c, order)) for c in terms.values()), default=1)
    raw = [[Q(0) for _ in range(2*M+1)] for _ in range(d)]
    for k, c in terms.items():
        a = local_coefficients(derivative(c, order), left, length)
        for j, v in enumerate(a):
            if not k:
                if sine and v:
                    raise ValueError('Nonzero constant sine')
                raw[j][M] += v
            elif sine:
                raw[j][M-k] += v/2
                raw[j][M+k] -= v/2
            else:
                raw[j][M-k] += v/2
                raw[j][M+k] += v/2
    lo = np.empty((d, 2*M+1))
    hi = lo.copy()
    for j in range(d):
        for k in range(2*M+1):
            q = audit.qbounds(raw[j][k])
            lo[j, k], hi[j, k] = q.lo, q.hi
    return P(I(lo, hi), -M, int(sine))


def polynomial(c, r):
    return sum((float(a)*r.power(j) for j, a in enumerate(c)), Jet(0))


def cartesian(case, rv, tv):
    r, theta = Jet(rv, [1, 0]), Jet(tv, [0, 1])
    values = []
    for axis, terms in enumerate(case['fields']):
        val = Jet(0)
        for k, c in terms.items():
            angle = 3*k*theta
            val += polynomial(c, r)*(angle.sin() if axis == 1 else angle.cos())
        values.append(val)
    R, T, Z = values
    # Differentiate the Cartesian map directly by automatic differentiation.
    h = polynomial([Q(0)]+[a/Q(j+1) for j, a in enumerate(case['w'])], r)
    return [(r+R)*theta.cos()-T*theta.sin(),
            (r+R)*theta.sin()+T*theta.cos(), h+Z]


def midpoint_value(p, u, theta):
    c = (p.c.lo/2+p.c.hi/2)
    radial = np.array([u**j for j in range(c.shape[0])])@c
    modes = np.arange(p.first, p.first+c.shape[1])
    return float(((1j**p.phase)*np.sum(radial*np.exp(3j*modes*theta))).real)


def run_case(case):
    left, right = case['interval']
    length = right-left
    fields = [[field(c, left, length, n, axis == 1)
               for axis, c in enumerate(case['fields'])] for n in range(3)]
    r = scalar([Q(0), Q(1)], left, length)
    w = scalar(case['w'], left, length)
    wr = scalar(derivative(case['w'], 1), left, length)
    metric, _, residuals, _, _, _ = audit.metric_residuals(fields, r, w)
    kp, eta, _ = audit.perturbative_curvature(fields, r, w, wr, metric, case['background_curvature'])
    M = max(max(c, default=0) for c in case['fields'])
    kd, area = audit.direct_curvature(fields, r, w, wr, audit.base.trigonometry(M, 96), metric)
    actual_metric, actual_k, formula_error, actual_area = 0., 0., 0., math.inf
    for u in np.linspace(0, 1, 11):
        rv = float(left)+float(length)*u
        wv = sum(float(a)*rv**j for j, a in enumerate(case['w']))
        for theta in np.linspace(0, 2*math.pi/3, 97):
            xyz = cartesian(case, rv, theta)
            a = np.array([x.d[0] for x in xyz])
            b = np.array([x.d[1] for x in xyz])
            G = np.array([[a@a, a@b], [a@b, b@b]])
            scale = np.diag([1/math.sqrt(1+wv*wv), 1/rv])
            defect = scale@G@scale-np.eye(2)
            em = float(np.max(np.abs(np.linalg.eigvalsh(defect))))
            cross = np.cross(a, b)
            norm = np.linalg.norm(cross)
            normal = cross/norm
            B = sum((normal[j]*xyz[j].h for j in range(3)), np.zeros((2, 2)))
            k = float(np.max(np.abs(np.linalg.eigvals(np.linalg.solve(G, B)))))
            exact_res = [G[0, 0]-(1+wv*wv), G[0, 1], G[1, 1]-rv*rv]
            observed = [midpoint_value(z, u, theta) for z in residuals]
            formula_error = max(formula_error, float(np.max(np.abs(np.subtract(exact_res, observed)))))
            actual_metric = max(actual_metric, em)
            actual_k = max(actual_k, k)
            actual_area = min(actual_area, norm)
    # These floating comparisons are diagnostics; the review gives the proof.
    assert formula_error < 2e-12, (case['name'], formula_error)
    assert actual_metric <= metric+2e-13, (case['name'], actual_metric, metric)
    assert kd is not None and actual_k <= kd+2e-12
    if kp is not None:
        assert actual_k <= kp+2e-12
    assert actual_area+2e-13 >= area
    return dict(name=case['name'], metric_upper=metric, direct_curvature_upper=kd,
                perturbative_curvature_upper=kp, covariant_hessian_upper=eta,
                sampled_cartesian_metric=actual_metric, sampled_cartesian_curvature=actual_k,
                coordinate_metric_formula_difference=formula_error,
                direct_area_lower=area, sampled_cartesian_area_lower=actual_area)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--out', type=Path, required=True)
    args = parser.parse_args()
    cases = [
        dict(name='round cone, zero perturbation', interval=(Q(2, 5), Q(3, 5)),
             w=[Q(1, 2)], fields=[{}, {}, {}], background_curvature=2.),
        dict(name='independent threefold Cartesian polynomial map', interval=(Q(2, 5), Q(3, 5)),
             w=[Q(7, 10), Q(1, 10)],
             fields=[{1: [Q(0), Q(0), Q(1, 5000)]},
                     {2: [Q(0), Q(0), Q(0), Q(-3, 10000)]},
                     {1: [Q(0), Q(1, 10000)], 2: [Q(0), Q(0), Q(0), Q(1, 25000)]}],
             background_curvature=2.),
        dict(name='large radial second jets cancel to an exact cone', interval=(Q(49, 100), Q(51, 100)),
             w=[Q(-9), Q(20)], fields=[{}, {}, {0: [Q(0), Q(19, 2), Q(-10)]}],
             background_curvature=20.)]
    results, failures = [], []
    for case in cases:
        try:
            results.append(run_case(case))
        except Exception as exc:
            failures.append(dict(name=case['name'], exception=type(exc).__name__, message=str(exc)))
    report = dict(status=('PASS formula/component review diagnostics' if not failures
                          else 'Component review found a safe rejection'),
                  scope=__doc__, audited_script=str(path),
                  audited_script_sha256=hashlib.sha256(path.read_bytes()).hexdigest(),
                  reviewer_script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                  radial_samples_per_case=11, angular_samples_per_case=97,
                  cases=results, failures=failures,
                  does_not_certify=['physical background packet validity', 'all-tail interval coverage',
                                    'complete closed-surface metric or reach', 'README completion'])
    args.out.write_text(json.dumps(report, indent=2)+'\n')
    print(json.dumps(dict(status=report['status'], cases=results, failures=failures)), flush=True)


if __name__ == '__main__':
    main()
