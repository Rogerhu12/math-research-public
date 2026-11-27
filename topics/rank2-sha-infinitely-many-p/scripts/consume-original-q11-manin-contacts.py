#!/usr/bin/env python3
"""Compute the genuine Manin value of the already published original Q_11.

Only the immutable original receipt is consumed.  The section search and the
two-cover lift are never run.  All Hasse points, including ramified branches,
are retained through complete Fitting ideals over F_11[X].
"""
import hashlib
import json
import os
import runpy
import sys
import time
from pathlib import Path

if os.environ.get("GITHUB_ACTIONS") != "true" or \
        os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public":
    raise SystemExit("Mathematical execution requires the named public GitHub Actions repository.")

HELPER_NAME = "lift-original-q11-section-to-two-cover.py"
HELPER_SHA256 = "812fd5e5a8899e2b47095c2eee50e22ba5b7063397121a0e44ec8801d1fe3b43"
Q = 11


def main():
    started = time.monotonic()
    helper_path = Path(__file__).with_name(HELPER_NAME)
    helper_raw = helper_path.read_bytes()
    if hashlib.sha256(helper_raw).hexdigest() != HELPER_SHA256:
        raise RuntimeError("The already published rational-field/receipt helper source differs.")
    # This name leaves the helper's main() inactive: no search, root, or lift runs.
    helper = runpy.run_path(str(helper_path), run_name="rank2_manin_source_definitions")
    Rat = helper["Rat"]
    poly = helper["poly"]
    binding = helper["ORIGINAL"]
    paid = helper["read_paid_result"](binding)
    os.environ.pop("RANK2_ACTIONS_READ_TOKEN", None)
    if paid.get("q") != Q or paid.get("source_sha256") != binding["script_sha256"] or \
            paid.get("enumeration_sha256") != binding["enumeration_sha256"] or \
            paid.get("normalized_solution_count") != 1 or \
            paid.get("mathematical_status") != "ACTUAL_ORIGINAL_HEIGHT_22_OVER_3_SECTION_FOUND" or \
            len(paid.get("representatives", [])) != 1:
        raise RuntimeError("The pinned live source does not supply the unique original Q_11.")

    xvar = Rat(poly([0, 1]))
    disc = 4*xvar**3 + 1
    Base = helper["quadratic_field"](disc)
    XB, VB = Base(xvar), Base(0, 1)
    YB = (VB-1)/2
    t = -YB/27
    x, W = helper["original_section"](paid["representatives"][0], XB, YB)
    xs = x + Base(1)/12
    a4 = t/2 - Base(1)/48
    a6 = t**2/4 - t/24 + Base(1)/864
    if -3*W**2/4 != xs**3 + a4*xs + a6:
        raise ArithmeticError("The live original point does not return the specified short model.")

    def dr(r):
        return Rat(r.n.derivative()*r.d-r.n*r.d.derivative(), r.d**2)

    def db(f):
        # D_B X=V, D_B V=6X^2, V^2=4X^3+1.
        return Base(disc*dr(f.b) + 6*xvar**2*f.b, dr(f.a))

    def dks(f):
        return (XB/9)*db(f)

    def pmul(f, g):
        ans = [Base(0) for _ in range(len(f)+len(g)-1)]
        for i, fi in enumerate(f):
            for j, gj in enumerate(g):
                ans[i+j] = ans[i+j] + fi*gj
        return ans

    def peval(f, value):
        ans = Base(0)
        for coefficient in reversed(f):
            ans = ans*value + coefficient
        return ans

    power = [Base(1)]
    cubic = [a6, a4, Base(0), Base(1)]
    for _ in range((Q-1)//2):
        power = pmul(power, cubic)
    hasse = power[Q-1]
    high_part = power[Q:]
    z = (dks(xs)-2*xs**2-(1-36*t)*xs/6-4*a4/3)/W
    mu = W*peval(high_part, xs)/2 + (z**Q + hasse*z)/3
    if mu.is_zero():
        raise ArithmeticError("The primitive original Q_11 has zero Manin image.")

    def polynomial_pair(f):
        if f.a.d.degree() != 0 or f.b.d.degree() != 0:
            raise ArithmeticError("A required affine regular function still has a finite pole.")
        return f.a.n, f.b.n

    ma, mb = polynomial_pair(mu)
    ha, hb = polynomial_pair(hasse)
    disc_poly = disc.n

    def enc_pair(f):
        a, b = polynomial_pair(f)
        return {"coefficient_1": [int(c) for c in a],
                "coefficient_V": [int(c) for c in b]}

    def fitting_pair(f, g):
        # The ideal (f,g) in F_11[X,V]/(V^2-disc) has these four full rows.
        a, b = polynomial_pair(f)
        c, d = polynomial_pair(g)
        rows = ((a,b), (disc_poly*b,a), (c,d), (disc_poly*d,c))
        gcd = poly([])
        for i in range(4):
            for j in range(i+1,4):
                minor = rows[i][0]*rows[j][1]-rows[i][1]*rows[j][0]
                gcd = gcd.gcd(minor)
        if gcd.is_zero():
            raise ArithmeticError("The specified complete quotient is not finite.")
        gcd = gcd * pow(int(gcd[gcd.degree()]), Q-2, Q)
        return gcd

    hasse_norm = hasse.norm()
    if hasse_norm.d.degree() != 0 or hasse_norm.n.degree() != Q-2:
        raise ArithmeticError("The complete finite Hasse divisor has the wrong degree.")
    if fitting_pair(hasse, db(hasse)).degree() != 0:
        raise ArithmeticError("The finite Hasse divisor is not geometrically reduced.")

    # Full thick intersections: length O_B/(Hasse^n,mu), no point samples.
    lengths, fit_records = [], []
    hasse_power = Base(1)
    for n in range(1,Q):
        hasse_power = hasse_power*hasse
        fitting = fitting_pair(hasse_power, mu)
        lengths.append(fitting.degree())
        fit_records.append({"thickness": n, "length": fitting.degree(),
                            "fitting_generator": [int(c) for c in fitting]})
    increments = [lengths[0]] + [lengths[i]-lengths[i-1] for i in range(1,len(lengths))]
    if any(x < 0 for x in increments) or increments[0] != increments[1] or \
            any(increments[i+1] > increments[i] for i in range(len(increments)-1)) or \
            increments[-1] != 0:
        raise ArithmeticError("The full supersingular multiplicities contradict the proved formal bounds.")

    def pole_at_O(a,b):
        values = []
        if not a.is_zero():
            values.append(2*a.degree())
        if not b.is_zero():
            values.append(2*b.degree()+3)
        return max(values)

    mu_pole = pole_at_O(ma,mb)
    canonical_nu_order = Q-mu_pole
    if canonical_nu_order < 0 or canonical_nu_order > Q-2 or canonical_nu_order == 1:
        raise ArithmeticError("The canonical good-fiber Manin order violates the complete model.")

    def cusp_order(sign):
        # X is a parameter at V=+/-1.  Solve the exact branch V^2=1+4X^3.
        bound = Q+1
        vseries = [sign % Q] + [0]*bound
        inv_twice = pow((2*sign) % Q, Q-2, Q)
        for n in range(1,bound+1):
            target = 4 if n == 3 else 0
            inner = sum(vseries[i]*vseries[n-i] for i in range(1,n))
            vseries[n] = (target-inner)*inv_twice % Q
        aa, bb = [int(c) for c in ma], [int(c) for c in mb]
        for n in range(bound+1):
            value = aa[n] if n < len(aa) else 0
            value += sum(bb[i]*vseries[n-i] for i in range(min(n,len(bb)-1)+1))
            if value % Q:
                return n
        raise ArithmeticError("The exact cusp valuation exceeds its global divisor bound.")

    cplus, cminus = cusp_order(1), cusp_order(-1)
    if cplus < 1 or cminus < 1:
        raise ArithmeticError("A multiplicative boundary did not cancel its KS pole.")
    finite_ss_zero_degree = lengths[-1]
    remaining_nu_zero_degree = Q-2-canonical_nu_order-finite_ss_zero_degree-(cplus-1)-(cminus-1)
    if remaining_nu_zero_degree < 0:
        raise ArithmeticError("The exact global zero divisor has negative remaining degree.")

    contacts = {"1": Q-2-lengths[0] + int(canonical_nu_order == 0)}
    for n in range(2,Q-1):
        count = increments[n-1]-increments[n]
        if canonical_nu_order == n:
            count += 1
        if count:
            contacts[str(n)] = count
    if sum(contacts.values()) != Q-1:
        raise ArithmeticError("The contact census does not retain every supersingular point.")

    value_data = {
        "function_field": "F11(X)[V]/(V^2-4X^3-1); Y=(V-1)/2; t=-Y/27",
        "mu_over_original_delta": enc_pair(mu),
        "hasse_in_short_model": enc_pair(hasse),
        "original_delta_square": -3,
        "finite_Hasse_norm": [int(c) for c in hasse_norm.n],
        "finite_thick_intersections": fit_records,
        "canonical_nu_order": canonical_nu_order,
        "cusps": {"Y0_mu_order": cplus, "Yminus1_mu_order": cminus,
                  "Y0_nu_order": cplus-1, "Yminus1_nu_order": cminus-1},
        "geometric_ss_contact_counts_by_exact_order": contacts,
        "remaining_non_ss_non_cusp_nu_zero_degree": remaining_nu_zero_degree,
    }
    value_raw = json.dumps(value_data, sort_keys=True, separators=(",", ":")).encode()
    result = {
        "status": "EXACT_ORIGINAL_Q11_MANIN_AND_FULL_SUPERSINGULAR_CONTACTS",
        "q": Q,
        "input_receipt": dict(binding, consumed_live=True, section_search_repeated=False),
        "helper_source_sha256": HELPER_SHA256,
        "helper_main_called": False,
        "values": value_data,
        "values_sha256": hashlib.sha256(value_raw).hexdigest(),
        "identities": {
            "original_short_point_equation": True,
            "published_Broumas_formula_in_original_W_orientation": True,
            "all_finite_Hasse_points_and_thick_orders": True,
            "both_multiplicative_boundaries_and_canonical_fiber": True,
            "global_nu_zero_degree": Q-2,
            "no_point_sampling": True,
        },
        "scope": {
            "original_27_weighted_values_nonzero": False,
            "target_p_contact_inflation_claimed": False,
            "infinitely_many_target_p": False,
        },
        "source_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "elapsed_seconds": time.monotonic()-started,
    }
    encoded = json.dumps(result, sort_keys=True, separators=(",", ":"))
    if len(encoded.encode()) > 60000:
        raise RuntimeError("The compact exact receipt exceeds the existing runner bound.")
    print(encoded)


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        print(json.dumps({"status": "EXECUTION_ERROR", "error_type": type(exc).__name__,
                          "message": str(exc)}, sort_keys=True, separators=(",", ":")),
              file=sys.stderr)
        raise
