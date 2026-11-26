#!/usr/bin/env python3
"""Read one existing driver error without rerunning a numerical calculation.

Publish only the error class, traceback source locations and their hashes.
Do not copy raw trace text, source statements, parameter vectors or arrays.
"""
import argparse
import hashlib
import json
from pathlib import Path
import re


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--work', type=Path, required=True)
    parser.add_argument('--run', type=Path, required=True)
    parser.add_argument('--expected-run-sha', required=True)
    parser.add_argument('--outdir', type=Path, required=True)
    args = parser.parse_args()
    work, run, out = args.work.resolve(), args.run.resolve(), args.outdir.resolve()
    if work not in run.parents or work not in out.parents:
        raise ValueError('The input and output must remain in the actual runner work directory')
    digest = sha(run)
    if digest != args.expected_run_sha:
        raise ValueError('The actual error run changed before inspection')
    record = json.loads(run.read_text())
    trace = record.get('traceback')
    if not isinstance(trace, str) or not trace or not record.get('error'):
        raise ValueError('No actual saved driver exception is available')
    matches = re.findall(r'^\s*File "([^"\n]+)", line (\d+), in ([^\n]+)$', trace, re.M)
    frames = {}
    for index, (name, line, function) in enumerate(matches):
        path = Path(name)
        frames['frame_%02d' % index] = dict(path=name, line=int(line), function=function,
            source_sha256=sha(path) if path.is_file() else None)
    error_type = re.match(r'^([A-Za-z_][A-Za-z_0-9.]*)\(', str(record['error']))
    result = dict(run=str(run), run_sha256=digest,
        error_type=error_type.group(1) if error_type else None,
        traceback_sha256=hashlib.sha256(trace.encode()).hexdigest(),
        frame_count=len(frames), frames=frames,
        solver_return_saved=bool(record.get('raw_return')),
        physical_return_saved=bool(record.get('physical_sha256')),
        numerical_calculation_performed=False, complete_surface=False)
    out.mkdir(parents=True, exist_ok=False)
    payload = dict(status='actual_saved_exception_inspected', result=result,
        source_hashes={str(Path(__file__).resolve()):sha(__file__)}, complete_surface=False)
    (out/'summary.json').write_text(json.dumps(payload, indent=2, allow_nan=False)+'\n')


if __name__ == '__main__':
    main()
