#!/usr/bin/env python3
"""R483: canonical odd sigma CM13/19 and complete original S/T/new/ref rows.

Exact characteristic-zero arithmetic only.  The whole matrices come from the
complete canonical fiber certificates R466, R476, and R480.  No varying-prime
sampling and no identification of an auxiliary slope with a rank-two slope.
"""
from pathlib import Path
from math import gcd
import json
import runpy

BASE = Path(__file__).resolve().parents[1]
H = runpy.run_path(str(BASE / "scripts/check-r466-fixed-two-division-source.py"))
for key in ("Q", "Mat", "Poly", "fq", "fa", "fn", "fs", "fm", "fi", "fp",
            "pa", "ps", "pm", "pd", "ptrim", "km", "ka", "ks", "kp",
            "kvec", "kzero", "identity", "rank", "get_entry", "serialize_matrix"):
    globals()[key] = H[key]
ZERO, ONE = fq(0), fq(1)
OMEGA = fq(Q(-1, 2), Q(1, 2))


def decode(d):
    return tuple(Mat([[Q(x) for x in row] for row in d[k]]) for k in ("real", "delta"))


def read(name):
    return json.loads((BASE / name).read_text())


def division_q(norm, gamma):
    degree = (norm - 1) // 2
    terms = degree // 3
    xx = [Q(1), Q(-1, 7), Q(1, 637), Q(-1, 84721)]
    logs = [ZERO] + [
        fm(fq(-xx[k] / (6*k*(6*k-1))), fs(fp(gamma, 6*k), fq(norm)))
        for k in range(1, terms+1)]
    e = [ONE]
    for n in range(1, terms+1):
        val = ZERO
        for k in range(1, n+1):
            val = fa(val, fm(fq(k), fm(logs[k], e[n-k])))
        e.append(fm(val, fq(Q(1, n))))
    B = Poly(xx)
    coefficients = []
    for k in range(terms+1):
        val = e[k]
        for j in range(k):
            val = fs(val, fm(coefficients[j], fq((B**(degree-3*j))[k-j])))
        coefficients.append(val)
    q = [ZERO] * (degree+1)
    for j, coefficient in enumerate(coefficients):
        q[degree-3*j] = coefficient
    return q


def odd_sigma_fiber(norm, gamma, q, target=1):
    """The entire S1 line: one exact complete fiber fixes the absolute scalar."""
    gb = (gamma[0], -gamma[1])
    qb = [(a[0], -a[1]) for a in q]
    ng = H["qmap"](q, norm)
    f = pa(ng, ps(pm(q, q), fm(fq(-target), fp(gamma, 2))))
    assert len(f) == norm+1 and f[-1] == ONE

    def red(a):
        return pd(a, f)[1]

    def invert(a):
        r0, r1, s0, s1 = f, a, [ZERO], [ONE]
        while r1 != [ZERO]:
            quotient, r2 = pd(r0, r1)
            r0, r1, s0, s1 = r1, r2, s1, pa(s0, ps(pm(quotient, s1), fq(-1)))
        assert len(r0) == 1 and r0[0] != ZERO
        result = red(ps(s0, fi(r0[0])))
        assert red(pm(a, result)) == [ONE]
        return result

    traces = [fq(norm)]
    for k in range(1, norm):
        value = fm(fq(k), f[norm-k])
        for j in range(1, k):
            value = fa(value, fm(f[norm-j], traces[k-j]))
        traces.append(fn(value))
    framed = ps(red(pm(qb, invert(q))), fm(gb, fi(gamma)))
    total = ZERO
    for j, coefficient in enumerate(framed):
        total = fa(total, fm(coefficient, traces[j]))
    return fm(total, fi(gamma))


def main():
    g13, g19 = fq(Q(7, 2), Q(1, 2)), fq(4, 1)
    q13, q19 = division_q(13, g13), division_q(19, g19)
    assert q19 == H["q19_polynomial"]()[1]
    s13, s19 = odd_sigma_fiber(13, g13, q13), odd_sigma_fiber(19, g19, q19)
    assert s13 == fq(-1) and s19 == fq(1)
    assert fp(s13, 6) == fp(s19, 6) == ONE

    r465 = read("scripts/check-r465-common-six-sigma-true-core-marginal.json")
    for det in (int(r465["full_determinant"]), int(r465["old_Y_fixed_cover_determinant"])):
        assert gcd(det*42, 13*19) == 1

    I72 = identity(13)
    M72 = decode(read("notes/2026-11-14-literature-degree72-cm7-exact.json")["matrix"])
    N72 = decode(read("scripts/check-r480-actual-input-cm19.json")["matrix"])
    assert kp(M72, 6, I72) == kp(N72, 6, I72) == I72
    assert km(M72, N72) == km(N72, M72)
    K72 = ks(kp(M72, 3, I72), fq(-1))
    PT = km(ks(ka(I72, K72), fq(Q(1, 2))),
            H["eig_project"](N72, OMEGA, I72, 6))
    assert rank(PT) == 1 and km(PT, PT) == PT
    X = Poly([0, 1])
    tp = X*(X+4)*(X**3-96*X**2+48*X+64)*(7*X**2-4*X+16)
    tp *= (X+1)*(X-8)*(X**2+20*X-8)/7
    T = kvec([tp[j] for j in range(13)])
    assert get_entry(T, 11) == ONE and get_entry(T, 12) == ZERO
    assert km(M72, T) == ks(T, fq(-1))
    assert km(N72, T) == ks(T, OMEGA)
    assert km(PT, T) == T and km(K72, T) == T
    assert km(PT, K72) == PT
    joint_dimensions = []
    roots = [ONE, OMEGA, fp(OMEGA, 2), fq(-1), fn(OMEGA), fn(fp(OMEGA, 2))]
    for a in roots:
        row = []
        E = H["eig_project"](M72, a, I72, 6)
        for b in roots:
            row.append(rank(km(E, H["eig_project"](N72, b, I72, 6))))
        joint_dimensions.append(row)

    I136 = identity(23)
    M136 = decode(read("notes/2026-11-14-theta-degree136-cm7-exact.json")["matrix"])
    N136 = decode(read("notes/2026-11-14-theta-degree136-cm19-exact.json")["matrix"])
    # R466's whole identity is N13=R*N7^23; R=+1 on this principal block.
    N13 = kp(M136, 5, I136)
    assert kp(N13, 11, I136) == M136
    assert kp(N13, 18, I136) == kp(N136, 18, I136) == I136
    PS = H["eig_project"](N13, fq(-1), I136)
    Pnew = km(ks(ka(I136, ks(N136, fn(OMEGA))), fq(Q(1, 2))),
              H["eig_project"](N13, OMEGA, I136))
    PH = km(ks(ka(I136, ks(N136, fn(fp(OMEGA, 2)))), fq(Q(1, 2))),
            H["eig_project"](N13, ONE, I136))
    Sd = decode(r465["S_double"])
    Xi = decode(r465["Xi_double"])
    r476 = read("scripts/check-r476-full-xi-wstar-bridge.json")
    Hr = decode(r476["reference_mass_one"])
    New = decode(read("scripts/check-r470-original-negative-source-new-line.json")["Snew"])
    for P in (PS, Pnew, PH):
        assert rank(P) == 1 and km(P, P) == P
    assert km(PS, Sd) == Sd
    assert km(Pnew, New) == New
    assert km(PH, Hr) == Hr
    assert km(PS, Xi) == ks(Sd, fq(Q(-1, 4), Q(-1, 4)))
    assert km(Pnew, Xi) == ks(New, fq(Q(52, 3)))
    assert km(PH, Xi) == ks(Hr, fq(Q(-1, 2016), Q(-1, 2016)))
    negative9 = ks(ka(I136, ks(kp(M136, 9, I136), fq(-1))), fq(Q(1, 2)))
    assert km(Pnew, negative9) == km(PH, negative9) == kzero(23, 23)
    assert km(PS, negative9) == PS
    assert km(PS, Pnew) == km(PS, PH) == km(Pnew, PH) == kzero(23, 23)

    report = {
        "field": "Q(delta), delta^2=-3",
        "normalizations": "N_a=M_a/a, original odd sigma half-character and original six input scales",
        "q13": [[str(x) for x in c] for c in q13],
        "q19": [[str(x) for x in c] for c in q19],
        "odd_sigma_CM13": ["-1", "0"],
        "odd_sigma_CM19": ["1", "0"],
        "six_sigma_simultaneous_characters": {"13": "1", "19": "1"},
        "coordinate_determinants": [r465["full_determinant"], r465["old_Y_fixed_cover_determinant"]],
        "physical_to_unscaled_sigma_determinant_factor": "-42",
        "coprime_to_13_and_19": True,
        "degree72_joint_roots_order": [[str(x) for x in c] for c in roots],
        "degree72_joint_N7_N19_dimensions": joint_dimensions,
        "degree72_T_source": serialize_matrix(T),
        "degree72_T_projector": serialize_matrix(PT),
        "degree72_T_projector_formula": "(I+K72)/2 * E_omega(N19); K72=-N7^3 on principal",
        "degree136_N13_formula": "N13=N7^5 on principal; whole is reflection*N7^23",
        "degree136_S_projector": serialize_matrix(PS),
        "degree136_new_projector": serialize_matrix(Pnew),
        "degree136_reference_projector": serialize_matrix(PH),
        "marginal_companion_masses": {
            "S_state0": ["1", "0"],
            "S_state1": ["-1/4", "-1/4"],
            "new_state0": ["0", "0"],
            "new_state1": ["52/3", "0"],
            "reference_state0": ["0", "0"],
            "reference_state1_b1": ["-1/2016", "-1/2016"],
            "T_both_states": ["0", "6"]
        },
        "reference_curve_D": 668168,
        "companion_total_p_core": {
            "S_state0": "lambda^5", "S_state1": "lambda^5",
            "T": "lambda^5", "new": "-lambda^5", "reference": "-lambda^5"
        },
        "boundary": "All companion CM traces retain full fibers. Old mixed W restrictions move with the companion branches and cannot be put through a projector unchanged."
    }
    Path(__file__).with_suffix(".json").write_text(json.dumps(report, indent=2) + "\n")
    print("R483: odd CM13/19 phases, complete T/S/new/ref projectors, and both determinant conditions proved.")


if __name__ == "__main__":
    main()
