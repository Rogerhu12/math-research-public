"""WEJ complete positive extension, profile, angular-inverse and mean graphs.
No entry point. This file declares future verified arithmetic only.
The finite Jet algebra is copied from WGS; no WGS producer is imported or called.
All actual old inputs are admitted by the owner before these functions are called.
Normalized c[a,b] bounds the ordinary derivative divided by a! b!.
A missing lift value is never silently made into a function bound.
"""
from __future__ import annotations
from fractions import Fraction
from math import comb, factorial
import copy

_ACTIVE_RECORD_CAPTURE = None

def _capture_printed_record(value, direction):
    if _ACTIVE_RECORD_CAPTURE is not None:
        event={"direction":direction,"record":copy.deepcopy(value)}
        _ACTIVE_RECORD_CAPTURE["records"].append(event)
        hook=_ACTIVE_RECORD_CAPTURE.get("on_record")
        if hook is not None:
            hook(copy.deepcopy(event))
    return value
from flint import arb

MAX_DEGREE = 15
JET_GROUPS = ((0, 0), (1, 1), (2, 2), (3, 3), (4, 4),
              (5, 6), (7, 9), (10, 12), (13, 15))

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
    return _capture_printed_record({"ball": up(x).str(75)}, "upper")

def lower_record(x, label):
    y = lower(x, label)
    r = _capture_printed_record({"ball": y.str(75)}, "lower")
    return r, lower(arb(r["ball"]), label + " after retained serialization")

def pospower(x, p, q=1):
    if not isinstance(p, int) or not isinstance(q, int) or q <= 0:
        raise TypeError("power exponent must be an exact rational")
    x = lower(x, "negative rational power") if p < 0 else up(x)
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


# ---------------------------------------------------------------------------
# Saved finite-jet decoding and exact typed demands.
# ---------------------------------------------------------------------------
N0 = 388
POTENTIAL_L = Fraction(1, 2000)
POTENTIAL_MARGIN = Fraction(1, 5000)
RC = Fraction(76285779072683, 320000000000000)
ROOT_LO = Fraction(1191984371497, 5000000000000)
ROOT_HI = Fraction(2383968743003, 10000000000000)
OLD_COEFFICIENT_STRIP = Fraction(1, 32)
MAX_Z_DEGREE = 9

class LiftJet(Jet):
    """All actual derivative indices, with no fictitious periodic lift value."""
    def __init__(self, m, p, coefficients, label):
        wanted = set(indices(m, p)) - {(0, 0)}
        if set(coefficients) != wanted:
            raise ValueError("incomplete lift derivative envelope: " + label)
        self.m, self.p, self.label = m, p, label
        self.c = {k: up(coefficients[k]) for k in wanted}

def decode_saved_jet(doc, label, radial_only=False):
    if set(doc) != {"shape", "group_upper", "value_omitted_for_lift"}:
        raise ValueError("unexpected saved finite-jet schema: " + label)
    m, p = doc["shape"]
    if not isinstance(m, int) or not isinstance(p, int) or not 0 <= p <= m <= 15:
        raise ValueError("invalid finite-jet shape")
    groups = [(a, min(b, m)) for a, b in JET_GROUPS if a <= m]
    if len(doc["group_upper"]) != len(groups):
        raise ValueError("incomplete saved degree groups")
    omit = doc["value_omitted_for_lift"]
    if type(omit) is not bool or (omit and radial_only):
        raise ValueError("invalid lift/radial qualification")
    out = {}
    for (left, right), r in zip(groups, doc["group_upper"]):
        if r is None:
            if not (omit and left == right == 0):
                raise ValueError("an unpaid group is not a lift value")
            continue
        v = read_up(r)
        for a, b in indices(m, p):
            if left <= a+b <= right:
                out[a, b] = arb(0) if radial_only and b else v
    return (LiftJet if omit else Jet)(m, p, out, label)

def lift_from_local_deviation(doc, label="local_X"):
    t = decode_saved_jet(doc, label + "_minus_phi")
    out = {k: v for k, v in t.c.items() if k != (0, 0)}
    out[0, 1] = up(out[0, 1] + 1)
    return LiftJet(t.m, t.p, out, label)

def ordinary(t, a=0, b=0):
    if (a, b) not in t.c:
        raise ValueError("unpaid derivative " + t.label + str((a, b)))
    return up(ex(factorial(a)*factorial(b))*t.c[a, b])

def scalar_save(out, name, x, positive_lower=False):
    if positive_lower:
        out[name], y = lower_record(x, name)
        return y
    out[name] = record(x)
    return read_up(out[name])

def jets_save(mapping, omitted=(), radial_names=()):
    doc = emit_jets(mapping, omitted)
    work = {k: decode_saved_jet(v, k, k in radial_names) for k, v in doc.items()}
    return work, doc

def primitive_A0(t, m, p, label):
    """Only for a full A0 Fourier envelope. P has A0 norm one.
    This helper must never be applied to decoded WGS amplitude/geometry sup jets.
    """
    out = {}
    for a, b in indices(m, p):
        key = (a, 0 if b == 0 else b-1)
        if key not in t.c:
            raise ValueError("unpaid A0 primitive predecessor")
        out[a, b] = up(t.c[key]/ex(4 if b == 0 else b))
    return Jet(m, p, out, label)

def finite_composition(outer_ordinary, inner, m, p, label):
    if len(outer_ordinary) <= m:
        raise ValueError("incomplete finite composition derivative list")
    inner.need(m, p)
    delta = positive_degree(inner, m, p)
    power = constant(arb(1), m, p)
    ans = constant(outer_ordinary[0], m, p)
    for k in range(1, m+1):
        power = mul(power, delta, m=m, p=p)
        ans = add(ans, scale(power, up(outer_ordinary[k]/ex(factorial(k)))),
                  m=m, p=p, label=label)
    return ans

def exponential_A0(t, m, p, label):
    """Banach-algebra exponential; derivatives of the actual exponent."""
    t.need(m, p)
    value = up(t.c[0, 0].exp())
    return from_log_derivatives(positive_degree(t, m, p), value, m, p, label)

def derivative_series_from_ordinary(values, m, label):
    if len(values) <= m:
        raise ValueError("missing complete univariate derivative")
    return ordinary_jet({(0,k): values[k] for k in range(m+1)}, m, 0, label)

def full_input_mean_gamma_bridge(cut_mean_record, local_c, qualification):
    """Only [rc,r_plus], never a symmetric complex disk extension."""
    required = (
        "FA2_full_24_gate_success", "cut_record_qualified_at_rc",
        "same_original_germ_2549", "same_real_family_and_intrinsic_parameter",
        "V10_ordinary_radial_covers_rc_to_root_plus",
        "eta_equals_minus_gamma_mean", "eta_log_r_is_eta1_over_em")
    if any(qualification.get(k) is not True for k in required):
        raise ValueError("unqualified local mean/gamma bridge")
    old = {"mean_at_cut_lower": cut_mean_record,
           "V_r_upper": local_c["V"][1][0],
           "eta_upper": local_c["ep"],
           "eta_log_r_upper": local_c["eta_log_r"]}
    # The owner copies these old records verbatim, not normalized to a new ball.
    mc = read_lower(old["mean_at_cut_lower"], "cut mean at rc")
    vr, ep, elog = (read_up(old[k]) for k in ("V_r_upper", "eta_upper", "eta_log_r_upper"))
    rows = {}
    h = scalar_save(rows, "interval_length_upper", ex(ROOT_HI-RC))
    variation = scalar_save(rows, "mean_variation_upper", h*vr)
    attempted_mean_margin = mc-variation
    try:
        ml = scalar_save(rows, "mean_local_lower", attempted_mean_margin, True)
    except ArithmeticError as error:
        error.complete_new_prefix = {"copied_old_records":old,
            "new_complete_records":rows, "mean_positive_gate_passed":False,
            "attempted_mean_margin_ball":attempted_mean_margin.str(75),
            "attempted_mean_margin_type":"failed directed raw interval, not a norm upper",
            "qualified_real_interval":[str(RC),str(ROOT_HI)],
            "downstream_gamma_conclusion_authorized":False}
        raise
    etar = scalar_save(rows, "eta_r_upper", ep*elog)
    g = scalar_save(rows, "gamma_upper", ep/ml)
    g1 = scalar_save(rows, "gamma_r_eta_term_upper", etar/ml)
    g2 = scalar_save(rows, "gamma_r_mean_term_upper", ep*vr/(ml*ml))
    gr = scalar_save(rows, "gamma_r_upper", g1+g2)
    doc = {"copied_old_records": old, "new_complete_records": rows,
           "new_ball_slots": 8, "copied_ball_slots": 4,
           "real_interval": [str(RC), str(ROOT_HI)],
           "symmetric_complex_domain_authorized": False}
    return {"mean_lower": ml, "gamma": g, "gamma_r": gr, "eta_r": etar}, doc

# ---------------------------------------------------------------------------
# Complete C64 extension. All derivatives through 16 and the nonzero tail.
# ---------------------------------------------------------------------------
def falling_integer(n, k):
    if not 0 <= k <= n:
        raise ValueError("invalid finite falling factorial")
    return factorial(n)//factorial(n-k)

def complete_extension_scalars(qualified_original_potential):
    if qualified_original_potential is not True:
        raise ValueError("the complete potential image and M0=276 qualification are missing")
    L, margin, M0 = ex(POTENTIAL_L), ex(POTENTIAL_MARGIN), ex(276)
    chi, V, M, Bcompact, Btail = [], [], [], [], []
    out = {"chi_derivatives": [], "original_V_new_Cauchy_derivatives": [],
           "Vext_derivatives": [], "B_compact_derivatives": [],
           "B_nonzero_tail_derivatives": []}
    normal = Fraction(factorial(129), factorial(64)**2)
    for k in range(17):
        if k == 0:
            bound = arb(1)
        else:
            exact_sum = Fraction(0)
            for j in range(k):
                a, b = 64-j, 64-(k-1-j)
                maximum = Fraction((a**a)*(b**b), (a+b)**(a+b))
                exact_sum += (comb(k-1, j)*falling_integer(64,j)*
                              falling_integer(64,k-1-j))*maximum
            bound = up(ex(normal*exact_sum)*(ex(2)/L)**k)
        out["chi_derivatives"].append(record(bound))
        chi.append(read_up(out["chi_derivatives"][-1]))
        out["original_V_new_Cauchy_derivatives"].append(record(ex(factorial(k))*M0/margin**k))
        V.append(read_up(out["original_V_new_Cauchy_derivatives"][-1]))
        total = up(sum((ex(comb(k,i))*chi[i]*V[k-i] for i in range(k+1)), arb(0)))
        out["Vext_derivatives"].append(record(total))
        M.append(read_up(out["Vext_derivatives"][-1]))
        out["B_compact_derivatives"].append(record(M[k]/ex(2*k+1)))
        Bcompact.append(read_up(out["B_compact_derivatives"][-1]))
    constants = {}
    CB = scalar_save(constants, "complete_cB_upper", M0*L.sqrt())
    rising = Fraction(1)
    for k in range(17):
        if k:
            rising *= Fraction(2*k-1, 2)
        tail = up(CB*ex(rising)*pospower(L, -2*k-1, 2))
        out["B_nonzero_tail_derivatives"].append(record(tail))
        Btail.append(read_up(out["B_nonzero_tail_derivatives"][-1]))
    both = [up(max(a,b)) for a,b in zip(Bcompact,Btail)]
    out["complete_B_derivatives"] = [record(v) for v in both]
    both = [read_up(r) for r in out["complete_B_derivatives"]]
    H1 = scalar_save(constants, "complete_H1_upper",
                L*(M[2]/5+M[0]*M[0])+M[0]/(2*L))
    out["constants"] = constants
    out["cutoff_degree"] = 129
    out["cutoff_class"] = "C64 with the exact two constant exterior pieces"
    out["potential_domain"] = "[-1/2000,0] plus a closed disk of radius 1/5000"
    out["actual_original_image_lower_must_exceed"] = "7/10000"
    out["Bext_negative_tail_retained"] = True
    return {"M": M, "B": both, "CB": CB, "H1": H1, "L": L}, out

def complete_extended_amplitude_patch(patch, extension):
    T = patch["T"]
    ve = finite_composition(extension["M"], T, 12, 2, "Vext_of_T")
    be = finite_composition(extension["B"], T, 12, 2, "Bext_of_T")
    bp = finite_composition(extension["B"][1:], T, 12, 2, "Bext_prime_of_T")
    a0, b0, a1, b1 = (patch[k] for k in ("a0","b0","a1","b1"))
    a1e = add(a1, mul(be,T,b0,m=12,p=2),m=12,p=2,label="a1_ext")
    b1e = add(b1, mul(be,a0,m=12,p=2),m=12,p=2,label="b1_ext")
    # All IN.8 second/third polynomial entries, including the cB^2 cross.
    in2a = mul(be,T,b1e,m=12,p=2,label="IN2_a")
    in2b = add(mul(be,a1e,m=12,p=2),mul(bp,b0,m=12,p=2),
               m=12,p=2,label="IN2_b")
    in3b = mul(bp,b1e,m=12,p=2,label="IN3_b")
    new = {"Vext":ve,"Bext":be,"Bext_prime":bp,"a1_ext":a1e,
           "b1_ext":b1e,"IN2_a":in2a,"IN2_b":in2b,"IN3_b":in3b}
    work, saved = jets_save(new)
    return work, {"complete_jets":saved,
                  "root_and_positive_reference_unchanged":True,
                  "IN3_a_is_exactly_zero":True,
                  "cB_squared_first_Airy_cross_retained":True,
                  "shape":[12,2], "original_free_amplitudes_recomputed":0}

# ---------------------------------------------------------------------------
# Complete physical coefficients. The original fields are not residual-zero.
# ---------------------------------------------------------------------------
def complete_physical_patch(primitives, saved_drift, eta_jet):
    """primitives contains full A0 U,V and radial beta,K,gamma; total14/r1."""
    m,p = 14,1
    U,V,beta,K,gamma = (primitives[k] for k in ("U","V","beta","K","gamma"))
    U.need(15,1); V.need(15,1)
    for t in (beta,K,gamma,eta_jet,saved_drift):
        t.need(m,p)
    one = constant(arb(1),m,p)
    UU=mul(U,U,m=m,p=p); KVV=mul(K,V,V,m=m,p=p)
    S=add(UU,KVV,m=m,p=p,label="complete_S")
    L11=mul(beta,add(one,scale(UU,3),KVV,m=m,p=p),m=m,p=p,label="absolute_L11")
    L22=mul(beta,add(one,UU,scale(KVV,3),m=m,p=p),m=m,p=p,label="absolute_L22")
    ell=scale(mul(beta,U,V,m=m,p=p),2,label="absolute_ell")
    Uphi=U.derivative(0,1,m,p,"u_phi")
    Vphi=V.derivative(0,1,m,p,"v_phi")
    Iv=primitive_A0(V,m,p,"I_v")
    b2=add(L22,scale(mul(beta,K,Vphi,Iv,m=m,p=p),2),
           mul(gamma,Uphi,m=m,p=p),m=m,p=p,label="complete_b2")
    b1=mul(K,add(ell,scale(mul(beta,Uphi,Iv,m=m,p=p),2),
                  mul(gamma,Vphi,m=m,p=p),m=m,p=p),m=m,p=p,label="complete_b1")
    mapping={"U":U.part(m,p),"V":V.part(m,p),"beta":beta,"K":K,"gamma":gamma,
             "eta":eta_jet,"d":saved_drift,"S":S,"L11":L11,"L22":L22,
             "ell":ell,"U_phi":Uphi,"V_phi":Vphi,"I_v":Iv,"b1":b1,"b2":b2}
    # No numerical sign is used: the exact signed definitions are kept separately.
    work,saved=jets_save({k:t.part(m,p) for k,t in mapping.items()},
                         radial_names=("beta","K","gamma","eta"))
    return work,{"complete_A0_jets":saved,"shape":[m,p],
        "new_target":"complete posterior A0 coefficient envelope, not old WGS scalar-sup coefficient budgets",
        "exact_L11":"-beta*(1+3*u*u+K*v*v)",
        "exact_L22":"beta*(1-u*u-3*K*v*v)",
        "exact_ell":"-2*beta*u*v",
        "exact_b2":"P(L22-2*beta*K*v_phi*I(v)-gamma*u_phi)",
        "exact_b1":"K*(ell-2*beta*u_phi*I(v)+gamma*v_phi)",
        "P_has_norm_one_only_in_the_declared_A0_or_Hs_spaces":True,
        "full_physical_mean_and_background_residual_retained":True}

def strict_physical_primitives(old, saved_coefficients):
    """New physical envelope, using old Qmixed and actual finite band384.

    saved_coefficients must be WGS complete_strict_coefficient_conclusion.new_jets.
    Its d is independently a full A0 bound: complete_strict_coefficients builds
    beta*(U^2+K*V^2) in the original SJ Fourier Banach algebra, then uses I/4
    for angular degree zero and the exact derivative shift for degrees >=1.
    Fixed normalized-degree positive sums preserve that A0 bound. This does
    not reclassify any WGS geometry or amplitude sup jet as a Fourier norm.
    eta is the purely radial gamma times complete mean(V), decoded radial.
    """
    m,p=15,1
    table=old["Qmixed"]
    values={}
    for a,b in indices(m,p):
        v=table[a][b] if b<=3 else up(ex(384)**(b-3)*table[a][3])
        values[a,b]=v
    U=ordinary_jet(values,m,p,"strict_U_A0")
    V=ordinary_jet(values,m,p,"strict_V_A0")
    pp={"U":U,"V":V}
    for k in ("beta","K","gamma"):
        pp[k]=radial(old[k],m,p,"strict_"+k)
    d=decode_saved_jet(saved_coefficients["d"],"strict_saved_d")
    eta=decode_saved_jet(saved_coefficients["eta"],"strict_saved_eta",True)
    return pp,d,eta

def local_physical_primitives(c, bridge):
    """Only real [rc,r_plus]; ordinary original tables retain their full identity."""
    m,p=15,1
    margin=ex(OLD_COEFFICIENT_STRIP)
    def table_jet(name):
        values={}
        for a,b in indices(m,p):
            if b<=4:
                values[a,b]=read_up(c[name][a][b])
            else:
                values[a,b]=up(ex(factorial(b-4))*read_up(c[name][a][4])/margin**(b-4))
        return ordinary_jet(values,m,p,"local_"+name+"_A0")
    pp={"U":table_jet("U"),"V":table_jet("V")}
    pp["beta"]=radial([read_up(c["beta"]),read_up(c["beta_r"])],m,p,"local_beta")
    pp["K"]=radial([read_up(c["K"]),read_up(c["Kr"])],m,p,"local_K")
    pp["gamma"]=radial([bridge["gamma"],bridge["gamma_r"]],m,p,"local_gamma")
    eta=radial([read_up(c["ep"]),bridge["eta_r"]],m,p,"local_eta")
    vals={}
    for a,b in indices(m,p):
        source=c["D"] if a==0 else c["Dr"]
        last=5 if a==0 else 2
        vals[a,b]=(read_up(source[b]) if b<=last else
                   up(ex(factorial(b-last))*read_up(source[last])/margin**(b-last)))
    return pp,ordinary_jet(vals,m,p,"local_saved_d_and_new_high_jets"),eta

# ---------------------------------------------------------------------------
# Same angular inverse, strict JI recipe and local old J0. No new inverse chosen.
# ---------------------------------------------------------------------------
def wiener_at_most_one(t, s):
    s=abs(Fraction(s))
    if s>1:
        raise ValueError("this multiplier recipe is only for |s|<=1")
    # <4j>^s <= 1+|4j|; the A0 derivative norm sums every Fourier mode.
    return ordinary(t) if s==0 else up(ordinary(t)+ordinary(t,0,1))

def complete_same_J_patch(physical, eta_lower, local_old=None):
    P=physical
    U,V,beta,ell,Uphi,Vphi=(P[k] for k in ("U","V","beta","ell","U_phi","V_phi"))
    em=lower(eta_lower,"same physical eta")
    b=ordinary(beta); br=ordinary(beta,1,0)
    uu,vv=ordinary(U),ordinary(V)
    ui=up(min(uu,ordinary(Uphi)/4))
    vi=up(min(vv/4,ordinary(Vphi)/16))
    rows={}
    alpha=scalar_save(rows,"alpha_absolute_upper",2*b/em)
    loga=scalar_save(rows,"aJ_log_modulus_upper",alpha*uu*vv/4)
    ap=scalar_save(rows,"aJ_and_inverse_upper",loga.exp())
    amin=scalar_save(rows,"aJ_positive_lower",(-loga).exp(),True)
    if local_old is None:
        if not (uu<8 and vv<8 and ordinary(Uphi)<7 and
                ordinary(Vphi)<7 and b<ex(Fraction(1,4)) and em>1):
            raise ArithmeticError("the original whole strict JI premises were not admitted")
        ds=scalar_save(rows,"strict_JI_DJ_lower",
                       ex(Fraction(79,128))*(-ex(Fraction(7,4))).exp(),True)
        Cc=scalar_save(rows,"strict_complete_Cc_upper",ap*ui/(4*em*ds))
        Cp=scalar_save(rows,"strict_complete_Cp_upper",
                       ap*ap/4*(ui/(4*em)+Cc*(1+alpha*ui*vi)))
        J0=scalar_save(rows,"same_J_L2_upper",1/(4*em)+alpha*vv*Cp+alpha*vi*Cc)
        L0=scalar_save(rows,"same_L_L2_upper",ordinary(ell)+b*ordinary(Vphi)*uu/2)
        old_copy={}
    else:
        if local_old.get("same_full_germ_even0_to_odd") is not True:
            raise ValueError("local J0 does not have the required ordinary angular domain")
        old_copy={"same_J_L2_upper":local_old["J0"],
                  "same_L_L2_upper":local_old["L0"]}
        J0=read_up(old_copy["same_J_L2_upper"])
        L0=read_up(old_copy["same_L_L2_upper"])
        ds=None
    dstruct=scalar_save(rows,"complete_structural_DJ_lower",
                        amin/(1+2*b*uu*J0*vv),True)
    dl=scalar_save(rows,"complete_selected_DJ_lower",
                   dstruct if ds is None else max(dstruct,ds),True)
    Lt={}
    for key,s in (("minus_one",-1),("minus_two_thirds",Fraction(-2,3)),
                  ("zero",0),("one_third",Fraction(1,3))):
        if s==0:
            Lt[key]=L0
        else:
            Lt[key]=scalar_save(rows,"L_"+key+"_upper",
                wiener_at_most_one(ell,s)+b*wiener_at_most_one(Vphi,s)*
                wiener_at_most_one(U,s)/2)
    ci=scalar_save(rows,"physical_I_gain_upper",ex(17).sqrt()/4)
    pp=scalar_save(rows,"P0_gain_upper",ci/em)
    gm2=scalar_save(rows,"same_J_Hminus2_to_Hminus1_upper",
             pp+pp*pp*Lt["minus_one"]+J0*pp*pp*L0*Lt["minus_one"])
    gm53=scalar_save(rows,"same_J_Hminus5_3_to_Hminus2_3_upper",
             pp+pp*pp*Lt["minus_two_thirds"]+
             J0*pp*pp*Lt["one_third"]*Lt["minus_two_thirds"])
    scalar_save(rows,"same_IJ_Hminus2_to_L2_upper",ci*gm2)
    jp=scalar_save(rows,"same_J_left_angular_derivative_upper",(1+L0*J0)/em)
    g0=scalar_save(rows,"same_J_L2_to_H1_upper",(J0*J0+jp*jp).sqrt())
    Lr=scalar_save(rows,"complete_L_radial_L2_upper",
         ordinary(ell,1,0)+(br*ordinary(Vphi)*uu+
          b*ordinary(Vphi,1,0)*uu+b*ordinary(Vphi)*ordinary(U,1,0))/2)
    etar=ordinary(P["eta"],1,0)
    Jr=scalar_save(rows,"same_J_radial_L2_upper",J0*(etar*jp+Lr*J0))
    doc={"new_complete_records":rows,"copied_old_records":old_copy,
         "space":"the original angular even-mean-zero to odd realization",
         "finite_inverse_identity":"P0-P0*L*P0+J*(L*P0)^2",
         "root_and_strict_inverses_agree_only_on_their_actual_overlap":True,
         "stable_trace_inverse_used":False,"physical_means_discarded":False}
    eta_record, em_retained = lower_record(em,"same angular eta")
    rows["same_eta_positive_lower"] = eta_record
    work={"J0":J0,"L0":L0,"DJ_lower":dl,"aJ_upper":ap,"aJ_lower":amin,
          "alpha":alpha,"Lr0":Lr,"Jr0":Jr,"Jphi0":jp,
          "Gamma_minus2":gm2,"Gamma_minus5_3":gm53,"Gamma_zero":g0,
          "cI":ci,"eta_lower":em_retained,
          "J0_upper":old_copy.get("same_J_L2_upper",rows.get("same_J_L2_upper")),
          "L0_upper":old_copy.get("same_L_L2_upper",rows.get("same_L_L2_upper")),
          "eta_lower_record":eta_record}
    return work,doc

# ---------------------------------------------------------------------------
# Full mean duals, radial feedback, and the exact N6 degree-nine mean polynomial.
# ---------------------------------------------------------------------------
def complete_mean_kernel_patch(P,J):
    m,p=8,1
    U,V,beta,K,eta,d=(P[k] for k in ("U","V","beta","K","eta","d"))
    em=J["eta_lower"]; dl=J["DJ_lower"]
    meanV=radial([ordinary(V),ordinary(V,1,0)],m,p,"absolute_physical_mean")
    etai=reciprocal(eta,em,m,p,"eta_inverse")
    alpha=scale(mul(beta,etai,m=m,p=p),2,label="alpha")
    Iuv=primitive_A0(mul(U,V,m=m,p=p),m,p,"I_uv")
    exponent=mul(alpha,Iuv,m=m,p=p,label="aJ_exponent_absolute")
    aJ=exponential_A0(exponent,m,p,"aJ")
    Iv=P["I_v"].part(m,p)
    integrand=mul(aJ,add(constant(arb(1),m,p),
                        mul(alpha,U,Iv,m=m,p=p),m=m,p=p),
                  m=m,p=p,label="DJ_integrand_absolute")
    rows={}
    DJup=scalar_save(rows,"complete_DJ_upper",ordinary(integrand))
    DJr=scalar_save(rows,"complete_DJ_r_upper",ordinary(integrand,1,0))
    dj=radial([DJup,DJr],m,p,"DJ_modulus_and_radial_derivative")
    dji=reciprocal(dj,dl,m,p,"DJ_inverse")
    e=scale(mul(beta,meanV,etai,dji,
                 primitive_A0(mul(aJ,U,m=m,p=p),m,p,"I_aJ_u"),
                 m=m,p=p),2,label="dual_e")
    # H2*e includes -(d*e)' in full, with the coefficient derivative.
    mm,pp=6,0
    de=mul(d,e,m=7,p=0,label="d_times_e")
    H2e=add(de.derivative(0,1,mm,pp),
        mul(P["L22"],e,m=mm,p=pp),
        scale(mul(beta,K,V,
          primitive_A0(mul(P["V_phi"],e,m=mm,p=pp),mm,pp,"I_vphi_e"),
          m=mm,p=pp),2),m=mm,p=pp,label="H2_adjoint_e_absolute")
    # ||Pv||_A0 <= ||v||_A0. Its true mean is removed only inside this kernel.
    ek=add(H2e,scale(mul(beta,meanV,K,V,m=mm,p=pp),2),
           m=mm,p=pp,label="dual_ekappa")
    er=e.derivative(1,0,6,0,"dual_e_r")
    b=ordinary(beta); kabs=ordinary(K); meanabs=ordinary(V)
    S0=ordinary(P["S"]); b20=ordinary(P["b2"])
    k0=scalar_save(rows,"complete_k_L2_upper",J["J0"]*b20)
    kp=scalar_save(rows,"complete_k_phi_L2_upper",(b20+J["L0"]*k0)/em)
    kr=scalar_save(rows,"complete_k_r_L2_upper",
       J["J0"]*(ordinary(P["b2"],1,0)+ordinary(eta,1,0)*kp+J["Lr0"]*k0))
    cb=scalar_save(rows,"complete_cb_upper",ordinary(U)*k0)
    feedback=scalar_save(rows,"complete_feedback_upper",
                  2*b*meanabs*(cb+kabs*meanabs))
    base=scalar_save(rows,"complete_mean_base_upper",b*(1+S0))
    ae=scalar_save(rows,"complete_aeff_upper",base+feedback)
    E0=scalar_save(rows,"complete_E_L2_upper",
           ordinary(P["L11"])+b*ordinary(P["U_phi"])*ordinary(U)/2)
    Rm=scalar_save(rows,"complete_Rmean_L2_upper",
           kr+ordinary(d)*kp+(E0+ae)*k0+ordinary(P["b1"]))
    scalar_save(rows,"complete_I_k_L2_upper",k0/4)
    scalar_save(rows,"complete_I_Rmean_L2_upper",Rm/4)
    nf=add(er,scale(e,ae,6,0),H2e,
             scale(mul(beta,meanV,K,V,m=6,p=0),2),
             m=6,p=0,label="complete_mean_normalform_kernel")
    work,jetdoc=jets_save({"aJ":aJ,"dual_e":e,"dual_e_r":er,
                           "dual_ekappa":ek,"mean_normalform_kernel":nf})
    doc={"complete_jets":jetdoc,"new_complete_records":rows,
         "dual_e_exact":"-2*beta*m/(eta*DJ) * I(aJ*u)",
         "dual_ekappa_exact":"-H2_adjoint*dual_e+2*beta*m*K*(v-m)",
         "physical_mean_equation":"z_r=aeff*z-Fmean; z(root)=0",
         "complete_feedback_exact":"2*beta*H/DJ",
         "complete_propagator_identity":
             "a_phys(r)/a_phys(s)*sqrt(EG(r)/EG(s))*exp(integral_s^r 2*beta*H/DJ)",
         "R0_in_the_alternative_mean_ratio_formula_retained":True,
         "same_Jr_and_all_coefficient_radial_derivatives_retained":True,
         "no_gamma_lower_division_used_in_the_positive_feedback_bound":True}
    work.update({"aeff":ae,"k0":k0,"kphi0":kp,"kr0":kr,"Rm0":Rm,
                 "Ik0":read_up(rows["complete_I_k_L2_upper"]),
                 "IRm0":read_up(rows["complete_I_Rmean_L2_upper"]),
                 "retained_records":rows})
    return work,doc

def polynomial_save(poly,label):
    doc=[emit_jet(t) for t in poly]
    work=[decode_saved_jet(r,label+"_"+str(k)) for k,r in enumerate(doc)]
    return work,doc

def angular_A_polynomial(poly, ve_tphi, m, label):
    out=[zero(m,0,label+"_"+str(k)) for k in range(len(poly)+1)]
    for k,t in enumerate(poly):
        out[k]=add(out[k],t.derivative(0,1,m,0),m=m,p=0)
        out[k+1]=add(out[k+1],mul(ve_tphi,t,m=m,p=0),m=m,p=0)
    return out

def complete_mean_N6_patch(patch,ext,kernel,point_profile_upper):
    m=6
    e=kernel["dual_e"]; ek=kernel["dual_ekappa"]
    T=patch["T"]; X=patch["X"]
    Tr=T.derivative(1,0,m,0); Xr=X.derivative(1,0,m,0)
    mr=add(scale(Xr,2),mul(Tr,add(constant(arb(1),m,0),T,m=m,p=0),
                          m=m,p=0),m=m,p=0,label="Mr_entry_sum")
    w0=add(patch["a0"],patch["b0"],m=m,p=0,label="w0_sum")
    w1=add(ext["a1_ext"],ext["b1_ext"],m=m,p=0,label="w1ext_sum")
    w0r=add(patch["a0"].derivative(1,0,m,0),
             patch["b0"].derivative(1,0,m,0),m=m,p=0)
    w1r=add(ext["a1_ext"].derivative(1,0,m,0),
             ext["b1_ext"].derivative(1,0,m,0),m=m,p=0)
    ve=ext["Vext"]
    p0=mul(e,mr,w0,m=m,p=0)
    p1=add(mul(e,mr,w1,m=m,p=0),mul(e,w0r,m=m,p=0),
             mul(ek,w0,m=m,p=0),m=m,p=0)
    p2=add(mul(e,w1r,m=m,p=0),
             mul(e,ve,Tr,patch["b0"],m=m,p=0),
             mul(ek,w1,m=m,p=0),m=m,p=0)
    p3=mul(e,ve,Tr,ext["b1_ext"],m=m,p=0)
    initial,initial_doc=polynomial_save([p0,p1,p2,p3],"mean_initial")
    Hinv=patch["H_inverse_entry_sum"]
    ve_tphi=mul(ve,T.derivative(0,1,m,0),m=m,p=0)
    vv=[mul(Hinv,t,m=m,p=0) for t in initial]
    vv,vdoc=polynomial_save(vv,"mean_v0")
    levels=[vdoc]
    for step in range(1,6):
        mm=m-step
        av=angular_A_polynomial(vv,ve_tphi,mm,"mean_A_"+str(step))
        vv=[mul(Hinv,t,m=mm,p=0) for t in av]
        vv,vdoc=polynomial_save(vv,"mean_v"+str(step))
        levels.append(vdoc)
    terminal=angular_A_polynomial(vv,ve_tphi,0,"mean_terminal")
    terminal,tdoc=polynomial_save(terminal,"mean_terminal")
    if len(terminal)!=MAX_Z_DEGREE+1:
        raise ValueError("the complete degree-nine mean polynomial was not retained")
    rows={}; weighted=[]
    for k,t in enumerate(terminal):
        weighted.append(scalar_save(rows,"terminal_degree_"+str(k)+"_weighted_upper",
                                    ordinary(t)/ex(N0)**k))
    amplitude=scalar_save(rows,"complete_mean_terminal_amplitude_upper",
                          sum(weighted,arb(0)))
    single=scalar_save(rows,"single_signed_mean_source_upper",
                       point_profile_upper*amplitude)
    complete=scalar_save(rows,"complete_reflected_mean_source_upper",2*single)
    return {"single_CF":single,"CF":complete}, {
        "complete_initial_z_polynomial":initial_doc,
        "complete_six_inverse_polynomial_levels":levels,
        "complete_terminal_z_polynomial":tdoc,
        "new_complete_records":rows,
        "z_variable":"n^-1, not the physical mean",
        "retained_degrees":[0,1,2,3,4,5,6,7,8,9],
        "source_power_before_N6":"13/6","complete_source_decay_power":"23/6",
        "point_profile_is_one_signed_genuine_column":True,
        "reflected_assembly_factor":2,
        "independent_second_reference_port_eliminated":False,
        "all_six_angular_operations_and_the_last_terminal_retained":True}

def complete_mean_union(kernel_by_patch, source_by_patch):
    if set(kernel_by_patch)!={"strict","local"} or set(source_by_patch)!={"strict","local"}:
        raise ValueError("both complete real patches are required")
    rows={}
    a=scalar_save(rows,"complete_union_aeff_upper",
             max(v["aeff"] for v in kernel_by_patch.values()))
    CF=scalar_save(rows,"complete_union_mean_source_upper",
             max(v["CF"] for v in source_by_patch.values()))
    G=scalar_save(rows,"complete_backward_mean_propagator_upper",(ex(ROOT_HI)*a).exp())
    Z=scalar_save(rows,"complete_physical_mean_upper",ex(ROOT_HI)*G*CF)
    Zr=scalar_save(rows,"complete_physical_mean_radial_upper",a*Z+CF)
    # This is a whole positive Gronwall alternative, not removal of the feedback.
    return {"CF":CF,"Z":Z,"Zr":Zr,"Gmean":G,"retained_records":rows}, {
        "new_complete_records":rows,
        "ordinary_radial_measure":True,
        "complete_root_to_waist_mean":True,
        "coefficient_power":"n^(-23/6)",
        "same_continuous_trial_and_scalar_mean_across_all_true_seams":True,
        "root_mean_initial_value":0,
        "normalform_root_and_waist_terms_are_an_exact_alternative_not_omitted":True,
        "full_feedback_and_R0_not_assumed_zero":True}

# ---------------------------------------------------------------------------
# Complete exact-profile C4 kernel: near ODE plus far Jost, all low outputs.
# ---------------------------------------------------------------------------
def stirling_second(n,k):
    if n==0:
        return 1 if k==0 else 0
    if k==0 or k>n:
        return 0
    return stirling_second(n-1,k-1)+k*stirling_second(n-1,k)

def complete_Jost_scalars(extension):
    """WUB.15 exact finite Euler polynomial, then WUB.12 through order five."""
    L=extension["L"]; M=extension["M"]
    constant_part=Fraction(5,36)
    terms={(0,2):Fraction(4,9)}
    Q=[]; exact=[]; saved_Q=[]
    for k in range(6):
        val=ex(abs(constant_part))
        for (j,power),coefficient in terms.items():
            val += ex(abs(coefficient))*L**power*M[j]
        saved_Q.append(record(up(val))); Q.append(read_up(saved_Q[-1]))
        exact.append({"constant":str(constant_part),
             "terms":[{"V_derivative":j,"s_power":p,"coefficient":str(c)}
                      for (j,p),c in sorted(terms.items())]})
        if k<5:
            new={}
            for (j,power),coefficient in terms.items():
                key=(j,power)
                new[key]=new.get(key,Fraction(0))+coefficient*(Fraction(2,3)*power-2-k)
                key=(j+1,power+1)
                new[key]=new.get(key,Fraction(0))-Fraction(2,3)*coefficient
            terms={key:c for key,c in new.items() if c}
            constant_part*=(-2-k)
    rows={}
    A=scalar_save(rows,"complete_Jost_modulus_upper",Q[0].exp())
    pref=scalar_save(rows,"complete_Jost_recursion_prefactor",(Q[0]/2).exp()/2)
    C=[A]; saved_C=[record(A)]
    for k in range(1,6):
        first=A*Q[k-1]
        boundary=sum((ex(comb(k-1,l))*Q[l]*C[k-1-l]
                      for l in range(k-1)),arb(0))
        integral=A*Q[k]/ex(k+1)
        other=sum((ex(comb(k,l))*Q[l]*C[k-l]/ex(k+2)
                   for l in range(1,k)),arb(0))
        saved_C.append(record(up(pref*(first+boundary+integral+other))))
        C.append(read_up(saved_C[-1]))
    # Euler derivatives: t>=1, so the extra t^-1 or t^-2 is at most one.
    E=[A]; Ep=[C[1]]
    for m in range(1,5):
        E.append(up(sum((ex(stirling_second(m,k))*C[k] for k in range(1,m+1)),arb(0))))
        Ep.append(up(sum((ex(stirling_second(m,k))*C[k+1] for k in range(1,m+1)),arb(0))))
    doc={"exact_five_Euler_polynomials":exact,"complete_Q_0_5":saved_Q,
         "complete_C_0_5":saved_C,"new_complete_records":rows,
         "complete_Euler_a_0_4":[record(v) for v in E],
         "complete_Euler_aprime_0_4":[record(v) for v in Ep],
         "genuine_Jost_basis_fixed_at_true_infinity":True,
         "complete_input_dependent_Sn_retained":True,
         "input_frequency_derivatives_used":False}
    return {"E":[read_up(r) for r in doc["complete_Euler_a_0_4"]],
            "Ep":[read_up(r) for r in doc["complete_Euler_aprime_0_4"]]},doc

def complete_profile_geometry(patch,which,tstar,strict_phase_lower,old_fold):
    if which not in ("strict","local"):
        raise ValueError("unknown actual profile patch")
    T,X=patch["T"],patch["X"]; rows={}
    ts=lower(tstar,"whole T/rho")
    if which=="strict":
        rho=scalar_save(rows,"strict_rho_lower",ex(ROOT_LO-RC),True)
        qrho=scale(T,1/rho,4,0,"strict_abs_T_over_rho")
        ph=[ordinary(patch["phase"],0,k) for k in range(1,5)]
        ml=lower(strict_phase_lower,"saved strict phase gap")
    else:
        # T(root,phi)=0 identically. Apply the fundamental theorem in ordinary r.
        qrho=T.derivative(1,0,4,0,"local_regular_abs_T_over_rho")
        E=read_up(old_fold["E"]); TM=read_up(old_fold["TM"]); BT=read_up(old_fold["BT"])
        ml=scalar_save(rows,"local_phase_and_X_lower",2-E-up(TM.sqrt()*BT),True)
        halfgap=power_jet(qrho,ts,Fraction(3,2),4,0,"q_to_three_halves")
        phase_add=scale(halfgap,ex(Fraction(2,3))*pospower(ex(ROOT_HI-RC),3,2))
        ph=[up(ordinary(X,0,k)+ordinary(phase_add,0,k)) for k in range(1,5)]
    # The near X and each far phase are different maps with these common bounds.
    ph=[up(max(v,ordinary(X,0,k))) for k,v in enumerate(ph,1)]
    phase_rows=[record(v) for v in ph]; ph=[read_up(r) for r in phase_rows]
    ml=scalar_save(rows,"complete_phase_lower",ml,True)
    q_work,q_doc=jets_save({"T_over_rho":qrho})
    return {"q":q_work["T_over_rho"],"q_lower":ts,"phase_lower":ml,
            "phase_derivatives":ph,"T_upper":ordinary(T)},{
        "new_complete_records":rows,"complete_phase_derivatives_1_4":phase_rows,
        "complete_regular_quotient_jet":q_doc["T_over_rho"],
        "actual_near_X_and_both_far_Phi_maps_kept_distinct":True,
        "local_quotient_uses_T_root_identically_zero":which=="local",
        "individual_root_Phi_radial_derivative_used":False}

def complete_profile_patch(patch,geometry,extension,Jost):
    q=geometry["q"]; qlow=geometry["q_lower"]; rows={}
    R0=scalar_save(rows,"complete_near_radius_scale",pospower(ex(Fraction(3,2)),2,3)/qlow)
    xs=scalar_save(rows,"complete_scaled_near_factor",pospower(ex(2),5,3)*R0)
    xmax=scalar_save(rows,"complete_scaled_near_T_upper",xs*ordinary(q))
    M=extension["M"]
    n43=pospower(ex(N0),-4,3)
    near=[ex(12),up(ex(12)*pospower(1+xmax,1,4))]
    near_records=[record(v) for v in near]
    near=[read_up(r) for r in near_records]
    for k in range(4):
        val=(xmax+n43*M[0])*near[k]
        if k:
            val+=ex(k)*near[k-1]
        val+=n43*sum((ex(comb(k,j))*M[j]*pospower(ex(N0),-2*j,3)*near[k-j]
                     for j in range(1,k+1)),arb(0))
        near_records.append(record(up(val))); near.append(read_up(near_records[-1]))
    xi=scale(q,xs,4,0,"scaled_T_angular_jet")
    near0=finite_composition(near,xi,4,0,"near_Y")
    near1=scale(finite_composition(near[1:],xi,4,0,"near_Yxi"),
                pospower(ex(N0),-1,3))
    nb=scalar_save(rows,"complete_near_bN_inverse_upper",pospower(1+2*R0,1,4))
    near_pair=scale(add(near0,near1,m=4,p=0),nb,label="near_profile_component_sum")
    # Far phase amplitudes. log(t) has angular derivatives (3/2) log(q).
    logt=scale(log_derivatives(q,qlow,4,0,"log_q"),ex(Fraction(3,2)))
    aa=finite_composition(Jost["E"],logt,4,0,"far_a_of_log_t")
    ap=finite_composition(Jost["Ep"],logt,4,0,"far_aprime_of_log_t")
    invt=from_log_derivatives(logt,arb(1),4,0,"absolute_one_over_t_jet")
    qfour=power_jet(q,qlow,Fraction(-1,4),4,0,"q_inverse_fourth")
    sq=scale(power_jet(q,qlow,Fraction(1,2),4,0,"sqrt_q"),ex(ROOT_HI).sqrt())
    bracket=add(aa,scale(mul(invt,aa,m=4,p=0),ex(Fraction(1,6))),ap,m=4,p=0)
    far_pair=mul(qfour,add(aa,mul(sq,bracket,m=4,p=0),m=4,p=0),m=4,p=0)
    fb=scalar_save(rows,"complete_far_bN_conversion_upper",pospower(1+1/R0,1,4))
    # Each phase coefficient of one column is <=6/5 after the fixed Ai/Bi basis.
    # sqrt(pi)>=1 is used as a safe exact upper for its reciprocal.
    far_pair=scale(far_pair,ex(Fraction(6,5))*fb,label="one_far_phase_profile")
    whole=add(near_pair,scale(far_pair,2),m=4,p=0,
              label="complete_near_plus_both_far_profile")
    Pstar=scalar_save(rows,"single_signed_point_profile_upper",
                     12*(2+geometry["T_upper"].sqrt()))
    jet_work,jetdoc=jets_save({"near_profile":near_pair,"one_far_phase":far_pair,
                              "complete_profile":whole})
    # Finite inverse phase jets and the full-circle H^-2 pullback norm.
    ml=geometry["phase_lower"]; f1,f2,f3,f4=geometry["phase_derivatives"]
    inv1=scalar_save(rows,"inverse_phase_derivative_1_upper",1/ml)
    inv2=scalar_save(rows,"inverse_phase_derivative_2_upper",f2/ml**3)
    inv3=scalar_save(rows,"inverse_phase_derivative_3_upper",f3/ml**4+3*f2*f2/ml**5)
    inv4=scalar_save(rows,"inverse_phase_derivative_4_upper",
              f4/ml**5+10*f2*f3/ml**6+15*f2*f2*f2/ml**7)
    K0=scalar_save(rows,"complete_phase_pullback_L2_upper",1/ml.sqrt())
    K2=scalar_save(rows,"complete_phase_pullback_Hminus2_upper",
          f1.sqrt()*(inv1+ex(2).sqrt()*(inv2+inv1*inv1)+
                     inv3+3*inv1*inv2+inv1*inv1*inv1))
    inverse={1:inv1,2:inv2,3:inv3,4:inv4}
    profile=jet_work["complete_profile"]
    # The same complete matrix envelope holds for both physical input signs.
    # Output k=0 and all low outputs remain in the weighted Schur sum.
    weights={}
    for key,d in (("zero",Fraction(0)),("five_thirds",Fraction(5,3)),("two",Fraction(2))):
        Kd=scalar_save(rows,"complete_phase_pullback_"+key+"_upper",
            K0 if d==0 else pospower(K0,(2*d.denominator-d.numerator),2*d.denominator)*
                             pospower(K2,d.numerator,2*d.denominator))
        # sum_{l!=0} <4l>^d/(4|l|)^4 <=17/64 for all 0<=d<=2.
        wl=[]
        for a in range(5):
            val=ordinary(profile) if a==0 else arb(0)
            derivative4=arb(0)
            for j in range(1,5):
                if a<=j:
                    derivative4 += (bell(4,j,inverse)*ex(comb(j,a))*
                                    ordinary(profile,0,j-a))
            val+=ex(Fraction(17,64))*derivative4
            wl.append(record(up(pospower(ex(2),d.numerator,2*d.denominator)*Kd*val)))
        weights[key]=wl
    doc={"new_complete_records":rows,"complete_near_scaled_ODE_derivatives_0_5":near_records,
         "complete_profile_jets":jetdoc,"complete_full_output_block_weights":weights,
         "weight_input":"sum_{a=0}^4 weight[a] times full ordinary angular amplitude component-sum derivative[a]",
         "block_bound":"N^-d * (1+N^(2/3)*rho)^(-1/4) * weighted_amplitude_sum",
         "full_output_zero_and_low_modes_retained":True,
         "no_output_block_orthogonality_used":True,
         "partition_used_only_in_the_estimate_not_inserted_in_the_trial":True,
         "single_signed_reference_column":True,
         "complete_block_includes_all_signed_Fourier_inputs":True,
         "near_partition_has_zero_angular_derivatives":True,
         "two_Jost_phases_already_included":True,
         "independent_second_reference_port_eliminated":False}
    return {"Pstar":Pstar,"Pstar_record":rows["single_signed_point_profile_upper"],
            "block_weights":{k:[read_up(r) for r in v] for k,v in weights.items()},
            "block_weight_records":weights},doc

# ---------------------------------------------------------------------------
# Read-only WGS handoff and declared graph interfaces. No numerical driver.
# ---------------------------------------------------------------------------
def readonly_WGS_handoff(main,copies,verified_pair):
    """The owner first checks both immutable file bytes and the bidirectional IDs."""
    if verified_pair is not True:
        raise ValueError("the two actual WGS files have not been admitted")
    if not (main.get("complete") is True and main.get("proved") is True
            and main.get("actual_returncode")==0 and len(main.get("gates",[]))==24
            and all(g.get("passed") is True for g in main["gates"])
            and copies.get("complete") is True):
        raise ValueError("not the complete successful WGS pair")
    for key in ("run_id","run_attempt","source_sha256","math_module_sha256",
                "input_manifest_sha256","actual_scientific_checkout_commit"):
        if main.get(key)!=copies.get(key):
            raise ValueError("WGS two-file identity disagreement: "+key)
    if main["complete_derivative_request_certificate"]["fixed_degree_groups"] != [list(g) for g in JET_GROUPS]:
        raise ValueError("unrecognized WGS finite-jet grouping")
    strict={}
    for field in ("complete_strict_geometry_conclusion","complete_strict_leading_conclusion"):
        for name,doc in main[field]["complete_jets"].items():
            strict[name]=decode_saved_jet(doc,"strict_"+name)
    for name,doc in main["complete_strict_forcing_conclusion"]["complete_forcing_jets"].items():
        strict[name]=decode_saved_jet(doc,"strict_"+name)
    for name,doc in main["complete_free_first_transport_conclusion"]["complete_jets"].items():
        strict[name]=decode_saved_jet(doc,"strict_"+name)
    strict["T"]=strict["t"]
    strict["X"]=strict["X_derivatives"]
    strict["phase"]=strict["phase_derivatives"]
    local={k:decode_saved_jet(v,"local_"+k) for k,v in
           main["complete_local_regular_packet_conclusion"]["complete_jets"].items()}
    local["X"]=lift_from_local_deviation(
        main["complete_local_regular_packet_conclusion"]["complete_jets"]["X_minus_phi"])
    # T is signed in the function identities, but every Jet is an absolute envelope.
    records=copies["copied_original_scalar_records"]
    old={"Qmixed":[[read_up(records["Q_"+str(a)+"_"+str(b)]) for b in range(4)]
                    for a in range(3)]}
    for key in ("beta","K","gamma"):
        old[key]=[read_up(records[key+"_"+str(a)]) for a in range(4)]
    old["strict_eta_lower"]=read_lower(records["eta_lower"],"original strict eta")
    old["local_eta_lower"]=read_lower(copies["copied_complete_local_coefficients"]["em"],"local eta")
    old["strict_phase_lower"]=read_lower(
        main["complete_higher_flow_and_cut_conclusion"]["strict_phase_lower"],"saved strict phase")
    old["whole_t_over_rho_lower"]=read_lower(
        main["complete_strict_geometry_conclusion"]["complete_positive_lowers"]["whole_t_over_rho"],
        "saved whole T/rho")
    old["strict_t_lower"]=read_lower(records["t_cut_lower"],"saved strict T")
    old["strict_t_lower_record"]=records["t_cut_lower"]
    old["whole_t_over_rho_record"]=main["complete_strict_geometry_conclusion"][
        "complete_positive_lowers"]["whole_t_over_rho"]
    return {"patches":{"strict":strict,"local":local},
            "old":old,"strict_saved_coefficients":
                main["complete_strict_coefficient_conclusion"]["new_jets"],
            "local_c":copies["copied_complete_local_coefficients"],
            "old_fold":copies["copied_original_stage_records"]["fold"],
            "norm_types":{"WGS_geometry_and_amplitude":"scalar sup or component-sup sum",
                          "physical_U_V_tables":"complete Fourier A0",
                          "strict_saved_drift":"independent full Fourier A0 from WGS coefficient Banach products and primitive",
                          "strict_saved_eta":"purely radial coefficient; no angular derivatives",
                          "aJ_and_dual_kernels":"new complete Fourier A0",
                          "J0":"ordinary angular L2 even0-to-odd"},
            "selected_real_member_only":True}


def posterior_bundle_for_residual(handoff,extended,physical,J,kernels,profile,mean_union):
    """Types for the new residual module. Records are original retained strings."""
    result={}
    for patch in ("strict","local"):
        g=handoff["patches"][patch]
        result[patch]={
          "physical_coefficients":physical[patch],
          "geometry":{
            "X":g["X"],"T":g["T"],"Q":g["Q"],
            "X_derivative_jet":g["X"],"T_absolute_jet":g["T"],
            "T_derivative_absolute_jet":g["T"],
            "X_phi_jet":g["X"].derivative(0,1,14,3),
            "T_phi_absolute_jet":g["T"].derivative(0,1,14,3),
            "H_inverse_entry_sum":g["H_inverse_entry_sum"],
            "mu_inverse":g["mu_inverse"],"Fa":g["Fa"],"Fb":g["Fb"]},
          "amplitudes":{"w0_pair":[g["a0"],g["b0"]],
                        "w1ext_pair":[extended[patch]["a1_ext"],extended[patch]["b1_ext"]],
                        "a1ext":extended[patch]["a1_ext"],"b1ext":extended[patch]["b1_ext"]},
          "potential":{"V_of_T_jet":extended[patch]["Vext"],
                       "Vext":extended[patch]["Vext"],
                       "Bext":extended[patch]["Bext"],
                       "Bext_prime":extended[patch]["Bext_prime"]},
          "same_J":dict(J[patch],eta_lower=J[patch]["eta_lower_record"]),
          "mean":kernels[patch],
          "qualifications":{"complete_WUA_transport_cancellation":True,
                            "same_original_reflected_column":True,
                            "all_future_arithmetic_values_require_complete_graph_admission":True},
          "scalar_Q_identity":
              "A*(D0-E)*J*(D0-B)-A*K*C; all exact commutators and means retained",
          "positive_Jet_subtraction_used_to_prove_cancellation":False}
    result["strict"]["geometry"].update(
        x=handoff["patches"]["strict"]["x"],y=handoff["patches"]["strict"]["y"],
        strict_T_lower=handoff["old"]["strict_t_lower_record"])
    return {
      "complete_patches":result,
      "complete_block_receiver_weights":{
          k:{"0":profile[k]["block_weight_records"]["zero"],
             "-5/3":profile[k]["block_weight_records"]["five_thirds"],
             "-2":profile[k]["block_weight_records"]["two"]} for k in ("strict","local")},
      "block_rows_include_complete_reflected_assembly":True,
      "block_reflection_qualification":
          "uniform coefficients on all signed Fourier j; both true phases retained; restriction to the normalized real reflected carrier has norm one",
      "single_signed_pointwise_upper":{k:profile[k]["Pstar_record"] for k in ("strict","local")},
      "whole_t_over_rho_lower":handoff["old"]["whole_t_over_rho_record"],
      "complete_mean":mean_union,
      "true_jump_interface":{
          "total_original_interfaces":3070,"all_original_interfaces_in_strict_patch":True,
          "each_subset_count_upper":3070,
          "actual_subsets_disjoint_at_original_PW_cut":True,
          "collar_rho_lower":str(ROOT_LO-RC),
          "strict_rho_lower":str(ROOT_LO-Fraction(2333968743003,10**13)),
          "forcing_difference_rule":"actual two one-sided forcing jets; their sum is a positive bound",
          "waist_cut_and_root_endpoints_are_not_artificial_jumps":True,
          "j2_exactly_zero_only_for_the_continuous_completed_WUA_trial":True},
      "complete_whole_error_claimed":False,
      "complete_four_endpoint_constants_claimed":False,
      "finite_Schur_or_full_incoming_inverse_claimed":False}

def complete_static_demand_certificate():
    return {
      "kind":"static_WEJ_extension_profile_sameJ_fullmean_math_contract_v1",
      "has_entry_point":False,"scientific_execution_performed":False,
      "old_WGS_math_imported_or_called":False,
      "new_gamma_bridge_real_interval":[str(RC),str(ROOT_HI)],
      "new_gamma_bridge_slots":{"copied":4,"new":8},
      "physical_coefficients":{
        "primitive_U_V":[15,1],"output_complete_A0":[14,1],
        "same_normalized_derivative_convention_as_WGS":True,
        "radial_beta_K_gamma_eta_requested_only_through":1,
        "eta_rr_beta_rr_or_gamma_rr_inferred":False},
      "extension":{
        "cutoff_C64_derivatives":list(range(17)),
        "original_potential_new_Cauchy_derivatives":list(range(17)),
        "B_compact_and_nonzero_tail_derivatives":list(range(17)),
        "extended_amplitude_and_IN2_IN3_jet_shape":[12,2]},
      "profile":{
        "Jost_Euler_Q_orders":list(range(6)),
        "Jost_derivative_C_orders":list(range(6)),
        "near_scaled_ODE_derivative_orders":list(range(6)),
        "full_angular_profile_orders":list(range(5)),
        "complete_output_weight_rows":["0","-5/3","-2"],
        "weight_columns":"ordinary amplitude angular derivatives 0..4",
        "near_partition_is_radial_only":True,
        "all_true_phases_each_have_the_admitted_common_inverse_derivative_bound":True},
      "same_angular_J":{
        "real_parity":"even0 to odd",
        "negative_gain_windows":["-2 -> -1","-5/3 -> -2/3"],
        "other_gain_window":"0 -> 1",
        "left_I_window":"I J: -2 -> 0",
        "full_radial_J_derivative_retained":True,
        "stable_trace_inverse_substituted":False},
      "mean":{
        "dual_e":[8,1],"dual_e_r":[6,0],"dual_ekappa":[6,0],
        "initial_z_degrees":list(range(4)),
        "N6_inverse_level_shapes":[{"degree":3+k,"angular_degree":6-k} for k in range(6)],
        "terminal_z_degrees":list(range(10)),
        "maximum_final_z_degree":9,
        "complete_decay_power":"23/6",
        "single_signed_and_reflected_bounds_separate":True,
        "mean_propagator":"whole positive Gronwall including complete feedback",
        "R0_or_mean_feedback_assumed_zero":False},
      "exact_norm_rules":{
        "I_one_quarter":"only full Fourier A0 or the actual fixed Sobolev/L2 primitive",
        "WGS_geometry_amplitude":"pointwise sup/component-sup-sum; never relabelled A0",
        "aJ_exponential":"new complete Fourier A0 Banach-algebra exponential of background",
        "N6_amplitude_primitives":"actual finite profile identity, not sup primitive norm",
        "end_point_physical_means":"two stored coordinates and the actual rank-one reflection constraint"},
      "required_predecessors":{
        "WGS_main":"32ff92c516fcc5c43f3619930d4845d294289270",
        "WGS_original_copies":"d6d13860e322d82ce354c8c0d0eb0f279ca63b3c",
        "FA2_cut_mean":"2001f4e2eeece1cda56b18b90dccab04b7f6d336",
        "local_same_J_process":"0d69c33697dc49f68df5075e335a4cde886e3c6c",
        "local_same_J_source":"e655654613cdc4fb56b7982ba220d764d4607875",
        "original_potential_actual":"9b8741b1508d7c3754d76f884d48a6af14d1194f",
        "original_genuine_actual":"5e7669f1990e1c4e9e3769afe3641ef6d84b82a3"},
      "owner_obligations":[
        "verify every immutable original byte, domain and field before a new graph",
        "save each complete returned graph before a later graph is evaluated",
        "save the complete actual prefix and failed positivity diagnostic",
        "only reuse an unchanged already computed graph after exact identity validation",
        "no old successful scientific target, ray or producer may be called",
        "do not turn a posterior subtotal into the whole waist or incoming error",
        "the source/jump, all four endpoints, finite rows and whole error are separate downstream graphs"]
    }

# ---------------------------------------------------------------------------
# Neutral complete-node publication protocol, with no filesystem or CLI.
# The owner supplies an atomic durable journal and schema decoder.
# ---------------------------------------------------------------------------
def all_saved_ball_strings(value):
    if isinstance(value,dict):
        if set(value)=={"ball"} and isinstance(value["ball"],str):
            return {value["ball"]}
        out=set()
        for v in value.values():
            out.update(all_saved_ball_strings(v))
        return out
    if isinstance(value,list):
        out=set()
        for v in value:
            out.update(all_saved_ball_strings(v))
        return out
    return set()


def evaluate_declared_node(node_name,binding,producer,decode_saved,publish_graph,prior=None):
    """Neutral atomic callback: publish_graph(name, whole_doc) returns saved JSON.

    The owner verifies binding's complete mathematical AST/input/dependency IDs.
    prior is a previously validated whole node envelope, if one exists.
    An unchanged complete node is decoded without calling producer. A preserved
    partial is blocked until a separately specified exact prefix recovery; this
    function never reruns a failed mathematical target automatically.

    Each newly printed scalar is included in a full prefix document and sent to
    publish_graph before the next printed scalar. The publisher uses atomic
    replace inside this one new node attempt and must preserve the final file
    on any later operational failure. Separate nodes have separate fixed names.
    No file, network, subprocess or scientific entry point is implemented here.
    """
    global _ACTIVE_RECORD_CAPTURE
    if _ACTIVE_RECORD_CAPTURE is not None:
        raise RuntimeError("nested or concurrent scientific graph evaluation")
    if not isinstance(node_name,str) or not node_name or not isinstance(binding,dict):
        raise ValueError("missing immutable complete-node identity")
    if prior is not None:
        if prior.get("binding")!=binding or prior.get("node_name")!=node_name:
            raise ValueError("saved node identity changed; preserve its original bytes")
        if prior.get("complete") is not True:
            raise ValueError("preserved partial node cannot be automatically recomputed")
        return decode_saved(copy.deepcopy(prior["conclusion"]))
    capture={"records":[]}
    def save_prefix(event=None, failure=None, returned=None, explicit=None):
        payload={"kind":"WEJ_complete_atomic_node_v1","node_name":node_name,
                 "binding":copy.deepcopy(binding),"complete":False,
                 "printed_record_events":copy.deepcopy(capture["records"]),
                 "conclusion":copy.deepcopy(returned),
                 "explicit_math_prefix":copy.deepcopy(explicit),
                 "failure":failure,"automatic_retry_authorized":False}
        readback=publish_graph(node_name,payload)
        if readback!=payload:
            raise ValueError("atomic prefix readback changed its complete JSON")
    capture["on_record"]=save_prefix
    _ACTIVE_RECORD_CAPTURE=capture
    try:
        ignored_work,conclusion=producer()
        if not isinstance(conclusion,dict):
            raise TypeError("a scientific graph must return its full typed document")
        issued={event["record"]["ball"] for event in capture["records"]}
        if not issued.issubset(all_saved_ball_strings(conclusion)):
            raise ValueError("complete graph omitted a printed scientific record")
    except BaseException as error:
        save_prefix(failure={"type":type(error).__name__,"message":str(error)},
                    returned=locals().get("conclusion"),
                    explicit=getattr(error,"complete_new_prefix",None))
        raise
    finally:
        _ACTIVE_RECORD_CAPTURE=None
    payload={"kind":"WEJ_complete_atomic_node_v1","node_name":node_name,
             "binding":copy.deepcopy(binding),"complete":True,
             "printed_record_event_count":len(capture["records"]),
             "all_printed_records_in_complete_conclusion":True,
             "conclusion":copy.deepcopy(conclusion),"failure":None,
             "automatic_retry_authorized":False}
    # Publication and downstream formatting are outside the scientific try:
    # their failure must not relabel or overwrite a completed math graph.
    saved=publish_graph(node_name,payload)
    if saved!=payload:
        raise ValueError("atomic complete-node readback changed the full JSON")
    return decode_saved(copy.deepcopy(saved["conclusion"]))

def decode_extension_conclusion(doc):
    return {"M":[read_up(r) for r in doc["Vext_derivatives"]],
            "B":[read_up(r) for r in doc["complete_B_derivatives"]],
            "CB":read_up(doc["constants"]["complete_cB_upper"]),
            "H1":read_up(doc["constants"]["complete_H1_upper"]),
            "L":ex(POTENTIAL_L)}

def decode_extended_patch_conclusion(doc):
    return {k:decode_saved_jet(v,k) for k,v in doc["complete_jets"].items()}

def decode_physical_patch_conclusion(doc):
    return {k:decode_saved_jet(v,k,k in ("beta","K","gamma","eta"))
            for k,v in doc["complete_A0_jets"].items()}

def decode_mean_union_conclusion(doc):
    rows=doc["new_complete_records"]
    return {"CF":read_up(rows["complete_union_mean_source_upper"]),
            "Z":read_up(rows["complete_physical_mean_upper"]),
            "Zr":read_up(rows["complete_physical_mean_radial_upper"]),
            "Gmean":read_up(rows["complete_backward_mean_propagator_upper"]),
            "retained_records":rows}
# ---------------------------------------------------------------------------
# Read-only reconstruction from an already published complete conclusion.
# No producer, exp, sqrt, positive power or new scalar record is evaluated.
# Exact constants and normalized-derivative decoding are the declared format.
# ---------------------------------------------------------------------------
def decode_bridge_conclusion(doc):
    rows=doc["new_complete_records"]
    return {"mean_lower":read_lower(rows["mean_local_lower"],"retained local mean"),
            "gamma":read_up(rows["gamma_upper"]),
            "gamma_r":read_up(rows["gamma_r_upper"]),
            "eta_r":read_up(rows["eta_r_upper"])}

def decode_same_J_conclusion(doc):
    rows=doc["new_complete_records"]
    old=doc["copied_old_records"]
    def pick(name):
        return old[name] if name in old else rows[name]
    em=rows["same_eta_positive_lower"]
    return {
        "J0":read_up(pick("same_J_L2_upper")),
        "L0":read_up(pick("same_L_L2_upper")),
        "DJ_lower":read_lower(rows["complete_selected_DJ_lower"],"retained DJ"),
        "aJ_upper":read_up(rows["aJ_and_inverse_upper"]),
        "aJ_lower":read_lower(rows["aJ_positive_lower"],"retained aJ"),
        "alpha":read_up(rows["alpha_absolute_upper"]),
        "Lr0":read_up(rows["complete_L_radial_L2_upper"]),
        "Jr0":read_up(rows["same_J_radial_L2_upper"]),
        "Jphi0":read_up(rows["same_J_left_angular_derivative_upper"]),
        "Gamma_minus2":read_up(rows["same_J_Hminus2_to_Hminus1_upper"]),
        "Gamma_minus5_3":read_up(rows["same_J_Hminus5_3_to_Hminus2_3_upper"]),
        "Gamma_zero":read_up(rows["same_J_L2_to_H1_upper"]),
        "cI":read_up(rows["physical_I_gain_upper"]),
        "eta_lower":read_lower(em,"retained same angular eta"),
        "J0_upper":copy.deepcopy(pick("same_J_L2_upper")),
        "L0_upper":copy.deepcopy(pick("same_L_L2_upper")),
        "eta_lower_record":copy.deepcopy(em)}

def decode_Jost_conclusion(doc):
    return {"E":[read_up(r) for r in doc["complete_Euler_a_0_4"]],
            "Ep":[read_up(r) for r in doc["complete_Euler_aprime_0_4"]]}

def decode_profile_geometry_conclusion(doc,whole_t_over_rho_record,T_value_upper):
    return {
        "q":decode_saved_jet(doc["complete_regular_quotient_jet"],"retained_T_over_rho"),
        "q_lower":read_lower(whole_t_over_rho_record,"retained whole T/rho"),
        "phase_lower":read_lower(doc["new_complete_records"]["complete_phase_lower"],
                                  "retained complete phase"),
        "phase_derivatives":[read_up(r) for r in doc["complete_phase_derivatives_1_4"]],
        "T_upper":up(T_value_upper)}

def decode_profile_conclusion(doc):
    weights=doc["complete_full_output_block_weights"]
    r=doc["new_complete_records"]["single_signed_point_profile_upper"]
    return {"Pstar":read_up(r),"Pstar_record":copy.deepcopy(r),
            "block_weights":{k:[read_up(v) for v in vv] for k,vv in weights.items()},
            "block_weight_records":copy.deepcopy(weights)}

def decode_mean_kernel_conclusion(doc):
    rows=doc["new_complete_records"]
    work={k:decode_saved_jet(v,k) for k,v in doc["complete_jets"].items()}
    names={"aeff":"complete_aeff_upper",
           "k0":"complete_k_L2_upper","kphi0":"complete_k_phi_L2_upper",
           "kr0":"complete_k_r_L2_upper","Rm0":"complete_Rmean_L2_upper",
           "Ik0":"complete_I_k_L2_upper","IRm0":"complete_I_Rmean_L2_upper"}
    work.update({k:read_up(rows[v]) for k,v in names.items()})
    work["retained_records"]=copy.deepcopy(rows)
    return work

def decode_mean_N6_conclusion(doc):
    rows=doc["new_complete_records"]
    return {"single_CF":read_up(rows["single_signed_mean_source_upper"]),
            "CF":read_up(rows["complete_reflected_mean_source_upper"])}

def complete_atomic_node_catalog():
    """Fixed scientific nodes; the owner supplies paths and immutable bindings."""
    nodes=[
        ("mean_gamma_bridge","full_input_mean_gamma_bridge",
         "decode_bridge_conclusion",(),12),
        ("extension_scalars","complete_extension_scalars",
         "decode_extension_conclusion",(),104),
        ("extended_amplitude_strict","complete_extended_amplitude_patch",
         "decode_extended_patch_conclusion",("extension_scalars",),64),
        ("extended_amplitude_local","complete_extended_amplitude_patch",
         "decode_extended_patch_conclusion",("extension_scalars",),64),
        ("physical_coefficients_strict","complete_physical_patch",
         "decode_physical_patch_conclusion",(),144),
        ("physical_coefficients_local","complete_physical_patch",
         "decode_physical_patch_conclusion",("mean_gamma_bridge",),144),
        ("same_angular_J_strict","complete_same_J_patch",
         "decode_same_J_conclusion",("physical_coefficients_strict",),24),
        ("same_angular_J_local","complete_same_J_patch",
         "decode_same_J_conclusion",("physical_coefficients_local",),21),
        ("Jost_scalars","complete_Jost_scalars",
         "decode_Jost_conclusion",("extension_scalars",),24),
        ("profile_geometry_strict","complete_profile_geometry",
         "decode_profile_geometry_conclusion",(),11),
        ("profile_geometry_local","complete_profile_geometry",
         "decode_profile_geometry_conclusion",(),11),
        ("profile_block_strict","complete_profile_patch",
         "decode_profile_conclusion",
         ("extension_scalars","Jost_scalars","profile_geometry_strict"),51),
        ("profile_block_local","complete_profile_patch",
         "decode_profile_conclusion",
         ("extension_scalars","Jost_scalars","profile_geometry_local"),51),
        ("mean_kernel_strict","complete_mean_kernel_patch",
         "decode_mean_kernel_conclusion",
         ("physical_coefficients_strict","same_angular_J_strict"),45),
        ("mean_kernel_local","complete_mean_kernel_patch",
         "decode_mean_kernel_conclusion",
         ("physical_coefficients_local","same_angular_J_local"),45),
        ("mean_N6_strict","complete_mean_N6_patch",
         "decode_mean_N6_conclusion",
         ("extended_amplitude_strict","mean_kernel_strict","profile_block_strict"),201),
        ("mean_N6_local","complete_mean_N6_patch",
         "decode_mean_N6_conclusion",
         ("extended_amplitude_local","mean_kernel_local","profile_block_local"),201),
        ("mean_union","complete_mean_union",
         "decode_mean_union_conclusion",
         ("mean_kernel_strict","mean_kernel_local","mean_N6_strict","mean_N6_local"),5)]
    return {
        "protocol":"publish_graph(node_name,complete_json_doc) returns canonical saved/read-back JSON",
        "node_file_basename_rule":"node_name + '.json'; one node per fixed file",
        "owner_supplies_run_directory_and_exact_binding":True,
        "node_envelope_kind":"WEJ_complete_atomic_node_v1",
        "all_downstream_arithmetic_from_saved_record_endpoints":True,
        "conclusion_is_the_complete_mathematical_payload":True,
        "complete_node_is_immutable":True,
        "partial_recovery_requires_separate_exact_prefix_plan":True,
        "nodes":[{"name":n,"producer":p,"decoder":d,"direct_new_dependencies":list(dep),
                  "saved_ball_slots":slots}
                 for n,p,d,dep,slots in nodes],
        "total_saved_ball_slots":sum(v[4] for v in nodes),
        "exact_original_copied_slots":6,
        "slot_count_is_not_a_count_of_independent_Arb_operations":True,
        "new_node_headers_are_supplied_by_the_owner_not_fabricated_here":True}
