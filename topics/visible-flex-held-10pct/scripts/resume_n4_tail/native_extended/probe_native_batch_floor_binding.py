#!/usr/bin/env python3
"""Two declared three-stage batch calls for the original .1 and production .05.

This is a source/binary/configuration-interface check, not an algorithm scan.
Each case uses the same three saved inputs and the full42x40 implicit Jacobian.
Every output binary64 state/tangent and available root diagnostic must match
the already accepted LD full-Jac probe. No Node tail, DN or nonlinear MP runs.
"""
import argparse
import copy
import gzip
import hashlib
import importlib.util
import json
import math
from pathlib import Path
import struct
import subprocess
import sys
import time
import traceback


HARNESS_SHA='42893f210b6d31c59abd04cdfec415a2408a543f726f87d808fc99cf8fad45db'
LD_SUMMARY_SHA='94f774a4ebac0c1dcad8f6de8e3796f4e6ab23475694e09acefb9fb7e4c86908'
CASES=[dict(label='capsule-point1',floor=.1),dict(label='production-point05',floor=.05)]


def ref(path):
    p=Path(path).resolve()
    return dict(path=str(p),sha256=hashlib.sha256(p.read_bytes()).hexdigest())


def load(path):
    p=Path(path)
    return json.loads(gzip.decompress(p.read_bytes()) if p.suffix=='.gz' else p.read_bytes())


def packed(values):
    return struct.pack('<'+'d'*len(values),*values)


def digest(data):
    return hashlib.sha256(data).hexdigest()


def save(path,data,compressed=False):
    path=Path(path)
    raw=(json.dumps(data,ensure_ascii=False,allow_nan=False,indent=None if compressed else 2)+'\n').encode()
    with path.open('xb') as stream:
        stream.write(gzip.compress(raw,mtime=0) if compressed else raw)
    return ref(path)


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--plan',type=Path,required=True)
    parser.add_argument('--build-record',type=Path,required=True)
    a=parser.parse_args();plan=load(a.plan);build=load(a.build_record)
    if plan['schema']!='n4-native-production-floor-v1' or plan['batch_cases']!=CASES:
        raise ValueError('The unique two-case protocol plan changed')
    for item in plan['files'].values():
        if ref(item['path'])!=item:
            raise ValueError('The frozen source/input changed: '+item['path'])
    if plan['files']['batch_probe']!=ref(__file__) or build['plan']!=ref(a.plan):
        raise ValueError('Build/probe plan identity mismatch')
    if not build['success'] or any(r['returncode']!=0 for r in build['compile_results'].values()):
        raise ValueError('The separately reviewed compile did not succeed')
    for item in (build['library'],build['batch_executable']):
        if ref(item['path'])!=item:
            raise ValueError('The just-built binary changed')
    for key,entry in build['compile_results'].items():
        if entry['command']!=plan['compile_commands'][key]:
            raise ValueError('The actual compiler command differs from the frozen plan')
        for name in ('stdout','stderr','binary'):
            if ref(entry[name]['path'])!=entry[name]:
                raise ValueError('The actual compiler artifact changed')
    if plan['files']['harness']['sha256']!=HARNESS_SHA:
        raise ValueError('Only the existing fieldwise codec may be reused')
    spec=importlib.util.spec_from_file_location('reviewed_native_protocol',plan['files']['harness']['path'])
    h=importlib.util.module_from_spec(spec);spec.loader.exec_module(h)
    cs=load(plan['files']['capsule_summary']['path'])
    production=load(plan['files']['production_CP']['path'])
    if (plan['files']['production_CP']!=cs['input'] or
            production['response']['checkpoint']['parameters']['projectionFloor']!=.05):
        raise ValueError('The production floor is not bound to the original actual DN checkpoint')
    for key in ('source_sha256','additional_original_root_sources'):
        for path,digest_value in cs[key].items():
            if ref(path)['sha256']!=digest_value:
                raise ValueError('Original frozen source changed: '+path)
    capsule=load(cs['coefficients']['path'])
    ld=load(plan['files']['LD_summary']['path'])
    if (plan['files']['LD_summary']['sha256']!=LD_SUMMARY_SHA or
            not ld['all_native42_state_pairs_bitwise_identical'] or
            not ld['all_binary64_42_state_pairs_bitwise_identical']):
        raise ValueError('The original complete LD result identity is missing')
    if ref(ld['raw']['path'])!=ld['raw'] or ref(cs['coefficients']['path'])!=cs['coefficients']:
        raise ValueError('The saved full LD or coefficient bytes changed')
    old=load(ld['raw']['path'])
    originals=[r for r in old['rows'] if r['with_jac']]
    if [r['stage'] for r in originals]!=[43,38,175] or capsule['root_rules']['floor']!=.1:
        raise ValueError('Only the original three full-Jac states and capsule are supported')
    prefix=Path(plan['batch_output_prefix']);prefix.parent.mkdir(parents=True,exist_ok=True)
    suffixes=['summary.json','raw.json.gz','failure.json.gz']
    for case in CASES:
        suffixes += [case['label']+suffix for suffix in ('.input.bin','.output.bin','.stdout','.stderr','.checkpoint.json.gz')]
    if any(Path(str(prefix)+'-'+suffix).exists() for suffix in suffixes):
        raise ValueError('Do not overwrite a completed or partial interface execution')
    context=dict(scope=__doc__,source=ref(__file__),plan=ref(a.plan),build_record=ref(a.build_record),
        library=build['library'],batch_executable=build['batch_executable'],files=plan['files'],
        original_capsule=cs['coefficients'],original_full_LD=ld['raw'],command=sys.argv,
        batch_processes_planned=2,stages_per_process=3,with_jac=True,
        source_identity_external_to_payload_token=True,
        original_sources_modified=False,whole_tail_or_DN_invoked=False,nonlinear_MP_invoked=False)
    rows,scalars=[],[];prior_payload=None;last=None
    began=time.monotonic()
    try:
        for case in CASES:
            last=case
            current=copy.deepcopy(capsule);current['root_rules']['floor']=case['floor']
            payload,token=h.batch_payload(current,with_jac=True)
            # The wire header is8+9*4 bytes; its64-byte token is followed by
            # four original rule doubles, beginning with the selected floor.
            if struct.unpack('<d',payload[108:116])[0]!=case['floor']:
                raise ValueError('Declared floor is not at its exact ABI byte offset')
            if prior_payload is not None:
                keep=lambda data:data[:44]+data[116:]
                if keep(payload)!=keep(prior_payload):
                    raise ValueError('The two inputs differ beyond their floor and payload token')
            prior_payload=payload
            base=Path(str(prefix)+'-'+case['label'])
            input_path,output_path=Path(str(base)+'.input.bin'),Path(str(base)+'.output.bin')
            input_path.write_bytes(payload)
            command=[build['batch_executable']['path'],str(input_path),str(output_path)]
            print(json.dumps(dict(event='fixture_batch_start',**case,command=command)),flush=True)
            started=time.monotonic()
            done=subprocess.run(command,capture_output=True,check=False)
            wall=time.monotonic()-started
            stdout,stderr=Path(str(base)+'.stdout'),Path(str(base)+'.stderr')
            stdout.write_bytes(done.stdout);stderr.write_bytes(done.stderr)
            call=dict(**case,command=command,returncode=done.returncode,wall_seconds=wall,
                input=ref(input_path),output=ref(output_path) if output_path.exists() else None,
                stdout=ref(stdout),stderr=ref(stderr),payload_token=token)
            if done.returncode:
                rows.append(dict(call=call));raise RuntimeError('New batch CLI failed; artifacts retained')
            output=h.read_batch_output(output_path,token,20,3,True)
            comparisons=[]
            for index,(row,reference) in enumerate(zip(output,originals,strict=True)):
                if len(row['state'])!=42 or len(row['tangent'])!=1680:
                    raise ValueError('An output/mean/Jacobian component is missing')
                same_state=packed(row['state'])==packed(reference['state'])
                same_jac=packed(row['tangent'])==packed(reference['tangent'])
                fields={'root_calls':'root_calls','root_updates':'root_updates','root_fallbacks':'root_fallbacks',
                    'minA':'minA','minD':'minD','maximum_root_relative_residual':'max_root_relative_residual',
                    'min_literal_Jacobian_pivot':'min_literal_Jacobian_pivot'}
                same_root=all(packed([row[k]])==packed([reference['diagnostics'][v]]) for k,v in fields.items())
                comparison=dict(stage=reference['stage'],state42_bitwise_matches_old_LD=same_state,
                    tangent42_by40_bitwise_matches_old_LD=same_jac,root_aggregates_bitwise_match_old_LD=same_root,
                    state42_sha256=digest(packed(row['state'])),tangent42_by40_sha256=digest(packed(row['tangent'])),
                    root_calls=row['root_calls'],root_updates=row['root_updates'],root_fallbacks=row['root_fallbacks'],
                    minA=row['minA'],minD=row['minD'],max_root_relative_residual=row['maximum_root_relative_residual'],
                    minimum_literal_Jacobian_pivot=row['min_literal_Jacobian_pivot'],kernel_seconds=row['kernel_seconds'])
                comparisons.append(comparison)
            raw_row=dict(call=call,outputs=output,comparisons=comparisons)
            rows.append(raw_row)
            checkpoint=save(Path(str(base)+'.checkpoint.json.gz'),dict(**context,row=raw_row),True)
            if not all(r[k] for r in comparisons for k in ('state42_bitwise_matches_old_LD',
                    'tangent42_by40_bitwise_matches_old_LD','root_aggregates_bitwise_match_old_LD')):
                raise ValueError('Full new-batch/floor/output interface identity failed')
            scalar=dict(call=call,comparisons=comparisons,checkpoint=checkpoint)
            scalars.append(scalar)
            print(json.dumps(dict(event='fixture_batch_complete',**scalar)),flush=True)
        raw=save(Path(str(prefix)+'-raw.json.gz'),dict(**context,rows=rows),True)
        summary=save(Path(str(prefix)+'-summary.json'),dict(**context,raw=raw,named_results=scalars,
            completed_batch_processes=2,completed_native_stages=6,
            all_252_state_and_10080_tangent_binary64_values_match_old_LD=True,
            all_root_aggregates_match_old_LD=True,
            only_floor_and_payload_token_changed_between_two_input_files=True,
            seconds=time.monotonic()-began,
            scope_limit='Identity holds only for these saved three stages; .05 and .1 are different domain gates for general inputs. Production Node hook/norm/DN/audit are not executed.'))
        print(json.dumps(dict(event='terminal',summary=summary)),flush=True)
    except Exception:
        failure=save(Path(str(prefix)+'-failure.json.gz'),dict(**context,last_case=last,
            completed_rows=rows,completed_scalars=scalars,traceback=traceback.format_exc()),True)
        print(json.dumps(dict(event='failure',record=failure)),flush=True)
        raise


if __name__=='__main__':
    main()
