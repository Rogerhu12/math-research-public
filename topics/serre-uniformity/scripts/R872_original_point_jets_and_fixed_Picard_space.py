#!/usr/bin/env python3
"""R872: source-bound P0 jets and the actual fixed Picard RR spaces.

New arithmetic runs only in the public repository's Actions.  The exact
characteristic-zero sources are finite unit-solve expressions in the original
W and P0 data.  Their modular images are computed and checked here; modular
entries are never relabelled as reconstructed rational coefficients.
"""
import argparse
from fractions import Fraction
import gzip
import hashlib
import json
import os
from pathlib import Path
import sys
import time
import traceback

RESULT = "R872-original-P0-jets-and-fixed-Picard-RR-spaces"
FINAL = "p41-original-P0-jets-and-fixed-Picard-RR-spaces-certificate.json"
PREFIX = "R872-"
PRIME = 1000000753
RANK = 272
EPS = [0] + [1]*144 + [2]*127
JET_LAST = 272
R872_PROOF_SHA = "bd6ee11af3fbbce8db2767bc327265176992bb3be15395018df6612ab4e2dae2"
SOURCES = ("R805", "R806", "R856", "R860", "R868", "R827")
PROOFS = ("R872", "R868", "R805", "R809")
META = ("public-actions-input.json", "run-receipt.json", "core-receipt.json")
STRATEGY = {
    "scope": "original_P0_jets_and_fixed_chi_complete_RR_spaces",
    "field": "K=Q(zeta), zeta^2+zeta+1=0",
    "prime": PRIME,
    "normal_basis_degrees": EPS,
    "normal_basis_integer_scale_applied_again": False,
    "point_source": "R856 actual original P0",
    "socle_source": "R868 actual h with selected free coordinate",
    "reuse_complete_original_W_modular_reduction": True,
    "reuse_original_point_minor_and_both_inverse_products": True,
    "local_parameter": "first z-z0 if alpha is a unit; otherwise w-w0 if beta is a unit",
    "jet_first_order": 0,
    "jet_last_order": JET_LAST,
    "jet_coefficient_count": JET_LAST+1,
    "jet_equations": "all272 normal eigenvector equations and beta0/beta1 normalizations",
    "exact_jet_source": "unique formal Hensel solution with the original fixed unit minor",
    "characteristic_zero_jet_coefficients_reconstructed": False,
    "V2_basis": "beta_i*z^a with i first and 0<=a<=2-epsilon_i",
    "V3_basis": "beta_i*z^a with i first and 0<=a<=3-epsilon_i",
    "V5_basis": "beta_i*z^a with i first and 0<=a<=5-epsilon_i",
    "first_kernel": {"rows": 272, "columns": 418, "rank": 272, "dimension": 146},
    "u_selection": "first normalized exact kernel basis vector with nonzero order272 coefficient",
    "pencil_a": "the selected u itself",
    "pencil_b_schedule": "sum(c^j * U_j), c=1,2,..., exact integer coefficients",
    "new_V2_multiplier_degree_bound": "2+epsilon_input-epsilon_output<=4",
    "existing_cyclic_nodes": [0, 1, 2, 3, 4],
    "multiplication_matrix_convention": "row_output_column_input",
    "pencil_complete_rank": 962,
    "fixed_chi_kernel_rank": 272,
    "fixed_chi_kernel_dimension": 418,
    "fixed_chi_kernel_equation": "u*t+b*s=0 in complete V5; projection to s",
    "single_u_product_and_690_inverse_reused_across_trials": True,
    "full_characteristic_zero_Krylov_inverse_computed": False,
    "old_W_point_kernel_and_Krylov_inverses_recomputed": False,
    "original_Gamma_or_Mg_required": False,
    "actual_five_Lj_RR128_or_144_computed": False,
    "original_t_frame_calibration_computed": False,
    "only_budget_pencil_limit_and_transport_excluded_from_identity": True,
}

class BudgetStop(Exception):
    pass

class UnitFailure(Exception):
    pass

class SearchStop(Exception):
    pass

def sha(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for block in iter(lambda: f.read(1024*1024), b""):
            h.update(block)
    return h.hexdigest()

def read(path):
    path = Path(path)
    if path.name.endswith(".gz"):
        with gzip.open(path, "rt", encoding="utf-8") as f:
            return json.load(f)
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def save(path, value):
    path = Path(path)
    temporary = path.with_name(path.name+".tmp")
    if path.name.endswith(".gz"):
        with open(temporary, "wb") as raw:
            with gzip.GzipFile(filename="", mode="wb", fileobj=raw, mtime=0,
                               compresslevel=1) as zipped:
                data = json.dumps(value, sort_keys=True, separators=(",", ":"),
                                  ensure_ascii=False).encode("utf-8")
                zipped.write(data)
    else:
        temporary.write_text(json.dumps(value, sort_keys=True, separators=(",", ":"),
                                        ensure_ascii=False)+"\n", encoding="utf-8")
    os.replace(temporary, path)

def fingerprint(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":"),
                                     ensure_ascii=False).encode("utf-8")).hexdigest()

def plain(entry):
    return {key: entry[key] for key in ("file", "bytes", "sha256")}

def spec(path):
    path = Path(path)
    return {"file": path.name, "bytes": path.stat().st_size, "sha256": sha(path)}

def bound(directory, entry):
    entry = plain(entry)
    assert Path(entry["file"]).name == entry["file"]
    p = Path(directory)/entry["file"]
    assert spec(p) == entry, str(p)
    return p

def identity(source):
    return {k: source[k] for k in
            ("result", "run_id", "source_commit", "core_sha256", "manifest_sha256")}

def source_identity(source):
    out = identity(source)
    for key in ("configuration_sha256", "selected_file_count", "selected_files_sha256"):
        out[key] = source[key]
    out["certificate"] = plain(source["certificate"]) if source.get("certificate") else None
    out["configuration_stage"] = (
        plain(source["configuration_stage"]) if source.get("configuration_stage") else None)
    return out

def expected_tag(item):
    return {
        "result": RESULT, "source_sha256": item["core_sha256"], "p": 41,
        "python_flint": "0.9.0", "method_sha256": item["method_sha256"],
        "proofs_sha256": {key: item["proofs"][key]["sha256"] for key in PROOFS},
        "sources": {label: source_identity(item["sources"][label]) for label in SOURCES},
        "inputs": item["inputs"], "normal_basis_degrees": EPS, "strategy": STRATEGY,
    }

def q(value):
    if isinstance(value, list):
        assert len(value) == 2
        return Fraction(int(value[0]), int(value[1]))
    return Fraction(value)

def qmod(value, prime=PRIME):
    value = q(value)
    den = value.denominator % prime
    if not den:
        raise UnitFailure("An exact rational denominator is not a unit at the selected prime.")
    return value.numerator % prime * pow(den, -1, prime) % prime

def kmod(value, root):
    assert isinstance(value, list) and len(value) == 2
    return (qmod(value[0]) + root*qmod(value[1])) % PRIME

def basis(m):
    return [(i, a) for i in range(RANK) for a in range(max(0, m-EPS[i]+1))]

def matrix_rows(matrix):
    return [[int(matrix[i, j]) for j in range(matrix.ncols())]
            for i in range(matrix.nrows())]

def pivot_columns(matrix, rank):
    answer = []
    for row in range(rank):
        answer.append(next(j for j in range(matrix.ncols()) if matrix[row, j]))
    assert answer == sorted(set(answer))
    return answer

class Source:
    """Original immutable source bytes; explicit allowance for the ended R827 checkpoint."""
    def __init__(self, label, source):
        self.label, self.source = label, source
        self.directory = Path(source["directory"])
        self.files = {name: plain(entry) for name, entry in source["files"].items()}
        assert all(name == entry["file"] for name, entry in self.files.items())
        assert len(self.files) == source["selected_file_count"]
        assert fingerprint(self.files) == source["selected_files_sha256"]
        for entry in self.files.values():
            bound(self.directory, entry)
        manifest = read(self.directory/"full-outputs-manifest.json")
        assert self.files["full-outputs-manifest.json"]["sha256"] == source["manifest_sha256"]
        indexed = {entry["file"]: plain(entry) for entry in manifest["files"]}
        assert len(indexed) == len(manifest["files"])
        for name, entry in self.files.items():
            if name in ("full-outputs-manifest.json", "full-outputs-manifest-reference.json"):
                continue
            assert indexed[name] == entry, (label, name)
        initial = read(self.directory/"public-actions-input.json")
        run = read(self.directory/"run-receipt.json")
        assert initial["result"] == run["result"] == source["result"]
        assert initial["source_commit"] == run["source_commit"] == source["source_commit"]
        assert str(run["workflow_run_id"]) == str(source["run_id"])
        assert initial["core_sha256"] == source["core_sha256"]
        self.certificate_spec = plain(source["certificate"]) if source.get("certificate") else None
        if self.certificate_spec is not None:
            assert self.files[self.certificate_spec["file"]] == self.certificate_spec
            self.certificate = read(self.directory/self.certificate_spec["file"])
            self.tag = self.certificate["configuration"]
        else:
            assert label == "R827"
            configuration_stage = plain(source["configuration_stage"])
            assert self.files[configuration_stage["file"]] == configuration_stage
            anchor = read(self.directory/configuration_stage["file"])
            assert anchor["complete"] is True
            self.tag = anchor["configuration"]
            self.certificate = None
        assert self.tag["result"] == source["result"]
        assert self.tag["source_sha256"] == source["core_sha256"]
        assert fingerprint(self.tag) == source["configuration_sha256"]
        if label != "R827":
            assert run["complete"] is True and run["process_exit_code"] == 0
            assert self.certificate["complete"] is True
        else:
            permitted = source["accepted_checkpoint_exit_codes"]
            assert 0 not in permitted and run["complete"] is False
            assert run["process_exit_code"] in permitted
        if run.get("core_receipt_sha256") is not None:
            assert self.files["core-receipt.json"]["sha256"] == run["core_receipt_sha256"]
            core = read(self.directory/"core-receipt.json")
            assert core["source_sha256"] == source["core_sha256"]
            assert core["result"] == source["result"]
            if label != "R827":
                assert core["complete"] is True
                assert core["certificate_sha256"] == self.certificate_spec["sha256"]
        else:
            assert label == "R827" and run["complete"] is False
        self.initial = initial

    def stage(self, entry):
        entry = plain(entry)
        assert self.files[entry["file"]] == entry
        value = read(self.directory/entry["file"])
        assert value["complete"] is True and value["configuration"] == self.tag
        if "result" in value:
            assert value["result"] == self.source["result"]
        return value

class Job:
    def __init__(self, args):
        from flint import nmod_mat
        self.Matrix = nmod_mat
        self.args, self.started = args, time.monotonic()
        self.deadline = self.started + 60*float(args.budget_minutes)
        self.item = read(args.config)
        assert self.item["result"] == RESULT
        assert self.item["core_sha256"] == sha(__file__)
        assert sha(self.item["method"]) == self.item["method_sha256"]
        assert self.item["proofs"]["R872"]["sha256"] == R872_PROOF_SHA
        for key in PROOFS:
            assert sha(self.item["proofs"][key]["file"]) == self.item["proofs"][key]["sha256"]
        self.tag = expected_tag(self.item)
        self.out = Path(args.out)
        self.out.mkdir(parents=True, exist_ok=True)
        self.controls = self.item.get("controls", {})
        self.maximum_pencil_trials = int(self.controls.get("maximum_pencil_trials", 8))
        assert self.maximum_pencil_trials > 0
        self.refs, self.completed, self.current = {}, {}, None
        self.sources = {label: Source(label, self.item["sources"][label]) for label in SOURCES}
        self.V2, self.V3, self.V5 = basis(2), basis(3), basis(5)
        assert len(self.V2) == 418 and len(self.V3) == 690 and len(self.V5) == 1234
        self.V5loc = {pair: i for i, pair in enumerate(self.V5)}
        self.jet_rows, self.zseries, self.wseries = [], [], []

    def budget(self):
        if time.monotonic() >= self.deadline:
            raise BudgetStop("The public Actions arithmetic budget was reached.")

    def mat(self, rows):
        return self.Matrix(rows, PRIME)

    def zero(self, rows, columns):
        return self.mat([[0]*columns for _ in range(rows)])

    def eye(self, n):
        return self.mat([[int(i == j) for j in range(n)] for i in range(n)])

    def path(self, name):
        return self.out/(PREFIX+name+".json.gz")

    def old(self, name):
        path = self.path(name)
        if not path.exists():
            return None
        value = read(path)
        assert value["configuration"] == self.tag and value["complete"] is True
        assert value["result"] == RESULT
        self.completed[path.name] = spec(path)
        return value

    def put(self, name, data):
        # Commit a returned computation before observing the next budget boundary.
        value = dict(data, complete=True, configuration=self.tag, result=RESULT)
        path = self.path(name)
        save(path, value)
        entry = spec(path)
        self.completed[path.name] = entry
        return entry

    def own(self, entry):
        value = read(bound(self.out, entry))
        assert value["complete"] is True and value["configuration"] == self.tag
        assert value["result"] == RESULT
        self.completed[entry["file"]] = plain(entry)
        return value

    def source_input(self, key):
        entry = self.item["inputs"][key]
        assert entry["source_group"] in SOURCES
        value = self.sources[entry["source_group"]].stage(entry)
        return value, {"source_group": entry["source_group"], **plain(entry)}

    def source_list(self, key):
        out = []
        for entry in self.item["inputs"][key]:
            value = self.sources[entry["source_group"]].stage(entry)
            out.append((value, {"source_group": entry["source_group"], **plain(entry)}))
        return out

    def prepare(self):
        self.hsource, self.hspec = self.source_input("exact_socle")
        self.minor, self.minorspec = self.source_input("point_minor")
        self.inverse, self.inversespec = self.source_input("point_inverse")
        self.integral, self.integralspec = self.source_input("point_integral_index")
        self.point, self.pointspec = self.source_input("point_values")
        self.free, self.freespec = self.source_input("free_basis")
        self.Windex, self.Wspec = self.source_input("W_source_index")
        self.reduction, self.reductionspec = self.source_input("W_reduction")
        self.place, self.placespec = self.source_input("place_audit")
        self.points = self.source_list("Krylov_points")
        assert self.hsource["all_272_original_W_minus_w0_equations_exactly_verified"] is True
        assert self.hsource["all_272_integral_K_equations_exactly_zero"] is True
        assert self.hsource["original_column_scaling_restored_exactly"] is True
        assert self.hsource["free_original_normal_coordinate"] == 271
        assert self.hsource["free_original_normal_coordinate_value_K_1_zeta"] == [["1","1"],["0","1"]]
        assert plain(self.hsource["source_point_minor"]) == plain(self.minorspec)
        assert plain(self.hsource["source_fixed_inverse"]) == plain(self.inversespec)
        assert plain(self.hsource["source_integral_matrix"]) == plain(self.integralspec)
        assert self.minor["characteristic_zero_rank_271_certified"] is True
        assert self.minor["column_indices"] == self.minor["row_indices"] == list(range(271))
        assert self.minor["free_normal_coordinate"] == 271 and self.minor["prime"] == PRIME
        assert self.inverse["both_products_verified_for_both_embeddings"] is True
        assert plain(self.inverse["source_point_minor"]) == plain(self.minorspec)
        assert self.integral["all_272_original_P0_left_equations_exactly_zero"] is True
        assert self.integral["matrix_description"] == "H=(W(z0)-w0 I)*diag(column_scales)"
        assert self.point["normal_basis_rank"] == RANK and self.point["normal_basis_degrees"] == EPS
        assert self.point["original_P0_in_both_charts_verified"] is True
        assert self.point["all_272_two_chart_value_transitions_verified"] is True
        assert self.free["degree_distribution"] == [1,144,127]
        assert plain(self.point["source_free_basis"]) == plain(self.freespec)
        assert self.Windex["normal_basis_degrees"] == EPS
        assert self.Windex["coefficient_rule"]["additional_scale"] == [1,1]
        assert self.Windex["matrix_convention"] == "row_output_column_input"
        assert identity(self.Windex["source_original_R806_producer"]) == identity(self.sources["R806"].source)
        assert self.reduction["prime"] == PRIME and self.place["prime"] == PRIME
        assert self.reduction["original_rational_denominators_all_units"] is True
        assert self.reduction["original_W_e0_equals_e1_verified"] is True
        assert self.place["genuine_DVR_lift_source_not_an_arbitrary_modular_kernel_candidate"] is True
        original_groups = self.Windex["source_exact_coordinate_groups"]
        assert len(original_groups) == 34
        assert [plain(x) for x in self.reduction["source_R806_coordinate_groups"]] == [plain(x) for x in original_groups]
        for entry in original_groups:
            assert self.sources["R806"].files[entry["file"]] == plain(entry)
        self.root = int(self.place["original_zeta_root"])
        assert (self.root*self.root+self.root+1) % PRIME == 0
        roots = self.minor["roots_zeta_mod_prime"]
        assert self.root in roots and roots == self.inverse["roots_zeta_mod_prime"]
        embedding = roots.index(self.root)
        self.inverseH = self.mat(self.inverse["inverse_matrices_mod_prime"][embedding])
        self.Wcoef = [self.mat(rows) for rows in self.reduction["W_coefficients_mod_prime"]]
        assert len(self.Wcoef) == 4 and all(x.nrows() == x.ncols() == RANK for x in self.Wcoef)
        prepared = self.old("point-linearization")
        if prepared is None:
            self.budget()
            h = [kmod(x, self.root) for x in self.hsource["h_tau_K_1_zeta"]]
            ell = [kmod(x, self.root) for x in self.point["normal_basis_values_K_1_zeta"]["tau"]]
            z0 = kmod(self.point["chart_base_values_K_1_zeta"]["tau"], self.root)
            w0 = ell[1]
            assert len(h) == len(ell) == RANK
            assert h[271] == 1 and ell[0] == 1 and ell[271]
            scales = [qmod(x) for x in self.integral["column_scales_Q"]]
            assert len(scales) == RANK and all(scales)
            HB = self.minor["actual_minor_matrices_mod_prime"][embedding]
            assert len(HB) == 271 and all(len(row) == 271 for row in HB)
            # Reuse the saved complete selected block. The two missing borders
            # are fixed by the already exact left and right kernels.
            oldA = [[0]*RANK for _ in range(RANK)]
            scale_inverses = [pow(s,-1,PRIME) for s in scales]
            for i in range(271):
                for j in range(271):
                    oldA[i][j] = int(HB[i][j])*scale_inverses[j] % PRIME
                oldA[i][271] = -sum(oldA[i][j]*h[j] for j in range(271)) % PRIME
            invleft = pow(ell[271],-1,PRIME)
            for j in range(RANK):
                oldA[271][j] = -sum(ell[i]*oldA[i][j] for i in range(271))*invleft % PRIME
            A0 = self.mat(oldA)
            Taylor = [
                A0+w0*self.eye(RANK),
                self.Wcoef[1]+(2*z0)*self.Wcoef[2]+(3*z0*z0)*self.Wcoef[3],
                self.Wcoef[2]+(3*z0)*self.Wcoef[3],
                self.Wcoef[3],
            ]
            ellrow, hcol = self.mat([ell]), self.mat([[x] for x in h])
            alpha = int((ellrow*hcol)[0,0])
            beta = int((ellrow*Taylor[1]*hcol)[0,0])
            parameter = "z_minus_z0" if alpha else "w_minus_w0" if beta else None
            data = {
                "prime": PRIME, "original_zeta_root": self.root,
                "source_exact_socle": self.hspec, "source_point_values": self.pointspec,
                "source_point_minor": self.minorspec, "source_fixed_inverse": self.inversespec,
                "source_integral_matrix": self.integralspec,
                "source_W_reduction": self.reductionspec,
                "h_mod_prime": h, "point_evaluation_mod_prime": ell,
                "z0_mod_prime": z0, "w0_mod_prime": w0,
                "column_scales_mod_prime": scales,
                "A0_mod_prime": oldA,
                "Taylor_W_coefficients_mod_prime": [matrix_rows(x) for x in Taylor],
                "alpha_mod_prime": alpha, "beta_mod_prime": beta,
                "chosen_local_parameter": parameter,
                "chosen_parameter_derivative_is_a_unit": parameter is not None,
                "old_W_at_P0_and_271_inverse_reused": True,
                "new_arithmetic_only_border_recovery_and_derivative_coefficients": True,
            }
            self.put("point-linearization", data)
            prepared = self.old("point-linearization")
        assert prepared["source_exact_socle"] == self.hspec
        assert prepared["source_point_values"] == self.pointspec
        assert prepared["source_point_minor"] == self.minorspec
        assert prepared["source_fixed_inverse"] == self.inversespec
        assert prepared["source_integral_matrix"] == self.integralspec
        assert prepared["source_W_reduction"] == self.reductionspec
        assert prepared["prime"] == PRIME and prepared["original_zeta_root"] == self.root
        self.refs["point_linearization"] = spec(self.path("point-linearization"))
        self.h = prepared["h_mod_prime"]
        self.ell = prepared["point_evaluation_mod_prime"]
        self.z0, self.w0 = prepared["z0_mod_prime"], prepared["w0_mod_prime"]
        self.scale = prepared["column_scales_mod_prime"]
        self.A0 = self.mat(prepared["A0_mod_prime"])
        self.Taylor = [self.mat(x) for x in prepared["Taylor_W_coefficients_mod_prime"]]
        self.ellrow, self.hcol = self.mat([self.ell]), self.mat([[x] for x in self.h])
        self.alpha, self.beta = prepared["alpha_mod_prime"], prepared["beta_mod_prime"]
        self.parameter = prepared["chosen_local_parameter"]
        if self.parameter is None:
            raise UnitFailure("Neither local-parameter derivative is a unit at this original residue place.")
        assert [int(p["z0"]) for p,_ in self.points] == [0,1,2,3,4]
        for point, entry in self.points:
            assert point["prime"] == PRIME and point["usable"] is True
            assert point["actual_cyclic_rank"] == RANK
            assert point["both_inverse_products_verified"] is True
            assert plain(point["source_original_W"]) == plain(self.reductionspec)
            assert point["actual_determinant_mod_prime"]
        audit = {
            "prime": PRIME, "original_zeta_root": self.root,
            "source_exact_socle": self.hspec, "source_point_minor": self.minorspec,
            "source_fixed_inverse": self.inversespec, "source_point_integral_index": self.integralspec,
            "source_original_P0_values": self.pointspec, "source_free_basis": self.freespec,
            "source_original_W_index": self.Wspec, "source_complete_W_reduction": self.reductionspec,
            "source_original_place": self.placespec, "source_Krylov_points": [s for _,s in self.points],
            "alpha_mod_prime": self.alpha, "beta_mod_prime": self.beta,
            "source_point_linearization": self.refs["point_linearization"],
            "chosen_local_parameter": self.parameter,
            "chosen_parameter_derivative_is_a_unit": True,
            "all_original_W_polynomial_coefficients_are_integral_at_this_place": True,
            "integrality_not_inferred_from_only_W_at_P0": True,
            "point_matrix_reused_from_old_minor_and_two_exact_kernel_borders": True,
            "old_point_matrix_or_W_evaluation_not_recomputed": True,
            "normal_beta0_equals_one_and_beta1_equals_w": True,
            "exact_alpha_definition": "original ell dot original h",
            "exact_beta_definition": "original ell * derivative(original W)(z0) * original h",
            "exact_local_source": {
                "equation": "ell(x) W(z(x)) = w(x) ell(x)",
                "normalization": "ell_0(x)=1",
                "constant_term": self.pointspec,
                "unit_solver": self.minorspec,
                "formal_branch_is_original_P0_by_normalization_and_Hensel_uniqueness": True,
            },
            "all_original_scales_preserved": True,
        }
        old = self.old("source-audit")
        if old is None:
            self.refs["source_audit"] = self.put("source-audit", audit)
        else:
            assert all(old[k] == v for k,v in audit.items())
            self.refs["source_audit"] = spec(self.path("source-audit"))
        self.jet_rows, self.zseries, self.wseries = [], [], []


    def checkpoint(self, phase, **values):
        data = {"result": RESULT, "configuration": self.tag, "complete": False,
                "phase": phase, "updated_elapsed_seconds": time.monotonic()-self.started,
                **values}
        save(self.path("current"), data)
        self.current = spec(self.path("current"))
        return self.current

    def row_combination(self, pairs):
        result = [0]*RANK
        for scalar, row in pairs:
            scalar %= PRIME
            if scalar:
                for j in range(RANK):
                    result[j] = (result[j]+scalar*row[j]) % PRIME
        return self.mat([result])

    def solve_normalized_left(self, rhs):
        assert rhs.nrows() == 1 and rhs.ncols() == RANK
        assert int((rhs*self.hcol)[0,0]) == 0
        scaled = self.mat([[int(rhs[0,j])*self.scale[j] % PRIME for j in range(271)]])
        selected = scaled*self.inverseH
        temporary = [int(selected[0,j]) for j in range(271)]+[0]
        y0 = temporary[0]
        result = self.mat([[(temporary[j]-y0*self.ell[j]) % PRIME for j in range(RANK)]])
        assert int(result[0,0]) == 0 and result*self.A0 == rhs
        return matrix_rows(result)[0]

    def jets(self):
        entries = []
        self.jet_rows, self.zseries, self.wseries = [], [], []
        self.zsquare, self.zcube = [], []
        for n in range(JET_LAST+1):
            name = f"point-jet-{n:04d}"
            previous = entries[-1] if entries else None
            old = self.old(name)
            if old is None:
                self.budget()
                if n == 0:
                    elln, zn, wn, z2n, z3n = self.ell, self.z0, self.w0, 0, 0
                elif self.parameter == "z_minus_z0":
                    rhs = self.zero(1,RANK)
                    for a in range(1,min(3,n)+1):
                        rhs -= self.mat([self.jet_rows[n-a]])*self.Taylor[a]
                    rhs += self.row_combination(
                        (self.wseries[a],self.jet_rows[n-a]) for a in range(1,n))
                    wn = -int((rhs*self.hcol)[0,0])*pow(self.alpha,-1,PRIME) % PRIME
                    target = rhs+wn*self.ellrow
                    elln = self.solve_normalized_left(target)
                    zn, z2n, z3n = int(n == 1), int(n == 2), int(n == 3)
                    assert elln[1] == wn
                else:
                    assert self.parameter == "w_minus_w0"
                    # These powers of z-z0 at order n do not depend on z_n.
                    z2n = sum(self.zseries[a]*self.zseries[n-a]
                               for a in range(1,n)) % PRIME
                    z3n = sum(self.zseries[a]*self.zsquare[n-a]
                               for a in range(1,n-1)) % PRIME
                    square = self.zsquare+[z2n]
                    cube = self.zcube+[z3n]
                    rhs = self.mat([self.jet_rows[n-1]])
                    rhs -= self.row_combination(
                        (self.zseries[n-i],self.jet_rows[i]) for i in range(1,n))*self.Taylor[1]
                    rhs -= self.row_combination(
                        (square[n-i],self.jet_rows[i]) for i in range(0,max(0,n-1)))*self.Taylor[2]
                    rhs -= self.row_combination(
                        (cube[n-i],self.jet_rows[i]) for i in range(0,max(0,n-2)))*self.Taylor[3]
                    zn = int((rhs*self.hcol)[0,0])*pow(self.beta,-1,PRIME) % PRIME
                    target = rhs-zn*(self.ellrow*self.Taylor[1])
                    elln = self.solve_normalized_left(target)
                    wn = int(n == 1)
                    assert elln[1] == wn
                data = {
                    "prime": PRIME, "original_zeta_root": self.root,
                    "order": n, "local_parameter": self.parameter,
                    "source_point_linearization": self.refs["point_linearization"],
                    "source_previous_order": previous,
                    "normal_basis_jet_mod_prime": elln,
                    "z_jet_mod_prime": zn, "w_jet_mod_prime": wn,
                    "shift_z_square_coefficient_mod_prime": z2n,
                    "shift_z_cube_coefficient_mod_prime": z3n,
                    "all272_original_eigenvector_equations_verified_at_this_order": True,
                    "beta0_and_beta1_normalizations_verified": True,
                    "old_point_inverse_reused": True,
                    "exact_characteristic_zero_definition": {
                        "kind": "original_unique_Hensel_normal_branch_coefficient",
                        "order": n, "local_parameter": self.parameter,
                        "recurrence": "R872.9-10" if self.parameter == "z_minus_z0" else "R872.11-12",
                        "source_point_linearization": self.refs["point_linearization"],
                        "source_exact_W": self.Wspec, "source_exact_socle": self.hspec,
                        "source_exact_P0": self.pointspec,
                        "fixed_linear_solve": self.minorspec,
                        "normalization": "ell[0]=1, ell[1]=w",
                    },
                    "rational_coefficients_reconstructed": False,
                }
                self.put(name,data)
                old = self.old(name)
            assert old["order"] == n and old["local_parameter"] == self.parameter
            assert old["source_previous_order"] == previous
            assert old["source_point_linearization"] == self.refs["point_linearization"]
            assert old["all272_original_eigenvector_equations_verified_at_this_order"] is True
            assert old["beta0_and_beta1_normalizations_verified"] is True
            assert len(old["normal_basis_jet_mod_prime"]) == RANK
            self.jet_rows.append(old["normal_basis_jet_mod_prime"])
            self.zseries.append(old["z_jet_mod_prime"])
            self.wseries.append(old["w_jet_mod_prime"])
            self.zsquare.append(old["shift_z_square_coefficient_mod_prime"])
            self.zcube.append(old["shift_z_cube_coefficient_mod_prime"])
            entries.append(spec(self.path(name)))
            self.checkpoint("point_jets", completed_last_order=n, latest_order=entries[-1])
        name = "point-jets-index"
        old = self.old(name)
        if old is None:
            self.put(name,{
                "prime": PRIME, "original_zeta_root": self.root,
                "first_order": 0, "last_order": JET_LAST, "coefficient_count": JET_LAST+1,
                "normal_basis_rank": RANK, "local_parameter": self.parameter,
                "source_point_linearization": self.refs["point_linearization"],
                "orders": entries,
                "all273_orders_and_all272_normal_equations_verified": True,
                "actual_original_local_jets_mod_prime_computed": True,
                "exact_characteristic_zero_Hensel_expressions_defined": True,
                "original_t_equals_a_cubed_frame_not_replaced": True,
                "original_t_frame_calibration_computed": False,
            })
            old = self.old(name)
        assert old["orders"] == entries
        self.refs["point_jets"] = spec(self.path(name))
        return self.refs["point_jets"]

    def jet_matrix(self):
        name = "V2-original-point-jet-matrix"
        old = self.old(name)
        if old is None:
            self.budget()
            zpowers = [
                [int(n == 0) for n in range(JET_LAST+1)],
                self.zseries,
                [(self.z0*self.z0 if n == 0 else
                  2*self.z0*self.zseries[n]+self.zsquare[n]) % PRIME
                 for n in range(JET_LAST+1)],
            ]
            rows = []
            for n in range(JET_LAST+1):
                self.budget()
                rows.append([
                    sum(self.jet_rows[k][i]*zpowers[a][n-k] for k in range(n+1)) % PRIME
                    for i,a in self.V2])
            self.put(name,{
                "prime": PRIME, "source_point_jets": self.refs["point_jets"],
                "normal_basis_rank": RANK, "normal_basis_degrees": EPS,
                "V2_basis": [{"normal_basis_row": i,"power_of_z": a} for i,a in self.V2],
                "row_orders": list(range(JET_LAST+1)),
                "matrix_mod_prime": rows, "matrix_shape": [JET_LAST+1,len(self.V2)],
                "vanishing_constraint_orders": [0,271],
                "extra_order_for_exact_vanishing_selection": 272,
                "normal_integer_scale_applied_again": False,
                "exact_matrix_definition": {
                    "kind": "coefficients_of_z_power_times_original_beta_Hensel_series",
                    "source_point_jets": self.refs["point_jets"],
                    "ordinary_source": self.freespec,
                },
            })
            old = self.old(name)
        assert old["source_point_jets"] == self.refs["point_jets"]
        assert old["row_orders"] == list(range(JET_LAST+1))
        assert old["matrix_shape"] == [273,418]
        self.jetmatrix = self.mat(old["matrix_mod_prime"])
        self.refs["V2_jet_matrix"] = spec(self.path(name))
        return self.refs["V2_jet_matrix"]

    def first_kernel(self):
        name = "complete-V2-272P0-kernel"
        old = self.old(name)
        if old is None:
            self.budget()
            J = self.mat([[int(self.jetmatrix[i,j]) for j in range(418)] for i in range(272)])
            augmented = self.mat([
                [int(J[i,j]) for j in range(418)]+[int(i == j) for j in range(272)]
                for i in range(272)])
            reduced,total_rank = augmented.rref()
            assert total_rank == 272
            all_pivots = pivot_columns(reduced,total_rank)
            pivots = [j for j in all_pivots if j < 418]
            rank = len(pivots)
            if rank != 272:
                self.put(name,{
                    "prime": PRIME, "source_jet_matrix": self.refs["V2_jet_matrix"],
                    "accepted": False, "actual_rank_mod_prime": rank,
                    "failure_only_this_residue_specialization": True,
                    "selected_pivot_columns": pivots,
                })
                raise UnitFailure("The original 272-condition jet map has deficient rank at this residue place.")
            free = [j for j in range(418) if j not in set(pivots)]
            square = self.mat([[int(J[i,j]) for j in pivots] for i in range(272)])
            inverse = self.mat([[int(reduced[i,418+j]) for j in range(272)] for i in range(272)])
            assert square*inverse == self.eye(272) and inverse*square == self.eye(272)
            U = [[0]*146 for _ in range(418)]
            for k,j in enumerate(free):
                U[j][k] = 1
                for i,pivot in enumerate(pivots):
                    U[pivot][k] = -int(reduced[i,j]) % PRIME
            kernel = self.mat(U)
            assert J*kernel == self.zero(272,146)
            coefficient272 = self.mat([[int(self.jetmatrix[272,j]) for j in range(418)]])*kernel
            extra = matrix_rows(coefficient272)[0]
            candidates = [j for j,x in enumerate(extra) if x]
            if not candidates:
                self.put(name,{
                    "prime": PRIME, "source_jet_matrix": self.refs["V2_jet_matrix"],
                    "accepted": False, "actual_rank_mod_prime": 272,
                    "selected_pivot_columns": pivots, "free_columns": free,
                    "kernel_basis_mod_prime": U, "extra_order272_coefficients_mod_prime": extra,
                    "failure_only_this_residue_specialization": True,
                })
                raise UnitFailure("No normalized kernel column has an order272 unit at this residue place.")
            self.put(name,{
                "prime": PRIME, "source_jet_matrix": self.refs["V2_jet_matrix"],
                "accepted": True, "actual_rank_mod_prime": 272, "actual_kernel_dimension": 146,
                "selected_row_orders": list(range(272)),
                "selected_pivot_columns": pivots, "free_columns": free,
                "actual_selected_minor_mod_prime": matrix_rows(square),
                "inverse_selected_minor_mod_prime": matrix_rows(inverse),
                "both_selected_inverse_products_verified": True,
                "kernel_basis_mod_prime": U, "all272_by146_residuals_zero": True,
                "extra_order272_coefficients_mod_prime": extra,
                "first_exact_order272_basis_index": candidates[0],
                "full_characteristic_zero_RR_kernel_certified": True,
                "characteristic_zero_kernel_dimension": 146,
                "exact_kernel_definition": {
                    "kind": "full_original_jet_kernel_unit_solve",
                    "source_exact_jet_matrix": self.refs["V2_jet_matrix"],
                    "rows": list(range(272)), "pivot_columns": pivots, "free_columns": free,
                    "free_coordinates": "identity146",
                    "pivot_coordinates": "-J_pivot_inverse * J_free",
                    "rank_upper_and_lower_certificate": "R872.15-16 and the actual unit minor",
                    "modular_kernel_entries_are_not_reconstructed_rationals": True,
                },
            })
            old = self.old(name)
        if old["accepted"] is not True:
            raise UnitFailure("The retained original jet-kernel residue certificate was not accepted.")
        assert old["source_jet_matrix"] == self.refs["V2_jet_matrix"]
        assert old["actual_rank_mod_prime"] == 272 and old["actual_kernel_dimension"] == 146
        assert old["all272_by146_residuals_zero"] is True
        self.U = self.mat(old["kernel_basis_mod_prime"])
        self.u_index = old["first_exact_order272_basis_index"]
        self.extra272 = old["extra_order272_coefficients_mod_prime"]
        self.refs["V2_point_kernel"] = spec(self.path(name))
        return self.refs["V2_point_kernel"]

    def anchor(self, role, trial=None):
        assert role in ("u","b")
        name = "anchor-u" if role == "u" else f"anchor-b-trial-{trial:06d}"
        old = self.old(name)
        if old is None:
            self.budget()
            if role == "u":
                weights = [int(j == self.u_index) for j in range(146)]
                schedule_parameter = None
            else:
                assert trial is not None and trial >= 1
                weights = [pow(trial,j,PRIME) for j in range(146)]
                schedule_parameter = trial
            column = self.U*self.mat([[x] for x in weights])
            coords = [int(column[i,0]) for i in range(418)]
            vector = [[0]*RANK for _ in range(3)]
            for c,(i,a) in zip(coords,self.V2):
                vector[a][i] = c
            exact = {
                "kind": "original_V2_point_kernel_combination",
                "source_complete_kernel": self.refs["V2_point_kernel"],
                "basis_coefficients": (
                    {"kind":"standard_basis","index":self.u_index,"dimension":146}
                    if role == "u" else
                    {"kind":"integer_powers","base":trial,"exponents":[0,145]}),
                "source_normal_basis": self.freespec,
                "represented_function": "anchor_section / original_tau^2",
            }
            self.put(name,{
                "prime": PRIME, "role": role, "trial": trial,
                "schedule_parameter": schedule_parameter,
                "source_complete_kernel": self.refs["V2_point_kernel"],
                "kernel_basis_combination_mod_prime": weights,
                "V2_coordinates_mod_prime": coords,
                "normal_polynomial_coefficients_mod_prime": vector,
                "exact_section_definition": exact,
                "vanishes_at_original_P0_to_order_at_least272": True,
                "order272_is_exact": role == "u",
                "exact_order272_unit": (
                    self.extra272[self.u_index]
                    if role == "u" else None),
                "normal_integer_scale_applied_again": False,
            })
            old = self.old(name)
        assert old["source_complete_kernel"] == self.refs["V2_point_kernel"]
        assert old["role"] == role and old["trial"] == trial
        if role == "u":
            assert old["exact_order272_unit"]
            self.refs["anchor_u"] = spec(self.path(name))
        return old,spec(self.path(name))

    def multiplier(self, anchor, anchor_spec, label):
        name = label+"-multiplier-polynomial"
        old = self.old(name)
        if old is not None:
            assert old["source_anchor"] == anchor_spec
            assert old["weighted_support_verified"] is True
            return old,spec(self.path(name))
        node_specs = []
        for point,point_spec in self.points:
            z0 = int(point["z0"])
            node_name = label+f"-multiplier-at-z-{z0}"
            node = self.old(node_name)
            if node is None:
                self.budget()
                values = anchor["normal_polynomial_coefficients_mod_prime"]
                evaluated = [sum(values[k][i]*pow(z0,k,PRIME) for k in range(3)) % PRIME
                             for i in range(RANK)]
                W = self.mat(point["W_evaluated_mod_prime"])
                inverse = self.mat(point["inverse_Krylov_matrix_mod_prime"])
                vector = self.mat([[x] for x in evaluated])
                columns = []
                for j in range(RANK):
                    columns.append([int(vector[i,0]) for i in range(RANK)])
                    if j+1 < RANK:
                        vector = W*vector
                image = self.mat(columns).transpose()*inverse
                assert [int(image[i,0]) for i in range(RANK)] == evaluated
                self.put(node_name,{
                    "prime": PRIME, "z0": z0,
                    "source_anchor": anchor_spec, "source_original_Krylov": point_spec,
                    "source_original_W_reduction": self.reductionspec,
                    "matrix_mod_prime": matrix_rows(image),
                    "original_normal_anchor_value": evaluated,
                    "first_column_equals_original_anchor_value": True,
                    "old_Krylov_inverse_reused": True,
                    "matrix_direction": "K_anchor * inverse_Krylov",
                    "exact_source": "multiplication by the original exact V2 anchor at this cyclic node",
                })
                node = self.old(node_name)
            assert node["source_anchor"] == anchor_spec
            assert node["source_original_Krylov"] == point_spec
            node_specs.append(spec(self.path(node_name)))
            self.checkpoint("V2_multiplier", anchor=anchor_spec,
                            completed_point=z0, point_stage=node_specs[-1])
        self.budget()
        nodes = [self.own(entry) for entry in node_specs]
        weights = []
        for x in range(5):
            polynomial, denominator = [1],1
            for y in range(5):
                if x == y:
                    continue
                nxt = [0]*(len(polynomial)+1)
                for k,c in enumerate(polynomial):
                    nxt[k] = (nxt[k]-y*c) % PRIME
                    nxt[k+1] = (nxt[k+1]+c) % PRIME
                polynomial = nxt
                denominator = denominator*(x-y) % PRIME
            inverse = pow(denominator,-1,PRIME)
            weights.append([x*inverse % PRIME for x in polynomial])
        matrices = [self.mat(value["matrix_mod_prime"]) for value in nodes]
        coefficients = []
        for power in range(5):
            coefficient = self.zero(RANK,RANK)
            for j in range(5):
                coefficient += weights[j][power]*matrices[j]
            coefficients.append(matrix_rows(coefficient))
        for i in range(RANK):
            for j in range(RANK):
                allowed = 2+EPS[j]-EPS[i]
                for power in range(allowed+1,5):
                    assert coefficients[power][i][j] == 0
            for power in range(5):
                expected = anchor["normal_polynomial_coefficients_mod_prime"][power][i] if power < 3 else 0
                assert coefficients[power][i][0] == expected
        self.put(name,{
            "prime": PRIME, "source_anchor": anchor_spec,
            "source_original_W": self.Wspec, "point_stages": node_specs,
            "source_original_Krylov_points": [entry for _,entry in self.points],
            "nodes": [0,1,2,3,4], "Lagrange_weights_mod_prime": weights,
            "coefficient_matrices_mod_prime": coefficients,
            "maximum_degree": 4, "regular_section_degree": 2,
            "weighted_entry_degree_bound": "2+epsilon_input-epsilon_output",
            "weighted_support_verified": True, "first_column_verified_at_all_coefficients": True,
            "exact_multiplier_definition": {
                "kind": "unique_original_V2_multiplication_matrix",
                "source_exact_anchor": anchor_spec, "source_exact_W": self.Wspec,
                "polynomial_degree_and_direction": "R809.7, R872.5",
                "coefficient_integrality": "five original cyclic unit nodes and their unit Vandermonde",
            },
            "abstract_characteristic_zero_multiplier_and_true_modular_image_certified": True,
            "characteristic_zero_multiplier_coefficients_reconstructed": False,
            "old_point_matrices_or_Krylov_inverses_recomputed": False,
        })
        return self.old(name),spec(self.path(name))

    def product_matrix(self, multiplier, multiplier_spec, label):
        name = label+"-V3-to-V5-product"
        old = self.old(name)
        if old is None:
            self.budget()
            values = multiplier["coefficient_matrices_mod_prime"]
            rows = [[0]*len(self.V3) for _ in range(len(self.V5))]
            for col,(j,a) in enumerate(self.V3):
                for i in range(RANK):
                    for power in range(5):
                        value = values[power][i][j]
                        target = (i,power+a)
                        if target in self.V5loc:
                            rows[self.V5loc[target]][col] = value
                        else:
                            assert value == 0
            self.put(name,{
                "prime": PRIME, "source_multiplier": multiplier_spec,
                "source_anchor": multiplier["source_anchor"],
                "input_V3_basis": [{"normal_basis_row": i,"power_of_z": a} for i,a in self.V3],
                "output_V5_basis": [{"normal_basis_row": i,"power_of_z": a} for i,a in self.V5],
                "matrix_mod_prime": rows, "matrix_shape": [1234,690],
                "all_original_normal_polynomial_coefficients_retained": True,
                "all_terms_outside_V5_verified_zero": True,
                "exact_matrix_definition": "multiplication by the same exact V2 anchor on the complete original V3",
            })
            old = self.old(name)
        assert old["source_multiplier"] == multiplier_spec
        assert old["matrix_shape"] == [1234,690]
        return old,spec(self.path(name))


    def u_quotient(self, product, product_spec):
        name = "u-V3-image-and-row-quotient"
        old = self.old(name)
        if old is None:
            self.budget()
            P = self.mat(product["matrix_mod_prime"])
            augmented = self.mat([
                [int(P[j,i]) for j in range(1234)]+[int(i == j) for j in range(690)]
                for i in range(690)])
            reduced,total_rank = augmented.rref()
            assert total_rank == 690
            row_indices = [j for j in pivot_columns(reduced,690) if j < 1234]
            rank = len(row_indices)
            if rank != 690:
                self.put(name,{
                    "prime": PRIME, "source_u_product": product_spec,
                    "accepted": False, "actual_image_rank_mod_prime": rank,
                    "failure_only_this_residue_specialization": True,
                })
                raise UnitFailure("The original u*V3 map has deficient image rank at this residue place.")
            remaining = [j for j in range(1234) if j not in set(row_indices)]
            square = self.mat([[int(P[i,j]) for j in range(690)] for i in row_indices])
            inverse = self.mat([
                [int(reduced[i,1234+j]) for j in range(690)] for i in range(690)]).transpose()
            assert square*inverse == self.eye(690) and inverse*square == self.eye(690)
            quotient_coefficients = self.mat([
                [int(P[i,j]) for j in range(690)] for i in remaining])*inverse
            self.put(name,{
                "prime": PRIME, "source_u_product": product_spec,
                "accepted": True, "actual_image_rank_mod_prime": 690,
                "row_indices": row_indices, "remaining_row_indices": remaining,
                "selected_inverse_mod_prime": matrix_rows(inverse),
                "both_selected_inverse_products_verified": True,
                "quotient_coefficient_matrix_mod_prime": matrix_rows(quotient_coefficients),
                "quotient_shape": [544,1234],
                "quotient_formula": "y_remaining - quotient_coefficients*y_selected",
                "exact_quotient_definition": {
                    "source_exact_u_product": product_spec,
                    "selected_rows": row_indices,
                    "coefficient_matrix": "P_u_remaining * inverse(P_u_selected)",
                    "selected_minor_is_a_unit": True,
                },
                "same_u_multiplication_and_inverse_reused_in_all_trials": True,
            })
            old = self.old(name)
        if old["accepted"] is not True:
            raise UnitFailure("The retained u*V3 image has no accepted unit block at this place.")
        assert old["source_u_product"] == product_spec
        assert old["actual_image_rank_mod_prime"] == 690
        self.refs["u_product"] = product_spec
        self.refs["u_quotient"] = spec(self.path(name))
        self.Pu = self.mat(product["matrix_mod_prime"])
        self.uI, self.uR = old["row_indices"],old["remaining_row_indices"]
        self.PuInverse = self.mat(old["selected_inverse_mod_prime"])
        self.PuQuotient = self.mat(old["quotient_coefficient_matrix_mod_prime"])
        return old,self.refs["u_quotient"]

    def pencil_trial(self, trial, b, bspec, product, product_spec):
        name = f"pencil-trial-{trial:06d}-quotient"
        quotient = self.old(name)
        if quotient is None:
            self.budget()
            P = self.mat(product["matrix_mod_prime"])
            selected = self.mat([[int(P[i,j]) for j in range(690)] for i in self.uI])
            remaining = self.mat([[int(P[i,j]) for j in range(690)] for i in self.uR])
            Q = remaining-self.PuQuotient*selected
            self.put(name,{
                "prime": PRIME, "trial": trial,
                "source_u_product": self.refs["u_product"],
                "source_u_quotient": self.refs["u_quotient"],
                "source_b_anchor": bspec, "source_b_product": product_spec,
                "matrix_mod_prime": matrix_rows(Q), "matrix_shape": [544,690],
                "exact_quotient_source": "Pi_u composed with original multiplication by b",
            })
            quotient = self.old(name)
        qspec = spec(self.path(name))
        assert quotient["source_b_product"] == product_spec
        assert quotient["source_u_quotient"] == self.refs["u_quotient"]
        profile_name = f"pencil-trial-{trial:06d}-rank-profile"
        profile = self.old(profile_name)
        if profile is None:
            self.budget()
            Q = self.mat(quotient["matrix_mod_prime"])
            reduced,rank = Q.transpose().rref()
            row_indices = pivot_columns(reduced,rank)
            assert rank <= 272, "The actual image violates the proven geometric rank bound."
            self.put(profile_name,{
                "prime": PRIME, "trial": trial, "source_quotient": qspec,
                "actual_quotient_rank_mod_prime": rank,
                "actual_pencil_rank_mod_prime": 690+rank,
                "selected_quotient_rows": row_indices,
                "accepted": rank == 272,
                "criterion": "actual pencil rank962 proves no extra common zero beyond272P0",
                "failure_does_not_disprove_the_original_RR_space": rank != 272,
            })
            profile = self.old(profile_name)
        assert profile["source_quotient"] == qspec and profile["trial"] == trial
        profile_spec = spec(self.path(profile_name))
        self.checkpoint("pencil_trial", trial=trial, rank_profile=profile_spec,
                        actual_pencil_rank=profile["actual_pencil_rank_mod_prime"])
        if not profile["accepted"]:
            return None
        kernel_name = f"pencil-trial-{trial:06d}-complete-fixed-chi-kernel"
        old = self.old(kernel_name)
        if old is None:
            self.budget()
            Q = self.mat(quotient["matrix_mod_prime"])
            I = profile["selected_quotient_rows"]
            assert len(I) == 272
            augmented = self.mat([
                [int(Q[i,j]) for j in range(690)]+[int(k == j) for j in range(272)]
                for k,i in enumerate(I)])
            reduced,total_rank = augmented.rref()
            assert total_rank == 272
            pivots = [j for j in pivot_columns(reduced,272) if j < 690]
            assert len(pivots) == 272
            free = [j for j in range(690) if j not in set(pivots)]
            assert len(free) == 418
            square = self.mat([[int(Q[i,j]) for j in pivots] for i in I])
            inverse = self.mat([
                [int(reduced[i,690+j]) for j in range(272)] for i in range(272)])
            assert square*inverse == self.eye(272) and inverse*square == self.eye(272)
            srows = [[0]*418 for _ in range(690)]
            for k,j in enumerate(free):
                srows[j][k] = 1
                for i,pivot in enumerate(pivots):
                    srows[pivot][k] = -int(reduced[i,j]) % PRIME
            S = self.mat(srows)
            assert Q*S == self.zero(544,418)
            Pb = self.mat(product["matrix_mod_prime"])
            selected_Pb = self.mat([[int(Pb[i,j]) for j in range(690)] for i in self.uI])
            T = -(self.PuInverse*(selected_Pb*S))
            assert self.Pu*T+Pb*S == self.zero(1234,418)
            combined_rows = self.uI+[self.uR[i] for i in I]
            combined_columns = list(range(690))+[690+j for j in pivots]
            assert len(set(combined_rows)) == len(set(combined_columns)) == 962
            self.put(kernel_name,{
                "prime": PRIME, "trial": trial,
                "source_anchor_u": self.refs["anchor_u"], "source_anchor_b": bspec,
                "source_u_product": self.refs["u_product"], "source_b_product": product_spec,
                "source_u_quotient": self.refs["u_quotient"],
                "source_quotient": qspec, "source_rank_profile": profile_spec,
                "actual_pencil_rank_mod_prime": 962,
                "actual_quotient_rank_mod_prime": 272, "actual_kernel_dimension": 418,
                "selected_quotient_rows": I, "selected_pivot_columns": pivots,
                "free_columns": free,
                "selected_minor_mod_prime": matrix_rows(square),
                "inverse_selected_minor_mod_prime": matrix_rows(inverse),
                "both_selected_inverse_products_verified": True,
                "combined_962_minor_original_rows": combined_rows,
                "combined_962_minor_original_columns": combined_columns,
                "combined_minor_nonzero_by_unit_block_Schur_factorization": True,
                "V3_kernel_basis_mod_prime": srows,
                "paired_u_multiplier_coordinates_mod_prime": matrix_rows(T),
                "all544_by418_quotient_residuals_zero": True,
                "all1234_by418_complete_V5_relations_zero": True,
                "exact_full_characteristic_zero_W_Dchi_certified": True,
                "full_characteristic_zero_dimension": 418,
                "normal_integer_scale_applied_again": False,
                "exact_kernel_definition": {
                    "kind": "full_projected_original_multiplication_kernel",
                    "source_exact_quotient": qspec,
                    "selected_rows": I, "pivot_columns": pivots, "free_columns": free,
                    "free_coordinates": "identity418",
                    "pivot_coordinates": "-Q_selected_pivots_inverse*Q_selected_free",
                    "paired_u_coordinates": "-P_u_selected_inverse*P_b_selected*s",
                    "full_global_relation": "u*t+b*s=0 in original V5",
                    "characteristic_zero_rank_from_geometry_and_unit_minor": 272,
                    "modular_values_not_relabelled_characteristic_zero_coefficients": True,
                },
                "divisor_definition": {
                    "source_exact_u": self.refs["anchor_u"],
                    "equation": "div_2H(u)=272*P0+D_chi",
                    "D_chi_degree": 272, "D_chi_avoids_original_P0": True,
                    "common_zero_of_u_b": "272*P0",
                    "space": "H0(3H-D_chi)",
                },
            })
            old = self.old(kernel_name)
        assert old["source_b_product"] == product_spec
        assert old["source_quotient"] == qspec
        assert old["all544_by418_quotient_residuals_zero"] is True
        assert old["all1234_by418_complete_V5_relations_zero"] is True
        assert old["actual_kernel_dimension"] == 418
        self.refs["fixed_chi_kernel"] = spec(self.path(kernel_name))
        self.refs["accepted_pencil_profile"] = profile_spec
        self.refs["accepted_anchor_b"] = bspec
        self.refs["accepted_b_product"] = product_spec
        self.accepted_trial = trial
        return self.refs["fixed_chi_kernel"]

    def fixed_divisor(self):
        name = "original-fixed-chi-divisor-and-section-source"
        old = self.old(name)
        if old is None:
            self.put(name,{
                "prime": PRIME,
                "source_original_P0": self.pointspec,
                "source_complete_V2_point_kernel": self.refs["V2_point_kernel"],
                "source_exact_u": self.refs["anchor_u"],
                "source_exact_b": self.refs["accepted_anchor_b"],
                "source_complete_W_Dchi": self.refs["fixed_chi_kernel"],
                "source_actual_pencil_profile": self.refs["accepted_pencil_profile"],
                "H_degree": 272, "original_curve_genus": 127,
                "D_chi_degree": 272,
                "D_chi_definition": "div_2H(u)-272*P0",
                "D_chi_effective_and_avoids_original_P0": True,
                "chi_definition": "H-272*P0",
                "principal_function": {
                    "kind": "original_section_divided_by_original_tau_power",
                    "source_exact_section": self.refs["anchor_u"], "tau_power": 2,
                    "no_additional_scalar_or_82_power": True,
                },
                "exact_divisor_identity": "chi-(D_chi-H)=-div(u/tau^2)",
                "complete_RR_source": {
                    "space": "H0(3H-D_chi)", "dimension": 418,
                    "source": self.refs["fixed_chi_kernel"],
                    "basis_convention": "original V3 normal polynomial coordinates",
                    "coefficient_representation": "exact source-bound unit-solve expressions plus actual modular images",
                },
                "actual_complete_fixed_chi_RR_space_certified": True,
                "original_five_eta_ideals_changed": False,
                "five_original_Lj_128_spaces_computed": False,
                "five_original_Lj_144_weight_one_complements_computed": False,
                "original_t_frame_calibration_computed": False,
                "connection_or_Poincare_period_computed": False,
            })
            old = self.old(name)
        assert old["source_complete_W_Dchi"] == self.refs["fixed_chi_kernel"]
        assert old["actual_complete_fixed_chi_RR_space_certified"] is True
        self.refs["fixed_chi_divisor"] = spec(self.path(name))
        return self.refs["fixed_chi_divisor"]

    def run(self):
        self.prepare()
        self.jets()
        self.jet_matrix()
        self.first_kernel()
        u,uspec = self.anchor("u")
        multiplier,mspec = self.multiplier(u,uspec,"u")
        product,pspec = self.product_matrix(multiplier,mspec,"u")
        self.u_quotient(product,pspec)
        for trial in range(1,self.maximum_pencil_trials+1):
            self.budget()
            b,bspec = self.anchor("b",trial)
            label = f"b-trial-{trial:06d}"
            multiplier,mspec = self.multiplier(b,bspec,label)
            product,pspec = self.product_matrix(multiplier,mspec,label)
            if self.pencil_trial(trial,b,bspec,product,pspec) is not None:
                self.fixed_divisor()
                self.checkpoint("complete", accepted_trial=trial,
                                fixed_chi_divisor=self.refs["fixed_chi_divisor"])
                return self.finish(True,None)
        raise SearchStop("The finite pencil trial limit was reached without the sufficient rank962 certificate.")

    def manifest(self):
        entries = []
        for path in sorted(self.out.glob(PREFIX+"*.json.gz")):
            if path.name in (PREFIX+"current.json.gz",PREFIX+"exact-stages-manifest.json.gz"):
                continue
            value = read(path)
            assert value["result"] == RESULT and value["configuration"] == self.tag
            if value["complete"] is True:
                entries.append(spec(path))
        value = {
            "result": RESULT, "configuration": self.tag, "complete": True,
            "files": entries, "all_complete_mathematical_stages_retained": True,
            "current_checkpoint_not_in_complete_inventory": True,
        }
        path = self.path("exact-stages-manifest")
        save(path,value)
        return spec(path)

    def finish(self, complete, reason):
        manifest = self.manifest()
        actual_profile = None
        if self.refs.get("accepted_pencil_profile"):
            actual_profile = self.own(self.refs["accepted_pencil_profile"])
        final = {
            "result": RESULT, "configuration": self.tag, "complete": bool(complete),
            "p": 41, "prime": PRIME, "original_curve_genus": 127,
            "source_identities": {label: source_identity(self.item["sources"][label]) for label in SOURCES},
            "source_audit": self.refs.get("source_audit"),
            "point_linearization": self.refs.get("point_linearization"),
            "point_jets": self.refs.get("point_jets"),
            "original_V2_jet_matrix": self.refs.get("V2_jet_matrix"),
            "complete_original_146_kernel": self.refs.get("V2_point_kernel"),
            "anchor_u": self.refs.get("anchor_u"),
            "u_product": self.refs.get("u_product"), "u_quotient": self.refs.get("u_quotient"),
            "accepted_pencil_profile": self.refs.get("accepted_pencil_profile"),
            "accepted_anchor_b": self.refs.get("accepted_anchor_b"),
            "accepted_b_product": self.refs.get("accepted_b_product"),
            "complete_fixed_chi_418_kernel": self.refs.get("fixed_chi_kernel"),
            "fixed_chi_divisor_and_principal_function": self.refs.get("fixed_chi_divisor"),
            "actual_original_P0_local_parameter_certified": bool(self.refs.get("source_audit")),
            "actual_original_P0_jets_through_order272_computed": bool(self.refs.get("point_jets")),
            "actual_original_complete_146_kernel_certified": bool(self.refs.get("V2_point_kernel")),
            "actual_fixed_degree272_divisor_certified": bool(self.refs.get("anchor_u")),
            "actual_fixed_chi_complete_418_RR_space_certified": bool(self.refs.get("fixed_chi_divisor")),
            "actual_pencil_rank": actual_profile["actual_pencil_rank_mod_prime"] if actual_profile else None,
            "accepted_pencil_trial": getattr(self,"accepted_trial",None),
            "characteristic_zero_sources_are_exact_unit_solve_expressions": True,
            "characteristic_zero_jet_or_RR_coefficients_reconstructed": False,
            "five_original_Lj_RR128_computed": False,
            "five_original_Lj_weight_one_144_complements_computed": False,
            "original_t_frame_calibration_computed": False,
            "original_Gamma_or_Mg_computed": False,
            "connection_Poincare_period_or_height_computed": False,
            "failure_or_stop_reason": reason,
            "stage_manifest": manifest, "resume_state": self.current,
            "seconds": time.monotonic()-self.started,
        }
        if complete:
            assert final["actual_fixed_chi_complete_418_RR_space_certified"]
            assert final["actual_pencil_rank"] == 962
        save(self.out/FINAL,final)
        return final


def main():
    if os.environ.get("GITHUB_ACTIONS") != "true" or \
       os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public":
        raise SystemExit("R872 new arithmetic belongs only to the authorized public repository Actions.")
    sys.set_int_max_str_digits(0)
    parser = argparse.ArgumentParser()
    parser.add_argument("--config",required=True)
    parser.add_argument("--out",required=True)
    parser.add_argument("--budget-minutes",type=float,default=300)
    args = parser.parse_args()
    started, job, final, error, code = time.monotonic(),None,None,None,0
    out = Path(args.out)
    out.mkdir(parents=True,exist_ok=True)
    try:
        job = Job(args)
        final = job.run()
    except BudgetStop as exc:
        code,error = 124,{"type":"BudgetStop","message":str(exc)}
        if job is not None:
            final = job.finish(False,error)
    except (UnitFailure,SearchStop) as exc:
        code,error = 2,{"type":type(exc).__name__,"message":str(exc)}
        if job is not None:
            final = job.finish(False,error)
    except BaseException as exc:
        code,error = 1,{"type":type(exc).__name__,"message":str(exc)}
        traceback.print_exc()
        if job is not None:
            try:
                final = job.finish(False,error)
            except BaseException:
                traceback.print_exc()
    receipt = {
        "result": RESULT, "source_sha256": sha(__file__),
        "configuration": job.tag if job is not None else None,
        "complete": bool(final and final["complete"]), "error": error,
        "process_exit_code": code,
        "certificate_sha256": sha(out/FINAL) if (out/FINAL).exists() else None,
        "stage_manifest": final["stage_manifest"] if final else None,
        "actual_original_P0_jets_through_order272_computed":
            bool(final and final["actual_original_P0_jets_through_order272_computed"]),
        "actual_original_complete_146_kernel_certified":
            bool(final and final["actual_original_complete_146_kernel_certified"]),
        "actual_fixed_chi_complete_418_RR_space_certified":
            bool(final and final["actual_fixed_chi_complete_418_RR_space_certified"]),
        "actual_pencil_rank": final["actual_pencil_rank"] if final else None,
        "five_original_Lj_RR128_computed": False,
        "five_original_Lj_weight_one_144_complements_computed": False,
        "connection_Poincare_period_or_height_computed": False,
        "seconds": time.monotonic()-started,
    }
    save(out/"core-receipt.json",receipt)
    print(json.dumps({k:v for k,v in receipt.items() if k != "configuration"},
                     sort_keys=True,separators=(",",":")),flush=True)
    return code


if __name__ == "__main__":
    raise SystemExit(main())
