"""n4 raw compact controls preserving mean and the physical cos(8 phi) moment.

The lambda=0 support basis is frozen at the accepted canonical order J.
The lambda=1 basis uses only the 2 by 2 weighted Gram inverse for 1 and
cos(2*n*phi). Higher represented moments may move along the homotopy.
The unused c8 row is zero. New modes beyond J have no lambda=0 primary leak.
"""
from fractions import Fraction as F
from functools import lru_cache
import hashlib
import math
from pathlib import Path
import mpmath as mp
import numpy as np
import complementary_moment_basis as canonical
import moment_interval_bounds as interval

CanonicalBasis = canonical.ComplementaryMomentBasis


@lru_cache(None)
def legacy_basis(n, J, a, eps, center, precision, quadrature_order):
    return CanonicalBasis(n, J, a, eps, center, precision, quadrature_order, False)


@lru_cache(None)
def raw_constants(n, M, a, eps, center_half_period, precision):
    with mp.workdps(precision):
        a, eps = mp.mpf(str(a)), mp.mpf(str(eps))
        T = 2 * mp.pi / n
        W = [1 - (2*a + eps) / T]
        for j in range(1, 2*M+1):
            omega = mp.mpf(n*j)
            iz = mp.j * omega * eps
            exponential = mp.exp(iz)
            integrals = [mp.expm1(iz) / iz]
            for k in range(1, 10):
                integrals.append(exponential / iz - k * integrals[-1] / iz)
            transition = eps * mp.re(mp.exp(mp.j*omega*a) * sum(
                canonical._S_COEF[k] * integrals[k] for k in range(10)))
            value = 2/T * (transition - mp.sin(omega*(a+eps))/omega)
            W.append(value * (-1)**(j*center_half_period))
        G = mp.matrix(M+1, M+1)
        for j in range(M+1):
            for k in range(M+1):
                G[j,k] = W[k] if j == 0 else W[j] if k == 0 else (W[abs(j-k)]+W[j+k])/2
        ids = (0, 2)
        low = mp.matrix([[G[j,k] for k in ids] for j in ids])
        H = mp.matrix(M-1, M+1)
        for target in range(3, M+1):
            coefficients = mp.lu_solve(low, mp.matrix([G[k,target] for k in ids]))
            H[target-2,target] = 1
            for k, value in zip(ids, coefficients):
                H[target-2,k] = -value
        moments = 2*G*H.T
        residual = max(abs(moments[k,j]) for k in ids for j in range(M-1))
        A = mp.matrix([[moments[j,k-2] for k in range(3,M+1)] for j in range(3,M+1)])
        eigen = mp.eigsy(A, eigvals_only=True)
        if eigen[0] <= 0:
            raise ArithmeticError('The raw weighted Gram Schur complement must be positive')
        D = mp.diag([1-(n*j)**2 for j in range(3,M+1)])
        singular = mp.svd(D*A, compute_uv=False)
        return dict(
            canonical_trig_coefficients=np.array([[float(H[j,k]) for k in range(M+1)] for j in range(M-1)]),
            support_condition=float(eigen[eigen.rows-1]/eigen[0]),
            rho_condition=float(singular[0]/singular[singular.rows-1]),
            high_precision_moment_residual=mp.nstr(residual,12),
            compact_primary_moment_max=float(max(abs(moments[1,j]) for j in range(M-1))))


@lru_cache(None)
def raw_enclosures(n, M, a_text, eps_text, center_half_period):
    a, eps = F(a_text), F(eps_text)
    add, neg, mul, scale, divide = (getattr(interval,key) for key in ('add','neg','mul','scale','divide'))
    pi = interval.pi_interval()
    W = [add((F(1),F(1)), neg(divide((n*(2*a+eps),)*2, scale(pi,F(2)))))]
    for j in range(1, M+3):
        si, co = interval.sincos(n*j*a)
        re, im = interval.beta_characteristic(n*j*eps)
        value = neg(divide(add(mul(si,re),mul(co,im)),scale(pi,F(j))))
        W.append(scale(value,F((-1)**(j*center_half_period))))
    def gram(j,k):
        return W[k] if j == 0 else W[j] if k == 0 else scale(add(W[abs(j-k)],W[j+k]),F(1,2))
    ids = (0,2)
    B = [[gram(j,k) for k in ids] for j in ids]
    with mp.workdps(100):
        midpoint = mp.matrix(2,2)
        for j in range(2):
            for k in range(2):
                value = (B[j][k][0]+B[j][k][1])/2
                midpoint[j,k] = mp.mpf(value.numerator)/value.denominator
        candidate = midpoint**-1
        R = [[F(mp.nstr(candidate[j,k],60)) for k in range(2)] for j in range(2)]
    residual = []
    for j in range(2):
        row = []
        for k in range(2):
            value = (F(j==k),F(j==k))
            for l in range(2):
                value = add(value,neg(scale(B[l][k],R[j][l])))
            row.append(value)
        residual.append(row)
    beta = max(sum(interval.upper_abs(v) for v in row) for row in residual)
    if beta >= 1:
        raise ArithmeticError('Mean/c8 Gram inverse lacks a rational Neumann certificate')
    rnorm = max(sum(abs(v) for v in row) for row in R)
    error = beta/(1-beta)*rnorm
    inverse = [[(v-error,v+error) for v in row] for row in R]
    H = [[(F(0),F(0))]*(M+1)]
    for target in range(3,M+1):
        row = [(F(0),F(0))]*(M+1)
        row[target] = (F(1),F(1))
        for j, frequency in enumerate(ids):
            value = (F(0),F(0))
            for k, frequency2 in enumerate(ids):
                value = add(value,mul(inverse[j][k],gram(frequency2,target)))
            row[frequency] = neg(value)
        H.append(row)
    return dict(coefficients=H,neumann_residual=beta,inverse_error=error,
                defining_identity='Each active raw control is W times cos(j*n*phi) minus its weighted projection onto {1,cos(2*n*phi)}; j>=3. Mean and physical 2n moment vanish. The unused 2n parameter row is zero.')


def make_raw_basis(anchor_modes):
    J = int(anchor_modes)
    if J < 3:
        raise ValueError('A frozen canonical anchor order J>=3 is required')

    class RawMeanC8Basis(CanonicalBasis):
        def __init__(self,base_mode=4,modes=16,halfwidth=.147,transition=.16,
                     center=np.pi/4,precision=80,quadrature_order=64,lock_fundamental=False):
            self.n, self.M = int(base_mode), int(modes)
            self.a, self.eps, self.center = float(halfwidth), float(transition), float(center)
            self.T = 2*np.pi/self.n
            self.precision = int(precision)
            self.lock_fundamental = False
            self.anchor_modes = J
            if self.n != 4 or self.M < J or lock_fundamental:
                raise ValueError('n4 raw path needs n=4, M>=frozen J, and the original unlocked primary')
            if not 0 < self.a < self.a+self.eps < self.T/2:
                raise ValueError('Invalid complementary control geometry')
            self.center_half_period = int(round(self.center/(self.T/2)))
            if self.center_half_period not in (0,1) or abs(self.center-self.center_half_period*self.T/2)>1e-12:
                raise ValueError('Only the original reflection centers are supported')
            old = legacy_basis(self.n,J,self.a,self.eps,self.center,self.precision,quadrature_order)
            self.constants = raw_constants(self.n,self.M,self.a,self.eps,self.center_half_period,self.precision)
            self.H = self.constants['canonical_trig_coefficients'].copy()
            self.fundamental_leakage = np.zeros(self.M-1)
            self.fundamental_leakage[:J-1] = old.fundamental_leakage
            self.freq = self.n*np.arange(self.M+1)
            self.target_freq = self.freq[2:]
            self.gx,self.gw = np.polynomial.legendre.leggauss(int(quadrature_order))
            self.certificate = dict(raw_enclosures(self.n,self.M,str(self.a),str(self.eps),self.center_half_period))
            self.certificate['fundamental'] = list(old.certificate['fundamental'])+[(F(0),F(0))]*(self.M-J)
            self.certificate['legacy_neumann_residual'] = old.certificate['neumann_residual']
            self.certificate['legacy_inverse_error'] = old.certificate['inverse_error']
            bounds = self.certificate['coefficients']
            cutoff = [canonical.cutoff_derivative_upper(k)/F(str(self.eps))**k for k in range(6)]
            absolute = [[interval.upper_abs(value) for value in row] for row in bounds]
            error = [[max(abs(F.from_float(float(self.H[j,k]))-v) for v in bounds[j][k])
                      for k in range(self.M+1)] for j in range(self.M-1)]
            def derivative_bounds(coeff):
                trig = [[sum(coeff[j][k]*(int(self.freq[k])**r if r else 1) for k in range(self.M+1))
                         for j in range(self.M-1)] for r in range(6)]
                return np.array([[interval.upper_float(sum(math.comb(r,l)*cutoff[l]*trig[r-l][j] for l in range(r+1)))
                                  for j in range(self.M-1)] for r in range(6)])
            self.cutoff_bounds = np.array([interval.upper_float(v) for v in cutoff])
            self.derivative_bounds = derivative_bounds(absolute)
            self.coefficient_evaluation_error_bounds = derivative_bounds(error)
            fundamental = self.certificate['fundamental']
            self.fundamental_absolute_upper = np.array([interval.upper_float(interval.upper_abs(v)) if interval.upper_abs(v) else 0. for v in fundamental])
            self.fundamental_evaluation_error = np.array([interval.upper_float(max(abs(F.from_float(float(self.fundamental_leakage[j]))-v) for v in bounds)) for j,bounds in enumerate(fundamental)])

        def summary(self):
            out = super().summary()
            out.update(
                canonical_low_moments='Mean and physical cos(8*phi) correction are zero; higher moments are free. The compact primary moment is not locked.',
                control_path='raw-mean-c8-with-frozen-canonical-low-start-v1',
                low_start_projection_order=self.anchor_modes,
                unused_correction_index=0,
                legacy_coefficient_neumann_residual_upper=interval.upper_float(self.certificate['legacy_neumann_residual']),
                legacy_coefficient_inverse_error_upper=interval.upper_float(self.certificate['legacy_inverse_error']),
                compact_primary_moment_max=self.constants['compact_primary_moment_max'],
                scope='Exact compact support and exact two low-moment constraints; only the 2 by 2 low Gram block is inverted for compact controls. The original J-dependent analytic start is frozen across M refinement.')
            return out

    return RawMeanC8Basis


def provenance(anchor_modes):
    return dict(
        definition=__doc__,anchor_modes=int(anchor_modes),
        source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        canonical_source_sha256=hashlib.sha256(Path(canonical.__file__).read_bytes()).hexdigest(),
        interval_source_sha256=hashlib.sha256(Path(interval.__file__).read_bytes()).hexdigest())
