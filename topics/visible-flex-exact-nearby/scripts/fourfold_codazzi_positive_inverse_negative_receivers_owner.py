"""One actual56 target: original physical positive ports to true negative receivers.

Whole58/224/32 and immutable SP/PW/WTA/WX are admitted before numerical imports.
No source packet, signed finite column, old target, or hypothetical result is made.
"""
from __future__ import annotations
import argparse, copy, hashlib, importlib.util, json, os, platform, sys, time, traceback
from pathlib import Path

REPO = "Rogerhu12/math-research-public"
TOPIC = "topics/visible-flex-exact-nearby"
KIND = "complete_actual_positive_to_negative_receiver_stage_v1"
STAGE = "negative_receivers"
PARAMETERS = {
    "arithmetic_bits": 320, "decimal_record_digits": 60,
    "maximum_scientific_wall_seconds": 900, "old_completed_target_calls": 0,
    "ordinary_radial_measure": "dr", "normalised_angular_measure": True,
    "original_physical_port_count": 14, "receiver_count": 4,
    "fixed_waist_normalizer_J": 268435456,
    "original_WPN_radial_projection_cells": 24480,
    "negative_ordinary_or_impulse_source_in_this_target": False,
    "actual_particular_WPN_source_packet_in_this_target": False,
}
RECEIVER_CODES = (
    "true_full_root_mixed", "complete_negative_waist_density",
    "left_normalized_joint_two_branches", "WPL_physical_primitive",
)
SCI_FIELDS = sorted([
    "identity", "complete", "proved", "actual_returncode", "failure", "stage",
    "completed_targets", "current_target", "new_records", "saved_record_count",
    "parameters", "result", "whole_completed_inputs", "reference_identity",
    "selected_receiver_identity", "high_response_source_binding",
    "old_scientific_target_calls", "new_arrays_published", "new_artifacts",
    "new_Releases", "wall_seconds", "runtime",
])
FIXED_SMALL_INPUTS = {
    "SP_execution": (
        "notes/primitive_mean_strict_propagation_ci/run-43731464771-1/execution.json",
        "a3a02969178e5e8b3b040fafd51d08b25d75b3f3922f2ae2e9ee0d4a8ab18a12"),
    "PW_execution": (
        "notes/positive_ports_to_waist_density_ci/run-43734233535-1/execution.json",
        "f17516d3083cd2782866c2163635a3a89efe9479ced8f57eefb2bf63e3f92e90"),
    "WTA_actual": (
        "notes/waist_normalizer_coefficients_ci/run-43763134339-1/actual-scientific-conclusion.json",
        "2a406e4506bb5a19646924e2072ec83d8806055a083ba7e1b1acfb9ab21d142d"),
    "WTA_execution": (
        "notes/waist_normalizer_coefficients_ci/run-43763134339-1/execution.json",
        "571e0993583844079d0aad828cd2da093336761429551d1e25b88e912f40fcf7"),
    "WX_execution": (
        "notes/true_waist_coordinates_saved_products_ci/run-43763424840-1/execution.json",
        "e9fc1611dc582e0264f0222069e03d8e9a1953616db540fc14896d4765abfb12"),
}
CENTRE = "440866a368f68b472bc904c90fbe9862f2ff13e9f884ffced6a4819c04866a47"
DIRECTION = "6a71cb8109b095cd242823d181e7c1ef525355b9b90bf8c59f88668b68231d04"
ROOT_INTERVAL = ["1191984371497/5000000000000", "2383968743003/10000000000000"]
FIXED_REFERENCE_IDENTITY = {
    "all_original_parent_definitions_verified": True,
    "complete_original_WVC_file": {
        "bytes": 78627,
        "git_blob_sha": "746ec1e16befe8914c64521ad087c1f1dd23ab73",
        "path": "topics/visible-flex-exact-nearby/notes/continuous_centre_tracefree_residual_ci/run-43891414339-1/actual-scientific-conclusion.json",
        "role": "WVC_actual",
        "sha256": "85fd5bc63c7cb558ef04ff9699f1f9be81dbd7e7b9638a2e0922818dc559cb88"
    },
    "fine_cell_count": 24480,
    "fine_refinement": 160,
    "finite_normalizer_rule": "rho2=1+h^2*(a^2+c^2*q^2)/12",
    "kind": "complete_fixed_WVC_signed_reference_identity_v1",
    "no_completed_bound_target_recomputed": True,
    "original_reference_chain": {
        "count": 153,
        "sha256": "6fd1cc7b7bc2fb449804263962199175763e3c2d7e4816dfa46778a4d26108ac"
    },
    "reference_outer_impedance": "13/80",
    "same_original_D_S_and_true_root": True,
    "scalar_trace_identically_zero": True,
    "selected_diagonal_chain": {
        "count": 153,
        "sha256": "b19d7e319a9ea4e49909e12b1dfe71ddc23adf5a273708288b3fe6b0cc3af8d2"
    }
}


def require(ok, message):
    if not ok:
        raise ValueError(message)


def canonical(value):
    return (json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False,
                       allow_nan=False)+"\n").encode()


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def blob(raw):
    return hashlib.sha1(b"blob "+str(len(raw)).encode()+b"\0"+raw).hexdigest()


def parse(raw):
    return json.loads(raw, parse_constant=lambda value: (_ for _ in ()).throw(ValueError(value)))


def atomic(path, raw):
    temporary = path.with_name(path.name+".partial")
    with temporary.open("wb") as stream:
        stream.write(raw); stream.flush(); os.fsync(stream.fileno())
    os.replace(temporary, path)
    require(path.read_bytes() == raw, "whole scalar prefix byte readback")


def target_order():
    return ["negative_port_%02d_%s_upper" % (j, code)
            for j in range(14) for code in RECEIVER_CODES]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--manifest", type=Path, required=True)
    parser.add_argument("--manifest-sha", required=True)
    parser.add_argument("--input-map", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--checkout", required=True)
    args = parser.parse_args()
    require(os.environ.get("GITHUB_ACTIONS") == "true"
            and os.environ.get("GITHUB_REPOSITORY") == REPO,
            "new scalar arithmetic only in the public own Actions repository")
    raw_manifest = args.manifest.read_bytes()
    require(sha(raw_manifest) == args.manifest_sha, "whole actual-input manifest")
    manifest = parse(raw_manifest)
    require(manifest["scientific_kind"] == KIND and manifest["stage"] == STAGE
            and manifest["parameters"] == PARAMETERS
            and manifest["target_order"] == target_order()
            and manifest["complete_record_counts"] == [56]
            and manifest["allowed_scientific_fields"] == SCI_FIELDS,
            "one entire56 receiver target with unchanged original port input spaces")
    specs = {spec["role"]: spec for spec in manifest["files"]}
    require(len(specs) == len(manifest["files"]), "unique complete input roles")
    paths = parse(args.input_map.read_bytes())
    require(set(paths) == set(specs), "every whole current input is materialized")
    contents = {}
    for role, spec in specs.items():
        raw = Path(paths[role]).read_bytes()
        require(0 < len(raw) < 100000 and len(raw) == spec["bytes"]
                and sha(raw) == spec["sha256"] and blob(raw) == spec["git_blob_sha"],
                "whole immutable input bytes: "+role)
        raw.decode("utf-8")
        contents[role] = raw
    require(sha(Path(__file__).read_bytes()) == specs["science"]["sha256"],
            "the actual numerical owner is the pinned source")
    for role, (path, digest) in FIXED_SMALL_INPUTS.items():
        require(specs[role]["path"] == TOPIC+"/"+path
                and specs[role]["sha256"] == digest,
                "exact completed old receiver input: "+role)

    def data(role):
        return parse(contents[role])

    def load(role):
        module_spec = importlib.util.spec_from_file_location("_negative_receivers_"+role, paths[role])
        require(module_spec is not None and module_spec.loader is not None, "explicit pure module")
        module = importlib.util.module_from_spec(module_spec)
        module_spec.loader.exec_module(module)
        return module

    def physical_pair(stage, count):
        ar, er, mr = stage+"_actual", stage+"_execution", stage+"_manifest"
        actual, execution, old_manifest = data(ar), data(er), data(mr)
        ident = actual["identity"]
        require(actual["complete"] is True and actual["proved"] is True
                and actual["actual_returncode"] == 0 and actual["failure"] is None
                and execution["complete"] is True and execution["failure"] is None
                and execution["actual_child_returncode"] == 0
                and ident["kind"] == "complete_actual_positive_physical_scalar_stage_v1"
                and ident["scalar_stage"] == stage
                and ident["manifest_sha256"] == execution["manifest_sha256"] == specs[mr]["sha256"]
                and ident["run_id"] == execution["run_id"]
                and ident["run_attempt"] == execution["run_attempt"] == "1",
                "genuine complete actual positive predecessor: "+stage)
        require(old_manifest["kind"] == "actual_positive_physical_scalar_stage_inputs_v1"
                and old_manifest["stage"] == stage
                and sorted(actual) == old_manifest["allowed_scientific_fields"]
                and actual["parameters"] == old_manifest["parameters"]
                and actual["saved_record_count"] == count
                and actual["completed_targets"] == old_manifest["target_order"]
                and set(actual["new_records"]) == set(actual["completed_targets"])
                and count in old_manifest["complete_record_counts"]
                and actual["stage"] == "complete_"+stage+"_scalar_branch"
                and actual["result"]["complete_new_record_order"] == actual["completed_targets"]
                and actual["result"]["topic_completion_proved"] is False,
                "all original record names, fields and full completion branch")
        require(execution["current_input_receipts"] == old_manifest["files"]
                and ident["source_sha256"] == next(
                    spec["sha256"] for spec in old_manifest["files"] if spec["role"] == "science"),
                "original entire actual source/execution/manifest binding")
        found = [value for value in execution["scientific_files"] if value["path"] == specs[ar]["path"]]
        require(found == [{key: specs[ar][key] for key in ("path", "bytes", "sha256")}],
                "execution identifies this exact whole scientific file")
        for name in ("old_scientific_target_calls", "new_arrays_published", "new_artifacts", "new_Releases"):
            require(actual[name] == 0, "original no-repeat/no-array scope: "+name)
        return actual

    gate = physical_pair("gate", 58)
    ports = physical_pair("ports", 224)
    wpn = physical_pair("wpn", 32)
    ref = gate["reference_identity"]
    require(ref == FIXED_REFERENCE_IDENTITY,
            "the same COMPLETE admitted original WVC/D/S/true-root reference identity")
    require(ports["reference_identity"] == wpn["reference_identity"] == ref
            and gate["result"]["same_actual_internal_gate_passed"] is True
            and gate["result"]["same_actual_physical_outer_gate_passed"] is True,
            "same actual full internal and physical outer gate")
    for doc, roles in (
            (ports, ("gate_actual", "gate_execution", "gate_manifest")),
            (wpn, ("gate_actual", "gate_execution", "gate_manifest",
                   "ports_actual", "ports_execution", "ports_manifest"))):
        for role in roles:
            require(doc["whole_completed_inputs"][role]["file"] == specs[role],
                    "same actual chain reference: "+role)
    for role in ("low_actual", "low_execution", "low_manifest",
                 "D_actual", "D_execution", "weighted_actual", "weighted_execution"):
        require(gate["whole_completed_inputs"][role]
                == ports["whole_completed_inputs"][role]
                == wpn["whole_completed_inputs"][role],
                "same exact prior low/reference/high receiver identity: "+role)

    def legacy_science(role, run, kind, gates):
        execution = data(role)
        actual = execution["actual_scientific_receipt"]
        require(execution["complete"] is True and execution["actual_returncode"] == 0
                and execution["actual_failure"] is None
                and execution["run_id"] == actual["run_id"] == run
                and execution["run_attempt"] == actual["run_attempt"] == "1"
                and actual["kind"] == kind and actual["complete"] is True
                and actual["proved"] is True and actual["actual_returncode"] == 0
                and actual["failure"] is None and len(actual["gates"]) == gates
                and all(value["passed"] is True for value in actual["gates"])
                and actual["arithmetic_bits"] == 320
                and actual["input_manifest_sha256"] == execution["input_manifest_sha256"]
                and actual["source_sha256"] == execution["source_budget_source_sha256"],
                "whole immutable legacy science and every gate: "+role)
        require(actual["old_numerical_enclosures_recomputed"] == 0
                and execution["old_numerical_enclosures_recomputed"] == 0,
                "old receiver target was not repeated")
        return actual

    sp = legacy_science("SP_execution", "43731464771",
                        "actual_complete_primitive_mean_strict_propagation_v1", 20)
    pw = legacy_science("PW_execution", "43734233535",
                        "actual_complete_positive_ports_to_waist_density_v1", 21)
    wx = legacy_science("WX_execution", "43763424840",
                        "actual_true_waist_coordinates_from_saved_positive_products_v1", 20)
    wta, wta_execution = data("WTA_actual"), data("WTA_execution")
    require(wta["kind"] == "actual_waist_normalizer_coefficients_and_two_window_gates_v1"
            and wta["complete"] is True and wta["proved"] is True
            and wta["actual_returncode"] == 0 and wta["failure"] is None
            and wta["run_id"] == wta_execution["run_id"] == "43763134339"
            and wta["run_attempt"] == wta_execution["run_attempt"] == "1"
            and wta_execution["complete"] is True and wta_execution["actual_returncode"] == 0
            and wta_execution["actual_failure"] is None and len(wta["gates"]) == 20
            and all(value["passed"] is True for value in wta["gates"])
            and wta_execution["input_manifest_sha256"] == wta["input_manifest_sha256"]
            and wta_execution["source_sha256"] == wta["source_sha256"]
            and wta_execution["scientific_conclusion"]["sha256"] == specs["WTA_actual"]["sha256"]
            and wta_execution["scientific_conclusion"]["bytes"] == specs["WTA_actual"]["bytes"],
            "whole actual fixed right-waist normalizer and its execution")
    require(wta["original_numerical_enclosures_recomputed"] == 0
            and wta["old_source_or_integral_calls"] == 0,
            "read the old normalizer without its old calculation")
    require(wta["original_SP_source_and_manifest_sha256"]
                == [sp["source_sha256"], sp["input_manifest_sha256"]]
            and wta["arithmetic_bits"] == sp["arithmetic_bits"] == 320
            and wta["parameters"]["exact_delta_half_width"] == "1/100000000"
            and wx["mathematical_parameters"]["exact_real_delta_radius"] == "1/100000000",
            "whole old SP family range, WTA copy source, and WX original range agree")
    family = sp["exact_family_identity"]
    require(family["continuous_centre_definition_sha256"] == CENTRE
            and family["continuous_response_definition_sha256"] == DIRECTION
            and family["fixed_current_eta"] == "eta_0"
            and pw["exact_family_identity"] == wta["copied_SP_family_identity"] == family,
            "same full repaired reference, complete direction and independent means")
    require(sp["mathematical_parameters"]["exact_root_interval"] == ROOT_INTERVAL
            and sp["mathematical_parameters"]["exact_root_Cauchy_radius"] == "1/200"
            and sp["mathematical_parameters"]["exact_strict_interval"]
                == ["0", "2333968743003/10000000000000"]
            and sp["mathematical_parameters"]["complete_mean_coordinates"] == 2,
            "the original true negative root and strict intervals, both means")
    gain_records = sp["complete_endpoint_readout_conclusion"]
    prior_gains = pw["complete_negative_inputs_conclusion"][
        "original_endpoint_gain_fields_read_verbatim"]
    require(all(prior_gains[key] == gain_records[key] for key in prior_gains)
            and set(prior_gains) == {
                "root_or_affine_jump_to_waist_density_gain",
                "ordinary_root_window_source_to_waist_density_gain",
                "strict_L1_Hminus1_source_to_waist_density_gain",
                "strict_L2_Hminus1_source_to_waist_density_gain"},
            "all four SP receiver balls copied literally through PW")
    for flag in ("all_Fourier_variations_and_two_means_retained",
                 "actual_radial_measure_used", "original_positive_graph_and_root_mixed_ports_retained"):
        require(sp["scope"][flag] is True, "complete SP scope: "+flag)
    require(pw["scope"]["finite_root_head_and_two_means_independent"] is True
            and pw["scope"]["raw_input_153over16_and_output9_are_distinct"] is True,
            "PW original root and independent mean coordinates")

    fixed = [value for value in wta["complete_fixed_cutoff_results"]
             if value["J"] == PARAMETERS["fixed_waist_normalizer_J"]]
    require(len(fixed) == 1 and fixed[0]["inverse_on_both_windows_proved"] is True
            and fixed[0]["finite_complement_and_two_means_identity"] is True
            and fixed[0]["strict_tests_passed"] == fixed[0]["strict_tests_total"] == 4
            and all(value["passed"] is True for value in fixed[0]["all_four_strict_tests"]),
            "the SAME fixed Js inverse including both mean identities")
    h_coord = wx["complete_selected_H_coordinate_conclusion"]
    common = wx["complete_selected_common_input_conclusion"]
    require(h_coord["only_same_selected_actual_conjugacy"] is True
            and h_coord["all_density_Jacobians_and_normalized_measures_retained"] is True
            and h_coord["independent_physical_mean_block_is_identity"] is True
            and common["no_projection_commuted_through_coordinate"] is True
            and common["rigid_rotation_isometry_does_not_change_norm"] is True
            and common["complete_inverse_H_output_L2_factor"]
                == h_coord["complete_inverse_density_L2_upper"]
            and wx["mathematical_parameters"]["exact_root_interval"] == ROOT_INTERVAL
            and wx["mathematical_parameters"]["fixed_intrinsic_parameter"] == "eta_0",
            "actual selected output density map, rotation and original left order")
    require(not any(name in sys.modules for name in ("flint", "numpy", "scipy")),
            "complete immutable admission precedes numerical imports")
    require(os.environ["GITHUB_RUN_ATTEMPT"] == "1" and not args.output.exists(),
            "one new never-overwritten scientific prefix")
    args.output.parent.mkdir(parents=True, exist_ok=True)
    document = {
        "identity": {"kind": KIND, "scalar_stage": STAGE,
            "source_sha256": specs["science"]["sha256"], "manifest_sha256": args.manifest_sha,
            "run_id": os.environ["GITHUB_RUN_ID"], "run_attempt": "1",
            "event_commit": os.environ["GITHUB_SHA"], "actual_checkout_commit": args.checkout,
            "arithmetic_bits": PARAMETERS["arithmetic_bits"]},
        "complete": False, "proved": False, "actual_returncode": None, "failure": None,
        "stage": "whole_actual_predecessors_admitted", "completed_targets": [],
        "current_target": None, "new_records": {}, "saved_record_count": 0,
        "parameters": copy.deepcopy(PARAMETERS), "result": None,
        "whole_completed_inputs": {role: {"file": copy.deepcopy(spec), "json_path": []}
                                  for role, spec in specs.items() if not spec["path"].endswith(".py")},
        "reference_identity": copy.deepcopy(ref),
        "selected_receiver_identity": {
            "complete_family_identity": copy.deepcopy(family),
            "selected_H_whole_source": {"file": copy.deepcopy(specs["WX_execution"]),
                "json_path": ["actual_scientific_receipt", "complete_selected_H_coordinate_conclusion"]},
            "fixed_Js": PARAMETERS["fixed_waist_normalizer_J"],
            "input_spaces_are_original_fourteen_physical_ports": True,
            "physical_ports_promoted_to_common_high_input": False},
        "high_response_source_binding": copy.deepcopy(ports["high_response_source_binding"]),
        "old_scientific_target_calls": 0, "new_arrays_published": 0, "new_artifacts": 0,
        "new_Releases": 0, "wall_seconds": 0.0, "runtime": {},
    }
    require(sorted(document) == SCI_FIELDS, "exact whole scientific schema")
    began = time.perf_counter()

    def save():
        document["wall_seconds"] = time.perf_counter()-began
        require(document["wall_seconds"] <= PARAMETERS["maximum_scientific_wall_seconds"],
                "bounded new scalar arithmetic with complete prefix")
        raw = canonical(document)
        require(len(raw) <= manifest["operation"]["maximum_scientific_bytes"],
                "complete scientific prefix fits the declared small-result budget")
        atomic(args.output, raw)

    save()
    try:
        import flint
        from importlib.metadata import version
        runtime = {"python": platform.python_version(), "packages": {"python-flint": version("python-flint")}}
        require(runtime == manifest["runtime"], "fixed directed scalar runtime")
        document["runtime"] = runtime
        flint.ctx.prec = PARAMETERS["arithmetic_bits"]

        class API:
            def __init__(self):
                self.arb = flint.arb; self.zero = self.arb(0); self.one = self.arb(1)
            def rational(self, n, d=1):
                require(type(n) is int and type(d) is int and d > 0, "exact rational")
                return self.arb(n)/self.arb(d)
            def lower(self, value):
                require(value.is_finite(), "finite lower"); return value.lower()
            def sqrt(self, value):
                require(value.is_finite() and value.lower() >= 0, "nonnegative square root")
                return value.sqrt()
            def interval(self, a, b):
                require(a.is_finite() and b.is_finite() and a.lower() <= b.upper(), "whole interval")
                return a.lower().union(b.upper())
            def old_interval(self, record):
                if isinstance(record, dict) and "lower" in record and "upper" in record:
                    return self.interval(self.arb(record["lower"]).lower(), self.arb(record["upper"]).upper())
                value = self.arb(record["ball"] if isinstance(record, dict) else record)
                require(value.is_finite(), "whole original scalar ball")
                return value

        api = API()
        core, pn = load("scalar_core"), load("pn_math")
        admitted = {
            "private_token": object(), "reference_identity": ref,
            "whole_actual_low_58_224_science_execution_and_manifest_verified": True,
            "same_selected_DF_physical_B_Cmean_height_and_jump_rows_verified": True,
            "whole_original_SP_PW_science_execution_and_domains_verified": True,
            "whole_actual_32_WPN_science_execution_and_manifest_verified": True,
            "whole_WTA_WX_and_original_left_receiver_order_verified": True,
        }
        pn._admit_chain(admitted, ports["result"], wpn["result"])
        cr = core.saved_upper(api, gain_records["root_or_affine_jump_to_waist_density_gain"])
        bh = core.saved_upper(api, h_coord["complete_inverse_density_L2_upper"])
        kw = core.saved_upper(api, fixed[0]["same_inverse_two_window_bounds"]["L2"])

        def emit(name, value):
            require(name == manifest["target_order"][document["saved_record_count"]]
                    and value.is_finite(), "complete column-major new scalar order")
            point = value.upper()
            require(point >= api.zero, "nonnegative final bound")
            record = {"ball": point.str(PARAMETERS["decimal_record_digits"]), "bound": "upper"}
            candidate = copy.deepcopy(document)
            candidate["new_records"][name] = record
            candidate["saved_record_count"] += 1
            candidate["completed_targets"].append(name)
            candidate["current_target"] = None
            candidate["stage"] = "complete_new_scalar_saved"
            candidate["wall_seconds"] = time.perf_counter()-began
            require(candidate["wall_seconds"] <= PARAMETERS["maximum_scientific_wall_seconds"],
                    "bounded candidate scalar arithmetic")
            raw = canonical(candidate)
            require(len(raw) <= manifest["operation"]["maximum_scientific_bytes"],
                    "whole candidate scientific prefix size")
            temporary = args.output.with_name(args.output.name+".candidate")
            atomic(temporary, raw)
            reread_document = parse(temporary.read_bytes())
            require(reread_document == candidate, "whole candidate document readback")
            reread = reread_document["new_records"][name]
            ball = api.arb(reread["ball"])
            require(reread == record and ball.is_finite() and ball.contains(point),
                    "whole saved new ball contains original upper and is read back")
            # Publish a completed prefix only AFTER the candidate's numerical readback.
            atomic(args.output, raw)
            document.clear()
            document.update(candidate)
            temporary.unlink()
            return ball.upper()

        def old_port(j, code):
            record = ports["new_records"]["port_%02d_%s_upper" % (j, code)]
            require(record["bound"] == "upper", "original complete224 directed upper")
            return core.saved_upper(api, record)

        for j in range(14):
            prefix = "negative_port_%02d_" % j
            c = api.one if j == 9 else api.zero
            root = pn.full_root(api, core, c, old_port(j, "low_root97"),
                                old_port(j, "high_root_mixed"))
            root_saved = emit(prefix+RECEIVER_CODES[0]+"_upper", root)
            # Every dependent expression uses the WHOLE saved predecessor.
            density_saved = emit(prefix+RECEIVER_CODES[1]+"_upper",
                                 core.upper(api, cr*root_saved))
            observed = pn.left_normalized_waist_observations(api, core, admitted,
                                                             density_saved, bh, kw)
            emit(prefix+RECEIVER_CODES[2]+"_upper",
                 observed["left_normalized_joint_two_branches_upper"])
            emit(prefix+RECEIVER_CODES[3]+"_upper",
                 observed["WPL_complete_physical_primitive_row_upper"])
        require(document["completed_targets"] == target_order()
                and document["saved_record_count"] == 56,
                "all14 physical columns and all4 complete receivers")
        document["result"] = {
            "kind": "complete_actual_fourteen_positive_ports_to_negative_receivers_v1",
            "reference_identity": copy.deepcopy(ref),
            "input_order": copy.deepcopy(ports["result"]["input_order"]),
            "output_order": list(RECEIVER_CODES),
            "output_qualifications": [
                "complete true root mixed H^-2/3 x H^-1, including actual root-even96",
                "complete homogeneous-negative old-circle waist primitive plus both physical means",
                "joint two left-normalized branches; original physical input unit unchanged",
                "WPL complete physical primitive row; original physical input unit unchanged"],
            "complete_new_record_order": target_order(), "complete_new_record_count": 56,
            "both_individual_branch_bounds_use_the_joint_branch_record": True,
            "both_density_means_joint_bound_uses_the_complete_waist_record": True,
            "every_root_to_waist_dependency_used_whole_saved_record_upper": True,
            "actual_general_L2_WPN_state_was_given_a_trace": False,
            "original_high_root_factor9_repeated": False,
            "physical_ports_promoted_to_common_Hminus4over3_input": False,
            "Ni_or_Lambda_right_input_change_performed": False,
            "same_primitive_or_density_mean_fee_repeated": False,
            "all_fourteen_positive_port_to_negative_bounds_proved": True,
            "particular_WPN_source_packet_status": "not_in_this_target_no_actual_packet_supplied",
            "particular_physical_WPN_source_receiver_proved": False,
            "common_high_Phi_Upsilon_strong_addition_size_proved": False,
            "new_negative_ordinary_source_size_proved": False,
            "signed_finite_matrix_entries_reconstructed": False,
            "complete_incoming_inverse_proved": False,
            "true_nu_or_phase_Schur_proved": False,
            "nonlinear_background_or_surface_proved": False,
            "topic_completion_proved": False,
            "old_completed_scientific_targets_recomputed": 0,
        }
        document["complete"] = document["proved"] = True
        document["actual_returncode"] = 0
        document["stage"] = "complete_"+STAGE+"_scalar_branch"
        save()
        return 0
    except BaseException as error:
        document["complete"] = document["proved"] = False
        document["actual_returncode"] = 1
        document["stage"] = "failed_with_complete_scalar_prefix"
        document["failure"] = {"type": type(error).__name__, "message": str(error)[:1500],
                               "traceback": traceback.format_exc()[-6000:]}
        print(traceback.format_exc(), flush=True)
        document["wall_seconds"] = time.perf_counter()-began
        atomic(args.output, canonical(document))
        return 1


if __name__ == "__main__":
    sys.exit(main())
