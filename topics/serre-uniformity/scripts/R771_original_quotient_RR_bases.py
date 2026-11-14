#!/usr/bin/env python3
"""R771: certify explicit original quotient RR basis recipes modulo a good prime.

Only public repository Actions may execute this new arithmetic.  Every output
basis element is a characteristic-zero Eisenstein trace/product recipe; a
nonzero finite-field minor certifies its independence, not a guessed lift.
Old topology, periods, Hom lattices and map degrees are read, not recomputed.
"""
import argparse
import gzip
import hashlib
import json
import math
import os
from pathlib import Path
import sys
import time

import flint
from flint import nmod_mat, nmod_poly

RESULT = "R771-p41-original-quotient-RR-bases"
FINAL = "p41-original-quotient-RR-basis-certificate.json"
P, N, ELL, XI41, SQRTM3 = 41, 82, 739, 538, 98
MAX_EXP = 1640
HODGE_SHA = "7fdac934ab8be401afbe793c9dd6d790bba2dc1f39cdbb134fc51748870816be"
DEGREE_SHA = "7c2c611b9a5f43bc3a2a0007bf2cb5dd2fa8d10f133b663dbca0d054e1515de0"
DIMENSIONS = {1: 146, 2: 418, 3: 690, 4: 962, 5: 1234, 6: 1506}


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def read(path):
    data = Path(path).read_bytes()
    if str(path).endswith(".gz"):
        data = gzip.decompress(data)
    return json.loads(data)


def save(path, value):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    data = (json.dumps(value, sort_keys=True, separators=(",", ":"))+"\n").encode()
    if path.suffix == ".gz":
        data = gzip.compress(data, mtime=0)
    temporary = path.with_name(path.name+".tmp")
    temporary.write_bytes(data)
    temporary.replace(path)


def mm(a, b, modulus):
    return tuple(x % modulus for x in
                 (a[0]*b[0]+a[1]*b[2], a[0]*b[1]+a[1]*b[3],
                  a[2]*b[0]+a[3]*b[2], a[2]*b[1]+a[3]*b[3]))


def action(v, g):
    a, b = v
    return (a*g[0]+b*g[2]) % N, (a*g[1]+b*g[3]) % N


def neg(v, modulus=N):
    return tuple((-x) % modulus for x in v)


def coefficients(f, length=None):
    row = [int(x) for x in f.coeffs()]
    if length is not None:
        row = row[:length]+[0]*max(0, length-len(row))
    return row


def product(a, b):
    return a.mul_low(b, MAX_EXP+1)


def record(recipe, series):
    return {"recipe": recipe, "coefficients_mod_ell": coefficients(series)}


def decode_record(row):
    return row["recipe"], nmod_poly(row["coefficients_mod_ell"], ELL)


def coefficient_rows(records, bound):
    rows = []
    for row in records:
        values = row["coefficients_mod_ell"]
        rows.append(values[:bound+1]+[0]*max(0, bound+1-len(values)))
    return rows


def independent_rows(records, bound):
    """Select original rows via pivot columns of the transpose; no guessed recipes."""
    matrix = nmod_mat(coefficient_rows(records, bound), ELL).transpose()
    reduced, rank = matrix.rref()
    pivots = []
    for i in range(rank):
        pivot = next(j for j in range(reduced.ncols()) if reduced[i, j])
        pivots.append(pivot)
    assert pivots == sorted(set(pivots))
    return [records[j] for j in pivots], pivots


def actual_minor(records, bound):
    matrix = nmod_mat(coefficient_rows(records, bound), ELL)
    reduced, rank = matrix.rref()
    assert rank == len(records)
    columns = [next(j for j in range(reduced.ncols()) if reduced[i, j])
               for i in range(rank)]
    minor = nmod_mat([[matrix[i, j] for j in columns] for i in range(rank)], ELL)
    determinant = int(minor.det())
    assert determinant != 0
    return {"coefficient_exponents": columns, "determinant_mod_ell": determinant,
            "rows": rank, "columns": rank, "prime": ELL,
            "original_recipe_rows_not_reduced_combinations": True}


class Job:
    def __init__(self, args):
        assert flint.__version__ == "0.9.0"
        self.args, self.out = args, args.output
        self.out.mkdir(parents=True, exist_ok=True)
        assert sha(args.hodge_certificate) == HODGE_SHA
        assert sha(args.degree_certificate) == DEGREE_SHA
        hodge, degree = read(args.hodge_certificate), read(args.degree_certificate)
        assert hodge["complete"] and hodge["Hodge_rank"] == 6
        assert hodge["rank_certificate"]["pivot_exponents"] == [1, 4, 7, 13, 16, 19]
        assert hodge["rank_certificate"]["determinant_mod_prime"] == 407
        assert hodge["rank_certificate"]["prime"] == ELL
        assert hodge["rank_certificate"]["zeta41_mod_prime"] == XI41
        assert hodge["rank_certificate"]["sqrt_minus_three_mod_prime"] == SQRTM3
        assert degree["complete"] and degree["selected_index"] == 4
        assert degree["selected_degree"] == "1206"
        assert degree["full_integral_period_lattice_Z_rank"] == 12
        self.xi82 = (-pow(XI41, 21, ELL)) % ELL
        assert pow(XI41, 41, ELL) == 1 and XI41 != 1
        assert pow(self.xi82, 82, ELL) == 1
        assert pow(self.xi82, 41, ELL) != 1 and pow(self.xi82, 2, ELL) != 1
        assert SQRTM3*SQRTM3 % ELL == ELL-3
        self.xi_powers = [pow(self.xi82, i, ELL) for i in range(N)]
        self.tag = {
            "result": RESULT, "source_sha256": sha(__file__),
            "python_flint": flint.__version__, "R767_proof_sha256": sha(args.proof),
            "R745_hodge_certificate_sha256": HODGE_SHA,
            "R759_degree_certificate_sha256": DEGREE_SHA,
            "p": P, "level": N, "prime": ELL, "xi41_mod_ell": XI41,
            "xi82_mod_ell": self.xi82, "sqrt_minus_three_mod_ell": SQRTM3,
            "max_exponent_qY": MAX_EXP,
            "parameter": "qY=Q^3=exp(2*pi*i*tau/82), original reference coset0",
            "E1_normalization": "Zywina Lemma4.7, c0 and both signed divisor sums",
            "trace_normalization": "one_half sum over actual H82, equivalently H82/{+-I}",
            "target_group": "mod2 <C>, mod41 original normalizer of tau=zeta",
        }
        self.started = time.monotonic()

    def path(self, name):
        return self.out/(name+".json.gz")

    def cached(self, name):
        path = self.path(name)
        if not path.exists():
            return None
        value = read(path)
        assert value["configuration"] == self.tag
        return value

    def store(self, name, value):
        value = dict(value, configuration=self.tag)
        save(self.path(name), value)
        print(json.dumps({"stage": name, "complete": value.get("complete", False),
                          "rank": value.get("rank"),
                          "seconds": time.monotonic()-self.started}), flush=True)
        return value

    def group(self):
        name = "R771-original-level82-Eisenstein-label-group"
        old = self.cached(name)
        if old and old["complete"]:
            return old
        identity = (1, 0, 0, 1)
        C = (0, 1, 1, 1)
        H2 = {identity, C, mm(C, C, 2)}
        reflection = (-1 % P, -1 % P, 0, 1)
        plus, minus = set(), set()
        for a in range(P):
            for b in range(P):
                matrix = (a, -b % P, b, (a+b) % P)
                determinant = (a*a+a*b+b*b) % P
                if determinant == 1:
                    plus.add(matrix)
                elif determinant == P-1:
                    minus.add(matrix)
        assert len(plus) == len(minus) == 42
        H41 = plus | {mm(reflection, a, P) for a in minus}
        assert len(H41) == 84
        H = set()
        for g2 in H2:
            for gp in H41:
                H.add(tuple(gp[i]+P*((g2[i]-gp[i]) % 2) for i in range(4)))
        assert len(H) == 252 and all((g[0]*g[3]-g[1]*g[2]) % N == 1 for g in H)
        assert neg(identity) in H and all(neg(g) in H for g in H)
        half = sorted({min(g, neg(g)) for g in H})
        assert len(half) == 126
        labels = {(a, b) for a in range(N) for b in range(N)
                  if (a % P, b % P) != (0, 0)}
        assert len(labels) == 6720
        remaining, representatives = set(labels), []
        while remaining:
            first = min(remaining)
            orbit = {action(first, g) for g in H}
            assert orbit <= remaining and len(orbit) in (84, 252)
            representatives.append(first)
            remaining.difference_update(orbit)
        beta = sorted({min(v, neg(v)) for v in labels})
        assert len(representatives) == 40 and len(beta) == 3360
        return self.store(name, {
            "complete": True, "H2": sorted(H2), "H41": sorted(H41),
            "H82": sorted(H), "H82_mod_center": half,
            "first_label_orbit_representatives": representatives,
            "second_labels_mod_sign": beta,
            "original_tame_C": C, "all_group_determinants_one_mod82": True,
            "old_R738_cosets_or_topology_recomputed": False})

    def eisenstein(self):
        """All E1 series, row checkpoints.  Reuse a completed row verbatim."""
        table = [[None]*N for _ in range(N)]
        inv2, invN = pow(2, -1, ELL), pow(N, -1, ELL)
        for a in range(N):
            name = "R771-Eisenstein-row-"+str(a).zfill(2)
            old = self.cached(name)
            if old and old["complete"]:
                assert old["first_label_coordinate"] == a
                rows = old["series_by_second_coordinate"]
                assert len(rows) == N
            else:
                rows = []
                for b in range(N):
                    coeff = [0]*(MAX_EXP+1)
                    if a == 0:
                        if b:
                            z = self.xi_powers[b]
                            coeff[0] = inv2*(1+z)*pow((1-z) % ELL, -1, ELL) % ELL
                    else:
                        coeff[0] = (inv2-a*invN) % ELL
                    for sign, residue, phase in ((1, a, b), (-1, (-a) % N, (-b) % N)):
                        first = residue if residue else N
                        for m in range(first, MAX_EXP+1, N):
                            for n in range(1, MAX_EXP//m+1):
                                index = m*n
                                coeff[index] = (coeff[index]+sign*self.xi_powers[(phase*n) % N]) % ELL
                    rows.append(coefficients(nmod_poly(coeff, ELL)))
                self.store(name, {"complete": True, "first_label_coordinate": a,
                                  "series_by_second_coordinate": rows,
                                  "last_exponent": MAX_EXP})
            table[a] = [nmod_poly(row, ELL) for row in rows]
        assert not table[0][0] and not table[0][41]
        assert not table[41][0] and not table[41][41]
        for a in range(N):
            for b in range(N):
                assert table[(-a) % N][(-b) % N] == -table[a][b]
        return table

    def select(self, name, initial, recipes, evaluate, dimension, bound, batch_size):
        old = self.cached(name)
        if old and old["complete"]:
            assert old["rank"] == dimension and old["coefficient_bound"] == bound
            return old
        basis = list(initial) if old is None else old["basis"]
        processed = 0 if old is None else old["processed_candidates"]
        assert len(basis) <= dimension
        pending = []
        last_index = processed

        def flush(count):
            nonlocal basis
            before = len(basis)
            combined = basis+pending
            selected, pivots = independent_rows(combined, bound)
            assert pivots[:before] == list(range(before))
            assert len(selected) <= dimension, "Rank exceeded the proved characteristic-zero dimension"
            basis = selected
            self.store(name, {"complete": False, "rank": len(basis),
                              "coefficient_bound": bound, "processed_candidates": count,
                              "basis": basis})

        if len(basis) < dimension:
            for index, recipe in enumerate(recipes):
                if index < processed:
                    continue
                pending.append(record(recipe, evaluate(recipe)))
                last_index = index+1
                if len(pending) == batch_size:
                    flush(last_index)
                    pending = []
                    if len(basis) == dimension:
                        break
            if pending and len(basis) < dimension:
                flush(last_index)
        assert len(basis) == dimension, \
            "The actual modular-form candidates did not reach the required rank at this prime"
        minor = actual_minor(basis, bound)
        return self.store(name, {"complete": True, "rank": dimension,
                                "coefficient_bound": bound,
                                "processed_candidates": last_index,
                                "basis": basis, "actual_nonzero_minor": minor,
                                "characteristic_zero_independence_certified_by_unit_reduction": True})

    def weight_two(self, group, table):
        alpha = [tuple(x) for x in group["first_label_orbit_representatives"]]
        beta = [tuple(x) for x in group["second_labels_mod_sign"]]
        H = [tuple(x) for x in group["H82_mod_center"]]
        total = len(alpha)*len(beta)
        assert total == 134400 and math.gcd(65537, total) == 1

        def recipes():
            for count in range(total):
                index = (65537*count+17) % total
                a, b = divmod(index, len(beta))
                yield {"kind": "E1_pair_trace", "lambda": list(alpha[a]),
                       "mu": list(beta[b]), "candidate_permutation_index": count}

        def evaluate(recipe):
            first, second = recipe["lambda"], recipe["mu"]
            ans = nmod_poly([], ELL)
            for g in H:
                a, b = action(first, g)
                c, d = action(second, g)
                ans += product(table[a][b], table[c][d])
            return ans.truncate(MAX_EXP+1)

        return self.select("R771-basis-M2", [], recipes(), evaluate, 146, 273, 24)

    def powers(self, first):
        spaces = {1: first}
        polynomials = {1: [decode_record(x)[1] for x in first["basis"]]}
        for degree in range(2, 7):
            previous = polynomials[degree-1]

            def recipes():
                for i in range(146):
                    for j in range(len(previous)):
                        if degree == 2 and j < i:
                            continue
                        yield {"kind": "product", "left_power": 1, "left_index": i,
                               "right_power": degree-1, "right_index": j}

            def evaluate(recipe):
                return product(polynomials[1][recipe["left_index"]],
                               previous[recipe["right_index"]])

            value = self.select("R771-basis-power-"+str(degree), [], recipes(), evaluate,
                                DIMENSIONS[degree], 272*degree, 128)
            spaces[degree] = value
            polynomials[degree] = [decode_record(x)[1] for x in value["basis"]]
        return spaces, polynomials

    def level_one(self):
        name = "R771-original-E4-E6-eta12-and-RR-denominators"
        old = self.cached(name)
        if old and old["complete"]:
            return {key: nmod_poly(old[key], ELL) for key in ("E4", "E6", "eta12")}
        e4, e6 = [0]*(MAX_EXP+1), [0]*(MAX_EXP+1)
        e4[0] = e6[0] = 1
        for divisor in range(1, MAX_EXP//N+1):
            for n in range(divisor, MAX_EXP//N+1, divisor):
                e4[N*n] = (e4[N*n]+240*pow(divisor, 3, ELL)) % ELL
                e6[N*n] = (e6[N*n]-504*pow(divisor, 5, ELL)) % ELL
        E4, E6 = nmod_poly(e4, ELL), nmod_poly(e6, ELL)
        eta = nmod_poly([1], ELL)
        for m in range(1, (MAX_EXP-41)//N+1):
            coeff = [0]*(min(12*N*m, MAX_EXP-41)+1)
            for r in range(13):
                exponent = N*m*r
                if exponent <= MAX_EXP-41:
                    coeff[exponent] = ((-1)**r*math.comb(12, r)) % ELL
            eta = eta.mul_low(nmod_poly(coeff, ELL), MAX_EXP-41+1)
        eta = eta.left_shift(41).truncate(MAX_EXP+1)
        delta = product(eta, eta)
        assert (product(product(E4, E4), E4)-product(E6, E6)).truncate(MAX_EXP+1) == \
            delta*1728
        denominator_half = eta*pow(2, -1, ELL)-E6*(SQRTM3*pow(144, -1, ELL) % ELL)
        denominator = product(denominator_half, denominator_half)
        assert int(denominator[0]) == -pow(6912, -1, ELL) % ELL
        self.store(name, {"complete": True, "E4": coefficients(E4),
                         "E6": coefficients(E6), "eta12": coefficients(eta),
                         "t_eta12": coefficients(denominator_half),
                         "t_squared_Delta": coefficients(denominator),
                         "eta12_squared_equals_Delta_verified": True,
                         "denominator_constant_mod_ell": int(denominator[0]),
                         "denominator_characteristic_zero":
                            "(eta_Dedekind^12/2-sqrt(-3)*E6/144)^2"})
        return {"E4": E4, "E6": E6, "eta12": eta}

    def augment(self, spaces, polys, basic):
        outputs = {}
        for weight, base_power, first_rank, bound in ((6, 3, 690, 820), (12, 6, 1506, 1640)):
            initial = [record({"kind": "power_basis", "power": base_power, "index": i}, series)
                       for i, series in enumerate(polys[base_power])]
            layers = [(1, "E4", 1)] if weight == 6 else \
                     [(1, "E4", 4), (2, "E6", 3), (3, "E4E6", 1)]
            current = initial
            rank = first_rank
            for level, factor_name, power in layers:
                factor = product(basic["E4"], basic["E6"]) if factor_name == "E4E6" else basic[factor_name]

                def recipes():
                    for i in range(len(polys[power])):
                        yield {"kind": "elliptic_layer_product", "factor": factor_name,
                               "power": power, "index": i}

                def evaluate(recipe):
                    return product(factor, polys[power][recipe["index"]])

                rank += 2
                value = self.select("R771-basis-M"+str(weight)+"-layer-"+str(level),
                                    current, recipes(), evaluate, rank, bound, 16)
                current = value["basis"]
            if weight == 6:
                last = [
                    {"kind": "level_one", "name": "E6"},
                    {"kind": "level_one", "name": "eta12"},
                ]

                def evaluate(recipe):
                    return basic[recipe["name"]]
            else:
                last = [
                    {"kind": "level_one_product", "first": "E6", "second": "E6"},
                    {"kind": "level_one_product", "first": "E6", "second": "eta12"},
                ]

                def evaluate(recipe):
                    return product(basic[recipe["first"]], basic[recipe["second"]])
            rank += 2
            expected = 694 if weight == 6 else 1514
            assert rank == expected
            outputs[weight] = self.select("R771-basis-M"+str(weight)+"-complete", current,
                                           iter(last), evaluate, expected, bound, 2)
        return outputs


def main():
    if os.environ.get("GITHUB_ACTIONS") != "true" or \
       os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public":
        raise SystemExit("New exact arithmetic belongs to the public repository Actions.")
    sys.set_int_max_str_digits(0)
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--hodge-certificate", type=Path, required=True)
    parser.add_argument("--degree-certificate", type=Path, required=True)
    parser.add_argument("--proof", type=Path, required=True)
    args = parser.parse_args()
    args.output.mkdir(parents=True, exist_ok=True)
    try:
        job = Job(args)
        final = args.output/FINAL
        if final.exists():
            cert = read(final)
            assert cert["complete"] and cert["configuration"] == job.tag
            for row in cert["stages"]:
                assert sha(args.output/row["file"]) == row["sha256"]
            save(args.output/"core-receipt.json", {
                "result": RESULT, "complete": True, "source_sha256": sha(__file__),
                "certificate_sha256": sha(final), "reused_complete": True})
            return
        group = job.group()
        table = job.eisenstein()
        first = job.weight_two(group, table)
        spaces, polys = job.powers(first)
        basic = job.level_one()
        full = job.augment(spaces, polys, basic)
        stages = [{"file": path.name, "bytes": path.stat().st_size, "sha256": sha(path)}
                  for path in sorted(args.output.glob("R771-*.json.gz"))]
        certificate = {
            "result": RESULT, "configuration": job.tag, "complete": True,
            "p": P, "source_quotient_genus": 127, "level": N, "prime": ELL,
            "H82_order": len(group["H82"]), "effective_trace_order": len(group["H82_mod_center"]),
            "M2_dimension": 146, "M2_actual_minor": first["actual_nonzero_minor"],
            "M2_exact_seeds": [row["recipe"] for row in first["basis"]],
            "power_basis_dimensions": {str(k): spaces[k]["rank"] for k in range(1, 7)},
            "M6_dimension": full[6]["rank"], "M6_actual_minor": full[6]["actual_nonzero_minor"],
            "M12_dimension": full[12]["rank"], "M12_actual_minor": full[12]["actual_nonzero_minor"],
            "exact_RR_basis_recipe_field": "Q(xi82) subset original M=K(U)",
            "RR_divisor_for_selected_actual_map": "2*(t)_0, degree1640",
            "RR_basis_formula": "F_i/(eta_Dedekind^12/2-sqrt(-3)*E6/144)^2",
            "selected_actual_map_index": 4, "selected_actual_map_degree": "1206",
            "cusp_ramification_bound_from_unchanged_R745": 19,
            "required_exact_RR_basis_series_through_qY": 2846,
            "required_original_h_over_dQ_series_through_Q": 8557,
            "actual_characteristic_zero_RR_basis_recipes_certified": True,
            "characteristic_zero_basis_coefficients_reconstructed_numerically": False,
            "full_required_characteristic_zero_q_series_computed": False,
            "actual_y_map_beta_or_height_computed": False,
            "old_topology_periods_Hom_lattice_or_degrees_recomputed": False,
            "M6_694_minus_degree_not_asserted_without_nonspeciality": True,
            "stages": stages, "seconds": time.monotonic()-job.started}
        save(final, certificate)
        save(args.output/"core-receipt.json", {
            "result": RESULT, "complete": True, "source_sha256": sha(__file__),
            "certificate_sha256": sha(final),
            "M2_dimension": 146, "M6_dimension": 694, "M12_dimension": 1514})
        print(json.dumps({"result": RESULT, "complete": True, "M2": 146,
                          "M6": 694, "M12": 1514}), flush=True)
    except BaseException as error:
        save(args.output/"core-receipt.json", {
            "result": RESULT, "complete": False, "source_sha256": sha(__file__),
            "error": type(error).__name__+": "+str(error), "completed_stages_preserved": True})
        raise


if __name__ == "__main__":
    main()
