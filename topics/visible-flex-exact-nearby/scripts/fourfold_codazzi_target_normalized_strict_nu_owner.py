"""BNC first true target-normalized strict-parameter96 signed column.

Whole NP/PO/ASB/JC and successful DWTB are inputs. Only necessary exact
carriers are restored; the new science consists of the complete192
physical quadratures, five full fees, their joint sum and96 signed values.
"""
from __future__ import annotations
import argparse
import copy
import hashlib
import json
import os
import platform
import subprocess
import sys
import time
import traceback
import importlib.util
from fractions import Fraction
from pathlib import Path

REPO = "Rogerhu12/math-research-public"
TOPIC = "topics/visible-flex-exact-nearby/"
SOURCE = TOPIC+"scripts/fourfold_codazzi_target_normalized_strict_nu_owner.py"
WORKER = TOPIC+"scripts/fourfold_codazzi_target_normalized_strict_nu_public_worker.py"
GENERATOR = TOPIC+"scripts/make_target_normalized_strict_nu_manifest.py"
KIND = "R147_complete_target_normalized_strict_nu_column_v1"
STAGE = "target_normalized_strict_nu_column"
MANIFEST_KIND = "R147_complete_target_normalized_strict_nu_column_inputs_v1"
TARGETS = [
    "complete_target_B_row_error_on_NP_trial_upper",
    "complete_target_B_receiver_on_NP_PDE_error_upper",
    "complete_target_B_trial_compound_error_upper",
    "complete_target_B_trial_quadrature_alias_upper",
    "complete_target_B_trial_quadrature_rounding_upper",
    "complete_target_normalized_strict_nu_column_error_upper",
    "complete_signed_target_normalized_strict_nu_column",
]
RUNTIME = {"python": "3.12.14", "packages": {"numpy": "2.3.5", "python-flint": "0.9.0"}}
PARAMETERS = {
    "arithmetic_bits": 320, "power_series_cap": 9,
    "decimal_record_digits": 60, "private_ball_digits": 90,
    "maximum_scientific_wall_seconds": 16800,
    "row_count": 96, "complete_row_positive_modes": 192,
    "complete_physical_source_positive_modes": 96, "new_grid_points": 8192,
    "physical_frequency_factor": 4, "physical_period": "pi/2", "physical_strip": "1/128",
    "normalized_angular_measure": True,
    "target": "E96_a_star B_inverse physical_strict_nu_column",
    "target_normalizer": "B=Id+T_w I", "true_target_phase": "a=2*H(0)=b-Omega",
    "physical_column": "U_Hinverse (yplus+yminus)/2",
    "true_physical_column_high_modes_set_to_zero": False,
    "physical_mean_slots_eliminated": False, "nonlocal_phase_column_included": False,
    "whole_original_NP_arrays": 4, "whole_original_NP_shape": [740, 193],
    "whole_original_DWTB_row_shape": [96, 192],
    "whole_original_NP_run": "45893562391/1", "whole_original_PO_run": "45903437912/1",
    "whole_original_ASB_run": "45908403884/1", "whole_original_JC_run": "45887337009/1",
    "selected_member_run": "43588332723/1", "selected_member_loss": "1/250",
    "selected_parameter_is_a_numeric_point": False,
    "original_grid_CORETYPE": "unset", "original_trial_CORETYPE": "Haswell", "all_threads": 1,
    "old_completed_scientific_target_calls": 0, "new_complete_targets": 7,
}
SCI_FIELDS = sorted([
    "identity", "parameters", "runtime", "complete", "proved", "actual_returncode", "failure",
    "stage", "progress", "wall_seconds", "completed_targets", "current_target", "candidate_record",
    "new_records", "saved_record_count", "result", "whole_completed_inputs",
    "reference_identity", "selected_member_identity", "copied_prior_scalar_records",
    "carrier_restoration", "necessary_B_row_carrier_receipt", "necessary_NP_trial_receipt",
    "necessary_carrier_rematerializations", "private_physical_grid_receipt",
    "private_unit_disk_input_receipt", "private_complete_observation_receipt",
    "private_exact_column_receipt", "complete_observation_modes", "complete_observation_prefix",
    "old_scientific_target_calls", "new_arrays_published", "new_artifacts", "new_Releases",
])
THREADS = ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS",
           "BLIS_NUM_THREADS", "VECLIB_MAXIMUM_THREADS", "NUMEXPR_NUM_THREADS")


def require(ok, message):
    if not ok:
        raise ValueError(message)


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def canonical(value):
    return (json.dumps(value, sort_keys=True, separators=(",", ":"),
                       ensure_ascii=False, allow_nan=False)+"\n").encode()


def parse(raw):
    return json.loads(raw, parse_constant=lambda value: (_ for _ in ()).throw(ValueError(value)))


def atomic(path, raw):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(path.name+".partial")
    temporary.write_bytes(raw)
    os.replace(temporary, path)


def load(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def admit_complete_inputs(contents, specs, manifest, snapshot_paths):
    admission = load(snapshot_paths["admission"], "_BNC_complete_input_admission")
    return admission.admit_complete_inputs(contents, specs, manifest, snapshot_paths)


def carrier_child(args, context):
    require(args.carrier_directory is not None and args.carrier_receipt is not None
            and not args.carrier_directory.exists() and not args.carrier_receipt.exists(),
            "one fresh original-grid-only private child")
    args.carrier_directory.mkdir(parents=True)
    document = {"kind": "BNC_necessary_original_grid_progress_v1", "complete": False,
                "failure": None, "stage": "whole_DWTB_actual_admitted", "progress": {}, "result": None}
    began = time.perf_counter()

    def progress(stage, details):
        document["stage"], document["progress"] = stage, details
        document["wall_seconds"] = time.perf_counter()-began
        atomic(args.carrier_receipt, canonical(document))
        require(document["wall_seconds"] <= PARAMETERS["maximum_scientific_wall_seconds"],
                "the necessary original input prefix is preserved before runtime expiry")

    try:
        dw = context["parents"]["DW"]
        document["result"] = dw["owner"].restore_original_grid(
            context["DW_context"], dw["contents"]["carrier_original_owner"], args.carrier_directory, progress)
        document["complete"] = True
        progress("same_whole_original_endpoint_raw_grid_SHA_restored", {})
    except BaseException as exc:
        document["failure"] = {"type": type(exc).__name__, "message": str(exc),
                               "traceback": traceback.format_exc()}
        atomic(args.carrier_receipt, canonical(document))
        raise


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ("manifest", "input-map", "output"):
        parser.add_argument("--"+name, type=Path, required=True)
    parser.add_argument("--manifest-sha", required=True)
    parser.add_argument("--checkout", required=True)
    parser.add_argument("--carrier-only", action="store_true")
    parser.add_argument("--carrier-directory", type=Path)
    parser.add_argument("--carrier-receipt", type=Path)
    args = parser.parse_args()
    require(os.environ.get("GITHUB_ACTIONS") == "true" and os.environ.get("GITHUB_REPOSITORY") == REPO
            and os.environ.get("GITHUB_RUN_ATTEMPT") == "1", "one first public complete BNC target")
    manifest_raw = args.manifest.read_bytes()
    manifest = parse(manifest_raw)
    require(sha(manifest_raw) == args.manifest_sha and manifest["kind"] == MANIFEST_KIND
            and manifest["scientific_kind"] == KIND and manifest["stage"] == STAGE
            and manifest["parameters"] == PARAMETERS and manifest["runtime"] == RUNTIME
            and manifest["target_order"] == TARGETS and manifest["complete_record_counts"] == [7]
            and manifest["allowed_scientific_fields"] == SCI_FIELDS, "the complete first BNC contract")
    specs = {item["role"]: item for item in manifest["files"]+manifest["historical_inputs"]}
    snapshot_paths = {key: Path(value) for key, value in parse(args.input_map.read_bytes()).items()}
    require(set(snapshot_paths) == set(specs) and sha(Path(__file__).read_bytes()) == specs["science"]["sha256"],
            "the immutable owner and every complete private input")
    contents = {role: path.read_bytes() for role, path in snapshot_paths.items()}
    sys.dont_write_bytecode = True
    context = admit_complete_inputs(contents, specs, manifest, snapshot_paths)
    if args.carrier_only:
        carrier_child(args, context)
        return 0
    require(not args.output.exists(), "never overwrite a prior complete or partial outcome")
    parents, pure = context["parents"], context["math"]
    np_actual, po_actual, sb_actual, dw_actual = (parents[tag]["actual"] for tag in ("NP", "PO", "SB", "DW"))
    poi = context["PO_prior"]
    jc = poi["JC"]
    copied = {
        "N0": copy.deepcopy(po_actual["new_records"]["complete_NP_even_physical_trial_L2_upper"]),
        "Db": copy.deepcopy(sb_actual["new_records"]["complete_true_NP_short_waist_density_error_upper"]),
        "BH": copy.deepcopy(poi["old_bounds"]["BH"]),
        "EH": copy.deepcopy(jc["copied_prior_scalar_records"]["EH"]),
        "G0": copy.deepcopy(jc["copied_prior_scalar_records"]["G0"]),
        "m": copy.deepcopy(jc["new_records"]["complete_interpolation_derivative_lower"]),
        "J": copy.deepcopy(dw_actual["new_records"]["complete_I_trial_Hilbert_Schmidt_upper"]),
        "eR": copy.deepcopy(dw_actual["new_records"]["complete_target_B_inverse96_joint_L2_row_error_upper"]),
    }
    document = {
        "identity": {"kind": KIND, "scalar_stage": STAGE, "source_sha256": specs["science"]["sha256"],
            "manifest_sha256": args.manifest_sha, "arithmetic_bits": 320,
            "run_id": os.environ["GITHUB_RUN_ID"], "run_attempt": "1",
            "event_commit": os.environ["GITHUB_SHA"], "actual_checkout_commit": args.checkout,
            "whole_parent_identities": {tag: {name: specs[tag+"_"+name]["sha256"]
                for name in ("manifest", "actual", "execution")} for tag in ("NP", "PO", "SB", "DW")}},
        "parameters": PARAMETERS, "runtime": {}, "complete": False, "proved": False,
        "actual_returncode": None, "failure": None, "stage": "whole_original_completed_inputs_admitted",
        "progress": {}, "wall_seconds": 0.0, "completed_targets": [], "current_target": None,
        "candidate_record": None, "new_records": {}, "saved_record_count": 0, "result": None,
        "whole_completed_inputs": {"all_descriptors_sha256": sha(canonical(manifest["files"]+manifest["historical_inputs"])),
            "current_objects": len(manifest["files"]), "historical_objects": len(manifest["historical_inputs"]),
            "all_parent_bindings_recovered_from_whole_original_manifests": True},
        "reference_identity": copy.deepcopy(np_actual["reference_identity"]),
        "selected_member_identity": copy.deepcopy(np_actual["selected_member_identity"]),
        "copied_prior_scalar_records": copied, "carrier_restoration": None,
        "necessary_B_row_carrier_receipt": None, "necessary_NP_trial_receipt": None,
        "necessary_carrier_rematerializations": 0, "private_physical_grid_receipt": None,
        "private_unit_disk_input_receipt": None, "private_complete_observation_receipt": None,
        "private_exact_column_receipt": None, "complete_observation_modes": 0,
        "complete_observation_prefix": None, "old_scientific_target_calls": 0,
        "new_arrays_published": 0, "new_artifacts": 0, "new_Releases": 0,
    }
    require(sorted(document) == SCI_FIELDS, "the whole compact BNC scientific schema")
    began = time.perf_counter()
    private = args.output.parent/"private-complete-BNC"
    private.mkdir()

    def save():
        document["wall_seconds"] = time.perf_counter()-began
        raw = canonical(document)
        require(len(raw) <= manifest["operation"]["maximum_scientific_bytes"],
                "the complete new signed conclusion fits the public file limit")
        atomic(args.output, raw)

    def progress(stage, details):
        document["stage"], document["progress"] = stage, details
        save()
        require(document["wall_seconds"] <= PARAMETERS["maximum_scientific_wall_seconds"],
                "the complete true natural prefix is preserved before runtime expiry")
        print(json.dumps(dict(stage=stage, **details), sort_keys=True), flush=True)

    save()
    try:
        from importlib.metadata import version
        runtime = {"python": platform.python_version(),
                   "packages": {name: version(name) for name in ("numpy", "python-flint")}}
        require(runtime == RUNTIME and os.environ.get("OPENBLAS_CORETYPE") == "Haswell"
                and all(os.environ.get(name) == "1" for name in THREADS), "the whole original immutable arithmetic runtime")
        document["runtime"] = dict(runtime, OPENBLAS_CORETYPE="Haswell", all_threads=1, arithmetic_bits=320)
        carrier_dir = private/"whole-original-grid"
        carrier_receipt = private/"whole-original-grid-progress.json"
        command = [sys.executable, str(Path(__file__)), "--manifest", str(args.manifest),
            "--manifest-sha", args.manifest_sha, "--input-map", str(args.input_map),
            "--output", str(args.output), "--checkout", args.checkout, "--carrier-only",
            "--carrier-directory", str(carrier_dir), "--carrier-receipt", str(carrier_receipt)]
        child_env = dict(os.environ)
        child_env.pop("OPENBLAS_CORETYPE", None)
        document["necessary_carrier_rematerializations"] = 1
        save()
        with (private/"original-grid-only.stdout").open("wb") as child_log:
            child = subprocess.Popen(command, env=child_env, stdout=child_log, stderr=subprocess.STDOUT)
            last_update = 0.0
            try:
                while child.poll() is None:
                    now = time.perf_counter()
                    if now-last_update >= 45:
                        if carrier_receipt.exists():
                            document["carrier_restoration"] = parse(carrier_receipt.read_bytes())
                        progress("necessary_same_original_grid_restoration_running", {})
                        last_update = now
                    time.sleep(2)
            except BaseException:
                child.terminate()
                try:
                    child.wait(timeout=30)
                except subprocess.TimeoutExpired:
                    child.kill()
                    child.wait()
                raise
        require(carrier_receipt.exists(), "the necessary carrier child left its full actual receipt")
        document["carrier_restoration"] = parse(carrier_receipt.read_bytes())
        restored = document["carrier_restoration"]
        require(child.returncode == 0 and restored["complete"] is True and restored["failure"] is None
                and restored["result"]["complete"] is True
                and restored["result"]["grid"] == context["DW_context"]["AS"]["actual"]["private_grid_receipt"],
                "the whole original endpoint/raw/grid has its actual original SHA before any BNC science")
        grid_raw = (carrier_dir/"complete-original-AS-grid.json").read_bytes()
        import numpy as np
        import flint
        flint.ctx.prec, flint.ctx.cap = 320, 9
        api = context["DW_context"]["carrier"].directed_api(flint)
        api.midpoint_real = lambda value: value.mid()
        api.midpoint_complex = lambda value: api.acb(value.real.mid(), value.imag.mid())
        exact_string = context["row_restore"].exact_string
        exact_rows, row_receipt = context["row_restore"].restore(
            np, api, context["DW_context"], dw_actual, grid_raw, private/"same-complete-B-rows", progress)
        document["necessary_B_row_carrier_receipt"] = row_receipt
        progress("same_original_B_rows_restored_without_old_error_targets", {"rows": 96})

        # The original NP four full arrays, without its old residual or pairings.
        npm = parents["NP"]["manifest"]
        paths, raws = context["paths_by_path"], context["raws_by_path"]
        roles, helper = npm["roles"], context["row_inputs"]
        original_body = json.loads(raws[roles["old_body_manifest"]])
        rows, part_receipts = helper.admit_all_rows(
            [paths[item["path"]] for item in npm["historical_inputs"] if item["role"].startswith("original_rows_")],
            {"old_body_manifest": original_body, "NW": {"difference": context["NP_SB"]["prior"]["D"]}})
        waist, scalars, np_receipt = context["NP_restore"].restore(
            np, flint, npm, np_actual, raws, paths, helper, rows, part_receipts,
            private/"same-complete-NP", progress, atomic)
        document["necessary_NP_trial_receipt"] = np_receipt

        def ball(record):
            return context["DW_context"]["carrier"].whole_ball(api, record)

        def upper(record):
            return context["DW_context"]["carrier"].whole_upper(api, record)

        # Reuse the original K(0) finite input algebra, not the wider whole-cell
        # K interval. No intrinsic enclosure or scalar norm target is rerun.
        core = load(paths[roles["trial_math"]], "_BNC_original_physical_waist_algebra")
        backend, unused = helper.directed_backend(np, flint, raws[roles["box_math"]], raws[roles["fft_math"]])
        c = core.DirectedContext(np, api.arb, backend["Box"], backend["CBox"], backend["zeros"],
            backend["arb_box"], backend["reduce_box"], backend["DirectedFFT"]())
        row0 = rows[0]
        left, right = map(Fraction, row0["interval"])
        Kfield = core.scalar_taylor(c, row0["intrinsic_midpoint_jets"], row0["intrinsic_whole_third_jets"],
                                   "K", *row0["interval"], left, right, ball)
        require(Kfield.degree == 0 and left == 0, "the complete original scalar at the actual waist")
        Kbox = core.trial_value(c, Kfield.coefficients, c.box(-1))[0, 0]
        Kradius = float(np.max(Kfield.error.hi))
        Kbox = Kbox+c.Box(-Kradius, Kradius)
        K0 = api.arb(float(Kbox.lo)).union(api.arb(float(Kbox.hi)))
        mean_record = np_actual["new_records"]["complete_signed_strict_nu_waist_column"]["whole_selected_waist_mean_enclosure"]
        mean = ball(mean_record)
        require(K0.upper() < 0 and mean.upper() < 0 and scalars["waist_a"].lower() > 0,
                "whole original same-selected physical denominators, never fixed midpoint state")
        q, ng = (-K0).sqrt(), scalars["waist_a"]**2/(mean*mean)
        coefficients = pure.physical_positive_coefficients(api, waist, q, ng)
        original_grid = parse(grid_raw)["all_pairs"]
        require(len(original_grid) == 8192, "all original full-phase G input values")
        physical_grid = []
        for m, pair in enumerate(original_grid):
            angle = api.arb.pi()*m/(2*8192)
            f = sum((2*value*(4*n*angle).cos() for n, value in enumerate(coefficients, 1)), api.zero)
            phase = api.arb(pair[1])
            entry = [f.str(90), phase.str(90)]
            require(api.arb(entry[0]).contains(f) and api.arb(entry[1]).contains(phase),
                    "both full physical polynomial and original G balls survive the stored grid")
            physical_grid.append(entry)
            if m and m % 1024 == 0:
                progress("new_complete_physical_NP_grid", {"complete_nodes": m, "total_nodes": 8192})
        physical_body = {"kind": "BNC_complete_physical_NP_and_original_G_grid_v1", "nodes": 8192,
            "all_pairs": physical_grid, "source_positive_modes": 96,
            "original_G_grid_sha256": sha(grid_raw), "original_NP_trial_definition_sha256": np_receipt["complete_original_trial_definition_sha256"],
            "complete_selected_mean_ball": copy.deepcopy(mean_record),
            "complete_original_waist_K_ball": K0.str(90), "complete_q_ball": q.str(90), "complete_ng_ball": ng.str(90),
            "true_physical_source_is_not_a_numeric_selected_state": True}
        physical_raw = canonical(physical_body)
        physical_path = private/"complete-new-physical-grid.json"
        atomic(physical_path, physical_raw)
        require(physical_path.read_bytes() == physical_raw, "every new physical source/G pair saved and read")
        document["private_physical_grid_receipt"] = {"bytes": len(physical_raw), "sha256": sha(physical_raw),
            "nodes": 8192, "source_positive_modes": 96, "whole_original_G_phase_retained": True}
        whole_grid = [(api.arb(f), api.arb(g)) for f, g in parse(physical_path.read_bytes())["all_pairs"]]
        kernel = pure.CompletePhysicalQuadrature(api, whole_grid)

        def encoded_upper(value):
            point = value.upper()
            require(point.is_finite() and point >= 0, "one complete new nonnegative bound")
            body = {"ball": point.str(60), "bound": "upper"}
            require(api.arb(body["ball"]).contains(point), "whole directed new bound round trip")
            return body

        input_body = {"kind": "BNC_complete_new_unit_circle_input_v1", "nodes": 8192,
            "physical_grid_sha256": sha(physical_raw),
            "raw_mean_radius_upper": encoded_upper(kernel.raw_radius),
            "all_exact_u_sreal_simag_and_tau_balls": [
                [exact_string(api, kernel.u[m]), exact_string(api, kernel.s[m].real),
                 exact_string(api, kernel.s[m].imag), kernel.tau[m].str(90)] for m in range(8192)]}
        input_raw = canonical(input_body)
        input_path = private/"complete-new-physical-disk-input.json"
        atomic(input_path, input_raw)
        require(input_path.read_bytes() == input_raw, "all new8192 disk input points and full radii saved/read")
        input_body = parse(input_path.read_bytes())
        for m, (u, sr, si, tau) in enumerate(input_body["all_exact_u_sreal_simag_and_tau_balls"]):
            formal_u = api.rational(Fraction(u))
            formal_s = api.acb(api.rational(Fraction(sr)), api.rational(Fraction(si)))
            formal_tau = api.arb(tau)
            require(formal_u == kernel.u[m] and formal_s == kernel.s[m]
                    and formal_tau.contains(kernel.tau[m]), "every exact disk point and whole radius survives")
            kernel.u[m], kernel.s[m], kernel.tau[m] = formal_u, formal_s, formal_tau.upper()
        kernel.raw_radius = upper(input_body["raw_mean_radius_upper"])
        document["private_unit_disk_input_receipt"] = {"bytes": len(input_raw), "sha256": sha(input_raw),
            "nodes": 8192, "all_complete_point_centers_and_radii_read_back": True}
        progress("new_full_physical_grid_and_unit_circle_inputs_saved", {"nodes": 8192})

        mode_path = private/"complete-new-physical-observations.jsonl"
        with mode_path.open("wb") as stream:
            for n in range(1, 193):
                disk = kernel.next()
                body = {"kind": "BNC_complete_one_physical_observation_disk_v1", "mode": n,
                    "complete_grid_points": 8192, "whole_input_sha256": sha(input_raw),
                    "exact_center_pair": [exact_string(api, disk["center"].real), exact_string(api, disk["center"].imag)],
                    "complete_radius_upper": encoded_upper(disk["radius"])}
                mode_raw = canonical(body)
                offset = stream.tell()
                stream.write(mode_raw)
                stream.flush()
                os.fsync(stream.fileno())
                with mode_path.open("rb") as check:
                    check.seek(offset)
                    require(check.readline() == mode_raw, "one entire natural new observation saved/read")
                document["complete_observation_modes"] = n
                if n % 16 == 0:
                    prefix_raw = mode_path.read_bytes()
                    document["complete_observation_prefix"] = {"complete_modes": n, "total_modes": 192,
                        "bytes": len(prefix_raw), "sha256": sha(prefix_raw),
                        "unfinished_prefix_is_not_a_complete_column": n != 192}
                    progress("new_complete_BNC_observation_prefix", {"complete_modes": n, "total_modes": 192})
        mode_raw = mode_path.read_bytes()
        all_modes = [parse(line) for line in mode_raw.splitlines()]
        require(len(all_modes) == 192 and [item["mode"] for item in all_modes] == list(range(1, 193))
                and all(item["complete_grid_points"] == 8192 and item["whole_input_sha256"] == sha(input_raw)
                        for item in all_modes), "all192 entire observations and their common whole input")
        document["private_complete_observation_receipt"] = {"bytes": len(mode_raw), "sha256": sha(mode_raw),
            "complete_positive_modes": 192, "complete_grid_points_per_mode": 8192,
            "all_complete_modes_read_back": True}
        centers = [item["exact_center_pair"] for item in all_modes]
        exact_column = pure.complete_exact_signed_pairings(exact_rows, centers)
        column_body = {"kind": "BNC_complete_exact_signed_trial_column_v1", "rows": 96,
            "all96_exact_signed_rationals": exact_column,
            "whole_original_row_carrier_sha256": row_receipt["row_trial"]["sha256"],
            "whole_new_observation_sha256": sha(mode_raw)}
        column_raw = canonical(column_body)
        column_path = private/"complete-new-exact-signed-column.json"
        atomic(column_path, column_raw)
        require(column_path.read_bytes() == column_raw, "the entire exact rational signed96 column saved/read")
        exact_column = parse(column_path.read_bytes())["all96_exact_signed_rationals"]
        document["private_exact_column_receipt"] = {"bytes": len(column_raw), "sha256": sha(column_raw),
            "rows": 96, "all_signs_and_complete192_row_support_retained": True}

        formal_disks = [{"mode": item["mode"], "complete_grid_points": item["complete_grid_points"],
                         "radius": upper(item["complete_radius_upper"])} for item in all_modes]
        values = pure.complete_component_errors(api,
            saved_joint_B_row_error=upper(copied["eR"]), saved_trial_row_HS=upper(copied["J"]),
            saved_physical_N0=upper(copied["N0"]), saved_short_waist_density_error=upper(copied["Db"]),
            saved_BH=upper(copied["BH"]), saved_EH=upper(copied["EH"]), saved_G0=upper(copied["G0"]),
            saved_interpolation_lower=ball(copied["m"]), whole_saved_observation_disks=formal_disks)

        def finish(name, body):
            require(name == TARGETS[document["saved_record_count"]], "the complete seven-object BNC natural order")
            document["current_target"], document["candidate_record"] = name, body
            save()
            formal = parse(args.output.read_bytes())["candidate_record"]
            require(formal == body, "the entire new conclusion saved/read before any dependency")
            document["new_records"][name] = formal
            document["completed_targets"].append(name)
            document["saved_record_count"] += 1
            document["current_target"] = document["candidate_record"] = None
            save()
            return formal

        formal_components = {}
        for name in pure.COMPONENT_ORDER:
            formal_components[name] = upper(finish(name, encoded_upper(values[name])))
        error = pure.complete_column_error(api, formal_components)
        formal_error = finish(TARGETS[5], encoded_upper(error))
        enclosures = pure.complete_signed_enclosures(api, exact_column, upper(formal_error))
        signed_records = []
        for j, value in enumerate(enclosures, 1):
            text = value.str(60)
            require(api.arb(text).contains(value), "the entire true signed component is formally enclosed")
            signed_records.append({"row": j, "ball": text, "bound": "signed_enclosure"})
        signed = {"kind": "BNC_complete_true_target_normalized_strict_nu_column_v1", "rows": 96,
            "all96_exact_signed_trial_rationals": exact_column, "all96_true_signed_balls": signed_records,
            "joint_l2_error_upper": formal_error,
            "prior_two_independent_density_mean_balls": copy.deepcopy(np_actual["new_records"][
                "complete_signed_strict_nu_waist_column"]["complete_signed_output_balls"]["independent_density_means"]),
            "physical_mean_slots_eliminated": False, "nonlocal_phase_or_mean_height_column_claimed": False,
            "true_full_physical_high_forcing_retained": True, "whole_physical_column_used": True,
            "original_target_normalizer_and_true_phase_retained": True}
        finish(TARGETS[6], signed)
        document["result"] = {"kind": KIND, "complete_new_record_count": 7, "complete_new_record_order": list(TARGETS),
            "complete_new_physical_observation_modes": 192, "complete_true_target_normalized_signed_rows": 96,
            "joint_l2_column_error_proved": True, "whole_nonunitary_physical_receiver_paid": True,
            "whole_unshifted_G_and_true_target_a_used": True,
            "all_row_PDE_compound_alias_and_disk_fees_retained": True,
            "both_independent_physical_means_retained": True,
            "old_completed_scientific_targets_recomputed": False,
            "full_homogeneous_inverse_or_high_Schur_proved": False,
            "nonlocal_phase_or_mean_height_column_claimed": False, "topic_completion_proved": False}
        document["complete"] = document["proved"] = True
        document["actual_returncode"] = 0
        document["stage"] = "complete_"+STAGE+"_scalar_branch"
        save()
        print(json.dumps({"complete": True, "new_targets": 7, "true_signed_rows": 96,
                          "old_scientific_target_calls": 0, "actual_sha256": sha(args.output.read_bytes())},
                         sort_keys=True), flush=True)
        return 0
    except BaseException as exc:
        document["complete"] = document["proved"] = False
        document["actual_returncode"] = 1
        document["failure"] = {"type": type(exc).__name__, "message": str(exc),
                               "traceback": traceback.format_exc()}
        save()
        raise


if __name__ == "__main__":
    sys.exit(main())
