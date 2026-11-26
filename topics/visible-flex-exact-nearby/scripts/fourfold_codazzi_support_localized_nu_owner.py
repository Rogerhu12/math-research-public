"""SL: four new support-aware scalar combinations of complete old records.

No source, Green, Cauchy, SP, or earlier R147 target is re-evaluated.
The entire completed predecessor and D objects supply the only old bounds.
"""
from __future__ import annotations
import argparse, ast, copy, hashlib, importlib.util, json, os, platform, sys, time, traceback
from fractions import Fraction
from pathlib import Path

REPO = "Rogerhu12/math-research-public"
TOPIC = "topics/visible-flex-exact-nearby"
KIND = "R147_support_localized_selected_negative_nu_ordinary_v1"
STAGE = "support_localized_selected_negative_nu"
MANIFEST_KIND = "R147_support_localized_selected_negative_nu_inputs_v1"
SOURCE = TOPIC+"/scripts/fourfold_codazzi_support_localized_nu_owner.py"
MATH = TOPIC+"/scripts/fourfold_codazzi_support_localized_nu_math.py"
WORKER = TOPIC+"/scripts/fourfold_codazzi_support_localized_nu_public_worker.py"
GENERATOR = TOPIC+"/scripts/make_support_localized_nu_manifest.py"
PROOF = TOPIC+"/results/R147-supplement-support-localized-parameter-source-reception.md"
OLD = {
    "previous_actual": (TOPIC+"/notes/negative_nu_waist_ci/run-45781137624-1/actual-negative-nu-waist.json",
        "1a06d01060a63eac98aeaa330f130a8ee766ab5ac878634e637f9cea30e1cb70"),
    "previous_execution": (TOPIC+"/notes/negative_nu_waist_ci/run-45781137624-1/execution.json",
        "eeb4ed157912e742e8d773ca32b04570296973b924f4a92b1a4ec153c30efe2b"),
    "previous_manifest": (TOPIC+"/notes/2026-11-26-negative-nu-waist-inputs.json",
        "b697e8665801a6e4d5120ca312d72a339cc28a2516d6dabd255f56ee79690f2d"),
}
LEGACY_ROLES = ("D_execution", "D_manifest", "D_source", "proof_D", "proof_R147",
                "proof_SP", "proof_PW", "proof_SC", "reviewed_rules")
OLD_TARGETS = [
    "selected_negative_source_from_original_whole_body_upper",
    "selected_negative_source_from_same_fixed_window_upper",
    "complete_negative_ordinary_L2_to_waist_density_gain_upper",
    "selected_negative_nu_ordinary_to_waist_density_upper",
]
TARGETS = [
    "compact_parameter_source_L2_to_waist_gain_upper",
    "selected_base_and_state_change_negative_waist_upper",
    "selected_compact_parameter_change_negative_waist_upper",
    "selected_support_localized_negative_nu_ordinary_waist_upper",
]
PARAMETERS = {
    "arithmetic_bits": 320, "decimal_record_digits": 70,
    "maximum_scientific_wall_seconds": 300,
    "source": "F_nu(Q_delta,nu_delta)-(partial_r-A_delta)Z",
    "source_norm": "ordinary_L2_dr_L2_phi_complete_moving_pair",
    "source_split": "s_delta=s_0+(A_delta-A_0)Z+(F_nu_delta-F_nu_0)",
    "compact_support": ["1/20", "9/50"], "compact_length": "13/100",
    "exact_original_negative_window": ["0", "2383968743003/10000000000000"],
    "exact_strict_interval": ["0", "2333968743003/10000000000000"],
    "continuous_centre_definition_sha256": "440866a368f68b472bc904c90fbe9862f2ff13e9f884ffced6a4819c04866a47",
    "continuous_direction_definition_sha256": "6a71cb8109b095cd242823d181e7c1ef525355b9b90bf8c59f88668b68231d04",
    "fixed_intrinsic_parameter": "eta_0",
    "delta_budget_radius": "1/10000000000",
    "selected_member_run": "43588332723/1", "selected_member_loss": "1/250",
    "selected_to_budget_ratio_upper": "936826/1000000",
    "complete_output": "original_waist_primitive_pair_and_both_physical_density_means",
    "positive_inverse_or_incoming_used": False,
}
SCI_FIELDS = ["actual_returncode", "candidate_record", "complete", "completed_targets",
    "copied_prior_scalar_records", "current_target", "failure", "identity", "new_Releases",
    "new_arrays_published", "new_artifacts", "new_records", "old_scientific_target_calls",
    "parameters", "proved", "reference_identity", "result", "runtime", "saved_record_count",
    "selected_member_identity", "stage", "wall_seconds", "whole_completed_inputs"]


def require(ok, message):
    if not ok:
        raise ValueError(message)


def canonical(value):
    return (json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False,
                       allow_nan=False)+"\n").encode()


def parse(raw):
    return json.loads(raw, parse_constant=lambda x: (_ for _ in ()).throw(ValueError(x)))


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def descriptor(role, path, raw):
    return {"role": role, "path": path, "bytes": len(raw), "sha256": sha(raw),
            "git_blob_sha": hashlib.sha1(b"blob "+str(len(raw)).encode()+b"\0"+raw).hexdigest()}


def atomic(path, raw):
    temporary = path.with_name(path.name+".partial")
    with temporary.open("wb") as stream:
        stream.write(raw); stream.flush(); os.fsync(stream.fileno())
    os.replace(temporary, path)


def gather(root):
    """Read only complete small current objects; no numerical imports."""
    contents, specs = {}, {}

    def add(role, path):
        require(path.startswith(TOPIC+"/") and ".." not in Path(path).parts,
                "current topic input path")
        raw = (root/path).read_bytes()
        require(0 < len(raw) < 100000, "whole small UTF8 input: "+role)
        raw.decode()
        if path.endswith(".py"):
            ast.parse(raw.decode(), filename=path)
        contents[role] = raw
        specs[role] = descriptor(role, path, raw)

    for role, (path, digest) in OLD.items():
        add(role, path)
        require(specs[role]["sha256"] == digest, "complete immutable predecessor: "+role)
    legacy = {x["role"]: x for x in parse(contents["previous_manifest"])["files"]}
    for role in LEGACY_ROLES:
        add(role, legacy[role]["path"])
        require(specs[role] == legacy[role], "same original source/proof: "+role)
    for new_role, old_role in (("previous_science", "science"), ("worker_template", "worker")):
        add(new_role, legacy[old_role]["path"])
        expected = dict(legacy[old_role], role=new_role)
        require(specs[new_role] == expected, "same original complete source: "+new_role)
    for role, path in (("science", SOURCE), ("math", MATH), ("worker", WORKER),
                       ("generator", GENERATOR), ("proof", PROOF)):
        add(role, path)
    require(len({x["path"] for x in specs.values()}) == len(specs), "unique whole inputs")
    return contents, specs


def admit(contents, specs):
    """Only metadata, literal previous records, and exact rational support."""
    require(set(contents) == set(specs), "entire admitted input closure")
    for role, raw in contents.items():
        require(0 < len(raw) < 100000 and descriptor(role, specs[role]["path"], raw) == specs[role],
                "complete current input binding: "+role)
    for role, (path, digest) in OLD.items():
        require(specs[role]["path"] == path and specs[role]["sha256"] == digest,
                "immutable completed predecessor: "+role)
    old, execution, manifest = (parse(contents[k]) for k in OLD)
    old_specs = {x["role"]: x for x in manifest["files"]}
    require(old["identity"]["kind"] == "R147_complete_selected_negative_nu_ordinary_to_waist_v1"
            and old["identity"]["run_id"] == execution["run_id"] == "45781137624"
            and str(old["identity"]["run_attempt"]) == str(execution["run_attempt"]) == "1"
            and old["complete"] is old["proved"] is execution["complete"] is True
            and old["failure"] is execution["failure"] is None
            and old["actual_returncode"] == execution["actual_child_returncode"] == 0
            and old["completed_targets"] == OLD_TARGETS and old["saved_record_count"] == 4
            and old["candidate_record"] is old["current_target"] is None
            and set(old["new_records"]) == set(OLD_TARGETS)
            and old["identity"]["manifest_sha256"] == execution["manifest_sha256"]
                == specs["previous_manifest"]["sha256"]
            and old["identity"]["source_sha256"] == specs["previous_science"]["sha256"],
            "complete successful original R147 four-record actual and execution")
    require(execution["scientific_files"] == [{
                "path": specs["previous_actual"]["path"],
                "bytes": specs["previous_actual"]["bytes"],
                "sha256": specs["previous_actual"]["sha256"]}],
            "actual complete output is the one published by the predecessor")
    for role in LEGACY_ROLES:
        require(specs[role] == old_specs[role], "unchanged whole predecessor input: "+role)
    for new_role, old_role in (("previous_science", "science"), ("worker_template", "worker")):
        require(specs[new_role] == dict(old_specs[old_role], role=new_role),
                "complete previously bound executable: "+new_role)
    for key in ("continuous_centre_definition_sha256", "continuous_direction_definition_sha256",
                "fixed_intrinsic_parameter", "delta_budget_radius", "selected_member_run",
                "selected_member_loss", "selected_to_budget_ratio_upper",
                "exact_original_negative_window", "exact_strict_interval", "source", "source_norm"):
        require(old["parameters"][key] == PARAMETERS[key], "same original mathematical parameter: "+key)
    for key in ("both_physical_density_means_in_output", "complete_second_nonmean_source_admitted_by_SC2",
                "complete_negative_ordinary_to_waist_density_contribution_proved"):
        require(old["result"][key] is True, "whole completed receiver qualification: "+key)
    require(old["result"]["complete_nu_response_error_proved"] is False
            and old["result"]["complete_incoming_inverse_proved"] is False,
            "old partial scope is retained")
    de, dm = parse(contents["D_execution"]), parse(contents["D_manifest"])
    d = de["actual_scientific_receipt"]
    require(de["complete"] is d["complete"] is d["proved"] is True
            and de["actual_returncode"] == d["actual_returncode"] == 0
            and de["actual_failure"] is d["failure"] is None
            and de["run_id"] == d["run_id"] == "43713242980"
            and de["run_attempt"] == d["run_attempt"] == "1"
            and d["input_manifest_sha256"] == specs["D_manifest"]["sha256"]
            and d["source_sha256"] == specs["D_source"]["sha256"]
            and d["parameters"] == dm["parameters"]
            and len(d["gates"]) == 12 and all(x["passed"] is True for x in d["gates"])
            and d["complete_original_rows_verified"] == 7721
            and d["complete_nu_response_extra_source_sign"]
                == "Delta F_nu + Delta A times the same complete continuous Z",
            "whole actual D object with its separately saved source components")
    require(old["whole_completed_inputs"]["D_execution"]["file"] == specs["D_execution"]
            and old["whole_completed_inputs"]["D_manifest"]["file"] == specs["D_manifest"],
            "the predecessor really used this entire D execution and manifest")
    fees = d["complete_scalar_fee_conclusions"]
    negative, compact = fees["fixed_negative_window"], fees["compact_metric_support"]
    require(negative["exact_interval"] == PARAMETERS["exact_original_negative_window"]
            and compact["exact_interval"] == PARAMETERS["compact_support"]
            and compact["exact_total_radial_measure"] == PARAMETERS["compact_length"]
            and negative["ordinary_L2_bounds"]["N_nu"] == compact["ordinary_L2_bounds"]["N_nu"],
            "original compact metric source and full state-change source stay distinct")
    require(Fraction(PARAMETERS["compact_support"][1])
                < Fraction(PARAMETERS["exact_strict_interval"][1])
            and Fraction(PARAMETERS["compact_support"][1])
                - Fraction(PARAMETERS["compact_support"][0]) == Fraction(PARAMETERS["compact_length"]),
            "the entire true support is strictly below the root window")
    prior = old["copied_prior_scalar_records"]
    saved = {
        "S_N": prior["source_zero_same_fixed_negative_full"],
        "A_N": negative["ordinary_L2_bounds"]["M1_Zphi_plus_M0_Z"],
        "N_C": compact["ordinary_L2_bounds"]["N_nu"],
        "C1": prior["original_SP_PW_negative_gains"]["strict_L1_Hminus1_source_to_waist_density_gain"],
        "G_N": old["new_records"][OLD_TARGETS[2]],
    }
    require(not any(x in sys.modules for x in ("flint", "numpy", "scipy")),
            "admission is metadata-only, not an old-target rerun")
    return old, copy.deepcopy(saved)


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    for name in ("manifest", "input-map", "output"):
        ap.add_argument("--"+name, required=True, type=Path)
    ap.add_argument("--manifest-sha", required=True)
    ap.add_argument("--checkout", required=True)
    a = ap.parse_args()
    require(os.environ.get("GITHUB_ACTIONS") == "true"
            and os.environ.get("GITHUB_REPOSITORY") == REPO
            and os.environ.get("GITHUB_RUN_ATTEMPT") == "1", "new scalar science only on public Actions")
    manifest_raw = a.manifest.read_bytes()
    require(sha(manifest_raw) == a.manifest_sha, "whole current launch manifest")
    manifest = parse(manifest_raw)
    require(manifest["kind"] == MANIFEST_KIND and manifest["scientific_kind"] == KIND
            and manifest["stage"] == STAGE and manifest["parameters"] == PARAMETERS
            and manifest["target_order"] == TARGETS and manifest["complete_record_counts"] == [4]
            and manifest["allowed_scientific_fields"] == SCI_FIELDS, "one exact new scalar branch")
    specs = {x["role"]: x for x in manifest["files"]}
    paths = parse(a.input_map.read_bytes())
    require(set(paths) == set(specs) and len(specs) == len(manifest["files"]), "complete immutable inputs")
    contents = {k: Path(v).read_bytes() for k, v in paths.items()}
    require(sha(Path(__file__).read_bytes()) == specs["science"]["sha256"], "this pinned new owner")
    old, saved = admit(contents, specs)
    sys.dont_write_bytecode = True
    module_spec = importlib.util.spec_from_file_location("_R147_support_math", paths["math"])
    math = importlib.util.module_from_spec(module_spec)
    module_spec.loader.exec_module(math)
    require(list(math.TARGETS) == TARGETS, "same four explicit mathematical expressions")
    require(not a.output.exists(), "never overwrite previous science")
    a.output.parent.mkdir(parents=True, exist_ok=True)
    document = {
        "identity": {"kind": KIND, "scalar_stage": STAGE, "source_sha256": specs["science"]["sha256"],
            "manifest_sha256": a.manifest_sha, "run_id": os.environ["GITHUB_RUN_ID"], "run_attempt": "1",
            "event_commit": os.environ["GITHUB_SHA"], "actual_checkout_commit": a.checkout,
            "arithmetic_bits": PARAMETERS["arithmetic_bits"]},
        "complete": False, "proved": False, "actual_returncode": None, "failure": None,
        "stage": "whole_support_source_inputs_admitted", "completed_targets": [], "current_target": None,
        "candidate_record": None, "new_records": {}, "saved_record_count": 0,
        "parameters": copy.deepcopy(PARAMETERS), "result": None,
        "whole_completed_inputs": {k: copy.deepcopy(v) for k, v in specs.items()},
        "reference_identity": copy.deepcopy(old["reference_identity"]),
        "selected_member_identity": copy.deepcopy(old["selected_member_identity"]),
        "copied_prior_scalar_records": {**saved,
            "previous_complete_negative_ordinary_contribution": copy.deepcopy(old["new_records"][OLD_TARGETS[3]])},
        "old_scientific_target_calls": 0, "new_arrays_published": 0, "new_artifacts": 0,
        "new_Releases": 0, "wall_seconds": 0.0, "runtime": {},
    }
    require(sorted(document) == SCI_FIELDS, "complete declared scientific envelope")
    began = time.perf_counter()

    def save():
        document["wall_seconds"] = time.perf_counter()-began
        require(document["wall_seconds"] < PARAMETERS["maximum_scientific_wall_seconds"], "short scalar budget")
        raw = canonical(document)
        require(len(raw) <= manifest["operation"]["maximum_scientific_bytes"], "complete small result")
        atomic(a.output, raw)

    save()
    try:
        import flint
        from importlib.metadata import version
        runtime = {"python": platform.python_version(), "packages": {"python-flint": version("python-flint")}}
        require(runtime == manifest["runtime"], "same directed scalar runtime")
        document["runtime"] = runtime
        flint.ctx.prec = PARAMETERS["arithmetic_bits"]
        arb = flint.arb

        def old_upper(record):
            value = arb(record["ball"])
            if "lower" in record and "upper" in record:
                value = value.union(arb(record["lower"])).union(arb(record["upper"]))
            require(value.is_finite() and value.lower() >= 0, "whole nonnegative old scalar ball")
            return value.upper()

        def emit(name, value):
            require(name == TARGETS[document["saved_record_count"]] and value.is_finite()
                    and value >= 0 and document["candidate_record"] is None, "next complete new scalar")
            point = value.upper()
            record = {"ball": point.str(PARAMETERS["decimal_record_digits"]), "bound": "upper"}
            document["candidate_record"] = {"name": name, "record": record}
            document["current_target"] = name
            document["stage"] = "whole_support_scalar_candidate_saved"
            save()
            reread = parse(a.output.read_bytes())["candidate_record"]
            require(reread == {"name": name, "record": record} and arb(record["ball"]).contains(point),
                    "whole saved candidate contains the directed value")
            document["new_records"][name] = record
            document["completed_targets"].append(name)
            document["saved_record_count"] += 1
            document["candidate_record"] = document["current_target"] = None
            document["stage"] = "complete_support_scalar_saved"
            save()
            formal = parse(a.output.read_bytes())["new_records"][name]
            require(formal == record and arb(formal["ball"]).contains(point), "formal complete ball retained")
            return arb(formal["ball"]).upper()

        class API:
            zero = arb(0)

            @staticmethod
            def rational(numerator, denominator):
                return arb(numerator)/arb(denominator)

            @staticmethod
            def sqrt(value):
                return value.sqrt()

        values = math.receive(API(), {k: old_upper(v) for k, v in saved.items()}, emit)
        previous = arb(old["new_records"][OLD_TARGETS[3]]["ball"])
        require(values["complete_negative_ordinary_contribution"] < previous.lower(),
                "new complete saved bound strictly improves the untouched original record")
        require(values["complete_negative_ordinary_contribution"] < arb(187)/arb(1000000),
                "complete improved ordinary contribution is strictly below 0.000187")
        require(values["localized_receiver"] < old_upper(saved["G_N"]), "genuine support receiver improvement")
        document["result"] = {
            "kind": KIND, "complete_new_record_count": 4, "complete_new_record_order": list(TARGETS),
            "same_selected_original_source_and_receiver": True,
            "source_split_made_before_receiver_norms": True,
            "only_parameter_difference_is_compact": True,
            "both_physical_density_means_in_output": True,
            "complete_second_nonmean_source_admitted_by_SC2": True,
            "complete_negative_ordinary_to_waist_density_contribution_proved": True,
            "whole_saved_dependency_uppers_used": True,
            "strict_improvement_of_previous_complete_record_proved": True,
            "strict_upper_187_over_1000000_proved": True,
            "old_Cauchy_source_or_strict_computation_repeated": False,
            "positive_root_interface_exterior_phase_inputs_included": False,
            "complete_nu_response_error_proved": False, "complete_incoming_inverse_proved": False,
            "true_nu_or_phase_Schur_proved": False, "topic_completion_proved": False,
        }
        document["complete"] = document["proved"] = True
        document["actual_returncode"] = 0
        document["stage"] = "complete_"+STAGE+"_scalar_branch"
        save()
        return 0
    except BaseException as error:
        document["complete"] = document["proved"] = False
        document["actual_returncode"] = 1
        document["stage"] = "failed_with_complete_support_scalar_prefix"
        document["failure"] = {"type": type(error).__name__, "message": str(error)[:2000],
                               "traceback": traceback.format_exc()[-5000:]}
        document["wall_seconds"] = time.perf_counter()-began
        atomic(a.output, canonical(document))
        traceback.print_exc()
        return 1


if __name__ == "__main__":
    sys.exit(main())
