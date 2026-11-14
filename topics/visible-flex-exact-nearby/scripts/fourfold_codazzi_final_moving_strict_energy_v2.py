#!/usr/bin/env python3
"""Same actual four-state strict energy, with fresh true target cells to r_a.

The original [0,.238] cached arithmetic is preserved. Every new cell is
evaluated by the complete original full-target provider on its true scalar
germ and the actual fixed nu; no crossing-root cached K box is cropped.
The scalar-mean coefficient and true mean-interface costs are also retained.
This file was prepared during the runtime outage; no native result is implied.
"""
from __future__ import annotations
import argparse
from bisect import bisect_right
from fractions import Fraction
from pathlib import Path
import time

from flint import arb, ctx
import fourfold_codazzi_final_moving_strict_energy as base
from fourfold_codazzi_full_body_graft_target_jets import ReciprocalFullTargetJets
from fourfold_codazzi_curvature_angle_energy_prefix import polynomial_ranges,dyadic,read
from fourfold_codazzi_final_nu_return_derivative import EXPECTED_CANDIDATE,exact_w_value,CONTROL_LEFT,CONTROL_RIGHT
from fourfold_codazzi_moving_sobolev_rows import StrongDirectSums
from fourfold_codazzi_rotational_cap_jacobi import box_from_record
from fourfold_phase_beta_bulk_interval import exact_arb
from fourfold_phase_metric_defect import record,save,sha

KIND='actual_final_moving_four_state_fresh_negative_root_entry_and_scalar_mean'
BASE_RIGHT=Fraction(119,500)
DEFAULT_RIGHT=Fraction('0.2383878742994')


def fresh_identity(c,index):
    left,right=c['cuts'][index:index+2]
    if right<=BASE_RIGHT:
        lo,hi,j,k,row=base.identity(c,index)
        return lo,hi,j,k,row,'original_cached_complete_box',row['actual_scalar_germ']
    if left<BASE_RIGHT:raise ValueError('new target cells must split at the original strict endpoint')
    j=min(bisect_right(c['nodes'],left)-1,len(c['nodes'])-2)
    k=bisect_right(c['fresh_target'].cuts,left)-1
    gl,gr=c['fresh_target'].cuts[k:k+2]
    if not (c['nodes'][j]<=left<right<=c['nodes'][j+1] and gl<=left<right<=gr):
        raise ValueError('new candidate/actual-scalar refinement is incomplete')
    return left,right,j,None,None,'fresh_true_target_closed_box',list(map(str,(gl,gr)))


def prepare(args):
    if sha(args.candidate)!=EXPECTED_CANDIDATE:
        raise ValueError('restore the exact complete final ac1 candidate; a new centre requires a new explicit contract')
    if not 0<args.right<=DEFAULT_RIGHT:raise ValueError('this actual extension ends at the stated r_a')
    legacy=argparse.Namespace(**vars(args))
    legacy.right=min(args.right,BASE_RIGHT)
    c,doc=base.prepare(legacy)
    if sha(args.object)!=c['meta']['object_sha256']:
        raise ValueError('the exact same original intrinsic object is required')
    half=Fraction(doc['original_parameter_half_width'])
    if not 0<=half<=Fraction(1,10**9):raise ValueError('unexpected actual affine parameter range')
    target=ReciprocalFullTargetJets(args.object,half,512)
    if args.right>BASE_RIGHT:
        extra={BASE_RIGHT,args.right}
        extra.update(r for r in c['nodes']+target.cuts if BASE_RIGHT<r<args.right)
        c['cuts']=sorted(set(c['cuts'])|extra)
    c['fresh_target']=target
    doc.update(kind=KIND,source_sha256=sha(__file__),
        exact_requested_interval=['0',str(args.right)],
        total_closed_radial_cells=len(c['cuts'])-1,
        cached_prefix_end=str(min(args.right,BASE_RIGHT)),
        new_target_interval=None if args.right<=BASE_RIGHT else [str(BASE_RIGHT),str(args.right)],
        fresh_target_closed_cell_evaluation_required=True,
        no_root_crossing_cached_K_interval_is_cropped=True,
        scalar_mean_residual_sensitive_diagonal_retained=True,
        scalar_mean_multiplicative_and_nu_interface_fees_retained=True)
    doc['inputs'][str(args.object)]=sha(args.object)
    extra_dependencies=(
        'fourfold_codazzi_final_moving_strict_energy.py',
        'fourfold_codazzi_final_nu_return_derivative.py',
        'fourfold_codazzi_full_body_graft_target_jets.py',
        'fourfold_codazzi_reciprocal_compact_target_jets.py',
        'fourfold_codazzi_cubic_target_jets.py','fourfold_codazzi_high_target_jets.py',
        'fourfold_phase_cap_scaled_body.py','fourfold_phase_natural_exterior_graft.py',
        'fourfold_phase_exterior_entry_jet.py')
    doc['dependencies'].update({name:sha(Path(__file__).with_name(name)) for name in extra_dependencies})
    return c,doc


def scalar_mean(y,yr,a,alpha,m,aa):
    mm=a['s']+alpha*y[m]
    if not mm<0 or not aa>0:raise ValueError('actual scalar mean chart is unresolved')
    U2=alpha**2*sum((x*x for x in y[:m]),arb(0))/2
    V2=alpha**2*sum((x*x for x in y[m+1:]),arb(0))/2
    Var=U2+a['K']*V2
    R0=(alpha*yr[m]-a['beta']*alpha*y[m]
        *(1-a['K']*(mm*mm+mm*a['s']+a['s']**2))
        +a['beta']*mm*Var)
    cc=2*a['beta']*Var
    ct=cc-3*R0/mm
    return dict(actual_a=aa,actual_m=mm,nonmean_u_square=U2,
        nonmean_v_square=V2,actual_signed_variance=Var,
        actual_mean_residual=R0,nonmean_quadratic_diagonal=cc,
        residual_sensitive_mean_diagonal=ct,n=aa**2/mm**2,
        mean_transform_tau=-2*aa**2/mm**3,
        actual_reference_n=aa**2/a['s']**2)


def coefficient_row(c,index,sampler):
    left,right,j,k,row,kind,germ=fresh_identity(c,index)
    if kind=='original_cached_complete_box':
        a=base.target_bounds(row,left,right,c['nu'])
        aa=box_from_record(row['true_target_coefficients']['a'])
    else:
        values,actual=c['fresh_target'].coefficients(left,right,Fraction(c['meta']['exact_float_nu']))
        if list(map(str,actual))!=germ:raise ValueError('actual new scalar germ changed')
        a={name:values[name] for name in ('gamma','beta','K','K1','s','s1')}
        aa=values['a']
        if not a['K']<0:raise ValueError('a complete freshly evaluated target cell is not strictly negative')
        if not a['gamma']>0 or not a['s']<0:
            raise ValueError('a complete fresh rotational target chart is unresolved')
    y,yr=polynomial_ranges(c['saved'],c['nodes'],j,left,right)
    fields,_=sampler.fields(y,c['alpha'],a['s'])
    b,strong=base.direct_coefficients(y,fields,a,c['alpha'],c['modes'])
    sm=scalar_mean(y,yr,a,c['alpha'],c['modes'],aa)
    return dict(common_row=index,interval=list(map(str,(left,right))),
        candidate_piece=j,original_target_row=k,target_kind=kind,actual_scalar_germ=germ,
        actual_target={name:record(a[name]) for name in ('gamma','beta','K','K1','s')},
        base={name:record(v) for name,v in b.items()},
        strong={name:record(v) for name,v in strong.items()},
        scalar_mean={name:record(v) for name,v in sm.items()})


def complete_scalar_mean(c,doc):
    sm=[{name:box_from_record(value) for name,value in row['scalar_mean'].items()} for row in doc['rows']]
    Iminus=arb(0);signed=arb(0)
    for i,z in enumerate(sm):
        length=exact_arb(c['cuts'][i+1]-c['cuts'][i])
        ct=z['residual_sensitive_mean_diagonal']
        signed+=length*ct
        Iminus+=length*max(arb(0),-ct.lower()).upper()
    jump_log=arb(0);parameter_jump=arb(0);interfaces=[]
    for item in doc['jumps']:
        i=item['common_row'];r=Fraction(item['radius'])
        # A complete full-cell mean gap also bounds both exact one-sided
        # endpoint means. The exact dyadic mean jump was paid by base.
        gap=min((-sm[i-1]['actual_m']).lower(),(-sm[i]['actual_m']).lower()).lower()
        if not gap>0:raise ValueError('a true two-sided mean interface gap is unresolved')
        jm=box_from_record(item['exact_mean_jump']).upper()
        e=(jm/gap).upper()
        logfee=(3*e).upper();jump_log+=logfee
        # Since the genuine rotational gap is positive, 0<=rho<1.
        # tau+/tau-=(1-dm/mplus)^3; retain all three exact powers.
        ratio_fee=(3*e+3*e**2+e**3).upper()
        w=exact_arb(exact_w_value(r)) if CONTROL_LEFT<r<CONTROL_RIGHT else arb(0)
        shifted=(w*ratio_fee).upper();parameter_jump+=shifted
        interfaces.append(dict(common_row=i,radius=str(r),true_two_sided_mean_gap=record(gap),
            exact_mean_jump_abs=record(jm),multiplicative_backward_log_fee=record(logfee),
            complete_tau_ratio_difference_upper=record(ratio_fee),
            reference_subtracted_nu_interface_source_upper=record(shifted)))
    loggamma=(Iminus+jump_log).upper()
    doc['scalar_mean_full_bounds']=dict(
        exact_requested_interval=doc['exact_requested_interval'],
        actual_signed_diagonal_integral=record(signed),
        actual_negative_diagonal_integral_upper=record(Iminus.upper()),
        complete_multiplicative_interface_log_upper=record(jump_log.upper()),
        complete_log_uniform_factor_upper=record(loggamma),
        complete_reference_subtracted_nu_interface_sum_upper=record(parameter_jump.upper()),
        interfaces=interfaces,
        complete_mean_given_nonmean_scalar_only=True,
        mean_or_nu_scalar_not_deleted=True,
        whole_body_inverse_proved=False)
    # Avoid serializing inf when a valid but very broad log bound is large.
    doc['scalar_mean_full_bounds']['uniform_factor_if_log_less_than_100']=(
        record(loggamma.exp().upper()) if loggamma<100 else None)


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--candidate',type=Path,required=True)
    p.add_argument('--object',type=Path,default=Path('data/phase_ring_continuation/type_fixed_step02_d5_exact_affine_step5_object.json'))
    p.add_argument('--target',type=Path,default=Path('notes/2026-11-13-Codazzi-true-target-r02-v1-native.json.gz'))
    p.add_argument('--collar',type=Path,default=Path('notes/2026-11-13-R133-actual-root-collar-complete-coefficients-v2-native.json.gz'))
    p.add_argument('--type-cover',type=Path,default=Path('notes/2026-11-13-R133-compact-nu-full-type-cover-native.json.gz'))
    p.add_argument('--right',type=Fraction,default=DEFAULT_RIGHT)
    p.add_argument('--angles',type=int,default=1024)
    p.add_argument('--resume',type=Path);p.add_argument('--max-new-rows',type=int)
    p.add_argument('--out',type=Path,required=True)
    args=p.parse_args();ctx.prec=320;ctx.cap=6;started=time.monotonic()
    if args.out.exists():raise FileExistsError('preserve all earlier complete, partial and failed records')
    c,doc=prepare(args)
    if args.resume:
        old=read(args.resume)
        for name in ('kind','source_sha256','inputs','candidate_metadata','exact_nu','exact_amplitude',
                     'exact_requested_interval','total_closed_radial_cells','closed_angular_cells','dependencies'):
            if old[name]!=doc[name]:raise ValueError('complete saved-prefix identity changed: '+name)
        if old['failure'] is not None or old['complete']:
            raise ValueError('only a successful saved complete-row prefix can resume')
        for index,row in enumerate(old['rows']):
            left,right,j,k,actual,kind,germ=fresh_identity(c,index)
            if (row['common_row']!=index or row['interval']!=list(map(str,(left,right)))
                or row['candidate_piece']!=j or row['original_target_row']!=k
                or row['target_kind']!=kind or row['actual_scalar_germ']!=germ):
                raise ValueError('a saved complete row changed its genuine mathematical cell')
        doc['rows']=old['rows'];doc['resume_history']=old['resume_history']+[
            dict(path=str(args.resume),sha256=sha(args.resume),saved_complete_rows=len(old['rows']),
                 original_complete=False,missing_exit_status_not_inferred=True)]
    first=len(doc['rows']);last=len(c['cuts'])-1
    if args.max_new_rows is not None:
        if args.max_new_rows<=0:raise ValueError('positive explicit new-row count required')
        last=min(last,first+args.max_new_rows)
    sampler=StrongDirectSums(c['modes'],args.angles);checkpoint=time.monotonic()
    try:
        for index in range(first,last):
            doc['rows'].append(coefficient_row(c,index,sampler))
            if time.monotonic()-checkpoint>15:
                doc['wall_seconds']=time.monotonic()-started;save(args.out,doc)
                print(dict(rows=len(doc['rows']),total=len(c['cuts'])-1,
                           right=doc['rows'][-1]['interval'][1]),flush=True)
                checkpoint=time.monotonic()
        if len(doc['rows'])==len(c['cuts'])-1:
            base.complete_comparison(c,doc)
            complete_scalar_mean(c,doc)
            doc['fresh_target_evaluated_closed_cell_count']=sum(row['target_kind']=='fresh_true_target_closed_box' for row in doc['rows'])
        else:doc['explicit_saved_complete_row_prefix_only']=True
    except Exception as exc:
        doc['complete']=False
        doc['failure']=dict(type=type(exc).__name__,message=str(exc))
        raise
    finally:
        doc['wall_seconds']=time.monotonic()-started;save(args.out,doc)
    print(dict(complete=doc['complete'],failure=doc['failure'],rows=len(doc['rows']),
               requested=doc['exact_requested_interval'],out=str(args.out)),flush=True)


if __name__=='__main__':
    main()
