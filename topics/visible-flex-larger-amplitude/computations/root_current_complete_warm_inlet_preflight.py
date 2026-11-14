#!/usr/bin/env python3
"""Evaluate the original inlet of one genuinely constructed current-M32 warm.

Author: geometry_audit (GPT-6 Astra Pro; AI-assisted), 2026-11-13.
This intercepts the unchanged original explicit no-worker warm inspection
after the actual full parameter/state warm has been constructed. It evaluates
the original initial(p), retaining all32 modes and the corrected provider.
No geometry field, RMS/Jacobian, tail worker or new BVP is run. The report's
domain flag covers only this original construction and inlet projection.
"""
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[key]='1'
import argparse
from fractions import Fraction as F
import gzip
import hashlib
import json
from pathlib import Path
import sys
import numpy as np

HERE=Path(__file__).resolve().parent
PINS={
    'root_actual_geometry_field_anchor.py':'da6726c130503113a9483da2365cea70e59f22f26e09eb19b08ba57632229a77',
    'strong_frontload_anchor_loader_adapter.py':'aa32079179e20a95493cd911185ea69e7df2b4d5b150a713597e9d2f9fd73c86',
    'strong_monotone_initial_speed_anchor.py':'583af82cdd6bb672325844587d8aac67e47365ccb5152ac2eae543837adc0ffc',
    'root_geometry_anchor_current_interfaces.py':'8da06d8c7909b55e56bef75e92dceec8e1dd3226b208a80896fa2ce7aaaa0b48',
}


def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def read(path):
    path=Path(path);data=path.read_bytes()
    return json.loads(gzip.decompress(data) if path.suffix=='.gz' else data)
def rat(value):value=F(value);return dict(numerator=str(value.numerator),denominator=str(value.denominator))


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--plan',type=Path,required=True)
    p.add_argument('--candidate',required=True)
    p.add_argument('--out-prefix',type=Path,required=True)
    a=p.parse_args()
    for name,want in PINS.items():
        if sha(HERE/name)!=want:raise ValueError('A frozen current inlet input adapter changed')
    plan=read(a.plan)
    if (Path.cwd()!=Path(plan['cwd']) or plan['modes']!=32 or
            not plan.get('current_anchor_complete_geometry_interface')):
        raise ValueError('Require an actual current M32 anchor plan in its original cwd')
    for path,want in plan['source_and_input_sha256'].items():
        if sha(path)!=want:raise ValueError('A real current source or input changed: '+path)
    rows=[r for r in plan['candidates'] if r['name']==a.candidate]
    if len(rows)!=1 or a.candidate not in ('baseline','combined'):
        raise ValueError('Select the unique original baseline or explicitly combined current candidate')
    row=rows[0]
    original=row['command'][row['command'].index('--')+1:]
    if original[1]!=str(HERE/'root_actual_geometry_field_anchor.py'):
        raise ValueError('The original current corrected-provider geometry entry changed')
    command=original[2:]
    for flag in ('--geometry-grid','--geometry-array','--resident-rss-guard-mib','--mean-angular','--geometry-batch'):
        if command.count(flag)!=1:raise ValueError('The complete original geometry command changed')
        index=command.index(flag);del command[index:index+2]
    if list(a.out_prefix.parent.glob(a.out_prefix.name+'*')):
        raise FileExistsError('Use a fresh preflight prefix, separate from the planned geometry')
    a.out_prefix.parent.mkdir(parents=True,exist_ok=True)
    out=Path(str(a.out_prefix)+'-report.json')
    command[command.index('--out-prefix')+1]=str(a.out_prefix)
    command[command.index('--inspect-warm-output')+1]=str(out)
    reference_path=Path(command[command.index('--actual-reference')+1])
    reference=read(reference_path)
    if not reference['solver_success'] or reference['audit_pending'] or reference['core']['frequencies']!=list(range(2,65,2)):
        raise ValueError('The real current accepted full32 core is required')
    if '--response-data' in command:
        from root_geometry_anchor_current_interfaces import require_response
        response_path=Path(command[command.index('--response-data')+1]);require_response(read(response_path))
    elif a.candidate!='baseline':
        raise ValueError('A genuine combined current warm requires the completed current response')
    from strong_frontload_anchor_loader_adapter import build
    namespace,anchor_provenance=build('geometry',__file__)
    entry,patched,preparation=namespace['prepare_entry']()
    import strong_actual_warm_screen as warm
    prior_inspection=warm.inspect_warm;prior_argv=sys.argv
    captured={}
    def inspect_inlet(obj,x,y,parameters,baseline_H,**unused):
        obj.select(parameters)
        initial=obj.initial(parameters)
        core=np.asarray(obj.actual_coefficients(parameters),dtype=np.float64)
        if core.shape!=(32,) or not np.isfinite(core).all() or not np.isfinite(initial).all():
            raise ValueError('The actual complete warm inlet is not finite')
        metrics=dict(obj._inlet_metrics)
        if not all(key in metrics and np.isfinite(metrics[key]) for key in ('position','first','second','metric_l1')):
            raise ValueError('The original inlet diagnostics changed schema')
        H=np.asarray(obj.tail_height(y[:,-1]),dtype=np.float64)
        if H.shape!=(32,) or not np.isfinite(H).all():raise ValueError('The complete genuine warm H is missing')
        frequencies=2*np.arange(1,33)
        tails={str(k):rat(sum(((int(m)**2-1)*abs(F.from_float(float(c))) for c,m in zip(core,frequencies) if m>=k),F(0))) for k in (16,24,32,40,48)}
        same=core.tobytes()==np.asarray(reference['core']['coefficients'],dtype=np.float64).tobytes()
        regression={key:abs(metrics[key]-reference['summary']['inlet'][key]) for key in ('position','first','second','metric_l1')} if same else None
        if regression is not None and max(regression.values())>3e-12:
            raise ValueError('The actual unchanged full-core inlet did not reproduce its saved original values')
        captured.update(scope=__doc__,schema='genuinely-constructed-current-full32-warm-inlet-v1',
            finite_domain_passed=True,finite_domain_scope='Original current warm construction and initial(p) projection only; full geometry is not evaluated.',
            actual_full_core=core.tolist(),actual_parameter_count=len(parameters),actual_parameters=np.asarray(parameters).tolist(),
            original_inlet_metrics=metrics,complete_core_weighted_tails_exact_binary=tails,
            exact_binary_complete_axis_gap=rat(2*sum((F.from_float(float(v)) for v in core[::2]),F(0))),
            genuine_warm_H=H.tolist(),warm_H_bitwise_equal_to_baseline=(H.tobytes()==np.asarray(baseline_H,dtype=np.float64).tobytes()),
            complete_H_change_max=float(np.max(abs(H-np.asarray(baseline_H)))),
            same_complete_core_as_actual_accepted_reference=same,same_core_original_inlet_regression=regression,
            original_initial_state_size=int(initial.size),new_geometry_field_or_full_collocation=False,
            physical_metric_is_only_projected_inlet_here=True,nonlinear_solution=False,true_new_H_tail_evaluated=False)
        return captured
    warm.inspect_warm=inspect_inlet
    sys.argv=[str(Path(__file__).resolve()),*command]
    try:patched()
    finally:warm.inspect_warm=prior_inspection;sys.argv=prior_argv
    if not captured or not out.exists():raise RuntimeError('The genuine original warm constructor did not reach the inlet inspection')
    result=read(out)
    if not result['finished'] or not result['finite_domain_passed'] or result['worker_start_attempts']!=0:
        raise ValueError('The original explicit no-worker warm inspection did not complete')
    if np.asarray(result['actual_core']).tobytes()!=np.asarray(captured['actual_full_core']).tobytes():
        raise ValueError('The recorded outer warm and actual constructed core differ')
    result['current_inlet_preflight_adapter']=dict(source_sha256=sha(__file__),original_pins=PINS,
        plan=str(a.plan),plan_sha256=sha(a.plan),candidate=a.candidate,
        exact_original_geometry_command=original,executed_actual_constructor_arguments=command,
        only_geometry_flags_removed=True,original_target_and_all_neutral_steps_unchanged=True,
        actual_input_preparation=preparation,anchor_provider_provenance=anchor_provenance,
        original_initial_formula_unchanged=True,original_full_warm_constructor_unchanged=True,
        no_geometry_RMS_Jacobian_Node_or_new_solution=True)
    tmp=out.with_name(out.name+'.inlet-provenance.tmp')
    tmp.write_text(json.dumps(result,indent=2)+'\n');tmp.replace(out)
    print(json.dumps(dict(event='actual_current_complete_inlet_preflight_finished',out=str(out),sha256=sha(out),
        inlet=result['original_inlet_metrics'],same_core_regression=result['same_core_original_inlet_regression'])),flush=True)


if __name__=='__main__':main()
