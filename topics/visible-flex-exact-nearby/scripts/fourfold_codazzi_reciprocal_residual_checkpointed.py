#!/usr/bin/env python3
"""Continuous full reciprocal residual with compact, resumable native rows.

The actual interval operations are the previously proved v3 operations.
This driver saves each completed group of closed cells and all real PPoly
interface jumps. A failed mathematical gate is preserved, not resumed over.
All angular modes, original target tails and radial Taylor terms are kept.
"""
from __future__ import annotations
import argparse
import gzip
import hashlib
import json
import os
import time
from bisect import bisect_right
from fractions import Fraction
from pathlib import Path
from flint import arb,ctx
from fourfold_codazzi_reciprocal_continuous_residual_v3 import (
    load_candidate,COORDINATES,ReciprocalCompactTargetJets,DirectedFFT,
    all_cells,exact_candidate_series,target_model,residual_polynomials,
    full_residual_norm,whole_chart_bounds,interface_jump,record,sha,exact_arb)
from fourfold_codazzi_rotational_cap_jacobi import box_from_record


def load(path):
    raw=Path(path).read_bytes()
    return json.loads(gzip.decompress(raw) if str(path).endswith('.gz') else raw)


def persist(path,value):
    raw=(json.dumps(value,indent=2,allow_nan=False)+'\n').encode()
    if str(path).endswith('.gz'):raw=gzip.compress(raw,mtime=0)
    temporary=Path(str(path)+'.partial');temporary.write_bytes(raw);os.replace(temporary,path)


def principal_bound(chart,K,alpha):
    """det S=K and tr S=Kv+(1+u^2)/v, all theta and all r."""
    v=chart['v_lower'].union(chart['v_upper'])
    ua=(abs(exact_arb(alpha))*chart['normalized_U_abs']).upper()
    u2=arb(0).union((ua*ua).upper())
    trace=K*v+(1+u2)/v;T=abs(trace).upper()
    discriminant=(T*T-4*K.lower()).upper()
    if discriminant<0:raise ValueError('inconsistent complete principal-curvature discriminant')
    return ((T+discriminant.sqrt())/2).upper()


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--object',type=Path,default=Path('data/phase_ring_continuation/type_fixed_step02_d5_exact_affine_step5_object.json'))
    ap.add_argument('--candidate',type=Path,required=True)
    ap.add_argument('--right',type=Fraction,default=Fraction(3,2))
    ap.add_argument('--half-width',type=Fraction,default=Fraction(0))
    ap.add_argument('--nodes',type=int,default=512);ap.add_argument('--angles',type=int,default=2048)
    ap.add_argument('--bits',type=int,default=192);ap.add_argument('--subdivide',type=int,default=1)
    ap.add_argument('--first',type=int,default=0);ap.add_argument('--count',type=int)
    ap.add_argument('--checkpoint-cells',type=int,default=8)
    ap.add_argument('--pause-after-cells',type=int,default=0)
    ap.add_argument('--resume',action='store_true');ap.add_argument('--out',type=Path,required=True)
    args=ap.parse_args();started=time.monotonic();ctx.prec=args.bits;ctx.cap=6
    if args.out.exists()!=args.resume:raise FileExistsError('an existing incomplete result requires explicit --resume')
    if args.checkpoint_cells<1 or args.pause_after_cells<0:raise ValueError('invalid checkpoint schedule')
    data=load_candidate(args.candidate);meta=json.loads(str(data['metadata']));m=int(meta['modes']);N=args.angles
    if meta['coordinates']!=COORDINATES or meta['object_sha256']!=sha(args.object):
        raise ValueError('the exact complete same-target reciprocal candidate is required')
    if N<=6*m or N&(N-1) or args.subdivide<1 or args.first<0:
        raise ValueError('unaliased complete support and a valid exact partition are required')
    if not 0<args.right<=Fraction(3,2) or args.half_width<0:raise ValueError('invalid target domain')
    alpha=Fraction.from_float(float(meta['amplitude']));nu=Fraction(meta['exact_float_nu'])
    knots=[Fraction.from_float(float(x)) for x in data['radial_nodes']]
    if knots[0]!=0 or knots[-1]<args.right:raise ValueError('no extrapolation of a saved candidate')
    target=ReciprocalCompactTargetJets(args.object,args.half_width,args.nodes);fft=DirectedFFT()
    cuts=all_cells(knots,target,args.right);cells=[]
    for lo,hi in zip(cuts,cuts[1:]):
        cells.extend((lo+(hi-lo)*j/args.subdivide,lo+(hi-lo)*(j+1)/args.subdivide) for j in range(args.subdivide))
    end=len(cells) if args.count is None else min(len(cells),args.first+args.count)
    if not args.first<end:raise ValueError('empty selected continuous cell range')
    dependencies={name:sha(Path(__file__).with_name(name)) for name in (
        'fourfold_codazzi_reciprocal_continuous_residual_v3.py',
        'fourfold_codazzi_reciprocal_compact_target_jets.py','fourfold_codazzi_cubic_target_jets.py',
        'fourfold_codazzi_high_target_jets.py','fourfold_phase_metric_defect.py',
        'fourfold_phase_cap_scaled_body.py','fourfold_phase_beta_bulk_box.py',
        'fourfold_phase_beta_bulk_interval.py','fourfold_codazzi_candidate_shards.py',
        'fourfold_codazzi_rotational_cap_jacobi.py')}
    identity=dict(source_sha256=sha(__file__),dependencies=dependencies,
        candidate_sha256=sha(args.candidate),object_sha256=sha(args.object),
        partition_sha256=hashlib.sha256(json.dumps([[str(l),str(r)] for l,r in cells]).encode()).hexdigest(),
        first=args.first,end_exclusive=end,half_width=str(args.half_width),bits=args.bits,N=N,
        nodes=args.nodes,subdivide=args.subdivide,exact_nu=str(nu),exact_amplitude=str(alpha))
    if args.resume:
        doc=load(args.out)
        if doc['identity']!=identity or doc['complete'] or doc['failure'] is not None:
            raise ValueError('only the same interrupted, nonfailed complete-cell run may resume')
        if len(doc['rows'])>end-args.first:raise ValueError('invalid saved complete-cell count')
        for j,row in enumerate(doc['rows'],args.first):
            if row['index']!=j or row['interval']!=list(map(str,cells[j])):
                raise ValueError('a completed row or exact partition changed')
        doc['resumptions'].append(dict(completed_rows=len(doc['rows'])))
        previous_seconds=float(doc['wall_seconds'])
    else:
        doc=dict(kind='checkpointed_complete_reciprocal_continuous_residual_and_candidate_II',
            complete=False,failure=None,identity=identity,candidate_path=str(args.candidate),
            exact_selected_interval=[str(cells[args.first][0]),str(cells[end-1][1])],
            total_partition_cells=len(cells),first=args.first,end_exclusive=end,
            modes=m,angles=N,rows=[],complete_interface_jumps=[],resumptions=[],wall_seconds=0.,
            complete_original_primitive_tail=True,all_saved_candidate_modes_retained=True,
            whole_real_angular_circle=True,whole_requested_body=False,
            candidate_principal_bound_is_not_an_immersion_or_reach_certificate=True,
            inverse_proved=False,nonlinear_PDE_existence_proved=False,final_geometric_criteria_proved=False)
        previous_seconds=0.;persist(args.out,doc)
    def store():
        doc['wall_seconds']=previous_seconds+time.monotonic()-started;persist(args.out,doc)
    initial=len(doc['rows']);maxima=[arb(0),arb(0)];gap=None;curvature=arb(0)
    for row in doc['rows']:
        maxima=[max(a,box_from_record(row['complete_residual_A0'][k])).upper() for a,k in zip(maxima,('U','V'))]
        g=box_from_record(row['absolute_v_gap']);gap=g if gap is None else min(gap,g).lower()
        curvature=max(curvature,box_from_record(row['candidate_principal_abs_upper'])).upper()
    try:
        for index in range(args.first+initial,end):
            left,right=cells[index];mid=(left+right)/2;piece=bisect_right(knots,left)-1
            if not knots[piece]<=left<right<=knots[piece+1]:raise ValueError('incomplete actual polynomial coverage')
            whole,germ=target.coefficients(left,right,nu);centre,_=target.coefficients(mid,mid,nu)
            fields,full,half=exact_candidate_series(data['piece_coefficients'][:,piece],knots[piece],left,right,m,N,fft)
            model={name:target_model(centre,whole,name,half) for name in ('gamma','beta','K','s')}
            RU,RV,v=residual_polynomials(fields,model,alpha)
            bounds,per_order,degree=full_residual_norm((RU,RV),N,3*m,fft)
            chart=whole_chart_bounds(full,model,alpha,N,fft)
            kappa=principal_bound(chart,whole['K'],alpha)
            doc['rows'].append(dict(index=index,interval=list(map(str,(left,right))),candidate_piece=piece,
                actual_scalar_germ=list(map(str,germ)),exact_angular_support_index=3*m,
                full_radial_polynomial_degree=degree,
                complete_residual_A0={name:record(value) for name,value in zip(('U','V'),bounds)},
                all_uniform_target_and_roundoff_remainders_A0={name:record(poly.error) for name,poly in zip(('U','V'),(RU,RV))},
                absolute_v_gap=record(chart['absolute_v_gap']),candidate_principal_abs_upper=record(kappa)))
            maxima=[max(a,b).upper() for a,b in zip(maxima,bounds)]
            gap=chart['absolute_v_gap'] if gap is None else min(gap,chart['absolute_v_gap']).lower()
            curvature=max(curvature,kappa).upper()
            doc['maximum_complete_residual_A0']=[record(z) for z in maxima]
            doc['minimum_actual_v_gap']=record(gap);doc['maximum_candidate_principal_abs_upper']=record(curvature)
            if len(doc['rows'])%args.checkpoint_cells==0 or index==end-1:
                store();print(dict(complete_rows=len(doc['rows']),requested_rows=end-args.first,
                    last_interval=list(map(str,(left,right))),residual_A0=[z.str(12) for z in maxima],
                    candidate_kappa=curvature.str(12),wall_seconds=doc['wall_seconds']),flush=True)
            if args.pause_after_cells and len(doc['rows'])-initial>=args.pause_after_cells and index<end-1:
                store();print(dict(intentional_cell_checkpoint_pause=True,complete_rows=len(doc['rows'])),flush=True);return
        jump_sum=[arb(0),arb(0)];doc['complete_interface_jumps']=[]
        selected_left,selected_right=cells[args.first][0],cells[end-1][1]
        for j in range(1,len(knots)-1):
            if not selected_left<knots[j]<=selected_right:continue
            values=interface_jump(data['piece_coefficients'][:,j-1],data['piece_coefficients'][:,j],knots[j]-knots[j-1],m,N)
            doc['complete_interface_jumps'].append(dict(knot_index=j,radius=str(knots[j]),complete_A0=[record(v) for v in values]))
            jump_sum=[a+b for a,b in zip(jump_sum,values)]
        doc.update(complete=True,whole_requested_body=args.first==0 and end==len(cells),
            total_complete_interface_jump_A0=[record(v) for v in jump_sum])
    except Exception as error:
        doc['failure']=dict(index=locals().get('index'),interval=list(map(str,locals().get('cells',[])[index])) if 'index' in locals() else None,
            error_type=type(error).__name__,message=str(error))
    store();print(dict(complete=doc['complete'],failure=doc['failure'],rows=len(doc['rows']),
        whole_requested_body=doc['whole_requested_body'],wall_seconds=doc['wall_seconds']),flush=True)
    if not doc['complete']:raise RuntimeError(str(doc['failure']))


if __name__=='__main__':main()
