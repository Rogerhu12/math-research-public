#!/usr/bin/env python3
"""Retarget one physically slower prefix turn to the same actual tail port.

The changed turn is selected from an observed curvature bottleneck. The
source candidate remains immutable. This is a new metric design, not a
same-g refinement or a nonlinear solution. The tail metric is unchanged.
"""
import os
for key in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[key] = '1'
import argparse, copy, json, time
from pathlib import Path
import numpy as np
from scipy.optimize import brentq
import fd2d_moderate_deep_screen as moderate

fm = moderate.fm


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--source', type=Path, required=True)
    p.add_argument('--label', default='early_shallow_return')
    p.add_argument('--curvature', type=float, required=True)
    p.add_argument('--pdeep', type=float, default=1.48)
    p.add_argument('--out-prefix', type=Path, required=True)
    a = p.parse_args(); started = time.monotonic(); stem = a.out_prefix
    if list(stem.parent.glob(stem.name+'*')):
        raise FileExistsError('A fresh physical design stem is required')
    stem.parent.mkdir(parents=True, exist_ok=True)
    original = json.loads(a.source.read_text()); initial = copy.deepcopy(original)
    pieces = [x for x in initial['segments'] if x.get('label') == a.label]
    if len(pieces) != 1 or pieces[0]['kind'] != 'turn' or a.curvature <= 0:
        raise ValueError('Select one turn and a positive meridian curvature')
    piece = pieces[0]; old = copy.deepcopy(piece)
    piece.update(K=a.curvature, L=abs(piece['p1']-piece['p0'])/(.92*a.curvature),
                 length_from_turn_rate=True)
    coast = next(x for x in initial['segments']
                 if x.get('label') == 'partial_return_matching_coast')
    coast['L'] = .01
    initial['local_turn_design'] = dict(label=a.label, old_piece=old,
        new_curvature=a.curvature, source_candidate=a.source.name,
        source_candidate_sha256=fm.digest(a.source), generator=Path(__file__).name,
        generator_sha256=fm.digest(__file__), new_physical_prefix_metric=True,
        physical_tail_unchanged=True, target_reason='Actual gap .05 body curvature bottleneck')
    for key in ('metric_diagnostics', 'full_m2_amplification'):
        initial.pop(key, None)
    seed = stem.with_name(stem.name+'-initial.json')
    seed.write_text(json.dumps(initial, indent=2)+'\n')
    family = moderate.ModerateFamily(seed)
    path = stem.with_name(stem.name+'-report.json')
    report = dict(schema='fd2d-local-turn-prefix-design-v1', source_sha256=fm.digest(__file__),
        initial_sha256=fm.digest(seed), changed_turn=a.label, curvature=a.curvature,
        target_direction=family.target.tolist(), physical_tail_unchanged=True,
        evaluations=[], completed=False, nonlinear_solution=False, continuous_certificate=False)
    def save():
        report['seconds'] = time.monotonic()-started
        path.write_text(json.dumps(report, indent=2, allow_nan=False)+'\n')
    def shoot(T):
        value, end = family.shoot(a.pdeep, float(T))
        row = dict(T=float(T), residual=value, terminal_fg=end.tolist())
        report['evaluations'].append(row); save()
        print(json.dumps(dict(event='shoot', **row)), flush=True)
        return value
    upper = family.Tmax(a.pdeep); lo = 0.; flo = shoot(lo)
    hi = min(.2, .95*upper); fhi = shoot(hi)
    while flo*fhi > 0 and hi < .95*upper:
        hi = min(2*hi, .95*upper); fhi = shoot(hi)
    if flo*fhi > 0:
        report.update(completed=True, root_found=False, Tmax=upper); save()
        raise RuntimeError('No positive-coast root in the tested connected bracket')
    T = brentq(shoot, lo, hi, xtol=5e-13, rtol=1e-14)
    row, bundle, trace = family.root_record(a.pdeep, T)
    bundle['status']['metric_frozen'] = True
    bundle['selection_reason'] = 'One slowed turn at an actual curvature bottleneck, matched to unchanged actual tail m2 port; finite linear initializer only'
    candidate = stem.with_name(stem.name+'-candidate.json')
    trajectory = stem.with_name(stem.name+'-trajectory.npz')
    candidate.write_text(json.dumps(bundle, indent=2)+'\n')
    np.savez_compressed(trajectory, **trace.sample())
    report.update(completed=True, root_found=True, root=row, Tmax=upper,
        candidate_file=candidate.name, candidate_sha256=fm.digest(candidate),
        trajectory_file=trajectory.name, trajectory_sha256=fm.digest(trajectory))
    save(); print(json.dumps(dict(event='complete', root=row,
        candidate_sha256=fm.digest(candidate), seconds=report['seconds'])), flush=True)


if __name__ == '__main__':
    main()
