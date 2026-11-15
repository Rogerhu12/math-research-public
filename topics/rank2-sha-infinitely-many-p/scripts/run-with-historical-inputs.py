#!/usr/bin/env python3
"""Run a historical topic script in temporary storage with verified old inputs.

This utility never restores data into the working checkout. See the adjacent
rule-15 provenance note. Historical data are deleted with TemporaryDirectory.
"""
import argparse
import hashlib
import json
import pathlib
import re
import shutil
import subprocess
import sys
import tempfile

TOPIC = pathlib.Path(__file__).resolve().parents[1]
ROOT = TOPIC.parents[1]
PREFIX = "topics/rank2-sha-infinitely-many-p/"
MANIFESTS = [TOPIC / "ci/removed-recomputable-output-manifest.json",
             TOPIC / "ci/removed-recomputable-dependent-output-manifest.json"]
REPOSITORY = "https://github.com/Rogerhu12/math-research-public.git"

def checked_relative(value):
    p = pathlib.PurePosixPath(value)
    if p.is_absolute() or ".." in p.parts:
        raise ValueError("Paths must stay in the temporary topic checkout: " + value)
    if str(p).startswith(PREFIX):
        p = pathlib.PurePosixPath(str(p)[len(PREFIX):])
    return p

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", action="append", default=[],
                        help="Restore only this removed input; repeat as needed.")
    parser.add_argument("--no-historical-inputs", action="store_true")
    parser.add_argument("--emit-output",
                        help="After execution, print this newly generated topic file.")
    parser.add_argument("script", help="Topic-relative or repository-relative script.")
    parser.add_argument("args", nargs=argparse.REMAINDER)
    options = parser.parse_args()
    manifests = [json.loads(path.read_text(encoding="utf-8")) for path in MANIFESTS]
    sources = {m["source_commit"] for m in manifests}
    if len(sources) != 1:
        raise ValueError("These manifests must share their immutable audit snapshot")
    source = sources.pop()
    all_entries = [entry for m in manifests for entry in m["entries"]]
    if len({entry["path"] for entry in all_entries}) != len(all_entries):
        raise ValueError("Duplicate historical input provenance")
    if not re.fullmatch(r"[0-9a-f]{40}", source):
        raise ValueError("Invalid immutable source commit")
    script = checked_relative(options.script)
    if script.parts[0] != "scripts" or not (TOPIC / script).is_file():
        raise ValueError("Expected an existing topic script")
    if options.no_historical_inputs and options.input:
        raise ValueError("Choose either explicit inputs or no historical inputs")
    wanted = {str(checked_relative(x)) for x in options.input}
    entries = []
    for entry in all_entries:
        if not entry["path"].startswith(PREFIX):
            raise ValueError("Manifest escaped topic")
        rel = str(checked_relative(entry["path"]))
        if not options.no_historical_inputs and (not wanted or rel in wanted):
            entries.append(entry)
    found = {str(checked_relative(x["path"])) for x in entries}
    if wanted - found:
        raise ValueError("Unknown removed inputs: " + ", ".join(sorted(wanted - found)))
    # Positional file destinations are relative to the temporary root, never to
    # the user's checkout. Absolute/traversing paths are deliberately refused.
    arguments = options.args[1:] if options.args[:1] == ["--"] else options.args
    for arg in arguments:
        if pathlib.PurePosixPath(arg).is_absolute() or ".." in pathlib.PurePosixPath(arg).parts:
            raise ValueError("Argument points outside temporary checkout: " + arg)
    emit = checked_relative(options.emit_output) if options.emit_output else None

    with tempfile.TemporaryDirectory(prefix="rank2-historical-check-") as temp:
        temporary = pathlib.Path(temp)
        runroot = temporary / "root"
        runtopic = runroot / PREFIX
        shutil.copytree(TOPIC, runtopic, ignore=shutil.ignore_patterns("__pycache__"))
        if (ROOT / "README.md").is_file():
            shutil.copy2(ROOT / "README.md", runroot / "README.md")
        historical = temporary / "source.git"
        initialized = False

        def read_historical(entry):
            nonlocal initialized
            expression = source + ":" + entry["path"]
            # Read objects already present without changing the current branch.
            attempt = subprocess.run(["git", "show", expression], cwd=ROOT,
                                     stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)
            if attempt.returncode == 0:
                data = attempt.stdout
            else:
                if not initialized:
                    subprocess.run(["git", "init", "--bare", "--quiet", str(historical)], check=True)
                    for key, value in [("remote.origin.url", REPOSITORY),
                                       ("remote.origin.promisor", "true"),
                                       ("remote.origin.partialclonefilter", "blob:none")]:
                        subprocess.run(["git", "-C", str(historical), "config", key, value], check=True)
                    subprocess.run(["git", "-C", str(historical), "fetch", "--quiet",
                                    "--filter=blob:none", "--depth=1", "origin", source], check=True)
                    initialized = True
                data = subprocess.check_output(["git", "-C", str(historical), "show", expression])
            if len(data) != entry["bytes"] or hashlib.sha256(data).hexdigest() != entry["sha256"]:
                raise RuntimeError("Historical SHA256/size mismatch: " + entry["path"])
            return data

        for entry in entries:
            target = runroot / entry["path"]
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(read_historical(entry))
        if emit:
            output = runtopic / emit
            output.parent.mkdir(parents=True, exist_ok=True)
            # An emitted file must be produced by this execution, not merely be
            # a restored historical certificate.
            if output.exists():
                output.unlink()
        command = {
            ".js": ["node"], ".py": [sys.executable],
            ".sage": ["sage"], ".sh": ["bash"],
        }.get(script.suffix)
        if command is None:
            raise ValueError("Unsupported engine; use the historical workflow for " + script.suffix)
        print("RANK2_HISTORICAL_INPUTS " + json.dumps({
            "source_commit": source, "restored_inputs": len(entries),
            "script": PREFIX + str(script), "args": arguments,
            "temporary_only": True, "outputs_persisted": False,
        }), file=sys.stderr)
        result = subprocess.run(command + [str(runtopic / script)] + arguments,
                                cwd=runroot, stdout=subprocess.PIPE if emit else None)
        if result.returncode:
            if emit and result.stdout:
                sys.stderr.buffer.write(result.stdout)
            return result.returncode
        if emit:
            if not output.is_file():
                raise RuntimeError("The script did not generate the requested output")
            if result.stdout:
                sys.stderr.buffer.write(result.stdout)
            sys.stdout.buffer.write(output.read_bytes())
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
