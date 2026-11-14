#!/usr/bin/env python3
"""Directed time residual on one actual saved Bernstein-reference subspan.

Selects an exact internal rational-time segment and an exact complex initial
label x.  The saved real/imaginary binary64 Fourier coefficients define the
reference; Arb evaluates them and converts the degree-seven Bernstein basis
exactly, with directed coefficient errors.  This is a local residual sample,
not a whole initial-circle, whole branch, or global true-flow certificate.
"""
from __future__ import annotations

import argparse
from fractions import Fraction
import gzip
import io
import json
import math
from pathlib import Path
import time

import numpy as np
from flint import arb, acb, acb_series, ctx

from fourfold_phase_beta_interval import series_constant, ball_record
from fourfold_phase_beta_bulk_interval import exact_arb
from fourfold_phase_beta_affine import sha
from fourfold_phase_field_time_taylor import FieldTimeModel, record_complex


def internal_rational_time(row):
    if row['kind'] != 'rational':
        raise ValueError('this strict sample accepts internal exact rational times only')
    return Fraction(int(row['numerator']), int(row['denominator']))


def load_segment(manifest_path, segment):
    manifest_path = Path(manifest_path)
    manifest = json.loads(manifest_path.read_text())
    if (not manifest.get('complete') or manifest.get('time_basis') != 'bernstein'
            or manifest['time_degree'] != 7 or manifest['fields'] != ['U', 'L']):
        raise ValueError('complete degree-seven U/L Bernstein reference required')
    if not 0 <= segment < manifest['segment_count']:
        raise ValueError('reference segment index outside the branch')
    shard = next(row for row in manifest['shards']
                 if row['start_segment'] <= segment < row['start_segment']+row['segment_count'])
    path = manifest_path.parent/shard['path']
    if sha(path) != shard['sha256'] or path.stat().st_size != shard['bytes']:
        raise ValueError('reference shard hash/size mismatch')
    with np.load(io.BytesIO(gzip.decompress(path.read_bytes())), allow_pickle=False) as saved:
        meta = json.loads(str(saved['metadata']))
        real, imag = saved['coefficient_real'].copy(), saved['coefficient_imag'].copy()
    first, count, K = shard['start_segment'], shard['segment_count'], manifest['Fourier_degree']
    if (meta['start_segment'] != first or meta['segment_count'] != count
            or meta['source_sha256'] != manifest['source_sha256']
            or meta['exact_times'] != manifest['exact_time_endpoints'][first:first+count+1]
            or real.shape != (count, 8, 2, K+1) or imag.shape != real.shape
            or not np.all(np.isfinite(real)) or not np.all(np.isfinite(imag))
            or np.any(imag[:, :, :, 0] != 0)):
        raise ValueError('reference shard convention/shape/exact times differ')
    row = segment-first
    left, right = map(internal_rational_time, manifest['exact_time_endpoints'][segment:segment+2])
    if manifest['time_orientation']*(right-left) <= 0:
        raise ValueError('nonpositive oriented exact segment')
    return manifest, shard, path, real[row], imag[row], left, right


def reference_time_coefficients(real, imag, label, sub_left, sub_right):
    """Evaluate finite real Fourier pairs, then exact Bernstein composition."""
    K = real.shape[-1]-1
    control = [[acb(0), acb(0)] for _ in range(8)]
    phases = [(acb(0, k)*label).exp() for k in range(K+1)]
    opposite = [(-acb(0, k)*label).exp() for k in range(K+1)]
    for j in range(8):
        for field in range(2):
            total = acb(arb(float(real[j, field, 0])))
            for k in range(1, K+1):
                cr, ci = arb(float(real[j, field, k])), arb(float(imag[j, field, k]))
                total += acb(cr, ci)*phases[k]+acb(cr, -ci)*opposite[k]
            control[j][field] = acb(total.real) if label.imag == 0 else total
    center, half = (sub_left+sub_right)/2, (sub_right-sub_left)/2
    u = acb_series([acb(exact_arb(center)), acb(exact_arb(half))])
    U, L = series_constant(0), series_constant(0)
    for j in range(8):
        basis = math.comb(7, j)*u**j*(1-u)**(7-j)
        U += control[j][0]*basis
        L += control[j][1]*basis
    Y = U+label/4
    return [Y[j] for j in range(8)], [L[j] for j in range(8)]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--manifest', type=Path, required=True)
    parser.add_argument('--object', type=Path, required=True)
    parser.add_argument('--root-certificate', type=Path, required=True)
    parser.add_argument('--segment', type=int, required=True)
    parser.add_argument('--initial-label-real', default='1/2')
    parser.add_argument('--initial-label-imag', default='0')
    parser.add_argument('--sub-left', default='3/8')
    parser.add_argument('--sub-right', default='5/8')
    parser.add_argument('--quarter-nodes', type=int, default=512)
    parser.add_argument('--jet-order', type=int, default=16)
    parser.add_argument('--outer-radius', default='8')
    parser.add_argument('--radial-radius', default='3/1000')
    parser.add_argument('--E-radius', default='1/400')
    parser.add_argument('--tail-sigma', default='8/25')
    parser.add_argument('--state-tube', default='1/65536')
    parser.add_argument('--bits', type=int, default=160)
    parser.add_argument('--out', type=Path, required=True)
    args = parser.parse_args()
    started = time.monotonic()
    ctx.prec = args.bits
    manifest, shard, shard_path, real, imag, a, b = load_segment(args.manifest, args.segment)
    ident = manifest['trace_identity']
    if ident['angular_scale'] != 4 or ident['sign'] not in (-1, 1):
        raise ValueError('physical-angle Y=x/4+U and an exact saved branch sign are required')
    if sha(args.object) != ident['source_sha256'] or sha(args.root_certificate) != ident['root_certificate_sha256']:
        raise ValueError('reference traces and exact graph/root are different objects')
    sub_left, sub_right = Fraction(args.sub_left), Fraction(args.sub_right)
    if not 0 <= sub_left < sub_right <= 1:
        raise ValueError('invalid exact normalized subspan')
    left, right = a+(b-a)*sub_left, a+(b-a)*sub_right
    tau0, h = (left+right)/2, (right-left)/2
    model = FieldTimeModel(args.object, args.root_certificate, tau0, h,
        nodes=args.quarter_nodes, order=args.jet_order, outer_radius=Fraction(args.outer_radius),
        radial_radius=Fraction(args.radial_radius), E_radius=Fraction(args.E_radius),
        tail_sigma=Fraction(args.tail_sigma), branch_sign=int(ident['sign']))
    label_re, label_im = Fraction(args.initial_label_real), Fraction(args.initial_label_imag)
    label = acb(exact_arb(label_re), exact_arb(label_im))
    theta, L = reference_time_coefficients(real, imag, label, sub_left, sub_right)
    result = model.residual_bound(theta, L, Fraction(args.state_tube))
    report = dict(kind='directed_actual_Bernstein_reference_time_residual_on_one_strict_subspan',
        complete=True, source_sha256=sha(__file__),
        field_engine_sha256=sha(Path(__file__).with_name('fourfold_phase_field_time_taylor.py')),
        native_dependency_sha256={name:sha(Path(__file__).with_name(name)) for name in
            ['fourfold_phase_beta_interval.py', 'fourfold_phase_beta_bulk_interval.py',
             'fourfold_phase_beta_bulk_box.py', 'fourfold_phase_beta_affine.py']},
        reference_manifest=str(args.manifest), reference_manifest_sha256=sha(args.manifest),
        reference_shard=shard['path'], reference_shard_sha256=sha(shard_path),
        object_sha256=sha(args.object), root_certificate_sha256=sha(args.root_certificate),
        exact_delta_fraction=str(model.target.affine_delta), segment=args.segment,
        original_exact_time_endpoints=[str(a), str(b)],
        normalized_subspan=[str(sub_left), str(sub_right)], exact_time_endpoints=[str(left), str(right)],
        tau_center=str(tau0), time_halfwidth=str(h),
        initial_label=dict(real=str(label_re), imag=str(label_im)),
        state_coordinate='physical theta=Y=x/4+U; reference Fourier label x has period 2*pi',
        branch_sign=int(ident['sign']), radial_common_cell=list(map(str, model.cell)),
        bits=args.bits, nodes=args.quarter_nodes, retained_time_order=args.jet_order,
        time_outer_radius=args.outer_radius, radial_tail_radius=args.radial_radius,
        E_tail_radius=args.E_radius, primitive_tail_normalized_angle_strip=args.tail_sigma,
        state_tube_radius=args.state_tube,
        reference_theta_coefficients=[record_complex(value) for value in theta],
        reference_L_coefficients=[record_complex(value) for value in L],
        e0_coefficients=[record_complex(result['e0'][j]) for j in range(model.precision)],
        e1_coefficients=[record_complex(result['e1'][j]) for j in range(model.precision)],
        residual_and_time_tail={key:ball_record(result[key]) for key in
                               ('e0_bound', 'e1_bound', 'e0_tail', 'e1_tail')},
        analytic_outer_domain={key:ball_record(value) for key, value in result['domain'].items()},
        reference_outer_image={key:ball_record(value) for key, value in result['image'].items()},
        E_infinite_error_on_radial_disk=ball_record(model.budget['E_error']),
        local_zero_initial_error_R60_budgets={key:ball_record(result[key]) for key in
                                             ('qmin', 'qmax', 'A', 'B', 'C', 'denominator', 'R', 'actual_error_upper')},
        hypothetical_matching_left_initial_flow_proved=result['local_matching_initial_flow_proved'],
        elapsed_seconds=time.monotonic()-started,
        limitations=['This is the actual frozen reference restricted to one exact label and one exact time subspan',
                     'No continuous initial-label grid/strip coverage or complete-time coverage is claimed',
                     'Zero initial error is a separate local model assumption, not the accumulated error of the global branch',
                     'No root collar, parameter derivatives, complete flow or Wiener residual certificate'])
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(report, indent=2)+'\n')
    print(json.dumps({key:report[key] for key in
          ['complete', 'segment', 'exact_time_endpoints', 'initial_label', 'residual_and_time_tail',
           'hypothetical_matching_left_initial_flow_proved', 'elapsed_seconds']}, indent=2), flush=True)


if __name__ == '__main__':
    main()
