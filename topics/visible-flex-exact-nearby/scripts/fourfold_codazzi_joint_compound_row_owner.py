"""JC: seven new directed joint-row scalars from complete old conclusions.

No original KAM, DFT row, PDE trial, residual or norm target is executed.
The entire fixed RW input admission is reused as readonly standard-library
code. All three new lowers and four uppers are saved and read back before
their use in another new scalar.
"""
from __future__ import annotations
import argparse, ast, copy, gzip, hashlib, json, os, platform, sys, time, traceback, types
from pathlib import Path
from fractions import Fraction

REPO = "Rogerhu12/math-research-public"
TOPIC = "topics/visible-flex-exact-nearby"
KIND = "R149_complete_joint_compound_waist_row_error_v1"
STAGE = "joint_compound_waist_row_error"
MANIFEST_KIND = "R149_complete_joint_compound_row_inputs_v1"
SOURCE_PATH = TOPIC+"/scripts/fourfold_codazzi_joint_compound_row_owner.py"
WORKER_PATH = TOPIC+"/scripts/fourfold_codazzi_joint_compound_row_public_worker.py"
GENERATOR_PATH = TOPIC+"/scripts/make_joint_compound_row_manifest.py"
OLD_MANIFEST = TOPIC+"/notes/2026-11-26-reflected-waist-rows-inputs.json"
RENAMED_RW_ROLES = {name: "RW_"+name for name in ("science", "worker", "generator", "proof")}
TARGETS = [
    "Wiener_strip_interpolation_derivative_lower",
    "saved_derivative_interpolation_lower",
    "complete_interpolation_derivative_lower",
    "joint96_composition_error_upper",
    "joint96_Wiener_input_operator_upper",
    "complete_joint96_DFT_tail_and_alias_upper",
    "complete_joint96_scalar_row_operator_error_upper",
]
PARAMETERS = {
    "arithmetic_bits": 320, "decimal_record_digits": 60,
    "maximum_scientific_wall_seconds": 120,
    "row_modes": 96, "physical_frequency_factor": 4,
    "physical_period": "pi/2", "normalized_angular_measure": True,
    "original_conjugacy_strip": "1/128", "original_selected_loss": "1/250",
    "original_selected_run": "43588332723/1", "trial_fourier_cutoff": 1024,
    "grid_points": 4096, "fixed_original_waist_normalizer_cutoff": 268435456,
    "old_numerical_producers_called": 0, "original_DFT_rows_recomputed": 0,
    "new_complete_joint_scalar_records": 7,
}
SCI_FIELDS = sorted([
    "identity", "complete", "proved", "actual_returncode", "failure", "stage",
    "completed_targets", "current_target", "candidate_record", "new_records",
    "saved_record_count", "parameters", "result", "whole_completed_inputs",
    "reference_identity", "selected_member_identity", "copied_prior_scalar_records",
    "old_scientific_target_calls", "new_arrays_published", "new_artifacts",
    "new_Releases", "wall_seconds", "runtime",
])


def require(ok, message):
    if not ok:
        raise ValueError(message)


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def blob(raw):
    return hashlib.sha1(b"blob "+str(len(raw)).encode()+b"\0"+raw).hexdigest()


def parse(raw):
    return json.loads(raw, parse_constant=lambda x: (_ for _ in ()).throw(ValueError(x)))


def canonical(value):
    return (json.dumps(value, sort_keys=True, separators=(",", ":"),
                       ensure_ascii=False, allow_nan=False)+"\n").encode()


def atomic(path, raw):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    temp = path.with_name(path.name+".tmp")
    with temp.open("wb") as f:
        f.write(raw)
        f.flush()
        os.fsync(f.fileno())
    os.replace(temp, path)


def definitions(raw, name):
    """Load byte-admitted definitions; their numerical main is never called."""
    module = types.ModuleType(name)
    module.__file__ = name
    ast.parse(raw.decode(), filename=name)
    exec(compile(raw, name, "exec"), module.__dict__)
    return module


def admit_complete_inputs(contents, specs):
    require(set(contents) == set(specs), "all whole current and original native inputs")
    for role, spec in specs.items():
        raw = contents[role]
        require(type(raw) is bytes and len(raw) == spec["bytes"]
                and sha(raw) == spec["sha256"] and blob(raw) == spec["git_blob_sha"],
                "complete original bytes: "+role)
        if spec.get("encoding") != "gzip-json":
            require(0 < len(raw) < 100000, "complete small UTF8 input")
            raw.decode("utf-8")
            if spec["path"].endswith(".py"):
                ast.parse(raw.decode(), filename=spec["path"])
    require(specs["science"]["path"] == SOURCE_PATH
            and specs["worker"]["path"] == WORKER_PATH
            and specs["generator"]["path"] == GENERATOR_PATH
            and specs["RW_manifest"]["path"] == OLD_MANIFEST,
            "exact source and unchanged old RW definition paths")
    old = parse(contents["RW_manifest"])
    require(old["kind"] == "R149_complete_reflected_finite_waist_row_inputs_v1"
            and old["stage"] == "reflected_finite_waist_rows"
            and old["complete_record_counts"] == [96],
            "the whole original RW manifest, not a new trial definition")
    old_specs, old_contents = {}, {}
    for spec in old["files"]+old["historical_inputs"]:
        role = spec["role"]
        here = RENAMED_RW_ROLES.get(role, role)
        require(here in specs and dict(specs[here], role=role) == spec,
                "unchanged complete old RW input: "+role)
        old_specs[role], old_contents[role] = spec, contents[here]
    extra = {"science", "worker", "generator", "proof", "joint_math", "RW_manifest"}
    expected = {RENAMED_RW_ROLES.get(s["role"], s["role"])
                for s in old["files"]+old["historical_inputs"]} | extra
    require(set(specs) == expected, "all and only complete JC and original RW inputs")
    rw = definitions(contents["RW_science"], "_readonly_original_RW_admission")
    prior = rw.admit_complete_inputs(old_contents, old_specs)
    joint = definitions(contents["joint_math"], "_pure_JC_definitions")
    require(list(joint.OUTPUT_ORDER) == TARGETS
            and all(PARAMETERS[key] == value for key, value in joint.PARAMETERS.items()),
            "the proved joint formula, real frequency and original strip")
    records = joint.original_W_records(prior["W"])
    require(not any(name in sys.modules for name in ("flint", "numpy", "scipy")),
            "admission executes no numerical producer")
    return prior, records


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--manifest", type=Path, required=True)
    ap.add_argument("--manifest-sha", required=True)
    ap.add_argument("--input-map", type=Path, required=True)
    ap.add_argument("--output", type=Path, required=True)
    ap.add_argument("--checkout", required=True)
    args = ap.parse_args()
    require(os.environ.get("GITHUB_ACTIONS") == "true"
            and os.environ.get("GITHUB_REPOSITORY") == REPO
            and os.environ.get("GITHUB_RUN_ATTEMPT") == "1",
            "one new child in the authorized public repository")
    raw_manifest = args.manifest.read_bytes()
    require(sha(raw_manifest) == args.manifest_sha, "entire actual JC manifest")
    manifest = parse(raw_manifest)
    require(manifest["kind"] == MANIFEST_KIND and manifest["scientific_kind"] == KIND
            and manifest["stage"] == STAGE and manifest["parameters"] == PARAMETERS
            and manifest["target_order"] == TARGETS and manifest["complete_record_counts"] == [7]
            and manifest["allowed_scientific_fields"] == SCI_FIELDS,
            "one complete new seven-scalar JC target")
    specs = {s["role"]: s for s in manifest["files"]+manifest["historical_inputs"]}
    paths = parse(args.input_map.read_bytes())
    require(set(paths) == set(specs), "complete restored input map")
    contents = {role: Path(path).read_bytes() for role, path in paths.items()}
    require(sha(Path(__file__).read_bytes()) == specs["science"]["sha256"],
            "the actual new numerical source is pinned")
    prior, records = admit_complete_inputs(contents, specs)
    require(not args.output.exists(), "never overwrite a completed or failed prefix")
    document = {
        "identity": {
            "kind": KIND, "scalar_stage": STAGE,
            "source_sha256": specs["science"]["sha256"],
            "joint_math_sha256": specs["joint_math"]["sha256"],
            "manifest_sha256": args.manifest_sha,
            "run_id": os.environ["GITHUB_RUN_ID"], "run_attempt": "1",
            "event_commit": os.environ["GITHUB_SHA"], "actual_checkout_commit": args.checkout,
            "arithmetic_bits": PARAMETERS["arithmetic_bits"],
        },
        "complete": False, "proved": False, "actual_returncode": None, "failure": None,
        "stage": "complete_original_conjugacy_inputs_admitted",
        "completed_targets": [], "current_target": None, "candidate_record": None,
        "new_records": {}, "saved_record_count": 0,
        "parameters": copy.deepcopy(PARAMETERS), "result": None,
        "whole_completed_inputs": {role: copy.deepcopy(spec) for role, spec in specs.items()},
        "reference_identity": copy.deepcopy(prior["family"]),
        "selected_member_identity": {
            "run": "43588332723/1", "loss": "1/250", "physical_strip": "1/128",
            "original_RW_manifest_sha256": specs["RW_manifest"]["sha256"],
            "all_old_true_and_false_loss_outcomes_preserved": True,
            "selected_parameter_replaced_by_a_numeric_point": False,
        },
        "copied_prior_scalar_records": copy.deepcopy(records),
        "old_scientific_target_calls": 0, "new_arrays_published": 0,
        "new_artifacts": 0, "new_Releases": 0, "wall_seconds": 0.0, "runtime": {},
    }
    require(sorted(document) == SCI_FIELDS, "complete new scientific schema")
    began = time.perf_counter()

    def save():
        document["wall_seconds"] = time.perf_counter()-began
        require(document["wall_seconds"] <= PARAMETERS["maximum_scientific_wall_seconds"],
                "bounded new scalar combinations")
        raw = canonical(document)
        require(len(raw) <= manifest["operation"]["maximum_scientific_bytes"],
                "one complete small scientific output")
        atomic(args.output, raw)

    save()
    try:
        import flint
        from importlib.metadata import version
        runtime = {"python": platform.python_version(),
                   "packages": {"python-flint": version("python-flint")}}
        require(runtime == manifest["runtime"], "fixed directed scalar runtime")
        document["runtime"] = runtime
        flint.ctx.prec = PARAMETERS["arithmetic_bits"]
        arb = flint.arb

        def old_upper(record):
            require(isinstance(record, dict) and isinstance(record.get("ball"), str),
                    "entire saved original scalar ball")
            value = (arb(record["lower"]).lower().union(arb(record["upper"]).upper())
                     if "lower" in record and "upper" in record else arb(record["ball"]))
            require(value.is_finite() and value.lower() >= 0, "complete original nonnegative ball")
            return value.upper()

        def emit(index, value):
            name, bound = TARGETS[index], "lower" if index < 3 else "upper"
            require(index == document["saved_record_count"] and value.is_finite(),
                    "ordered complete new directed scalar")
            point = value.lower() if bound == "lower" else value.upper()
            if bound == "upper":
                require(point >= 0, "nonnegative upper")
            record = {"ball": point.str(PARAMETERS["decimal_record_digits"]), "bound": bound}
            require(document["candidate_record"] is None, "no pending scalar replaced")
            document["candidate_record"] = {"name": name, "record": record}
            document["current_target"], document["stage"] = name, "whole_new_scalar_candidate_saved"
            save()
            candidate = parse(args.output.read_bytes())["candidate_record"]
            ball = arb(candidate["record"]["ball"])
            require(candidate == {"name": name, "record": record}
                    and ball.is_finite() and ball.contains(point), "candidate whole-ball readback")
            document["new_records"][name] = copy.deepcopy(candidate["record"])
            document["completed_targets"].append(name)
            document["saved_record_count"] += 1
            document["candidate_record"] = document["current_target"] = None
            document["stage"] = "complete_new_scalar_saved"
            save()
            formal = parse(args.output.read_bytes())["new_records"][name]
            final = arb(formal["ball"])
            require(formal == candidate["record"] and final.is_finite() and final.contains(point),
                    "formal saved scalar retains the complete directed value")
            return final.lower() if bound == "lower" else final.upper()

        eh, g0, g1, h1 = (old_upper(records[key]) for key in ("EH", "G0", "G1", "H1"))
        require(g1 >= 1 and h1 >= 1, "whole degree-one derivative norms include constant one")
        sigma = arb(1)/128
        m0 = emit(0, 1-(g0+eh)/sigma)
        m1 = emit(1, 2-(g1 if g1 >= h1 else h1))
        m = emit(2, m0 if m0 >= m1 else m1)
        require(m > 0, "strictly positive entire saved homotopy Jacobian")
        sqrt_lower = m.sqrt().lower()
        require(sqrt_lower > 0, "positive directed square-root denominator")
        composition = emit(3, 384*eh/sqrt_lower)
        joint = emit(4, arb(192).sqrt().upper()*(384*(sigma+g0)).exp().upper())
        tail = emit(5, joint*((-4*sigma*1025).exp().upper()+(-4*sigma*3072).exp().upper()))
        error = emit(6, composition+tail)
        require(error >= 0 and document["completed_targets"] == TARGETS,
                "the entire joint row error is saved")
        document["result"] = {
            "complete_new_record_count": 7, "complete_new_record_order": list(TARGETS),
            "complete_joint_row_operator_error_proved": True,
            "strict_positive_saved_homotopy_lower": True,
            "all_DFT_alias_and_infinite_compound_tails_paid": True,
            "all_dependent_scalars_use_formal_readback_bounds": True,
            "original_RW_trials_unchanged": True,
            "true_target96_orthonormality_only": True,
            "old_angle_nonunitarity_paid": True, "both_physical_density_means_retained": True,
            "full_incoming_row_requires_original_KW_factor": True,
            "TC_trial_row_term_uses_original_fixed_Js_identity": True,
            "signed_PDE_columns_or_finite_inverse_proved": False,
            "full_nu_phase_mean_Schur_proved": False, "topic_completion_proved": False,
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
        document["failure"] = {"type": type(error).__name__, "message": str(error)[:2000],
                               "traceback": traceback.format_exc()[-8000:]}
        document["wall_seconds"] = time.perf_counter()-began
        atomic(args.output, canonical(document))
        print(traceback.format_exc(), flush=True)
        return 1


if __name__ == "__main__":
    sys.exit(main())
