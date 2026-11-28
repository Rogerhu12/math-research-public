#!/usr/bin/env python3
"""Validated angular three-jets for the actual NEW Cartesian R53 prefix.

These are interval inputs, not a metric certificate. The exact threefold
covariance reduces scalar Gram verification to [0,2*pi/3]. Every closed box
in that sector and its left endpoint are enclosed; no sampled maximum is
substituted for a continuous derivative bound. All arrays stay outside Git.
"""
import os
for _key in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[_key] = '1'
import argparse
import bisect
import json
from pathlib import Path
import time

import mpmath as mp
import numpy as np

from cartesian_prefix_interval_geometry import (
    AngularRanges, K, SCRIPTS, load_actual_prefix, save, sha)
from phase_angle_chart import PhaseAngleChart


class MetricAngularRanges(AngularRanges):
    def hull_core(self, theta):
        lo, hi = map(float, theta.x)
        inside = self.cuts[bisect.bisect_right(self.cuts, lo):
                           bisect.bisect_left(self.cuts, hi)]
        grid = [lo]+inside+[hi]
        result = None
        for left, right in zip(grid[:-1], grid[1:]):
            value = self.v.point(self.I(left, right))
            if result is None:
                result = {key: list(value[key]) for key in
                          ('F', 'Ft', 'Ftt', 'Fttt', 'Ftttt')}
            else:
                result = {key: [self.v.hull(a, b) for a, b in
                               zip(result[key], value[key])] for key in result}
        parts = len(grid)-1
        self.maximum_material_parts = max(self.maximum_material_parts, parts)
        self.total_material_parts += parts
        return {key: self.matrix(value) for key, value in result.items()}

    def bases(self, psi, order):
        if order < 3:
            return super().bases(psi, order)
        if order != 3:
            raise ValueError('Only the complete angular three-jet is used')
        sp, cp = self.v.sincos(self.I(self.p.pm)*psi)
        sh, _ = self.v.sincos(self.I(self.p.hm)*psi)
        return self.I(self.p.pm**3)*sp, -self.I(self.p.pm**3)*cp, self.I(self.p.hm**3)*sh

    def projection_coefficients(self):
        """Exact interval reexpression of q times the original projection."""
        p, I = self.p, self.I
        planar = {int(k): j for j, k in enumerate(p.pm)}
        height = {int(k): p.P+j for j, k in enumerate(p.hm)}
        values = [I(0) for _ in range(p.P+len(p.hm))]
        c = I(p.source_initial)
        values[planar[1]] = c.item(0)
        for j, m in enumerate(p.modes):
            R, T = c.item(1+j), c.item(1+p.M+j)
            values[planar[1+int(m)]] += (R+T)/2
            values[planar[1-int(m)]] += (R-T)/2
            values[height[int(m)]] += c.item(1+2*p.M+j)
        return I(p.q)*self.matrix(values)

    def data(self, psi, theta, core):
        I, p = self.I, self.p
        s3, c3 = self.v.sincos(3*psi)
        st, ct = self.v.sincos(theta)
        er, et = self.matrix([ct, st, I(0)]), self.matrix([-st, ct, I(0)])
        rho, rp, rpp = 1-I(p.E0)*c3, 3*I(p.E0)*s3, 9*I(p.E0)*c3
        b, bp = -I(p.Epp)*s3/3, -I(p.Epp)*c3
        bpp, bppp = 3*I(p.Epp)*s3, 9*I(p.Epp)*c3
        G, G1, G2, G3, G4 = (core[key] for key in
                              ('F', 'Ft', 'Ftt', 'Fttt', 'Ftttt'))
        composed = [G, rho*G1, rho*rho*G2+rp*G1,
                    rho**3*G3+3*rho*rp*G2+rpp*G1]
        circles = [er, rho*et, rp*et-rho*rho*er,
                   (rpp-rho**3)*et-3*rho*rp*er]
        zero = I(np.zeros(3))
        second = [b*G1, bp*G1+b*rho*G2,
                  bpp*G1+(2*bp*rho+b*rp)*G2+b*rho*rho*G3,
                  bppp*G1+(3*bpp*rho+3*bp*rp+b*rpp)*G2
                  +(3*bp*rho*rho+3*b*rho*rp)*G3+b*rho**3*G4]
        target = [[composed[j], self.matrix([I(0), I(0), I(1)]) if j == 0 else zero,
                   second[j]] for j in range(4)]
        bases = [self.bases(psi, j) for j in range(4)]
        lift = [composed[j]-circles[j]-self.tensor(self.projection_data, bases[j])
                for j in range(4)]
        radial = p.core_lift_radial.jets[:, 0, 0]
        center = [self.matrix([target[j][r]-self.tensor(p.rep.jets[r, :, 0], bases[j])
                               -I(radial[r])*lift[j] for r in range(3)]) for j in range(4)]
        return bases, lift, center, (s3, c3)

    def _build(self, progress):
        I, v, N, p = self.I, self.v, self.N, self.p
        if (np.any(np.asarray(p.pm) % 3 != 1) or np.any(np.asarray(p.hm) % 3 != 0)
                or p.flow.base_mode != 3 or not abs(p.E0) < 1):
            raise ValueError('Exact threefold covariance/monotone center chart is required')
        self.projection_data = self.projection_coefficients()
        # Both endpoint uncertainty and box width use true pi intervals.
        width = v.from_mp(2*mp.iv.pi/(3*N))
        t = I(0., float(width.x[1]))
        basis = {tag: [[[] for _ in range(3)] for _ in range(4)] for tag in ('point', 'box')}
        lifts = {tag: [[] for _ in range(4)] for tag in ('point', 'box')}
        centers = {tag: [[] for _ in range(4)] for tag in ('point', 'box')}
        trig = {tag: [[], []] for tag in ('point', 'box')}
        psi_bounds = []
        for j in range(N):
            pl, pr = v.from_mp(2*mp.iv.pi*j/(3*N)), v.from_mp(2*mp.iv.pi*(j+1)/(3*N))
            pb = I(float(pl.x[0]), float(pr.x[1]))
            def theta(angle):
                sine, _ = v.sincos(3*angle)
                return angle-I(p.E0)*sine/3
            tl, tr = theta(pl), theta(pr)
            tb = I(float(tl.x[0]), float(tr.x[1]))
            bp, hp, dp, tp = self.data(pl, tl, self.hull_core(tl))
            bb, hb, db, tb3 = self.data(pb, tb, self.hull_core(tb))
            # Enclose the SMALL actual correction before short-strip
            # derivatives amplify it. Whole-box second/third derivatives
            # remain genuine analytic bounds from the true core oracle.
            hb = [hp[0]+t*hp[1]+t.sq()*hb[2]/2, hp[1]+t*hb[2], hb[2], hb[3]]
            db = [dp[0]+t*dp[1]+t.sq()*db[2]/2, dp[1]+t*db[2], db[2], db[3]]
            for tag, bs, hs, ds, ts in (('point', bp, hp, dp, tp), ('box', bb, hb, db, tb3)):
                for derivative in range(4):
                    for axis in range(3):
                        basis[tag][derivative][axis].append(bs[derivative][axis])
                    lifts[tag][derivative].append(hs[derivative])
                    centers[tag][derivative].append(ds[derivative])
                for k in range(2):
                    trig[tag][k].append(ts[k])
            psi_bounds.append(pb)
            if (j+1) % 64 == 0:
                progress(dict(stage='new_map_metric_angular_tables', completed=j+1, total=N,
                              material_parts=self.total_material_parts))
        arrays = dict(psi_boxes=np.asarray(self.matrix(psi_bounds).x), angular_width=np.asarray(width.x))
        for tag in ('point', 'box'):
            for derivative in range(4):
                for axis in range(3):
                    arrays[f'{tag}_basis_{derivative}_{axis}'] = np.asarray(
                        self.matrix(basis[tag][derivative][axis], axis=1).x)
                arrays[f'{tag}_lift_{derivative}'] = np.asarray(self.matrix(lifts[tag][derivative]).x)
                arrays[f'{tag}_center_{derivative}'] = np.asarray(self.matrix(centers[tag][derivative], axis=1).x)
            for k in range(2):
                arrays[f'{tag}_trig_{k}'] = np.asarray(self.matrix(trig[tag][k]).x)
        if any(not np.all(np.isfinite(a)) for a in arrays.values()):
            raise ArithmeticError('Every complete angular interval must be finite')
        self.arrays = arrays


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source-run', type=Path, required=True)
    parser.add_argument('--outdir', type=Path, required=True)
    parser.add_argument('--angular', type=int, default=1536, help='Closed boxes per exact 2*pi/3 sector')
    args = parser.parse_args()
    repo, out = SCRIPTS.parents[2], args.outdir.resolve()
    if out == repo or repo in out.parents or args.angular < 32:
        raise ValueError('At least 32 complete sector boxes; all interval arrays outside Git')
    out.mkdir(parents=True, exist_ok=False)
    started = time.monotonic()
    report = dict(status='loading_actual_new_map', scope=__doc__, metric_certified=False,
                  source_run=str(args.source_run.resolve()), source_run_sha256=sha(args.source_run),
                  old_numeric_bounds_reused=False, whole_surface=False)
    def progress(value):
        report.update(progress=value, seconds=time.monotonic()-started)
        save(out/'summary.json', report)
        print(json.dumps({**value, 'seconds': report['seconds']}), flush=True)
    record, prefix = load_actual_prefix(args.source_run)
    if prefix.end_lift is not None:
        raise ValueError('A cut lift requires its own explicitly extended exact-map contract')
    chart = PhaseAngleChart(prefix)
    defining = out/'exact-defining-jets.npz'
    np.savez(defining, knots=prefix.rep.x, jets=prefix.rep.jets,
             lift_jets=prefix.core_lift_radial.jets, chart_jets=chart.rep.jets,
             planar_modes=prefix.pm, height_modes=prefix.hm,
             source_initial=prefix.source_initial, E0=prefix.E0, Epp=prefix.Epp,
             q=prefix.q, center_width=prefix.center_width)
    report.update(modes=prefix.M, physical_sha256=record['physical_sha256'],
                  homotopy=record['core_settings']['homotopy'], mean_nodes=prefix.mean_nodes,
                  radial_spans=len(prefix.rep.x)-1, chart=chart.report(),
                  defining_jets=dict(path=str(defining), sha256=sha(defining)))
    progress(dict(stage='actual_new_map_and_chart_loaded'))
    ranges = MetricAngularRanges(prefix, args.angular, progress)
    table = out/'continuous-angular-three-jets.npz'
    np.savez(table, **ranges.arrays)
    sources = [Path(__file__), Path(__file__).with_name('cartesian_prefix_interval_geometry.py'),
               Path(__file__).parents[1]/'tail/actual_cartesian_prefix.py',
               SCRIPTS/'finite_closure/m3_m8_closed_map/shared_jet.py',
               SCRIPTS/'finite_closure/m3_m8_closed_map/m3_shared_prefix.py',
               SCRIPTS/'finite_closure/m3_m8_closed_map/phase_angle_chart.py', *ranges.oracle_sources]
    report.update(status='complete_angular_three_jet_interval_tables',
                  angular_sector='[0,2*pi/3]', angular_boxes_per_sector=args.angular,
                  full_circle_box_equivalent=3*args.angular,
                  exact_threefold_covariance=('pm=1 mod 3, hm=0 mod 3, the exact R53 core '
                      'is threefold, and every radial coefficient, lift and center repair '
                      'preserves X(s,psi+2*pi/3)=R_(2*pi/3) X(s,psi); normalized Gram is periodic'),
                  right_sector_endpoint_gram_equals_left_exactly=True,
                  angular_tables=dict(path=str(table), sha256=sha(table)),
                  oracle=ranges.oracle_metadata, maximum_material_parts=ranges.maximum_material_parts,
                  source_hashes={str(path.resolve()): sha(path) for path in sources},
                  seconds=time.monotonic()-started)
    save(out/'summary.json', report)
    print(json.dumps({key: report[key] for key in ('status', 'angular_boxes_per_sector', 'seconds')}), flush=True)


if __name__ == '__main__':
    main()
