#!/usr/bin/env python3
"""R811: complete original base-y polar preimages in two normal affine charts.

Only source-bound already certified regular A/B multipliers are consumed.
All new L[z] Euclidean, kernel, and Laurent arithmetic runs in public Actions.
"""
import argparse
import gzip
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import sys
import tarfile
import time

import flint
from flint import fmpq

RESULT = "R811-original-polynomial-polar-preimages"
FINAL = "p41-original-polynomial-polar-preimages-certificate.json"
REGULAR_RESULT = "R811-original-regular-multipliers-and-polar-preimages"
REGULAR_SCOPE = "base_regular_multipliers"
SCOPE = "complete_base_y_two_chart_polar_preimages"
FIELD_CORE_SHA = "f196cb805d1ca91e8995866032a0a3ec3f96aac06e03b67a7c1f196fff759251"
PROOF_SHA = "263d8a15085c3fc053dac1df546ad0c3efb565d67ce312c78ec6e5ddb4dccf78"
FREE, LDEG, DEGREE = 272, 14, 5
EPS = [0]+[1]*144+[2]*127
FIELD_BASIS = "b^0..b^6,s*b^0..s*b^6; s=1+2*zeta; original b"


def guard():
    if os.environ.get("GITHUB_ACTIONS") != "true" or \
       os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public":
        raise SystemExit("New original-field polynomial arithmetic belongs to public repository Actions.")


def sha(path):
    value = hashlib.sha256()
    with Path(path).open("rb") as source:
        for block in iter(lambda: source.read(1024*1024), b""):
            value.update(block)
    return value.hexdigest()


def read(path):
    path = Path(path)
    with (gzip.open if path.suffix == ".gz" else open)(path, "rt", encoding="utf-8") as source:
        return json.load(source)


def save(path, value):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(path.name+".tmp")
    raw = (json.dumps(value, sort_keys=True, separators=(",", ":"))+"\n").encode()
    if path.suffix == ".gz":
        with temporary.open("wb") as target:
            with gzip.GzipFile(filename="", fileobj=target, mode="wb", mtime=0, compresslevel=2) as stream:
                stream.write(raw)
    else:
        temporary.write_bytes(raw)
    temporary.replace(path)


def spec(path):
    path = Path(path)
    return {"file": path.name, "bytes": path.stat().st_size, "sha256": sha(path)}


def plain(value):
    return {key: value[key] for key in ("file", "bytes", "sha256")}


def fingerprint(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def producer_identity(value):
    answer = {key: value[key] for key in
              ("result", "run_id", "source_commit", "core_sha256", "manifest_sha256", "certificate_name")}
    answer["certificate_sha256"] = value["files"][value["certificate_name"]]
    return answer


class BudgetStop(RuntimeError):
    pass


class Retained:
    def __init__(self, root, identity):
        self.root, self.identity = Path(root)/"R811", identity
        manifest_path = self.root/"full-outputs-manifest.json"
        assert sha(manifest_path) == identity["manifest_sha256"]
        manifest = read(manifest_path)
        assert manifest["result"] == REGULAR_RESULT == identity["result"]
        self.files = {row["file"]: row for row in manifest["files"]}
        assert len(self.files) == len(manifest["files"])
        self.checked = {}
        run, core, initial = (self.raw(name) for name in
            ("run-receipt.json", "core-receipt.json", "public-actions-input.json"))
        assert run["complete"] is True and run["process_exit_code"] == 0
        assert run["result"] == core["result"] == initial["result"] == REGULAR_RESULT
        assert str(run["workflow_run_id"]) == str(identity["run_id"])
        assert run["source_commit"] == initial["source_commit"] == identity["source_commit"]
        assert initial["source_repository"] == "Rogerhu12/math-research-public"
        assert core["complete"] is True and core["source_sha256"] == identity["core_sha256"]
        assert initial["core_sha256"] == initial["job"]["core_sha256"] == identity["core_sha256"]
        assert run["core_receipt_sha256"] == self.files["core-receipt.json"]["sha256"]
        name = identity["certificate_name"]
        assert identity["files"][name] == self.files[name]["sha256"] == core["certificate_sha256"]
        self.certificate, self.initial = self.raw(name), initial
        assert self.certificate["complete"] is True and self.certificate["result"] == REGULAR_RESULT
        self.tag = self.certificate["configuration"]
        assert self.tag["source_sha256"] == identity["core_sha256"] and self.tag["python_flint"] == "0.9.0"
        inventory = self.stage(self.certificate["stage_manifest"])
        self.inventory = {row["file"]: plain(row) for row in inventory["files"]}
        assert len(self.inventory) == len(inventory["files"])
        for name, row in self.inventory.items():
            assert row == plain(self.files[name])

    def raw(self, name):
        assert Path(name).name == name
        row = self.files[name]
        if name in self.identity["files"]:
            assert row["sha256"] == self.identity["files"][name]
        path = self.root/name
        if name not in self.checked:
            assert spec(path) == plain(row)
            self.checked[name] = plain(row)
        return read(path)

    def stage(self, entry):
        assert plain(entry) == plain(self.files[entry["file"]])
        value = self.raw(entry["file"])
        assert value["complete"] is True and value["configuration"] == self.tag
        return value

    def indexed(self, entry):
        assert self.inventory[entry["file"]] == plain(entry)
        return self.stage(entry)


class Job:
    def __init__(self, args):
        self.args, self.out, self.started = args, args.output, time.monotonic()
        self.out.mkdir(parents=True, exist_ok=True)
        self.item = read(args.config)
        assert self.item["producer_inputs_pending"] is False
        assert self.item["result"] == RESULT and self.item["p"] == 41
        assert self.item["core_sha256"] == sha(__file__)
        assert self.item["requested_stage"] == SCOPE
        assert self.item["R811_proof_sha256"] == sha(args.proof) == PROOF_SHA
        assert self.item["polynomial_method_sha256"] == sha(args.method)
        assert self.item["module_helper_sha256"] == sha(args.module_helper)
        assert self.item["field_core_sha256"] == sha(args.field_core) == FIELD_CORE_SHA
        assert self.item["matrix_tile_size"] == 16
        assert self.item["transcript_archive_operations_per_chunk"] == 128
        assert self.item["expected_original_polar_degree_for_final_comparison_only"] == 1206
        assert flint.__version__ == "0.9.0"
        assert set(self.item["retained_artifacts"]) == {"R811"}
        self.producer = Retained(args.retained, self.item["retained_artifacts"]["R811"])
        certificate = self.producer.certificate
        assert certificate["completed_scope"] == REGULAR_SCOPE
        assert certificate["requested_targets"] == ["A", "B"]
        assert certificate["normal_affine_basis_rank"] == FREE and certificate["normal_basis_degrees"] == EPS
        assert certificate["coefficient_field_basis"] == FIELD_BASIS
        assert self.producer.tag["R811_proof_sha256"] == PROOF_SHA
        for key in ("regular_multipliers_computed", "two_chart_regular_pairs_computed",
                    "all_weighted_degree_bounds_verified",
                    "all_original_first_columns_verified_coefficientwise",
                    "all_complete_polynomial_commutator_identities_verified",
                    "all_original_scalar_and_field_normalizations_preserved",
                    "normal_integral_basis_preserved"):
            assert certificate[key] is True
        assert certificate["base_polar_preimages_computed"] is False
        assert certificate["commutator_maximum_degree"] == 8
        assert certificate["exact_commutator_points"] == list(range(9))
        pair = certificate["original_y_operator_pair"]
        assert pair["numerator"] == "A" and pair["denominator"] == "B"
        assert pair["common_t_power_cancels_exactly"] == DEGREE
        assert pair["source_B_actually_nonzero"] is True
        self.target_specs = certificate["target_multipliers"]
        assert set(self.target_specs) == {"A", "B"}
        self.target_data, self.components, self.models = {}, {}, {}
        for target in ("A", "B"):
            value = self.producer.indexed(self.target_specs[target])
            assert value["target"] == target and value["regular_degree_bound"] == DEGREE
            assert value["normal_affine_basis_rank"] == FREE and value["normal_basis_degrees"] == EPS
            assert value["coefficient_field_basis"] == FIELD_BASIS
            assert value["all14_components_verified_in_original_field_basis"] is True
            assert value["all_complete_polynomial_commutator_identities_verified"] is True
            assert value["all_first_columns_verified_coefficientwise"] is True
            assert value["two_regular_charts_use_original_homogeneous_degree"] is True
            assert value["original_target_actually_nonzero"] is True
            target_tag = value["target_configuration"]
            assert value["target_configuration_sha256"] == fingerprint(target_tag)
            assert target_tag["basis_configuration_sha256"] == fingerprint(self.producer.tag)
            assert target_tag["target"] == target and target_tag["regular_degree_bound"] == DEGREE
            assert target_tag["coefficient_field_basis"] == FIELD_BASIS
            assert target_tag["source_R809_normal_vector"] == certificate["source_R809_normal_vectors"][target]
            original = target_tag["source_R809_target_configuration"]
            assert target_tag["source_R809_target_configuration_sha256"] == fingerprint(original)
            assert target_tag["original_b_model"] == original["original_b_model"]
            self.models[target] = target_tag["original_b_model"]
            entries = value["field_component_multipliers"]
            assert len(entries) == LDEG
            components = []
            for component, entry in enumerate(entries):
                row = self.producer.indexed(entry)
                assert row["target"] == target and row["field_component"] == component
                assert row["target_configuration"] == target_tag
                assert row["target_configuration_sha256"] == fingerprint(target_tag)
                assert row["coefficient_field_basis"] == FIELD_BASIS
                assert row["regular_degree_bound"] == DEGREE
                assert row["weighted_degree_bound_verified"] is True
                assert row["original_first_column_verified_coefficientwise"] is True
                assert row["complete_polynomial_commutator_identity_verified"] is True
                if row["zero_component_proved_from_exact_original_vector"]:
                    assert row["matrix_row_blocks_tau"] == row["matrix_row_blocks_sigma"] == []
                    assert row["zero_identity_follows_exactly_without_modular_zero_assumption"] is True
                else:
                    assert row["primitive_cyclic_uniqueness_identifies_true_regular_multiplier"] is True
                    assert row["sigma_regular_transition_preserves_original_section"] is True
                    assert row["exact_commutator_points"] == list(range(9))
                    assert len(row["matrix_row_blocks_tau"]) == len(row["matrix_row_blocks_sigma"]) == 17
                components.append((entry, row))
            self.target_data[target], self.components[target] = value, components
        assert self.models["A"] == self.models["B"], "Two original targets used different b models"
        module_spec = importlib.util.spec_from_file_location("R811_frozen_polynomial_module", args.module_helper)
        self.M = importlib.util.module_from_spec(module_spec)
        module_spec.loader.exec_module(self.M)
        field_spec = importlib.util.spec_from_file_location("R811_frozen_original_degree7_field", args.field_core)
        self.Fmodule = importlib.util.module_from_spec(field_spec)
        field_spec.loader.exec_module(self.Fmodule)
        self.F = self.Fmodule.QKField(self.Fmodule.dp(self.models["A"]))
        assert self.F.degree == 7 and self.F.mod[7] == 1
        self.tick_count = 0
        self.A = self.M.Algebra(self.F, self.tick)
        self.tag = {
            "result": RESULT, "source_sha256": sha(__file__), "python_flint": flint.__version__,
            "R811_proof_sha256": PROOF_SHA, "polynomial_method_sha256": sha(args.method),
            "module_helper_sha256": sha(args.module_helper), "field_core_sha256": FIELD_CORE_SHA,
            "R811_regular_producer": producer_identity(self.producer.identity),
            "R811_regular_certificate": plain(self.producer.files[self.producer.identity["certificate_name"]]),
            "source_target_multipliers": self.target_specs,
            "source_original_b_model": self.models["A"],
            "original_b_model_source_target_configuration_hashes": {
                target: self.target_data[target]["target_configuration_sha256"] for target in ("A", "B")},
            "original_R805_free_basis": self.producer.tag["original_R805_free_basis"],
            "actual_sigma_integer_n": certificate["actual_sigma_integer_n"],
            "normal_affine_basis_rank": FREE, "normal_basis_degrees": EPS,
            "source_coefficient_field_basis": FIELD_BASIS,
            "arithmetic_coefficient_field": "original L=Q(b,zeta); zeta^2+zeta+1=0",
            "field_basis_conversion": "a+s*c -> (a+c)+2*c*zeta; s=1+2*zeta",
            "polynomial_product_b_stride": 13, "matrix_tile_size": 16,
            "original_regular_pair_degree": DEGREE,
            "original_function_pair": "(A/tau^5)/(B/tau^5)=(A/sigma^5)/(B/sigma^5)",
            "matrix_convention": "output normal row, input normal column",
            "new_embedding_or_model_scalar_chosen": False,
            "only_current_large_work_vectors_and_necessary_final_ideal_basis_retained": True,
            "expected_degree_not_used_to_fill_any_kernel_rank_or_ideal_degree": True,
        }
        self.S = self.M.StageStore(self.out, self.tag, self.budget)

    def budget(self):
        if time.monotonic()-self.started >= self.args.budget_minutes*60-20:
            raise BudgetStop("Complete polynomial operations and latest atomic matrices retained.")

    def tick(self):
        self.tick_count += 1
        if self.tick_count % 256 == 0:
            self.budget()

    def ranges(self):
        return [(first, min(first+16, FREE)) for first in range(0, FREE, 16)]

    def weighted_count(self, first, stop):
        return sum(DEGREE+EPS[column]-EPS[row]+1
                   for row in range(first, stop) for column in range(FREE))

    def raw_component_blocks(self, target, chart, first, stop):
        result = []
        block_index = first//16
        for component, (component_spec, record) in enumerate(self.components[target]):
            if record["zero_component_proved_from_exact_original_vector"]:
                result.append(None)
                continue
            entry = record["matrix_row_blocks_"+chart][block_index]
            value = self.producer.indexed(entry)
            assert value["target_configuration"] == self.target_data[target]["target_configuration"]
            assert value["target_configuration_sha256"] == self.target_data[target]["target_configuration_sha256"]
            assert value["target"] == target and value["field_component"] == component
            assert (value["row_first"], value["row_stop"]) == (first, stop)
            assert value["regular_degree_bound"] == DEGREE
            denominator = int(value["common_positive_denominator"])
            assert denominator > 0
            raw = value["coefficient_numerators"]
            assert len(raw) == self.weighted_count(first, stop)
            if chart == "sigma":
                assert value["every_transition_exponent_nonnegative"] is True
                assert value["common_homogeneous_factor_in_pair"] == "t^5"
                assert value["source_tau_matrix_row_block"] == record["matrix_row_blocks_tau"][block_index]
            result.append({"source": entry, "numerators": raw, "denominator": denominator})
        return result

    def source_matrix(self, chart):
        matrix = self.M.VectorMatrix(self.S, self.A, "R811-polar-"+chart+"-source-pair",
                                     2*FREE, FREE, "columns", 16)
        source = {"original_R811_target_indexes": self.target_specs, "chart": chart,
                  "operator_pair": "[M_A,-M_B]", "source_original_b_model": self.models["A"]}
        if matrix.finished:
            assert matrix.state["source_original_pair_definition"] == source
            return matrix
        if matrix.state is None:
            prefix_eps = [0]
            for value in EPS:
                prefix_eps.append(prefix_eps[-1]+value)
            for first, stop in self.ranges():
                for target, base, sign in (("A", 0, 1), ("B", FREE, -1)):
                    missing = [column for column in range(FREE)
                               if not matrix.initial_tile_exists(base+column, first)]
                    if not missing:
                        continue
                    self.budget()
                    blocks = self.raw_component_blocks(target, chart, first, stop)
                    row_offsets, offset = {}, 0
                    for output in range(first, stop):
                        row_offsets[output] = offset
                        offset += FREE*(DEGREE-EPS[output]+1)+sum(EPS)
                    assert offset == self.weighted_count(first, stop)
                    for column in missing:
                        self.budget()
                        polynomials = []
                        for output in range(first, stop):
                            start = row_offsets[output]+column*(DEGREE-EPS[output]+1)+prefix_eps[column]
                            count = DEGREE+EPS[column]-EPS[output]+1
                            coefficients = []
                            for k in range(count):
                                rational = [
                                    fmpq(int(block["numerators"][start+k]), block["denominator"])
                                    if block is not None else fmpq(0) for block in blocks]
                                value = self.A.field_from_b_s(rational)
                                coefficients.append(value if sign == 1 else -value)
                            polynomial = self.M.Poly(self.A, coefficients)
                            assert polynomial.degree() <= DEGREE+EPS[column]-EPS[output]
                            polynomials.append(polynomial)
                        matrix.put_initial_tile(base+column, first, polynomials, {
                            "source_target_index": self.target_specs[target], "target": target, "chart": chart,
                            "source_component_row_blocks": [
                                block["source"] if block is not None else None for block in blocks],
                            "normal_input_column": column, "operator_sign": sign,
                            "source_field_basis_conversion_only": True,
                            "source_rational_multiplier_not_recomputed": True,
                            "common_homogeneous_pair_degree": DEGREE})
            vectors = [matrix.initial_vector(i) for i in range(2*FREE)]
            matrix.initialize(vectors, {"phase": "source_complete"}, source)
        matrix.finish({
            "source_original_pair_definition": source,
            "operator_pair_is_exact_original_MA_and_negative_MB": True,
            "all_weighted_support_bounds_preserved": True,
            "only_original_field_coordinate_conversion_performed": True,
            "new_regular_multiplier_or_new_original_model_computed": False,
            "source_B_actually_nonzero": True,
            "full_row_rank_reason": "M_B is invertible over the original function field L(z)"})
        return matrix


    def transcript_archive(self, matrix, chart_result_spec):
        """Preserve original small transcript bytes in128-operation tar chunks."""
        chunks = []
        width = self.item["transcript_archive_operations_per_chunk"]
        for first in range(0, matrix.state["operation_count"], width):
            self.budget()
            stop = min(first+width, matrix.state["operation_count"])
            stem = matrix.label+"-transcript-"+str(first).zfill(10)+"-"+str(stop).zfill(10)
            index_name = stem+"-archive-index"
            archive = self.out/(stem+".tar.gz")
            if self.S.exists(index_name):
                data = self.S.load(index_name)
                assert data["matrix_final_index"] == self.S.spec(matrix.final_name)
                assert data["closed_chart_certificate"] == chart_result_spec
                assert (data["first_operation"], data["last_operation_exclusive"]) == (first, stop)
                assert spec(archive) == data["archive"]
                members = data["original_member_specs"]
            else:
                names = []
                for number in range(first, stop):
                    names.extend([matrix.S.path(matrix.plan_name(number)),
                                  matrix.S.path(matrix.receipt_name(number))])
                members = [spec(path) for path in names]
                if not archive.exists():
                    temporary = archive.with_name(archive.name+".tmp")
                    with temporary.open("wb") as target:
                        with gzip.GzipFile(filename="", fileobj=target, mode="wb", mtime=0,
                                           compresslevel=2) as compressed:
                            with tarfile.open(fileobj=compressed, mode="w") as bundle:
                                for path, entry in zip(names, members):
                                    assert spec(path) == entry
                                    info = tarfile.TarInfo(path.name)
                                    info.size, info.mtime, info.mode = entry["bytes"], 0, 0o644
                                    with path.open("rb") as source:
                                        bundle.addfile(info, source)
                    temporary.replace(archive)
                self.S.put(index_name, {
                    "kind": "archived_original_unimodular_transcript",
                    "matrix_final_index": self.S.spec(matrix.final_name),
                    "closed_chart_certificate": chart_result_spec,
                    "first_operation": first, "last_operation_exclusive": stop,
                    "archive": spec(archive), "original_member_specs": members,
                    "original_plan_and_receipt_bytes_not_transformed": True,
                    "mathematical_operations_not_replayed_during_archiving": True})
                data = self.S.load(index_name)
            expected = {row["file"]: row for row in members}
            assert len(expected) == len(members) == 2*(stop-first)
            seen = set()
            with tarfile.open(archive, "r:gz") as bundle:
                for member in bundle:
                    assert member.isfile() and Path(member.name).name == member.name
                    assert member.name in expected and member.name not in seen
                    entry = expected[member.name]
                    assert member.size == entry["bytes"]
                    digest, size = hashlib.sha256(), 0
                    with bundle.extractfile(member) as source:
                        for block in iter(lambda: source.read(1024*1024), b""):
                            digest.update(block)
                            size += len(block)
                    assert size == entry["bytes"] and digest.hexdigest() == entry["sha256"]
                    seen.add(member.name)
            assert seen == set(expected)
            # The archive index and every unchanged byte have been verified.
            # A hard exit while unlinking leaves the complete archive as the
            # sole source and resumes this same hash-checked removal.
            for entry in members:
                path = self.out/entry["file"]
                if path.exists():
                    assert spec(path) == entry
                    path.unlink()
            chunks.append(self.S.spec(index_name))
        return chunks

    def close_work_matrices(self, chart, result_spec, matrices, joint):
        """After complete direct kernel verification, retain only the final ideal's large vectors."""
        name = "R811-polar-"+chart+"-closed-work-retention"
        if self.S.exists(name):
            value = self.S.load(name)
            assert value["closed_chart_certificate"] == result_spec
            assert value["retained_joint_Hermite_basis"] == self.S.spec(joint.final_name)
            for archived_spec in value["unmodified_transcript_archive_indexes"]:
                archived = self.S.load(archived_spec)
                assert spec(self.out/archived["archive"]["file"]) == archived["archive"]
            self.S.load(value["superseded_work_file_pruning_plan"])
            return self.S.spec(name)
        archived = []
        for matrix in [*matrices, joint]:
            archived.extend(self.transcript_archive(matrix, result_spec))
        plan_name = name+"-pruning-plan"
        prefixes = [matrix.label+"-v-" for matrix in matrices]
        if self.S.exists(plan_name):
            plan = self.S.load(plan_name)
            assert plan["closed_chart_certificate"] == result_spec
            assert plan["removable_matrix_prefixes"] == prefixes
        else:
            paths = sorted(path for path in self.out.glob("R811-polar-*.json.gz")
                           if any(path.name.startswith(prefix) for prefix in prefixes))
            entries = [spec(path) for path in paths]
            self.S.put(plan_name, {
                "kind": "completed_exact_work_matrix_pruning_plan",
                "closed_chart_certificate": result_spec,
                "removable_matrix_prefixes": prefixes,
                "retained_joint_Hermite_basis": self.S.spec(joint.final_name),
                "superseded_large_files": entries,
                "full_exact_Mp_H_equals_Mq_W_already_complete": True})
            plan = self.S.load(plan_name)
        entries = plan["superseded_large_files"]
        for entry in entries:
            self.budget()
            assert any(entry["file"].startswith(prefix) for prefix in prefixes)
            assert not entry["file"].startswith(joint.label+"-v-")
            path = self.out/entry["file"]
            if path.exists():
                assert spec(path) == entry
                path.unlink()
        assert not any(path.name.startswith(prefix) for path in self.out.glob("*.json.gz") for prefix in prefixes)
        return self.S.put(name, {
            "closed_chart_certificate": result_spec,
            "retained_joint_Hermite_basis": self.S.spec(joint.final_name),
            "unmodified_transcript_archive_indexes": archived,
            "superseded_work_file_pruning_plan": self.S.spec(plan_name),
            "actual_superseded_large_file_count": len(entries),
            "actual_superseded_large_bytes": sum(row["bytes"] for row in entries),
            "only_final_normal_ideal_joint_basis_retained_as_large_work_matrix": True,
            "original_retained_R811_producer_files_deleted_or_changed": False,
            "all_small_transcripts_retained_in_source_bound_exact_archives": True})

    def chart(self, chart):
        assert chart in ("tau", "sigma")
        result_name = "R811-polar-"+chart+"-complete-original-preimage"
        source = self.source_matrix(chart)
        reduced = self.M.VectorMatrix(self.S, self.A, "R811-polar-"+chart+"-reduced-pair",
                                      2*FREE, FREE, "columns", 16)
        rows = self.M.VectorMatrix(self.S, self.A, "R811-polar-"+chart+"-reverse-kernel-rows",
                                   2*FREE, FREE, "rows", 16)
        joint = self.M.VectorMatrix(self.S, self.A, "R811-polar-"+chart+"-joint-Hermite-kernel",
                                    FREE, 2*FREE, "columns", 16)
        if self.S.exists(result_name):
            result = self.S.load(result_name)
            assert result["source_original_target_indexes"] == self.target_specs
            assert result["source_original_b_model"] == self.models["A"]
            assert result["joint_Hermite_kernel"] == self.S.spec(joint.final_name)
            assert result["complete_original_normal_polar_preimage_certified"] is True
            retention = self.close_work_matrices(chart, self.S.spec(result_name),
                                                 [source, reduced, rows], joint)
            return result, self.S.spec(result_name), joint, retention
        if reduced.state is None:
            reduced.initialize(source.state["vectors"], self.M.reducer_control(FREE, False),
                {"immutable_unreduced_original_pair": self.S.spec(source.final_name),
                 "borrowed_source_vectors_never_mutated_or_deleted_by_work_cleanup": True})
        self.M.reduce_columns(reduced, FREE, False)
        self.M.reverse_kernel_replay(reduced, rows, FREE)
        self.M.transpose_kernel_rows(rows, joint, FREE)
        self.M.reduce_columns(joint, FREE, True)
        # The direct check uses the independent ORIGINAL P, never its reduced Gamma/zero form.
        check = self.M.verify_full_kernel_product(source, joint, "R811-polar-"+chart)
        check_data = self.S.load(check)
        assert check_data["source_original_pair_matrix"] == self.S.spec(source.final_name)
        assert check_data["source_joint_Hermite_kernel"] == self.S.spec(joint.final_name)
        assert check_data["full_original_Mp_H_equals_Mq_W_verified_exactly"] is True
        diagonal = joint.state["actual_diagonal"]
        degree = sum(row["degree"] for row in diagonal)
        boundary = sum(row["order_at_zero"] for row in diagonal)
        result_spec = self.S.put(result_name, {
            "chart": chart, "variable": "z" if chart == "tau" else "t",
            "source_original_target_indexes": self.target_specs,
            "source_original_b_model": self.models["A"],
            "immutable_unreduced_original_pair": self.S.spec(source.final_name),
            "unimodular_column_reduction": self.S.spec(reduced.final_name),
            "reverse_time_original_left_operator_kernel": self.S.spec(rows.final_name),
            "joint_Hermite_kernel": self.S.spec(joint.final_name),
            "direct_complete_original_polynomial_kernel_identity": check,
            "normal_affine_basis_rank": FREE, "normal_basis_degrees": EPS,
            "ideal_H_rows": [0, FREE], "denominator_relation_W_rows": [FREE, 2*FREE],
            "full_row_rank_from_actual_nonzero_original_denominator": True,
            "full_kernel_not_only_selected_solutions": True,
            "kernel_projection_injective_over_original_function_field": True,
            "all_final_Hermite_columns_transport_W_by_same_unimodular_operations": True,
            "actual_diagonal": diagonal,
            "actual_polynomial_module_colength": degree,
            "actual_variable_zero_boundary_length": boundary,
            "actual_degree_counts_all_residue_degrees_and_multiplicities": True,
            "complete_original_normal_polar_preimage_certified": True,
            "ideal_equals_full_preimage_MA_v_in_MB_R": True,
            "original_function_pair_constants_rescaled": False,
            "old_function_multipliers_or_CM_coordinates_recomputed": False,
            "global_degree_or_eta_claimed_from_single_chart": False})
        retention = self.close_work_matrices(chart, result_spec, [source, reduced, rows], joint)
        print(json.dumps({"stage": "complete_original_polar_chart", "chart": chart,
                          "actual_module_colength": degree, "actual_zero_boundary_length": boundary,
                          "seconds": time.monotonic()-self.started}), flush=True)
        return self.S.load(result_spec), result_spec, joint, retention

    def receipt(self, final):
        save(self.out/"core-receipt.json", {
            "result": RESULT, "complete": True, "source_sha256": sha(__file__),
            "certificate_sha256": sha(final), "completed_scope": SCOPE,
            "original_base_map_polar_divisor_computed": True,
            "complete_preimages_in_both_original_normal_affine_rings": True,
            "five_original_function_DAG_eta_or_height_computed": False})

    def run(self):
        final = self.out/FINAL
        if final.exists():
            previous = read(final)
            assert previous["result"] == RESULT and previous["complete"] is True
            assert previous["configuration"] == self.tag and previous["completed_scope"] == SCOPE
            manifest = self.S.load(previous["stage_manifest"])
            for entry in manifest["files"]:
                assert spec(self.out/entry["file"]) == entry
            for entry in manifest["transcript_archives"]:
                assert spec(self.out/entry["file"]) == entry
            self.receipt(final)
            return 0
        tau, tau_spec, Htau, tau_retention = self.chart("tau")
        sigma, sigma_spec, Hsigma, sigma_retention = self.chart("sigma")
        forward = self.M.verify_laurent_inclusion(Htau, Hsigma, EPS,
                    "R811-polar-tau-to-sigma", "tau", "sigma")
        backward = self.M.verify_laurent_inclusion(Hsigma, Htau, EPS,
                    "R811-polar-sigma-to-tau", "sigma", "tau")
        degree_on_tau = tau["actual_polynomial_module_colength"]
        boundary_from_sigma = sigma["actual_variable_zero_boundary_length"]
        degree = degree_on_tau+boundary_from_sigma
        expected = self.item["expected_original_polar_degree_for_final_comparison_only"]
        degree_spec = self.S.put("R811-polar-actual-global-degree", {
            "tau_complete_preimage": tau_spec, "sigma_complete_preimage": sigma_spec,
            "degree_on_tau_chart": degree_on_tau,
            "degree_on_missing_boundary_from_sigma_chart": boundary_from_sigma,
            "actual_global_degree": degree, "independently_known_original_map_degree": expected,
            "actual_count_matches_original_degree": degree == expected,
            "degree_formula": "sum deg diag(Htau)+sum ord_0 diag(Hsigma)",
            "two_whole_affine_colengths_not_added": True,
            "residue_degrees_and_nonreduced_multiplicities_included": True,
            "known_degree_not_used_to_construct_or_adjust_output": True})
        assert degree == expected, "Preserved actual polar-degree certificate differs from original map degree"
        assert not list(self.out.glob("R811-polar-*-current.json.gz"))
        name = "R811-polar-stage-manifest"
        files = [spec(path) for path in sorted(self.out.glob("R811-polar-*.json.gz"))
                 if path.name != name+".json.gz"]
        archives = [spec(path) for path in sorted(self.out.glob("R811-polar-*-transcript-*.tar.gz"))]
        manifest = self.S.put(name, {
            "files": files, "transcript_archives": archives,
            "archive_member_hashes_in_individual_archive_indexes": True,
            "historical_large_work_payloads_explicitly_pruned_only_after_exact_chart_completion": True})
        certificate = {
            "result": RESULT, "complete": True, "p": 41, "configuration": self.tag,
            "completed_scope": SCOPE, "original_map_index": 4,
            "normal_affine_basis_rank": FREE, "normal_basis_degrees": EPS,
            "original_field_model": self.models["A"], "source_coefficient_field_basis": FIELD_BASIS,
            "source_R811_regular_producer": producer_identity(self.producer.identity),
            "source_original_A_B_multiplier_indexes": self.target_specs,
            "actual_sigma_integer_n": self.tag["actual_sigma_integer_n"],
            "complete_affine_preimages": {"tau": tau_spec, "sigma": sigma_spec},
            "original_polar_ideal_bases": {
                "tau": {"joint_kernel": self.S.spec(Htau.final_name), "ideal_rows": [0, FREE],
                        "companion_W_rows": [FREE, 2*FREE]},
                "sigma": {"joint_kernel": self.S.spec(Hsigma.final_name), "ideal_rows": [0, FREE],
                          "companion_W_rows": [FREE, 2*FREE]}},
            "full_two_chart_overlap_containments": {"tau_to_sigma": forward, "sigma_to_tau": backward},
            "actual_degree_certificate": degree_spec,
            "degree_on_tau_chart": degree_on_tau,
            "degree_on_missing_boundary_from_sigma_chart": boundary_from_sigma,
            "actual_global_pole_degree": degree,
            "original_base_map_polar_divisor_computed": True,
            "all_polynomial_kernel_and_two_chart_containment_identities_verified": True,
            "complete_kernel_unimodularity_not_replaced_by_inclusion_only": True,
            "original_function_pair_homogeneous_factor_and_constants_preserved": True,
            "normal_integral_basis_preserved": True,
            "work_retention_receipts": {"tau": tau_retention, "sigma": sigma_retention},
            "cusp_radical_or_small_divisor_extraction_computed": False,
            "five_original_function_DAG_computed": False,
            "original_eta_rigidification_or_height_computed": False,
            "original_A_isogeny_kernel_coordinate_lift_computed": False,
            "old_CM_Hom_Laurent_S5_or_regular_multiplier_computation_repeated": False,
            "characteristic_zero_Krylov_matrix_or_inverse_computed": False,
            "stage_manifest": manifest, "seconds": time.monotonic()-self.started,
        }
        save(final, certificate)
        self.receipt(final)
        return 0


def main():
    guard()
    sys.set_int_max_str_digits(0)
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ("config", "proof", "method", "module-helper", "field-core", "retained", "output"):
        parser.add_argument("--"+name, type=Path, required=True)
    parser.add_argument("--budget-minutes", type=float, default=300)
    args = parser.parse_args()
    try:
        return Job(args).run()
    except BaseException as error:
        args.output.mkdir(parents=True, exist_ok=True)
        save(args.output/"core-receipt.json", {
            "result": RESULT, "complete": False, "source_sha256": sha(__file__),
            "error": type(error).__name__+": "+str(error),
            "completed_source_bound_operations_and_latest_atomic_checkpoints_preserved": True,
            "original_base_map_polar_divisor_computed": False,
            "eta_or_height_computed": False})
        raise


if __name__ == "__main__":
    sys.exit(main())
