#!/usr/bin/env python3
"""Recover exact original tail knots in a small window from a checked suffix.

Only the last required known blobs are read. Actual radii are reconstructed
backwards from the exact cut with the same normalized increments, never from
displayed cumulative-radius columns. The later main full-tail stream still
checks the complete normalization and all source identities.
"""
from __future__ import annotations
import argparse,gzip,hashlib,importlib.util,json,os,time
from fractions import Fraction as Q
from pathlib import Path
import numpy as np

MANIFEST_SHA='cc23977e25a09c34db91723dd784cab4b18b89e325fc2ca2fb8dd7ee6866a104'
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def load(name,p):
    spec=importlib.util.spec_from_file_location(name,p)
    m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);return m

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--scripts',type=Path,required=True)
    ap.add_argument('--manifest',type=Path,required=True);ap.add_argument('--out',type=Path,required=True)
    ap.add_argument('--window',nargs=2,default=['.432','.436'])
    ap.add_argument('--source-transport',choices=('git-blob-api','raw-known-commit'),default='git-blob-api')
    args=ap.parse_args()
    if args.out.exists():raise FileExistsError('Fresh local source-knot recipe required')
    if sha(args.manifest)!=MANIFEST_SHA:raise ValueError('Wrong original manifest')
    meta=json.loads(args.manifest.read_text());rg=meta['radialGeometry']
    low,high=map(Q,args.window);inner,outer=Q(rg['innerAnchor']),Q(rg['outerAnchor'])
    if not inner<low<high<outer:raise ValueError('Local knot window must be inside the finite original tail')
    scale=Q(int(rg['normalization']['numerator']),int(rg['normalization']['denominator']))
    producer_path=args.scripts/'6a65-m12-stream-tail-exact-endpoint.py'
    consumer_path=args.scripts/'6a65-m12-stream-tail-query-and-source-bounds-recovered.py'
    producer=load('suffix_original_blob_table',producer_path)
    consumer=load('suffix_checked_payload_reader',consumer_path)
    offsets=[];count=0
    for info in meta['files']:offsets.append(count);count+=info['rows']-1
    if count!=18552 or count!=rg['spanCount']:raise ValueError('Original source span count changed')
    headers={'User-Agent':'M12-original-tail-local-knot-suffix','Accept':'application/vnd.github+json'}
    token=os.environ.get('M12_RECOVERY_TOKEN')
    if token:headers['Authorization']='Bearer '+token
    right=outer;previous=None;selected={};lower_neighbor=None;upper_neighbor=None;receipts=[]
    began=time.monotonic()
    for file_index in range(len(meta['files'])-1,-1,-1):
        info=meta['files'][file_index];name=Path(info['path']).name
        key=name.split('-raw')[1].split('.f64')[0].replace('-part','-')
        blob=producer.BLOBS[key]
        raw=consumer.recover_payload(producer,blob,info,args.source_transport,headers)
        a=np.frombuffer(gzip.decompress(raw),dtype='<f8').reshape(info['rows'],info['columns'])
        if previous is not None and not np.array_equal(a[-1],previous):
            raise ValueError('Exact suffix shared rows changed')
        lengths=[Q.from_float(float(v)) for v in a[1:,-1]]
        if min(lengths)<=0:raise ValueError('Nonpositive original source increment')
        reverse_nodes=[right]
        for ell in reversed(lengths):reverse_nodes.append(reverse_nodes[-1]-scale*ell)
        nodes=list(reversed(reverse_nodes))
        for j,r in enumerate(nodes):
            node_index=offsets[file_index]+j
            if low<=r<=high:selected[node_index]=r
            elif r<low and (lower_neighbor is None or r>lower_neighbor[1]):
                lower_neighbor=(node_index,r)
            elif r>high and (upper_neighbor is None or r<upper_neighbor[1]):
                upper_neighbor=(node_index,r)
        receipts.append({'file':name,'git_blob':blob,'sha256':info['sha256'],'bytes':len(raw),
                         'source_span_offset':offsets[file_index],'spans':len(lengths),
                         'left_exact':str(nodes[0]),'right_exact':str(nodes[-1])})
        right=nodes[0];previous=a[0].copy()
        if right<low:break
    if right>=low or lower_neighbor is None or upper_neighbor is None:
        raise ArithmeticError('Exact suffix does not cover the requested window')
    for i,r in (lower_neighbor,upper_neighbor):selected[i]=r
    indices=sorted(selected)
    if any(b!=a+1 for a,b in zip(indices,indices[1:])):raise ArithmeticError('Source knot window has a gap')
    output={'schema':'6a65-original-M12-local-source-knot-suffix-v1','script_sha256':sha(__file__),
            'manifest_sha256':MANIFEST_SHA,'endpoint_blob_table_sha256':sha(producer_path),
            'checked_payload_reader_sha256':sha(consumer_path),'source_transport':args.source_transport,
            'window_exact':[str(low),str(high)],'normalization_exact':str(scale),
            'source_node_indices':indices,'radius_fraction':[str(selected[i]) for i in indices],
            'source_blocks':receipts,'blocks_read':len(receipts),
            'bytes_read':sum(r['bytes'] for r in receipts),
            'exact_cut_backward_increment_arithmetic':True,
            'requires_complete_normalization_check_by_main_stream':True,
            'temporary_preparation_parameter_not_new_source':True,'seconds':time.monotonic()-began}
    args.out.write_text(json.dumps(output,indent=2)+'\n')
    print(json.dumps({k:output[k] for k in ('schema','blocks_read','bytes_read','window_exact','seconds')} |
                     {'nodes':len(indices),'recipe_sha256':sha(args.out)},indent=2))
if __name__=='__main__':main()

