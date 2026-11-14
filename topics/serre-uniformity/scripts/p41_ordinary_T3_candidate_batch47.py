#!/usr/bin/env python3
"""Resume actual support and principal norms for specified remaining disks."""
import argparse
import gzip
import hashlib
import json
from pathlib import Path
import subprocess
import sys


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def read(path):
    raw = Path(path).read_bytes()
    return json.loads(gzip.decompress(raw) if str(path).endswith(".gz") else raw)


def save(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    raw = (json.dumps(data, sort_keys=True, separators=(",", ":"))+"\n").encode()
    temp = path.with_suffix(path.suffix+".new")
    temp.write_bytes(gzip.compress(raw, mtime=0))
    temp.replace(path)


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    for name in ["script-dir", "qc-dir", "ordinary-lifts", "support-source", "norm-source", "output"]:
        ap.add_argument("--"+name, type=Path, required=True)
    ap.add_argument("--j-list", nargs="+", type=int, required=True)
    args = ap.parse_args()
    base = args.qc_dir.resolve()
    folder = base / "ordinary-F3-norms"
    folder.mkdir(exist_ok=True)
    out = {"requested_j": args.j_list, "completed": {}, "support_completed": {},
           "source_sha256": sha(__file__),
           "dependency_source_sha256": {p.name: sha(p) for p in [args.support_source, args.norm_source]},
           "complete": False}
    if args.output.exists():
        old = read(args.output)
        assert old["source_sha256"] == out["source_sha256"]
        assert old["requested_j"] == out["requested_j"]
        assert old["dependency_source_sha256"] == out["dependency_source_sha256"]
        out = old
    save(args.output, out)
    for j in args.j_list:
        disk = "ORD_j"+str(j).zfill(2)
        support = folder / (disk+"_actual_T3_support47.json.gz")
        norm = folder / (disk+"_actual_T3_principal_norm47.json.gz")
        if disk not in out["support_completed"]:
            if not support.exists() or not read(support).get("complete_actual_T3_support"):
                subprocess.run([sys.executable, str(args.support_source),
                                "--script-dir", str(args.script_dir),
                                "--ordinary-lifts", str(args.ordinary_lifts),
                                "--j", str(j), "--output", str(support)], check=True)
            d = read(support)
            assert d["source_disk_id"] == disk and d["complete_actual_T3_support"]
            assert d["source_sha256"] == sha(args.support_source)
            out["support_completed"][disk] = {"basename": support.name, "sha256": sha(support)}
            save(args.output, out)
        if disk not in out["completed"]:
            if not norm.exists() or not read(norm).get("complete_actual_principal_norm_on_T3_P"):
                subprocess.run([sys.executable, str(args.norm_source),
                                "--script-dir", str(args.script_dir),
                                "--support", str(support),
                                "--principal-expression", str(base/"ordinary-F2-norms"/(disk+"_actual_principal_function47.json.gz")),
                                "--transport-directory", str(base/"ordinary-principal-transports"/disk),
                                "--based-points", str(base/"p41_all19_based_points47.json.gz"),
                                "--second-kind-certificate", str(base/"ordinary-second-kind"/(disk+"_second_kind_complete47.json.gz")),
                                "--multiplication", str(base/"ordinary-abel-with-transports"/(disk+"_multiply47.json.gz")),
                                "--cache-dir", str(base/"ordinary-norm-cache"),
                                "--output", str(norm)], check=True)
            d = read(norm)
            assert d["disk_id"] == disk and d["complete_actual_principal_norm_on_T3_P"]
            assert d["input_sha256"][support.name] == sha(support)
            assert d["source_sha256"] == sha(args.norm_source)
            out["completed"][disk] = {
                "norm_file": norm.name, "norm_sha256": sha(norm),
                "actual_norm_mod47four": d["actual_norm_Phi_T3_P_mod47four"],
                "actual_log_norm_mod47four": d["actual_log_norm_Phi_T3_P_mod47four"],
            }
            save(args.output, out)
            print("T3 CANDIDATE COMPLETE", disk, len(out["completed"]), "/", len(args.j_list),
                  out["completed"][disk], flush=True)
    out["complete"] = True
    save(args.output, out)
    print("PASS REQUESTED ACTUAL T3 CANDIDATE NORMS", sha(args.output), flush=True)


if __name__ == "__main__":
    main()
