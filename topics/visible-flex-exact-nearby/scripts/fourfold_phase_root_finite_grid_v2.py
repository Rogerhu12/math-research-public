#!/usr/bin/env python3
"""True root and all available root-frame values on an exact grid.

The inverse DFT evaluates the already enclosed finite position primitive.
The unchanged infinite-primitive fee is then added coefficient by coefficient.
Angular jets still use the exact geometric ODE. A point grid by itself does
not certify Fourier coefficients: the separate complete strip alias fee is
required in the subsequent aggregation.
"""
from __future__ import annotations

import argparse
from fractions import Fraction
import gzip
import hashlib
import json
from pathlib import Path
import time

import numpy as np
from flint import acb, acb_series, arb, ctx

from fourfold_native_series_fft import NativeSeriesFFT
from fourfold_phase_beta_bulk_interval import exact_arb
from fourfold_phase_beta_interval import add_real_cauchy_error, ball_record, series_constant, series_real
from fourfold_phase_beta_parameter_germ import provenance
from fourfold_phase_canonical_root_jets import CanonicalRootModel, Jet, real_jet


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def read(path):
    with (gzip.open(path, 'rt') if str(path).endswith('.gz') else Path(path).open()) as f:
        return json.load(f)


def save(path, value):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix+'.tmp')
    with (gzip.open(tmp, 'wt') if str(path).endswith('.gz') else tmp.open('w')) as f:
        json.dump(value, f, indent=2)
        f.write('\n')
    tmp.replace(path)


class GridRootModel(CanonicalRootModel):
    def __init__(self, object_path, half_width, root_certificate, *, nodes, grid, refine_steps):
        if grid < nodes or grid % 2:
            raise ValueError('evaluation grid must be even and at least the primitive grid')
        super().__init__(object_path, half_width, root_certificate, nodes=nodes, angular_order=0)
        self.initial_root = self.root
        self.root_refinement = []
        self.target.fourier = NativeSeriesFFT()
        old, ctx.cap = ctx.cap, max(8, self.m+3)
        try:
            if refine_steps:
                self.root, self.root_refinement = self.target.refine_certified_root(
                    self.root, self.scale, self.budget, steps=refine_steps)
                # The original family interval contains every actual root.
                # Parametric interval Newton only intersects that interval;
                # its original common polynomial spans and outer budgets remain valid.
                self.coefficient, self.radius, self.E, self.C, self.K = self.target.target(
                    self.root, self.scale, self.budget)
                self.beta, self.gamma, _, _ = self.target.scalars(acb(self.root), -self.scale)
                self.kappa = acb_series([-self.K[j+1]/self.scale for j in range(4)], prec=4)
            if not self.kappa[0].real > 0:
                raise ValueError('positive true curvature quotient was lost')
            self.grid = grid
            finite = np.empty((grid, 3), object)
            for key in np.ndindex(finite.shape):
                finite[key] = series_constant(0, self.m)
            for k, frequency in enumerate(self.target.frequency):
                if frequency % 4:
                    raise ValueError('the actual primitive is not fourfold periodic')
                for c in range(3):
                    finite[(frequency//4) % grid, c] = acb_series(
                        [self.coefficient[k, c][j] for j in range(self.m)], prec=self.m)
            finite = NativeSeriesFFT().fft(finite, inverse=True)*grid
            for key in np.ndindex(finite.shape):
                finite[key] = add_real_cauchy_error(series_real(finite[key]),
                    self.budget['field_errors'][0], self.scale, self.budget['radial_radius'])
            self.position_grid = finite
        finally:
            ctx.cap = old

    def at_index(self, index):
        if not 0 <= index < self.grid:
            raise ValueError('grid index out of range')
        self.current_index = index
        self.current_angle = arb.pi()*index/(2*self.grid)
        value = self.evaluate(self.current_angle)
        row = dict(index=index, exact_quarter_fraction=str(Fraction(index, self.grid)),
                   Y_prime=value['Y_prime'], v0=value['V_root_canonical_angle_derivatives'][0])
        for name in ('alpha', 'B', 'q', 't0', 'physical_n', 'physical_support_numerator',
                     'physical_Fz', 'D', 'W'):
            row[name] = value[name]
        for name in ('V_xi_root', 'root_momentum_shear', 'physical_height',
                     'source_root_factor', 'grounded_flux_root_factor'):
            row[name] = value[name+'_canonical_angle_derivatives'][0]
        return row

    def position(self, angle, tangent):
        if angle is not self.current_angle:
            raise ValueError('precomputed primitive used away from its exact grid angle')
        old, ctx.cap = ctx.cap, self.m
        try:
            # These values already contain the genuine infinite primitive.
            # For each radial coefficient use F_theta=a T-Jrot F, exactly
            # as in CanonicalRootModel.position. No finite angular derivative
            # of the primitive is substituted for this geometric identity.
            aT = [self.lift(self.radius)*v for v in tangent]
            rows = [[self.position_grid[self.current_index, c]] for c in range(3)]
            for k in range(1, self.n):
                force = [acb_series([aT[c].coefficient(i, k-1) for i in range(self.m)],
                                    prec=self.m) for c in range(3)]
                rows[0].append((force[0]+rows[1][k-1])/k)
                rows[1].append((force[1]-rows[0][k-1])/k)
                rows[2].append(force[2]/k)
            return [real_jet(Jet([[rows[c][j][i] for i in range(self.m)]
                                 for j in range(self.n)], time_precision=self.m,
                                angle_precision=self.n)) for c in range(3)]
        finally:
            ctx.cap = old


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--object', type=Path, default=Path(
        'data/phase_ring_continuation/type_fixed_step02_d5_exact_affine_step5_object.json'))
    p.add_argument('--root-certificate', type=Path, default=Path(
        'data/phase_ring_continuation/type_fixed_step02_d5_step5_local_parameter_root_jets_h5e7.json'))
    p.add_argument('--complex-root', type=Path, default=Path(
        'notes/2026-11-12-actual-root-complex-potential-variation.json.gz'))
    p.add_argument('--half-width', type=Fraction, default=Fraction(1, 1000000000))
    p.add_argument('--nodes', type=int, default=512)
    p.add_argument('--grid', type=int, default=4096)
    p.add_argument('--refine-steps', type=int, default=3)
    p.add_argument('--indices', type=int, nargs='+')
    p.add_argument('--first', type=int, default=0)
    p.add_argument('--last', type=int)
    p.add_argument('--bits', type=int, default=256)
    p.add_argument('--out', type=Path, required=True)
    a = p.parse_args()
    if not 0 <= a.refine_steps <= 10:
        raise ValueError('invalid interval Newton step count')
    ctx.prec, ctx.cap = a.bits, 10
    wall, cpu = time.monotonic(), time.process_time()
    model = GridRootModel(a.object, a.half_width, a.root_certificate,
                         nodes=a.nodes, grid=a.grid, refine_steps=a.refine_steps)
    identity = provenance(model.target, a.object)
    outer = read(a.complex_root)
    ilo, ihi = map(Fraction, identity['exact_parameter_interval'])
    olo, ohi = map(Fraction, outer['object']['exact_parameter_interval'])
    if (not outer['proved'] or outer['failed_cells'] or outer['pending']
            or outer['root_certificate_sha256'] != sha(a.root_certificate)
            or outer['object']['origin_inputs_sha256'] != identity['origin_inputs_sha256']
            or outer['object']['direction_sha256'] != identity['direction_sha256']
            or not olo <= ilo <= ihi <= ohi):
        raise ValueError('the complete complex root strip belongs to another actual family')
    indices = a.indices if a.indices is not None else list(range(a.first, a.grid if a.last is None else a.last))
    if len(set(indices)) != len(indices) or any(not 0 <= j < a.grid for j in indices):
        raise ValueError('invalid exact grid selection')
    report = dict(kind='actual_root_exact_grid_values', complete=False,
        source_sha256=sha(__file__), identity=identity, grid=a.grid, primitive_nodes=a.nodes,
        bits=a.bits, root_certificate_path=str(a.root_certificate),
        root_certificate_sha256=sha(a.root_certificate), complex_root_path=str(a.complex_root),
        complex_root_sha256=sha(a.complex_root), initial_certified_root=ball_record(model.initial_root),
        refined_family_root=ball_record(model.root), interval_Newton_trace=model.root_refinement,
        primitive_full_uniform_error=ball_record(model.budget['field_errors'][0]),
        common_scalar_spans=model.spans, requested_indices=indices,
        dependencies={name:sha(Path(__file__).parent/name) for name in (
            'fourfold_phase_canonical_root_jets.py', 'fourfold_native_series_fft.py',
            'fourfold_phase_beta_parameter_germ.py', 'fourfold_phase_beta_interval.py',
            'fourfold_phase_beta_bulk_interval.py', 'fourfold_time_angle_jets.py')},
        Fourier_alias_paid=False, physical_finite_columns_claimed=False, rows=[])
    save(a.out, report)
    for j in indices:
        row = model.at_index(j)
        report['rows'].append(row)
        if len(report['rows']) % 32 == 0:
            report.update(wall_seconds=time.monotonic()-wall, cpu_seconds=time.process_time()-cpu)
            save(a.out, report)
            print(dict(completed_nodes=len(report['rows']), requested_nodes=len(indices),
                       cpu_seconds=report['cpu_seconds'], wall_seconds=report['wall_seconds']), flush=True)
    report.update(complete=True, full_grid_complete=set(indices)==set(range(a.grid)),
                  wall_seconds=time.monotonic()-wall, cpu_seconds=time.process_time()-cpu)
    save(a.out, report)
    print(dict(complete=True, nodes=len(indices), full_grid_complete=report['full_grid_complete'],
               root=report['refined_family_root'], first_values=report['rows'][:2],
               cpu_seconds=report['cpu_seconds'], wall_seconds=report['wall_seconds']), flush=True)


if __name__ == '__main__':
    main()
