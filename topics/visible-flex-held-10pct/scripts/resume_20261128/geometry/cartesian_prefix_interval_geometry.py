#!/usr/bin/env python3
"""Continuous geometry of the NEW complete Cartesian R53 prefix.

The final Cartesian shared-Hermite coefficients, the complete true-core lift,
and the actual center two-jet repair define the map.  Source primitive means,
old R62 bounds and sampled jets are not substituted for that map.  This checks
geometry only; it does not certify metric error, a tail, reach or refinement.
All interval arrays and polynomial data stay outside the repository.
"""
import os
for _key in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[_key] = '1'
import argparse
import bisect
from fractions import Fraction as Q
import hashlib
import importlib.util
import json
from pathlib import Path
import sys
import time
from types import SimpleNamespace

import mpmath as mp
import numpy as np

HERE = Path(__file__).resolve().parent
SCRIPTS = HERE.parents[1]
sys.path.insert(0, str(HERE.parent/'tail'))
from actual_cartesian_prefix import load_actual_prefix
sys.path.insert(0, str(SCRIPTS/'finite_closure/m3_m8_closed_map'))
import interval_geometry_kernel as K
from m3_interval_center import add_center_correction


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    value = importlib.util.module_from_spec(spec)
    sys.modules[name] = value
    spec.loader.exec_module(value)
    return value


def save(path, value):
    temporary = Path(str(path)+'.tmp')
    temporary.write_text(json.dumps(value, indent=2, allow_nan=False)+'\n')
    temporary.replace(path)


class AngularRanges:
    def __init__(self, prefix, nodes, progress):
        self.p, self.N = prefix, int(nodes)
        support = SCRIPTS/'resume_m3'
        mean = support/'certify_r59_fixed_mean_ranges.py'
        kernel = SCRIPTS/'finite_closure/m3_m8_closed_map/interval_geometry_kernel.py'
        # The general already-proved oracle's zero phase specialization is
        # exactly R53.  It adds no supported phase control to the source field.
        source = SCRIPTS/'resume_20261126/warm_phase_validated_core.py'
        factory = module('_new_cartesian_R53_validated', source)
        exact_baseline = SimpleNamespace(base_mode=3, baseline=prefix.core,
                                         controls=np.zeros(1))
        self.v = factory.build_oracle(exact_baseline, support, mean, kernel,
                                     progress=progress)
        self.I, self.IK = self.v.I, self.v.K
        self.oracle_metadata = self.v.metadata()
        self.oracle_metadata.update(
            queried_core_kind='true-R53-material-support',
            zero_phase_specialization=True,
            source_field_relabelled=False,
            source_supported_phase_controls_added=False)
        self.oracle_sources = [source, support/'r53_validated_material_core.py', mean, kernel]
        self.cuts = []
        for sector in range(-1, 5):
            for boundary in self.v.pg:
                self.cuts.extend(map(float, (boundary+sector*self.v.T).x))
        self.cuts = sorted(set(self.cuts))
        self.full_basis = [None]*3
        self.lift = [None]*3
        self.center = [None]*3
        self.maximum_material_parts = 0
        self.total_material_parts = 0
        self._build(progress)

    def matrix(self, values, axis=0):
        return self.I.raw(self.IK.stack([z.x for z in values], axis))

    def hull_core(self, theta):
        lo, hi = map(float, theta.x)
        middle = self.cuts[bisect.bisect_right(self.cuts, lo):
                           bisect.bisect_left(self.cuts, hi)]
        grid = [lo]+middle+[hi]
        values = None
        parts = 0
        for left, right in zip(grid[:-1], grid[1:]):
            current = self.v.point(self.I(left, right))
            parts += 1
            if values is None:
                values = {name: list(current[name]) for name in ('F', 'Ft', 'Ftt', 'Fttt')}
            else:
                values = {name: [self.v.hull(a, b) for a, b in zip(values[name], current[name])]
                          for name in values}
        self.maximum_material_parts = max(self.maximum_material_parts, parts)
        self.total_material_parts += parts
        return {name: self.matrix(value) for name, value in values.items()}

    def bases(self, psi, order):
        p, I = self.p, self.I
        sp, cp = self.v.sincos(I(p.pm)*psi)
        sh, ch = self.v.sincos(I(p.hm)*psi)
        if order == 0:
            xx, yy, zz = cp, sp, ch
        elif order == 1:
            xx, yy, zz = -I(p.pm)*sp, I(p.pm)*cp, -I(p.hm)*sh
        elif order == 2:
            xx, yy, zz = -I(p.pm**2)*cp, -I(p.pm**2)*sp, -I(p.hm**2)*ch
        else:
            raise ValueError('Only angular two-jets are used')
        return xx, yy, zz

    def tensor(self, coefficients, basis):
        I, p = self.I, self.p
        coefficients = I(coefficients)
        return self.matrix([(coefficients.item(slice(0, p.P))*basis[0]).sum(),
                            (coefficients.item(slice(0, p.P))*basis[1]).sum(),
                            (coefficients.item(slice(p.P, None))*basis[2]).sum()])

    def projection(self, psi, order):
        """Original exact binary Fourier coefficients, with interval products."""
        I, p = self.I, self.p
        c = I(p.source_initial);m = I(p.modes)
        sn, co = self.v.sincos(m*psi)
        ss, cc = self.v.sincos(psi)
        r = c.item(0)+(c.item(slice(1, p.M+1))*co).sum()
        t = (c.item(slice(p.M+1, 2*p.M+1))*sn).sum()
        z = (c.item(slice(2*p.M+1, None))*co).sum()
        if order:
            rp = -(m*c.item(slice(1, p.M+1))*sn).sum()
            tp = (m*c.item(slice(p.M+1, 2*p.M+1))*co).sum()
            zp = -(m*c.item(slice(2*p.M+1, None))*sn).sum()
        if order == 1:
            r, t, z = rp-t, r+tp, zp
        elif order == 2:
            rpp = -(m*m*c.item(slice(1, p.M+1))*co).sum()
            tpp = -(m*m*c.item(slice(p.M+1, 2*p.M+1))*sn).sum()
            zpp = -(m*m*c.item(slice(2*p.M+1, None))*co).sum()
            r, t, z = rpp-r-2*tp, tpp-t+2*rp, zpp
        return I(p.q)*self.matrix([r*cc-t*ss, r*ss+t*cc, z])

    def data(self, psi, theta, core):
        I, p = self.I, self.p
        s3, c3 = self.v.sincos(3*psi)
        st, ct = self.v.sincos(theta)
        er, et = self.matrix([ct, st, I(0)]), self.matrix([-st, ct, I(0)])
        rho, rhop = 1-I(p.E0)*c3, 3*I(p.E0)*s3
        b, bp, bpp = -I(p.Epp)*s3/3, -I(p.Epp)*c3, 3*I(p.Epp)*s3
        G, G1, G2, G3 = (core[name] for name in ('F', 'Ft', 'Ftt', 'Fttt'))
        composed = [G, rho*G1, rho*rho*G2+rhop*G1]
        circles = [er, rho*et, rhop*et-rho*rho*er]
        target = [[G, self.matrix([I(0), I(0), I(1)]), b*G1],
                  [rho*G1, I(np.zeros(3)), bp*G1+b*rho*G2],
                  [rho*rho*G2+rhop*G1, I(np.zeros(3)),
                   bpp*G1+(2*bp*rho+b*rhop)*G2+b*rho*rho*G3]]
        bases = [self.bases(psi, order) for order in range(3)]
        lift = [composed[j]-circles[j]-self.projection(psi, j) for j in range(3)]
        radial = p.core_lift_radial.jets[:, 0, 0]
        center = [self.matrix([target[j][r]-self.tensor(p.rep.jets[r, :, 0], bases[j])
                               -I(radial[r])*lift[j] for r in range(3)])
                  for j in range(3)]
        return bases, lift, center

    def _build(self, progress):
        I, v, N = self.I, self.v, self.N
        box_bases = [[[] for _ in range(3)] for _ in range(3)]
        lift_values = [[] for _ in range(3)]
        center_values = [[] for _ in range(3)]
        width = v.from_mp(mp.iv.pi/N)
        t = I(-float(width.x[1]), float(width.x[1]))
        for j in range(N):
            pl, pr = v.from_mp(2*mp.iv.pi*j/N), v.from_mp(2*mp.iv.pi*(j+1)/N)
            pc = v.from_mp(mp.iv.pi*(2*j+1)/N)
            pb = I(float(pl.x[0]), float(pr.x[1]))
            def theta(p):
                s, _ = v.sincos(3*p)
                return p-I(self.p.E0)*s/3
            tl, tr, tc = theta(pl), theta(pr), theta(pc)
            # E0 is an exact defining constant and |E0|<1; monotonicity
            # makes the endpoint hull a complete true material-angle image.
            tb = I(float(tl.x[0]), float(tr.x[1]))
            bp, hp, dp = self.data(pc, tc, self.hull_core(tc))
            bb, hb, db = self.data(pb, tb, self.hull_core(tb))
            for derivative in range(3):
                for axis in range(3):
                    box_bases[derivative][axis].append(bb[derivative][axis])
            # Tight small lift/repair ranges before multiplying short-strip
            # Hermite derivatives.  The remainder uses the entire box,
            # never a numerical finite difference or a sampled derivative.
            lift_ranges = [hp[0]+t*hp[1]+t.sq()*hb[2]/2,
                           hp[1]+t*hb[2], hb[2]]
            center_ranges = [dp[0]+t*dp[1]+t.sq()*db[2]/2,
                             dp[1]+t*db[2], db[2]]
            for derivative in range(3):
                lift_values[derivative].append(lift_ranges[derivative])
                center_values[derivative].append(center_ranges[derivative])
            if (j+1) % 64 == 0:
                progress(dict(stage='new_map_true_core_boxes', completed=j+1, total=N,
                              material_parts=self.total_material_parts))
        for derivative in range(3):
            self.full_basis[derivative] = [self.matrix(x, axis=1).x
                                          for x in box_bases[derivative]]
            self.lift[derivative] = self.matrix(lift_values[derivative]).x
            self.center[derivative] = self.matrix(center_values[derivative], axis=1).x
        self.center = K.stack(self.center)


def geometry(fields, curvature):
    X, Xs, Xss, Xp, Xpp, Xsp = fields
    normal = K.cross(Xp, Xs)
    area = K.sqrt(K.norm2(normal))
    if np.any(area[0] <= 0):
        return None
    support = K.div(K.dot(X, normal), area)
    radius = K.sqrt(K.norm2(X))
    E, F, G = K.norm2(Xs), K.dot(Xs, Xp), K.norm2(Xp)
    L, M, NN = [K.div(K.dot(z, normal), area) for z in (Xss, Xsp, Xpp)]
    diag = np.full(area[0].shape, np.inf)
    determinant = np.full_like(diag, np.inf)
    for sign in (-1, 1):
        aa = K.add(K.scale(E, curvature), K.scale(L, sign))
        bb = K.add(K.scale(F, curvature), K.scale(M, sign))
        cc = K.add(K.scale(G, curvature), K.scale(NN, sign))
        diag = np.minimum(diag, np.minimum(aa[0], cc[0]))
        determinant = np.minimum(determinant, K.sub(K.mul(aa, cc), K.square(bb))[0])
    return dict(support=support[0], radius=radius[1], area=area[0],
                curvature_psd_diagonal=diag, curvature_psd_determinant=determinant)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source-run', type=Path, required=True)
    parser.add_argument('--outdir', type=Path, required=True)
    parser.add_argument('--angular', type=int, default=1024)
    parser.add_argument('--batch', type=int, default=8)
    parser.add_argument('--curvature', type=float, default=12.3)
    parser.add_argument('--support', type=float, default=.087)
    parser.add_argument('--radius', type=float, default=1.34)
    args = parser.parse_args()
    repo = SCRIPTS.parents[2]
    out = args.outdir.resolve()
    if repo == out or repo in out.parents:
        raise ValueError('Interval arrays stay outside the source repository')
    if args.angular < 64 or args.batch < 1 or not 0 < args.curvature <= 12.3:
        raise ValueError('Positive full-circle coverage and original curvature budget required')
    out.mkdir(parents=True, exist_ok=False)
    started = time.monotonic()
    report = dict(status='loading_actual_C2_prefix', scope=__doc__, complete=False,
                  metric_certified=False, tail_attached=False, complete_surface=False,
                  source_run=str(args.source_run.resolve()), source_run_sha256=sha(args.source_run),
                  old_numeric_bounds_reused=False, source_primitive_substituted=False)
    def progress(value):
        report['progress'] = value
        report['seconds'] = time.monotonic()-started
        save(out/'summary.json', report)
        print(json.dumps({**value, 'seconds': report['seconds']}), flush=True)
    record, prefix = load_actual_prefix(args.source_run)
    if prefix.end_lift is not None:
        raise ValueError('This entry must explicitly extend its contract before attaching a cut repair')
    report.update(modes=prefix.M, homotopy=record['core_settings']['homotopy'],
                  physical_sha256=record['physical_sha256'], radial_spans=len(prefix.rep.x)-1,
                  mean_nodes=prefix.mean_nodes, center_width=prefix.center_width)
    data_path = out/'actual-prefix-exact-defining-jets.npz'
    np.savez(data_path, knots=prefix.rep.x, jets=prefix.rep.jets,
             lift_jets=prefix.core_lift_radial.jets, planar_modes=prefix.pm,
             height_modes=prefix.hm, source_initial=prefix.source_initial,
             E0=prefix.E0, Epp=prefix.Epp, q=prefix.q, center_width=prefix.center_width)
    report['defining_jets_sha256'] = sha(data_path)
    progress(dict(stage='actual_new_map_loaded'))
    ranges = AngularRanges(prefix, args.angular, progress)
    range_path = out/'actual-prefix-true-core-angular-ranges.npz'
    np.savez(range_path, center=np.stack(ranges.center), lift=np.stack(ranges.lift))
    report['true_core_angular_ranges_sha256'] = sha(range_path)
    report['oracle'] = ranges.oracle_metadata
    coeff, lift_coeff = [], []
    for derivative in range(3):
        z = K.hermite_bernstein(prefix.rep.x, prefix.rep.jets, derivative)
        coeff.append((z[0].min(axis=0), z[1].max(axis=0)))
        z = K.hermite_bernstein(prefix.core_lift_radial.x, prefix.core_lift_radial.jets, derivative)
        lift_coeff.append((z[0].min(axis=0), z[1].max(axis=0)))
    low, high = prefix.rep.x[:-1], prefix.rep.x[1:]
    total, failed = 0, 0
    first_failures = []
    bounds = dict(support_lower=np.inf, radius_upper=0., area_lower=np.inf,
                  curvature_psd_diagonal_lower=np.inf, curvature_psd_determinant_lower=np.inf)
    for start in range(0, len(low), args.batch):
        sl = slice(start, start+args.batch)
        fields = []
        for radial, angular in ((0, 0), (1, 0), (2, 0), (0, 1), (0, 2), (1, 1)):
            c = (coeff[radial][0][:, sl], coeff[radial][1][:, sl])
            b = ranges.full_basis[angular]
            value = K.stack([K.linear_field((c[0][:prefix.P], c[1][:prefix.P]), b[0]),
                             K.linear_field((c[0][:prefix.P], c[1][:prefix.P]), b[1]),
                             K.linear_field((c[0][prefix.P:], c[1][prefix.P:]), b[2])], -1)
            h = (lift_coeff[radial][0][0, sl, None, None],
                 lift_coeff[radial][1][0, sl, None, None])
            core = (ranges.lift[angular][0][None, :, :], ranges.lift[angular][1][None, :, :])
            fields.append(K.add(value, K.mul(h, core)))
        fields = add_center_correction(fields, low[sl], high[sl], prefix.center_width, ranges.center)
        if not all(np.all(np.isfinite(v)) for field in fields for v in field):
            raise ArithmeticError('A complete new-map jet interval is nonfinite')
        values = geometry(fields, args.curvature)
        if values is None:
            bad = np.ones((len(low[sl]), args.angular), bool)
        else:
            bad = ((values['support'] < args.support) | (values['radius'] > args.radius)
                   | (values['curvature_psd_diagonal'] <= 0)
                   | (values['curvature_psd_determinant'] <= 0))
            for key, name in [('support_lower', 'support'), ('radius_upper', 'radius'),
                              ('area_lower', 'area'), ('curvature_psd_diagonal_lower', 'curvature_psd_diagonal'),
                              ('curvature_psd_determinant_lower', 'curvature_psd_determinant')]:
                reducer = max if key == 'radius_upper' else min
                scalar = float(np.max(values[name]) if reducer is max else np.min(values[name]))
                bounds[key] = reducer(bounds[key], scalar)
        total += bad.size
        failed += int(bad.sum())
        for i, j in np.argwhere(bad)[:max(0, 20-len(first_failures))]:
            entry = dict(radial=[float(low[start+i]), float(high[start+i])], angle=int(j))
            if values is not None:
                entry.update({key: float(value[i, j]) for key, value in values.items()})
            first_failures.append(entry)
        if start % 64 == 0:
            progress(dict(stage='new_map_continuous_geometry', radial_done=start+len(bad),
                          radial_total=len(low), boxes=total, failed_boxes=failed))
    sources = [Path(__file__), HERE.parent/'tail/actual_cartesian_prefix.py',
               SCRIPTS/'finite_closure/m3_m8_closed_map/shared_jet.py',
               SCRIPTS/'finite_closure/m3_m8_closed_map/m3_shared_prefix.py',
               SCRIPTS/'finite_closure/m3_m8_closed_map/m3_interval_center.py', *ranges.oracle_sources]
    report.update(status='continuous_new_prefix_geometry_certified' if failed == 0 else 'continuous_new_prefix_geometry_unresolved',
                  complete=failed == 0, continuous_prefix_geometry_certified=failed == 0,
                  covered_radial=[float(low[0]), float(high[-1])], full_angular_range='[0,2*pi]',
                  angular_boxes=args.angular, boxes=total, failed_boxes=failed,
                  first_failures=first_failures, bounds=bounds,
                  thresholds=dict(curvature=args.curvature, support=args.support, radius=args.radius),
                  source_hashes={str(path.resolve()): sha(path) for path in sources},
                  seconds=time.monotonic()-started)
    save(out/'summary.json', report)
    print(json.dumps({key: report[key] for key in ('status', 'boxes', 'failed_boxes', 'bounds', 'seconds')}), flush=True)


if __name__ == '__main__':
    main()
