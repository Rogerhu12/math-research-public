#!/usr/bin/env python3
"""Check the proposed 2x2 background blocks against the unchanged native J.

Five original frozen stages retain every coefficient/grid byte and have their
complete initial state set to literal zero solely to check the background
preconditioner algebra. These are explicit zero-background test inputs, not
accepted nonlinear tail data or an attempt to reduce the original problem.
"""
import argparse
import hashlib
import json
from pathlib import Path
import struct
import subprocess
import time

import numpy as np

from tail_full_state_tangent_predictor import load, ref, module


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--repo',type=Path,required=True)
    p.add_argument('--predictor-summary',type=Path,required=True)
    p.add_argument('--preconditioner-dir',type=Path,required=True)
    p.add_argument('--outdir',type=Path,required=True)
    a=p.parse_args();out=a.outdir.resolve();out.mkdir(parents=True,exist_ok=False)
    predictor=load(a.predictor_summary)
    record=load(predictor['actual_fresh_native_record']['path'])
    manifest=load(record['manifest']['path'])
    for item in (predictor['actual_fresh_native_record'],record['input'],record['manifest'],
                 manifest['native_files']['executable']):
        if ref(item['path'])!=item:
            raise ValueError('Actual source/input/native reference changed')
    bg=load(predictor['original_scaling']['path'])
    helper=module('_background_zero_wire',a.repo/'topics/visible-flex-held-10pct/scripts/resume_n4_tail/native_extended/parallel_native_batch.py')
    wire=Path(record['input']['path']).read_bytes();shape=helper.split_wire(wire)
    M,K=shape['modes'],2*shape['modes'];indices=[0,22,80,813,shape['count']-1]
    header=bytearray(shape['header']);struct.pack_into('<i',header,36,len(indices));header[44:108]=b'0'*64
    chunks=[]
    for n in indices:
        start,end=shape['spans'][n];body=bytearray(wire[start:end]);body[8:8+8*(K+2)]=bytes(8*(K+2));chunks.append(body)
    body=b''.join(chunks);header[44:108]=hashlib.sha256(header+body).hexdigest().encode('ascii')
    inp,op=out/'zero-background-input.bin',out/'zero-background-output.bin'
    inp.write_bytes(header+body)
    before=time.monotonic()
    run=subprocess.run([manifest['native_files']['executable']['path'],str(inp),str(op)],capture_output=True)
    (out/'native.stdout').write_bytes(run.stdout);(out/'native.stderr').write_bytes(run.stderr)
    if run.returncode!=0:
        raise RuntimeError('Original native zero-background probe failed: '+run.stderr.decode())
    duration=time.monotonic()-before
    zero_shape=helper.split_wire(inp.read_bytes());data=op.read_bytes()
    blocks,failed=helper.output_records(data,zero_shape,len(indices),zero_shape['token'],run.returncode)
    with np.load(a.preconditioner_dir/'unaccepted-gmres-predictor.npz',allow_pickle=False) as saved:
        transfers=saved['background_transfers'].copy()
    rows=[]
    for local,(start,end,status) in enumerate(blocks):
        n=indices[local];offset=start+8+8*(K+2)
        tangent=np.frombuffer(data,dtype='<f8',count=(K+2)*K,offset=offset).reshape(K+2,K).copy()
        tangent[M:K,:]/=bg['portRatios'][n]
        expected=np.zeros((K+2,K))
        for j in range(M):
            ix=[j,M+j];expected[np.ix_(ix,ix)]=transfers[n,j]
        diff=np.abs(tangent-expected)
        rows.append(dict(stage=n,maximum_absolute_difference=float(diff.max()),
            maximum_scale_normalized_difference=float(np.max(diff/np.maximum(1.,np.abs(tangent)))),
            maximum_original_entry=float(np.max(np.abs(tangent)))))
    report=dict(scope=__doc__,source=ref(__file__),predictor_summary=ref(a.predictor_summary),
        actual_native_record=predictor['actual_fresh_native_record'],
        preconditioner_summary=ref(a.preconditioner_dir/'summary.json'),
        native_executable=manifest['native_files']['executable'],input=ref(inp),output=ref(op),
        selected_stages=indices,original_grid_and_coefficients_retained=True,
        explicit_zero_state_probe=True,wall_seconds=duration,rows=rows,
        maximum_scale_normalized_difference=max(r['maximum_scale_normalized_difference'] for r in rows),
        nonlinear_tail_accepted=False)
    (out/'summary.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2))


if __name__=='__main__':
    main()
