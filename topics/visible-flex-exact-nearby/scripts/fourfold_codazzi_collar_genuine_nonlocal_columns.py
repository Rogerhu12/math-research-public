"""Five unprojected G.10 columns of n*w0+w1^V on the original physical root collar.

The caller applies the single remaining input power n^(1/6). The local
G.9 row is exactly absent in this particular target. No finite local
residual, old angular inverse or spectral output norm is evaluated here.
"""
from fractions import Fraction as Q
from flint import acb, arb
from fourfold_codazzi_signed_density_transport_arithmetic import exact
from fourfold_codazzi_true_phase_original_inputs import check
from fourfold_codazzi_true_characteristic_root_input import radial_laurent, cauchy_tail
from fourfold_codazzi_collar_signed_laurent_enclosure import Field, WIDTH, angular_taylor
from fourfold_codazzi_collar_laurent_terminal import terminal
from fourfold_codazzi_physical_shifted_circle_backend import Column
import fourfold_codazzi_correlated_collar_reference as reference


class Angular:
    """Value and its independently qualified full angular derivative."""
    def __init__(self, value, derivative):
        self.value, self.derivative = value, derivative

    def __add__(self, other):
        return Angular(self.value + other.value, self.derivative + other.derivative)

    def __sub__(self, other):
        return self + other.scale(-1)

    def __mul__(self, other):
        return Angular(self.value * other.value,
                       self.derivative * other.value + self.value * other.derivative)

    def scale(self, scalar):
        return Angular(self.value.scale(scalar), self.derivative.scale(scalar))

    def reciprocal(self):
        inv = self.value.reciprocal()
        return Angular(inv, -(inv * inv * self.derivative))


def geometry(arr, major, rho):
    def field(name, radial=0, angular=0):
        bound, radius, strip = major[name]
        poly = radial_laurent(arr[name], rho, radial)
        if angular:
            poly = poly.theta(angular)
        error = cauchy_tail((bound, radius, strip-WIDTH), abs(rho).upper(),
                            len(arr[name]), radial, angular)
        return Field(poly.lo, poly.c, error)

    def jet(name, angular=0):
        return Angular(field(name, angular=angular), field(name, angular=angular+1))

    out = {name: jet(name) for name in ('Xp', 'Q', 'a0', 'b0', 'w1a', 'w1b')}
    y = jet('T', 1)
    out.update(T=Angular(field('T'), y.value), y=y, chi=field('chi'))
    # The saved coefficient arrays expand in rho=r_*-r. D is the
    # ordinary PHYSICAL r derivative minus d times the angular derivative.
    drift = field('d')
    out['D'] = {name: -field(name, radial=1) - drift * out[name].derivative
                for name in ('a0', 'b0', 'w1a', 'w1b')}
    return out


def potentials(t, coefficients):
    values = reference.bounded_potential(coefficients, 32)
    averages = [v/(2*k+1) for k, v in enumerate(values)]
    radius = exact(reference.R)
    def value_gradient(series):
        return (angular_taylor(t, series, arb(276)),
                angular_taylor(t, series, arb(276), 1).scale(1/radius))
    return value_gradient(values), value_gradient(averages)


def amplitudes(g, nn, inv2, sign, v, v_phi, eta, potential, average):
    """Full G.10 amplitudes prior to either genuine Airy column application."""
    t, x, y, q = (g[k] for k in ('T', 'Xp', 'y', 'Q'))
    leading_a, leading_b = g['a0'], g['b0'].scale(sign)
    correction_a, correction_b = g['w1a'].scale(sign), g['w1b']
    vj, vj_t = potential
    bj, bj_t = average
    B = Angular(bj, bj_t * y.value)
    z = Angular(vj.scale(inv2), (vj_t*y.value).scale(inv2))
    ka = t * leading_b
    wa = leading_a.scale(nn) + correction_a + B * ka
    wb = leading_b.scale(nn) + correction_b + B * leading_a

    # DT=Q X_phi. These are material derivatives of the amplitudes,
    # before applying the true terminal column or exp(i eps n X).
    dt = q.value * x.value
    db = bj_t * dt
    da0, db0 = g['D']['a0'], g['D']['b0'].scale(sign)
    dwa = (da0.scale(nn) + g['D']['w1a'].scale(sign) + db * ka.value
           + bj * (dt*leading_b.value + t.value*db0))
    dwb = db0.scale(nn) + g['D']['w1b'] + db * leading_a.value + bj * da0

    # G.5: B_j H_{D,j}^V w= -i eps Q K w
    #     -Q(V/n^2) (-i eps x,y)^t (i eps y,x)w/[x^2+(T-V/n^2)y^2].
    # Differentiate this entire ordered expression in the angular jet.
    ii = acb(0, sign)
    det_inv = (x*x + (t-z)*y*y).reciprocal()
    coefficient = (q*z*((y*wa).scale(ii) + x*wb)*det_inv).scale(-1)
    fa = ((q*t*wb).scale(-ii) + (x*coefficient).scale(-ii))
    fb = (q*wa).scale(-ii) + y*coefficient
    ga, gb = dwa-fa.derivative, dwb-fb.derivative
    # eta is radial and B_j commutes pointwise with the scalar field v.
    # Thus eta h=F, y_amp=v F and q_amp=v g - v_phi F including v's mean.
    return dict(Fw=(wa.value, wb.value), Fh=(fa.value.scale(1/eta), fb.value.scale(1/eta)),
                Fy=(v*fa.value, v*fb.value), Fg=(ga, gb),
                Fq=(v*ga-v_phi*fa.value, v*gb-v_phi*fb.value))


def physical_inputs(c, g, v, v_phi, eta, lo, hi):
    """rows[sign index][Ai/Bi index] are directly usable Words.known_rhs kwargs.

    Keep the removed unit in the supplied header for any later radial or
    reflection use. Pointwise column norms are unchanged after restoring it.
    """
    check(97 <= lo <= hi and (eta.lower()>0 or eta.upper()<0),
          'actual full input band and genuine same-circle characteristic gap')
    nn = arb(4*lo).union(arb(4*hi))
    inv2 = exact(Q(1, (4*hi)**2)).union(exact(Q(1, (4*lo)**2)))
    scaled_t = g['T'].value.scale(1/exact(reference.R))
    coefficients = reference.scaled_potential(c, lo, hi)
    pot, avg = potentials(scaled_t, coefficients)
    columns, shear = terminal(scaled_t, coefficients, lo, hi)
    finite_mean, oscillatory_phase = g['chi'].separated_mean()
    check(finite_mean.imag.contains(0), 'original finite real phase mean for the common removed input unit')
    rows = []
    for sign in (1, -1):
        phase = oscillatory_phase.scale(acb(0, sign)*nn).exponential()
        amplit = amplitudes(g, nn, inv2, sign, v, v_phi, eta, pot, avg)
        terminal_rows = [{'local': Column(Field.scalar(0), mean_zero=True)} for _ in columns]
        for name, (a, b) in amplit.items():
            pure, companion = [(a*y + b*yt) * phase for y, yt in columns]
            terminal_rows[0][name] = Column(pure + companion.scale(shear))
            terminal_rows[1][name] = Column(companion)
        rows.append(terminal_rows)
    return rows, finite_mean
