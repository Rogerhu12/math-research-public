#!/usr/bin/env python3
"""Compare the actual lambda-zero/positive-lambda delta path on real nodal data.

This is explicitly a diagnostic of a saved current equation state. It does
not pass accepted_original, alter a run label, invoke a BVP/native solve or
assemble a complete collocation matrix. Every state/support column at the
selected actual nodes is retained in the original-vs-V5 comparison.
"""
import os
for _key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[_key] = '1'

import argparse
import gc
import hashlib
import importlib.util
import json
from pathlib import Path
import resource
import sys
import time
import numpy as np

HERE = Path(__file__).resolve().parent
SCRIPTS = HERE.parents[1]
sys.path[:0] = [str(HERE),str(SCRIPTS/'resume_20261126')]
from material_design_secant_predictor import option
from material_delta_column import OriginalDeltaColumn


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def ref(path):
    path = Path(path).resolve()
    return dict(path=str(path),sha256=sha(path))


def module(name,path):
    spec = importlib.util.spec_from_file_location(name,path)
    obj = importlib.util.module_from_spec(spec)
    sys.modules[name] = obj
    spec.loader.exec_module(obj)
    return obj


def difference(first,second):
    delta = np.abs(first-second)
    location = np.unravel_index(np.argmax(delta),delta.shape)
    return dict(maximum_absolute=float(np.max(delta)),
        relative_l2=float(np.linalg.norm(first-second)/max(np.linalg.norm(second),np.finfo(float).tiny)),
        maximum_location=list(map(int,location)),second_l2=float(np.linalg.norm(second)))


def build_original_model(record, repo):
    """Keep the portable source's real hasattr branch, including lambda zero."""
    source = Path(option(record,'--source-topic'))
    cfg = json.loads(Path(option(record,'--profile')).read_text())
    chart = json.loads(Path(option(record,'--chart')).read_text())
    port_path = Path(option(record,'--port'))
    port = json.loads(port_path.read_text())
    port['cut']['_prefix_bridge'] = cfg['prefix_bridge']
    port['_sha256'] = sha(port_path)
    scripts = source/'scripts'
    coupler = module('portable_m3_coupler',scripts/'db6f-prefix-coupled.py')
    module('portable_m3_flat',scripts/'db6f-prefix-flat-profile.py').install(coupler.adaptive)
    coupler.adaptive.old.install_source(source/'repro/source-root')
    module('portable_m3_short',Path(option(record,'--short-bridge'))).install()
    fourier = module('portable_m3_fourier_jac',scripts/'78718-prefix-fourier-jacobian.py')
    fourier.install(coupler.adaptive)
    cache = module('_unaccepted_actual_fourier_cache',HERE.parent/'design/cached_fourier_tables.py')
    table_stats = cache.install(fourier)
    provider = module('portable_m3_custom_core',Path(option(record,'--core-module')))
    settings = json.loads(Path(option(record,'--core-config')).read_text())
    factory = provider.make_factory(settings)
    __import__('fixed_metric_mode3_core').PlanarSupportCore = factory
    __import__('fixed_metric_mode3_bvp').PlanarSupportCore = factory
    Flow,Base = coupler.adaptive.build_classes(chart)
    sys.path.insert(0,str(SCRIPTS/'resume_m3/round_raw_lib'))
    from exact_core_lift import install_core_lift
    Base = install_core_lift(Flow,Base)
    available = hasattr(factory,'jet_parameter_derivatives')
    if available:
        import analytic_adaptive_core_jac as analytic
        analytic.parameter_jets = lambda core,theta: core.jet_parameter_derivatives(theta)
        analytic.install(Base)
    obj = Base(cfg,port,record['gauge_q'],record['modes'],record['angular'],False,record['warp_reference'])
    obj.bcweights = np.full(obj.M,record['gates']['physical_bc_tol']/record['gates']['bc_tol'])
    return obj,table_stats,dict(core_factory_has_jet_parameter_derivatives=available,
        original_analytic_core_parameter_install_called=available,
        live_V5_delta_install_called=available,
        actual_original_branch='analytic core-control path' if available else 'original full finite-difference parameter fallback',
        no_missing_factory_attribute_fabricated=True)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ('source-run','checkpoint-metadata','outdir'):
        parser.add_argument('--'+name,type=Path,required=True)
    parser.add_argument('--node-count',type=int,default=7)
    parser.add_argument('--steps',type=float,nargs='+',default=[1e-6,2e-7,5e-8])
    args = parser.parse_args()
    if not 1 <= args.node_count <= 9 or any(not np.isfinite(h) or h <= 0 for h in args.steps):
        raise ValueError('Use one to nine actual nodes and positive finite difference steps')
    out = args.outdir.resolve()
    repo = SCRIPTS.parents[2]
    if out == repo or repo in out.parents:
        raise ValueError('Keep scientific diagnostic arrays outside the source tree')
    run_bytes = args.source_run.read_bytes()
    meta_bytes = args.checkpoint_metadata.read_bytes()
    record,metadata = json.loads(run_bytes),json.loads(meta_bytes)
    checkpoint = (args.checkpoint_metadata.parent/metadata['file']).resolve()
    if (metadata.get('kind') != 'unaccepted_complete_nodal_restart'
            or metadata.get('accepted_bvp') is not False
            or metadata.get('before_full_J_assembly') is not True
            or sha(checkpoint) != metadata['sha256']):
        raise ValueError('Require a genuine complete unaccepted nodal checkpoint with matching SHA')
    for group in (record['source_hashes'],record['inputs'],metadata['original_source_hashes']):
        for path,expected in group.items():
            if sha(path) != expected:
                raise ValueError('A real checkpoint source/input changed: '+path)
    with np.load(checkpoint,allow_pickle=False) as saved:
        x,y,p,pscale = (saved[key].copy() for key in ('x','y','p','pscale'))
    M = record['modes']
    if (x.shape != (metadata['nodes'],) or y.shape != (3*M+1,len(x))
            or p.shape != (M,) or pscale.shape != (M-1,)
            or not all(np.all(np.isfinite(a)) for a in (x,y,p,pscale))
            or not np.all(np.diff(x)>0) or x[0] != 0 or x[-1] != 1
            or not np.array_equal(pscale,np.asarray(record['parameter_scales']))):
        raise ValueError('The complete original mesh/state/parameter coordinates differ')
    out.mkdir(parents=True,exist_ok=False)
    (out/'source-run-snapshot.json').write_bytes(run_bytes)
    (out/'checkpoint-metadata-snapshot.json').write_bytes(meta_bytes)
    started = time.monotonic()
    obj,table_stats,branch = build_original_model(record,repo)
    if not np.array_equal(obj.pscale,pscale):
        raise ValueError('The fresh original model changed the checkpoint parameter scales')
    indices = np.unique(np.rint(np.linspace(0,len(x)-1,args.node_count)).astype(int))
    t,yy = x[indices],y[:,indices]
    obj.initial(p)
    memo_path = HERE.parent/'design/material_core_evaluate_cache.py'
    memo = module('_unaccepted_delta_core_memo',memo_path)
    material_class = __import__('material_flattened_support_core').MaterialFlattenedSupportCore
    memo_stats = memo.install(material_class,max_entries=4)
    base = obj.fun(t,yy,p)
    original_dy,original_dp = obj.fun_jac(t,yy,p)
    analytical = OriginalDeltaColumn(obj,p).rhs(t,yy)
    adapter_path = HERE.parent/'design/analytic_delta_jac_adapter.py'
    adapter = module('_unaccepted_delta_actual_v5_adapter',adapter_path)
    adapter_stats = (adapter.install(type(obj)) if branch['live_V5_delta_install_called']
                     else dict(installed=False,reason='The original lambda-zero factory has no parameter-jet attribute; V5 installer is never called'))
    new_dy,new_dp = obj.fun_jac(t,yy,p)
    v5_RHS = obj.fun(t,yy,p)
    comparisons,columns = [],[]
    for step in args.steps:
        plus,minus = p.copy(),p.copy()
        plus[0] += step
        minus[0] -= step
        fd = (obj.fun(t,yy,plus)-obj.fun(t,yy,minus))/(2*step)
        row = dict(step=step,**difference(analytical,fd))
        row['source_node_at_maximum'] = int(indices[row['maximum_location'][1]])
        comparisons.append(row)
        columns.append(fd)
        print(json.dumps(dict(event='real_unaccepted_delta_FD',**row)),flush=True)
        gc.collect()
    restored = obj.fun(t,yy,p)
    invariants = dict(original_state_columns_bitwise_equal=bool(np.array_equal(original_dy,new_dy)),
        original_all_support_columns_bitwise_equal=bool(np.array_equal(original_dp[:,1:,:],new_dp[:,1:,:])),
        original_RHS_after_V5_install_bitwise_equal=bool(np.array_equal(base,v5_RHS)),
        original_base_RHS_restored_bitwise=bool(np.array_equal(base,restored)))
    if branch['live_V5_delta_install_called']:
        invariants['V5_delta_column_equals_declared_analytic_bitwise'] = bool(np.array_equal(new_dp[:,0,:],analytical))
    else:
        invariants['original_full_parameter_J_restored_bitwise'] = bool(np.array_equal(original_dp,new_dp))
    if not all(invariants.values()):
        raise ArithmeticError('A declared unchanged full-node RHS/Jacobian component changed: '+str(invariants))
    np.savez_compressed(out/'selected-complete-columns.npz',source_indices=indices,t=t,
        analytic=analytical,finite_differences=np.asarray(columns),steps=np.asarray(args.steps),
        original_dy=original_dy,original_dp=original_dp,actual_branch_repeated_dy=new_dy,actual_branch_repeated_dp=new_dp)
    report = dict(status='real_unaccepted_complete_node_delta_comparison_returned',
        scope=__doc__,source=ref(__file__),source_run_observed=dict(path=str(args.source_run.resolve()),
            sha256=hashlib.sha256(run_bytes).hexdigest()),
        source_run_snapshot=ref(out/'source-run-snapshot.json'),
        checkpoint_metadata_observed=dict(path=str(args.checkpoint_metadata.resolve()),
            sha256=hashlib.sha256(meta_bytes).hexdigest()),
        checkpoint_metadata_snapshot=ref(out/'checkpoint-metadata-snapshot.json'),
        checkpoint=ref(checkpoint),checkpoint_ordinal=metadata['checkpoint_ordinal'],
        source_role='genuine_unaccepted_before-full-J_complete_nodal_snapshot',
        original_parameter_J_branch=branch,analytic_column_is_independent_diagnostic=not branch['live_V5_delta_install_called'],
        source_is_accepted_original=False,nodes=len(x),evaluated_nodes=len(t),
        selected_actual_node_indices=indices.tolist(),state_components=obj.n,modes=M,angular=obj.nt,
        original_core_settings=record['core_settings'],original_profile=record['physical_profile'],
        original_gauge_q=record['gauge_q'],original_warp_reference=record['warp_reference'],
        original_gates=record['gates'],physical_delta=float(obj.cfg['delta']+p[0]),
        original_centered_delta_vs_analytic=difference(analytical,original_dp[:,0,:]),
        finite_differences=comparisons,unchanged_component_checks=invariants,
        complete_selected_columns=ref(out/'selected-complete-columns.npz'),
        fourier_assembly_cache=table_stats,core_evaluate_memo=memo_stats,V5_adapter=adapter_stats,
        source_hashes={str(path.resolve()):sha(path) for path in
            (Path(__file__),HERE/'material_delta_column.py',SCRIPTS/'resume_m3/portable_prefix_continue.py',
             Path(option(record,'--core-module')),
             memo_path,adapter_path)},
        elapsed_seconds=time.monotonic()-started,
        maximum_rss_KiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
        current_live_source_or_equations_changed=False,large_collocation_J_assembled=False,
        BVP_or_native_solve_invoked=False,interval_derivative_certificate=False,
        nonlinear_convergence_proved=False)
    (out/'comparison.json').write_text(json.dumps(report,indent=2,allow_nan=False)+'\n')
    print(json.dumps(dict(status=report['status'],report=ref(out/'comparison.json'),
        elapsed_seconds=report['elapsed_seconds'],maximum_rss_KiB=report['maximum_rss_KiB'],
        unchanged_component_checks=invariants)),flush=True)


if __name__ == '__main__':
    main()
