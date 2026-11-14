#!/usr/bin/env python3
"""R774: the actual original Hodge function cubed, with complete finite prefix.

Reuse R735, R745, R748, R759 and the actually completed R771 basis.
No newform coefficient, finite toric fiber, period or integral lattice is
recomputed.  All new exact arithmetic belongs to public repository Actions.
"""
import argparse
import gzip
import hashlib
import itertools
import json
import math
import os
from pathlib import Path
import sys
import time

import flint
from flint import fmpq, fmpq_poly, fmpz_mat, fmpz_poly, nmod_mat

RESULT = "R774-original-p41-Hodge-cube"
FINAL = "p41-original-Hodge-cube-certificate.json"
Q_BOUND, QY_BOUND, PACK, CYC = 2460, 820, 121, 40
PACK_LENGTH = PACK*QY_BOUND
DEN = 1722
OLD = {
    "p41-original-CM-model-certificate.json":
        "752aa03f9cbe7d3174a7c508fce3043e21e8e85fd087e01acc4bca82a5cbd574",
    "p41-original-Hodge-input-certificate.json":
        "7fdac934ab8be401afbe793c9dd6d790bba2dc1f39cdbb134fc51748870816be",
    "original-p41-Hodge-q-expansions.json.gz":
        "a629d550bd2f3102111bbb58fe707470081e2062da10221ab778fe3ba71b53dd",
    "R748-extended-newform-coefficients.json.gz":
        "0c7d73a2a2c9202c6a25f343c9357a8b59d9cfc4928a29b5d460dbf84828bff0",
    "p41-original-integral-period-lattice-and-degree-certificate.json":
        "7c2c611b9a5f43bc3a2a0007bf2cb5dd2fa8d10f133b663dbca0d054e1515de0",
    "R759-original-integral-maps-and-bounded-recovery-input.json.gz":
        "037b56d016d502408173319d76a3067a65dd50250c31bc2225c0fca598396ecc",
}
PROOF_SHA = "30006eca29d55c9b2e227f490e0ec9ffe128073f1c49c6dab25d3e532f4db59d"
BASIS_CERT = "p41-original-quotient-RR-basis-certificate.json"
BASIS_STATE = "R771-basis-M6-complete.json.gz"


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


def dp(value):
    return fmpq_poly([int(x) for x in value["numerator"]], int(value["denominator"]))


def ep(value):
    return {"numerator": [str(x) for x in value.numer().coeffs()],
            "denominator": str(value.denom())}


def zcoeff(poly):
    return [str(x) for x in poly.coeffs()]


def mul_s(left, right):
    """Unreduced xi blocks; input degree sums are strictly below PACK."""
    a, b = left
    c, d = right
    ac = a.mul_low(c, PACK_LENGTH)
    bd = b.mul_low(d, PACK_LENGTH)
    cross = (a+b).mul_low(c+d, PACK_LENGTH)-ac-bd
    return ac-3*bd, cross


def reduce_cyclotomic_blocks(poly):
    """Each block has xi degree <=117; use xi^41=1 then Phi41=0."""
    answer = []
    for k in range(QY_BOUND):
        base = PACK*k
        cyclic = [sum(int(poly[base+j]) for j in range(r, PACK, 41))
                  for r in range(41)]
        answer.extend(v-cyclic[40] for v in cyclic[:40])
    return answer


class OriginalL:
    """The unchanged R735 Q[b] with the original zeta adjoined."""
    def __init__(self, encoded_modulus):
        self.mod = dp(encoded_modulus)
        assert self.mod.degree() == 7 and self.mod[7] == 1

    def decode(self, value):
        return dp(value[0]) % self.mod, dp(value[1]) % self.mod

    def zero(self):
        return fmpq_poly([]), fmpq_poly([])

    def add(self, left, right):
        return left[0]+right[0], left[1]+right[1]

    def scale(self, value, scalar):
        return value[0]*scalar, value[1]*scalar

    def multiply(self, left, right):
        a, b = left
        c, d = right
        ac, bd = a*c, b*d
        return (ac-bd) % self.mod, (a*d+b*c-bd) % self.mod

    def encode(self, value):
        return [ep(value[0]), ep(value[1])]


class Job:
    def __init__(self, args):
        assert flint.__version__ == "0.9.0"
        self.args, self.out = args, args.output
        self.out.mkdir(parents=True, exist_ok=True)
        self.started = time.monotonic()
        objects = {}
        for name, digest in OLD.items():
            path = args.inputs/name
            assert sha(path) == digest, name
            objects[name] = read(path)
        self.hodge = objects["original-p41-Hodge-q-expansions.json.gz"]
        self.extended = objects["R748-extended-newform-coefficients.json.gz"]
        self.maps = objects["R759-original-integral-maps-and-bounded-recovery-input.json.gz"]
        self.model = objects["p41-original-CM-model-certificate.json"]
        hc = objects["p41-original-Hodge-input-certificate.json"]
        dc = objects["p41-original-integral-period-lattice-and-degree-certificate.json"]
        assert hc["complete"] and hc["Hodge_rank"] == 6 and hc["c1_coset"] == 4424
        assert hc["rank_certificate"]["pivot_exponents"] == [1, 4, 7, 13, 16, 19]
        assert hc["rank_certificate"]["determinant_mod_prime"] == 407
        assert self.hodge["p"] == 41 and self.hodge["full_level"] == 246
        assert self.hodge["max_exponent_Q"] == 800
        assert self.hodge["eta_mod_p"] == [7, 30] and self.hodge["zeta"] == "eta^14"
        assert self.hodge["torus_average_coefficients_denominator"] == DEN
        assert self.hodge["q_row_common_denominator"] == DEN
        assert self.extended["complete"] and self.extended["cutoff"] == 4096
        assert self.extended["configuration"]["fixed_input_sha256"]["hodge"] == \
            OLD["original-p41-Hodge-q-expansions.json.gz"]
        assert self.extended["coefficients_eta"][:801] == self.hodge["newform_coefficients_eta"]
        assert len(self.extended["coefficients_eta"]) == 4097
        assert self.model["complete"] and self.model["exact_F_of_b_zero"]
        assert self.model["original_b_not_a_replacement_twist"]
        assert dc["complete"] and dc["selected_index"] == 4 and dc["selected_degree"] == "1206"
        assert self.maps["complete"] and self.maps["selected_index"] == 4
        assert self.maps["selected_degree"] == "1206" and self.maps["c1_coset"] == 4424
        assert self.maps["Z_basis_rank"] == 12 and self.maps["O_K_rank"] == 6
        self.L = OriginalL(self.model["minimal_polynomial"])
        all_vectors = self.maps["all_twelve_integral_map_differential_vectors_in_original_omega_basis"]
        assert len(all_vectors) == 12 and all(len(v) == 6 for v in all_vectors)
        self.encoded_v = all_vectors[4]
        self.v = [self.L.decode(value) for value in self.encoded_v]
        assert any(a or b for a, b in self.v)
        assert sha(args.proof) == PROOF_SHA
        assert sha(args.inputs/BASIS_CERT) == args.basis_certificate_sha256
        assert sha(args.inputs/BASIS_STATE) == args.basis_state_sha256
        self.bc = read(args.inputs/BASIS_CERT)
        self.bs = read(args.inputs/BASIS_STATE)
        assert self.bc["complete"] and self.bc["M2_dimension"] == 146
        assert self.bc["M6_dimension"] == 694 and self.bc["M12_dimension"] == 1514
        assert self.bc["configuration"]["source_sha256"] == args.basis_core_sha256
        assert self.bc["configuration"]["xi41_mod_ell"] == 538
        assert self.bc["configuration"]["sqrt_minus_three_mod_ell"] == 98
        assert self.bc["configuration"]["prime"] == 739
        assert self.bs["complete"] and self.bs["configuration"] == self.bc["configuration"]
        assert self.bs["rank"] == 694 and len(self.bs["basis"]) == 694
        match = [x for x in self.bc["stages"] if x["file"] == BASIS_STATE]
        assert len(match) == 1 and match[0]["sha256"] == args.basis_state_sha256
        self.tag = {
            "result": RESULT, "source_sha256": sha(__file__), "python_flint": flint.__version__,
            "retained_input_sha256": OLD, "R772_proof_sha256": PROOF_SHA,
            "R771_basis_certificate_sha256": args.basis_certificate_sha256,
            "R771_basis_state_sha256": args.basis_state_sha256,
            "R771_core_sha256": args.basis_core_sha256,
            "selected_map_index": 4, "selected_map_degree": "1206",
            "Q_bound": Q_BOUND, "qY_bound": QY_BOUND, "original_newform_prefix_bound": 4096,
            "Q_parameter": "exp(2*pi*i*tau/246), original reference coset0",
            "qY_parameter": "Q^3", "H_normalization": "H=alpha*F/1722; alpha^3=4",
            "cube_normalization": "H^3=4*F^3/1722^3",
            "field": "M=L(xi41), L=Q(b,zeta), s=1+2*zeta",
            "coefficient_basis": "b^i and s*b^i, 0<=i<7; xi^r, 0<=r<40",
            "unreduced_cyclotomic_pack": PACK,
            "c1_phase_applied_a_second_time": False,
        }
        self.triples = list(itertools.combinations_with_replacement(range(6), 3))
        assert len(self.triples) == 56

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
                          "seconds": time.monotonic()-self.started}), flush=True)
        return value

    def fourier_rows(self):
        name = "R774-original-six-Fourier-rows-through-2460"
        old = self.cached(name)
        if old and old["complete"]:
            return old
        phi = fmpz_poly(self.hodge["Phi42"])
        assert phi.degree() == 12
        eta = fmpz_poly([0, 1])
        powers = [fmpz_poly([1])]
        for _ in range(1, 42):
            powers.append((powers[-1]*eta) % phi)
        beta = powers[1]+powers[41]
        beta_powers = [fmpz_poly([1])]
        for _ in range(5):
            beta_powers.append((beta_powers[-1]*beta) % phi)
        # Matrix traces in the fixed old power basis; no finite toric fiber.
        traces = [sum(int(powers[(j+i) % 42][i]) for i in range(12)) for j in range(12)]
        assert traces[0] == 12
        c = [fmpz_poly(row) for row in self.hodge["torus_average_numerators_eta"]]
        assert len(c) == 41 and not c[0]
        linear = []
        for j in range(6):
            by_r = []
            for r in range(41):
                w = (beta_powers[j]*c[r]) % phi
                row = []
                for k in range(12):
                    value = (w*powers[k]) % phi
                    row.append(sum(int(value[i])*traces[i] for i in range(12)))
                by_r.append(row)
            linear.append(by_r)
        rows = list(self.hodge["q_rows"]) if old is None else old["q_rows"]
        done = 800 if old is None else old["completed_through_Q"]
        assert rows[:len(self.hodge["q_rows"])] == self.hodge["q_rows"]
        inv6 = pow(6, -1, 41)
        coefficients = self.extended["coefficients_eta"]
        for n in range(done+1, Q_BOUND+1):
            an = coefficients[n]
            if any(an):
                assert n % 3 == 1 and (n % 2 == 1 or n % 4 == 0)
                six = []
                for j in range(6):
                    values = [0]*41
                    for r in range(1, 41):
                        full = sum(int(an[k])*linear[j][r][k] for k in range(12))
                        assert full % 2 == 0
                        values[-n*r*inv6 % 41] += full//2
                    six.append([str(x-values[40]) for x in values[:40]])
                rows.append({"n": n, "tame_factor": "s" if n % 2 else "3",
                             "six_integer_trace_Fourier_polynomials": six})
            if (n-800) % 64 == 0 or n == Q_BOUND:
                self.store(name, {"complete": n == Q_BOUND, "completed_through_Q": n,
                    "q_rows": rows, "newform_coefficients_recomputed": False,
                    "old_Fourier_rows_recomputed": False, "old_Q_bound": 800,
                    "reused_newform_Q_bound": 4096,
                    "normalization": "F_j=sum(s*P_jn for odd n, 3*P_jn for 4|n)*Q^n"})
        return self.cached(name)

    def cusp_order(self, rows):
        name = "R774-actual-cusp-order-and-leading-coefficient"
        old = self.cached(name)
        if old and old["complete"]:
            return old
        source_s = (fmpq_poly([1]), fmpq_poly([2]))
        leading, exponent = None, None
        tested = []
        for row in rows:
            n = row["n"]
            if n > 19:
                break
            P = row["six_integer_trace_Fourier_polynomials"]
            value = []
            for r in range(CYC):
                coordinate = self.L.zero()
                for j in range(6):
                    coordinate = self.L.add(coordinate, self.L.scale(self.v[j], int(P[j][r])))
                if row["tame_factor"] == "s":
                    coordinate = self.L.multiply(coordinate, source_s)
                else:
                    assert row["tame_factor"] == "3"
                    coordinate = self.L.scale(coordinate, 3)
                value.append(coordinate)
            nonzero = any(a or b for a, b in value)
            tested.append({"Q_exponent": n, "selected_exact_coefficient_nonzero": nonzero})
            if nonzero:
                exponent, leading = n, value
                break
        assert exponent is not None and 1 <= exponent <= 19 and exponent % 3 == 1
        return self.store(name, {"complete": True, "actual_cusp_ramification_e": exponent,
            "first_nonzero_F_exponent_Q": exponent, "tested_supported_exponents": tested,
            "F_leading_coefficient_by_xi_power": [self.L.encode(v) for v in leading],
            "coefficient_field": "M=L(xi41), original b and zeta",
            "H_leading_coefficient": "alpha/1722 times saved F leading coefficient",
            "primitive_leading_coefficient": "alpha/(7*e) times saved F leading coefficient",
            "no_new_choice_of_target_translation": True})

    def packed_functions(self, rows):
        name = "R774-six-original-integer-packed-functions"
        old = self.cached(name)
        if old and old["complete"]:
            return [(fmpz_poly([int(x) for x in row["real"]]),
                     fmpz_poly([int(x) for x in row["s"]])) for row in old["functions"]]
        data = [[[0]*PACK_LENGTH for _ in range(2)] for _ in range(6)]
        for row in rows:
            n = row["n"]
            assert n % 3 == 1
            k = (n-1)//3
            if k >= QY_BOUND:
                continue
            s_part = int(row["tame_factor"] == "s")
            factor = 1 if s_part else 3
            for j, coefficients in enumerate(row["six_integer_trace_Fourier_polynomials"]):
                assert len(coefficients) == CYC
                for r, coefficient in enumerate(coefficients):
                    data[j][s_part][PACK*k+r] = factor*int(coefficient)
        functions = [(fmpz_poly(row[0]), fmpz_poly(row[1])) for row in data]
        self.store(name, {"complete": True, "pack_block": PACK,
            "max_xi_degree_before_products": 39, "max_G_exponent": QY_BOUND-1,
            "definition": "F_j(Q)=Q*G_j(qY), G_j=real+s*imaginary",
            "functions": [{"real": zcoeff(a), "s": zcoeff(b)} for a, b in functions]})
        return functions

    def products(self, functions):
        pairs = {}
        for i in range(6):
            for j in range(i, 6):
                name = "R774-packed-pair-"+str(i)+"-"+str(j)
                old = self.cached(name)
                if old and old["complete"]:
                    pair = (fmpz_poly([int(x) for x in old["real"]]),
                            fmpz_poly([int(x) for x in old["s"]]))
                else:
                    pair = mul_s(functions[i], functions[j])
                    self.store(name, {"complete": True, "indices": [i, j],
                        "real": zcoeff(pair[0]), "s": zcoeff(pair[1]),
                        "max_xi_degree": 78, "no_cyclotomic_block_carry": True})
                pairs[i, j] = pair
        paths = []
        for index, (i, j, k) in enumerate(self.triples):
            name = "R774-cubic-monomial-"+str(index).zfill(2)
            old = self.cached(name)
            if not (old and old["complete"]):
                a, b = mul_s(pairs[i, j], functions[k])
                real = reduce_cyclotomic_blocks(a)
                imag = reduce_cyclotomic_blocks(b)
                self.store(name, {"complete": True, "indices": [i, j, k],
                    "G_exponent_range_exclusive": [0, QY_BOUND], "xi_basis_degree": CYC,
                    "real_coefficients_flat_qY_xi": [str(x) for x in real],
                    "s_coefficients_flat_qY_xi": [str(x) for x in imag],
                    "coefficient_ring": "Z[s,xi41], s^2=-3, Phi41(xi41)=0",
                    "unreduced_max_xi_degree": 117, "pack_block": PACK,
                    "complete_low_product_computed": True})
            paths.append(self.path(name))
        return paths

    def scalars(self):
        name = "R774-original-L-cubic-scalars"
        old = self.cached(name)
        if old and old["complete"]:
            return old
        products = {}
        for i in range(6):
            for j in range(i, 6):
                products[i, j] = self.L.multiply(self.v[i], self.v[j])
        scalars = []
        for i, j, k in self.triples:
            multiplicity = 1 if i == k else (3 if i == j or j == k else 6)
            scalar = self.L.scale(self.L.multiply(products[i, j], self.v[k]),
                                 fmpq(4*multiplicity, DEN**3))
            # A+B*zeta=(A-B/2)+(B/2)*s, with the fixed s=1+2*zeta.
            real, imag = scalar[0]-scalar[1]/2, scalar[1]/2
            scalars.append((real, imag))
        rational = [[fmpq(0)]*112 for _ in range(14)]
        for j, (a, b) in enumerate(scalars):
            for i in range(7):
                rational[i][2*j], rational[i][2*j+1] = a[i], -3*b[i]
                rational[7+i][2*j], rational[7+i][2*j+1] = b[i], a[i]
        # Do not inflate every b-coordinate to one enormous common numerator.
        # Retain its exact rational scale once, and multiply primitive rows.
        integer, row_scales = [], []
        for row in rational:
            local_denominator = 1
            for value in row:
                local_denominator = math.lcm(local_denominator, int(value.denom()))
            values = [int((value*local_denominator).numer()) for value in row]
            content = 0
            for value in values:
                content = math.gcd(content, abs(value))
            if content:
                scale = fmpq(content, local_denominator)
                integer.append([value//content for value in values])
            else:
                scale = fmpq(0)
                integer.append(values)
            row_scales.append([str(scale.numer()), str(scale.denom())])
        denominator = 1
        for numerator, local_denominator in row_scales:
            denominator = math.lcm(denominator, int(local_denominator))
        v739, reduced_denominator = 0, denominator
        while reduced_denominator % 739 == 0:
            reduced_denominator //= 739
            v739 += 1
        d = int(self.model["minimal_polynomial"]["denominator"])
        v2, v3, residual = 0, 0, d
        while residual % 2 == 0:
            residual //= 2
            v2 += 1
        while residual % 3 == 0:
            residual //= 3
            v3 += 1
        return self.store(name, {"complete": True, "triples": [list(x) for x in self.triples],
            "selected_original_v_in_omega_basis": self.encoded_v,
            "scalar_for_triple": "4*multinomial*v_i*v_j*v_k/1722^3",
            "row_basis": ["b^"+str(i) for i in range(7)]+["s*b^"+str(i) for i in range(7)],
            "column_basis": "real,s parts of each of the 56 saved monomials",
            "common_denominator": str(denominator),
            "common_denominator_739_valuation": v739,
            "rational_row_scales": row_scales,
            "primitive_integer_matrix": [[str(x) for x in row] for row in integer],
            "original_b_minimal_polynomial": self.model["minimal_polynomial"],
            "original_model_denominator_two_valuation": v2,
            "original_model_denominator_three_valuation": v3,
            "original_model_denominator_residual": str(residual)})

    def combine(self, paths, scalars, order):
        # The 56*2 short integer series contain no large L coefficients.
        rows = []
        for path in paths:
            value = read(path)
            assert value["configuration"] == self.tag and value["complete"]
            rows.append([int(x) for x in value["real_coefficients_flat_qY_xi"]])
            rows.append([int(x) for x in value["s_coefficients_flat_qY_xi"]])
        assert len(rows) == 112 and all(len(row) == QY_BOUND*CYC for row in rows)
        C = fmpz_mat([[int(x) for x in row] for row in scalars["primitive_integer_matrix"]])
        scalar_sha = sha(self.path("R774-original-L-cubic-scalars"))
        files, first_nonzero = [], None
        for first in range(1, QY_BOUND+1, 32):
            last = min(QY_BOUND+1, first+32)
            name = "R774-exact-H3-qY-"+str(first).zfill(4)+"-"+str(last-1).zfill(4)
            old = self.cached(name)
            if old and old["complete"]:
                block = old
                assert block["first_exponent"] == first and block["last_exponent_exclusive"] == last
                assert block["rational_row_scale_stage_sha256"] == scalar_sha
            else:
                start, end = (first-1)*CYC, (last-1)*CYC
                source = fmpz_mat([row[start:end] for row in rows])
                target = C*source
                block = self.store(name, {"complete": True, "first_exponent": first,
                    "last_exponent_exclusive": last,
                    "rational_row_scale_stage_sha256": scalar_sha,
                    "coefficient_layout": "14 rows (b^i,s*b^i), columns (qY exponent,xi^r), r0..39",
                    "integer_numerators": [[str(target[i, j]) for j in range(target.ncols())]
                                           for i in range(14)],
                    "normalization": "multiply each integer row by its saved rational_row_scale; H^3, factor4/1722^3 and qY shift included"})
            for n in range(first, last):
                offset = (n-first)*CYC
                nonzero = any(int(block["integer_numerators"][i][offset+r]) != 0
                              for i in range(14) for r in range(CYC))
                if nonzero and first_nonzero is None:
                    first_nonzero = n
            files.append(self.path(name))
        assert first_nonzero == order["actual_cusp_ramification_e"]
        return files

    def finite_M6_comparison(self, paths, scalars):
        name = "R774-cleared-H3-in-the-actual-M6-basis-mod739"
        old = self.cached(name)
        if old and old["complete"]:
            return old
        prime, xi, s = 739, 538, 98
        powers = [pow(xi, r, prime) for r in range(CYC)]
        target = [[0]*7 for _ in range(QY_BOUND+1)]
        denominator = int(scalars["common_denominator"])
        multipliers = [(int(a)*(denominator//int(b))) % prime
                       for a, b in scalars["rational_row_scales"]]
        for path in paths:
            block = read(path)
            assert block["configuration"] == self.tag and block["complete"]
            first, last = block["first_exponent"], block["last_exponent_exclusive"]
            rows = block["integer_numerators"]
            for n in range(first, last):
                offset = (n-first)*CYC
                for i in range(7):
                    target[n][i] = sum(
                        (multipliers[i]*int(rows[i][offset+r])+s*multipliers[7+i]*int(rows[7+i][offset+r]))*powers[r]
                        for r in range(CYC)) % prime
        matrix_rows = []
        for row in self.bs["basis"]:
            data = row["coefficients_mod_ell"]
            matrix_rows.append(data[:QY_BOUND+1]+[0]*max(0, QY_BOUND+1-len(data)))
        original = nmod_mat(matrix_rows, prime).transpose()
        columns = self.bs["actual_nonzero_minor"]["coefficient_exponents"]
        assert len(columns) == 694 and all(0 <= n <= QY_BOUND for n in columns)
        A = nmod_mat([[original[n, j] for j in range(694)] for n in columns], prime)
        B = nmod_mat([target[n] for n in columns], prime)
        coordinates = A.solve(B)
        assert original*coordinates == nmod_mat(target, prime)
        return self.store(name, {"complete": True, "prime": prime,
            "xi41_mod_prime": xi, "sqrt_minus_three_mod_prime": s,
            "target": "common_denominator * H^3, not an unjustified divided reduction",
            "common_denominator_739_valuation": scalars["common_denominator_739_valuation"],
            "common_denominator": scalars["common_denominator"],
            "basis_state_sha256": self.args.basis_state_sha256,
            "basis_minor": self.bs["actual_nonzero_minor"],
            "coordinate_rows_by_basis_then_b_power":
                [[int(coordinates[i, j]) for j in range(7)] for i in range(694)],
            "all_821_coefficients_verified_for_all_seven_b_coordinates": True,
            "characteristic_zero_M6_coordinates_inferred_from_reduction": False})

    def finish(self, rows, order, scalars, paths, finite):
        stages = [{"file": p.name, "bytes": p.stat().st_size, "sha256": sha(p)}
                  for p in sorted(self.out.glob("R774-*.json.gz"))]
        certificate = {"result": RESULT, "configuration": self.tag, "complete": True,
            "p": 41, "selected_original_map_index": 4, "selected_original_map_degree": "1206",
            "original_c1_coset": 4424, "original_newform_prefix_reused_through": 4096,
            "newform_coefficients_recomputed": False,
            "old_Fourier_rows_through_800_recomputed": False,
            "original_six_Fourier_rows_generated_through_Q": Q_BOUND,
            "six_row_count": len(rows),
            "actual_cusp_ramification_e": order["actual_cusp_ramification_e"],
            "original_H_normalization": "H=alpha*F/1722, alpha^3=4",
            "exact_H_cubed_generated_through_qY": QY_BOUND,
            "qY_constant_coefficient_zero": True, "exact_H_cubed_nonzero": True,
            "exact_coefficient_field": "M=L(xi41), [M:Q]=560; L=K(b)",
            "exact_coefficient_basis_order": "b^0..b^6,s*b^0..s*b^6, then xi^0..xi^39",
            "exact_rows_stored_with_primitive_integers_and_rational_row_scales": True,
            "rational_row_scale_stage": "R774-original-L-cubic-scalars.json.gz",
            "common_denominator_bit_length": int(scalars["common_denominator"]).bit_length(),
            "common_denominator_739_valuation": scalars["common_denominator_739_valuation"],
            "H3_blocks": [{"file": p.name, "sha256": sha(p)} for p in paths],
            "original_model_denominator_two_valuation": scalars["original_model_denominator_two_valuation"],
            "original_model_denominator_three_valuation": scalars["original_model_denominator_three_valuation"],
            "original_model_denominator_residual": scalars["original_model_denominator_residual"],
            "M6_line_bundle_degree": 820, "full_prefix_uniquely_identifies_original_H3": True,
            "mod739_cleared_H3_coordinates_in_actual_M6_basis_verified": True,
            "all_821_coefficients_verified_for_all_seven_b_coordinates":
                finite["all_821_coefficients_verified_for_all_seven_b_coordinates"],
            "characteristic_zero_M6_basis_coordinates_computed": False,
            "actual_y_map_beta_or_height_computed": False,
            "no_Neron_Manin_or_KS_scale_changed": True,
            "old_model_topology_periods_or_lattice_recomputed": False,
            "stages": stages, "seconds": time.monotonic()-self.started}
        save(self.out/FINAL, certificate)
        save(self.out/"core-receipt.json", {"result": RESULT, "complete": True,
            "source_sha256": sha(__file__), "certificate_sha256": sha(self.out/FINAL),
            "actual_cusp_ramification_e": order["actual_cusp_ramification_e"],
            "exact_H3_prefix_through_qY": QY_BOUND, "old_newform_coefficients_recomputed": False})
        return certificate


def main():
    if os.environ.get("GITHUB_ACTIONS") != "true" or \
       os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public":
        raise SystemExit("New exact arithmetic belongs to the public repository Actions.")
    sys.set_int_max_str_digits(0)
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--inputs", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--proof", type=Path, required=True)
    parser.add_argument("--basis-core-sha256", required=True)
    parser.add_argument("--basis-certificate-sha256", required=True)
    parser.add_argument("--basis-state-sha256", required=True)
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
            save(args.output/"core-receipt.json", {"result": RESULT, "complete": True,
                "source_sha256": sha(__file__), "certificate_sha256": sha(final),
                "reused_complete": True})
            return
        rows = job.fourier_rows()["q_rows"]
        order = job.cusp_order(rows)
        functions = job.packed_functions(rows)
        products = job.products(functions)
        scalars = job.scalars()
        blocks = job.combine(products, scalars, order)
        finite = job.finite_M6_comparison(blocks, scalars)
        cert = job.finish(rows, order, scalars, blocks, finite)
        print(json.dumps({"result": RESULT, "complete": True,
            "actual_e": cert["actual_cusp_ramification_e"],
            "exact_H3_through_qY": QY_BOUND}), flush=True)
    except BaseException as error:
        save(args.output/"core-receipt.json", {"result": RESULT, "complete": False,
            "source_sha256": sha(__file__), "error": type(error).__name__+": "+str(error),
            "completed_and_partial_stages_preserved": True})
        raise


if __name__ == "__main__":
    main()
