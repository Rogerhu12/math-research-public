#!/usr/bin/env python3
"""Bounded source-faithful streaming GB over the already complete F31[s] NF.

The only long-lived arithmetic state is at most one degree-45 row per module
component and its two small constant multiples. A prefix result is explicitly
not the full original module basis and must never be fed to the Ann stage.
"""
from __future__ import annotations
import argparse
import importlib.util
import json
from pathlib import Path
import subprocess
import time


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--mapping", type=Path, required=True)
    parser.add_argument("--nf-receipt", type=Path, required=True)
    parser.add_argument("--out", type=Path, required=True)
    parser.add_argument("--singular", required=True)
    parser.add_argument("--binary", type=Path)
    parser.add_argument("--seconds", type=int, default=60)
    parser.add_argument("--soft-seconds", type=int, default=50)
    parser.add_argument("--memory-mib", type=int, default=512)
    parser.add_argument("--max-sources", type=int, default=0)
    args = parser.parse_args()
    if (args.seconds < 10 or args.soft_seconds < 1 or args.soft_seconds > args.seconds - 5
            or args.memory_mib <= 0 or args.max_sources < 0 or args.max_sources > 2195):
        raise ValueError("invalid explicit limits")
    root = Path(__file__).resolve().parent
    helper_path = root / "2026-11-14-r150-native-normal-form-graded-ssi-789f.py"
    spec = importlib.util.spec_from_file_location("r150_graded_ssi", helper_path)
    helper = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(helper)
    args.out.mkdir(parents=True, exist_ok=True)
    args.out = args.out.resolve()
    mapping = json.loads(args.mapping.read_text())
    nf_receipt = json.loads(args.nf_receipt.read_text())
    input_hash = helper.sha256_file(args.input)
    if (nf_receipt["status"] != "completed" or not nf_receipt["allSources"]
            or nf_receipt["sourceCount"] != 2195 or nf_receipt["targetCount"] != 9
            or nf_receipt["outputs"]["normal-forms.bin"]["sha256"] != input_hash
            or mapping["field"] != 31 or len(mapping["sources"]) != 2195
            or len(mapping["components"]) != 1034 or mapping["targets"] != list(range(2, 11))):
        raise ValueError("not the complete source-faithful original F31 normal forms")
    header, fixture = helper.runtime_header(args.singular, args.out)
    header_file = args.out / "runtime-graded-ssi-header.txt"
    header_file.write_text(header)
    source = root / "2026-11-14-r150-native-graded-module-gb-789f.cpp"
    arithmetic = root / "2026-11-14-r150-native-normal-form-789f.cpp"
    receipt = {
        "format": "r150-native-graded-module-gb-v1", "field": 31, "moduleOrder": "dp,c",
        "fullSourceCount": 2195, "targetCount": 9, "components": 1034, "maximumDegree": 45,
        "inputSHA256": input_hash, "mappingSHA256": helper.sha256_file(args.mapping),
        "nfReceiptSHA256": helper.sha256_file(args.nf_receipt),
        "cppSHA256": helper.sha256_file(source), "arithmeticSHA256": helper.sha256_file(arithmetic),
        "runnerSHA256": helper.sha256_file(Path(__file__)), "runtimeFixture": fixture,
        "secondsLimit": args.seconds, "softSeconds": args.soft_seconds,
        "memoryMiBLimit": args.memory_mib, "maximumSourcesRequested": args.max_sources,
        "status": "preparing", "outputs": {},
    }
    receipt_file = args.out / "native-gb-receipt.json"
    save = lambda: receipt_file.write_text(json.dumps(receipt, indent=2) + "\n")
    save()
    if args.binary is None:
        args.binary = args.out / "native-graded-gb"
        command = ["timeout", "--kill-after=10s", "30s", "prlimit", "--as=536870912", "--core=0", "--",
                   "g++", "-O3", "-std=c++17", str(source), "-o", str(args.binary)]
        result = subprocess.run(command, capture_output=True, text=True)
        if result.returncode != 0:
            receipt.update({"status": "compile-failed", "compileExit": result.returncode,
                            "compileOutput": result.stdout + result.stderr})
            save()
            print(result.stdout + result.stderr)
            raise SystemExit(1)
    receipt["binarySHA256"] = helper.sha256_file(args.binary)
    receipt["status"] = "running"
    save()
    prefix = args.out / "gb"
    command = ["timeout", "--kill-after=10s", f"{args.seconds}s", "prlimit",
               f"--as={args.memory_mib * 1024 * 1024}", "--core=0", "--", str(args.binary),
               str(args.input.resolve()), str(header_file), str(prefix), str(args.max_sources), str(args.soft_seconds)]
    print(json.dumps({"phase": "bounded-native-graded-gb-start", "secondsLimit": args.seconds,
                      "memoryMiBLimit": args.memory_mib, "softSeconds": args.soft_seconds}), flush=True)
    before = time.monotonic()
    result = subprocess.run(command, capture_output=True, text=True)
    elapsed = time.monotonic() - before
    (args.out / "native-gb.log").write_text(result.stdout + result.stderr)
    events = []
    for line in result.stdout.splitlines():
        try:
            events.append(json.loads(line))
        except ValueError:
            pass
    last = events[-1] if events else None
    complete = result.returncode == 0 and last and last.get("status") == "native-univariate-gb-complete"
    prefix_only = result.returncode == 0 and last and last.get("status") == "native-univariate-gb-prefix-only"
    receipt.update({"status": "completed" if complete else "prefix-only" if prefix_only else "failed-or-incomplete",
                    "exitCode": result.returncode, "elapsedSeconds": elapsed, "nativeStatistics": last})
    for suffix in ["operations.bin", "basis.ssi", "basis-metadata.json"]:
        file = Path(str(prefix) + "-" + suffix)
        if file.exists():
            receipt["outputs"][suffix] = {"file": str(file), "bytes": file.stat().st_size,
                                           "sha256": helper.sha256_file(file)}
    receipt["sourceIdentity"] = (
        "Input nodes 1..2195 are the original numbered normal-form sources. Each arithmetic node is "
        "previous-current minus coefficient*s^exponent*saved-basis. Swaps and stores are recorded. "
        "Final records give the constant normalization of each distinct-leading-component row. "
        "No parameter polynomial is inverted. Only status=completed spans all original 2195 sources."
    )
    save()
    print(result.stdout)
    if result.stderr:
        print(result.stderr)
    print(json.dumps({"status": receipt["status"], "elapsedSeconds": elapsed,
                      "nativeStatistics": last, "outputs": receipt["outputs"]}))
    if not complete:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
