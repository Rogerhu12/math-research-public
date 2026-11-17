#!/usr/bin/env python3
"""Record a completed true same-metric prefix--tail refinement without arrays."""
import argparse
import gzip
import hashlib
import json
from pathlib import Path
import shlex


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def scalars(value):
    return {key: item for key, item in value.items()
            if not isinstance(item, (dict, list))}


def load(path):
    raw = Path(path).read_bytes()
    return json.loads(gzip.decompress(raw) if str(path).endswith('.gz') else raw)


def scalar_tree(value):
    """Keep named scalar evidence; omit every derived sequence recursively."""
    if isinstance(value, dict):
        return {key: scalar_tree(item) for key, item in value.items()
                if not isinstance(item, list)}
    return value


def indexed(value):
    return {str(i): item for i, item in enumerate(value)}


def checkpoint_info(path):
    cp = load(path)
    chunks = {}
    for chunk in cp['pp_coefficient_chunks']:
        source = path.parent / chunk['file']
        assert sha(source) == chunk['sha256'], source
        chunks[chunk['file']] = {k: v for k, v in chunk.items() if k != 'file'}
    return cp, dict(file=path.name, sha256=sha(path), chunk_hashes=chunks)


def outcome(summary, cp):
    keys = ('solver_success', 'nodes', 'message', 'max_rms', 'max_bc',
            'gauge_amplitude', 'meridian_length', 'seconds', 'tail_calls',
            'actual_primary_amplitude', 'worker_returncode_after_close')
    out = {key: summary[key] for key in keys if key in summary}
    out.update(config=summary['config'],
               prefix=scalars(summary['summary']),
               seam=scalars(summary['tail_seam']),
               domain_newton=summary['domain_newton'],
               physical_profile=summary['physical_profile'],
               parameters=indexed(cp['parameters']),
               central_correction_scales=indexed(cp['central_correction_scales']),
               core=scalars(cp['core_summary']))
    return out


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--prefix', type=Path, required=True)
    parser.add_argument('--input-prefix', type=Path, required=True)
    parser.add_argument('--out', type=Path, required=True)
    args = parser.parse_args()
    stem = args.prefix
    summary_path = stem.with_name(stem.name + '-summary.json')
    previous_path = args.input_prefix.with_name(args.input_prefix.name + '-summary.json')
    summary, previous = load(summary_path), load(previous_path)
    cp, cp_info = checkpoint_info(stem.with_suffix('.json.gz'))
    old_cp, old_cp_info = checkpoint_info(args.input_prefix.with_suffix('.json.gz'))
    assert summary['solver_success'] and previous['solver_success']
    assert cp['config']['actual_nonlinear_tail'] and old_cp['config']['actual_nonlinear_tail']
    assert cp['fixed_metric'] and cp['config']['fixed_metric']
    assert cp['physical_profile'] == old_cp['physical_profile'] == summary['fixed_physical_profile']
    assert cp['physical_port_sha256'] == old_cp['physical_port_sha256']
    assert summary['input_checkpoint_sha256'] == old_cp_info['sha256']
    assert summary['seed']['complete_map_projection_error'] < 2e-10
    assert max(summary['seed']['complete_core_identity_error'].values()) < 2e-10
    assert summary['max_bc'] <= cp['config']['bc_tol']
    assert summary['tail_seam']['tail_converged']
    tail_responses = {}
    for path in sorted(stem.parent.glob(stem.name + '-tail_*.json.gz')):
        raw = load(path)
        response = raw['response']
        history = response['history']
        tail_responses[path.name] = dict(
            sha256=sha(path), converged=response['converged'],
            residual=response['residual'],
            request_jacobian=raw['request']['jacobian'],
            request_audit=raw['request']['audit'],
            final_iteration=history[-1] if history else None,
            audit=response['audit'])
    before, after = outcome(previous, old_cp), outcome(summary, cp)
    result = dict(
        scope=f"Completed true nonlinear prefix--tail M{old_cp['config']['modes']}-to-M{cp['config']['modes']} refinement at the identical physical metric. Finite sampled validation only; no positive circle homotopy, full closed family, continuous error bound or arbitrary-epsilon construction is asserted.",
        collector_sha256=sha(__file__),
        fixed_physical_profile=cp['physical_profile'],
        physical_port_sha256=cp['physical_port_sha256'],
        input_summary_sha256=sha(previous_path), output_summary_sha256=sha(summary_path),
        original=before, refinement=after,
        observed_ratios={key: after['prefix'][key] / before['prefix'][key]
                         for key in ('metric_l1', 'flow_defect', 'darboux_l1')},
        input_checkpoint=old_cp_info, output_checkpoint=cp_info,
        seed=scalar_tree(summary['seed']),
        actual_outer_checks={str(i): row for i, row in enumerate(summary['actual_outer_checks'])},
        tail_initialization=summary['tail_initialization'],
        tail_responses=tail_responses,
        original_driver_sha256=summary['script_sha256'],
        original_coupler_sha256=summary['original_coupler_sha256'],
        sparse_helper_sha256=summary['sparse_helper_sha256'],
        periodic_engine_sha256=summary['periodic_engine_sha256'],
        tail_source_sha256=summary['tail_source_sha256'],
        actual_command=shlex.join(summary['command']),
        run_file_hashes={path.name: sha(path) for path in sorted(stem.parent.glob(stem.name + '*'))
                         if path.is_file()},
        log_sha256=sha(stem.parent.with_suffix('.log')),
        data_policy='Physical parameters and scalar audits only. Checkpoint fields, tail states and all core certificate tables remain scratch-only; SHA-256 identities are retained.')
    if 'coefficient_certificate' in summary:
        result['coefficient_certificate'] = scalar_tree(summary['coefficient_certificate'])
    args.out.write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps(dict(bytes=args.out.stat().st_size, sha256=sha(args.out),
                          ratios=result['observed_ratios'])))


if __name__ == '__main__':
    main()
