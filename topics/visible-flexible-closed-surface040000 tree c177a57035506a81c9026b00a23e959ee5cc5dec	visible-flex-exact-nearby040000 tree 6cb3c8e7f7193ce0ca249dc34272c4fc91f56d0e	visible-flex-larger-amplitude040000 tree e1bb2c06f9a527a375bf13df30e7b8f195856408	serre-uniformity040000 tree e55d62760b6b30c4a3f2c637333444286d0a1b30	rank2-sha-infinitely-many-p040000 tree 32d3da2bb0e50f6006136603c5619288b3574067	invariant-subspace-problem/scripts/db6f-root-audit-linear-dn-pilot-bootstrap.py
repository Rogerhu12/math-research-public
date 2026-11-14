#!/usr/bin/env python3
"""Closed first-packet identity check; no claim about an active pilot's goal."""
import argparse
import hashlib
import importlib.util
import json
from pathlib import Path


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--out', type=Path, required=True)
    a = ap.parse_args()
    topic = Path(__file__).resolve().parents[1]
    notes = topic/'notes'
    pre = '2026-11-09-db6f-'
    module_path = topic/'scripts/db6f-prefix-tail-linear-continuation-client-v2.py'
    assert hashlib.sha256(module_path.read_bytes()).hexdigest() == '6d278d78e275df2e0e66db3eb0edb592321fecc22c1c229eacd53f5869166d15'
    spec = importlib.util.spec_from_file_location('reviewed_pure_packet_helpers', module_path)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    guard_path = notes/(pre+'root-linear-dn-pilot-v2-01-guard-launch.json')
    assert m.identity(guard_path)['sha256'] == 'ac6ecb605fdb14d5af91e7cc00520d21673bab006d00f8108556b7876871e54d'
    guard = m.read(guard_path)
    for row in guard['bound_files']:
        m.verify(row)
    launch_path = Path(guard['original_pilot_launch']['path'])
    launch = m.read(launch_path)
    policy = m.read(launch['policy']['path'])
    seed = m.read(launch['bootstrap_packet']['path'])
    packet_path = Path(launch['record_prefix']+'_0001.json.gz')
    assert m.identity(packet_path)['sha256'] == 'de47db235f5c94d4848b745c2b9f36bde6e99b47d24af376b0818386f84a47f0'
    packet = m.read(packet_path)
    assert set(packet) == {'request', 'response', 'config', 'source_sha256'}
    assert m.canonical(packet['config']) == m.canonical(m.read(launch['config']['path']))
    assert m.canonical(packet['source_sha256']) == m.canonical(policy['source_sha256'])
    assert len(packet['source_sha256']) == 9
    assert set(packet['request']) == {'height', 'jacobian', 'audit'}
    assert packet['request']['jacobian'] is False and packet['request']['audit'] is False
    assert m.same_height(packet['request']['height'], seed['request']['height'])
    response = packet['response']
    parameters = response['checkpoint']['parameters']
    assert m.canonical(m.without_io(parameters)) == m.canonical(m.without_io(seed['response']['checkpoint']['parameters']))
    m.validate_response(response, 15, parameters, 2e-9, False, False)
    assert response['converged'] is True and response['residual'] < 2e-9
    assert response['heightJetJacobian'] is None and response['audit'] is None
    assert m.same_height(response['checkpoint']['cutHeight'], packet['request']['height'])
    assert parameters['depth'] == 864 and parameters['physicalDepth'] == 12
    assert len(response['checkpoint']['states']) == 865
    assert len(response['checkpoint']['rawStates']) == 13
    assert not m.same_height(packet['request']['height'], m.read(launch['target_packet']['path'])['request']['height'])
    files = [guard_path, launch_path, Path(launch['policy']['path']),
             Path(launch['bootstrap_packet']['path']), packet_path, module_path, Path(__file__)]
    report = dict(status='ACTUAL_NEW_PROCESS_BOOTSTRAP_FINITE_DN_ONLY',
                  actual_physical_call=1, source_bindings_rehashed=len(guard['bound_files']),
                  actual_response_source_count=9, exact_seed_request=True,
                  original_config_and_tolerance_preserved=True,
                  residual=response['residual'], history_length=len(response['history']),
                  last_iteration=response['history'][-1], state_shape=[865, 30], raw_shape=[13, 30],
                  finite_state_and_full_original_schema_valid=True,
                  requested_jacobian=False, requested_audit=False,
                  target_goal_success_not_inferred=True, pilot_tool_exit_not_observed=True,
                  files=[m.identity(p) for p in files],
                  scope='Closed bootstrap H0 response only. The active H1 pilot, prefix, final seam, geometry and G5 remain separate.')
    with a.out.open('x') as f:
        json.dump(report, f, ensure_ascii=False, indent=2)
        f.write('\n')
    print(json.dumps(dict(status=report['status'], residual=response['residual'],
                          input_count=len(guard['bound_files']), report=m.identity(a.out))))


if __name__ == '__main__':
    main()
