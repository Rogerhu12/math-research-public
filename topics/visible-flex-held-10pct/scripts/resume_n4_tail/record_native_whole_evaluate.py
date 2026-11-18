#!/usr/bin/env python3
"""Collect one complete native/provider evaluate terminal, without any flow.

Independently decode the saved boundary64 output and replay only the original
binary64 row conversion, subtraction, mean sum and normalized maximum. These
are read-only arithmetic checks of saved arrays, not a new root/RK/Jacobian.
"""
import argparse
import gzip
import hashlib
import json
from pathlib import Path
import struct
import sys
import numpy as np


def ref(p):
    p=Path(p).resolve()
    return dict(path=str(p),sha256=hashlib.sha256(p.read_bytes()).hexdigest())
def load(p):
    p=Path(p)
    return json.loads(gzip.decompress(p.read_bytes()) if p.suffix=='.gz' else p.read_bytes())
def verify(item):
    if ref(item['path'])!=item:raise ValueError('Immutable reference changed: '+item['path'])
def digest(b):return hashlib.sha256(b).hexdigest()
def json_numeric_bytes(a):
    # JSON.stringify loses -0. Native wire is retained separately, unchanged.
    b=np.asarray(a,dtype='<f8').copy();b[b==0]=0
    return b.tobytes()


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--workspace',type=Path,required=True)
    parser.add_argument('--out',type=Path,required=True)
    a=parser.parse_args();w=a.workspace.resolve()
    topic=w/'math-research-public/topics/visible-flex-held-10pct'
    base=w/'n4_work/native-node-adapter-v1'
    plan=load(base/'plan.json');summary=load(base/'entry-summary.json');resource=load(base/'entry-resource.json')
    if summary['status']!='complete' or summary['native_evaluate_count']!=1:
        raise ValueError('A complete one-evaluate terminal is required')
    if resource['status']!='observed_terminal' or resource['child_returncode']!=0:
        raise ValueError('A genuine zero child terminal is required')
    for item in [*plan['files'].values(),summary['raw'],summary['static_metadata']]:verify(item)
    manifest=load(plan['files']['manifest']['path'])
    for item in [*manifest['original_sources'],*manifest['owned_sources'],
                 *manifest['native_files'].values(),*manifest['runtime_libraries']]:verify(item)
    batch_path=base/'actual-entry/0001-jac-record.json';batch=load(batch_path)
    if batch['status']!='complete' or batch['returncode']!=0 or batch['signal'] is not None or batch['spawn_error'] is not None:
        raise ValueError('The complete native process did not succeed')
    for key in ['input','output','stdout','stderr','manifest','static_metadata']:verify(batch[key])
    data=load(summary['raw']['path']);metadata=load(summary['static_metadata']['path'])
    old=load(plan['files']['production_CP']['path']);states=np.asarray(old['response']['checkpoint']['states'],dtype='<f8')
    scales=np.asarray(data['scales'],dtype='<f8');target=np.asarray(data['target'],dtype='<f8')
    raw=Path(batch['output']['path']).read_bytes();input_bytes=Path(batch['input']['path']).read_bytes()
    if raw[:8]!=b'VFN4OUT1' or struct.unpack_from('<4i',raw,8)!=(1,20,2304,1):raise ValueError('Output header differs')
    token=raw[24:88].decode()
    if token!=input_bytes[44:108].decode() or token!=digest(input_bytes[:44]+input_bytes[108:]):
        raise ValueError('Input/output payload token mismatch')
    if len(raw)!=31905880:raise ValueError('Output has not exactly2304 complete fullJac rows')
    if not (states.shape==(2305,40) and scales.shape==(2305,) and np.isfinite(scales).all() and (scales>0).all()):
        raise ValueError('Original complete states/scales invalid')
    offset=88;norm=0.;mean=0.;minA=float('inf');minD=float('inf');kernel=0.
    root_calls=root_updates=root_fallbacks=0;state_scalars=tangent_scalars=0;peaks=[]
    minimum_pivot=float('inf');maximum_root_residual=0.
    for n in range(2304):
        index,status=struct.unpack_from('<2i',raw,offset);offset+=8
        if (index,status)!=(n,0):raise ValueError('Stage ordering/status differs')
        native_state=np.frombuffer(raw,dtype='<f8',count=42,offset=offset).copy();offset+=336
        native_J=np.frombuffer(raw,dtype='<f8',count=1680,offset=offset).reshape(42,40).copy();offset+=13440
        counters=struct.unpack_from('<3Q',raw,offset);offset+=24
        diag=struct.unpack_from('<5d',raw,offset);offset+=40
        if not (np.isfinite(native_state).all() and np.isfinite(native_J).all()):raise ValueError('Nonfinite native outputs')
        expected_steps=metadata['stages'][n]['nsteps']
        if counters[0]!=4*expected_steps:raise ValueError('Root count differs from actual cusp grid')
        ratio=metadata['stages'][n]['portRatio']
        out=native_state[:40].copy();out[20:]/=ratio
        J=native_J[:40].copy();J[20:]/=ratio
        flow=data['flows'][n];residual=out-states[n]
        if json_numeric_bytes(out)!=json_numeric_bytes(flow['out']):raise ValueError('Original output port-row conversion mismatch')
        if json_numeric_bytes(J.ravel())!=json_numeric_bytes(flow['J']):raise ValueError('Original first40 Jacobian row conversion mismatch')
        if json_numeric_bytes(residual)!=json_numeric_bytes(data['residuals'][n]):raise ValueError('Original shooting subtraction mismatch')
        h=float(native_state[40])+float(native_state[41])
        if struct.pack('<d',h)!=struct.pack('<d',flow['meanHeight']):raise ValueError('Two-mean sum differs')
        if (diag[0],diag[1])!=(flow['minA'],flow['minD']):raise ValueError('Root-domain diagnostics differ')
        norm=max(norm,float(np.max(np.abs(residual)/scales[n])));mean+=h
        minA=min(minA,diag[0]);minD=min(minD,diag[1]);minimum_pivot=min(minimum_pivot,diag[3])
        maximum_root_residual=max(maximum_root_residual,diag[2]);kernel+=diag[4]
        root_calls+=counters[0];root_updates+=counters[1];root_fallbacks+=counters[2]
        state_scalars+=42;tangent_scalars+=1680
        j=int(np.argmax(np.abs(residual)))
        peaks.append(dict(stage=n,component=j,normalized=abs(float(residual[j]))/float(scales[n])))
    if offset!=len(raw):raise ValueError('Output EOF differs')
    end=float(np.max(np.abs(np.asarray(data['end']))/scales[-1]))
    left=float(np.max(np.abs(states[0,:20]-target)/scales[0]))
    norm=max(norm,end,left)
    if (norm,minA,minD)!=(summary['original_normalizedResidual'],summary['minA'],summary['minD']):
        raise ValueError('Original complete normalized maximum/minima mismatch')
    if mean!=summary['meanHeightToCut']:raise ValueError('Complete original mean sum mismatch')
    if end!=summary['far_Robin_normalized_max'] or left!=summary['left_target_normalized_max']:
        raise ValueError('Original boundary contributions mismatch')
    if kernel!=batch['kernel_seconds_sum']:raise ValueError('Saved kernel timing sum mismatch')
    if data['config']!=old['config']:raise ValueError('Saved config changed')
    files=dict(plan=ref(base/'plan.json'),summary=ref(base/'entry-summary.json'),raw=summary['raw'],
        resource=ref(base/'entry-resource.json'),process_log=ref(base/'entry-process.log'),
        batch_record=ref(batch_path),batch_input=batch['input'],batch_output=batch['output'],
        batch_stdout=batch['stdout'],batch_stderr=batch['stderr'],static_metadata=summary['static_metadata'],
        native_events=ref(base/'actual-entry/events.jsonl'),manifest=plan['files']['manifest'],
        input_CP=plan['files']['production_CP'],
        entry_record=ref(topic/'scripts/resume_n4_tail/native_whole_evaluate_entry.json'))
    record=dict(scope=__doc__,source=ref(__file__),command=sys.argv,files=files,
        executed_sources=plan['files'],observer_session=67330,
        observer=dict(status=resource['status'],child_returncode=resource['child_returncode'],
            observed_utc=resource['observed_utc'],seconds=resource['seconds'],
            maximum_sampled_tree_rss_kib=resource['maximum_sampled_tree_rss_kib'],
            child_rusage_maxrss_kib=resource['child_rusage_maxrss_kib'],
            memory_scope='Namespace sampled RSS and RUSAGE_CHILDREN maxrss are different observations; neither is asserted to be a whole-host/full-tree simultaneous peak.'),
        native_process=dict(returncode=batch['returncode'],signal=batch['signal'],process_wall_seconds=batch['process_wall_seconds'],
            kernel_seconds_sum=kernel,decode_and_validation_seconds=batch['decode_and_validation_seconds']),
        all_stages_complete=2304,native_calls=1,actual_grid_counts=metadata['counts'],
        independently_checked_native_state_scalars=state_scalars,
        independently_checked_native_tangent_scalars=tangent_scalars,
        independently_checked_original_consumed_J_scalars=2304*1600,
        output_row_conversion_and_original_norm_match=True,
        JSON_signed_zero_scope='Raw binary64 output remains exact; JSON array comparisons normalize signed zero only because the executed JSON.stringify serialization already does so.',
        root_calls=root_calls,root_updates=root_updates,root_fallbacks=root_fallbacks,
        min_literal_Jacobian_pivot=minimum_pivot,max_root_relative_residual=maximum_root_residual,
        original_normalizedResidual=norm,original_gate=2e-9,same_state_below_original_gate=norm<2e-9,
        minA=minA,minD=minD,far_Robin_normalized_max=end,left_target_normalized_max=left,
        meanHeightToCut=mean,dominantResidual=summary['largestResidual'][0],
        producer_checks=summary['fixtureIdentity'],original_CP_nodes_mutated=False,
        new_H_or_physical_model=False,DN_Newton_solve_invoked=False,cutJets_or_audit_invoked=False,
        conclusion_scope='Complete finite same-state flow+literal Jacobian transport and original full norm. This is not an actual accepted DN/Jac/cut/audit response, fullH continuation, prefix coupling, exact arc or closed family.')
    with a.out.open('x') as stream:
        json.dump(record,stream,indent=2,ensure_ascii=False,allow_nan=False);stream.write('\n')
    print(json.dumps(dict(record=ref(a.out),normalizedResidual=norm,root_calls=root_calls,read_only=True)))


if __name__=='__main__':main()
