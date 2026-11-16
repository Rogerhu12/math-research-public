#!/usr/bin/env sage-python
"""Offline SAME-source original shadow consumer.

Use:
  python3 read-original-shadow-pass-receipts.py <pinned args> |
    docker run --network none -i ... sage -python this_script.py <same pinned args>

The host authenticates actual public jobs.  Only its JSON envelope crosses stdin.
The Sage process rechecks all pinned metadata, hashes, and whole certificates;
it never reads a token, fetches a log, or writes a recomputable data file.
"""
import os
if (os.environ.get("GITHUB_ACTIONS")!="true" or
        os.environ.get("GITHUB_REPOSITORY")!="Rogerhu12/math-research-public"):
    raise SystemExit("Run only in the public research Actions.")
if any(os.environ.get(k) for k in ("GH_TOKEN","GITHUB_TOKEN","RANK2_GITHUB_TOKEN")):
    raise SystemExit("The repository token must remain on the host, outside Sage.")
import argparse
import hashlib
import importlib.util
import json
import sys
import time
from pathlib import Path
DIRECTORY=Path(__file__).resolve().parent
sys.path.insert(0,str(DIRECTORY))
from original_shadow_receipt_tools import (
    canonical,digest,add_pinned_arguments,pinned_request,validate_envelope)
STARTED=time.monotonic()

def progress(stage,**kw):
    print("RANK2_SHADOW_CONSUMER_STAGE "+canonical(dict(
        stage=stage,elapsed_seconds=time.monotonic()-STARTED,**kw)),flush=True)

def import_script(filename,module_name):
    path=DIRECTORY/filename
    spec=importlib.util.spec_from_file_location(module_name,str(path))
    module=importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

def main():
    parser=argparse.ArgumentParser()
    add_pinned_arguments(parser)
    parser.add_argument("--trace-method",choices=("tate","scalar","compare"),
                        default="tate")
    args=parser.parse_args()
    request=pinned_request(args)
    incoming=sys.stdin.buffer.read(2*1024*1024+1)
    if len(incoming)>2*1024*1024:
        raise RuntimeError("The host envelope exceeds the fixed receipt budget.")
    envelope=json.loads(incoming.decode("utf-8"))
    host_hash=hashlib.sha256((DIRECTORY/"read-original-shadow-pass-receipts.py").read_bytes()).hexdigest()
    first,packet=validate_envelope(envelope,request,host_hash)
    from original_shadow_coordinate_tools import certificate_weight
    first_weight=certificate_weight(first,"F")
    packet_weight=certificate_weight(packet,"P")
    progress("both same original PASS receipts rechecked offline",
             first_weight=first_weight,packet_weight=packet_weight,
             envelope_sha256=envelope["envelope_sha256"],
             first_source=first["source"],first_run=first["run_id"],
             packet_source=packet["source"],packet_run=packet["run_id"],
             trace_method=args.trace_method)
    # No mathematical reconstruction begins before BOTH true whole certificates.
    local_module=import_script("produce-original-shadow-local-input.py","original_shadow_local_input")
    progress("same original full-precision local input start",prime=args.prime)
    local,local_summary=local_module.build_local_input(
        args.prime,1226,1428,64,(0,1,2))
    progress("same original full-precision local input complete",
             summary_sha256=digest(local_summary),
             sigma_a_index=[int(i) for i in local["sigma_a_index"]])
    front=import_script("produce-original-shadow-rr-eta48.py","original_shadow_rr_eta48")
    rr,rr_summary=front.build_frontend(args.prime,(1,),205,"eta48")
    progress("same original RR frontend complete",summary_sha256=digest(rr_summary))
    from original_shadow_coordinate_tools import build_reduced_maps
    maps,maps_summary=build_reduced_maps(rr,local,first,packet)
    progress("same original reduced maps complete",summary_sha256=digest(maps_summary))
    from original_shadow_relative_six_tools import consume_original_relative_six
    result=consume_original_relative_six(rr,maps,trace_method=args.trace_method)
    dependencies=[
        "launch-original-shadow-consumer.py",
        "read-original-shadow-pass-receipts.py",
        "original_shadow_receipt_tools.py",
        "produce-original-shadow-local-input.py",
        "original_good_prime_germ_tools.py",
        "check-r873-original-cm-petersson-degree.py",
        "original_low_weight_cm_tools.py",
        "produce-original-shadow-rr-eta48.py",
        "original_shadow_coordinate_tools.py",
        "original_shadow_relative_six_tools.py",
        "original_shadow_tate_trace_tools.py",
        "original_shadow_coefficient_tools.py",
    ]
    manifest={
        "kind":"rank2_original_shadow_consumer_public_execution",
        "prime":args.prime,"parameters":dict(request,trace_method=args.trace_method),
        "source":os.environ.get("RANK2_SOURCE_SHA"),
        "run_id":os.environ.get("RANK2_RUN_ID",os.environ.get("GITHUB_RUN_ID")),
        "run_attempt":os.environ.get("RANK2_RUN_ATTEMPT"),
        "image":os.environ.get("RANK2_IMAGE"),
        "readme_blobs":{"root":os.environ.get("RANK2_ROOT_README_SHA"),
                        "topic":os.environ.get("RANK2_TOPIC_README_SHA")},
        "script_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "dependency_sha256":{
            filename:hashlib.sha256((DIRECTORY/filename).read_bytes()).hexdigest()
            for filename in dependencies},
        "public_pass_envelope_sha256":envelope["envelope_sha256"],
        "host_authenticated_run_heads":{
            k:envelope["authentication"][k]["run_head_sha"] for k in ("F","P")},
        "local_summary_sha256":digest(local_summary),
        "RR_summary_sha256":digest(rr_summary),
        "reduced_map_summary_sha256":digest(maps_summary),
        "original_shadow_result_sha256":digest(result),
        "original_rational_AJ_detected_nonzero":result["original_rational_AJ_detected_nonzero"],
        "elapsed_seconds":time.monotonic()-STARTED,
        "Sage_network_mode":"none",
        "recomputable_data_file_written":False,
    }
    print("RANK2_SHADOW_CONSUMER_MANIFEST "+canonical(manifest),flush=True)
    print("RANK2_SHADOW_CONSUMER_MANIFEST_SHA256 "+digest(manifest),flush=True)

if __name__=="__main__":
    main()
