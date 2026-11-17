#!/usr/bin/env python3
"""Retain scalar evidence for an actually solved new primary-width design."""
import argparse
import gzip
import hashlib
import json
from pathlib import Path
import shlex


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def load(path):
    raw = Path(path).read_bytes()
    return json.loads(gzip.decompress(raw) if str(path).endswith('.gz') else raw)


def scalars(value):
    if isinstance(value, dict):
        return {k: scalars(v) for k, v in value.items() if not isinstance(v, list)}
    return value


def checkpoint(path):
    record = load(path)
    chunks = {}
    for item in record.get('pp_coefficient_chunks', []):
        file = path.parent / item['file']
        if sha(file) != item['sha256']:
            raise ValueError('Checkpoint coefficient chunk mismatch: ' + str(file))
        chunks[item['file']] = item['sha256']
    return record, dict(file=str(path), sha256=sha(path), chunk_hashes=chunks)


def physical_core(record):
    parameters = record['parameters']
    scales = record['central_correction_scales']
    core = record['core_summary']
    certificate = core.get('control_certificate', {})
    result = scalars(core)
    result['parameters'] = {str(j): v for j, v in enumerate(parameters)}
    result['central_correction_scales'] = {str(j): v for j, v in enumerate(scales)}
    result['corrections'] = {str(j): scales[j] * parameters[j + 1]
                             for j in range(len(scales))}
    result['complete_control_certificate_sha256'] = hashlib.sha256(
        json.dumps(certificate, sort_keys=True, separators=(',', ':')).encode()).hexdigest()
    result['omitted_certificate_fields'] = ','.join(
        k for k, v in certificate.items() if isinstance(v, list))
    return result


def main():
    p = argparse.ArgumentParser(description=__doc__)
    for key in ('prefix', 'before-record', 'resource', 'out'):
        p.add_argument('--' + key, type=Path, required=True)
    p.add_argument('--previous-observability', type=Path)
    a = p.parse_args()
    row = load(a.prefix.with_suffix('.json'))
    previous = load(a.before_record)
    input_path = Path(row['arguments']['checkpoint'])
    old, old_identity = checkpoint(input_path)
    assert old_identity['sha256'] == row['input_checkpoint_sha256']
    assert old_identity['sha256'] == previous['output_checkpoint']['sha256']
    assert old['solver_success'] and old['fixed_metric']
    assert old['physical_profile'] == row['physical_profile']
    final_path = a.prefix.with_suffix('.json.gz')
    final = None
    final_identity = None
    if final_path.exists():
        final, final_identity = checkpoint(final_path)
        assert final['solver_success'] == row['success']
        assert final['physical_profile'] == old['physical_profile']
        assert final['parameters'] == row['parameters']
        assert final['raw_control_anchor_modes'] == old['raw_control_anchor_modes']
        assert final['plateau_settings'] == row['new_primary_design']['new_settings']
    resource = load(a.resource)
    assert resource['status'] == 'observed_terminal'
    assert resource['child_returncode'] == 0
    command = resource['command']
    loader = Path(command[command.index('--loader') + 1]).resolve()
    dependencies = ('refine_fixed_raw_n4.py', 'refine_fixed_large_radius.py',
                    'raw_fixed_core.py', 'raw_n4_free_complementary.py',
                    'raw_n4_complementary.py', 'tight_moment_interval_bounds.py',
                    'trace_domain_newton.py', 'large_radius_local_core.py',
                    'local_flatten_core.py', 'exact_core_lift.py',
                    'analytic_adaptive_core_jac.py')
    for name in dependencies:
        if sha(loader / name) != row['source_sha256'][name]:
            raise ValueError('Executed dependency changed after the solve: ' + name)
    driver = Path(__file__).with_name('solve_changed_primary_width.py')
    assert sha(driver) == row['new_primary_design']['wrapper_sha256']
    before = previous['after']
    result = dict(
        scope='A new complete primary flattening width at a fixed physical meridian/tail profile, using all old physical raw controls only as the initial guess. This is not same-core refinement. Finite nonlinear BVP and full sampled metric are reported separately; the boundary still uses the finite linear DN.',
        collector_sha256=sha(__file__), before_record_sha256=sha(a.before_record),
        input_checkpoint=old_identity, output_checkpoint=final_identity,
        physical_profile=old['physical_profile'],
        raw_control_anchor_modes=old['raw_control_anchor_modes'],
        before=dict(primary_transition=old['plateau_settings']['transition'],
                    nodes=before['nodes'], actual_q=before['actual_q'],
                    max_rms=before['max_rms'], max_bc=before['max_bc'],
                    summary=before['summary']),
        after={k: row[k] for k in ('success', 'message', 'nodes', 'actual_q',
                                   'max_rms', 'max_bc', 'seconds', 'domain_newton')
               if k in row},
        changed_design=scalars(row['new_primary_design']),
        starting_checkpoint_embedding=row['starting_checkpoint_embedding'],
        coefficient_certificate=scalars(row.get('coefficient_certificate', {})),
        source_sha256=row['source_sha256'],
        executed_loader_root=str(loader),
        checked_executed_dependencies={name: row['source_sha256'][name]
                                       for name in dependencies},
        actual_command=shlex.join(resource['command']),
        resource=scalars(resource), resource_sha256=sha(a.resource),
        output_sha256=sha(a.prefix.with_suffix('.json')),
        log_sha256=sha(a.prefix.with_suffix('.log')),
        newton_trace_sha256=sha(a.prefix.with_name(a.prefix.name + '-newton.jsonl')),
        complete_sampled_metric_below_1e_minus_6=False,
        data_policy='No meshes, fields, high-order derivative-bound arrays, or regenerable spectral tables are retained here. Full fields stay in scratch; only hashes, small physical controls and scalar diagnostics are stored.')
    if final:
        result['after']['core'] = physical_core(final)
        result['after']['settings'] = final['plateau_settings']
        result['after']['config'] = final['config']
    if 'summary' in row:
        result['after']['summary'] = scalars(row['summary'])
        result['complete_sampled_metric_below_1e_minus_6'] = row['summary']['metric_l1'] <= 1e-6
        result['new_design_ratios_to_old_design'] = {
            key: row['summary'][key] / before['summary'][key]
            for key in ('metric_l1', 'flow_defect', 'darboux_l1')}
    if a.previous_observability:
        result['previous_attempt_observability'] = dict(
            record_sha256=sha(a.previous_observability),
            record=scalars(load(a.previous_observability)),
            claim='An absent tool session with no observed return code or mathematical terminal is observability loss only.')
    a.out.write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps(dict(bytes=a.out.stat().st_size, sha256=sha(a.out))))


if __name__ == '__main__':
    main()
