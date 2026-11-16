"""WGS complete positive finite-jet graph. New formulas only; no entry point.
The owner runner validates all old evidence before calling these routines.
All coefficients are nonnegative complete norm bounds, with ordinary-radial
one-sided derivatives. A coefficient c[a,b] bounds |d_r^a d_phi^b f|/(a!b!).
The formal jet weights are exactly one; they are not analyticity radii.
"""
from __future__ import annotations
from fractions import Fraction
from math import comb, factorial
from flint import arb

MAX_DEGREE = 15
JET_GROUPS = ((0, 0), (1, 1), (2, 2), (3, 3), (4, 4),
              (5, 6), (7, 9), (10, 12), (13, 15))
STRICT_SHAPES = {
    "phase_derivatives": (15, 3), "X_derivatives": (15, 3),
    "omega": (15, 3), "t": (15, 3), "x": (14, 3), "y": (14, 3),
    "Q": (13, 2), "determinant": (13, 2), "mu_inverse": (13, 2),
    "H_inverse_entry_sum": (13, 2),
    "G": (14, 3), "a0": (14, 3), "b0": (14, 3),
    "v0": (12, 2), "Fb": (12, 1), "Fa": (12, 1),
    "transport_kernel": (12, 1), "R": (12, 2),
    "a1": (12, 2), "b1": (12, 2),
}
LOCAL_SHAPES = {
    "X_minus_phi": (15, 3), "T": (15, 3), "G": (14, 3),
    "Q": (13, 2), "H_inverse_entry_sum": (13, 2),
    "mu_inverse": (13, 2), "a0": (14, 3), "b0": (14, 3),
    "Fb": (12, 1), "Fa": (12, 1), "a1": (12, 2), "b1": (12, 2),
}

def ex(n):
    if isinstance(n, Fraction):
        return arb(n.numerator) / arb(n.denominator)
    if not isinstance(n, int):
        raise TypeError("ex accepts exact integers or Fraction, never a rational string")
    return arb(n)

def up(x):
    x = arb(x)
    if not x.is_finite() or x.upper() < 0:
        raise ArithmeticError("nonfinite or negative complete norm bound")
    return x.upper()

def lower(x, label):
    x = arb(x)
    if not x.is_finite() or not x.lower() > 0:
        raise ArithmeticError("missing complete positive lower: " + label)
    return x.lower()

def read_up(record):
    if not isinstance(record, dict) or set(record) != {"ball"}:
        raise TypeError("the directed reader requires one complete original ball")
    return up(arb(record["ball"]))

def read_lower(record, label):
    if not isinstance(record, dict) or set(record) != {"ball"}:
        raise TypeError("the directed reader requires one complete original ball")
    return lower(arb(record["ball"]), label)

def record(x):
    return {"ball": up(x).str(75)}

def lower_record(x, label):
    y = lower(x, label)
    r = {"ball": y.str(75)}
    return r, lower(arb(r["ball"]), label + " after retained serialization")

def pospower(x, p, q=1):
    if not isinstance(p, int) or not isinstance(q, int) or q <= 0:
        raise TypeError("power exponent must be an exact rational")
    x = up(x)
    if x == 0:
        if p <= 0:
            raise ArithmeticError("nonpositive power denominator")
        return arb(0)
    return up(x ** (ex(p) / ex(q)))

def indices(m, p):
    return tuple((a, b) for k in range(m + 1)
                 for a in range(min(p, k) + 1) for b in (k - a,))

class Jet:
    """A complete finite normalized derivative bound, never a sampled Taylor jet."""
    def __init__(self, m, p, coefficients, label):
        self.m, self.p, self.label = m, p, label
        kk = indices(m, p)
        if set(coefficients) != set(kk):
            raise ValueError("incomplete derivative set: " + label)
        self.c = {k: up(coefficients[k]) for k in kk}

    def need(self, m, p):
        missing = [k for k in indices(m, p) if k not in self.c]
        if missing:
            raise ValueError("unpaid derivative of " + self.label + ": " + str(missing[0]))
        return self

    def part(self, m, p, label=None):
        self.need(m, p)
        return Jet(m, p, {k: self.c[k] for k in indices(m, p)}, label or self.label)

    def derivative(self, dr=0, da=0, m=None, p=None, label=None):
        if m is None:
            m = self.m - dr - da
        if p is None:
            p = self.p - dr
        if m < 0 or p < 0:
            raise ValueError("negative derivative request")
        out = {}
        for a, b in indices(m, p):
            k = (a + dr, b + da)
            if k not in self.c:
                raise ValueError("unpaid shifted derivative of " + self.label + ": " + str(k))
            f = factorial(a + dr) // factorial(a)
            f *= factorial(b + da) // factorial(b)
            out[a, b] = up(ex(f) * self.c[k])
        return Jet(m, p, out, label or self.label + "_derivative")

def zero(m, p, label="zero"):
    return Jet(m, p, {k: arb(0) for k in indices(m, p)}, label)

def constant(v, m, p, label="constant"):
    d = {k: arb(0) for k in indices(m, p)}
    d[0, 0] = up(v)
    return Jet(m, p, d, label)

def ordinary_jet(values, m, p, label):
    return Jet(m, p, {k: up(values[k] / ex(factorial(k[0]) * factorial(k[1])))
                     for k in indices(m, p)}, label)

def radial(values, m, p, label):
    if len(values) <= p:
        raise ValueError("missing radial coefficient: " + label)
    return Jet(m, p, {(a, b): (up(values[a] / ex(factorial(a))) if b == 0 else arb(0))
                     for a, b in indices(m, p)}, label)

def add(*terms, m, p, label="positive_sum"):
    for t in terms:
        t.need(m, p)
    return Jet(m, p, {k: up(sum((t.c[k] for t in terms), arb(0)))
                     for k in indices(m, p)}, label)

def scale(t, scalar, m=None, p=None, label="scaled_jet"):
    m = t.m if m is None else m
    p = t.p if p is None else p
    t.need(m, p)
    s = up(scalar)
    return Jet(m, p, {k: up(s * t.c[k]) for k in indices(m, p)}, label)

def mul(*terms, m, p, label="complete_product"):
    for t in terms:
        t.need(m, p)
    out = constant(arb(1), m, p)
    for t in terms:
        c = {}
        for a, b in indices(m, p):
            c[a, b] = up(sum((out.c[i, j] * t.c[a-i, b-j]
                             for i in range(a + 1) for j in range(b + 1)), arb(0)))
        out = Jet(m, p, c, label)
    return out

def positive_degree(t, m, p):
    t.need(m, p)
    d = {k: t.c[k] for k in indices(m, p)}
    d[0, 0] = arb(0)
    return Jet(m, p, d, "positive_degree_" + t.label)

def power_jet(t, gap, exponent, m, p, label):
    """Finite Faà di Bruno, not a convergent infinite binomial series."""
    t.need(m, p)
    gap = lower(gap, label + "_gap")
    a = Fraction(exponent)
    value = pospower(t.c[0, 0] if a >= 0 else gap, a.numerator, a.denominator)
    out = constant(value, m, p, label)
    delta = positive_degree(t, m, p)
    term = constant(arb(1), m, p)
    binomial = Fraction(1)
    for ell in range(1, m + 1):
        term = mul(term, delta, m=m, p=p)
        binomial *= (a - ell + 1) / ell
        if binomial == 0:
            break
        e = a - ell
        base = t.c[0, 0] if e >= 0 else gap
        w = up(ex(abs(binomial)) * pospower(base, e.numerator, e.denominator))
        out = add(out, scale(term, w), m=m, p=p, label=label)
    return out

def reciprocal(t, gap, m, p, label):
    return power_jet(t, gap, Fraction(-1), m, p, label)

def log_derivatives(t, gap, m, p, label):
    """Only derivatives of log; the unused constant is exactly zero."""
    t.need(m, p)
    gap = lower(gap, label + "_gap")
    d = positive_degree(t, m, p)
    power = constant(arb(1), m, p)
    out = zero(m, p, label)
    for ell in range(1, m + 1):
        power = mul(power, d, m=m, p=p)
        out = add(out, scale(power, up(1 / (ex(ell) * gap ** ell))),
                  m=m, p=p, label=label)
    return out

def from_log_derivatives(logjet, value_upper, m, p, label):
    """The finite exponential polynomial; no scalar exp/log is evaluated."""
    logjet.need(m, p)
    if logjet.c[0, 0] != 0:
        raise ValueError("the log-derivative jet must have zero constant")
    term = constant(arb(1), m, p)
    out = term
    for ell in range(1, m + 1):
        term = mul(term, logjet, m=m, p=p)
        out = add(out, scale(term, 1 / ex(factorial(ell))), m=m, p=p)
    return scale(out, value_upper, label=label)

def cauchy(M, radial_margin, angular_margin, m, p, label):
    rr = lower(radial_margin, label + "_radial_margin")
    ss = lower(angular_margin, label + "_angular_margin")
    return Jet(m, p, {(a, b): up(M / (rr ** a * ss ** b))
                     for a, b in indices(m, p)}, label)

def bell(n, k, values):
    cache = {}
    def go(nn, kk):
        if nn == 0:
            return arb(1) if kk == 0 else arb(0)
        if kk == 0 or nn < kk:
            return arb(0)
        key = (nn, kk)
        if key not in cache:
            cache[key] = up(sum((ex(comb(nn-1, j-1)) * values[j] *
                                  go(nn-j, kk-1)
                                  for j in range(1, nn-kk+2)), arb(0)))
        return cache[key]
    return go(n, k)

def compose_ordinary(derivatives, flow, n):
    if n == 0:
        return up(derivatives[0])
    return up(sum((derivatives[k] * bell(n, k, flow)
                   for k in range(1, n + 1)), arb(0)))

def emit_jet(t, omit_value=False):
    """Fixed groups dominate every normalized degree, with no discarded index."""
    out = []
    for left, right in JET_GROUPS:
        right = min(right, t.m)
        if left > right:
            continue
        values = []
        for k in range(left, right + 1):
            if omit_value and k == 0:
                continue
            values.append(up(sum((v for (a, b), v in t.c.items() if a+b == k), arb(0))))
        out.append(None if not values else record(max(values)))
    return {"shape": [t.m, t.p], "group_upper": out,
            "value_omitted_for_lift": bool(omit_value)}

def emit_jets(mapping, omitted=()):
    return {k: emit_jet(v, k in omitted) for k, v in mapping.items()}

def derivative_certificate():
    # An index is an exact integer pair, not a numerical derivative evaluation.
    predecessors = {
        "phase_derivatives": [("flow", 15, 0), ("a_sigma", 14, 2)],
        "t": [("phase_derivatives", 15, 3)],
        "x": [("phase_derivatives", 15, 3)],
        "y": [("t", 15, 3)],
        "G": [("t", 14, 3), ("q", 3, 3), ("ell0", 2, 2)],
        "w0": [("G", 14, 3), ("x", 14, 3), ("y", 14, 3), ("t", 14, 3)],
        "forcing": [("w0", 14, 3), ("background", 14, 2),
                    ("eta", 2, 2), ("Q", 12, 1), ("mu_inverse", 12, 1)],
        "transport_kernel": [("forcing", 12, 1), ("v0", 12, 1),
                             ("Q", 12, 1), ("phase_derivatives", 13, 1),
                             ("t", 12, 1)],
        "free_w1": [("transport_kernel", 12, 1), ("v0", 12, 2),
                    ("a_sigma", 11, 1), ("flow", 12, 0), ("t", 12, 2)],
    }
    return {
        "normalized_coefficients": "ordinary derivative norm divided by a! b!",
        "formal_radial_weight": 1, "formal_angular_weight": 1,
        "allowed_indices": "0<=a<=p; b>=0; a+b<=m",
        "fixed_degree_groups": [list(g) for g in JET_GROUPS],
        "reconstruction": "a! b! times the upper for the group containing a+b",
        "strict_shapes": {k: list(v) for k, v in STRICT_SHAPES.items()},
        "local_shapes": {k: list(v) for k, v in LOCAL_SHAPES.items()},
        "ordered_predecessors": predecessors,
        "phase_value_not_a_periodic_function": True,
        "no_root_radial_three_bound_for_individual_Phi": True,
        "new_genuine_potential_packet_included": False,
        "all_product_indices_checked_before_their_arithmetic": True,
    }

def complete_strict_coefficients(s):
    m, p = 14, 2
    background = {}
    for a, b in indices(m, p):
        v = s["Qmixed"][a][b] if b <= 3 else up(ex(384) ** (b-3) * s["Qmixed"][a][3])
        background[a, b] = v
    U = ordinary_jet(background, m, p, "complete_U")
    V = ordinary_jet(background, m, p, "complete_V")
    beta = radial(s["beta"], m, p, "beta")
    gamma = radial(s["gamma"], m, p, "gamma")
    K = radial(s["K"], m, p, "K")
    q = radial(s["q"], 15, 3, "q")
    one = constant(arb(1), m, p)
    UU = mul(U, U, m=m, p=p)
    VV = mul(V, V, m=m, p=p)
    SS = add(UU, mul(K, VV, m=m, p=p), m=m, p=p, label="S_complete")
    mean_values = [up(ex(factorial(a)) * SS.c[a, 0]) for a in range(3)]
    meanS = radial(mean_values, m, p, "mean_S")
    meanV = radial([s["Qmixed"][a][0] for a in range(3)], m, p, "full_mean_V")
    eta0 = mul(gamma, meanV, m=m, p=p, label="eta")
    eta = radial([ordinary_value(eta0, a, 0) for a in range(3)], 15, 2, "eta")
    BS = mul(beta, SS, m=m, p=p)
    drift_ordinary = {}
    for a, b in indices(15, p):
        if b == 0:
            drift_ordinary[a, b] = up(ex(factorial(a)) * BS.c[a, 0] / 4)
        else:
            drift_ordinary[a, b] = up(ex(factorial(a)*factorial(b-1)) * BS.c[a, b-1])
    d = ordinary_jet(drift_ordinary, 15, p, "complete_drift")
    a_sigma = add(d, mul(eta, q, m=15, p=p), m=15, p=p, label="both_a_sigma")
    ell0 = scale(mul(beta, meanS, m=m, p=p), 2, label="ell0")
    work = dict(U=U, V=V, beta=beta, gamma=gamma, K=K, q=q, S=SS,
                meanS=meanS, eta=eta, d=d, a_sigma=a_sigma, ell0=ell0, one=one)
    doc = {"new_jets": emit_jets({k: work[k] for k in ("eta", "d", "a_sigma", "ell0")}),
           "background_pair_used_as_each_component_upper": True,
           "full_physical_mean_kept": True,
           "old_Qmixed_and_intrinsic_jets_read_only": True,
           "new_target": "whole strict coefficient products, not old per-piece rows"}
    return work, doc

def complete_higher_flow_and_cut(s, c):
    flow = {k: s["flow"][k] for k in range(1, 5)}
    cut = {k: s["cut_phase"][k] for k in range(1, 5)}
    d = c["d"]
    for k in range(5, 16):
        value = sum((ex(factorial(j)) * d.c[0, j] * bell(k, j, flow)
                     for j in range(2, k+1)), arb(0))
        flow[k] = up(s["rc"] * flow[1] * value)
    cut_base = up(1 + s["xdev_cut"] + s["t_cut_upper"].sqrt() * s["y_cut"])
    for k in range(5, 16):
        cut[k] = up(ex(factorial(k-1)) * cut_base / s["SG"] ** (k-1))
    p_rec, pmin = lower_record(1 - s["xdev_cut"] -
                               up(s["t_cut_upper"].sqrt() * s["y_cut"]), "cut phase")
    phase = {k: compose_ordinary(cut, flow, k) for k in range(1, 16)}
    phi_rec, phi_min = lower_record(pmin * s["flow_lower"], "strict phase")
    work = {"flow": flow, "cut_phase": cut, "phase": phase,
            "cut_lower": pmin, "phase_lower": phi_min}
    doc = {"flow_orders_5_through_15": [record(flow[k]) for k in range(5, 16)],
           "cut_phase_orders_5_through_15": [record(cut[k]) for k in range(5, 16)],
           "complete_strict_phase_angular_orders_1_through_15":
               [record(phase[k]) for k in range(1, 16)],
           "cut_phase_lower": p_rec, "strict_phase_lower": phi_rec,
           "old_flow_1_through_4_recomputed": 0,
           "old_cut_phase_1_through_4_recomputed": 0,
           "all_shorter_intervals_both_branches_both_orientations": True}
    return work, doc

def ordinary_value(t, a, b):
    if (a, b) not in t.c:
        raise ValueError("unpaid ordinary derivative: " + t.label + str((a, b)))
    return up(ex(factorial(a) * factorial(b)) * t.c[a, b])

def complete_strict_geometry(s, c, f):
    # No lift value is treated as a bounded periodic scalar.
    vals = {(0, 0): arb(0)}
    vals.update({(0, b): f["phase"][b] for b in range(1, 16)})
    aa = c["a_sigma"]
    for a in range(1, 4):
        for b in range(16-a):
            vals[a, b] = up(sum((ex(comb(a-1, i)*comb(b, j)) *
                                 ordinary_value(aa, i, j) *
                                 vals[a-1-i, b-j+1]
                                 for i in range(a) for j in range(b+1)), arb(0)))
    phase = ordinary_jet(vals, 15, 3, "both_Phi_derivatives_no_value")
    eta_up = c["eta"].c[0, 0]
    omega_up = up(ex(Fraction(2, 3)) * pospower(s["t_cut_upper"], 3, 2) +
                  s["rc"] * eta_up * s["q_upper"] * f["phase"][1])
    omega_low = lower(ex(Fraction(2, 3)) *
                      (s["t_cut_lower"] ** (ex(3)/2)), "omega_cut_lower")
    omega_data = dict(phase.c)
    omega_data[0, 0] = omega_up
    omega = Jet(15, 3, omega_data, "omega")
    tjet = scale(power_jet(omega, omega_low, Fraction(2, 3), 15, 3, "omega_two_thirds"),
                 pospower(ex(Fraction(3, 2)), 2, 3), label="minus_T")
    t_lower = s["t_cut_lower"]
    t_upper = tjet.c[0, 0]
    x = phase.derivative(0, 1, 14, 3, "X_phi")
    y = tjet.derivative(0, 1, 14, 3, "T_phi_absolute")
    determinant = mul(x, x, m=13, p=2, label="Phi_plus_phi_times_Phi_minus_phi")
    # Each branch derivative is bounded by x. This is the positive product
    # identity, rather than a difference of interval upper bounds.
    drec, dlow = lower_record(f["phase_lower"] * f["phase_lower"], "fold determinant")
    invsqrt = power_jet(tjet, t_lower, Fraction(-1, 2), 13, 2, "inverse_sqrt_minus_T")
    Q = mul(c["eta"], c["q"], invsqrt, m=13, p=2, label="Q_fold")
    qrec, qlow = lower_record(s["eta_lower"] * s["q_lower"] / up(t_upper.sqrt()),
                             "Q_fold")
    mu = mul(Q, Q, determinant, m=13, p=2, label="mu")
    mrec, mlow = lower_record(qlow * qlow * dlow, "mu")
    mu_inverse = reciprocal(mu, mlow, 13, 2, "mu_inverse")
    numerator = add(scale(x, 2, 13, 2),
                    mul(add(constant(arb(1), 13, 2), tjet, m=13, p=2),
                        y, m=13, p=2), m=13, p=2, label="H_adjugate_entry_sum")
    H_inverse = mul(numerator, reciprocal(determinant, dlow, 13, 2, "D_inverse"),
                    m=13, p=2, label="H_inverse_entry_sum")
    loc_tstar = lower(s["fold_Am"] ** (ex(2)/3), "local t/rho")
    strict_tstar = lower(t_lower / s["root_upper"], "strict t/rho")
    tsrec, tstar = lower_record(min(loc_tstar, strict_tstar), "whole t/rho")
    work = {"phase_derivatives": phase, "X_derivatives": phase,
            "omega": omega, "t": tjet, "x": x, "y": y, "Q": Q,
            "determinant": determinant, "mu_inverse": mu_inverse,
            "H_inverse_entry_sum": H_inverse,
            "t_lower": t_lower, "t_upper": t_upper,
            "Q_lower": qlow, "D_lower": dlow, "mu_lower": mlow,
            "t_over_rho_lower": tstar}
    doc = {"complete_jets": emit_jets({k: work[k] for k in (
                "phase_derivatives", "X_derivatives", "omega", "t", "x", "y",
                "Q", "determinant", "mu_inverse", "H_inverse_entry_sum")},
                ("phase_derivatives", "X_derivatives")),
           "complete_positive_lowers": {"determinant": drec, "Q_fold": qrec,
                                         "mu": mrec, "whole_t_over_rho": tsrec},
           "t_over_rho_candidates": {"local": {"ball": loc_tstar.str(75)},
                                      "strict": {"ball": strict_tstar.str(75)}},
           "strict_minus_T_lower_is_old_cut_lower": True,
           "root_Phi_radial_derivatives_not_asserted": True,
           "ordinary_one_sided_r_and_full_real_lifts": True}
    return work, doc

def complete_strict_leading(s, c, f, g):
    t, q = g["t"], c["q"]
    G_upper = up(s["fold_G"] * s["leading_reverse"] *
                 pospower(g["t_upper"] * s["q_cut_upper"] * s["q_cut_upper"] /
                          (s["t_cut_lower"] * s["q_lower"] * s["q_lower"]), 1, 4))
    gr = (g["t_lower"] * s["q_cut_lower"] * s["q_cut_lower"] /
          (s["t_cut_upper"] * s["q_upper"] * s["q_upper"]))
    G_lower_raw = (gr ** (ex(1)/4)) / (s["fold_Gi"] * s["leading_forward"])
    grec, G_lower = lower_record(G_lower_raw, "strict G")
    m, p = 14, 3
    logt = log_derivatives(t, g["t_lower"], m, p, "log_minus_T")
    logq = log_derivatives(q, s["q_lower"], m, p, "log_q")
    logr = zero(m, p, "integrated_ell0_derivatives").c
    for a in range(1, 4):
        logr[a, 0] = up(ordinary_value(c["ell0"], a-1, 0) / ex(factorial(a)))
    logEG = Jet(m, p, logr, "log_EG_derivatives")
    logG = add(scale(logt, ex(Fraction(1, 4))),
               scale(logq, ex(Fraction(1, 2))), logEG, m=m, p=p, label="log_G_derivatives")
    G = from_log_derivatives(logG, G_upper, m, p, "G")
    xx = mul(g["x"], g["x"], m=m, p=p)
    tyy = mul(g["t"], g["y"], g["y"], m=m, p=p)
    a0 = mul(G, add(xx, tyy, m=m, p=p), m=m, p=p, label="a0")
    b0 = scale(mul(G, g["x"], g["y"], m=m, p=p), 2, label="b0")
    v0 = mul(G, g["x"], g["x"], m=12, p=2, label="both_v0")
    vrec, vlow = lower_record(G_lower * f["phase_lower"] * f["phase_lower"], "v0")
    work = {"G": G, "a0": a0, "b0": b0, "v0": v0,
            "G_lower": G_lower, "v0_lower": vlow}
    doc = {"complete_jets": emit_jets({k: work[k] for k in ("G", "a0", "b0", "v0")}),
           "complete_G_upper": record(G_upper), "complete_G_lower": grec,
           "complete_v0_lower": vrec,
           "forward_and_reverse_old_scalar_fees_used_in_their_own_direction": True,
           "new_scalar_flow_exponentials": 0,
           "v0_positive_identity": "G times Phi_sigma_phi squared",
           "log_derivative_signs_replaced_only_by_complete_positive_triangle": True}
    return work, doc

def complete_strict_forcing(s, c, g, w):
    m, p = 12, 1
    beta, eta, K = c["beta"], c["eta"], c["K"]
    U, V, d = c["U"], c["V"], c["d"]
    one = constant(arb(1), m, p)
    def prod(*terms):
        return mul(*terms, m=m, p=p)
    def summ(*terms):
        return add(*terms, m=m, p=p)
    def Dr(t):
        return t.derivative(1, 0, m, p)
    def Da(t):
        return t.derivative(0, 1, m, p)
    def Dbound(t):
        return summ(Dr(t), prod(d, Da(t)))
    eta_inv = reciprocal(eta, s["eta_lower"], m, p, "eta_inverse")
    # The e, b and ell jets must also have the derivatives occurring below.
    mm, pp = 13, 2
    uu = mul(U, U, m=mm, p=pp)
    kvv = mul(K, V, V, m=mm, p=pp)
    e = mul(beta, add(constant(arb(1), mm, pp), scale(uu, 3), kvv,
                      m=mm, p=pp), m=mm, p=pp, label="e")
    b = mul(beta, add(constant(arb(1), mm, pp), uu, scale(kvv, 3),
                      m=mm, p=pp), m=mm, p=pp, label="b_local")
    ell = scale(mul(beta, U, V, m=mm, p=pp), 2, label="ell")
    eratio = prod(Dr(eta), eta_inv)
    dp = Da(d)
    tQ = summ(eratio, dp, e)
    T0 = summ(eratio, scale(prod(beta, c["meanS"]), 4), scale(dp, 5))
    rQ = summ(Dbound(ell), prod(eta, Da(e)),
              scale(prod(beta, eta, Da(U), U), 2),
              prod(ell, summ(eratio, dp)))
    theta = summ(prod(rQ, eta_inv), scale(prod(beta, K, V, Da(V)), 2))
    V0 = summ(prod(tQ, b), Dbound(b),
              prod(K, summ(prod(ell, ell), scale(prod(beta, eta, V, Da(U)), 4))))
    second_angular = summ(prod(d, d), prod(eta, eta, K))
    drift_first = summ(prod(d, dp), Dr(d))
    def diagonal(a):
        return summ(a.derivative(2, 0, m, p),
                    scale(prod(d, a.derivative(1, 1, m, p)), 2),
                    prod(second_angular, a.derivative(0, 2, m, p)),
                    prod(drift_first, a.derivative(0, 1, m, p)),
                    prod(T0, Dbound(a)), prod(V0, a))
    Fb_num = summ(diagonal(w["a0"]), prod(theta, g["Q"], g["t"], w["b0"]))
    Fa_num = summ(diagonal(w["b0"]), prod(theta, g["Q"], w["a0"]))
    Fb = mul(g["mu_inverse"], Fb_num, m=m, p=p, label="complete_Fb")
    Fa = mul(g["mu_inverse"], Fa_num, m=m, p=p, label="complete_Fa")
    work = dict(Fb=Fb, Fa=Fa, e=e, b_local=b, ell=ell, tQ=tQ, T0=T0,
                rQ=rQ, theta=theta, V0=V0)
    doc = {"complete_forcing_jets": emit_jets({"Fb": Fb, "Fa": Fa}),
           "complete_coefficient_jets": emit_jets({k: work[k] for k in (
               "e", "b_local", "ell", "tQ", "T0", "rQ", "theta", "V0")}),
           "both_components": True,
           "full_theta_Q_KT_product_present": True,
           "full_second_order_drift_and_original_means_present": True,
           "background_ordinary_radial_order_max": 2,
           "leading_ordinary_radial_order_max": 3,
           "no_old_forcing_target_executed": True}
    return work, doc

def complete_local_regular_packet(s, old):
    hloc = s["root_upper"] - s["rc"]
    hrec, hmargin = lower_record(s["saved_h"] - hloc, "local cover inside saved h")
    majors = old["majorants"]
    def cj(name, shape, output_name=None):
        val, rr, ss = majors[name]
        return cauchy(val, rr-hloc, ss, shape[0], shape[1], output_name or name)
    packet = {
        "X_minus_phi": cj("chi", (15, 3), "local_X_minus_phi"),
        "T": cj("T", (15, 3), "local_T"),
        "G": cj("G", (14, 3), "local_G"),
        "Q": cj("Q", (13, 2), "local_Q"),
        "a0": cj("a0", (14, 3), "local_a0"),
        "b0": cj("b0", (14, 3), "local_b0"),
        "Fb": cj("F0", (12, 1), "local_Fb"),
        "Fa": cj("F1", (12, 1), "local_Fa"),
    }
    folded = old["fold"]
    H0 = up((2*folded["E"] + (1+folded["TM"])*folded["BT"]) /
            lower(folded["gap"], "original full complex D"))
    M0 = up(1 / lower(folded["mu"], "original full complex mu"))
    packet["H_inverse_entry_sum"] = cauchy(H0, s["RG"]-hloc, s["SG"],
                                            13, 2, "local_H_inverse")
    packet["mu_inverse"] = cauchy(M0, s["RG"]-hloc, s["SG"], 13, 2, "local_mu_inverse")
    free = {}
    for name in ("a1", "b1"):
        values = {}
        for a, b in indices(12, 2):
            if b <= 3:
                values[a, b] = old["free_component"][name][a][b]
            elif a <= 1 and b <= 6:
                # The old complete two-component sum bounds either component.
                values[a, b] = s["old_FA_free_jets"][a][b]
            else:
                values[a, b] = up(ex(factorial(b-3)) *
                                   old["free_component"][name][a][3] /
                                   s["saved_strip"] ** (b-3))
        free[name] = ordinary_jet(values, 12, 2, "local_" + name)
    packet.update(free)
    doc = {"complete_jets": emit_jets(packet),
           "local_cover_saved_h_margin": hrec,
           "complete_local_H_inverse_holomorphic_upper": record(H0),
           "complete_local_mu_inverse_holomorphic_upper": record(M0),
           "free_p0_p1_p2_q0_through_q3_recomputed": 0,
           "old_FA_free_orders_through_six_recomputed": 0,
           "both_old_component_tables_read": True,
           "free_and_genuine_amplitude_distinct": True,
           "individual_Phi_radial_jets_at_root_not_used": True,
           "local_original_piece_label": 2549,
           "local_to_strict_function_identity": "same actual root-normalized germ at rc"}
    return packet, doc

def complete_free_first_transport(s, c, f, g, w, force, local):
    m, p = 12, 1
    v0inv = reciprocal(w["v0"], w["v0_lower"], m, p, "v0_inverse")
    invs = power_jet(g["t"], g["t_lower"], Fraction(-1, 2), m, p, "inverse_s")
    tau = mul(g["Q"], g["x"], m=m, p=p, label="both_tau")
    force_pair = add(force["Fa"], mul(force["Fb"], invs, m=m, p=p), m=m, p=p)
    kernel = scale(mul(tau, v0inv, force_pair, m=m, p=p),
                   ex(Fraction(1, 2)), label="both_transport_kernel")
    # The cut value is the same free amplitude, never a zero restart.
    cut_t = {(0, 0): s["t_cut_upper"]}
    for b in range(1, 13):
        cut_t[0, b] = (s["cut_t_derivatives"][b] if b <= 4 else
                      up(ex(factorial(b-1))*s["y_cut"]/s["SG"]**(b-1)))
    cut_t = ordinary_jet(cut_t, 12, 0, "cut_minus_T")
    cut_s = power_jet(cut_t, s["t_cut_lower"], Fraction(1, 2), 12, 0, "cut_s")
    cut_v1 = add(local["a1"], mul(cut_s, local["b1"], m=12, p=0),
                 m=12, p=0, label="cut_v1")
    cut_R = mul(cut_v1, v0inv, m=12, p=0, label="cut_R")
    cut_R_der = {k: ordinary_value(cut_R, 0, k) for k in range(13)}
    K_der = {k: ordinary_value(kernel, 0, k) for k in range(13)}
    rvals = {}
    for b in range(13):
        rvals[0, b] = up(compose_ordinary(cut_R_der, f["flow"], b) +
                          s["rc"] * compose_ordinary(K_der, f["flow"], b))
    aa = c["a_sigma"]
    for b in range(12):
        rvals[1, b] = up(sum((ex(comb(b, j)) * ordinary_value(aa, 0, j) *
                              rvals[0, b-j+1] for j in range(b+1)), arb(0)) +
                           ordinary_value(kernel, 0, b))
    for b in range(11):
        rvals[2, b] = up(sum((ex(comb(b, j)) *
                              (ordinary_value(aa, 1, j)*rvals[0, b-j+1] +
                               ordinary_value(aa, 0, j)*rvals[1, b-j+1])
                              for j in range(b+1)), arb(0)) +
                           ordinary_value(kernel, 1, b))
    R = ordinary_jet(rvals, 12, 2, "both_R")
    v1 = mul(w["v0"], R, m=12, p=2, label="both_v1")
    # The two branch average/difference each have the common branch bound.
    a1 = v1.part(12, 2, "strict_a1")
    b1 = mul(v1, power_jet(g["t"], g["t_lower"], Fraction(-1, 2),
                          12, 2, "strict_inverse_s"),
             m=12, p=2, label="strict_b1")
    work = {"transport_kernel": kernel, "R": R, "a1": a1, "b1": b1}
    doc = {"complete_jets": emit_jets(work),
           "complete_cut_ratio_angular_jet": emit_jet(cut_R),
           "both_characteristic_branches_and_physical_signs": True,
           "old_root_trace_preserved_at_cut": True,
           "ordinary_fixed_dr_endpoints_and_all_partial_intervals": True,
           "actual_original_interfaces_retained": 3070,
           "old_free_amplitude_targets_recomputed": 0,
           "new_ray_integrations": 0, "new_scalar_exponential_evaluations": 0,
           "genuine_potential_addition_included": False}
    return work, doc

def complete_global_packet_conclusion(strict_geometry, strict_leading,
                                       strict_forcing, local, transport):
    """A union of two qualified patches, retaining both complete bounds."""
    links = {
        "X": ["strict_geometry.X_derivatives", "local.X_minus_phi"],
        "T": ["strict_geometry.t", "local.T"],
        "Q": ["strict_geometry.Q", "local.Q"],
        "H_inverse": ["strict_geometry.H_inverse_entry_sum", "local.H_inverse_entry_sum"],
        "mu_inverse": ["strict_geometry.mu_inverse", "local.mu_inverse"],
        "G": ["strict_leading.G", "local.G"],
        "a0": ["strict_leading.a0", "local.a0"],
        "b0": ["strict_leading.b0", "local.b0"],
        "Fb": ["strict_forcing.Fb", "local.Fb"],
        "Fa": ["strict_forcing.Fa", "local.Fa"],
        "a1": ["strict_transport.a1", "local.a1"],
        "b1": ["strict_transport.b1", "local.b1"],
    }
    required = (
        (strict_geometry, {k: v for k, v in STRICT_SHAPES.items()
                           if k in ("phase_derivatives", "X_derivatives", "omega", "t",
                                    "x", "y", "Q", "determinant", "mu_inverse",
                                    "H_inverse_entry_sum")}),
        (strict_leading, {k: STRICT_SHAPES[k] for k in ("G", "a0", "b0", "v0")}),
        (strict_forcing, {k: STRICT_SHAPES[k] for k in ("Fb", "Fa")}),
        (transport, {k: STRICT_SHAPES[k] for k in ("transport_kernel", "R", "a1", "b1")}),
        (local, LOCAL_SHAPES),
    )
    for bundle, shapes in required:
        for name, shape in shapes.items():
            bundle[name].need(*shape)
    return {
        "complete_named_global_free_jet_graph": True,
        "same_actual_functions_on_the_common_cut": True,
        "patch_links": links,
        "union_bound_rule": "max of the two already complete patch bounds after their common identity",
        "X_local_rule": "add the exact identity derivative at (0,1); omit the lift value",
        "T_strict_rule": "T=-t, with identical absolute derivative bounds",
        "normalization": "old root-normalized free first transport; original fixed intrinsic eta0",
        "ordinary_one_sided_derivatives": True,
        "physical_angular_frequency": 4,
        "independent_physical_means_retained": True,
        "actual_nonlinear_background_proved": False,
        "complete_genuine_potential_packet_proved": False,
        "complete_N6_residual_constants_proved": False,
        "complete_negative_receiver_constant_proved": False,
        "complete_four_waist_endpoint_constants_proved": False,
        "high_contraction_proved": False,
        "finite_or_incoming_inverse_proved": False,
    }
