#!/usr/bin/env python3
"""Full final-centre scalar mean Green from already certified target boxes.

No primitive or angular solver is rerun. Three original complete coefficient
covers are joined exactly and refined with every actual PPoly node. The
control changes E,K,s only inside its original support. All true m jumps
and the reference-subtracted nu interface column remain in the budget.
This producer was prepared during the runtime outage; no native run is
claimed until its complete output exists.
"""
from __future__ import annotations
import argparse
from bisect import bisect_right
from fractions import Fraction
import json
from pathlib import Path
import time

from flint import arb,ctx
from fourfold_codazzi_candidate_shards import load_candidate
from fourfold_codazzi_curvature_angle_energy_prefix import read,dyadic,polynomial_ranges,actual_jump,bump_jets
from fourfold_codazzi_moving_actual_R_boundary import COORDINATES
from fourfold_codazzi_final_nu_return_derivative import EXPECTED_CANDIDATE,exact_w_value,CONTROL_LEFT,CONTROL_RIGHT
from fourfold_codazzi_final_moving_strict_energy_v2 import scalar_mean
from fourfold_codazzi_rotational_cap_jacobi import box_from_record
from fourfold_phase_beta_bulk_interval import exact_arb
from fourfold_phase_metric_defect import record,save,sha

KIND='actual_final_complete_scalar_mean_Green_cached_full_target'
EXPECTED={
 'prefix':'2307b288a1c8c0597e205d154a1d7d587cf907af614a40cc1ef8935f849d6a63',
 'collar':'b4aaff3190d8a76ebadd6ab0c2772181bbb00c91e6d2037a9e8d58d5710dbcc8',
 'positive':'3a89805ebe1ab22000529a7a8c2fdc262b1c3a2afbc52433cf610d2d6542ff22'}
RIGHT=Fraction(25,8)


def nonnegative(x):
    if x.upper()<0:raise ValueError('a true nonnegative scalar quantity lost its enclosure')
    return x.intersection(arb(0).union(x.upper()))


def target_values(item,left,right,nu):
    row=item['row']
    if item['kind']=='positive':
        if left<Fraction(239,1000):raise ValueError('the unchanged positive cache starts at .239')
        z={k:box_from_record(row['coefficients'][k]) for k in ('a','gamma','beta','K','Cref')}
        if not z['Cref']<0 or not z['a']>0 or not z['gamma']>0:
            raise ValueError('the original true positive rotational chart is unresolved')
        a=z['a'];s=1/z['Cref']
        return dict(a=a,gamma=z['gamma'],beta=z['beta'],K=z['K'],s=s,
                    s1=z['beta']*s*(1-z['K']*s*s))
    z={k:box_from_record(row['true_target_coefficients'][k]) for k in ('a','a1','E','K','beta')}
    w,w1,_=bump_jets(left,right)
    E=z['E']*(nu*w).exp();gap=E-z['a1']**2
    if not z['a']>0 or not E>0 or not gap>0:
        raise ValueError('the complete controlled rotational chart is unresolved')
    K=(z['K']+nu*z['beta']*w1/(2*z['E']))/((nu*w).exp())
    s=-z['a']*(E/gap).sqrt()
    return dict(a=z['a'],gamma=E.sqrt()/z['a'],beta=z['beta'],K=K,s=s,
                s1=z['beta']*s*(1-K*s*s))


def prepare(args):
    if sha(args.candidate)!=EXPECTED_CANDIDATE:
        raise ValueError('only the restored exact full final ac1 candidate is supported')
    saved=load_candidate(args.candidate);meta=json.loads(str(saved['metadata']))
    if meta['coordinates']!=COORDINATES:raise ValueError('the actual moving angle coordinate changed')
    alphaq=Fraction(meta['exact_float_amplitude']);nuq=Fraction(meta['exact_float_nu'])
    if alphaq!=dyadic(meta['amplitude']) or nuq!=dyadic(meta['nu']):
        raise ValueError('the exact binary64 parameter identities changed')
    sources={};items=[]
    for kind in ('prefix','collar','positive'):
        path=getattr(args,kind)
        if sha(path)!=EXPECTED[kind]:raise ValueError('restore the exact complete original '+kind+' coefficient certificate')
        doc=read(path);sources[kind]=doc
        if not doc['complete'] or doc['object_sha256']!=meta['object_sha256']:
            raise ValueError('the actual cached target object is incomplete or differs')
        if Fraction(doc['parameter_half_width'])!=Fraction(1,10**9):
            raise ValueError('the original entire affine parameter interval changed')
        for index,row in enumerate(doc['rows']):
            items.append(dict(kind=kind,index=index,row=row))
    if not sources['positive']['cap_linear_reference_certified']:
        raise ValueError('the original complete positive reference failed its actual gates')
    endpoint=Fraction(0)
    for item in items:
        left,right=map(Fraction,item['row']['interval'])
        gl,gr=map(Fraction,item['row']['actual_scalar_germ'])
        if left!=endpoint or not left<right or not gl<=left<right<=gr:
            raise ValueError('the three actual target covers lost complete adjacency or a real germ')
        endpoint=right
    if endpoint!=RIGHT:raise ValueError('the actual coefficient union is not the full body through R')
    nodes=list(map(dyadic,saved['radial_nodes']))
    if nodes[0]!=0 or nodes[-1]!=RIGHT:raise ValueError('the full saved candidate does not cover the stated body')
    tn=[Fraction(item['row']['interval'][0]) for item in items]+[RIGHT]
    cuts=sorted(set(nodes)|set(tn)|{CONTROL_LEFT,CONTROL_RIGHT})
    context=dict(saved=saved,meta=meta,nodes=nodes,items=items,tn=tn,cuts=cuts,
                 m=int(meta['modes']),alpha=exact_arb(alphaq),nu=exact_arb(nuq))
    doc=dict(kind=KIND,source_sha256=sha(__file__),complete=False,failure=None,
        candidate_sha256=EXPECTED_CANDIDATE,candidate_metadata=meta,
        exact_amplitude=str(alphaq),exact_nu=str(nuq),exact_interval=['0',str(RIGHT)],
        inputs={str(getattr(args,k)):sha(getattr(args,k)) for k in ('candidate','prefix','collar','positive')},
        whole_original_affine_parameter_interval=True,original_parameter_half_width='1/1000000000',
        complete_original_primitive_tail_reused=True,
        no_fresh_native_target_or_angular_solver_used=True,
        complete_mean_given_nonmean_only=True,all_variation_Fourier_modes_retained=True,
        variation_coordinates='physical h=(delta u,delta v), actual delta nu; not alpha-normalized',
        complete_mean_source_and_independent_response_jumps_retained=True,
        no_inverse_turning_weight=True,actual_body_inverse_proved=False,
        actual_nu_scalar_nonzero_proved=False,independent_outer_cap_mean_and_fB_retained=True,
        total_closed_cells=len(cuts)-1,rows=[],interfaces=[],resume_history=[],
        dependencies={name:sha(Path(__file__).with_name(name)) for name in (
            'fourfold_codazzi_candidate_shards.py','fourfold_codazzi_curvature_angle_energy_prefix.py',
            'fourfold_codazzi_moving_actual_R_boundary.py','fourfold_codazzi_final_nu_return_derivative.py',
            'fourfold_codazzi_final_moving_strict_energy_v2.py',
            'fourfold_codazzi_rotational_cap_jacobi.py','fourfold_phase_beta_bulk_interval.py',
            'fourfold_phase_metric_defect.py')})
    return context,doc


def identity(c,index):
    left,right=c['cuts'][index:index+2]
    j=min(bisect_right(c['nodes'],left)-1,len(c['nodes'])-2)
    k=bisect_right(c['tn'],left)-1;item=c['items'][k]
    l,r=map(Fraction,item['row']['interval'])
    if not c['nodes'][j]<=left<right<=c['nodes'][j+1] or not l<=left<right<=r:
        raise ValueError('a complete actual candidate/target refinement was lost')
    return left,right,j,k,item


def row_budget(c,index):
    left,right,j,k,item=identity(c,index)
    a=target_values(item,left,right,c['nu'])
    y,yr=polynomial_ranges(c['saved'],c['nodes'],j,left,right)
    z=scalar_mean(y,yr,a,c['alpha'],c['m'],a['a'])
    # Orthogonality is exact on the entire moving circle. The interval
    # radius is radial/target uncertainty, not an omitted Fourier tail.
    U2=nonnegative(z['nonmean_u_square'])
    V2=nonnegative(z['nonmean_v_square'])
    n=z['n'];beta=a['beta'];K=a['K'];gamma=a['gamma']
    w,w1,_=bump_jets(left,right)
    rho=(1-z['actual_reference_n']).intersection(arb(0).union(arb(1)))
    Knu=-K*w+beta*w1/(2*gamma**2*a['a']**2)
    reduced=z['residual_sensitive_mean_diagonal']*rho*w+2*beta*n*V2*Knu
    nonmean=(4*abs(beta)*n*(U2+K**2*V2).sqrt()).upper()
    z.update(actual_rho=rho,actual_K_nu=Knu,
             reduced_nu_mean_source=reduced,
             ordinary_nonmean_L2_to_transformed_mean_rate=nonmean,
             ordinary_mean_source_rate=z['mean_transform_tau'])
    return dict(common_row=index,interval=list(map(str,(left,right))),candidate_piece=j,
        target_union_row=k,target_kind=item['kind'],original_target_row=item['index'],
        actual_scalar_germ=item['row']['actual_scalar_germ'],
        actual_target={name:record(a[name]) for name in ('a','gamma','beta','K','s')},
        scalar_mean={name:record(value) for name,value in z.items()})


def complete_bounds(c,doc):
    if len(doc['rows'])!=len(c['cuts'])-1:raise ValueError('a prefix cannot be called the complete scalar Green')
    z=[{k:box_from_record(v) for k,v in row['scalar_mean'].items()} for row in doc['rows']]
    Iminus=arb(0);signed=arb(0);jlog=arb(0);jnu=arb(0)
    f_nonmean=arb(0);f_mean=arb(0);f_nu=arb(0)
    f_nonmean2=arb(0);f_mean2=arb(0)
    lengths=[];invtaus=[];taumax=[];rate_nm=[];rate_mean=[];rate_nu=[];direct_nu=[]
    for i,row in enumerate(z):
        length=exact_arb(c['cuts'][i+1]-c['cuts'][i])
        ct=row['residual_sensitive_mean_diagonal']
        signed+=length*ct;Iminus+=length*max(arb(0),-ct.lower()).upper()
        f_nonmean+=length*row['ordinary_nonmean_L2_to_transformed_mean_rate'].upper()
        f_mean+=length*row['ordinary_mean_source_rate'].upper()
        f_nu+=length*abs(row['reduced_nu_mean_source']).upper()
        tau=row['mean_transform_tau']
        if not tau>0:raise ValueError('the complete positive scalar conjugating factor is unresolved')
        lengths.append(length);invtaus.append((1/tau.lower()).upper());taumax.append(tau.upper())
        rate_nm.append(row['ordinary_nonmean_L2_to_transformed_mean_rate'].upper())
        rate_mean.append(tau.upper());rate_nu.append(abs(row['reduced_nu_mean_source']).upper())
        w,_,_=bump_jets(c['cuts'][i],c['cuts'][i+1])
        direct_nu.append(abs(row['actual_rho']*w/tau).upper())
        f_nonmean2+=length*rate_nm[-1]**2;f_mean2+=length*rate_mean[-1]**2
    m=c['m'];nu_atoms=[arb(0) for row in doc['rows']]
    jump_waist_before_invtau0=arb(0);jump_output_L2=arb(0);prefix_invtau2=arb(0)
    # Arbitrary response jump data may occur at every common interface,
    # even where the actual centre itself is continuous. Their l1 norm
    # is a separate input, never absorbed into the candidate mean jumps.
    for i in range(1,len(doc['rows'])):
        prefix_invtau2+=lengths[i-1]*invtaus[i-1]**2
        jump_waist_before_invtau0=max(jump_waist_before_invtau0,taumax[i]).upper()
        jump_output_L2=max(jump_output_L2,taumax[i]*prefix_invtau2.sqrt()).upper()
    for i in range(1,len(doc['rows'])):
        if doc['rows'][i-1]['candidate_piece']==doc['rows'][i]['candidate_piece']:continue
        j=doc['rows'][i]['candidate_piece'];r=c['nodes'][j]
        if r!=c['cuts'][i]:raise ValueError('a real mean join is not in the full closed cover')
        exact=actual_jump(c['saved'],c['nodes'],j)
        jump=(abs(c['alpha']*exact_arb(exact[m]))).upper()
        gap=min((-z[i-1]['actual_m']).lower(),(-z[i]['actual_m']).lower()).lower()
        if not gap>0:raise ValueError('a complete two-sided mean gap is unresolved')
        e=(jump/gap).upper();lf=(3*e).upper()
        ratio=(3*e+3*e**2+e**3).upper()
        w=exact_arb(exact_w_value(r)) if CONTROL_LEFT<r<CONTROL_RIGHT else arb(0)
        rho_upper=min(z[i-1]['actual_rho'].upper(),z[i]['actual_rho'].upper()).upper()
        nf=(rho_upper*w*ratio).upper()
        jlog+=lf;jnu+=nf;nu_atoms[i]=nf
        doc['interfaces'].append(dict(common_row=i,candidate_join=j,radius=str(r),
            exact_mean_jump_abs=record(jump),two_sided_mean_gap=record(gap),
            complete_backward_log_fee=record(lf),
            complete_tau_ratio_minus_one_abs=record(ratio),
            full_reference_subtracted_nu_interface_fee=record(nf)))
    loggamma=(Iminus+jlog).upper()
    invtau0=(arb(107)/100)**3/(2*(arb(53436641)/50000000)**2)
    # The following strict endpoint constants were separately proved for
    # this exact candidate, including its whole original eta interval.
    coefficients=dict(
        outer_mean_z=arb('2.693551e-13'),
        outer_physical_Cmean=arb('9.061105e-12'),
        true_cap_DZ_mean=arb('6.680588e-18'),
        independent_fB_dotH2_mean=arb('7.422875e-19'),
        nonmean_Linfty_r_L2_feedback=(invtau0*f_nonmean).upper(),
        ordinary_mean_source_Linfty_r=(invtau0*f_mean).upper(),
        nonmean_L2_rphi_feedback=(invtau0*f_nonmean2.sqrt()).upper(),
        ordinary_mean_source_L2_r=(invtau0*f_mean2.sqrt()).upper(),
        independent_response_mean_jumps_l1=(invtau0*jump_waist_before_invtau0).upper(),
        reference_subtracted_nu_body_and_interface=(invtau0*(f_nu+jnu)).upper())
    # Entire-body L2 bounds use a positive separable majorant of the
    # triangular kernel: 1_{r<t} invtau(r) rate(t). The true radial
    # direction is kept; no supremum over unrelated t<r is introduced.
    def schur(rate):
        suffix=arb(0);rownorm=arb(0);prefix=arb(0);colnorm=arb(0)
        for i in range(len(rate)-1,-1,-1):
            suffix+=lengths[i]*rate[i]
            rownorm=max(rownorm,invtaus[i]*suffix).upper()
        for i in range(len(rate)):
            prefix+=lengths[i]*invtaus[i]
            colnorm=max(colnorm,rate[i]*prefix).upper()
        return (rownorm*colnorm).sqrt().upper(),rownorm,colnorm
    Snm,Rnm,Cnm=schur(rate_nm);Sm,Rm,Cm=schur(rate_mean)
    invtau_L2=sum((lengths[i]*invtaus[i]**2 for i in range(len(lengths))),arb(0)).sqrt().upper()
    nu_body_suffix=arb(0);nu_atom_suffix=arb(0);nu_output2=arb(0);nu_direct2=arb(0)
    for i in range(len(lengths)-1,-1,-1):
        nu_body_suffix+=lengths[i]*rate_nu[i]
        # The atom at the left endpoint of cell i acts only to its left.
        output=(invtaus[i]*(nu_body_suffix+nu_atom_suffix)).upper()
        nu_output2+=lengths[i]*output**2
        nu_direct2+=lengths[i]*direct_nu[i]**2
        nu_atom_suffix+=nu_atoms[i]
    outer_tau=(2*arb('0.000007')**2/(arb(29)/5)**3).upper()
    outer_physical=(2*arb('0.000007')**2/(arb(29)/5)).upper()
    whole_coefficients=dict(
        raw_outer_mean_z=(outer_tau*invtau_L2).upper(),
        outer_physical_Cmean=(outer_physical*invtau_L2).upper(),
        true_cap_DZ_mean=(outer_physical*invtau_L2*arb('7.372818e-7')).upper(),
        independent_fB_dotH2_mean=(outer_physical*invtau_L2*arb('8.1920198958e-8')).upper(),
        ordinary_mean_source_L2_r=Sm,
        nonmean_L2_rphi_feedback=Snm,
        independent_response_mean_jumps_l1=jump_output_L2,
        reduced_nu_body_and_interface=nu_output2.sqrt().upper())
    doc.update(complete=True,whole_radial_body=True,
        all_exact_mean_interfaces_retained=True,
        all_reference_subtracted_parameter_interfaces_retained=True,
        bounds=dict(
            signed_residual_sensitive_diagonal_integral=record(signed),
            negative_diagonal_integral_upper=record(Iminus.upper()),
            full_interface_log_upper=record(jlog.upper()),
            complete_log_Gamma_upper=record(loggamma),
            complete_reduced_nu_body_integral_upper=record(f_nu.upper()),
            complete_reduced_nu_interface_sum_upper=record(jnu.upper()),
            full_body_L2_coefficients_still_to_multiply_by_Gamma={name:record(v) for name,v in whole_coefficients.items()},
            full_body_direct_nu_contact_L2=record(nu_direct2.sqrt().upper()),
            complete_triangular_Schur_integral_upper=dict(
                nonmean_row=record(Rnm),nonmean_column=record(Cnm),
                mean_source_row=record(Rm),mean_source_column=record(Cm)),
            coefficients_still_to_multiply_by_Gamma={name:record(v) for name,v in coefficients.items()},
            complete_full_body_mean_gain_if_log_Gamma_below_100=(
                {name:record((loggamma.exp()*v).upper()) for name,v in whole_coefficients.items()} if loggamma<100 else None),
            complete_waist_mean_gain_if_log_Gamma_below_100=(
                {name:record((loggamma.exp()*v).upper()) for name,v in coefficients.items()} if loggamma<100 else None)),
        output_scope='Whole-body L2 and waist mean scalar bounds given the full nonmean field/source, independent outer rows and all response jumps; not a whole coupled inverse or a scalar nonzero claim',
        actual_body_inverse_proved=False,actual_nu_scalar_nonzero_proved=False)


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--candidate',type=Path,required=True)
    p.add_argument('--prefix',type=Path,default=Path('notes/2026-11-13-Codazzi-true-target-r02-v1-native.json.gz'))
    p.add_argument('--collar',type=Path,default=Path('notes/2026-11-13-R133-actual-root-collar-complete-coefficients-v2-native.json.gz'))
    p.add_argument('--positive',type=Path,default=Path('notes/2026-11-13-Codazzi-rotational-positive-cap-v2-native.json.gz'))
    p.add_argument('--resume',type=Path);p.add_argument('--max-new-rows',type=int)
    p.add_argument('--out',type=Path,required=True)
    args=p.parse_args();ctx.prec=320;ctx.cap=6;started=time.monotonic()
    if args.out.exists():raise FileExistsError('preserve all earlier complete, partial and failed attempts')
    c,doc=prepare(args)
    if args.resume:
        old=read(args.resume)
        for key in ('kind','source_sha256','candidate_sha256','candidate_metadata','exact_amplitude','exact_nu',
                    'exact_interval','inputs','total_closed_cells','dependencies'):
            if old[key]!=doc[key]:raise ValueError('saved complete-prefix identity changed: '+key)
        if old['complete'] or old['failure'] is not None:
            raise ValueError('only a successful exact saved-row prefix may resume')
        for i,row in enumerate(old['rows']):
            l,r,j,k,item=identity(c,i)
            if (row['common_row']!=i or row['interval']!=list(map(str,(l,r)))
                or row['candidate_piece']!=j or row['target_union_row']!=k
                or row['target_kind']!=item['kind'] or row['original_target_row']!=item['index']
                or row['actual_scalar_germ']!=item['row']['actual_scalar_germ']):
                raise ValueError('an actual saved scalar row changed its mathematical domain')
        doc['rows']=old['rows'];doc['resume_history']=old['resume_history']+[
            dict(path=str(args.resume),sha256=sha(args.resume),saved_complete_rows=len(old['rows']),
                 original_complete=False,missing_exit_code_not_inferred=True)]
    first=len(doc['rows']);last=len(c['cuts'])-1
    if args.max_new_rows is not None:
        if args.max_new_rows<=0:raise ValueError('positive explicit new-row count required')
        last=min(last,first+args.max_new_rows)
    checkpoint=time.monotonic()
    try:
        for i in range(first,last):
            doc['rows'].append(row_budget(c,i))
            if time.monotonic()-checkpoint>15:
                doc['wall_seconds']=time.monotonic()-started;save(args.out,doc)
                print(dict(rows=len(doc['rows']),total=len(c['cuts'])-1,
                           right=doc['rows'][-1]['interval'][1]),flush=True)
                checkpoint=time.monotonic()
        if len(doc['rows'])==len(c['cuts'])-1:complete_bounds(c,doc)
        else:doc['explicit_saved_complete_row_prefix_only']=True
    except Exception as exc:
        doc['complete']=False;doc['failure']=dict(type=type(exc).__name__,message=str(exc));raise
    finally:
        doc['wall_seconds']=time.monotonic()-started;save(args.out,doc)
    print(dict(complete=doc['complete'],failure=doc['failure'],rows=len(doc['rows']),
               interval=doc['exact_interval'],out=str(args.out)),flush=True)


if __name__=='__main__':
    main()
