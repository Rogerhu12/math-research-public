#!/usr/bin/env python3
"""Compare a smaller actual radial batch with complete recorded old outputs.

The old, individually input-bound cache entry is a comparison reference only.
No old cache item is relabelled for a different batching identity. The original
actual augmented callbacks compute every new value; no Newton or tail runs.
"""
from __future__ import annotations
import argparse
import gzip
import hashlib
import importlib.util
import json
from pathlib import Path
import struct
import sys

HERE=Path(__file__).resolve().parent
SELF_SHA=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()


def read_call(path,cache):
    data=path.read_bytes();payload=gzip.decompress(data);offset=len(cache.MAGIC)
    if not payload.startswith(cache.MAGIC):raise ValueError('Old call magic differs')
    size=struct.unpack('<Q',payload[offset:offset+8])[0];offset+=8
    record=json.loads(payload[offset:offset+size]);offset+=size
    if cache.sha(cache.canonical(record['request']))!=record['key'] or path.stem[:-4]!=record['key']:
        raise ValueError('Old complete call key mismatch')
    inputs={};outputs=[]
    for collection in ('inputs','outputs'):
        for item in record[collection]:
            n=item['array']['bytes'];value=cache.restore_array(item['array'],payload[offset:offset+n]);offset+=n
            if collection=='inputs':inputs[item['name']]=value
            else:outputs.append(value)
    if offset!=len(payload):raise ValueError('Old call trailing bytes')
    return record,inputs,tuple(outputs) if record['tuple_output'] else outputs[0],hashlib.sha256(data).hexdigest()


def main():
    parser=argparse.ArgumentParser(add_help=False,description=__doc__)
    parser.add_argument('--reference-jacobian-entry',type=Path,required=True)
    parser.add_argument('--reference-RHS-entry',type=Path,required=True)
    own,remaining=parser.parse_known_args()
    import strong_prefix_evaluation_cache as cache
    original_inspect=cache.Runtime.inspect
    sources={str(path):hashlib.sha256(path.read_bytes()).hexdigest() for path in
        (Path(__file__),HERE/'strong_prefix_evaluation_cache.py',HERE/'strong_cached_prefix_actual_bvp.py')}
    def inspect(runtime,obj,x,y,p):
        import numpy as np
        checks={};comparisons=[]
        for name,path in (('fun_jac',own.reference_jacobian_entry),('fun',own.reference_RHS_entry)):
            record,values,expected,file_sha=read_call(path,cache)
            if record['request']['operation']!=name or record['request']['object']!=runtime.object_identity(obj):
                raise ValueError('Recorded physical/chart/target identity differs')
            identity_path=path.parent/'identity.json';identity=json.loads(identity_path.read_text())
            if cache.sha(cache.canonical(identity))!=record['request']['identity_sha256']:
                raise ValueError('Original source/runtime identity changed')
            for file,digest in identity['source']['files'].items():
                if hashlib.sha256(Path(file).read_bytes()).hexdigest()!=digest:
                    raise ValueError('An original computation source/input changed: '+file)
            actual=runtime.originals[name](obj,values['t'],values['y'],values['p'])
            before=expected if isinstance(expected,tuple) else (expected,)
            after=actual if isinstance(actual,tuple) else (actual,)
            equal=len(before)==len(after) and all(cache.describe(a)==cache.describe(b) for a,b in zip(before,after))
            checks[name+'_complete_bytes_and_layout_equal']=equal
            checks[name+'_complete_selected_parameters_restored']=np.array_equal(obj.controls,values['p'])
            comparisons.append(dict(operation=name,reference_file=str(path),reference_sha256=file_sha,
                original_batch_sizes=identity['batch_sizes'],new_batch_sizes=runtime.batch_sizes,
                input_shapes={k:list(v.shape) for k,v in values.items()},complete_outputs=len(after),
                output_descriptors=[cache.describe(v) for v in after],
                max_absolute_difference=[float(np.max(np.abs(a-b))) for a,b in zip(before,after)],
                reference_source_and_complete_input_guards_passed=True))
        obj.select(p);obj.flow()
        result=dict(scope=__doc__,finished=True,passed=all(checks.values()),checks=checks,
            comparisons=comparisons,source_sha256=sources,old_cache_not_relabelled_or_used_as_result=True,
            original_physical_and_angular_equations_unchanged=True,Node_processes=0,Newton_steps=0,new_solution=False)
        path=Path(runtime.configuration['inspect_output'])
        cache.atomic_new(path,json.dumps(result,indent=2,allow_nan=False).encode()+b'\n')
        print(json.dumps(dict(event='actual_prefix_smaller_batch_checked',passed=result['passed'],path=str(path))),flush=True)
        if not result['passed']:raise ValueError('Actual complete smaller-batch check failed')
        raise cache.InspectionComplete()
    cache.Runtime.inspect=inspect
    spec=importlib.util.spec_from_file_location('strong_prefix_batch_original_entry',HERE/'strong_cached_prefix_actual_bvp.py')
    entry=importlib.util.module_from_spec(spec);spec.loader.exec_module(entry)
    old=sys.argv;sys.argv=[old[0],*remaining]
    try:entry.main()
    finally:sys.argv=old;cache.Runtime.inspect=original_inspect


if __name__=='__main__':main()
