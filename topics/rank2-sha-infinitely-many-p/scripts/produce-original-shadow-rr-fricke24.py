#!/usr/bin/env sage-python
"""R882 Appendix B: original Fricke degree24 Riemann--Roch front end.

Mathematics is executed only in this repository's public Actions.  Normalize
B+=X_0(867)/w_867 (degree24 over the original eta coordinate), compute BOTH
Fricke RR summands, and return them to the original D_S denominator.  The
returned original function field is the SAME simple degree48 k(t)[T] model
used by the eta48 coordinate and relative-divisor consumers; it is not
normalized a second time here.

This independent producer leaves the existing degree306/eta48 producers and
all characteristic-zero map certificates unchanged.  Its success certifies
only this finite-field RR front end, never either map or a nonzero shadow.
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
from sage.all import ZZ, GF, PolynomialRing, FunctionField, matrix, binomial
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


def cyclic_relation_and_eta_polynomial(prime, terms):
    """Original complete 17^2 relation, then its monic degree576 eta polynomial.

    This repeats the original resultant construction but performs NO degree576
    factorization.  All 18 backtracking walks and only those walks are removed.
    """
    k = GF(prime)
    P3 = PolynomialRing(k, names=("tt", "zz", "vv"), order="degrevlex")
    tt, zz, vv = P3.gens()
    f = base.evaluate_phi(terms, tt, zz, P3.zero())
    g = base.evaluate_phi(terms, zz, vv, P3.zero())
    progress("fricke24: complete phi289 resultant start", middle_degree=18)
    res = f.resultant(g, zz)
    assert all(e[1] == 0 for e in res.dict())
    kT = PolynomialRing(k, "T0")
    T0 = kT.gen()
    kTV = PolynomialRing(kT, "V0")
    V0 = kTV.gen()
    resultant = sum((k(c)*T0**e[0]*V0**e[2]
                     for e, c in res.dict().items()), kTV.zero())
    cyclic, remainder = resultant.quo_rem((V0-T0)**18)
    assert remainder == 0
    assert cyclic.degree() == 306 and cyclic.leading_coefficient() == 1
    cyclic_hash = digest([str(c) for c in cyclic.list()])
    progress("fricke24: exact backtracking removal complete",
             cyclic_degree=306, cyclic_coefficients_sha256=cyclic_hash)

    kt = PolynomialRing(k, "t0")
    t0 = kt.gen()
    ktX = PolynomialRing(kt, "X")
    coefficients = {}
    for j, cj in enumerate(cyclic.list()):
        for i, cij in enumerate(cj.list()):
            if cij:
                n = i+j
                coefficients[n] = (coefficients.get(n, kt.zero()) +
                                   cij*t0**(12*(306-j)))
    G = ktX([coefficients.get(i, kt.zero())
             for i in range(max(coefficients)+1)])
    removed_X_order = int(G.valuation())
    G = G >> removed_X_order
    content = kt.zero()
    for c in G.list():
        content = content.gcd(c)
    assert content
    G = ktX([c//content for c in G.list()])
    assert G.degree() == 576

    K = FunctionField(k, "t_eta")
    t_eta = K.gen()
    KX = PolynomialRing(K, "X")

    def at_eta(c):
        return sum((K(a)*t_eta**i for i, a in enumerate(c.list())), K.zero())

    R = KX([at_eta(c) for c in G.list()]).monic()
    assert R.degree() == 576
    progress("fricke24: whole eta relation complete",
             total_degree=576, removed_X_order=removed_X_order,
             coefficients_sha256=digest([str(c) for c in R.list()]))
    return k, kt, K, R, cyclic_hash


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


def make_fricke_fields(prime, terms):
    k, kt, K, R, cyclic_hash = cyclic_relation_and_eta_polynomial(prime, terms)
    t_eta = K.gen()
    a = K(729)*t_eta**12

    # R882 (B13), including the constant and the high coefficients.
    progress("fricke24: full reciprocal coefficient check")
    assert R[576] == 1 and R[0] == a**288
    for n in range(1, 289):
        assert R[288-n] == a**n*R[288+n]
    KJ = PolynomialRing(K, "J")
    Jvar = KJ.gen()
    Q = KJ(R[288])
    Cprev, Cnow = KJ(2), Jvar
    for n in range(1, 289):
        Q += R[288+n]*Cnow
        Cprev, Cnow = Cnow, Jvar*Cnow-a*Cprev
    assert Q.degree() == 288 and Q.leading_coefficient() == 1
    progress("fricke24: degree288 reciprocal polynomial complete",
             reciprocal_degree=288,
             coefficients_sha256=digest([str(c) for c in Q.list()]))

    progress("fricke24: degree288 factorization start")
    factors = Q.factor()
    summaries = []
    selected = []
    for fac, multiplicity in factors:
        assert multiplicity == 1
        cleared = clear_factor_coefficients(fac, kt)
        low = min(24*int(c.valuation())-i
                  for i, c in enumerate(cleared) if c)
        initial = sum((c[int(c.valuation())]
                       for i, c in enumerate(cleared)
                       if c and 24*int(c.valuation())-i == low), k.zero())
        summaries.append({
            "degree":int(fac.degree()), "multiplicity":int(multiplicity),
            "initial_weight":int(low), "initial_at_1_1":int(initial)})
        if initial == 0:
            selected.append(fac.monic())
    assert len(selected) == 1 and selected[0].degree() == 24
    fplus = selected[0]
    assert fplus.gcd(fplus.derivative()).degree() == 0
    assert Q % fplus == 0
    progress("fricke24: original degree24 factor selected",
             factors=summaries,
             factor_coefficients_sha256=digest([str(c) for c in fplus.list()]))

    Bplus = K.extension(fplus, "J")
    J = Bplus.gen()
    delta = J**2-Bplus(4*a)

    # Recover the original simple eta48 field without normalizing it.
    # X^24 fplus(X+a/X) is a POLYNOMIAL: 24+i-2k >= 0.
    KX = R.parent()
    X = KX.gen()
    H = KX.zero()
    for i, ci in enumerate(fplus.list()):
        for j in range(i+1):
            H += ci*binomial(i, j)*a**j*X**(24+i-2*j)
    assert H.degree() == 48 and H.leading_coefficient() == 1
    assert H.gcd(H.derivative()).degree() == 0
    assert R % H == 0
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
    progress("fricke24: exact original U recovery in simple eta48 field")
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
    progress("fricke24: original degree48 return complete",
             quotient_degree=24, original_degree=48,
             original_factor_sha256=digest([str(c) for c in H.list()]),
             U_and_denominator_ratio_sha256=hash_functions([U, at]))

    return {
        "constants":k, "rational_base":K, "quotient":Bplus,
        "J":J, "delta":delta, "quotient_polynomial":fplus,
        "field":B, "T":T, "U":U, "V":V, "w":w,
        "lift_plus":lift_plus, "denominator_ratio":at,
        "reciprocal_factor_summary":summaries,
        "cyclic_coefficients_sha256":cyclic_hash,
    }


def quotient_divisors(fields):
    """All finite and infinite data are computed on the degree24 quotient."""
    Bplus = fields["quotient"]
    K = fields["rational_base"]
    J = fields["J"]
    t = Bplus(K.gen())

    progress("fricke24: degree24 finite maximal order start")
    Ofin = Bplus.maximal_order()
    assert len(Ofin.basis()) == 24
    progress("fricke24: degree24 finite maximal order complete", integral_rank=24)
    progress("fricke24: degree24 infinite maximal order start")
    Oinf = Bplus.maximal_order_infinite()
    assert len(Oinf.basis()) == 24
    progress("fricke24: degree24 infinite maximal order complete", integral_rank=24)

    # J=T+729/V has poles at every quotient cusp and nowhere else.
    # The special two cusp pairs have pole orders 1 and 289; the other
    # sixteen geometric pairs have pole order 1.  The two summands have
    # unequal orders in each case, so no leading-coefficient cancellation.
    progress("fricke24: complete quotient cusp divisors start")
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
    progress("fricke24: full eighteen quotient cusps certified",
             geometric_cusps=18, J_pole_degree=306,
             t_divisor=divisor_record(tdiv),
             cusp_pole_divisor_sha256=digest(divisor_record(Jpoles)))

    progress("fricke24: full logarithmic and branch divisors start")
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
    progress("fricke24: full normalized divisors certified",
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


def build_frontend(prime=29, rr_powers=(1,), q_precision=None, model="fricke24"):
    assert prime in (29, 41) and model == "fricke24"
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
        progress("fricke24: invariant RR layer start",
                 divisor_multiple=m, expected_dimension=neven)
        even_basis = Deven.basis_function_space()
        assert len(even_basis) == neven
        progress("fricke24: invariant RR basis complete",
                 divisor_multiple=m, dimension=neven,
                 functions_sha256=hash_functions(even_basis))
        progress("fricke24: anti-invariant RR layer start",
                 divisor_multiple=m, expected_dimension=nodd)
        odd_basis = Dodd.basis_function_space()
        assert len(odd_basis) == nodd
        progress("fricke24: anti-invariant RR basis complete",
                 divisor_multiple=m, dimension=nodd,
                 functions_sha256=hash_functions(odd_basis))

        # R882 (B9), in this direction.  Do not invert at.
        multiplier = at**m
        converted = [multiplier*lift_plus(f) for f in even_basis]
        converted += [multiplier*w*lift_plus(f) for f in odd_basis]
        assert len(converted) == 204*m-84
        if m == 1:
            assert (neven, nodd) == (54, 66)
        progress("fricke24: both signs returned to original D_S",
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
                progress("fricke24: original Tate rows",
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
        progress("fricke24: full original RR layer certified", **summaries[-1])

    # The consumers require the SIMPLE eta48 presentation, which is precisely
    # the field returned above.  The construction method is separately named.
    # Quotient places are NOT mislabeled as places of B; unused original
    # divisor/place keys are None rather than forcing a second normalization.
    context = {
        "prime":prime, "model":"eta48", "rr_method":"fricke24",
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
        "prime":prime, "model":"fricke24", "returned_field_model":"eta48",
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
    parser.add_argument("--model", choices=("fricke24",), default="fricke24")
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
