#!/usr/bin/env python3
"""Read completed static producer evidence without invoking any flow.

The process log is not given a false final hash: its first complete immutable
static-identity line is copied verbatim and separately hashed in scratch.
"""
import argparse
import datetime
import gzip
import hashlib
import json
from pathlib import Path
import struct
import sys

PLAN_SHA='a466fa5c14e2c956f9ede00c3259b4551ef7935efdb9f7912e2d6bc71af5eba5'

def sha(b):return hashlib.sha256(b).hexdigest()
def ref(p):
    p=Path(p).resolve()
    return dict(path=str(p),sha256=sha(p.read_bytes()))
def load(p):
    p=Path(p)
    return json.loads(gzip.decompress(p.read_bytes()) if p.suffix=='.gz' else p.read_bytes())
def verify(item):
    if ref(item['path'])!=item:raise ValueError('Changed immutable reference: '+item['path'])
def doubles(values):return struct.pack('<'+'d'*len(values),*values)

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--workspace',type=Path,required=True)
    parser.add_argument('--out',type=Path,required=True)
    a=parser.parse_args();w=a.workspace.resolve()
    base=w/'n4_work/native-node-adapter-v1'
    plan_path=base/'plan.json';plan=load(plan_path)
    if ref(plan_path)['sha256']!=PLAN_SHA:raise ValueError('Unexpected frozen plan')
    for item in plan['files'].values():verify(item)
    manifest=load(plan['files']['manifest']['path'])
    for item in [*manifest['original_sources'],*manifest['owned_sources'],
                 *manifest['native_files'].values(),*manifest['runtime_libraries']]:verify(item)
    metadata_path=base/'actual-entry/static-metadata.json.gz';metadata=load(metadata_path)
    verify(metadata['template']);template=Path(metadata['template']['path']).read_bytes()
    inp_path=base/'actual-entry/0001-jac-input.bin';raw=inp_path.read_bytes()
    if raw[:8]!=b'VFN4LD01':raise ValueError('Wrong wire magic')
    cfg=struct.unpack_from('<9i',raw,8)
    if cfg!=(1,20,512,4,128,30,20,2304,1):raise ValueError('Wrong actual full batch config')
    token=raw[44:108].decode()
    if sha(raw[:44]+raw[108:])!=token:raise ValueError('Payload token mismatch')
    if struct.unpack_from('<4d',raw,108)!=(.05,8e-14,5e-12,1e-300):raise ValueError('Original production rules differ')
    original=load(plan['files']['production_CP']['path'])
    states=original['response']['checkpoint']['states']
    offset=42284;total_steps=total_points=extra=0
    allowed=bytearray(len(raw))
    for start,end in [(40,44),(44,108)]:allowed[start:end]=b'\x01'*(end-start)
    for n,item in enumerate(metadata['stages']):
        nsteps,npoints=struct.unpack_from('<2i',raw,offset)
        if (nsteps,npoints)!=(item['nsteps'],item['npoints']):raise ValueError('Stage dimensions mismatch')
        if item['blockOffset']!=offset or item['initialOffset']!=offset+8:raise ValueError('Stage offset mismatch')
        offset+=8
        if raw[offset:offset+336]!=doubles(states[n+1]+[0.,0.]):raise ValueError('Original node column units/means changed')
        allowed[offset:offset+336]=b'\x01'*336;offset+=336
        coeff=raw[offset:offset+256*npoints]
        if sha(coeff)!=item['coefficients_sha256']:raise ValueError('Coefficient block mismatch')
        offset+=256*npoints
        grid=raw[offset:offset+36*nsteps]
        if sha(grid)!=item['grid_sha256']:raise ValueError('Literal grid block mismatch')
        offset+=36*nsteps
        if offset-item['blockOffset']!=item['blockLength']:raise ValueError('Stage wire length mismatch')
        total_steps+=nsteps;total_points+=npoints;extra+=nsteps!=16*len(item['profileGrids'])
    if offset!=len(raw) or len(template)!=len(raw):raise ValueError('Wire EOF mismatch')
    if any(x!=y and not flag for x,y,flag in zip(raw,template,allowed)):
        raise ValueError('Full input differs from static template outside state/withJac/token')
    counts=metadata['counts']
    expected=dict(stageCount=2304,totalSteps=total_steps,totalUniquePoints=total_points,
        stagesWithExtraCuspSteps=extra,headerBytes=42284,inputBytes=len(raw),
        stateOnlyOutputBytes=88+2304*(8+336+64),fullJacOutputBytes=88+2304*(8+336+13440+64))
    if counts!=expected:raise ValueError('Actual wire/grid counts mismatch')
    if (total_steps,total_points,extra)!=(36891,76086,27):raise ValueError('Unexpected actually measured grid')
    first=(base/'entry-process.log').read_bytes().splitlines(keepends=True)[0]
    identity=json.loads(first)
    if identity['event']!='original_static_producer_identity_passed' or identity['complete_native_evaluates_so_far']!=0:
        raise ValueError('Producer identity did not precede native execution')
    if identity['counts']!=counts:raise ValueError('Static log/count mismatch')
    snapshot=base/'entry-static-identity.jsonl'
    if snapshot.exists():
        if snapshot.read_bytes()!=first:raise ValueError('Existing static event snapshot differs')
    else:snapshot.write_bytes(first)
    fixture_rows=identity['fixtureIdentity']
    if [r['stage'] for r in fixture_rows]!=[43,38,175]:raise ValueError('Original fixture order differs')
    for row in fixture_rows:
        for key in ['all42_input_equal','state_trig_equal','mu_port_and_scale_equal',
                    'all_literal_grid_bytes_equal','all_original_coefficient_points_equal']:
            if row[key] is not True:raise ValueError('A producer byte-identity gate did not pass')
    owned={str(Path(item['path']).relative_to(manifest['source_topic'])):item for item in manifest['owned_sources']}
    changed=[]
    for item in manifest['original_sources']:
        relative=str(Path(item['path']).relative_to(manifest['original_source_topic']))
        if item['sha256']!=owned[relative]['sha256']:changed.append(relative)
    if changed!=['scripts/950f-tail-stage-core.mjs','scripts/950f-tail-stage-port-v3.mjs']:
        raise ValueError('Unexpected existing-source changes')
    record=dict(scope=__doc__,source=ref(__file__),command=sys.argv,
        collected_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
        plan=ref(plan_path),files=plan['files'],manifest=plan['files']['manifest'],
        original_sources=manifest['original_sources'],changed_owned_sources=[owned[name] for name in changed],
        added_owned_sources=[owned['scripts/'+name] for name in ['native_batch_adapter.mjs','native_batch_factory.mjs']],
        native_files=manifest['native_files'],runtime_libraries=manifest['runtime_libraries'],
        syntax_checks=plan['syntax_checks'],literal_core_and_worker_patches=4,
        original_core_reversible_patch_identity=True,original_split_and_same_mu_cache_unchanged=True,
        actual_static_metadata=ref(metadata_path),actual_static_template=metadata['template'],
        actual_full_input=ref(inp_path),payload_token=token,completed_static_event=ref(snapshot),
        all2304_original_state_inputs_and_two_zero_means_byte_equal=True,
        static_template_unchanged_outside_inputs_mode_and_token=True,
        actual_grid_and_wire_counts=counts,three_fixture_identity=fixture_rows,
        production_projectionFloor=.05,old_capsule_projectionFloor=.1,
        static_preparation_seconds=metadata['staticPreparationSeconds'],initiated_observer_session=67330,
        numerical_status_scope='Only completed static producer/packing checks and one initiated evaluate. This record makes no claim about the subsequent native flow terminal. A separate terminal record must bind exit/output.',
        full_evaluate_terminal_claim=False,DN_solve_invoked_by_entry=False,
        shape=dict(native_state=42,native_J=[42,40],original_sparse_J=[40,40]),
        input_columns_scaled=False,output_pi_rows_divided_by_original_portRatio=True,
        output_mean_is_sum_of_original_two_components=True,
        original_norm_scales_targets_Robin_line_search_correction_cut_audit_unchanged=True,
        source_scope='Native state-dependent LD and literal implicit Jacobian replace only the whole-evaluate flow provider. Original cutJets/FD/audit remain original .05 binary64 engines. No closure, exact arc or continuous certificate.')
    with a.out.open('x') as stream:
        json.dump(record,stream,indent=2,ensure_ascii=False,allow_nan=False);stream.write('\n')
    print(json.dumps(dict(record=ref(a.out),actual_counts=counts,read_only=True,new_flow=False)))

if __name__=='__main__':main()
