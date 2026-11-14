#!/usr/bin/env python3
"""Phase Newton with one fixed mean coefficient and recorded actual type checks.

Preserves the saved circumference-radius shift and beta4(0). Every improved
iterate is archived with actual finite-primitive metric/geometry diagnostics
and a full-body sampled curvature-type scan. A requested outer-curvature
floor is a sampled line-search gate, not a uniform positivity certificate.
"""
from __future__ import annotations

import argparse
import ctypes
import gc
import hashlib
import json
from pathlib import Path
import shutil

import numpy as np
from scipy.interpolate import BSpline

from fourfold_phase_newton import PhaseNewton
from fourfold_banded_normal import banded_gauss_newton
from fourfold_outer_ring_diagnostic import warped_curvature


def type_diagnostic(solver, vector, angles=256):
    x = np.unique(np.r_[np.linspace(0., .7, 351), np.linspace(.7, solver.length, 231), .445])
    target, lower, upper, nlower, nupper = [np.zeros(len(x)) for _ in range(5)]
    alpha = solver.unpack(vector)[1]
    for start in range(0, len(x), 48):
        xx = x[start:start+48]
        sl = slice(start, start+len(xx))
        jets = solver.geometry(vector, xx, angles)[0]
        _, fx, ft, fxx, fxt, ftt = jets
        cross = np.cross(ft, fx)
        jac2 = np.sum(cross*cross, axis=2)
        normal = cross/np.sqrt(jac2)[:, :, None]
        l, m, n = (np.sum(normal*t, axis=2) for t in (fxx, fxt, ftt))
        gauss = (l*n-m*m)/jac2
        lower[sl], upper[sl] = gauss.min(axis=1), gauss.max(axis=1)
        nlower[sl], nupper[sl] = n.min(axis=1), n.max(axis=1)
        E = np.mean(np.sum(fx*fx, axis=2), axis=1)
        Ep = 2*np.mean(np.sum(fx*fxx, axis=2), axis=1)
        c, d, d2 = (solver.mean(xx, alpha, j) for j in range(3))
        target[sl] = warped_curvature(c[:, 0], d[:, 0], d2[:, 0], E, Ep)
    roots = [float(x[i]-target[i]*(x[i+1]-x[i])/(target[i+1]-target[i]))
             for i in np.nonzero(target[:-1]*target[1:] < 0.)[0]]
    outer = x >= .3
    ring = (x >= .3) & (x <= .6)
    core = x <= .7
    ix = np.flatnonzero(outer)[np.argmin(lower[outer])]
    return dict(kind='floating_sampled_full_body_type_not_bounds', radial_samples=len(x),
                quarter_period_angles=angles, target_K0_sign_crossings_linear_samples=roots,
                target_outer_minimum=float(target[outer].min()),
                actual_outer_Gauss_minimum=float(lower[outer].min()),
                actual_outer_minimum_x=float(x[ix]),
                target_ring_minimum=float(target[ring].min()),
                actual_ring_Gauss_minimum=float(lower[ring].min()),
                actual_N_core_maximum=float(nupper[core].max()),
                actual_N_core_minimum=float(nlower[core].min()),
                actual_N_full_maximum=float(nupper.max()),
                actual_N_full_minimum=float(nlower.min()),
                target_at_0445=float(np.interp(.445, x, target)),
                actual_Gauss_at_0445=[float(np.interp(.445, x, lower)), float(np.interp(.445, x, upper))])


class ConstrainedPhaseNewton(PhaseNewton):
    def prepare_fixed(self, beta_waist, index, value, gauss=3, angles=256):
        super().prepare(beta_waist, gauss, angles)
        if not 0 <= index < self.mean_count:
            raise ValueError('fixed mean index is out of range')
        full_index = 2*self.modes*self.points+index
        column = int(np.nonzero(self.keep == full_index)[0][0])
        self.offset += np.asarray(self.projector[:, column].toarray()).ravel()*value
        keep_columns = np.delete(np.arange(len(self.keep)), column)
        self.projector = self.projector[:, keep_columns].tocsc()
        self.keep = self.keep[keep_columns]
        self.fixed_mean_index, self.fixed_mean_value = int(index), float(value)
        self.outer_floor = None
        self.core_N_upper = None
        self.type_vector = None
        self.type_cache = None
        self.last_snapshot_vector = None
        self.snapshot_records = []

    def normal_system(self, free):
        # Release freed diagnostic/assembly buffers before the next large
        # Gram assembly. The numerical matrix is unchanged by this trim.
        gc.collect()
        libc = ctypes.CDLL(None)
        if hasattr(libc, 'malloc_trim'):
            libc.malloc_trim(0)
        return super().normal_system(free)

    def get_type(self, vector):
        if self.type_vector is None or not np.array_equal(vector, self.type_vector):
            self.type_cache = type_diagnostic(self, vector, angles=max(256, self.angles))
            self.type_vector = vector.copy()
        return self.type_cache

    def fun(self, free):
        vector = self.expand(free)
        if self.outer_floor is not None or self.core_N_upper is not None:
            info = self.get_type(vector)
            bad_outer = (self.outer_floor is not None and
                         info['actual_outer_Gauss_minimum'] < self.outer_floor)
            bad_N = (self.core_N_upper is not None and
                     info['actual_N_core_maximum'] >= self.core_N_upper)
            if bad_outer or bad_N:
                print(json.dumps(dict(rejected_sampled_type=info, outer_floor=self.outer_floor,
                                      core_N_upper=self.core_N_upper)), flush=True)
                raise ValueError('sampled actual type violated the requested line-search gate')
        return super().fun(free)

    def save(self, vector, path, amplitude):
        if self.last_snapshot_vector is not None and np.array_equal(vector, self.last_snapshot_vector):
            return
        super().save(vector, path, amplitude)
        with np.load(path, allow_pickle=False) as f:
            payload = {name: f[name] for name in f.files}
        metadata = json.loads(str(payload['metadata']))
        metadata['fixed_mean_coefficients'] = {str(self.fixed_mean_index): self.fixed_mean_value}
        metadata['sampled_outer_curvature_floor'] = self.outer_floor
        metadata['sampled_core_N_upper'] = self.core_N_upper
        payload['metadata'] = np.array(json.dumps(metadata))
        temporary = Path(str(path)+'.tmp.npz')
        np.savez_compressed(temporary, **payload)
        temporary.replace(path)
        number = len(self.snapshot_records)
        archived = Path(path).with_name(Path(path).stem+f'.step{number:02d}.npz')
        shutil.copyfile(path, archived)
        diagnostic = self.diagnostic(vector, angles=max(256, self.angles))
        record = dict(step=number, checkpoint=str(archived),
                      checkpoint_sha256=hashlib.sha256(archived.read_bytes()).hexdigest(),
                      fixed_mean_index=self.fixed_mean_index, fixed_mean_value=self.fixed_mean_value,
                      alpha=self.unpack(vector)[1].tolist(), diagnostic=diagnostic,
                      type_diagnostic=self.get_type(vector),
                      limitations=['Floating samples', 'Finite Robin endpoint',
                                   'The outer-curvature acceptance gate is not a continuous certificate'])
        archived.with_suffix('.json').write_text(json.dumps(record, indent=2)+'\n')
        self.snapshot_records.append(record)
        self.last_snapshot_vector = vector.copy()
        print(json.dumps(dict(archived_improved_state=record)), flush=True)


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--start-phase', type=Path, required=True)
    ap.add_argument('--fix-mean-index', type=int, default=2)
    ap.add_argument('--fixed-mean-value', type=float)
    ap.add_argument('--iterations', type=int, default=2)
    ap.add_argument('--regularization', type=float, default=1e-5)
    ap.add_argument('--outer-floor', type=float)
    ap.add_argument('--core-N-upper', type=float)
    ap.add_argument('--cache', type=Path, required=True)
    ap.add_argument('--out', type=Path, required=True)
    args = ap.parse_args()
    with np.load(args.start_phase, allow_pickle=False) as f:
        metadata = json.loads(str(f['metadata']))
        vector = f['vector']
        solver = ConstrainedPhaseNewton(**metadata['parameters'])
        solver.radius_shift = BSpline(f['radius_shift_knots'], f['radius_shift_coefficients'],
                                      int(f['radius_shift_degree']))
        solver.source_position = metadata.get('source_position')
    fixed = args.fixed_mean_value
    if fixed is None:
        fixed = float(solver.unpack(vector)[1][args.fix_mean_index])
    solver.prepare_fixed(metadata['beta_waist'], args.fix_mean_index, fixed,
                         metadata['radial_gauss_points_per_interval'], metadata['quarter_period_angles'])
    solver.outer_floor = args.outer_floor
    solver.core_N_upper = args.core_N_upper
    args.cache.parent.mkdir(parents=True, exist_ok=True)
    solver.snapshot_path = args.cache
    result = banded_gauss_newton(solver, vector[solver.keep], args.iterations, args.regularization)
    final = solver.expand(result.x)
    solver.save(final, args.cache, metadata['beta_waist'])
    report = dict(kind='floating_fixed_mean_phase_correction_not_exact_surface',
                  source_checkpoint=str(args.start_phase),
                  source_checkpoint_sha256=hashlib.sha256(args.start_phase.read_bytes()).hexdigest(),
                  cost=result.cost, message=result.message, optimality=result.optimality,
                  fixed_mean_index=args.fix_mean_index, fixed_mean_value=fixed,
                  history=solver.history, accepted_snapshots=solver.snapshot_records,
                  primitive_audit=solver.primitive_audit(final))
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(report, indent=2)+'\n')
    print(json.dumps(dict(final_cost=result.cost, final_snapshot=solver.snapshot_records[-1])), flush=True)


if __name__ == '__main__':
    main()
