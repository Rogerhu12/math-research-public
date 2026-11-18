#!/usr/bin/env python3
"""Bind the generic frozen kernel to actual n3/M8 coefficients and root traces.

The double run must reproduce every original V8 root operand/judgment and all
18 outputs of each of the three actual over-gate stages. The following LD
samples use the unchanged generic kernel and its full 18 by 16 implicit flow
Jacobian. They are arithmetic samples, not a whole-tail acceptance or an
independent MP verification of this dimension's variational derivative.
"""
import argparse
import ctypes as C
import gzip
import hashlib
import importlib.util
import json
import math
from pathlib import Path
import sys
import time
import traceback


def ref(path):
    p=Path(path).resolve()
    return dict(path=str(p),sha256=hashlib.sha256(p.read_bytes()).hexdigest())


def load(path):
    p=Path(path)
    return json.loads(gzip.decompress(p.read_bytes()) if p.suffix=='.gz' else p.read_bytes())


def check(item):
    if ref(item['path'])!=item:raise ValueError('Bound source/input changed: '+item['path'])


def module(path,name,expected):
    if ref(path)['sha256']!=expected:raise ValueError('Frozen helper source differs')
    spec=importlib.util.spec_from_file_location(name,path)
    m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
    return m


def save(path,value,compressed=False):
    b=(json.dumps(value,ensure_ascii=False,allow_nan=False,indent=None if compressed else 2)+'\n').encode()
    with Path(path).open('xb') as f:f.write(gzip.compress(b,mtime=0) if compressed else b)
    return ref(path)


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--capsule-summary',type=Path,required=True)
    p.add_argument('--build',type=Path,required=True)
    p.add_argument('--out-dir',type=Path,required=True)
    p.add_argument('--node',default='node')
    a=p.parse_args();out=a.out_dir.resolve();out.mkdir(exist_ok=False)
    scripts=Path(__file__).resolve().parents[2]
    old=scripts/'resume_n4_tail'
    helper_path=old/'native_extended/probe_native_frozen_flow.py'
    scalar_path=old/'probe_frozen_stage_multiprecision.py'
    bridge=old/'frozen_stage_arithmetic_bridge.mjs'
    helper=module(helper_path,'m3_native_abi_helpers','42893f210b6d31c59abd04cdfec415a2408a543f726f87d808fc99cf8fad45db')
    base=module(scalar_path,'m3_original_v8_callbacks','a4e5297beb66c218b0b716ff27992830f2d5db6a56655ffab76c9a9b7a4af819')
    if ref(bridge)['sha256']!='ca62c285779a8f1c60749bf208009f47ca887c3316015206fb1e68a1a3fe6205':raise ValueError('Original V8 arithmetic bridge changed')
    cs=load(a.capsule_summary)
    for file,digest in cs['source_sha256'].items():check(dict(path=file,sha256=digest))
    for name in ('input','complete_rows','coefficients','reference'):check(cs[name])
    capsule,reference=load(cs['coefficients']['path']),load(cs['reference']['path'])
    if (capsule['modes'],capsule['spacing'],capsule['quadrature'],capsule['independent_quadrature_nodes'])!=(8,3,128,128):
        raise ValueError('This independent baseline is only n3/M8/N128')
    if [f['stage'] for f in capsule['fixtures']]!=[86,87,88] or cs['trace_arithmetic_restored_exactly'] is not True:
        raise ValueError('Original complete named row/source scope changed')
    build=load(a.build)
    if not build['success'] or build['files']['production_cpp']['sha256']!='e5a7d3b0a1021aae54fabcd3c5baae0558cab4246b4a10cfdeb31b6d275a8ddf':
        raise ValueError('The unchanged production kernel build is required')
    for item in [build['files']['production_cpp'],build['files']['header'],build['library'],build['batch_executable']]:check(item)
    context=dict(scope=__doc__,source=ref(__file__),command=[sys.executable,*sys.argv],
        capsule_summary=ref(a.capsule_summary),coefficients=cs['coefficients'],reference=cs['reference'],
        build=ref(a.build),native_library=build['library'],native_executable=build['batch_executable'],
        generic_CPP=build['files']['production_cpp'],header=build['files']['header'],
        ABI_helper=ref(helper_path),original_V8_helper=ref(scalar_path),original_V8_bridge=ref(bridge),
        original_input=cs['input'],original_complete_rows=cs['complete_rows'],
        production_changed=False,DN_or_prefix_solve_invoked=False)
    library=C.CDLL(build['library']['path'])
    library.vf_runtime_info.argtypes=[C.c_char_p,C.c_size_t];library.vf_runtime_info.restype=C.c_int
    buf=C.create_string_buffer(4096)
    if library.vf_runtime_info(buf,len(buf)):raise ValueError('Runtime identity query failed')
    runtime=json.loads(buf.value)
    for key,kind in (('config_size',helper.Config),('step_size',helper.Step),('stage_size',helper.Stage),('callbacks_size',helper.Callbacks),('diagnostics_size',helper.Diagnostics)):
        if runtime[key]!=C.sizeof(kind):raise ValueError('C ABI layout mismatch: '+key)
    if runtime['long_double_significand_bits']!=64 or not runtime['round_to_nearest']:raise ValueError('Unsupported native precision/rounding')
    context['runtime']=runtime
    library.vf_run_stage.argtypes=[C.POINTER(helper.Config),C.POINTER(helper.Stage),C.c_int,C.c_int,C.POINTER(helper.Callbacks),
        helper.DoublePointer,helper.DoublePointer,C.POINTER(C.c_ubyte),C.POINTER(C.c_ubyte),C.POINTER(helper.Diagnostics),C.c_char_p,C.c_size_t]
    library.vf_run_stage.restype=C.c_int
    M=capsule['modes'];K=2*M;size=K+2;scalars=[];raw=[];began=time.monotonic();event_count=0
    arithmetic=base.V8Float(bridge,a.node)
    try:
        for fixture,expected in zip(capsule['fixtures'],reference['rows'],strict=True):
            if fixture['stage']!=expected['stage']:raise ValueError('Original stage order changed')
            events=[];callback_errors=[]
            def trans(n,D,u,need_jac,sd,bm,user):
                try:
                    sqrtD,bmn=arithmetic.root_transcendentals([dict(D=D[i],u=u[i]) for i in range(n)],bool(need_jac))
                    for i,v in enumerate(sqrtD):sd[i]=v
                    if need_jac:
                        for i,v in enumerate(bmn):bm[i]=v
                    return 0
                except Exception:callback_errors.append(traceback.format_exc());return 1
            def sqrt(value,result,user):
                try:result[0]=arithmetic.sqrt(value);return 0
                except Exception:callback_errors.append(traceback.format_exc());return 1
            def trace(code,ints,ni,values,nv,scalar_mode,message,user):
                try:
                    if scalar_mode!=0:raise ValueError('Double baseline emitted another scalar type')
                    integers=[ints[i] for i in range(ni)]
                    data=C.string_at(values,nv*8);text=message.decode() if message else None
                    events.append(helper.decode_event(code,integers,helper.decoded_values(data,0),text,M));return 0
                except Exception:callback_errors.append(traceback.format_exc());return 1
            callback_objects=(helper.DoubleTrans(trans),helper.DoubleSqrt(sqrt),helper.Trace(trace))
            callbacks=helper.Callbacks(*callback_objects,None)
            config,stage,keepers=helper.abi_inputs(capsule,fixture)
            state=(C.c_double*size)();encoded=(C.c_ubyte*(size*8))();diag=helper.Diagnostics();error=C.create_string_buffer(4096)
            status=library.vf_run_stage(C.byref(config),C.byref(stage),0,0,C.byref(callbacks),state,None,encoded,None,C.byref(diag),error,len(error))
            actual=list(state);equal=helper.packed(actual)==helper.packed(expected['state'])
            mismatch=helper.first_trace_difference(events,expected['events'],base.numeric_identity)
            if status or callback_errors or not equal or mismatch is not None:
                fail=save(out/'failure.json.gz',dict(**context,stage=fixture['stage'],status=status,error=error.value.decode(),
                    callback_errors=callback_errors,state=actual,events=events,all_output_equal=equal,first_trace_difference=mismatch),True)
                raise RuntimeError('Independent m3 native baseline failed: '+fail['path'])
            event_count+=len(events)
            item=dict(stage=fixture['stage'],all_18_outputs_bitwise_equal=True,all_original_root_events_bitwise_equal=True,
                      verified_events=len(events),state_sha256=helper.fhash(actual),root_calls=diag.root_calls)
            scalars.append(item);raw.append(dict(stage=fixture['stage'],double_state=actual,double_events=events))
            print(json.dumps(dict(event='m3_native_double_baseline_complete',**item)),flush=True)
    finally:arithmetic.close()
    baseline=save(out/'double-baseline.json',dict(**context,named_results=scalars,verified_output_count=len(scalars)*size,
        verified_event_count=event_count,all_named_output_and_root_events_bitwise_equal=True,seconds=time.monotonic()-began))
    # The following distinct arithmetic samples are computed only after the
    # actual n3/M8 baseline above. No n4 fixture result substitutes for it.
    for index,fixture in enumerate(capsule['fixtures']):
        config,stage,keepers=helper.abi_inputs(capsule,fixture)
        callbacks=helper.Callbacks(helper.DoubleTrans(),helper.DoubleSqrt(),helper.Trace(),None)
        state=(C.c_double*size)();tangent=(C.c_double*(size*K))()
        encoded=(C.c_ubyte*(size*10))();encoded_jac=(C.c_ubyte*(size*K*10))()
        diag=helper.Diagnostics();error=C.create_string_buffer(4096)
        status=library.vf_run_stage(C.byref(config),C.byref(stage),1,1,C.byref(callbacks),state,tangent,encoded,encoded_jac,C.byref(diag),error,len(error))
        if status or not all(math.isfinite(v) for v in list(state)+list(tangent)):
            fail=save(out/'LD-failure.json',dict(**context,stage=fixture['stage'],status=status,error=error.value.decode()))
            raise RuntimeError('Independent m3 LD sample failed: '+fail['path'])
        actual=list(state);physical=[v if j<M else v/fixture['portRatio'] for j,v in enumerate(actual[:K])]
        residual=[v-fixture['targetNode40'][j] for j,v in enumerate(physical)]
        scaled=[abs(v)/fixture['normalizationScale'] for v in residual]
        raw[index].update(LD_state=actual,LD_tangent=list(tangent),native80_state=bytes(encoded).hex(),native80_tangent=bytes(encoded_jac).hex(),physical_residual=residual)
        scalars[index].update(LD_state_sha256=helper.fhash(actual),LD_tangent_sha256=helper.fhash(list(tangent)),
            LD_Jacobian_entries=size*K,LD_fixed_state_row_norm=max(scaled),LD_peak_component=max(range(K),key=lambda j:scaled[j]),
            LD_root_calls=diag.root_calls,LD_root_updates=diag.root_updates,LD_root_fallbacks=diag.root_fallbacks,
            LD_minA=diag.minA,LD_minD=diag.minD,LD_maximum_root_relative_residual=diag.max_root_relative_residual,
            independent_MP_variational_check=False)
        print(json.dumps(dict(event='m3_native_LD_sample_complete',**scalars[index])),flush=True)
    raw_ref=save(out/'raw.json.gz',dict(**context,rows=raw),True)
    result=dict(**context,double_baseline=baseline,named_results=scalars,raw=raw_ref,
        verified_output_count=len(scalars)*size,verified_event_count=event_count,
        all_named_output_and_root_events_bitwise_equal=True,seconds=time.monotonic()-began,
        complete_original_norm_evaluated=False,whole_tail_accepted=False,
        scope_limit='Three actual stages only. Scalar/root arithmetic port identity and generic implicit Jacobian evaluation do not prove whole-tail convergence, the stopping-algorithm derivative, or a continuous ODE bound.')
    print(json.dumps(dict(event='m3_native_baseline_terminal',summary=save(out/'summary.json',result))),flush=True)


if __name__=='__main__':main()
