#!/usr/bin/env python3
"""Execute only four original code-identity predicates, never a final audit."""
from pathlib import Path
from hashlib import sha256
import argparse
import importlib.util
import json
import sys

PINNED = {
    "db6f-prefix-audit-spectral-true-m14-direct-csc.py": "b6222f3394c53eebd8409c922ed2e009de85b4bcdbfa5a6e8c8d57b2294967e0",
    "db6f-prefix-spectral-true-m14-direct-csc.py": "b6fd772b5f44819186fc7e31af370ffa199bfa5c9b14a2722b36345bcf26cd24",
    "db6f-prefix-direct-csc-entry-gates.py": "d110a15669612ae75207d98b46b8ee31c41d5f98dc8a9b693a06a4cbc399606b",
    "db6f-prefix-spectral-affine-replay.py": "ad219dbab80278670665ac3cb5401cb55daf33834cea8495dd16bf1c1396e4bd",
}
SCIPY_SHA = "59afffb3607b272ae77f346d86428e43eca359fe90f2605da60a9571e60970d2"
NAMES = ("prepare_sys", "construct_global_jac", "compute_jac_indices", "solve_bvp")

def digest(path):
    return sha256(Path(path).read_bytes()).hexdigest()

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--reproduction", type=Path, required=True)
    parser.add_argument("--out", type=Path, required=True)
    args=parser.parse_args()
    if args.out.exists():
        raise FileExistsError(args.out)
    base=Path(__file__).resolve().parent.parent
    scripts=base/"scripts"
    for name, expected in PINNED.items():
        assert digest(scripts/name)==expected, name
    rep=json.loads(args.reproduction.read_text())
    launch_row=rep["launch"]; launch_path=Path(launch_row["path"])
    assert digest(launch_path)==launch_row["sha256"]
    assert launch_path.stat().st_size==launch_row["bytes"]
    launch=json.loads(launch_path.read_text())
    assert sys.executable==launch["command"][0]
    original=rep["csc_selection"]["original_runtime"]
    assert set(original)==set(NAMES)
    scipy_path=Path(original["prepare_sys"]["filename"])
    assert digest(scipy_path)==SCIPY_SHA
    path=scripts/"db6f-prefix-audit-spectral-true-m14-direct-csc.py"
    spec=importlib.util.spec_from_file_location("independent_original_runtime_gate_probe",path)
    module=importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    rows=[]
    for name in NAMES:
        try:
            module._compiled_runtime_record(original[name],scipy_path,name,"scipy.integrate._bvp")
        except ValueError as error:
            rows.append({"function":name,"accepted":False,"error_type":type(error).__name__,"error":str(error)})
        else:
            rows.append({"function":name,"accepted":True})
    for name, expected in PINNED.items():
        assert digest(scripts/name)==expected, name
    result={
        "schema":"78718-independent-original-runtime-gate-probe-v1",
        "status":"ORIGINAL_RUNTIME_PREDICATES_ONLY_NOT_A_FINAL_AUDIT",
        "scope":"Only _compiled_runtime_record on the four recorded original exports. No selected-function/factory audit and no mathematical success inference.",
        "probe_sha256":digest(__file__),
        "sys_executable":sys.executable,
        "sys_version":sys.version,
        "reproduction_sha256":digest(args.reproduction),
        "launch_sha256":digest(launch_path),
        "unchanged_source_sha256":PINNED,
        "scipy_source_sha256":SCIPY_SHA,
        "rows":rows,
        "any_original_gate_rejects":any(not r["accepted"] for r in rows),
        "original_sources_unchanged":True,
        "full_auditor_executed":False,
        "solver_calls":0,
        "callback_calls":0,
        "candidate_optimization":False,
        "run02_success_inferred":False,
    }
    raw=(json.dumps(result,indent=2,allow_nan=False)+"\n").encode()
    assert len(raw)<100_000
    with args.out.open("xb") as stream:
        stream.write(raw)
    rejected=sum(not r["accepted"] for r in rows)
    print("original_runtime_predicates",len(rows),"rejected",rejected,"accepted",len(rows)-rejected)
    print("report_bytes",len(raw),"sha256",sha256(raw).hexdigest())
    print("original_sources_unchanged",True,"full_auditor_executed",False,"solver_calls",0)

if __name__=="__main__":
    main()
