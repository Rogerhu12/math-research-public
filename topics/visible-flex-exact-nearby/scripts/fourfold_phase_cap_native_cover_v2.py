#!/usr/bin/env python3
"""Actual inner-cap energy with adaptive true Gaussian and angular tail budgets.

Every retained interval belongs to one exact scalar common span and one finite
trial element. Complete native primitive error, angular alias, analytic radial
tail, Gauss node/weight uncertainty and dyadic matrix selection are paid. A
small interval can use a fixed larger germ disk; near-coincident knots are
never merged. One completed FE at a time keeps memory and recovery bounded.
"""
from __future__ import annotations

import argparse
from bisect import bisect_right
from fractions import Fraction
import json
from pathlib import Path
import time

from flint import arb,acb,ctx
from fourfold_phase_beta_bulk_box import CBox,zeros
from fourfold_phase_beta_bulk_interval import exact_arb
from fourfold_phase_beta_interval import ball_record
from fourfold_phase_cap_energy_interval import (FiniteTrial,gauss_rule,sha,
    analytic_radial_moduli,angular_alias_fees,sampled_energy,hermitian_midpoint)
from fourfold_phase_cap_scaled_body import common_cells
from fourfold_phase_cap_vector_germs import VectorScaledBodyForm
from fourfold_phase_cap_wiener_cover import write_json,read_json


def paid_interval(target,trial,element,left,right,sigma,error_density,rules,
                  minimum_radius,max_order):
    half=exact_arb((right-left)/2);center=exact_arb((left+right)/2)
    length=2*half;goal=length*error_density
    aliases,angle_moduli=angular_alias_fees(target,trial,element,left,right,sigma)
    alias=[length*x for x in aliases]
    if not max(alias)<goal/3:
        raise ValueError('whole infinite angular alias exceeds its allocated interval error')
    attempts=[];chosen=None
    for nominal in (4,2):
        radius=max(nominal*half,minimum_radius)
        try:
            moduli=analytic_radial_moduli(target,trial,element,center,radius)
        except (ValueError,ZeroDivisionError) as exc:
            attempts.append(dict(nominal_factor=nominal,passed=False,reason=str(exc)))
            continue
        ratio=half/radius
        if not ratio<1:
            raise ValueError('true radial Gauss disk does not strictly contain the interval')
        for order in range(2,max_order+1):
            fees=[4*half*M*ratio**(2*order)/(1-ratio) for M in moduli]
            if max(fees)<goal/3:
                chosen=order,radius,moduli,fees
                break
        attempts.append(dict(nominal_factor=nominal,passed=chosen is not None,
            exact_radius=ball_record(radius),matrix_moduli=list(map(ball_record,moduli))))
        if chosen is not None:break
    if chosen is None:
        raise ValueError('no larger true radial disk paid the requested Gaussian budget: '+json.dumps(attempts))
    order,radius,moduli,radial_fees=chosen
    if order not in rules:rules[order]=gauss_rule(order)
    nodes,weights=rules[order]
    integrals=[zeros((trial.d,trial.d)),zeros((trial.d,trial.d))]
    for node,weight in zip(nodes,weights):
        values=sampled_energy(target,trial,element,acb(center+half*node))
        for j,value in enumerate(values):
            integrals[j]+=value*CBox.from_acb(acb(half*weight))
    energy=[]
    for j,value in enumerate(integrals):
        middle,rounding=hermitian_midpoint(value)
        total=(rounding+radial_fees[j]+alias[j]).upper()
        if not total<=goal:
            raise ValueError('true node/weight and primitive errors exceed the remaining interval budget')
        energy.append(dict(matrix_middle=[[[float(z.real),float(z.imag)] for z in row] for row in middle],
            full_operator_error=ball_record(total),directed_node_and_weight_error=ball_record(rounding),
            radial_Gauss_full_tail=ball_record(radial_fees[j].upper()),
            complete_angular_alias=ball_record(alias[j].upper()),
            analytic_radial_matrix_modulus=ball_record(moduli[j])))
    return dict(exact_radial_interval=[str(left),str(right)],finite_element=element,
        actual_common_span=list(map(str,target.cell)),gauss_order=order,
        true_radial_disk_radius=ball_record(radius),radial_outer_factor=ball_record(radius/half),
        complete_angular_form_moduli=list(map(ball_record,angle_moduli)),domain_attempts=attempts,
        primal_energy=energy[0],dual_energy=energy[1])


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--trial',type=Path,default=Path('notes/2026-11-12-cap-space-boundary4-interior16-P2.json'))
    parser.add_argument('--start-element',type=int,default=0)
    parser.add_argument('--stop-element',type=int,default=20)
    parser.add_argument('--bits',type=int,default=160)
    parser.add_argument('--primitive-nodes',type=int,default=256)
    parser.add_argument('--angles',type=int,default=1024)
    parser.add_argument('--normalized-strip',type=Fraction,default=Fraction(1,32))
    parser.add_argument('--minimum-analytic-radius',type=Fraction,default=Fraction(1,4096))
    parser.add_argument('--max-gauss-order',type=int,default=32)
    parser.add_argument('--max-depth',type=int,default=10)
    parser.add_argument('--error-per-length',type=Fraction,default=Fraction(1,10000))
    parser.add_argument('--seed',type=Path,default=Path('notes/2026-11-12-cap-scaled-true-energy-first-span.json'))
    parser.add_argument('--reuse-partial',type=Path)
    parser.add_argument('--out-dir',type=Path,required=True)
    parser.add_argument('--stop-file',type=Path)
    args=parser.parse_args();ctx.prec,ctx.cap=args.bits,4
    wall,cpu=time.monotonic(),time.process_time()
    trial=FiniteTrial(args.trial)
    if not 0<=args.start_element<args.stop_element<=trial.cells:
        raise ValueError('invalid actual finite-element interval')
    first,last=map(lambda j:Fraction(float(trial.mesh[j])),(args.start_element,args.stop_element))
    if not Fraction(1,4)<=first<last<=3:
        raise ValueError('native body cover excludes the separately defined natural graft')
    target=VectorScaledBodyForm(trial.object_path,args.primitive_nodes,args.angles,
        arb('.003'),arb('.0025'),arb('.32'))
    common=common_cells(target);rules={}
    seed=json.loads(args.seed.read_text())
    if (not seed['complete'] or seed['object_sha256']!=trial.report['object_sha256']
        or seed['trial_report_sha256']!=sha(args.trial)):
        raise ValueError('the completed seed energy belongs to a different true graph or exact trial')
    for name,digest in seed['dependency_sha256'].items():
        if sha(Path(__file__).with_name(name))!=digest:
            raise ValueError('a seed native proof dependency changed: '+name)
    if seed['source_sha256']!=sha(Path(__file__).with_name('fourfold_phase_cap_scaled_body.py')):
        raise ValueError('the seed native proof source changed')
    seed_interval=list(map(Fraction,seed['requested_exact_radial_interval']))
    reuse_rows=[];reuse_identity=None;reuse_element=None;reuse_end=None
    if args.reuse_partial is not None:
        partial=read_json(args.reuse_partial);old_identity=partial['identity']
        if (old_identity['source_sha256']!=sha(Path(__file__).with_name('fourfold_phase_cap_native_cover.py'))
            or old_identity['object_sha256']!=trial.report['object_sha256']
            or old_identity['trial_report_sha256']!=sha(args.trial)
            or old_identity['exact_trial_arrays']!=trial.report['arrays']
            or old_identity['completed_seed']!=dict(path=str(args.seed),sha256=sha(args.seed))):
            raise ValueError('the saved native prefix differs from the exact input or its paid kernel')
        for name,digest in old_identity['dependency_sha256'].items():
            if sha(Path(__file__).with_name(name))!=digest:
                raise ValueError('a saved prefix proof dependency changed: '+name)
        reuse_element=partial['element']
        start,end=map(lambda x:Fraction(float(x)),trial.mesh[reuse_element:reuse_element+2])
        if partial['exact_radial_interval']!=[str(start),str(end)]:
            raise ValueError('the saved native prefix uses a different finite trial element')
        cursor=start
        for row in sorted(partial['intervals'],key=lambda x:Fraction(x['exact_radial_interval'][0])):
            l,r=map(Fraction,row['exact_radial_interval'])
            if l!=cursor:break
            if not l<r<=end:raise ValueError('invalid completed interval in saved native prefix')
            for key in ('primal_energy','dual_energy'):
                if not arb(row[key]['full_operator_error']['ball']).is_finite():
                    raise ValueError('nonfinite previously paid energy error')
                if len(row[key]['matrix_middle'])!=trial.d or any(len(x)!=trial.d for x in row[key]['matrix_middle']):
                    raise ValueError('wrong matrix size in the saved native prefix')
            reuse_rows.append(row);cursor=r
        if not reuse_rows:raise ValueError('the old partial file has no contiguous completed prefix')
        reuse_end=cursor
        reuse_identity=dict(path=str(args.reuse_partial),sha256=sha(args.reuse_partial),
            source_sha256=old_identity['source_sha256'],element=reuse_element,
            exact_completed_prefix=[str(start),str(cursor)],completed_rows=len(reuse_rows))
    identity=dict(source_sha256=sha(__file__),
        dependency_sha256={name:sha(Path(__file__).with_name(name)) for name in (
            'fourfold_phase_cap_energy_interval.py','fourfold_phase_cap_scaled_body.py',
            'fourfold_phase_cap_vector_germs.py','fourfold_phase_cap_moment_space.py',
            'fourfold_phase_beta_bulk_box.py','fourfold_phase_beta_affine.py')},
        trial_report_path=str(args.trial),trial_report_sha256=sha(args.trial),
        exact_trial_arrays=trial.report['arrays'],object_sha256=trial.report['object_sha256'],
        exact_delta_fraction=trial.report['exact_delta_fraction'],bits=args.bits,
        primitive_nodes=args.primitive_nodes,angular_nodes=args.angles,
        normalized_angular_strip=str(args.normalized_strip),
        minimum_analytic_radius=str(args.minimum_analytic_radius),max_gauss_order=args.max_gauss_order,
        error_density_target=str(args.error_per_length),max_depth=args.max_depth,
        completed_seed=dict(path=str(args.seed),sha256=sha(args.seed)))
    identity['reused_completed_native_prefix']=reuse_identity
    manifest=dict(kind='true_native_inner_body_energy_cover',complete=False,identity=identity,
        requested_exact_radial_interval=[str(first),str(last)],
        requested_element_range=[args.start_element,args.stop_element],elements=[],
        full_positive_cap_complete=False,
        scope='Only the explicitly requested actual body cells. All true primitive, angular alias, radial Gaussian tail, and finite arithmetic fees are retained.')
    def checkpoint():
        manifest['CPU_seconds_this_invocation']=time.process_time()-cpu
        manifest['wall_seconds_this_invocation']=time.monotonic()-wall
        manifest['certified_gauss_rules']={str(n):dict(nodes=list(map(ball_record,x)),weights=list(map(ball_record,w)))
                                          for n,(x,w) in rules.items()}
        write_json(args.out_dir/'manifest.json',manifest)
    for element in range(args.start_element,args.stop_element):
        if args.stop_file is not None and args.stop_file.exists():
            manifest['stopped_between_elements']=True;checkpoint();break
        a,b=map(lambda x:Fraction(float(x)),trial.mesh[element:element+2])
        path=args.out_dir/f'element_{element:03d}.json.gz'
        if path.exists():
            old=read_json(path)
            if old.get('identity')!=identity or old.get('exact_radial_interval')!=[str(a),str(b)]:
                raise ValueError('saved native interval changed its source or actual mathematical input')
            if old.get('complete'):
                manifest['elements'].append(dict(element=element,path=str(path),sha256=sha(path),complete=True,
                    errors=old['integrated_operator_errors']))
                checkpoint();continue
        points=sorted({a,b}|{x for x in common if a<x<b}
            |({reuse_end} if element==reuse_element else set()))
        rows=[];failed=[];rejected=[]
        if element==reuse_element:
            for original in reuse_rows:
                copied=dict(original);copied['reused_completed_native_prefix']=reuse_identity
                rows.append(copied)
        report=dict(kind='true_native_inner_body_element_energy',complete=False,identity=identity,
            element=element,exact_radial_interval=[str(a),str(b)],original_common_span_count=len(points)-1,
            intervals=rows,failed=failed,rejected=rejected)
        local_wall,local_cpu=time.monotonic(),time.process_time()
        for left,right in zip(points,points[1:]):
            if element==reuse_element and right<=reuse_end:
                continue
            if [left,right]==seed_interval:
                for row in seed['intervals']:
                    copy=dict(row);copy['reused_completed_proof']=identity['completed_seed'];rows.append(copy)
                continue
            k=bisect_right(common,(left+right)/2)-1
            target.set_cell(common[k],common[k+1])
            pending=[(left,right,0)]
            while pending:
                l,r,depth=pending.pop()
                try:
                    row=paid_interval(target,trial,element,l,r,exact_arb(args.normalized_strip),
                        exact_arb(args.error_per_length),rules,exact_arb(args.minimum_analytic_radius),args.max_gauss_order)
                    row['subdivision_depth']=depth;rows.append(row)
                except (ValueError,ZeroDivisionError) as exc:
                    item=dict(exact_radial_interval=[str(l),str(r)],depth=depth,reason=str(exc))
                    if depth==args.max_depth:failed.append(item)
                    else:
                        rejected.append(item);mid=(l+r)/2
                        pending.extend([(mid,r,depth+1),(l,mid,depth+1)])
                report['CPU_seconds']=time.process_time()-local_cpu
                report['wall_seconds']=time.monotonic()-local_wall
                report['certified_gauss_rules']={str(n):dict(nodes=list(map(ball_record,x)),weights=list(map(ball_record,w)))
                                                  for n,(x,w) in rules.items()}
                write_json(path,report)
            print(json.dumps(dict(element=element,finished_common_span=[str(left),str(right)],
                accepted_intervals=len(rows),failed=len(failed),CPU_seconds=time.process_time()-local_cpu)),flush=True)
            if failed:break
        rows.sort(key=lambda row:Fraction(row['exact_radial_interval'][0]))
        cursor=a
        for row in rows:
            l,r=map(Fraction,row['exact_radial_interval'])
            if l!=cursor:break
            cursor=r
        report['complete']=not failed and cursor==b
        report['integrated_operator_errors']={key:ball_record(sum((
            arb(row[key]['full_operator_error']['ball']).upper() for row in rows),arb(0)).upper())
            for key in ('primal_energy','dual_energy')}
        write_json(path,report)
        manifest['elements'].append(dict(element=element,path=str(path),sha256=sha(path),
            complete=report['complete'],errors=report['integrated_operator_errors']))
        checkpoint()
        print(json.dumps(dict(element=element,complete=report['complete'],accepted=len(rows),failed=len(failed),
            errors={k:v['ball'] for k,v in report['integrated_operator_errors'].items()},
            CPU_seconds=report.get('CPU_seconds'),wall_seconds=report.get('wall_seconds'))),flush=True)
        if not report['complete']:raise SystemExit('native body interval incomplete; all partial matrices preserved')
        del rows,report
    manifest['complete']=all(x['complete'] for x in manifest['elements']) and len(manifest['elements'])==args.stop_element-args.start_element
    manifest['integrated_operator_errors']={key:ball_record(sum((arb(x['errors'][key]['ball']).upper()
        for x in manifest['elements']),arb(0)).upper()) for key in ('primal_energy','dual_energy')}
    checkpoint()


if __name__=='__main__':main()
