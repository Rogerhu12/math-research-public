#!/usr/bin/env python3
"""Validate saved read-only transport observations without making Git calls.

This consumer does not inspect credentials or environment variables and cannot
fetch, pull, push, write Git configuration, or change the object store.
"""
import argparse
import hashlib
import json
from pathlib import Path


def digest(raw):
    return hashlib.sha256(raw).hexdigest()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--inputs', type=Path, required=True)
    parser.add_argument('--out', type=Path, required=True)
    args = parser.parse_args()
    raw = args.inputs.read_bytes()
    inputs = json.loads(raw)
    checks = []

    def check(name, condition):
        if not condition:
            raise ValueError(name)
        checks.append(name)

    local = inputs['config_observation']
    check('exact repository path', local['repository'] ==
          '/workspace/scratch/d1aa462cfc02/math-research')
    check('effective filter came from local config',
          local['effective']['remote.origin.partialclonefilter'] ==
          'file:.git/config\tblob:limit=10485760')
    check('effective negotiation came from local config',
          local['effective']['fetch.negotiationAlgorithm'] ==
          'file:.git/config\tskipping')
    former = inputs['earlier_filter_write']['entries']
    check('earlier actual blob-none write exit zero', any(
        row['key'] == 'remote.origin.partialclonefilter' and
        row['new'] == 'blob:none' and row['exitcode'] == 0
        for row in former))
    changed = inputs['maintenance_filter_write']
    check('subsequent actual maintenance write exit zero',
          changed['exitcode'] == 0 and changed['command'][-4:] ==
          ['config', '--local', 'remote.origin.partialclonefilter',
           'blob:limit=10485760'])
    check('configuration overwrite followed earlier setting',
          inputs['earlier_filter_write']['utc'] <
          inputs['maintenance_report_start_utc'] < local['observed_utc'])
    network = inputs['authenticated_lsremote']
    check('read-only network command only ls-remote', network['argv'] ==
          ['git', '-c', 'protocol.version=2', 'ls-remote', 'origin',
           'refs/heads/main'])
    check('read-only ls-remote exit zero', network['exit_code'] == 0)
    packet = inputs['packet_trace']
    packet_path = Path(packet['file'])
    if not packet_path.is_absolute():
        packet_path = args.inputs.parent / packet_path
    text = packet_path.read_text()
    check('complete sanitized packet trace SHA', digest(text.encode()) ==
          packet['sha256'])
    check('protocol version two actually advertised',
          'git< version 2\n' in text)
    check('server filter capability actually advertised',
          'git< fetch=shallow wait-for-done filter\n' in text)
    check('only ls-refs command in trace',
          'command=ls-refs' in text and 'command=fetch' not in text)
    check('no HTTP header trace', 'Authorization:' not in text and
          '=> Send header:' not in text and '<= Recv header:' not in text)
    check('no credential token in any archived observation',
          'github_pat_' not in raw.decode() + text and
          'ghp_' not in raw.decode() + text)

    result = {
        'schema': 'saved-read-only-git-transport-evidence-v1',
        'finished': True,
        'input_sha256': digest(raw),
        'source_sha256': digest(Path(__file__).read_bytes()),
        'checks': checks,
        'check_count': len(checks),
        'configuration_fact': {
            'earlier_blob_none_write_utc': inputs['earlier_filter_write']['utc'],
            'later_maintenance_start_utc': inputs['maintenance_report_start_utc'],
            'later_maintenance_command': changed['command'],
            'later_maintenance_exitcode': changed['exitcode'],
            'observed_effective_config': local,
            'conclusion': 'The maintenance script actually changed blob:none '
                          'back to the 10 MiB filter after the earlier setting. '
                          'An environment rollback is not needed to explain '
                          'this observed difference.'},
        'protocol_fact': {
            'network_exitcode': network['exit_code'],
            'network_wall_seconds': network['wall_seconds'],
            'remote_head': network['stdout'].strip(),
            'advertised_fetch_capability': 'shallow wait-for-done filter',
            'protocol': 2,
            'packet_trace_sha256': packet['sha256']},
        'performance_observations': inputs['performance_observations'],
        'command_override_proposal': [
            'git', '-c', 'remote.origin.partialclonefilter=blob:none',
            '-c', 'fetch.negotiationAlgorithm=skipping',
            'pull', '--rebase', '--no-stat', 'origin', 'main'],
        'limits': [
            'This consumer and its input probes make no Git writer calls.',
            'The original protocol probe was ls-remote, not fetch.',
            'No have/ACK negotiation was observed; this does not prove the '
            'cause of the repeated full-sized duplicate fetch packs.',
            'No performance improvement is attributed to a configuration '
            'change. Concurrent remote commits and maintenance latency also '
            'affect rejected pushes.',
            'No new pull or configuration edit was performed by this agent.',
            'Future instrumentation should apply only to the parent-owned '
            'normal pull if large transfers recur.'],
    }
    args.out.write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps({'finished': True, 'checks': len(checks),
                      'output': str(args.out),
                      'sha256': digest(args.out.read_bytes())}))


if __name__ == '__main__':
    main()
