#!/usr/bin/env python3
"""Run independent exact critical-source searches on a four-core runner.

Outputs are finite diagnostic matrices, not an infinite-prime claim.  The
original small completed rectangle can be skipped without altering a case.
"""
import argparse
from concurrent.futures import ThreadPoolExecutor, as_completed
import json
from pathlib import Path
import subprocess
import tempfile
import time


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", type=Path, required=True)
    parser.add_argument("--max-D", type=int, default=10)
    parser.add_argument("--max-J", type=int, default=4)
    parser.add_argument("--skip-D", type=int, default=8)
    parser.add_argument("--skip-J", type=int, default=3)
    parser.add_argument("--stop-after", type=int, default=3)
    args = parser.parse_args()
    args.out.mkdir(parents=True, exist_ok=True)
    src = Path(__file__).with_name("search-rank2-critical-source-defect.cpp")
    summary = []
    with tempfile.TemporaryDirectory(prefix="rank2-critical-") as tmp:
        binary = Path(tmp) / "critical-source-defect"
        subprocess.run(["g++", "-O2", "-std=c++17", str(src), "-o", str(binary)], check=True)

        def job(D):
            first_J = args.skip_J + 1 if D <= args.skip_D else 0
            if first_J > args.max_J:
                return {"D": D, "skipped": True}
            cmd = [str(binary), str(D), str(args.max_J), str(args.stop_after), str(D), str(first_J)]
            started = time.time()
            print(f"Starting D={D}, J={first_J}..{args.max_J}", flush=True)
            with (args.out / f"D{D}-defects.jsonl").open("w") as out, (args.out / f"D{D}-progress.log").open("w") as err:
                run = subprocess.run(cmd, stdout=out, stderr=err)
            result = {"D": D, "min_J": first_J, "max_J": args.max_J,
                      "returncode": run.returncode, "seconds": round(time.time()-started, 3)}
            print(json.dumps(result), flush=True)
            return result

        with ThreadPoolExecutor(max_workers=4) as pool:
            futures = [pool.submit(job, D) for D in range(2, args.max_D + 1)]
            for future in as_completed(futures):
                summary.append(future.result())
                (args.out / "search-status.json").write_text(json.dumps(sorted(summary, key=lambda x: x["D"]), indent=2) + "\n")
    assert all(item.get("returncode", 0) == 0 for item in summary), "A search worker failed"


if __name__ == "__main__":
    main()
