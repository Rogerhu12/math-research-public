"""Consume complete Grassmann maps for the original 58/224/32 physical stages."""
from __future__ import annotations
import argparse, ast, copy, hashlib, importlib.util, json, os, platform, re, sys, time, traceback
from pathlib import Path
from fractions import Fraction

REPO = "Rogerhu12/math-research-public"
KIND = "complete_actual_positive_physical_scalar_stage_v1"
PARAMETERS = {"arithmetic_bits": 320, "decimal_record_digits": 60,
              "maximum_scientific_wall_seconds": 900,
              "old_completed_target_calls": 0,
              "ordinary_radial_measure": "dr", "normalised_angular_measure": True,
              "original_WPN_radial_projection_cells": 24480}
SCI_FIELDS = sorted([
    "identity", "complete", "proved", "actual_returncode", "failure", "stage",
    "completed_targets", "current_target", "new_records", "saved_record_count",
    "parameters", "result", "whole_completed_inputs", "reference_identity",
    "high_response_source_binding", "old_scientific_target_calls", "new_arrays_published",
    "new_artifacts", "new_Releases", "wall_seconds", "runtime",
])
PRIVATE_RESULT_FIELDS = {
    "source_receivers", "kappa", "boundary", "outer_b_poisson_low",
    "positive_outer_block_upper", "physical_block_inverse_majorant", "private_readback_values",
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
    return json.loads(raw, parse_constant=lambda v: (_ for _ in ()).throw(ValueError(v)))


def atomic(path, raw):
    temporary = path.with_name(path.name+".partial")
    with temporary.open("wb") as stream:
        stream.write(raw); stream.flush(); os.fsync(stream.fileno())
    os.replace(temporary, path)
    require(path.read_bytes() == raw, "whole new scalar-prefix byte readback")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--manifest", type=Path, required=True)
    parser.add_argument("--manifest-sha", required=True)
    parser.add_argument("--input-map", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--checkout", required=True)
    args = parser.parse_args()
    require(os.environ.get("GITHUB_ACTIONS") == "true" and os.environ.get("GITHUB_REPOSITORY") == REPO,
            "new scalar work only in this public own Actions repository")
    raw_manifest = args.manifest.read_bytes()
    require(sha(raw_manifest) == args.manifest_sha, "entire actual stage manifest")
    manifest = parse(raw_manifest)
    require(manifest["scientific_kind"] == KIND and manifest["parameters"] == PARAMETERS
            and manifest["stage"] in ("gate", "ports", "wpn"), "one exact scalar stage")
    specs = {s["role"]: s for s in manifest["files"]}
    paths = parse(args.input_map.read_bytes())
    require(set(paths) == set(specs), "all complete small current inputs")
    contents = {}
    for role, spec in specs.items():
        raw = Path(paths[role]).read_bytes()
        require(0 < len(raw) < 100000 and len(raw) == spec["bytes"]
                and sha(raw) == spec["sha256"] and blob(raw) == spec["git_blob_sha"],
                "whole input identity: "+role)
        contents[role] = raw
    require(sha(Path(__file__).read_bytes()) == specs["science"]["sha256"], "exact bound owner")

    def data(role):
        return parse(contents[role])

    def load(role):
        module_spec = importlib.util.spec_from_file_location("_physical_chain_"+role, paths[role])
        require(module_spec is not None and module_spec.loader is not None, "explicit pure module")
        module = importlib.util.module_from_spec(module_spec)
        module_spec.loader.exec_module(module)
        return module

    def pair(actual_role, execution_role, manifest_role=None, expected_run=None):
        actual, execution = data(actual_role), data(execution_role)
        identity = actual.get("identity", actual)
        require(actual["complete"] is True and actual.get("failure") is None
                and execution.get("scientific_complete", execution.get("complete")) is True
                and execution.get("failure") is None and execution["actual_child_returncode"] == 0
                and actual.get("actual_returncode", 0) == 0,
                "complete actual/scientific pair: "+actual_role)
        if "run_id" in identity:
            require(identity["run_id"] == execution["run_id"]
                    and identity["run_attempt"] == execution["run_attempt"], "same actual run")
        if expected_run is not None:
            require(execution["run_id"] == expected_run and execution["run_attempt"] == "1",
                    "the immutable original input run: "+actual_role)
        receipt = [s for s in execution["scientific_files"] if s["path"] == specs[actual_role]["path"]]
        require(receipt == [{k: specs[actual_role][k] for k in ("path", "bytes", "sha256")}],
                "execution identifies the complete scientific file")
        if manifest_role is not None:
            old_manifest = data(manifest_role)
            require(identity["manifest_sha256"] == execution["manifest_sha256"] == specs[manifest_role]["sha256"],
                    "whole predecessor manifest is bound to both actual files")
            if "operation" in old_manifest and "scientific_field_names" in old_manifest["operation"]:
                op = old_manifest["operation"]
                require(sorted(actual) == op["scientific_field_names"]
                        and actual["scientific_modules"] == op["scientific_module_binding"]
                        and actual["parameters"] == old_manifest["parameters"]
                        and actual["complete_current_file_receipts"] == old_manifest["files"]
                        and execution["current_input_receipts"] == old_manifest["files"]
                        and [x["name"] for x in actual["gates"]] == op["complete_gate_names"]
                        and all(x["passed"] is True for x in actual["gates"]),
                        "entire original scientific schema, inputs and final gates")
            elif old_manifest.get("kind") == "actual_positive_physical_scalar_stage_inputs_v1":
                require(sorted(actual) == old_manifest["allowed_scientific_fields"]
                        and actual["parameters"] == old_manifest["parameters"]
                        and actual["completed_targets"] == old_manifest["target_order"][:actual["saved_record_count"]]
                        and actual["saved_record_count"] in old_manifest["complete_record_counts"]
                        and execution["current_input_receipts"] == old_manifest["files"]
                        and actual["identity"]["source_sha256"] == next(
                            x["sha256"] for x in old_manifest["files"] if x["role"] == "science"),
                        "entire paid prior scalar-stage schema and original source binding")
        return actual, execution

    low, lowe = pair("low_actual", "low_execution", "low_manifest")
    core = load("closure_math")
    validator = load("grassmann_validator")
    bound = {role: specs[role] for role in (
        "true_low193_grassmann_owner","grassmann_validator","grassmann_math","grassmann_runner",
        "grassmann_carriers","original81_restore","grassmann_proof",
        "true_low193_whole_child_coefficients","true_low193_direct_flow_math")}
    validator.admit_success(contents["low_actual"],contents["low_execution"],contents["low_manifest"],
        actual_spec=specs["low_actual"],execution_spec=specs["low_execution"],manifest_spec=specs["low_manifest"],
        expected_reference=data("gh5_actual")["reference_identity"],bound_definitions=bound)
    gh5, gh5e = pair("gh5_actual", "gh5_execution", expected_run="44736533396")
    gh4, gh4e = pair("gh4_actual", "gh4_execution", expected_run="44740105701")
    D, De = pair("D_actual", "D_execution", "D_manifest", "44745017016")
    L, Le = pair("L_actual", "L_execution", expected_run="44724797559")
    weighted, weightede = pair("weighted_actual", "weighted_execution", "weighted_manifest", "44746534556")
    base0, basep, negative, negativep = (data(role) for role in
        ("base0_summary", "base0_process", "negative_summary", "negative_process"))
    high_admission = load("original_high_admission")
    high_admission.admit_original_high_reports(base0, basep, negative, negativep,
                                              specs["base0_summary"], specs["negative_summary"])
    gate = gatee = port = porte = whva = None
    if manifest["stage"] in ("ports", "wpn"):
        gate, gatee = pair("gate_actual", "gate_execution", "gate_manifest")
        require(gate["identity"]["kind"] == KIND and gate["identity"]["scalar_stage"] == "gate"
                and gate["proved"] is True and gate["saved_record_count"] == 58
                and gate["result"]["same_actual_physical_outer_gate_passed"] is True,
                "the whole actual58 physical gate precedes the port stage")
        for role in ("low_actual", "low_execution", "low_manifest", "weighted_actual", "weighted_execution", "D_actual", "D_execution"):
            require(gate["whole_completed_inputs"][role]["file"] == specs[role],
                    "same exact actual-input chain through the paid58 gate: "+role)
    if manifest["stage"] == "wpn":
        port, porte = pair("ports_actual", "ports_execution", "ports_manifest")
        whva, whvae = pair("WHVA_actual", "WHVA_execution", expected_run="43838214094")
        require(port["identity"]["kind"] == KIND and port["identity"]["scalar_stage"] == "ports"
                and port["proved"] is True and port["saved_record_count"] == 224,
                "all224 actual port bounds precede WPN")
        for role in ("low_actual", "low_execution", "gate_actual", "gate_execution", "gate_manifest", "weighted_actual", "D_actual"):
            require(port["whole_completed_inputs"][role]["file"] == specs[role],
                    "same exact actual-input chain through all224 ports: "+role)
        require("q=Fraction(max(scale//8," in contents["exact_reference_source"].decode()
                and "N=24480" in contents["WPN_lifting_proof"].decode().replace(" ", ""),
                "the original exact q floor and original24480 projection proof are explicit inputs")
    require(not any(n in sys.modules for n in ("flint", "numpy", "scipy")),
            "whole prior admission precedes numerical imports")
    require(os.environ["GITHUB_RUN_ATTEMPT"] == "1" and not args.output.exists(),
            "one never-overwritten new stage")
    args.output.parent.mkdir(parents=True, exist_ok=True)
    document = {
        "identity": {"kind": KIND, "scalar_stage": manifest["stage"], "source_sha256": specs["science"]["sha256"],
            "manifest_sha256": args.manifest_sha, "run_id": os.environ["GITHUB_RUN_ID"], "run_attempt": "1",
            "event_commit": os.environ["GITHUB_SHA"], "actual_checkout_commit": args.checkout,
            "arithmetic_bits": PARAMETERS["arithmetic_bits"]},
        "complete": False, "proved": False, "actual_returncode": None, "failure": None,
        "stage": "whole_actual_predecessors_admitted", "completed_targets": [], "current_target": None,
        "new_records": {}, "saved_record_count": 0, "parameters": copy.deepcopy(PARAMETERS),
        "result": None, "whole_completed_inputs": {role: {"file": copy.deepcopy(spec), "json_path": []}
            for role, spec in specs.items() if not spec["path"].endswith(".py")},
        "reference_identity": copy.deepcopy(low["reference_identity"]), "high_response_source_binding": None,
        "old_scientific_target_calls": 0, "new_arrays_published": 0, "new_artifacts": 0,
        "new_Releases": 0, "wall_seconds": 0.0, "runtime": {}}
    require(sorted(document) == SCI_FIELDS, "complete exact scientific output schema")
    began = time.perf_counter()

    def save():
        document["wall_seconds"] = time.perf_counter()-began
        require(document["wall_seconds"] <= PARAMETERS["maximum_scientific_wall_seconds"],
                "bounded scalar evaluation wall; complete prefix retained")
        raw = canonical(document)
        require(len(raw) <= manifest["operation"]["maximum_scientific_bytes"], "whole scalar prefix size")
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
            def lower(self, x):
                require(x.is_finite(), "finite scalar lower"); return x.lower()
            def sqrt(self, x):
                require(x.is_finite() and x.lower() >= 0, "nonnegative square root"); return x.sqrt()
            def interval(self, a, b):
                require(a.is_finite() and b.is_finite() and a.lower() <= b.upper(), "whole finite interval")
                return a.lower().union(b.upper())
            def hull(self, values):
                require(values and all(v.is_finite() for v in values), "finite nonempty hull")
                value = values[0]
                for v in values[1:]: value = value.union(v)
                return value
            def old_interval(self, record):
                if isinstance(record, dict) and "lower" in record and "upper" in record:
                    return self.interval(self.arb(record["lower"]).lower(), self.arb(record["upper"]).upper())
                value = self.arb(record["ball"] if isinstance(record, dict) else record)
                require(value.is_finite(), "whole old finite scalar record"); return value
        api = API()
        admitted = core.admit_complete_inputs(api, low, lowe, gh5, gh5e, gh4, gh4e,
            D, De, L, Le, negative, weighted=weighted, weighted_execution=weightede)
        document["high_response_source_binding"] = copy.deepcopy(admitted["high_response_source_binding"])

        def emit(name, value, bound):
            require(bound in ("upper", "lower") and value.is_finite(), "whole directed endpoint")
            require(manifest["target_order"][document["saved_record_count"]] == name,
                    "exact complete stage record order")
            point = value.upper() if bound == "upper" else value.lower()
            record = {"ball": point.str(PARAMETERS["decimal_record_digits"]), "bound": bound}
            candidate = copy.deepcopy(document)
            candidate["new_records"][name] = record
            candidate["saved_record_count"] += 1
            candidate["completed_targets"].append(name)
            candidate["current_target"] = None
            candidate["stage"] = "complete_new_scalar_saved"
            candidate["wall_seconds"] = time.perf_counter()-began
            require(candidate["wall_seconds"] <= PARAMETERS["maximum_scientific_wall_seconds"],
                    "bounded scalar evaluation wall before accepting a new record")
            raw = canonical(candidate)
            require(len(raw) <= manifest["operation"]["maximum_scientific_bytes"],
                    "whole candidate scalar-prefix size")
            candidate_path = args.output.with_name(args.output.name+".candidate")
            atomic(candidate_path, raw)
            reread_raw = candidate_path.read_bytes()
            reread = parse(reread_raw)
            require(reread_raw == raw and reread == candidate,
                    "entire candidate scalar prefix read back before acceptance")
            saved = reread["new_records"][name]
            ball = api.arb(saved["ball"])
            require(saved == record and ball.contains(point),
                    "whole candidate ball contains the original endpoint")
            candidate_path.replace(args.output)
            document.clear(); document.update(reread)
            require(args.output.read_bytes() == raw, "same verified bytes in formal scalar prefix")
            return ball.upper() if bound == "upper" else ball.lower()

        def read_saved(doc, name, bound="upper"):
            record = doc["new_records"][name]
            require(record["bound"] == bound, "the actual saved endpoint direction")
            ball = api.arb(record["ball"])
            require(ball.is_finite(), "whole complete saved endpoint")
            return ball.upper() if bound == "upper" else ball.lower()

        if manifest["stage"] == "gate":
            result = core.complete_new_scalar_closure(api, admitted, emit)
            document["proved"] = result["same_actual_physical_outer_gate_passed"]
        elif manifest["stage"] == "ports":
            closed = core.restore_complete_gate_from_saved_records(api, admitted, gate)
            ports_math = load("ports_math")
            result = ports_math.complete_original_ports(api, core, admitted, closed, weighted,
                lambda n, b: read_saved(gate, n, b), emit)
            document["proved"] = True
        else:
            wpn_math = load("wpn_math")
            wpn_admitted = {"private_token": object(), "reference_identity": admitted["reference_identity"],
                "same_original_WOB_operator_and_S_verified": True,
                "whole_prior_58_and_224_results_and_executions_verified": True,
                "whole_WHVA_and_reference_boundary_executions_verified": True,
                "original_24480_projection_and_q_floor_verified": True}
            result = wpn_math.complete_two_row_response(api, core, wpn_admitted, port["result"], whva, D,
                lambda col, code: read_saved(port, "port_%02d_%s_upper" % (col, code)), emit)
            document["proved"] = True
        require(result["complete_new_record_order"] == document["completed_targets"]
                and document["saved_record_count"] in manifest["complete_record_counts"],
                "one exact complete mathematical branch")
        document["result"] = {k: copy.deepcopy(v) for k, v in result.items() if k not in PRIVATE_RESULT_FIELDS}
        require(document["result"]["topic_completion_proved"] is False, "whole task remains separate")
        document["complete"] = True; document["actual_returncode"] = 0
        document["stage"] = "complete_"+manifest["stage"]+"_scalar_branch"
        save()
        return 0
    except BaseException as error:
        document["complete"] = False; document["proved"] = False; document["actual_returncode"] = 1
        document["stage"] = "failed_with_complete_scalar_prefix"
        document["failure"] = {"type": type(error).__name__, "message": str(error)[:1500],
            "traceback": traceback.format_exc()[-6000:]}
        print(traceback.format_exc(), flush=True)
        # Preserve the prefix even if the exception was the wall budget.
        document["wall_seconds"] = time.perf_counter()-began
        atomic(args.output, canonical(document))
        return 1


if __name__ == "__main__":
    sys.exit(main())
