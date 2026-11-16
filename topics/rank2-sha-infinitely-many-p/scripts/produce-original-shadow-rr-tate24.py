#!/usr/bin/env sage-python
"""R882 Appendices B,D: direct Tate degree24 Riemann--Roch front end.

Public Actions only.  The COMPLETE original degree24 equation is recovered
from all 24 local Tate traces and the global pole bounds.  The source eta
coordinate, reciprocal J, both Fricke RR summands and the original D_S
denominator are retained.  This independent producer does not change a
running producer or assert either characteristic-zero map or a shadow.
No recomputable data file is written.
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
from sage.all import ZZ, GF, PolynomialRing, FunctionField, matrix, vector, binomial, LaurentSeriesRing
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
        progress("tate24: unit Newton reversion", precision=known)
    # The right inverse is already unique in the formal-automorphism group.
    # Check the other composition too, retaining the same full precision.
    assert answer.compose_mod(unit_parameter.truncate(precision),
                              x**precision) == x
    return answer


def original_tate_J_unit(prime, precision=8000):
    """J(q(u))=u^-1*junit(u), u^24=t(q), with every leading root fixed."""
    k = GF(prime)
    R = PolynomialRing(k, "u_local")
    u = R.gen()
    precision = int(precision)
    assert precision >= 8000
    # Euler's pentagonal formula is integral in every characteristic.
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
    den = truncated_product(e3, e289, precision)
    tunit = truncated_product(truncated_product(e1, e867, precision),
                             den.inverse_series_trunc(precision), precision)
    assert tunit[0] == 1
    # Official polynomial_element.pyx _nth_root_series is unit Newton.
    # n=24 is invertible for BOTH specified primes; start=1 fixes the eta root.
    root = tunit._nth_root_series(24, precision, start=k.one())
    assert root[0] == 1
    assert truncated_power(root, 24, precision) == tunit
    u_of_q = (root << 1).truncate(precision)
    progress("tate24: absolute 24th root complete", precision=precision,
             root_sha256=digest([int(a) for a in root.list()]))
    q_of_u = newton_reversion(u_of_q, precision)

    ratio = truncated_product(e1, e3.inverse_series_trunc(precision), precision)
    Tunit_q = truncated_power(ratio, 12, precision)
    usable = precision-1
    Tunit_u = Tunit_q.truncate(usable).compose_mod(
        q_of_u.truncate(usable), u**usable)
    q_unit = q_of_u >> 1
    A = truncated_product(Tunit_u,
                          q_unit.inverse_series_trunc(usable), usable)
    assert A[0] == 1
    # J=T+729*t^12/T and t=u^24; multiplying J by u gives
    # A+729*u^290/A.  This exponent and the sign are absolute.
    junit = (A+k(729)*(A.inverse_series_trunc(usable) << 290)).truncate(usable)
    assert junit[0] == 1
    progress("tate24: original reciprocal trace input complete",
             q_precision=precision, usable_J_unit_precision=usable,
             u_of_q_sha256=digest([int(a) for a in u_of_q.list()]),
             q_of_u_sha256=digest([int(a) for a in q_of_u.list()]),
             J_unit_sha256=digest([int(a) for a in junit.list()]))
    return k, R, junit, usable


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


def direct_tate_quotient_polynomial(prime, q_precision=8000,
                                    trace_precision=330):
    """R882(D): the complete monic degree24 polynomial of the original J."""
    trace_precision = int(trace_precision)
    assert trace_precision >= 330
    assert q_precision-1 > 24*(trace_precision-1)+24
    k, Ru, junit, usable = original_tate_J_unit(prime, q_precision)
    u = Ru.gen()
    kt = PolynomialRing(k, "t0")
    K = FunctionField(k, "t_eta")
    t_eta = K.gen()
    Lt = LaurentSeriesRing(k, "t_trace", default_prec=trace_precision)
    t_trace = Lt.gen()
    traces = [Lt(24)]
    powers = [Ru.one()]
    for j in range(1, 25):
        powers.append(truncated_product(powers[-1], junit, usable))
        coefficients = [k(24)*powers[-1][24*n+j]
                        for n in range(trace_precision)]
        trace = Lt(coefficients).add_bigoh(trace_precision)
        if j == 24:
            trace += k(24)/t_trace
        assert trace.precision_absolute() >= trace_precision
        assert trace.valuation() >= (-1 if j == 24 else 0)
        traces.append(trace)
        progress("tate24: complete local trace", power=j,
                 negative_terms=(1 if j == 24 else 0),
                 t_precision=trace_precision)

    # c_m=(-1)^m e_m: m*c_m + sum_{j=1}^m S_j*c_(m-j)=0.
    coefficients = [Lt.one()]
    rational = [K.one()]
    records = []
    common_finite_denominator = kt.one()
    for m in range(1, 25):
        cm = -sum((traces[j]*coefficients[m-j] for j in range(1, m+1)),
                  Lt.zero())/k(m)
        assert cm.precision_absolute() >= trace_precision
        assert cm.valuation() >= (-1 if m == 24 else 0)
        coefficients.append(cm)
        regular = cm*(t_trace if m == 24 else 1)
        data = [k(regular[n]) for n in range(trace_precision)]
        nb = 16+(289*m)//24+(1 if m == 24 else 0)
        numerator, denominator = bounded_rational_reconstruction(
            data, nb, 16, kt)
        common_finite_denominator = common_finite_denominator.lcm(denominator)
        assert common_finite_denominator.degree() <= 16

        def at_t(p):
            return sum((K(a)*t_eta**i for i, a in enumerate(p.list())), K.zero())
        rat = at_t(numerator)/at_t(denominator)
        if m == 24:
            assert data[0] == -1
            rat /= t_eta
        rational.append(rat)
        records.append({
            "m":m, "numerator_bound":nb, "denominator_bound":16,
            "numerator_degree":int(numerator.degree()),
            "denominator_degree":int(denominator.degree()),
            "removed_t_pole":bool(m == 24),
            "rational_coefficient_sha256":digest(str(rat))})
        progress("tate24: globally unique coefficient recovered", **records[-1])

    KJ = PolynomialRing(K, "J")
    fplus = KJ(list(reversed(rational)))
    assert fplus.degree() == 24 and fplus.leading_coefficient() == 1
    assert fplus.gcd(fplus.derivative()).degree() == 0
    cleared = clear_factor_coefficients(fplus, kt)
    low = min(24*int(c.valuation())-i
              for i, c in enumerate(cleared) if c)
    initial = sum((c[int(c.valuation())]
                   for i, c in enumerate(cleared)
                   if c and 24*int(c.valuation())-i == low), k.zero())
    assert initial == 0

    # A full finite Laurent check, independent of simply trusting the linear
    # solve.  Multiply the cleared equation by u^24; every exponent is >=0.
    check_precision = usable-24
    residual = Ru.zero()
    for i, ci in enumerate(cleared):
        inflated = Ru({24*j:a for j, a in enumerate(ci.list()) if a})
        term = truncated_product(inflated, powers[i], check_precision)
        residual += (term << (24-i)).truncate(check_precision)
    assert residual.truncate(check_precision) == 0
    result = {
        "method":"complete original Tate trace and global pole bounds",
        "q_precision":q_precision, "t_trace_precision":trace_precision,
        "finite_common_denominator_degree":int(common_finite_denominator.degree()),
        "equation_Laurent_check_precision":check_precision,
        "coefficient_records":records,
        "quotient_polynomial_sha256":digest([str(c) for c in fplus.list()]),
        "initial_weight":int(low), "initial_at_1_1":int(initial),
        "degree":24,
    }
    progress("tate24: complete degree24 equation certified", **result)
    return k, kt, K, fplus, result

def make_fricke_fields(prime, terms):
    k, kt, K, fplus, certificate = direct_tate_quotient_polynomial(prime)
    t_eta = K.gen()
    a = K(729)*t_eta**12
    summaries = [{
        "degree":24, "multiplicity":1,
        "initial_weight":certificate["initial_weight"],
        "initial_at_1_1":certificate["initial_at_1_1"],
        "construction":"globally unique direct Tate coefficient reconstruction"}]
    Bplus = K.extension(fplus, "J")
    J = Bplus.gen()
    delta = J**2-Bplus(4*a)

    # Recover the original simple eta48 field without normalizing it.
    # X^24 fplus(X+a/X) is a POLYNOMIAL: 24+i-2k >= 0.
    KX = PolynomialRing(K, "X")
    X = KX.gen()
    H = KX.zero()
    for i, ci in enumerate(fplus.list()):
        for j in range(i+1):
            H += ci*binomial(i, j)*a**j*X**(24+i-2*j)
    assert H.degree() == 48 and H.leading_coefficient() == 1
    assert H.gcd(H.derivative()).degree() == 0
    B = K.extension(H, "T")
    T = B.gen()
    Tb = B(t_eta)
    Jimage = T+B(a)/T
    w = T-B(a)/T
    assert fplus(Jimage) == 0
    assert w**2 == Jimage**2-B(4*a)

    def lift_plus(f):
        out = B.zero()
        for ci in reversed(Bplus(f).list()):
            out = out*Jimage+B(ci)
        return out

    assert lift_plus(delta) == w**2
    V = T/Tb**12
    BZ = PolynomialRing(B, "Z")
    Z = BZ.gen()
    progress("tate24: exact original U recovery in simple eta48 field")
    ugcd = base.evaluate_phi(terms, T, Z, BZ.zero()).gcd(
           base.evaluate_phi(terms, Z, V, BZ.zero())).monic()
    assert ugcd.degree() == 1
    U = -ugcd[0]
    assert base.evaluate_phi(terms, T, U, B.zero()) == 0
    assert base.evaluate_phi(terms, U, V, B.zero()) == 0
    assert U != T and U != V

    def fricke_image(f):
        out = B.zero()
        TW = B(a)/T
        for ci in reversed(B(f).list()):
            out = out*TW+B(ci)
        return out

    assert H(B(a)/T) == 0
    assert fricke_image(T) == B(729)/V
    assert fricke_image(V) == B(729)/T
    assert fricke_image(U) == B(729)/U
    assert fricke_image(w) == -w

    # This derivative is with respect to the actual rational generator t_eta.
    # No new normalization of B or implicit switch of a modular coordinate.
    dTdt = T.derivative()
    assert dTdt != 0
    at = -T/(B(24)*Tb*dTdt)
    progress("tate24: original degree48 return complete",
             quotient_degree=24, original_degree=48,
             original_factor_sha256=digest([str(c) for c in H.list()]),
             U_and_denominator_ratio_sha256=hash_functions([U, at]))

    return {
        "constants":k, "rational_base":K, "quotient":Bplus,
        "J":J, "delta":delta, "quotient_polynomial":fplus,
        "field":B, "T":T, "U":U, "V":V, "w":w,
        "lift_plus":lift_plus, "denominator_ratio":at,
        "reciprocal_factor_summary":summaries,
        "cyclic_coefficients_sha256":None,
        "direct_tate_certificate":certificate,
    }

def quotient_divisors(fields):
    """All finite and infinite data are computed on the degree24 quotient."""
    Bplus = fields["quotient"]
    K = fields["rational_base"]
    J = fields["J"]
    t = Bplus(K.gen())

    progress("tate24: degree24 finite maximal order start")
    Ofin = Bplus.maximal_order()
    assert len(Ofin.basis()) == 24
    progress("tate24: degree24 finite maximal order complete", integral_rank=24)
    progress("tate24: degree24 infinite maximal order start")
    Oinf = Bplus.maximal_order_infinite()
    assert len(Oinf.basis()) == 24
    progress("tate24: degree24 infinite maximal order complete", integral_rank=24)

    # J=T+729/V has poles at every quotient cusp and nowhere else.
    # The special two cusp pairs have pole orders 1 and 289; the other
    # sixteen geometric pairs have pole order 1.  The two summands have
    # unequal orders in each case, so no leading-coefficient cancellation.
    progress("tate24: complete quotient cusp divisors start")
    Jpoles = J.divisor_of_poles()
    cusps = tuple(Jpoles.support())
    assert Jpoles.degree() == 306
    assert sum(int(p.degree()) for p in cusps) == 18
    Cplus = divisor(Bplus, {p:1 for p in cusps})
    tdiv = t.divisor()
    zeros = [(p, int(n)) for p, n in tdiv.list() if n > 0]
    poles = [(p, int(n)) for p, n in tdiv.list() if n < 0]
    assert len(zeros) == len(poles) == 1
    pinf, nz = zeros[0]
    pother, npole = poles[0]
    assert pinf.degree() == pother.degree() == 1
    assert nz == 24 and npole == -24
    assert Jpoles.multiplicity(pinf) == 1
    assert Jpoles.multiplicity(pother) == 289
    assert {p for p, n in tdiv.list()}.issubset(set(cusps))
    progress("tate24: full eighteen quotient cusps certified",
             geometric_cusps=18, J_pole_degree=306,
             t_divisor=divisor_record(tdiv),
             cusp_pole_divisor_sha256=digest(divisor_record(Jpoles)))

    progress("tate24: full logarithmic and branch divisors start")
    dlogt = t.differential()/t
    canonical_divisor = dlogt.divisor()
    assert canonical_divisor.degree() == 72
    Dplus = canonical_divisor+Cplus
    assert Dplus.is_effective() and Dplus.degree() == 90
    assert Dplus.multiplicity(pinf) == 0
    delta_divisor = fields["delta"].divisor()
    Adata, branchdata = {}, {}
    for p, n0 in delta_divisor.list():
        n = int(n0)
        # Python integer floor is deliberate: poles are included.
        if n//2:
            Adata[p] = n//2
        if n % 2:
            branchdata[p] = 1
    A = divisor(Bplus, Adata)
    branch = divisor(Bplus, branchdata)
    assert delta_divisor == 2*A+branch
    assert branch.is_effective() and branch.degree() == 24
    assert A.degree() == -12
    assert set(branch.support()).isdisjoint(set(cusps))
    progress("tate24: full normalized divisors certified",
             quotient_genus_from_canonical=37,
             Dplus_degree=90, branch_degree=24, A_degree=-12,
             logarithmic_divisor_sha256=digest(divisor_record(Dplus)),
             branch_divisor_sha256=digest(divisor_record(branch)),
             half_discriminant_divisor_sha256=digest(divisor_record(A)))

    return {
        "cusps":cusps, "cusp_divisor":Cplus, "original_cusp":pinf,
        "Dplus":Dplus, "A":A, "branch":branch,
        "delta_divisor":delta_divisor, "t_divisor":tdiv,
    }


def build_frontend(prime=29, rr_powers=(1,), q_precision=None, model="tate24"):
    assert prime in (29, 41) and model == "tate24"
    powers = tuple(sorted(set(int(m) for m in rr_powers)))
    assert powers and powers[0] >= 1
    q_precision = (max(205, 204*max(powers)+1)
                   if q_precision is None else int(q_precision))
    assert q_precision >= 204*max(powers)+1

    terms, phi_hash = base.hecke17_level3()
    fields = make_fricke_fields(prime, terms)
    qdiv = quotient_divisors(fields)
    k = fields["constants"]
    B = fields["field"]
    at = fields["denominator_ratio"]
    w = fields["w"]
    lift_plus = fields["lift_plus"]

    evaluator = base.Eta48TateEvaluator(k)
    # This checks the original positive w branch and the absolute multiplier:
    # Q*w and a_t both have constant term 1, using the original exact eta.
    at_jet, _ = evaluator.expansion(at, 2)
    assert at_jet[0] == 1
    # w/T is regular, with constant 1 (the other square root gives -1).
    wT_jet, _ = evaluator.expansion(w/fields["T"], 2)
    assert wT_jet[0] == 1

    bases, jets, summaries = {}, {}, []
    for m in powers:
        Deven = m*qdiv["Dplus"]+(m//2)*qdiv["branch"]
        Dodd = m*qdiv["Dplus"]+qdiv["A"]+((m+1)//2)*qdiv["branch"]
        neven = 90*m+24*(m//2)-36
        nodd = 90*m-12+24*((m+1)//2)-36
        assert Deven.degree() == neven+36
        assert Dodd.degree() == nodd+36
        assert neven+nodd == 204*m-84
        assert Deven.degree() > 72 and Dodd.degree() > 72
        progress("tate24: invariant RR layer start",
                 divisor_multiple=m, expected_dimension=neven)
        even_basis = Deven.basis_function_space()
        assert len(even_basis) == neven
        progress("tate24: invariant RR basis complete",
                 divisor_multiple=m, dimension=neven,
                 functions_sha256=hash_functions(even_basis))
        progress("tate24: anti-invariant RR layer start",
                 divisor_multiple=m, expected_dimension=nodd)
        odd_basis = Dodd.basis_function_space()
        assert len(odd_basis) == nodd
        progress("tate24: anti-invariant RR basis complete",
                 divisor_multiple=m, dimension=nodd,
                 functions_sha256=hash_functions(odd_basis))

        # R882 (B9), in this direction.  Do not invert at.
        multiplier = at**m
        converted = [multiplier*lift_plus(f) for f in even_basis]
        converted += [multiplier*w*lift_plus(f) for f in odd_basis]
        assert len(converted) == 204*m-84
        if m == 1:
            assert (neven, nodd) == (54, 66)
        progress("tate24: both signs returned to original D_S",
                 divisor_multiple=m, invariant_dimension=neven,
                 anti_invariant_dimension=nodd, total_dimension=len(converted),
                 original_functions_sha256=hash_functions(converted))

        raw_bounds = [
            evaluator.term_lower_bound(a, i)
            for f in converted for i, a in enumerate(f.list()) if a]
        evaluator.prepare(max(1, q_precision-min(raw_bounds, default=0)))
        rows, lowest_raw = [], 0
        for i, f in enumerate(converted):
            row, low = evaluator.expansion(f, q_precision)
            rows.append(row)
            lowest_raw = min(lowest_raw, low)
            if i % 8 == 7 or i+1 == len(converted):
                progress("tate24: original Tate rows",
                         divisor_multiple=m, completed=i+1, total=len(converted),
                         lowest_raw_valuation=lowest_raw)
        M = matrix(k, rows)
        rank = M[:, :204*m+1].rank()
        assert rank == len(converted)
        bases[m], jets[m] = converted, M
        summaries.append({
            "divisor_multiple":m, "weight":2*m,
            "invariant_dimension":neven, "anti_invariant_dimension":nodd,
            "dimension":len(converted), "jet_precision":q_precision,
            "sturm_rank":int(rank), "basis_sha256":hash_functions(converted),
            "jets_sha256":digest([[int(a) for a in row] for row in rows]),
            "lowest_raw_laurent_valuation":lowest_raw})
        progress("tate24: full original RR layer certified", **summaries[-1])

    # The consumers require the SIMPLE eta48 presentation, which is precisely
    # the field returned above.  The construction method is separately named.
    # Quotient places are NOT mislabeled as places of B; unused original
    # divisor/place keys are None rather than forcing a second normalization.
    context = {
        "prime":prime, "model":"eta48", "rr_method":"tate24",
        "constants":k, "rational_base":fields["rational_base"], "field":B,
        "T":fields["T"], "U":fields["U"], "V":fields["V"],
        "cusps":None, "original_cusp":None, "weight_two_divisor":None,
        "original_cusp_specification":{
            "ord_t":24, "ord_T":-1, "ord_U":-17, "ord_V":-289,
            "leading_t":1, "leading_T":1, "leading_w":1},
        "rr_bases":bases, "rr_jets":jets, "tate_evaluator":evaluator,
        "phi17_terms":terms, "denominator_ratio":at,
        "fricke_quotient":fields["quotient"], "fricke_J":fields["J"],
        "fricke_w":w, "fricke_quotient_divisors":qdiv,
        "fricke_lift":lift_plus,
    }
    result = {
        "kind":"rank2_original_good_prime_rr_front",
        "status":"exact_frontend_only",
        "prime":prime, "model":"tate24", "returned_field_model":"eta48",
        "level":867, "normalized_function_field_degree":24,
        "function_field_degree":48, "original_T_degree":306,
        "quotient_genus":37, "genus":85,
        "quotient_geometric_cusps":18, "geometric_cusps":36,
        "quadratic_branch_degree":24,
        "quotient_logarithmic_divisor_degree":90,
        "weight_two_divisor_degree":204,
        "denominator_conversion":"a_t^m, a_t=-T/(24*t*dT_dt)",
        "phi17_integer_terms_sha256":phi_hash,
        "cyclic_coefficients_sha256":fields["cyclic_coefficients_sha256"],
        "reciprocal_factor_summary":fields["reciprocal_factor_summary"],
        "direct_tate_certificate":fields["direct_tate_certificate"],
        "high_degree_resultant_computed":False,
        "rr_layers":summaries,
        "scope":(
            "The complete original D_S RR spaces and exact Tate jets are "
            "constructed through both Fricke summands. Neither original "
            "characteristic-zero map nor a nonzero shadow is asserted."),
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
    parser.add_argument("--model", choices=("tate24",), default="tate24")
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
