#!/usr/bin/env python3
"""Summarize saved, unfiltered R225 Frenet solves and retain a small BVP seed.

This is a consumer of actual completed output, not a replacement solver.
Only identical metric_identity_sha256 entrance runs form the refinement table.
The turn's first failed RHS trial is diagnostic, never an accepted solution.
"""
import argparse
import gzip
import hashlib
import json
import math
from pathlib import Path


def read(path):
    raw = path.read_bytes()
    return json.loads(gzip.decompress(raw)), hashlib.sha256(raw).hexdigest()


def main():
    p = argparse.ArgumentParser()
    p.add_argument('--work', type=Path, required=True)
    p.add_argument('--summary', type=Path, required=True)
    p.add_argument('--seed', type=Path, required=True)
    a = p.parse_args()
    entrance = []
    for name in ['r225-v030-L090-k020-M48.json.gz',
                 'r225-v030-L090-k020-M48-smallstep.json.gz',
                 'r225-v030-L090-k020-M64.json.gz',
                 'r225-v030-L090-k020-M96.json.gz',
                 'r225-v030-L090-k020-M128.json.gz']:
        d, h = read(a.work / name)
        entrance.append(dict(file=name, sha256=h,
                             **{k: d[k] for k in ('status', 'reached_s', 'target_s',
                               'metric_identity_sha256', 'numerical_parameters',
                               'summary', 'seconds', 'calls', 'source_sha256')}))
    assert len({r['metric_identity_sha256'] for r in entrance}) == 1
    m128, m128hash = read(a.work / entrance[-1]['file'])
    turn = []
    for mode in (96, 128):
        name = f'r225-turn-vm060-K4-M{mode}.json.gz'
        d, h = read(a.work / name)
        turn.append(dict(file=name, sha256=h,
                         **{k: d[k] for k in ('status', 'reached_s', 'target_s',
                            'metric_identity_sha256', 'numerical_parameters',
                            'summary', 'seconds', 'calls', 'source_sha256')}))
    assert len({r['metric_identity_sha256'] for r in turn}) == 1
    t128, t128hash = read(a.work / turn[-1]['file'])
    begin = min(t128['rows'], key=lambda r: abs(r['s'] - .95))
    last = t128['rows'][-1]
    fail = t128['failed_rhs_trial']
    growth = []
    for b, c, f in zip(begin['spectral_bands'], last['spectral_bands'], fail['spectral_bands']):
        growth.append(dict(first_mode_index=b['first_mode_index'],
                           last_mode_index=b['last_mode_index'],
                           coefficient_l2_at_join=b['coefficient_l2'],
                           coefficient_l2_at_failed_trial=f['coefficient_l2'],
                           coefficient_growth=f['coefficient_l2']/b['coefficient_l2'],
                           second_jet_l2_at_join=b['polar_second_jet_l2'],
                           second_jet_l2_at_failed_trial=f['polar_second_jet_l2'],
                           second_jet_growth=f['polar_second_jet_l2']/b['polar_second_jet_l2'],
                           last_interval_log_growth_per_s=math.log(f['coefficient_l2']/c['coefficient_l2'])/(fail['s']-last['s'])))
    stable_rows = [r for r in t128['rows'] if r['s'] >= .946]
    summary = dict(scope=__doc__, entrance_same_g=entrance, turn_same_g=turn,
                   turning_metric=t128['metric_identity'],
                   turning_rows=stable_rows,
                   failed_trial={k: v for k, v in fail.items() if k != 'coefficient_state'},
                   growth_from_turn_join=growth,
                   caveats=[
                       'All geometry extrema are finite samples of an open prefix.',
                       'D_sample is twice the largest sampled norm of the reflected prefix; it is not the complete closed F0 diameter.',
                       'A failed RHS trial is not an accepted field.',
                       'Frequency growth diagnoses numerical Cauchy instability; it is not a theorem of geometric nonexistence.',
                       'The first 32 exact rational core coefficients are unchanged in all entrance and turn runs.',
                       'A future BVP allowing additional core coefficients defines a new core and must recompute its metric and gap bounds.'])
    # Each retained state has every coefficient. The full original files retain
    # all 181 entrance stations and all accepted turn stations in scratch.
    indices = sorted(set(range(0, len(m128['state_locations']), 10)) |
                     {len(m128['state_locations']) - 1})
    turn_indices = [i for i, r in enumerate(t128['rows']) if r['s'] <= .958455656232]
    seed = dict(scope='Actual full-spectrum entrance states for a future BVP initial guess; not a completed BVP.',
                M=128, N=1536,
                convention='r[0..M], t[1..M], z[0..M] in the moving normal-angle polar frame; frequencies 2*j.',
                entrance_input_sha256=m128hash, turn_input_sha256=t128hash,
                metric_identity=m128['metric_identity'],
                turn_metric_identity=t128['metric_identity'],
                entrance_indices=indices,
                entrance_s=[m128['state_locations'][i] for i in indices],
                entrance_states=[m128['coefficient_states'][i] for i in indices],
                stable_turn_indices=turn_indices,
                stable_turn_s=[t128['state_locations'][i] for i in turn_indices],
                stable_turn_states=[t128['coefficient_states'][i] for i in turn_indices],
                endpoint_constraints=dict(core='Original R225 initial state fixes all 32 support coefficients and sets higher coefficients exactly zero.',
                                          terminal='No terminal boundary condition has yet been solved.'))
    a.summary.parent.mkdir(parents=True, exist_ok=True)
    a.seed.parent.mkdir(parents=True, exist_ok=True)
    a.summary.write_text(json.dumps(summary, indent=2) + '\n')
    a.seed.write_bytes(gzip.compress((json.dumps(seed, separators=(',', ':')) + '\n').encode(), mtime=0))
    print(json.dumps(dict(entrance_runs=len(entrance), turn_runs=len(turn),
                          seed_stations=len(indices) + len(turn_indices),
                          summary_bytes=a.summary.stat().st_size,
                          seed_bytes=a.seed.stat().st_size,
                          seed_sha256=hashlib.sha256(a.seed.read_bytes()).hexdigest())))


if __name__ == '__main__':
    main()
