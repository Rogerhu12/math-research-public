#!/usr/bin/env python3
"""Low-residency continuation of the already certified width-five Miller DAG.

This does not replace or relabel the original generator.  Its SHA and the
exact starting checkpoint are appended as continuation provenance.  Cached
points are decoded before the large model is built, and their JSON is freed.
The original plan, RNG, chart, section degrees and all function nodes persist.
"""
import argparse
import ctypes
import gc
import gzip
import hashlib
import json
from pathlib import Path
import random
import resource
import sys
import time


def read(path):
    raw=path.read_bytes()
    return json.loads(gzip.decompress(raw) if path.suffix=='.gz' else raw),hashlib.sha256(raw).hexdigest()


def release(label):
    gc.collect()
    try:ctypes.CDLL(None).malloc_trim(0)
    except AttributeError:pass
    status=Path('/proc/self/status').read_text().splitlines()
    print(label,'; '.join(x for x in status if x.startswith(('VmRSS:','VmHWM:'))),flush=True)


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--script-dir',type=Path,required=True)
    parser.add_argument('--initial',type=Path,default=Path('/tmp/p41_translation_build47_complete.json.gz'))
    parser.add_argument('--checkpoint',type=Path,default=Path('/tmp/p41_translation_window47_rolling.json.gz'))
    parser.add_argument('--precomputation',type=Path,default=Path('/tmp/p41_translation_window47_precomputation.json.gz'))
    parser.add_argument('--original-driver',type=Path,default=Path('/tmp/p41_translation_window_slp47.py'))
    parser.add_argument('--max-nodes',type=int,default=369)
    args=parser.parse_args();folder=args.script_dir.resolve()
    sys.path.insert(0,str(folder));sys.path.insert(0,str(Path(__file__).parent))
    import p41_r2_matrix as r
    from p41_formal47_multiply import write_checkpoint,restore_tuple,point_hash,zero_test_mod47
    from p41_translation_window_slp47 import make_plan,independently_expand,digest
    from p41_group_operations47 import load_sources,make_model,flip
    from p41_poincare_miller47 import addflip_with_section
    from p41_translation_build47 import prepare_chart,TARGET
    started=time.monotonic();continuation_sha=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    original_sha=hashlib.sha256(args.original_driver.read_bytes()).hexdigest()
    assert Path(make_plan.__code__.co_filename).resolve()==args.original_driver.resolve()
    data,starting_sha=read(args.checkpoint)
    multiplier=data['target_multiplier'];current_node=data['current_node']
    assert 17<=current_node<=369 and data['generating_source_sha256']==original_sha
    digits,plan,precount,final_node=make_plan(multiplier)
    assert independently_expand(plan,multiplier)==data['integer_counts']
    assert data['plan']==plan and data['signed_digits_ascending']==digits
    assert data['plan_sha256']==digest(plan) and len(data['nodes'])==current_node
    assert data['current_exponent']==plan[current_node-1]['exponent']
    for expected,node in zip(plan,data['nodes']):
        assert all(node[k]==v for k,v in expected.items())
        assert digest(node['principal_section_coefficients'])==node['principal_coefficient_sha256']
    original_current=r.from_json(data.pop('point_coordinates'))
    current_A=r.from_json(data.pop('point_frobenius'))
    assert point_hash(original_current,current_A)==data['point_sha256']
    chart=data['working_chart'];expected_sources=data['source_sha256']
    rng=random.Random();rng.setstate(restore_tuple(data['random_state']))
    expected_helper=hashlib.sha256(Path(prepare_chart.__code__.co_filename).read_bytes()).hexdigest()
    assert data['chart_helper_source_sha256']==expected_helper
    published,published_sha=read(folder/'data/p41_formal47_multiplication_saved.json.gz')
    assert published['target_multiplier']==multiplier and published['source_sha256']==expected_sources
    assert data['published_multiplier_sha256']==published_sha
    del published
    initial,initial_sha=read(args.initial)
    assert initial_sha==data['initial_source_sha256']
    assert initial['source_sha256']==expected_sources and initial['current_expression']==TARGET
    assert len(initial['steps'])==24 and initial['status'].startswith('complete actual integral point 3*D_b')
    assert initial['working_chart']==chart and initial['point_sha256']==data['initial_point_sha256']
    del initial
    release('WINDOW FINISH VALIDATED PREFIX')
    # Only cache points actually used by the remaining fixed DAG.
    needed={int(op[k]) for op in plan[current_node:] for k in ['left','right'] if k in op and op[k]<=precount}
    precomputed,pre_sha=read(args.precomputation)
    assert pre_sha==data['precomputation_sha256']
    for key in ['source_sha256','initial_source_sha256','initial_point_sha256','generating_source_sha256','plan_sha256','working_chart']:
        assert precomputed[key]==data[key]
    assert precomputed['nodes']==data['nodes'][:precount]
    cache={}
    for number in sorted(needed):
        rec=precomputed['points'].pop(str(number))
        old,action=r.from_json(rec['point_coordinates']),r.from_json(rec['point_frobenius'])
        assert point_hash(old,action)==rec['point_sha256']
        cache[number]=(old,action)
        del rec
    del precomputed
    release('WINDOW FINISH DECODED ONLY '+str(len(cache))+' REQUIRED CACHE POINTS')
    sources,hashes=load_sources(folder/'data');assert hashes==expected_sources
    M0=make_model(sources);del sources
    release('WINDOW FINISH MODEL JSON RELEASED')
    original_A2,original_A3=M0['A2'],M0['A3']
    M,C2,C2i,C3=prepare_chart(M0,chart,r)
    del M0
    # No later operation uses the original CM point or its large evaluation matrix.
    for key in ['B','WB','AB']:M.pop(key,None)
    current_K=r.mm(C2i,original_current)
    assert r.equal(r.mm(original_A2,r.conjugate(original_current)),r.mm(original_current,current_A))
    del original_current
    for number in sorted(cache):
        old,action=cache[number]
        assert r.equal(r.mm(original_A2,r.conjugate(old)),r.mm(old,action))
        cache[number]=(r.mm(C2i,old),action)
    if cache:del old,action
    data.setdefault('continuations',[]).append({'source_sha256':continuation_sha,'original_driver_sha256':original_sha,
       'starting_node':current_node,'starting_checkpoint_sha256':starting_sha,
       'cached_node_indices':sorted(cache),'provenance':'low-residency loading only; same exact DAG, RNG, chart and arithmetic functions'})
    release('ACTUAL LOW-RESIDENCY WINDOW RESUME '+str(current_node))

    def checkpoint(message):
        original=r.mm(C2,current_K)
        data['point_coordinates']=r.to_json(original);data['point_frobenius']=r.to_json(current_A)
        data['point_sha256']=point_hash(original,current_A);data['current_node']=current_node
        data['current_exponent']=plan[current_node-1]['exponent']
        data['actual_sign']=1 if data['current_exponent']>0 else -1
        nxt=plan[current_node] if current_node<len(plan) else None
        data['window_cursor']=None if nxt is None else {k:nxt[k] for k in ['node','phase','remaining_power','operation']}
        data['random_state']=rng.getstate()
        sha,size=write_checkpoint(args.checkpoint,data)
        print(message,current_node,'nodes','bytes',size,'sha',sha,'seconds',round(time.monotonic()-started,2),
              'peak_MiB',round(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1024,2),flush=True)
        data.pop('point_coordinates');data.pop('point_frobenius')

    def point(number):
        if number in cache:return cache[number]
        assert number==current_node
        return current_K,current_A

    for item in plan[current_node:min(len(plan),args.max_nodes)]:
        KP,AP=point(item['left'])
        if item['operation']=='flip':
            out_K,out_A,details=flip(r.mm(M['V2'],KP),AP,M,rng,'common finish flip '+str(item['node']))
            original_section=r.mm(C2,r.mm(KP,r.column(details['f_coefficients'])))
            degree=2;record={k:v for k,v in details.items() if k not in ['kernel_block','frobenius_matrix']}
            record['reconstructible_kernel_block_sha256']=digest(details['kernel_block']);del details
        else:
            KQ,AQ=point(item['right'])
            out_K,out_A,section,record=addflip_with_section(KP,AP,KQ,AQ,M,rng,
                'common finish '+item['operation']+' '+str(item['node']),r,same=item['operation']=='double')
            original_section=r.mm(C3,section);degree=3
        assert r.equal(r.mm(original_A2 if degree==2 else original_A3,r.conjugate(original_section)),original_section)
        encoded=r.to_json(original_section);record.update(item)
        record.update({'principal_section_degree':degree,'principal_section_coefficients':encoded,
            'principal_coefficient_sha256':digest(encoded),'point_sha256':point_hash(r.mm(C2,out_K),out_A),
            'continuation_source_sha256':continuation_sha})
        data['nodes'].append(record);current_node,current_K,current_A=item['node'],out_K,out_A
        checkpoint('ACTUAL COMMON WINDOW CONTINUATION CHECKPOINT')
    if current_node==final_node:
        assert data['current_exponent']==multiplier and len(data['nodes'])==369
        data['zero_test_mod47_in_working_chart']=zero_test_mod47(current_K,M)
        data['status']='complete actual m*(3D_b) point and full width5 signed-window DAG; all360 AddFlip and9 flip nodes retained; zero reduction PASS; true formal endpoint and height evaluation remain'
        checkpoint('ACTUAL COMMON WINDOW CONTINUATION COMPLETE')


if __name__=='__main__':main()
