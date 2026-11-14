#!/usr/bin/env python3
"""Original p41 Hodge basis and exact finite translate input for R732.

This new arithmetic runs only in the public repository Actions.  R738's
completed cells, cycles, and intersection form are read by hash, not rebuilt.
No CM period, quotient rational function, beta, or height is evaluated here.
"""
import argparse
from fractions import Fraction
import gzip
import hashlib
import json
import math
import os
from pathlib import Path
import sys
import time

from flint import fmpz, fmpz_poly

P, N, ORDER, BOUND = 41, 246, 42, 800
RESULT = "R745-p41-original-Hodge-input"
LABELS = [1, 13, 19, 25, 31, 37]
DEN = P*(P+1)
GAMMA = (7, 30)
EXPECTED = {
    "original-cosets-and-markings.json.gz":
        "6a73cb699abb5e53328a040ec86bea2c4cac7ef690a29984912c43417cfd0161",
    "integral-compact-Manin-cycles.json.gz":
        "d4dcbac16cc24cefd378fc7afea02fcd34b8043d255c1e84407ff7d21bd257cf",
    "p41-original-period-input-certificate.json":
        "a853f36bf5d6f7d238e805a5c2134b2f7b3db17528195d56d980e66c9c769009",
}


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def read(path):
    data = Path(path).read_bytes()
    return json.loads(gzip.decompress(data) if str(path).endswith(".gz") else data)


def save(path, value):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    data = (json.dumps(value, sort_keys=True, separators=(",", ":")) + "\n").encode()
    if path.suffix == ".gz":
        data = gzip.compress(data, mtime=0)
    tmp = path.with_name(path.name + ".tmp")
    tmp.write_bytes(data)
    tmp.replace(path)


def fm(z, w):
    a, b = z
    c, d = w
    return ((a*c-b*d) % P, (a*d+b*c-b*d) % P)


def fc(z):
    return ((z[0]-z[1]) % P, -z[1] % P)


def fi(z):
    norm = (z[0]*z[0]-z[0]*z[1]+z[1]*z[1]) % P
    assert norm
    inv = pow(norm, -1, P)
    return tuple(inv*a % P for a in fc(z))


def fp(z, k):
    out = (1, 0)
    while k:
        if k & 1:
            out = fm(out, z)
        z = fm(z, z)
        k >>= 1
    return out


def cyclotomic_42():
    x = fmpz_poly([0, 1])
    table = {}
    for d in (1, 2, 3, 6, 7, 14, 21, 42):
        value = x**d-1
        for e in table:
            if d % e == 0:
                value, remainder = divmod(value, table[e])
                assert not remainder
        table[d] = value
    assert table[42].degree() == 12
    return table[42]


def coefficients(poly, length=12):
    assert poly.degree() < length
    return [int(poly[i]) for i in range(length)]


class Field:
    def __init__(self):
        self.modulus = cyclotomic_42()
        self.eta = fmpz_poly([0, 1])
        self.powers = [fmpz_poly([1])]
        for _ in range(1, ORDER):
            self.powers.append(self.mul(self.powers[-1], self.eta))
        assert self.mul(self.powers[-1], self.eta) == 1
        self.zeta = self.powers[14]
        self.s = 1+2*self.zeta
        self.beta = self.eta+self.powers[-1]
        assert self.mul(self.zeta, self.zeta)+self.zeta+1 == 0
        assert self.mul(self.s, self.s) == -3
        self.traces = [sum(int(self.powers[(j+i) % ORDER][i])
                           for i in range(12)) for j in range(ORDER)]
        assert self.traces[0] == 12

    def mul(self, a, b):
        return (a*b) % self.modulus

    def auto(self, a, h):
        result = fmpz_poly([])
        for j in range(a.degree()+1):
            result += int(a[j])*self.powers[h*j % ORDER]
        return result % self.modulus

    def trace(self, a):
        return sum(int(a[i])*self.traces[i] for i in range(a.degree()+1))

    def eval_mod_p(self, a):
        result = (0, 0)
        for i in reversed(range(a.degree()+1)):
            result = fm(result, GAMMA)
            result = ((result[0]+int(a[i])) % P, result[1])
        return result


def finite_points():
    logs, value = {}, (1, 0)
    for j in range(ORDER):
        assert value not in logs
        logs[value] = j
        value = fm(value, GAMMA)
    assert value == (1, 0) and fp(GAMMA, 14) == (0, 1)
    assert all(fp(GAMMA, ORDER//q) != (1, 0) for q in (2, 3, 7))
    points = []
    for a in range(P):
        for b in range(P):
            if a == b == 0:
                continue
            y = (a, b)
            # theta(y)=[y]^(-(p-1)); gamma is the same original Teich label.
            logarithm = logs[fm(fc(y), fi(y))]
            points.append((a, b, (a*a-a*b+b*b) % P,
                           (2*a-b) % P, (-logarithm) % ORDER))
    assert len(points) == P*P-1
    return logs, points


def toric_vector(K, points):
    # rho([[a,-1],[1,a+1]]) e_0, with identity as the last projective torus point.
    counts = [[0]*ORDER for _ in range(P)]
    for a in range(P):
        delta = (a*a+a+1) % P
        assert delta
        for _, _, norm, trace, exponent in points:
            target = (delta*((a+1)*norm+trace)+a) % P
            counts[target][exponent] += 1
    sums = [fmpz_poly(row) % K.modulus for row in counts]
    numerator = [-a for a in sums]
    numerator[0] += P
    c = [a-numerator[0] for a in numerator]
    assert not c[0]
    assert all(K.auto(a, -1) == a for a in c)
    toric_norm = numerator[0]-1
    assert K.eval_mod_p(toric_norm) == (P-1, 0)
    total = sum(c, fmpz_poly([]))
    norm_squared_numerator = P*sum((K.mul(a, a) for a in c), fmpz_poly([]))
    norm_squared_numerator -= K.mul(total, total)
    assert (P+1)*norm_squared_numerator == DEN*DEN*toric_norm
    assert -(P+1)*total == DEN*toric_norm
    # Original normalizer M=[[-1,-1],[0,1]], without moving the split line.
    moved = [fmpz_poly([]) for _ in range(P)]
    for r, a in enumerate(c):
        moved[(-r-1) % P] += a
    assert all(moved[r]-moved[0] == c[r] for r in range(P))
    # One generator of the actual projective Cartan suffices for full invariance.
    generator = None
    for a in range(P):
        # Matrix [[a,-1],[1,a+1]] is multiplication by (a+1)+zeta.
        ratio = fm(fc(((a+1) % P, 1)), fi(((a+1) % P, 1)))
        if all(fp(ratio, ORDER//q) != (1, 0) for q in (2, 3, 7)):
            generator = a
            break
    assert generator is not None
    a = generator
    delta = (a*a+a+1) % P
    # The resulting coordinates have denominator p*DEN; keep it until comparison.
    image = [fmpz_poly([]) for _ in range(P)]
    for r in range(P):
        if not c[r]:
            continue
        row = [[0]*ORDER for _ in range(P)]
        for _, _, norm, trace, exponent in points:
            target = (delta*((r+a+1)*norm+trace)+a) % P
            row[target][exponent] += 1
        for target in range(P):
            image[target] -= K.mul(fmpz_poly(row[target]) % K.modulus, c[r])
    assert all(image[r]-image[0] == P*c[r] for r in range(P))
    return c, toric_norm, generator


def newform(K, logs):
    ans = [fmpz_poly([]) for _ in range(BOUND+1)]
    limit = math.isqrt(4*BOUND//3)+2
    primary_count = 0
    for a in range(-limit, limit+1):
        if a % 3 != 1:
            continue
        for b in range(-limit, limit+1):
            if b % 3:
                continue
            norm = a*a-a*b+b*b
            if not 1 <= norm <= BOUND or norm % P == 0:
                continue
            y = (a % P, b % P)
            exponent = -logs[fm(fc(y), fi(y))] % ORDER
            ans[norm] += K.mul(a+b*K.zeta, K.powers[exponent])
            primary_count += 1
    ans = [a % K.modulus for a in ans]
    assert ans[1] == 1 and not ans[2] and ans[4] == -2
    for n, a in enumerate(ans):
        assert K.auto(a, -1) == a
        if n % 3 != 1 or n % P == 0 or n % 4 == 2:
            assert not a
        if 4*n <= BOUND:
            assert ans[4*n] == -2*a
    return ans, primary_count


def tame_checks(K):
    z2 = K.mul(K.zeta, K.zeta)
    v = (fmpz_poly([1]), -z2)
    def ss(w):
        return w[1], w[0]
    def tt(w):
        return -w[0], -w[0]+w[1]
    cv = tt(ss(v))
    assert cv == tuple(K.mul(z2, a) for a in v)
    reflected = tt(tuple(K.auto(a, -1) for a in v))
    assert reflected == tuple(-a for a in v)
    canonical = tuple(K.mul(K.s, a) for a in v)
    assert tt(tuple(K.auto(a, -1) for a in canonical)) == canonical
    return {"basis": ["H0", "4*H2"],
            "S2_coefficient_matrix": [[0, 1], [1, 0]],
            "T2_coefficient_matrix": [[-1, 0], [-1, 1]],
            "positive_vector": [coefficients(a) for a in v],
            "full_graph_reflection_on_raw_vector": "-1",
            "canonical_arithmetic_scale": "s=sqrt(-3)",
            "positive_original_twist_scale": "alpha*s; alpha^3=4, alpha>0",
            "c1_raw_transport": "zeta^2",
            "transport_already_in_global_period_table": False,
            "c1_transport_rule": "Evaluate the global form at g_star(zeta), or slash once and evaluate at zeta."}


def q_expansions(K, c, a):
    beta_powers = [fmpz_poly([1])]
    for _ in range(5):
        beta_powers.append(K.mul(beta_powers[-1], K.beta))
    linear = []
    for j in range(6):
        by_r = []
        for r in range(P):
            w = K.mul(beta_powers[j], c[r])
            by_r.append([K.trace(K.mul(w, K.powers[k])) for k in range(12)])
        linear.append(by_r)
    inv6 = pow(6, -1, P)
    rows = []
    for n in range(1, BOUND+1):
        if not a[n]:
            continue
        an = coefficients(a[n])
        polynomials = []
        for j in range(6):
            fourier = [0]*P
            for r in range(1, P):
                full_trace = sum(an[k]*linear[j][r][k] for k in range(12))
                assert full_trace % 2 == 0
                # Half of the full degree-12 trace is Tr_F/Q on this real element.
                fourier[-n*r*inv6 % P] += full_trace//2
            last = fourier[-1]
            polynomials.append([str(v-last) for v in fourier[:-1]])
        assert n % 2 == 1 or n % 4 == 0
        rows.append({"n": n, "tame_factor": "s" if n % 2 else "3",
                     "six_integer_trace_Fourier_polynomials": polynomials})
    return beta_powers, rows


def evaluate_mod(coeffs, x, prime):
    value = 0
    for a in reversed(coeffs):
        value = (value*x+int(a)) % prime
    return value


def determinant_mod(matrix, prime):
    a = [row[:] for row in matrix]
    answer = 1
    for c in range(len(a)):
        pivot = next(r for r in range(c, len(a)) if a[r][c] % prime)
        if pivot != c:
            a[c], a[pivot] = a[pivot], a[c]
            answer = -answer
        value = a[c][c] % prime
        answer = answer*value % prime
        inv = pow(value, -1, prime)
        for r in range(c+1, len(a)):
            scale = a[r][c]*inv % prime
            a[r] = [(x-scale*y) % prime for x, y in zip(a[r], a[c])]
    return answer % prime


def rank_certificate(rows):
    tried = []
    for prime in range(2*123+1, 100_000, 123):
        if DEN % prime == 0 or not fmpz(prime).is_prime():
            continue
        root = next(pow(a, (prime-1)//P, prime) for a in range(2, prime)
                    if pow(a, (prime-1)//P, prime) != 1)
        assert pow(root, P, prime) == 1
        s = next(a for a in range(prime) if (a*a+3) % prime == 0)
        echelon, selected, selected_rows = {}, [], []
        for item in rows:
            original = [evaluate_mod(poly, root, prime)
                        for poly in item["six_integer_trace_Fourier_polynomials"]]
            v = original[:]
            for pivot, old in sorted(echelon.items()):
                scale = v[pivot]
                v = [(x-scale*y) % prime for x, y in zip(v, old)]
            pivot = next((j for j, x in enumerate(v) if x), None)
            if pivot is None:
                continue
            inv = pow(v[pivot], -1, prime)
            echelon[pivot] = [x*inv % prime for x in v]
            selected.append(item["n"])
            selected_rows.append(original)
            if len(echelon) == 6:
                det = determinant_mod(selected_rows, prime)
                assert det
                return {"rank": 6, "prime": prime, "zeta41_mod_prime": root,
                        "sqrt_minus_three_mod_prime": s, "pivot_exponents": selected,
                        "integer_trace_minor": selected_rows, "determinant_mod_prime": det,
                        "normalization": "Removed each nonzero common row factor alpha*s/1722 or 3*alpha/1722; differential also has factor246.",
                        "earlier_specializations": tried}
        tried.append({"prime": prime, "rank": len(echelon)})
    raise ArithmeticError("No certified full-rank specialization in the stated finite range")


def kmul(a, b):
    # Coefficients in Q[s], s^2=-3, used only for the actual a(q) coordinate.
    return (a[0]*b[0]-3*a[1]*b[1], a[0]*b[1]+a[1]*b[0])


def kadd(a, b):
    return (a[0]+b[0], a[1]+b[1])


def coordinate_a():
    # W=Q^123, q=W^2.  a/alpha=(s/12)Q^-41 A(W).
    degree = (BOUND+41)//123
    small = degree//2
    eta_inverse = [1]+[0]*small
    for n in range(1, small+1):
        nxt = [0]*(small+1)
        for i, v in enumerate(eta_inverse):
            for j in range((small-i)//n+1):
                nxt[i+n*j] += v*math.comb(11+j, 11)
        eta_inverse = nxt
    e6 = [1]+[-504*sum(d**5 for d in range(1, n+1) if n % d == 0)
               for n in range(1, small+1)]
    ratio = [sum(e6[i]*eta_inverse[n-i] for i in range(n+1))
             for n in range(small+1)]
    zero = (Fraction(0), Fraction(0))
    target = [zero for _ in range(degree+1)]
    for n, value in enumerate(ratio):
        target[2*n] = (Fraction(value), Fraction(0))
    target[1] = (Fraction(0), Fraction(24))
    A = [(Fraction(1), Fraction(0))]
    for n in range(1, degree+1):
        known = zero
        for i in range(n):
            for j in range(n):
                k = n-i-j
                if 0 <= k < n:
                    known = kadd(known, kmul(kmul(A[i], A[j]), A[k]))
        A.append(tuple((x-y)/3 for x, y in zip(target[n], known)))
    for n in range(degree+1):
        actual = zero
        for i in range(n+1):
            for j in range(n-i+1):
                actual = kadd(actual, kmul(kmul(A[i], A[j]), A[n-i-j]))
        assert actual == target[n]
    return {"formula": "a/alpha=(s/12)*Q^(-41)*(E6(Q^246)/prod(1-Q^(246n))^12+24*s*Q^123)^(1/3)",
            "root_constant": 1, "W": "Q^123", "s_relation": "s^2=-3",
            "A_W_coefficients_Q_plus_Qs": [[str(x), str(y)] for x, y in A],
            "checked_cube_through_W_degree": degree,
            "cusp_leading_coefficient": "alpha*s/12", "at_base_zeta_a": "zeta",
            "at_marked_c1_a": "1"}


def rational_pair(a, c):
    if c == 0:
        return (1, 0)
    g = math.gcd(a, c)
    a, c = a//g, c//g
    if c < 0:
        a, c = -a, -c
    return (a, c)


def period_input(K, beta_powers, c, cells, cycles):
    translations = []
    inv6 = pow(6, -1, P)
    for r in range(1, P):
        k = 6*(r*inv6 % P)
        assert k % 6 == 0 and k % P == r
        translations.append({"r": r, "k_r": k,
                             "A_r": [1, -k, 0, N], "B_r": [4, -4*k, 0, N]})
    coefficients_by_j_h_r = []
    for j in range(6):
        by_h = []
        for h in LABELS:
            by_h.append({"h": h, "numerators_eta":
                         [coefficients(K.auto(K.mul(beta_powers[j], c[r]), h))
                          for r in range(1, P)]})
        coefficients_by_j_h_r.append(by_h)
    endpoints, lookup, rows = [], {}, []
    def number(pair):
        if pair not in lookup:
            lookup[pair] = len(endpoints)
            endpoints.append([str(pair[0]), str(pair[1])])
        return lookup[pair]
    lifts = [[int(x) for x in row] for row in cells["SL2Z_lifts"]]
    for edge in cycles["relative_basis_edges"]:
        positive = cycles["edge_positive_negative_cosets"][edge][0]
        a, b, c0, d = lifts[positive]
        transformed = []
        for item in translations:
            k = item["k_r"]
            transformed.append([
                number(rational_pair(b-k*d, N*d)),
                number(rational_pair(a-k*c0, N*c0)),
                number(rational_pair(4*(b-k*d), N*d)),
                number(rational_pair(4*(a-k*c0), N*c0))])
        rows.append({"relative_edge": edge, "positive_coset": positive,
                     "A0_Ainfinity_B0_Binfinity": transformed})
    return {"translations": translations,
            "period_prefactor": "alpha*s/7",
            "exact_scalar_identity": "246/(41*42)=1/7",
            "trace_weight_numerators_j_h_r": coefficients_by_j_h_r,
            "B_term_factor": "-zeta^2",
            "newform_period": "lambda_h(t)=Omega0^(-1)*integral_infinity_to_t(2*pi*i*f_h(tau)dtau)",
            "rational_endpoints": endpoints, "relative_edge_endpoint_rows": rows,
            "compact_basis_source": EXPECTED["integral-compact-Manin-cycles.json.gz"],
            "closed_cycles_recomputed": False,
            "closed_period_rule": "Use each retained compact Manin coefficient; for each r take lambda(Ainfinity)-lambda(A0)-zeta^2*(lambda(Binfinity)-lambda(B0)); sum with the displayed j,h,r numerator and alpha*s/7.",
            "CM_period_values_computed": False}


def load_topology(directory):
    objects = {}
    for name, digest in EXPECTED.items():
        path = directory/name
        assert sha(path) == digest, name
        objects[name] = read(path)
    cert = objects["p41-original-period-input-certificate.json"]
    assert cert["complete"] and cert["c1_coset"] == 4424
    assert cert["marked_c1_SL2Z"] == [15130, 123, 123, 1]
    assert cert["c1_deck_cosets"] == [4424, 0, 1258]
    assert cert["c0_cosets"] == [2876, 2822, 2823]
    assert cert["genus"] == 400 and cert["compact_rank"] == 800
    assert cert["intersection_determinant"] == "1"
    return objects["original-cosets-and-markings.json.gz"], \
        objects["integral-compact-Manin-cycles.json.gz"]


def compute(out, old):
    started = time.monotonic()
    cells, cycles = load_topology(old)
    K = Field()
    logs, points = finite_points()
    c, toric_norm, generator = toric_vector(K, points)
    a, primary_count = newform(K, logs)
    tame = tame_checks(K)
    beta_powers, rows = q_expansions(K, c, a)
    rank = rank_certificate(rows)
    save(out/"original-p41-Hodge-q-expansions.json.gz", {
        "result": RESULT, "p": P, "full_level": N, "max_exponent_Q": BOUND,
        "Q": "exp(2*pi*i*tau/246)", "eta": "exp(2*pi*i/42)",
        "eta_mod_p": list(GAMMA), "zeta": "eta^14", "xi": "exp(2*pi*i/41)",
        "Phi42": coefficients(K.modulus, 13), "real_Hecke_generator": "beta=eta+eta^-1",
        "positive_embeddings": LABELS, "primary_generator": "a+b*zeta with a=1 mod3,b=0 mod3",
        "theta_direction": "theta(y)=eta^(-log_gamma(bar(y)/y))",
        "newform_coefficients_eta": [coefficients(x) for x in a],
        "torus_average_coefficients_denominator": DEN,
        "torus_average_numerators_eta": [coefficients(x) for x in c],
        "toric_norm_eta": coefficients(toric_norm), "torus_generator_a": generator,
        "original_cusp_function_scale": "alpha; alpha^3=4, alpha>0",
        "q_rows": rows, "q_row_common_denominator": DEN,
        "differential_rule": "omega_j=246*alpha*sum_n(tame_factor*P_jn(xi)/1722)*Q^(n-1)dQ",
        "tame_and_arithmetic_descent": tame, "source_coordinate_a": coordinate_a(),
        "rank_certificate": rank,
    })
    period = period_input(K, beta_powers, c, cells, cycles)
    save(out/"original-p41-Hodge-period-kernel-input.json.gz", period)
    files = [{"file": name, "bytes": (out/name).stat().st_size, "sha256": sha(out/name)}
             for name in ("original-p41-Hodge-q-expansions.json.gz",
                          "original-p41-Hodge-period-kernel-input.json.gz")]
    cert = {"result": RESULT, "complete": True, "p": P, "level": N,
            "source_genus": 400, "Hodge_rank": 6, "max_exponent_Q": BOUND,
            "rank_certificate": rank, "primary_terms": primary_count,
            "original_norm_mod_p": [40, 0], "torus_invariance_verified": True,
            "normalizer_invariance_verified": True, "full_tame_descent_verified": True,
            "retained_topology_hashes": EXPECTED, "topology_recomputed": False,
            "c1_coset": 4424, "c1_raw_transport": "zeta^2",
            "c0_cosets": [2876, 2822, 2823],
            "canonical_scale": "sqrt(-3)", "actual_twist_scale": "alpha*sqrt(-3)",
            "differential_q_parameter_factor": 246, "period_prefactor": "alpha*sqrt(-3)/7",
            "finite_translate_pairs": 40, "relative_edges": len(period["relative_edge_endpoint_rows"]),
            "rational_endpoints": len(period["rational_endpoints"]),
            "CM_period_or_map_or_beta_or_height_computed": False,
            "source_sha256": sha(__file__), "files": files,
            "seconds": time.monotonic()-started}
    save(out/"p41-original-Hodge-input-certificate.json", cert)
    save(out/"core-receipt.json", {"result": RESULT, "complete": True,
        "source_sha256": sha(__file__),
        "certificate_sha256": sha(out/"p41-original-Hodge-input-certificate.json"),
        "CM_period_or_map_or_beta_or_height_computed": False})
    return cert


def main():
    if os.environ.get("GITHUB_ACTIONS") != "true" or \
       os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public":
        raise SystemExit("Exact task arithmetic runs only in the public repository Actions.")
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--retained-topology", type=Path, required=True)
    args = parser.parse_args()
    args.output.mkdir(parents=True, exist_ok=True)
    try:
        cert = compute(args.output, args.retained_topology)
        print(json.dumps({"complete": True, "rank": cert["Hodge_rank"],
                          "seconds": cert["seconds"]}), flush=True)
        return 0
    except BaseException as error:
        save(args.output/"core-receipt.json", {"result": RESULT, "complete": False,
            "source_sha256": sha(__file__), "error": type(error).__name__+": "+str(error),
            "CM_period_or_map_or_beta_or_height_computed": False})
        raise


if __name__ == "__main__":
    sys.exit(main())
