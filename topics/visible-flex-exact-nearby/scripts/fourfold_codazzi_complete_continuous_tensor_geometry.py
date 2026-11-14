#!/usr/bin/env python3
"""Combine actual mesh, radial ODE and complete angular certificates.

Each saved radial cell receives the full tensor interpolation fee. Partial
radial inputs give only a recorded partial region, with no claim about the
waist witness or the complete surface. Resume consumes new original rows;
it checks the old row digest and never reintegrates the ODE.
"""
from __future__ import annotations
import argparse
from fractions import Fraction
import gzip
import hashlib
import json
from pathlib import Path
import time
from flint import arb, ctx
from fourfold_phase_beta_bulk_interval import exact_arb
from fourfold_phase_metric_defect import record
from fourfold_codazzi_rotational_cap_jacobi import box_from_record

CANDIDATE = 'ac1d5b98fbe77294c363e0a766c4322e8dd8c2024ef839d548f930c70330a413'
MESH = '5ed344a88f7f3015fff7a734283b430d0518abe0d4346abf63716893e4edb209'
ANGULAR = '7a3dd2c1d48b611f5d9a6bd8c2d7ebeeeb4c2f6a7c2bcc4f61f4d012be4e2f90'
RADIAL_SOURCE = '3347e0614a01300d770a40355214aa8135332faec9ba84121f1870ffd674d8bb'
KIND = 'complete_actual_model_tensor_geometry_from_original_native_rows_v1'


def digest(raw):
    return hashlib.sha256(raw).hexdigest()


def load(path):
    raw = Path(path).read_bytes()
    data = gzip.decompress(raw) if raw[:2] == bytes((31, 139)) else raw
    return json.loads(data), digest(raw)


def save(path, value):
    raw = (json.dumps(value, indent=2, allow_nan=False) + '\n').encode()
    if str(path).endswith('.gz'):
        raw = gzip.compress(raw, mtime=0)
    tmp = Path(str(path) + '.partial')
    tmp.write_bytes(raw)
    tmp.replace(path)


def row_bytes(row):
    return json.dumps(row, sort_keys=True, separators=(',', ':'), allow_nan=False).encode()


def upper(value):
    return box_from_record(value).upper()


def lower(value):
    return box_from_record(value).lower()


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--mesh', type=Path, required=True)
    ap.add_argument('--radial', type=Path, required=True)
    ap.add_argument('--angular', type=Path, required=True)
    ap.add_argument('--out', type=Path, required=True)
    ap.add_argument('--resume', action='store_true')
    args = ap.parse_args()
    if args.out.exists() != args.resume:
        raise FileExistsError('use a new output or explicit same-input resume')
    start = time.monotonic()
    ctx.prec, ctx.cap = 192, 6
    mesh, mesh_sha = load(args.mesh)
    radial, radial_sha = load(args.radial)
    angular, angular_sha = load(args.angular)
    if mesh_sha != MESH or angular_sha != ANGULAR:
        raise ValueError('the complete original mesh and angular natives are required')
    mi, ri = mesh['identity'], radial['identity']
    if (not mesh['complete'] or mesh['failure'] is not None or
        not angular['complete'] or angular['failure'] is not None or
        radial['failure'] is not None or ri['source_sha256'] != RADIAL_SOURCE):
        raise ValueError('a complete mesh/angle and a successful original radial prefix are required')
    if not (mi['candidate_sha256'] == ri['candidate_sha256'] ==
            angular['candidate_sha256'] == CANDIDATE):
        raise ValueError('the model candidate identity differs')
    for mk, rk in [('geometry_report_sha256', 'geometry_report_sha256'),
                   ('original_chain_sha256', 'original_geometry_chain_sha256'),
                   ('radial_grid_sha256', 'radial_grid_sha256')]:
        if mi[mk] != ri[rk]:
            raise ValueError('the model geometry identities differ: ' + mk)
    if (ri['object_sha256'] != angular['object_sha256'] or
        ri['actual_alpha'] != angular['exact_amplitude'] or
        ri['actual_nu'] != angular['exact_nu']):
        raise ValueError('the target or exact metric parameters differ')
    if (ri['angles'] != 512 or mesh['total_radial_cells'] != 8966 or
        radial['total_radial_rows'] != 8967 or angular['common_closed_box_count'] != 7722):
        raise ValueError('the complete original domains differ')
    if not (angular['full_real_angular_circle'] and
            angular['complete_original_6143_value_jumps_paid'] and
            radial['whole_closed_radial_intervals'] and
            radial['all_connection_modes_retained']):
        raise ValueError('a complete mode, interface or continuous domain assertion is missing')
    if not all(x['complete_endpoint_bits_equal'] for x in radial['block_checks']):
        raise ValueError('an original numerical radial endpoint changed')
    mesh_rows = mesh['rows']
    radial_rows = radial['rows']
    if (len(mesh_rows) != 8966 or
        [x['radial_index'] for x in mesh_rows] != list(range(8965, -1, -1)) or
        [x['radial_index'] for x in radial_rows] != list(range(8965, 8965-len(radial_rows), -1))):
        raise ValueError('the complete mesh or radial prefix is unordered or has a hole')
    identity = dict(source_sha256=digest(Path(__file__).read_bytes()),
        candidate_sha256=CANDIDATE, mesh_sha256=mesh_sha, angular_sha256=angular_sha,
        radial_identity=ri, exact_world_height_translation=mi['exact_height_translation'],
        dependencies={name:digest(Path(__file__).with_name(name).read_bytes()) for name in (
            'fourfold_phase_beta_bulk_interval.py', 'fourfold_phase_metric_defect.py',
            'fourfold_codazzi_rotational_cap_jacobi.py')})
    angular_F = upper(angular['bounds']['position_second_angular_derivative'])
    angular_N = upper(angular['bounds']['frame_second_angular_derivative'])
    angle_fee_F = ((arb.pi() / 1024)**2 * angular_F / 8).upper()
    angle_fee_N = ((arb.pi() / 1024)**2 * angular_N / 8).upper()
    if args.resume:
        doc, _ = load(args.out)
        if doc['identity'] != identity or doc['complete'] or doc['failure'] is not None:
            raise ValueError('only a successful same-identity partial tensor consumer may resume')
        done, elapsed = len(doc['rows']), doc['wall_seconds']
        if done >= len(radial_rows):
            raise ValueError('no genuinely new completed radial rows are available')
    else:
        done, elapsed = 0, 0.
        doc = dict(kind=KIND, identity=identity, complete=False, failure=None,
            total_radial_cells=8966, consumed_radial_cells=0,
            rows=[], radial_snapshots=[], wall_seconds=0.,
            tensor_proof='R133-supplement-complete-mesh-hulls-and-continuous-tensor-geometry.md, T.7--T.14',
            exact_angle_grid_and_true_fourfold_wrap=True,
            complete_angular_native_used=True,
            angular_interpolation_fees=dict(position=record(angle_fee_F), frame_normal=record(angle_fee_N)),
            original_model_anchor_errors_included=True,
            actual_exterior_world_anchor_error_included=False,
            continuous_repair_background_transfer_included=False,
            final_metric_parameter_change_included=False,
            nonlinear_exact_solution_correction_included=False,
            real_tail_caps_or_markers_included=False,
            geometric_surface_unit_normal_identified=False,
            final_closed_surface_geometry_proved=False)
    prefix = hashlib.sha256()
    for row in radial_rows[:done]:
        prefix.update(row_bytes(row))
    if done and prefix.hexdigest() != doc['consumed_radial_prefix_sha256']:
        raise ValueError('a previously consumed original radial row changed')
    previous_F = upper(radial['model_anchor_position_error']) if not done else upper(radial_rows[done-1]['cumulative_position_error'])
    previous_N = upper(radial['model_anchor_frame_error']) if not done else upper(radial_rows[done-1]['cumulative_frame_error'])
    try:
        for k, row in enumerate(radial_rows[done:], start=done):
            mesh_row = mesh_rows[k]
            if row['interval'] != mesh_row['interval'] or row['radial_index'] != mesh_row['radial_index']:
                raise ValueError('a true radial mesh cell differs')
            left, right = map(Fraction, row['interval'])
            h = exact_arb(right-left)
            if not h > 0:
                raise ValueError('a radial cell is not positive')
            second_F, second_N = [], []
            substeps = row['one_sided_germ_substeps']
            # The producer integrates backwards. Verify the actual whole
            # closed germ partition before taking any derivative maximum.
            expected = right
            for part in substeps:
                a, b = map(Fraction, part['interval'])
                if b != expected or not a < b:
                    raise ValueError('the complete scalar germ partition has a gap')
                expected = a
                A0, A1 = map(upper, part['connection_derivative_norms'][:2])
                f0, f1 = map(upper, part['radial_position_derivative_norms'][:2])
                second_F.append((A0*f0+f1).upper())
                second_N.append((A0*A0+A1).upper())
            if expected != left:
                raise ValueError('the scalar germs do not cover the complete mesh cell')
            MF, MN = max(second_F), max(second_N)
            current_F, current_N = upper(row['cumulative_position_error']), upper(row['cumulative_frame_error'])
            node_F, node_N = max(previous_F, current_F), max(previous_N, current_N)
            fee_F_r, fee_N_r = (h*h*MF/8).upper(), (h*h*MN/8).upper()
            fee_F, fee_N = (node_F+fee_F_r+angle_fee_F).upper(), (node_N+fee_N_r+angle_fee_N).upper()
            R, A, d = upper(mesh_row['vertex_radius_upper']), lower(mesh_row['bilinear_frame_support_lower']), lower(mesh_row['convex_hull_witness_distance_lower'])
            vals = dict(position_error=fee_F, frame_normal_error=fee_N,
                radial_position_interpolation_error=fee_F_r,
                radial_frame_normal_interpolation_error=fee_N_r,
                true_model_radius_upper=(R+fee_F).upper(),
                true_model_frame_support_lower=(A-fee_F-R*fee_N).lower(),
                distance_to_saved_witness_lower=(d-fee_F).lower())
            if not all(x.is_finite() for x in vals.values()):
                raise ValueError('a continuous tensor budget is nonfinite')
            doc['rows'].append(dict(radial_index=row['radial_index'], interval=row['interval'],
                complete_scalar_germ_count=len(substeps), **{key:record(value) for key,value in vals.items()}))
            prefix.update(row_bytes(row))
            previous_F, previous_N = current_F, current_N
        doc['consumed_radial_prefix_sha256'] = prefix.hexdigest()
        doc['consumed_radial_cells'] = len(doc['rows'])
        doc['radial_snapshots'].append(dict(sha256=radial_sha,
            complete=radial['complete'], complete_blocks=radial['complete_blocks'],
            radial_cells=len(radial_rows), newly_consumed_cells=len(radial_rows)-done))
        doc['complete'] = bool(radial['complete'] and len(doc['rows']) == 8966)
        if not doc['rows']:
            raise ValueError('no true radial cells were supplied')
        doc['continuous_certified_radial_interval'] = [doc['rows'][-1]['interval'][0], '25/8']
        doc['certified_region_bounds'] = dict(
            radius_upper=record(max(upper(x['true_model_radius_upper']) for x in doc['rows'])),
            frame_support_lower=record(min(lower(x['true_model_frame_support_lower']) for x in doc['rows'])),
            distance_to_saved_witness_lower=record(min(lower(x['distance_to_saved_witness_lower']) for x in doc['rows'])),
            position_error_upper=record(max(upper(x['position_error']) for x in doc['rows'])),
            frame_normal_error_upper=record(max(upper(x['frame_normal_error']) for x in doc['rows'])))
        if doc['complete']:
            waist = upper(radial_rows[-1]['cumulative_position_error'])
            doc['actual_model_waist_witness_error'] = record(waist)
            doc['complete_continuous_model_bounds'] = dict(
                radius_upper=doc['certified_region_bounds']['radius_upper'],
                frame_support_lower=doc['certified_region_bounds']['frame_support_lower'],
                distance_from_actual_rotated_waist_to_complete_reflected_model_lower=record(
                    (lower(doc['certified_region_bounds']['distance_to_saved_witness_lower'])-waist).lower()))
        doc['wall_seconds'] = elapsed+time.monotonic()-start
        save(args.out, doc)
    except Exception as error:
        doc['failure'] = dict(type=type(error).__name__, message=str(error))
        doc['wall_seconds'] = elapsed+time.monotonic()-start
        save(args.out, doc)
        raise
    print(json.dumps(dict(complete=doc['complete'], cells=doc['consumed_radial_cells'],
        certified_interval=doc['continuous_certified_radial_interval'],
        bounds=doc.get('complete_continuous_model_bounds', doc['certified_region_bounds']),
        newly_consumed_cells=len(radial_rows)-done, wall_seconds=doc['wall_seconds']), allow_nan=False))


if __name__ == '__main__':
    main()
