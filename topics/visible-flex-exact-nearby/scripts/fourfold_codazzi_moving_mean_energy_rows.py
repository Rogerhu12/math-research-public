#!/usr/bin/env python3
"""A complete bounded part of the actual moving-energy radial partition.

Uses exactly the v2 directed angular formulas. A completed part certifies
only its explicitly numbered closed rows. The separate complete consumer
must check the full union before applying a whole-interval conclusion.
"""
from __future__ import annotations
import argparse,json,time
from bisect import bisect_right
from fractions import Fraction
from pathlib import Path
from flint import ctx
from fourfold_codazzi_moving_mean_energy_prefix_v2 import (
    read,dyadic,target_bounds,polynomial_ranges,angular_fields,row_coefficients,
    load_candidate,COORDINATES,exact_arb,DirectedFFT,record,save,sha)


def arguments(parser):
    parser.add_argument('--candidate',type=Path,required=True)
    parser.add_argument('--target',type=Path,default=Path('notes/2026-11-13-Codazzi-true-target-r02-v1-native.json.gz'))
    parser.add_argument('--collar',type=Path,default=Path('notes/2026-11-13-R133-actual-root-collar-complete-coefficients-v2-native.json.gz'))
    parser.add_argument('--type-cover',type=Path,default=Path('notes/2026-11-13-R133-compact-nu-full-type-cover-native.json.gz'))
    parser.add_argument('--right',type=Fraction,default=Fraction(119,500))
    parser.add_argument('--angles',type=int,default=4096)
    return parser


def prepare(args):
    saved=load_candidate(args.candidate);meta=json.loads(str(saved['metadata']))
    native=read(args.target);types=read(args.type_cover);inputs=[args.candidate,args.target,args.type_cover]
    if (meta['coordinates']!=COORDINATES or meta['object_sha256']!=native['object_sha256']
        or not native['complete'] or not types['complete'] or not types['exactly_one_real_K_root']
        or types['inputs'].get(str(args.target))!=sha(args.target)):
        raise ValueError('the complete actual candidate and true target identities differ')
    right=args.right
    if not 0<right<=Fraction(119,500):raise ValueError('only the proved strict negative prefix is accepted')
    target_rows=list(native['rows'])
    if right>Fraction(1,5):
        collar=read(args.collar);inputs.append(args.collar)
        if (not collar['complete'] or not collar['whole_real_radial_interval']
            or collar['object_sha256']!=native['object_sha256']
            or collar['parameter_half_width']!=native['parameter_half_width']
            or collar['inputs'].get(str(args.type_cover))!=sha(args.type_cover)):
            raise ValueError('the full genuine root collar is required')
        target_rows.extend(collar['rows'])
    nuq=Fraction(meta['exact_float_nu']);nulo,nuhi=map(Fraction,types['exact_nu_interval'])
    if nuq!=dyadic(meta['nu']) or not nulo<=nuq<=nuhi:raise ValueError('actual nu lies outside the proved target interval')
    m=int(meta['modes']);angles=args.angles
    if angles<=2*m or angles&(angles-1):raise ValueError('a complete power-of-two angular grid is required')
    nodes=list(map(dyadic,saved['radial_nodes']))
    if nodes[0]!=0 or nodes[-1]<right:raise ValueError('candidate extrapolation is forbidden')
    tnodes=[Fraction(row['interval'][0]) for row in target_rows]+[Fraction(target_rows[-1]['interval'][1])]
    if tnodes[0]!=0 or any(Fraction(a['interval'][1])!=Fraction(b['interval'][0]) for a,b in zip(target_rows,target_rows[1:])):
        raise ValueError('the original actual target partition changed')
    cuts=sorted({Fraction(0),right}|{x for x in (Fraction(1,20),Fraction(9,50)) if x<right}|
        {x for x in nodes if 0<x<right}|{x for x in tnodes if 0<x<right})
    header=dict(object_sha256=meta['object_sha256'],candidate_metadata=meta,actual_fixed_nu=str(nuq),
        exact_amplitude=str(dyadic(meta['amplitude'])),exact_interval=['0',str(right)],
        parameter_half_width=native['parameter_half_width'],whole_affine_parameter_interval=True,
        complete_primitive_tail=True,closed_angular_cells=angles,all_Fourier_variations_retained=True,
        independent_allowed_mean_retained=True,inputs={str(p):sha(p) for p in inputs},
        total_common_partition_rows=len(cuts)-1,
        coefficient_formula_source_sha256=sha(Path(__file__).with_name('fourfold_codazzi_moving_mean_energy_prefix_v2.py')))
    return dict(saved=saved,meta=meta,native=native,types=types,target_rows=target_rows,nodes=nodes,
        target_nodes=tnodes,cuts=cuts,alpha=exact_arb(dyadic(meta['amplitude'])),nu=exact_arb(nuq),
        m=m,angles=angles,header=header)


def identify(context,index):
    nodes,tnodes,cuts=context['nodes'],context['target_nodes'],context['cuts']
    left,right=cuts[index:index+2]
    j=min(bisect_right(nodes,left)-1,len(nodes)-2);k=bisect_right(tnodes,left)-1
    row=context['target_rows'][k];tl,tr=map(Fraction,row['interval'])
    if not nodes[j]<=left<right<=nodes[j+1] or not tl<=left<right<=tr:
        raise ValueError('the exact common candidate/target row is incomplete')
    return left,right,j,k,row


def main():
    ap=arguments(argparse.ArgumentParser(description=__doc__))
    ap.add_argument('--first-row',type=int,required=True);ap.add_argument('--row-count',type=int,default=150)
    ap.add_argument('--out',type=Path,required=True)
    args=ap.parse_args();started=time.monotonic();ctx.prec=320
    if args.out.exists():raise FileExistsError('preserve each actual complete-row part')
    context=prepare(args);total=context['header']['total_common_partition_rows']
    first=args.first_row;last=min(total,first+args.row_count)
    if not 0<=first<last<=total:raise ValueError('the requested complete-row part is empty or invalid')
    doc=dict(context['header'],kind='actual_moving_mean_energy_complete_row_part',complete=False,
        source_sha256=sha(__file__),first_common_row=first,last_common_row_exclusive=last,
        exact_requested_subinterval=list(map(str,(context['cuts'][first],context['cuts'][last]))),
        whole_body_interval_claimed=False,rows=[],failure=None)
    fft=DirectedFFT();checkpoint=time.monotonic()
    try:
        for index in range(first,last):
            left,right,j,k,row=identify(context,index)
            a=target_bounds(row,left,right,context['nu'])
            y,_=polynomial_ranges(context['saved'],context['nodes'],j,left,right)
            fields,nodes=angular_fields(y,context['m'],context['alpha'],a['s'],context['angles'],fft)
            c=row_coefficients(fields,nodes,a,context['angles'])
            doc['rows'].append(dict(common_row=index,interval=[str(left),str(right)],candidate_piece=j,native_row=k,
                actual_scalar_germ=row['actual_scalar_germ'],
                actual_target={name:record(a[name]) for name in ('gamma','beta','K','K1')},
                bounds={name:record(value) for name,value in c.items()}))
            if time.monotonic()-checkpoint>20:
                doc['wall_seconds']=time.monotonic()-started;save(args.out,doc)
                print(dict(common_row=index,completed=len(doc['rows']),planned=last-first,right=str(right)),flush=True)
                checkpoint=time.monotonic()
        doc.update(complete=True,whole_requested_radial_subinterval=True)
    except Exception as exc:doc['failure']=dict(type=type(exc).__name__,message=str(exc))
    doc['wall_seconds']=time.monotonic()-started;save(args.out,doc)
    print(dict(complete=doc['complete'],failure=doc['failure'],first=first,last=last,rows=len(doc['rows']),
        total=total,wall_seconds=doc['wall_seconds']),flush=True)
    if not doc['complete']:raise RuntimeError(str(doc['failure']))


if __name__=='__main__':main()
