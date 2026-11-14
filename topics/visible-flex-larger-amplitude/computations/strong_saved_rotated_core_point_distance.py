#!/usr/bin/env python3
"""Stream finite-set distances from a saved core point to rotated saved points.

AI-assisted research workflow, strong_recovery, 2026-11-13.
P is the actually stored, unsolved fine warm prefix point set. Q is its exact
Cartesian quarter-turn R(x,y,z)=(-y,x,z). The second diagnostic set includes
R_z(P), where R_z(x,y,z)=(x,y,-z). The selected W is an actual saved core point,
not a point manufactured from a desired low-mode amplitude.

The finite dyadic minimum is enclosed with a complete streamed scan and an
exact exhibited-pair upper bound. Missing continuum, tail, and cap points may
decrease the distance. No continuous Hausdorff lower bound, complete closed
surface, actual new solution, or noncongruence statement is produced. These
prescribed rotated finite sets are congruent by construction.
"""
from __future__ import annotations
import os
for _name in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[_name] = '1'
import argparse
import datetime
from fractions import Fraction
import gzip
import hashlib
import io
import json
import math
from pathlib import Path
import resource
import time
import numpy as np


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def read(path):
    return json.loads(Path(path).read_text())


def exact(value):
    value = Fraction(value)
    return dict(numerator=str(value.numerator), denominator=str(value.denominator))


def binary(value):
    return Fraction.from_float(float(value))


def sqrt_interval(value, bits=100):
    value = Fraction(value)
    if value < 0:
        raise ValueError('Nonnegative squared distance required')
    n = math.isqrt((value.numerator << (2*bits))//value.denominator)
    low = Fraction(n, 1 << bits)
    high = low if low*low == value else Fraction(n+1, 1 << bits)
    if not low*low <= value <= high*high:
        raise ArithmeticError('Exact square-root sandwich failed')
    return low, high


def main():
    p = argparse.ArgumentParser(description=__doc__)
    for name in ('screen', 'geometry-resource', 'prepared-core', 'point-root', 'out'):
        p.add_argument('--'+name, type=Path, required=True)
    a = p.parse_args()
    start = time.monotonic()
    if a.out.exists():
        raise FileExistsError('Use a fresh diagnostic output')
    screen, owned, prepared = map(read, (a.screen, a.geometry_resource, a.prepared_core))
    if (owned.get('exitcode') != 0 or not owned.get('wait4_observed')
            or not screen['finished'] or screen['nonlinear_solution']
            or screen['worker_start_attempts'] != 0 or not screen['finite_domain_passed']):
        raise ValueError('An actually completed unsolved fine warm geometry is required')
    if (np.asarray(screen['actual_core'], dtype=np.float64).tobytes()
            != np.asarray(prepared['actual_complete_core'], dtype=np.float64).tobytes()):
        raise ValueError('The full saved warm core differs from the prepared core')
    geometry = screen['geometry_fields']
    capture = geometry['actual_point_cloud']
    point_path = a.point_root/capture['file']
    grid_path = a.point_root/geometry['grid_file']
    if sha(point_path) != capture['sha256'] or sha(grid_path) != geometry['grid_sha256']:
        raise ValueError('The complete point-cloud or coordinate-grid identity differs')
    manifest, grid = read(point_path), read(grid_path)
    shape = tuple(manifest['shape'])
    t = np.asarray(grid['numerical_t'], dtype=np.float64)
    if (manifest['schema'] != 'complete-geometry-chunks-v1' or manifest['dtype'] != 'float64'
            or not manifest['complete'] or shape != (len(t), int(grid['angular']), 3)
            or shape[1] % 4 or t[0] != 0. or t[-1] != 1. or not np.all(np.diff(t) > 0)
            or capture['components'] != ['x', 'y', 'z'] or not capture['actual_prefix_only']
            or capture['complete_original_mean'] != 1552):
        raise ValueError('The original complete fine point-cloud conventions differ')
    states = {name:dict(minimum_float_squared=math.inf, selected=None, points_scanned=0)
              for name in ('quarter_rotated_prefix', 'quarter_rotated_reflected_union')}
    coverage, chunks, W, witness = 0, [], None, None
    for chunk_number, item in enumerate(manifest['chunks']):
        path = point_path.parent/item['file']
        data = path.read_bytes()
        if (hashlib.sha256(data).hexdigest() != item['sha256'] or item['start'] != coverage
                or not 0 <= item['start'] < item['end'] <= shape[0]):
            raise ValueError('A complete point chunk or its contiguous coverage differs')
        values = np.load(io.BytesIO(gzip.decompress(data)), allow_pickle=False)
        if (values.dtype != np.float64 or values.shape != (item['end']-item['start'], shape[1], 3)
                or not np.isfinite(values).all() or np.max(abs(values)) >= 1024.):
            raise ValueError('Finite small complete Cartesian point chunks are required')
        if W is None:
            j = int(np.argmax(values[0, :, 0]))
            W = values[0, j].copy()
            witness = dict(chunk_number=chunk_number, chunk_file=str(path),
                chunk_sha256=item['sha256'], radial_index=0, angular_index=j,
                numerical_t=float(t[0]), physical_s=0., eta=float(2*np.pi*j/shape[1]),
                cartesian=W.tolist(), selection='Maximum saved x on the entire actual first radial/core row',
                saved_core_max_abs_z=float(np.max(abs(values[0, :, 2]))),
                witnessed_point_is_in_P=True)
        flat = values.reshape(-1, 3)
        for reflected in (False, True):
            rotated = np.column_stack((-flat[:, 1], flat[:, 0],
                                       -flat[:, 2] if reflected else flat[:, 2]))
            delta = rotated-W
            squared = np.sum(delta*delta, axis=1)
            if not np.isfinite(squared).all() or np.any(squared < 0):
                raise ArithmeticError('Finite nonnegative squared distances required')
            k = int(np.argmin(squared))
            names = ('quarter_rotated_reflected_union',) if reflected else tuple(states)
            for name in names:
                state = states[name]
                state['points_scanned'] += len(flat)
                value = float(squared[k])
                if value < state['minimum_float_squared']:
                    radial = item['start']+k//shape[1]
                    angular = k % shape[1]
                    eta = float(2*np.pi*angular/shape[1])
                    at_core_axis = radial == 0 and angular % (shape[1]//4) == 0
                    state['minimum_float_squared'] = value
                    state['selected'] = dict(chunk_number=chunk_number, chunk_file=str(path),
                        chunk_sha256=item['sha256'], radial_index=radial, angular_index=angular,
                        numerical_t=float(t[radial]), eta=eta,
                        physical_s=0. if radial == 0 else None,
                        physical_theta=eta if at_core_axis else None,
                        physical_theta_symbolic=(str(2*angular)+'*pi/'+str(shape[1])) if at_core_axis else None,
                        coordinate_explanation=('At t=0, s=0; at a quarter-period core axis all even-mode sine chart offsets vanish.'
                            if at_core_axis else 'Numerical t and eta are exact stored indices; a separate original chart replay is needed for physical s/theta.'),
                        separate_physical_coordinate_replay_needed=not at_core_axis,
                        source_point=flat[k].tolist(), reflected_in_z=reflected,
                        rotated_point=rotated[k].tolist())
        coverage = item['end']
        chunks.append(dict(file=str(path), sha256=item['sha256'], start=item['start'],
                           end=item['end'], bytes=len(data)))
        del flat, values, data, delta, squared, rotated
    if coverage != shape[0] or W is None:
        raise ValueError('The complete saved point set was not covered')
    u = Fraction(1, 2**53)
    allowance = Fraction(1, 2**1000)
    for state in states.values():
        q = binary(state['minimum_float_squared'])
        lower_q = max(Fraction(0), (q-allowance)/(1+u)**5)
        selected = state['selected']
        upper_q = sum((binary(x)-binary(y))**2 for x,y in zip(W, selected['rotated_point']))
        low, unused = sqrt_interval(lower_q)
        unused, high = sqrt_interval(upper_q)
        if low > high:
            raise ArithmeticError('Finite-set distance bounds crossed')
        state.update(exact_selected_pair_squared_distance=exact(upper_q),
            complete_scan_squared_distance_lower=exact(lower_q),
            finite_set_min_distance_lower=exact(low), finite_set_min_distance_upper=exact(high),
            distance_display=[float(low), float(high)],
            selected_pair_is_a_float_scan_minimizer=True,
            no_exact_unique_nearest_point_claim=True)
    core = [binary(x) for x in screen['actual_core']]
    axis_gap = 2*sum(core[::2], Fraction(0))
    report = dict(schema='complete-saved-core-to-rotated-point-set-distance-v1', scope=__doc__,
        created_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
        source_sha256=sha(__file__), input_sha256={str(p):sha(p) for p in
            (a.screen, a.geometry_resource, a.prepared_core, point_path, grid_path)},
        point_shape=list(shape), complete_original_mean_angular=1552,
        complete_prefix_points=int(shape[0]*shape[1]), all_original_chunks_consumed=True,
        chunks=chunks, witness=witness, distance_diagnostics=states,
        exact_quarter_turn_matrix=[[0,-1,0],[1,0,0],[0,0,1]],
        reflection_matrix=[[1,0,0],[0,1,0],[0,0,-1]],
        coordinate_contract=geometry['common_coordinates'],
        complete_stored_core_axis_support_gap=exact(axis_gap), core_axis_gap_display=float(axis_gap),
        set_and_family_scope=dict(P='Exactly the saved unsolved fine warm Cartesian prefix samples.',
            second_unrotated_set='P union R_z(P), explicitly a finite diagnostic union.',
            rotation_connection='Quarter-turn is the geometric core phase rotation used by the planar core witness. This consumer applies that exact Cartesian rotation to the saved prefix point set; it does not certify an accepted all-time extension or the rotation action on fixed caps.',
            W_membership='W is copied from the actually saved core row, and belongs to both unrotated diagnostic sets.',
            added_continuum_tail_or_cap_points_can_decrease_distance=True,
            finite_directed_Hausdorff_lower_witness_only=True,
            these_prescribed_sets_are_rigidly_congruent_by_construction=True,
            not_a_deltaE_or_noncongruence_witness=True,
            continuous_Hausdorff_or_closed_surface_deltaHold_lower_bound=False),
        roundoff_contract=dict(unit_roundoff=exact(u), positive_squared_sum_relative_factors=5,
            absolute_subnormal_allowance=exact(allowance),
            exact_selected_pair_arithmetic=True, exact_sqrt_sandwich_bits=100,
            geometry_interpolation_or_continuum_cover_error_paid=False),
        new_ODE_Node_Newton_or_geometry_field_calls=0,
        elapsed_seconds=time.monotonic()-start, peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    with a.out.open('x') as stream:
        json.dump(report, stream, indent=2, allow_nan=False)
        stream.write('\n')
    print(json.dumps(dict(event='complete_saved_rotated_distance_finished', output=str(a.out),
        sha256=sha(a.out), distances={k:v['distance_display'] for k,v in states.items()},
        selected_indices={k:[v['selected']['radial_index'],v['selected']['angular_index']] for k,v in states.items()},
        original_core_gap=float(axis_gap), new_field_calls=0)), flush=True)


if __name__ == '__main__':
    main()
