#!/usr/bin/env python3
# New 78718 explicit storage adaptation; original mathematical source is retained below.
"""Local diagnosis of the prefix metric certificate's conservative budget.

This inspects selected already-certified intervals, without constructing a
new surface or claiming a new full-prefix certificate. Angular arc bounds
use the existing directed-rounding backend after coefficient cancellation.
Mid-coefficient sampled values are explicitly diagnostic, not enclosures.
"""
import os
for name in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[name] = '1'
import argparse
from fractions import Fraction as Q
import gzip
import hashlib
import importlib.util
import io
import json
from pathlib import Path
import sys
import time
import numpy as np

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('prefix_budget_existing_backend', HERE/'78718-prefix-angular-arithmetic-storage-v2.py')
backend = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = backend
spec.loader.exec_module(backend)
poly, base = backend.poly, backend.base
I, P, qb = backend.I, backend.P, backend.qbounds


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def check(condition, message):
    if not condition:
        raise ValueError(message)


def load_uncorrected_region(path):
    """Reproduce the zero-correction prefix without loading any tail arrays."""
    meta = json.loads(path.read_text())
    check(meta['representation'] == 'exact-common-cut-prefix', 'Expected common-cut metadata')
    source = path.parent/Path(meta['base_geometry']).name
    check(sha(source) == meta['base_geometry_sha256'], 'Changed base map')
    implementation = HERE/'78718-prefix-common-cut-storage-v1.py'
    check(sha(implementation) == meta['common_cut_implementation_sha256'], 'Changed common-cut definition')
    geom = base.ExactHermite(source)
    old, new = geom.M, int(meta['modes'])
    lo = np.zeros((len(geom.x)-1, 6, 3*new+2))
    hi = lo.copy()
    lo[:, :, 0], hi[:, :, 0] = geom.power.lo[:, :, 0], geom.power.hi[:, :, 0]
    lo[:, :, -1], hi[:, :, -1] = geom.power.lo[:, :, -1], geom.power.hi[:, :, -1]
    for j in range(3):
        lo[:, :, j*new+1:j*new+old+1] = geom.power.lo[:, :, j*old+1:(j+1)*old+1]
        hi[:, :, j*new+1:j*new+old+1] = geom.power.hi[:, :, j*old+1:(j+1)*old+1]
    geom.power, geom.M = I(lo, hi), new
    cutoff = float(geom.x[meta['correction_start_index']])
    return geom, meta, cutoff


def traditional(A, e, ep, residuals):
    err = [r.norm() for r in residuals]
    amin, rmin = poly.lower_value(A), float(poly.down(1-e.norm()))
    v = float((I(ep.norm())/(3*I(rmin))).hi)
    ar = float(poly.down(amin*rmin))
    ee = I(err[0])+2*I(v)*I(err[1])+I(v).square()*I(err[2])
    ef = (I(err[1])+I(v)*I(err[2]))/I(ar)
    eg = I(err[2])/I(ar).square()
    return dict(coordinate_residual_upper=err, a_lower=amin, rho_lower=rmin,
        chart_velocity_upper=v, meridional_entry_upper=float(ee.hi),
        mixed_entry_upper=float(ef.hi), angular_entry_upper=float(eg.hi),
        operator_upper=float(max((ee+ef).hi, (ef+eg).hi)))


def restrict(p, left, right):
    return P(poly.compose(p.c, qb(left), qb(right-left)), p.first, p.phase)


def angular_bound(A, rho, theta_s, residuals, trig):
    er, fr, gr = [backend.value_range(p, trig) for p in residuals]
    ar = backend.value_range(A)
    rr = backend.value_range(rho, trig)
    ts = backend.value_range(theta_s, trig)
    check(float(ar.lo) > 0 and np.min(rr.lo) > 0, 'Local chart lower bound failed')
    v = ts/rr
    e = er-2*v*fr+v.square()*gr
    f = (fr-v*gr)/(ar*rr)
    g = gr/(ar*rr).square()
    ae = np.maximum(abs(e.lo), abs(e.hi))
    af = np.maximum(abs(f.lo), abs(f.hi))
    ag = np.maximum(abs(g.lo), abs(g.hi))
    upper = np.maximum(poly.up(ae+af), poly.up(af+ag))
    k = int(np.argmax(upper))
    return dict(operator_upper=float(upper[k]), worst_arc=k,
                component_abs_upper=[float(np.max(v)) for v in (ae, af, ag)])


def midpoint_value(p, radial, angle):
    c = backend.real_coefficients(p)
    mid = np.asarray(c.lo, np.longdouble)/2+np.asarray(c.hi, np.longdouble)/2
    coeff = np.zeros((len(radial), mid.shape[1]), dtype=np.longdouble)
    for row in mid[::-1]:
        coeff = coeff*np.asarray(radial, np.longdouble)[:, None]+row
    waves = np.arange(mid.shape[1], dtype=np.longdouble)[:, None]*np.asarray(angle, np.longdouble)[None, :]
    trig = np.sin(waves) if p.phase else np.cos(waves)
    return coeff@trig


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--geometry', type=Path, required=True)
    ap.add_argument('--target', type=Path, required=True)
    ap.add_argument('--certificate', type=Path, required=True)
    ap.add_argument('--intervals', type=int, nargs='+', default=[0, 74])
    ap.add_argument('--angular', type=int, nargs='+', default=[64, 128, 256])
    ap.add_argument('--out', type=Path, required=True)
    args = ap.parse_args()
    start = time.monotonic()
    geom, meta, cutoff = load_uncorrected_region(args.geometry)
    target = json.loads(args.target.read_text())
    data_path = args.target.parent/target['data_file']
    check(sha(data_path) == target['data_sha256'], 'Changed analytic target packet')
    raw = np.load(io.BytesIO(gzip.decompress(data_path.read_bytes())), allow_pickle=False)
    certificate = json.loads(args.certificate.read_text())
    check(certificate['geometry_sha256'] == sha(args.geometry) and
          certificate['target_sha256'] == sha(args.target), 'Different original certificate inputs')
    cosine = P(I(np.array([[.5, 0., .5]])), -1, 0)
    sine = P(I(np.array([[.5, 0., -.5]])), -1, 1)
    rows = []
    for k in args.intervals:
        left, right = float(raw['left'][k]), float(raw['right'][k])
        check(0 <= left < right <= cutoff, 'Selected interval reaches common-cut correction')
        A, e, ep = [poly.target_scalar(raw, name, k) for name in ('a', 'e', 'ep')]
        rho, theta_s = P.scalar(1.)-e*cosine, ep*sine*qb(Q(-1, 3))
        a2 = A*A
        target_metric = [P.scalar(1.)+a2*theta_s*theta_s, a2*theta_s*rho, a2*rho*rho]
        actual = poly.geometry_coefficients(geom, left, right)
        residuals = [a-b for a, b in zip(actual, target_metric)]
        original = traditional(A, e, ep, residuals)
        if k == certificate['worst_interval']:
            check(original['operator_upper'] == certificate['metric_operator_upper'],
                  'The original worst-interval arithmetic was not reproduced')
        nominal = [P(I(r.c.lo/2+r.c.hi/2), r.first, r.phase) for r in residuals]
        coefficient_midpoint_norm = [r.norm() for r in nominal]
        radial_split = {}
        for count in (2, 4, 8):
            values = []
            for j in range(count):
                l, r = Q(j, count), Q(j+1, count)
                AA, ee, eep = [restrict(p, l, r) for p in (A, e, ep)]
                rr = [restrict(p, l, r) for p in residuals]
                values.append(traditional(AA, ee, eep, rr)['operator_upper'])
            radial_split[str(count)] = max(values)
        arcs = {}
        for count in args.angular:
            trig = base.trigonometry(2*geom.M, count)
            arcs[str(count)] = angular_bound(A, rho, theta_s, residuals, trig)
        rr = np.linspace(0., 1., 9)
        theta = 2*np.pi*np.arange(4096)/4096
        Er, Fr, Gr = [midpoint_value(p, rr, theta) for p in residuals]
        av, rhov, tsv = [midpoint_value(p, rr, theta) for p in (A, rho, theta_s)]
        v = tsv/rhov
        ee = Er-2*v*Fr+v*v*Gr
        ef = (Fr-v*Gr)/(av*rhov)
        eg = Gr/(av*rhov)**2
        point_op = (abs(ee+eg)+np.sqrt((ee-eg)**2+4*ef*ef))/2
        sampled_fft = [float(np.max(np.sum(abs(np.fft.fft(z, axis=1)/len(theta)), axis=1)))
                       for z in (ee, ef, eg)]
        rows.append(dict(interval=k, left=left, right=right, original=original,
            coefficient_midpoint_residual_norm_diagnostic=coefficient_midpoint_norm,
            radial_only_subdivision_operator_upper=radial_split,
            angular_arc_operator_upper=arcs,
            midpoint_coefficient_sample_diagnostic=dict(radial_samples=len(rr), angular_samples=len(theta),
                normalized_component_fft_l1=sampled_fft, operator_max=float(np.max(point_op)),
                continuous_bound=False)))
    result = dict(status='LOCAL-interval-budget-diagnosis-only', scope=__doc__,
        script_sha256=sha(__file__),
        inputs={name: dict(file=str(path), sha256=sha(path)) for name, path in {
            'geometry': args.geometry, 'target': args.target, 'certificate': args.certificate}.items()},
        backend_sha256={name: sha(HERE/name) for name in ['78718-prefix-angular-arithmetic-storage-v2.py',
            '78718-prefix-metric-polynomial-storage-v1.py', '78718-prefix-continuous-hermite-storage-v1.py',
            '78718-prefix-common-cut-storage-v1.py']},
        common_cut_zero_correction_region_end=cutoff, original_whole_prefix_bound=certificate['metric_operator_upper'],
        inspected_intervals=rows, full_prefix_recertified=False, new_map_constructed=False,
        seconds=time.monotonic()-start)
    args.out.write_text(json.dumps(result, indent=2, allow_nan=False)+'\n')
    print(json.dumps(dict(status=result['status'], seconds=result['seconds'],
        intervals=[dict(index=r['interval'], old=r['original']['operator_upper'],
            radial8=r['radial_only_subdivision_operator_upper']['8'],
            angular256=r['angular_arc_operator_upper'].get('256')) for r in rows])))


if __name__ == '__main__':
    main()
