#!/usr/bin/env python3
"""Independent complete128 primal experiment around the original full native loop.

Request113 does not replace the original64 residual, direction producer,
32-by10 native iteration, final Jacobian or audit.  It observes the same fresh
first R273 delta with two explicit binary128 root stopping configurations.
All scientific execution is restricted to the public repository Actions.
"""
from __future__ import annotations
import argparse
import ast
import hashlib
import json
import os
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
FROZEN103 = "geometry_20261115_native_noj_neighbor_current576_solve.py"
FROZEN103_SHA = "c8c072e0d65567ba86e9fb72d3708ef5771c8b4ee475e9fcec611371cd447c79"
BRIDGE = "geometry_20261115_native_primal128_bridge.mjs"
BRIDGE_SHA = "3655c81a5771deaa26a0d22b8fc4bbbead0302cd06983ddd4f5d12eded44ebe8"
CPP = "geometry_20261115_native_primal128.cpp"
CPP_SHA = "1b59cd1059c147f3fedf28a663fed25049c80a42d782838506aba4a7b7df591d"
DRIVER = Path(__file__).name


def digest(raw):
    return hashlib.sha256(raw).hexdigest()


def file_sha(file):
    h = hashlib.sha256()
    with Path(file).open("rb") as stream:
        for block in iter(lambda: stream.read(1 << 20), b""):
            h.update(block)
    return h.hexdigest()


def once(text, before, after):
    if text.count(before) != 1:
        raise ValueError("Unique frozen source anchor required: " + repr(before[:140]))
    return text.replace(before, after, 1)


def derived_scope():
    raw = (HERE / FROZEN103).read_bytes()
    if digest(raw) != FROZEN103_SHA:
        raise ValueError("The original103 temporary-lifecycle driver changed")
    for name, expected in ((BRIDGE, BRIDGE_SHA), (CPP, CPP_SHA)):
        if file_sha(HERE / name) != expected:
            raise ValueError("Independent113 source changed: " + name)
    source = raw.decode()
    # Producer/runtime names only.  Frozen95 sources, R273 mathematics and
    # the exact original nonlinear solve/evaluate/trial source are retained.
    source = source.replace("geometry_20261115_native_noj_neighbor_current576_solve.py", DRIVER)
    source = source.replace("geometry_20261115_native_noj_neighbor_current576_solve_hook.mjs",
                            "geometry_20261115_native_primal128_current576_probe_hook.mjs")
    source = source.replace("exact_20261115_native_noj_neighbor_current576_",
                            "exact_20261115_native_primal128_current576_")
    source = source.replace("geometry_20261115_native_noj_neighbor_proposal.mjs", BRIDGE)
    source = source.replace("436cfde61ed98720f0e0802978dc4874c42eb42a0193e426b5c5e9e3e0261037", BRIDGE_SHA)
    source = source.replace("native-noj-neighbor-current576", "native-primal128-current576")
    source = source.replace("noj-neighbor-current-native576", "primal128-current-native576")
    source = source.replace("VISIBLE_FLEX_NATIVE_NOJ_NEIGHBOR_CURRENT576_SOLVE_SPEC",
                            "VISIBLE_FLEX_NATIVE_PRIMAL128_CURRENT576_SOLVE_SPEC")
    source = source.replace("native103", "native113").replace("NATIVE103", "NATIVE113")
    source = source.replace("request103", "request113").replace("Request103", "Request113")
    source = source.replace("_103_watch", "_113_watch")
    source = source.replace("noJ-neighbor-original-loop", "binary128-experiment-original-loop")
    source = source.replace('"proposal_full_noJ_evaluations_maximum": 3',
                            '"proposal_full_noJ_evaluations_maximum": 0, "binary128_configurations": 2, "binary128_states_per_configuration": 11')
    scope = {"__name__": "_native113_original_lifecycle", "__file__": str(HERE / DRIVER)}
    exec(compile(source, str(HERE / DRIVER), "exec"), scope)
    original_factory = scope["prepared_sources"]

    def prepared_sources():
        generated, driver, generation = original_factory()
        hook_name = "geometry_20261115_native_primal128_current576_probe_hook.mjs"
        hook = generated[hook_name].replace("emit103", "emit113")
        hook = hook.replace("// Request113 derived hook. Original full noJ evaluates base and two adjacent words.\n"
                            "// Only a strictly decreasing proposal reaches the unchanged original ten trials.\n"
                            "// Otherwise this same fresh J goes directly to complete R273; raw files are temporary.\n",
                            "// Request113: same fresh R273 delta; independent complete128 primal experiment.\n"
                            "// The original64 nonlinear loop, ten trials, final J and audit remain unchanged.\n")
        hook = once(hook, "import {proposeNeighbors} from './" + BRIDGE + "';",
                    "import {runPrimal128Experiment} from './" + BRIDGE + "';\n"
                    "let native113SplitIntegrationInterval=null,native113CuspAwareFlow=null;")
        import_anchor = "  {splitIntegrationInterval}=await import(pathToFileURL(cuspPath));"
        hook = once(hook, import_anchor, import_anchor + "\n native113SplitIntegrationInterval=splitIntegrationInterval;native113CuspAwareFlow=cfg.cuspAwareFlow===true;")
        start = hook.index("   if(it===0){\n    const proposed=proposeNeighbors(")
        end = hook.index("   if(answer===null){", start)
        hook = hook[:start] + "   // No adjacent-word proposal.  The same fresh full R273 direction is used.\n" + hook[end:]
        anchor = "   record.direction=directionRecord;record.linear_direction_returned=true;directions++;"
        hook = once(hook, anchor, anchor + """
   if(it===0){
    try{
     record.primal128=runPrimal128Experiment(installedDN,args,answer.delta,native113SplitIntegrationInterval,{
      source_sha256:spec.source_sha256,hook_sha256:fileSHA(selfPath),native_call:call,
      original_cuspAwareFlow:native113CuspAwareFlow,
      nonlinear_iteration:it,fresh_snapshot_result_sha256:snapshot.result.sha256,
      complete_current_array_sha256:snapshot.raw_array_sha256,
      original_current_norm:record.source_current_withJ_norm,
      complete_current_delta_sha256:answer.delta_receipt.sha256},emit113);
    }catch(error){
     record.primal128={experiment_error:cleanError(error),native_accepted:false,
      original_correction_and_native_acceptance_not_replaced:true};
     emit113({event:'native113_experiment_observer_error',...record.primal128});
    }
   }
""".rstrip())
        hook = hook.replace("first_neighbor_only_at_iteration0:true,additional_noJ_proposal_full_calls_maximum:3,original_trial_body_unchanged:true",
                            "first_neighbor_proposal_disabled:true,independent_binary128_experiment_only_at_iteration0:true,original_trial_body_unchanged:true")
        generated[hook_name] = hook
        generation["derived_source_sha256"][hook_name] = digest(hook.encode())
        generation["hook_sha256"] = digest(hook.encode())
        generation["original103_driver_sha256"] = FROZEN103_SHA
        generation["primal128_bridge_sha256"] = BRIDGE_SHA
        generation["primal128_cpp_source_sha256"] = CPP_SHA
        generation["source_changes_are_first_proposal_identities_and_temporary_retention_only"] = False
        generation["independent_complete_primal_experiment_added_after_same_fresh_R273"] = True
        generation["original64_native_root_RHS_RK_evaluate_and_ten_trial_body_retained"] = True
        generation["original64_J_not_claimed_exact_derivative_of_binary128_primal"] = True
        # The generated full driver hashes its actual hook file at launch;
        # no obsolete precomputed hook SHA is left in its source.
        generation["executed_derived_driver_sha256"] = digest(driver.encode())
        for name, text in generated.items():
            if name.endswith(".py"):
                ast.parse(text, filename=name)
        ast.parse(driver, filename=DRIVER)
        return generated, driver, generation

    scope["prepared_sources"] = prepared_sources
    return scope


def main():
    if os.environ.get("GITHUB_ACTIONS") != "true" or os.environ.get("GITHUB_REPOSITORY", "").lower() != "rogerhu12/math-research-public":
        raise RuntimeError("Scientific execution only in the public repository Actions")
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument("--quad-executable", type=Path, required=True)
    parser.add_argument("--quad-budget-seconds", type=int, default=7200)
    parser.add_argument("--quad-threads", type=int, default=2)
    args, remaining = parser.parse_known_args()
    executable = args.quad_executable.resolve()
    temp = Path(os.environ["RUNNER_TEMP"]).resolve()
    if not executable.is_file() or not executable.is_relative_to(temp) or executable.is_symlink():
        raise ValueError("Use the compiled executable in this run's temporary directory")
    if not 60 <= args.quad_budget_seconds <= 14400 or not 1 <= args.quad_threads <= 4:
        raise ValueError("Explicit independent primal experiment budget/threads required")
    os.environ.update(VISIBLE_FLEX_PRIMAL128_EXECUTABLE=str(executable),
                      VISIBLE_FLEX_PRIMAL128_EXECUTABLE_SHA256=file_sha(executable),
                      VISIBLE_FLEX_PRIMAL128_CPP_SHA256=CPP_SHA,
                      VISIBLE_FLEX_PRIMAL128_SECONDS=str(args.quad_budget_seconds),
                      VISIBLE_FLEX_PRIMAL128_THREADS=str(args.quad_threads))
    print(json.dumps(dict(event="native113_experiment_setup", source_sha256=file_sha(__file__),
                         original103_source_sha256=FROZEN103_SHA, cpp_source_sha256=CPP_SHA,
                         bridge_source_sha256=BRIDGE_SHA, executable_sha256=file_sha(executable),
                         binary128_budget_seconds=args.quad_budget_seconds, threads=args.quad_threads,
                         original_native_max_iterations=32, original_native_trials=10,
                         original_native_tolerance=2e-9, native_accepted=False,
                         new_binary128_final_J_or_audit=False,
                         raw_publication=False), separators=(",", ":")), flush=True)
    previous_argv = sys.argv
    try:
        sys.argv = [str(HERE / DRIVER), *remaining]
        scope = derived_scope()
        return int(scope["main"]())
    finally:
        sys.argv = previous_argv


if __name__ == "__main__":
    raise SystemExit(main())
