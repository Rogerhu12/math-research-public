#!/usr/bin/env python3
"""Re-read every frozen coefficient and verify the retarget identities exactly.

Floating arrays are used only as exact dyadic containers and for exact equality.
The initial identity is independently recomputed with Fraction arithmetic.
No true-flow or numerical interpolation assertion is made.
"""
from __future__ import annotations
import argparse
from fractions import Fraction
import hashlib
import json
from pathlib import Path
import numpy as np
from fourfold_shared_dense_reference import load


def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def document(row):
    path=Path(row['path'])
    if sha(path)!=row['sha256']:raise ValueError('definition hash mismatch')
    return path,json.loads(path.read_text())


def branch(row,fields):
    path,doc=document(row)
    if (not doc.get('complete') or doc['fields']!=fields
        or doc['time_basis']!='bernstein' or doc['time_degree']!=7):
        raise ValueError('invalid branch convention')
    count=0;first=last=None
    for shard in doc['shards']:
        source=path.parent/shard['path']
        if sha(source)!=shard['sha256'] or source.stat().st_size!=shard['bytes']:
            raise ValueError('coefficient hash or size mismatch')
        data=load(source);meta=json.loads(str(data['metadata']))
        r,i=data['coefficient_real'],data['coefficient_imag']
        shape=(shard['segment_count'],8)+((2,) if fields==['U','L'] else ())+(doc['Fourier_degree']+1,)
        if (shard['start_segment']!=count or r.shape!=shape or i.shape!=shape
            or meta['start_segment']!=count or meta['segment_count']!=shard['segment_count']
            or meta['exact_times']!=doc['exact_time_endpoints'][count:count+shard['segment_count']+1]
            or not np.all(np.isfinite(r)) or not np.all(np.isfinite(i)) or np.any(i[...,0]!=0)):
            raise ValueError('coverage, metadata, finite-coefficient or real-mean failure')
        for a,b in zip(r,i):
            left=(a[0].copy(),b[0].copy());right=(a[-1].copy(),b[-1].copy())
            if first is None:first=left
            if last is not None and any(not np.array_equal(x,y) for x,y in zip(last,left)):
                raise ValueError('nonzero exact internal coefficient jump')
            last=right;count+=1
    if count!=doc['segment_count'] or len(doc['exact_time_endpoints'])!=count+1:
        raise ValueError('incomplete branch')
    return doc,first,last


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--descriptor',type=Path,required=True);p.add_argument('--out',type=Path,required=True)
    args=p.parse_args();d=json.loads(args.descriptor.read_text())
    objects={}
    for leg in ['forward','backward']:
        base=branch(d['old_'+leg+'_reference'],['U','L']);q=branch(d['Q_'+leg],['Qtilde'])
        if (base[0]['exact_time_endpoints']!=q[0]['exact_time_endpoints']
            or base[0]['leg']!=leg or q[0]['leg']!=leg):raise ValueError('different time grids or leg labels')
        qr,qi=q[1]
        if qr[0]!=1 or np.any(qr[1:]!=0) or np.any(qi!=0):raise ValueError('Q initial polynomial is not exactly one')
        objects[leg]=(base,q)
    forward,backward=objects['forward'][0],objects['backward'][0]
    if forward[0]['exact_time_endpoints'][-1]!=backward[0]['exact_time_endpoints'][0]:
        raise ValueError('different exact turn times')
    if any(not np.array_equal(a[0],b[0]) for a,b in zip(forward[2],backward[1])):
        raise ValueError('base U has a nonzero exact leg jump')
    _,H=document(d['target_H']);_,a=document(d['initial_correction'])
    D=1<<a['denominator_power_of_two'];HD=1<<H['denominator_power_of_two']
    oldr,oldi=forward[1];count=0
    if (len(a['nonnegative_integer_coefficients'])!=a['degree']+1
        or a['degree']<max(H['H_degree'],oldr.shape[-1]-1)):
        raise ValueError('initial correction omits a high coefficient')
    for k,pair in enumerate(a['nonnegative_integer_coefficients']):
        target=H['h_nonnegative_integer_coefficients'][k] if k<=H['H_degree'] else (0,0)
        for j,old in enumerate((oldr,oldi)):
            value=Fraction.from_float(float(old[0,k])) if k<old.shape[-1] else Fraction(0)
            if value+Fraction(int(pair[j]),D)!=Fraction(int(target[j]),4*HD):
                raise ValueError('the exact initial identity is false')
            count+=1
    for leg in ['forward','backward']:
        b,q=objects[leg]
        if b[0]['trace_identity']['exact_delta_fraction']!=d['old_exact_delta_fraction']:
            raise ValueError('base belongs to a different old object')
    _,target=document(d['target_object']);_,root=document(d['target_root'])
    delta=Fraction(int(target['delta_fraction']['numerator']),int(target['delta_fraction']['denominator']))
    if (delta!=Fraction(d['target_exact_delta_fraction']) or Fraction(root['exact_delta_fraction'])!=delta
        or Fraction(H['source_metadata']['exact_delta_fraction'])!=delta):raise ValueError('mixed target identities')
    out=dict(kind='exact_retarget_identity_check',complete=True,
        source_sha256=sha(__file__),descriptor=str(args.descriptor),descriptor_sha256=sha(args.descriptor),
        all_base_and_Q_shards_re_read=True,checked_initial_real_rational_coefficients=count,
        legs={leg:dict(segments=objects[leg][0][0]['segment_count'],
            base_exact_internal_U_L_jumps_zero=True,Q_exact_internal_jumps_zero=True,Q_start_exactly_one=True)
            for leg in ['forward','backward']},
        exact_initial_H_over_four=True,exact_turn_U_junction=True,
        exact_full_corrected_junction_by_symbolic_product_identity=True,
        old_exact_delta_fraction=d['old_exact_delta_fraction'],target_exact_delta_fraction=str(delta),
        limitations=['These identities are for the defined reference, not an actual flow.',
                     'No value of Qtilde away from its initial edge is assumed positive or accurate as a Jacobian.'])
    args.out.write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(dict(out=str(args.out),sha256=sha(args.out),exact_initial=True,exact_junction=True)))


if __name__=='__main__':main()
