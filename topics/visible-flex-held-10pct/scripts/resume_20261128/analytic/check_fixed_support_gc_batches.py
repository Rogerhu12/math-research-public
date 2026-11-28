#!/usr/bin/env python3
"""One real seven-node fixed-g RHS/full-Jacobian batching check, no global J."""
import os
for _name in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[_name]='1'
import argparse,gc,hashlib,importlib.util,json,resource,sys,time,weakref
from pathlib import Path
import numpy as np
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE))
import fixed_support_literal_model as literal


def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def module(name,path):
    spec=importlib.util.spec_from_file_location(name,path);value=importlib.util.module_from_spec(spec)
    sys.modules[name]=value;spec.loader.exec_module(value);return value

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--donor-run',type=Path,required=True);ap.add_argument('--outdir',type=Path,required=True)
    args=ap.parse_args();begin=time.monotonic();run_path=args.donor_run.resolve()
    run=json.loads(run_path.read_text());terminal=json.loads((run_path.parent/'actual-process-terminal.json').read_text())
    manifest=json.loads((run_path.parent/'last-nodal-jac-input.json').read_text())
    checkpoint=run_path.parent/manifest['file']
    if (terminal['run_sha256']!=sha(run_path) or terminal['observed_child_returncode']!=-9
            or terminal['latest_complete_nodal_checkpoint']['sha256']!=sha(checkpoint)
            or manifest['sha256']!=sha(checkpoint) or run.get('fixed_metric') is not True):
        raise ValueError('Require the actual latest interrupted fixed-g nodal source')
    with np.load(checkpoint,allow_pickle=False) as z:
        x,y,p,scale=(z[k].copy() for k in ('x','y','p','pscale'))
    idx=np.unique(np.rint(np.linspace(0,len(x)-1,7)).astype(int));t,yy=x[idx],y[:,idx]
    assert len(idx)==7
    args.outdir.mkdir(parents=True,exist_ok=False)
    obj=literal.load_model(dict(source_run=str(run_path)))
    if (not obj.fixed or obj.cfg!=run['frozen_profile'] or obj.M!=32 or obj.nt!=1024
            or not np.array_equal(obj.pscale,scale) or run['mean_nodes']!=1168):
        raise ValueError('The actual complete fixed-g model changed')
    cache_path=HERE.parent/'design/cached_fourier_tables.py'
    cache=module('_fixed_gc_check_fourier_cache',cache_path)
    tables=cache.install(sys.modules['_metric_fourier_jac'])
    obj.initial(p)
    memo_path=HERE.parent/'design/material_core_evaluate_cache.py'
    memo=module('_fixed_gc_check_core_memo',memo_path).install(type(obj._core))
    flow=obj.flow(p[0]);refs=[weakref.ref(o) for o in gc.get_objects() if isinstance(o,type(flow))]
    collected=gc.collect();retired=sum(r() is None for r in refs)
    self_cycles={name:getattr(getattr(flow,name,None),'__self__',None) is flow
                 for name in ('fun','fun_jac','c2_interpolant')}
    fixed_same=all(obj.flow(float(p[0])+d) is flow for d in (0.,1e-4,-1e-4))
    if not fixed_same:raise ValueError('This is not the declared shared fixed Flow')
    print(json.dumps(dict(stage='actual_fixed_model_and_seven_nodes_loaded',nodes=idx.tolist(),
        fixed_flow_shared=True,construction_collection=collected,retired_adaptive_flows=retired)),flush=True)
    rhs=obj.fun(t,yy,p);dy,dp=obj.fun_jac(t,yy,p)
    guarded_path=HERE.parent/'design/exception_safe_radial_batches.py'
    guarded=module('_fixed_gc_check_finally_batches',guarded_path)
    expected='2d2b413a46a23882341a4d5cac7ce2bc2c44c8444129d322d898288597c2c7a7'
    if sha(guarded_path)!=expected:raise ValueError('The reviewed finally batching source changed')
    stats=guarded.statistics()
    # Three real slices (3,3,1) also exercise the genuine final short batch;
    # no new field, artificial exception, or numerical parameter is supplied.
    rr=guarded.split_rhs(obj.fun,3,stats)(t,yy,p)
    jj,pp=guarded.split_jac(obj.fun_jac,3,stats)(t,yy,p)
    checks={name:dict(bitwise_equal=np.array_equal(old,new),maximum_difference=float(np.max(np.abs(old-new))))
            for name,old,new in [('rhs',rhs,rr),('all_dy',dy,jj),('all_dp_including_log_q',dp,pp)]}
    if not all(v['bitwise_equal'] for v in checks.values()):
        raise ArithmeticError('The actual full fixed-g seven-node outputs differ under guarded batching')
    assert obj.flow(p[0]) is flow and obj.cfg==run['frozen_profile']
    report=dict(status='actual_fixed_support_seven_node_complete_rhs_dy_dp_bitwise_equal_with_finally_batches',
        source_sha256=sha(__file__),donor_run=str(run_path),donor_run_sha256=sha(run_path),
        actual_terminal_sha256=sha(run_path.parent/'actual-process-terminal.json'),
        checkpoint=str(checkpoint),checkpoint_sha256=sha(checkpoint),nodes=idx.tolist(),
        modes=obj.M,angular=obj.nt,mean_nodes=1168,complete_states=obj.n,complete_parameters=obj.M,
        q_actual=float(obj.support_amplitude),physical_delta=obj.cfg['delta'],
        old_solver_rhs_block=64,old_solver_jac_batch=32,small_check_block=3,
        checks=checks,statistics=stats,flow_bound_method_self_cycles=self_cycles,
        same_fixed_flow_for_all_scalar_arguments=fixed_same,
        old_fixed_model_uses_design_delta_finite_differences=False,
        constructor_unreachable_objects_collected=collected,
        constructor_retired_adaptive_flows_observed_via_weakrefs=retired,
        current_live_adaptive_flow_count_after_collection=sum(1 for o in gc.get_objects() if isinstance(o,type(flow))),
        live_physical_Flow_or_cache_cleared=False,exceptional_fixed_g_call_tested=False,
        observed_signal9_cause_inferred=False,all_physical_parameters_and_gates_unchanged=True,
        full_J_assembled=False,nonlinear_solver_invoked=False,accepted_bvp=False,
        complete_surface=False,maximum_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
        elapsed_seconds=time.monotonic()-begin,
        dependencies={str(path):sha(path) for path in (HERE/'fixed_support_literal_model.py',cache_path,memo_path,guarded_path)})
    (args.outdir/'report.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps({k:report[k] for k in ('status','checks','statistics','maximum_rss_kib','elapsed_seconds')},indent=2),flush=True)

if __name__=='__main__':main()
