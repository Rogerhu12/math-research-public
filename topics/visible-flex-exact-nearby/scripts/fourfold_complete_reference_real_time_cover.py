#!/usr/bin/env python3
"""Resumable real-time image and q gates for all actual reference segments."""
from __future__ import annotations
import argparse
from fractions import Fraction
import gzip
import json
from pathlib import Path
import time
from flint import arb,ctx
from fourfold_phase_beta_affine import sha
from fourfold_phase_beta_bulk_interval import exact_arb
from fourfold_phase_beta_interval import ball_record
from fourfold_retarget_reference_jets import RetargetReference
from fourfold_complete_reference_segment import CompleteReferenceSegment
from fourfold_complete_reference_real_time_q import real_time_q


def document(path):
    path=Path(path);raw=path.read_bytes()
    return json.loads(gzip.decompress(raw)if path.suffix=='.gz'else raw)


def save(path,doc):
    path=Path(path);raw=(json.dumps(doc,indent=2)+'\n').encode()
    if len(raw)>1_000_000 and path.suffix!='.gz':raise ValueError('gzip required above 1MB')
    data=gzip.compress(raw,mtime=0)if path.suffix=='.gz'else raw
    if len(data)>5_000_000:raise ValueError('split a file above 5MB')
    path.parent.mkdir(parents=True,exist_ok=True)
    temp=path.with_name(path.name+'.tmp');temp.write_bytes(data);temp.replace(path)


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--descriptor',type=Path,default=Path('data/phase_ring_continuation/step5_retargeted_reference/descriptor.json'))
    p.add_argument('--leg',choices=('forward','backward'),default='forward')
    p.add_argument('--segments',default='all');p.add_argument('--label-widths',default='1/512,1/256,1/128')
    p.add_argument('--q-widths',default='1/256')
    p.add_argument('--nodes',type=int,default=512);p.add_argument('--taylor-order',type=int,default=8)
    p.add_argument('--bits',type=int,default=256);p.add_argument('--compare-physical-strip',default='1/64')
    p.add_argument('--out-directory',type=Path,required=True);p.add_argument('--index',type=Path,required=True)
    p.add_argument('--resume',action='store_true');args=p.parse_args();ctx.prec=args.bits
    start,cpu=time.monotonic(),time.process_time();ref=RetargetReference(args.descriptor)
    widths=list(map(Fraction,args.label_widths.split(',')));qwidths=list(map(Fraction,args.q_widths.split(',')))
    count=ref.base[args.leg][1]['segment_count']
    requested=list(range(count))if args.segments=='all'else list(map(int,args.segments.split(',')))
    if len(set(requested))!=len(requested)or any(not 0<=i<count for i in requested):
        raise ValueError('unique valid reference segments required')
    outer=exact_arb(Fraction(args.compare_physical_strip))
    common=dict(source_sha256=sha(__file__),
        dependency_sha256={name:sha(Path(__file__).with_name(name))for name in
            ['fourfold_complete_reference_segment.py','fourfold_complete_reference_real_time_q.py']},
        descriptor_sha256=sha(args.descriptor),leg=args.leg,
        base_reference_manifest_sha256=sha(ref.base[args.leg][0]),
        Q_reference_manifest_sha256=sha(ref.Q[args.leg][0]),
        target_object_sha256=ref.doc['target_object']['sha256'],
        target_root_sha256=ref.doc['target_root']['sha256'],
        exact_target_delta_fraction=ref.doc['target_exact_delta_fraction'],
        label_widths=list(map(str,widths)),q_label_widths=list(map(str,qwidths)),
        angular_nodes=args.nodes,taylor_order=args.taylor_order,
        bits=args.bits,comparison_physical_theta_strip=args.compare_physical_strip)
    index=dict(kind='complete_reference_real_time_image_and_q_cover',complete=False,
        **common,requested_segments=requested,cases=[],
        limitations=['Exact finite reference only; no true-flow Jacobian or approximation is inferred.',
            'A numeric image/strip comparison does not validate a true-field domain identity.',
            'Every leaf retains full Bernstein controls and continuous angular remainders.'])
    if args.resume and args.index.exists():
        index=document(args.index)
        if any(index.get(k)!=v for k,v in common.items())or index['requested_segments']!=requested:
            raise ValueError('real-time-cover resume identity/settings changed')
    done={}
    for row in index['cases']:
        path=Path(row['path'])
        if sha(path)!=row['sha256']or path.stat().st_size!=row['bytes']:
            raise ValueError('completed real-time leaf changed or is missing')
        leaf=document(path)
        if not leaf.get('complete')or any(leaf.get(k)!=v for k,v in common.items()):
            raise ValueError('completed real-time leaf has a different definition')
        if leaf['segment']!=row['segment']or len(leaf['image_gates'])!=len(widths)or len(leaf['q_gates'])!=len(qwidths):
            raise ValueError('completed real-time leaf index mismatch')
        done[row['segment']]=row
    index['complete']=False;save(args.index,index)
    for segment in requested:
        if segment in done:continue
        before=time.monotonic();model=CompleteReferenceSegment(ref,args.leg,segment)
        images=[]
        for S in widths:
            gate=model.real_time_image(S,nodes=args.nodes,p=args.taylor_order)
            value=arb(gate['physical_theta_image_strip']['upper']).upper()
            if not gate['complete_real_time_image_proved']or not value.is_finite():
                raise ValueError('the complete real-time image gate failed')
            images.append(dict(**gate,comparison_physical_theta_strip=args.compare_physical_strip,
                strictly_within_comparison_strip=bool(value<outer),
                comparison_strip_margin=ball_record((outer-value).lower())))
        qs=[real_time_q(model,S,nodes=args.nodes,p=args.taylor_order)for S in qwidths]
        leaf=dict(kind='complete_reference_real_time_image_and_q_leaf',complete=True,**common,
                  segment=segment,image_gates=images,q_gates=qs,identity=model.identity,
                  elapsed_seconds=time.monotonic()-before)
        path=args.out_directory/f'{args.leg}_{segment:04d}.json.gz';save(path,leaf)
        row=dict(segment=segment,path=str(path),sha256=sha(path),bytes=path.stat().st_size,
            physical_images={g['initial_label_strip']:g['physical_theta_image_strip']for g in images},
            q_real_lower={g['initial_label_strip']:g['full_real_time_q_real_lower']for g in qs},
            all_inside_comparison_strip=all(g['strictly_within_comparison_strip']for g in images),
            all_real_time_q_positive=all(g['q_nonzero_on_complete_real_time_label_strip_proved']for g in qs))
        index['cases'].append(row);done[segment]=row
        index['elapsed_seconds_this_process']=time.monotonic()-start
        index['cpu_seconds_this_process']=time.process_time()-cpu;save(args.index,index)
        print(json.dumps(dict(segment=segment,complete=True,
            image_bounds={g['initial_label_strip']:g['physical_theta_image_strip']['ball']for g in images},
            q_lower={g['initial_label_strip']:g['full_real_time_q_real_lower']['ball']for g in qs},
            all_inside_comparison_strip=row['all_inside_comparison_strip'],
            all_real_time_q_positive=row['all_real_time_q_positive'],
            elapsed_seconds_this_process=index['elapsed_seconds_this_process'])),flush=True)
    for row in index['cases']:
        if sha(row['path'])!=row['sha256']:raise ValueError('final complete leaf hash changed')
    index['complete']=True;index['all_requested_segments_proved']=set(done)==set(requested)
    index['whole_reference_leg']=bool(index['all_requested_segments_proved']and args.segments=='all')
    index['all_inside_comparison_strip']=all(r['all_inside_comparison_strip']for r in index['cases'])
    index['all_real_time_q_positive']=all(r['all_real_time_q_positive']for r in index['cases'])
    index['elapsed_seconds_this_process']=time.monotonic()-start
    index['cpu_seconds_this_process']=time.process_time()-cpu;save(args.index,index)
    print(json.dumps(dict(complete=True,whole_reference_leg=index['whole_reference_leg'],
        all_inside_comparison_strip=index['all_inside_comparison_strip'],
        all_real_time_q_positive=index['all_real_time_q_positive'],sha256=sha(args.index))),flush=True)


if __name__=='__main__':main()
