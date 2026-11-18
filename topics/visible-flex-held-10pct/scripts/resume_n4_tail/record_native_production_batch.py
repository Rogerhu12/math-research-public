#!/usr/bin/env python3
"""Read-only independent fieldwise audit of the completed two floor batches.

Decode every input field and output state/Jacobian byte from the existing files.
Do not import the native codec/library or run any mathematical evaluator.
"""
import argparse
import gzip
import hashlib
import json
from pathlib import Path
import struct
import sys


SCALARS=('r3','r4','sqrt2','sqrt12','E','w2','pDenominator','targetFactor',
         'sigma','fluxPrefactor','qLNumerator','meanFactor')


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


def nested(value):
    if isinstance(value,dict):
        if set(value)=={'path','sha256'}:
            yield value
        else:
            for child in value.values():
                yield from nested(child)
    elif isinstance(value,list):
        for child in value:
            yield from nested(child)


class Reader:
    def __init__(self,data):
        self.data=data;self.offset=0

    def take(self,n):
        out=self.data[self.offset:self.offset+n]
        if len(out)!=n:
            raise ValueError('Truncated existing binary file')
        self.offset+=n
        return out

    def unpack(self,kind):
        return struct.unpack('<'+kind,self.take(struct.calcsize('<'+kind)))

    def end(self):
        if self.offset!=len(self.data):
            raise ValueError('Unexpected trailing bytes')


def audit_input(data,case,capsule):
    r=Reader(data)
    if r.take(8)!=b'VFN4LD01' or r.unpack('9i')!=(1,20,512,4,128,30,20,3,1):
        raise ValueError('Binary input header changed')
    token=r.take(64).decode()
    if token!=digest(data[:44]+data[108:]) or token!=case['payload_token']:
        raise ValueError('The input payload token is not its complete fieldwise hash')
    rules=capsule['root_rules']
    wanted=[case['floor'],rules['tolerance'],rules['fallback_tolerance'],rules['scale_floor']]
    if r.take(32)!=packed(wanted) or r.take(160)!=packed(rules['halving_factors']):
        raise ValueError('A declared original root rule changed')
    for key in ('state_cos','state_sin'):
        values=[v for row in capsule['trig'][key] for v in row]
        if r.take(len(values)*8)!=packed(values):
            raise ValueError('The original state-trig byte sequence changed')
    counts=[]
    for fixture in capsule['fixtures']:
        nsteps,npoints=r.unpack('2i')
        if r.take(336)!=packed(fixture['initial42']):
            raise ValueError('A full original42 stage input changed')
        points,lookup=[],{}
        for point in fixture['points']:
            key=(point['profile'],packed([point['x']]))
            values=[point['coefficients'][name] for name in SCALARS]+point['coefficients']['pNumerator']
            if key not in lookup:
                lookup[key]=len(points);points.append(values)
            elif packed(points[lookup[key]])!=packed(values):
                raise ValueError('Conflicting saved coefficient lookup')
        if npoints!=len(points):
            raise ValueError('Unexpected unique coefficient count')
        coefficients=[v for row in points for v in row]
        if r.take(8*len(coefficients))!=packed(coefficients):
            raise ValueError('A frozen coefficient double changed')
        total=0
        for profile,grid in enumerate(fixture['grid']):
            for step,row in enumerate(grid):
                x,h=row['x'],row['h']
                ids=[lookup[(profile,packed([xx]))] for xx in (x,x+h/2,x+h)]
                if r.take(36)!=struct.pack('<5i2d',profile,step,*ids,x,h):
                    raise ValueError('A real frozen RK step/abscissa/coefficient index changed')
                total+=1
        if total!=nsteps:
            raise ValueError('Unexpected actual RK step count')
        counts.append(dict(stage=fixture['stage'],steps=nsteps,unique_points=npoints))
    r.end()
    return token,counts


def audit_output(data,token,reference,raw_rows,comparisons):
    r=Reader(data)
    if r.take(8)!=b'VFN4OUT1' or r.unpack('4i')!=(1,20,3,1) or r.take(64).decode()!=token:
        raise ValueError('Binary output header or echoed token changed')
    rows=[]
    for index,old in enumerate(reference):
        if r.unpack('2i')!=(index,0):
            raise ValueError('A native stage did not return success in the actual binary')
        state,jac=r.take(336),r.take(13440)
        if state!=packed(old['state']) or jac!=packed(old['tangent']):
            raise ValueError('A complete state/tangent byte differs from old full LD')
        if state!=packed(raw_rows[index]['state']) or jac!=packed(raw_rows[index]['tangent']):
            raise ValueError('Parsed JSON rows differ from their original binary authority')
        root=r.unpack('3Q5d')
        d=old['diagnostics']
        if (root[:3]!=(d['root_calls'],d['root_updates'],d['root_fallbacks']) or
                packed(root[3:7])!=packed([d['minA'],d['minD'],d['max_root_relative_residual'],d['min_literal_Jacobian_pivot']])):
            raise ValueError('An original available root aggregate changed')
        c=comparisons[index]
        if (c['stage']!=old['stage'] or c['state42_sha256']!=digest(state) or
                c['tangent42_by40_sha256']!=digest(jac) or c['kernel_seconds']!=root[7]):
            raise ValueError('Saved comparison scalar differs from binary output')
        rows.append(dict(stage=old['stage'],state42_bitwise_identical=True,
            tangent42_by40_bitwise_identical=True,available_root_aggregates_bitwise_identical=True,
            state42_sha256=digest(state),tangent42_by40_sha256=digest(jac),
            root_calls=root[0],root_updates=root[1],root_fallbacks=root[2],
            minA=root[3],minD=root[4],maximum_root_relative_residual=root[5],
            minimum_literal_Jacobian_pivot=root[6],kernel_seconds=root[7]))
    r.end()
    return rows


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    for name in ('plan','summary','resource','log','out'):
        parser.add_argument('--'+name,type=Path,required=True)
    a=parser.parse_args();plan,summary,resource=map(load,(a.plan,a.summary,a.resource))
    if ref(a.plan)['sha256']!='6d3aa2a9deaea97a73e2a6d4a227c6f7ae0e775edbbd94c4982c748721d41a4e':
        raise ValueError('Another frozen source/floor plan')
    if ref(a.summary)['sha256']!='53c90c199ece0e11cb9e556a0c93a363a2113f79392915f81914e5cb20e83a21':
        raise ValueError('Another original execution summary')
    seen={}
    for item in nested(summary):
        if ref(item['path'])!=item:
            raise ValueError('Changed source/input/output identity')
        seen[item['path']]=item
    if (resource['status']!='observed_terminal' or resource['child_returncode']!=0 or
            resource['command']!=plan['batch_probe_command'] or
            resource['script_sha256']!=plan['files']['observer']['sha256'] or
            summary['command']!=plan['batch_probe_command'][1:]):
        raise ValueError('No matching genuine original observer terminal')
    log=[json.loads(line) for line in a.log.read_text().splitlines() if line.strip()]
    if len(log)!=5 or log[-1]!={'event':'terminal','summary':ref(a.summary)}:
        raise ValueError('Unexpected process-log call count or terminal')
    raw=load(summary['raw']['path']);capsule=load(summary['original_capsule']['path'])
    prior=load(summary['original_full_LD']['path'])
    old=[row for row in prior['rows'] if row['with_jac']]
    if [row['stage'] for row in old]!=[43,38,175] or len(raw['rows'])!=2:
        raise ValueError('Original complete stage/case inventory differs')
    inputs=[];cases=[]
    for index,row in enumerate(raw['rows']):
        call=row['call'];name=plan['batch_cases'][index]
        if ({k:call[k] for k in ('label','floor')}!=name or call['returncode']!=0 or
                call['command']!=[summary['batch_executable']['path'],call['input']['path'],call['output']['path']]):
            raise ValueError('Wrong case, command or native process exit')
        scalar=summary['named_results'][index]
        if load(scalar['checkpoint']['path'])['row']!=row or scalar['call']!=call:
            raise ValueError('Original per-case checkpoint differs')
        if log[2*index]!={'event':'fixture_batch_start',**name,'command':call['command']}:
            raise ValueError('Original CLI start differs')
        if log[2*index+1]!={'event':'fixture_batch_complete',**scalar}:
            raise ValueError('Original CLI completion differs')
        data=Path(call['input']['path']).read_bytes();inputs.append(data)
        token,counts=audit_input(data,call,capsule)
        output=Path(call['output']['path']).read_bytes()
        audit=audit_output(output,token,old,row['outputs'],row['comparisons'])
        cases.append(dict(call=call,checkpoint=scalar['checkpoint'],input_bytes=len(data),
            output_bytes=len(output),actual_three_stage_counts=counts,binary_identity=audit))
    if len(inputs[0])!=len(inputs[1]) or inputs[0][:44]+inputs[0][116:]!=inputs[1][:44]+inputs[1][116:]:
        raise ValueError('The two complete inputs differ outside the declared token/floor region')
    different=[j for j,(x,y) in enumerate(zip(*inputs,strict=True)) if x!=y]
    result=dict(scope=__doc__,source=ref(__file__),command=sys.argv,plan=ref(a.plan),
        summary=ref(a.summary),raw=summary['raw'],resource=ref(a.resource),log=ref(a.log),
        files=plan['files'],build_record=summary['build_record'],library=summary['library'],
        batch_executable=summary['batch_executable'],cases=cases,
        checked_path_references=len(seen),completed_CLI_processes=2,completed_native_stages=6,
        independently_verified_state_values=252,independently_verified_tangent_values=10080,
        all_complete_state_tangent_and_root_aggregate_identities=True,
        all_frozen_input_coefficients_trig_states_and_real_grid_fields_identical=True,
        input_difference=dict(total_changed_bytes=len(different),
            changed_token_bytes=sum(44<=j<108 for j in different),
            changed_floor_bytes=sum(108<=j<116 for j in different),
            changed_outside_declared_region=0,
            interpretation='Only these allowed regions differ; this does not say all72 bytes changed.'),
        execution=dict(observer_session=20894,child_returncode=0,
            observed_utc=resource['observed_utc'],observer_seconds=resource['seconds']),
        no_new_flow_or_Jacobian_in_collector=True,whole_tail_or_DN_invoked=False,
        production_Node_hook_installed=False,
        scope_limit='This original-three-stage identity verifies the new compiled binary/configuration/fieldwise interface at floor.1 and.05. It does not equate the different gates for arbitrary states, establish all physical cusp grids, or accept a full tail.')
    with a.out.open('x') as stream:
        json.dump(result,stream,indent=2,ensure_ascii=False,allow_nan=False);stream.write('\n')
    print(json.dumps(dict(record=ref(a.out),input_difference=result['input_difference'],
        input_bytes=[c['input_bytes'] for c in cases],output_bytes=[c['output_bytes'] for c in cases])),flush=True)


if __name__=='__main__':
    main()
