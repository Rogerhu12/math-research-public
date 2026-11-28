"""H96: seven first complete height rows on the unchanged original96 TC trials.

Whole P96 and RHI metadata admission precedes numerical imports.  Necessary
TC/NP arrays and the original all18 RHI endpoint/chain must match their old
whole SHA256 receipts.  A passive cache keeps the original A9/x3 degree6
polynomials privately; old phase, residual, norm and strip targets never run.
"""
from __future__ import annotations
import argparse, ast, gzip, hashlib, importlib.util, json, os, platform
import resource, shutil, sys, tempfile, time, traceback
from fractions import Fraction as F
from pathlib import Path

REPO = "Rogerhu12/math-research-public"
TOPIC = "topics/visible-flex-exact-nearby"
SOURCE = TOPIC+"/scripts/fourfold_codazzi_finite_trial_height_owner.py"
MATH = TOPIC+"/scripts/fourfold_codazzi_finite_trial_height_math.py"
CARRIERS = TOPIC+"/scripts/fourfold_codazzi_finite_trial_height_carriers.py"
WORKER = TOPIC+"/scripts/fourfold_codazzi_finite_trial_height_public_worker.py"
GENERATOR = TOPIC+"/scripts/make_finite_trial_height_manifest.py"
PROOF = TOPIC+"/results/R149-supplement-complete-height-row-on-original-finite-trials.md"
P96_MANIFEST = TOPIC+"/notes/2026-11-27-finite-trial-phase-complete-inputs.json"
P96_SOURCE = TOPIC+"/scripts/fourfold_codazzi_finite_trial_phase_owner.py"
P96_BASE = TOPIC+"/notes/finite_trial_phase_ci/run-45926971089-1"
RHI_MANIFEST = TOPIC+"/notes/2026-11-27-relative-nu-carriers-inputs.json"
RHI_BASE = TOPIC+"/notes/relative_nu_carriers_ci/run-45933988440-1"
RHI_SOURCE = TOPIC+"/scripts/fourfold_codazzi_relative_nu_carrier_owner.py"
RHI_MATH = TOPIC+"/scripts/fourfold_codazzi_relative_nu_carrier_math.py"
RHI_RESTORE = TOPIC+"/scripts/fourfold_codazzi_relative_nu_carrier_restore.py"
RHI_WORKER = TOPIC+"/scripts/fourfold_codazzi_relative_nu_carrier_public_worker.py"
WMR_ADMISSION = TOPIC+"/scripts/fourfold_codazzi_world_mean_height_owner.py"
TC_RESTORE = TOPIC+"/scripts/fourfold_codazzi_finite_trial_phase_restore.py"
NP_RESTORE = TOPIC+"/scripts/fourfold_codazzi_strict_nu_trial_carrier_restore.py"
KIND = "R149_complete_original_finite_trial_height_rows_v1"
MANIFEST_KIND = "R149_complete_original_finite_trial_height_rows_inputs_v1"
STAGE = "complete_original_finite_trial_height_rows"
RUNTIME = {"python":"3.12.14", "packages":{"numpy":"2.3.5", "python-flint":"0.9.0"}}
TARGETS = [
    "complete_same_selected_TC_canonical_height_row96",
    "complete_same_selected_TC_waist_Jacobian_L2_upper96",
    "complete_same_selected_TC_reference_height_row96",
    "complete_same_selected_TC_actual_cap_height_row96",
    "complete_same_selected_TC_actual_cap_height_joint_radius",
    "complete_same_selected_TC_height_reduced_phase_row96",
    "complete_same_selected_TC_height_reduced_phase_joint_radius"]
COUNTS = [96, 96, 96, 96, 1, 96, 1]
SIGNED_INDICES = (0, 2, 3, 5)
PARAMETERS = {
    "arithmetic_bits":320, "decimal_record_digits":60,
    "maximum_scientific_wall_seconds":18000,
    "complete_TC_trial_arrays":4, "complete_TC_trial_shape":[7671,193,96],
    "complete_TC_trial_bytes":4548105216, "complete_TC_certificate_cells":7724,
    "complete_original_rows":7721, "complete_NP_trial_arrays":4,
    "complete_NP_trial_shape":[740,193], "complete_RHI_cells":2847,
    "complete_RHI_endpoint_shape":[2048,18], "complete_RHI_endpoint_bytes":294912,
    "private_polynomial_cache_shape":[2847,7,2048,12],
    "private_polynomial_cache_bytes":3918200832,
    "original_polynomial_variable":"u=(right-r)/(right-left)",
    "private_polynomial_index_order":"original rhi.full_plan forward index",
    "maximum_private_disk_bytes":12884901888,
    "maximum_resident_bytes":17179869184,
    "complete_new_contraction_grid":8192,
    "maximum_complete_angular_degree":3584,
    "exact_height_body_interval":["0","9/50"],
    "physical_period":"pi/2", "physical_frequency_factor":4,
    "normalized_angular_measure":True, "original_world_frame_determinant":-1,
    "complete_same_selected_RHI_A_C0_error":"13/100000000",
    "complete_same_selected_RHI_x_C0_error":"33/500000000",
    "unrestricted_C0_primitive_factor":"2/5",
    "reference_vertical_covector_error":"108627/1000000000",
    "reference_world_position_error":"232743/1000000000",
    "actual_cap_frame_distance":"447/200000",
    "actual_cap_position_distance":"67/15625",
    "complete_height_phase_pivot_interval":["-1543/1000","-1901/1250"],
    "complete_selected_state_difference_upper":"1/500000000",
    "J_variation_operator_factor":"525/128", "J_background_difference_factor":"7875/1024",
    "P96_complete_signed_phase_and_negative_L1_vectors_reused":True,
    "both_moving_means_and_physical_coordinate_term_retained":True,
    "actual_Yb_Kb_and_remaining_geometric_impulse_ports_independent":True,
    "true_PDE_corrected_columns":False,
    "old_scientific_targets_recomputed":False,
    "old169_phase_carriers_restored":False,
    "new_trial_selected":False, "new_complete_targets":7,
    "automatic_scientific_retry":False}
SCI_FIELDS = sorted([
    "identity","parameters","runtime","complete","proved","actual_returncode",
    "failure","stage","completed_targets","current_target","candidate_record",
    "new_records","saved_record_count","whole_completed_inputs","reference_identity",
    "selected_member_identity","whole_prior_record_sources",
    "necessary_original_trial_receipts","necessary_original_NP_receipts",
    "necessary_relative_carrier_receipt","height_integral_prefix","result",
    "old_scientific_target_calls","new_arrays_published","new_artifacts",
    "new_Releases","wall_seconds"])


def require(ok, message):
    if not ok:
        raise ValueError(message)


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def canonical(value):
    return (json.dumps(value, sort_keys=True, separators=(",", ":"),
                       ensure_ascii=False, allow_nan=False)+"\n").encode()


def parse(raw):
    return json.loads(gzip.decompress(raw) if raw[:2] == b"\x1f\x8b" else raw,
        parse_constant=lambda x: (_ for _ in ()).throw(ValueError(x)))


def load(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def atomic(path, raw):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(path.name+".candidate")
    with temporary.open("wb") as stream:
        stream.write(raw); stream.flush(); os.fsync(stream.fileno())
    os.replace(temporary, path)


def gather(root):
    """Merge whole frozen P96/RHI closures, with no unused phase169 expansion."""
    root = Path(root)
    p96m, rhim = (parse((root/path).read_bytes()) for path in (P96_MANIFEST, RHI_MANIFEST))
    current, roles = {}, {}
    def add(role, path, expected=None, alias=True):
        require(path.startswith(TOPIC+"/") and ".." not in Path(path).parts,
                "whole topic input path")
        raw = (root/path).read_bytes(); raw.decode()
        require(0 < len(raw) < 100000, "small whole UTF8 input: "+role)
        if path.endswith(".py"):
            ast.parse(raw.decode(), filename=path)
        spec = {"role":role, "path":path, "bytes":len(raw), "sha256":sha(raw),
            "git_blob_sha":hashlib.sha1(b"blob "+str(len(raw)).encode()+b"\0"+raw).hexdigest()}
        if expected is not None:
            require(all(spec[key] == expected[key] for key in
                        ("path","bytes","sha256","git_blob_sha")),
                    "same whole immutable predecessor input: "+role)
        if path in current:
            require(all(spec[key] == current[path][key] for key in
                        ("path","bytes","sha256","git_blob_sha")), "identical merged whole input")
        current.setdefault(path, spec)
        if alias:
            roles[role] = path
    # Canonical worker keys must occur in the actual file inventory, not only aliases.
    review = next(item for item in p96m["files"] if item["role"] == "reviewed_rules")
    add("reviewed_rules", review["path"], review)
    for prefix, path, old in (("P96", P96_MANIFEST, p96m), ("RHI", RHI_MANIFEST, rhim)):
        add(prefix+"_manifest", path)
        for item in old["files"]:
            add(prefix+"_"+item["role"], item["path"], item, False)
    for key, path in rhim["roles"].items():
        roles.setdefault(key, path)
    extra = [
        ("P96_source",P96_SOURCE),
        ("P96_actual",P96_BASE+"/actual-finite-trial-phase.json"),
        ("P96_execution",P96_BASE+"/execution.json"),
        ("RHI_source",RHI_SOURCE), ("RHI_math",RHI_MATH), ("RHI_worker",RHI_WORKER),
        ("RHI_actual",RHI_BASE+"/actual-relative-nu-carriers.json"),
        ("RHI_execution",RHI_BASE+"/execution.json"),
        ("RHI_restore",RHI_RESTORE), ("TC_restore",TC_RESTORE), ("NP_restore",NP_RESTORE),
        ("original_RHI_admission",WMR_ADMISSION),
        ("science",SOURCE), ("height_math",MATH), ("height_carriers",CARRIERS),
        ("worker",WORKER), ("generator",GENERATOR), ("proof",PROOF)]
    proofs = {
        "proof_RH":"R147-supplement-relative-height-carriers-and-short-full-frequency-errors.md",
        "proof_RHI":"R147-supplement-certified-relative-parameter-frame-and-position-carriers.md",
        "proof_PH":"R147-supplement-exact-nonlocal-phase-and-height-parameter-ports.md",
        "proof_WRC":"R147-supplement-complete-reference-world-height-and-original-negative-receiver.md",
        "proof_CW":"R147-supplement-actual-cap-world-anchors-and-supported-nu-height.md",
        "proof_HP":"R147-supplement-actual-height-pivot-and-complete-phase-mean-transfer.md"}
    extra += [(key, TOPIC+"/results/"+name) for key, name in proofs.items()]
    for role, path in extra:
        add(role, path)
    history = rhim["historical_inputs"]
    require(history == p96m["historical_inputs"] and len(history) == 51,
            "one identical complete original base/rows/family closure")
    specs = list(current.values())+history
    require(len({item["path"] for item in specs}) == len(specs)
            and len({item["role"] for item in specs}) == len(specs),
            "all complete inputs occur exactly once")
    require(all(next(x for x in current.values() if x["role"] == key)["path"] == roles[key]
                for key in ("science", "worker", "reviewed_rules")),
            "canonical executable and README contract inventory roles")
    return {"files":sorted(current.values(), key=lambda x:x["role"]),
            "historical_inputs":history, "roles":roles}


def admit(manifest, raws, paths):
    roles = manifest["roles"]
    p96m = parse(raws[roles["P96_manifest"]])
    p96 = load(paths[roles["P96_source"]], "_H96_whole_original_P96_metadata")
    tc = p96.admit(p96m, raws, paths)
    rhi_admit = load(paths[roles["original_RHI_admission"]], "_H96_whole_original_RHI_metadata")
    relative = rhi_admit.admit(manifest, raws, paths)
    actual, execution = (parse(raws[roles[key]]) for key in ("P96_actual", "P96_execution"))
    source = next(item for item in p96m["files"] if item["role"] == "science")
    require(actual["complete"] is actual["proved"] is execution["complete"] is True
            and actual["actual_returncode"] == execution["actual_child_returncode"] == 0
            and actual["failure"] is execution["failure"] is None
            and actual["identity"]["kind"] == p96.KIND == p96m["scientific_kind"]
            and actual["identity"]["source_sha256"] == source["sha256"]
            and sha(raws[roles["P96_source"]]) == source["sha256"]
            and actual["identity"]["manifest_sha256"] == sha(raws[roles["P96_manifest"]])
            and execution["manifest_sha256"] == sha(raws[roles["P96_manifest"]])
            and actual["parameters"] == p96.PARAMETERS == p96m["parameters"]
            and actual["runtime"] == {**RUNTIME, "OPENBLAS_CORETYPE":"Haswell"}
            and actual["completed_targets"] == p96.TARGETS == p96m["target_order"]
            and actual["saved_record_count"] == 6 and set(actual["new_records"]) == set(p96.TARGETS)
            and sorted(actual) == p96m["allowed_scientific_fields"]
            and actual["current_target"] is actual["candidate_record"] is None
            and actual["identity"]["run_id"] == execution["run_id"] == "45926971089"
            and actual["identity"]["run_attempt"] == execution["run_attempt"] == "1"
            and actual["reference_identity"] == tc["prior"]["R147"]["reference_identity"]
                == relative["NP"]["reference_identity"]
            and actual["selected_member_identity"] == tc["prior"]["R147"]["selected_member_identity"]
                == relative["NP"]["selected_member_identity"]
            and execution["scientific_files"] == [{"path":roles["P96_actual"],
                "bytes":len(raws[roles["P96_actual"]]), "sha256":sha(raws[roles["P96_actual"]])}],
            "the entire actually completed six P96 targets on the identical original family/trial")
    for index, name in enumerate(p96.TARGETS):
        saved = actual["new_records"][name]
        if index == 5:
            require(set(saved) == {"ball", "bound"} and saved["bound"] == "upper"
                    and isinstance(saved["ball"], str), "whole saved phase joint radius")
        else:
            keys = {"complete_count", "bound", "balls"}|({"exact_dyadic_centres"} if index == 4 else set())
            require(set(saved) == keys and saved["complete_count"] == 96
                    and saved["bound"] == ("signed_enclosure" if index in (0,4) else "upper")
                    and len(saved["balls"]) == 96 and all(isinstance(x,str) for x in saved["balls"]),
                    "every original complete96-vector: "+name)
            if index == 4:
                require(len(saved["exact_dyadic_centres"]) == 96
                        and all(isinstance(x,str) for x in saved["exact_dyadic_centres"]),
                        "all original selected phase centres")
    for key in ("same_four_whole_original_TC_arrays", "all169_original_phase_germs",
                "all3095_original_two_leg_polynomial_hashes", "complete_true_root_sliver_included",
                "both_means_and_original_phase_constant_retained",
                "same_original_orthonormal_trial_input_coordinates",
                "every_dependent_target_uses_whole_saved_readback"):
        require(actual["result"][key] is True, "whole prior P96 qualification: "+key)
    for key in ("true_PDE_corrected_columns_proved", "original_TC_negative_result_complete",
                "full_regular_or_Theta_inverse_proved", "full_phase_Schur_or_topic_completion_proved",
                "new_trial_selected", "old_scientific_targets_recomputed"):
        require(actual["result"][key] is False, "independent unpaid original responsibility: "+key)
    require(actual["necessary_original_trial_receipts"]["complete_original_arrays"]
            == tc["TC_state"]["proposal"]["complete_endpoint_arrays"],
            "all four original whole TC arrays, with unchanged exact dyadic coordinates")
    require(not any(name in sys.modules for name in ("numpy", "flint", "scipy")),
            "complete input admission before any numerical call")
    return {**relative, "P96":actual, "P96_manifest":p96m,
            "TC_manifest":tc["TC_manifest"], "TC_state":tc["TC_state"],
            "TC_matrix":tc["TC_matrix"]}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ("manifest", "input-map", "output"):
        parser.add_argument("--"+name, type=Path, required=True)
    parser.add_argument("--manifest-sha", required=True)
    parser.add_argument("--checkout", required=True)
    args = parser.parse_args()
    require(os.environ.get("GITHUB_ACTIONS") == "true"
            and os.environ.get("GITHUB_REPOSITORY") == REPO
            and os.environ.get("GITHUB_RUN_ATTEMPT") == "1",
            "one authorized first public H96 target sequence")
    raw_manifest = args.manifest.read_bytes(); manifest = parse(raw_manifest)
    require(sha(raw_manifest) == args.manifest_sha and manifest["kind"] == MANIFEST_KIND
            and manifest["scientific_kind"] == KIND and manifest["stage"] == STAGE
            and manifest["parameters"] == PARAMETERS and manifest["runtime"] == RUNTIME
            and manifest["target_order"] == TARGETS and manifest["allowed_scientific_fields"] == SCI_FIELDS,
            "the whole new immutable H96 mathematical contract")
    specs = manifest["files"]+manifest["historical_inputs"]
    input_map = parse(args.input_map.read_bytes())
    require(set(input_map) == {item["role"] for item in specs}, "every complete declared input")
    raws, paths = {}, {}
    for item in specs:
        path = Path(input_map[item["role"]]); raw = path.read_bytes()
        require(len(raw) == item["bytes"] and sha(raw) == item["sha256"], "whole input: "+item["role"])
        raws[item["path"]], paths[item["path"]] = raw, path
    require(sha(Path(__file__).read_bytes()) == next(item["sha256"] for item in specs
                                                   if item["role"] == "science"), "entire running owner")
    sys.dont_write_bytecode = True
    admitted = admit(manifest, raws, paths)
    npm, roles = admitted["NP_manifest"], manifest["roles"]
    nr = npm["roles"]
    helper = load(paths[nr["inputs_math"]], "_H96_all_original_rows")
    rows, part_receipts = helper.admit_all_rows(
        [paths[item["path"]] for item in npm["historical_inputs"]
         if item["role"].startswith("original_rows_")],
        {"old_body_manifest":parse(raws[nr["old_body_manifest"]]),
         "NW":{"difference":admitted["prior"]["D"]}})
    require(not args.output.exists(), "preserve every genuine execution and accepted prefix")
    state = {
        "identity":{"kind":KIND,"scalar_stage":STAGE,"manifest_sha256":args.manifest_sha,
            "source_sha256":sha(Path(__file__).read_bytes()),"run_id":os.environ["GITHUB_RUN_ID"],
            "run_attempt":"1","event_commit":os.environ["GITHUB_SHA"],
            "actual_checkout_commit":args.checkout,"arithmetic_bits":320},
        "parameters":PARAMETERS,"runtime":{},"complete":False,"proved":False,
        "actual_returncode":None,"failure":None,"stage":"whole_H96_inputs_admitted",
        "completed_targets":[],"current_target":None,"candidate_record":None,
        "new_records":{},"saved_record_count":0,
        "whole_completed_inputs":{"complete_inventory_sha256":sha(canonical(specs)),
            "current_files":len(manifest["files"]),"historical_files":len(manifest["historical_inputs"]),
            "complete_original_rows":len(rows),"all40_original_parts_admitted":True,
            "P96_complete_targets":6,"RHI_complete_targets":4,
            "same_original_implicit_selected_member":True,
            "unused_phase169_carrier_objects_restored":0},
        "reference_identity":admitted["NP"]["reference_identity"],
        "selected_member_identity":admitted["NP"]["selected_member_identity"],
        "whole_prior_record_sources":{
            "P96_actual":{"path":roles["P96_actual"],"sha256":sha(raws[roles["P96_actual"]]),
                "complete_targets":admitted["P96"]["completed_targets"]},
            "RHI_actual":{"path":roles["RHI_actual"],"sha256":sha(raws[roles["RHI_actual"]]),
                "complete_targets":admitted["RHI"]["completed_targets"]}},
        "necessary_original_trial_receipts":None,"necessary_original_NP_receipts":None,
        "necessary_relative_carrier_receipt":None,"height_integral_prefix":None,"result":None,
        "old_scientific_target_calls":0,"new_arrays_published":0,"new_artifacts":0,
        "new_Releases":0,"wall_seconds":0.}
    require(sorted(state) == SCI_FIELDS, "whole H96 result envelope")
    started = time.perf_counter()
    def save(enforce=True):
        state["wall_seconds"] = time.perf_counter()-started
        if enforce:
            require(state["wall_seconds"] <= PARAMETERS["maximum_scientific_wall_seconds"],
                    "new H96 wall budget; entire accepted prefix remains saved")
            require(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss*1024
                    <= PARAMETERS["maximum_resident_bytes"], "the complete16GiB resident budget")
        raw = canonical(state)
        require(len(raw) <= manifest["operation"]["maximum_scientific_bytes"],
                "whole small public scientific receipt")
        atomic(args.output, raw)
    def progress(stage, details):
        state["stage"] = stage; save()
        print(json.dumps({"stage":stage, **details}), flush=True)
    def save_prefix(prefix):
        require(isinstance(prefix,dict), "one whole genuine new integral prefix")
        state["height_integral_prefix"] = prefix; save()
        require(parse(args.output.read_bytes())["height_integral_prefix"] == prefix,
                "entire96-column prefix saved and read back")
    save()
    try:
        import numpy as np
        import flint
        from importlib.metadata import version
        runtime = {"python":platform.python_version(),
                   "packages":{name:version(name) for name in RUNTIME["packages"]}}
        require(runtime == RUNTIME and sys.byteorder == "little" and platform.machine() == "x86_64"
                and os.environ.get("OPENBLAS_CORETYPE") == "Haswell"
                and all(os.environ.get(key) == "1" for key in (
                    "OPENBLAS_NUM_THREADS","OMP_NUM_THREADS","MKL_NUM_THREADS",
                    "BLIS_NUM_THREADS","VECLIB_MAXIMUM_THREADS","NUMEXPR_NUM_THREADS")),
                "the identical original floating CPU branch and directed arithmetic runtime")
        state["runtime"] = {**runtime,"OPENBLAS_CORETYPE":"Haswell"}
        flint.ctx.prec = 320; arb = flint.arb
        def read_ball(record):
            value = arb(record["ball"])
            if "lower" in record and "upper" in record:
                value = value.union(arb(record["lower"])).union(arb(record["upper"]))
            require(value.is_finite(), "entire finite saved original ball")
            return value
        def record(value, direction):
            value = value if direction == "signed_enclosure" else value.upper()
            require(value.is_finite() and (direction == "signed_enclosure" or value >= 0),
                    "complete finite directed scalar")
            text = value.str(PARAMETERS["decimal_record_digits"])
            require(arb(text).contains(value), "entire directed scalar survives serialization")
            return text
        def publish(name, values, direction, centres=None):
            index = state["saved_record_count"]
            require(index < len(TARGETS) and name == TARGETS[index]
                    and isinstance(values,list) and len(values) == COUNTS[index]
                    and direction == ("signed_enclosure" if index in SIGNED_INDICES else "upper"),
                    "one next complete declared96-vector or scalar target")
            saved = {"complete_count":len(values),"bound":direction,
                     "balls":[record(value,direction) for value in values]}
            if index in (3,5):
                require(isinstance(centres,list) and len(centres) == 96
                        and all(isinstance(x,str) for x in centres), "all exact96 joint-radius centres")
                exact = [F(text) for text in centres]
                require(all(q.denominator & (q.denominator-1) == 0 for q in exact),
                        "each centre is an exact dyadic choice")
                saved["exact_dyadic_centres"] = centres
            else:
                require(centres is None, "only the two declared joint vectors carry centre choices")
            state["current_target"] = name
            state["candidate_record"] = {"name":name,"record":saved}; save()
            require(parse(args.output.read_bytes())["candidate_record"] == state["candidate_record"],
                    "entire candidate persisted before its success marker")
            state["new_records"][name] = saved; state["completed_targets"].append(name)
            state["saved_record_count"] += 1
            state["current_target"] = state["candidate_record"] = None; save()
            restored = parse(args.output.read_bytes())["new_records"][name]
            require(restored == saved, "whole final record readback")
            return [arb(text) if direction == "signed_enclosure" else arb(text).upper()
                    for text in restored["balls"]]
        core = load(paths[nr["trial_math"]], "_H96_original1024_directed_core")
        nu = load(paths[nr["nu_math"]], "_H96_original_strict_trial_math")
        rhi = load(paths[roles["RHI_math"]], "_H96_original_RHI_coefficients")
        tc_restore = load(paths[roles["TC_restore"]], "_H96_original_TC_restore")
        np_restore = load(paths[roles["NP_restore"]], "_H96_original_NP_restore")
        carriers = load(paths[roles["height_carriers"]], "_H96_passive_relative_polynomial_cache")
        math = load(paths[roles["height_math"]], "_H96_first_complete_height_math")
        require(math.TARGETS == TARGETS and math.COUNTS == COUNTS
                and math.SIGNED_INDICES == SIGNED_INDICES and math.GRID == 8192
                and math.MAXIMUM_DEGREE == 3584 and core.GRID == 1024,
                "all seven declared targets and an unchanged original1024 context")
        backend, unused = helper.directed_backend(np, flint, raws[nr["box_math"]], raws[nr["fft_math"]])
        c = core.DirectedContext(np, arb, backend["Box"], backend["CBox"], backend["zeros"],
                                backend["arb_box"], backend["reduce_box"], backend["DirectedFFT"]())
        reader, unused = helper.candidate_reader(np, raws[nr["candidate_reader"]])
        iterator, unused = helper.repair_iterator(raws[nr["repair_source"]])
        base = reader(paths[nr["base_index"]])
        repair = parse(raws[nr["old_centre_repair"]])
        require(helper.ALPHA == nu.ALPHA, "same exact original selected-background offset convention")
        with tempfile.TemporaryDirectory(prefix="private-H96-original-carriers-") as private:
            needed_disk = (PARAMETERS["complete_TC_trial_bytes"]
                           +PARAMETERS["private_polynomial_cache_bytes"]+268435456)
            require(shutil.disk_usage(private).free > needed_disk,
                    "all fixed whole carriers and256MiB support fit the available private disk")
            tc_jets, definition, tc_plan, offsets, exact_offsets, receipts = tc_restore.restore(
                np, flint, c, helper, base, iterator, repair, rows, admitted["TC_manifest"],
                admitted["TC_state"], paths[nr["proposal_math"]], private, progress)
            state["necessary_original_trial_receipts"] = receipts; save()
            for value in tc_jets+list(offsets.values()):
                carriers.release_resident_pages(value)
            unused_waist, unused_intrinsic, np_receipts = np_restore.restore(np, flint, npm,
                admitted["NP"], raws, paths, helper, rows, part_receipts, private, progress, atomic)
            state["necessary_original_NP_receipts"] = np_receipts; save()
            np_jets = [np.memmap(Path(private)/("original_NP_endpoint_derivative_%d.f64"%order),
                                dtype="<f8", mode="r", shape=(740,193)) for order in range(4)]
            nodes, original_plan = nu.complete_plan(rows, base["radial_nodes"])
            last = max(item["background_piece"] for item in original_plan)
            prefix_digest = hashlib.sha256()
            for piece in range(last+1):
                prefix_digest.update(canonical({"piece":piece,
                    "physical_offset":list(map(str,exact_offsets[piece]))}))
            require({"pieces":last+1,"signed_offset_sequence_sha256":prefix_digest.hexdigest(),
                "entire_scientific_domain":"[0,9/50]","all_preceding_interface_offsets_included":True}
                == admitted["NP"]["trial_definition"]["necessary_complete_centre_prefix"],
                "the full TC offset carrier contains the identical original RHI/NP prefix")
            del exact_offsets
            rhi_plan, polynomial_path, endpoint, restoration = carriers.restore(
                np, c, core, nu, rhi, base, offsets, rows, nodes, original_plan, np_jets,
                read_ball, admitted["RHI"], paths[roles["RHI_restore"]], private, progress, atomic)
            state["necessary_relative_carrier_receipt"] = restoration; save()
            private_bytes = sum(path.stat().st_size for path in Path(private).rglob("*") if path.is_file())
            require(private_bytes <= PARAMETERS["maximum_private_disk_bytes"],
                    "whole necessary private carrier inventory remains within its disk bound")
            bundle = {"np":np,"flint":flint,"c":c,"core":core,"nu":nu,"rhi":rhi,
                "tc_helper":helper,"tc_definition":definition,"tc_plan":tc_plan,"tc_jets":tc_jets,
                "base":base,"offsets":offsets,"rows":rows,"read_ball":read_ball,
                "rhi_plan":rhi_plan,"relative_polynomial_path":polynomial_path,
                "relative_endpoint":endpoint,"rhi_actual":admitted["RHI"],"p96_actual":admitted["P96"]}
            progress("new_complete_TC96_height_contraction", {"complete_relative_cells":2847,
                "complete_trial_columns":96,"private_carrier_bytes":private_bytes,
                "complete_new_grid":8192,"old_scientific_target_calls":0})
            result = math.compute(bundle, publish, save_prefix, progress)
            require(core.GRID == 1024 and state["saved_record_count"] == 7
                    and state["completed_targets"] == TARGETS,
                    "unchanged original context and all seven complete saved new targets")
        state["result"] = {**result,"kind":KIND,
            "all_four_whole_original_TC_arrays_verified":True,
            "all_four_whole_original_NP_arrays_verified":True,
            "original_RHI_all18_endpoint_and_entire_chain_verified":True,
            "entire_original2847_degree6_polynomials_used":True,
            "all_complete_target_records_saved_and_read_back":True,
            "new_trial_selected":False,"old_scientific_targets_recomputed":False,
            "unused_phase169_carriers_restored":False,
            "full_regular_or_Theta_inverse_proved":False,
            "full_height_phase_Schur_or_topic_completion_proved":False}
        state.update(complete=True, proved=True, actual_returncode=0,
                     stage="complete_"+STAGE+"_scalar_branch")
        save(); return 0
    except BaseException as error:
        state.update(complete=False, proved=False, actual_returncode=1,
            failure={"type":type(error).__name__,"message":str(error)[:2500],
                     "traceback":traceback.format_exc()[-5000:]})
        save(False)
        print(json.dumps({"actual_failure":state["failure"],
                          "saved_record_count":state["saved_record_count"]}), flush=True)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
