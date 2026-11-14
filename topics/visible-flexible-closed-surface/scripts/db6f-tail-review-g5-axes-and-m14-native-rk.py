#!/usr/bin/env python3
"""Independent read-only provenance/parameter audit of the G5 axes note.

This program reads frozen JSON/gzip/source files only. It imports no project
module, constructs no solver/flow, and does not evaluate saved state arrays.
The exact-rational index check below is a proof of same-stage warm copying,
not a run of remeshCheckpoint or a future M14 candidate.
"""
import argparse
import ast
import gzip
import hashlib
import json
from fractions import Fraction
from pathlib import Path


HERE = Path(__file__).resolve().parent
TOPIC = HERE.parent
NOTES = TOPIC / "notes"
STEM = "2026-11-09-db6f-prefix-g5-axes-and-m14-native-rk"
NOTE_SHA = "2b24b749be6351e6906e268bacc03d3412dccb7d58d192880495e40c976f54c8"
PUBLICATION_SHA = "c0c54cf74f0946dae82a75a09080a59b201a14b38a915aacf085051c9e1afbdc"
PHYSICAL_SHA = "811e8cdccbad6edd4c487afc8ec07c16d519995cd9c5b182bc79ab327f414071"
SIX = ["frozen_profile", "chart", "warp_reference_q", "physical_port_sha256",
       "physical_tail_parameters", "physical_tail_cut"]


def require(value, message):
    if not value:
        raise AssertionError(message)


def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":"),
                      allow_nan=False, ensure_ascii=False)


def same(left, right, message):
    require(canonical(left) == canonical(right), message)


def read(path):
    path = Path(path)
    raw = path.read_bytes()
    if path.suffix == ".gz":
        raw = gzip.decompress(raw)
    return json.loads(raw)


def identity(path):
    path = Path(path).resolve()
    raw = path.read_bytes()
    return {"path": str(path), "bytes": len(raw),
            "sha256": hashlib.sha256(raw).hexdigest()}


def verified(row):
    actual = identity(row["path"])
    same(actual, {k: row[k] for k in actual}, "Frozen source identity differs")
    return actual


def static_fragment(path, fragments):
    text = Path(path).read_text()
    for fragment in fragments:
        require(fragment in text, "Missing manually-reviewed source fragment in " + Path(path).name)
    return {"file": identity(path), "fragment_count": len(fragments)}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    require(args.out.resolve().parent == NOTES, "Report must remain in this topic's notes")
    require(not args.out.exists(), "Refuse to overwrite a report")

    note = NOTES / (STEM + ".md")
    pub_path = NOTES / (STEM + "-publication.json")
    require(identity(note)["sha256"] == NOTE_SHA, "Reviewed note changed")
    require(identity(pub_path)["sha256"] == PUBLICATION_SHA, "Author publication changed")
    pub = read(pub_path)
    require(pub["file_count"] == len(pub["files"]) == 3, "Wrong author publication extent")
    author_files = [verified(row) for row in pub["files"]]
    require(sum(row["bytes"] for row in author_files) == pub["total_bytes"] == 32190,
            "Author byte count differs")
    ledger_path = NOTES / (STEM + "-sources.json")
    ledger = read(ledger_path)
    require(ledger["count"] == len(ledger["bindings"]) == 30, "Wrong source ledger extent")
    require(len({row["path"] for row in ledger["bindings"]}) == 30, "Duplicate source")
    bindings = [verified(row) for row in ledger["bindings"]]
    verified(ledger["metadata"])
    metadata = read(ledger["metadata"]["path"])
    same(metadata["six_frozen_fields"], SIX, "Wrong six-field scope")

    sequence_path = NOTES / "2026-11-09-db6f-tail-g5-closed-sequence-inputs.json"
    sequence = read(sequence_path)
    require(len(sequence["rows"]) == 6, "Wrong existing G5 sequence size")
    require(sequence["physical_definition_canonical_sha256"] == PHYSICAL_SHA,
            "Original frozen definition differs")
    by_checkpoint = {Path(row["checkpoint"]).name: row for row in sequence["rows"]}

    extracted = []
    expected_steps = (32, 64, 128)
    expected_nodes = (778, 2570, 2570)
    expected_residual = (1.3505653752886372e-10, 1.872382418274325e-10,
                         8.191673022591901e-11)
    common_physical = None
    for i, row in enumerate(metadata["historical_rows"]):
        cp_id, tail_id = verified(row["checkpoint"]), verified(row["final_tail"])
        cp, packet = read(cp_id["path"]), read(tail_id["path"])
        seq = by_checkpoint[Path(cp_id["path"]).name]
        require(cp_id["sha256"] == seq["checkpoint_sha256"] and
                tail_id["sha256"] == seq["tail_final_record_sha256"],
                "History does not match the original G5 table")
        same(cp["tail_seam"]["tail_record"], Path(tail_id["path"]).name,
             "Not the checkpoint's own final tail")
        same(cp["tail_config"], packet["config"], "Tail response config differs")
        require(cp["solver_success"] is True and cp["config"]["actual_nonlinear_tail"] is True,
                "Historical CP is not marked as a successful true-tail solve")
        response = packet["response"]
        require(response["converged"] is True and "failed" not in response,
                "Historical final response failed")
        require(packet["request"]["jacobian"] is True and packet["request"]["audit"] is True,
                "Historical final response is not Jac/audit")
        require(response["residual"] == expected_residual[i] == seq["tail_residual"],
                "Historical residual differs")
        same(cp["tail_seam"]["tail_jets"], response["jets"], "Saved seam jets differ")
        same(cp["tail_seam"]["tail_shooting_residual"], response["residual"],
             "Saved seam residual differs")
        cfg, par = cp["tail_config"], response["checkpoint"]["parameters"]
        require(cp["nodes"] == expected_nodes[i] == row["prefix_nodes"], "Historical mesh count differs")
        require(cp["config"]["fixed_metric"] is (i != 0), "Design/fixed-g distinction lost")
        require(cp["config"]["tol"] == (2e-7 if i == 0 else 2e-9), "Historical prefix tol differs")
        for key, value in {"modes": 8, "spacing": 3, "depth": 10, "shootingParts": 2,
                           "steps": expected_steps[i], "auditSteps": expected_steps[i],
                           "quadrature": 256, "linearFar": 32, "linearSteps": 256,
                           "solveTolerance": 2e-9, "maxIterations": 30 if i == 0 else 36,
                           "calibrationSteps": 512}.items():
            same(cfg[key], value, "Historical tail setting differs: " + key)
        for key, value in {"physicalDepth": 10, "depth": 180, "shootingParts": 2,
                           "steps": expected_steps[i], "auditSteps": expected_steps[i],
                           "quadrature": 256, "linearFar": 32, "linearSteps": 256,
                           "projectionFloor": 0.05}.items():
            same(par[key], value, "Historical resolved parameter differs: " + key)
        for key in ("prefix_config", "tail_config", "resolved_parameters"):
            actual = cp["config"] if key == "prefix_config" else cfg if key == "tail_config" else par
            same(row[key], {k: actual[k] for k in row[key]}, "Author extracted historical field differs")
        require(row["base_RK_intervals_per_raw_profile"] == 2 * expected_steps[i], "Wrong base RK count")
        physical = {k: cp[k] for k in SIX}
        phash = hashlib.sha256(canonical(physical).encode()).hexdigest()
        require(phash == PHYSICAL_SHA == row["frozen_six_fields_canonical_sha256"],
                "Six physical fields differ")
        if common_physical is None:
            common_physical = physical
        same(common_physical, physical, "Historical common-g dictionary differs")
        require(row["tail_residual"] == response["residual"] and
                row["tail_converged"] is True and row["final_jacobian"] is True and
                row["final_audit"] is True, "Author historical success metadata differs")
        extracted.append({"checkpoint": cp_id, "own_final_tail": tail_id,
                          "native_steps": cfg["steps"], "parts": cfg["shootingParts"],
                          "tail_angular": cfg["quadrature"], "base_intervals": 2 * cfg["steps"],
                          "prefix_nodes": cp["nodes"], "prefix_tol": cp["config"]["tol"],
                          "fixed_from_start": cp["config"]["fixed_metric"],
                          "final_residual": response["residual"]})
    require(len(extracted) == 3, "Wrong historical row count")

    launch_id = verified(metadata["current_launch"])
    config_id = verified(metadata["current_config"])
    seed_id = verified(metadata["current_source_checkpoint"])
    launch, config, seed = read(launch_id["path"]), read(config_id["path"]), read(seed_id["path"])
    same(launch["source_checkpoint"], seed_id, "Launch seed differs")
    same(launch["tail_config"], config_id, "Launch config differs")
    same(launch["settings"], metadata["current_input_settings"], "Current numerical settings differ")
    current_bound = [verified(row) for row in launch["bindings"]]
    require(len(current_bound) == 106 and len({x["path"] for x in current_bound}) == 106,
            "Current frozen input graph differs")
    same({k: seed[k] for k in SIX}, common_physical, "Current M14 seed changes fixed g")
    for key, value in {"modes": 14, "spacing": 3, "depth": 12, "shootingParts": 8,
                       "steps": 32, "auditSteps": 32, "quadrature": 512, "linearFar": 32,
                       "linearSteps": 256, "solveTolerance": 2e-9, "maxIterations": 36,
                       "calibrationSteps": 512, "warpSteps": 16}.items():
        same(config[key], value, "Current original setting differs: " + key)
    same(metadata["current_tail_numerical_parameters"],
         {k: config[k] for k in metadata["current_tail_numerical_parameters"]},
         "Author current extracted fields differ")
    require(config.get("correctInitialBoundary", True) is True, "Boundary warm correction disabled")
    require(config.get("projectionFloor", 0.05) == 0.05, "Projection floor changed")
    same(launch["weights"], [1.0] + [float(1 << (9*j*j).bit_length())
                                   for _ in range(3) for j in range(1, 15)], "Current W14 differs")
    warm_id = verified(launch["own_actual_tail_warm"])
    require(config["initialCheckpoint"] == warm_id["path"], "Warm file is not own source final tail")
    warm = read(warm_id["path"])["response"]["checkpoint"]
    require(warm["parameters"]["modes"] == 14 and warm["parameters"]["physicalDepth"] == 12
            and warm["parameters"]["depth"] == 864 and warm["parameters"]["shootingParts"] == 8,
            "Current stage geometry differs")
    require(len(warm["states"]) == 865 and all(len(x) == 28 for x in warm["states"]),
            "Current staged shape differs")
    same(warm["rawNode"], list(range(0, 865, 72)), "Current raw layout differs")
    require(len(warm["rawStates"]) == 13, "Current raw state count differs")

    # With P fixed, all new stage endpoints are old endpoints. Verify the
    # exact branch index (including reversed profile/stage ordering) for all
    # 865 states; no floating profile or RK evaluation occurs.
    old_parts = new_parts = 8
    J, depth = 9, 12
    copies = {}
    for n in range(depth + 1):
        copies[n * J * new_parts] = n * J * old_parts
    layout = [(j, Fraction(k, new_parts)) for j in range(J-1, -1, -1)
              for k in range(new_parts-1, -1, -1)]
    for n in range(depth):
        for i in range(1, J * new_parts):
            j, raw_left = layout[i-1]
            z = raw_left * old_parts
            require(z.denominator == 1, "Warm endpoint would use interpolation")
            source = n * J * old_parts + (J-1-j)*old_parts + old_parts-int(z)
            copies[n * J * new_parts+i] = source
    require(copies == {i: i for i in range(865)}, "Same-stage copy is not exact identity")
    radial_grids = []
    for small, large in ((32, 64), (64, 128)):
        a = {Fraction(k, 8*small) for k in range(8*small+1)}
        b = {Fraction(k, 8*large) for k in range(8*large+1)}
        require(a <= b and max(b) == 1 and min(b) == 0, "Base RK grid not nested")
        radial_grids.append({"small_steps": small, "large_steps": large,
                             "small_base_intervals": 8*small, "large_base_intervals": 8*large,
                             "exact_uniform_grid_inclusion": True,
                             "same_breakpoint_union_preserves_inclusion": True})

    # Anchors for the manually read call paths. These do not replace the
    # semantic review, and do not import or execute the functions.
    S = HERE
    R = TOPIC / "repro/source-root/topics/large-amplitude-twist-flex/scripts"
    static = [
        static_fragment(S / "950f-tail-subdivision.mjs", [
            "a=k/parts,b=(k+1)/parts,h=b-a", "drdx:h*g.drdx,dlogwdx:h*g.dlogwdx",
            "profile.integrationBreakpoints=(base.integrationBreakpoints??[])",
            "buildStableStageGraphs(physical,stages,{modes,spacing,linearFar,linearSteps})"]),
        static_fragment(R / "f6tail_cusp_grid.mjs", [
            "export function splitIntegrationInterval", "export function integrationGrid",
            "const grid=splitIntegrationInterval(x,x+h,profile.integrationBreakpoints)"]),
        static_fragment(R / "f6tail_fast_split_flux_engine.mjs", [
            "steps=opts.stepsPerSegment??64", "integrationGrid(steps,cuts)"]),
        static_fragment(S / "db6f-prefix-tail-shared-core.mjs", [
            "flowStateWithJacobian(s,c.profiles,{stepsPerSegment:steps})",
            "for(let k=0;k<steps;k++)state=c.engine.rk4(state,profile,k/steps,1/steps)",
            "audit:opts.audit?audit(sol,opts.auditSteps??tail.parameters.steps):null",
            "buildStableStageGraphs(physical,stages,{modes:M,spacing,linearFar,linearSteps})"]),
        static_fragment(S / "950f-tail-warm-remesh.mjs", [
            "if(Math.abs(z-nearest)<1e-12){copy(prior.states[baseIndex+oldParts-nearest],states[i]);continue;}",
            "const oldParts=old.shootingParts,newParts=dn.tail.parameters.shootingParts"]),
        static_fragment(S / "closing_recalibrated_tail.mjs", [
            "modes:1,depth:protectCell", "calibrationSteps,steps:1,quadrature:16"]),
        static_fragment(S / "db6f-prefix-tail-shared-client.py", [
            "self.calls=0;self.cache_key=None;self.cache_value=None", "and not audit and"]),
        static_fragment(S / "db6f-prefix-tail-shared-worker.mjs", [
            "const states=remeshCheckpoint(prior,dn,createFastSplitFluxMomentumTailEngine)",
            "if(initial&&cfg.correctInitialBoundary!==false)",
            "auditSteps:cfg.auditSteps??cfg.steps"]),
        static_fragment(S / "db6f-prefix-spectral-true-m14.py", [
            "'shootingParts': 8, 'steps': 32, 'auditSteps': 32",
            "equal(cfg, expected_config(reference, out)", "runner.solve_bvp = selected"]),
        static_fragment(S / "db6f-prefix-audit-spectral-true-m14.py", [
            "equal(c.without_io(cp['parameters']), c.without_io(context['prior']['response']['checkpoint']['parameters'])",
            "equal(seam['angular_samples'], 896"]),
        static_fragment(S / "db6f-prefix-coupled.py", [
            "for outer in range(8):", "n=max(512,64*self.M)"]),
    ]
    tree = ast.parse((S / "db6f-prefix-spectral-true-m14.py").read_text())
    assignments = {x.targets[0].id: x.value for x in tree.body
                   if isinstance(x, ast.Assign) and len(x.targets) == 1 and isinstance(x.targets[0], ast.Name)}
    same(ast.literal_eval(assignments["SETTINGS"]), launch["settings"], "Selector SETTINGS differs")
    require(ast.literal_eval(assignments["IO_FIELDS"]) == {
        "initialCheckpoint", "traceFile", "iterationCheckpointFile", "trialDiagnosticFile", "trialStatePrefix"},
        "Parameters comparison excludes unapproved numerical fields")

    report = {
        "status": "PASS_READ_ONLY_G5_AXES_AND_CONDITIONAL_M14_INTERFACE",
        "scope": "Exact frozen-file identity, independent JSON field extraction, source call-path review, and rational stage indices only. No historical solver rerun or future candidate.",
        "checker": identity(__file__), "reviewed_note": identity(note),
        "author_publication": identity(pub_path), "author_files": author_files,
        "source_ledger": identity(ledger_path), "source_bindings_rechecked": len(bindings),
        "current_launch_bindings_rechecked": len(current_bound),
        "original_G5_sequence": identity(sequence_path),
        "physical_definition_sha256": PHYSICAL_SHA, "historical_rows": extracted,
        "current_launch": launch_id, "current_config": config_id, "current_seed": seed_id,
        "current_own_final_warm": warm_id, "same_stage_copies_checked": len(copies),
        "rational_RK_grid_checks": radial_grids, "source_semantic_anchors": static,
        "old_G5_notes_require_erratum": False, "new_G5_gate_created": False,
        "current_run_result_inferred": False, "future_candidate_created": False,
        "historical_solvers_rerun": False, "solver_calls": 0, "BVP_calls": 0,
        "DN_calls": 0, "flow_calls": 0, "RK_calls": 0,
        "active_result_files_read": False, "git_mutations": 0,
    }
    data = (json.dumps(report, indent=2, ensure_ascii=False, allow_nan=False) + "\n").encode()
    require(len(data) < 100_000, "Report too large")
    with args.out.open("xb") as handle:
        handle.write(data)
    print(json.dumps({"status": report["status"], "report": identity(args.out),
                      "source_bindings": 30, "launch_bindings": 106,
                      "historical_rows": 3, "same_stage_copies": 865, "solver_calls": 0}))


if __name__ == "__main__":
    main()
