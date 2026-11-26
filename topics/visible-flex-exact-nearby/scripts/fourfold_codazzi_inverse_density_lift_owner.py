"""IL: whole original inverse one-leg lift and three compound derivatives.

The four new scalar targets consume complete old public conclusions and the
original exact terminal coefficients. No old flow, KAM, fit or norm target
runs. This file's admission path imports only the Python standard library.
"""
from __future__ import annotations
import argparse, ast, copy, gzip, hashlib, json, os, platform, sys, time, traceback, types
from pathlib import Path
from fractions import Fraction

REPO = "Rogerhu12/math-research-public"
TOPIC = "topics/visible-flex-exact-nearby"
KIND = "R149_complete_original_inverse_density_lift_v1"
STAGE = "original_inverse_density_lift"
MANIFEST_KIND = "R149_complete_inverse_density_lift_inputs_v1"
SOURCE_PATH = TOPIC+"/scripts/fourfold_codazzi_inverse_density_lift_owner.py"
WORKER_PATH = TOPIC+"/scripts/fourfold_codazzi_inverse_density_lift_public_worker.py"
GENERATOR_PATH = TOPIC+"/scripts/make_inverse_density_lift_manifest.py"
OLD_MANIFEST = TOPIC+"/notes/2026-11-26-reflected-waist-rows-inputs.json"
RENAMED_RW_ROLES = {name: "RW_"+name for name in ("science", "worker", "generator", "proof")}
TARGETS = ["same_selected_inverse_lift_error_upper",
           "complete_original_trial_first_derivative_upper",
           "complete_original_trial_second_derivative_upper",
           "complete_original_trial_third_derivative_upper"]
PARAMETERS = {
    "arithmetic_bits": 320, "decimal_record_digits": 60,
    "maximum_scientific_wall_seconds": 120,
    "physical_frequency_factor": 4, "physical_period": "pi/2",
    "inverse_lift_strip": "1/256", "original_conjugacy_strip": "1/128",
    "original_selected_run": "43588332723/1", "original_selected_loss": "1/250",
    "original_terminal_modes": 64, "original_terminal_sides": 2,
    "original_one_leg_side_index": 1, "original_postcomposition_modes": 48,
    "original_transport_germs": 169, "original_actual_transport_steps": 3095,
    "exact_inverse_map": "p=H composed with Xminus_inverse",
    "exact_finite_trial": "K48 composed with second original terminal phase lift",
    "terminal_constant_mean_retained": True,
    "terminal_rotation_is_separate_from_postcomposition": True,
    "old_numerical_producers_called": 0, "new_complete_scalar_records": 4,
}
SCI_FIELDS = sorted([
    "identity", "complete", "proved", "actual_returncode", "failure", "stage",
    "completed_targets", "current_target", "candidate_record", "new_records",
    "saved_record_count", "parameters", "result", "whole_completed_inputs",
    "reference_identity", "selected_member_identity", "copied_prior_scalar_records",
    "old_scientific_target_calls", "new_arrays_published", "new_artifacts",
    "new_Releases", "wall_seconds", "runtime",
])
EXTRA_HISTORICAL_INPUTS = [
    dict(role="terminal_cover_native", path=TOPIC+"/notes/phase_transport_complete_ci/run-43580721166-1/complete-169-cover.json.gz",
         bytes=143466, sha256="d2e9f2479dc677694c8e84945ac1787f6a5366446d4fd30eac5b3c3008ecc1ae",
         git_blob_sha="57ad0f432edd0b60ac0ab52dee81354deccc7985",
         commit="46f127c7153f5393dcd2a00f42d4c1d3662c294d", encoding="gzip-json", restore_only=True),
    dict(role="wiener_native", path=TOPIC+"/notes/phase_small_consumers_ci/run-43586895661-1/consumers/wiener.json.gz",
         bytes=109293, sha256="33db2c82010e619300b7c6df0b088a047cc6220de09de59ab56fb477ae4f04b4",
         git_blob_sha="53d4d9fd693788a08f51bbe497b213e308f87cf1",
         commit="46f127c7153f5393dcd2a00f42d4c1d3662c294d", encoding="gzip-json", restore_only=True),
]


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
    module = types.ModuleType(name)
    module.__file__ = name
    ast.parse(raw.decode(), filename=name)
    exec(compile(raw, name, "exec"), module.__dict__)
    return module


def native(contents, role):
    raw = gzip.decompress(contents[role])
    require(0 < len(raw) < 4000000, "one whole original natural object")
    return parse(raw)


def admit_complete_inputs(contents, specs):
    require(set(contents) == set(specs), "every whole current and historical input")
    for role, spec in specs.items():
        raw = contents[role]
        require(type(raw) is bytes and len(raw) == spec["bytes"]
                and sha(raw) == spec["sha256"] and blob(raw) == spec["git_blob_sha"],
                "entire original input byte identity: "+role)
        if spec.get("encoding") != "gzip-json":
            require(0 < len(raw) < 100000, "one complete small current UTF8 input")
            raw.decode()
            if spec["path"].endswith(".py"):
                ast.parse(raw.decode(), filename=spec["path"])
    require(specs["science"]["path"] == SOURCE_PATH
            and specs["worker"]["path"] == WORKER_PATH
            and specs["generator"]["path"] == GENERATOR_PATH
            and specs["RW_manifest"]["path"] == OLD_MANIFEST,
            "the declared original inverse-lift source and unchanged RW manifest")
    old = parse(contents["RW_manifest"])
    require(old["kind"] == "R149_complete_reflected_finite_waist_row_inputs_v1"
            and old["complete_record_counts"] == [96], "whole original RW input contract")
    old_specs, old_contents = {}, {}
    for spec in old["files"]+old["historical_inputs"]:
        role = spec["role"]
        here = RENAMED_RW_ROLES.get(role, role)
        require(here in specs and dict(specs[here], role=role) == spec,
                "unchanged original whole RW prerequisite: "+role)
        old_specs[role], old_contents[role] = spec, contents[here]
    extra = {"science", "worker", "generator", "proof", "DC_proof", "DC_math",
             "RW_manifest", "cover_source", "wiener_source", "cover_process",
             "terminal_cover_native", "wiener_native"}
    expected = {RENAMED_RW_ROLES.get(s["role"], s["role"])
                for s in old["files"]+old["historical_inputs"]} | extra
    require(set(specs) == expected, "complete declared original input closure")
    for spec in EXTRA_HISTORICAL_INPUTS:
        require(specs[spec["role"]] == spec, "same original complete terminal native")
    rw = definitions(contents["RW_science"], "_IL_original_RW_admission")
    prior = rw.admit_complete_inputs(old_contents, old_specs)
    cover, wiener, post, r31 = (native(contents, role) for role in
        ("terminal_cover_native", "wiener_native", "K_native", "R31_native"))
    process, nine, manifest, publication = (parse(contents[role]) for role in
        ("cover_process", "nine_process", "nine_manifest", "nine_publication"))
    for role in ("cover_source", "wiener_source", "terminal_cover_native"):
        rw.old_pin(manifest, specs[role])
    rw.publication_record(publication, "consumers/wiener.json.gz", specs["wiener_native"])
    step = next(s for s in nine["steps"] if s["name"] == "wiener")
    require(step["exit_code"] == 0 and step["native_sha256"] == specs["wiener_native"]["sha256"]
            and step["mathematical_source_sha256"] == specs["wiener_source"]["sha256"],
            "entire actual original widening source/output receipt")
    require(process["kind"] == "actual_exact_phase_transport_resume127_public_CI"
            and process["complete"] is True and process["repository"] == REPO
            and process["run_id"] == "43580721166" and process["run_attempt"] == "1"
            and process["child_exit_code"] == process["consumer_exit_code"] == 0
            and process["whole_transport_complete"] is True
            and process["observed_complete_transport_germs"] == 169,
            "actual complete original 169-germ public execution")
    receipt = next(s for s in process["native_files"] if s["file"] == "complete-169-cover.json.gz")
    require(receipt["bytes"] == specs["terminal_cover_native"]["bytes"]
            and receipt["sha256"] == specs["terminal_cover_native"]["sha256"],
            "entire original cover recorded by its completed public process")
    rw.all_gates(cover, 7, "entire original 169-germ cover")
    rw.all_gates(wiener, 8, "entire original full Wiener lift")
    require(cover["kind"] == "actual_chronological_full_frequency_phase_transport_cover"
            and cover["complete"] is cover["whole_negative_domain"] is True
            and cover["source_sha256"] == specs["cover_source"]["sha256"]
            and cover["original_producer_sha256"] == specs["H_transport_source"]["sha256"]
            and cover["root_contract_sha256"] == specs["H_native"]["sha256"]
            and cover["complete_transport_germs"] == len(cover["germs"]) == 169
            and cover["actual_steps"] == 3095,
            "whole original two-leg transport coverage and source")
    require(wiener["kind"] == "actual_saved_phase_transport_Wiener_widening"
            and wiener["complete"] is wiener["whole_negative_domain"] is True
            and wiener["source_sha256"] == specs["wiener_source"]["sha256"]
            and wiener["transport_cover_sha256"] == specs["terminal_cover_native"]["sha256"]
            and wiener["original_producer_sha256"] == specs["H_transport_source"]["sha256"]
            and wiener["root_contract_sha256"] == specs["H_native"]["sha256"]
            and wiener["germ_count"] == len(wiener["consumed_germs"]) == 169
            and wiener["actual_steps"] == 3095
            and wiener["genuine_input_Wiener_strip"] == "1/50"
            and wiener["widened_residual_strip"] == "1/24"
            and wiener["outer_field_strip"] == "1/16"
            and wiener["whole_residual_keeps_all_unprojected_frequencies"] is True
            and wiener["real_scalar_mean_transport_is_isometric"] is True
            and wiener["complete_transport_polynomials_not_recomputed"] is True,
            "same whole old unprojected Fourier, mean, and root qualifications")
    require(post["wiener_lift_sha256"] == specs["wiener_native"]["sha256"]
            and post["physical_true_defect_strip"] == "1/50"
            and cover["exact_processed_interval"] == wiener["exact_processed_interval"]
            and cover["exact_terminal_phase_state"] == wiener["exact_terminal_phase_state"]
            and cover["exact_terminal_phase_mean"] == wiener["exact_terminal_phase_mean"],
            "no single-leg substitution or change of terminal carrier")
    config = cover["configuration"]
    require(config["modes"] == 64 and config["full_output_frequency_bound"] == 128
            and config["exact_eta_offset"] == "0"
            and config["derived_definition_sha256"] == prior["family"]["continuous_centre_definition_sha256"]
            and config["candidate_sha256"] == prior["family"]["original_candidate_sha256"]
            and config["exact_initial_H_sine_coefficients"] == prior["H_sines"]
            and config["exact_initial_H_cosine_coefficients"] == prior["H_cosines"],
            "exact original starting H24 and same repaired centre")
    states = cover["exact_terminal_phase_state"]
    require(len(states) == 2 and all(len(side) == 129 for side in states),
            "both whole original 129-frequency terminal arrays")
    normalized = []
    for side in states:
        pairs = [tuple(Fraction(v) for v in pair) for pair in side]
        require(all(len(pair) == 2 for pair in pairs) and pairs[64][1] == 0
                and all(pairs[64-n] == (pairs[64+n][0], -pairs[64+n][1])
                        for n in range(1, 65)), "exact reality, complete signs and central mean")
        normalized.append(pairs)
    pure = definitions(contents["DC_math"], "_IL_pure_DC_formulas")
    require(pure.INVERSE_LIFT_STRIP == PARAMETERS["inverse_lift_strip"]
            and pure.PHYSICAL_FREQUENCY == 4, "the proved physical inverse-lift formula")
    records = {"EH": prior["chosen"]["physical_true_conjugacy_minus_G_norm"],
               "G1": prior["W"]["exact_G_derivative_norm"],
               "Y": r31["complete_return_first_parameter"],
               "selected_delta": prior["chosen"]["parameter_change"],
               "post_transport": post["multiplied_complete_true_transport_residual"],
               "post_root": post["multiplied_genuine_Wiener_root_sliver"],
               "one_leg_Lipschitz": r31["complete_real_parameter_one_leg_Lipschitz"]}
    require(not any(name in sys.modules for name in ("flint", "numpy", "scipy")),
            "whole original input admission calls no numerical module")
    return prior, records, normalized, pure


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
            and os.environ.get("GITHUB_RUN_ATTEMPT") == "1", "only one original public child")
    raw_manifest = args.manifest.read_bytes()
    require(sha(raw_manifest) == args.manifest_sha, "whole pinned IL manifest")
    manifest = parse(raw_manifest)
    require(manifest["kind"] == MANIFEST_KIND and manifest["scientific_kind"] == KIND
            and manifest["stage"] == STAGE and manifest["parameters"] == PARAMETERS
            and manifest["target_order"] == TARGETS and manifest["complete_record_counts"] == [4]
            and manifest["allowed_scientific_fields"] == SCI_FIELDS,
            "one exact four-target IL object")
    specs = {s["role"]: s for s in manifest["files"]+manifest["historical_inputs"]}
    paths = parse(args.input_map.read_bytes())
    require(set(paths) == set(specs), "entire original input snapshot mapping")
    contents = {role: Path(path).read_bytes() for role, path in paths.items()}
    require(sha(Path(__file__).read_bytes()) == specs["science"]["sha256"], "pinned actual owner")
    prior, records, states, pure = admit_complete_inputs(contents, specs)
    require(not args.output.exists(), "a previous whole prefix is never replaced")
    document = {
        "identity": {"kind": KIND, "scalar_stage": STAGE,
            "source_sha256": specs["science"]["sha256"],
            "DC_math_sha256": specs["DC_math"]["sha256"], "manifest_sha256": args.manifest_sha,
            "run_id": os.environ["GITHUB_RUN_ID"], "run_attempt": "1",
            "event_commit": os.environ["GITHUB_SHA"], "actual_checkout_commit": args.checkout,
            "arithmetic_bits": PARAMETERS["arithmetic_bits"]},
        "complete": False, "proved": False, "actual_returncode": None, "failure": None,
        "stage": "whole_original_inverse_lift_inputs_admitted",
        "completed_targets": [], "current_target": None, "candidate_record": None,
        "new_records": {}, "saved_record_count": 0, "parameters": copy.deepcopy(PARAMETERS),
        "result": None, "whole_completed_inputs": copy.deepcopy(specs),
        "reference_identity": copy.deepcopy(prior["family"]),
        "selected_member_identity": {"run": "43588332723/1", "loss": "1/250",
            "physical_strip": "1/128", "inverse_lift_strip": "1/256",
            "original_RW_manifest_sha256": specs["RW_manifest"]["sha256"],
            "all_old_true_and_false_loss_outcomes_preserved": True,
            "selected_parameter_replaced_by_a_numeric_point": False},
        "copied_prior_scalar_records": copy.deepcopy(records),
        "old_scientific_target_calls": 0, "new_arrays_published": 0,
        "new_artifacts": 0, "new_Releases": 0, "wall_seconds": 0.0, "runtime": {},
    }
    require(sorted(document) == SCI_FIELDS, "whole IL result schema")
    began = time.perf_counter()

    def save():
        document["wall_seconds"] = time.perf_counter()-began
        require(document["wall_seconds"] <= PARAMETERS["maximum_scientific_wall_seconds"],
                "bounded new inverse-lift scalar operations")
        raw = canonical(document)
        require(len(raw) <= manifest["operation"]["maximum_scientific_bytes"], "whole small result")
        atomic(args.output, raw)

    save()
    try:
        import flint
        from importlib.metadata import version
        runtime = {"python": platform.python_version(),
                   "packages": {"python-flint": version("python-flint")}}
        require(runtime == manifest["runtime"], "same fixed scalar arithmetic runtime")
        document["runtime"] = runtime
        flint.ctx.prec = PARAMETERS["arithmetic_bits"]
        arb = flint.arb

        def rational(n, d=1):
            q = Fraction(n)/Fraction(d)
            return arb(q.numerator)/q.denominator

        def old_upper(record):
            require(isinstance(record, dict) and isinstance(record.get("ball"), str),
                    "one complete saved original ball")
            ball = (arb(record["lower"]).lower().union(arb(record["upper"]).upper())
                    if "lower" in record and "upper" in record else arb(record["ball"]))
            require(ball.is_finite() and ball.lower() >= 0, "complete nonnegative old bound")
            return ball.upper()

        def emit(index, value):
            require(index == document["saved_record_count"] and value.is_finite()
                    and value.lower() >= 0, "the next whole new upper scalar")
            name, point = TARGETS[index], value.upper()
            record = {"ball": point.str(PARAMETERS["decimal_record_digits"]), "bound": "upper"}
            require(document["candidate_record"] is None, "no pending candidate is replaced")
            document["candidate_record"] = {"name": name, "record": record}
            document["current_target"], document["stage"] = name, "whole_new_scalar_candidate_saved"
            save()
            candidate = parse(args.output.read_bytes())["candidate_record"]
            ball = arb(candidate["record"]["ball"])
            require(candidate == {"name": name, "record": record}
                    and ball.is_finite() and ball.contains(point), "complete candidate readback")
            document["new_records"][name] = copy.deepcopy(candidate["record"])
            document["completed_targets"].append(name)
            document["saved_record_count"] += 1
            document["candidate_record"] = document["current_target"] = None
            document["stage"] = "complete_new_scalar_saved"
            save()
            formal = parse(args.output.read_bytes())["new_records"][name]
            final = arb(formal["ball"])
            require(formal == candidate["record"] and final.is_finite() and final.contains(point),
                    "whole formal saved bound")
            return final.upper()

        api = types.SimpleNamespace(zero=arb(0), one=arb(1), rational=rational,
            lower=lambda x: x.lower(), magnitude=lambda x: abs(x).upper(),
            sqrt=lambda x: x.sqrt(), exp=lambda x: x.exp())
        require(old_upper(records["one_leg_Lipschitz"]) < rational(1, 16),
                "the full original single-leg complex strip inclusion")
        lift = pure.full_inverse_lift_error(api, **{key: old_upper(records[key]) for key in
            ("EH", "G1", "Y", "selected_delta", "post_transport", "post_root")})
        emit(0, lift["same_selected_inverse_lift_error_upper"])
        # New complete compound targets only: every original exact coefficient
        # is included. Neither an old scalar target nor the old fit is rerun.
        side = states[PARAMETERS["original_one_leg_side_index"]]
        terminal_amplitudes = [(rational(a)**2+rational(b)**2).sqrt().upper()
                               for a, b in side[65:]]
        post_amplitudes = [(rational(s)**2+rational(c)**2).sqrt().upper()
                          for s, c in zip(prior["K_sines"], prior["K_cosines"])]
        A, K = {}, {}
        for derivative in (1, 2, 3):
            A[derivative] = (arb(int(derivative == 1))+2*sum(
                (rational(4*n)**derivative*a for n, a in enumerate(terminal_amplitudes, 1)), arb(0))).upper()
            K[derivative] = (arb(int(derivative == 1))+sum(
                (rational(4*n)**derivative*a for n, a in enumerate(post_amplitudes, 1)), arb(0))).upper()
        emit(1, K[1]*A[1])
        emit(2, K[2]*A[1]**2+K[1]*A[2])
        emit(3, K[3]*A[1]**3+3*K[2]*A[1]*A[2]+K[1]*A[3])
        document["result"] = {
            "complete_new_record_order": list(TARGETS), "complete_new_record_count": 4,
            "whole_original_inverse_lift_error_proved": True,
            "all_three_trial_derivative_bounds_proved": True,
            "original_full_terminal_coefficients_and_means_retained": True,
            "same_selected_parameter_and_true_root_used": True,
            "all_old_unprojected_transport_and_root_fees_retained": True,
            "all_new_scalars_saved_and_read_back": True,
            "new_or_old_ray_ODE_called": False,
            "complete_density_compression_rows_proved": False,
            "whole_Theta_one_loss_paid": False,
            "full_nu_phase_mean_Schur_proved": False, "topic_completion_proved": False,
        }
        require(document["completed_targets"] == TARGETS, "all four complete original-map targets")
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
        traceback.print_exc()
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
