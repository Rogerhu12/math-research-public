#!/usr/bin/env python3
"""True root Fourier interpolants with complete aliases and primitive error.

Both Y' and v0 are even under the exact physical D4 reflection. The position
primitive has parity (even, odd, even), the physical root shear is odd, and
the along-shear derivative preserves even scalar fields. This proves the
reflection used here before any finite DFT is performed.
"""
from __future__ import annotations
import argparse
from fractions import Fraction
import gzip
import hashlib
import json
from pathlib import Path

from flint import acb, arb, ctx
from fourfold_phase_beta_interval import ball_record


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


def stored(row):
    return arb(row['lower']).lower().union(arb(row['upper']).upper())


def dyadic(value):
    value = arb(value)
    if not value.is_exact():
        raise ValueError('only an exact dyadic may define the finite interpolant')
    m, e = value.man_exp()
    return [str(m), int(e)]


def decode(pair):
    value = arb((int(pair[0]), int(pair[1])))
    if not value.is_exact():
        raise ValueError('precision too low for exact dyadic coefficient')
    return value


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--grid-manifest', type=Path,
        default=Path('data/root_finite_grid/grid4096_h1e9/manifest.json'))
    p.add_argument('--bits', type=int, default=320)
    p.add_argument('--out', type=Path, required=True)
    a = p.parse_args()
    ctx.prec = a.bits
    grid = read(a.grid_manifest)
    if not grid['complete'] or grid['worker_sha256'] != sha(grid['worker_path']):
        raise ValueError('incomplete or changed actual root grid')
    N = grid['grid']; K = N//2
    if N < 4 or N % 2:
        raise ValueError('even actual sample grid required')
    rows = []
    for chunk in grid['chunks']:
        if sha(chunk['path']) != chunk['sha256']:
            raise ValueError('actual root grid shard changed')
        doc = read(chunk['path'])
        if not doc['complete'] or doc['identity'] != grid['identity']['identity']:
            raise ValueError('grid shard belongs to another actual parameter family')
        for name, digest in doc['dependencies'].items():
            if sha(Path('scripts')/name) != digest:
                raise ValueError('root grid dependency changed: '+name)
        rows.extend(doc['rows'])
    if [r['index'] for r in rows] != list(range(K+1)):
        raise ValueError('actual half-period grid has a gap or duplicate')
    outer_path = Path(doc['complex_root_path'])
    if sha(outer_path) != doc['complex_root_sha256']:
        raise ValueError('complete complex root certificate changed')
    outer = read(outer_path)
    if not outer['proved'] or outer['pending'] or outer['failed_cells']:
        raise ValueError('incomplete outer strip')
    S = arb(Fraction(outer['exact_physical_angle_strip']).numerator)/Fraction(outer['exact_physical_angle_strip']).denominator
    bounds = outer['uniform_bounds']
    MY = max(stored(c['Y_prime_modulus']).upper() for c in outer['cells'])
    y_real_lower = min(stored(c['Y_prime_real']).lower() for c in outer['cells'])
    V = stored(bounds['v0_minus_reference_modulus_upper']).upper()
    if bounds['v0_reference_constant'] != 5050:
        raise ValueError('the certified potential split changed')
    rr = (-4*S).exp()
    lebesgue = 1+4/arb.pi()*(1+arb(N-1).log()/2)
    inverse_derivative_L2_Linfty = arb.pi()/(4*arb(3).sqrt())
    fields = {}
    all_values = {}
    for name, modulus, constant in (('Y_prime', MY, 0), ('residual_v0', V, 5050)):
        key = 'Y_prime' if name == 'Y_prime' else 'v0'
        half = [stored(row[key])-constant for row in rows]
        values = half+list(reversed(half[1:-1]))
        all_values[name] = values
        center = [v.mid() for v in values]
        radii = [abs(v-c).upper() for v,c in zip(values, center)]
        node_max = max(radii)
        node_rms = (sum((r*r for r in radii), arb(0))/N).sqrt().upper()
        transformed = [z/N for z in acb.dft([acb(v) for v in center])]
        coefficients = []
        errors = []
        for n in range(K+1):
            z = transformed[n]
            if not z.imag.contains(0):
                raise ValueError('the exact even midpoint DFT lost its real axis')
            value = z.real
            if 0 < n < K:
                opposite = transformed[-n]
                if not opposite.imag.contains(0):
                    raise ValueError('reflected real midpoint DFT lost its real axis')
                value = value.intersection(opposite.real)
            middle = value.mid()
            coefficients.append(middle)
            errors.append(abs(value-middle).upper())
        # P=c0+2 sum_{n=1}^{K-1} cn cos(4n theta)+cK cos(4K theta).
        rounding_L1 = errors[0]+2*sum(errors[1:K], arb(0))+errors[K]
        rounding_L2 = (errors[0]**2+2*sum((e*e for e in errors[1:K]),arb(0))
                       +errors[K]**2/2).sqrt().upper()
        alias_real = (4*modulus*rr**K/(1-rr)).upper()
        uniform = (lebesgue*node_max+alias_real+rounding_L1).upper()
        primitive = (inverse_derivative_L2_Linfty*(node_rms+alias_real+rounding_L2)).upper()
        fields[name] = dict(nonnegative_cosine_DFT_coefficients=[dyadic(c) for c in coefficients],
            representation='c0+2*sum(c_n*cos(4*n*theta),1<=n<K)+c_K*cos(4*K*theta)',
            complete_outer_strip_modulus=ball_record(modulus),
            maximum_nodal_ball_error=ball_record(node_max), discrete_nodal_RMS_error=ball_record(node_rms),
            finite_DFT_rounding_L1=ball_record(rounding_L1.upper()), finite_DFT_rounding_L2=ball_record(rounding_L2),
            complete_real_interpolation_alias=ball_record(alias_real),
            uniform_real_error=ball_record(uniform),
            zero_mean_primitive_uniform_error=ball_record(primitive),
            exact_degree=K)
    yy = all_values['Y_prime']
    mean_alias = 2*MY*rr**N/(1-rr**N)
    true_mean = sum(yy, arb(0))/N+arb(0, mean_alias.upper())
    if not true_mean > 0:
        raise ValueError('positive actual root circumference unresolved')
    frequency = 1/true_mean
    old_frequency = stored(bounds['full_circle_frequency_lower']).lower().union(
        stored(bounds['full_circle_frequency_upper']).upper())
    frequency = frequency.intersection(old_frequency)
    yc = [decode(row) for row in fields['Y_prime']['nonnegative_cosine_DFT_coefficients']]
    qcenter = (1/yc[0]).mid()
    qerror = abs(frequency-qcenter).upper()
    primitive_size = (2*sum((abs(yc[n])/(4*n) for n in range(1,K)),arb(0))
                      +abs(yc[K])/(4*K)).upper()
    Herror = (frequency.upper()*stored(fields['Y_prime']['zero_mean_primitive_uniform_error']).upper()
              +qerror*primitive_size).upper()
    m = (frequency.lower()*y_real_lower).lower()
    M = (frequency.upper()*MY).upper()
    inverse_strip = (arb(7)/8*m*S).lower()
    if not m > 0 or not 0 < inverse_strip < m*S:
        raise ValueError('strict actual canonical image strip is unresolved')
    low = 0
    while 4*frequency.lower()*(low+1) < 2048:
        low += 1
    report = dict(kind='actual_root_finite_midpoint_Fourier_fits_and_true_angle_primitive', proved=True,
        source_sha256=sha(__file__), bits=a.bits, grid_manifest_path=str(a.grid_manifest),
        grid_manifest_sha256=sha(a.grid_manifest), identity=grid['identity'],
        complex_root_path=str(outer_path), complex_root_sha256=sha(outer_path),
        exact_physical_strip=outer['exact_physical_angle_strip'], grid=N, half_grid_nodes=K+1,
        reflection_proof='physical root scalars Yprime and v0 are even; the primitive has (even,odd,even) parity and the along-shear derivative preserves even scalars',
        Lebesgue_constant_upper=ball_record(lebesgue.upper()),
        physical_zero_mean_primitive_L2_to_Linfty=ball_record(inverse_derivative_L2_Linfty.upper()),
        fields=fields, true_frequency=ball_record(frequency), finite_H_frequency_dyadic=dyadic(qcenter),
        finite_H_definition='theta+q_center*(2*sum(c_n*sin(4*n*theta)/(4*n),1<=n<K)+c_K*sin(4*K*theta)/(4*K))',
        finite_Yprime_primitive_modulus_upper=ball_record(primitive_size),
        true_H_minus_finite_H_real_uniform_error=ball_record(Herror),
        frequency_minus_finite_frequency=ball_record(qerror),
        true_Hprime_complex_real_lower=ball_record(m), true_Hprime_complex_modulus_upper=ball_record(M),
        strict_canonical_image_strip=ball_record(inverse_strip), canonical_low_cutoff=low,
        scope=['All true sampling uncertainty, finite DFT roundoff and infinite angular aliases are paid.',
               'The exact midpoint polynomials are numerical references and do not redefine the geometry.',
               'No finite root-shear column, full feedback inverse, or nonlinear zero is declared here.'])
    save(a.out, report)
    print(dict(proved=True, q=report['true_frequency'], Herror=report['true_H_minus_finite_H_real_uniform_error'],
               Yerror=fields['Y_prime']['uniform_real_error'], verror=fields['residual_v0']['uniform_real_error'],
               Hprime_lower=report['true_Hprime_complex_real_lower'], Hprime_upper=report['true_Hprime_complex_modulus_upper'],
               inverse_strip=report['strict_canonical_image_strip'], low_cutoff=low), flush=True)


if __name__ == '__main__':
    main()
