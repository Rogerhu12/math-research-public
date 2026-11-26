"""IR: first complete96 original inverse-density rows and two full residuals.

Metadata admission consumes the complete IL actual, all its original input
objects and receipt, and DC/DB/IR sources. Scientific execution occurs only
in the public repository. Floating linear algebra chooses exact dyadic
trials; the full signed Fourier residual is certified independently.
"""
from __future__ import annotations
import argparse, ast, copy, gzip, hashlib, json, os, platform, sys, time, traceback, types
from pathlib import Path
from fractions import Fraction

REPO = "Rogerhu12/math-research-public"
TOPIC = "topics/visible-flex-exact-nearby"
KIND = "R149_complete_original_inverse_density_rows_v1"
STAGE = "original_inverse_density_rows"
MANIFEST_KIND = "R149_complete_inverse_density_rows_inputs_v1"
SOURCE_PATH = TOPIC+"/scripts/fourfold_codazzi_inverse_density_rows_owner.py"
WORKER_PATH = TOPIC+"/scripts/fourfold_codazzi_inverse_density_rows_public_worker.py"
GENERATOR_PATH = TOPIC+"/scripts/make_inverse_density_rows_manifest.py"
IL_MANIFEST = TOPIC+"/notes/2026-11-27-inverse-density-lift-inputs.json"
RENAMED_IL_ROLES = {name: "IL_"+name for name in ("science", "worker", "generator", "proof")}
ROW_TARGETS = ["row_%03d" % j for j in range(1, 97)]
JOINT_TARGETS = ["complete_joint_energy_residual_upper", "complete_joint_L2_residual_upper",
                 "complete_coordinate_row_L2_error_upper"]
TARGETS = ROW_TARGETS+JOINT_TARGETS
ROW_FIELDS = ["H", "L2", "analytic_model_H", "analytic_model_L2", "real_model_L2"]
PARAMETERS = {
    "arithmetic_bits": 320, "decimal_record_digits": 50, "private_ball_digits": 80,
    "maximum_scientific_wall_seconds": 14400,
    "row_modes": 96, "trial_modes": 192, "grid_points": 4096, "output_cutoff": 1024,
    "physical_frequency_factor": 4, "physical_period": "pi/2",
    "inverse_lift_strip": "1/256", "original_conjugacy_strip": "1/128",
    "original_selected_run": "43588332723/1", "original_selected_loss": "1/250",
    "positive_RHS_coefficient": "2*j*(1-i)",
    "real_root_basis": "sqrt(2)*cos(4*j*x), j=1..96",
    "whole_coordinate_operator": "E96star Dplus_inverse C_inverse",
    "original_source_A_already_applied": False,
    "exact_trial_definition": "full saved little-endian binary64 complex dyadic matrix, shape192x96x2",
    "trial_selection": "numpy solve of sampled same-sign inverse-density matrix; no sampled bound",
    "proposal_container": "python@sha256:4d1caded1f729ae443eb803f26ffde7b61e696aeaef62f099abb6dd6b14257c7",
    "proposal_blas_coretype": "Haswell", "all_proposal_threads": 1,
    "trial_primitive": "positive Fourier primitive; output positive sign then full negative conjugate",
    "full_Hdot_minus_half_and_L2_residuals": True,
    "complete_DFT_aliases_and_infinite_output_tails": True,
    "whole_true_map_model_difference_in_both_norms": True,
    "original_terminal_means_retained": True,
    "old_numerical_producers_called": 0, "IL_targets_recomputed": 0,
    "new_scientific_target_count": 99,
}
SCI_FIELDS = sorted([
    "identity", "complete", "proved", "actual_returncode", "failure", "stage",
    "completed_targets", "current_target", "candidate_record", "new_records",
    "saved_record_count", "parameters", "result", "whole_completed_inputs",
    "reference_identity", "selected_member_identity", "copied_prior_scalar_records",
    "old_scientific_target_calls", "new_arrays_published", "new_artifacts",
    "new_Releases", "wall_seconds", "runtime", "global_bounds",
    "private_grid_receipt", "private_trial_receipt", "private_sample_chain_sha256",
    "private_head_chain_sha256", "private_complete_row_count",
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
    module = types.ModuleType(name)
    module.__file__ = name
    ast.parse(raw.decode(), filename=name)
    exec(compile(raw, name, "exec"), module.__dict__)
    return module


def choose_complete_dyadic_trial_bytes(np, formal_grid):
    """Choose only the exact finite carrier; no certified row target runs.

    A later public consumer may call this with the same whole formal grid
    and immutable runtime solely to rematerialize the original matrix. It
    must then require the complete original byte count and SHA, rather than
    accepting a new trial or repeating a completed residual target.
    """
    require(os.environ.get("GITHUB_ACTIONS") == "true"
            and os.environ.get("GITHUB_REPOSITORY") == REPO,
            "finite trial choice or necessary rematerialization is public only")
    require(len(formal_grid) == PARAMETERS["grid_points"], "the whole exact saved grid")
    dimension, count = PARAMETERS["row_modes"], PARAMETERS["trial_modes"]
    phase = np.asarray([float(value.mid()) for value in formal_grid], dtype=np.float64)
    modes = np.arange(1, count+1, dtype=np.float64)
    exponentials = np.exp(4j*phase[:, None]*modes[None, :])
    sampled = np.fft.fft(exponentials, axis=0)/PARAMETERS["grid_points"]
    matrix = sampled[1:count+1, :]*(modes[:, None]/modes[None, :])
    rhs = np.zeros((count, dimension), dtype=np.complex128)
    for j in range(1, dimension+1):
        rhs[j-1, j-1] = 2*j*(1-1j)
    proposed = np.linalg.solve(matrix, rhs)
    require(proposed.shape == (count, dimension) and np.isfinite(proposed).all(),
            "all96 finite trial proposals exist")
    exact = np.empty((count, dimension, 2), dtype="<f8")
    exact[:, :, 0], exact[:, :, 1] = proposed.real, proposed.imag
    return exact.tobytes(order="C")


def admit_complete_inputs(contents, specs):
    require(set(contents) == set(specs), "entire current and original historical closure")
    for role, spec in specs.items():
        raw = contents[role]
        require(type(raw) is bytes and len(raw) == spec["bytes"]
                and sha(raw) == spec["sha256"] and blob(raw) == spec["git_blob_sha"],
                "whole immutable source/result byte identity: "+role)
        if spec.get("encoding") != "gzip-json":
            require(0 < len(raw) < 100000, "whole small current text input")
            raw.decode()
            if spec["path"].endswith(".py"):
                ast.parse(raw.decode(), filename=spec["path"])
    require(specs["science"]["path"] == SOURCE_PATH
            and specs["worker"]["path"] == WORKER_PATH
            and specs["generator"]["path"] == GENERATOR_PATH
            and specs["IL_manifest"]["path"] == IL_MANIFEST,
            "same exact new row owner and whole IL manifest")
    old = parse(contents["IL_manifest"])
    require(old["kind"] == "R149_complete_inverse_density_lift_inputs_v1"
            and old["stage"] == "original_inverse_density_lift"
            and old["complete_record_counts"] == [4], "entire original IL contract")
    il_specs, il_contents = {}, {}
    for spec in old["files"]+old["historical_inputs"]:
        role = spec["role"]
        here = RENAMED_IL_ROLES.get(role, role)
        require(here in specs and dict(specs[here], role=role) == spec,
                "unchanged whole original IL prerequisite: "+role)
        il_specs[role], il_contents[role] = spec, contents[here]
    additions = {"science", "worker", "generator", "proof", "IR_math", "DB_proof", "DB_math",
                 "IL_manifest", "IL_actual", "IL_execution"}
    expected = {RENAMED_IL_ROLES.get(s["role"], s["role"])
                for s in old["files"]+old["historical_inputs"]} | additions
    require(set(specs) == expected, "all and only the entire IR/IL declared closure")
    il = definitions(contents["IL_science"], "_IR_complete_IL_metadata")
    prior, old_records, states, DC = il.admit_complete_inputs(il_contents, il_specs)
    actual, execution = parse(contents["IL_actual"]), parse(contents["IL_execution"])
    identity = actual["identity"]
    run, attempt = identity["run_id"], identity["run_attempt"]
    base = TOPIC+"/notes/inverse_density_lift_ci/run-"+run+"-"+attempt
    require(run.isdigit() and attempt == "1"
            and specs["IL_actual"]["path"] == base+"/actual-original-inverse-density-lift.json"
            and specs["IL_execution"]["path"] == base+"/execution.json",
            "same first actual original inverse-lift run")
    require(identity["kind"] == il.KIND and identity["scalar_stage"] == il.STAGE
            and identity["source_sha256"] == specs["IL_science"]["sha256"]
            and identity["DC_math_sha256"] == specs["DC_math"]["sha256"]
            and identity["manifest_sha256"] == specs["IL_manifest"]["sha256"]
            and identity["arithmetic_bits"] == 320
            and actual["parameters"] == il.PARAMETERS == old["parameters"]
            and actual["complete"] is actual["proved"] is True
            and actual["actual_returncode"] == 0 and actual["failure"] is None
            and actual["candidate_record"] is actual["current_target"] is None
            and actual["stage"] == "complete_"+il.STAGE+"_scalar_branch"
            and actual["completed_targets"] == il.TARGETS == old["target_order"]
            and actual["saved_record_count"] == 4
            and set(actual["new_records"]) == set(il.TARGETS)
            and actual["whole_completed_inputs"] == il_specs
            and actual["copied_prior_scalar_records"] == old_records
            and actual["reference_identity"] == prior["family"]
            and actual["old_scientific_target_calls"] == 0
            and actual["new_arrays_published"] == actual["new_artifacts"] == actual["new_Releases"] == 0,
            "entire complete same-selected four-scalar actual IL, never a prefix")
    for name in il.TARGETS:
        require(set(actual["new_records"][name]) == {"ball", "bound"}
                and actual["new_records"][name]["bound"] == "upper"
                and isinstance(actual["new_records"][name]["ball"], str),
                "every original complete saved IL scalar")
    result = actual["result"]
    require(result["complete_new_record_count"] == 4
            and result["complete_new_record_order"] == il.TARGETS
            and all(result[key] is True for key in (
                "whole_original_inverse_lift_error_proved", "all_three_trial_derivative_bounds_proved",
                "original_full_terminal_coefficients_and_means_retained", "same_selected_parameter_and_true_root_used",
                "all_old_unprojected_transport_and_root_fees_retained", "all_new_scalars_saved_and_read_back"))
            and result["new_or_old_ray_ODE_called"] is False,
            "all complete IL mathematical scope qualifications")
    require(execution["kind"] == "R149_complete_inverse_density_lift_execution_v1"
            and execution["repository"] == REPO
            and execution["run_id"] == run and execution["run_attempt"] == attempt
            and execution["manifest_sha256"] == specs["IL_manifest"]["sha256"]
            and execution["complete"] is True and execution["failure"] is None
            and execution["actual_child_returncode"] == 0
            and execution["scientific_children"] == 1
            and execution["old_completed_targets_recomputed"] == 0
            and execution["old_numerical_producers_called"] == 0
            and execution["original_scientific_complete"] is True
            and execution["original_scientific_failure"] is None
            and execution["completed_new_scalar_targets"] == 4
            and execution["actual_scientific_checkout"] == identity["actual_checkout_commit"]
            and execution["current_input_receipts"] == old["files"],
            "complete original public execution with unchanged source/input qualifications")
    receipt = next(s for s in execution["scientific_files"] if s["path"] == specs["IL_actual"]["path"])
    require(receipt["bytes"] == specs["IL_actual"]["bytes"]
            and receipt["sha256"] == specs["IL_actual"]["sha256"],
            "whole actual IL result explicitly saved by its completed public worker")
    history = execution["historical_restoration"]
    require(history["original_native_files_restored"] == 6
            and history["scientific_targets_recomputed"] == 0
            and history["complete_receipts"] == [dict(s, whole_original_bytes_restored=True,
                new_numerical_computation=False) for s in old["historical_inputs"]],
            "all six exact original carriers really restored without numerical replay")
    IR = definitions(contents["IR_math"], "_IR_pure_complete_row_formulas")
    DB = definitions(contents["DB_math"], "_IR_pure_regularization_formulas")
    require((IR.DIMENSION, IR.TRIAL_MODES, IR.GRID_POINTS, IR.OUTPUT_CUTOFF,
             IR.PHYSICAL_FREQUENCY, IR.PHYSICAL_STRIP) == (96, 192, 4096, 1024, 4, "1/256"),
            "the exact proved full-row trial/alias/tail parameters")
    require(not any(name in sys.modules for name in ("flint", "numpy", "scipy")),
            "complete metadata admission performs no numerical target")
    return prior, actual, states, DC, DB, IR


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
            and os.environ.get("GITHUB_RUN_ATTEMPT") == "1", "one public first row execution")
    raw_manifest = args.manifest.read_bytes()
    require(sha(raw_manifest) == args.manifest_sha, "whole actual IR manifest")
    manifest = parse(raw_manifest)
    require(manifest["kind"] == MANIFEST_KIND and manifest["scientific_kind"] == KIND
            and manifest["stage"] == STAGE and manifest["parameters"] == PARAMETERS
            and manifest["target_order"] == TARGETS and manifest["complete_record_counts"] == [96, 3]
            and manifest["allowed_scientific_fields"] == SCI_FIELDS,
            "the complete new96-row/two-norm target with all3 joint conclusions")
    specs = {s["role"]: s for s in manifest["files"]+manifest["historical_inputs"]}
    paths = parse(args.input_map.read_bytes())
    require(set(paths) == set(specs), "every current and historical snapshot")
    contents = {role: Path(path).read_bytes() for role, path in paths.items()}
    require(sha(Path(__file__).read_bytes()) == specs["science"]["sha256"], "pinned new actual owner")
    prior, old, states, DC, DB, IR = admit_complete_inputs(contents, specs)
    require(not args.output.exists(), "never replace an old completed or failed whole prefix")
    document = {
        "identity": {"kind": KIND, "scalar_stage": STAGE,
            "source_sha256": specs["science"]["sha256"],
            "IR_math_sha256": specs["IR_math"]["sha256"],
            "DC_math_sha256": specs["DC_math"]["sha256"],
            "DB_math_sha256": specs["DB_math"]["sha256"],
            "IL_actual_sha256": specs["IL_actual"]["sha256"],
            "manifest_sha256": args.manifest_sha, "run_id": os.environ["GITHUB_RUN_ID"],
            "run_attempt": "1", "event_commit": os.environ["GITHUB_SHA"],
            "actual_checkout_commit": args.checkout, "arithmetic_bits": PARAMETERS["arithmetic_bits"]},
        "complete": False, "proved": False, "actual_returncode": None, "failure": None,
        "stage": "whole_original_IL_and_selected_inputs_admitted",
        "completed_targets": [], "current_target": None, "candidate_record": None,
        "new_records": {}, "saved_record_count": 0, "parameters": copy.deepcopy(PARAMETERS),
        "result": None, "whole_completed_inputs": copy.deepcopy(specs),
        "reference_identity": copy.deepcopy(prior["family"]),
        "selected_member_identity": copy.deepcopy(old["selected_member_identity"]),
        "copied_prior_scalar_records": {"IL": copy.deepcopy(old["new_records"]),
            "whole_H_Wiener_derivative": copy.deepcopy(prior["chosen"]["physical_true_conjugacy_derivative_Astrip_upper"])},
        "old_scientific_target_calls": 0, "new_arrays_published": 0,
        "new_artifacts": 0, "new_Releases": 0, "wall_seconds": 0.0, "runtime": {},
        "global_bounds": None, "private_grid_receipt": None, "private_trial_receipt": None,
        "private_sample_chain_sha256": None, "private_head_chain_sha256": None,
        "private_complete_row_count": 0,
    }
    require(sorted(document) == SCI_FIELDS, "entire IR scientific schema")
    began = time.perf_counter()
    private = args.output.parent/"private-complete-inverse-density-row-carriers"
    private.mkdir()

    def save():
        document["wall_seconds"] = time.perf_counter()-began
        require(document["wall_seconds"] <= PARAMETERS["maximum_scientific_wall_seconds"],
                "bounded first complete inverse-density row execution")
        raw = canonical(document)
        require(len(raw) <= manifest["operation"]["maximum_scientific_bytes"],
                "one complete small scientific result, never split or truncated")
        atomic(args.output, raw)

    save()
    try:
        import flint
        import numpy as np
        from importlib.metadata import version
        runtime = {"python": platform.python_version(),
                   "packages": {name: version(name) for name in ("numpy", "python-flint")}}
        require(runtime == manifest["runtime"], "fixed first-row numerical runtime")
        require(os.environ.get("OPENBLAS_CORETYPE") == PARAMETERS["proposal_blas_coretype"]
                and all(os.environ.get(name) == "1" for name in
                    ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS", "NUMEXPR_NUM_THREADS")),
                "same explicitly fixed finite-proposal BLAS scheduling")
        document["runtime"] = runtime
        flint.ctx.prec = PARAMETERS["arithmetic_bits"]
        arb, acb = flint.arb, flint.acb

        def rational(n, d=1):
            q = Fraction(n)/Fraction(d)
            return arb(q.numerator)/q.denominator

        api = types.SimpleNamespace(arb=arb, acb=acb, acb_mat=flint.acb_mat,
            zero=arb(0), one=arb(1), rational=rational,
            lower=lambda v: v.lower(), magnitude=lambda v: abs(v).upper(),
            sqrt=lambda v: v.sqrt(), exp=lambda v: v.exp())

        def old_upper(record):
            require(isinstance(record, dict) and isinstance(record.get("ball"), str),
                    "entire original formal upper ball")
            value = (arb(record["lower"]).lower().union(arb(record["upper"]).upper())
                     if "lower" in record and "upper" in record else arb(record["ball"]))
            require(value.is_finite() and value.lower() >= 0, "whole old nonnegative bound")
            return value.upper()

        def record(value, bound="upper"):
            require(value.is_finite() and bound in ("upper", "lower"), "complete directed scalar")
            point = value.upper() if bound == "upper" else value.lower()
            if bound == "upper":
                require(point >= 0, "one nonnegative upper bound")
            return {"ball": point.str(PARAMETERS["decimal_record_digits"]), "bound": bound}, point

        def read_record(encoded, original):
            value = arb(encoded["ball"])
            require(value.is_finite() and value.contains(original), "whole scalar serialization includes its value")
            return value.upper() if encoded["bound"] == "upper" else value.lower()

        def private_real(name, values):
            body = {"kind": "R149_complete_original_inverse_lift_grid_v1",
                    "complete_count": len(values), "all_balls": [v.str(PARAMETERS["private_ball_digits"]) for v in values]}
            raw = canonical(body)
            path = private/name
            atomic(path, raw)
            read = path.read_bytes()
            require(read == raw, "whole private real carrier bytes")
            saved = parse(read)
            result = [arb(v) for v in saved["all_balls"]]
            require(len(result) == len(values) and all(v.is_finite() and v.contains(old)
                    for v, old in zip(result, values)), "every original grid ball saved and read back")
            return result, {"bytes": len(raw), "sha256": sha(raw), "complete_count": len(result)}

        def private_complex(name, values, kind, mode):
            body = {"kind": kind, "mode": mode, "complete_count": len(values),
                    "all_complex_balls": [[v.real.str(PARAMETERS["private_ball_digits"]),
                        v.imag.str(PARAMETERS["private_ball_digits"])] for v in values]}
            raw = canonical(body)
            path = private/name
            atomic(path, raw)
            read = path.read_bytes()
            require(read == raw, "whole private complex carrier bytes")
            saved = parse(read)
            result = [acb(arb(re), arb(im)) for re, im in saved["all_complex_balls"]]
            require(len(result) == len(values) and all(v.is_finite()
                    and v.real.contains(old.real) and v.imag.contains(old.imag)
                    for v, old in zip(result, values)), "all complete signed carrier balls read back")
            return result, {"bytes": len(raw), "sha256": sha(raw), "complete_count": len(result)}

        ep = old_upper(old["new_records"]["same_selected_inverse_lift_error_upper"])
        p1 = old_upper(old["new_records"]["complete_original_trial_first_derivative_upper"])
        h1 = old_upper(prior["chosen"]["physical_true_conjugacy_derivative_Astrip_upper"])
        globals_raw = IR.complete_global_bounds(api, h1, ep, p1)
        global_records, global_points = {}, {}
        for name, value in globals_raw.items():
            if isinstance(value, bool):
                global_records[name] = value
            else:
                bound = "lower" if name.endswith("lower") else "upper"
                global_records[name], global_points[name] = record(value, bound)
        document["global_bounds"] = global_records
        document["stage"] = "whole_new_global_bounds_saved"
        save()
        formal_globals = parse(args.output.read_bytes())["global_bounds"]
        require(formal_globals == global_records, "complete global-bound record readback")
        global_bounds = {name: (value if isinstance(value, bool)
            else read_record(value, global_points[name])) for name, value in formal_globals.items()}
        # This is an exact declared analytic domain, not a floating upper
        # that may enlarge the admitted strip after decimal serialization.
        require(arb(formal_globals["physical_strip"]["ball"]).contains(rational(1, 256)),
                "the formal strip record contains the original exact strip")
        global_bounds["physical_strip"] = rational(1, 256)
        require(global_bounds["real_model_bound_available"] == bool(global_bounds["homotopy_derivative_lower"] > 0),
                "formal complete homotopy bound retains the actual sign")
        kernels = IR.complete_kernels(api, DC, DB, global_bounds)
        grid = IR.exact_compound_grid(api, states[1], prior["K_sines"], prior["K_cosines"])
        grid, grid_receipt = private_real("whole-original-compound-grid.json", grid)
        document["private_grid_receipt"] = grid_receipt
        document["stage"] = "whole_exact_compound_grid_saved_and_read_back"
        save()
        print("IR: whole directed original inverse-lift grid saved and read back", flush=True)

        # Arbitrary finite proposal only. No numerical entry below is accepted
        # as an enclosure, inverse bound or residual certificate.
        raw = choose_complete_dyadic_trial_bytes(np, grid)
        path = private/"whole-trial-coefficients.f64"
        atomic(path, raw)
        read = path.read_bytes()
        require(read == raw and len(raw) == IR.TRIAL_MODES*IR.DIMENSION*2*8,
                "the entire exact dyadic trial matrix saved byte for byte")
        formal_trial = np.frombuffer(read, dtype="<f8").reshape(IR.TRIAL_MODES, IR.DIMENSION, 2)
        require(formal_trial.tobytes(order="C") == raw
                and np.isfinite(formal_trial).all(), "all trial coefficients read back unchanged")
        columns = [[acb(rational(Fraction(float(formal_trial[n, j, 0]))),
                        rational(Fraction(float(formal_trial[n, j, 1]))))
                    for n in range(IR.TRIAL_MODES)] for j in range(IR.DIMENSION)]
        document["private_trial_receipt"] = {"bytes": len(raw), "sha256": sha(raw),
            "shape": [IR.TRIAL_MODES, IR.DIMENSION, 2], "dtype": "<f8", "order": "C",
            "exact_binary64_dyadic_definition": True,
            "no_proposal_condition_number_or_sampled_residual_used_as_bound": True}
        document["stage"] = "all96_exact_finite_trial_columns_saved_and_read_back"
        save()
        del formal_trial
        factory = IR.CompletePrimitiveSampleFactory(api, grid, columns)
        tables = IR.fft_tables(api)

        def emit(index, value, row=False):
            require(index == document["saved_record_count"] and document["candidate_record"] is None,
                    "only the next complete new target may be saved")
            name = TARGETS[index]
            if row:
                require(set(value) == set(ROW_FIELDS), "all five complete row residual/model fields")
                encoded, points = {}, {}
                for key in ROW_FIELDS:
                    if value[key] is None:
                        require(key == "real_model_L2" and not global_bounds["real_model_bound_available"],
                                "only the explicitly unavailable homotopy alternative may be absent")
                        encoded[key] = None
                    else:
                        encoded[key], points[key] = record(value[key])
            else:
                encoded, points = record(value)
            candidate = {"name": name, "record": encoded}
            document["candidate_record"] = candidate
            document["current_target"], document["stage"] = name, "whole_new_target_candidate_saved"
            save()
            read = parse(args.output.read_bytes())["candidate_record"]
            require(read == candidate, "whole complete candidate readback")
            if row:
                for key, point in points.items():
                    read_record(read["record"][key], point)
            else:
                read_record(read["record"], points)
            document["new_records"][name] = copy.deepcopy(read["record"])
            document["completed_targets"].append(name)
            document["saved_record_count"] += 1
            document["candidate_record"] = document["current_target"] = None
            document["stage"] = "complete_new_target_saved"
            save()
            formal = parse(args.output.read_bytes())["new_records"][name]
            require(formal == read["record"], "whole formal target readback")
            if row:
                return {key: (None if formal[key] is None else read_record(formal[key], points[key]))
                        for key in ROW_FIELDS}
            return read_record(formal, points)

        formal_columns = []
        for j in range(1, IR.DIMENSION+1):
            actual_j, samples = factory.next_complete_samples()
            require(actual_j == j, "complete original row order")
            samples, sample_receipt = private_complex("row-%03d-positive-primitive-samples.json" % j,
                samples, "R149_complete_positive_primitive_sample_column_v1", j)
            document["private_sample_chain_sha256"] = sha(canonical({
                "previous": document["private_sample_chain_sha256"], "mode": j, "receipt": sample_receipt}))
            transform = IR.complete_directed_dft(api, samples, tables)
            bounds = IR.complete_column_bounds(api, columns[j-1], global_bounds, kernels)
            head = IR.entire_signed_head(api, j, transform, bounds, kernels)
            head, head_receipt = private_complex("row-%03d-whole-signed-residual-head.json" % j,
                head, "R149_complete_signed_density_residual_head_positive_conjugate_pair_v1", j)
            document["private_head_chain_sha256"] = sha(canonical({
                "previous": document["private_head_chain_sha256"], "mode": j, "receipt": head_receipt}))
            document["private_complete_row_count"] = j
            value = IR.complete_residual_norms(api, DC, DB, head, bounds)
            formal_columns.append(emit(j-1, value, row=True))
            print("IR: saved complete full-frequency row %d/96 in both norms" % j, flush=True)
        joint = IR.complete_joint_residual(api, formal_columns)
        energy = emit(96, joint["H"])
        emit(97, joint["L2"])
        emit(98, energy/2)
        require(document["completed_targets"] == TARGETS
                and document["private_complete_row_count"] == 96,
                "all96 original complete rows and all3 joint conclusions")
        document["result"] = {
            "complete_new_record_count": 99, "complete_new_record_order": list(TARGETS),
            "complete_row_count": 96, "complete_joint_record_count": 3,
            "same_full_signed_residual_used_in_both_norms": True,
            "all_frequencies_aliases_and_true_map_errors_paid": True,
            "positive_input_positive_output_then_negative_conjugate": True,
            "exact_output_mean_is_zero": True,
            "whole_private_grids_trials_and_heads_saved_and_read_back": True,
            "complete_original_coordinate_rows_on_L2_proved": True,
            "all_joint_bounds_use_all96_formal_saved_rows": True,
            "additional_sqrt96_after_joint_error": False,
            "original_A_already_applied": False,
            "whole_VQ_or_Theta_rows_claimed": False,
            "independent_physical_density_mean_rows_paid": False,
            "full_nu_phase_mean_Schur_proved": False,
            "IL_or_other_old_scientific_targets_recomputed": False,
            "topic_completion_proved": False,
        }
        document["complete"] = document["proved"] = True
        document["actual_returncode"] = 0
        document["stage"] = "complete_"+STAGE+"_branch"
        save()
        return 0
    except BaseException as error:
        document["complete"] = document["proved"] = False
        document["actual_returncode"] = 1
        document["stage"] = "failed_with_complete_new_row_prefix"
        document["failure"] = {"type": type(error).__name__, "message": str(error)[:2000],
                               "traceback": traceback.format_exc()[-8000:]}
        document["wall_seconds"] = time.perf_counter()-began
        atomic(args.output, canonical(document))
        traceback.print_exc()
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
