#!/usr/bin/env python3
"""Actual full-mode radial decay and growing analytic width on a true cap.

The weight is W_m(r)=(a(r)/a(L))**(mu+tau*abs(m)).
The true zero-outer-port member of the already proved centred cap is used.
All Fourier modes, both mean equations and the true regular Jacobi fee remain.
This is curvature screening, not a height/flux map or a regular-tail match.
"""
from __future__ import annotations
import argparse,gzip,json
from fractions import Fraction
from pathlib import Path
import numpy as np
from flint import arb,ctx
from fourfold_codazzi_rotational_cap_jacobi import box_from_record
from fourfold_codazzi_candidate_shards import load_candidate
from fourfold_codazzi_cap_centered_residual_v5 import polynomials,total
from fourfold_codazzi_cap_open_curvature_ports_v2 import trace
from fourfold_phase_beta_bulk_box import arb_box
from fourfold_phase_beta_bulk_interval import exact_arb
from fourfold_phase_metric_defect import record,save,sha


def read(path):return json.loads(gzip.decompress(Path(path).read_bytes()))


def row_constants(v,ql,qu,mu,tau):
    g,b,ell=v['gamma'],v['beta'],v['lambda_ref']
    if not g>0 or not b<0 or not ell>0 or not ql>0:
        raise ValueError('the true positive cap chart is missing')
    q=ql.union(qu);t=-b/g
    # For every M>=4 the C normalized rate is at least this expression.
    cn=(q-t*(tau+(ell+1+mu)/4)).lower()
    dn=(q+tau*t).lower()
    values=dict(normalized_D_rate_lower=dn,normalized_C_rate_lower=cn,
        gamma_lower=g.lower(),q_lower=ql,q_upper=qu,
        ell_lower=ell.lower(),ell_upper=ell.upper(),Cref_abs_lower=(-v['Cref']).lower())
    if not cn>0 or not dn>0:return values,False
    # The exact D source ratio is fractional-linear in y=1/M, so its
    # extrema on all frequencies occur at y=0 or y=1/4.
    KD=max(((1+q*t*y)/(q+tau*t+(2+mu)*t*y)).upper()
           for y in (arb(0),arb(1)/4)).upper()
    values.update(triangular_coupling=(1/cn).upper(),nonlinear_D_kernel=KD,
        nonlinear_C_kernel=(t/(4*(q-t*(tau+(ell+1+mu)/4)))).upper(),
        mean_nonlinear_kernel=(1/(ell.lower()+1+mu)).upper())
    return values,True


def aggregate(rows):
    q=max(r['q_upper'] for r in rows).upper()
    T=max(r['triangular_coupling'] for r in rows).upper()
    KD=max(r['nonlinear_D_kernel'] for r in rows).upper()
    KC=max(r['nonlinear_C_kernel'] for r in rows).upper()
    Km=max(r['mean_nonlinear_kernel'] for r in rows).upper()
    HD=(1+(1+q)*T).upper();HC=(1+q).upper()
    K=max(Km,HD*KD+(1+q)*KC).upper()
    Cmin=min(r['Cref_abs_lower'] for r in rows).lower()
    ell=max(arb(1),max(r['ell_upper'] for r in rows)).upper()
    return dict(q_upper=q,triangular_coupling=T,nonlinear_D_kernel=KD,
        nonlinear_C_kernel=KC,mean_nonlinear_kernel=Km,boundary_D=HD,boundary_C=HC,
        complete_pair_nonlinear_kernel=K,Cref_abs_lower=Cmin,ell_upper=ell)


def ball(const,radius,inner):
    C=const['Cref_abs_lower'];L=const['ell_upper'];K=const['complete_pair_nonlinear_kernel']
    denominator=(C-radius).lower()
    if not denominator>0:return dict(passed=False,denominator_positive=False)
    Q=(L*radius*radius/denominator).upper()
    DQ=(L*(2*radius/denominator+radius*radius/(denominator*denominator))).upper()
    lip=(K*DQ).upper();image=(const['boundary_C']*inner+K*Q).upper()
    return dict(passed=bool(lip<1 and image<radius),denominator_positive=True,
        radius=record(radius),Q_bound=record(Q),DQ_bound=record(DQ),
        contraction=record(lip),image=record(image),
        image_margin=record((radius-image).lower()),denominator_lower=record(denominator))


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--reference',type=Path,default=Path('notes/2026-11-13-Codazzi-rotational-positive-cap-v2-native.json.gz'))
    ap.add_argument('--kernels',type=Path,default=Path('notes/2026-11-13-R133-A0-driven-cap-r1-native.json.gz'))
    ap.add_argument('--cap',type=Path,default=Path('notes/2026-11-13-R133-centered-cap-r1-v4-jumps-native.json.gz'))
    ap.add_argument('--regularity',type=Path,default=Path('notes/2026-11-13-R133-centered-cap-r1-regularity-native.json.gz'))
    ap.add_argument('--candidate',type=Path,default=Path('notes/2026-11-13-R133-compact-metric-outer-mean-m64-candidate.npz.gz'))
    ap.add_argument('--left',type=Fraction,default=Fraction(3,2))
    ap.add_argument('--mu',type=Fraction,default=Fraction(4,3))
    ap.add_argument('--tau',type=Fraction,default=Fraction(1,64))
    ap.add_argument('--radius',type=Fraction,default=Fraction(1,2500))
    ap.add_argument('--out',type=Path,required=True)
    args=ap.parse_args();ctx.prec=320
    if args.out.exists():raise FileExistsError('use a distinct actual screening result')
    if args.mu<=0 or args.tau<=0 or args.radius<=0:raise ValueError('positive exact weights and radius required')
    native,kernels,cap,reg=(read(p) for p in (args.reference,args.kernels,args.cap,args.regularity))
    if (not native['complete'] or not native['cap_linear_reference_certified']
        or native['source_sha256']!=sha(Path(__file__).with_name('fourfold_codazzi_rotational_cap_jacobi_v2.py'))
        or not kernels['complete'] or not kernels['unweighted_nonzero_rates_positive']
        or not kernels['backward_mean_rates_positive'] or kernels['input_sha256']!=sha(args.reference)
        or not cap['complete'] or not cap['actual_driven_cap_exists'] or not cap['actual_solution_radially_continuous']
        or not reg['complete'] or not reg['all_exact_radial_interface_point_sources_paid']
        or reg['input_sha256']!=sha(args.cap) or reg['kernels_sha256']!=sha(args.kernels)
        or cap['inputs'].get(str(args.candidate))!=sha(args.candidate)):
        raise ValueError('complete same-object continuous cap and linear kernels are required')
    for doc,name in ((kernels,'fourfold_codazzi_cap_A0_translation_budget.py'),
                     (cap,'fourfold_codazzi_centered_cap_interface_jumps.py'),
                     (reg,'fourfold_codazzi_centered_cap_regularity.py')):
        if doc['source_sha256']!=sha(Path(__file__).with_name(name)):
            raise ValueError('the actually executed cap producer differs')
        if not all(doc[k] for k in ('whole_affine_parameter_interval','whole_real_angular_circle','complete_primitive_tail')):
            raise ValueError('the complete target scope is missing')
        for key in ('object_sha256','exact_center_parameter','parameter_half_width'):
            if doc[key]!=native[key]:raise ValueError('true target identity differs: '+key)
    old_left,right=map(Fraction,cap['exact_requested_interval'])
    if not old_left<=args.left<right==Fraction(25,8):raise ValueError('screen only the proved true cap suffix')
    mu,tau=exact_arb(args.mu),exact_arb(args.tau)
    selected=[];wrows=[];urows=[];cursor=args.left;weighted_rates=True
    for item in kernels['rows']:
        lo,hi=map(Fraction,item['interval'])
        if hi<=args.left:continue
        lo=max(lo,args.left);nr=native['rows'][item['native_index']]
        nl,nh=map(Fraction,nr['interval']);gl,gh=map(Fraction,nr['actual_scalar_germ'])
        if lo!=cursor or not gl<=nl<=lo<hi<=nh<=gh:raise ValueError('the actual closed suffix/germ cover differs')
        v={k:box_from_record(z) for k,z in nr['coefficients'].items()}
        ql=box_from_record(item['q_lower']).lower();qu=box_from_record(item['q_upper']).upper()
        w,ok=row_constants(v,ql,qu,mu,tau);u,uok=row_constants(v,ql,qu,arb(0),arb(0))
        if not uok:raise ValueError('the already proved unweighted suffix rate was lost')
        weighted_rates=weighted_rates and ok;wrows.append(w);urows.append(u)
        selected.append(dict(native_index=item['native_index'],interval=[str(lo),str(hi)],
            actual_scalar_germ=nr['actual_scalar_germ'],weighted_rates_positive=ok,
            weighted={k:record(z) for k,z in w.items()},unweighted={k:record(z) for k,z in u.items()}))
        cursor=hi
    if cursor!=right or not selected:raise ValueError('the entire actual regular entrance is not covered')
    saved=load_candidate(args.candidate);meta=json.loads(str(saved['metadata']));m=int(meta['modes'])
    if meta['object_sha256']!=native['object_sha256'] or meta['coordinates']!='B=alpha*b; C=Cref_nu+alpha*c':
        raise ValueError('the complete exact finite centre changed')
    nodes=list(map(lambda x:Fraction.from_float(float(x)),saved['radial_nodes']))
    alpha=arb_box(exact_arb(Fraction.from_float(float(meta['amplitude']))))
    Bmax=np.zeros(2*m+1);Cmax=np.zeros_like(Bmax)
    for j in range(len(nodes)-1):
        lo=max(nodes[j],args.left);hi=min(nodes[j+1],right)
        if lo>=hi:continue
        b,_,c,*_=polynomials(saved,nodes,j,lo,hi,alpha,m)
        Bmax=np.maximum(Bmax,b.abs_upper());Cmax=np.maximum(Cmax,c.abs_upper())
    atleft=trace(saved,args.left)
    finite_inner=sum((abs(exact_arb(x)) for x in atleft[m+1:]),arb(0)).upper()
    old_error=box_from_record(reg['bounds']['actual_correction_X0']).upper()
    inner=(finite_inner+old_error).upper()
    original_pair=(total(Bmax)+total(Cmax)+old_error).upper()
    radius=exact_arb(args.radius)
    uconst=aggregate(urows);uradius=max(radius,original_pair).upper()
    unweighted_ball=ball(uconst,uradius,inner)
    same_branch=bool(unweighted_ball.get('denominator_positive')
        and box_from_record(unweighted_ball['contraction']).upper()<1)
    wconst=aggregate(wrows) if weighted_rates else None
    wball=ball(wconst,radius,inner) if weighted_rates else dict(passed=False)
    passed=bool(weighted_rates and wball['passed'] and same_branch)
    first=native['rows'][selected[0]['native_index']]['coefficients']
    aL=box_from_record(first['a']);aR=box_from_record(native['true_R74_entrance']['radius'])
    ratio=(aR.upper()/aL.lower()).upper()
    if not 0<ratio<1:raise ValueError('the true radial contraction factor is missing')
    sigma=(-tau*ratio.log()).lower();weight=(mu*ratio.log()).exp().upper()
    screened=(weight*radius).upper()
    result=dict(kind='actual_same_cap_radial_decay_and_growing_full_analytic_width',complete=True,
        source_sha256=sha(__file__),inputs={str(p):sha(p) for p in (args.reference,args.kernels,args.cap,args.regularity,args.candidate)},
        object_sha256=native['object_sha256'],exact_center_parameter=native['exact_center_parameter'],
        parameter_half_width=native['parameter_half_width'],exact_requested_interval=[str(args.left),str(right)],
        whole_affine_parameter_interval=True,whole_real_angular_circle=True,complete_primitive_tail=True,
        original_proved_cap_interval=cap['exact_requested_interval'],
        exact_radial_power=str(args.mu),exact_width_growth=str(args.tau),exact_radius=str(args.radius),
        norm='sum_m sup_r (a(L)/a(r))^(mu+tau*abs(m)) |U_m(r)|, pair sum, m in all 4Z',
        full_mean_retained=True,selected_outer_inputs=dict(d_nonzero=0,B_mean=0,c_mean=0),
        selected_closed_boxes=len(selected),rows=selected,weighted_rates_positive=weighted_rates,
        weighted_constants=None if wconst is None else {k:record(v) for k,v in wconst.items()},
        weighted_ball=wball,unweighted_uniqueness_constants={k:record(v) for k,v in uconst.items()},
        unweighted_uniqueness_ball=unweighted_ball,same_original_branch_identified=same_branch and passed,
        curvature_screening_certified=passed,
        bounds={k:record(v) for k,v in dict(exact_finite_inner_c_A0=finite_inner,
            actual_inner_c_A0=inner,original_proved_correction_X0=old_error,
            complete_centre_suffix_B_A0=total(Bmax),complete_centre_suffix_c_A0=total(Cmax),
            original_actual_suffix_pair_X0=original_pair,a_right_over_a_left_upper=ratio,
            right_analytic_width_lower=sigma,right_common_radial_weight_upper=weight,
            right_analytic_B_plus_c_A0_upper=screened).items()},
        true_R74_fee_retained=kernels['true_R74_linear_tail_fee_retained'],
        all_Fourier_modes_retained=True,zero_outer_data_are_not_asserted_nonlinearly_regular=True,
        height_or_grounded_flux_identified=False,periodic_frame_holonomy_proved=False,
        nonlinear_regular_tail_matched=False,body_matched=False,closed_surface_complete=False,
        dependencies={name:sha(Path(__file__).with_name(name)) for name in (
            'fourfold_codazzi_rotational_cap_jacobi.py','fourfold_codazzi_candidate_shards.py',
            'fourfold_codazzi_cap_centered_residual_v5.py','fourfold_codazzi_cap_open_curvature_ports_v2.py',
            'fourfold_phase_beta_bulk_box.py','fourfold_phase_beta_bulk_interval.py','fourfold_phase_metric_defect.py')})
    save(args.out,result)
    print(dict(certified=passed,weighted_rates=weighted_rates,rows=len(selected),
        weighted_contraction=wball.get('contraction'),inner=inner.str(12),
        right_curvature_analytic_A0=screened.str(12),width=sigma.str(12)),flush=True)


if __name__=='__main__':main()
