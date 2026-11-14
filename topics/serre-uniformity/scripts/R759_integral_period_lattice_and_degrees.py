#!/usr/bin/env python3
"""R759: the complete original integral-period lattice and exact map degrees.

Read the successful R754 periods and unchanged R738 intersection matrix.
No old CM model, finite vector, period, topology or Hom kernel is recomputed.
All mathematical execution is restricted to the public repository Actions.
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
from flint import fmpq, fmpq_mat, fmpz_mat

RESULT = "R759-original-integral-period-lattice-and-map-degrees"
CYCLES_SHA = "d4dcbac16cc24cefd378fc7afea02fcd34b8043d255c1e84407ff7d21bd257cf"
PERIOD_FILE = "R754-all-original-closed-period-verification.json.gz"
CERT_FILE = "p41-original-period-and-Hom-kernel-certificate.json"
CYCLES_FILE = "integral-compact-Manin-cycles.json.gz"
DIM, CHAINS, GENUS = 12, 800, 400


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def read(path):
    data = Path(path).read_bytes()
    if str(path).endswith(".gz"):
        data = gzip.decompress(data)
    return json.loads(data)


def save(path, obj):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    data = (json.dumps(obj, sort_keys=True, separators=(",", ":"))+"\n").encode()
    if path.suffix == ".gz":
        data = gzip.compress(data, mtime=0)
    temporary = path.with_name(path.name+".tmp")
    temporary.write_bytes(data)
    temporary.replace(path)


def eq(q):
    return [str(q.numer()), str(q.denom())]


def dq(pair):
    return fmpq(int(pair[0]), int(pair[1]))


def encode_q(M):
    return [[eq(M[i, j]) for j in range(M.ncols())] for i in range(M.nrows())]


def decode_q(rows):
    return fmpq_mat([[dq(x) for x in row] for row in rows])


def encode_z(M):
    return [[str(M[i, j]) for j in range(M.ncols())] for i in range(M.nrows())]


def decode_z(rows):
    return fmpz_mat([[int(x) for x in row] for row in rows])


def integral_matrix(M):
    rows = []
    for i in range(M.nrows()):
        row = []
        for j in range(M.ncols()):
            q = fmpq(M[i, j])
            assert q.denom() == 1, "An allegedly integral coordinate has a denominator"
            row.append(int(q.numer()))
        rows.append(row)
    return fmpz_mat(rows)


def identity(n):
    return fmpz_mat([[int(i == j) for j in range(n)] for i in range(n)])


def decode_poly(poly, length=7):
    denominator = int(poly["denominator"])
    numerators = [int(x) for x in poly["numerator"]]
    assert len(numerators) <= length
    return [fmpq(numerators[i] if i < len(numerators) else 0, denominator)
            for i in range(length)]


def encode_poly(coefficients):
    denominator = 1
    for x in coefficients:
        denominator = math.lcm(denominator, int(x.denom()))
    numerators = [int((x*denominator).numer()) for x in coefficients]
    while numerators and numerators[-1] == 0:
        numerators.pop()
    return {"numerator": [str(x) for x in numerators], "denominator": str(denominator)}


def gram_schmidt(G):
    """Exact LDL^t of a positive Gram matrix; no real approximations."""
    n = G.nrows()
    mu = [[fmpq(0) for _ in range(n)] for _ in range(n)]
    norms = [fmpq(0) for _ in range(n)]
    for i in range(n):
        for j in range(i):
            numerator = fmpq(G[i, j])
            for k in range(j):
                numerator -= mu[i][k]*mu[j][k]*norms[k]
            mu[i][j] = numerator/norms[j]
        norms[i] = fmpq(G[i, i])-sum(
            (mu[i][j]*mu[i][j]*norms[j] for j in range(i)), fmpq(0))
        assert norms[i] > 0, "The original degree form is not positive definite"
        mu[i][i] = fmpq(1)
    return mu, norms


def nearest_integer(q):
    # floor(q+1/2), with an explicit deterministic tie convention.
    return (2*int(q.numer())+int(q.denom()))//(2*int(q.denom()))


class Job:
    def __init__(self, args):
        assert flint.__version__ == "0.9.0"
        self.args = args
        self.output = args.output
        self.output.mkdir(parents=True, exist_ok=True)
        self.started = time.monotonic()
        cert_path = args.inputs/CERT_FILE
        period_path = args.inputs/PERIOD_FILE
        cycles_path = args.inputs/CYCLES_FILE
        assert sha(cycles_path) == CYCLES_SHA
        cert = read(cert_path)
        assert cert["complete"] and cert["p"] == 41 and cert["source_genus"] == GENUS
        assert cert["configuration"]["source_sha256"] == args.r754_core_sha256
        assert cert["constraint_rank"] == 36 and cert["kernel_dimension_over_K"] == 6
        assert cert["all_800_chains_verified_for_all_six_kernel_vectors"]
        matches = [x for x in cert["stages"] if x["file"] == PERIOD_FILE]
        assert len(matches) == 1 and sha(period_path) == matches[0]["sha256"]
        self.periods = read(period_path)
        assert self.periods["configuration"] == cert["configuration"]
        assert self.periods["complete"] and self.periods["kernel_dimension_over_K"] == 6
        assert self.periods["all_800_original_chains_verified_for_each_of_six_vectors"]
        self.cycles = read(cycles_path)
        assert self.cycles["p"] == 41 and self.cycles["genus"] == GENUS
        assert self.cycles["intersection_determinant"] == "1"
        assert len(self.cycles["compact_cycles_in_oriented_Manin_edges"]) == CHAINS
        self.tag = {"result": RESULT, "source_sha256": sha(__file__),
                    "python_flint": flint.__version__,
                    "R754_core_sha256": args.r754_core_sha256,
                    "R754_certificate_sha256": sha(cert_path),
                    "R754_verified_periods_sha256": sha(period_path),
                    "R738_cycles_sha256": CYCLES_SHA,
                    "period_coordinate_order": "1,zeta; Im(zeta)>0",
                    "Q_direction_order": "h0,...,h5,zeta*h0,...,zeta*h5",
                    "intersection": "Omega_ij=gamma_i dot gamma_j; R759 dual-spine proof",
                    "degree_sign": "-a^t Omega^{-1} b"}

    def path(self, name):
        return self.output/(name+".json.gz")

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

    def rational_periods(self):
        original = self.periods["periods_in_K"]
        assert len(original) == CHAINS and all(len(row) == 6 for row in original)
        rows = []
        denominator = 1
        for row in original:
            a = [dq(value[0]) for value in row]
            b = [dq(value[1]) for value in row]
            # zeta(a+b*zeta)=-b+(a-b)*zeta.
            real = a+[-x for x in b]
            zeta = b+[x-y for x, y in zip(a, b)]
            rows.extend([real, zeta])
            for q in real+zeta:
                denominator = math.lcm(denominator, int(q.denom()))
        P = fmpq_mat(rows)
        integer = integral_matrix(P*denominator)
        return P, integer, denominator

    def saturated_lattice(self, P, integer, denominator):
        finished = self.cached("R759-saturated-integral-period-lattice")
        if finished and finished["complete"]:
            return (decode_q(finished["coefficient_basis_columns"]),
                    decode_z(finished["integer_period_rows_interleaved_1_zeta"]),
                    decode_z(finished["zeta_action_on_integral_basis"]))
        name = "R759-complete-period-row-HNF"
        prior = self.cached(name)
        done = 0 if prior is None else prior["processed_rows"]
        H = fmpz_mat(0, DIM) if prior is None else decode_z(prior["nonzero_HNF_rows"])
        steps = [] if prior is None else prior["unimodular_steps"]
        assert 0 <= done <= 2*CHAINS
        if not (prior and prior["complete"]):
            for first in range(done, 2*CHAINS, 32):
                last = min(first+32, 2*CHAINS)
                old_rank = H.nrows()
                stacked_rows = [[H[i, j] for j in range(DIM)] for i in range(old_rank)]
                stacked_rows += [[integer[i, j] for j in range(DIM)] for i in range(first, last)]
                stacked = fmpz_mat(stacked_rows)
                all_h, U = stacked.hnf(transform=True)
                assert U*stacked == all_h and abs(U.det()) == 1
                assert all_h.is_hnf()
                nonzero = [[all_h[i, j] for j in range(DIM)] for i in range(all_h.nrows())
                           if any(all_h[i, j] for j in range(DIM))]
                assert len(nonzero) <= DIM
                H = fmpz_mat(nonzero) if nonzero else fmpz_mat(0, DIM)
                steps.append({"first_original_row": first, "last_original_row_exclusive": last,
                              "previous_rank": old_rank, "new_rank": H.nrows(),
                              "unimodular_transformation": encode_z(U)})
                self.store(name, {"complete": last == 2*CHAINS,
                                  "common_denominator": str(denominator), "processed_rows": last,
                                  "nonzero_HNF_rows": encode_z(H), "unimodular_steps": steps})
        assert H.nrows() == H.ncols() == DIM and H.det() != 0
        # H consists of ROW lattice generators.  Its inverse therefore acts
        # on coefficient COLUMNS: H*x/D is integral iff x=D*H^{-1}*n.
        coefficient_basis = H.inv()*denominator
        assert H*coefficient_basis == identity(DIM)*denominator
        integral_periods = integral_matrix(P*coefficient_basis)
        J = fmpz_mat(DIM, DIM)
        for j in range(6):
            J[j, j+6] = -1
            J[j+6, j] = 1
            J[j+6, j+6] = -1
        zeta_action = integral_matrix(coefficient_basis.inv()*J*coefficient_basis)
        assert zeta_action*zeta_action+zeta_action+identity(DIM) == fmpz_mat(DIM, DIM)
        assert zeta_action.det() == 1
        self.store("R759-saturated-integral-period-lattice", {
            "complete": True, "rank_over_Z": DIM, "rank_over_O_K": 6,
            "common_denominator": str(denominator), "row_HNF": encode_z(H),
            "coefficient_basis_columns": encode_q(coefficient_basis),
            "integer_period_rows_interleaved_1_zeta": encode_z(integral_periods),
            "zeta_action_on_integral_basis": encode_z(zeta_action),
            "all_1600_rows_used": True, "all_HNF_steps_unimodular": True,
            "complete_integral_period_lattice_not_a_selected_submodule": True})
        return coefficient_basis, integral_periods, zeta_action

    def degree_form(self, periods, zeta_action):
        name = "R759-original-map-degree-form"
        prior = self.cached(name)
        if prior and prior["complete"]:
            return decode_z(prior["twice_degree_Gram_matrix"])
        a = fmpz_mat([[periods[2*i, j] for j in range(DIM)] for i in range(CHAINS)])
        b = fmpz_mat([[periods[2*i+1, j] for j in range(DIM)] for i in range(CHAINS)])
        omega = fmpz_mat(self.cycles["intersection_matrix"])
        assert omega.nrows() == omega.ncols() == CHAINS and omega == -omega.transpose()
        # New right hand sides only: no inverse matrix or topology recomputation.
        Yq = omega.solve(b)
        assert omega*Yq == b
        Y = integral_matrix(Yq)
        C = -(a.transpose()*Y)
        S = C+C.transpose()
        assert S == S.transpose() and all(S[i, i] % 2 == 0 for i in range(DIM))
        _, norms = gram_schmidt(S)
        assert zeta_action.transpose()*S*zeta_action == S
        self.store(name, {"complete": True, "intersection_solve_Omega_Y_equals_b": encode_z(Y),
                         "twice_degree_Gram_matrix": encode_z(S),
                         "exact_LDL_positive_diagonal": [eq(x) for x in norms],
                         "positive_definite": True, "zeta_isometry": True,
                         "degree_formula": "d(n)=n^t S n/2=-a(n)^t Omega^{-1} b(n)",
                         "old_topology_or_intersection_not_recomputed": True})
        return S

    def short_basis(self, S):
        name = "R759-exact-degree-LLL"
        prior = self.cached(name)
        if prior and prior["complete"]:
            return (decode_z(prior["unimodular_rows"]),
                    decode_z(prior["twice_degree_Gram_matrix"]))
        U = identity(DIM) if prior is None else decode_z(prior["unimodular_rows"])
        k = 1 if prior is None else prior["next_index"]
        iterations = 0 if prior is None else prior["iterations"]
        delta = fmpq(3, 4)
        if not (prior and prior["complete"]):
            while k < DIM:
                for j in range(k-1, -1, -1):
                    G = U*S*U.transpose()
                    mu, norms = gram_schmidt(G)
                    q = nearest_integer(mu[k][j])
                    if q:
                        for c in range(DIM):
                            U[k, c] -= q*U[j, c]
                G = U*S*U.transpose()
                mu, norms = gram_schmidt(G)
                if norms[k] >= (delta-mu[k][k-1]**2)*norms[k-1]:
                    k += 1
                else:
                    for c in range(DIM):
                        old = U[k, c]
                        U[k, c] = U[k-1, c]
                        U[k-1, c] = old
                    k = max(1, k-1)
                iterations += 1
                if iterations % 20 == 0 or k == DIM:
                    self.store(name, {"complete": False, "next_index": k,
                                     "iterations": iterations, "unimodular_rows": encode_z(U)})
        assert abs(U.det()) == 1
        G = U*S*U.transpose()
        mu, norms = gram_schmidt(G)
        assert all(abs(mu[i][j]) <= fmpq(1, 2) for i in range(DIM) for j in range(i))
        assert all(norms[k] >= (delta-mu[k][k-1]**2)*norms[k-1] for k in range(1, DIM))
        self.store(name, {"complete": True, "next_index": DIM, "iterations": iterations,
                         "unimodular_rows": encode_z(U), "twice_degree_Gram_matrix": encode_z(G),
                         "delta": [3, 4], "eta": [1, 2], "all_LLL_inequalities_exact": True,
                         "global_shortest_vector_claimed": False})
        return U, G

    def map_inputs(self, P, coefficient_basis, integral_periods, zeta_action, U, G):
        finished = self.cached("R759-original-integral-maps-and-bounded-recovery-input")
        if finished and finished["complete"]:
            return finished
        new_basis = coefficient_basis*U.transpose()
        new_periods = integral_periods*U.transpose()
        assert integral_matrix(P*new_basis) == new_periods
        new_zeta = integral_matrix(U.transpose().inv()*zeta_action*U.transpose())
        assert new_zeta.transpose()*G*new_zeta == G
        old = self.periods["six_L_differential_vectors"]
        assert len(old) == 6 and all(len(row) == 6 for row in old)
        old_coefficients = [[(decode_poly(value[0]), decode_poly(value[1])) for value in row]
                            for row in old]
        maps = []
        for k in range(DIM):
            vector = []
            for j in range(6):
                first, second = [fmpq(0)]*7, [fmpq(0)]*7
                for ell in range(6):
                    x, y = new_basis[ell, k], new_basis[ell+6, k]
                    a, b = old_coefficients[ell][j]
                    for t in range(7):
                        first[t] += x*a[t]-y*b[t]
                        second[t] += x*b[t]+y*(a[t]-b[t])
                vector.append([encode_poly(first), encode_poly(second)])
            maps.append(vector)
        degrees = [int(G[i, i])//2 for i in range(DIM)]
        assert all(G[i, i] == 2*degrees[i] and degrees[i] > 0 for i in range(DIM))
        selected = min(range(DIM), key=lambda i: (degrees[i], i))
        d = degrees[selected]
        # The unchanged a-map has degree 4920/6=820.  Every cusp is a pole,
        # so D=m*(a)_0 is an effective rational divisor away from the q cusp.
        m = (2*d+GENUS+819)//820
        divisor_degree = 820*m
        M0 = divisor_degree+2*d
        result = {"complete": True, "Z_basis_rank": DIM, "O_K_rank": 6,
                  "all_twelve_integral_map_differential_vectors_in_original_omega_basis": maps,
                  "coefficient_basis_columns_in_original_h_zeta_h_directions": encode_q(new_basis),
                  "all_integer_periods_interleaved_1_zeta": encode_z(new_periods),
                  "twice_degree_Gram_matrix": encode_z(G),
                  "zeta_action_on_this_Z_basis": encode_z(new_zeta),
                  "degrees": [str(x) for x in degrees], "selected_index": selected,
                  "selected_degree": str(d), "selection": "least degree among the exact LLL basis",
                  "global_minimum_degree_claimed": False,
                  "target": "original R735 C/L: y^2=x^3+b; omega_C=dx/(2y)",
                  "base_point": "original c0, with f(c0)=O", "c1_coset": 4424,
                  "RR_divisor": "D=m*(a)_0, j=6912*a^3*(1-a^3)",
                  "RR_m": str(m), "RR_divisor_degree": str(divisor_degree),
                  "RR_M0": str(M0), "RR_basis_series_through": str(M0+2*d),
                  "RR_differential_series_through": str(M0+3*d),
                  "ramification_bound_at_q_cusp": str(d),
                  "actual_RR_basis_or_rational_functions_computed": False,
                  "actual_beta_coordinates_or_height_computed": False,
                  "no_quotient_Manin_or_KS_scale_assumed_a_41_unit": True}
        self.store("R759-original-integral-maps-and-bounded-recovery-input", result)
        return result


def main():
    if os.environ.get("GITHUB_ACTIONS") != "true" or \
       os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public":
        raise SystemExit("Exact mathematical execution belongs to the public repository Actions.")
    sys.set_int_max_str_digits(0)
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--inputs", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--r754-core-sha256", required=True)
    args = parser.parse_args()
    job = Job(args)
    try:
        final = args.output/"p41-original-integral-period-lattice-and-degree-certificate.json"
        if final.exists():
            completed = read(final)
            assert completed["configuration"] == job.tag and completed["complete"]
            for stage in completed["stages"]:
                assert sha(args.output/stage["file"]) == stage["sha256"]
            save(args.output/"core-receipt.json", {"result": RESULT, "complete": True,
                 "source_sha256": sha(__file__), "certificate_sha256": sha(final),
                 "reused_complete": True})
            return
        P, integer, denominator = job.rational_periods()
        coefficient_basis, integral_periods, zeta_action = job.saturated_lattice(P, integer, denominator)
        S = job.degree_form(integral_periods, zeta_action)
        U, G = job.short_basis(S)
        actual = job.map_inputs(P, coefficient_basis, integral_periods, zeta_action, U, G)
        stages = [{"file": p.name, "bytes": p.stat().st_size, "sha256": sha(p)}
                  for p in sorted(args.output.glob("R759-*.json.gz"))]
        certificate = {"result": RESULT, "configuration": job.tag, "complete": True,
             "p": 41, "source_genus": GENUS, "unchanged_original_closed_chains": CHAINS,
             "full_integral_period_lattice_Z_rank": DIM, "O_K_rank": 6,
             "all_1600_rational_period_rows_used": True,
             "HNF_unimodular_steps_verified": True, "zeta_stability_verified": True,
             "original_intersection_solve_verified": True,
             "positive_definite_degree_form_verified": True,
             "exact_LLL_inequalities_verified": True,
             "degree_formula": "-a^t Omega^{-1} b, coordinates 1,zeta",
             "degrees_of_LLL_Z_basis": actual["degrees"],
             "selected_index": actual["selected_index"], "selected_degree": actual["selected_degree"],
             "global_minimum_degree_claimed": False,
             "RR_divisor": actual["RR_divisor"], "RR_m": actual["RR_m"],
             "RR_M0": actual["RR_M0"],
             "RR_basis_series_through": actual["RR_basis_series_through"],
             "RR_differential_series_through": actual["RR_differential_series_through"],
             "old_mathematical_results_recomputed": False,
             "actual_rational_functions_beta_or_height_computed": False,
             "stages": stages, "seconds": time.monotonic()-job.started}
        save(final, certificate)
        save(args.output/"core-receipt.json", {"result": RESULT, "complete": True,
             "source_sha256": sha(__file__), "certificate_sha256": sha(final),
             "selected_degree": actual["selected_degree"]})
        print(json.dumps({"result": RESULT, "complete": True,
                          "selected_degree": actual["selected_degree"]}), flush=True)
    except BaseException as error:
        save(args.output/"core-receipt.json", {"result": RESULT, "complete": False,
             "source_sha256": sha(__file__), "error": type(error).__name__+": "+str(error),
             "completed_stages_preserved": True})
        raise


if __name__ == "__main__":
    main()
