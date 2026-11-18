#!/usr/bin/env python3
"""Read the completed six-call native LD probe; never load a library or flow.

Independently decode all canonical80 outputs with exact rational arithmetic,
check every stored boundary64 conversion and state-only/full-Jac pair, and
recompute the saved MP90 state-error scalars. Full arrays stay in scratch.
"""
import argparse
from fractions import Fraction
import gzip
import hashlib
import json
import math
from pathlib import Path
import struct
import sys

import mpmath as mp

mp.mp.dps = 140
PLAN_SHA = 'b30bdac3396a3ba141b72d3ec0aa67c989cab5da2ef0602db82973acbfb3bd5b'
PROBE_SHA = '4d6b143bfda1c7ba04e1538aeeade874bc5df3d011fc181d7a3ea3b8ed8865dc'
SUMMARY_SHA = '94f774a4ebac0c1dcad8f6de8e3796f4e6ab23475694e09acefb9fb7e4c86908'
ROOT_KEYS = ('root_calls','root_updates','root_fallbacks','trace_events',
             'minA','minD','max_root_relative_residual','scalar_bytes')


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def ref(path):
    return dict(path=str(Path(path).resolve()),sha256=sha(path))


def load(path):
    p=Path(path)
    return json.loads(gzip.decompress(p.read_bytes()) if p.suffix=='.gz' else p.read_bytes())


def check(item):
    if ref(item['path']) != item:
        raise ValueError('Saved identity changed: '+item['path'])


def nested_refs(value):
    if isinstance(value,dict):
        if set(value)=={'path','sha256'}:
            yield value
        else:
            for v in value.values():
                yield from nested_refs(v)
    elif isinstance(value,list):
        for v in value:
            yield from nested_refs(v)


def packed(values):
    return struct.pack('<'+'d'*len(values),*values)


def digest(data):
    return hashlib.sha256(data).hexdigest()


def native_fraction(data):
    significand,se=struct.unpack('<QH',data)
    exponent=se&0x7fff
    if exponent==0x7fff:
        raise ValueError('Nonfinite canonical80 output')
    shift=(exponent if exponent else 1)-16383-63
    value=Fraction(significand)*(Fraction(2)**shift)
    return -value if se&0x8000 else value


def native_values(encoded):
    if len(encoded)%10:
        raise ValueError('Incomplete canonical80 encoding')
    exact=[native_fraction(encoded[k:k+10]) for k in range(0,len(encoded),10)]
    boundary=[]
    for k,value in enumerate(exact):
        _,se=struct.unpack('<QH',encoded[10*k:10*k+10])
        boundary.append(-0.0 if value==0 and se&0x8000 else float(value))
    return exact,boundary


def mp_exact(value):
    return mp.mpf(value.numerator)/value.denominator


def errors(values,reference,fixture):
    diff=[v-mp.mpf(reference[j]) for j,v in enumerate(values)]
    ratio,scale=mp.mpf(float(fixture['portRatio'])),mp.mpf(float(fixture['normalizationScale']))
    norm=[abs(diff[j] if j<20 else diff[j]/ratio)/scale for j in range(40)]
    return dict(maximum_all42_absolute_error=mp.nstr(max(map(abs,diff)),32),
        maximum_mean2_absolute_error=mp.nstr(max(map(abs,diff[40:])),32),
        maximum_normalized_physical_error=mp.nstr(max(norm),32),
        normalized_error_peak_component=max(range(40),key=lambda j:norm[j]))


def root_identity(row):
    return [packed([row[k]]).hex() if isinstance(row[k],float) else row[k] for k in ROOT_KEYS]


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    for name in ('plan','summary','resource','log','out'):
        parser.add_argument('--'+name,type=Path,required=True)
    a=parser.parse_args()
    if sha(a.plan)!=PLAN_SHA or sha(a.summary)!=SUMMARY_SHA:
        raise ValueError('Collector is restricted to the unique completed six-call run')
    plan,summary,resource=load(a.plan),load(a.summary),load(a.resource)
    if summary['source']['sha256']!=PROBE_SHA or summary['plan']!=ref(a.plan):
        raise ValueError('The native run is not the frozen source/plan')
    seen={}
    for value in (plan,summary):
        for item in nested_refs(value):
            seen[item['path']]=item
    for item in seen.values():
        check(item)
    cs=load(plan['files']['capsule_summary']['path'])
    original_sources={**cs['source_sha256'],**cs['additional_original_root_sources']}
    for path,digest_value in original_sources.items():
        if sha(path)!=digest_value:
            raise ValueError('Original source changed: '+path)
    if (resource['status']!='observed_terminal' or resource['child_returncode']!=0 or
            resource['command']!=plan['command'] or
            resource['script_sha256']!=plan['files']['observer']['sha256'] or
            summary['command']!=plan['command'][1:]):
        raise ValueError('No matching genuine successful observer terminal')
    events=[json.loads(line) for line in a.log.read_text().splitlines() if line.strip()]
    starts=[e for e in events if e['event']=='native_call_start']
    ends=[e for e in events if e['event']=='native_call_complete']
    calls=[dict(stage=e['stage'],with_jac=e['with_jac']) for e in starts]
    if calls!=plan['calls'] or [dict(stage=e['stage'],with_jac=e['with_jac']) for e in ends]!=calls:
        raise ValueError('The original log does not contain exactly the prescribed six calls')
    if events[-1]!={'event':'terminal','summary':ref(a.summary)}:
        raise ValueError('No matching final summary in original process log')
    raw=load(summary['raw']['path'])
    capsule=load(summary['coefficients']['path'])
    high=load(summary['mp90_raw']['path'])
    baseline=load(plan['files']['native_baseline']['path'])
    if len(raw['rows'])!=6 or len(summary['named_results'])!=6 or len(summary['pairs'])!=3:
        raise ValueError('Incomplete saved result inventory')
    runtime=summary['runtime_initial']
    if (runtime['long_double_significand_bits']!=64 or runtime['long_double_storage_bytes']!=16
            or not runtime['round_to_nearest'] or ((runtime['x87_control_word']>>8)&3)!=3):
        raise ValueError('Different actual extended runtime')
    named=[]
    total_state_values=total_tangent_values=0
    for index in range(3):
        fixture=capsule['fixtures'][index]
        reference=high['rows'][index]
        pair_rows=[]
        for offset in (0,1):
            number=2*index+offset
            row=raw['rows'][number]
            scalar=summary['named_results'][number]
            if (dict(stage=row['stage'],with_jac=row['with_jac'])!=calls[number] or
                    row['stage']!=fixture['stage'] or reference['stage']!=row['stage']):
                raise ValueError('Saved stage/order mismatch')
            checkpoint=load(scalar['checkpoint']['path'])
            if checkpoint['row']!=row:
                raise ValueError('Independent per-call checkpoint differs from final raw')
            if {k:v for k,v in ends[number].items() if k!='event'}!=scalar:
                raise ValueError('Saved call scalar differs from original process log')
            native=bytes.fromhex(row['native_state_hex'])
            exact,converted=native_values(native)
            if len(exact)!=42 or len(row['state'])!=42:
                raise ValueError('An entire state or mean is missing')
            boundary=packed(row['state'])
            if boundary.hex()!=row['state64_hex'] or packed(converted)!=boundary:
                raise ValueError('Saved state boundary is not the original native80-to64 conversion')
            if digest(boundary)!=scalar['output42_sha256'] or digest(native)!=scalar['native_output42_sha256']:
                raise ValueError('Saved state hash differs')
            native_error=errors([mp_exact(v) for v in exact],reference['state'],fixture)
            boundary_error=errors([mp.mpf(v) for v in row['state']],reference['state'],fixture)
            if native_error!=scalar['native_error_to_mp90'] or boundary_error!=scalar['boundary64_error_to_mp90']:
                raise ValueError('Independent all42/mean/physical MP90 comparison differs')
            physical=[v if j<20 else v/fixture['portRatio'] for j,v in enumerate(row['state'][:40])]
            residual=[v-fixture['targetNode40'][j] for j,v in enumerate(physical)]
            if (packed(residual)!=packed(row['fixed_target_residual']) or
                    max(map(abs,residual))/fixture['normalizationScale']!=scalar['fixed_target_normalized_residual']):
                raise ValueError('Original fixed-target diagnostic changed')
            if (row['runtime_before']!=runtime or row['runtime_after']!=runtime or
                    row['input_arrays_before']!=row['input_arrays_after']):
                raise ValueError('Original runtime/complete input invariants did not hold')
            diag=row['diagnostics']
            if diag!=scalar['diagnostics'] or diag['root_calls']!=64 or diag['trace_events']!=0 or diag['scalar_bytes']!=10:
                raise ValueError('Different null-trace root diagnostics')
            if row['with_jac']:
                encoded=bytes.fromhex(row['native_tangent_hex'])
                tangent_exact,tangent_converted=native_values(encoded)
                if len(tangent_exact)!=1680 or len(row['tangent'])!=1680:
                    raise ValueError('The full42x40 tangent is incomplete')
                tangent64=packed(row['tangent'])
                if (tangent64.hex()!=row['tangent64_hex'] or packed(tangent_converted)!=tangent64 or
                        digest(encoded)!=scalar['native_tangent42_by40_sha256'] or
                        digest(tangent64)!=scalar['tangent42_by40_sha256']):
                    raise ValueError('A saved tangent encoding/conversion/hash differs')
                if diag['min_literal_Jacobian_pivot'] is None or not diag['min_literal_Jacobian_pivot']>0:
                    raise ValueError('Literal implicit decomposition lacks its own positive observed pivot')
                total_tangent_values+=1680
            total_state_values+=42
            pair_rows.append(row)
        first,second=pair_rows
        pair=dict(stage=fixture['stage'],
            native42_bitwise_identical=first['native_state_hex']==second['native_state_hex'],
            binary64_42_bitwise_identical=first['state64_hex']==second['state64_hex'],
            root_diagnostics_bitwise_identical=root_identity(first['diagnostics'])==root_identity(second['diagnostics']))
        if pair!=summary['pairs'][index] or not all(v for k,v in pair.items() if k!='stage'):
            raise ValueError('Complete original state-only/full-Jac identity gate failed')
        rounded=[float(Fraction(v)) for v in reference['state']]
        equal_rounding=[packed([v])==packed([w]) for v,w in zip(second['state'],rounded,strict=True)]
        s0,s1=summary['named_results'][2*index:2*index+2]
        named.append(dict(**pair,original_binary64_error_to_mp90=baseline['named_results'][index]['native_error_to_mp90'],
            native_error_to_mp90=s1['native_error_to_mp90'],boundary64_error_to_mp90=s1['boundary64_error_to_mp90'],
            boundary64_components_equal_to_rounded_saved_mp90=sum(equal_rounding),
            boundary64_components_total=42,fixed_target_normalized_residual=s1['fixed_target_normalized_residual'],
            root_diagnostics={k:s1['diagnostics'][k] for k in ROOT_KEYS},
            minimum_literal_Jacobian_pivot=s1['diagnostics']['min_literal_Jacobian_pivot'],
            state_only_checkpoint=s0['checkpoint'],full_Jacobian_checkpoint=s1['checkpoint'],
            state_only_kernel_seconds=s0['diagnostics']['kernel_seconds'],
            full_Jacobian_kernel_seconds=s1['diagnostics']['kernel_seconds'],
            state_only_FFI_seconds=s0['ffi_seconds'],full_Jacobian_FFI_seconds=s1['ffi_seconds'],
            state_only_decode_compare_seconds=s0['python_decode_compare_seconds'],
            full_Jacobian_decode_compare_seconds=s1['python_decode_compare_seconds'],
            native_state_sha256=s1['native_output42_sha256'],state64_sha256=s1['output42_sha256'],
            native_tangent_sha256=s1['native_tangent42_by40_sha256'],tangent64_sha256=s1['tangent42_by40_sha256']))
    if total_state_values!=252 or total_tangent_values!=5040:
        raise ValueError('Complete six-call output conversion counts differ')
    result=dict(scope=__doc__,collector=ref(__file__),collector_command=sys.argv,
        plan=ref(a.plan),summary=ref(a.summary),raw=summary['raw'],resource=ref(a.resource),log=ref(a.log),
        files=plan['files'],original_input=summary['original_input'],original_fixture=summary['original_fixture'],
        original_source_sha256=original_sources,source=summary['source'],build_record=summary['build_record'],
        library=summary['library'],runtime=runtime,loaded_runtime=summary['loaded_runtime'],
        execution=dict(observer_session=95607,child_returncode=resource['child_returncode'],
            observed_utc=resource['observed_utc'],observer_seconds=resource['seconds'],
            probe_seconds=summary['seconds'],maximum_sampled_tree_rss_kib=resource['maximum_sampled_tree_rss_kib'],
            child_rusage_maxrss_kib=resource['child_rusage_maxrss_kib'],
            RSS_scope='Sampled namespace tree RSS and RUSAGE_CHILDREN maxrss are distinct observations, not a whole-host/all-process peak.'),
        checked_path_references=len(seen),checked_original_source_count=len(original_sources),
        native_call_count=6,trace_callback=False,extra_traced_calls=0,
        independently_decoded_native_state_values=total_state_values,
        independently_decoded_native_tangent_values=total_tangent_values,
        all_native_to_boundary64_conversions_bitwise_identical=True,
        all_three_native_and_boundary_state_pairs_bitwise_identical=True,
        all_three_available_root_diagnostic_pairs_bitwise_identical=True,
        named_results=named,whole_tail_or_DN_invoked=False,independent_Jacobian_reference_verified=False,
        root_diagnostic_scope=summary['root_diagnostic_scope'],timing_scope=summary['timing_scope'],
        scope_limit=summary['scope_limit'],
        conclusion='Original finite flow states are materially closer to savedMP90 before and after the boundary64 conversion. State-only/full-Jac and encoding gates pass; these fixed nodes still do not pass original DN tolerance. The complete independent tangent comparison, batch, original DN and audit remain unpaid.')
    with a.out.open('x') as f:
        json.dump(result,f,indent=2,ensure_ascii=False,allow_nan=False)
        f.write('\n')
    print(json.dumps(dict(record=ref(a.out),stages=[dict(stage=r['stage'],
        native_error=r['native_error_to_mp90']['maximum_normalized_physical_error'],
        boundary_error=r['boundary64_error_to_mp90']['maximum_normalized_physical_error'],
        rounded_mp90_equal=r['boundary64_components_equal_to_rounded_saved_mp90']) for r in named])),flush=True)


if __name__=='__main__':
    main()
