#!/usr/bin/env python3
"""Finish saved actual M28 through original RMS/BC and bounded postprocessing.

No Newton solve or Node worker is permitted. A separately completed full
audited tail packet must match the entire exact H. The original pending/accepted
raw fields are identical. Actual physical C2 interpolation, complete mean and
the unchanged audit run with smaller independent radial batches. No angle,
point, mode, equation, tolerance, mean or acceptance gate is removed.
"""
from __future__ import annotations
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'):
    os.environ[key]='1'
for key in tuple(os.environ):
    if key in ('GH_TOKEN','GITHUB_TOKEN','GITHUB_PAT') or key.startswith('GIT_CONFIG_'):
        os.environ.pop(key,None)
import argparse
import gc
import gzip
import hashlib
import inspect
import json
from pathlib import Path
import subprocess
import sys
import textwrap
import time
import types
from types import SimpleNamespace
import numpy as np
import scipy.integrate as integrate
import root_actual_pending_recovery as recovery
import root_raw_collocation as raw
import root_radial_batching as radial
import strong_sameg_spectral_refinement as spectral
from strong_actual_recorded_tail_port import verified_packet
from root_actual_staged_tail import raw_arrays,read_json,sha

HERE=Path(__file__).resolve().parent
SELF_SHA=sha(__file__)

def main():
    parser=argparse.ArgumentParser(add_help=False)
    parser.add_argument('--accepted-raw',type=Path,required=True)
    parser.add_argument('--original-spectral-plan',type=Path,required=True)
    parser.add_argument('--physical-batch-size',type=int,choices=(4,8,12),default=8)
    own,remaining=parser.parse_known_args()
    def arg(name):
        if remaining.count(name)!=1:raise ValueError('Exactly one '+name+' is required')
        return Path(remaining[remaining.index(name)+1])
    for forbidden in ('--postprocess-only','--check-only','--validate-acceptance-only',
                      '--allow-converged-design-reference','--extra-physical-mesh'):
        if forbidden in remaining:
            raise ValueError('Original staged acceptance and complete postprocessing required')
    pending_file=arg('--raw-collocation-restart');config=arg('--tail-config')
    fixed_reference=arg('--fixed-reference');source_topic=arg('--source-topic')
    packet_file=arg('--tail-packet');ready_file=arg('--tail-ready');out=arg('--out-prefix')
    plan=read_json(own.original_spectral_plan)
    for name,expected in plan['source_sha256'].items():
        if not (HERE/name).is_file() or sha(HERE/name)!=expected:
            raise ValueError('Original spectral mathematical source differs: '+name)
    if {p.name:sha(p) for p in sorted(HERE.glob('*.mjs'))}!=plan['MJS_source_sha256']:
        raise ValueError('Original MJS source bytes changed')
    accepted,A=raw_arrays(own.accepted_raw);pending,B=raw_arrays(pending_file)
    ident=accepted['identity'];reference=read_json(fixed_reference)
    if (not accepted['solver_success'] or accepted['status']!=0 or
            accepted['physical_surface'] is not False or not ident['fixed'] or
            ident['modes']!=28 or ident['angular']!=1024 or ident['tol']!=1e-7 or
            int(str(arg('--modes')))!=28 or int(str(arg('--angular')))!=1024 or
            float(str(arg('--tol')))!=1e-7):
        raise ValueError('Original accepted M28/N1024/tol7 raw and same CLI required')
    if spectral.canonical(ident)!=spectral.canonical(pending['identity']):
        raise ValueError('Accepted and pending full physical/chart identities differ')
    for name in ('x','y','p','cubic','rms'):
        if A[name].shape!=B[name].shape or A[name].tobytes()!=B[name].tobytes():
            raise ValueError('Accepted/pending complete arrays differ: '+name)
    if (pending['solver_success'] or not pending['provenance'].get('affine_inner_success') or
            not pending['provenance'].get('actual_nonlinear_coupling_pending') or
            sha(config)!=ident['coupling_context']['tail_config_sha256']):
        raise ValueError('Original pending checkpoint/configuration required')
    stored,ready,cfg,H,packet_provenance=verified_packet(packet_file,ready_file,config,source_topic)
    expected_H=-float(ident['gauge'])*A['y'][2*ident['modes']+1:,-1]
    if H.tobytes()!=expected_H.tobytes():
        raise ValueError('Saved audited packet is not the exact complete raw H')
    for key,left,right in (
        ('profile',ident['profile'],reference['frozen_profile']),
        ('physical_tail_parameters',ident['physical_tail_parameters'],reference['physical_tail_parameters']),
        ('physical_tail_cut',ident['physical_tail_cut'],reference['physical_tail_cut']),
        ('reference_coefficients',ident['reference_coefficients'],reference['chart_reference_coefficients']),
        ('reference_frequencies',ident['reference_frequencies'],reference['chart_reference_frequencies']),
        ('numerical_reference_knots',ident['numerical_reference_knots'],reference['numerical_meridian_chart']['reference_t'])):
        if spectral.canonical(left)!=spectral.canonical(right):
            raise ValueError('Original fixed metric/reference differs: '+key)
    source_input_keys={str(p):sha(p) for p in (own.accepted_raw,pending_file,config,
        fixed_reference,packet_file,ready_file,own.original_spectral_plan)}
    provenance=dict(scope=__doc__,entry_sha256=SELF_SHA,
        source_input_sha256=source_input_keys,physical_batch_size=own.physical_batch_size,
        complete_H_bitwise_equal=True,all_five_accepted_pending_raw_arrays_bitwise_equal=True,
        original_reference_t_requested=True,physical_metric_changes=0,Newton_calls=0,Node_workers=0,
        true_audited_response_reused=True,reused_already_audited_packet=True,
        source_packet_sha=sha(packet_file),audit_recomputed_in_this_postprocess=False,
        complete_packet_ready_binding=packet_provenance,
        transforms=[],live_raw_restores=0,small_actual_C2_comparison=None,small_complete_mean_comparison=None,
        physical_data_guard=None,original_acceptance_and_full_physical_audit_preserved=True,
        MJS_sources_unchanged=True)
    del A,B,pending,stored,ready,cfg,H
    gc.collect()
    out.parent.mkdir(parents=True,exist_ok=True)
    report=out.with_name(out.name+'-bounded-postprocess.json')
    if report.exists() or out.with_suffix('.json.gz').exists():
        raise FileExistsError('Fresh postprocessing prefix required')
    original_read=raw.read;old_radial=(radial.value.__defaults__,radial.state_jacobian.__defaults__)
    if old_radial!=((48,),(48,)):
        raise ValueError('Original independent radial defaults changed')
    radial.value.__defaults__=(own.physical_batch_size,)
    radial.state_jacobian.__defaults__=(own.physical_batch_size,)
    def save():
        data=(json.dumps(provenance,indent=2,allow_nan=False)+'\n').encode()
        tmp=report.with_name(report.name+'.tmp')
        tmp.write_bytes(data);tmp.replace(report)
    def compile_variant(fn,replacements):
        original=textwrap.dedent(inspect.getsource(fn))
        transformed=original
        for before,after,count in replacements:
            if transformed.count(before)!=count:
                raise ValueError('Independent batching source anchor changed: '+fn.__qualname__+' '+repr(before))
            transformed=transformed.replace(before,after)
        namespace=dict(fn.__globals__)
        exec(compile(transformed,fn.__code__.co_filename+'::strong-independent-batch', 'exec'),namespace)
        result=namespace[fn.__name__]
        provenance['transforms'].append(dict(function=fn.__qualname__,
            source_file=fn.__code__.co_filename,
            complete_source_file_sha256=sha(fn.__code__.co_filename),
            original_function_sha256=hashlib.sha256(original.encode()).hexdigest(),
            compiled_function_sha256=hashlib.sha256(transformed.encode()).hexdigest(),
            replacements=[dict(old=a,new=b,count=c) for a,b,c in replacements],
            radial_arithmetic_order_inside_each_point_unchanged=True))
        return result
    def install_streamed_fields(obj,solution):
        if getattr(obj,'_strong_sameg_postprocessing_installed',False):return
        obj.initial(solution.p);flow=obj.flow(solution.p[0]);b=own.physical_batch_size
        original_fun=flow.adapt_fun;original_c2=flow.c2_interpolant
        fun_fn=original_fun.__func__;c2_fn=original_c2.__func__
        new_fun=compile_variant(fun_fn,[
            ('range(0,len(s),64)',f'range(0,len(s),{b})',1),
            ('slice(first,first+64)',f'slice(first,first+{b})',1)])
        new_c2=compile_variant(c2_fn,[
            ('range(0,len(s),64)',f'range(0,len(s),{b})',1),
            ('slice(first,first+64)',f'slice(first,first+{b})',1)])
        new_height=compile_variant(flow.height_integral.__func__,[
            ('range(0,len(flat),128)',f'range(0,len(flat),{b})',1),
            ('first:first+128',f'first:first+{b}',2)])
        adaptive=sys.modules.get('numerical_mode2_adaptive')
        if adaptive is None:raise ValueError('Actual pinned adaptive module was not loaded')
        original_audit=adaptive.audit
        new_audit=compile_variant(original_audit,[
            ('range(0,len(ss),32)',f'range(0,len(ss),{b})',1),
            ('ss[first:first+32]',f'ss[first:first+{b}]',1)])
        indices=np.unique(np.linspace(0,len(solution.x)-1,13,dtype=int))
        s,_=obj.chart(solution.x[indices],solution.p[0])
        small=SimpleNamespace(x=s,y=solution.y[:,indices],p=solution.p)
        baseline=original_c2(small)
        flow.adapt_fun=types.MethodType(new_fun,flow)
        try:
            changed=types.MethodType(new_c2,flow)(small)
        except BaseException:
            flow.adapt_fun=original_fun
            raise
        same=(np.isfinite(baseline.c).all() and np.isfinite(changed.c).all() and
              baseline.x.tobytes()==changed.x.tobytes() and
              baseline.c.tobytes()==changed.c.tobytes())
        check=dict(actual_saved_node_indices=indices.tolist(),points=len(indices),
            modes=obj.M,angular=obj.nt,complete_physical_quintic_coefficients_bitwise_equal=same,
            max_coefficient_absolute_difference=float(np.max(abs(baseline.c-changed.c))),
            original_C2_batch=64,new_C2_batch=b,
            original_mean_batch=128,new_mean_batch=b,
            original_audit_batch=32,new_audit_batch=b,
            angular_counts_and_all_mean_Gauss_nodes_unchanged=True)
        provenance['small_actual_C2_comparison']=check;save()
        if not same:
            flow.adapt_fun=original_fun
            raise ValueError('Actual original-vs-batched small C2 coefficients differ')
        flow.c2_interpolant=types.MethodType(new_c2,flow)
        i=min(int(np.argmax(solution.rms_residuals)),len(solution.x)-3)
        tiny_indices=np.arange(i,i+3,dtype=int)
        tiny_s,_=obj.chart(solution.x[tiny_indices],solution.p[0])
        tiny=SimpleNamespace(x=tiny_s,y=solution.y[:,tiny_indices],p=solution.p)
        tiny.sol=flow.c2_interpolant(tiny)
        sample_s=np.sort(np.r_[tiny_s,(tiny_s[:-1]+tiny_s[1:])/2])
        N=max(512,16*(obj.M*3+1))
        old_h=flow.height_integral(tiny,sample_s,N,6)
        new_h=types.MethodType(new_height,flow)(tiny,sample_s,N,6)
        mean_same=(np.isfinite(old_h).all() and np.isfinite(new_h).all() and old_h.tobytes()==new_h.tobytes())
        provenance['small_complete_mean_comparison']=dict(actual_saved_node_indices=tiny_indices.tolist(),
            angular=N,Gauss_order=6,all_positive_Gauss_nodes_unchanged=True,
            complete_mean_values_bitwise_equal=bool(mean_same),
            max_absolute_difference=float(np.max(abs(old_h-new_h))))
        save()
        if not mean_same:
            raise ValueError('Actual original-vs-batched complete mean values differ')
        flow.height_integral=types.MethodType(new_height,flow)
        adaptive.audit=new_audit
        obj._strong_sameg_postprocessing_installed=True
        del baseline,changed,small,tiny,old_h,new_h
        gc.collect()
        print(json.dumps(dict(event='actual_M28_bounded_C2_check_passed',**check)),flush=True)
    def same_chart_read(path,obj,args):
        if Path(path).resolve()!=pending_file.resolve():
            return original_read(path,obj,args)
        if obj.tail is not None and not getattr(obj,'_strong_sameg_postprocessing_installed',False):
            raise ValueError('A live client began before raw identity restoration')
        obj._neck_knots=np.asarray(ident['numerical_reference_knots'],dtype=float).copy()
        obj.chart_breaks=obj._neck_knots.copy()
        obj.select(np.asarray(accepted['parameter_state'],dtype=float))
        solution,record=original_read(path,obj,args)
        actual=raw.identity(obj,args)
        if spectral.canonical(actual)!=spectral.canonical(ident):
            raise ValueError('Original full raw identity changed after same-chart construction')
        flow=obj.flow(solution.p[0])
        if (flow.cfg!=reference['frozen_profile'] or flow.end!=reference['meridian_length'] or
                np.asarray(flow.breaks,dtype=np.float64).tobytes()!=np.asarray(reference['numerical_meridian_chart']['physical_s'],dtype=np.float64).tobytes()):
            raise ValueError('The actual fixed physical profile/length/breaks changed')
        current_H=obj.tail_height(solution.y[:,-1])
        if current_H.tobytes()!=expected_H.tobytes():
            raise ValueError('Actual fixed object changed the exact complete physical H')
        provenance['live_raw_restores']+=1
        provenance['physical_data_guard']=dict(full_identity_exact=True,
            reference_t_bitwise_equal=True,profile_length_and_breaks_exact=True,
            complete_28_H_bitwise_equal=True)
        install_streamed_fields(obj,solution)
        save()
        return solution,record
    raw.read=same_chart_read
    original_solve_bvp=recovery.bounded.blocks._bvp.solve_bvp
    original_public_solve_bvp=integrate.solve_bvp
    original_popen=subprocess.Popen
    def forbidden_newton(*args,**kwargs):
        raise RuntimeError('This saved-state postprocessing must not run a new BVP')
    # The staged adapter replaces Actual.solve_coupled with its real RMS/BC
    # acceptance function. This guard rejects any accidental SciPy BVP call.
    recovery.bounded.blocks._bvp.solve_bvp=forbidden_newton
    integrate.solve_bvp=forbidden_newton
    def forbid_Node(command,*args,**kwargs):
        if isinstance(command,(list,tuple)) and command and Path(str(command[0])).name=='node':
            raise RuntimeError('This postprocess must use the already audited exact-H packet; no Node worker is allowed')
        return original_popen(command,*args,**kwargs)
    subprocess.Popen=forbid_Node
    started=time.monotonic();error=None;oldargv=sys.argv
    save()
    try:
        sys.argv=[oldargv[0],*remaining]
        recovery.main()
    except BaseException as exc:
        error=repr(exc)
        raise
    finally:
        raw.read=original_read;sys.argv=oldargv
        radial.value.__defaults__,radial.state_jacobian.__defaults__=old_radial
        recovery.bounded.blocks._bvp.solve_bvp=original_solve_bvp
        integrate.solve_bvp=original_public_solve_bvp
        subprocess.Popen=original_popen
        provenance.update(seconds=time.monotonic()-started,entry_error=error,
            source_sha256_at_start=SELF_SHA)
        summary=out.with_name(out.name+'-summary.json')
        if summary.exists():
            end=read_json(summary)
            provenance['observed_output']=dict(solver_success=end.get('solver_success'),
                audit_pending=end.get('audit_pending'),
                max_rms_collocation_residual=end.get('max_rms_collocation_residual'),
                summary=end.get('summary'))
        save()
        for path in (out.with_suffix('.json.gz'),summary):
            if not path.exists():continue
            data=read_json(path);data['same_g_M28_bounded_postprocess']=provenance
            content=(json.dumps(data,indent=2)+'\n').encode()
            if path.suffix=='.gz':content=gzip.compress(content,mtime=0)
            if len(content)>=5_000_000:raise ValueError('Metadata file limit exceeded')
            temp=path.with_name(path.name+'.bounded.tmp');temp.write_bytes(content);temp.replace(path)
    final=read_json(out.with_name(out.name+'-summary.json'))
    if (not final.get('solver_success') or final.get('audit_pending',True) or
            provenance['small_actual_C2_comparison'] is None or
            provenance['live_raw_restores']<2):
        raise RuntimeError('Original complete staged acceptance/postprocess did not finish')
    print(json.dumps(dict(event='same_g_M28_postprocess_complete',
        solver_success=True,physical_audit_complete=True,Newton_calls=0,Node_workers=0,
        reused_already_audited_packet=True,source_packet_sha=sha(packet_file),
        summary=final.get('summary'))),flush=True)

if __name__=='__main__':main()
