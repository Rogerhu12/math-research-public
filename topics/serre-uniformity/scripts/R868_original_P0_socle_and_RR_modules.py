#!/usr/bin/env python3
"""R868: one exact original P0 socle, two point inverse ideals, five RR sources.

All arithmetic is restricted to the public Actions entry point.  This file
does not recompute W, a Fourier coefficient, a point value, or a prior ideal.
The new solve is one rank-271 K=Q(zeta) kernel, with exact full multiply-back.
The five degree-254 modules are source-bound ideal expressions; no 128-section
RR basis, connection, or height is claimed by this first scope.
"""

import argparse
from fractions import Fraction
import gzip
import hashlib
import json
import math
import os
from pathlib import Path
import re
import sys
import time
import traceback

RESULT = "R868-original-P0-socle-and-degree254-RR-modules"
FINAL = "p41-original-P0-socle-and-RR-module-certificate.json"
PREFIX = "R868-"
MANIFEST = "full-outputs-manifest.json"
META = ("public-actions-input.json", "run-receipt.json", "core-receipt.json")
BASE = ("result", "run_id", "source_commit", "core_sha256", "manifest_sha256")
SOURCES = ("R805", "R806", "R849", "R856", "R860")
PROOFS = ("R868", "YP", "FM", "R856", "R860", "GP")
EPS = [0] + [1] * 144 + [2] * 127
RANK = 272
MINOR_RANK = 271
GROUPS = 34
PQ = [(165, 67), (93, 67), (100, 67), (168, 67), (371, 134)]
CERTIFICATES = {
    "R805": "p41-original-affine-pencil-free-basis-certificate.json",
    "R806": "p41-original-primitive-multiplication-certificate.json",
    "R849": "p41-original-global-addition-polar-ideal-DAG-certificate.json",
    "R856": "p41-original-fixed-branch-ideal-bases-certificate.json",
    "R860": "p41-original-semilinear-resolvent-DAG-certificate.json",
}
STRATEGY = {
    "scope": "P0_single_pole_and_five_degree254_module_sources",
    "normal_basis_rank": 272,
    "point_fiber_rank_target": 271,
    "point_inverse_power": 254,
    "K_basis": "1,zeta; zeta^2+zeta+1=0",
    "W_matrix_convention": "row_output_column_input",
    "point_source": "original_R856_P0_in_both_charts",
    "prime_schedule": "successive_primes_p>=1000000753_with_p_mod_3=1",
    "root_order": "first_integer_a>=2_with_nontrivial_cube_root_then_its_square",
    "minor_selection": "first_embedding_RREF_columns_then_transpose_RREF_rows",
    "one_common_minor_must_be_unit_at_both_K_embeddings": True,
    "integer_column_scaling": "original_denominator*point_z_denominator^3*point_w_denominator/gcd_content",
    "free_coordinate_in_integral_system": 1,
    "final_free_original_normal_coordinate": 1,
    "Dixon": "one_fixed_pair_of_271_inverses_and_two_integral_K_residuals",
    "RR_rectangle": "each_Q_coordinate_bound_floor_sqrt((M-1)/2);2*bound^2<M",
    "RR_attempt_every_digits": 8,
    "full_exact_original_normal_equations": 272,
    "full_exact_K_coordinate_equations": 544,
    "sigma_kernel_transport": "h_sigma[i]=v0^(-epsilon[i])*h_tau[i]",
    "socle_argument_allows_ramified_fiber": True,
    "point_inverse_generators": "1,f_chart^254; complete by curve DVR valuations",
    "source_eta_root": "eta_degree_zero_fractional_ideal",
    "two_weight_certificate": {"weight0": 128, "weight1": 144},
    "old_W_point_values_or_ideals_recomputed": False,
    "characteristic_zero_determinant_or_full_Krylov_inverse_computed": False,
    "degree254_RR_basis_128_computed": False,
    "original_connection_or_height_computed": False,
    "only_transport_resume_budget_and_search_limits_excluded_from_identity": True,
}


class BudgetStop(Exception):
    pass


class SearchStop(Exception):
    pass


def sha(path):
    h = hashlib.sha256()
    with Path(path).open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def read(path):
    path = Path(path)
    with (gzip.open(path, "rt", encoding="utf-8") if path.name.endswith(".gz")
          else path.open("r", encoding="utf-8")) as stream:
        return json.load(stream)


def save(path, value, fast=False):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    temp = path.with_name(path.name + ".tmp")
    payload = json.dumps(value, sort_keys=True, ensure_ascii=False,
                         separators=(",", ":")).encode() + b"\n"
    with temp.open("wb") as stream:
        if path.name.endswith(".gz"):
            with gzip.GzipFile(fileobj=stream, mode="wb", mtime=0,
                              compresslevel=1 if fast else 6) as compressed:
                compressed.write(payload)
        else:
            stream.write(payload)
        stream.flush()
        os.fsync(stream.fileno())
    os.replace(temp, path)


def fingerprint(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True,
                                    separators=(",", ":")).encode()).hexdigest()


def plain(entry):
    assert isinstance(entry, dict)
    result = {k: entry[k] for k in ("file", "bytes", "sha256")}
    assert Path(result["file"]).name == result["file"]
    assert isinstance(result["bytes"], int) and result["bytes"] >= 0
    assert re.fullmatch(r"[0-9a-f]{64}", result["sha256"])
    return result


def spec(path):
    path = Path(path)
    return {"file": path.name, "bytes": path.stat().st_size, "sha256": sha(path)}


def bound(directory, entry):
    entry = plain(entry)
    path = Path(directory) / entry["file"]
    assert path.is_file(), entry["file"]
    assert path.stat().st_size == entry["bytes"], entry["file"]
    assert sha(path) == entry["sha256"], entry["file"]
    return path


def identity(source):
    return {k: source[k] for k in BASE}


def source_identity(source):
    return {**identity(source), "certificate": plain(source["certificate"]),
            "configuration_sha256": source["configuration_sha256"],
            "selected_file_count": len(source["files"]),
            "selected_files_sha256": fingerprint(source["files"])}


def expected_tag(item):
    return {
        "result": RESULT, "source_sha256": item["core_sha256"], "p": 41,
        "python_flint": "0.9.0", "method_sha256": item["method_sha256"],
        "proofs_sha256": {k: item["proofs"][k]["sha256"] for k in PROOFS},
        "sources": {k: source_identity(item["sources"][k]) for k in SOURCES},
        "normal_basis_degrees": EPS, "strategy": STRATEGY,
    }


def q(value):
    if isinstance(value, (list, tuple)):
        assert len(value) == 2
        return Fraction(int(value[0]), int(value[1]))
    return Fraction(value)


def qdata(value):
    value = q(value)
    return [str(value.numerator), str(value.denominator)]


def kval(value):
    assert len(value) == 2
    return (q(value[0]), q(value[1]))


def kdata(value):
    return [qdata(value[0]), qdata(value[1])]


def kadd(a, b):
    return a[0] + b[0], a[1] + b[1]


def kneg(a):
    return -a[0], -a[1]


def kmul(a, b):
    return a[0]*b[0] - a[1]*b[1], a[0]*b[1] + a[1]*b[0] - a[1]*b[1]


def kinv(a):
    n = a[0]*a[0] - a[0]*a[1] + a[1]*a[1]
    assert n != 0
    return (a[0] - a[1])/n, -a[1]/n


def kpow(a, n):
    if n < 0:
        return kpow(kinv(a), -n)
    result = (Fraction(1), Fraction(0))
    while n:
        if n & 1:
            result = kmul(result, a)
        n >>= 1
        if n:
            a = kmul(a, a)
    return result


def gcd_list(values):
    result = 0
    for value in values:
        result = math.gcd(result, int(value))
    return abs(result)


def lcm_den(values):
    result = 1
    for value in values:
        result = math.lcm(result, q(value).denominator)
    return result


def qmod(value, prime):
    value = q(value)
    assert value.denominator % prime
    return value.numerator % prime * pow(value.denominator % prime, -1, prime) % prime


def kmod(value, prime, root):
    return (qmod(value[0], prime) + root*qmod(value[1], prime)) % prime


def probable_prime_32(n):
    """Deterministic Miller--Rabin in the explicitly restricted 32-bit range."""
    assert 2 <= n < 2**32
    for small in (2, 3, 5, 7, 11, 13, 17):
        if n == small:
            return True
        if n % small == 0:
            return False
    d, s = n - 1, 0
    while d % 2 == 0:
        d //= 2
        s += 1
    for base in (2, 3, 5, 7, 11, 13, 17):
        a = pow(base, d, n)
        if a in (1, n-1):
            continue
        for _ in range(s-1):
            a = a*a % n
            if a == n-1:
                break
        else:
            return False
    return True


def primes():
    candidate = 1000000753
    while candidate < 2**32:
        if candidate % 3 == 1 and probable_prime_32(candidate):
            yield candidate
        candidate += 2


def roots_of_zeta(prime):
    assert prime % 3 == 1
    for a in range(2, prime):
        root = pow(a, (prime-1)//3, prime)
        if root != 1:
            other = root*root % prime
            assert root != other and (root*root+root+1) % prime == 0
            return [root, other]
    raise AssertionError("no nontrivial cube root in a prime field p=1 mod3")


def pivot_columns(reduced, rank):
    rows = reduced.tolist()
    answer = []
    for row in rows[:rank]:
        answer.append(next(i for i, x in enumerate(row) if int(x)))
    assert answer == sorted(set(answer)) and len(answer) == rank
    return answer


def rational_reconstruct(a, modulus, limit):
    a %= modulus
    if a == 0:
        return Fraction(0)
    r0, r1, t0, t1 = modulus, a, 0, 1
    while abs(r1) > limit:
        if r1 == 0:
            return None
        quotient = r0 // r1
        r0, r1 = r1, r0-quotient*r1
        t0, t1 = t1, t0-quotient*t1
    if t1 == 0 or abs(t1) > limit or math.gcd(r1, t1) != 1:
        return None
    if math.gcd(t1, modulus) != 1 or (a*t1-r1) % modulus:
        return None
    return Fraction(r1, t1)


class Source:
    def __init__(self, label, source):
        self.label, self.source = label, source
        self.directory = Path(source["directory"])
        self.files = {name: plain(entry) for name, entry in source["files"].items()}
        assert all(name == entry["file"] for name, entry in self.files.items())
        for entry in self.files.values():
            bound(self.directory, entry)
        self.manifest = read(self.directory / MANIFEST)
        assert self.files[MANIFEST]["sha256"] == source["manifest_sha256"]
        entries = {entry["file"]: plain(entry) for entry in self.manifest["files"]}
        assert len(entries) == len(self.manifest["files"])
        for name, entry in self.files.items():
            if name != MANIFEST:
                assert entries[name] == entry, (label, name)
        initial, run, core = [read(self.directory / name) for name in META]
        assert initial["result"] == run["result"] == core["result"] == source["result"]
        assert initial["source_commit"] == run["source_commit"] == source["source_commit"]
        assert str(run["workflow_run_id"]) == str(source["run_id"])
        assert initial["core_sha256"] == core["source_sha256"] == source["core_sha256"]
        assert run["complete"] is True and run["process_exit_code"] == 0
        assert run["error"] is None and core["complete"] is True
        assert run["core_receipt_sha256"] == self.files["core-receipt.json"]["sha256"]
        self.certificate_spec = plain(source["certificate"])
        assert self.certificate_spec["file"] == CERTIFICATES[label]
        assert self.files[self.certificate_spec["file"]] == self.certificate_spec
        self.certificate = read(self.directory / self.certificate_spec["file"])
        assert self.certificate["result"] == source["result"]
        assert self.certificate["complete"] is True
        assert core["certificate_sha256"] == self.certificate_spec["sha256"]
        self.tag = self.certificate["configuration"]
        assert self.tag["source_sha256"] == source["core_sha256"]
        assert self.tag["result"] == source["result"]
        assert fingerprint(self.tag) == source["configuration_sha256"]

    def indexed(self, entry):
        entry = plain(entry)
        assert self.files[entry["file"]] == entry, (self.label, entry["file"])
        value = read(self.directory / entry["file"])
        assert value["complete"] is True and value["configuration"] == self.tag
        return value

    def named(self, name):
        return self.indexed(self.files[name])


class Job:
    def __init__(self, args):
        from flint import fmpz_mat, nmod_mat
        self.Zmat, self.Pmat = fmpz_mat, nmod_mat
        self.args, self.started = args, time.monotonic()
        self.deadline = self.started + 60*float(args.budget_minutes)
        self.item = read(args.config)
        assert self.item["result"] == RESULT and self.item["core_sha256"] == sha(__file__)
        assert sha(self.item["method"]) == self.item["method_sha256"]
        for key in PROOFS:
            assert sha(self.item["proofs"][key]["file"]) == self.item["proofs"][key]["sha256"]
        self.tag = expected_tag(self.item)
        self.out = Path(args.out)
        self.out.mkdir(parents=True, exist_ok=True)
        self.controls = self.item.get("controls", {})
        self.max_prime_trials = int(self.controls.get("maximum_prime_trials", 8))
        self.max_digits = int(self.controls.get("maximum_Dixon_digits", 8192))
        assert self.max_prime_trials >= 1 and self.max_digits >= 1
        self.refs = {}
        self.current = None
        self.stage_files = {}
        self.sources = {label: Source(label, self.item["sources"][label]) for label in SOURCES}
        self.prepare()

    def check_time(self):
        if time.monotonic() >= self.deadline:
            raise BudgetStop("wall-clock arithmetic budget reached")

    def load(self, name):
        path = self.out / (PREFIX + name + ".json.gz")
        if not path.exists():
            return None
        value = read(path)
        assert value["result"] == RESULT and value["configuration"] == self.tag
        assert value["complete"] is True
        self.stage_files[path.name] = spec(path)
        return value

    def put(self, name, value, fast=False):
        old = self.load(name)
        if old is not None:
            return self.stage_files[PREFIX + name + ".json.gz"]
        payload = {"result": RESULT, "configuration": self.tag, "complete": True, **value}
        assert payload["complete"] is True
        path = self.out / (PREFIX + name + ".json.gz")
        save(path, payload, fast)
        entry = spec(path)
        self.stage_files[path.name] = entry
        return entry

    def own(self, entry):
        path = bound(self.out, entry)
        value = read(path)
        assert value["result"] == RESULT and value["configuration"] == self.tag
        assert value["complete"] is True
        self.stage_files[path.name] = plain(entry)
        return value

    def prepare(self):
        self.W_source = self.sources["R860"].certificate["coefficient_source_index"]
        self.Windex = self.sources["R860"].indexed(self.W_source)
        assert self.Windex["normal_basis_degrees"] == EPS
        assert self.Windex["normal_basis_rank"] == RANK
        assert self.Windex["matrix_convention"] == "row_output_column_input"
        assert self.Windex["coefficient_rule"]["additional_scale"] == [1, 1]
        assert self.Windex["complete_original_coefficient_sources_retained"] is True
        assert self.Windex["original_weighted_support_checked_in_all_groups"] is True
        assert identity(self.Windex["source_original_R806_producer"]) == identity(self.item["sources"]["R806"])
        assert identity(self.sources["R860"].tag["sources"]["R806"]) == identity(self.item["sources"]["R806"])
        self.mapping = self.Windex["S_row_to_polynomial_coefficient"]
        assert len(self.mapping) == 690
        assert [x["S_row"] for x in self.mapping] == list(range(690))
        assert len(self.Windex["normal_column_source_locations"]) == RANK
        assert len(self.Windex["source_exact_coordinate_groups"]) == GROUPS
        self.values_source = self.sources["R856"].files["R856-original-P0-normal-values.json.gz"]
        self.values = self.sources["R856"].indexed(self.values_source)
        assert self.values["normal_basis_rank"] == RANK
        assert self.values["normal_basis_degrees"] == EPS
        assert self.values["all_272_two_chart_value_transitions_verified"] is True
        assert self.values["original_P0_in_both_charts_verified"] is True
        assert self.values["additional_scale_inserted"] is False
        free_source = self.sources["R805"].files["R805-graded-free-basis.json.gz"]
        assert plain(self.values["source_free_basis"]) == free_source
        self.z0 = kval(self.values["chart_base_values_K_1_zeta"]["tau"])
        self.v0 = kval(self.values["chart_base_values_K_1_zeta"]["sigma"])
        assert kmul(self.z0, self.v0) == (1, 0)
        self.bpoint = [kval(a) for a in self.values["normal_basis_values_K_1_zeta"]["tau"]]
        assert len(self.bpoint) == RANK and self.bpoint[0] == (1, 0)
        self.w0 = self.bpoint[1]
        self.point_den = lcm_den(self.z0)
        self.w_den = lcm_den(self.w0)
        self.left_den = lcm_den([a for pair in self.bpoint for a in pair])
        self.left0 = [int(self.left_den*a[0]) for a in self.bpoint]
        self.left1 = [int(self.left_den*a[1]) for a in self.bpoint]
        self.Z = tuple(int(self.point_den*a) for a in self.z0)
        self.W0 = tuple(int(self.w_den*a) for a in self.w0)
        self.Zpowers = [(1, 0)]
        for _ in range(3):
            self.Zpowers.append(kmul(self.Zpowers[-1], self.Z))
        self.GP_source = self.sources["R849"].files["R839-global-polar-exact-global-function-and-five-polar-expression-DAG.json.gz"]
        self.GP = self.sources["R849"].indexed(self.GP_source)
        assert self.GP["original_eta_Picard_input_DAGs_defined"] is True
        assert self.GP["five_original_addition_pole_ideals_as_fractional_DAGs_certified"] is True
        assert self.GP["normal_polynomial_ideal_lattices_materialized"] is False
        assert plain(self.GP["normal_basis_source"]) == free_source
        ids = {node["id"] for node in self.GP["graph_nodes"]}
        assert len(ids) == len(self.GP["graph_nodes"]) == self.GP["actual_graph_node_count"]
        for node in self.GP["graph_nodes"]:
            assert all(ref in ids for ref in node["inputs"])
        for j, pair in enumerate(PQ, 1):
            output = self.GP["five_original_polar_and_eta_outputs"][str(j)]
            assert (output["p"], output["q"]) == pair
            assert output["eta_Picard_class"]["sign"] == -1
            assert output["eta_Picard_class"]["rational_denominator"] == pair[1]
            assert output["eta_Picard_class"]["ideal_nodes"] == output["eta_degree_zero_fractional_ideal"]
            for chart in ("tau", "sigma"):
                assert output["eta_degree_zero_fractional_ideal"][chart] in ids
        self.refs["source_audit"] = self.put("original-source-audit", {
            "source_W_index": plain(self.W_source), "source_P0_values": plain(self.values_source),
            "source_global_eta_DAG": plain(self.GP_source), "source_free_basis": free_source,
            "z0_K_1_zeta": kdata(self.z0), "v0_K_1_zeta": kdata(self.v0),
            "w0_K_1_zeta": kdata(self.w0), "normal_basis_degrees": EPS,
            "point_z_common_denominator": str(self.point_den),
            "point_w_common_denominator": str(self.w_den),
            "source_eta_root_name": "eta_degree_zero_fractional_ideal",
            "uses_original_not_three_isogenous_line_bundles": True,
            "all_source_identities_and_selected_bytes_verified": True,
            "all_mathematical_input_scales_preserved": True,
            "old_W_point_values_or_ideals_recomputed": False,
        })

    def integral_matrix(self):
        blocks = []
        for group in range(GROUPS):
            name = "point-integral-columns-" + f"{8*group:03d}-{8*group+8:03d}"
            old = self.load(name)
            if old is None:
                self.check_time()
                source = plain(self.Windex["source_exact_coordinate_groups"][group])
                coords = self.sources["R806"].indexed(source)
                numerators = coords["coordinate_numerators"]
                denominators = coords["column_denominators"]
                assert len(numerators) == 690 and all(len(row) == 8 for row in numerators)
                assert len(denominators) == 8
                columns, scales, contents = [], [], []
                for local in range(8):
                    j = 8*group+local
                    location = self.Windex["normal_column_source_locations"][j]
                    assert location == {"normal_input_column": j, "source_group": group, "local_column": local}
                    denominator = int(denominators[local])
                    assert denominator > 0
                    a0, a1 = [0]*RANK, [0]*RANK
                    for source_row, mapping in enumerate(self.mapping):
                        i, power = mapping["normal_basis_row"], mapping["power_of_z"]
                        value = int(numerators[source_row][local])
                        assert 0 <= i < RANK and 0 <= power <= 3
                        if power > 1+EPS[j]-EPS[i]:
                            assert value == 0
                        factor = self.w_den*self.point_den**(3-power)*value
                        a0[i] += factor*self.Zpowers[power][0]
                        a1[i] += factor*self.Zpowers[power][1]
                    a0[j] -= denominator*self.point_den**3*self.W0[0]
                    a1[j] -= denominator*self.point_den**3*self.W0[1]
                    content = gcd_list(a0+a1) or 1
                    a0 = [v//content for v in a0]
                    a1 = [v//content for v in a1]
                    scale = Fraction(denominator*self.point_den**3*self.w_den, content)
                    assert scale > 0
                    left0 = sum(b0*x0-b1*x1 for b0,b1,x0,x1 in zip(self.left0,self.left1,a0,a1))
                    left1 = sum(b0*x1+b1*x0-b1*x1 for b0,b1,x0,x1 in zip(self.left0,self.left1,a0,a1))
                    assert left0 == left1 == 0, ("original P0 left evaluation", j)
                    columns.append({"normal_input_column": j,
                                    "K_integer_coordinates": [[str(x),str(y)] for x,y in zip(a0,a1)]})
                    scales.append(qdata(scale))
                    contents.append(str(content))
                self.put(name, {"column_start": 8*group, "column_stop": 8*group+8,
                                "source_exact_W_group": source, "source_P0_values": plain(self.values_source),
                                "original_A_equals_H_times_inverse_column_scales": True,
                                "column_scales_Q": scales, "removed_positive_integer_column_contents": contents,
                                "columns": columns, "all_original_P0_left_equations_exactly_zero": True})
                old = self.load(name)
            assert old["column_start"] == 8*group and old["column_stop"] == 8*group+8
            blocks.append(self.stage_files[PREFIX+name+".json.gz"])
        H0, H1 = [[0]*RANK for _ in range(RANK)], [[0]*RANK for _ in range(RANK)]
        scales = [None]*RANK
        for entry in blocks:
            block = self.own(entry)
            for local, column in enumerate(block["columns"]):
                j = column["normal_input_column"]
                assert scales[j] is None
                scales[j] = q(block["column_scales_Q"][local])
                for i, pair in enumerate(column["K_integer_coordinates"]):
                    H0[i][j], H1[i][j] = int(pair[0]), int(pair[1])
        self.H0, self.H1, self.scales = H0, H1, scales
        self.refs["integral_matrix"] = self.put("point-integral-matrix-index", {
            "normal_basis_rank": RANK, "column_groups": blocks,
            "column_scales_Q": [qdata(v) for v in scales],
            "matrix_description": "H=(W(z0)-w0 I)*diag(column_scales)",
            "all_272_original_P0_left_equations_exactly_zero": True,
            "rank_upper_bound_271_from_nonzero_original_point_evaluation": True,
            "column_content_removal_changes_no_kernel_or_original_normal_scale": True,
        })

    def select_minor(self):
        accepted = self.load("accepted-point-minor")
        if accepted is not None:
            self.refs["point_minor"] = self.stage_files[PREFIX+"accepted-point-minor.json.gz"]
            self.minor = accepted
            return
        for trial, prime in enumerate(primes()):
            if trial >= self.max_prime_trials:
                raise SearchStop("prime trial limit; no characteristic-zero rank failure inferred")
            name = f"prime-{prime}-point-minor-trial"
            old = self.load(name)
            if old is not None:
                if old["accepted"]:
                    self.refs["point_minor"] = self.put("accepted-point-minor", {
                        **{k: v for k,v in old.items() if k not in ("result","configuration","complete")},
                        "source_trial": self.stage_files[PREFIX+name+".json.gz"]})
                    self.minor = self.load("accepted-point-minor")
                    return
                continue
            self.check_time()
            roots = roots_of_zeta(prime)
            bad = (self.point_den % prime == 0 or self.w_den % prime == 0 or self.left_den % prime == 0
                   or any(a.numerator % prime == 0 or a.denominator % prime == 0 for a in self.scales))
            if bad:
                self.put(name, {"prime": prime, "roots_zeta_mod_prime": roots,
                                "accepted": False, "reason": "original rational denominator or column scale not a unit",
                                "characteristic_zero_rank_failure_claimed": False})
                continue
            matrices = [[[ (self.H0[i][j]+root*self.H1[i][j]) % prime
                           for j in range(RANK)] for i in range(RANK)] for root in roots]
            rref, rank = self.Pmat(matrices[0], prime).rref()
            rank = int(rank)
            assert rank <= MINOR_RANK
            if rank != MINOR_RANK:
                self.put(name, {"prime": prime, "roots_zeta_mod_prime": roots, "accepted": False,
                                "reason": "first embedding rank below sufficient target", "actual_first_rank": rank,
                                "characteristic_zero_rank_failure_claimed": False})
                continue
            columns = pivot_columns(rref, rank)
            free = next(i for i in range(RANK) if i not in columns)
            transpose = [[matrices[0][i][j] for i in range(RANK)] for j in columns]
            row_rref, row_rank = self.Pmat(transpose, prime).rref()
            assert int(row_rank) == MINOR_RANK
            rows = pivot_columns(row_rref, MINOR_RANK)
            minors = [[[matrix[i][j] for j in columns] for i in rows] for matrix in matrices]
            determinants = [int(self.Pmat(a, prime).det()) for a in minors]
            if not all(determinants):
                self.put(name, {"prime": prime, "roots_zeta_mod_prime": roots, "accepted": False,
                                "reason": "same original minor is not a unit at second embedding",
                                "row_indices": rows, "column_indices": columns,
                                "determinants_mod_prime": determinants, "characteristic_zero_rank_failure_claimed": False})
                continue
            left = [[kmod(v, prime, root) for v in self.bpoint] for root in roots]
            for e, matrix in enumerate(matrices):
                assert left[e][0] == 1
                assert all(sum(left[e][i]*matrix[i][j] for i in range(RANK)) % prime == 0 for j in range(RANK))
            data = {"prime": prime, "roots_zeta_mod_prime": roots, "accepted": True,
                    "rank_target": MINOR_RANK, "row_indices": rows, "column_indices": columns,
                    "free_normal_coordinate": free, "determinants_mod_prime": determinants,
                    "actual_minor_matrices_mod_prime": minors,
                    "source_integral_matrix": self.refs["integral_matrix"],
                    "both_original_point_left_evaluation_vectors_verified": True,
                    "original_rational_denominators_and_scales_are_units": True,
                    "characteristic_zero_rank_271_certified": True,
                    "characteristic_zero_determinant_computed": False}
            trial_spec = self.put(name, data)
            self.refs["point_minor"] = self.put("accepted-point-minor", {**data, "source_trial": trial_spec})
            self.minor = self.load("accepted-point-minor")
            return

    def fixed_inverse(self):
        old = self.load("fixed-point-minor-inverses")
        prime = self.minor["prime"]
        if old is None:
            self.check_time()
            matrices = self.minor["actual_minor_matrices_mod_prime"]
            inverses = []
            for a in matrices:
                A = self.Pmat(a, prime)
                inverse = A.inv()
                right, left = (A*inverse).tolist(), (inverse*A).tolist()
                assert all(int(right[i][j]) == int(i == j) and int(left[i][j]) == int(i == j)
                           for i in range(MINOR_RANK) for j in range(MINOR_RANK))
                inverses.append([[int(x) for x in row] for row in inverse.tolist()])
            self.put("fixed-point-minor-inverses", {
                "prime": prime, "source_point_minor": self.refs["point_minor"],
                "roots_zeta_mod_prime": self.minor["roots_zeta_mod_prime"],
                "inverse_matrices_mod_prime": inverses,
                "both_products_verified_for_both_embeddings": True,
                "one_rational_542_system_implemented_as_two_split_271_systems": True})
            old = self.load("fixed-point-minor-inverses")
        assert old["source_point_minor"] == self.refs["point_minor"]
        self.refs["fixed_inverse"] = self.stage_files[PREFIX+"fixed-point-minor-inverses.json.gz"]
        self.inverses = [self.Pmat(matrix, prime) for matrix in old["inverse_matrices_mod_prime"]]
        rows, cols = self.minor["row_indices"], self.minor["column_indices"]
        self.M0 = self.Zmat([[self.H0[i][j] for j in cols] for i in rows])
        self.M1 = self.Zmat([[self.H1[i][j] for j in cols] for i in rows])
        self.M01 = self.M0-self.M1
        free = self.minor["free_normal_coordinate"]
        self.rhs0 = [-self.H0[i][free] for i in rows]
        self.rhs1 = [-self.H1[i][free] for i in rows]

    def system_product(self, x0, x1):
        a = self.Zmat([[int(x)] for x in x0])
        b = self.Zmat([[int(x)] for x in x1])
        y0, y1 = self.M0*a-self.M1*b, self.M1*a+self.M01*b
        return [int(y0[i,0]) for i in range(MINOR_RANK)], [int(y1[i,0]) for i in range(MINOR_RANK)]

    def modular_correction(self, r0, r1):
        p, roots = self.minor["prime"], self.minor["roots_zeta_mod_prime"]
        images = []
        for root, inverse in zip(roots, self.inverses):
            rhs = self.Pmat([[(a+root*b) % p] for a,b in zip(r0,r1)], p)
            answer = inverse*rhs
            images.append([int(answer[i,0]) for i in range(MINOR_RANK)])
        eta = pow((roots[0]-roots[1]) % p, -1, p)
        d1 = [(a-b)*eta % p for a,b in zip(*images)]
        d0 = [(a-roots[0]*b) % p for a,b in zip(images[0],d1)]
        return d0, d1

    def save_current(self, digits, modulus, x0, x1, r0, r1):
        value = {"result": RESULT, "configuration": self.tag, "complete": False,
                 "prime": self.minor["prime"], "digits": digits, "modulus": str(modulus),
                 "source_point_minor": self.refs["point_minor"], "source_fixed_inverse": self.refs["fixed_inverse"],
                 "solution_residues_K_coordinates": [[str(x) for x in x0], [str(x) for x in x1]],
                 "exact_current_residual_K_coordinates": [[str(x) for x in r0], [str(x) for x in r1]],
                 "residual_invariant": "rhs-M*x=modulus*current_residual",
                 "free_integral_coordinate": 1}
        path = self.out/(PREFIX+"Dixon-current.json.gz")
        save(path, value, fast=True)
        self.current = spec(path)
        self.digit_receipt(value)

    def digit_receipt(self, current):
        digits = current["digits"]
        name = f"Dixon-digit-{digits:06d}-receipt"
        old = self.load(name)
        if old is None:
            self.put(name, {"prime": current["prime"], "digits": digits,
                            "modulus_bits": int(current["modulus"]).bit_length(),
                            "source_point_minor": self.refs["point_minor"],
                            "source_fixed_inverse": self.refs["fixed_inverse"],
                            "completed_current_payload_sha256": fingerprint(current),
                            "exact_residual_division_verified": True})

    def load_current(self):
        path = self.out/(PREFIX+"Dixon-current.json.gz")
        if not path.exists():
            return 0, 1, [0]*MINOR_RANK, [0]*MINOR_RANK, self.rhs0[:], self.rhs1[:]
        current = read(path)
        assert current["result"] == RESULT and current["configuration"] == self.tag
        assert current["complete"] is False
        assert current["source_point_minor"] == self.refs["point_minor"]
        assert current["source_fixed_inverse"] == self.refs["fixed_inverse"]
        digits, modulus = int(current["digits"]), int(current["modulus"])
        assert modulus == self.minor["prime"]**digits
        x0, x1 = [[int(x) for x in row] for row in current["solution_residues_K_coordinates"]]
        r0, r1 = [[int(x) for x in row] for row in current["exact_current_residual_K_coordinates"]]
        assert all(len(row) == MINOR_RANK for row in (x0,x1,r0,r1))
        assert all(0 <= x < modulus for x in x0+x1)
        y0, y1 = self.system_product(x0,x1)
        assert all(b-y == modulus*r for b,y,r in zip(self.rhs0,y0,r0))
        assert all(b-y == modulus*r for b,y,r in zip(self.rhs1,y1,r1))
        self.current = spec(path)
        self.digit_receipt(current)
        return digits, modulus, x0, x1, r0, r1

    def reconstruction(self, digits, modulus, x0, x1):
        name = f"RR-at-digits-{digits:06d}"
        old = self.load(name)
        if old is not None:
            if old["all_coordinates_reconstructed_and_exact_system_verified"]:
                return [[q(x) for x in row] for row in old["solution_K_Q_coordinates"]]
            return None
        self.check_time()
        limit = math.isqrt((modulus-1)//2)
        assert 2*limit*limit < modulus
        values = []
        first_missing = None
        for i, x in enumerate(x0+x1):
            value = rational_reconstruct(x, modulus, limit)
            if value is None:
                first_missing = i
                break
            values.append(value)
        common = {"digits": digits, "prime": self.minor["prime"], "modulus_bits": modulus.bit_length(),
                  "strict_rectangle_bound": str(limit), "strict_rectangle_2_bound_squared_lt_modulus": True,
                  "source_point_minor": self.refs["point_minor"]}
        if first_missing is not None:
            self.put(name, {**common, "all_coordinates_reconstructed_and_exact_system_verified": False,
                            "first_failed_Q_coordinate": first_missing, "reason": "strict rational reconstruction incomplete"})
            return None
        a, b = values[:MINOR_RANK], values[MINOR_RANK:]
        denominator = lcm_den(values)
        a_int, b_int = [int(denominator*v) for v in a], [int(denominator*v) for v in b]
        y0, y1 = self.system_product(a_int,b_int)
        failures = [(e,i) for e,(yy,rr) in enumerate(((y0,self.rhs0),(y1,self.rhs1)))
                    for i,(yv,rv) in enumerate(zip(yy,rr)) if yv != denominator*rv]
        if failures:
            self.put(name, {**common, "all_coordinates_reconstructed_and_exact_system_verified": False,
                            "reason": "reconstructed candidate failed exact selected system",
                            "first_failed_exact_selected_equation": list(failures[0]),
                            "failed_exact_selected_equation_count": len(failures)})
            return None
        self.put(name, {**common, "all_coordinates_reconstructed_and_exact_system_verified": True,
                        "solution_K_Q_coordinates": [[qdata(x) for x in a], [qdata(x) for x in b]],
                        "all_542_selected_Q_equations_exactly_verified": True})
        return a,b

    def exact_socle(self):
        old = self.load("exact-original-normal-socle-vector")
        if old is not None:
            self.refs["exact_socle"] = self.stage_files[PREFIX+"exact-original-normal-socle-vector.json.gz"]
            self.h = [kval(x) for x in old["h_tau_K_1_zeta"]]
            return
        self.fixed_inverse()
        digits, modulus, x0, x1, r0, r1 = self.load_current()
        recovered = None
        period = STRATEGY["RR_attempt_every_digits"]
        while True:
            if digits and (digits % period == 0 or digits >= self.max_digits):
                recovered = self.reconstruction(digits,modulus,x0,x1)
                if recovered is not None:
                    break
            if digits >= self.max_digits:
                raise SearchStop("Dixon digit limit; exact socle vector not yet reconstructed")
            self.check_time()
            d0,d1 = self.modular_correction(r0,r1)
            y0,y1 = self.system_product(d0,d1)
            p = self.minor["prime"]
            differences0 = [a-b for a,b in zip(r0,y0)]
            differences1 = [a-b for a,b in zip(r1,y1)]
            assert all(x % p == 0 for x in differences0+differences1)
            x0 = [a+modulus*b for a,b in zip(x0,d0)]
            x1 = [a+modulus*b for a,b in zip(x1,d1)]
            r0 = [x//p for x in differences0]
            r1 = [x//p for x in differences1]
            modulus *= p
            digits += 1
            self.save_current(digits,modulus,x0,x1,r0,r1)
        a,b = recovered
        columns, free = self.minor["column_indices"], self.minor["free_normal_coordinate"]
        u = [(Fraction(0),Fraction(0)) for _ in range(RANK)]
        u[free] = (Fraction(1),Fraction(0))
        for j,aa,bb in zip(columns,a,b):
            u[j] = (aa,bb)
        denominator = lcm_den([x for pair in u for x in pair])
        u0 = [int(denominator*pair[0]) for pair in u]
        u1 = [int(denominator*pair[1]) for pair in u]
        U0,U1 = self.Zmat([[x] for x in u0]),self.Zmat([[x] for x in u1])
        H0,H1 = self.Zmat(self.H0),self.Zmat(self.H1)
        full0,full1 = H0*U0-H1*U1,H1*U0+(H0-H1)*U1
        assert all(int(full0[i,0]) == int(full1[i,0]) == 0 for i in range(RANK))
        h = [tuple(self.scales[i]*v/self.scales[free] for v in pair) for i,pair in enumerate(u)]
        assert h[free] == (1,0)
        assert all(tuple(self.scales[free]*v/self.scales[i] for v in pair) == u[i]
                   for i,pair in enumerate(h))
        self.refs["exact_socle"] = self.put("exact-original-normal-socle-vector", {
            "source_point_minor": self.refs["point_minor"], "source_integral_matrix": self.refs["integral_matrix"],
            "source_fixed_inverse": self.refs["fixed_inverse"],
            "source_successful_reconstruction": self.stage_files[PREFIX+f"RR-at-digits-{digits:06d}.json.gz"],
            "prime": self.minor["prime"], "Dixon_digits": digits,
            "normal_basis_rank": RANK, "free_original_normal_coordinate": free,
            "free_original_normal_coordinate_value_K_1_zeta": kdata((1,0)),
            "h_tau_K_1_zeta": [kdata(v) for v in h],
            "integral_system_kernel_u_K_1_zeta": [kdata(v) for v in u],
            "all_272_integral_K_equations_exactly_zero": True,
            "all_272_original_W_minus_w0_equations_exactly_verified": True,
            "original_column_scaling_restored_exactly": True,
            "exact_nonzero_original_normal_socle_vector_computed": True,
            "full_residual_K_1_zeta": [kdata((0,0)) for _ in range(RANK)],
            "no_characteristic_zero_determinant_computed": True})
        self.h = h

    def point_generators(self):
        old = self.load("two-chart-point-inverse-power-generators")
        if old is not None:
            self.refs["point_inverse_power"] = self.stage_files[PREFIX+"two-chart-point-inverse-power-generators.json.gz"]
            return
        self.check_time()
        h_sigma = [kmul(h,kpow(self.v0,-e)) for h,e in zip(self.h,EPS)]
        assert all(kmul(a,kpow(self.v0,e)) == b for a,b,e in zip(h_sigma,self.h,EPS))
        u0,u1 = [],[]
        for h,e in zip(self.h,EPS):
            if e == 0:
                a,b = (Fraction(0),Fraction(0)),(Fraction(0),Fraction(0))
            elif e == 1:
                a,b = kmul(h,self.z0),(Fraction(0),Fraction(0))
            else:
                b = kmul(h,kpow(self.z0,2))
                a = kmul(b,self.v0)
            u0.append(a);u1.append(b)
        for i,e in enumerate(EPS):
            # r_sigma-r_tau=(v-v0)*(u0+v*u1) in each original beta row.
            lhs = [(Fraction(0),Fraction(0)) for _ in range(3)]
            lhs[e] = kadd(lhs[e],h_sigma[i])
            lhs[0] = kadd(lhs[0],kneg(self.h[i]))
            rhs = [kneg(kmul(self.v0,u0[i])), kadd(u0[i],kneg(kmul(self.v0,u1[i]))), u1[i]]
            assert lhs == rhs
        charts = {}
        for chart,point,hvec in (("tau",self.z0,self.h),("sigma",self.v0,h_sigma)):
            charts[chart] = {
                "base_variable": "z" if chart == "tau" else "v=1/z",
                "normal_basis": "beta" if chart == "tau" else "gamma=v^epsilon beta",
                "numerator_constant_normal_vector_K_1_zeta": [kdata(v) for v in hvec],
                "denominator_polynomial_K_1_zeta": [kdata(kneg(point)),kdata((1,0))],
                "point_inverse_power": 254,
                "generator_expressions": ["1", "(normal_numerator/linear_denominator)^254"],
                "only_pole_on_original_affine_chart": "P0", "exact_pole_order_of_f": 1,
                "complete_inverse_ideal_certified_by_all_DVR_valuations": True,
                "exact_new_H_plus_P0_section": True,
                "full_H_plus_P0_basis_dimension": 147,
                "first_146_basis_members": ["1", "z" if chart == "tau" else "v", "normal_basis_1_through_144"],
            }
        self.refs["point_inverse_power"] = self.put("two-chart-point-inverse-power-generators", {
            "source_exact_socle": self.refs["exact_socle"], "source_P0_values": plain(self.values_source),
            "charts": charts, "normal_basis_degrees": EPS,
            "sigma_transport_all_272_exactly_verified": True,
            "overlap_f_sigma": "-z*z0*f_tau+u0+v*u1",
            "overlap_u_normal_vectors_K_1_zeta": [[kdata(v) for v in u0],[kdata(v) for v in u1]],
            "all_272_degree2_overlap_polynomial_identities_exactly_verified": True,
            "both_point_inverse_power_ideals_certified": True,
            "two_generator_power_equality_uses_curve_DVR_not_general_ring_binomial_claim": True,
            "optional_255_power_generator_transition": "binomial upper triangular; diagonal (-z*z0)^k",
            "all_147_basis_claims_use_original_V1_dimension_and_exact_P0_simple_pole": True})

    def module_DAGs(self):
        old = self.load("five-original-degree254-affine-module-DAGs")
        if old is not None:
            self.refs["five_modules"] = self.stage_files[PREFIX+"five-original-degree254-affine-module-DAGs.json.gz"]
            return
        self.check_time()
        nodes = []
        def node(operation, inputs, data, domain):
            payload = {"operation": operation, "inputs": inputs, "data": data, "domain": domain}
            name = "r868n"+fingerprint(payload)
            assert not any(v["id"] == name for v in nodes)
            nodes.append({"id":name,"ordinal":len(nodes),**payload})
            return name
        point_nodes = {}
        for chart in ("tau","sigma"):
            f = node("exact_original_normal_vector_over_linear_base_polynomial", [],
                     {"source": self.refs["point_inverse_power"], "chart": chart,
                      "source_group": "R868", "no_unexpanded_kernel_replaces_exact_vector": True}, "K(Y)")
            power = node("field_nonnegative_integer_power",[f],{"exponent":254},"K(Y)")
            point_nodes[chart] = node("fractional_ideal_generated_by_one_and_function",[power],
                                     {"exact_identity":"I_P0^(-254)","DVR_completeness_proof":"868.8/868.14"},"I_"+chart)
        outputs = {}
        for j,(p,q_) in enumerate(PQ,1):
            old_out = self.GP["five_original_polar_and_eta_outputs"][str(j)]
            outputs[str(j)] = {"p":p,"q":q_,"degree":254,"charts":{},
                               "eta_original_sign":-1,"eta_original_denominator":q_}
            for chart in ("tau","sigma"):
                old_root = old_out["eta_degree_zero_fractional_ideal"][chart]
                original = node("certified_original_external_fractional_ideal_DAG_root",[],
                                {"source_group":"R849","source":plain(self.GP_source),
                                 "source_configuration_sha256":self.item["sources"]["R849"]["configuration_sha256"],
                                 "source_node":old_root,"source_key":"eta_degree_zero_fractional_ideal",
                                 "original_j":j,"chart":chart,"original_line_bundle":"O(-Z_j)"},"I_"+chart)
                result = node("invertible_fractional_ideal_product",[original,point_nodes[chart]],
                              {"exact_identity":"L_j*I_P0^(-254)","original_line_bundle_unchanged":True},"I_"+chart)
                outputs[str(j)]["charts"][chart] = result
        self.refs["five_modules"] = self.put("five-original-degree254-affine-module-DAGs", {
            "source_original_global_eta_DAG": plain(self.GP_source),
            "source_original_global_producer": identity(self.item["sources"]["R849"]),
            "source_point_inverse_power": self.refs["point_inverse_power"],
            "external_original_graph_node_count": self.GP["actual_graph_node_count"],
            "graph_nodes": nodes, "actual_new_graph_node_count": len(nodes), "five_outputs": outputs,
            "both_chart_original_eta_root_keys_verified": True,
            "five_degree254_affine_module_DAGs_defined": True,
            "not_the_three_isogenous_real_descent_ideal": True,
            "point_power_uses_original_P0_not_pencil_fiber": True,
            "complete_original_parent_graph_and_leaf_identities_retained_by_R849_reference": True,
            "degree254_RR_basis_128_computed": False,
            "original_connection_or_height_computed": False,
            "next_complete_section_certificate": {"weight0":128,"weight1":144,
                "function_field_rank":272,"requires_exact_membership_in_both_original_chart_modules":True,
                "pushforward_split_type":"O^128 plus O(-1)^144","source_proof":"868.19-868.22"}})

    def inventory(self):
        # Bind every complete stage actually present; an old false FINAL never
        # supplies the inventory for a later checkpoint.
        entries = []
        for path in sorted(self.out.glob(PREFIX+"*.json.gz")):
            if path.name.startswith(PREFIX+"stage-manifest-") or path.name == PREFIX+"Dixon-current.json.gz":
                continue
            if path.name in self.stage_files:
                entry = self.stage_files[path.name]
                assert sha(path) == entry["sha256"] and path.stat().st_size == entry["bytes"]
            else:
                value = read(path)
                assert value["result"] == RESULT and value["configuration"] == self.tag
                assert value["complete"] is True
                entry = spec(path)
            entries.append(entry)
        identity_value = fingerprint(entries)[:20]
        path = self.out/(PREFIX+"stage-manifest-"+identity_value+".json.gz")
        value = {"result":RESULT,"configuration":self.tag,"complete":True,"files":entries,
                 "file_count":len(entries),"current_checkpoints_not_complete_stages":True}
        if not path.exists():
            save(path,value)
        else:
            assert read(path) == value
        return spec(path)

    def finish(self, reason=None, error=None):
        for key,name in (("point_minor","accepted-point-minor"),
                         ("exact_socle","exact-original-normal-socle-vector"),
                         ("point_inverse_power","two-chart-point-inverse-power-generators"),
                         ("five_modules","five-original-degree254-affine-module-DAGs")):
            if key not in self.refs and self.load(name) is not None:
                self.refs[key] = self.stage_files[PREFIX+name+".json.gz"]
        path = self.out/(PREFIX+"Dixon-current.json.gz")
        if path.exists():
            self.current = spec(path)
        complete = "five_modules" in self.refs and error is None
        manifest = self.inventory()
        value = {"result":RESULT,"configuration":self.tag,"complete":complete,"p":41,
                 "point_fiber_rank_271_certified":"point_minor" in self.refs,
                 "exact_normal_socle_vector_computed":"exact_socle" in self.refs,
                 "both_point_inverse_power_ideals_certified":"point_inverse_power" in self.refs,
                 "five_degree254_affine_module_DAGs_defined":complete,
                 "degree254_RR_basis_128_computed":False,"original_connection_or_height_computed":False,
                 "old_W_point_values_or_ideals_recomputed":False,
                 "source_audit":self.refs.get("source_audit"),
                 "integral_matrix":self.refs.get("integral_matrix"),
                 "point_minor":self.refs.get("point_minor"),"exact_socle":self.refs.get("exact_socle"),
                 "point_inverse_power":self.refs.get("point_inverse_power"),
                 "five_affine_module_DAGs":self.refs.get("five_modules"),
                 "stage_manifest":manifest,"current_checkpoint":self.current,
                 "seconds":time.monotonic()-self.started,"stop_reason":reason,"error":error}
        save(self.out/FINAL,value)
        return value

    def run(self):
        prior_path = self.out/FINAL
        if prior_path.exists():
            prior = read(prior_path)
            assert prior["result"] == RESULT and prior["configuration"] == self.tag
            if prior["complete"]:
                for key in ("source_audit","point_minor","exact_socle","point_inverse_power","five_affine_module_DAGs"):
                    self.own(prior[key])
                inventory = self.own(prior["stage_manifest"])
                for entry in inventory["files"]:
                    bound(self.out, entry)
                return prior
        self.integral_matrix()
        self.select_minor()
        self.exact_socle()
        self.point_generators()
        self.module_DAGs()
        return self.finish()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--config",required=True)
    parser.add_argument("--out",required=True)
    parser.add_argument("--budget-minutes",type=float,default=300)
    args = parser.parse_args()
    if hasattr(sys,"set_int_max_str_digits"):
        sys.set_int_max_str_digits(0)
    assert os.environ.get("GITHUB_ACTIONS") == "true", "new mathematics is authorized only in public Actions"
    started = time.monotonic()
    job,value,code,error = None,None,1,None
    try:
        job = Job(args)
        value = job.run()
        code = 0 if value["complete"] else 2
    except (BudgetStop,SearchStop) as exc:
        error = None
        code = 2
        if job is not None:
            value = job.finish(type(exc).__name__+": "+str(exc))
        else:
            error = type(exc).__name__+": "+str(exc)
    except Exception as exc:
        error = type(exc).__name__+": "+str(exc)
        traceback.print_exc()
        if job is not None:
            try:
                value = job.finish("error",error)
            except Exception:
                traceback.print_exc()
    out = Path(args.out)
    out.mkdir(parents=True,exist_ok=True)
    receipt = {"result":RESULT,"source_sha256":sha(__file__),"complete":bool(value and value["complete"]),
               "process_exit_code":code,"error":error,"seconds":time.monotonic()-started,
               "certificate_sha256":sha(out/FINAL) if value is not None else None,
               "stage_manifest":value["stage_manifest"] if value else None,
               "stop_reason":value.get("stop_reason") if value else None,
               "point_fiber_rank_271_certified":bool(value and value["point_fiber_rank_271_certified"]),
               "exact_normal_socle_vector_computed":bool(value and value["exact_normal_socle_vector_computed"]),
               "both_point_inverse_power_ideals_certified":bool(value and value["both_point_inverse_power_ideals_certified"]),
               "five_degree254_affine_module_DAGs_defined":bool(value and value["five_degree254_affine_module_DAGs_defined"]),
               "degree254_RR_basis_128_computed":False,"original_connection_or_height_computed":False}
    save(out/"core-receipt.json",receipt)
    print(json.dumps(receipt,sort_keys=True))
    return code


if __name__ == "__main__":
    sys.exit(main())
