"""Prepared true-integral interface for the R44 endpoint control space.

This is source preparation, not an executed certificate for a candidate.
The old R36/R37/R41 sources stay unchanged.  The primary integral/Green
definition is reused with the actual primary width.  Controls are instead
the retained raw B2..B(M-2) and T=SA-SB,U=SB, at lambda=1 only.

Widths use decimal-roundtrip rationals; q and all physical controls are
the exact binary64 reals.  The mathematical reflection centre is pi/3.
The local cos(d) occurs only multiplied by the compact cutoff: it is not
periodically continued as a free global harmonic.  No source quadrature,
source inverse residual or numerical positivity guard is a rigorous bound.
"""
from fractions import Fraction as F
import math

import integral_core_intervals as ri
from fast_integral_core_intervals import FastExactRawM3Core
from generic_raw_core_intervals import (
    AdaptiveHornerCutoff, primary_constants, raw_projection,
    fixed_atlas_identity, literal_structure,
)


TRACE_KIND = 'exact_m3_circle_trace_replacement_integral'
TRACE_PATH = 'circle-trace-replace-last-two-v1'


def trace_projection(control, L):
    """Enclose the true R44 D=G^-1 V; columns are A,B before T,U conversion."""
    I = {k: ri.divide(control.complete(k)[0], L) for k in (0, 1, 2, 3, 4, 6)}
    g00 = ri.sub(ri.point(1), I[0])
    g01 = I[3]
    g11 = ri.scale(ri.sub(ri.sub(ri.point(1), I[0]), I[6]), F(1, 2))
    determinant = ri.sub(ri.mul(g00, g11), ri.power(g01, 2))
    assert g00[0] > 0 and determinant[0] > 0
    rhs = ((I[0], I[1]),
           (ri.neg(I[3]), ri.scale(ri.neg(ri.add(I[2], I[4])), F(1, 2))))
    columns = []
    for j in range(2):
        columns.append((
            ri.divide(ri.sub(ri.mul(g11, rhs[0][j]), ri.mul(g01, rhs[1][j])), determinant),
            ri.divide(ri.sub(ri.mul(g00, rhs[1][j]), ri.mul(g01, rhs[0][j])), determinant),
        ))
    D = tuple(tuple(columns[j][i] for j in range(2)) for i in range(2))
    TU = tuple((ri.sub(row[0], row[1]), row[1]) for row in D)
    return D, TU, dict(gram=(g00, g01, g11), determinant=determinant, rhs=rhs)


class ExactCircleTraceM3Core(FastExactRawM3Core):
    """R41 normal/material formulas with explicitly replaced control algebra.

The required provenance is an explicit definition descriptor containing
core_kind, core_control_path, core_round_settings, physical_controls and
core_projection_order_J.  It must be derived from the actual candidate's
full parameters/scales, not inferred from a diagnostic summary.  This
constructor does not itself establish that any BVP or metric gate passed.
"""
    def __init__(self, core, provenance):
        settings = provenance['core_round_settings']
        assert provenance['core_kind'] == TRACE_KIND
        assert provenance['core_control_path'] == TRACE_PATH
        assert core.summary()['core_kind'] == TRACE_KIND
        assert core.basis.summary()['control_path'] == TRACE_PATH
        assert core.base_mode == 3 and core.bimodal_eta == 0
        assert settings['bimodal_eta'] == 0 and settings['lock_fundamental'] is True
        assert settings['center'] == math.pi/3 and core.center == settings['center']
        for attribute, key in (('a', 'halfwidth'), ('transition', 'transition'),
                               ('control_transition', 'control_transition'), ('lam', 'homotopy')):
            assert getattr(core, attribute) == settings[key]
        self.q = F.from_float(float(core.support_amplitude))
        self.lam = F.from_float(float(core.lam))
        self.c = tuple(F.from_float(float(v)) for v in core.corrections)
        assert self.q > 0 and self.lam == 1
        assert literal_structure([float(v) for v in self.c]) == literal_structure(provenance['physical_controls'])
        self.M = len(self.c)+1
        self.keep = self.M-3
        assert self.M >= 4 and core.basis.M == self.M == provenance['core_projection_order_J']
        assert core.basis.keep == self.keep
        self.t, self.u = self.c[-2:]
        self.local_cosine_coefficient = self.u-self.t
        self.L = ri.scale(ri.pi_interval(), F(1, 3))
        self.T = ri.scale(self.L, 2)
        a, bp, bc = (F(str(settings[k])) for k in ('halfwidth', 'transition', 'control_transition'))
        assert 0 < a < a+bp < self.L[0] and a < a+bc < self.L[0]
        self.primary = AdaptiveHornerCutoff(a, bp, self.plain, 4)
        self.controls = AdaptiveHornerCutoff(a, bc, self.plain, 3*(self.M+1))
        self.beta, self.center_per_q = primary_constants(self.primary, self.L)
        self.raw_H, self.raw_projection_certificate = raw_projection(self.controls, self.L, self.M)
        self.trace_AB, self.trace_TU, self.trace_projection_certificate = trace_projection(self.controls, self.L)
        # b = W P + chi*(t+(u-t)*cos(x)).  Combine the complete physical
        # controls and low projection before any absolute-value estimate.
        D = [ri.sum_intervals(ri.scale(self.raw_H[j][k], self.c[j])
                              for j in range(self.keep)) for k in range(self.M+1)]
        for k in range(2):
            D[k] = ri.sub(D[k], ri.add(ri.scale(self.trace_AB[k][0], self.t),
                                      ri.scale(self.trace_AB[k][1], self.local_cosine_coefficient)))
        self.D = tuple(D)
        raw_error = [ri.magnitude(ri.sub(self.raw_H[j][k], ri.point(F.from_float(float(core.basis.raw.H[j, k])))))
                     for j in range(self.keep) for k in range(self.M+1)]
        trace_error = [ri.magnitude(ri.sub(self.trace_TU[i][j],
                        ri.point(F.from_float(float(core.basis.trace_projection[i, j])))))
                       for i in range(2) for j in range(2)]
        self.source_projection_coefficient_error_upper = max(raw_error+trace_error)
        self.source_coefficient_scope = ('Coefficient enclosure only. Numerical cutoff/trigonometric evaluation, '
                                        'quadrature, inverse and source jets require their separate error budgets.')
        self.global_bounds = self._global_bounds()

    def control_jets(self, x, order=4):
        assert isinstance(order, int) and 0 <= order <= 5
        chi = self.controls.jets(x, order)
        W = [ri.sub(ri.point(1), chi[0])]+[ri.neg(v) for v in chi[1:]]
        P = [ri.sum_intervals(ri.scale(ri.mul(v, self.trig(x, k, r)), (-1)**k)
                              for k, v in enumerate(self.D)) for r in range(order+1)]
        g = [ri.add(ri.point(self.t if r == 0 else 0),
                    ri.scale(ri.trig_derivative(x, 1, r), self.local_cosine_coefficient))
             for r in range(order+1)]
        return [ri.sum_intervals(ri.scale(ri.add(ri.mul(W[ell], P[r-ell]),
                                                 ri.mul(chi[ell], g[r-ell])), math.comb(r, ell))
                                 for ell in range(r+1)) for r in range(order+1)]

    def control_primitive(self, x):
        compact = ri.sum_intervals(ri.scale(ri.mul(v, ri.sub(self.plain(3*k, x)[0],
                                                  self.controls.integrals(3*k, x)[0])), (-1)**k)
                                   for k, v in enumerate(self.D))
        seed = ri.add(ri.scale(self.controls.integrals(0, x)[0], self.t),
                      ri.scale(self.controls.integrals(1, x)[0], self.local_cosine_coefficient))
        return ri.add(compact, seed)

    def _global_bounds(self):
        cut = [ri.cutoff_derivative_bound(r)/self.controls.b**r for r in range(6)]
        def frequency_power(k, r):
            return (3*k)**r if r else 1
        P = [sum(ri.magnitude(v)*frequency_power(k, r) for k, v in enumerate(self.D)) for r in range(6)]
        Prho = [sum(ri.magnitude(v)*abs(1-(3*k)**2)*frequency_power(k, r)
                    for k, v in enumerate(self.D)) for r in range(4)]
        B = abs(self.local_cosine_coefficient)
        extent = self.controls.a+self.controls.b
        g0 = min(abs(self.t)+B, abs(self.u)+B*min(F(2), extent**2/2))
        g = [g0]+[B*(min(F(1), extent) if r % 2 else 1) for r in range(1, 6)]
        support = [sum(F(math.comb(r, ell))*cut[ell]*(P[r-ell]+g[r-ell])
                       for ell in range(r+1)) for r in range(6)]
        curvature = []
        for r in range(4):
            # (W P) + (W P)'' = W(P+P'') + 2W'P' + W''P.
            window = sum(F(math.comb(r, ell))*(cut[ell]*Prho[r-ell]
                         +2*cut[ell+1]*P[r-ell+1]+cut[ell+2]*P[r-ell])
                         for ell in range(r+1))
            # g+g''=t.  Keep this cancellation before differentiating.
            seed = abs(self.t)*cut[r]+sum(F(math.comb(r, ell))*(
                        2*cut[ell+1]*g[r-ell+1]+cut[ell+2]*g[r-ell])
                        for ell in range(r+1))
            curvature.append(window+seed)
        pc = [ri.cutoff_derivative_bound(r)/self.primary.b**r for r in range(4)]
        derivatives = []
        for r in range(1, 4):
            primary = 8*3**r+sum(F(math.comb(r, ell))*pc[ell]*(
                         16-self.beta[0] if ell == r else 8*3**(r-ell))
                         for ell in range(1, r+1))
            derivatives.append(self.q*primary+curvature[r])
        return dict(rho_lower=1-8*self.q+self.q*self.beta[0]-curvature[0],
                    rho_upper=1+8*self.q+curvature[0],
                    rho_phi_upper=derivatives[0],rho_phiphi_upper=derivatives[1],
                    rho_phiphiphi_piecewise_upper=derivatives[2],
                    control_support_derivative_bounds=support,
                    control_curvature_piecewise_derivative_bounds=curvature)

    def protected_circle(self):
        """Exact local identities only; positive radius or holding is separate."""
        radius = ri.point(1+8*self.q+self.t)
        c = ri.sub(ri.scale(self.center_per_q, self.q), ri.point(self.local_cosine_coefficient))
        return dict(radius=radius,project_c=c,
                    centre_vector_rule='O=-project_c*er(pi/3)',
                    angular_halfwidth=self.controls.a,
                    material_center=self.L,
                    scope='Circle identity on the common protected arc; no positivity, full-surface or held-ratio assertion.')


def control_curvature_enclosure(core, panels=256):
    """Prepared R41 midpoint/Lipschitz enclosure with the combined trace bound."""
    assert isinstance(core, ExactCircleTraceM3Core)
    assert isinstance(panels, int) and panels > 0
    lower, upper = None, None
    for j in range(panels):
        x = ri.scale(core.L, F(2*j+1, 2*panels))
        jets = core.control_jets(x, 2)
        value = ri.add(jets[0], jets[2])
        lower = value[0] if lower is None else min(lower, value[0])
        upper = value[1] if upper is None else max(upper, value[1])
    lipschitz = core.global_bounds['control_curvature_piecewise_derivative_bounds'][1]
    remainder = core.L[1]*lipschitz/(2*panels)
    enclosure = lower-remainder,upper+remainder
    return dict(panels=panels,half_sector=core.L,exact_midpoint_value_hull=(lower,upper),
                lipschitz_upper=lipschitz,whole_panel_remainder=remainder,
                whole_angle_enclosure=enclosure,absolute_upper=ri.magnitude(enclosure))
