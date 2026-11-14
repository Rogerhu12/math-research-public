#!/usr/bin/env python3
"""One original no-J stage replay of the actual request17 cold-tail failure.

All original modes, geometry, RK12, source bytes, scales and branch guards
remain.  This entry checks the complete failed iteration0/ready/config/source
identity, starts the unchanged true client constructor under one recorded
request-loop instrumentation hook, then sends a diagnostic protocol only.
It never calls TailClient.solve, dn.solve, Newton, or a repeated zero solve.
No failed response or diagnostic is promoted to an accepted tail anchor.
"""
from __future__ import annotations

import argparse
import gzip
import hashlib
import json
import os
from pathlib import Path
import time


HERE = Path(__file__).resolve().parent
FILES = {
    "failed_response": ("true-tail_0001.json.gz", "ebe8932a7ba1a995f49b365344e795714bc0fdfccc606765cc69944b56a6b7a0"),
    "iteration": ("true-tail_iteration.json.gz", "e996f37aa4eb7cfb0bb8b5bb912f594af794d16146240ee6db114c22eb55de7d"),
    "ready": ("true-tail_ready.json.gz", "4a2c24f3f4cdddc4dd581a50fd13c13fd6c00cd0646404e2ac4a64a80b12c678"),
    "intent": ("true-tail_intent.json", "3d67e9fc2d761f2edc2b9b0ba6b217f34409aaa0b6376b11f90ce72ff537476d"),
    "capacity": ("true-tail_capacity.json", "4f0f7aaab43f8ed90c478c2983026671f4c17ddcbe25d494746a4dafc96210dc"),
}
PINNED_SOURCES = {
    "exact_20261114_true_tail_client.py": "1cdf0e14ae3f71dd57a8c0ab3036f11943929860296153ca7886e20e7b445a09",
    "exact_20261114_seeded_zero_tail_client.py": "a8de071c0667b342dfc7a2731c9a47ce3d071e03496875637f80424864114776",
    "tail_frozen_worker.mjs": "3788050920ea7a585b03d1f86b33efef262b3169b9d8907e07abff5e3d382054",
}
CACHE_ONLY_PROVENANCE = {
    "exact_20261114_seeded_zero_tail_client.py": PINNED_SOURCES["exact_20261114_seeded_zero_tail_client.py"],
    "imported_completed_zero_response": "6b4ff3e5bc11e23419242ee018b668c57f08b6dbdd791cd43d81883bf6f4960e",
}


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def read(path):
    raw = Path(path).read_bytes()
    return json.loads(gzip.decompress(raw) if raw[:2] == b"\x1f\x8b" else raw)


def write(path, record):
    raw = (json.dumps(record, ensure_ascii=False, sort_keys=True,
                     indent=2, allow_nan=False)+"\n").encode()
    if len(raw) >= 1_000_000:
        raise ValueError("Use a real gzip evidence packet for a large record")
    with Path(path).open("xb") as stream:
        stream.write(raw)


def main():
    if (os.environ.get("GITHUB_ACTIONS") != "true" or
            os.environ.get("GITHUB_REPOSITORY", "").lower() != "rogerhu12/math-research-public"):
        raise RuntimeError("Execute the actual native replay only in this public repository Actions")
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--failed-directory", type=Path, required=True)
    p.add_argument("--source-topic", type=Path, required=True)
    p.add_argument("--out", type=Path, required=True)
    p.add_argument("--node-heap", type=int, default=1536)
    a = p.parse_args()
    a.out = a.out.resolve()
    a.out.mkdir(parents=True, exist_ok=True)
    if any(a.out.iterdir()):
        raise ValueError("Use an empty actual-replay output directory")
    for name,digest in PINNED_SOURCES.items():
        if sha(HERE/name) != digest:
            raise ValueError("The frozen numerical/provenance source changed: "+name)
    from exact_20261114_seeded_zero_tail_client import (
        same, numerical_configuration, numerical_sources, ready_semantics, IO_KEYS)
    import exact_20261114_true_tail_client as original

    def equal(left,right,label):
        if not same(left,right):
            raise ValueError("Actual cold replay identity differs: "+label)

    paths,records,inputs = {},{},{}
    for key,(filename,digest) in FILES.items():
        path = (a.failed_directory/filename).resolve()
        if sha(path) != digest:
            raise ValueError("This is not the retained actual request17 input: "+filename)
        paths[key],records[key] = path,read(path)
        inputs[key] = dict(path=str(path),sha256=digest,bytes=path.stat().st_size)
    failure,iteration,ready,intent,capacity = (records[key]
        for key in ("failed_response","iteration","ready","intent","capacity"))
    runtime = (a.failed_directory/"true-tail_runtime-config.json").resolve()
    if sha(runtime) != intent["source_sha256"]["runtime_config"]:
        raise ValueError("The original runtime config no longer matches its actual intent")
    inputs["runtime_config"] = dict(path=str(runtime),sha256=sha(runtime),bytes=runtime.stat().st_size)
    runtime_config = read(runtime)
    equal(failure["config"],runtime_config,"full original runtime configuration")
    if "initialCheckpoint" in runtime_config or ready["warmEmbedding"] is not None:
        raise ValueError("The original selected request must have the recorded cold initialization")
    response = failure["response"]
    checkpoint = response["checkpoint"]
    if (not response.get("failed") or response.get("converged") is True
            or response["lastIteration"]["iteration"] != 0
            or iteration["status"] != "iteration-recovery-only"
            or iteration["call"] != 1 or iteration["iteration"]["iteration"] != 0):
        raise ValueError("Retain the actual failed first iteration, without promoting its status")
    if (failure["request"]["jacobian"] is not True
            or failure["request"]["audit"] is not False):
        raise ValueError("Original failed request identity differs")
    for key in ("parameters","states","rawNode","rawStates","cutHeight"):
        equal(checkpoint[key],iteration["checkpoint"][key],"failure/iteration "+key)
    equal(checkpoint["cutHeight"],failure["request"]["height"],"complete actual H")
    equal(checkpoint["parameters"],ready["parameters"],"original ready/checkpoint parameters")
    equal(failure["capacity_adapter"],capacity,"complete original capacity manifest")
    current_catalog = dict(failure["source_sha256"])
    for key,digest in CACHE_ONLY_PROVENANCE.items():
        equal(current_catalog.pop(key,None),digest,"actual original cache-only provenance "+key)
    equal(current_catalog,intent["source_sha256"],"actual worker vs pre-cache intent source inventory")
    config = numerical_configuration(runtime_config)
    equal({k:config[k] for k in ("modes","quadrature","spacing","depth","steps","auditSteps","shootingParts","solveTolerance")},
        dict(modes=112,quadrature=2048,spacing=2,depth=8,steps=12,auditSteps=12,
             shootingParts=8,solveTolerance=2e-9),"original finite dimensions/steps/gates")
    height = failure["request"]["height"]
    if len(height) != 112 or not any(v != 0 for v in height):
        raise ValueError("Keep the true nonzero full height; no thresholding")
    config_path = a.out/"replay-input-config.json"
    # Only original output I/O paths are removed; every numerical value is retained.
    original.write(config_path,config)
    hook = HERE/"exact_20261114_tail_cold_residual_probe_hook.mjs"
    spec = dict(schema="actual-cold-tail-stage-replay-spec-v1",original_public_run="43598917532",
        source_sha256=sha(__file__),hook_sha256=sha(hook),inputs=inputs,
        original_input_config_sha256=intent["source_sha256"]["input_config"],
        replay_input_config_sha256=sha(config_path),output=str(a.out),
        numerical_configuration=config,numerical_parameters=numerical_configuration(checkpoint["parameters"]),
        io_keys=sorted(IO_KEYS),original_request=failure["request"],
        no_tail_or_BVP_solve=True,no_threshold_or_frequency_change=True)
    spec_path = a.out/"replay-spec.json"
    write(spec_path,spec)
    started=time.monotonic()
    prior_environment=os.environ.get("VISIBLE_FLEX_COLD_REPLAY_SPEC")
    os.environ["VISIBLE_FLEX_COLD_REPLAY_SPEC"]=str(spec_path)
    popen = original.subprocess.Popen
    spawned_commands=[]

    def diagnostic_popen(command,*args,**kwargs):
        expected_worker=str(HERE/"tail_frozen_worker.mjs")
        # The original constructor may lazily read a public asset with git;
        # those ordinary read-only subprocesses do not receive any hook.
        if not isinstance(command,list) or expected_worker not in command:
            return popen(command,*args,**kwargs)
        if (len(command)!=8 or command[0]!="node"
                or command[4]!="--import" or command[6]!=expected_worker):
            raise ValueError("Only the original exact true-client worker launch may receive this instrumentation")
        actual=list(command[:6])+["--import",str(hook)]+list(command[6:])
        spawned_commands.append(actual)
        return popen(actual,*args,**kwargs)

    client=None
    final_record=dict(schema="actual-cold-tail-replay-launcher-v1",inputs=inputs,
        source_sha256=sha(__file__),hook_sha256=sha(hook),spec_sha256=sha(spec_path),
        original_source_sha256=intent["source_sha256"],
        separately_retained_cache_only_provenance=CACHE_ONLY_PROVENANCE,
        original_worker_sources_not_modified=True,only_request_loop_instrumented=True,
        no_TailClient_solve_called=True,task_completed=False)
    try:
        original.subprocess.Popen=diagnostic_popen
        try:
            client=original.TailClient(config_path,a.source_topic.resolve()/"repro/source-root",
                                       a.out/"original-constructor",node_heap=a.node_heap)
        finally:
            original.subprocess.Popen=popen
        equal(numerical_configuration(client._configuration),config,"all current numerical config values")
        equal(numerical_sources(client.sources),numerical_sources(intent["source_sha256"]),
              "all actual consumed original numerical source bytes")
        equal(ready_semantics(client.ready),ready_semantics(ready),"full original/current ready semantics")
        current_capacity=original.read(client.capacity_record)
        for key in ("name","capacity","requestedCapacity","nodeVersion","adapterSHA256",
                    "originalConstructorCapacity","numericalChange","retained","files"):
            equal(current_capacity[key],capacity[key],"original/current capacity "+key)
        if len(spawned_commands)!=1:
            raise AssertionError("Only one original native constructor is needed")
        final_record.update(actual_command=spawned_commands[0],identity_verified_before_stage_pass=True,
            current_sources=client.sources,current_capacity_sha256=sha(client.capacity_record),
            complete_current_ready_sha256=sha(a.out/"original-constructor_ready.json.gz"))
        write(a.out/"verified-launch-intent.json",final_record)
        print(json.dumps(dict(event="cold-replay-identities-verified",source_sha256=sha(__file__),
            failure_sha256=inputs["failed_response"]["sha256"],all_original_modes=112,
            RK_steps=12,actual_original_evaluate_with_J=False)),flush=True)
        client.proc.stdin.write(json.dumps(dict(cold_replay=sha(spec_path)))+"\n")
        client.proc.stdin.flush()
        with (a.out/"diagnostic-stdout.jsonl").open("x") as stream:
            for line in client.proc.stdout:
                stream.write(line);stream.flush()
                print(line.rstrip(),flush=True)
        code=client.proc.wait()
        final_record["worker_exit_code"]=code
        if code!=0:
            raise RuntimeError("The no-J diagnostic worker failed; preserve its stderr/instrumentation and original inputs")
        summary=read(a.out/"summary.json")
        if summary.get("schema")!="actual-cold-tail-no-J-stage-replay-v1" or not summary.get("finished"):
            raise ValueError("No completed actual diagnostic summary was produced")
        final_record.update(finished=True,summary_sha256=sha(a.out/"summary.json"),
            stage_evaluation_completed=summary["evaluation_completed"],
            original_native_solve_calls=client.calls,new_tail_acceptance=False)
        return_code=0 if summary["evaluation_completed"] else 2
    except Exception as error:
        final_record.update(finished=False,error=repr(error),new_tail_acceptance=False)
        return_code=2
        raise
    finally:
        original.subprocess.Popen=popen
        if client is not None:client.close()
        if prior_environment is None:os.environ.pop("VISIBLE_FLEX_COLD_REPLAY_SPEC",None)
        else:os.environ["VISIBLE_FLEX_COLD_REPLAY_SPEC"]=prior_environment
        final_record["elapsed_seconds"]=time.monotonic()-started
        write(a.out/"launcher-result.json",final_record)
    return return_code


if __name__=="__main__":
    raise SystemExit(main())
