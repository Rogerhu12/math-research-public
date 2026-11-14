#!/usr/bin/env python3
"""Serialize the existing R150NF31 coefficients through Singular's SSI format.

No normal form is recomputed.  The SSI version, token limit, option words and
ring declaration are obtained from the currently selected Singular executable.
Its complete small fixture payload is checked before emitting any large input.

The scalar/module layout is the one in Singular/links/ssiLink.cc, functions
ssiWritePoly_R, ssiWriteIdeal_R, ssiReadPoly_R and case 10 of ssiRead1.  In this
specific prime field, one term is: coefficient, component, exponent of s.
"""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path
import struct
import subprocess
import time


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        while b := f.read(1024 * 1024):
            h.update(b)
    return h.hexdigest()


def bounded_singular(executable: str, script: Path, seconds: int, mib: int):
    return subprocess.run(
        ["timeout", "--kill-after=10s", f"{seconds}s", "prlimit",
         f"--as={mib * 1024 * 1024}", "--core=0", "--", executable,
         "-q", str(script)],
        capture_output=True, text=True,
    )


def runtime_header(executable: str, out: Path) -> tuple[str, dict]:
    fixture = out / "ssi-runtime-fixture.ssi"
    script = out / "ssi-runtime-fixture.sing"
    script.write_text(
        "ring R=31,s,(c,dp);\n"
        "module A=(30*s^2+16)*gen(1)+7*gen(1034),2*s*gen(2);\n"
        f'link ell="ssi:w {fixture}";\n'
        'write(ell,A);close(ell);\n'
        'if(nrows(A)!=1034||ncols(A)!=2){print("SSI_FIXTURE_FAILED");quit;}\n'
        'print("SSI_RUNTIME_FIXTURE_WRITTEN");\nquit;\n'
    )
    r = bounded_singular(executable, script, 10, 128)
    (out / "ssi-runtime-fixture.log").write_text(r.stdout + r.stderr)
    if (r.returncode != 0 or "SSI_RUNTIME_FIXTURE_WRITTEN" not in r.stdout.splitlines()
            or any(line.lstrip().startswith("?") for line in r.stdout.splitlines())):
        raise ValueError("current Singular fixture did not complete: " + r.stdout + r.stderr)
    text = fixture.read_text()
    marker = "\n10 "
    if marker not in text:
        raise ValueError("unsupported SSI module envelope in current runtime")
    head, body = text.split(marker, 1)
    tokens = [int(t) for t in ("10 " + body).split()]
    expected = [10, 1034, 2, 3, 30, 1, 2, 16, 1, 0, 7, 1034, 0, 1, 2, 2, 1]
    if tokens != expected:
        raise ValueError("current SSI coefficient, component, exponent or module format differs")
    header_lines = head.splitlines()
    if len(header_lines) != 2 or not header_lines[0].startswith("98 ") or not header_lines[1].startswith("15 "):
        raise ValueError("unsupported SSI ring/version header")
    return head + "\n", {
        "header": header_lines,
        "fixtureSHA256": sha256_file(fixture),
        "fixtureModuleTokens": tokens,
        "runtimeExecutable": executable,
        "sourceReference": "https://github.com/Singular/Singular/blob/Release-4-4-0/Singular/links/ssiLink.cc",
        "fixtureStatus": "exact-current-runtime-payload-verified",
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--mapping", type=Path, required=True)
    parser.add_argument("--out", type=Path, required=True)
    parser.add_argument("--singular", required=True)
    parser.add_argument("--probe-seconds", type=int, default=0)
    parser.add_argument("--probe-memory-mib", type=int, default=1024)
    args = parser.parse_args()
    if args.probe_seconds < 0 or args.probe_memory_mib <= 0:
        raise ValueError("invalid probe limits")
    args.out.mkdir(parents=True, exist_ok=True)
    args.out = args.out.resolve()
    mapping = json.loads(args.mapping.read_text())
    if mapping["field"] != 31 or len(mapping["components"]) != 1034:
        raise ValueError("not the original F31 quotient mapping")
    header, fixture = runtime_header(args.singular, args.out)
    started = time.monotonic()
    receipt = {
        "format": "r150-native-normal-forms-ssi-v1", "field": 31,
        "inputFile": str(args.input.resolve()), "inputSHA256": sha256_file(args.input),
        "mappingFile": str(args.mapping.resolve()), "mappingSHA256": sha256_file(args.mapping),
        "sourceSHA256": sha256_file(Path(__file__)), "runtimeFixture": fixture,
        "status": "serializing", "normalFormsRecomputed": False,
    }
    receipt_file = args.out / "ssi-receipt.json"
    save = lambda: receipt_file.write_text(json.dumps(receipt, indent=2) + "\n")
    save()
    output = args.out / "normal-forms.ssi"
    scalar_count = 0
    max_degree = -1
    source_rows = []
    target_numbers = []
    with args.input.open("rb") as f, output.open("w", buffering=1024 * 1024) as out:
        def read(n):
            b = f.read(n)
            if len(b) != n:
                raise ValueError("truncated normal-form binary")
            return b

        def u32():
            return struct.unpack("<I", read(4))[0]

        def u16():
            return struct.unpack("<H", read(2))[0]

        if read(8) != b"R150NF31":
            raise ValueError("wrong normal-form binary magic")
        ns, nt, nc = u32(), u32(), u32()
        if (ns, nt, nc) != (len(mapping["sources"]), len(mapping["targets"]), 1034):
            raise ValueError("binary and original mapping dimensions differ")
        out.write(header)
        for group, size in (("source", ns), ("target", nt)):
            out.write(f"10 {nc} {size}\n")
            for j in range(size):
                raw, target, count = u32(), u16(), u32()
                expected_raw = mapping["sources"][j]["raw"] if group == "source" else 0
                expected_target = 0 if group == "source" else mapping["targets"][j]
                if (raw, target) != (expected_raw, expected_target):
                    raise ValueError("binary original-source/target identity mismatch")
                (source_rows if group == "source" else target_numbers).append(raw if group == "source" else target)
                entries = []
                terms = 0
                previous = 0
                for _ in range(count):
                    component, length = u16(), read(1)[0]
                    coefficients = read(length)
                    if not previous < component <= nc or not 1 <= length <= 46:
                        raise ValueError("bad component order or parameter degree")
                    if not coefficients[-1] or any(c >= 31 for c in coefficients):
                        raise ValueError("noncanonical prime-field polynomial")
                    previous = component
                    terms += sum(c != 0 for c in coefficients)
                    max_degree = max(max_degree, length - 1)
                    entries.append((component, coefficients))
                # SSI does not sort a vector after reading it. For (c,dp), the
                # required order is increasing component then decreasing s-degree.
                out.write(str(terms) + " ")
                for component, coefficients in entries:
                    out.write(" ".join(f"{coefficients[k]} {component} {k}"
                                       for k in range(len(coefficients) - 1, -1, -1)
                                       if coefficients[k]))
                    out.write(" ")
                out.write("\n")
                scalar_count += terms
        if f.read(1):
            raise ValueError("trailing normal-form binary data")
    receipt.update({
        "status": "serialized", "sources": ns, "targets": nt, "components": nc,
        "sourceRows": source_rows, "targetNumbers": target_numbers,
        "nonzeroScalarCoefficients": scalar_count, "maximumParameterDegree": max_degree,
        "serializationSeconds": time.monotonic() - started,
        "output": {"file": str(output), "bytes": output.stat().st_size, "sha256": sha256_file(output)},
    })
    save()
    if args.probe_seconds:
        probe = args.out / "ssi-load-probe.sing"
        probe.write_text(
            "ring R=31,s,(c,dp);\n"
            f'link nativeInput="ssi:r {output}";\n'
            'module Reduced=read(nativeInput);\n'
            'print("SSI_REDUCED_LOADED");\n'
            'module Target=read(nativeInput);close(nativeInput);\n'
            # Reapply desired options after SSI restores its captured option word.
            'option(redSB);\n'
            f'if(nrows(Reduced)!=1034||ncols(Reduced)!={ns}||nrows(Target)>1034||ncols(Target)!={nt})'
            '{print("SSI_NATIVE_DIMENSIONS_FAILED");quit;}\n'
            'print("SSI_NATIVE_ROWS="+string(nrows(Reduced)));\n'
            'print("SSI_NATIVE_COLUMNS="+string(ncols(Reduced)));\n'
            'print("SSI_TARGET_COLUMNS="+string(ncols(Target)));\n'
            'print("SSI_NATIVE_INPUT_LOADED");\nquit;\n'
        )
        before = time.monotonic()
        result = bounded_singular(args.singular, probe, args.probe_seconds, args.probe_memory_mib)
        elapsed = time.monotonic() - before
        (args.out / "ssi-load-probe.log").write_text(result.stdout + result.stderr)
        lines = [s.strip() for s in result.stdout.splitlines()]
        error = any(s.startswith("?") or s.endswith("_FAILED") for s in lines)
        completed = result.returncode == 0 and "SSI_NATIVE_INPUT_LOADED" in lines and not error
        receipt["loadProbe"] = {
            "secondsLimit": args.probe_seconds, "memoryMiBLimit": args.probe_memory_mib,
            "exitCode": result.returncode, "elapsedSeconds": elapsed, "singularError": error,
            "status": "completed" if completed else "failed-or-incomplete", "stdout": result.stdout,
        }
        receipt["status"] = "serialized-and-loaded" if completed else "serialized-load-incomplete"
        save()
    print(json.dumps({k: v for k, v in receipt.items() if k not in {"sourceRows", "targetNumbers", "runtimeFixture"}}))
    if args.probe_seconds and receipt["loadProbe"]["status"] != "completed":
        raise SystemExit(1)


if __name__ == "__main__":
    main()
