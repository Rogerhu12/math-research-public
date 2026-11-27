#!/usr/bin/env python3
"""Read only the two unfinished original CM disks, using the unchanged QC engine.

The successful six-disk request is immutable, hash-pinned common input.
This entry accepts only four complete new short-Cartier records for IDs0/141.
"""
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import signal
import sys
import traceback

ROOT=Path(__file__).resolve().parents[3]
PRE="topics/serre-uniformity/"
THIS=PRE+"scripts/full_p47_QC_special_two.py"
REQUEST=ROOT/(PRE+"notes/full-p47-QC-special-two-request.json")
ENGINE_PATH=PRE+"scripts/full_p47_QC_first_rows.py"
COMMON_PATH=PRE+"notes/full-p47-QC-first-rows-request.json"
COMMON_SHA="95e8ccb0bd7906f1c0c47fbebc794c77994b3fd5cba58766d31fbc53ac3dbc0b"
NEW_SOURCE={
    "source":"d935282c49c9c19d541729ca5bd59579aac7e82f",
    "run":45998781656,
    "job":140504817189,
    "request_sha256":"ed9508e1cd4d0f4b9950c68eebde5ada7fddf29d1e63810df7e367bffa6b8bc2",
}
ENGINE=None


def read_request():
    if os.environ.get("GITHUB_ACTIONS")!="true" or os.environ.get(
            "GITHUB_REPOSITORY")!="Rogerhu12/math-research-public":
        raise RuntimeError("Mathematics is restricted to this public repository's Actions.")
    raw=REQUEST.read_bytes()
    ENGINE.REQUEST_HASH=hashlib.sha256(raw).hexdigest()
    if ENGINE.REQUEST_HASH!=os.environ.get("SERRE_EXPECTED_REQUEST_SHA256"):
        raise RuntimeError("The separate special-two QC request hash changed.")
    fresh=json.loads(raw)
    if (fresh["execution_id"]!="full-p47-QC-special-two-v1" or
            fresh["prime"]!=47 or fresh["coefficient_prime"]!=4513 or
            fresh["sage_version"]!="10.6" or fresh["python_flint_version"]!="0.9.0" or
            fresh["total_seconds"]!=2400 or fresh["reserve_seconds"]!=60 or
            fresh["CM_candidate_ids"]!=[0,141] or fresh["correspondences"]!=["ZA","ZB"] or
            fresh["excluded_completed_CM_ids"]!=[76,77,100,108,196,220]):
        raise RuntimeError("Only the two still unread original QC disks are in scope.")
    if fresh["consumed_common_QC_request"]!={"path":COMMON_PATH,"sha256":COMMON_SHA}:
        raise RuntimeError("The immutable common QC input changed.")
    common_raw=(ROOT/COMMON_PATH).read_bytes()
    if hashlib.sha256(common_raw).hexdigest()!=COMMON_SHA:
        raise RuntimeError("The successful six-disk request must remain unchanged.")
    common=json.loads(common_raw)
    if (common["execution_id"]!="full-p47-QC-first-rows-v2" or
            common["CM_candidate_ids"]!=fresh["excluded_completed_CM_ids"] or
            common["CM_coordinate_method"]!="signed-Jacobi-R1119" or
            common["prime"]!=47 or common["coefficient_prime"]!=4513 or
            common["total_seconds"]!=2400 or common["reserve_seconds"]!=60):
        raise RuntimeError("The consumed common request has the wrong original scope.")
    if fresh["consumed_third_kind_source"]!=NEW_SOURCE:
        raise RuntimeError("The four new local values must come from their own complete run.")
    rows=fresh["consumed_third_kind_values"]
    expected={(0,"ZA"),(0,"ZB"),(141,"ZA"),(141,"ZB")}
    if (not isinstance(rows,list) or len(rows)!=4 or
            {(r.get("candidate_id"),r.get("angle")) for r in rows}!=expected or
            any(r.get("method")!="R1118-short-Cartier" for r in rows) or
            ENGINE.digest(rows)!=fresh["consumed_third_kind_values_sha256"]):
        raise RuntimeError("Exactly four complete, own-divisor short-Cartier records are required.")
    cc=fresh["consumed_Cartier_matrix_certificate"]
    if (not isinstance(cc,dict) or
            ENGINE.digest(cc)!=fresh["consumed_Cartier_matrix_certificate_sha256"] or
            cc.get("dimension")!=73 or cc.get("one_minus_C_determinant")!=551 or
            cc.get("Cartier_row_matrix_sha256")!=
                "deda5ed6dbe8122f243c46bb60245cf8facc00b6040a8f34958c9ca4241d855d" or
            cc.get("Cartier_column_matrix_sha256")!=
                "21fc43c13f58e974adb58804e3480f80d3268104546e31e40ca5370806bbb58f"):
        raise RuntimeError("The four values lost the common original full73 Cartier frame.")
    pins=dict(common["source_sha256"])
    for path,wanted in fresh["source_sha256"].items():
        if path in pins and pins[path]!=wanted:
            raise RuntimeError("The separate request cannot alter an old source pin: "+path)
        pins[path]=wanted
    if (pins.get(COMMON_PATH)!=COMMON_SHA or
            pins.get(ENGINE_PATH)!="ac9ac63dd31556b6b4952c71a5aa4b9c1e4826c9ccfb044bace50090cf861ea4" or
            THIS not in pins):
        raise RuntimeError("The original QC engine, old input or new entry is not pinned.")
    for path,wanted in pins.items():
        if hashlib.sha256((ROOT/path).read_bytes()).hexdigest()!=wanted:
            raise RuntimeError("An original special-two QC source changed: "+path)
    req=dict(common)
    for key in ("execution_id","CM_candidate_ids","consumed_third_kind_values",
                "consumed_third_kind_values_sha256","consumed_Cartier_matrix_certificate",
                "consumed_Cartier_matrix_certificate_sha256","consumed_third_kind_source",
                "scope","storage","rules_last_read_commit"):
        req[key]=fresh[key]
    req["source_sha256"]=pins
    req["consumed_common_QC_request"]=fresh["consumed_common_QC_request"]
    req["excluded_completed_CM_ids"]=fresh["excluded_completed_CM_ids"]
    return req


def main():
    global ENGINE
    spec=importlib.util.spec_from_file_location("original_QC_common_engine",ROOT/ENGINE_PATH)
    ENGINE=importlib.util.module_from_spec(spec)
    sys.modules[spec.name]=ENGINE
    spec.loader.exec_module(ENGINE)
    ENGINE.REQUEST=REQUEST
    ENGINE.THIS=THIS
    ENGINE.read_request=read_request
    if sys.argv[1:]==["--field-worker"]:
        ENGINE.field_worker()
    elif not sys.argv[1:]:
        ENGINE.main()
    else:
        raise RuntimeError("Unexpected command-line arguments.")


if __name__=="__main__":
    try:
        main()
    except BaseException as exc:
        signal.setitimer(signal.ITIMER_REAL,0)
        if ENGINE is not None:
            ENGINE.emit("receipt",status="incomplete",source=ENGINE.SOURCE,
                run=os.environ.get("GITHUB_RUN_ID"),request_sha256=ENGINE.REQUEST_HASH,
                stage=ENGINE.STAGE,completed=ENGINE.COMPLETED,
                exception_type=type(exc).__name__,message=str(exc),
                scope="Only complete requested original IDs0/141 QC rows survive.")
        else:
            print(json.dumps({"kind":"receipt","status":"incomplete",
                "exception_type":type(exc).__name__,"message":str(exc)},sort_keys=True),flush=True)
        traceback.print_exc()
        sys.exit(1)
