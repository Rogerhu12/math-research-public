#!/usr/bin/env python3
"""Exact finite-prefix and fixed-marker inputs for conditional theorem R238.

The saved binary64 coefficients are treated as exact rationals. This checks
that every radial PPoly span has a nonzero nonmean height polynomial, and
optionally checks the finite cap marker plan by rational arithmetic. It does
not certify embedding, the tail/collar, metric error, or delta_E.
"""
from __future__ import annotations
import argparse
from fractions import Fraction
import gzip
import hashlib
import io
import json
from pathlib import Path
import numpy as np


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def read(path):
    raw = Path(path).read_bytes()
    return json.loads(gzip.decompress(raw) if raw[:2] == b'\x1f\x8b' else raw)


def rat(value):
    if isinstance(value, float):
        return Fraction.from_float(value)
    return Fraction(value)


def determinant(rows):
    a, b, c = rows
    return (a[0]*(b[1]*c[2]-b[2]*c[1])
            - a[1]*(b[0]*c[2]-b[2]*c[0])
            + a[2]*(b[0]*c[1]-b[1]*c[0]))


def prefix(checkpoint):
    rec = read(checkpoint)
    M = int(rec['config']['modes'])
    mode = int(rec['config'].get('base_mode', 2))
    if mode != 2 or rat(rec['gauge_amplitude']) == 0:
        raise ValueError('R238 prefix adapter requires mode 2 and nonzero gauge')
    if not rec.get('solver_success') or not rec.get('actual_tail'):
        raise ValueError('An accepted actual-tail prefix checkpoint is required')
    if rec['angular_chart'] not in ('frozen-spline-adaptive-v1', 'general-support-core-blend-v1'):
        raise ValueError('Unrecognized parity-preserving prefix chart')
    if rec['angular_chart'] == 'general-support-core-blend-v1':
        if any(int(n) % 2 for n in rec['chart_reference_frequencies']):
            raise ValueError('General support chart contains an odd core frequency')
    mesh = [rat(x) for x in rec['mesh']]
    if len(mesh) < 2 or any(b <= a for a, b in zip(mesh, mesh[1:])):
        raise ValueError('Nonempty strictly ordered physical mesh required')
    chunks = rec.get('pp_coefficient_chunks')
    arrays, bindings = [], []
    first = 0
    if chunks:
        for item in chunks:
            path = checkpoint.parent/item['file']
            digest = sha(path)
            if digest != item['sha256']:
                raise ValueError('Coefficient hash mismatch: '+path.name)
            start, end = item['state_first'], item['state_last_exclusive']
            if start != first or end <= start:
                raise ValueError('Coefficient chunks have a gap or overlap')
            raw = gzip.decompress(path.read_bytes())
            array = np.load(io.BytesIO(raw), allow_pickle=False)
            if array.dtype != np.dtype('float64') or array.shape[2] != end-start:
                raise ValueError('Wrong saved coefficient dtype or state range')
            first = end
            arrays.append(array)
            bindings.append(dict(file=path.name, sha256=digest,
                                 state_first=start, state_last_exclusive=end))
        coefficients = np.concatenate(arrays, axis=2)
    else:
        coefficients = np.asarray(rec['pp_coefficients'], dtype=np.float64)
    if coefficients.ndim != 3 or coefficients.shape[1:] != (len(mesh)-1, 3*M+1):
        raise ValueError('Expected physical PPoly layout (degree+1, spans, 3*M+1)')
    if not np.isfinite(coefficients).all():
        raise ValueError('Nonfinite polynomial coefficient')
    height = coefficients[:, :, 2*M+1:]
    witnesses, uncovered = [], []
    degree = len(coefficients)-1
    for span in range(len(mesh)-1):
        nonzero = np.argwhere(height[:, span, :] != 0)
        if not len(nonzero):
            uncovered.append(span)
            continue
        row, harmonic = map(int, nonzero[0])
        value = float(height[row, span, harmonic])
        exact = Fraction.from_float(value)
        witnesses.append(dict(span=span, monomial_power=degree-row,
                              harmonic=2*(harmonic+1), coefficient_hex=value.hex(),
                              exact_numerator=str(exact.numerator),
                              exact_denominator=str(exact.denominator)))
    return dict(checkpoint_sha256=sha(checkpoint), modes=M, spans=len(mesh)-1,
                polynomial_degree=degree, coefficient_chunks=bindings,
                all_height_polynomials_nonzero=not uncovered,
                uncovered_spans=uncovered, witnesses=witnesses,
                algebraic_interpretation='Binary64 values are exact dyadic rationals; nonzero is exact, not a tolerance test.',
                conditional_conclusion='If the saved latitude circles are embedded, the parity and angular analyticity of SavedPrefix imply no planar open subset in this prefix (R238 section 5).')


def markers(plan_path, assembly_path):
    plan, assembly = read(plan_path), read(assembly_path)
    if assembly['inputs']['plan']['sha256'] != sha(plan_path):
        raise ValueError('Assembly and plan provenance differ')
    cuff = rat(plan['cuff'])
    cap_h = rat(assembly['mean_gauge']['upper_cap_height'])
    rows = plan['fixed_cap']['markers']
    if len(rows) != 4 or cuff <= 0 or cap_h <= 0:
        raise ValueError('Expected four markers on two separated caps')
    radii, centers, checks = [], [], []
    for marker in rows:
        radius = rat(marker['radius'])
        center_xy = [rat(x) for x in marker['center']]
        height = rat(marker['height'])
        inside = (0 < radius < cuff and
                  sum(x*x for x in center_xy) < (cuff-radius)**2)
        center = center_xy+[(1 if marker['upper'] else -1)*cap_h]
        radii.append(radius)
        centers.append(center)
        checks.append(dict(index=marker['index'], radius_positive=radius > 0,
                           nonzero_height=height != 0, strictly_inside_cap=inside))
    separated = []
    for i in range(4):
        for j in range(i+1,4):
            if rows[i]['upper'] == rows[j]['upper']:
                d2 = sum((centers[i][k]-centers[j][k])**2 for k in range(2))
                separated.append(dict(indices=[i+1,j+1],
                    exact_squared_margin=str(d2-(radii[i]+radii[j])**2),
                    disjoint=d2 > (radii[i]+radii[j])**2))
    det = determinant([[centers[i][k]-centers[3][k] for k in range(3)]
                       for i in range(3)])
    valid = (len(set(radii)) == 4 and det != 0 and
             all(all(v for k,v in row.items() if k != 'index') for row in checks) and
             all(row['disjoint'] for row in separated))
    return dict(plan_sha256=sha(plan_path), assembly_sha256=sha(assembly_path),
                exact_support_circle_centers=[[str(x) for x in row] for row in centers],
                exact_radii=[str(x) for x in radii],
                support_centers_affine_determinant=str(det),
                pairwise_distinct_radii=len(set(radii)) == 4,
                per_marker=checks, same_cap_pairs=separated,
                finite_marker_algebra_passed=valid,
                unpaid='Embedded full closed surface, annular active component with no planar open subset, and genuine continuous image change.')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--checkpoint', type=Path, required=True)
    parser.add_argument('--plan', type=Path)
    parser.add_argument('--assembly', type=Path)
    parser.add_argument('--out', type=Path, required=True)
    args = parser.parse_args()
    if bool(args.plan) != bool(args.assembly):
        parser.error('--plan and --assembly must be supplied together')
    result = prefix(args.checkpoint)
    witness = result.pop('witnesses')
    witness_path = args.out.with_name(args.out.stem+'-witnesses.json.gz')
    if args.out.exists() or witness_path.exists():
        raise FileExistsError('Refusing to overwrite an existing evidence file')
    args.out.parent.mkdir(parents=True, exist_ok=True)
    raw = (json.dumps(witness, separators=(',',':'), allow_nan=False)+'\n').encode()
    witness_path.write_bytes(gzip.compress(raw, compresslevel=9, mtime=0))
    result.update(schema='R238-exact-prefix-planar-germ-inputs-v1',
                  source_sha256=sha(__file__),
                  witness_file=witness_path.name, witness_sha256=sha(witness_path),
                  witness_raw_sha256=hashlib.sha256(raw).hexdigest(),
                  witnesses=len(witness), actual_delta_E_certified=False,
                  full_active_nonplanarity_certified=False, task_completed=False)
    if args.plan:
        result['fixed_markers'] = markers(args.plan, args.assembly)
    args.out.write_text(json.dumps(result, indent=2, allow_nan=False)+'\n')
    print(json.dumps(dict(output=str(args.out), spans=result['spans'],
          prefix_nonzero_height_passed=result['all_height_polynomials_nonzero'],
          marker_algebra_passed=result.get('fixed_markers',{}).get('finite_marker_algebra_passed'),
          actual_delta_E_certified=False)), flush=True)
    if not result['all_height_polynomials_nonzero']:
        raise SystemExit(1)
    if args.plan and not result['fixed_markers']['finite_marker_algebra_passed']:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
