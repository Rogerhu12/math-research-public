#!/usr/bin/env python3
"""Bounded R170 finite-provider/archive check; never assemble F/J or solve."""
from __future__ import annotations
import argparse
import copy
import json
from pathlib import Path
import time
import numpy as np
from fd2d_gc_archive_arrays import identity, load_npz, save_npz
from fd2d_gc_raw_native_field import locate_bound
from fd2d_gc_raw_bump_dae import RawBumpDAE
from fd2d_dyadic_bernstein_tail import strict_witness_controls, DyadicBernsteinFlatDevelopableFamily
from fd2d_gc_dyadic_tail_problem import (
    create_dyadic_tail_problem, checkpoint_arrays, scaled_tail_linear_constraints)
from fd2d_gc_dyadic_tail_archive_native import (
    bind_dyadic_tail_archive_native, load_dyadic_tail_archive_body_reader)


def write(path, value):
    path = Path(path)
    if path.exists():
        raise FileExistsError(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value,indent=2,allow_nan=False)+'\n')


def same_bits(a, b):
    a, b = np.asarray(a), np.asarray(b)
    return a.dtype == b.dtype and a.shape == b.shape and a.tobytes() == b.tobytes()


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--foundation-definition',type=Path,required=True)
    ap.add_argument('--radius-packet',type=Path,required=True)
    ap.add_argument('--out-prefix',type=Path,required=True)
    args = ap.parse_args()
    if list(args.out_prefix.parent.glob(args.out_prefix.name+'*')):
        raise FileExistsError('Use a fresh output prefix')
    started = time.monotonic()
    meta = json.loads(args.foundation_definition.read_text())
    saved_path = locate_bound(args.foundation_definition,meta['arrays'])
    saved = load_npz(saved_path)
    candidate = locate_bound(args.foundation_definition,meta['candidate_input'])
    inlet = locate_bound(args.foundation_definition,meta['reference_inlet_input'])
    cache = locate_bound(args.foundation_definition,meta['reference_cache_input'])
    radius = json.loads(args.radius_packet.read_text())
    if not radius['passed'] or radius['candidate_sha256'] != identity(candidate)['sha256']:
        raise ValueError('Radius packet does not bind the same candidate')
    kwargs = dict(reference_inlet=inlet,reference_cache=cache,max_step=.04,gap=.9,
        reference_rim_fraction=float(meta['coast_reference_definition']['rim_fraction']),
        minimum_active_n=float(meta['gauss_l_definition']['selected_finite_evaluation_floor']),
        base_lower_bound='4/5',base_lower_provenance=identity(args.radius_packet),radius_floor=.1)
    problem = create_dyadic_tail_problem(candidate,saved_field=saved_path,split_cells=(),**kwargs)
    warm, refinement = problem.inject_saved_field()
    y,p = problem.unpack(warm)
    if not (same_bits(y,saved['corrections']) and same_bits(p,saved['parameters'])
            and same_bits(problem.x,saved['mesh'])):
        raise AssertionError('New search domain changed the initial field or mesh')
    actual = warm.copy()
    _, actual_p = problem.unpack(actual)
    actual_p[problem.tail_parameter_slice] = np.array([float(v) for v in strict_witness_controls()])
    tail = problem.tail(actual_p[problem.tail_parameter_slice])
    if type(tail) is not DyadicBernsteinFlatDevelopableFamily:
        raise AssertionError('The actual provider did not select the genuine new tail class')
    # Domain formula comparison at one real radial label, not a whole
    # operators/normal assembly. Central and profile predicates are retained.
    view = copy.copy(problem)
    index = 1
    view.x = problem.x[[index]].copy()
    view.N = 1
    view.h = np.diff(view.x)
    view.size = view.q+view.parameter_count
    view.coords = {key:(value[..., [index]].copy() if value.ndim and value.shape[-1]==problem.N
                       else value.copy()) for key,value in problem.coords.items()}
    view._operator_cache = {}
    point_vector = np.r_[y[[index]].ravel(),actual_p]
    old_rejected = not RawBumpDAE.parameter_domain(view,point_vector)
    new_permitted = view.parameter_domain(point_vector)
    if not old_rejected or not new_permitted:
        raise AssertionError('The intended strict domain enlargement was not consumed')
    scale = np.linspace(.3,1.4,problem.parameter_count)
    qp = scaled_tail_linear_constraints(problem,actual_p,scale)
    trial = np.linspace(-.2,.3,problem.parameter_count)
    left = qp['matrix']@trial
    right = qp['unscaled_tail_matrix']@(scale*trial)[problem.tail_parameter_slice]
    qp_difference = float(np.max(abs(left-right)))
    non_tail = np.ones(problem.parameter_count,bool)
    non_tail[problem.tail_parameter_slice] = False
    if np.any(qp['matrix'][:,non_tail] != 0.) or qp_difference > 1e-15:
        raise AssertionError('Tail rows used the wrong explicit parameter columns')
    arrays = checkpoint_arrays(problem,actual,identity(candidate)['sha256'],refinement_definition=refinement)
    arrays['R170_fixture_definition'] = np.array(json.dumps(dict(
        mathematical_state_changed_only_in_tail_controls=True,
        nonlinear_solve_or_acceptance=False,actual_residual_not_evaluated=True),sort_keys=True))
    row = save_npz(str(args.out_prefix)+'-fixture.npz',**arrays)
    restored = create_dyadic_tail_problem(candidate,saved_field=row['path'],split_cells=(),**kwargs)
    restored_warm, restored_definition = restored.inject_saved_field()
    if not same_bits(actual,restored_warm):
        raise AssertionError('New-domain archive restart changed defining bytes')
    native = bind_dyadic_tail_archive_native(row['path'],foundation_definition=args.foundation_definition)
    native_path = str(args.out_prefix)+'-native-definition.json'
    write(native_path,native.definition())
    body = load_dyadic_tail_archive_body_reader(native_path)
    uu = np.array([.7,1.1])
    cut = body.physical(body.trace_cut,uu)
    direct = tail.cut_port(uu,position_jets=False)
    diff = {key:float(np.max(abs(cut[key]-direct[key]))) for key in ('n','m','l','n_u','m_u','l_u')}
    if max(diff.values()) > 2e-14:
        raise AssertionError('New archive-native cut trace differs from the actual new tail')
    if not (same_bits(body.parameters,actual_p) and same_bits(body.values,y)
            and same_bits(body.nodes,problem.x)):
        raise AssertionError('New native decoder changed actual defining arrays')
    report = dict(schema='fd2d-R170-provider-archive-bounded-check-v1',
        source=identity(__file__),input_foundation=identity(args.foundation_definition),
        input_field=identity(saved_path),radius_packet=identity(args.radius_packet),
        actual_layout=dict(modes=problem.K,nodes=problem.N,raw_columns=problem.q,
            tail_count=16,parameter_count=problem.parameter_count,
            tail_slice=qp['tail_slice']),
        initial_field_mesh_and_parameter_bytes_preserved=True,
        actual_new_tail_class=type(tail).__module__+'.'+type(tail).__name__,
        old_global_box_rejected_witness=old_rejected,
        new_exact_domain_permitted_witness_at_one_operator_point=new_permitted,
        operator_point=float(view.x[0]),central_cap_screen_invoked=False,
        actual_domain_certificate=tail.control_certificate,
        full_parameter_matrix_shape=list(qp['matrix'].shape),
        all_non_tail_matrix_columns_exactly_zero=True,
        scaled_tail_row_identity_maximum_error=qp_difference,
        saved_fixture=row,restarted_complete_vector_bytewise_equal=True,
        archive_native_defining_arrays_bytewise_equal=True,
        new_archive_native_definition=identity(native_path),
        cut_trace_small_comparison=diff,
        provider_definition=problem.tail_search_domain_definition,
        provider_source=identity(Path(__file__).with_name('fd2d_gc_dyadic_tail_problem.py')),
        native_source=identity(Path(__file__).with_name('fd2d_gc_dyadic_tail_archive_native.py')),
        existing_sources_or_live_state_modified=False,
        whole_F_J_normal_BVP_or_body_evaluated=False,
        actual_nonlinear_acceptance_or_geometry_claimed=False,
        elapsed_seconds=time.monotonic()-started,internal_check_passed=True,
        process_exit_recorded_separately=True)
    report_path = str(args.out_prefix)+'-report.json'
    write(report_path,report)
    print(json.dumps(dict(report=report_path,passed=True,layout=report['actual_layout'],
        cut_max=max(diff.values()),qp_row_error=qp_difference,
        elapsed_seconds=report['elapsed_seconds']),allow_nan=False),flush=True)


if __name__ == '__main__':
    main()
