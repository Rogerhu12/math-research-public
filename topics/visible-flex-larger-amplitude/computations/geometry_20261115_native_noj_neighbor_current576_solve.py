#!/usr/bin/env python3
"""Request103: original noJ neighbor proposal, then the unchanged full R273 loop.

Only public Actions runs science. Old95 sources remain untouched. Three small
runtime sources are generated from exact old bytes; only producer identities,
the first proposal and temporary-output lifetime change. No data artifact is
uploaded by this entry. Full arrays needed by the old QR remain runner-local
until that correction is consumed, then are removed. Scalars and hashes are
printed; failed95 is never an accepted anchor.
"""
from __future__ import annotations
import argparse
import gzip
import hashlib
import json
import math
import os
from pathlib import Path
import shutil
import sys
import threading
import time
import traceback

HERE = Path(__file__).resolve().parent
DRIVER = "geometry_20261115_native_noj_neighbor_current576_solve.py"
PROPOSAL = "geometry_20261115_native_noj_neighbor_proposal.mjs"
PROPOSAL_SHA = "436cfde61ed98720f0e0802978dc4874c42eb42a0193e426b5c5e9e3e0261037"
OLD = {
 "geometry_20261115_native_word_first_current576_solve.py":
 "69c9a8d5cccfcfdcdda35c475b089609c789747803a7b363a17fb67c5bae28d0",
 "geometry_20261115_native_word_first_current576_solve_hook.mjs":
 "932961ef9f267f95f5de6bb28791ed43ef2c66d15b18b55823bc3f2384545bc3",
 "exact_20261115_native_word_first_current576_system.py":
 "2c6c012d9f2306f2ac13d240510eb8086b74d2b60ff318aa9e359dd72c05a3a8",
 "exact_20261115_native_word_first_current576_chain_qr.py":
 "4c887fbb4a16e0d2219969043e708c2d49c446f0ac75ba1dc3e6e17f7d2ee314",
}
NAMES = {
 "geometry_20261115_native_word_first_current576_solve.py": DRIVER,
 "geometry_20261115_native_word_first_current576_solve_hook.mjs":
 "geometry_20261115_native_noj_neighbor_current576_solve_hook.mjs",
 "exact_20261115_native_word_first_current576_system.py":
 "exact_20261115_native_noj_neighbor_current576_system.py",
 "exact_20261115_native_word_first_current576_chain_qr.py":
 "exact_20261115_native_noj_neighbor_current576_chain_qr.py",
}
THREADS = []
STOP = threading.Event()


def sha_bytes(raw):
 return hashlib.sha256(raw).hexdigest()


def sha_file(path):
 h = hashlib.sha256()
 with Path(path).open("rb") as stream:
  for block in iter(lambda: stream.read(1 << 20), b""):
   h.update(block)
 return h.hexdigest()


def emit(event, **values):
 print(json.dumps(dict(event=event, **values), ensure_ascii=False, allow_nan=False,
                  separators=(",", ":")), flush=True)


def read(path):
 raw = Path(path).read_bytes()
 return json.loads(gzip.decompress(raw) if raw[:2] == b"\x1f\x8b" else raw)


def change(text, old, new):
 if text.count(old) != 1:
  raise ValueError("A unique frozen source anchor is required: " + repr(old[:100]))
 return text.replace(old, new, 1)


def wire(text):
 for old, new in NAMES.items():
  text = text.replace(old, new)
 return (text.replace("native-word-first-current576", "native-noj-neighbor-current576")
         .replace("word-first-current-native576", "noj-neighbor-current-native576")
         .replace("VISIBLE_FLEX_NATIVE_WORD_FIRST_CURRENT576_SOLVE_SPEC",
                  "VISIBLE_FLEX_NATIVE_NOJ_NEIGHBOR_CURRENT576_SOLVE_SPEC")
         .replace("all_original_payloads_artifact_only", "all_original_payloads_runner_temporary_only")
         .replace("all_arrays_artifact_only", "all_arrays_runner_temporary_only"))


def prepared_sources():
 source = {}
 for name, digest in OLD.items():
  raw = (HERE / name).read_bytes()
  if sha_bytes(raw) != digest:
   raise ValueError("Frozen source changed: " + name)
  source[name] = raw.decode("utf-8")
 if sha_file(HERE / PROPOSAL) != PROPOSAL_SHA:
  raise ValueError("Independent real-noJ proposal source changed.")
 system_name = "exact_20261115_native_word_first_current576_system.py"
 qr_name = "exact_20261115_native_word_first_current576_chain_qr.py"
 hook_name = "geometry_20261115_native_word_first_current576_solve_hook.mjs"
 driver_name = "geometry_20261115_native_word_first_current576_solve.py"
 system = wire(source[system_name])
 system_sha = sha_bytes(system.encode())
 qr = change(wire(source[qr_name]), OLD[system_name], system_sha)
 qr_sha = sha_bytes(qr.encode())
 hook = wire(source[hook_name])
 hook = change(hook, "import {spawnSync} from 'node:child_process';",
     "import {spawnSync} from 'node:child_process';\n"
     "import {proposeNeighbors} from './" + PROPOSAL + "';\n"
     "const emit103=value=>process.stderr.write('NATIVE103 '+JSON.stringify(value)+'\\n');")
 # Remove the obsolete disk-based affine selector completely.
 start = hook.index("function checkedWordDirection(")
 stop = hook.index("let installedDN=null", start)
 hook = hook[:start] + hook[stop:]
 # Pass existing original closures through the one correction call only.
 hook = change(hook,
  ".correction({ev,states,target,scales,it,M,K,depth});'};",
  ".correction({ev,states,target,scales,it,M,K,depth,evaluate,cellFlow});'};")
 begin = hook.index("   if(it===0){\n    const wordDir=")
 end = hook.index("   if(answer===null){", begin)
 proposal_block = """   if(it===0){
    const proposed=proposeNeighbors(args,{
     source_sha256:spec.source_sha256,proposal_source_sha256:spec.word_candidate.source_sha256,
     hook_sha256:fileSHA(selfPath),native_call:call,nonlinear_iteration:it,
     snapshot_sequence:sequence,fresh_snapshot_result_sha256:snapshot.result.sha256
    },emit103);
    const resultReceipt=writeJSON(iterationDir,'real-noJ-neighbor-proposal.json',proposed.report);
    record.neighbor_proposal={selected:proposed.selected,result_sha256:resultReceipt.sha256,
     selected_label:proposed.report.selected_label,
     original_noJ_full_calls_started:proposed.report.original_noJ_full_calls_started,
     original_noJ_full_calls_completed:proposed.report.original_noJ_full_calls_completed,
     only_direction_proposal:true,original_ten_trials_still_required:true};
    if(proposed.selected)answer={selected:true,delta:proposed.delta,
     result_receipt:resultReceipt,input_binding:null,direction_checkpoint:null,array_manifest:null,
     delta_receipt:{shape:[577,224],bytes:577*224*8,sha256:proposed.report.delta_sha256,
      storage:'memory-only; not archived'},new_matrix_identity_sha256:null,
     negative_zero_count:proposed.negative_zero_count,direction_kind:'single-adjacent-input-word',
     complete_model_diagnostics_not_used_as_acceptance_gate:true};
   }
"""
 hook = hook[:begin] + proposal_block + hook[end:]
 # Preserve QR mathematics. Read a bounded scalar summary before removing
 # each correction's transient full snapshot/factor/direction output.
 hook = change(hook,
  "   answer.direction_kind='complete-R273-current576-QR';",
  """   answer.direction_kind='complete-R273-current576-QR';
   const qrReport=JSON.parse(unpack(fs.readFileSync(path.join(qrDir,'result.json.gz'))));
   const originalReadback=qrReport.original_exact_readback??{};
   record.QR_scalars={eta_cli_text:qrReport.eta_cli_text,eta_binary64:qrReport.eta_binary64,
    result_sha256:answer.result_receipt.sha256,factor_summary:qrReport.factor_summary,
    original_exact_norm:originalReadback.exact_global_original_sigma_norm,
    original_stored_base_exact_norm:originalReadback.exact_stored_base_sigma_norm,
    original_readback_rows:originalReadback.exact_rows,
    complete_raw_direction_sha256:answer.delta_receipt.sha256,
    actual_error:qrReport.actual_error??null};
""".rstrip())
 hook = change(hook,
  "   record.direction=directionRecord;record.linear_direction_returned=true;directions++;",
  """   record.direction=directionRecord;record.linear_direction_returned=true;directions++;
   emit103({event:'native103_original_correction_returned',native_call:call,nonlinear_iteration:it,
    source_sha256:spec.source_sha256,hook_sha256:fileSHA(selfPath),
    current_original_norm:record.source_current_withJ_norm,
    current_state_sha256:snapshot.current_state_sha256,
    complete_current_array_sha256:snapshot.raw_array_sha256,
    direction_kind:answer.direction_kind,delta_sha256:answer.delta_receipt.sha256,
    neighbor_proposal:record.neighbor_proposal??null,QR:record.QR_scalars??null,
    original_ten_noJ_trials_follow:true,native_accepted:false});
""".rstrip())
 hook = change(hook,
  "Current576 QR process failed; complete current snapshot and child logs retained",
  "Current576 QR process failed; compact child failure is printed before temporary cleanup")
 # Preserve a bounded actual child failure before raw cleanup, including
 # QR failures that occur before checkedCurrentDirection returns.
 hook = change(hook,
  "   record.actual_error=cleanError(error);actualFailure={native_call:call,nonlinear_iteration:it,snapshot_sequence:sequence,error:record.actual_error};",
  """   record.actual_error=cleanError(error);actualFailure={native_call:call,nonlinear_iteration:it,snapshot_sequence:sequence,error:record.actual_error};
   let childFailure=null,childStderr=null;
   const qrFailurePath=path.join(iterationDir,'qr','result.json.gz');
   if(fs.existsSync(qrFailurePath)){
    try{
     const child=JSON.parse(unpack(fs.readFileSync(qrFailurePath)));
     const message=String(child.actual_error??''),trace=String(child.actual_traceback??'');
     childFailure={result_sha256:fileSHA(qrFailurePath),
      diagnostic_completed:child.diagnostic_completed??null,
      linear_direction_computed:child.linear_direction_computed??null,
      actual_error:message.slice(0,3000),actual_error_sha256:sha(message),
      traceback_tail:trace.slice(-6000),traceback_sha256:sha(trace),
      factor_summary:child.factor_summary??null};
    }catch(readError){childFailure={report_read_error:cleanError(readError)};}
   }
   const stderrPath=path.join(iterationDir,'qr.stderr.log');
   if(fs.existsSync(stderrPath)){
    try{
     const size=fs.statSync(stderrPath).size,tail=Buffer.alloc(Math.min(6000,size));
     const fd=fs.openSync(stderrPath,'r');let count=0;
     try{count=fs.readSync(fd,tail,0,tail.length,Math.max(0,size-tail.length));}
     finally{fs.closeSync(fd);}
     childStderr={bytes:size,sha256:record.qr_exit?.stderr?.sha256??fileSHA(stderrPath),
      tail:tail.subarray(0,count).toString('utf8'),tail_only:true};
    }catch(readError){childStderr={read_error:cleanError(readError)};}
   }
   emit103({event:'native103_original_correction_failure',native_call:call,
    nonlinear_iteration:it,current_state_sha256:record.current_state_sha256??null,
    actual_error:record.actual_error,child:childFailure,child_stderr:childStderr,
    raw_payload_cleanup_follows_this_record:true,native_accepted:false});
""".rstrip())
 hook = change(hook,
  """   throw error;
  }
 }};
}""",
  """   throw error;
  }finally{
   // Only this newly created correction scratch tree is removed.
   // A cleanup failure is reported; it is not a nonlinear acceptance test.
   try{
    fs.rmSync(iterationDir,{recursive:true,force:true});
    record.temporary_correction_payload_removed=true;
   }catch(error){
    record.temporary_correction_payload_removed=false;
    emit103({event:'native103_temporary_cleanup_error',nonlinear_iteration:it,error:cleanError(error)});
   }
  }
 }};
}""")
 hook = hook.replace(
  "first_word_only_at_iteration0_with_no_extra_trial_or_iteration:true",
  "first_neighbor_only_at_iteration0:true,additional_noJ_proposal_full_calls_maximum:3,original_trial_body_unchanged:true")
 hook = hook.replace(
  "old_saved_model_used_separately_only_to_select_the_first_proposal:true",
  "old_saved_affine_model_not_used_for_neighbor_selection:true")
 hook = hook.replace(
  "old_saved_stage10_J_used_only_in_parent_complete_model_selector:true",
  "old_saved_stage10_J_used_only_in_legacy_parent_diagnostic:true")
 hook = ("// Request103 derived hook. Original full noJ evaluates base and two adjacent words.\n"
         "// Only a strictly decreasing proposal reaches the unchanged original ten trials.\n"
         "// Otherwise this same fresh J goes directly to complete R273; raw files are temporary.\n"
         + hook[hook.index("import fs from 'node:fs';"):])
 hook_sha = sha_bytes(hook.encode())
 driver = wire(source[driver_name])
 doc_start = driver.index('"""')
 doc_end = driver.index('"""', doc_start + 3) + 3
 driver = (driver[:doc_start] + '"""Runtime request103 driver: real-noJ first proposal, '
           'same-fresh-J R273 fallback, original native acceptance, temporary raw outputs only."""'
           + driver[doc_end:])
 driver = change(driver, OLD[system_name], system_sha)
 driver = change(driver, OLD[qr_name], qr_sha)
 driver = change(driver,
  'CANDIDATE_NAME = "exact_20261115_native_word_first_candidate.py"',
  'CANDIDATE_NAME = "' + PROPOSAL + '"')
 driver = change(driver,
  'CANDIDATE_SHA = "d9692107d197dcb4478fc2027beec21e3e611e67109af9d4b13ae09fb506e226"',
  'CANDIDATE_SHA = "' + PROPOSAL_SHA + '"')
 driver = driver.replace(
  "old_complete_model_predicted_strict_decrease=prior",
  "legacy_parent_affine_prediction_not_used_for_selection=prior")
 driver = driver.replace("same_fresh_snapshot_R273_fallback_if_not_model_selected",
                         "same_fresh_snapshot_R273_fallback_if_no_real_noJ_decrease")
 driver = driver.replace("old_saved_model_used_only_for_first_candidate_selection=True",
                         "old_saved_affine_model_not_used_for_neighbor_selection=True")
 driver = change(driver, "        return popen(actual, *args, **kwargs)",
  "        proc = popen(actual, *args, **kwargs)\n"
  "        _103_watch(proc, kwargs.get('stderr'))\n"
  "        return proc")
 generated = {
  NAMES[system_name]: system, NAMES[qr_name]: qr, NAMES[hook_name]: hook}
 for name, content in generated.items():
  if name.endswith(".py"):
   compile(content, str(HERE / name), "exec")
 compile(driver, str(HERE / DRIVER), "exec")
 return generated, driver, {
  "old_source_sha256": OLD, "proposal_source_sha256": PROPOSAL_SHA,
  "derived_source_sha256": {name: sha_bytes(text.encode()) for name, text in generated.items()},
  "executed_derived_driver_sha256": sha_bytes(driver.encode()),
  "unchanged_R273_factor_source_sha256":
   "9b951f9525966d243c602b304dc77d48c554afa2cc003eb65665f46f8db0ad33",
  "unchanged_exact_kernel_sha256":
   "0bc8f9782077bbae2fd4f10c4f085c00356caf5005d331b18fc4f4d949da378f",
  "hook_sha256": hook_sha,
  "source_changes_are_first_proposal_identities_and_temporary_retention_only": True,
 }


def watch(proc, stderr_stream):
 """Forward only our compact marker records; never dump protocol/raw data."""
 path = getattr(stderr_stream, "name", None)
 if not isinstance(path, str):
  raise ValueError("The original worker stderr file is required.")
 def follow():
  try:
   with open(path, "rb") as stream:
    pending = b""
    while True:
     block = stream.read(65536)
     if block:
      pending += block
      while b"\n" in pending:
       line, pending = pending.split(b"\n", 1)
       if line.startswith(b"NATIVE103 "):
        value = json.loads(line[len(b"NATIVE103 "):])
        emit("native103_worker_record", record=value)
     elif proc.poll() is not None or STOP.is_set():
      break
     else:
      STOP.wait(0.1)
    if pending.startswith(b"NATIVE103 "):
     emit("native103_worker_record", record=json.loads(pending[len(b"NATIVE103 "):]))
  except Exception as error:
   emit("native103_scalar_log_forwarding_error", error=repr(error),
        not_a_scientific_acceptance_gate=True)
 thread = threading.Thread(target=follow, daemon=True)
 THREADS.append(thread)
 thread.start()


def compact(value, depth=0):
 """Scalars and small objects only; arrays are described, never printed."""
 if value is None or isinstance(value, (bool, int)):
  return value
 if isinstance(value, float):
  return value if math.isfinite(value) else {"nonfinite_repr": repr(value)}
 if isinstance(value, str):
  if len(value) <= 1500:
   return value
  raw = value.encode()
  return {"text_bytes": len(raw), "sha256": sha_bytes(raw),
          "prefix": value[:500], "complete_text_not_printed": True}
 if isinstance(value, dict) and depth < 4:
  return {str(key): compact(item, depth + 1) for key, item in value.items()}
 raw = json.dumps(value, ensure_ascii=False, sort_keys=True,
                  separators=(",", ":"), allow_nan=False).encode()
 return {"type": type(value).__name__, "items": len(value),
         "canonical_json_bytes": len(raw), "canonical_json_sha256": sha_bytes(raw),
         "payload_not_printed_or_archived": True}


def main():
 if os.environ.get("GITHUB_ACTIONS") != "true" or os.environ.get("GITHUB_REPOSITORY", "").lower() != "rogerhu12/math-research-public":
  raise RuntimeError("Science runs only in this public repository Actions.")
 parser = argparse.ArgumentParser(description=__doc__)
 parser.add_argument("--original91-directory", type=Path, required=True)
 parser.add_argument("--source-topic", type=Path, required=True)
 parser.add_argument("--eta", default="1")
 parser.add_argument("--node-heap", type=int, default=6144)
 parser.add_argument("--exact-workers", type=int, default=2)
 parser.add_argument("--max-factor-bytes", type=int, default=2147483648)
 parser.add_argument("--out", type=Path, required=True)
 args = parser.parse_args()
 if float(args.eta) != 1.0:
  raise ValueError("This request retains the original explicit R273 eta=1.")
 temp = Path(os.environ["RUNNER_TEMP"]).resolve()
 out = args.out.resolve()
 original = args.original91_directory.resolve()
 if (out == temp or not out.is_relative_to(temp) or out.exists()
     or out.is_relative_to(original) or original.is_relative_to(out)
     or out.is_relative_to(HERE) or HERE.is_relative_to(out)):
  raise ValueError("Use a fresh owned RUNNER_TEMP output independent of source and input.")
 generated, driver, generation = prepared_sources()
 created = []
 exit_code = 2
 error = None
 out.mkdir(parents=True, exist_ok=False)
 started = time.monotonic()
 emit("native103_source_and_parameters", source_sha256=sha_file(__file__),
      run_id=os.environ.get("GITHUB_RUN_ID"), run_attempt=os.environ.get("GITHUB_RUN_ATTEMPT"),
      source_commit=os.environ.get("GITHUB_SHA"), generation=generation,
      parameters={"eta_cli": args.eta, "node_heap": args.node_heap,
       "exact_workers": args.exact_workers, "max_factor_bytes": args.max_factor_bytes,
       "native_iterations": 32, "original_backtracks": 10, "native_tolerance": 2e-9,
       "proposal_full_noJ_evaluations_maximum": 3},
      original91_is_existing_evidence_only=True, failed95_is_not_an_anchor=True,
      raw_output_publication=False)
 try:
  for name, content in generated.items():
   path = HERE / name
   with path.open("xb") as stream:
    stream.write(content.encode())
   created.append((path, generation["derived_source_sha256"][name]))
  scope = {"__name__": "_native103_derived_driver", "__file__": str(HERE / DRIVER),
           "_103_watch": watch}
  exec(compile(driver, str(HERE / DRIVER), "exec"), scope)
  exit_code = int(scope["main"]())
 except BaseException as exc:
  error = repr(exc)
  emit("native103_entry_error", error=compact(error),
       traceback=compact(traceback.format_exc()))
 finally:
  STOP.set()
  for thread in THREADS:
   thread.join(timeout=5)
  result_path = out / "result.json"
  result = {}
  if result_path.is_file():
   try:
    result = read(result_path)
   except Exception as parse_error:
    emit("native103_original_result_read_error", error=repr(parse_error),
         original_file_sha256=sha_file(result_path), original_file_bytes=result_path.stat().st_size)
  # Print every original trial's scalar fields without re-evaluating it.
  trials = out / "native_trials.jsonl"
  if trials.is_file():
   with trials.open("rb") as stream:
    for index, line in enumerate(stream):
     if not line.strip():
      continue
     try:
      emit("native103_original_trial", index=index, original_line_sha256=sha_bytes(line),
           saved_record=compact(json.loads(line)), no_new_evaluation=True)
     except Exception as parse_error:
      emit("native103_original_trial_read_error", index=index,
           original_line_sha256=sha_bytes(line), error=repr(parse_error))
  response_path = out / "native_0001.json.gz"
  response = None
  response_receipt = None
  if response_path.is_file():
   response_receipt = {"bytes": response_path.stat().st_size,
                       "sha256": sha_file(response_path)}
   try:
    payload = read(response_path)
    actual = payload.get("response", {})
    response = {key: compact(actual[key]) for key in (
     "failed", "converged", "residual", "audit", "lastIteration") if key in actual}
    response["requested_complete_J_returned"] = actual.get("heightJetJacobian") is not None
   except Exception as parse_error:
    response = {"complete_original_response_unreadable": True, "error": repr(parse_error)}
  fields = ("native_accepted", "success", "residual", "audit", "original_native_requests",
   "actual_worker_exit_code", "actual_error", "actual_original_failure_message",
   "actual_original_converged_flag", "fresh_withJ_snapshots", "current_directions_returned",
   "current_R273_directions_returned", "word_directions_returned", "bridge_failure",
   "elapsed_seconds", "original_tolerance", "original_max_iterations")
  final = {"schema": "native103-noJ-neighbor-original-loop-summary-v1",
   "source_sha256": sha_file(__file__), "generation": generation,
   "run_id": os.environ.get("GITHUB_RUN_ID"), "source_commit": os.environ.get("GITHUB_SHA"),
   "exit_code": exit_code, "entry_error": compact(error),
   "actual_original_result": {key: compact(result[key]) for key in fields if key in result},
   "original_result_sha256": sha_file(result_path) if result_path.is_file() else None,
   "original_response_receipt": response_receipt, "original_response_scalars": response,
   "elapsed_seconds": time.monotonic() - started, "accepted_prefix": False,
   "task_completed": False, "no_native_or_final_audit_gate_changed": True,
   "no_raw_arrays_checkpoint_or_factor_uploaded": True,
   "summary_is_not_an_accepted_live_anchor": True}
  encoded = (json.dumps(final, ensure_ascii=False, sort_keys=True,
                       separators=(",", ":"), allow_nan=False) + "\n").encode()
  emit("native103_final", summary_sha256=sha_bytes(encoded), summary=final)
  try:
   shutil.rmtree(out)
  except Exception as cleanup_error:
   emit("native103_temporary_output_cleanup_error", error=repr(cleanup_error),
        only_this_owned_runner_directory=True, no_upload_will_follow=True)
  for path, expected in created:
   try:
    if path.is_file() and sha_file(path) == expected:
     path.unlink()
   except Exception as cleanup_error:
    emit("native103_generated_source_cleanup_error", file=path.name,
         error=repr(cleanup_error), not_a_scientific_acceptance_gate=True)
 return exit_code


if __name__ == "__main__":
 raise SystemExit(main())
