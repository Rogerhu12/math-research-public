#!/usr/bin/env python3
"""Original full residual/C2/metric diagnostics on one real unaccepted field.

Every nodal component and physical parameter is retained. No Jacobian, Newton,
BVP or tail solver is called. The original physical quintic and sampled audit
are evaluated once on this previously unaudited input; only radial batch sizes
are reduced. All original radial/angle samples, mean quadrature and arithmetic
formulas remain. Additional observations read the original metric arrays.
These diagnostics never create an accepted run or an admissible tail input.
"""
import os
for _key in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[_key] = '2'

import argparse
import hashlib
import importlib.util
import inspect
import json
from pathlib import Path
import resource
import sys
import textwrap
import time
from types import MethodType, SimpleNamespace

import numpy as np
import scipy.integrate._bvp as bvp

HERE = Path(__file__).resolve().parent
sys.path[:0] = [str(HERE), str(HERE.parent/'analytic'),
                str(HERE.parents[1]/'resume_m3')]
import check_unaccepted_design_delta_nodes_v2 as builder
import exception_safe_radial_batches as batches
import material_core_evaluate_cache as core_cache
import metric_audit_observer_v2 as metric_observer
import complete_factor_mmap as allocator


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def ref(path):
    path = Path(path).resolve()
    return dict(path=str(path), sha256=sha(path))


def rebatch_method(owner, name, replacements):
    """Change only declared radial loop and slice literals in a fresh method."""
    original = getattr(owner, name)
    function = original.__func__
    if function.__code__.co_freevars:
        raise ValueError('The declared radial method unexpectedly has closure state')
    source = textwrap.dedent(inspect.getsource(function))
    changed = source
    for old, new in replacements:
        if changed.count(old) != 1:
            raise ValueError('The original radial batch anchor changed: '+old)
        changed = changed.replace(old, new, 1)
    space = dict(function.__globals__)
    exec(compile(changed, str(Path(__file__).resolve())+'::'+name, 'exec'), space)
    setattr(owner, name, MethodType(space[function.__name__], owner))
    return dict(method=name, original_file=ref(inspect.getsourcefile(function)),
        original_function_sha256=hashlib.sha256(source.encode()).hexdigest(),
        executed_function_sha256=hashlib.sha256(changed.encode()).hexdigest(),
        declared_literal_replacements=replacements,
        all_radial_and_angular_points_retained=True,
        original_floating_formulas_retained=True, batch_bitwise_comparison_performed=False)


def install_geometry_observer(adaptive, physical_x, block):
    installation = metric_observer.install(adaptive)
    _, source, _ = metric_observer.derive(Path(adaptive.__file__))
    old = 'metric_observer.observe(s,first,errors,metric_fft,metric_rows,N)'
    new = ("metric_observer.observe(s,first,errors,metric_fft,metric_rows,N,"
           "g['theta'],Fs,Ft/a[:,None,None],fr['Vnormal'],a,fr['margin'])")
    patches = [('for first in range(0,len(ss),32):',
                'for first in range(0,len(ss),%d):' % block),
               ('s=ss[first:first+32]', 's=ss[first:first+%d]' % block),
               (old, new)]
    for before, after in patches:
        if source.count(before) != 1:
            raise ValueError('The exact observed-audit batch/context anchor changed')
        source = source.replace(before, after, 1)

    class GeometryObserver(metric_observer.MetricObserver):
        def __init__(self):
            super().__init__()
            self.inlet = None

        def observe(self, s, first, errors, transformed, sums, N,
                    theta, Fs, Ftheta_over_a, normal_velocity, radius, margin):
            super().observe(s, first, errors, transformed, sums, N)
            try:
                for component, row in enumerate(self.rows):
                    if row is None or not first <= row['radial_sample_index'] < first+len(s):
                        continue
                    i = row['radial_sample_index']-first
                    j = row['pointwise_max_psi_index']
                    nearest = int(np.argmin(np.abs(physical_x-s[i])))
                    interval = int(np.clip(np.searchsorted(physical_x,s[i],side='right')-1,
                                           0,len(physical_x)-2))
                    row.update(physical_theta=float(theta[i,j]),
                        original_uniform_psi=float(2*np.pi*j/N),
                        normalized_metric_components_at_point=errors[i,j].tolist(),
                        nearest_physical_node=nearest,
                        distance_to_nearest_physical_node=float(abs(physical_x[nearest]-s[i])),
                        original_physical_interval=physical_x[interval:interval+2].tolist(),
                        physical_radius=float(radius[i]), Frenet_margin=float(margin[i,j]),
                        physical_Fs=Fs[i,j].tolist(),
                        physical_Ftheta_over_a=Ftheta_over_a[i,j].tolist(),
                        original_normal_velocity=normal_velocity[i,j].tolist(),
                        flow_velocity_defect_at_point=(Fs[i,j]-normal_velocity[i,j]).tolist(),
                        zero_radial_location=bool(s[i] == 0),
                        source='Only arrays already present in this original audit block')
                if self.inlet is None and np.any(s == 0):
                    i = int(np.flatnonzero(s == 0)[0])
                    self.inlet = dict(s=0., metric_component_fft_l1=sums[i].tolist(),
                        metric_component_pointwise_max=np.max(np.abs(errors[i]),axis=0).tolist(),
                        core_error_source_identified=False)
            except Exception as error:
                self.errors.append(type(error).__name__+': '+str(error))

        def finish(self, original, N):
            result = super().finish(original, N)
            result['inlet_same_audit_arrays'] = self.inlet
            result['radial_reconstruction_vs_angular_error_source_proved'] = False
            return result

    space = dict(adaptive.audit.__globals__)
    space['__original_metric_observer_factory'] = GeometryObserver
    exec(compile(source, str(Path(__file__).resolve())+'::complete_observed_audit', 'exec'), space)
    adaptive.audit = space['audit']
    return dict(original_observer_installation=installation,
        executed_function_sha256=hashlib.sha256(source.encode()).hexdigest(),
        additional_declared_replacements=patches, radial_batch=block,
        additional_model_or_J_or_FFT_calls=0, same_input_previous_audit_rerun=False,
        original_all_samples_and_mean_quadrature_retained=True,
        acceptance_claimed=False, batch_bitwise_comparison_performed=False)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ('repo', 'source-run', 'checkpoint-metadata', 'outdir'):
        parser.add_argument('--'+name, type=Path, required=True)
    parser.add_argument('--rhs-block', type=int, default=8)
    parser.add_argument('--geometry-block', type=int, default=4)
    args = parser.parse_args()
    repo, source, metadata_path, out = (p.resolve() for p in
        (args.repo, args.source_run, args.checkpoint_metadata, args.outdir))
    if out == repo or repo in out.parents or min(args.rhs_block,args.geometry_block)<1:
        raise ValueError('Use a fresh scratch output and positive radial batches')
    run_bytes, meta_bytes = source.read_bytes(), metadata_path.read_bytes()
    record, metadata = json.loads(run_bytes), json.loads(meta_bytes)
    raw = metadata_path.parent/metadata['file']
    if (metadata.get('kind') != 'unaccepted_complete_nodal_restart'
            or metadata.get('accepted_bvp') is not False
            or metadata.get('before_full_J_assembly') is not True
            or sha(raw) != metadata['sha256'] or record.get('actual_tail_requested')):
        raise ValueError('Require the genuine complete unaccepted linear-port field')
    hashes = dict(record['source_hashes'])
    hashes.update(record['inputs'])
    hashes.update(metadata['original_source_hashes'])
    for filename, expected in hashes.items():
        if sha(filename) != expected:
            raise ValueError('An original source or complete input changed: '+filename)
    with np.load(raw, allow_pickle=False) as data:
        x,y,p,scales = (data[k].copy() for k in ('x','y','p','pscale'))
    M = record['modes']
    if (x.shape!=(metadata['nodes'],) or y.shape!=(3*M+1,len(x)) or p.shape!=(M,)
            or scales.shape!=(M-1,) or not np.array_equal(scales,record['parameter_scales'])
            or not all(np.isfinite(v).all() for v in (x,y,p,scales))
            or not np.all(np.diff(x)>0) or x[0]!=0 or x[-1]!=1):
        raise ValueError('The complete original nodal dimensions or parameter scales differ')
    out.mkdir(parents=True,exist_ok=False)
    (out/'source-run-snapshot.json').write_bytes(run_bytes)
    (out/'checkpoint-metadata-snapshot.json').write_bytes(meta_bytes)
    started = time.monotonic()
    events = out/'events.jsonl'

    def event(name, **fields):
        row = dict(event=name, seconds=time.monotonic()-started,
            maximum_RSS_KiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss, **fields)
        with events.open('a') as stream:
            stream.write(json.dumps(row,allow_nan=False)+'\n')
        print(json.dumps(row,allow_nan=False),flush=True)

    obj,table_stats,branch = builder.build_original_model(record,repo)
    if not np.array_equal(obj.pscale,scales):
        raise ValueError('The original model changed the complete parameter coordinates')
    cls = sys.modules['portable_m3_custom_core'].MaterialFlattenedSupportCore
    memo_stats = core_cache.install(cls)
    stats = batches.statistics()
    fun = batches.split_rhs(obj.fun,args.rhs_block,stats)
    obj.initial(p)
    h = np.diff(x)
    col,middle_y,f,middle_f = bvp.collocation_fun(fun,y,p,x,h)
    spline = bvp.create_spline(y,f,x,h)
    rms = bvp.estimate_rms_residuals(fun,spline,x,h,p,1.5*col/h,middle_f)
    bc = obj.bc(y[:,0],y[:,-1],p)
    physical_bc = obj.terminal(y[:,-1],p)*obj.bcweights
    if not all(np.isfinite(v).all() for v in (col,rms,bc,physical_bc)):
        raise FloatingPointError('An original complete residual is not finite')
    worst = int(np.argmax(rms))
    residuals = dict(maximum_RMS=float(rms[worst]),worst_interval_index=worst,
        worst_reference_interval=x[worst:worst+2].tolist(),
        maximum_collocation_residual=float(np.max(np.abs(col))),
        maximum_BC=float(np.max(np.abs(bc))),
        maximum_physical_terminal_BC=float(np.max(np.abs(physical_bc))),
        intervals_above_original_tol=int(np.count_nonzero(rms>record['gates']['tol'])),
        all_original_node_midpoint_RMS_sample_domains_passed=True,
        original_gates=record['gates'], BVP_acceptance_claimed=False)
    (out/'residuals.json').write_text(json.dumps(residuals,indent=2,allow_nan=False)+'\n')
    event('complete_original_unaccepted_residuals_returned',**residuals)
    obj.initial(p)
    flow = obj.flow(p[0])
    physical = SimpleNamespace(x=obj.chart(x,p[0])[0],y=y,p=p)
    block = args.geometry_block
    methods = []
    methods.append(rebatch_method(flow,'adapt_fun',[
        ('range(0,len(s),64)',f'range(0,len(s),{block})'),
        ('slice(first,first+64)',f'slice(first,first+{block})')]))
    methods.append(rebatch_method(flow,'c2_interpolant',[
        ('range(0,len(s),64)',f'range(0,len(s),{block})'),
        ('slice(first,first+64)',f'slice(first,first+{block})')]))
    methods.append(rebatch_method(flow,'height_integral',[
        ('range(0,len(flat),128)',f'range(0,len(flat),{block})'),
        ('flat[first:first+128]',f'flat[first:first+{block}]'),
        ('means[first:first+128]',f'means[first:first+{block}]')]))
    physical.sol = flow.c2_interpolant(physical)
    physical_path = out/'unaccepted-diagnostic-physical.npz'
    np.savez_compressed(physical_path,x=physical.x,c=physical.sol.c,p=p)
    event('original_full_physical_quintic_returned',physical=ref(physical_path),
        nodes=len(x),accepted_BVP=False)
    adaptive = sys.modules['portable_m3_coupler'].adaptive
    observation = install_geometry_observer(adaptive,physical.x,block)
    allocator_result = allocator.collect_and_trim()
    requested_N = int(builder.option(record,'--audit-angular'))
    audit = adaptive.audit(obj,physical,requested_N)
    event('original_full_unaccepted_metric_audit_returned',metric=audit['metric_l1'],
        components=audit['metric_observation']['components'],
        inlet=audit['metric_observation']['inlet_same_audit_arrays'],
        accepted_BVP=False)
    report = dict(kind='original_complete_unaccepted_physical_metric_diagnostic',scope=__doc__,
        source_role='actual_unaccepted_complete_1185_node_field_after_two_original_Newton_steps',
        source_run=ref(source),source_run_snapshot=ref(out/'source-run-snapshot.json'),
        checkpoint_metadata=ref(metadata_path),checkpoint=ref(raw),
        source_hashes={str(q.resolve()):sha(q) for q in
            (Path(__file__),Path(builder.__file__),Path(batches.__file__),Path(core_cache.__file__),
             Path(metric_observer.__file__),Path(bvp.__file__),Path(allocator.__file__))},
        original_definition_hashes=hashes,original_model_branch=branch,
        original_core_settings=record['core_settings'],original_profile=record['physical_profile'],
        original_gauge_q=obj.q,original_warp_reference=record['warp_reference'],
        physical_delta=float(obj.cfg['delta']+p[0]),all_parameters=p.tolist(),
        nodes=len(x),modes=M,angular=obj.nt,original_RHS_batch=args.rhs_block,
        residual_observation=residuals,unaccepted_physical_representation=ref(physical_path),
        physical_quintic_and_mean_batch_transforms=methods,metric_observer=observation,
        actual_prefix_audit=audit,original_all_audit_samples_retained=True,
        original_height_integral_order=6,actual_audit_angular_samples=audit['samples_psi'],
        radial_batch_change_bitwise_comparison_performed=False,
        actual_fourier_table_cache=table_stats,actual_core_memo=memo_stats,
        actual_radial_batch_statistics=stats,preaudit_unused_allocator_release=allocator_result,
        Jacobian_assembled=False,Newton_or_BVP_or_native_solver_invoked=False,
        old_accepted_field_audit_rerun=False,BVP_acceptance_claimed=False,
        diagnostic_field_may_be_used_as_accepted_or_tail_input=False,
        metric_error_source_proved=False,continuous_error_bound_claimed=False,
        seconds=time.monotonic()-started,
        maximum_RSS_KiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    target = out/'diagnostic.json'
    target.write_text(json.dumps(report,indent=2,allow_nan=False)+'\n')
    event('unaccepted_original_diagnostic_finished',report=ref(target),
        accepted_BVP=False,Jacobian_or_BVP_or_native_called=False)


if __name__ == '__main__':
    main()
