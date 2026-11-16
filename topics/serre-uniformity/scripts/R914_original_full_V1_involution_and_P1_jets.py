#!/usr/bin/env python3
"""Original full V1 involution and P1 jets, with no local mathematical execution.

The existing R853 tau/sigma/w0 answers and the original R837 selected rows
are reused.  Only the other 143 exact right hand sides are solved.  New
arithmetic is restricted to the public repository's Actions.
"""
import argparse
import gzip
import hashlib
import json
import os
from pathlib import Path
import re
import sys
import time
import traceback

import flint
from flint import fmpq, fmpq_mat, nmod_mat, nmod_poly

RESULT = "R914-original-full-V1-involution-and-P1-local-jets"
FINAL = "p41-original-full-V1-involution-and-P1-jets-certificate.json"
PREFIX = "R914-iota-"
INVENTORY = PREFIX + "stage-manifest.json.gz"
CURRENT = PREFIX + "current.json.gz"
PRIME = 1000000753
DIM, XI, QORDERS, ROWS = 146, 40, 14, 560
RANK, LAST, COUNT = 272, 272, 273
GROUP_SIZE = 16
EPS = [0] + [1] * 144 + [2] * 127
SOURCES = ("R786", "R805", "R837", "R853", "R872", "R883")
PROOFS = ("R912", "R802", "R805", "R853", "R872", "R883")
BASE = ("result", "run_id", "source_commit", "core_sha256", "manifest_sha256")
META = ("public-actions-input.json", "run-receipt.json", "core-receipt.json")
H64 = re.compile(r"[0-9a-f]{64}")
FREE_BASIS = {"file": "R805-graded-free-basis.json.gz", "bytes": 11649,
              "sha256": "74311a7a143fafc43a36d1a43f6146e6aa3cb28809a020e3fa1337fdc4e475c9"}
NAMES = {
    "three": ("R853", "R853-three-exact-original-V1-conjugates.json.gz"),
    "three_audit": ("R853", "R853-original-V1-prefix-and-source-audit.json.gz"),
    "minor": ("R837", "R837-original-V1-reflection-minor.json.gz"),
    "point_values": ("R837", "R837-original-P0-evaluation.json.gz"),
    "free": ("R805", FREE_BASIS["file"]),
    "point_linearization": ("R872", "R872-point-linearization.json.gz"),
    "point_jets": ("R872", "R872-point-jets-index.json.gz"),
    "point_audit": ("R872", "R872-source-audit.json.gz"),
    "t_frame": ("R883", "R883-original-t-first-order-unit-and-frame-DAG.json.gz"),
}
DEFINITIONS = {
    "R786": ("R786-exact-original-power5-short-basis",
        "4508095a95a2bcaec8c8db8fcd550fbc618b017d2bc0007945783bc109dbf851",
        "p41-exact-original-power5-short-basis-certificate.json"),
    "R805": ("R805-original-affine-pencil-free-basis",
        "730a7d8f51d76d1153386c63f2e082285ada4573a2baf8d87d1825d3ce75b420",
        "p41-original-affine-pencil-free-basis-certificate.json"),
    "R837": ("R837-original-fixed-branch-pencil",
        "5702b42ee014ab7552e61383e24b738fe5ed48955dfc207ad3d85cae08e8b924",
        "p41-original-fixed-branch-pencil-certificate.json"),
    "R853": ("R853-original-semilinear-V1-generator-conjugates",
        "5b65e7ccf7c6663949155fdd30abc4c765823e861259c8f9b90b26d0bc1511df",
        "p41-original-semilinear-V1-conjugates-certificate.json"),
    "R872": ("R872-original-P0-jets-and-fixed-Picard-RR-spaces",
        "0e5897512a2f45baaed9cd1b6b2badcb6bf6ee2b100fcd45db871ad9f6db1874",
        "p41-original-P0-jets-and-fixed-Picard-RR-spaces-certificate.json"),
    "R883": ("R883-original-t-first-order-frame",
        "2778a81b5639a1eb6285718574af0ce4b48b00e92b648c6ac29ffe70c1da66f7",
        "p41-original-t-first-order-frame-certificate.json"),
}
STRATEGY = {
    "scope": "complete_original_K_linear_V1_iota_and_P1_local_transport_only",
    "geometric_involution": "iota=T^41, qY->-qY, t->1-t; K fixed",
    "arithmetic_cY_not_substituted_for_geometric_iota": True,
    "original_integer_V1_scale_already_in_source": "6724",
    "additional_scale_applied": False,
    "full_source_rows": ROWS,
    "original_V1_dimension": DIM,
    "old_exact_target_order": ["tau", "sigma", "w0"],
    "new_exact_rhs_indices": [i for i in range(DIM) if i not in (0, 2, 73)],
    "new_exact_rhs_count": 143,
    "reused_columns": "C[:,0]=old_tau; C[:,2]=old_w0; C[:,73]=old_sigma-C[:,1]",
    "selected_rows": "the unchanged R837 original exact-nonzero minor",
    "exact_verification": "S*C=diag((-1)^floor(row/40))*S on all560 rows; C*C=I146",
    "coordinate_field": "Q, extended K-linearly; original s and zeta fixed",
    "auxiliary_prime": PRIME,
    "prime_role": "reduction of exact C and transport of already completed R872 jets",
    "original_normal_degrees": EPS,
    "P0_parameter": "rho0=z-z0",
    "P1_parameter": "rho1=iota^*rho0=z-2*beta72-z0",
    "jet_first_order": 0,
    "jet_last_order": LAST,
    "normal_group_size": GROUP_SIZE,
    "P1_t_frame": "t1=t-1; c1=-c0; all original first3 coefficients transported by minus",
    "old_three_exact_solves_recomputed": False,
    "old_reflection_minor_or_Fourier_rows_recomputed": False,
    "old_P0_Hensel_recurrence_recomputed": False,
    "old_W_Gamma_or_Mg_recomputed": False,
    "endpoint_rank8_order_or_norms_computed": False,
    "only_budget_and_transport_paths_excluded_from_identity": True,
}


class BudgetStop(RuntimeError):
    pass


class UnitFailure(RuntimeError):
    pass


def sha(path):
    h = hashlib.sha256()
    with Path(path).open("rb") as stream:
        for block in iter(lambda: stream.read(4 * 1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()


def fingerprint(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":"),
                                    ensure_ascii=False).encode()).hexdigest()


def plain(value):
    row = {k: value[k] for k in ("file", "bytes", "sha256")}
    assert Path(row["file"]).name == row["file"] and "\\" not in row["file"]
    assert row["file"] not in (".", "..")
    assert isinstance(row["bytes"], int) and row["bytes"] >= 0
    assert H64.fullmatch(row["sha256"])
    return row


def spec(path):
    path = Path(path)
    return {"file": path.name, "bytes": path.stat().st_size, "sha256": sha(path)}


def read(path):
    path = Path(path)
    with (gzip.open(path, "rt", encoding="utf-8") if path.name.endswith(".gz")
          else path.open("r", encoding="utf-8")) as stream:
        return json.load(stream)


def save(path, value):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(path.name + ".tmp")
    payload = (json.dumps(value, sort_keys=True, separators=(",", ":"),
                          ensure_ascii=False) + "\n").encode()
    with temporary.open("wb") as raw:
        if path.name.endswith(".gz"):
            with gzip.GzipFile(filename="", fileobj=raw, mode="wb", mtime=0,
                               compresslevel=2) as stream:
                stream.write(payload)
        else:
            raw.write(payload)
        raw.flush()
        os.fsync(raw.fileno())
    temporary.replace(path)


def bound(folder, value):
    value = plain(value)
    path = Path(folder) / value["file"]
    assert spec(path) == value, str(path)
    return path


def identity(value):
    return {k: str(value[k]) for k in BASE}


def source_identity(value):
    return {**identity(value),
            "configuration_sha256": value["configuration_sha256"],
            "selected_files_sha256": value["selected_files_sha256"],
            "selected_file_count": value["selected_file_count"],
            "certificate": plain(value["certificate"])}


def expected_tag(item):
    return {"result": RESULT, "source_sha256": item["core_sha256"], "p": 41,
            "python_flint": "0.9.0", "prime": PRIME,
            "proofs_sha256": {k: item["proofs"][k]["sha256"] for k in PROOFS},
            "method_sha256": item["method_sha256"],
            "sources": {k: source_identity(item["sources"][k]) for k in SOURCES},
            "strategy": STRATEGY}


def qdecode(value):
    assert isinstance(value, list) and len(value) == 2 and int(value[1]) > 0
    return fmpq(int(value[0]), int(value[1]))


def qencode(value):
    return [str(value.numer()), str(value.denom())]


def qmod(value):
    den = int(value.denom()) % PRIME
    if not den:
        raise UnitFailure("An exact rational coefficient denominator is not a unit at the original p753 place.")
    return int(value.numer()) % PRIME * pow(den, -1, PRIME) % PRIME


def kdecode(value):
    assert isinstance(value, list) and len(value) == 2
    return tuple(qdecode(x) for x in value)


def kencode(value):
    return [qencode(x) for x in value]


def kmul(x, y):
    return (x[0] * y[0] - x[1] * y[1],
            x[0] * y[1] + x[1] * y[0] - x[1] * y[1])


def kinverse(x):
    norm = x[0] * x[0] - x[0] * x[1] + x[1] * x[1]
    assert norm != 0, "The original exact tau fibre frame must be nonzero."
    return ((x[0] - x[1]) / norm, -x[1] / norm)


def kmod(x, zeta):
    return (qmod(x[0]) + zeta * qmod(x[1])) % PRIME


def rows(matrix):
    return [[int(matrix[i, j]) for j in range(matrix.ncols())]
            for i in range(matrix.nrows())]


class Source:
    def __init__(self, label, item):
        self.label, self.item = label, item
        self.directory = Path(item["directory"])
        expected_result, expected_core, expected_final = DEFINITIONS[label]
        assert item["result"] == expected_result and item["core_sha256"] == expected_core
        self.identity = identity(item)
        self.files = {name: plain(row) for name, row in item["files"].items()}
        assert all(name == row["file"] for name, row in self.files.items())
        assert len(self.files) == item["selected_file_count"]
        assert fingerprint([self.files[n] for n in sorted(self.files)]) == item["selected_files_sha256"]
        for row in self.files.values():
            bound(self.directory, row)
        manifest = read(self.directory / "full-outputs-manifest.json")
        assert self.files["full-outputs-manifest.json"]["sha256"] == item["manifest_sha256"]
        assert manifest["result"] == expected_result
        self.all_files = {row["file"]: plain(row) for row in manifest["files"]}
        assert len(self.all_files) == len(manifest["files"])
        for name, row in self.files.items():
            if name != "full-outputs-manifest.json":
                assert self.all_files[name] == row, (label, name)
        self.certificate_spec = plain(item["certificate"])
        assert self.certificate_spec["file"] == expected_final
        assert self.files[expected_final] == self.certificate_spec
        self.certificate = read(self.directory / expected_final)
        assert self.certificate["complete"] is True and self.certificate["result"] == expected_result
        self.tag = self.certificate["configuration"]
        assert self.tag["result"] == expected_result and self.tag["source_sha256"] == expected_core
        assert fingerprint(self.tag) == item["configuration_sha256"]
        initial, run, core = [read(self.directory / name) for name in META]
        assert initial["result"] == run["result"] == core["result"] == expected_result
        assert initial["source_commit"] == run["source_commit"] == item["source_commit"]
        assert str(run["workflow_run_id"]) == str(item["run_id"])
        assert initial["core_sha256"] == core["source_sha256"] == expected_core
        assert run["complete"] is True and run["process_exit_code"] == 0 and run.get("error") is None
        assert core["complete"] is True and core["certificate_sha256"] == self.certificate_spec["sha256"]
        assert run["core_receipt_sha256"] == self.files["core-receipt.json"]["sha256"]
        self.cache = {}

    def ref(self, name):
        return {"source_group": self.label, **self.files[name]}

    def stage(self, name):
        if name not in self.cache:
            assert name in self.files and self.files[name] == self.all_files[name]
            value = read(self.directory / name)
            assert value["complete"] is True and value["configuration"] == self.tag
            assert value.get("result", self.tag["result"]) == self.identity["result"]
            self.cache[name] = value
        return self.cache[name]


class Job:
    def __init__(self, args):
        self.args, self.out = args, Path(args.out)
        self.out.mkdir(parents=True, exist_ok=True)
        self.started = time.monotonic()
        self.deadline = self.started + 60 * args.budget_minutes
        self.item = read(args.config)
        assert self.item["result"] == RESULT and self.item["p"] == 41
        assert self.item["producer_inputs_pending"] is False
        assert self.item["core"] == Path(__file__).name and self.item["core_sha256"] == sha(__file__)
        assert 0 < args.budget_minutes <= 300 and flint.__version__ == "0.9.0"
        assert set(self.item["sources"]) == set(SOURCES)
        assert set(self.item["proofs"]) == set(PROOFS)
        for key in PROOFS:
            assert sha(self.item["proofs"][key]["file"]) == self.item["proofs"][key]["sha256"]
        assert sha(self.item["method"]) == self.item["method_sha256"]
        self.sources = {k: Source(k, self.item["sources"][k]) for k in SOURCES}
        self.tag = expected_tag(self.item)
        self.refs = {}
        self.current = None
        self.A = None
        self.C = None
        self.Cmod = None
        self.P0 = None
        self.P1 = None

    def budget(self):
        if time.monotonic() >= self.deadline:
            raise BudgetStop("R914 iota transport budget; completed source-bound stages retained.")

    def path(self, name):
        if not name.endswith(".json.gz"):
            name += ".json.gz"
        assert Path(name).name == name and name.startswith(PREFIX)
        return self.out / name

    def old(self, name):
        path = self.path(name)
        if not path.exists():
            return None
        data = read(path)
        assert data["result"] == RESULT and data["configuration"] == self.tag
        assert data["complete"] is True
        return data

    def stage(self, suffix, key, produce):
        name = PREFIX + suffix
        old = self.old(name)
        if old is None:
            self.budget()
            value = produce()
            old = dict(value, result=RESULT, configuration=self.tag, complete=True)
            save(self.path(name), old)
            print("R914_IOTA_STAGE=" + json.dumps(spec(self.path(name)), sort_keys=True), flush=True)
        self.refs[key] = spec(self.path(name))
        return old

    def checkpoint(self, phase, **values):
        data = {"result": RESULT, "configuration": self.tag, "complete": False,
                "phase": phase, "elapsed_seconds": time.monotonic() - self.started, **values}
        save(self.out / CURRENT, data)
        self.current = spec(self.out / CURRENT)

    def named(self, key):
        label, name = NAMES[key]
        return self.sources[label].stage(name)

    def ref(self, key):
        label, name = NAMES[key]
        return self.sources[label].ref(name)

    def prepare(self):
        r786, r805, r837, r853, r872, r883 = [self.sources[k] for k in SOURCES]
        assert identity(r837.tag["sources"]["R786"]) == r786.identity
        for label in ("R786", "R837"):
            assert identity(r853.tag["sources"][label]) == self.sources[label].identity
        assert identity(r872.tag["sources"]["R805"]) == r805.identity
        assert identity(r883.tag["sources"]["R872"]["identity"]) == r872.identity
        self.three = self.named("three")
        self.three_audit = self.named("three_audit")
        self.minor = self.named("minor")
        self.values = self.named("point_values")
        self.free = self.named("free")
        self.linear = self.named("point_linearization")
        self.jets = self.named("point_jets")
        self.point_audit = self.named("point_audit")
        self.t_frame = self.named("t_frame")
        assert plain(r853.certificate["three_conjugate_coordinates"]) == plain(self.ref("three"))
        assert plain(r853.certificate["source_audit"]) == plain(self.ref("three_audit"))
        assert plain(r805.certificate["graded_free_basis_stage"]) == FREE_BASIS
        assert plain(self.ref("free")) == FREE_BASIS
        assert plain(self.three_audit["original_normal_free_basis"]) == FREE_BASIS
        assert plain(self.point_audit["source_free_basis"]) == FREE_BASIS
        assert self.free["degree0_basis"] == "1"
        assert self.free["degree1_original_indices"] == list(range(2, DIM))
        assert self.free["degree_distribution"] == [1, 144, 127]
        assert self.free["affine_free_module_rank"] == RANK
        assert self.free["characteristic_zero_complement_certified"] is True
        assert r805.certificate["actual_pencil_n"] == 1
        self.leaves = self.free["degree2_original_M2_leaves"]
        assert len(self.leaves) == 127
        assert all(len(pair) == 2 and all(isinstance(i, int) and 0 <= i < DIM for i in pair)
                   for pair in self.leaves)
        assert self.three["target_order"] == ["tau", "sigma", "w0"]
        assert self.three["coordinate_matrix_shape"] == [DIM, 3]
        assert self.three["all560_original_coordinates_verified_for_each_conjugate"] is True
        assert self.three["twice_original_semilinear_action_verified_in_all560_coordinates"] is True
        self.three_raw = self.three["coordinates_in_original_integer_scaled_V1_basis"]
        assert len(self.three_raw) == DIM and all(len(row) == 3 for row in self.three_raw)
        assert self.minor["matrix_shape"] == [ROWS, DIM]
        assert self.minor["actual_modular_rank"] == self.minor["expected_characteristic_zero_rank"] == DIM
        assert self.minor["selected_columns"] == list(range(DIM))
        assert self.minor["minor_determinant_mod_prime"] != 0
        self.selected = self.minor["selected_rows"]
        assert len(self.selected) == len(set(self.selected)) == DIM
        assert all(isinstance(i, int) and 0 <= i < ROWS for i in self.selected)
        attempt_spec = plain(self.minor["successful_attempt"])
        assert r837.files[attempt_spec["file"]] == attempt_spec
        attempt = r837.stage(attempt_spec["file"])
        for key in ("matrix_shape", "actual_modular_rank", "selected_rows", "selected_columns",
                    "prime", "prime_index", "minor_determinant_mod_prime"):
            assert attempt[key] == self.minor[key]
        assert self.three["original_selected_rows"] == self.selected
        assert self.three_audit["selected_original_prefix_rows"] == self.selected
        assert plain(self.values["minor"]) == plain(self.ref("minor"))
        assert self.values["original_P0_evaluation_certified"] is True
        assert self.values["all_146_reflected_outputs_verified"] is True
        assert self.values["integer_scale_already_in_source"] == "6724"
        assert self.values["additional_scale_inserted"] is False
        assert self.jets["prime"] == self.linear["prime"] == PRIME
        assert self.jets["first_order"] == 0 and self.jets["last_order"] == LAST
        assert self.jets["coefficient_count"] == COUNT and self.jets["normal_basis_rank"] == RANK
        assert self.jets["local_parameter"] == self.linear["chosen_local_parameter"] == "z_minus_z0"
        assert plain(self.jets["source_point_linearization"]) == plain(self.ref("point_linearization"))
        assert self.jets["all273_orders_and_all272_normal_equations_verified"] is True
        assert plain(r872.certificate["point_jets"]) == plain(self.ref("point_jets"))
        assert plain(r872.certificate["point_linearization"]) == plain(self.ref("point_linearization"))
        assert self.point_audit["chosen_parameter_derivative_is_a_unit"] is True
        assert plain(self.point_audit["source_point_linearization"]) == plain(self.ref("point_linearization"))
        self.zeta = int(self.jets["original_zeta_root"])
        assert self.zeta == int(self.point_audit["original_zeta_root"])
        assert self.zeta == int(r883.certificate["original_zeta_root"])
        assert (self.zeta * self.zeta + self.zeta + 1) % PRIME == 0
        self.z0 = int(self.linear["z0_mod_prime"])
        self.w0 = int(self.linear["w0_mod_prime"])
        assert self.t_frame["original_t_first_order_unit_certified"] is True
        assert plain(r883.certificate["stages"][NAMES["t_frame"][1][:-8]]) == plain(self.ref("t_frame"))
        assert self.t_frame["exact_c_expression"]["underlying_original_Hensel_source"] == self.point_audit["exact_local_source"]
        assert self.t_frame["original_s_root"] == (2 * self.zeta + 1) % PRIME
        self.prefix_refs = []
        columns = []
        for i in range(DIM):
            self.budget()
            name = f"R786-exact-power-1-row-{i:04d}.json.gz"
            value = r786.stage(name)
            assert value["weight"] == 2 and value["bound_qY"] == 128
            assert value["integer_scale"] == "6724"
            assert value["original_R775_finite_coefficients_verified"] is True
            assert value["recipe"]["kind"] == "det_semilinear_E1_pair_trace"
            assert value["recipe"]["exact_global_field"] == "K"
            raw = value["integer_qY_xi_coefficients"]
            assert len(raw) == 129 and all(len(row) == XI for row in raw)
            columns.append([int(raw[n][r]) for n in range(QORDERS) for r in range(XI)])
            self.prefix_refs.append(r786.ref(name))
        assert [plain(r) for r in self.prefix_refs] == [plain(r) for r in self.three["original_R786_prefix_rows"]]
        self.A = [[columns[j][i] for j in range(DIM)] for i in range(ROWS)]
        self.old_order_refs = [plain(x) for x in self.jets["orders"]]
        assert len(self.old_order_refs) == COUNT
        assert len({x["file"] for x in self.old_order_refs}) == COUNT
        for n, row in enumerate(self.old_order_refs):
            assert row["file"] == f"R872-point-jet-{n:04d}.json.gz"
            assert r872.files[row["file"]] == row
        self.stage("source-audit", "source_audit", lambda: {
            "source_identities": {k: source_identity(self.item["sources"][k]) for k in SOURCES},
            "inputs": {k: self.ref(k) for k in NAMES},
            "original_R786_prefix_rows": self.prefix_refs,
            "old_R837_selected_rows": self.selected,
            "old_R837_successful_attempt": r837.ref(attempt_spec["file"]),
            "old_three_exact_solutions_reused": True,
            "original_normal_free_basis": self.ref("free"),
            "original_normal_basis_degrees": EPS,
            "original_R872_jet_index": self.ref("point_jets"),
            "original_jet_orders": self.old_order_refs,
            "prime": PRIME, "original_zeta_root": self.zeta,
            "original_s_root": (2 * self.zeta + 1) % PRIME,
            "original_V1_integer_scale_already_applied": "6724",
            "additional_integer_scale_inserted": False,
            "all_original_source_tags_and_bytes_verified": True,
            "old_source_mathematics_recomputed": False,
        })
        self.checkpoint("sources_verified")

    def exact_matrix(self):
        def produce():
            self.budget()
            columns = STRATEGY["new_exact_rhs_indices"]
            square = fmpq_mat([self.A[r] for r in self.selected])
            rhs = fmpq_mat([[(-1 if (r // XI) % 2 else 1) * self.A[r][j]
                             for j in columns] for r in self.selected])
            new = square.solve(rhs)
            assert square * new == rhs
            C = fmpq_mat(DIM, DIM)
            for j, original_column in enumerate(columns):
                for i in range(DIM):
                    C[i, original_column] = new[i, j]
            for i in range(DIM):
                C[i, 0] = qdecode(self.three_raw[i][0])
                C[i, 2] = qdecode(self.three_raw[i][2])
                C[i, 73] = qdecode(self.three_raw[i][1]) - C[i, 1]
            selected_rhs = fmpq_mat([[(-1 if (r // XI) % 2 else 1) * self.A[r][j]
                                      for j in range(DIM)] for r in self.selected])
            assert square * C == selected_rhs
            return {"source_audit": self.refs["source_audit"],
                "source_old_three_conjugates": self.ref("three"),
                "source_original_minor": self.ref("minor"),
                "original_selected_rows": self.selected,
                "coordinate_matrix_shape": [DIM, DIM],
                "coordinates_in_original_integer_scaled_V1_basis": [
                    [qencode(C[i, j]) for j in range(DIM)] for i in range(DIM)],
                "new_rhs_original_indices": columns, "new_exact_right_hand_side_count": len(columns),
                "old_rhs_recomputed": False,
                "column73_definition": "old_sigma_column minus newly solved original column1",
                "all_selected_exact_equations_multiplied_back": True,
                "coefficient_field": "Q, extended K-linearly",
                "full_global_action_certified_by_this_stage_alone": False}
        data = self.stage("exact-V1-coordinate-matrix", "exact_matrix", produce)
        assert data["new_rhs_original_indices"] == STRATEGY["new_exact_rhs_indices"]
        raw = data["coordinates_in_original_integer_scaled_V1_basis"]
        assert len(raw) == DIM and all(len(r) == DIM for r in raw)
        self.C = fmpq_mat([[qdecode(x) for x in r] for r in raw])
        self.checkpoint("exact_matrix_ready")

    def verify_exact_action(self):
        def produce():
            A = fmpq_mat(self.A)
            rhs = fmpq_mat([[(-1 if (r // XI) % 2 else 1) * x for x in self.A[r]]
                            for r in range(ROWS)])
            assert A * self.C == rhs
            I = fmpq_mat([[int(i == j) for j in range(DIM)] for i in range(DIM)])
            assert self.C * self.C == I
            for i in range(DIM):
                assert self.C[i, 0] == qdecode(self.three_raw[i][0])
                assert self.C[i, 2] == qdecode(self.three_raw[i][2])
                assert self.C[i, 1] + self.C[i, 73] == qdecode(self.three_raw[i][1])
                assert self.C[i, 0] == int(i == 0)
                assert self.C[i, 2] == int(i == 2)
            return {"source_exact_coordinate_matrix": self.refs["exact_matrix"],
                "source_original_minor": self.ref("minor"),
                "source_old_three_conjugates": self.ref("three"),
                "all560_by146_original_exact_Fourier_equations_verified": True,
                "full_verified_exact_equation_count": ROWS * DIM,
                "exact_matrix_square_is_identity146": True,
                "three_old_exact_answers_preserved_including_sigma_e1_plus_e73": True,
                "geometric_iota_K_linear_on_original_V1_certified": True,
                "coefficient_conjugation_performed": False,
                "full_normal272_semilinear_matrix_computed": False,
                "original_tau_and_w0_fixed_exactly": True,
                "original_R802_action_and_R837_injectivity_used": True}
        self.stage("exact-full-V1-action-verification", "exact_verification", produce)
        self.checkpoint("exact_global_iota_certified")

    def reduce_matrix(self):
        def produce():
            reduced = [[qmod(self.C[i, j]) for j in range(DIM)] for i in range(DIM)]
            C = nmod_mat(reduced, PRIME)
            assert C * C == nmod_mat([[int(i == j) for j in range(DIM)] for i in range(DIM)], PRIME)
            return {"prime": PRIME, "original_zeta_root": self.zeta,
                "source_exact_matrix": self.refs["exact_matrix"],
                "source_exact_action_verification": self.refs["exact_verification"],
                "coordinate_matrix_mod_prime": reduced, "matrix_shape": [DIM, DIM],
                "all_exact_coordinate_denominators_units_at_original_place": True,
                "original_minor_inverse_mod_prime_computed": False,
                "original_selected_minor_may_have_a_different_witness_prime": True}
        data = self.stage("original-p753-coordinate-matrix", "modular_matrix", produce)
        self.Cmod = nmod_mat(data["coordinate_matrix_mod_prime"], PRIME)

    def old_P0_V1_jets(self):
        def produce():
            out = []
            previous = None
            r872 = self.sources["R872"]
            for n, row in enumerate(self.old_order_refs):
                self.budget()
                value = r872.stage(row["file"])
                assert value["order"] == n and value["local_parameter"] == "z_minus_z0"
                assert value["source_previous_order"] == previous
                assert plain(value["source_point_linearization"]) == plain(self.ref("point_linearization"))
                assert value["all272_original_eigenvector_equations_verified_at_this_order"] is True
                assert value["beta0_and_beta1_normalizations_verified"] is True
                beta = [int(x) for x in value["normal_basis_jet_mod_prime"]]
                assert len(beta) == RANK and all(0 <= x < PRIME for x in beta)
                assert beta[0] == int(n == 0)
                z = int(value["z_jet_mod_prime"])
                assert z == (self.z0 if n == 0 else int(n == 1))
                assert beta[1] == value["w_jet_mod_prime"]
                out.append([int(n == 0), (z - beta[72]) % PRIME] + beta[1:145])
                previous = row
            assert len(out) == COUNT and all(len(x) == DIM for x in out)
            return {"prime": PRIME, "source_original_point_jets": self.ref("point_jets"),
                "source_original_point_linearization": self.ref("point_linearization"),
                "source_original_normal_free_basis": self.ref("free"),
                "matrix_shape": [COUNT, DIM], "matrix_mod_prime": out,
                "row_orders": list(range(COUNT)), "original_V1_columns": list(range(DIM)),
                "function_order": "e0/tau=1,e1/tau=z-beta72,ei/tau=beta_(i-1) for i=2..145",
                "local_parameter": "rho0=z-z0", "old273_Hensel_coefficients_recomputed": False,
                "only_rearrangement_and_original_linear_combination_of_completed_jets": True,
                "extra_integer_scale_applied": False}
        data = self.stage("original-P0-V1-jets", "P0_V1_jets", produce)
        self.P0 = nmod_mat(data["matrix_mod_prime"], PRIME)

    def P1_V1_jets(self):
        def produce():
            result = self.P0 * self.Cmod
            assert result * self.Cmod == self.P0
            matrix = rows(result)
            assert all(matrix[n][0] == int(n == 0) for n in range(COUNT))
            assert all(matrix[n][2] == int(self.P0[n, 2]) for n in range(COUNT))
            for n in range(COUNT):
                assert (matrix[n][1] + matrix[n][73]) % PRIME == (int(self.P0[n, 1]) - int(self.P0[n, 73])) % PRIME
            return {"prime": PRIME, "original_zeta_root": self.zeta,
                "source_original_P0_V1_jets": self.refs["P0_V1_jets"],
                "source_full_exact_iota_matrix": self.refs["exact_matrix"],
                "source_reduced_iota_matrix": self.refs["modular_matrix"],
                "matrix_shape": [COUNT, DIM], "matrix_mod_prime": matrix,
                "row_orders": list(range(COUNT)), "original_V1_columns": list(range(DIM)),
                "local_parameter": "rho1=iota^*rho0=z-2*beta72-z0",
                "source_point": "P0", "target_point": "P1=iota(P0)",
                "K_coefficients_conjugated": False,
                "all273_rows_transported_by_the_full146_matrix": True,
                "all273_rows_transport_back_to_original_P0": True,
                "original_tau_and_w0_fixed": True,
                "z_transport_is_z_minus_two_beta72": True,
                "exact_characteristic_zero_jet_definition": {
                    "operation": "right_multiply_original_Hensel_V1_row_by_exact_Ciota",
                    "original_Hensel_index": self.ref("point_jets"),
                    "exact_Ciota": self.refs["exact_matrix"],
                    "precision_coefficients": COUNT},
                "characteristic_zero_positive_order_jet_coefficients_reconstructed": False,
                "old_Hensel_recurrence_reexecuted": False}
        data = self.stage("P1-V1-jets", "P1_V1_jets", produce)
        self.P1 = nmod_mat(data["matrix_mod_prime"], PRIME)

    def exact_points(self):
        def produce():
            cm0 = [kdecode(x) for x in self.values["P0_values_K_1_zeta"]]
            cm1 = [kdecode(x) for x in self.values["P1_values_K_1_zeta"]]
            assert len(cm0) == len(cm1) == DIM and cm0[0] == cm1[0]
            inv_tau = kinverse(cm0[0])
            e0 = [kmul(x, inv_tau) for x in cm0]
            e1 = [kmul(x, inv_tau) for x in cm1]
            for c in range(2):
                source = fmpq_mat([[x[c] for x in e0]])
                assert source * self.C == fmpq_mat([[x[c] for x in e1]])
            mod0 = [kmod(x, self.zeta) for x in e0]
            mod1 = [kmod(x, self.zeta) for x in e1]
            assert mod0 == [int(self.P0[0, j]) for j in range(DIM)]
            assert mod1 == [int(self.P1[0, j]) for j in range(DIM)]
            beta1 = [(fmpq(1), fmpq(0))] + e1[2:]
            beta1.extend(kmul(e1[i], e1[j]) for i, j in self.leaves)
            assert len(beta1) == RANK
            z0 = tuple(e0[1][c] + e0[73][c] for c in range(2))
            z1 = tuple(e1[1][c] + e1[73][c] for c in range(2))
            assert kmod(z0, self.zeta) == self.z0
            assert tuple(z1[c] - 2 * beta1[72][c] - z0[c] for c in range(2)) == (0, 0)
            return {"prime": PRIME, "original_zeta_root": self.zeta,
                "source_original_P0_P1_CM_values": self.ref("point_values"),
                "source_original_free_basis": self.ref("free"),
                "source_exact_iota_matrix": self.refs["exact_matrix"],
                "source_P1_V1_jets": self.refs["P1_V1_jets"],
                "coefficient_basis": ["1", "zeta=(-1+sqrt(-3))/2"],
                "original_tau_normalized_P1_V1_values_K_1_zeta": [kencode(x) for x in e1],
                "original_P1_normal_values_K_1_zeta": [kencode(x) for x in beta1],
                "original_z0_K_1_zeta": kencode(z0),
                "original_z_P1_K_1_zeta": kencode(z1),
                "original_P1_normal_values_mod_prime": [kmod(x, self.zeta) for x in beta1],
                "both_original146_zero_order_rows_match_completed_P0_and_P1_values": True,
                "exact_K_point_row_transport_multiplied_back": True,
                "rho1_at_original_P1_exactly_zero": True,
                "original_CM_common_frame_cancelled_once_by_actual_tau": True,
                "old_CM_values_recomputed": False,
                "all_normalized_point_denominators_units_at_original_place": True}
        return self.stage("exact-original-P1-point-and-zero-order", "point_check", produce)

    def normal_jets(self, point_check):
        groups = []
        for first in range(0, RANK, GROUP_SIZE):
            stop = min(RANK, first + GROUP_SIZE)
            def produce(first=first, stop=stop):
                columns, recipes = [], []
                for i in range(first, stop):
                    self.budget()
                    if i == 0:
                        column = [int(n == 0) for n in range(COUNT)]
                        recipe = {"normal_basis_row": i, "operation": "constant_one"}
                    elif i <= 144:
                        column = [int(self.P1[n, i + 1]) for n in range(COUNT)]
                        recipe = {"normal_basis_row": i, "operation": "original_M2_div_tau", "original_M2_index": i + 1}
                    else:
                        a, b = self.leaves[i - 145]
                        pa = nmod_poly([int(self.P1[n, a]) for n in range(COUNT)], PRIME)
                        pb = nmod_poly([int(self.P1[n, b]) for n in range(COUNT)], PRIME)
                        product = pa * pb
                        column = [int(product[n]) for n in range(COUNT)]
                        recipe = {"normal_basis_row": i, "operation": "original_M2_product_div_tau2", "original_M2_leaves": [a, b]}
                    assert column[0] == point_check["original_P1_normal_values_mod_prime"][i]
                    columns.append(column)
                    recipes.append(recipe)
                return {"prime": PRIME, "original_zeta_root": self.zeta,
                    "source_P1_V1_jets": self.refs["P1_V1_jets"],
                    "source_original_R805_free_basis": self.ref("free"),
                    "source_exact_original_point_check": self.refs["point_check"],
                    "first_normal_row": first, "stop_normal_row": stop,
                    "normal_basis_rows": list(range(first, stop)),
                    "row_orders": list(range(COUNT)), "matrix_shape": [COUNT, stop - first],
                    "normal_basis_jet_matrix_mod_prime": [[columns[j][n] for j in range(stop - first)] for n in range(COUNT)],
                    "original_recipes": recipes,
                    "local_parameter": "rho1=iota^*rho0=z-2*beta72-z0",
                    "degree2_recipes_use_only_the_original_two_M2_leaves": True,
                    "all_group_zero_order_coefficients_equal_exact_original_P1_values": True,
                    "additional_integer_scale_applied": False,
                    "exact_jet_definitions_are_original_Hensel_then_full_iota_then_original_recipes": True,
                    "rational_positive_order_jet_coefficients_reconstructed": False}
            key = f"normal_group_{first // GROUP_SIZE:03d}"
            data = self.stage(f"P1-normal-jets-group-{first // GROUP_SIZE:03d}", key, produce)
            assert data["first_normal_row"] == first and data["stop_normal_row"] == stop
            groups.append(self.refs[key])
            self.checkpoint("normal_jet_transport", completed_normal_rows=stop, completed_groups=groups)
        index = self.stage("P1-normal-jets-index", "P1_normal_jets", lambda: {
            "prime": PRIME, "original_zeta_root": self.zeta,
            "original_normal_basis_degrees": EPS, "normal_basis_rank": RANK,
            "first_order": 0, "last_order": LAST, "coefficient_count": COUNT,
            "normal_groups": groups, "source_P1_V1_jets": self.refs["P1_V1_jets"],
            "source_exact_original_point_check": self.refs["point_check"],
            "source_original_R805_free_basis": self.ref("free"),
            "source_original_P0_jets": self.ref("point_jets"),
            "source_exact_full_V1_action": self.refs["exact_verification"],
            "local_parameter": "rho1=iota^*rho0=z-2*beta72-z0",
            "all272_original_normal_functions_transported_through_order272": True,
            "complete_original_K_function_transport_defined": True,
            "old_P0_jets_or_W_equations_recomputed": False,
            "new_endpoint_rank8_algebra_computed": False,
            "all_coefficients_are_reductions_of_exact_original_transport_definitions": True})
        assert index["normal_groups"] == groups

    def P1_frame(self):
        def produce():
            t0 = [int(x) for x in self.t_frame["original_t_first_three_coefficients_mod_prime"]]
            assert len(t0) == 3 and t0[0] == 0
            c0 = int(self.t_frame["original_t_over_rho_constant_mod_prime"])
            assert c0 == t0[1] and 0 < c0 < PRIME
            t1 = [(-x) % PRIME for x in t0]
            assert t1[1] != 0
            # rho1, evaluated on the transported P1 branch, must be precisely rho.
            for n in range(COUNT):
                actual = (int(self.P1[n, 1]) - int(self.P1[n, 73]) - (self.z0 if n == 0 else 0)) % PRIME
                assert actual == int(n == 1)
            return {"prime": PRIME, "original_zeta_root": self.zeta,
                "original_s_root": (2 * self.zeta + 1) % PRIME,
                "source_original_R883_t_frame": self.ref("t_frame"),
                "source_P1_V1_jets": self.refs["P1_V1_jets"],
                "source_complete_P1_normal_jets": self.refs["P1_normal_jets"],
                "source_exact_original_point_check": self.refs["point_check"],
                "source_full_V1_action": self.refs["exact_verification"],
                "P0_parameter": "rho0=z-z0",
                "P1_parameter": "rho1=iota^*rho0=z-2*beta72-z0",
                "rho1_is_not_replaced_by_z_minus_zP1": True,
                "rho1_on_P1_branch_equals_parameter_to_all273_available_coefficients": True,
                "original_P1_t_parameter": "t1=t-1",
                "exact_c1_expression": {"operation": "negate_original_c0",
                    "source_original_t_frame": self.ref("t_frame"),
                    "source_exact_c0_expression": self.t_frame["exact_c_expression"],
                    "reason": "iota^*t=1-t and rho1=iota^*rho0; K fixed"},
                "original_c0_mod_prime": c0, "original_c1_mod_prime": t1[1],
                "original_t1_first_three_coefficients_mod_prime": t1,
                "known_t1_coefficient_count": 3,
                "all273_t_coefficients_computed": False,
                "actual_original_P1_t_first_order_unit_certified": True,
                "frame_conversion": "L*rho1^m=(L*c1^(-m))*t1^m*(1+O(t1)); negative order uses positive c1 power",
                "no_frame_scalar_suppressed_or_normalized_to_one": True,
                "new_CM_period_or_R883_evaluation_computed": False,
                "characteristic_zero_c1_rational_coefficients_expanded": False,
                "endpoint_norm_det_fibre_or_full_rigidification_computed": False}
        self.stage("original-P1-parameter-and-t-frame", "P1_frame", produce)

    def inventory(self):
        entries = []
        for path in sorted(self.out.glob(PREFIX + "*.json.gz")):
            if path.name in (INVENTORY, CURRENT):
                continue
            value = read(path)
            assert value["result"] == RESULT and value["configuration"] == self.tag
            assert value["complete"] is True
            entries.append(spec(path))
        value = {"result": RESULT, "configuration": self.tag, "complete": True,
                 "files": entries, "only_actual_complete_stages_listed": True,
                 "current_checkpoint_excluded": True}
        save(self.out / INVENTORY, value)
        return spec(self.out / INVENTORY)

    def finish(self, complete, reason):
        inventory = self.inventory()
        final = {"result": RESULT, "configuration": self.tag, "complete": bool(complete),
            "p": 41, "prime": PRIME, "source_identities": self.tag["sources"],
            "source_audit": self.refs.get("source_audit"),
            "exact_full_V1_coordinate_matrix": self.refs.get("exact_matrix"),
            "exact_full_V1_verification": self.refs.get("exact_verification"),
            "coordinate_matrix_at_original_place": self.refs.get("modular_matrix"),
            "original_P0_V1_jet_representation": self.refs.get("P0_V1_jets"),
            "original_P1_V1_jets": self.refs.get("P1_V1_jets"),
            "original_P1_point_check": self.refs.get("point_check"),
            "original_P1_normal_jets": self.refs.get("P1_normal_jets"),
            "original_P1_parameter_and_t_frame": self.refs.get("P1_frame"),
            "actual_full146_exact_geometric_iota_certified": bool(self.refs.get("exact_verification")),
            "actual_original_P1_normal_jets_through_order272_computed": bool(self.refs.get("P1_normal_jets")),
            "actual_original_P1_t_first_order_unit_certified": bool(self.refs.get("P1_frame")),
            "new_exact_right_hand_side_count": 143 if self.refs.get("exact_matrix") else 0,
            "old_three_RHS_old_minor_and_old_Hensel_jets_recomputed": False,
            "full272_semilinear_normal_matrix_computed": False,
            "endpoint_rank8_integral_algebras_computed": False,
            "endpoint_NmPhi_detU_and_reference_frames_evaluated": False,
            "nine_norm_P0_P1_rigidification_computed": False,
            "Poincare_period_theta_or_height_computed": False,
            "stage_manifest": inventory, "resume_state": self.current,
            "stop_reason": reason, "seconds": time.monotonic() - self.started}
        if complete:
            assert all(final[k] for k in ("actual_full146_exact_geometric_iota_certified",
                "actual_original_P1_normal_jets_through_order272_computed",
                "actual_original_P1_t_first_order_unit_certified"))
        save(self.out / FINAL, final)
        return final

    def run(self):
        if (self.out / FINAL).exists():
            previous = read(self.out / FINAL)
            assert previous["result"] == RESULT and previous["configuration"] == self.tag
            if previous["complete"] is True:
                inventory = read(bound(self.out, previous["stage_manifest"]))
                assert inventory["complete"] is True and inventory["configuration"] == self.tag
                for row in inventory["files"]:
                    value = read(bound(self.out, row))
                    assert value["complete"] is True and value["configuration"] == self.tag
                if previous.get("resume_state") is not None:
                    bound(self.out, previous["resume_state"])
                return previous
        self.prepare()
        self.exact_matrix()
        self.verify_exact_action()
        self.reduce_matrix()
        self.old_P0_V1_jets()
        self.P1_V1_jets()
        points = self.exact_points()
        self.normal_jets(points)
        self.P1_frame()
        self.checkpoint("complete")
        return self.finish(True, None)


def main():
    if os.environ.get("GITHUB_ACTIONS") != "true" or \
       os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public":
        raise SystemExit("All new R914 mathematics is restricted to the public repository Actions.")
    sys.set_int_max_str_digits(0)
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config", required=True)
    parser.add_argument("--out", required=True)
    parser.add_argument("--budget-minutes", type=float, default=300)
    args = parser.parse_args()
    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    started, job, final, error, code = time.monotonic(), None, None, None, 0
    try:
        job = Job(args)
        final = job.run()
    except BudgetStop as exc:
        code, error = 124, {"type": "BudgetStop", "message": str(exc)}
    except UnitFailure as exc:
        code, error = 2, {"type": "UnitFailure", "message": str(exc),
                          "no_characteristic_zero_failure_asserted": True}
    except BaseException as exc:
        code, error = 1, {"type": type(exc).__name__, "message": str(exc)}
        traceback.print_exc()
    if job is not None and final is None:
        try:
            final = job.finish(False, error)
        except BaseException:
            traceback.print_exc()
            code = 1
    receipt = {"result": RESULT, "source_sha256": sha(__file__),
        "configuration_sha256": fingerprint(job.tag) if job else None,
        "complete": bool(code == 0 and final and final["complete"]),
        "process_exit_code": code, "error": error,
        "certificate_sha256": sha(out / FINAL) if final else None,
        "stage_manifest": final["stage_manifest"] if final else None,
        "actual_full146_exact_geometric_iota_certified": bool(final and final["actual_full146_exact_geometric_iota_certified"]),
        "actual_original_P1_normal_jets_through_order272_computed": bool(final and final["actual_original_P1_normal_jets_through_order272_computed"]),
        "actual_original_P1_t_first_order_unit_certified": bool(final and final["actual_original_P1_t_first_order_unit_certified"]),
        "endpoint_rank8_integral_algebras_or_Norm_frames_computed": False,
        "seconds": time.monotonic() - started}
    save(out / "core-receipt.json", receipt)
    print("R914_IOTA_CORE_RECEIPT=" + json.dumps(receipt, sort_keys=True), flush=True)
    return code


if __name__ == "__main__":
    raise SystemExit(main())
