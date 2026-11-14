#!/usr/bin/env python3
"""Directed all-mode unweighted cap kernels and a driven nonlinear BVP.

The four outer/inner boundary ports remain independent.  In particular,
this does not replace the uncomputed true nonlinear regular-tail relation
by its linear graph, and it makes no periodic-frame holonomy claim.
"""
from __future__ import annotations
import argparse,gzip,json
from bisect import bisect_right
from fractions import Fraction
from pathlib import Path
import numpy as np
from flint import arb,ctx
from fourfold_codazzi_rotational_cap_jacobi import box_from_record
from fourfold_phase_metric_defect import record,save,sha
from fourfold_codazzi_candidate_shards import load_candidate


def exact(value):
    value=Fraction(value)
    return arb(value.numerator)/value.denominator


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--input',type=Path,default=Path('notes/2026-11-13-Codazzi-rotational-positive-cap-v2-native.json.gz'))
    ap.add_argument('--object',type=Path,default=Path('data/phase_ring_continuation/type_fixed_step02_d5_exact_affine_step5_object.json'))
    ap.add_argument('--candidate',type=Path,default=Path('notes/2026-11-13-R133-compact-metric-outer-mean-m64-candidate.npz.gz'))
    ap.add_argument('--left',type=Fraction,default=Fraction(3,2))
    ap.add_argument('--radius',type=Fraction,default=Fraction(1,500))
    ap.add_argument('--inner-c-budget',type=Fraction,default=Fraction(1,2000))
    ap.add_argument('--outer-d-budget',type=Fraction,default=Fraction(1,1000000))
    ap.add_argument('--outer-b-mean-budget',type=Fraction,default=Fraction(1,1000000))
    ap.add_argument('--outer-c-mean-budget',type=Fraction,default=Fraction(1,1000000))
    ap.add_argument('--out',type=Path,required=True);args=ap.parse_args();ctx.prec=320
    if args.out.exists():raise FileExistsError('refusing to overwrite a cap result or failure')
    d=json.loads(gzip.decompress(args.input.read_bytes()))
    native=Path(__file__).with_name('fourfold_codazzi_rotational_cap_jacobi_v2.py')
    old=Path(__file__).with_name('fourfold_codazzi_rotational_cap_jacobi.py')
    if (not d['complete'] or not d['cap_linear_reference_certified'] or d['failure'] is not None
        or d['source_sha256']!=sha(native) or d['original_source_sha256']!=sha(old)
        or d['checkpoint_sha256']!=sha(d['checkpoint_path']) or d['object_sha256']!=sha(args.object)):
        raise ValueError('the complete actual positive-cap provenance changed')
    for name,h in d['dependency_sha256'].items():
        if sha(Path(__file__).with_name(name))!=h:raise ValueError('actual cap dependency changed: '+name)
    for name,h in d['input_theorem_sha256'].items():
        if sha(Path('results')/name)!=h:raise ValueError('actual cap theorem changed: '+name)
    if not all(d[k] for k in ('whole_affine_parameter_interval','whole_real_angular_circle','complete_primitive_tail')):
        raise ValueError('incomplete actual coefficient scope')
    rows=d['rows'];cursor=Fraction(239,1000)
    for row in rows:
        l,r=map(Fraction,row['interval']);gl,gr=map(Fraction,row['actual_scalar_germ'])
        if l!=cursor or not gl<=l<r<=gr:raise ValueError('actual closed radial/germ cover lost')
        cursor=r
    if cursor!=Fraction(25,8) or not Fraction(239,1000)<=args.left<cursor:
        raise ValueError('invalid actual cap interval')
    entry=d['true_R74_entrance'];radius=box_from_record(entry['radius']);omega=box_from_record(entry['normalized_omega'])
    initial=1/(1+(radius/(4*omega))**2).sqrt()
    fee=box_from_record(d['Jacobi']['full_frequency_interval']['complete_true_tail_fee']).upper()
    qlo=(initial.lower()-fee).lower();qhi=(initial.upper()+fee).upper();slack=arb(2)**-128
    if not qlo>0:raise ValueError('nonpositive complete actual regular Jacobi entrance')
    table=[]
    for index in reversed(range(len(rows))):
        row=rows[index];v={k:box_from_record(z) for k,z in row['coefficients'].items()}
        ell,g,b=v['lambda_ref'],v['gamma'],v['beta']
        linear=-b*(ell-1)/(4*g);bl=min(arb(0),linear.lower());bu=max(arb(0),linear.upper())
        ll,lu=ell.lower(),ell.upper()
        lo=(2*ll/((bl*bl+4*ll).sqrt()-bl)).lower()
        hi=((bu+(bu*bu+4*lu).sqrt())/2).upper()
        qlo=min(qlo,lo);qhi=max(qhi,hi)
        ql=(qlo*(1-slack)).lower();qu=(qhi*(1+slack)).upper()
        lower_margin=(ll+bl*ql-ql*ql).lower()
        upper_margin=(qu*qu-bu*qu-lu).lower()
        if not lower_margin>0 or not upper_margin>0:raise ValueError('nonpositive every-mode suffix Riccati face')
        l,r=map(Fraction,row['interval'])
        if r<=args.left:continue
        l=max(l,args.left)
        sd=(g*ql+min(arb(0),(-2*b).lower())/4).lower()
        sc=(g*ql+min(arb(0),(b*(ell+1)).lower())/4).lower()
        item=dict(native_index=index,interval=[str(l),str(r)],actual_scalar_germ=row['actual_scalar_germ'],
            q_lower=ql,q_upper=qu,D_rate_per_frequency=sd,C_rate_per_frequency=sc,
            gamma_upper=g.upper(),beta_abs_upper=abs(b).upper(),beta_upper=b.upper(),
            ell_lower=ll,ell_upper=lu,abs_Cref_lower=(-v['Cref']).lower(),
            lower_face_margin=lower_margin,upper_face_margin=upper_margin)
        if sc>0 and sd>0:
            item.update(triangular_coupling=(g.upper()/sc).upper(),
                nonlinear_D_kernel=((g.upper()+qu*abs(b).upper()/4)/sd).upper(),
                nonlinear_C_kernel=(abs(b).upper()/(4*sc)).upper())
        table.append(item)
    table.reverse();cursor=args.left
    for row in table:
        l,r=map(Fraction,row['interval'])
        if l!=cursor:raise ValueError('selected cap suffix is not contiguous')
        cursor=r
    rates_pass=all(x['D_rate_per_frequency']>0 and x['C_rate_per_frequency']>0 for x in table)
    means_pass=all(x['beta_upper']<0 for x in table)
    report=dict(kind='actual_all_mode_unweighted_cap_and_driven_nonlinear_budget',complete=True,
        source_sha256=sha(__file__),input_path=str(args.input),input_sha256=sha(args.input),
        object_path=str(args.object),object_sha256=sha(args.object),
        exact_center_parameter=d['exact_center_parameter'],parameter_half_width=d['parameter_half_width'],
        exact_requested_interval=[str(args.left),'25/8'],covered_interval=[str(args.left),str(cursor)],
        whole_affine_parameter_interval=True,whole_real_angular_circle=True,complete_primitive_tail=True,
        all_physical_nonzero_frequencies='m in 4Z minus zero, without finite truncation',
        true_R74_linear_tail_fee_retained=record(fee),
        suffix_Riccati_gate='at row i use the outward-expanded hull of the true entrance and every normalized positive comparison root on rows i..R',
        exact_relative_strict_slack='1/340282366920938463463374607431768211456',
        original_native_boxes=len(rows),selected_closed_boxes=len(table),
        unweighted_nonzero_rates_positive=rates_pass,backward_mean_rates_positive=means_pass,
        full_mean_retained=True,nonlinear_regular_tail_matched=False,
        nonlinear_body_matched=False,periodic_frame_holonomy_proved=False,closed_surface_complete=False,
        norm='X_s = sum_(m in 4Z) (1+|m|)^s sup_r |F_m(r)|; vector norm ||B||_X_s+||c||_X_s',
        independent_ports=['c_nonzero(left)','d_nonzero(25/8), d=b+q_m c','B_mean(25/8)','c_mean(25/8)'],
        rows=[{k:record(v) if isinstance(v,arb) else v for k,v in x.items()} for x in table])
    if not rates_pass or not means_pass:
        report.update(nonlinear_contraction_certified=False,failure='one or more actual unweighted/mean rate gates failed')
        save(args.out,report);print(dict(passed=False,boxes=len(table)),flush=True);return
    qu=max(x['q_upper'] for x in table).upper();T=max(x['triangular_coupling'] for x in table).upper()
    KD=max(x['nonlinear_D_kernel'] for x in table).upper();KC=max(x['nonlinear_C_kernel'] for x in table).upper()
    sd=min(x['D_rate_per_frequency'] for x in table).lower();sc=min(x['C_rate_per_frequency'] for x in table).lower()
    ell_lo=min(x['ell_lower'] for x in table).lower();ell_hi=max(x['ell_upper'] for x in table).upper()
    cmin=min(x['abs_Cref_lower'] for x in table).lower();bmin=min(-x['beta_upper'] for x in table).lower()
    Kmean=(1/(1+ell_lo)).upper();boundary_D=(1+(1+qu)*T).upper();boundary_C=(1+qu).upper()
    Knonzero=(boundary_D*KD+(1+qu)*KC).upper();K=max(Kmean,Knonzero).upper();L=max(arb(1),ell_hi).upper()
    R=exact(args.radius);eC=exact(args.inner_c_budget);eD=exact(args.outer_d_budget)
    eB0=exact(args.outer_b_mean_budget);eC0=exact(args.outer_c_mean_budget)
    if not R>0 or not cmin-R>0 or not min(eC,eD,eB0,eC0)>=0:raise ValueError('invalid nonlinear radius or ports')
    boundary=(boundary_C*eC+boundary_D*eD+eB0+eC0).upper()
    Q=(L*R*R/(cmin-R)).upper()
    image=(boundary+K*Q).upper();lip=(K*L*(2*R/(cmin-R)+R*R/(cmin-R)**2)).upper()
    const=dict(q_upper=qu,D_rate_per_frequency=sd,C_rate_per_frequency=sc,
        triangular_coupling=T,nonlinear_D_kernel=KD,nonlinear_C_kernel=KC,
        boundary_d_factor=boundary_D,boundary_c_factor=boundary_C,
        mean_C_nonlinear_kernel=Kmean,nonzero_pair_nonlinear_kernel=Knonzero,
        complete_pair_nonlinear_kernel=K,ell_lower=ell_lo,ell_upper=ell_hi,
        reference_C_abs_lower=cmin,minus_beta_lower=bmin,
        forced_B_mean_kernel=(1/(2*bmin)).upper(),
        forced_C_mean_kernel=(1/(bmin*(1+ell_lo))).upper(),
        nonzero_D_inhomogeneous_one_derivative_source_gain=(5/(4*sd)).upper(),
        nonzero_C_inhomogeneous_one_derivative_source_gain=(5/(4*sc)).upper(),
        nonlinear_radius=R,linear_boundary_budget=boundary,nonlinear_Q_budget=Q,
        closed_ball_image_upper=image,closed_ball_margin=(R-image).lower(),
        contraction_factor=lip,contraction_margin=(1-lip).lower(),actual_C_abs_lower=(cmin-R).lower())
    passed=bool(image<R and lip<1)
    saved=load_candidate(args.candidate);meta=json.loads(str(saved['metadata']));m=int(meta['modes'])
    if meta['object_sha256']!=d['object_sha256'] or meta['coordinates']!='B=alpha*b; C=Cref_nu+alpha*c':
        raise ValueError('boundary candidate is not normalized against this exact target')
    if args.left<Fraction(18,100):raise ValueError('the compact metric must already agree exactly with g0')
    nodes=[Fraction.from_float(float(x)) for x in saved['radial_nodes']]
    piece=min(len(nodes)-2,bisect_right(nodes,args.left)-1)
    if piece<0 or not nodes[piece]<=args.left<=nodes[piece+1]:raise ValueError('boundary cut outside the complete candidate')
    alpha=exact(Fraction.from_float(float(meta['amplitude'])));x=exact(args.left-nodes[piece]);norm=arb(0);coeff=[]
    for j in range(1,m+1):
        value=arb(0)
        for order in range(4):value=value*x+arb(float(saved['piece_coefficients'][order,piece,m+j]))
        value=alpha*value;coeff.append(record(value));norm+=arb(1+4*j)**2*abs(value)
    norm=norm.upper();boundary_pass=bool(norm<eC)
    report.update(constants={k:record(v) for k,v in const.items()},failure=None if passed else 'the nonlinear closed-ball or contraction gate failed',
        nonlinear_contraction_certified=passed,
        exact_port_budgets=dict(inner_nonzero_C=str(args.inner_c_budget),outer_nonzero_d=str(args.outer_d_budget),
            outer_B_mean=str(args.outer_b_mean_budget),outer_C_mean=str(args.outer_c_mean_budget)),
        actual_finite_inner_port=dict(path=str(args.candidate),sha256=sha(args.candidate),modes=m,
            exact_cut=str(args.left),exact_amplitude=str(Fraction.from_float(float(meta['amplitude']))),
            input_piece=piece,source_coordinates=meta['coordinates'],
            exact_dyadic_cosine_coefficient_enclosures=coeff,
            inhomogeneous_A2_norm_upper=record(norm),budget_margin=record((eC-norm).lower()),passed=boundary_pass,
            all_nonzero_boundary_modes_present=True,omitted_boundary_modes_exactly_zero=True,
            original_floating_solver_success_not_used=True,mean_at_left_is_an_output_not_copied_from_candidate=True),
        actual_driven_cap_exists=bool(passed and boundary_pass),
        genuine_regular_tail_relation_used=False,
        dependencies={name:sha(Path(__file__).with_name(name)) for name in (
            'fourfold_codazzi_rotational_cap_jacobi_v2.py','fourfold_codazzi_rotational_cap_jacobi.py',
            'fourfold_codazzi_candidate_shards.py','fourfold_phase_codazzi_two_end_probe.py',
            'fourfold_phase_metric_defect.py')})
    save(args.out,report)
    print(dict(passed=passed,actual_boundary_passed=boundary_pass,boxes=len(table),
        K=str(K),image=str(image),contraction=str(lip),actual_inner_A2=str(norm)),flush=True)


if __name__=='__main__':main()
