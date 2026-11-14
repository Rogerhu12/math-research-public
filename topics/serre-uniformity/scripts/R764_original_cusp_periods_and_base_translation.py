#!/usr/bin/env python3
"""R764 v2 reconstruction: original cusp periods and c0 translation.

Read complete R754/R759 certificates and the unchanged R738 cusp tree.
No old model, topology, period, Hom kernel or lattice is recomputed.
All new exact arithmetic runs only in the public repository Actions.
"""
import argparse
from collections import deque
import gzip
import hashlib
import json
import os
from pathlib import Path
import sys
import time

import flint
from flint import fmpq, fmpq_poly

RESULT = "R764-original-cusp-periods-and-base-translation"
FINAL = "p41-original-cusp-periods-and-base-translation-certificate.json"
C754 = "p41-original-period-and-Hom-kernel-certificate.json"
P754 = "R754-original-relative-periods.json.gz"
C759 = "p41-original-integral-period-lattice-and-degree-certificate.json"
M759 = "R759-original-integral-maps-and-bounded-recovery-input.json.gz"
CMODEL = "p41-original-CM-model-certificate.json"
CELLS = "original-cosets-and-markings.json.gz"
CYCLES = "integral-compact-Manin-cycles.json.gz"
FIXED = {
    CMODEL: "752aa03f9cbe7d3174a7c508fce3043e21e8e85fd087e01acc4bca82a5cbd574",
    CELLS: "6a73cb699abb5e53328a040ec86bea2c4cac7ef690a29984912c43417cfd0161",
    CYCLES: "d4dcbac16cc24cefd378fc7afea02fcd34b8043d255c1e84407ff7d21bd257cf",
}
EDGE_STAGE = "R764-nineteen-original-tree-edge-periods"
LABEL_STAGE = "R764-all-original-cusp-labels-and-c0-translations"
LABEL_POINTS = ["O", "(0,-b_half)", "(0,+b_half)"]


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


def eq(q):
    return [str(q.numer()), str(q.denom())]


def dq(pair):
    return fmpq(int(pair[0]), int(pair[1]))


def dp(poly):
    return fmpq_poly([int(x) for x in poly["numerator"]], int(poly["denominator"]))


def encode_K(pair):
    return [eq(pair[0]), eq(pair[1])]


def decode_K(value):
    return dq(value[0]), dq(value[1])


def add_K(x, y, sign=1):
    return x[0]+sign*y[0], x[1]+sign*y[1]


class Field:
    """Only the already certified degree-seven L=K(b); zeta^2=-zeta-1."""
    def __init__(self, modulus):
        assert modulus.degree() == 7 and modulus[7] == 1
        self.mod = modulus
        self.zero = (fmpq_poly([]), fmpq_poly([]))

    def decode(self, encoded):
        a, b = dp(encoded[0]), dp(encoded[1])
        assert a.degree() < 7 and b.degree() < 7
        return a, b

    def add(self, x, y):
        return x[0]+y[0], x[1]+y[1]

    def mul(self, x, y):
        a, b = x
        c, d = y
        ac, bd = a*c, b*d
        return ((ac-bd) % self.mod,
                ((a+b)*(c+d)-ac-2*bd) % self.mod)

    def constant(self, x):
        assert x[0].degree() <= 0 and x[1].degree() <= 0, \
            "A genuine cusp-to-cusp map period did not descend to K"
        return x[0][0], x[1][0]


def stage_sha(cert, filename):
    matches = [row for row in cert["stages"] if row["file"] == filename]
    assert len(matches) == 1, "Missing or duplicate producer stage"
    return matches[0]["sha256"]


class Job:
    def __init__(self, args):
        assert flint.__version__ == "0.9.0"
        self.args, self.out = args, args.output
        self.out.mkdir(parents=True, exist_ok=True)
        self.started = time.monotonic()
        for name, digest in FIXED.items():
            assert sha(args.inputs/name) == digest
        self.model = read(args.inputs/CMODEL)
        assert self.model["complete"] and self.model["exact_F_of_b_zero"]
        assert self.model["original_b_not_a_replacement_twist"]
        self.F = Field(dp(self.model["minimal_polynomial"]))
        self.c754 = read(args.inputs/C754)
        self.c759 = read(args.inputs/C759)
        assert self.c754["complete"] and self.c759["complete"]
        assert self.c754["p"] == self.c759["p"] == 41
        assert self.c754["source_genus"] == self.c759["source_genus"] == 400
        assert self.c754["configuration"]["source_sha256"] == args.r754_core_sha256
        assert self.c759["configuration"]["source_sha256"] == args.r759_core_sha256
        assert self.c759["configuration"]["R754_core_sha256"] == args.r754_core_sha256
        assert self.c759["configuration"]["R754_certificate_sha256"] == sha(args.inputs/C754)
        assert self.c754["constraint_rank"] == 36
        assert self.c754["kernel_dimension_over_K"] == 6
        assert self.c754["all_800_chains_verified_for_all_six_kernel_vectors"]
        assert self.c754["c1_coset"] == 4424
        assert self.c754["c0_cosets"] == [2876, 2822, 2823]
        assert self.c759["full_integral_period_lattice_Z_rank"] == 12
        assert self.c759["O_K_rank"] == 6
        assert self.c759["all_1600_rational_period_rows_used"]
        assert self.c759["positive_definite_degree_form_verified"]
        assert sha(args.inputs/P754) == stage_sha(self.c754, P754)
        assert sha(args.inputs/M759) == stage_sha(self.c759, M759)
        self.relative = read(args.inputs/P754)
        self.maps = read(args.inputs/M759)
        assert self.relative["complete"] and self.maps["complete"]
        assert self.relative["configuration"] == self.c754["configuration"]
        assert self.maps["configuration"] == self.c759["configuration"]
        assert self.relative["normalization"] == "R_C/Omega0 * integral_(g0 to gInfinity) omega_j"
        assert self.relative["full_6inverse_and_tame_phase_retained"]
        assert self.relative["c1_phase_not_applied_a_second_time"]
        assert self.relative["all_periods_in_actual_K_b"]
        assert self.maps["Z_basis_rank"] == 12 and self.maps["O_K_rank"] == 6
        assert self.maps["base_point"] == "original c0, with f(c0)=O"
        assert self.maps["c1_coset"] == 4424
        assert self.maps["degrees"] == self.c759["degrees_of_LLL_Z_basis"]
        assert self.maps["selected_index"] == self.c759["selected_index"]
        self.degrees = [int(x) for x in self.maps["degrees"]]
        assert len(self.degrees) == 12 and all(d > 0 for d in self.degrees)
        self.selected = int(self.maps["selected_index"])
        assert 0 <= self.selected < 12
        assert self.degrees[self.selected] == int(self.maps["selected_degree"])
        raw = self.maps["all_twelve_integral_map_differential_vectors_in_original_omega_basis"]
        assert len(raw) == 12 and all(len(row) == 6 for row in raw)
        self.vectors = [[self.F.decode(x) for x in row] for row in raw]
        self.cells, self.cycles = read(args.inputs/CELLS), read(args.inputs/CYCLES)
        assert self.cells["p"] == self.cycles["p"] == 41
        assert self.cells["genus"] == self.cycles["genus"] == 400
        assert self.cells["c1"]["coset"] == 4424
        assert self.cells["c0"]["cosets"] == [2876, 2822, 2823]
        assert self.cells["c1"]["marked_SL2Z_representative"] == [15130, 123, 123, 1]
        self.cusps = self.cells["cusps"]
        assert len(self.cusps) == 20 and all(len(c) == 246 for c in self.cusps)
        self.cusp_of = {}
        for i, orbit in enumerate(self.cusps):
            for coset in orbit:
                assert coset not in self.cusp_of
                self.cusp_of[coset] = i
        assert len(self.cusp_of) == 4920
        self.root = self.cusp_of[0]
        self.tree = [int(x) for x in self.cycles["dual_tree_edges"]]
        self.relative_edges = [int(x) for x in self.cycles["relative_basis_edges"]]
        assert len(self.tree) == len(set(self.tree)) == 19
        assert set(self.tree) <= set(self.relative_edges)
        assert len(self.relative_edges) == 819
        assert set(map(int, self.relative["periods"])) == set(self.relative_edges)
        self.endpoints = {}
        for edge in self.tree:
            pos, neg = self.cycles["edge_positive_negative_cosets"][edge]
            assert self.cells["S"][pos] == neg
            start, end = self.cusp_of[neg], self.cusp_of[pos]
            assert start != end
            self.endpoints[edge] = (start, end)
        self.zeta = [[int(x) for x in row]
                     for row in self.maps["zeta_action_on_this_Z_basis"]]
        assert len(self.zeta) == 12 and all(len(row) == 12 for row in self.zeta)
        self.tag = {
            "result": RESULT, "version": "v2-reconstructed-from-complete-producer-schemas",
            "source_sha256": sha(__file__), "python_flint": flint.__version__,
            "R754_core_sha256": args.r754_core_sha256,
            "R759_core_sha256": args.r759_core_sha256,
            "R754_certificate_sha256": sha(args.inputs/C754),
            "R754_relative_periods_sha256": sha(args.inputs/P754),
            "R759_certificate_sha256": sha(args.inputs/C759),
            "R759_integral_maps_sha256": sha(args.inputs/M759),
            "fixed_inputs": FIXED,
            "edge_orientation": "cusp(gS) to cusp(g), unchanged R738 positive coset",
            "period_coordinate_order": "1,zeta; Im(zeta)>0",
            "period_normalization": "R_C/Omega0 * integral h",
            "root_cusp": self.root, "root_coset": 0,
            "b_half": "-U^20*S(U)^3/8, the original real R735/R751 branch",
            "nu_points": LABEL_POINTS,
            "c0_translation": "f0=fP-fP(c0)",
        }

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

    def edge_periods(self):
        old = self.cached(EDGE_STAGE)
        if old and old["complete"]:
            assert old["tree_edges_in_original_order"] == self.tree
            assert len(old["records"]) == 19
            return old
        records = [] if old is None else old["records"]
        assert len(records) <= 19
        assert [row["edge"] for row in records] == self.tree[:len(records)]
        for edge in self.tree[len(records):]:
            original = self.relative["periods"][str(edge)]
            assert len(original) == 6
            pi = [self.F.decode(x) for x in original]
            actual = []
            for vector in self.vectors:
                total = self.F.zero
                for j in range(6):
                    total = self.F.add(total, self.F.mul(vector[j], pi[j]))
                actual.append(encode_K(self.F.constant(total)))
            start, end = self.endpoints[edge]
            records.append({"edge": edge, "start_cusp": start, "end_cusp": end,
                            "periods_in_K_for_twelve_maps": actual})
            self.store(EDGE_STAGE, {
                "complete": False, "records": records,
                "tree_edges_in_original_order": self.tree,
                "all_computed_periods_descend_exactly_to_K": True})
        return self.store(EDGE_STAGE, {
            "complete": True, "records": records, "tree_edges_in_original_order": self.tree,
            "all_computed_periods_descend_exactly_to_K": True,
            "original_periods_or_tree_recomputed": False})

    def labels(self, edges):
        old = self.cached(LABEL_STAGE)
        if old and old["complete"]:
            return old
        adjacency = [[] for _ in range(20)]
        values = {}
        for row in edges["records"]:
            edge, a, b = row["edge"], row["start_cusp"], row["end_cusp"]
            values[edge] = [decode_K(x) for x in row["periods_in_K_for_twelve_maps"]]
            adjacency[a].append((b, edge, 1))
            adjacency[b].append((a, edge, -1))
        paths = {self.root: []}
        periods = {self.root: [(fmpq(0), fmpq(0)) for _ in range(12)]}
        queue = deque([self.root])
        used = set()
        while queue:
            a = queue.popleft()
            for b, edge, sign in adjacency[a]:
                if edge in used:
                    continue
                used.add(edge)
                assert b not in paths, "The retained dual-tree list was not a tree"
                paths[b] = paths[a]+[[edge, sign]]
                periods[b] = [add_K(periods[a][i], values[edge][i], sign)
                              for i in range(12)]
                queue.append(b)
        assert len(paths) == 20 and len(used) == 19
        cusp_rows = []
        all_labels = []
        for c in range(20):
            integral, labels = [], []
            for a, b in periods[c]:
                first, second = a+b, 2*b-a
                assert first.denom() == second.denom() == 1, \
                    "(1-zeta)*the exact cusp period was not in Z[zeta]"
                x, y = int(first.numer()), int(second.numer())
                integral.append([str(x), str(y)])
                labels.append((x+y) % 3)
            all_labels.append(labels)
            cusp_rows.append({
                "cusp": c, "representative_coset": min(self.cusps[c]),
                "path_from_original_reference_cusp": paths[c],
                "periods_in_K": [encode_K(v) for v in periods[c]],
                "one_minus_zeta_times_period_integral_coordinates": integral,
                "nu_for_twelve_maps": labels})
        assert all_labels[self.root] == [0]*12
        map_rows, c0_labels = [], []
        for i, degree in enumerate(self.degrees):
            counts = [sum(row[i] == nu for row in all_labels) for nu in range(3)]
            assert sum(counts) == 20
            residual = [(degree-counts[nu]) % 3 for nu in range(3)]
            assert sorted(residual) == [0, 0, 1], \
                "The three genuine degree fibers did not single out one c0 label"
            nu0 = residual.index(1)
            c0_labels.append(nu0)
            m = (degree+127+819)//820
            bound = 820*m+degree
            map_rows.append({
                "map_index": i, "degree": str(degree),
                "cusp_counts_order_nu_0_1_2": counts,
                "degree_minus_counts_mod3": residual,
                "fP_c0_nu": nu0, "fP_c0_point": LABEL_POINTS[nu0],
                "f0_reference_cusp_nu": (-nu0) % 3,
                "based_map_formula": "f0=fP-fP(c0)",
                "quotient_y_degree": str(degree), "quotient_genus": 127,
                "quotient_RR_m": str(m), "quotient_RR_M": str(bound),
                "quotient_RR_basis_qY_through": str(bound+degree),
                "original_h_over_dQ_through": str(3*bound+4*degree)})
        # Columns describe multiplication by zeta on the actual Z-basis.
        for row in all_labels+[c0_labels]:
            for j in range(12):
                assert sum(row[i]*self.zeta[i][j] for i in range(12)) % 3 == row[j]
        return self.store(LABEL_STAGE, {
            "complete": True, "root_cusp": self.root, "cusps": cusp_rows,
            "all_twelve_maps": map_rows, "selected_index": self.selected,
            "selected_map": map_rows[self.selected],
            "all_cusp_and_c0_labels_are_zeta_invariant": True,
            "c0_translation_linear_functional_on_full_Z_lattice": c0_labels,
            "label_convention": LABEL_POINTS,
            "original_signed_b_half": "-U^20*S(U)^3/8",
            "all_three_degree_fiber_congruences_verified_for_all_twelve_maps": True,
            "CM_endpoint_integral_or_RR_functions_recomputed": False,
            "actual_rational_functions_beta_or_height_computed": False})


def main():
    if os.environ.get("GITHUB_ACTIONS") != "true" or \
       os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public":
        raise SystemExit("Exact mathematical execution belongs to the public repository Actions.")
    sys.set_int_max_str_digits(0)
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--inputs", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--r754-core-sha256", required=True)
    parser.add_argument("--r759-core-sha256", required=True)
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
        edges = job.edge_periods()
        labels = job.labels(edges)
        stages = [{"file": job.path(name).name, "bytes": job.path(name).stat().st_size,
                   "sha256": sha(job.path(name))} for name in (EDGE_STAGE, LABEL_STAGE)]
        cert = {
            "result": RESULT, "configuration": job.tag, "complete": True,
            "p": 41, "source_genus": 400, "quotient_genus": 127,
            "original_cusps": 20, "original_retained_tree_edges": 19,
            "actual_integral_maps": 12, "c1_coset": 4424,
            "c0_cosets": [2876, 2822, 2823],
            "all_tree_periods_descend_exactly_to_K": True,
            "all_one_minus_zeta_periods_integral": True,
            "all_degree_fiber_congruences_verified": True,
            "all_cusp_and_c0_labels_are_zeta_invariant": True,
            "label_convention": LABEL_POINTS,
            "c0_translation_linear_functional_on_full_Z_lattice":
                labels["c0_translation_linear_functional_on_full_Z_lattice"],
            "all_twelve_map_counts_and_c0_translations": labels["all_twelve_maps"],
            "selected_index": job.selected, "selected_map": labels["selected_map"],
            "old_model_topology_periods_Hom_kernel_lattice_or_degrees_recomputed": False,
            "actual_rational_functions_beta_or_height_computed": False,
            "stages": stages, "seconds": time.monotonic()-job.started}
        save(final, cert)
        save(args.output/"core-receipt.json", {
            "result": RESULT, "complete": True, "source_sha256": sha(__file__),
            "certificate_sha256": sha(final),
            "selected_map_fP_c0_nu": labels["selected_map"]["fP_c0_nu"]})
        print(json.dumps({"result": RESULT, "complete": True,
                          "selected_map_fP_c0_nu": labels["selected_map"]["fP_c0_nu"]}), flush=True)
    except BaseException as error:
        save(args.output/"core-receipt.json", {
            "result": RESULT, "complete": False, "source_sha256": sha(__file__),
            "error": type(error).__name__+": "+str(error), "completed_stages_preserved": True})
        raise


if __name__ == "__main__":
    main()
