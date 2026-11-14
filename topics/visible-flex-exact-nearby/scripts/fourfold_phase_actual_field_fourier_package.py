#!/usr/bin/env python3
"""Preserved exact Fourier/time polynomial for one actual strict field germ.

Recovery and preservation revision, 2026-11-12. The interrupted unpublished
summary-only package never reached an observed completion and saved no P.
This version adds a new exact dyadic coefficient contract; it is not claimed
to reproduce the old bytes or to inherit any unobserved numerical result.

P(u,theta) has physical theta period pi/2 and real coefficients as a function
on real u,theta. Its positive Fourier coefficients are saved exactly; negative
coefficients are their exact conjugates. All input balls, rounding fees, alias
terms and the full time/angular rectangular complement are separate from P.
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
from flint import arb, acb, acb_series, ctx

from fourfold_phase_beta_interval import ball_record
from fourfold_phase_beta_bulk_interval import exact_arb
from fourfold_phase_beta_affine import sha
from fourfold_phase_field_time_refined_root import (
    RefinedGermTimeModel, prepare_refined_root,
)
from fourfold_phase_uniform_field_time_grid_fast import uniform_f
from fourfold_boundary_fourier_budget import time_fourier_budget


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT/'data'/'phase_ring_continuation'


def write_json(path, value):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(path.name+'.writing')
    temporary.write_text(json.dumps(value, indent=2)+'\n')
    temporary.replace(path)


def positive_upper(record):
    """Read the directed decimal enclosure, not the approximate float."""
    value = arb(record['upper']).upper()
    if not value.is_finite() or not value > 0:
        raise ValueError('a finite strictly positive upper bound is required')
    return value


def dyadic_pair(value):
    """Exact midpoint as signed integer times a power of two."""
    if not value.is_finite() or not value.is_exact():
        raise ValueError('only an exact finite dyadic value may define P')
    mantissa, exponent = value.man_exp()
    encoded = [str(int(mantissa)), int(exponent)]
    restored = arb((int(encoded[0]), encoded[1]))
    if not restored.is_exact() or restored != value:
        raise ValueError('exact dyadic serialization roundtrip failed')
    return encoded


def read_dyadic(pair):
    if (not isinstance(pair, list) or len(pair) != 2
            or not isinstance(pair[0], str) or not isinstance(pair[1], int)):
        raise ValueError('malformed exact dyadic scalar')
    value = arb((int(pair[0]), pair[1]))
    if not value.is_exact() or dyadic_pair(value) != pair:
        raise ValueError('dyadic decoding is not exact at the current precision')
    return value


def encode_complex(value):
    return [*dyadic_pair(value.real), *dyadic_pair(value.imag)]


def decode_complex(row):
    if not isinstance(row, list) or len(row) != 4:
        raise ValueError('malformed complex coefficient')
    return acb(read_dyadic(row[:2]), read_dyadic(row[2:]))


def preserve_polynomial(model, values, degree, directory, identity, shard_time=4):
    """Choose, save and exactly reload P, returning all-node coefficient fees.

    Real-node Taylor coefficients are real mathematical quantities. Node
    midpoints are therefore chosen on the real axis. The positive-frequency
    DFT midpoint is chosen exactly; k=0 is projected to its known real value.
    The negative coefficient is DEFINED as its conjugate. Reality of the
    true Fourier coefficients transfers the same error bound to negative k.
    """
    directory = Path(directory)
    nodes, precision = values.shape[0], model.precision
    if (values.ndim != 2 or values.shape[1] != 1 or nodes < 2
            or nodes & (nodes-1) or not 0 <= degree < nodes//2 or shard_time < 1):
        raise ValueError('invalid field grid or retained polynomial dimensions')
    directory.mkdir(parents=True, exist_ok=True)
    midpoint = np.empty((nodes, 1), dtype=object)
    node_total = [arb(0) for _ in range(precision)]
    node_maximum = [arb(0) for _ in range(precision)]
    for j in range(nodes):
        if values[j, 0].prec < precision:
            raise ValueError('insufficient retained field time coefficients')
        row = []
        for i in range(precision):
            value = values[j, 0][i]
            if not value.is_finite() or not value.imag.contains(0):
                raise ValueError('real-node field reality or finiteness gate failed')
            fee = value.real.rad().upper()
            node_total[i] += fee
            node_maximum[i] = max(node_maximum[i], fee)
            row.append(acb(value.real.mid()))
        midpoint[j, 0] = acb_series(row, prec=precision)
    node_average = [(v/nodes).upper() for v in node_total]
    tick, cpu = time.monotonic(), time.process_time()
    transformed = model.target.fourier.fft(midpoint)/nodes
    transform_seconds, transform_cpu = time.monotonic()-tick, time.process_time()-cpu
    del midpoint

    manifest = dict(kind='exact_dyadic_real_Fourier_time_polynomial',
        schema_version=1, complete=False, identity=identity,
        source_sha256=sha(__file__), coefficient_encoding='[real_m,real_e,imag_m,imag_e]; m*2**e',
        frequency_scale=4, Fourier_degree=int(degree), time_precision=int(precision),
        bits_at_construction=int(ctx.prec), positive_frequency_indices=[0, int(degree)],
        negative_frequency_rule='P_i,-k=conjugate(P_i,k); P_i,0 is real',
        polynomial_definition='sum_j sum_k c[j,k]*u**j*exp(4*I*k*theta), I**2=-1',
        field_coordinate='physical f=dtheta/dtau; no time-halfwidth multiplier',
        shards=[], exactly_reloaded=False,
        scope='finite polynomial definition only; analytic approximation certificate is separate')
    manifest_path = directory/'manifest.json'
    write_json(manifest_path, manifest)
    roundoff = [arb(0) for _ in range(precision)]
    for start in range(0, precision, shard_time):
        stop = min(start+shard_time, precision)
        coefficients = []
        for i in range(start, stop):
            row = []
            for k in range(degree+1):
                value = transformed[k, 0][i]
                if not value.is_finite():
                    raise ValueError('nonfinite directed Fourier coefficient')
                selected = acb(value.real.mid(), 0 if k == 0 else value.imag.mid())
                fee = abs(value-selected).upper()
                roundoff[i] = max(roundoff[i], fee)
                encoded = encode_complex(selected)
                if decode_complex(encoded) != selected:
                    raise ValueError('selected complex coefficient did not reload exactly')
                row.append(encoded)
            coefficients.append(row)
        payload = dict(kind='exact_dyadic_real_Fourier_time_polynomial_shard',
            time_start=start, time_stop=stop, Fourier_degree=degree,
            identity=identity, coefficients=coefficients)
        raw = (json.dumps(payload, separators=(',', ':'), ensure_ascii=True)+'\n').encode()
        compressed = gzip.compress(raw, compresslevel=9, mtime=0)
        filename = 'coefficients_t%03d_%03d.json.gz' % (start, stop-1)
        destination = directory/filename
        temporary = destination.with_name(destination.name+'.writing')
        temporary.write_bytes(compressed)
        temporary.replace(destination)
        manifest['shards'].append(dict(path=filename, time_start=start, time_stop=stop,
            sha256=hashlib.sha256(compressed).hexdigest(), bytes=len(compressed)))
        write_json(manifest_path, manifest)
    del transformed
    combined = [(a+b).upper() for a,b in zip(node_average, roundoff)]
    if not all(v.is_finite() and v >= 0 for row in
               (node_average, node_maximum, roundoff, combined) for v in row):
        raise ValueError('invalid directed coefficient error')
    manifest['coefficient_error_budget'] = {
        'mean_true_real_node_errors':[ball_record(v) for v in node_average],
        'max_true_real_node_errors':[ball_record(v) for v in node_maximum],
        'max_directed_DFT_and_midpoint_choice_errors':[ball_record(v) for v in roundoff],
        'combined_retained_Fourier_coefficient_errors':[ball_record(v) for v in combined]}
    manifest['complete'] = True
    write_json(manifest_path, manifest)
    loaded, coefficient = load_polynomial(manifest_path)
    if (loaded['identity'] != identity or coefficient.shape !=
            (precision, 2*degree+1)):
        raise ValueError('complete polynomial reload failed')
    del coefficient
    manifest['exactly_reloaded'] = True
    write_json(manifest_path, manifest)
    return manifest_path, combined, dict(
        mean_node_errors=node_average, max_node_errors=node_maximum,
        max_exact_midpoint_DFT_rounding=roundoff, combined_DFT_noise=combined,
        DFT_seconds=transform_seconds, DFT_cpu_seconds=transform_cpu)


def load_polynomial(manifest_path):
    """Load the saved exact polynomial, requiring every shard/hash/shape."""
    manifest_path = Path(manifest_path)
    manifest = json.loads(manifest_path.read_text())
    if (manifest.get('kind') != 'exact_dyadic_real_Fourier_time_polynomial'
            or not manifest.get('complete') or manifest['schema_version'] != 1
            or manifest['frequency_scale'] != 4):
        raise ValueError('unsupported or incomplete finite polynomial')
    precision, degree = manifest['time_precision'], manifest['Fourier_degree']
    out = np.empty((precision, 2*degree+1), dtype=object)
    next_time = 0
    for shard in manifest['shards']:
        path = manifest_path.parent/shard['path']
        if (path.stat().st_size != shard['bytes'] or sha(path) != shard['sha256']
                or shard['time_start'] != next_time):
            raise ValueError('polynomial shard hash/size/order mismatch')
        payload = json.loads(gzip.decompress(path.read_bytes()))
        start, stop = shard['time_start'], shard['time_stop']
        if (payload['time_start'] != start or payload['time_stop'] != stop
                or payload['Fourier_degree'] != degree
                or payload['identity'] != manifest['identity']
                or len(payload['coefficients']) != stop-start):
            raise ValueError('polynomial shard metadata mismatch')
        for offset, row in enumerate(payload['coefficients']):
            if len(row) != degree+1:
                raise ValueError('polynomial coefficient row has wrong length')
            i = start+offset
            for k, encoded in enumerate(row):
                z = decode_complex(encoded)
                if k == 0 and z.imag != 0:
                    raise ValueError('Fourier zero mode is not exactly real')
                out[i, degree+k] = z
                out[i, degree-k] = acb(z.real, -z.imag)
        next_time = stop
    if next_time != precision:
        raise ValueError('missing time coefficient shards')
    return manifest, out


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--object', type=Path,
        default=DATA/'type_fixed_step02_d5_exact_affine_step5_object.json')
    parser.add_argument('--root-certificate', type=Path,
        default=DATA/'type_fixed_step02_d5_exact_affine_step5_root_tight.json')
    parser.add_argument('--domain-certificate', type=Path,
        default=DATA/'type_fixed_step02_d5_exact_affine_step5_reference419_whole_angle_time_domain.json')
    parser.add_argument('--germ-index', type=int, default=2)
    parser.add_argument('--angles', type=int, default=4096)
    parser.add_argument('--degree', type=int, default=1800)
    parser.add_argument('--time-order', type=int, default=52)
    parser.add_argument('--quarter-nodes', type=int, default=1024)
    parser.add_argument('--bits', type=int, default=320)
    parser.add_argument('--inner-physical-theta-strip', default='81/10000')
    parser.add_argument('--branch-sign', type=int, choices=(-1, 1), default=-1)
    parser.add_argument('--shard-time', type=int, default=4)
    parser.add_argument('--polynomial-dir', type=Path)
    parser.add_argument('--out', type=Path, required=True)
    args = parser.parse_args()
    started, cpu = time.monotonic(), time.process_time()
    ctx.prec, ctx.cap = args.bits, max(21, args.time_order+4)
    domain = json.loads(args.domain_certificate.read_text())
    if not (domain.get('complete')
            and domain.get('proved_full_physical_angle_and_complex_time_domain')
            and domain.get('complete_common_span_coverage')):
        raise ValueError('a completed whole physical-angle/complex-time domain is required')
    if (domain['target_object_sha256'] != sha(args.object)
            or domain['target_root_sha256'] != sha(args.root_certificate)):
        raise ValueError('domain and exact graph/root identities differ')
    if not 0 <= args.germ_index < len(domain['germs']):
        raise ValueError('invalid selected germ index')
    selected = domain['germs'][args.germ_index]
    if not selected['passed']:
        raise ValueError('selected analytic germ did not pass')
    cell = tuple(map(Fraction, selected['common_span']))
    left, right = map(Fraction, domain['exact_time_endpoints'])
    radius = Fraction(domain['time_radius'])
    outer_strip = Fraction(domain['physical_theta_strip'])
    inner_strip = Fraction(args.inner_physical_theta_strip)
    if (left == right or radius <= 1 or not 0 <= inner_strip < outer_strip
            or not 0 <= args.degree < args.angles//2):
        raise ValueError('invalid exact time/strip/retention data')
    modulus = positive_upper(selected['true_field_moduli']['f'])
    package = prepare_refined_root(args.object, args.root_certificate,
                                   nodes=args.quarter_nodes)
    if Fraction(domain['exact_delta_fraction']) != package.exact_delta:
        raise ValueError('domain and native evaluator have different exact parameters')
    tick = time.monotonic()
    model = RefinedGermTimeModel(args.object, args.root_certificate,
        (left+right)/2, (right-left)/2, refined_root=package, cell=cell,
        nodes=args.quarter_nodes, order=args.time_order, outer_radius=radius,
        branch_sign=args.branch_sign)
    geometry_seconds = time.monotonic()-tick
    required = [tuple(map(Fraction, row)) for row in domain['required_common_spans']]
    if required != model.required_common_cells:
        raise ValueError('domain and native model have different required common spans')
    identity = dict(object_sha256=sha(args.object),
        root_certificate_sha256=sha(args.root_certificate),
        domain_certificate_sha256=sha(args.domain_certificate),
        exact_delta_fraction=str(package.exact_delta),
        exact_time_endpoints=list(map(str, (left, right))),
        tau_center=str((left+right)/2), time_halfwidth=str((right-left)/2),
        common_span=list(map(str, cell)), germ_index=args.germ_index,
        branch_sign=args.branch_sign)
    polynomial_directory = args.polynomial_dir or args.out.with_name(args.out.stem+'_polynomial')
    report = dict(kind='directed_actual_strict_field_exact_polynomial_package',
        complete=False, source_sha256=sha(__file__),
        recovery_revision='new exact dyadic preservation; interrupted summary-only run not inherited',
        identity=identity, root_refinement=package.provenance,
        dependency_sha256={name:sha(Path(__file__).with_name(name)) for name in (
            'fourfold_phase_uniform_field_time_grid.py',
            'fourfold_phase_uniform_field_time_grid_fast.py',
            'fourfold_phase_field_time_refined_root.py',
            'fourfold_phase_field_time_taylor.py',
            'fourfold_phase_beta_interval.py', 'fourfold_phase_beta_bulk_interval.py',
            'fourfold_phase_beta_bulk_box.py', 'fourfold_phase_beta_affine.py',
            'fourfold_boundary_fourier_budget.py')},
        bits=args.bits, primitive_quarter_nodes=args.quarter_nodes,
        angular_nodes=args.angles, retained_Fourier_degree=args.degree,
        retained_time_order=args.time_order, time_outer_radius=str(radius),
        physical_outer_strip=str(outer_strip), physical_inner_strip=str(inner_strip),
        actual_joint_outer_modulus=ball_record(modulus),
        geometry_seconds=geometry_seconds, finite_polynomial_saved=False,
        complete_actual_piecewise_time_field=False)
    write_json(args.out, report)
    print(json.dumps(dict(stage='geometry', seconds=geometry_seconds)), flush=True)
    values, _, timing = uniform_f(model, args.angles, Fraction(0))
    report['grid_timing'] = timing
    write_json(args.out, report)
    print(json.dumps(dict(stage='whole real field grid', timing=timing)), flush=True)
    polynomial_manifest, errors, noise = preserve_polynomial(model, values, args.degree,
        polynomial_directory, identity, args.shard_time)
    report['finite_polynomial_saved'] = True
    report['polynomial_manifest'] = str(polynomial_manifest)
    report['polynomial_manifest_sha256'] = sha(polynomial_manifest)
    report['node_and_DFT_errors'] = {key:[ball_record(v) for v in noise[key]]
        for key in ('mean_node_errors', 'max_node_errors',
                    'max_exact_midpoint_DFT_rounding', 'combined_DFT_noise')}
    report['DFT_seconds'] = noise['DFT_seconds']
    report['DFT_cpu_seconds'] = noise['DFT_cpu_seconds']
    write_json(args.out, report)
    budgets = {}
    for derivative in (0, 1, 2):
        budget = time_fourier_budget(args.angles, args.degree, arb(0),
            exact_arb(outer_strip), exact_arb(inner_strip), modulus,
            exact_arb(radius), arb(1), errors, derivative=derivative, frequency_scale=4)
        if not all(v.is_finite() and v >= 0 for v in budget.values()):
            raise ValueError('nonfinite or negative complete reconstruction fee')
        budgets[str(derivative)] = {key:ball_record(value) for key,value in budget.items()}
    report['complete_time_Fourier_derivative_error_budgets'] = budgets
    checks = []
    for j in sorted({0, args.angles//7, args.angles//3, args.angles-1}):
        theta = acb(arb.pi()*j/(2*args.angles))
        direct, _ = model.time_field([theta])
        for i in range(model.precision):
            lhs, rhs = values[j, 0][i], direct[0][i]
            if not (lhs.real.overlaps(rhs.real) and lhs.imag.overlaps(rhs.imag)):
                raise ValueError('batch and direct true field coefficients disagree')
        checks.append(dict(node=j, all_retained_f_coefficients_overlap=True))
    report['independent_direct_node_checks'] = checks
    report['complete'] = True
    report['continuous_field_on_selected_germ_extension_proved'] = True
    report['elapsed_seconds'] = time.monotonic()-started
    report['cpu_seconds'] = time.process_time()-cpu
    report['limitations'] = [
        'The finite polynomial is saved exactly; it is not the actual infinite field',
        'All reported errors apply on |u|<=1 and the stated inner physical-theta strip',
        'Only the selected analytic germ extension is approximated',
        'Actual piecewise time coverage still requires all active germs',
        'No composition with the nonuniform reference, complete flow, Wiener map, or PDE conclusion']
    write_json(args.out, report)
    print(json.dumps(dict(complete=True,
        polynomial_manifest=str(polynomial_manifest),
        errors={key:value['total']['ball'] for key,value in budgets.items()},
        elapsed_seconds=report['elapsed_seconds'], cpu_seconds=report['cpu_seconds']),
        indent=2), flush=True)


if __name__ == '__main__':
    main()

