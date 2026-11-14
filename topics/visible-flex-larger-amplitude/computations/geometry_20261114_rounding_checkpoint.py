#!/usr/bin/env python3
"""Collect actual fixed-g R225 rounding replays without changing their fields."""
import argparse
import gzip
import hashlib
import json
from pathlib import Path


def read(path):
    raw = path.read_bytes()
    return json.loads(gzip.decompress(raw) if path.suffix == '.gz' else raw)


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    p = argparse.ArgumentParser()
    p.add_argument('--run', action='append', type=Path, required=True)
    p.add_argument('--profile', type=Path, required=True)
    p.add_argument('--fft-check', type=Path, required=True)
    p.add_argument('--entry-check', type=Path, required=True)
    p.add_argument('--summary-out', type=Path, required=True)
    p.add_argument('--checkpoint-out', type=Path, required=True)
    p.add_argument('--profile-out', type=Path, required=True)
    a = p.parse_args()
    runs = [(path, read(path)) for path in a.run]
    runs.sort(key=lambda pair: pair[1]['numerical_parameters']['M'])
    fingerprints = {d['metric_identity_sha256'] for _, d in runs}
    if len(fingerprints) != 1:
        raise ValueError('These are not replays of one fixed metric')
    if any(d['status'] != 'success' or d['reached_s'] != d['target_s'] for _, d in runs):
        raise ValueError('A replay did not reach the fixed endpoint')
    result = dict(scope='Actual same-g cold replays of an open prefix only; no closed diameter, all-t reach, or exact infinite-field existence assertion.',
                  metric_identity_sha256=next(iter(fingerprints)),
                  fixed_profile=read(a.profile),
                  fixed_profile_file_sha256=sha(a.profile),
                  fft_kernel_comparison=read(a.fft_check),
                  original_entry_design_diagnostic=read(a.entry_check),
                  runs=[])
    for path, d in runs:
        result['runs'].append(dict(path=path.name, sha256=sha(path), status=d['status'],
                                  reached_s=d['reached_s'], target_s=d['target_s'],
                                  numerical_parameters=d['numerical_parameters'],
                                  summary=d['summary'], endpoint=d['rows'][-1],
                                  stored_station_count=len(d['state_locations']),
                                  source_sha256=d['source_sha256'],
                                  fft_source_sha256=d['fft_source_sha256'],
                                  seconds=d['seconds'], calls=d['calls']))
    highest_path, highest = runs[-1]
    checkpoint = dict(highest)
    checkpoint['checkpoint_scope'] = 'Complete final Fourier state and full scalar metric; rows before the endpoint are omitted, while their original computed summary is retained. Recompute all stations with the cold replay source.'
    checkpoint['full_replay_sha256'] = sha(highest_path)
    checkpoint['full_replay_station_count'] = len(highest['state_locations'])
    for key in ('rows', 'coefficient_states', 'state_locations'):
        checkpoint[key] = highest[key][-1:]
    for path in (a.summary_out, a.checkpoint_out, a.profile_out):
        path.parent.mkdir(parents=True, exist_ok=True)
    a.summary_out.write_text(json.dumps(result, indent=2)+'\n')
    encoded = (json.dumps(checkpoint, indent=2)+'\n').encode()
    a.checkpoint_out.write_bytes(gzip.compress(encoded, mtime=0))
    a.profile_out.write_bytes(a.profile.read_bytes())
    print(json.dumps(dict(metric_identity_sha256=result['metric_identity_sha256'],
                          summary_sha256=sha(a.summary_out),
                          checkpoint_sha256=sha(a.checkpoint_out),
                          profile_sha256=sha(a.profile_out),
                          endpoint=highest['rows'][-1])))


if __name__ == '__main__':
    main()
