#!/usr/bin/env python3
"""Regroup an existing complete actual-tail metric certificate by exact radius.

No metric inequality is recomputed or tightened. Every reused row is kept
with its original bound, and any row touching the requested inner radial
domain is included in that domain's maximum. Exact defining increments,
not displayed absolute radii, determine which rows touch each domain.
"""
from __future__ import annotations
import argparse
from fractions import Fraction as Q
import gzip
import hashlib
import io
import json
from pathlib import Path
import time
import numpy as np


def ident(p):
    p=Path(p).resolve();b=p.read_bytes()
    return dict(file=str(p),bytes=len(b),sha256=hashlib.sha256(b).hexdigest())


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--manifest',type=Path,required=True);p.add_argument('--certificate',type=Path,required=True)
    p.add_argument('--packet',type=Path,required=True);p.add_argument('--out',type=Path,required=True)
    p.add_argument('--cuts',default='.16,.17,.18,.2,.25,.3,.35,.4,.45,.5,.55,outer')
    a=p.parse_args();start=time.monotonic()
    if a.out.exists():raise FileExistsError('Use a new report')
    manifest=json.loads(a.manifest.read_text());cert=json.loads(a.certificate.read_text());packet=json.loads(a.packet.read_text())
    mh=ident(a.manifest)['sha256']
    if packet['finite_tail_manifest_sha256']!=mh:raise ValueError('Wrong packet manifest')
    if cert['packet_sha256']!=ident(a.packet)['sha256']:raise ValueError('Wrong existing metric packet')
    rowpath=a.certificate.parent/cert['row_data_file'];rowid=ident(rowpath)
    if rowid['sha256']!=cert['row_data_sha256']:raise ValueError('Changed original metric rows')
    rows=json.loads(gzip.decompress(rowpath.read_bytes()))
    dpath=a.packet.parent/packet['data_file'];dataid=ident(dpath)
    if dataid['sha256']!=packet['data_sha256']:raise ValueError('Changed original background packet')
    with np.load(io.BytesIO(gzip.decompress(dpath.read_bytes())),allow_pickle=False) as raw:
        span=raw['span_index'].copy();left=raw['u_left'].copy();right=raw['u_right'].copy()
    increments=[];display=[];lastrow=None
    for f in manifest['files']:
        path=Path(f['path'])
        if not path.exists():path=a.manifest.parent/path.name
        payload=path.read_bytes()
        if hashlib.sha256(payload).hexdigest()!=f['sha256']:raise ValueError('Changed tail defining shard')
        block=np.frombuffer(gzip.decompress(payload),dtype='<f8').reshape(f['rows'],f['columns'])
        if lastrow is not None and not np.array_equal(block[0],lastrow):raise ValueError('Tail boundary rows differ')
        begin=0 if lastrow is None else 1
        display.extend(block[begin:,0].tolist());increments.extend(block[begin:,-1].tolist())
        lastrow=block[-1].copy()
    if 'radialGeometry' in manifest:
        m=manifest['radialGeometry'];beta=Q(int(m['normalization']['numerator']),int(m['normalization']['denominator']))
        rq=[Q(float(m['innerAnchor']))]
        for length in increments[1:]:rq.append(rq[-1]+beta*Q(length))
        if rq[-1]!=Q(float(m['outerAnchor'])):raise ValueError('Exact increments miss outer anchor')
    else:rq=list(map(Q,display))
    cuff=Q(float(manifest['parameters']['rCuff']));cuts=[rq[-1] if s.strip()=='outer' else Q(s.strip()) for s in a.cuts.split(',')]
    if any(c<=cuff or c>rq[-1] for c in cuts):raise ValueError('Cut outside the represented domain')
    if len(rows)!=len(span):raise ValueError('Row coverage changed')
    selected=[dict(cut_exact=str(c),metric_upper=0.,included_rows=0) for c in cuts]
    previous_span=-1;previous_right=Q(0)
    for j,row in enumerate(rows):
        i=int(span[j]);l,r=Q(float(left[j])),Q(float(right[j]))
        if row['packet_row']!=j or row['span_index']!=i:raise ValueError('Row index binding changed')
        if not 0<=l<r<=1:raise ValueError('Invalid local row')
        if i==previous_span:
            if l!=previous_right:raise ValueError('Coverage gap within span')
        elif i==previous_span+1:
            if previous_right!=1 or l!=0:raise ValueError('Coverage gap across spans')
        else:raise ValueError('Missing span')
        origin=cuff if i==-1 else rq[i];length=rq[0]-cuff if i==-1 else rq[i+1]-rq[i]
        lo,hi=origin+length*l,origin+length*r
        for cut,result in zip(cuts,selected):
            if lo<=cut:
                result['included_rows']+=1
                bound=float(row['metric_operator_upper'])
                if bound>result['metric_upper']:
                    result.update(metric_upper=bound,worst_packet_row=j,worst_span=i,
                                  worst_row_r_left_exact=str(lo),worst_row_r_right_exact=str(hi))
        previous_span=i;previous_right=r
    if previous_span!=len(rq)-2 or previous_right!=1:raise ValueError('Incomplete outer coverage')
    report=dict(schema='fd2d-existing-tail-metric-regions-v1',scope=__doc__,script=ident(__file__),
        manifest=ident(a.manifest),certificate=ident(a.certificate),packet=ident(a.packet),packet_data=dataid,
        original_row_data=rowid,whole_tail_row_count=len(rows),exact_partition_verified=True,
        cuff_exact=str(cuff),outer_exact=str(rq[-1]),inner_domains=selected,
        new_map_created=False,new_metric_estimate_computed=False,seconds=time.monotonic()-start)
    a.out.write_text(json.dumps(report,indent=2,allow_nan=False)+'\n')
    print(json.dumps(dict(out=str(a.out),inner_domains=[dict(cut=x['cut_exact'],bound=x['metric_upper']) for x in selected],
                         seconds=report['seconds'])),flush=True)


if __name__=='__main__':main()
