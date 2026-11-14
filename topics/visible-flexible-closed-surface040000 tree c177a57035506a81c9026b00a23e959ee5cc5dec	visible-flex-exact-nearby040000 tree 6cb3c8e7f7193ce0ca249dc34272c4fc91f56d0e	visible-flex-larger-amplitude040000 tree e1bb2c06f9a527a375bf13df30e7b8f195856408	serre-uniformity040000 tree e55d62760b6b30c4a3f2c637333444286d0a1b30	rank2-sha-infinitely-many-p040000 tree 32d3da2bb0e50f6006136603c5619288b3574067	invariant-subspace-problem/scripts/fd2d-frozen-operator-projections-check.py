#!/usr/bin/env python3
"""One two-node actual-4251 operator/jet/JVP and R155-view comparison.

No global residual, Jacobian, body, ODE or BVP is evaluated. The original
local two-node value chain is called once on each arithmetic provider to
confirm that the explicit R155 background view retains the new mixin.
"""
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[key] = '1'
import argparse
import copy
import hashlib
import json
from pathlib import Path
import resource
import time
import numpy as np
from fd2d_gc_archive_arrays import identity, load_npz
from fd2d_gc_midpoint_refined_positive_trace_v3 import create_midpoint_refined_problem
from fd2d_gc_positive_trace_stream_normal import radial_view
from fd2d_gc_raw_bump_dae import RawBumpDAE
from fd2d_gc_frozen_operator_projections import (
    install_frozen_operator_projection_cache, frozen_projection_operator_direction)


def difference(a, b):
    aa, bb = np.asarray(a), np.asarray(b)
    if aa.shape != bb.shape:
        raise ValueError('Comparison shape mismatch')
    if not np.all(np.isfinite(aa)) or not np.all(np.isfinite(bb)):
        raise FloatingPointError('Nonfinite compared array')
    return dict(shape=list(aa.shape), maximum_absolute=float(np.max(abs(aa-bb), initial=0.)),
                maximum_scaled=float(np.max(abs(aa-bb)/(1+abs(aa)), initial=0.)),
                bitwise_equal=bool(aa.dtype == bb.dtype and aa.tobytes() == bb.tobytes()))


def old_direction(view, operators, direction):
    """Differentiate the original, unfactored angular projection formula."""
    jet = operators['jet']; a = jet['a']
    da, dc = jet['a_parameters']@direction, jet['c_parameters']@direction
    inverse_direction = -da[None,:]/(view.coords['u_xi']*a[None,:]**2)
    op = np.zeros_like(operators['op'])
    for j in range(view.N):
        op[j,:view.e,:view.e] = -dc[j]*np.eye(view.e)
        op[j,:view.e,view.e:view.d] = view.PE@(inverse_direction[:,j,None]*view.Ox)
        op[j,:view.e,view.d:] = dc[j]*np.eye(view.e)
        op[j,view.e:,view.e:view.d] = -2*dc[j]*np.eye(view.K)
        op[j,view.e:,view.d:] = view.PO@(inverse_direction[:,j,None]*view.Ex)
    return dict(op=op, inv=inverse_direction, a=da, c=dc)


def main():
    p = argparse.ArgumentParser(description=__doc__)
    for name in ('input', 'candidate', 'radius-packet', 'reference-inlet', 'reference-cache', 'out'):
        p.add_argument('--'+name, type=Path, required=True)
    a = p.parse_args()
    if a.out.exists():
        raise FileExistsError('Use a new immutable small-check report')
    begun = time.perf_counter(); saved = load_npz(a.input)
    proof = json.loads(a.radius_packet.read_text())
    witness = dict(**identity(a.radius_packet), candidate_sha256=proof['candidate_sha256'])
    problem = create_midpoint_refined_problem(a.candidate, saved_field=saved, split_cells=(),
        max_step=.04, gap=.9, reference_inlet=a.reference_inlet, reference_cache=a.reference_cache,
        base_lower_bound='4/5', base_lower_provenance=witness, radius_floor=.1)
    if (problem.K, problem.N, problem.parameter_count) != (31,129,54):
        raise ValueError('This one-off fixture binds the actual K31/129/tail16 saved input')
    field, parameters = np.asarray(saved['corrections']), np.asarray(saved['parameters'])
    defining_names = ('seed_weight_definition', 'angular_atlas_definition', 'coast_reference_definition',
                      'reference_evaluation_definition', 'gauss_l_definition', 'positive_trace_definition',
                      'nested_angular_definition')
    definitions_before = {name:json.dumps(getattr(problem,name),sort_keys=True) for name in defining_names}
    # The one shared core evaluation is needed only by the original local
    # value chain below. No frame/body reconstruction is requested.
    problem.core(parameters[:problem.K])
    indices = np.array([64,65])
    old = radial_view(problem, indices)
    delta = parameters[problem.profile_parameter_slice].copy()
    if not np.any(delta != 0):
        raise ValueError('The check was requested at a genuinely nonzero physical delta')
    direction = (-1.)**np.arange(problem.J)*(1+np.arange(problem.J))/10
    alternative_delta = delta+1e-6*direction
    old_operators = [RawBumpDAE.operators(old, d) for d in (delta, alternative_delta)]
    old_jvp = old_direction(old, old_operators[0], direction)
    cache = install_frozen_operator_projection_cache(problem, byte_limit=32*1024*1024)
    new = radial_view(problem, indices)
    t = time.perf_counter(); first = new.operators(delta); miss_seconds = time.perf_counter()-t
    after_miss = cache.statistics()
    t = time.perf_counter(); second = new.operators(alternative_delta); hit_seconds = time.perf_counter()-t
    after_changed_delta = cache.statistics()
    compare = []
    for i, (before, after) in enumerate(zip(old_operators, (first,second))):
        compare.append(dict(delta_number=i,
            operator=difference(before['op'],after['op']),
            inverse=difference(before['inv'],after['inv']),
            advection=difference(before['adv'],after['adv']),
            scalar_and_parameter_jets={name:difference(before['jet'][name],after['jet'][name])
                                      for name in before['jet']}))
    new_jvp = frozen_projection_operator_direction(new, delta, direction)
    jvp = {name:difference(old_jvp[name],new_jvp[name]) for name in old_jvp}
    dy = np.cos(np.arange(2*problem.q).reshape(2,problem.q)/11)/17
    yy = field[indices]
    old_rhs = np.einsum('ndq,nq->nd',old_jvp['op'],yy)+np.einsum('ndq,nq->nd',old_operators[0]['op'],dy)
    new_rhs = np.einsum('ndq,nq->nd',new_jvp['op'],yy)+np.einsum('ndq,nq->nd',first['op'],dy)
    total_jvp = difference(old_rhs,new_rhs)
    # A fresh one-point copy must use its own x/N, while finding the
    # already frozen point in the shared cache.
    single = radial_view(problem, [int(indices[1])])
    single_result = single.operators(delta)
    copy_scope = dict(original_problem_nodes=problem.N, two_node_view_nodes=new.N,
        single_view_nodes=single.N, single_operator_shape=list(single_result['op'].shape),
        methods_bound_to_actual_views=bool(new.operators.__self__ is new and single.operators.__self__ is single),
        cache_identity_shared=bool(single._frozen_operator_projection_cache is cache
                                  and new._frozen_operator_projection_cache is cache),
        single_matches_same_two_node_slice=difference(first['op'][1],single_result['op'][0]))
    # Follow the original actual coast background and affine construction;
    # no global rows are assembled here.
    background = new.coast_background_view()
    affine = background.affine_view()
    background_scope = dict(background_class=type(background).__name__, affine_class=type(affine).__name__,
        background_cache_shared=bool(background._frozen_operator_projection_cache is cache),
        affine_cache_shared=bool(affine._frozen_operator_projection_cache is cache),
        methods_bound_to_actual_views=bool(background.operators.__self__ is background and affine.operators.__self__ is affine))
    local = np.r_[yy.ravel(), parameters]
    old_residual, old_data = old.evaluate(local, jacobian=False)
    new_residual, new_data = new.evaluate(local, jacobian=False)
    local_chain = dict(actual_input_nodes=indices.tolist(),
        residual=difference(old_residual,new_residual),
        fields=difference(old_data['fields'],new_data['fields']),
        Gauss=difference(old_data['full_gauss'],new_data['full_gauss']),
        Codazzi=difference(old_data['codazzi_cells'],new_data['codazzi_cells']),
        lifting_forcing=difference(old_data['lift']['forcing'],new_data['lift']['forcing']),
        scope='Only the original two-node local R153/R155 value chain, not the global finite objective')
    definitions_after = {name:json.dumps(getattr(problem,name),sort_keys=True) for name in defining_names}
    preserved = {name:definitions_before[name] == definitions_after[name] for name in defining_names}
    values = [q['operator']['maximum_scaled'] for q in compare]+[q['maximum_scaled'] for q in jvp.values()]
    values += [total_jvp['maximum_scaled'], local_chain['residual']['maximum_scaled']]
    passed = (max(values) < 2e-12 and all(preserved.values())
        and all(v['bitwise_equal'] for q in compare for v in q['scalar_and_parameter_jets'].values())
        and copy_scope['methods_bound_to_actual_views'] and copy_scope['cache_identity_shared']
        and background_scope['background_cache_shared'] and background_scope['affine_cache_shared']
        and cache.statistics()['explicit_background_view_wraps'] >= 2
        and after_miss['misses'] == 2 and after_changed_delta['misses'] == 2
        and after_changed_delta['hits'] >= 2
        and cache.statistics()['total_counted_bytes'] <= cache.byte_limit)
    report = dict(schema='fd2d-frozen-operator-projections-two-node-check-v1', passed=bool(passed),
        actual_execution=True, source=identity(__file__), input=identity(a.input), candidate=identity(a.candidate),
        adapter=identity(Path(__file__).with_name('fd2d_gc_frozen_operator_projections.py')),
        original_operator_source=identity(Path(__file__).with_name('fd2d_gc_raw_bump_dae.py')),
        radial_view_source=identity(Path(__file__).with_name('fd2d_gc_positive_trace_stream_normal.py')),
        bound_cache_definition=cache.binding, selected_input_nodes=indices.tolist(),
        physical_s=problem.x[indices].tolist(), actual_delta=delta.tolist(),
        nonzero_direction=direction.tolist(), changed_delta=alternative_delta.tolist(),
        point_operator_comparisons=compare, parameter_JVP=jvp, mixed_state_parameter_rhs_JVP=total_jvp,
        copy_scope=copy_scope, explicit_background_scope=background_scope,
        actual_two_node_value_chain=local_chain, original_field_definitions_unchanged=preserved,
        cache_after_first_two_points=after_miss, cache_after_different_delta=after_changed_delta,
        cache_final=cache.statistics(), first_miss_seconds=miss_seconds,
        changed_delta_hit_seconds=hit_seconds,
        timing_scope='Two points only; not a complete-run speed measurement or a diagnosis of process exit -9.',
        floating_refactor='old PE@((1/(U_xi*a))*Ox) vs new (PE@((1/U_xi)*Ox))/a, and corresponding PO/Ex block; real arithmetic identical.',
        no_BVP=True, no_whole_residual=True, no_whole_Jacobian=True, no_body=True,
        no_active_process_or_original_source_mutation=True,
        seconds=time.perf_counter()-begun, peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    a.out.write_text(json.dumps(report,indent=2,allow_nan=False)+'\n')
    print(json.dumps(dict(passed=report['passed'],maximum_operator_scaled=max(q['operator']['maximum_scaled'] for q in compare),
        maximum_JVP_scaled=max(q['maximum_scaled'] for q in jvp.values()),
        local_residual_scaled=local_chain['residual']['maximum_scaled'],
        cache=cache.statistics(),seconds=report['seconds'],peak_rss_kib=report['peak_rss_kib'])))
    if not passed:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
