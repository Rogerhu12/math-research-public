"""Rematerialize only the WHOLE original successful SN finite endpoint.

Metadata admission and Git-byte restoration use standard library only.
The point-proposal recurrence is called only in the public Actions owner,
under the original immutable arithmetic. No old residual/energy/norm runs.
"""
from __future__ import annotations
import hashlib
import importlib.util
import json
import os
import subprocess
import sys
from fractions import Fraction
from pathlib import Path
from types import SimpleNamespace

TOPIC = "topics/visible-flex-exact-nearby/"
MANIFEST_PATH = TOPIC+"notes/2026-11-15-R133-signed-nonmean-density-H3-CI-inputs.json"
MANIFEST_SHA = "f6e5f9fe938d897c2b57d3d34e42391455fc6cea9804576d4dcc90b2021a8351"
SOURCE = TOPIC+"scripts/fourfold_codazzi_signed_nonmean_density_H3.py"
HELPER = TOPIC+"scripts/fourfold_codazzi_signed_density_transport_arithmetic.py"
SOURCE_SHA = "6c63241ae5ad865952620f68d63670604875b460e51b083ecb66127cb785b339"
HELPER_SHA = "217a91e25ec7bb6cad5c115ddc4749f4d714c5ca47601e8ad8dd540e69ed1718"
EXECUTION_SHA = "eccb4ce4e7f8c783079e4400cd7a978214817d8092f50cd2bb8f1acbcf3d6ea6"
SCIENCE_SHA = "8fea75ce01dd4bbd0d20532332ed458af73634a995c1dbce5c3cbac511e0e8a0"
ENDPOINT_SHA = "3048266ba668164d7d9b5475c5262f1f3568cfe32a6e42c7bb496e4bda6c62b6"
ENDPOINT_BYTES = 245885
COMMITS = {"5e14fd1de48f7c51dbe465cebef048c3d948fc76",
           "46f127c7153f5393dcd2a00f42d4c1d3662c294d"}


def require(ok, message):
    if not ok:
        raise ValueError(message)


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def canonical(value):
    return (json.dumps(value, sort_keys=True, separators=(",", ":"),
                       allow_nan=False)+"\n").encode()


def parse(raw):
    return json.loads(raw, parse_constant=lambda value: (_ for _ in ()).throw(ValueError(value)))


def admit_complete_original(manifest_raw, execution_raw):
    require(len(manifest_raw) == 97309 and sha(manifest_raw) == MANIFEST_SHA,
            "whole original successful SN manifest")
    require(len(execution_raw) == 42242 and sha(execution_raw) == EXECUTION_SHA,
            "whole unique successful SN execution")
    manifest, execution = parse(manifest_raw), parse(execution_raw)
    science = execution["actual_scientific_receipt"]
    require(execution["complete"] is True and execution["scientific_target_complete"] is True
            and execution["actual_returncode"] == 0 and execution["actual_failure"] is None
            and execution["supervision_failure"] is None
            and str(execution["run_id"]) == "43751213826" and str(execution["run_attempt"]) == "1"
            and execution["repository"] == "Rogerhu12/math-research-public"
            and execution["source_budget_source_sha256"] == SOURCE_SHA
            and execution["helper_source_sha256"] == HELPER_SHA
            and execution["input_manifest_sha256"] == MANIFEST_SHA,
            "same original full successful public SN run and sources")
    raw = canonical(science)
    require(len(raw) == 22817 and sha(raw) == SCIENCE_SHA,
            "whole original successful scientific JSON bytes")
    require(science["complete"] is True and science["new_target_complete"] is True
            and science["actual_returncode"] == 0 and science["failure"] is None
            and science["source_sha256"] == SOURCE_SHA and science["helper_sha256"] == HELPER_SHA
            and science["input_manifest_sha256"] == MANIFEST_SHA
            and science["parameters"] == manifest["parameters"]
            and science["actual_gate_count"] == 21 and len(science["gates"]) == 21
            and all(gate["passed"] is True for gate in science["gates"])
            and science["latest_atomic_scientific_stage"] == "complete_new_H3_target",
            "entire final SN target, not a prefix")
    transport = science["complete_new_transport_conclusion"]
    require(science["actual_completed_original_transport_intervals"] == 3146
            and science["actual_new_transport_subcells_completed"] == 12584
            and science["actual_exact_radial_cursor"] == "0"
            and transport["original_intervals_read"] == 3146
            and transport["original_candidate_pieces_read"] == 2550
            and transport["new_subcells"] == 12584
            and transport["completed_prefix_budget_subcells_reused"] == 1256
            and transport["new_suffix_subcells_verified"] == 11328
            and transport["complete_residual_modes_not_truncated"] is True,
            "every original interval has exactly four complete subcells")
    identity = transport["complete_final_reference_endpoint_identity"]
    require(identity["canonical_bytes"] == ENDPOINT_BYTES and identity["sha256"] == ENDPOINT_SHA
            and identity["definition"] == "sorted exact dyadic real and imaginary Fourier coefficients, both signs",
            "complete two-branch exact original endpoint identity")
    rows = manifest["file_receipts"]
    require(len(rows) == 207 and sum(row["bytes"] for row in rows) == 13612391
            and len({row["path"] for row in rows}) == 207
            and {row["path"]: row["sha256"] for row in rows} == manifest["files"]
            and set(manifest["allowed_historical_commits"]) == COMMITS
            and manifest["files"][SOURCE] == SOURCE_SHA and manifest["files"][HELPER] == HELPER_SHA,
            "whole original207-file closure and its immutable history")
    terminal = science["complete_first_nonmean_coefficient_H3_conclusion"]
    require(terminal["all_complete_derivative_columns_0_through_3_saved"] is True
            and terminal["same_selected_parameter_and_true_mean"] is True
            and terminal["true_angle_only_at_original_selected_parameter"] is True
            and terminal["full_real_family_transport_half_width"] == "1/10000000000"
            and set(terminal["branches"]) == {"-1", "1"}
            and all(branch["derivative_orders"] == [0, 1, 2, 3]
                    and branch["complete_mean_is_exactly_zero"] is True
                    and len(branch["complete_transport_derivative_L2_error"]) == 4
                    for branch in terminal["branches"].values())
            and terminal["true_angle_derivatives"]["literal_31over32_33over32_gates_verified"] is True,
            "both whole error columns, selected parameter and true-density matrix")
    return manifest, execution, science


def restore_original_files(repo, destination, manifest_raw, current_by_path, progress):
    require(os.environ.get("GITHUB_ACTIONS") == "true"
            and os.environ.get("GITHUB_REPOSITORY") == "Rogerhu12/math-research-public",
            "private complete input restoration only in public Actions")
    manifest = parse(manifest_raw)
    require(sha(manifest_raw) == MANIFEST_SHA, "the original whole manifest")
    require(set(current_by_path) == set(manifest["current_text_paths"]),
            "every original current text is an immutable complete snapshot")
    repo, destination = Path(repo).resolve(), Path(destination).resolve()
    destination.mkdir(parents=True, exist_ok=False)
    fetched, receipt = set(), []
    for row in manifest["file_receipts"]:
        relative = row["path"]
        path = destination/relative
        require(relative.startswith(TOPIC) and path.resolve().is_relative_to(destination),
                "one original in-topic complete input path")
        if relative in current_by_path:
            raw = current_by_path[relative]
            origin = "current_whole_snapshot"
        else:
            commit = manifest["historical_input_overrides"].get(relative, manifest["historical_input_commit"])
            require(commit in COMMITS, "one original exact historical commit")
            if commit not in fetched:
                exists = subprocess.run(["git", "cat-file", "-e", commit+"^{commit}"],
                    cwd=repo, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL).returncode == 0
                if not exists:
                    subprocess.run(["git", "fetch", "--no-tags", "--filter=blob:none", "origin", commit],
                                   cwd=repo, check=True, stdout=subprocess.DEVNULL)
                fetched.add(commit)
            raw = subprocess.check_output(["git", "show", commit+":"+relative], cwd=repo)
            origin = commit
        require(len(raw) == row["bytes"] and sha(raw) == row["sha256"],
                "all bytes of original SN input: "+relative)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(raw)
        require(path.read_bytes() == raw, "whole private original input read-back")
        receipt.append(dict(row, origin=origin))
        if len(receipt) % 32 == 0:
            progress("restoring_original_SN_inputs", {"complete_files": len(receipt), "total_files": 207})
    path = destination/MANIFEST_PATH
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(manifest_raw)
    return {"kind": "AS_complete_original_SN_input_bytes_v1", "complete": True,
            "complete_files": 207, "complete_bytes": 13612391,
            "whole_original_file_receipts_sha256": sha(canonical(manifest["file_receipts"])),
            "whole_restoration_origins_sha256": sha(canonical(receipt)),
            "whole_original_manifest_sha256": MANIFEST_SHA}


def _load(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def rematerialize_original_endpoint(original_root, progress):
    require(os.environ.get("GITHUB_ACTIONS") == "true", "original finite carrier reconstruction only in Actions")
    root = Path(original_root).resolve()
    require(sha((root/SOURCE).read_bytes()) == SOURCE_SHA
            and sha((root/HELPER).read_bytes()) == HELPER_SHA,
            "whole original arithmetic before any numerical import")
    import flint
    flint.ctx.prec, flint.ctx.cap = 320, 9
    helper = _load(root/HELPER, "fourfold_codazzi_signed_density_transport_arithmetic")
    source = _load(root/SOURCE, "_AS_original_SN_point_source")

    def forbidden(*args, **kwargs):
        raise RuntimeError("AS forbids replay of a completed SN validation or norm target")

    for name in ("root_entry", "complete_taylor", "transport", "terminal", "main",
                 "gram_error_step", "complete_reference_residual", "finite_angle_derivative",
                 "inverse_density_constant", "h3_columns"):
        setattr(source, name, forbidden)
    for name in ("mean_parameter_fee", "mean_reference", "parameter_error"):
        setattr(source.Inputs, name, forbidden)
    for name in ("gram_error_step", "complete_reference_residual", "finite_angle_derivative",
                 "inverse_density_constant", "h3_columns"):
        setattr(helper, name, forbidden)
    for name in ("a", "l2", "h3"):
        setattr(helper.LP, name, forbidden)

    args = SimpleNamespace(root=root, manifest=root/MANIFEST_PATH, manifest_sha=MANIFEST_SHA,
                           bits=320, out=root/"private-original-SN-admission.json")
    diagnostics = {"gates": []}
    inp = source.Inputs(args, diagnostics)
    refs = {s: helper.LP([flint.acb(0)]*257, -128) for s in (-1, 1)}
    cursor = source.CUT
    saved_means = {
        inp.preparatory["latest_original_interval"]["original_interval"]:
            inp.preparatory["latest_original_interval"],
        inp.transport_prefix["complete_preparatory_conclusions"]["latest_original_interval"]["original_interval"]:
            inp.transport_prefix["complete_preparatory_conclusions"]["latest_original_interval"],
    }
    pieces, count = set(), 0
    for index in range(3145, -1, -1):
        old = inp.fp["rows"][index]
        left, right = map(Fraction, old["interval"])
        piece = int(old["actual_candidate_piece"])
        require(right == cursor and inp.nodes[piece] <= left < right <= inp.nodes[piece+1],
                "same complete original interval and candidate piece")
        row = inp.scalar_membership(left, right, old)
        if index in saved_means:
            saved = saved_means[index]
            require(saved["actual_candidate_piece"] == piece
                    and list(map(Fraction, saved["exact_interval"])) == [left, right],
                    "complete originally saved linear-mean proposal")
            mref = [helper.exact(Fraction(v)) for v in saved["complete_mean_reference_exact_coefficients"]]
        else:
            ml, mr = inp.endpoint_mean(index, "right"), inp.endpoint_mean(index, "left")
            mref = [helper.exact(helper.rat(ml)),
                    helper.exact(helper.rat((mr-ml)/helper.exact(right-left)))]
        boundaries = [right-(right-left)*Fraction(j, 4) for j in range(5)]
        for j in range(4):
            hi, lo = boundaries[j], boundaries[j+1]
            for sigma in (-1, 1):
                force, speed, unused = inp.nominal_source(index, row, piece, hi, hi, 7, mref, right, sigma)
                proposal, endpoint = helper.reference_step(refs[sigma], force, speed,
                                                           helper.exact(hi-lo), 128, 6)
                require(endpoint.finite() and endpoint.mean().is_zero(),
                        "complete original two-sign exact-dyadic reference")
                refs[sigma] = endpoint
            count += 1
        pieces.add(piece)
        cursor = left
        if index % 32 == 0:
            progress("rematerializing_original_SN_endpoint", {
                "complete_original_intervals": 3146-index, "complete_subcells": count,
                "exact_radial_cursor": str(cursor), "completed_old_validation_targets_replayed": 0})
    require(count == 12584 and cursor == 0 and len(pieces) == 2550,
            "entire original SN point recurrence reaches its real waist")
    value = {str(s): {"lo": refs[s].lo, "coefficients": [
        [str(helper.rat(z.real)), str(helper.rat(z.imag))] for z in refs[s].p]} for s in (-1, 1)}
    raw = source.canonical(value)
    require(len(raw) == ENDPOINT_BYTES and sha(raw) == ENDPOINT_SHA,
            "exact original whole two-branch endpoint SHA, no relaxation")
    path = root/"private-complete-original-SN-endpoint.json"
    path.write_bytes(raw)
    read = path.read_bytes()
    require(read == raw, "whole restored original endpoint read-back")
    formal = source.read(path)
    refs = {s: helper.LP([flint.acb(helper.exact(Fraction(z[0])), helper.exact(Fraction(z[1])))
                         for z in formal[str(s)]["coefficients"]], formal[str(s)]["lo"])
            for s in (-1, 1)}
    receipt = {"kind": "AS_exact_original_SN_two_branch_endpoint_restoration_v1", "complete": True,
               "bytes": ENDPOINT_BYTES, "sha256": ENDPOINT_SHA, "original_intervals": 3146,
               "complete_subcells": 12584, "original_candidate_pieces": 2550,
               "old_completed_residual_energy_norm_targets_replayed": 0,
               "both_branches_all257_coefficients_retained": True,
               "original_runtime_source_helper_and_serial_rounding_preserved": True}
    return inp, refs, helper, receipt
