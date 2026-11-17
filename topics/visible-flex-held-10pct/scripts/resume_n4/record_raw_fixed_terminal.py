#!/usr/bin/env python3
"""Collect an unaccepted fixed-g raw-core refinement with original diagnostics."""
import argparse
import gzip
import hashlib
import json
from pathlib import Path
import re
import shlex


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def load(path):
    raw = Path(path).read_bytes()
    return json.loads(gzip.decompress(raw) if str(path).endswith('.gz') else raw)


def scalar_tree(value):
    if isinstance(value, dict):
        return {key: scalar_tree(item) for key, item in value.items()
                if not isinstance(item, list)}
    return value


def checkpoint_identity(path):
    cp = load(path)
    chunks = {}
    for chunk in cp.get('pp_coefficient_chunks', []):
        file = path.parent / chunk['file']
        if sha(file) != chunk['sha256']:
            raise ValueError('Checkpoint chunk mismatch: ' + str(file))
        chunks[chunk['file']] = {k: v for k, v in chunk.items() if k != 'file'}
    return cp, dict(sha256=sha(path), chunks=chunks)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ('prefix', 'input-record', 'resource', 'out'):
        parser.add_argument('--' + name, type=Path, required=True)
    args = parser.parse_args()
    stem = args.prefix
    row = load(stem.with_suffix('.json'))
    if row.get('success'):
        raise ValueError('This collector requires an unaccepted terminal')
    before = load(args.input_record)
    input_path = Path(row['arguments']['checkpoint'])
    cp, input_identity = checkpoint_identity(input_path)
    assert cp['solver_success']
    assert cp['fixed_metric']
    assert input_identity['sha256'] == row['input_checkpoint_sha256']
    assert cp['physical_profile'] == row['physical_profile']
    assert before['output_checkpoint']['sha256'] == input_identity['sha256']
    log = stem.with_suffix('.log')
    mesh_rows = {}
    for line in log.read_text().splitlines():
        found = re.fullmatch(r'\s*(\d+)\s+([\d.eE+\-]+)\s+([\d.eE+\-]+)\s+(\d+)\s+\(?([\d]+)\)?\s*', line)
        if found:
            i, rms, bc, nodes, added = found.groups()
            mesh_rows[i] = dict(displayed_rms=float(rms), displayed_bc=float(bc),
                                nodes=int(nodes), displayed_added_nodes=int(added))
    trace_path = stem.with_name(stem.name + '-newton.jsonl')
    trace = [json.loads(line) for line in trace_path.read_text().splitlines()]
    final_newton = [entry for entry in trace if entry['event'] == 'newton_end']
    domain_errors = [entry for entry in trace if entry['event'] == 'collocation_exception']
    output = None
    if stem.with_suffix('.json.gz').exists():
        final, identity = checkpoint_identity(stem.with_suffix('.json.gz'))
        output = dict(**identity, solver_success=final['solver_success'],
                      modes=final['config']['modes'],
                      physical_profile=final['physical_profile'],
                      parameters={str(i): v for i, v in enumerate(final['parameters'])},
                      scales={str(i): v for i, v in enumerate(final['central_correction_scales'])})
        assert not final['solver_success']
    resource = load(args.resource)
    result = dict(
        scope='Attempted fixed-lambda M refinement at the same complete raw core/map seed and physical metric. The original finite solve did not accept; no convergence, full metric result, or mathematical nonexistence follows.',
        collector_sha256=sha(__file__), input_record_sha256=sha(args.input_record),
        input_checkpoint=input_identity, input_result=before['after'],
        terminal=scalar_tree(row), physical_profile=cp['physical_profile'],
        homotopy=cp['plateau_settings']['homotopy'],
        raw_control_anchor_modes=cp['raw_control_anchor_modes'],
        output_failed_checkpoint=output,
        displayed_mesh_iterations=mesh_rows,
        last_newton=final_newton[-1] if final_newton else None,
        domain_rejection_examples=dict(first=domain_errors[0] if domain_errors else None,
                                       last=domain_errors[-1] if domain_errors else None),
        actual_command=shlex.join(resource['command']),
        resource=scalar_tree(resource), resource_sha256=sha(args.resource),
        raw_output_sha256=sha(stem.with_suffix('.json')),
        log_sha256=sha(log), newton_trace_sha256=sha(trace_path),
        data_policy='Complete fields and meshes remain scratch-only. Physical control values, scalar terminal diagnostics and source/output hashes are retained.')
    args.out.write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps(dict(bytes=args.out.stat().st_size, sha256=sha(args.out))))


if __name__ == '__main__':
    main()
