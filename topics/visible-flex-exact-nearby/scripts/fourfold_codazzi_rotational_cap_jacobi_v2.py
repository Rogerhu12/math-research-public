#!/usr/bin/env python3
"""Strict-positive replay/refinement of the completed actual cap checkpoint.

Version 1 preserved a complete scalar cover but correctly failed its later
Riccati gate: one wide derived lambda ball crossed zero and a negative
upper/lower ratio had passed the width test. This version checks positivity
first, encloses positive products by endpoint arithmetic, and re-evaluates
only boxes needing genuine subdivision. The old source/report stay intact.
"""
from __future__ import annotations
import argparse,copy,gzip,json,time
from fractions import Fraction
from pathlib import Path
from flint import ctx
from fourfold_codazzi_rotational_cap_jacobi import RotationalPositiveCap,box_from_record,propagate
from fourfold_phase_metric_defect import record,save,sha
from fourfold_phase_beta_bulk_interval import exact_arb
from fourfold_phase_beta_affine import load_definition


def positive_lambda(K,E,R):
    if not all(x>0 for x in (K,E,R)):raise ValueError('nonpositive primitive coefficient before ratio')
    lo=(K.lower()*E.lower()/R.upper()).lower()
    hi=(K.upper()*E.upper()/R.lower()).upper()
    answer=lo.union(hi)
    if not answer>0:raise ValueError('positive endpoint quotient failed')
    return answer


def checked(values,maximum):
    values=dict(values);values['lambda_ref']=positive_lambda(values['K'],values['Ebar'],values['R'])
    if not all(values[k]>0 for k in ('a','Ebar','R','K','gamma','lambda_ref')) or not values['Cref']<0:
        raise ValueError('strict derived positive/negative chart gate failed before width ratio')
    ratio=max((values[k].upper()/values[k].lower()).upper() for k in ('gamma','lambda_ref','R'))
    if not 1<=ratio<exact_arb(maximum):raise ValueError('positive coefficient ratio requests actual subdivision')
    return values,ratio


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--checkpoint',type=Path,default=Path('notes/2026-11-13-Codazzi-rotational-positive-cap-native.json.gz'))
    ap.add_argument('--object',type=Path,default=Path('data/phase_ring_continuation/type_fixed_step02_d5_exact_affine_step5_object.json'))
    ap.add_argument('--out',type=Path,required=True)
    a=ap.parse_args();start=time.monotonic()
    if a.out.exists():raise FileExistsError('refusing to overwrite a completed or failed replay')
    old=json.loads(gzip.decompress(a.checkpoint.read_bytes()));ctx.prec=int(old['bits']);ctx.cap=6
    original=Path(__file__).with_name('fourfold_codazzi_rotational_cap_jacobi.py')
    if not old['complete'] or old['source_sha256']!=sha(original) or old['object_sha256']!=sha(a.object):
        raise ValueError('checkpoint does not bind the unchanged complete scalar source')
    for name,digest in old['dependency_sha256'].items():
        if sha(Path(__file__).with_name(name))!=digest:raise ValueError('checkpoint dependency changed: '+name)
    for name,digest in old['input_theorem_sha256'].items():
        if sha(Path('results')/name)!=digest:raise ValueError('checkpoint theorem input changed: '+name)
    definition,_,_,center=load_definition(a.object)
    if str(center)!=old['exact_center_parameter']:raise ValueError('different affine family center')
    maximum=Fraction(old['maximum_coefficient_ratio'])
    target=RotationalPositiveCap(a.object,Fraction(old['parameter_half_width']),int(old['nodes']))
    rows=[];rejections=[];fresh_count=0;reused_count=0;failed=None
    for index,oldrow in enumerate(old['rows']):
        left,right=map(Fraction,oldrow['interval'])
        if right<=3:
            germ=list(map(Fraction,oldrow['actual_scalar_germ']))
            if germ[0] not in target.cuts or germ[1] not in target.cuts or not germ[0]<=left<right<=germ[1]:
                raise ValueError('a cached body box lost its exact scalar germ identity')
        values={k:box_from_record(v) for k,v in oldrow['coefficients'].items()}
        try:
            values,ratio=checked(values,maximum);row=copy.deepcopy(oldrow)
            row['coefficients']['lambda_ref']=record(values['lambda_ref']);row['maximum_ratio']=record(ratio)
            row['reused_original_coefficient_box']=True;row['original_box_index']=index
            rows.append(row);reused_count+=1;continue
        except ValueError as error:
            rejections.append(dict(interval=oldrow['interval'],depth=oldrow['depth'],original_box_index=index,
                original_lambda_lower=oldrow['coefficients']['lambda_ref']['lower'],reason=str(error)))
        pending=[(left,right,int(oldrow['depth']))]
        while pending:
            l,r,depth=pending.pop()
            try:
                actual,germ,part=target.values(l,r);actual,ratio=checked(actual,maximum)
                rows.append(dict(interval=[str(l),str(r)],actual_scalar_germ=list(map(str,germ)),part=part,
                    coefficients={k:record(v) for k,v in actual.items()},maximum_ratio=record(ratio),depth=depth,
                    reused_original_coefficient_box=False,original_box_index=index));fresh_count+=1
            except (ValueError,ZeroDivisionError) as error:
                item=dict(interval=[str(l),str(r)],depth=depth,original_box_index=index,reason=str(error));rejections.append(item)
                if depth>=20:failed=item;break
                mid=(l+r)/2;pending.extend([(mid,r,depth+1),(l,mid,depth+1)])
        if failed:break
    endpoint=Fraction(old['exact_requested_interval'][0])
    for row in rows:
        left,right=map(Fraction,row['interval'])
        if left!=endpoint or right<=left:raise ValueError('strict replay lost complete closed coverage')
        endpoint=right
    complete=failed is None and endpoint==Fraction(old['exact_requested_interval'][1])
    report=copy.deepcopy(old)
    report.update(kind='actual_fixed_target_rotational_cap_complete_Codazzi_Jacobi_v2',source_sha256=sha(__file__),
        checkpoint_path=str(a.checkpoint),checkpoint_sha256=sha(a.checkpoint),
        original_source_sha256=sha(original),complete=complete,rows=rows,
        covered_interval=[old['exact_requested_interval'][0],str(endpoint)],failure=failed,
        original_scalar_boxes=len(old['rows']),reused_scalar_boxes=reused_count,fresh_scalar_boxes=fresh_count,
        strict_positive_rejections=rejections,cap_linear_reference_certified=False,
        repaired_gate='Check lambda>0 before any upper/lower ratio; positive K*Ebar/R is enclosed by ordered endpoint products, then subdivide its true scalar interval as necessary.',
        original_failure_preserved=dict(path=str(a.checkpoint),cap_linear_reference_certified=old['cap_linear_reference_certified'],
            message=old.get('Jacobi_failure'),no_successful_Jacobi_certificate_existed=True))
    report.pop('Jacobi_failure',None);report.pop('Jacobi',None)
    report['wall_seconds']=time.monotonic()-start;save(a.out,report)
    if complete:
        try:
            report['Jacobi']=propagate(rows,old['true_R74_entrance'],int(old['requested_finite_modes']))
            report['cap_linear_reference_certified']=True
        except (ValueError,ZeroDivisionError) as error:report['Jacobi_failure']=str(error)
    report['wall_seconds']=time.monotonic()-start;save(a.out,report)
    print(dict(complete=complete,certified=report['cap_linear_reference_certified'],boxes=len(rows),
        reused=reused_count,fresh=fresh_count,Jacobi_failure=report.get('Jacobi_failure'),wall_seconds=report['wall_seconds']),flush=True)
    if report['cap_linear_reference_certified']:
        print([dict(m=x['physical_frequency'],q_lower=x['final_q_lower']['lower'],q_upper=x['final_q_upper']['upper'])
            for x in report['Jacobi']['finite_mode_entries']],flush=True)


if __name__=='__main__':main()
