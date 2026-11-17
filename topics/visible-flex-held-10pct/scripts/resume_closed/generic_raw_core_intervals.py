"""True-integral m3 raw cores at independently declared primary/control widths.

This extends the R36/R37 oracle formulas, leaving those recorded sources
unchanged.  Mean correction, periodic Green constant and the raw 2 by 2
projection are recomputed from the actual widths.  No R32/R38 numeric
constant, source quadrature value or Fourier approximation is a bound.

The exact width convention is the source's decimal round-trip string.
The amplitude, homotopy and full physical control vector are exact
binary64 values.  The reflection center is the mathematical pi/3; its
binary source value only selects this explicitly checked convention.
"""
from fractions import Fraction as F
import hashlib
import json
import math

import integral_core_intervals as ri
from fast_integral_core_intervals import FastExactRawM3Core, HornerCutoffPrimitive


RAW_KIND = 'exact_m3_raw_local_circle_integral_lift'
RAW_PATH = 'raw-mean-primary-compact-v1'
PRIMITIVE_TARGET = F(1, 10**65)


def primitive_degree(width, frequency, target=PRIMITIVE_TARGET):
    """Pay the complete complex Taylor remainder before selecting a degree."""
    width, target = F(width), F(target)
    assert width > 0 and frequency >= 0 and target > 0
    degree = 64
    while width*abs(frequency*width)**(degree+1)/math.factorial(degree+2) > target:
        degree += 8
        if degree > 512:
            raise ArithmeticError('Declared primitive precision needs degree > 512')
    return degree


class AdaptiveHornerCutoff(HornerCutoffPrimitive):
    def __init__(self, a, b, plain, frequency, target=PRIMITIVE_TARGET):
        ri.CutoffPrimitive.__init__(self, a, b, primitive_degree(b, frequency, target))
        self.plain = plain
        self.maximum_frequency = int(frequency)
        self.requested_error = F(target)

    def complete_remainder(self):
        z = self.maximum_frequency*self.b
        return self.b*abs(z)**(self.degree+1)/math.factorial(self.degree+2)


def primary_constants(primary, L):
    """Exact mean correction and circle-center coefficient for eta=0, n=3."""
    moments = {k: primary.complete(k) for k in range(5)}
    mass = primary.a+primary.b/2
    beta = ri.neg(ri.divide(ri.scale(ri.sub(ri.point(mass), moments[3][0]), 8),
                            ri.sub(L, ri.point(mass))))
    sinL, cosL = ri.signed_sincos(L)
    cotL = ri.divide(cosL, sinL)
    g0 = ri.add(ri.mul(cotL, moments[1][0]), moments[1][1])
    g1 = ri.sub(ri.scale(g0, 8), ri.scale(ri.add(
        ri.mul(cotL, ri.add(moments[2][0], moments[4][0])),
        ri.sub(moments[4][1], moments[2][1])), 4))
    center = ri.add(ri.sub(ri.sub(ri.point(9), beta), g1), ri.mul(beta, g0))
    assert beta[1] < 0 and center[0] > 0
    return beta, center


def raw_projection(control, L, modes):
    """Exact weighted mean/primary projection; no higher-moment inverse.

    W(phi)=1-chi(phi-pi/3).  Its full-period mean cosine moments are
    w_0=1-(a+b/2)/L and w_k=-(-1)^k int chi*cos(3kx)/L.
    Each column uses only w_0,w_1,w_2,w_j,w_(j-1),w_(j+1), so appending
    zero controls is exactly nested, without a limiting argument.
    """
    assert isinstance(modes, int) and modes >= 2
    w = [ri.sub(ri.point(1), ri.divide(ri.point(control.a+control.b/2), L))]
    for k in range(1, modes+2):
        w.append(ri.scale(ri.divide(control.complete(3*k)[0], L), -(-1)**k))
    g00, g01, g11 = w[0], w[1], ri.scale(ri.add(w[0], w[2]), F(1, 2))
    determinant = ri.sub(ri.mul(g00, g11), ri.power(g01, 2))
    assert g00[0] > 0 and determinant[0] > 0
    rows = []
    residual = F(0)
    for j in range(2, modes+1):
        rhs0, rhs1 = w[j], ri.scale(ri.add(w[j-1], w[j+1]), F(1, 2))
        c0 = ri.divide(ri.sub(ri.mul(g11, rhs0), ri.mul(g01, rhs1)), determinant)
        c1 = ri.divide(ri.sub(ri.mul(g00, rhs1), ri.mul(g01, rhs0)), determinant)
        row = [ri.point(0) for _ in range(modes+1)]
        row[0], row[1], row[j] = ri.neg(c0), ri.neg(c1), ri.point(1)
        rows.append(tuple(row))
        r0 = ri.sub(ri.add(ri.mul(g00, c0), ri.mul(g01, c1)), rhs0)
        r1 = ri.sub(ri.add(ri.mul(g01, c0), ri.mul(g11, c1)), rhs1)
        residual = max(residual, ri.magnitude(r0), ri.magnitude(r1))
    return tuple(rows), dict(gram=(g00, g01, g11), determinant=determinant,
                             interval_substitution_residual_upper=residual)


class GeneralExactRawM3Core(FastExactRawM3Core):
    """The same normal/arc/jet formulas for general declared positive widths."""
    def __init__(self, core, provenance):
        settings = provenance['core_round_settings']
        assert provenance['core_kind'] == RAW_KIND
        assert provenance['core_control_path'] == RAW_PATH
        assert core.basis.summary()['control_path'] == RAW_PATH
        assert core.base_mode == 3 and core.bimodal_eta == 0
        assert settings['bimodal_eta'] == 0 and settings['lock_fundamental'] is True
        assert settings['center'] == math.pi/3
        assert core.center == settings['center']
        for attribute, key in (('a', 'halfwidth'), ('transition', 'transition'),
                               ('control_transition', 'control_transition'), ('lam', 'homotopy')):
            assert getattr(core, attribute) == settings[key]
        self.q = F.from_float(core.support_amplitude)
        self.lam = F.from_float(core.lam)
        self.c = tuple(F.from_float(v) for v in core.corrections)
        assert self.q > 0 and 0 <= self.lam <= 1
        assert [float(v) for v in self.c] == provenance['physical_controls']
        self.M = len(self.c)+1
        assert self.M >= 2 and core.basis.M == self.M == provenance['core_projection_order_J']
        self.L = ri.scale(ri.pi_interval(), F(1, 3))
        self.T = ri.scale(self.L, 2)
        a, bp, bc = (F(str(settings[k])) for k in ('halfwidth', 'transition', 'control_transition'))
        assert 0 < a < a+bp < self.L[0] and a < a+bc < self.L[0]
        # primary frequencies are at most 4; the raw two-moment projection
        # additionally needs j=M+1.  The returned error is checked exactly.
        self.primary = AdaptiveHornerCutoff(a, bp, self.plain, 4)
        self.controls = AdaptiveHornerCutoff(a, bc, self.plain, 3*(self.M+1))
        self.beta, self.center_per_q = primary_constants(self.primary, self.L)
        self.H, self.projection_certificate = raw_projection(self.controls, self.L, self.M)
        self.D = tuple(ri.sum_intervals(ri.scale(self.H[j][k], self.c[j]) for j in range(self.M-1))
                       for k in range(self.M+1))
        self.source_coefficient_error_upper = max(
            ri.magnitude(ri.sub(self.H[j][k], ri.point(F.from_float(float(core.basis.H[j, k])))))
            for j in range(self.M-1) for k in range(self.M+1))
        # These are two enclosures of the same exact raw projection.  The
        # source interval itself is not needed for any new inequality.
        source_H = core.basis.certificate['coefficients']
        assert all(max(self.H[j][k][0], source_H[j][k][0]) <=
                   min(self.H[j][k][1], source_H[j][k][1])
                   for j in range(self.M-1) for k in range(self.M+1))
        self.global_bounds = self._global_bounds()

    def _global_bounds(self):
        trig = [sum(ri.magnitude(v)*(3*k)**r for k, v in enumerate(self.D))
                if r else sum(ri.magnitude(v) for v in self.D) for r in range(6)]
        cut = [ri.cutoff_derivative_bound(r)/self.controls.b**r for r in range(6)]
        control = []
        for r in range(6):
            pure = sum(abs(c)*(3*(j+2))**r for j, c in enumerate(self.c))
            compact = sum(math.comb(r, ell)*cut[ell]*trig[r-ell] for ell in range(r+1))
            control.append((1-self.lam)*pure+self.lam*compact)
        rho_control = control[0]+control[2]
        minimum = 1-8*self.q+self.q*self.lam*self.beta[0]-rho_control
        maximum = 1+8*self.q+rho_control
        primary_cut = [ri.cutoff_derivative_bound(r)/self.primary.b**r for r in range(4)]
        derivatives = []
        for r in range(1, 4):
            primary = 8*3**r+self.lam*sum(
                math.comb(r, ell)*primary_cut[ell]*(16-self.beta[0] if ell == r else 8*3**(r-ell))
                for ell in range(1, r+1))
            derivatives.append(self.q*primary+control[r]+control[r+2])
        return dict(rho_lower=minimum, rho_upper=maximum,
                    rho_phi_upper=derivatives[0], rho_phiphi_upper=derivatives[1],
                    rho_phiphiphi_piecewise_upper=derivatives[2],
                    control_support_derivative_bounds=control)


def control_curvature_enclosure(core, panels=256):
    """Whole-angle bound from exact midpoints and a proved Lipschitz remainder.

    Evenness and 2*pi/3 periodicity reduce every angle to x in [0,pi/3].
    b+b'' is C2 and its derivative has the global bound B1+B3 already
    proved analytically.  Every closed panel is included, including all
    cutoff crossings.  These are not unbounded numerical samples.
    """
    assert isinstance(panels, int) and panels > 0
    lower, upper = None, None
    for j in range(panels):
        x = ri.scale(core.L, F(2*j+1, 2*panels))
        jets = core.control_jets(x, 2)
        value = ri.add(jets[0], jets[2])
        lower = value[0] if lower is None else min(lower, value[0])
        upper = value[1] if upper is None else max(upper, value[1])
    controls = core.global_bounds['control_support_derivative_bounds']
    lipschitz = controls[1]+controls[3]
    remainder = core.L[1]*lipschitz/(2*panels)
    enclosure = lower-remainder, upper+remainder
    return dict(panels=panels, half_sector=core.L,
                exact_midpoint_value_hull=(lower, upper),
                lipschitz_upper=lipschitz, whole_panel_remainder=remainder,
                whole_angle_enclosure=enclosure, absolute_upper=ri.magnitude(enclosure))


def literal_structure(value):
    """Canonical exact identity, retaining binary64 bits and data types."""
    if isinstance(value, bool) or value is None or isinstance(value, str):
        return value
    if isinstance(value, int):
        return {'integer': str(value)}
    if isinstance(value, float):
        if not math.isfinite(value):
            raise ValueError('A physical identity cannot contain nonfinite values')
        return {'binary64': value.hex()}
    if isinstance(value, (list, tuple)):
        return [literal_structure(v) for v in value]
    if isinstance(value, dict):
        return {str(k): literal_structure(value[k]) for k in sorted(value)}
    raise TypeError(type(value))


def fixed_atlas_identity(record, *, anchor_record=None, cut_width=.04):
    """Bind the true metric to one material domain; core data do not define g.

    All physical prefix/tail fields must be literally equal to the anchor.
    A core design change is not certified as an isometry by this identity.
    The complete closed-surface cap/column metric is outside this prefix
    identity.  The nominal physical rCut/wCut define the true bridge;
    physical_tail_cut contains derived source rounding and is not used as
    an independent physical parameter.
    """
    anchor = record if anchor_record is None else anchor_record
    physical_keys = ('frozen_profile', 'physical_tail_parameters')
    for key in physical_keys:
        if literal_structure(record[key]) != literal_structure(anchor[key]):
            raise ValueError('The candidate changes the frozen physical metric field: '+key)
    if literal_structure(record['meridian_length']) != literal_structure(anchor['meridian_length']):
        raise ValueError('A candidate must retain the original material L_binary anchor')
    body = dict(version='true-prefix-atlas-v1',
                frozen_profile=literal_structure(anchor['frozen_profile']),
                physical_tail_parameters=literal_structure(anchor['physical_tail_parameters']),
                material_length=literal_structure(anchor['meridian_length']),
                cut_width=literal_structure(float(cut_width)),
                convention='True physical prefix/bridge integrals; fixed L_binary; the R31 zero-value cut coordinate Hermite correction')
    encoded = json.dumps(body, sort_keys=True, separators=(',', ':')).encode()
    return dict(identity_sha256=hashlib.sha256(encoded).hexdigest(), exact_descriptor=body)
