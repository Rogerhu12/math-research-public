"""Input-only runtime identification using the existing public metadata engine.

The entire TC scientific pipeline is removed, including row restoration,
owner admission, QR proposals and all residual calls. Only the unchanged
Git/current input publisher and its capacity/README/rebase behavior remain.
"""
from pathlib import Path
import hashlib

BASE_NAME = "fourfold_codazzi_true_root_trial_public_worker.py"
BASE_BYTES = 43200
BASE_SHA256 = "fca2c64ec4b479c2599d13377d4d658242d42b028455c30c1c11482f73840c37"

FINAL_FILES = r'''
    def final_files():
        body = encode(state)
        require(len(body) <= op["maximum_execution_bytes"], "whole input-only execution receipt budget")
        report = ("# Original nodal carrier runtime identification\n\nRun "+run+"/"+attempt
            +". Complete original carrier identity recovered: "+str(state["complete"])+".\n\n"
            "The actual CPU, NumPy dispatch and BLAS core are recorded before the two declared "
            "untested schedules. An original nodal-to-Hermite producer is accepted only after "
            "the entire original cubic and all fourteen full-direction shard hashes match. "
            "The prior Haswell/default failure is reused without reproducing it. No TC owner, "
            "QR solve, old norm, residual, new scientific column or integration cell is run; "
            "all 992 already accepted TC cells remain unchanged.\n").encode()
        return {**staged, output_dir+"/execution.json": body, output_dir+"/report.md": report}
'''

PIPELINE = r'''
    try:
        head = pull()
        if git("cat-file", "-e", head+":"+marker_path, check_return=False).returncode == 0:
            prior = parse(git("show", head+":"+marker_path, binary=True).stdout)
            require(prior.get("problem_id") == manifest["problem_id"], "same already consumed input-only identification")
            print("Existing input-only identification retained; no automatic replay.", flush=True)
            print(encode(prior).decode(), end="", flush=True)
            return
        materialize_current(head)
        restore_history()
        helper = import_source(inputs_root/roles["owner"]["path"], "_original_nodal_runtime_only")
        helper.metadata_admit(manifest, inputs_root)
        require(not any(name in sys.modules for name in ("numpy", "flint", "scipy")),
                "the actual public worker and all input admission remain metadata only")
        cap, _ = capacity(head)
        require(cap["topic_blob_bytes"]+op["maximum_total_publication_bytes"]+RESERVE <= LIMIT,
                "whole topic room before the necessary carrier-only child")
        state["pre_execution_capacity"] = cap
        state["TC_original_complete_cells_retained"] = 992
        state["TC_new_scientific_targets_called"] = 0
        marker = {"kind": "consumed_R149_original_nodal_runtime_identification_v1",
            "problem_id": manifest["problem_id"], "manifest_sha256": args.manifest_sha,
            "run_id": run, "run_attempt": attempt, "prepared_utc": utc(), "output_directory": output_dir,
            "automatic_scientific_retry": False, "old_completed_targets_may_be_recomputed": False,
            "new_target_order": [], "untested_core_schedules": list(helper.SCHEDULES),
            "status": "only_original_carrier_identity_under_two_declared_untested_dispatches"}
        state["consumed_marker_publication"] = publish(
            lambda: {marker_path: encode(marker)}, "visible-exact: reserve original carrier runtime identification", True)
        materialize_current(pull())
        next_pull = time.monotonic()+1800
        def progress(value):
            nonlocal result, staged, next_pull
            result = parse(encode(value))
            result.update(run_id=run, run_attempt=attempt, input_manifest_sha256=args.manifest_sha)
            raw = encode(result)
            require(0 < len(raw) <= op["maximum_actual_bytes"], "whole actual runtime/carrier evidence budget")
            atomic(output/"actual-original-nodal-runtime.json", raw)
            staged = {output_dir+"/actual-original-nodal-runtime.json": raw}
            state["input_only_files"] = [{"path": p, "bytes": len(b), "sha256": sha(b)}
                                          for p, b in staged.items()]
            state["necessary_input_reconstruction_children"] = value["necessary_input_reconstruction_children"]
            state["accepted_original_carrier_schedule"] = value["accepted_schedule"]
            print("INPUT-ONLY ORIGINAL CARRIER PROGRESS "+encode({
                "complete": value["complete"], "accepted_schedule": value["accepted_schedule"],
                "schedule_results": [{k: v for k, v in row.items() if k in (
                    "OPENBLAS_CORETYPE", "actual_returncode", "complete", "reason")}
                    for row in value["schedule_results"]],
                "necessary_input_children": value["necessary_input_reconstruction_children"],
                "TC_scientific_children": 0, "TC_retained_complete_cells": 992}).decode(), end="", flush=True)
            if time.monotonic() >= next_pull:
                pull()
                next_pull = time.monotonic()+1800
        helper.run_fixed_schedules(manifest, inputs_root, temporary, progress)
        require(result is not None and result["complete"] is result["proved"] is True
                and result["failure"] is None and result["TC_scientific_children"] == 0
                and result["new_TC_integrated_cells"] == 0,
                "the original whole carrier identity was not recovered by either declared unused schedule")
        materialize_current(pull())
        state["complete"] = True
    except BaseException as exc:
        trace = traceback.format_exc()
        print(trace, flush=True)
        state["failure"] = {"type": type(exc).__name__, "message": str(exc)[:2000],
                            "traceback": trace[-6000:], "whole_trace_in_job_log": True}
    state["finished_utc"] = utc()
    for path, raw in staged.items():
        emit(path, raw)
    try:
        published = publish(final_files, "visible-exact: preserve whole original carrier runtime outcome")
        print("Published exact complete input-only outcome "+published["commit"], flush=True)
    except BaseException:
        traceback.print_exc()
        for path, raw in final_files().items():
            emit(path, raw)
        raise
    if not state["complete"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
'''


def patched_source():
    raw = Path(__file__).with_name(BASE_NAME).read_bytes()
    if len(raw) != BASE_BYTES or hashlib.sha256(raw).hexdigest() != BASE_SHA256:
        raise ValueError("the complete original metadata publication engine changed")
    source = raw.decode()
    before_rows = source.index("    def restore_rows():\n")
    publish_start = source.index("    def publish(factory, message, before_science=False):\n")
    pipeline_start = source.index("\n\n    try:\n        head = pull()\n", publish_start)
    source = source[:before_rows]+FINAL_FILES+source[publish_start:pipeline_start]+PIPELINE
    replacements = [
        ('OWNER = TOPIC+"/scripts/fourfold_codazzi_true_root_trial_owner.py"',
         'OWNER = TOPIC+"/scripts/fourfold_codazzi_original_nodal_runtime_identification.py"'),
        ('WORKER = TOPIC+"/scripts/fourfold_codazzi_true_root_trial_public_worker.py"',
         'WORKER = TOPIC+"/scripts/fourfold_codazzi_original_nodal_runtime_public_worker.py"'),
        ('TARGETS = ["complete_signed_finite_trial_matrices_and_waist96",\n'
         '           "complete_negative_finite_trial_sources96",\n'
         '           "complete_positive_finite_trial_sources96"]', 'TARGETS = []'),
        ('"R149_true_root_finite_trial_complete_inputs_v1"', '"R149_original_nodal_runtime_identification_inputs_v1"'),
        ('"R149_complete_true_root_finite_trial_residuals_v1"', '"R149_input_only_original_nodal_runtime_identification_v1"'),
        ('"true_root_finite_trial_residuals"', '"original_nodal_runtime_identification"'),
        ('"R149_complete_true_root_finite_trial_execution_v1"', '"R149_original_nodal_runtime_identification_execution_v1"'),
        ('op["maximum_total_publication_bytes"] == 170000', 'op["maximum_total_publication_bytes"] == 90000'),
        ('old_numerical_producers_called=0,old_completed_targets_recomputed=0,',
         'old_completed_scientific_targets_called=0,old_completed_targets_recomputed=0,'),
    ]
    for old, new in replacements:
        if source.count(old) != 1:
            raise ValueError("the exact input-only metadata adaptation did not match: "+old)
        source = source.replace(old, new)
    if "def capture(" in source or "reconstruct_direction()" in source or "owner.preflight(" in source:
        raise ValueError("a TC scientific/restoration pipeline remained in the input-only entry")
    return source


exec(compile(patched_source(), __file__, "exec"), globals())
