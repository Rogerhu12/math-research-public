#!/usr/bin/env python3
"""R791: original Hom Galois action, CM tangent, and eta divisor inputs.

All new arithmetic runs only in the public repository Actions.  Read the
completed R754 gamma descent and R759 integral maps; do not recompute them.
No polar divisor, eta value, height, or uniformity exclusion is claimed.
"""
import argparse
import json
import os
from pathlib import Path
import sys
import time

import flint
from flint import fmpq, fmpq_mat, fmpz_mat

from R754_original_periods_and_Hom_kernel import QKField, Composer, dp, read, save, sha

RESULT = "R791-original-Hom-Galois-and-eta-inputs"
FINAL = "p41-original-Hom-Galois-and-eta-input-certificate.json"
DIM, M, G = 12, 7, 6
FILES = {
    "p41-original-CM-model-certificate.json":
        "752aa03f9cbe7d3174a7c508fce3043e21e8e85fd087e01acc4bca82a5cbd574",
    "p41-original-period-and-Hom-kernel-certificate.json":
        "da4ef0eeac285da5cf32ad1372155dbb9d03917c18044b81b8236fac6e51107c",
    "R754-gamma-descent.json.gz":
        "cf37105d407ace9df6b86a80d112b58915202bfecfc9e2fd118f4be76af2b1d0",
    "p41-original-integral-period-lattice-and-degree-certificate.json":
        "7c2c611b9a5f43bc3a2a0007bf2cb5dd2fa8d10f133b663dbca0d054e1515de0",
    "R759-original-integral-maps-and-bounded-recovery-input.json.gz":
        "037b56d016d502408173319d76a3067a65dd50250c31bc2225c0fca598396ecc",
    "R748-original-signed-root-and-Hodge-first-jets.json":
        "56418d0cef84554584d8777aed4acb54a2dc57bbf95cc38a1bb42b12140769f3",
}
R754_CORE = "f196cb805d1ca91e8995866032a0a3ec3f96aac06e03b67a7c1f196fff759251"
R759_CORE = "17403f45f74e03e5a138376068e64e54c9bf6b2622a7b91bb178747d407708e0"
R748_CORE = "6b34e4946907cb657cb68ce585e43b8ef31295be36e3f700966daa0d4f133d7c"


def guard():
    if os.environ.get("GITHUB_ACTIONS") != "true" or \
       os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public":
        raise SystemExit("New mathematical execution belongs to public repository Actions.")


def encq(x):
    q = fmpq(x)
    return [str(q.numer()), str(q.denom())]


def encmat(A):
    return [[encq(A[i, j]) for j in range(A.ncols())] for i in range(A.nrows())]


def encint(A):
    return [[str(A[i, j]) for j in range(A.ncols())] for i in range(A.nrows())]


def integer_matrix(A):
    rows = []
    for i in range(A.nrows()):
        row = []
        for j in range(A.ncols()):
            q = fmpq(A[i, j])
            assert q.denom() == 1, "Actual integral Hom action has a denominator"
            row.append(int(q.numer()))
        rows.append(row)
    return fmpz_mat(rows)


def identity(n):
    return fmpz_mat([[int(i == j) for j in range(n)] for i in range(n)])


def conjugate(a):
    # b is the original real field generator; zeta goes to -1-zeta.
    return a.F.elt(a.a-a.b, -a.b)


def flat_vector(values):
    return [v.a[i] for v in values for i in range(M)] + \
           [v.b[i] for v in values for i in range(M)]


def columns(vectors):
    return fmpq_mat([[v[i] for v in vectors] for i in range(len(vectors[0]))])


def independent_rows(A, required=None):
    """Exact row elimination; retained row indices determine a square solve."""
    pivots, selected = {}, []
    for r in range(A.nrows()):
        row = [fmpq(A[r, c]) for c in range(A.ncols())]
        for c in sorted(pivots):
            if row[c]:
                a = row[c]
                row = [x-a*y for x, y in zip(row, pivots[c])]
        if any(row):
            c = next(j for j, value in enumerate(row) if value)
            a = row[c]
            pivots[c] = [x/a for x in row]
            selected.append(r)
            if required is not None and len(selected) == required:
                return selected
    return selected


def row_slice(A, indices):
    return fmpq_mat([[A[r, c] for c in range(A.ncols())] for r in indices])


def matpoly(coefficients, A):
    I = identity(A.nrows())
    answer = fmpz_mat(A.nrows(), A.ncols())
    for a in reversed(coefficients):
        answer = answer*A+int(a)*I
    return answer


def flatten_matrix(A):
    return [A[i, j] for i in range(A.nrows()) for j in range(A.ncols())]


def degree(v, Gram):
    answer = fmpq((v.transpose()*Gram*v)[0, 0], 2)
    assert answer.denom() == 1 and answer >= 0
    return int(answer.numer())


def column_list(v):
    assert v.ncols() == 1
    return [str(v[i, 0]) for i in range(v.nrows())]


def resolve_in_basis(basis, target):
    A = columns([flatten_matrix(x) for x in basis])
    chosen = independent_rows(A, len(basis))
    assert len(chosen) == len(basis)
    B = columns([flatten_matrix(target)])
    answer = row_slice(A, chosen).inv()*row_slice(B, chosen)
    assert A*answer == B
    return [encq(answer[i, 0]) for i in range(len(basis))]


class Job:
    def __init__(self, args):
        self.args, self.out = args, args.output
        self.out.mkdir(parents=True, exist_ok=True)
        self.started = time.monotonic()
        assert flint.__version__ == "0.9.0"
        objects = {}
        for name, digest in FILES.items():
            path = args.inputs/name
            assert sha(path) == digest, "Changed retained input: "+name
            objects[name] = read(path)
            assert objects[name]["complete"] is True
        cert754 = objects["p41-original-period-and-Hom-kernel-certificate.json"]
        cert759 = objects["p41-original-integral-period-lattice-and-degree-certificate.json"]
        maps = objects["R759-original-integral-maps-and-bounded-recovery-input.json.gz"]
        gamma = objects["R754-gamma-descent.json.gz"]
        tangent = objects["R748-original-signed-root-and-Hodge-first-jets.json"]
        assert cert754["configuration"]["source_sha256"] == R754_CORE
        assert cert759["configuration"]["source_sha256"] == R759_CORE
        assert gamma["configuration"] == cert754["configuration"]
        assert maps["configuration"] == cert759["configuration"]
        assert maps["selected_index"] == 4 and maps["selected_degree"] == "1206"
        assert maps["Z_basis_rank"] == DIM and maps["O_K_rank"] == G
        assert gamma["gamma"] == [7, 30]
        assert gamma["both_descents_verified_in_all_280_coordinates"] is True
        assert gamma["sigma_gamma_preserves_original_modulus"] is True
        assert tangent["all_six_Hodge_first_jets_exact"] is True
        phase = tangent["configuration"]["phase_tag"]
        assert phase["source_sha256"] == R748_CORE
        assert phase["fixed_input_sha256"]["hodge"] == \
            "a629d550bd2f3102111bbb58fe707470081e2062da10221ab778fe3ba71b53dd"
        assert phase["fixed_input_sha256"]["hodge_certificate"] == \
            "7fdac934ab8be401afbe793c9dd6d790bba2dc1f39cdbb134fc51748870816be"
        assert tangent["Hodge_basis"] == \
            "omega_j=2*pi*i*alpha*sqrt(-3)*Tr(beta^j*Fraw)d_tau; c1 slash once"
        self.L = QKField(dp(objects["p41-original-CM-model-certificate.json"]["minimal_polynomial"]))
        assert self.L.degree == M
        self.rho = self.L.decode(gamma["sigma_gamma_r_over_r"])
        self.sigma_b = self.L.decode(gamma["sigma_gamma_b"])
        self.sigma = Composer(self.sigma_b)
        self.vectors = [[self.L.decode(value) for value in row] for row in
                       maps["all_twelve_integral_map_differential_vectors_in_original_omega_basis"]]
        assert len(self.vectors) == DIM and all(len(row) == G for row in self.vectors)
        self.Gram = fmpz_mat([[int(x) for x in row] for row in maps["twice_degree_Gram_matrix"]])
        self.J = fmpz_mat([[int(x) for x in row] for row in maps["zeta_action_on_this_Z_basis"]])
        self.jet = [fmpq(x) for x in tangent["coarse_original_Hodge_primitive_first_coefficients"]]
        assert self.jet == [fmpq(43719, 11767), fmpq(200187, 23534), fmpq(162558, 11767),
                            fmpq(687471, 23534), fmpq(659397, 11767), fmpq(2521233, 23534)]
        self.tag = {"result": RESULT, "p": 41, "source_sha256": sha(__file__),
                    "field_helper_sha256": sha(Path(__file__).with_name("R754_original_periods_and_Hom_kernel.py")),
                    "python_flint": flint.__version__, "method_sha256": sha(args.method),
                    "request_sha256": sha(args.request), "retained_inputs": FILES,
                    "original_omega_basis": "R745 omega_0,...,omega_5; no extra c1 phase"}
        assert self.tag["field_helper_sha256"] == R754_CORE

    def save_stage(self, name, payload):
        save(self.out/name, {"result": RESULT, "configuration": self.tag, "complete": True, **payload})
        print(json.dumps({"stage": name, "complete": True, "sha256": sha(self.out/name)}), flush=True)

    def tangents(self):
        values = [sum((v[j]*self.jet[j] for j in range(G)), self.L.zero) for v in self.vectors]
        self.save_stage("R791-original-twelve-CM-tangents.json.gz", {
            "coordinate": "s=a-1 at the original c1", "original_c1_slash_count": 1,
            "actual_L_coefficients_h_i_over_ds_at_c1": [value.encode() for value in values],
            "zero_flags": [not bool(value) for value in values],
            "original_map_index": 4, "original_map_degree": "1206",
            "original_map_c1_tangent_nonzero": bool(values[4]),
            "original_map_y_or_beta_evaluated": False})
        return values

    def operators(self):
        L, sigma, rho, J, Gram = self.L, self.sigma, self.rho, self.J, self.Gram
        assert sigma.rational(L.mod) == 0
        assert rho**6 == self.sigma_b/L.gen
        b, product = L.gen, L.one
        ratios = [L.one]
        for _ in range(M):
            b = sigma(b)
            product = rho*sigma(product)
            ratios.append(product)
        assert b == L.gen and product == L.zeta**2
        assert sigma(conjugate(rho))*rho == 1
        assert conjugate(sigma(conjugate(sigma(L.gen)))) == L.gen
        A = columns([flat_vector(v) for v in self.vectors])
        indices = independent_rows(A, DIM)
        assert len(indices) == DIM
        inverse = row_slice(A, indices).inv()

        def actual_matrix(operation):
            B = columns([flat_vector([operation(x) for x in v]) for v in self.vectors])
            answer = integer_matrix(inverse*row_slice(B, indices))
            assert A*answer == B, "All 84 original field coordinates must agree"
            return answer

        C = actual_matrix(lambda x: rho*sigma(x))
        R = actual_matrix(conjugate)
        assert actual_matrix(lambda x: L.zeta*x) == J
        I, zero = identity(DIM), fmpz_mat(DIM, DIM)
        assert J*J+J+I == zero and R*R == I
        assert C**7 == J**2 and C**21 == I
        Cinv = C**20
        assert R*J*R == J**2 and R*C*R == Cinv and C*J == J*C
        assert all(A0.transpose()*Gram*A0 == Gram for A0 in (C, R, J))
        assert all(abs(A0.det()) == 1 for A0 in (C, R, J))
        phi21 = [1, -1, 0, 1, -1, 0, 1, 0, -1, 1, 0, -1, 1]
        assert matpoly(phi21, C) == zero
        S = C+Cinv
        psi21 = [1, -8, 8, 6, -6, -1, 1]
        assert matpoly(psi21, S) == zero
        basis = [I]+[C**j+Cinv**j for j in range(1, G)]
        assert len(independent_rows(columns([flatten_matrix(x) for x in basis]), G)) == G
        assert len(independent_rows(fmpq_mat(I+R))) == G
        assert len(independent_rows(fmpq_mat(I-R))) == G
        self.save_stage("R791-original-Hom-Galois-matrices.json.gz", {
            "basis": "R759 unchanged twelve LLL integral maps, columns",
            "gamma_matrix": encint(C), "complex_conjugation_matrix": encint(R),
            "zeta_matrix": encint(J), "twice_degree_Gram_matrix": encint(Gram),
            "field_sigma_b": self.sigma_b.encode(), "field_rho": rho.encode(),
            "rho_iterates_zero_through_seven": [a.encode() for a in ratios],
            "all_84_coordinates_verified": True, "all_three_actions_integral_unimodular": True,
            "all_three_actions_preserve_actual_degree_Gram": True,
            "gamma_order": 21, "gamma_seventh_power": "zeta^2",
            "Phi21_ascending": phi21, "real_minimal_polynomial_ascending": psi21,
            "real_and_anti_real_Hom_ranks": [G, G],
            "original_factor": "primitive A_42, represented by the original order-21 gamma",
            "remaining_elliptic_factor_included": False})
        return C, R, basis

    def descent_and_eta_inputs(self, C, R, basis, tangents):
        I, J, Gram = identity(DIM), self.J, self.Gram
        f = fmpz_mat([[int(i == 4)] for i in range(DIM)])
        candidates = []
        if R*f == f:
            candidates.append(("f", f))
        candidates += [("f+c(f)", f+R*f), ("[zeta]f+[zeta^2]c(f)", J*f+J**2*R*f)]
        records = [{"recipe": name, "Hom_coordinates": column_list(v), "degree": str(degree(v, Gram))}
                   for name, v in candidates]
        nonzero = [(degree(v, Gram), i, name, v) for i, (name, v) in enumerate(candidates) if v != fmpz_mat(DIM, 1)]
        assert nonzero
        d, _, name, w = min(nonzero, key=lambda row: (row[0], row[1]))
        assert R*w == w and d > 0
        real_orbit = columns([[int((A*w)[i, 0]) for i in range(DIM)] for A in basis])
        assert len(independent_rows(real_orbit, G)) == G
        assert R*real_orbit == real_orbit
        ws = [C**j*w for j in range(M)]
        assert all(degree(v, Gram) == d for v in ws)

        # H(u,v)=u v^dagger is recovered from the actual degree pairing.
        # a=Tr H=u^t G v, b=Tr(zeta^2 H)=u^t G Jv.
        # Thus H=(2a+b)/3+((a+2b)/3)zeta.  No polarization scale is discarded.
        E = fmpq_mat(DIM, DIM)
        for v in ws:
            arow = v.transpose()*Gram
            brow = (J*v).transpose()*Gram
            alpha = fmpq_mat(2*arow+brow)/3
            beta = fmpq_mat(arow+2*brow)/3
            integer_matrix(alpha)
            integer_matrix(beta)
            E += fmpq_mat(v)*alpha+fmpq_mat(J*v)*beta
        E = integer_matrix(E)
        assert E.det() != 0 and E.transpose()*Gram == Gram*E
        assert all(E*A == A*E for A in (C, R, J))
        d0 = M*d
        assert sum(E[i, i] for i in range(DIM)) == 2*d0
        e_coordinates = resolve_in_basis(basis, E)
        degree_data, trace_zero = [], []
        for j in range(1, G):
            plus = w+C**j*w
            plus_degree = degree(plus, Gram)
            assert plus_degree > 0
            dj = M*(plus_degree-2*d)
            ratio = fmpq(dj, d0)
            H = fmpq_mat(E)*(fmpq_mat(basis[j])-ratio*fmpq_mat(I))
            assert sum(H[i, i] for i in range(DIM)) == 0
            assert H.transpose()*Gram == Gram*H
            trace_zero.append(H)
            degree_data.append({"j": j, "base_degree": str(d),
                "sum_map_degree": str(plus_degree), "degree_Ej": str(dj),
                "degree_E0": str(d0), "degree_zero_coefficient_dj_over_d0": encq(ratio),
                "sum_map_Hom_coordinates": column_list(plus),
                "kappa_times_original_hj_Hom_matrix": encmat(H),
                "eta_polar_divisor_recipe":
                    "(1/3) * sum_tau ( E_(fR_tau+(T^j fR)_tau) - (2+dj/d0)*E_(fR_tau) )"})
        assert len(independent_rows(columns([flatten_matrix(H) for H in trace_zero]), G-1)) == G-1
        real_tangent = sum((int(w[i, 0])*tangents[i] for i in range(DIM)), self.L.zero)
        self.save_stage("R791-original-real-descent-and-eta-basis-inputs.json.gz", {
            "original_index4_is_Lplus_defined": R*f == f,
            "descent_candidates": records, "selected_real_map_recipe": name,
            "selected_real_map_Hom_coordinates": column_list(w), "selected_real_map_degree": str(d),
            "selected_real_map_c1_tangent": real_tangent.encode(),
            "selected_real_map_c1_tangent_nonzero": bool(real_tangent),
            "real_Hom_orbit_basis_columns": encmat(real_orbit),
            "real_Hom_orbit_rank": G, "original_F0_dimension": G-1,
            "kappa_times_vdagger_v_Hom_matrix": encint(E),
            "kappa_times_vdagger_v_in_real_Chebyshev_basis": e_coordinates,
            "degree_E0": str(d0), "degree_zero_basis": degree_data,
            "all_original_F0_directions_covered": True,
            "unknown_original_kappa_set_to_one": False,
            "original_vdagger_v_replaced_by_scalar": False,
            "original_q_alpha_or_c1_changed": False,
            "actual_polar_divisors_computed": False, "actual_eta_classes_computed": False,
            "nonzero_kernel_of_eta_proved": False, "actual_heights_computed": False})
        return {"original_index4_is_Lplus_defined": R*f == f,
                "original_index4_c1_tangent_nonzero": bool(tangents[4]),
                "all_twelve_original_c1_tangents_nonzero": all(bool(x) for x in tangents),
                "selected_real_map_recipe": name, "selected_real_map_degree": str(d),
                "degree_E0": str(d0), "degree_Ej": [r["degree_Ej"] for r in degree_data],
                "sum_map_degrees": [r["sum_map_degree"] for r in degree_data],
                "real_Hom_orbit_rank": G, "original_F0_basis_rank": G-1}

    def run(self):
        tangents = self.tangents()
        C, R, basis = self.operators()
        summary = self.descent_and_eta_inputs(C, R, basis, tangents)
        stages = [{"file": p.name, "bytes": p.stat().st_size, "sha256": sha(p)}
                  for p in sorted(self.out.glob("R791-*.json.gz"))]
        certificate = {"result": RESULT, "configuration": self.tag, "complete": True,
                       **summary, "stages": stages, "seconds": time.monotonic()-self.started,
                       "old_periods_Hom_lattice_or_target_recomputed": False,
                       "actual_eta_polar_divisors_points_heights_or_uniformity_computed": False}
        save(self.out/FINAL, certificate)
        save(self.out/"core-receipt.json", {"result": RESULT, "complete": True,
             "source_sha256": sha(__file__), "certificate_sha256": sha(self.out/FINAL),
             "stages": [{"file": row["file"], "sha256": row["sha256"]} for row in stages]})
        print(json.dumps({"result": RESULT, "complete": True, **summary}), flush=True)


def main():
    guard()
    sys.set_int_max_str_digits(0)
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--inputs", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--method", type=Path, required=True)
    parser.add_argument("--request", type=Path, required=True)
    args = parser.parse_args()
    try:
        Job(args).run()
    except BaseException as error:
        save(args.output/"core-receipt.json", {"result": RESULT, "complete": False,
             "source_sha256": sha(__file__), "error": type(error).__name__+": "+str(error),
             "completed_stages_preserved": True})
        raise


if __name__ == "__main__":
    main()
