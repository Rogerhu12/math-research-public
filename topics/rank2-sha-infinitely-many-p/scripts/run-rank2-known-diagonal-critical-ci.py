#!/usr/bin/env python3
"""Check exact critical matrices at one already identified diagonal prime.

This compares actual finite sources and does not assert complete central
vanishing from a first coefficient.  All source costs remain explicit.
"""
import argparse
from concurrent.futures import ThreadPoolExecutor, as_completed
import json
from pathlib import Path
import subprocess
import tempfile
import time


def source_rank(D, J):
    total = 0
    for n in range(D+1):
        m = n+1
        e = 3*((3*m+3)//4) + 2*((m+1)//2) + (2*m+2)//3 - 2
        total += e+1
    return total*(J+1)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", type=Path, required=True)
    parser.add_argument("--prime", type=int, default=3623)
    parser.add_argument("--workers", type=int, default=2)
    args = parser.parse_args()
    assert args.workers >= 1
    args.out.mkdir(parents=True, exist_ok=True)
    p, s = args.prime, (args.prime+1)//6
    tasks = []
    for D in range(2, 25):
        for J in range(1, 5):
            N = source_rank(D, J)
            ell = N-2*s
            if 1 <= ell < s-13:
                tasks.append((D, J, ell, N))
    (args.out / "actual-budgets.json").write_text(json.dumps(tasks, indent=2) + "\n")
    src = Path(__file__).with_name("search-rank2-critical-source-defect.cpp")
    summary = []
    with tempfile.TemporaryDirectory(prefix="rank2-known-diagonal-") as tmp:
        binary = Path(tmp) / "critical-source-defect"
        subprocess.run(["g++", "-O2", "-std=c++17", str(src), "-o", str(binary)], check=True)

        def run(task):
            D, J, ell, N = task
            key = f"p{p}-D{D}-J{J}"
            print(f"Starting {key}, ell={ell}, N={N}", flush=True)
            started = time.time()
            with (args.out / f"{key}-defects.jsonl").open("w") as out, (args.out / f"{key}-progress.log").open("w") as err:
                result = subprocess.run([str(binary), "--one", str(p), str(D), str(J), str(ell)], stdout=out, stderr=err)
            item = {"p": p, "D": D, "J": J, "ell": ell, "N": N,
                    "returncode": result.returncode, "seconds": round(time.time()-started, 3)}
            print(json.dumps(item), flush=True)
            return item

        with ThreadPoolExecutor(max_workers=args.workers) as pool:
            for future in as_completed([pool.submit(run, task) for task in tasks]):
                summary.append(future.result())
                (args.out / "matrix-status.json").write_text(json.dumps(summary, indent=2) + "\n")
    assert all(item["returncode"] == 0 for item in summary), "A matrix calculation failed"


if __name__ == "__main__":
    main()
