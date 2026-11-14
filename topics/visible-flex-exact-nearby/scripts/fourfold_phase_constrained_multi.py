#!/usr/bin/env python3
"""Phase correction with several mean coefficients held at saved values.

Separate from the first continuation solver so its archived source hash stays
recoverable. The remaining mean and all free phase coefficients absorb metric
error. Every improvement is saved with actual finite-primitive C2 diagnostics;
the curvature and N gates are sampled tests, never continuous certificates.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import shutil

import numpy as np
from scipy.interpolate import BSpline

from fourfold_phase_newton import PhaseNewton
from fourfold_phase_constrained import ConstrainedPhaseNewton
from fourfold_banded_normal import banded_gauss_newton


class MultipleFixedMeanPhase(ConstrainedPhaseNewton):
    def prepare_fixed_many(self, beta_waist, fixed, gauss=3, angles=256):
        fixed = {int(k): float(v) for k, v in fixed.items()}
        if not fixed or len(fixed) >= self.mean_count:
            raise ValueError('fix at least one mean and leave at least one mean free')
        first = next(iter(fixed))
        self.prepare_fixed(beta_waist, first, fixed[first], gauss, angles)
        for index, value in fixed.items():
            if index == first:
                continue
            if not 0 <= index < self.mean_count:
                raise ValueError('fixed mean index is out of range')
            full_index = 2*self.modes*self.points+index
            column = int(np.nonzero(self.keep == full_index)[0][0])
            self.offset += np.asarray(self.projector[:, column].toarray()).ravel()*value
            columns = np.delete(np.arange(len(self.keep)), column)
            self.projector = self.projector[:, columns].tocsc()
            self.keep = self.keep[columns]
        self.fixed_means = fixed

    def save(self, vector, path, amplitude):
        if self.last_snapshot_vector is not None and np.array_equal(vector, self.last_snapshot_vector):
            return
        PhaseNewton.save(self, vector, path, amplitude)
        with np.load(path, allow_pickle=False) as f:
            payload = {name: f[name] for name in f.files}
        metadata = json.loads(str(payload['metadata']))
        metadata['fixed_mean_coefficients'] = {str(k): v for k, v in self.fixed_means.items()}
        metadata['sampled_outer_curvature_floor'] = self.outer_floor
        metadata['sampled_core_N_upper'] = self.core_N_upper
        payload['metadata'] = np.array(json.dumps(metadata))
        temporary = Path(str(path)+'.tmp.npz')
        np.savez_compressed(temporary, **payload)
        temporary.replace(path)
        number = len(self.snapshot_records)
        archived = Path(path).with_name(Path(path).stem+f'.step{number:02d}.npz')
        shutil.copyfile(path, archived)
        record = dict(step=number, checkpoint=str(archived),
                      checkpoint_sha256=hashlib.sha256(archived.read_bytes()).hexdigest(),
                      fixed_mean_coefficients=self.fixed_means,
                      sampled_gates=dict(core_N_upper=self.core_N_upper, core_N_interval=[0., .7],
                                         outer_curvature_floor=self.outer_floor),
                      alpha=self.unpack(vector)[1].tolist(),
                      diagnostic=self.diagnostic(vector, angles=max(256, self.angles)),
                      type_diagnostic=self.get_type(vector),
                      limitations=['Floating samples', 'Finite Robin endpoint',
                                   'Sampled type gates are not continuous positivity certificates'])
        archived.with_suffix('.json').write_text(json.dumps(record, indent=2)+'\n')
        self.snapshot_records.append(record)
        self.last_snapshot_vector = vector.copy()
        print(json.dumps(dict(archived_improved_state=record)), flush=True)


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--start-phase', type=Path, required=True)
    ap.add_argument('--fix-means', default='0,2', help='comma-separated indices, fixed at saved values')
    ap.add_argument('--iterations', type=int, default=2)
    ap.add_argument('--regularization', type=float, default=1e-5)
    ap.add_argument('--outer-floor', type=float, default=0.)
    ap.add_argument('--core-N-upper', type=float, default=0.)
    ap.add_argument('--cache', type=Path, required=True)
    ap.add_argument('--out', type=Path, required=True)
    args = ap.parse_args()
    with np.load(args.start_phase, allow_pickle=False) as f:
        metadata = json.loads(str(f['metadata']))
        vector = f['vector']
        solver = MultipleFixedMeanPhase(**metadata['parameters'])
        solver.radius_shift = BSpline(f['radius_shift_knots'], f['radius_shift_coefficients'],
                                      int(f['radius_shift_degree']))
        solver.source_position = metadata.get('source_position')
    alpha = solver.unpack(vector)[1]
    fixed = {int(i): float(alpha[int(i)]) for i in args.fix_means.split(',')}
    solver.prepare_fixed_many(metadata['beta_waist'], fixed,
                              metadata['radial_gauss_points_per_interval'], metadata['quarter_period_angles'])
    solver.outer_floor, solver.core_N_upper = args.outer_floor, args.core_N_upper
    args.cache.parent.mkdir(parents=True, exist_ok=True)
    solver.snapshot_path = args.cache
    result = banded_gauss_newton(solver, vector[solver.keep], args.iterations, args.regularization)
    final = solver.expand(result.x)
    solver.save(final, args.cache, metadata['beta_waist'])
    report = dict(kind='floating_multiple_fixed_mean_phase_correction_not_exact_surface',
                  source_checkpoint=str(args.start_phase),
                  source_checkpoint_sha256=hashlib.sha256(args.start_phase.read_bytes()).hexdigest(),
                  fixed_mean_coefficients=fixed,
                  sampled_gates=dict(core_N_upper=solver.core_N_upper, core_N_interval=[0., .7],
                                     outer_curvature_floor=solver.outer_floor),
                  cost=result.cost, message=result.message, optimality=result.optimality,
                  history=solver.history, accepted_snapshots=solver.snapshot_records,
                  primitive_audit=solver.primitive_audit(final))
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(report, indent=2)+'\n')
    print(json.dumps(dict(final_cost=result.cost, final_snapshot=solver.snapshot_records[-1])), flush=True)


if __name__ == '__main__':
    main()
