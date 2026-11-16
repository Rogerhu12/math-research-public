#!/usr/bin/env sage-python
"""R909: original F with the exact PARI basis and small-prime Dixon continuation.

Run only in the public repository Actions.  Finite primes select product bases
and propose rational coefficients.  Only the full rational elliptic identity
certifies the original map.  No modular-parametrization/Manin-constant
assumption is used.
"""
import os
if (os.environ.get("GITHUB_ACTIONS") != "true" or
        os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public"):
    raise SystemExit("Run only in the public research repository Actions.")

import argparse
import hashlib
import json
import time
from pathlib import Path
from sage.all import (QQ, ZZ, GF, EllipticCurve, ModularForms, PowerSeriesRing,
                      LaurentSeriesRing, matrix, vector, next_prime,
                      set_random_seed)
from sage.env import SAGE_VERSION

PARSER = argparse.ArgumentParser()
PARSER.add_argument("--weights", default="4")
PARSER.add_argument("--prime-search-start", type=int, default=1000000)
PARSER.add_argument("--prime-search-ceiling", type=int, default=1001000)
PARSER.add_argument("--digits-schedule", default="512,1024")
PARSER.add_argument("--dixon-stride", type=int, default=32)
PARSER.add_argument("--product-prime", type=int, default=1000037)
ARGS = PARSER.parse_args()
WEIGHTS = [int(x) for x in ARGS.weights.split(",") if x]
assert WEIGHTS == [4], "R904 already excludes the original weight-two denominator"
DIXON_SCHEDULE = [int(x) for x in ARGS.digits_schedule.split(",") if x]
assert DIXON_SCHEDULE and DIXON_SCHEDULE == sorted(set(DIXON_SCHEDULE))
assert 1 <= DIXON_SCHEDULE[0] <= DIXON_SCHEDULE[-1] <= 2048
assert 1 <= ARGS.dixon_stride <= 64
assert 10000 <= ARGS.prime_search_start < ARGS.prime_search_ceiling < 94906266
assert ZZ(ARGS.product_prime).is_prime()
STARTED = time.monotonic()
set_random_seed(20261116)

def canonical(obj):
    return json.dumps(obj, sort_keys=True, separators=(",", ":"), ensure_ascii=True)

def digest(obj):
    return hashlib.sha256(canonical(obj).encode()).hexdigest()

def progress(stage, **kw):
    print("RANK2_FIRST_FACTOR_STAGE " + canonical(dict(
        stage=stage, elapsed_seconds=time.monotonic()-STARTED, **kw)), flush=True)

def hash_rows(rows):
    h = hashlib.sha256()
    for row in rows:
        for t in row:
            h.update(str(QQ(t)).encode())
            h.update(b"\n")
        h.update(b";\n")
    return h.hexdigest()

def eta12_unit(ring, precision):
    """E(Q)=prod(1-Q^n)^12, via the exact Euler pentagonal identity."""
    cc = [0]*precision
    cc[0] = 1
    n = 1
    while n*(3*n-1)//2 < precision:
        sign = -1 if n % 2 else 1
        for j in (n*(3*n-1)//2, n*(3*n+1)//2):
            if j < precision:
                cc[j] = sign
        n += 1
    return (ring(cc).add_bigoh(precision)**12).add_bigoh(precision)

def e2_series(ring, precision):
    sigma = [0]*precision
    for d in range(1, precision):
        for n in range(d, precision, d):
            sigma[n] += d
    return ring([1]+[-24*sigma[n] for n in range(1, precision)]).add_bigoh(precision)

from original_newton_cm_germs import short_y_U
from original_f_small_prime_dixon_map import (choose_first_factor_chart,
                                        lift_first_factor_chart)


LOW_MAX = max(204*k+612 for k in WEIGHTS)
LOW_PREC = LOW_MAX+2
CERT_MAX = max(612*(k+6) for k in WEIGHTS)
CERT_PREC = CERT_MAX+3
AN_MAX = 6*(CERT_PREC-1)+1
E17 = EllipticCurve(QQ, [0, 0, 0, 0, 17])
progress("complete original E17 newform", anlist_through=AN_MAX)
assert E17.conductor() == 10404 and E17.j_invariant() == 0
an = list(E17.anlist(AN_MAX))
assert len(an) == AN_MAX+1
assert [an[1], an[7], an[13], an[19]] == [1, -5, -7, -7]
assert an[2] == an[3] == an[17] == 0
assert all(c == 0 for i, c in enumerate(an) if i % 6 != 1)
f0 = [ZZ(an[6*j+1]) for j in range(CERT_PREC)]
assert f0[:4] == [1, -5, -7, -7]
f_hash = digest([str(t) for t in an])
Qring_low = PowerSeriesRing(QQ, "Q", default_prec=LOW_PREC)
eta_low = eta12_unit(Qring_low, LOW_PREC)
eta_low_coeff = [QQ(eta_low[i]) for i in range(LOW_PREC)]
assert all(t.denominator() == 1 for t in eta_low_coeff)

progress("same rational M2(867) basis", precision=LOW_PREC)
from original_pari_m2_basis import PariOriginalM2Basis
PARI_M2 = PariOriginalM2Basis(progress)
forms2 = PARI_M2.forms
q2exp = [g.q_expansion(LOW_PREC) for g in forms2]
q2low = [[QQ(g[j]) for j in range(LOW_PREC)] for g in q2exp]
q2hash = hash_rows(q2low)
fpbase = GF(ARGS.product_prime)
assert ARGS.product_prime > 6*LOW_MAX+1
assert all(t.denominator() % ARGS.product_prime for row in q2low for t in row)
assert matrix(fpbase, [[fpbase(t) for t in row[:205]] for row in q2low]).rank() == 120

# The producer proves completeness of every selected product basis by reaching
# the exact dimension with a nonzero minor at one good prime.
recipes_by_power = {1: [(i,) for i in range(120)]}
for power in range(2, max(k+6 for k in WEIGHTS)//2+1):
    weight = 2*power
    expected = 102*weight-84
    nsturm = 102*weight+1
    Sp = PowerSeriesRing(fpbase, "Q", default_prec=nsturm)
    two = [Sp([fpbase(t) for t in row[:nsturm]]).add_bigoh(nsturm) for row in q2low]
    previous = recipes_by_power[power-1]
    previous_series = []
    for rr in previous:
        ss = Sp.one().add_bigoh(nsturm)
        for ii in rr:
            ss *= two[ii]
        previous_series.append(ss.add_bigoh(nsturm))
    selected, selected_rows, seen = [], [], set()
    for i in range(120):
        new_recipes, new_rows = [], []
        for rr, ss in zip(previous, previous_series):
            recipe = tuple(sorted((i,)+rr))
            if recipe in seen:
                continue
            seen.add(recipe)
            prod = (two[i]*ss).add_bigoh(nsturm)
            new_recipes.append(recipe)
            new_rows.append([prod[j] for j in range(nsturm)])
        if not new_rows:
            continue
        all_recipes = selected+new_recipes
        all_rows = selected_rows+new_rows
        piv = tuple(matrix(fpbase, all_rows).transpose().pivots())
        selected = [all_recipes[j] for j in piv]
        selected_rows = [all_rows[j] for j in piv]
        progress("product basis rank", weight=weight, rank=len(selected),
                 expected=expected, batches=i+1)
        if len(selected) == expected:
            break
    assert len(selected) == expected, "No complete product basis was certified"
    recipes_by_power[power] = selected
    progress("complete rational product basis", weight=weight, dimension=expected,
             recipe_sha256=digest(selected), good_prime=ARGS.product_prime,
             sturm_prefix=nsturm)

qhigh_cache = {}
def product_rows(weight, precision, high=False):
    if high:
        if precision not in qhigh_cache:
            progress("extend same M2 basis for strict certificate", precision=precision)
            expanded = [g.q_expansion(precision) for g in forms2]
            qhigh_cache[precision] = [
                [QQ(g[j]) for j in range(precision)] for g in expanded]
        rows2 = qhigh_cache[precision]
    else:
        rows2 = [row[:precision] for row in q2low]
    ring = PowerSeriesRing(QQ, "Q", default_prec=precision)
    two = [ring(row).add_bigoh(precision) for row in rows2]
    result = []
    for recipe in recipes_by_power[weight//2]:
        s = ring.one().add_bigoh(precision)
        for i in recipe:
            s *= two[i]
        result.append([QQ(s[j]) for j in range(precision)])
    return result

def residue_solution(arows, brows, fp, low_order):
    precision = low_order+1
    ring = PowerSeriesRing(fp, "Q", default_prec=precision)
    am = [ring([fp(t) for t in row[:precision]]).add_bigoh(precision) for row in arows]
    bm = [ring([fp(t) for t in row[:precision]]).add_bigoh(precision) for row in brows]
    uu = ring(short_y_U(fp, f0, low_order)).add_bigoh(precision)
    ee = ring([fp(t) for t in eta_low_coeff[:precision]]).add_bigoh(precision)
    vv = (ee*uu).add_bigoh(precision)
    assert vv[0] == -1 and vv[1] == 5
    bv = [(b*vv).add_bigoh(precision) for b in bm]
    da, db = len(arows), len(brows)
    mat = matrix(fp, low_order+1, da+db,
                 lambda i, j: am[j][i] if j < da else -bv[j-da][i])
    ech = mat.echelon_form()
    piv = tuple(ech.pivots())
    if len(piv) == da+db:
        return {"rank": len(piv), "pivots": piv, "solution": None}
    pivset = set(piv)
    free = next(i for i in range(da+db) if i not in pivset)
    sol = vector(fp, da+db)
    sol[free] = 1
    for i, j in enumerate(piv):
        sol[j] = -ech[i, free]
    assert (mat*sol).is_zero()
    aa = sum((sol[i]*am[i] for i in range(da)), ring.zero())
    bb = sum((sol[da+j]*bm[j] for j in range(db)), ring.zero())
    assert bb != 0 and aa != 0
    assert aa.valuation() == bb.valuation()
    val = int(bb.valuation())
    assert aa[val] == -bb[val]
    return {"rank": len(piv), "pivots": piv, "solution": sol,
            "free": free, "B_valuation": val}

def initial_exact_check(sol, arows, brows, bval):
    da, db = len(arows), len(brows)
    precision = bval+13
    ring = PowerSeriesRing(QQ, "Q", default_prec=precision)
    aa = ring([sum((sol[i]*arows[i][j] for i in range(da)), QQ(0))
               for j in range(precision)]).add_bigoh(precision)
    bb = ring([sum((sol[da+i]*brows[i][j] for i in range(db)), QQ(0))
               for j in range(precision)]).add_bigoh(precision)
    if not aa or not bb or aa.valuation() != bval or bb.valuation() != bval:
        return False
    vg = (ring(short_y_U(QQ, f0, 12))*ring(eta_low_coeff[:13])).add_bigoh(13)
    return (aa-vg*bb).add_bigoh(bval+10) == 0

def strict_original_certificate(weight, sol, arows, brows):
    bound = 612*(weight+6)
    precision = bound+3
    ahigh = product_rows(weight+6, precision, high=True)
    bhigh = product_rows(weight, precision, high=True)
    assert all(row[:len(arows[i])] == arows[i] for i, row in enumerate(ahigh))
    assert all(row[:len(brows[i])] == brows[i] for i, row in enumerate(bhigh))
    da, db = len(ahigh), len(bhigh)
    ring = PowerSeriesRing(QQ, "Q", default_prec=precision)
    Q = ring.gen()
    aa = ring([sum((sol[i]*ahigh[i][j] for i in range(da)), QQ(0))
               for j in range(precision)]).add_bigoh(precision)
    bb = ring([sum((sol[da+i]*bhigh[i][j] for i in range(db)), QQ(0))
               for j in range(precision)]).add_bigoh(precision)
    assert aa != 0 and bb != 0 and aa.valuation() == bb.valuation()
    val = int(bb.valuation())
    assert aa[val] == -bb[val]
    lring = LaurentSeriesRing(QQ, "Q", default_prec=precision)
    vv = lring(aa)/lring(bb)
    assert vv[0] == -1 and vv[1] == 5
    ee = eta12_unit(ring, precision)
    delta = (Q*ee**2).add_bigoh(precision)
    HH = (Q*ring(f0[:precision]).add_bigoh(precision)**3*ee).add_bigoh(precision)
    assert HH[1] == 1 and HH[2] == -27
    e2 = e2_series(ring, precision)
    cc = (Q*aa.derivative())*bb-aa*(Q*bb.derivative())-QQ(1)/2*e2*aa*bb
    assert cc != 0 and cc.valuation() == 2*val
    assert cc[2*val] == bb[val]**2/2
    residual = (8*delta*cc**3-HH*bb**2*(aa**2-17*delta*bb**2)**2).add_bigoh(bound+1)
    bad = next((j for j in range(bound+1) if residual[j] != 0), None)
    info = {
        "sturm_bound": bound,
        "full_0_through_bound_identity": bad is None,
        "coordinate_coefficients_sha256": digest([str(QQ(t)) for t in sol]),
        "same_M2_high_basis_sha256": hash_rows(qhigh_cache[precision]),
        "numerator_weight": weight+6,
        "denominator_weight": weight,
        "B_order_at_infinity": val,
        "V_constant": "-1",
        "V_Q_coefficient": "5",
        "equation": "8*Delta*C^3=H*B^2*(A^2-17*Delta*B^2)^2"
    }
    if bad is not None:
        info["first_nonzero_index"] = bad
        info["first_nonzero_value_sha256"] = digest(str(QQ(residual[bad])))
    return bad is None, info

def choose_eligible_small_prime(weight, arows, brows, low_order):
    denominators = {t.denominator() for rows in (arows, brows)
                    for row in rows for t in row}
    prime = next_prime(max(ZZ(ARGS.prime_search_start)-1, ZZ(6*low_order+1)))
    searched = []
    while prime <= ARGS.prime_search_ceiling:
        entry = {"prime": int(prime)}
        if any(d % prime == 0 for d in denominators):
            entry["status"] = "nonunit_original_input_denominator"
        else:
            fp = GF(prime)
            ma = matrix(fp, [[fp(t) for t in row[:102*(weight+6)+1]]
                             for row in arows], implementation="linbox-double")
            mb = matrix(fp, [[fp(t) for t in row[:102*weight+1]]
                             for row in brows], implementation="linbox-double")
            assert "matrix_modn_dense_double" in type(ma).__module__
            assert "matrix_modn_dense_double" in type(mb).__module__
            arank, brank = ma.rank(), mb.rank()
            entry.update(numerator_basis_rank=int(arank),
                         denominator_basis_rank=int(brank),
                         exact_matrix_backend=type(ma).__module__+"."+type(ma).__name__)
            if arank == len(arows) and brank == len(brows):
                entry["status"] = "selected"
                searched.append(entry)
                progress("F Dixon eligible small prime selected",
                         prime=int(prime), search=searched)
                return prime, fp, searched
            entry["status"] = "bad_reduction_of_original_full_bases"
        searched.append(entry)
        prime = next_prime(prime)
    progress("F Dixon finite small-prime search exhausted", search=searched)
    return None, None, searched

cases = []
CERTIFIED_FIRST_FACTOR_SOLUTION = None
CERTIFIED_FIRST_FACTOR_WEIGHT = None
for weight in WEIGHTS:
    low_order = 204*weight+612
    precision = low_order+1
    arows = product_rows(weight+6, precision)
    brows = product_rows(weight, precision)
    da, db = len(arows), len(brows)
    assert da == 102*(weight+6)-84 and db == 102*weight-84
    case = {
        "weight": weight, "low_last_index_inclusive": low_order,
        "matrix_shape": [precision, da+db],
        "numerator_product_recipe_sha256": digest(recipes_by_power[(weight+6)//2]),
        "denominator_product_recipe_sha256": digest(recipes_by_power[weight//2]),
        "numerator_rational_basis_sha256": hash_rows(arows),
        "denominator_rational_basis_sha256": hash_rows(brows),
        "digits_schedule": DIXON_SCHEDULE,
        "prime_search_interval": [ARGS.prime_search_start, ARGS.prime_search_ceiling]
    }
    prime, fp, searched = choose_eligible_small_prime(
        weight, arows, brows, low_order)
    case["prime_search"] = searched
    if prime is None:
        case.update(status="finite_small_prime_search_exhausted_without_a_certificate",
                    scope="Only a finite auxiliary-prime budget; no map nonexistence conclusion.")
        cases.append(case)
        print("RANK2_FIRST_FACTOR_CASE "+canonical(case), flush=True)
        continue
    case["reconstruction_prime"] = int(prime)
    progress("original F small-prime low matrix", weight=weight,
             numerator_dimension=da, denominator_dimension=db,
             rows=precision, columns=da+db, prime=int(prime),
             digits_schedule=DIXON_SCHEDULE)
    chart = choose_first_factor_chart(arows, brows, fp, f0,
                                      eta_low_coeff, low_order, progress)
    if chart["solution"] is None:
        case.update(status="proved_no_ratio_for_original_n1_at_this_weight",
                    full_rank_prime=int(prime), modular_rank=chart["rank"])
    else:
        case.update(modular_rank=chart["rank"], free=chart["free"],
                    B_valuation_mod_prime=chart["B_valuation"])
        previous_solution = None
        previous_digits = 0
        history = []
        for digits in DIXON_SCHEDULE:
            progress("F Dixon precision stage start", weight=weight,
                     prime=int(prime), previous_digits=previous_digits,
                     requested_digits=digits, base_chart_recomputed=False)
            residues, modulus, lift_info, full_zero = lift_first_factor_chart(
                chart, arows, brows, f0, eta_low_coeff, prime, digits,
                low_order, progress, ARGS.dixon_stride,
                previous_solution=previous_solution,
                previous_digits=previous_digits)
            stage = {"digits": digits, "fixed_prime_lift": lift_info}
            if not full_zero:
                stage["status"] = "fixed_chart_fails_full_prime_power_window"
                history.append(stage)
                case.update(status=stage["status"],
                            scope="This chart failed an original row; no map nonexistence conclusion.")
                break
            previous_solution, previous_digits = residues, digits
            progress("F Dixon rational reconstruction start",
                     coordinates=len(residues), modulus_bits=int(modulus.nbits()),
                     digits=digits)
            try:
                sol = vector(QQ, [c.rational_reconstruction(modulus) for c in residues])
            except (ArithmeticError, ValueError, ZeroDivisionError):
                stage["status"] = "rational_reconstruction_incomplete"
                history.append(stage)
                progress("F Dixon precision stage not yet certified",
                         digits=digits, reason=stage["status"])
                continue
            assert sol[chart["free"]] == 1
            pivset = set(chart["pivots"])
            assert all(sol[j] == 0 for j in range(da+db)
                       if j != chart["free"] and j not in pivset)
            progress("F Dixon rational reconstruction complete",
                     coordinates=len(sol), coordinate_sha256=digest([str(c) for c in sol]),
                     digits=digits)
            progress("F Dixon original short exact check start", digits=digits)
            if not initial_exact_check(sol, arows, brows, chart["B_valuation"]):
                stage["status"] = "rational_candidate_fails_original_short_check"
                history.append(stage)
                progress("F Dixon precision stage not yet certified",
                         digits=digits, reason=stage["status"])
                continue
            progress("candidate reaches full original first-factor certificate",
                     weight=weight, prime=int(prime), digits=digits)
            passed, info = strict_original_certificate(weight, sol, arows, brows)
            stage["last_exact_certificate"] = info
            if not passed:
                stage["status"] = "rational_candidate_fails_original_full_certificate"
                history.append(stage)
                progress("F Dixon precision stage not yet certified",
                         digits=digits, reason=stage["status"],
                         first_nonzero_index=info["first_nonzero_index"])
                continue
            CERTIFIED_FIRST_FACTOR_SOLUTION = sol
            CERTIFIED_FIRST_FACTOR_WEIGHT = weight
            stage["status"] = "certified_original_first_factor"
            history.append(stage)
            case.update(
                status="certified_original_first_factor",
                certified_digits=digits, modulus_bits=int(modulus.nbits()),
                last_exact_certificate=info,
                coordinate_recipe="On original X0(10404): y=A/(eta(Q)^12*B), x=f(q)*(A^2-17*Delta*B^2)/(2*eta(Q)^12*C), Q=q^6.",
                original_differential="dx/(2y)=f(q)*dq/q",
                normalization="infinity maps to O; x=q^-2+O(q^4), y=-q^-3+O(q^3)",
                no_assumed_manin_constant=True)
            break
        else:
            case.update(status="dixon_precision_schedule_exhausted_without_a_certificate",
                        scope="No a priori height bound; finite precision exhaustion does not exclude the map.")
        case["precision_history"] = history
    cases.append(case)
    print("RANK2_FIRST_FACTOR_CASE "+canonical(case), flush=True)

result = {
    "kind": "rank2_original_first_factor_level867_coordinates",
    "source": os.environ.get("RANK2_SOURCE_SHA"),
    "run_id": os.environ.get("RANK2_RUN_ID"),
    "run_attempt": os.environ.get("RANK2_RUN_ATTEMPT"),
    "image": os.environ.get("RANK2_IMAGE"),
    "sage_version": SAGE_VERSION,
    "germ_algorithm": "R889 exact Newton; full defining residuals retained",
    "reconstruction_algorithm": "R909 exact PARI basis; small-prime LinBox chart; compatible Dixon continuation; unchanged complete char-zero certificate",
    "small_prime_dixon_dependency_sha256": hashlib.sha256(Path(__file__).with_name(
        "original_f_small_prime_dixon_map.py").read_bytes()).hexdigest(),
    "M2_basis_provenance": PARI_M2.provenance,
    "dixon_F_dependency_sha256": hashlib.sha256(Path(__file__).with_name(
        "original_f_small_prime_dixon_map.py").read_bytes()).hexdigest(),
    "dixon_reducer_dependency_sha256": hashlib.sha256(Path(__file__).with_name(
        "original_padic_dixon_map.py").read_bytes()).hexdigest(),
    "newton_germ_dependency_sha256": hashlib.sha256(Path(__file__).with_name(
        "original_newton_cm_germs.py").read_bytes()).hexdigest(),
    "slow_germ_dependency_sha256": hashlib.sha256(Path(__file__).with_name(
        "original_low_weight_cm_tools.py").read_bytes()).hexdigest(),
    "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    "readme_blobs": {
        "README.md": os.environ.get("RANK2_ROOT_README_SHA"),
        "topics/rank2-sha-infinitely-many-p/README.md":
            os.environ.get("RANK2_TOPIC_README_SHA")},
    "parameters": vars(ARGS),
    "original_curve": [0, 0, 0, 0, 17],
    "source_level": 10404, "base_level": 867, "base_parameter": "Q=q^6",
    "full_original_anlist_through": AN_MAX,
    "original_anlist_sha256": f_hash,
    "M2_low_basis_sha256": q2hash,
    "product_recipe_hashes": {
        str(2*p): digest(rr) for p, rr in recipes_by_power.items()},
    "cases": cases,
    "certified_original_first_factor": CERTIFIED_FIRST_FACTOR_SOLUTION is not None,
    "original_shadow_computed": False,
    "elapsed_seconds": time.monotonic()-STARTED,
    "consumer_contract": "Use the same-process CERTIFIED_FIRST_FACTOR_SOLUTION, CERTIFIED_FIRST_FACTOR_WEIGHT, forms2 and recipes_by_power, or deterministically replay this committed producer. No coefficient data file is created."
}
payload = canonical(result)
print("RANK2_FIRST_FACTOR_RESULT "+payload, flush=True)
print("RANK2_FIRST_FACTOR_SHA256 "+hashlib.sha256(payload.encode()).hexdigest(), flush=True)
