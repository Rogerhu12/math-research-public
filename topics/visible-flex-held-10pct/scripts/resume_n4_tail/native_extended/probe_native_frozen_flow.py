#!/usr/bin/env python3
"""Reviewed native probe harness; compilation alone does not execute this file.

float-baseline: original V8 scalar callbacks, exact126 outputs and116608 events.
longdouble: original formed-moment root/RK, native64-significand arithmetic,
           complete40-column literal implicit/flow Jacobian, gated by baseline.
export-batch: write the documented whole-evaluate binary payload only.
No command in this harness installs a production engine or invokes a DN solve.
"""
import argparse
import ctypes as C
import gzip
import hashlib
import importlib.util
import json
import math
from pathlib import Path
import struct
import sys
import time
import traceback
import mpmath as mp

BASE_SHA = 'a4e5297beb66c218b0b716ff27992830f2d5db6a56655ffab76c9a9b7a4af819'
BRIDGE_SHA = 'ca62c285779a8f1c60749bf208009f47ca887c3316015206fb1e68a1a3fe6205'
SCALARS = ('r3','r4','sqrt2','sqrt12','E','w2','pDenominator','targetFactor',
           'sigma','fluxPrefactor','qLNumerator','meanFactor')
mp.mp.dps = 140


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def ident(path):
    return dict(path=str(Path(path).resolve()), sha256=sha(path))


def load(path):
    path = Path(path)
    return json.loads(gzip.decompress(path.read_bytes()) if path.suffix == '.gz' else path.read_text())


def checked(ref):
    if sha(ref['path']) != ref['sha256']:
        raise ValueError('A frozen input/source changed: '+ref['path'])
    return load(ref['path'])


def packed(values):
    return struct.pack('<'+'d'*len(values), *values)


def fhash(values):
    return hashlib.sha256(packed(values)).hexdigest()


def save_gz(path, value):
    path.write_bytes(gzip.compress((json.dumps(value, ensure_ascii=False)+'\n').encode(), mtime=0))
    return ident(path)


def native80_value(data):
    if len(data) != 10:
        raise ValueError('Expected canonical10-byte x87 value')
    significand, se = struct.unpack('<QH', data)
    exponent = se & 0x7fff
    if exponent == 0x7fff:
        raise ValueError('Nonfinite native extended output')
    value = mp.ldexp(mp.mpf(significand), (exponent if exponent else 1)-16383-63)
    return -value if se & 0x8000 else value


def decoded_values(data, mode):
    if mode == 0:
        return list(struct.unpack('<'+'d'*(len(data)//8), data))
    return [mp.nstr(native80_value(data[i:i+10]), 40) for i in range(0,len(data),10)]


def decode_event(code, integer, value, message, M):
    J, size = M+1, 2*M+2
    if code == 1:
        return dict(event='rk_field',profile=integer[0],step=integer[1],label='abcd'[integer[2]],x=value[0])
    if code == 2:
        return dict(event='root_start',state=value[:size],x=value[size],
                    target=value[size+1:size+1+J],L=value[size+1+J:])
    if code == 3:
        return dict(event='evaluate_start',L=value[:J],Q=value[J:],needJac=bool(integer[0]))
    if code == 4:
        return dict(event='domain',n=integer[0],D=value[0],S=value[1],A=value[2],floor=value[3],
            D_pass=bool(integer[1]),S_compared=bool(integer[2]),
            S_pass=None if integer[3]<0 else bool(integer[3]),A_compared=bool(integer[4]),
            A_pass=None if integer[5]<0 else bool(integer[5]))
    if code == 5:
        return dict(event='evaluate_end',moments=value[:J],minD=value[J],minS=value[J+1],
                    minA=value[J+2],maxQuad=value[J+3])
    if code == 6:
        return dict(event='spd_positive',i=integer[0],value=value[0],positive=bool(integer[1]))
    if code == 7:
        return dict(event='root_stop',iteration=integer[0],err=value[0],scale=value[1],
                    tolerance=value[2],threshold=value[3],accepted=bool(integer[1]))
    if code == 8:
        return dict(event='root_return',iteration=integer[0],err=value[0],scale=value[1],roundoffFallback=bool(integer[1]))
    if code == 9:
        return dict(event='trial_start',k=integer[0],fac=value[0],trial=value[1:])
    if code == 10:
        return dict(event='trial_judgment',k=integer[0],er=value[0],err=value[1],scale=value[2],threshold=value[3],
                    improves=bool(integer[1]),tolerance_compared=bool(integer[2]),
                    within_tolerance=None if integer[3]<0 else bool(integer[3]),accepted=bool(integer[4]))
    if code == 11:
        return dict(event='trial_caught',k=integer[0],message=message)
    if code == 12:
        return dict(event='fallback_judgment',err=value[0],scale=value[1],tolerance=value[2],threshold=value[3],accepted=bool(integer[0]))
    raise ValueError('Unknown native trace event code: '+str(code))


def first_trace_difference(actual, expected, identity):
    if len(actual) != len(expected):
        return dict(reason='event_count',actual=len(actual),expected=len(expected))
    for i,(a,b) in enumerate(zip(actual,expected,strict=True)):
        if identity(a) != identity(b):
            return dict(reason='event_operand_or_judgment',index=i,actual=a,expected=b)
    return None


DoublePointer = C.POINTER(C.c_double)
DoubleTrans = C.CFUNCTYPE(C.c_int,C.c_size_t,DoublePointer,DoublePointer,C.c_int,DoublePointer,DoublePointer,C.c_void_p)
DoubleSqrt = C.CFUNCTYPE(C.c_int,C.c_double,DoublePointer,C.c_void_p)
Trace = C.CFUNCTYPE(C.c_int,C.c_int,C.POINTER(C.c_int64),C.c_size_t,C.POINTER(C.c_ubyte),C.c_size_t,C.c_int,C.c_char_p,C.c_void_p)


class Config(C.Structure):
    _fields_ = [(k,C.c_int32) for k in ('abi_version','M','N','spacing','nq','root_iterations','n_halves')]+[
        (k,C.c_double) for k in ('floor','tolerance','fallback_tolerance','scale_floor')]+[
        (k,DoublePointer) for k in ('cosine','sine','halves')]


class Step(C.Structure):
    _fields_ = [(k,C.c_int32) for k in ('profile','step','point_a','point_mid','point_end')]+[
        ('x',C.c_double),('h',C.c_double)]


class Stage(C.Structure):
    _fields_ = [('nsteps',C.c_int32),('npoints',C.c_int32),('steps',C.POINTER(Step)),
                ('coefficients',DoublePointer),('initial42',DoublePointer)]


class Callbacks(C.Structure):
    _fields_ = [('double_trans',DoubleTrans),('double_sqrt',DoubleSqrt),('trace',Trace),('user',C.c_void_p)]


class Diagnostics(C.Structure):
    _fields_ = [(k,C.c_uint64) for k in ('root_calls','root_updates','root_fallbacks','trace_events')]+[
        (k,C.c_double) for k in ('minA','minD','max_root_relative_residual','min_literal_Jacobian_pivot','kernel_seconds')]+[
        ('scalar_bytes',C.c_uint32)]


def array(values):
    return (C.c_double*len(values))(*values)


def fixture_payload(capsule, fixture):
    points,indices = [],{}
    for point in fixture['points']:
        key = (point['profile'],packed([point['x']]))
        values = [point['coefficients'][name] for name in SCALARS]+point['coefficients']['pNumerator']
        if key in indices:
            if packed(points[indices[key]]) != packed(values):
                raise ValueError('Duplicate original abscissa has different coefficients')
        else:
            indices[key] = len(points); points.append(values)
    steps = []
    for profile,grid in enumerate(fixture['grid']):
        for step,point in enumerate(grid):
            x,h = point['x'],point['h']
            ids = [indices[(profile,packed([xx]))] for xx in (x,x+h/2,x+h)]
            steps.append((profile,step,*ids,x,h))
    return dict(points=points,steps=steps,initial=fixture['initial42'])


def abi_inputs(capsule, fixture):
    rules = capsule['root_rules']
    cosine = array([v for row in capsule['trig']['state_cos'] for v in row])
    sine = array([v for row in capsule['trig']['state_sin'] for v in row])
    halves = array(rules['halving_factors'])
    config = Config(1,capsule['modes'],capsule['quadrature'],capsule['spacing'],capsule['independent_quadrature_nodes'],
        rules['iterations'],len(rules['halving_factors']),rules['floor'],rules['tolerance'],
        rules['fallback_tolerance'],rules['scale_floor'],cosine,sine,halves)
    payload = fixture_payload(capsule,fixture)
    coefficient = array([v for row in payload['points'] for v in row]);initial = array(payload['initial'])
    steps = (Step*len(payload['steps']))(*(Step(*row) for row in payload['steps']))
    stage = Stage(len(steps),len(payload['points']),steps,coefficient,initial)
    return config,stage,(cosine,sine,halves,coefficient,initial,steps)


def batch_payload(capsule, with_jac=True):
    rules = capsule['root_rules'];M=capsule['modes']
    header = b'VFN4LD01'+struct.pack('<9i',1,M,capsule['quadrature'],capsule['spacing'],
        capsule['independent_quadrature_nodes'],rules['iterations'],len(rules['halving_factors']),
        len(capsule['fixtures']),int(with_jac))
    body = packed([rules[k] for k in ('floor','tolerance','fallback_tolerance','scale_floor')])
    body += packed(rules['halving_factors'])
    for kind in ('state_cos','state_sin'):
        body += packed([v for row in capsule['trig'][kind] for v in row])
    for fixture in capsule['fixtures']:
        data=fixture_payload(capsule,fixture)
        body+=struct.pack('<2i',len(data['steps']),len(data['points']))+packed(data['initial'])
        body+=packed([v for row in data['points'] for v in row])
        for profile,step,ia,im,ie,x,h in data['steps']:
            body+=struct.pack('<5i2d',profile,step,ia,im,ie,x,h)
    token=hashlib.sha256(header+body).hexdigest().encode('ascii')
    return header+token+body,token.decode()


def read_batch_output(path, expected_token, M, stages, with_jac):
    """Protocol parser only; does not start the native binary or any solver."""
    data=memoryview(Path(path).read_bytes());offset=0
    def take(n):
        nonlocal offset
        if offset+n>len(data):raise ValueError('Truncated binary batch output')
        value=data[offset:offset+n].tobytes();offset+=n;return value
    if take(8)!=b'VFN4OUT1':raise ValueError('Output magic mismatch')
    if struct.unpack('<4i',take(16))!=(1,M,stages,int(with_jac)):raise ValueError('Output dimensions mismatch')
    if take(64).decode()!=expected_token:raise ValueError('Output input/source token mismatch')
    rows=[]
    for stage in range(stages):
        index,status=struct.unpack('<2i',take(8))
        if index!=stage:raise ValueError('Batch stage order mismatch')
        if status:
            length=struct.unpack('<I',take(4))[0]
            raise ValueError('Native batch failed stage '+str(stage)+': '+take(length).decode())
        count=2*M+2;state=list(struct.unpack('<'+'d'*count,take(8*count)))
        tangent=list(struct.unpack('<'+'d'*(count*2*M),take(8*count*2*M))) if with_jac else None
        root=struct.unpack('<3Q5d',take(64))
        rows.append(dict(stage_index=stage,state=state,tangent=tangent,
            root_calls=root[0],root_updates=root[1],root_fallbacks=root[2],
            minA=root[3],minD=root[4],maximum_root_relative_residual=root[5],
            min_literal_Jacobian_pivot=root[6],kernel_seconds=root[7]))
    if offset!=len(data):raise ValueError('Unexpected batch output trailing bytes')
    return rows


def mp_errors(values, reference, fixture):
    errors=[v-mp.mpf(reference[j]) for j,v in enumerate(values)]
    scale,ratio=mp.mpf(float(fixture['normalizationScale'])),mp.mpf(float(fixture['portRatio']))
    norm=[abs(errors[j] if j<20 else errors[j]/ratio)/scale for j in range(40)]
    return dict(maximum_all42_absolute_error=mp.nstr(max(map(abs,errors)),32),
        maximum_mean2_absolute_error=mp.nstr(max(map(abs,errors[40:])),32),
        maximum_normalized_physical_error=mp.nstr(max(norm),32),
        normalized_error_peak_component=max(range(40),key=lambda j:norm[j]))


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--mode',choices=('float-baseline','longdouble','export-batch'),required=True)
    for name in ('build-record','capsule-summary','old-float-baseline','mp90-summary','bridge','out-prefix'):
        p.add_argument('--'+name,type=Path,required=True)
    p.add_argument('--validated-native-baseline',type=Path)
    p.add_argument('--node',default='node')
    a=p.parse_args()
    build=load(a.build_record)
    for ref in list(build['sources'].values())+[build['library'],build['batch_executable']]:
        if sha(ref['path'])!=ref['sha256']:raise ValueError('Reviewed build/source identity changed')
    if build['sources']['harness']!=ident(__file__):raise ValueError('Harness was not part of reviewed frozen build')
    base_path=Path(__file__).resolve().parent.parent/'probe_frozen_stage_multiprecision.py'
    if sha(base_path)!=BASE_SHA or sha(a.bridge)!=BRIDGE_SHA:raise ValueError('Original scalar evaluator/bridge changed')
    spec=importlib.util.spec_from_file_location('original_frozen_reference',base_path)
    base=importlib.util.module_from_spec(spec);spec.loader.exec_module(base)
    cs,bs,ms=load(a.capsule_summary),load(a.old_float_baseline),load(a.mp90_summary)
    if (bs['source_sha256']!=BASE_SHA or not bs['all_original_operands_and_judgments_bitwise_identical'] or
        not bs['all_three_outputs42_bitwise_identical'] or bs['capsule_summary_sha256']!=sha(a.capsule_summary) or
        ms['validated_baseline_sha256']!=sha(a.old_float_baseline) or ms['capsule_summary_sha256']!=sha(a.capsule_summary) or
        ms['source_sha256']!=BASE_SHA or ms['precision']!='mp' or ms['dps']!=90):
        raise ValueError('Original baseline/MP90 identity mismatch')
    for key in ('source_sha256','additional_original_root_sources'):
        for path,digest in cs[key].items():
            if sha(path)!=digest:raise ValueError('A bound original source changed: '+path)
    capsule,reference,precise=checked(cs['coefficients']),checked(cs['reference']),checked(ms['raw'])
    if capsule['modes']!=20 or [f['stage']for f in capsule['fixtures']]!=[43,38,175]:
        raise ValueError('This probe is restricted to the authorized three original stages')
    paths={name:Path(str(a.out_prefix)+'-'+name+('.json'if name=='summary'else'.json.gz'))for name in ('raw','summary','failure')}
    for path in paths.values():
        if path.exists():raise ValueError('Do not overwrite an executed result: '+str(path))
    a.out_prefix.parent.mkdir(parents=True,exist_ok=True)
    context=dict(scope=__doc__,mode=a.mode,source=ident(__file__),build_record=ident(a.build_record),
        library=build['library'],batch_executable=build['batch_executable'],sources=build['sources'],
        original_evaluator=ident(base_path),bridge=ident(a.bridge),capsule_summary=ident(a.capsule_summary),
        old_float_baseline=ident(a.old_float_baseline),mp90_summary=ident(a.mp90_summary),
        coefficient_identity=cs['coefficients'],reference_identity=cs['reference'],mp90_raw=ms['raw'],
        command=sys.argv,root_rules=capsule['root_rules'],production_changed=False,full_tail_or_DN_invoked=False)
    if a.mode=='export-batch':
        path=Path(str(a.out_prefix)+'-batch.bin')
        if path.exists():raise ValueError('Refusing to overwrite batch payload')
        data,token=batch_payload(capsule);path.write_bytes(data)
        paths['summary'].write_text(json.dumps(dict(**context,batch=ident(path),manifest_token=token,
            mathematical_executable_invoked=False),ensure_ascii=False,indent=2)+'\n')
        return
    if a.mode=='longdouble':
        if a.validated_native_baseline is None:raise ValueError('Native exact baseline is required first')
        native_baseline=load(a.validated_native_baseline)
        if (native_baseline['mode']!='float-baseline' or not native_baseline['all_three_outputs42_bitwise_identical'] or
            not native_baseline['all_original_operands_and_judgments_bitwise_identical'] or
            native_baseline['verified_event_count']!=116608 or native_baseline['verified_output_count']!=126 or
            native_baseline['build_record']!=ident(a.build_record) or native_baseline['source']!=ident(__file__) or
            native_baseline['capsule_summary']!=ident(a.capsule_summary)):
            raise ValueError('Native exact baseline is not for these frozen sources/inputs')
        context['validated_native_baseline']=ident(a.validated_native_baseline)
    library=C.CDLL(build['library']['path'])
    library.vf_runtime_info.argtypes=[C.c_char_p,C.c_size_t];library.vf_runtime_info.restype=C.c_int
    runtime_buffer=C.create_string_buffer(4096)
    if library.vf_runtime_info(runtime_buffer,len(runtime_buffer)):raise ValueError('Native runtime info failed')
    runtime=json.loads(runtime_buffer.value)
    for key,kind in (('config_size',Config),('step_size',Step),('stage_size',Stage),('callbacks_size',Callbacks),('diagnostics_size',Diagnostics)):
        if runtime[key]!=C.sizeof(kind):raise ValueError('C ABI layout mismatch: '+key)
    if runtime['long_double_significand_bits']!=64 or not runtime['round_to_nearest']:
        raise ValueError('Unsupported runtime precision/rounding')
    context['runtime']=runtime
    library.vf_run_stage.argtypes=[C.POINTER(Config),C.POINTER(Stage),C.c_int,C.c_int,C.POINTER(Callbacks),
        DoublePointer,DoublePointer,C.POINTER(C.c_ubyte),C.POINTER(C.c_ubyte),C.POINTER(Diagnostics),C.c_char_p,C.c_size_t]
    library.vf_run_stage.restype=C.c_int
    mode=0 if a.mode=='float-baseline' else 1;with_jac=mode==1
    arithmetic=base.V8Float(a.bridge,a.node)if mode==0 else None
    rows,scalars=[],[];event_count=0;began=time.monotonic()
    try:
        for index,fixture in enumerate(capsule['fixtures']):
            events,encoded_events,callback_errors=[],[],[]
            def trans(n,D,u,need_jac,sd,bm,user):
                try:
                    sqrtD,bmn=arithmetic.root_transcendentals([dict(D=D[i],u=u[i])for i in range(n)],bool(need_jac))
                    for i,v in enumerate(sqrtD):sd[i]=v
                    if need_jac:
                        for i,v in enumerate(bmn):bm[i]=v
                    return 0
                except Exception:
                    callback_errors.append(traceback.format_exc());return 1
            def sqrt(value,result,user):
                try:result[0]=arithmetic.sqrt(value);return 0
                except Exception:
                    callback_errors.append(traceback.format_exc());return 1
            def trace(code,ints,ni,values,nv,scalar_mode,message,user):
                try:
                    integers=[ints[i]for i in range(ni)];data=C.string_at(values,nv*(8 if scalar_mode==0 else 10))
                    text=message.decode()if message else None
                    decoded=decoded_values(data,scalar_mode)
                    events.append(decode_event(code,integers,decoded,text,capsule['modes']))
                    if scalar_mode==1:encoded_events.append(dict(code=code,integers=integers,canonical80=data.hex(),message=text))
                    return 0
                except Exception:
                    callback_errors.append(traceback.format_exc());return 1
            callback_objects=(DoubleTrans(trans),DoubleSqrt(sqrt),Trace(trace))
            callbacks=Callbacks(*callback_objects,None)
            config,stage,keepers=abi_inputs(capsule,fixture)
            size=42;columns=40;stride=8 if mode==0 else 10
            state=(C.c_double*size)();tangent=(C.c_double*(size*columns))()if with_jac else None
            native_state=(C.c_ubyte*(size*stride))();native_tangent=(C.c_ubyte*(size*columns*stride))()if with_jac else None
            diagnostics=Diagnostics();error=C.create_string_buffer(4096)
            status=library.vf_run_stage(C.byref(config),C.byref(stage),mode,int(with_jac),C.byref(callbacks),
                state,tangent,native_state,native_tangent,C.byref(diagnostics),error,len(error))
            if status or callback_errors:
                failure=save_gz(paths['failure'],dict(**context,stage=fixture['stage'],status=status,error=error.value.decode(),
                    callback_errors=callback_errors,events=events,encoded_events=encoded_events))
                raise RuntimeError('Native stage failed; saved '+failure['path'])
            actual=list(state);old=reference['rows'][index];high=precise['rows'][index]
            if old['stage']!=fixture['stage']or high['stage']!=fixture['stage']:raise ValueError('Reference stage order changed')
            exact_output=packed(actual)==packed(old['state'])
            mismatch=first_trace_difference(events,old['events'],base.numeric_identity)if mode==0 else None
            if mode==0 and (not exact_output or mismatch is not None):
                failure=save_gz(paths['failure'],dict(**context,stage=fixture['stage'],state=actual,events=events,
                    exact_output=exact_output,first_trace_difference=mismatch))
                raise RuntimeError('Native exact baseline mismatch; saved '+failure['path'])
            encoded=bytes(native_state)
            native_values=[mp.mpf(v)for v in actual]if mode==0 else[native80_value(encoded[j:j+10])for j in range(0,len(encoded),10)]
            boundary_values=[mp.mpf(float(v))for v in actual]
            physical=[v if j<20 else v/fixture['portRatio']for j,v in enumerate(actual[:40])]
            residual=[v-fixture['targetNode40'][j]for j,v in enumerate(physical)]
            diag={name:getattr(diagnostics,name)for name,_ in Diagnostics._fields_}
            diag={name:(None if isinstance(value,float)and not math.isfinite(value)else value)for name,value in diag.items()}
            scalar=dict(stage=fixture['stage'],all42_original_bitwise_identical=exact_output,
                all_original_root_trace_bitwise_identical=(mismatch is None)if mode==0 else False,
                trace_events=len(events),output42_sha256=fhash(actual),native_output_sha256=hashlib.sha256(encoded).hexdigest(),
                diagnostics=diag,native_error_to_mp90=mp_errors(native_values,high['state'],fixture),
                boundary64_error_to_mp90=mp_errors(boundary_values,high['state'],fixture),
                fixed_target_normalized_residual=max(map(abs,residual))/fixture['normalizationScale'])
            row=dict(stage=fixture['stage'],state=actual,native_state_hex=encoded.hex(),events=events,
                encoded_events=encoded_events,residual=residual)
            if with_jac:
                row.update(tangent=list(tangent),native_tangent_hex=bytes(native_tangent).hex())
                scalar.update(tangent42_by40_sha256=fhash(list(tangent)),
                    native_tangent_sha256=hashlib.sha256(bytes(native_tangent)).hexdigest(),
                    literal_Jacobian_computed=True,independent_Jacobian_reference_verified=False)
            event_count+=len(events);rows.append(row);scalars.append(scalar)
            print(json.dumps(dict(event='native_stage_complete',**scalar)),flush=True)
    finally:
        if arithmetic is not None:arithmetic.close()
    if mode==0 and(event_count!=116608 or len(rows)*42!=126):raise ValueError('The complete prescribed baseline count differs')
    raw=save_gz(paths['raw'],dict(**context,rows=rows))
    result=dict(**context,raw=raw,named_results=scalars,seconds=time.monotonic()-began,
        verified_event_count=event_count if mode==0 else 0,verified_output_count=126 if mode==0 else 0,
        all_three_outputs42_bitwise_identical=all(s['all42_original_bitwise_identical']for s in scalars),
        all_original_operands_and_judgments_bitwise_identical=(mode==0),
        full40_column_Jacobian_computed=bool(with_jac),independent_Jacobian_reference_verified=False,
        original_norm_or_DN_acceptance_performed=False,
        scope_limit='Finite arithmetic only. Native implicit derivatives are evaluated at approximate returned roots, not derivatives of the stopping algorithm or certified continuous flows.')
    paths['summary'].write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(dict(event='terminal',summary=str(paths['summary'].resolve()),sha256=sha(paths['summary']))),flush=True)


if __name__=='__main__':main()
