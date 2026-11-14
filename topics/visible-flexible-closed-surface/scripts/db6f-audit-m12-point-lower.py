#!/usr/bin/env python3
"""Independent fixed-g identity and exact rational radial witness audit.

The selected Fr values are reconstructed directly from saved first/second
endpoint data and the midpoint data. No point_metric, interval polynomial
constructor or floating Horner is used for this extra radial-diagonal check.
The independently reviewed background point interval remains an input.
"""
import argparse
from fractions import Fraction as Q
import gzip
import hashlib
import importlib.util
import json
from pathlib import Path
import sys
import time

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
NOTES = ROOT/'notes'


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def check(condition, message):
    if not condition:
        raise ValueError(message)


def read(path):
    raw = Path(path).read_bytes()
    return json.loads(gzip.decompress(raw) if raw[:2] == b'\x1f\x8b' else raw)


def resolve(name):
    path = Path(name)
    if path.exists():
        return path
    path = ROOT/path
    if path.exists():
        return path
    return NOTES/Path(name).name


def exact_binary(x):
    return Q.from_float(float(x))


def trigonometry_exact(k):
    return (1, 0, -1, 0)[k % 4], (0, 1, 0, -1)[k % 4]


def derivative_from_exact_data(tail, index, local, length, column):
    u0, u1 = [exact_binary(tail.first[k, column]) for k in (index, index+1)]
    v0, v1 = [length*exact_binary(tail.second[k, column]) for k in (index, index+1)]
    middle = exact_binary(tail.midpoint[index, column])
    bubble = 16*middle-8*(u0+u1)-2*(v0-v1)
    coefficients = [u0, v0, -3*u0+3*u1-2*v0-v1+bubble,
                    2*u0-2*u1+v0+v1-2*bubble, bubble]
    return sum((coefficient*local**power for power, coefficient in enumerate(coefficients)), Q(0))


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--author', type=Path, required=True)
    ap.add_argument('--replay', type=Path, required=True)
    ap.add_argument('--proof', type=Path, required=True)
    ap.add_argument('--out', type=Path, required=True)
    args = ap.parse_args()
    started = time.monotonic()
    author, replay = read(args.author), read(args.replay)
    check(sha(args.author) == '13311ea4ecb781d0607ff6b58880c5f70bd79db2df2527aa9de3b6d9ad2e1b5e',
          'Unexpected frozen author point result')
    check(sha(args.proof) == '955a6550b43efb88f25767eaa0636fdb2be6eb397175507319c96fdddb2b8f92',
          'Unexpected reviewed point proof revision')
    check(set(author) == set(replay) and all(author[k] == replay[k] for k in author if k != 'seconds'),
          'A mathematical replay field differs')
    check(author['checked_points'] == 12 and author['center_span'] == 17148 and
          author['neighbor_spans'] == 0, 'Unexpected finite point search')
    wrapper = HERE/'db6f-root-tail-m12-point.py'
    check(sha(wrapper) == author['script_sha256'] ==
          '5d950fa6caa3aff062ba5a62e743abac5b00d7ef0721930f299135d1dbdc1bb1',
          'Changed fixed-input wrapper')
    paths, data = {}, {}
    for key, item in author['inputs'].items():
        paths[key] = resolve(item['file'])
        check(sha(paths[key]) == item['sha256'], 'Changed declared input '+key)
        if key != 'point':
            data[key] = read(paths[key])
    geometry, packet, whole, old = [data[k] for k in ('geometry', 'packet', 'whole', 'old_witness')]
    manifest_hash = sha(paths['manifest'])
    check(geometry['tail_manifest_sha256'] == whole['tail_manifest_sha256'] ==
          packet['finite_tail_manifest_sha256'] == packet['new_manifest_sha256'] == manifest_hash,
          'Different actual finite maps')
    check(whole['geometry_sha256'] == sha(paths['geometry']) and
          whole['separate_tail_metric_certificate']['packet_sha256'] == sha(paths['packet']),
          'R21 whole-map certificate is not bound to this input')
    definitions = author['background_definition_hashes']
    check(definitions and definitions == packet['background_definition_hashes'] == old['background_definition_hashes'],
          'Different exact background definitions')
    for name, item in definitions.items():
        check(sha(resolve(item['file'])) == item['sha256'], 'Changed exact background file '+name)
    old_manifest_path = resolve(packet['old_manifest'])
    check(sha(old_manifest_path) == packet['old_manifest_sha256'] == old['manifest_sha256'],
          'Wrong old finite-map/background connection')
    old_parameters = read(old_manifest_path)['parameters']
    new_parameters = data['manifest']['parameters']
    changed = {key for key in set(old_parameters)|set(new_parameters)
               if old_parameters.get(key) != new_parameters.get(key)}
    allowed = {'auditSteps', 'depth', 'farPadding', 'initialCheckpoint', 'maxIterations',
               'modes', 'physicalDepth', 'quadrature', 'shootingParts', 'steps', 'traceFile'}
    check(changed <= allowed, 'An unreviewed physical/background parameter changed')
    primitive_path = resolve(old['primitive'])
    check(sha(primitive_path) == old['primitive_sha256'] == author['primitive_sha256'], 'Changed exact primitive')
    primitive = read(primitive_path)
    check(primitive['inputs'] == definitions and primitive['parameters'] == old_parameters,
          'Primitive belongs to another physical background')
    source_hashes = dict(author['source_sha256'])
    source_hashes.update(primitive['sources'])
    source_hashes['db6f-audit-metric-polynomial.py'] = '02f9da4d86c7514bf90a3cfd185be85274c7ad0b9b34d3d20ede342d6b8adea4'
    for name, digest in source_hashes.items():
        check(sha(HERE/name) == digest, 'Changed mathematical source '+name)
    reader_path = HERE/'db6f_tail_integrated.py'
    spec = importlib.util.spec_from_file_location('independent_point_binary_reader', reader_path)
    reader = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = reader
    spec.loader.exec_module(reader)
    tail = reader.IntegratedTail(paths['manifest'])
    selected = author['selected_witness']
    index, u, quarter = selected['span'], Q(selected['local_exact']), selected['angle_multiple_of_pi_over_six']
    check(index == 17148 and u == Q(3, 4) and quarter == 2, 'Unexpected selected exact point')
    check(tail.unscaled_lengths is not None, 'Expected exact increment representation')
    radial = tail.meta['radialGeometry']
    inner, outer = Q(radial['innerAnchor']), Q(radial['outerAnchor'])
    raw_lengths = [exact_binary(x) for x in tail.unscaled_lengths]
    scale = (outer-inner)/sum(raw_lengths, Q(0))
    check(scale == tail.radial_scale, 'Reader radial normalization differs from exact Fraction reconstruction')
    radius = inner+scale*(sum(raw_lengths[:index], Q(0))+u*raw_lengths[index])
    length = scale*raw_lengths[index]
    check(radius == Q(selected['radius_exact']) and length > 0, 'Wrong exact physical witness radius')
    rr, tr, zr = Q(0), Q(0), Q(0)
    for col, mode in enumerate(tail.planar_modes):
        mode = int(mode)
        check((mode-1) % 3 == 0, 'Wrong planar congruence class')
        co, si = trigonometry_exact(((mode-1)//3)*quarter)
        value = derivative_from_exact_data(tail, index, u, length, col)
        rr += value*co
        tr += value*si
    for col, mode in enumerate(tail.height_modes, tail.P):
        mode = int(mode)
        check(mode >= 0 and mode % 3 == 0, 'Wrong height congruence class')
        co, _ = trigonometry_exact((mode//3)*quarter)
        zr += derivative_from_exact_data(tail, index, u, length, col)*co
    wl, wh = map(Q, selected['w_interval'])
    check(0 < wl <= wh and tr == 0, 'Unexpected point background or tangent symmetry')
    C = 2*rr+rr*rr+tr*tr+zr*zr
    numerator = sorted((C+2*zr*wl, C+2*zr*wh))
    denominator = (1+wl*wl, 1+wh*wh)
    quotients = [n/d for n in numerator for d in denominator]
    exact_range = (min(quotients), max(quotients))
    reported = tuple(map(Q, selected['normalized_component_intervals'][0]))
    check(reported[0] <= exact_range[0] <= exact_range[1] <= reported[1],
          'The reported radial-diagonal interval misses exact Fraction reconstruction')
    lower = Q(selected['relative_operator_lower'])
    check(lower == reported[0] == Q(author['whole_actual_metric_error_lower_exact']) ==
          Q(370012576184137, 18889465931478580854784), 'Unexpected exact radial lower endpoint')
    check(lower > Q('1.95883e-8') and lower > Q('9.79415')*Q('2e-9'),
          'Unsafe displayed strict threshold or conditional future comparison')
    result = dict(status='PASS-independent-M12-point-lower-fixed-g-and-Fraction-audit',
        scope=__doc__, script_sha256=sha(__file__),
        inputs={key: dict(file=str(path), sha256=sha(path)) for key, path in {
            'author': args.author, 'replay': args.replay, 'proof': args.proof, 'wrapper': wrapper}.items()},
        all_replay_mathematical_fields_equal=True, ignored_replay_fields=['seconds'],
        same_exact_background_files_verified=len(definitions),
        changed_numerical_parameters=sorted(changed), all_other_physical_parameters_equal=True,
        primitive_parameters_exactly_equal_old_manifest=True,
        mathematical_source_sha256=source_hashes,
        exact_radius=str(radius), exact_radial_scale=str(scale),
        radial_scale_is_dyadic=(scale.denominator & (scale.denominator-1)) == 0,
        direct_fraction_radial_diagonal_interval=[str(x) for x in exact_range],
        root_interval_contains_independent_exact_fraction_interval=True,
        strict_whole_error_lower_exact=str(lower), safe_decimal_lower_exact='1.95883e-8',
        conditional_future_improvement_factor_exact='195883/20000',
        future_same_g_whole_error_assumption_exact='1/500000000',
        future_error_assumption_already_certified=False, whole_surface_upper_computed=False,
        fixed_g_convergence_gate_5_paid=False, seconds=time.monotonic()-started)
    args.out.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(dict(status=result['status'], exact_lower=str(lower),
        direct_fraction_range_contained=True, same_physical_background=True,
        radial_scale_is_dyadic=result['radial_scale_is_dyadic'], seconds=result['seconds'])))


if __name__ == '__main__':
    main()
