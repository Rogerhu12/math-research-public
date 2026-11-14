#!/usr/bin/env python3
"""Resumable complete scalar Taylor cache for the actual negative two rays.

Each accepted cell has exact dyadic declared-degree models for beta,K,s,
gamma and q=sqrt(-K), with complete point jets plus the whole final
derivative. Original scalar/bump seams are never crossed.
The integrated error is a scalar certificate, not a ray/conjugacy proof.
"""
from __future__ import annotations
import argparse
from fractions import Fraction
import gzip,json,math,time
from pathlib import Path
from flint import arb,arb_series,ctx
from fourfold_codazzi_phase_complete_Arb_high_scalar_jets import FullArbScalarTarget
from fourfold_codazzi_rotational_cap_jacobi import box_from_record
from fourfold_codazzi_current_positive_complete_coefficients import OBJECT_SHA
from fourfold_phase_beta_bulk_interval import exact_arb
from fourfold_phase_metric_defect import record,save,sha

ROOT_LOWER=Fraction('0.2383968742994')
NU=Fraction(-2572625729470897,72057594037927936)
KIND='actual_complete_phase_scalar_high_Taylor_germ_v2'
NAMES=('beta','K','s','gamma','q')


def read(path):
    return json.loads(gzip.decompress(Path(path).read_bytes()))


def dyadic_midpoint(x):
    a,b=x.mid().man_exp();a,b=int(a),int(b)
    return Fraction(a*2**b) if b>=0 else Fraction(a,2**(-b))


def add_q(values,order):
    if not values['K']<0:raise ValueError('the entire requested scalar box is not strictly negative')
    previous=ctx.cap;ctx.cap=max(previous,order+1)
    try:
        q=arb_series([-values['K'+(str(j) if j else '')]/math.factorial(j) for j in range(order+1)],prec=order+1).sqrt()
        if q.prec<order+1:raise ValueError('the complete negative square-root jet order was truncated')
    finally:ctx.cap=previous
    result=dict(values)
    for j in range(order+1):result['q'+(str(j) if j else '')]=math.factorial(j)*q[j]
    return result


def weight(left,right):
    # This is only an adaptive allocation weight. The final saved error
    # is always the actually evaluated width times the complete remainder.
    return (2*(exact_arb(ROOT_LOWER-left).sqrt()-exact_arb(ROOT_LOWER-right).sqrt())).lower()


def make_model(target,left,right,nu):
    middle=(left+right)/2;half=exact_arb((right-left)/2)
    whole,germ=target.coefficients(left,right,nu);whole_details=target.last_details
    point,point_germ=target.coefficients(middle,middle,nu);point_details=target.last_details
    if germ!=point_germ:raise ValueError('point and whole derivative germs differ')
    order=target.jet_order
    whole,point=add_q(whole,order),add_q(point,order);models={};total=arb(0)
    for name in NAMES:
        p=[point[name+(str(j) if j else '')]/math.factorial(j) for j in range(order)]
        coefficients=[dyadic_midpoint(z) for z in p]
        factorial=math.factorial(order)
        coefficients.append(dyadic_midpoint(whole[name+str(order)]/factorial))
        fee=sum((abs(p[j]-exact_arb(coefficients[j]))*half**j for j in range(order)),arb(0))
        final_fee=(abs(whole[name+str(order)]-factorial*exact_arb(coefficients[order]))*half**order/factorial).upper()
        fee=(fee+final_fee).upper();total+=fee
        models[name]=dict(exact_centered_polynomial=list(map(str,coefficients)),
            complete_uniform_remainder=record(fee),whole_final_derivative=record(whole[name+str(order)]),
            selected_final_derivative_remainder=record(final_fee),
            complete_true_value=record(whole[name]),point_jets=[record(z) for z in p])
    return dict(interval=list(map(str,(left,right))),center=str(middle),actual_scalar_germ=list(map(str,germ)),
        models=models,complete_sum_uniform_remainders=record(total.upper()),
        integrated_sum_scalar_remainders=record((exact_arb(right-left)*total).upper()),
        whole_angular_exponential_details=whole_details,point_angular_exponential_details=point_details)


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--object',type=Path,default=Path('data/phase_ring_continuation/type_fixed_step02_d5_exact_affine_step5_object.json'))
    ap.add_argument('--nu',type=Fraction,default=NU)
    ap.add_argument('--half-width',type=Fraction,default=Fraction(0))
    ap.add_argument('--root-stop-gap',type=Fraction,default=Fraction(1,2**32))
    ap.add_argument('--total-scalar-error',type=Fraction,default=Fraction(1,2**42))
    ap.add_argument('--germ-start',type=int,default=0)
    ap.add_argument('--germ-stop',type=int)
    ap.add_argument('--initial-subdivisions',type=int,default=1)
    ap.add_argument('--bits',type=int,default=192)
    ap.add_argument('--exponential-bits',type=int,default=160)
    ap.add_argument('--jet-order',type=int,default=7)
    ap.add_argument('--max-depth',type=int,default=32)
    ap.add_argument('--resume',action='store_true')
    ap.add_argument('--out-dir',type=Path,required=True)
    args=ap.parse_args();started=time.monotonic();ctx.prec=args.bits;ctx.cap=args.jet_order+3
    if sha(args.object)!=OBJECT_SHA or args.nu!=NU or args.half_width!=0:
        raise ValueError('this first complete cache is for the actual fixed final nu and eta=0')
    if not 0<args.root_stop_gap<Fraction(1,10**5) or not 0<args.total_scalar_error<Fraction(1,10**6):
        raise ValueError('invalid declared root stop or complete scalar error allocation')
    if not 1<=args.initial_subdivisions<=64 or args.max_depth<4:
        raise ValueError('invalid bounded adaptive subdivision controls')
    right_end=ROOT_LOWER-args.root_stop_gap
    target=FullArbScalarTarget(args.object,args.half_width,args.exponential_bits,args.jet_order)
    cuts=[Fraction(0),*[r for r in target.cuts if 0<r<right_end],right_end]
    germs=list(zip(cuts[:-1],cuts[1:]));stop=len(germs) if args.germ_stop is None else args.germ_stop
    if not 0<=args.germ_start<stop<=len(germs):raise ValueError('invalid exact true-germ range')
    args.out_dir.mkdir(parents=True,exist_ok=True)
    configuration=dict(kind=KIND,source_sha256=sha(__file__),provider_sha256=sha(Path(__file__).with_name('fourfold_codazzi_phase_complete_Arb_high_scalar_jets.py')),
        object_sha256=OBJECT_SHA,exact_nu=str(args.nu),exact_eta_offset='0',
        exact_root_lower=str(ROOT_LOWER),root_stop_gap=str(args.root_stop_gap),
        complete_requested_interval=['0',str(right_end)],total_germs=len(germs),
        total_scalar_error=str(args.total_scalar_error),bits=args.bits,exponential_bits=args.exponential_bits,
        jet_order=args.jet_order,
        initial_subdivisions=args.initial_subdivisions,max_depth=args.max_depth)
    total_weight=weight(Fraction(0),right_end);all_reports=[]
    for index in range(args.germ_start,stop):
        left,right=germs[index];path=args.out_dir/f'germ{index:04d}.json.gz'
        partial=args.out_dir/f'germ{index:04d}.partial.json.gz'
        if path.exists():
            old=read(path)
            if not args.resume or old['configuration']!=configuration or not old['complete']:
                raise ValueError('an existing complete cache requires exact-source resume identity')
            all_reports.append(dict(path=path.name,sha256=sha(path),germ_index=index));continue
        if partial.exists():
            old=read(partial)
            if not args.resume or old['configuration']!=configuration:raise ValueError('an existing partial cache has a different exact identity')
            accepted=old['rows'];rejected=old['rejected_cells'];pending=[(Fraction(a),Fraction(b),int(d)) for a,b,d in old['pending']]
        else:
            sub=[left+(right-left)*j/args.initial_subdivisions for j in range(args.initial_subdivisions+1)]
            accepted=[];rejected=[];pending=[(a,b,0) for a,b in reversed(list(zip(sub[:-1],sub[1:])))]
        germ_start=time.monotonic()
        while pending:
            a,b,depth=pending.pop();allocation=(exact_arb(args.total_scalar_error)*weight(a,b)/total_weight).lower()
            model=None;failure=None
            try:
                model=make_model(target,a,b,args.nu)
                fee=box_from_record(model['integrated_sum_scalar_remainders']).upper()
                passed=fee<allocation
            except ValueError as exc:
                failure=str(exc);passed=False
            if passed:
                model['adaptive_depth']=depth;model['allocated_integrated_scalar_error']=record(allocation)
                accepted.append(model)
            else:
                rejected.append(dict(interval=list(map(str,(a,b))),depth=depth,
                    failure=failure,observed_integrated_scalar_error=None if model is None else model['integrated_sum_scalar_remainders'],
                    allocated_integrated_scalar_error=record(allocation)))
                if depth>=args.max_depth:
                    pending.append((a,b,depth))
                    save(partial,dict(configuration=configuration,germ_index=index,complete=False,rows=accepted,
                        rejected_cells=rejected,pending=[list(map(str,z)) for z in pending],failure='maximum actual subdivision depth reached'))
                    raise RuntimeError('the true scalar Taylor model did not close before the explicit depth limit')
                mid=(a+b)/2;pending.extend(((mid,b,depth+1),(a,mid,depth+1)))
            save(partial,dict(configuration=configuration,germ_index=index,complete=False,rows=accepted,
                rejected_cells=rejected,pending=[list(map(str,z)) for z in pending]))
            print(dict(germ=index,accepted=len(accepted),pending=len(pending),depth=depth,
                cell=list(map(str,(a,b))),passed=bool(passed),seconds=time.monotonic()-started),flush=True)
        accepted.sort(key=lambda r:Fraction(r['interval'][0]));cursor=left;fee=arb(0)
        for row in accepted:
            a,b=map(Fraction,row['interval'])
            if a!=cursor or b<=a:raise ValueError('the accepted complete scalar cells have a gap or overlap')
            cursor=b;fee+=box_from_record(row['integrated_sum_scalar_remainders'])
        allocation=(exact_arb(args.total_scalar_error)*weight(left,right)/total_weight).lower()
        gates=[dict(name=name,passed=bool(ok)) for name,ok in (
            ('every actual scalar and compact-bump germ boundary is respected',cursor==right),
            ('complete beta K s gamma and negative square root models retained',all(set(r['models'])==set(NAMES) for r in accepted)),
            ('exact dyadic coefficients of the declared degree are stored',all(len(r['models'][n]['exact_centered_polynomial'])==args.jet_order+1 for r in accepted for n in NAMES)),
            ('point and whole high jets include every angular exponential tail',all(r['whole_angular_exponential_details']['full_angular_exponential_error_not_grid_alias'] for r in accepted)),
            ('actual integrated complete scalar error fits this true germ allocation',fee<allocation),
            ('the final negative endpoint precedes the proved common root lower bound',right<=right_end<ROOT_LOWER),
        )]
        report=dict(configuration=configuration,kind=KIND,complete=all(g['passed'] for g in gates),germ_index=index,
            exact_interval=list(map(str,(left,right))),rows=accepted,rejected_cells=rejected,
            integrated_complete_scalar_error=record(fee.upper()),allocated_complete_scalar_error=record(allocation),
            gates=gates,no_ray_or_conjugacy_certificate_claimed=True,no_whole_operator_inverse_claimed=True,
            seconds=time.monotonic()-germ_start)
        save(path,report)
        if not report['complete']:raise RuntimeError('a true scalar germ budget failed')
        partial.unlink()
        all_reports.append(dict(path=path.name,sha256=sha(path),germ_index=index))
        save(args.out_dir/f'manifest-{args.germ_start:04d}-{stop:04d}.json.gz',dict(configuration=configuration,
            complete_requested_germs=index==stop-1,requested_germs=[args.germ_start,stop],reports=all_reports,
            total_seconds=time.monotonic()-started,whole_negative_domain=args.germ_start==0 and stop==len(germs)))
    print(dict(complete_requested_germs=True,germs=len(all_reports),total_germs=len(germs),seconds=time.monotonic()-started),flush=True)


if __name__=='__main__':main()
