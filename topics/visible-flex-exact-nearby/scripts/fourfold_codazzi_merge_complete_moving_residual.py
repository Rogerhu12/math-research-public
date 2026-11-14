#!/usr/bin/env python3
"""Merge all actual closed moving-residual rows without recomputing them.

The only accepted failed producer is the documented zero-width natural
graft domain rejection, strictly after all its successful body rows.
The complete graft must be supplied independently. Missing true candidate
joins are computed exactly; already verified joins are reused.
"""
from __future__ import annotations
import argparse,gzip,hashlib,json,time
from pathlib import Path
from fractions import Fraction
from bisect import bisect_right
from flint import arb,ctx
from fourfold_codazzi_moving_residual_checkpointed import (
    load,load_candidate,all_cells,ReciprocalFullTargetJets,sha,record,
    interface_jump,COORDINATES,exact_arb,persist)
from fourfold_codazzi_rotational_cap_jacobi import box_from_record

FINAL='ac1d5b98fbe77294c363e0a766c4322e8dd8c2024ef839d548f930c70330a413'
PREFIX='4bb304ebc21ae25671f10663131510c579eb9069381db55e136b8b11dd534295'

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--candidate',type=Path,required=True)
    ap.add_argument('--object',type=Path,default=Path(
        'data/phase_ring_continuation/type_fixed_step02_d5_exact_affine_step5_object.json'))
    ap.add_argument('--prefix',type=Path,default=Path(
        'notes/2026-11-13-R133-moving-alpha0765-fullR-first8-continuous-native.json.gz'))
    ap.add_argument('--prefix-reuse',type=Path,default=Path(
        'notes/2026-11-14-R133-final-residual-first8-reuse-and-jumps-native.json.gz'))
    ap.add_argument('--segments',type=Path,nargs='+',required=True)
    ap.add_argument('--out',type=Path,required=True)
    a=ap.parse_args();started=time.monotonic();ctx.prec=192;ctx.cap=6
    if a.out.exists():raise FileExistsError('preserve every complete merged report')
    if sha(a.candidate)!=FINAL or sha(a.prefix)!=PREFIX:
        raise ValueError('the original final candidate or published prefix changed')
    saved=load_candidate(a.candidate);meta=json.loads(str(saved['metadata']))
    if meta['coordinates']!=COORDINATES or meta['object_sha256']!=sha(a.object):
        raise ValueError('the true complete target or coordinate system differs')
    alpha=Fraction.from_float(float(meta['amplitude']));nu=Fraction(meta['exact_float_nu'])
    knots=[Fraction.from_float(float(x)) for x in saved['radial_nodes']]
    target=ReciprocalFullTargetJets(a.object,Fraction(0),512)
    cuts=all_cells(knots,target,Fraction(25,8));cells=list(zip(cuts,cuts[1:]))
    partition=hashlib.sha256(json.dumps([[str(l),str(r)] for l,r in cells]).encode()).hexdigest()
    if len(cells)!=7296 or len(knots)!=6145:raise ValueError('full exact partition changed')
    expected_source=sha(Path(__file__).with_name('fourfold_codazzi_moving_residual_checkpointed.py'))
    def check_identity(identity):
        expected=dict(source_sha256=expected_source,candidate_sha256=FINAL,
            object_sha256=sha(a.object),partition_sha256=partition,bits=192,
            N=256,nodes=512,subdivide=1,exact_nu=str(nu),exact_amplitude=str(alpha))
        if any(identity.get(k)!=v for k,v in expected.items()):
            raise ValueError('a complete residual identity differs')
        if not 0<=Fraction(identity['half_width'])<=Fraction(1,10**9):
            raise ValueError('a source lies outside the original parameter interval')
        for name,digest in identity['dependencies'].items():
            if Path(name).name!=name or sha(Path(__file__).with_name(name))!=digest:
                raise ValueError('an original complete producer dependency changed')
    prefix=load(a.prefix);reuse=load(a.prefix_reuse)
    check_identity(prefix['source_identity'])
    if (not prefix['complete'] or prefix['selected_count']!=8 or
        not all(x is True for x in prefix['gates'].values()) or
        not reuse['complete'] or reuse['prefix_sha256']!=PREFIX or
        reuse['candidate_sha256']!=FINAL or
        reuse['complete_original_identity']!=prefix['source_identity'] or
        reuse['verified_original_row_indices']!=list(range(8)) or
        reuse['source_sha256']!=sha(Path(__file__).with_name(
            'fourfold_codazzi_verify_residual_prefix_reuse.py'))):
        raise ValueError('the lawful prefix reuse and its new joins are unresolved')
    rows=list(prefix['rows']);jumps={x['knot_index']:x for x in reuse['complete_interface_jumps']}
    sources=[dict(path=str(a.prefix),sha256=sha(a.prefix),first=0,end_exclusive=8,
        half_width=prefix['source_identity']['half_width'],identity=prefix['source_identity'],
        successful_closed_rows_reused=True,whole_source_complete=True)]
    accepted_failure=None
    for path in a.segments:
        d=load(path);identity=d['identity'];check_identity(identity)
        if d['kind']!='checkpointed_complete_moving_continuous_residual_mean_and_physical_II':
            raise ValueError('unexpected native kind')
        first=identity['first'];end=first+len(d['rows'])
        if not d['complete']:
            fail=d['failure']
            if not (fail is not None and identity['half_width']=='0' and end==7271 and
                    first==3648 and identity['end_exclusive']==7296 and
                    fail['index']==7271 and fail['error_type']=='ValueError' and
                    fail['message']=='parameter half width must be positive' and
                    fail['interval']==[str(x) for x in cells[7271]]):
                raise ValueError('only the recorded terminal graft domain rejection is admissible')
            accepted_failure=dict(path=str(path),sha256=sha(path),failure=fail,
                successful_body_prefix=[first,end],failed_graft_rows_not_reused=True)
        elif d['failure'] is not None or end!=identity['end_exclusive']:
            raise ValueError('complete source count or failure flag is inconsistent')
        if first!=len(rows):raise ValueError('overlap or a missing complete source row')
        rows.extend(d['rows'])
        for jump in d['complete_interface_jumps']:
            j=jump['knot_index']
            if j in jumps:raise ValueError('an interface is counted twice')
            jumps[j]=jump
        sources.append(dict(path=str(path),sha256=sha(path),first=first,end_exclusive=end,
            half_width=identity['half_width'],identity=identity,
            successful_closed_rows_reused=True,whole_source_complete=d['complete']))
    if len(rows)!=len(cells):raise ValueError('all 7296 true closed rows are required')
    for i,row in enumerate(rows):
        left,right=cells[i];piece=bisect_right(knots,left)-1
        if (row['index']!=i or row['interval']!=[str(left),str(right)] or
            row['candidate_piece']!=piece or row['exact_angular_support_index']!=96 or
            not knots[piece]<=left<right<=knots[piece+1]):
            raise ValueError('a true closed row or complete Fourier support differs')
    reused=len(jumps);new=[]
    for j in range(1,len(knots)-1):
        if j in jumps:
            if jumps[j]['radius']!=str(knots[j]):raise ValueError('a reused true join moved')
            continue
        values=interface_jump(saved['piece_coefficients'][:,j-1],
            saved['piece_coefficients'][:,j],knots[j]-knots[j-1],32,256)
        jumps[j]=dict(knot_index=j,radius=str(knots[j]),complete_A0=[record(v) for v in values])
        new.append(j)
    if sorted(jumps)!=list(range(1,6144)):raise ValueError('all 6143 true joins are required')
    maxima0=[arb(0),arb(0)];maxima1=[arb(0),arb(0)]
    integrals=[arb(0),arb(0)];squares=[arb(0),arb(0)]
    physical={k:arb(0) for k in ('full_inverse_coordinate_displacement_C0',
        'physical_B_residual_C0','physical_C_residual_C0')}
    gap=None;mgap=None;kappa=arb(0)
    for row,(left,right) in zip(rows,cells):
        width=exact_arb(right-left)
        for j,k in enumerate(('U','V')):
            v=box_from_record(row['complete_residual_A0'][k]).upper()
            w=box_from_record(row['complete_residual_A1'][k]).upper()
            maxima0[j]=max(maxima0[j],v).upper();maxima1[j]=max(maxima1[j],w).upper()
            integrals[j]+=width*v;squares[j]+=width*v*v
        v=box_from_record(row['absolute_v_gap']).lower()
        gap=v if gap is None else min(gap,v).lower()
        v=box_from_record(row['complete_inverse_coordinate_and_physical_residual']['mean_absolute_gap']).lower()
        mgap=v if mgap is None else min(mgap,v).lower()
        kappa=max(kappa,box_from_record(row['candidate_principal_abs_upper']).upper()).upper()
        for k in physical:
            physical[k]=max(physical[k],box_from_record(
                row['complete_inverse_coordinate_and_physical_residual'][k]).upper()).upper()
    sums=[sum((box_from_record(jumps[j]['complete_A0'][k]).upper()
               for j in sorted(jumps)),arb(0)).upper() for k in range(2)]
    doc=dict(kind='complete_actual_moving_residual_all_closed_rows_and_interfaces',
        complete=True,failure=None,source_sha256=sha(__file__),
        original_producer_sha256=expected_source,candidate_sha256=FINAL,
        object_sha256=sha(a.object),exact_amplitude=str(alpha),exact_nu=str(nu),
        candidate_path=str(a.candidate),sources=sources,
        prefix_reuse=dict(path=str(a.prefix_reuse),sha256=sha(a.prefix_reuse)),
        terminal_domain_failure_preserved=accepted_failure,
        exact_full_partition_sha256=partition,interval=['0','25/8'],
        common_parameter_half_width=str(min(Fraction(s['half_width']) for s in sources)),
        original_candidate_all_shards_verified=True,all_original_dependencies_verified=True,
        all_7296_closed_rows_reused_without_recomputation=True,
        all_6143_actual_interfaces_paid=True,reused_interfaces=reused,
        newly_computed_interface_indices=new,whole_real_angular_circle=True,
        complete_original_primitive_tail=True,complete_intermediate_support=64,
        complete_residual_support=96,rows=rows,
        complete_interface_jumps=[jumps[j] for j in sorted(jumps)],
        bounds=dict(residual_A0_sup=[record(v) for v in maxima0],
            residual_A1_sup=[record(v) for v in maxima1],
            residual_L1_r_A0=[record(v.upper()) for v in integrals],
            residual_L2_r_L2_theta=[record(v.sqrt().upper()) for v in squares],
            total_interface_jump_A0=[record(v) for v in sums],
            total_interface_jump_angular_derivative_A0=[record((128*v).upper()) for v in sums],
            minimum_pointwise_v_gap=record(gap),minimum_mean_gap=record(mgap),
            maximum_candidate_principal_abs=record(kappa),
            physical_outputs={k:record(v) for k,v in physical.items()}),
        candidate_curvature_is_not_an_immersion_or_reach_certificate=True,
        inverse_proved=False,nonlinear_PDE_existence_proved=False,
        final_geometric_criteria_proved=False,wall_seconds=time.monotonic()-started)
    persist(a.out,doc)
    print(json.dumps(dict(complete=True,rows=len(rows),interfaces=len(jumps),
        new_interfaces=len(new),half_width=doc['common_parameter_half_width'],
        out=str(a.out),bounds=doc['bounds'])),flush=True)

if __name__=='__main__':main()
