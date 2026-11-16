#!/usr/bin/env sage-python
"""R882(C,E): original genus19 full-Atkin Riemann--Roch front end.

Public Actions only.  The COMPLETE degree24 equation over k(s) is recovered
from all 24 original Tate traces, the proved global coefficient pole bounds,
and the absolute eta branch.  Normalize only the genus19 quotient, retain
Au, Av and all four character blocks, then return to the SAME simple eta48
field and original D_S denominator.  No current run is replaced; neither
characteristic-zero map nor a nonzero shadow is asserted.  No data file.
"""
import os
if (os.environ.get("GITHUB_ACTIONS") != "true" or
        os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public"):
    raise SystemExit("Run this mathematical producer only in the public repository Actions.")

import argparse
import hashlib
import importlib.util
import json
import time
from pathlib import Path
from sage.all import ZZ, GF, PolynomialRing, FunctionField, matrix, vector, binomial, LaurentSeriesRing, PowerSeriesRing
from sage.rings.function_field.divisor import divisor
from sage.env import SAGE_VERSION

HERE = Path(__file__).resolve().parent
ETA48_PATH = HERE / "produce-original-shadow-rr-eta48.py"
_SPEC = importlib.util.spec_from_file_location("original_shadow_eta48_rr", ETA48_PATH)
base = importlib.util.module_from_spec(_SPEC)
_SPEC.loader.exec_module(base)
canonical = base.canonical
digest = base.digest
progress = base.progress
hash_functions = base.hash_functions
divisor_record = base.divisor_record
STARTED = time.monotonic()


def clear_factor_coefficients(fac, kt):
    """Primitive polynomial over k[t], retaining the absolute eta branch."""
    lden = kt.one()
    for c in fac.list():
        lden = lden.lcm(kt(c.denominator().list()))
    cleared = [kt(c.numerator().list()) *
               (lden//kt(c.denominator().list())) for c in fac.list()]
    content = kt.zero()
    for c in cleared:
        content = content.gcd(c)
    assert content
    return [c//content for c in cleared]



def truncated_product(a, b, precision):
    """Pinned Sage10.6 FLINT nmod multiplication, no integer integration."""
    return a._mul_trunc_(b, int(precision))


def truncated_power(a, exponent, precision):
    return a._power_trunc(int(exponent), int(precision))


def newton_reversion(unit_parameter, precision):
    """Inverse of u(q)=q+O(q^2) in F_r[[q]], valid beyond characteristic.

    Sage10.6 polynomial.revert_series rejects precision >= characteristic.
    Use its FLINT compose_mod and inverse_series_trunc instead: only the
    derivative's unit constant is inverted.  No division by the coefficient
    index occurs.
    """
    R = unit_parameter.parent()
    x = R.gen()
    precision = int(precision)
    assert unit_parameter[0] == 0 and unit_parameter[1] == 1
    answer = x
    known = 2
    while known < precision:
        target = min(2*known, precision)
        modulus = x**target
        f = unit_parameter.truncate(target)
        value = f.compose_mod(answer, modulus)
        derivative = f.derivative().compose_mod(answer, modulus)
        assert derivative[0] == 1
        correction = truncated_product(
            value-x, derivative.inverse_series_trunc(target), target)
        answer = (answer-correction).truncate(target)
        assert answer[0] == 0 and answer[1] == 1
        assert f.compose_mod(answer, modulus) == x
        known = target
        progress("tate19: unit Newton reversion", precision=known)
    # The right inverse is already unique in the formal-automorphism group.
    # Check the other composition too, retaining the same full precision.
    assert answer.compose_mod(unit_parameter.truncate(precision),
                              x**precision) == x
    return answer


def bounded_rational_reconstruction(coefficients, numerator_bound,
                                    denominator_bound, kt):
    """All supplied coefficients, not an unchecked short Pade approximant."""
    k = kt.base_ring()
    precision = len(coefficients)
    assert precision > numerator_bound+denominator_bound
    rows = []
    rhs = []
    for n in range(numerator_bound+1, precision):
        rows.append([coefficients[n-j] if n >= j else k.zero()
                     for j in range(1, denominator_bound+1)])
        rhs.append(-coefficients[n])
    M = matrix(k, rows)
    target = vector(k, rhs)
    solution = M.solve_right(target)
    assert M*solution == target
    denominator = kt([k.one()]+list(solution))
    assert denominator[0] == 1 and denominator.degree() <= denominator_bound
    numerator = (denominator*kt(coefficients)).truncate(precision)
    assert numerator.degree() <= numerator_bound
    common = numerator.gcd(denominator)
    numerator, denominator = numerator//common, denominator//common
    scale = denominator[0]
    assert scale != 0
    numerator, denominator = numerator/scale, denominator/scale
    numerator, denominator = kt(numerator), kt(denominator)
    assert denominator[0] == 1
    assert (denominator*kt(coefficients)-numerator).truncate(precision) == 0
    assert numerator.gcd(denominator) == 1
    return numerator, denominator



def original_tate_L_unit(prime, precision=4500):
    """L(Q(nu))=nu^-145*A(nu), nu^24=1/s=t/(1+t^2)."""
    k = GF(prime)
    R = PolynomialRing(k, "nu_local")
    nu = R.gen()
    precision = int(precision)
    assert precision >= 4500

    def euler(step):
        co = [k.zero()]*precision
        co[0] = k.one()
        n = 1
        while step*n*(3*n-1)//2 < precision:
            sign = k(-1 if n % 2 else 1)
            for e in (step*n*(3*n-1)//2, step*n*(3*n+1)//2):
                if e < precision:
                    co[e] += sign
            n += 1
        return R(co)

    e1, e3, e289, e867 = [euler(d) for d in (1, 3, 289, 867)]
    tunit = truncated_product(
        truncated_product(e1, e867, precision),
        truncated_product(e3, e289, precision).inverse_series_trunc(precision),
        precision)
    assert tunit[0] == 1
    denominator = (R.one()+
                   (truncated_product(tunit, tunit, precision) << 48)).truncate(precision)
    xunit = truncated_product(
        tunit, denominator.inverse_series_trunc(precision), precision)
    root = xunit._nth_root_series(24, precision, start=k.one())
    assert root[0] == 1
    assert truncated_power(root, 24, precision) == xunit
    nu_of_q = (root << 1).truncate(precision)
    progress("tate19: absolute unit 24th root", q_precision=precision,
             root_sha256=digest([int(a) for a in root.list()]))
    q_of_nu = newton_reversion(nu_of_q, precision)
    usable = precision-1

    ratio = truncated_product(
        e1, e3.inverse_series_trunc(precision), precision)
    Tunit_q = truncated_power(ratio, 12, precision)
    Tunit_nu = Tunit_q.truncate(usable).compose_mod(
        q_of_nu.truncate(usable), nu**usable)
    Aq = truncated_product(Tunit_nu,
                            (q_of_nu >> 1).inverse_series_trunc(usable), usable)
    assert Aq[0] == 1

    # C=t(Q(nu))/nu^24=q1^24*tau(Q(nu)) is the ACTUAL eta branch.
    # Its quadratic identity checks the chosen small t root, not a substitute.
    tau_nu = tunit.truncate(usable).compose_mod(
        q_of_nu.truncate(usable), nu**usable)
    C = truncated_product(
        truncated_power(q_of_nu >> 1, 24, usable), tau_nu, usable)
    assert C[0] == 1
    assert (C-R.one()-
            (truncated_product(C, C, usable) << 48)).truncate(usable) == 0
    C6 = truncated_power(C, 6, usable)
    A = truncated_product(Aq, C6.inverse_series_trunc(usable), usable)
    A += k(729)*(truncated_product(
        C6, Aq.inverse_series_trunc(usable), usable) << 290)
    A = A.truncate(usable)
    assert A[0] == 1
    progress("tate19: complete original L unit", q_precision=precision,
             usable_unit_precision=usable,
             nu_of_q_sha256=digest([int(a) for a in nu_of_q.list()]),
             q_of_nu_sha256=digest([int(a) for a in q_of_nu.list()]),
             small_t_unit_sha256=digest([int(a) for a in C.list()]),
             L_unit_sha256=digest([int(a) for a in A.list()]))
    return k, R, A, usable


def direct_tate_atkin_polynomial(prime, q_precision=4500,
                                 trace_precision=170):
    """R882(E): complete degree24 equation over k(s), genus19 source."""
    trace_precision = int(trace_precision)
    assert trace_precision >= 170
    assert q_precision-1 > 24*(trace_precision-1)+23
    k, Rnu, A, usable = original_tate_L_unit(prime, q_precision)
    nu = Rnu.gen()
    kx = PolynomialRing(k, "x_inv_s")
    Rx = PowerSeriesRing(k, "x_trace", default_prec=trace_precision)
    xx = Rx.gen()
    b = [(145*j)//24 for j in range(25)]
    powers = [Rnu.one()]
    scaled_traces = [Rx(24)]
    for j in range(1, 25):
        powers.append(truncated_product(powers[-1], A, usable))
        offset = 145*j-24*b[j]
        assert 0 <= offset < 24
        data = [k(24)*powers[-1][24*n+offset]
                for n in range(trace_precision)]
        Sj = Rx(data).add_bigoh(trace_precision)
        scaled_traces.append(Sj)
        progress("tate19: complete scaled trace", power=j,
                 removed_pole=b[j], local_offset=offset,
                 x_precision=trace_precision)

    Ks = FunctionField(k, "s_atkin")
    ss = Ks.gen()
    scaled_coefficients = [Rx.one()]
    rational = [Ks.one()]
    records = []
    common_denominator = kx.one()
    for m in range(1, 25):
        Rm = Rx.zero()
        for j in range(1, m+1):
            shift = b[m]-b[m-j]-b[j]
            assert shift in (0, 1)
            Rm += xx**shift*scaled_coefficients[m-j]*scaled_traces[j]
        Rm = (-Rm/k(m)).add_bigoh(trace_precision)
        assert Rm.precision_absolute() >= trace_precision
        scaled_coefficients.append(Rm)
        data = [k(Rm[n]) for n in range(trace_precision)]
        nb = b[m]+8
        numerator, denominator = bounded_rational_reconstruction(
            data, nb, 8, kx)
        common_denominator = common_denominator.lcm(denominator)
        assert common_denominator.degree() <= 8

        def at_inv_s(p):
            return sum((Ks(a)*ss**(-i) for i, a in enumerate(p.list())), Ks.zero())
        dm = ss**b[m]*at_inv_s(numerator)/at_inv_s(denominator)
        rational.append(dm)
        if m == 24:
            assert data[0] == -1
        records.append({
            "m":m, "pole_scale":b[m], "numerator_bound":nb,
            "denominator_bound":8,
            "numerator_degree":int(numerator.degree()),
            "denominator_degree":int(denominator.degree()),
            "rational_coefficient_sha256":digest(str(dm))})
        progress("tate19: unique full coefficient recovered", **records[-1])

    KL = PolynomialRing(Ks, "L_atkin")
    polynomial = KL(list(reversed(rational)))
    assert polynomial.degree() == 24 and polynomial.leading_coefficient() == 1
    assert polynomial.gcd(polynomial.derivative()).degree() == 0

    ks = PolynomialRing(k, "s0")
    cleared = clear_factor_coefficients(polynomial, ks)
    low = min(-24*j-145*i
              for i, ci in enumerate(cleared)
              for j, a in enumerate(ci.list()) if a)
    initial = sum((a for i, ci in enumerate(cleared)
                   for j, a in enumerate(ci.list())
                   if a and -24*j-145*i == low), k.zero())
    assert initial == 0
    residual = Rnu.zero()
    for i, ci in enumerate(cleared):
        shifted = Rnu({-24*j-145*i-low:a
                       for j, a in enumerate(ci.list()) if a})
        residual += truncated_product(shifted, powers[i], usable)
    assert residual.truncate(usable) == 0
    result = {
        "method":"full Atkin original Tate trace and global coefficient pole caps",
        "q_precision":q_precision, "x_trace_precision":trace_precision,
        "common_x_denominator_degree":int(common_denominator.degree()),
        "equation_Laurent_check_precision":usable,
        "initial_weight":int(low), "initial_at_1_1":int(initial),
        "coefficient_records":records, "degree":24,
        "polynomial_sha256":digest([str(c) for c in polynomial.list()])}
    progress("tate19: complete degree24 genus19 equation certified", **result)
    return k, Ks, polynomial, result

def make_atkin_fields(prime, terms):
    k, Ks, polynomial, certificate = direct_tate_atkin_polynomial(prime)
    D = Ks.extension(polynomial, "L_atkin")
    Latkin = D.gen()
    satkin = D(Ks.gen())

    # Exact E11; the original eta48 variable is retained for all consumers.
    K = FunctionField(k, "t_eta")
    t = K.gen()
    phi_s = Ks.hom([t+1/t])
    KJ = PolynomialRing(K, "J")
    p_t = KJ([t**(6*(24-i))*phi_s(ci)
               for i, ci in enumerate(polynomial.list())])
    assert p_t.degree() == 24 and p_t.leading_coefficient() == 1
    assert p_t.gcd(p_t.derivative()).degree() == 0
    a = K(729)*t**12
    KX = PolynomialRing(K, "X")
    X = KX.gen()
    H = KX.zero()
    for i, ci in enumerate(p_t.list()):
        for j in range(i+1):
            H += ci*binomial(i, j)*a**j*X**(24+i-2*j)
    assert H.degree() == 48 and H.leading_coefficient() == 1
    assert H.gcd(H.derivative()).degree() == 0
    B = K.extension(H, "T")
    T = B.gen()
    tt = B(t)
    V = T/tt**12
    Jimage = T+B(a)/T
    Limage = Jimage/tt**6
    simage = tt+1/tt
    uimage = tt-1/tt
    vimage = (T-B(a)/T)/tt**6
    assert p_t(Jimage) == 0
    assert uimage**2 == simage**2-4
    assert vimage**2 == Limage**2-2916
    lift_D = D.hom([Limage, simage])
    assert lift_D(Latkin) == Limage and lift_D(satkin) == simage

    BZ = PolynomialRing(B, "Z")
    Z = BZ.gen()
    progress("tate19: actual eta48 U recovery", source_degree=48)
    ugcd = base.evaluate_phi(terms, T, Z, BZ.zero()).gcd(
           base.evaluate_phi(terms, Z, V, BZ.zero())).monic()
    assert ugcd.degree() == 1
    U = -ugcd[0]
    assert base.evaluate_phi(terms, T, U, B.zero()) == 0
    assert base.evaluate_phi(terms, U, V, B.zero()) == 0
    assert U != T and U != V

    # These are the original absolute Atkin involutions, not newly chosen roots.
    W = B.hom([B(a)/T, tt])
    W3 = B.hom([B(729)/T, 1/tt])
    assert W(T) == B(729)/V and W(V) == B(729)/T
    assert W(U) == B(729)/U
    assert W3(T) == B(729)/T and W3(V) == B(729)/V
    assert W3(U) == B(729)/U
    for f in (T, tt):
        assert W(W(f)) == f and W3(W3(f)) == f
        assert W(W3(f)) == W3(W(f))
    assert W(Limage) == Limage and W3(Limage) == Limage
    assert W(uimage) == uimage and W3(uimage) == -uimage
    assert W(vimage) == -vimage and W3(vimage) == -vimage

    dTdt = T.derivative()
    assert dTdt != 0
    at = -T/(B(24)*tt*dTdt)
    progress("tate19: original degree48 field and both signs restored",
             quotient_genus=19, quotient_degree=24,
             original_field_degree=48,
             eta48_polynomial_sha256=digest([str(c) for c in H.list()]),
             complete_coordinates_sha256=hash_functions([U, uimage, vimage, at]))
    return {
        "constants":k, "rational_base":K, "quotient_base":Ks,
        "quotient":D, "quotient_polynomial":polynomial,
        "L_atkin":Latkin, "s_atkin":satkin,
        "field":B, "T":T, "U":U, "V":V,
        "u_atkin":uimage, "v_atkin":vimage, "lift_quotient":lift_D,
        "denominator_ratio":at, "direct_tate_certificate":certificate,
        "W":W, "W3":W3,
    }


def quotient_divisors(fields):
    """Only the true genus19 degree24 quotient is globally normalized."""
    D = fields["quotient"]
    s = fields["s_atkin"]
    L = fields["L_atkin"]
    progress("tate19: finite maximal order start", degree=24)
    O = D.maximal_order()
    assert len(O.basis()) == 24
    progress("tate19: finite maximal order complete", degree=24)
    Oinf = D.maximal_order_infinite()
    assert len(Oinf.basis()) == 24
    progress("tate19: infinite maximal order complete", degree=24)

    poles_L = L.divisor_of_poles()
    cusps = tuple(poles_L.support())
    assert poles_L.degree() == 153
    assert sum(int(Q.degree()) for Q in cusps) == 9
    distinguished = [(Q, int(n)) for Q, n in poles_L.list() if n != 1]
    assert len(distinguished) == 1
    pinf, order_L = distinguished[0]
    assert pinf.degree() == 1 and order_L == 145
    poles_s = s.divisor_of_poles()
    assert poles_s.degree() == 24
    assert poles_s.list() == [(pinf, 24)]
    CD = divisor(D, {Q:1 for Q in cusps})

    du = (s**2-4).divisor()
    assert all(int(n) % 2 == 0 for Q, n in du.list())
    Au = divisor(D, {Q:int(n)//2 for Q, n in du.list() if n})
    assert du == 2*Au and Au.degree() == 0
    dv = (L**2-2916).divisor()
    Av = divisor(D, {Q:int(n)//2 for Q, n in dv.list() if int(n)//2})
    branch = divisor(D, {Q:1 for Q, n in dv.list() if int(n) % 2})
    assert dv == 2*Av+branch
    assert branch.is_effective() and branch.degree() == 12
    assert Av.degree() == -6
    assert set(branch.support()).isdisjoint(set(cusps))
    canonical_divisor = s.differential().divisor()
    assert canonical_divisor.degree() == 36
    D0 = canonical_divisor-Au+CD
    assert D0.is_effective() and D0.degree() == 45
    assert D0.multiplicity(pinf) == 0
    assert canonical_divisor.multiplicity(pinf) == -25
    assert Au.multiplicity(pinf) == -24
    progress("tate19: all nine cusps and all four-block divisors certified",
             quotient_genus=19, geometric_cusps=9,
             original_cusp_L_pole=145, original_cusp_s_pole=24,
             Au_degree=0, Av_degree=-6, branch_degree=12, D0_degree=45,
             Au_sha256=digest(divisor_record(Au)),
             Av_sha256=digest(divisor_record(Av)),
             branch_sha256=digest(divisor_record(branch)),
             D0_sha256=digest(divisor_record(D0)),
             complete_cusp_poles_sha256=digest(divisor_record(poles_L)))
    return {
        "cusps":cusps, "cusp_divisor":CD, "original_cusp":pinf,
        "Au":Au, "Av":Av, "branch":branch, "D0":D0,
        "u_square_divisor":du, "v_square_divisor":dv,
        "s_poles":poles_s, "L_poles":poles_L,
    }


def build_frontend(prime=29, rr_powers=(1,), q_precision=None, model="tate19"):
    assert prime in (29, 41) and model == "tate19"
    powers = tuple(sorted(set(int(m) for m in rr_powers)))
    assert powers and powers[0] >= 1
    q_precision = (max(205, 204*max(powers)+1)
                   if q_precision is None else int(q_precision))
    assert q_precision >= 204*max(powers)+1

    terms, phi_hash = base.hecke17_level3()
    fields = make_atkin_fields(prime, terms)
    qdiv = quotient_divisors(fields)
    k, B = fields["constants"], fields["field"]
    at = fields["denominator_ratio"]
    uu, vv = fields["u_atkin"], fields["v_atkin"]
    lift_D = fields["lift_quotient"]
    tt = B(fields["rational_base"].gen())
    evaluator = base.Eta48TateEvaluator(k)
    at_jet, _ = evaluator.expansion(at, 2)
    assert at_jet[0] == 1
    u_jet, _ = evaluator.expansion(uu*tt, 2)
    assert u_jet[0] == -1
    v_jet, _ = evaluator.expansion(vv*tt**6/fields["T"], 2)
    assert v_jet[0] == 1

    bases, jets, summaries = {}, {}, []
    for m in powers:
        base_even = m*qdiv["D0"]+(m//2)*qdiv["branch"]
        base_odd = m*qdiv["D0"]+qdiv["Av"]+((m+1)//2)*qdiv["branch"]
        d0 = 45*m+12*(m//2)
        d1 = 45*m-6+12*((m+1)//2)
        specifications = [
            ("1", base_even, B.one(), d0-18),
            ("u", base_even+qdiv["Au"], uu, d0-18),
            ("v", base_odd, vv, d1-18),
            ("uv", base_odd+qdiv["Au"], uu*vv, d1-18),
        ]
        assert 2*(d0-18)+2*(d1-18) == 204*m-84
        if m == 1:
            assert [sp[3] for sp in specifications] == [27, 27, 33, 33]
        converted, blocks = [], []
        multiplier = at**m
        for label, divisor_input, sign_function, expected in specifications:
            assert divisor_input.degree() == expected+18
            assert divisor_input.degree() > 36
            progress("tate19: actual RR character block start",
                     divisor_multiple=m, character=label, expected_dimension=expected)
            basis = divisor_input.basis_function_space()
            assert len(basis) == expected
            lifted = [multiplier*sign_function*lift_D(f) for f in basis]
            converted.extend(lifted)
            blocks.append({
                "character":label, "dimension":len(basis),
                "divisor_sha256":digest(divisor_record(divisor_input)),
                "quotient_basis_sha256":hash_functions(basis),
                "original_basis_sha256":hash_functions(lifted)})
            progress("tate19: full RR block returned to original D_S",
                     divisor_multiple=m, **blocks[-1])
        assert len(converted) == 204*m-84
        bounds = [evaluator.term_lower_bound(a, i)
                  for f in converted for i, a in enumerate(f.list()) if a]
        evaluator.prepare(max(1, q_precision-min(bounds, default=0)))
        rows, lowest = [], 0
        for i, f in enumerate(converted):
            row, low = evaluator.expansion(f, q_precision)
            rows.append(row)
            lowest = min(lowest, low)
            if i % 8 == 7 or i+1 == len(converted):
                progress("tate19: original complete Tate rows",
                         divisor_multiple=m, completed=i+1,
                         total=len(converted), lowest_raw_valuation=lowest)
        M = matrix(k, rows)
        rank = M[:, :204*m+1].rank()
        assert rank == len(converted)
        bases[m], jets[m] = converted, M
        summaries.append({
            "divisor_multiple":m, "weight":2*m,
            "character_blocks":blocks, "dimension":len(converted),
            "jet_precision":q_precision, "sturm_rank":int(rank),
            "basis_sha256":hash_functions(converted),
            "jets_sha256":digest([[int(a) for a in row] for row in rows]),
            "lowest_raw_laurent_valuation":lowest})
        progress("tate19: all four original RR blocks certified", **summaries[-1])

    context = {
        "prime":prime, "model":"eta48", "rr_method":"tate19",
        "constants":k, "rational_base":fields["rational_base"], "field":B,
        "T":fields["T"], "U":fields["U"], "V":fields["V"],
        "cusps":None, "original_cusp":None, "weight_two_divisor":None,
        "original_cusp_specification":{
            "ord_t":24, "ord_T":-1, "ord_U":-17, "ord_V":-289,
            "leading_t":1, "leading_T":1,
            "leading_atkin_u":-1, "leading_atkin_v":1},
        "rr_bases":bases, "rr_jets":jets, "tate_evaluator":evaluator,
        "phi17_terms":terms, "denominator_ratio":at,
        "full_atkin_quotient":fields["quotient"],
        "full_atkin_divisors":qdiv, "full_atkin_lift":lift_D,
        "full_atkin_u":uu, "full_atkin_v":vv,
    }
    result = {
        "kind":"rank2_original_good_prime_rr_front",
        "status":"exact_frontend_only",
        "prime":prime, "model":"tate19", "returned_field_model":"eta48",
        "level":867, "normalized_function_field_degree":24,
        "function_field_degree":48, "original_T_degree":306,
        "quotient_genus":19, "genus":85,
        "quotient_geometric_cusps":9, "geometric_cusps":36,
        "quadratic_branch_degree_on_full_quotient":12,
        "quotient_D0_degree":45, "weight_two_divisor_degree":204,
        "denominator_conversion":"a_t^m, a_t=-T/(24*t*dT_dt)",
        "phi17_integer_terms_sha256":phi_hash,
        "direct_tate_certificate":fields["direct_tate_certificate"],
        "high_degree_resultant_computed":False, "rr_layers":summaries,
        "scope":(
            "The SAME original D_S RR spaces and original Tate jets, through "
            "all four full-Atkin blocks. No characteristic-zero map or "
            "nonzero Frobenius shadow is asserted."),
        "source":os.environ.get("RANK2_SOURCE_SHA"),
        "run_id":os.environ.get("RANK2_RUN_ID", os.environ.get("GITHUB_RUN_ID")),
        "sage_version":SAGE_VERSION,
        "script_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "dependency_sha256":{
            ETA48_PATH.name:hashlib.sha256(ETA48_PATH.read_bytes()).hexdigest()},
        "elapsed_seconds":time.monotonic()-STARTED,
        "readme_blobs":{
            "README.md":os.environ.get("RANK2_ROOT_README_SHA"),
            "topic":os.environ.get("RANK2_TOPIC_README_SHA")},
    }
    return context, result


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--prime", type=int, choices=(29, 41), default=29)
    parser.add_argument("--model", choices=("tate19",), default="tate19")
    parser.add_argument("--rr-powers", default="1")
    parser.add_argument("--q-precision", type=int, default=None)
    args = parser.parse_args()
    powers = tuple(int(a) for a in args.rr_powers.split(","))
    context, result = build_frontend(
        args.prime, powers, args.q_precision, args.model)
    globals()["ORIGINAL_SHADOW_RR_CONTEXT"] = context
    payload = canonical(result)
    print("RANK2_SHADOW_RR_RESULT " + payload, flush=True)
    print("RANK2_SHADOW_RR_SHA256 " +
          hashlib.sha256(payload.encode()).hexdigest(), flush=True)


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        failed = base.CURRENT_STAGE
        progress("failed", failed_stage=failed,
                 exception_type=type(exc).__name__, message=str(exc))
        raise
