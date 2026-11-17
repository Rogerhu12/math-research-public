#!/usr/bin/env python3
"""Extract a completed design terminal: scalar evidence, parameters and hashes."""
import argparse
import gzip
import hashlib
import json
from pathlib import Path


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def scalars(value):
    return {key: item for key, item in value.items() if not isinstance(item, (list, dict))}


def indexed(value):
    return {str(i): item for i, item in enumerate(value)}


def scalar_tree(value):
    if isinstance(value, dict):
        return {key: scalar_tree(item) for key, item in value.items() if not isinstance(item, list)}
    return value


def core_summary(value):
    out = scalars(value)
    if 'corrections' in value:
        out['corrections'] = indexed(value['corrections'])
    if 'control_certificate' in value:
        cert = value['control_certificate']
        out['control_certificate'] = scalars(cert)
        out['complete_control_certificate_sha256'] = hashlib.sha256(
            json.dumps(cert, sort_keys=True, separators=(',', ':')).encode()).hexdigest()
        out['omitted_certificate_fields'] = ','.join(
            sorted(key for key, item in cert.items() if isinstance(item, (list, dict))))
    return out


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--result', type=Path, required=True)
    parser.add_argument('--out', type=Path, required=True)
    parser.add_argument('--working-directory', type=Path)
    args = parser.parse_args()
    raw = json.loads(args.result.read_text())
    out = dict(scope='Terminal of the executed finite-prefix design, not a nonexistence claim. No unaccepted checkpoint is counted as an accepted continuation anchor.',
               collector_sha256=sha(__file__), arguments=raw['arguments'],
               result_sha256=sha(args.result), log_sha256=sha(args.result.with_suffix('.log')),
               seconds=raw['seconds'], source_sha256=raw['source_sha256'], rows={})
    for key in ('source_transforms', 'coefficient_certificate', 'complete_core_guard', 'driver_transforms'):
        if key in raw:
            out[key] = scalar_tree(raw[key])
    out['input_files'] = {}
    for key in ('profile', 'port', 'restart', 'previous'):
        if raw['arguments'].get(key):
            path = Path(raw['arguments'][key])
            if not path.is_absolute():
                path = (args.working_directory or args.result.parent) / path
            out['input_files'][key] = dict(path=str(path), sha256=sha(path))
    for i, row in enumerate(raw['rows']):
        result = scalars(row)
        for key in ('physical_profile', 'domain_newton', 'material_restart'):
            if key in row:
                result[key] = scalar_tree(row[key])
        for key in ('parameters',):
            if key in row:
                result[key] = indexed(row[key])
        for key in ('seed_core', 'core'):
            if key in row:
                result[key] = core_summary(row[key])
        if 'summary' in row:
            result['summary'] = scalars(row['summary'])
        for key in ('parameter_jac_checks', 'boundary_jac_checks'):
            if row.get(key):
                result[key] = {str(j): item for j, item in enumerate(row[key])}
        out['rows'][str(i)] = result
    out['checkpoints'] = {}
    for path in sorted(args.result.parent.glob(args.result.stem + '-lam*.json.gz')):
        cp = json.loads(gzip.decompress(path.read_bytes()))
        chunks = {}
        for chunk in cp['pp_coefficient_chunks']:
            assert sha(path.parent / chunk['file']) == chunk['sha256'], chunk['file']
            chunks[chunk['file']] = {key: item for key, item in chunk.items() if key != 'file'}
        out['checkpoints'][path.name] = dict(
            sha256=sha(path), solver_success=cp.get('solver_success'),
            chunk_hashes=chunks, physical_port_sha256=cp['physical_port_sha256'],
            physical_profile=cp['physical_profile'])
    trace = args.result.with_name(args.result.stem + '-newton.jsonl')
    if trace.exists():
        events = [json.loads(line) for line in trace.read_text().splitlines()]
        out['newton_trace'] = dict(sha256=sha(trace), events=len(events), final=events[-1])
    args.out.write_text(json.dumps(out, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps(dict(bytes=args.out.stat().st_size, sha256=sha(args.out))))


if __name__ == '__main__':
    main()
