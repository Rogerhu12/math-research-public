#!/usr/bin/env python3
"""Read completed native batch files; never construct or evaluate a model.

The native input contains states[1..depth], not node0. Therefore only residual
rows n>=1 are reconstructible here. Their maximum is a lower bound on the
original complete norm, not a replacement for node0/left/far-Robin tests.
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
def verify(item):
    if ref(item['path'])!=item:raise ValueError('Changed saved file '+item['path'])
def load(p):
    p=Path(p)
    return json.loads(gzip.decompress(p.read_bytes()) if p.suffix=='.gz' else p.read_bytes())


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--batch-records',type=Path,nargs='+',required=True)
    parser.add_argument('--complete-entry-summary',type=Path,required=True)
    parser.add_argument('--out',type=Path,required=True)
    a=parser.parse_args()
    entry=load(a.complete_entry_summary);verify(entry['raw'])
    prior=load(entry['raw']['path']);scales=np.asarray(prior['scales'],dtype=float)
    results=[]
    for record_path in a.batch_records:
        record=load(record_path)
        if record['status']!='complete' or record['returncode']!=0:
            raise ValueError('Only genuinely complete native batches are supported')
        for key in ['input','output','static_metadata','manifest']:verify(record[key])
        meta=load(record['static_metadata']['path'])
        if meta['scope']!={'M':20,'spacing':4,'quadrature':512,'steps':16,'projectionFloor':.05,
                          'orientation':1,'cuspAwareFlow':True,'stageCount':2304}:
            raise ValueError('Wrong current complete finite scope')
        incoming=Path(record['input']['path']).read_bytes();outgoing=Path(record['output']['path']).read_bytes()
        if incoming[:8]!=b'VFN4LD01' or outgoing[:8]!=b'VFN4OUT1':raise ValueError('Wrong protocol')
        header=struct.unpack_from('<9i',incoming,8);M=header[1];depth=header[7];withJac=header[8]
        if header[:7]!=(1,20,512,4,128,30,20) or depth!=2304 or withJac not in (0,1):raise ValueError('Wrong header')
        if struct.unpack_from('<4i',outgoing,8)!=(1,M,depth,withJac):raise ValueError('Output dimensions differ')
        token=hashlib.sha256(incoming[:44]+incoming[108:]).hexdigest()
        if incoming[44:108].decode()!=token or outgoing[24:88].decode()!=token:raise ValueError('Token differs')
        # The bound complete entry and native static template share the same
        # target and gain-defined scales. Require every static byte to match.
        template=Path(meta['template']['path']).read_bytes();verify(meta['template'])
        base=Path(load(entry['static_metadata']['path'])['template']['path']).read_bytes()
        if template!=base:raise ValueError('Original fixed static problem changed')
        state_inputs=[]
        for row in meta['stages']:
            state_inputs.append(np.frombuffer(incoming,dtype='<f8',count=40,offset=row['initialOffset']).copy())
        offset=88;dominant=None;above_gate=0;rows_compared=0;minA=float('inf');minD=float('inf')
        for n in range(depth):
            if struct.unpack_from('<2i',outgoing,offset)!=(n,0):raise ValueError('Wrong output stage status')
            offset+=8;values=np.frombuffer(outgoing,dtype='<f8',count=42,offset=offset).copy();offset+=336
            if withJac:offset+=13440
            counters=struct.unpack_from('<3Q',outgoing,offset);offset+=24
            diag=struct.unpack_from('<5d',outgoing,offset);offset+=40
            if counters[0]!=4*meta['stages'][n]['nsteps']:raise ValueError('Wrong original RK/root count')
            minA=min(minA,diag[0]);minD=min(minD,diag[1])
            if n==0:continue
            physical=values[:40].copy();physical[20:]/=meta['stages'][n]['portRatio']
            current=state_inputs[n-1];residual=physical-current;normalized=np.abs(residual)/scales[n]
            j=int(np.argmax(normalized));value=float(normalized[j]);rows_compared+=40
            above_gate+=int(np.count_nonzero(normalized>=2e-9))
            if dominant is None or value>dominant['normalized']:
                dominant=dict(stage=n,component=j,physicalMode=4*(j%20+1),kind='Q' if j<20 else 'pi',
                    normalized=value,difference=float(residual[j]),flow=float(physical[j]),
                    node=float(current[j]),scale=float(scales[n]),minA=diag[0],minD=diag[1])
        if offset!=len(outgoing):raise ValueError('Output EOF differs')
        results.append(dict(record=ref(record_path),input=record['input'],output=record['output'],
            static_metadata=record['static_metadata'],withJac=bool(withJac),call=record['call'],
            internal_component_rows=rows_compared,internal_components_at_or_above_original_gate=above_gate,
            dominantInternalResidual=dominant,minA=minA,minD=minD,
            complete_original_norm_known=False,node0_or_far_Robin_reconstructed=False))
    result=dict(scope=__doc__,source=ref(__file__),command=sys.argv,
        complete_entry_summary=ref(a.complete_entry_summary),complete_entry_raw=entry['raw'],
        results=results,new_flow_or_derivative=False,new_state_candidate=False,
        scope_limit='Only saved internal rows, with original binary64 conversion/subtraction/scales. No full original norm or lower bound on achievable mathematical/numerical error is claimed.')
    with a.out.open('x') as stream:
        json.dump(result,stream,indent=2,ensure_ascii=False,allow_nan=False);stream.write('\n')
    print(json.dumps(dict(output=ref(a.out),results=[dict(call=r['call'],dominant=r['dominantInternalResidual'],
        above=r['internal_components_at_or_above_original_gate']) for r in results])),flush=True)


if __name__=='__main__':main()
