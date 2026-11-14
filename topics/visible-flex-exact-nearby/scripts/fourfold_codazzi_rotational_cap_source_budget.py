#!/usr/bin/env python3
"""Consume the complete actual cap certificate for full-mode source bounds.

The mixed norm is sum_m |m|^s sup_r |F_m(r)|, not sup_r sum_m.  Sources
are the explicit forced curvature-Codazzi rows, with mean retained outside
the nonzero-frequency estimate. No metric-source conversion is assumed.
"""
from __future__ import annotations
import argparse,gzip,json
from fractions import Fraction
from pathlib import Path
from flint import arb,ctx
from fourfold_codazzi_rotational_cap_jacobi import box_from_record
from fourfold_phase_metric_defect import record,save,sha


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--input',type=Path,default=Path('notes/2026-11-13-Codazzi-rotational-positive-cap-v2-native.json.gz'))
    ap.add_argument('--out',type=Path,required=True);a=ap.parse_args();ctx.prec=256
    if a.out.exists():raise FileExistsError('refusing to overwrite a source-interface certificate')
    doc=json.loads(gzip.decompress(a.input.read_bytes()))
    source=Path(__file__).with_name('fourfold_codazzi_rotational_cap_jacobi_v2.py')
    if not doc['complete'] or not doc['cap_linear_reference_certified'] or doc['source_sha256']!=sha(source):
        raise ValueError('the complete actual positive-cap source identity has not passed')
    original=Path(__file__).with_name('fourfold_codazzi_rotational_cap_jacobi.py')
    if doc['original_source_sha256']!=sha(original) or doc['checkpoint_sha256']!=sha(doc['checkpoint_path']):
        raise ValueError('the strict replay no longer binds its preserved original checkpoint')
    for name,digest in doc['dependency_sha256'].items():
        if sha(Path(__file__).with_name(name))!=digest:raise ValueError('actual cap dependency changed: '+name)
    for name,digest in doc['input_theorem_sha256'].items():
        if sha(Path('results')/name)!=digest:raise ValueError('actual cap theorem changed: '+name)
    if not all(doc[k] for k in ('whole_affine_parameter_interval','whole_real_angular_circle','complete_primitive_tail')):
        raise ValueError('a partial coefficient scope cannot be promoted to a full-mode interface')
    endpoint=Fraction(doc['exact_requested_interval'][0]);rows=doc['rows']
    if endpoint!=Fraction(239,1000) or Fraction(doc['exact_requested_interval'][1])!=Fraction(25,8):
        raise ValueError('unexpected actual positive-cap domain')
    for row in rows:
        left,right=map(Fraction,row['interval'])
        if left!=endpoint or right<=left:raise ValueError('incomplete actual radial cover')
        endpoint=right
    if endpoint!=Fraction(25,8):raise ValueError('missing true regular entrance')
    full=doc['Jacobi']['full_frequency_interval'];ql=box_from_record(full['q_lower']).lower();qu=box_from_record(full['q_upper']).upper()
    original_ql,original_qu=ql,qu
    # Divide the vector field by the actual positive M*gamma before
    # taking its coefficient bounds. For every M>=4 the linear term
    # belongs to hull(0,-beta*(ell-1)/(4*gamma)). Keeping each radial
    # box intact avoids taking unrelated global gamma extremes.
    roots=[]
    for index,row in enumerate(rows):
        values={k:box_from_record(v) for k,v in row['coefficients'].items()}
        ell,gamma,beta=values['lambda_ref'],values['gamma'],values['beta']
        if not ell>0 or not gamma>0:raise ValueError('nonpositive local normalized Riccati gate')
        linear=-beta*(ell-1)/(4*gamma);bl=min(arb(0),linear.lower());bu=max(arb(0),linear.upper())
        ll,lu=ell.lower(),ell.upper()
        lo=(2*ll/((bl*bl+4*ll).sqrt()-bl)).lower()
        hi=((bu+(bu*bu+4*lu).sqrt())/2).upper()
        if not lo>0 or not hi>0:raise ValueError('nonpositive normalized Riccati comparison root')
        roots.append((lo,hi,ll,lu,bl,bu,index))
    entry=doc['true_R74_entrance'];radius=box_from_record(entry['radius']);omega=box_from_record(entry['normalized_omega'])
    initial=1/(1+(radius/(4*omega))**2).sqrt()
    tailfee=box_from_record(full['complete_true_tail_fee']).upper()
    initial_lo=(initial.lower()-tailfee).lower();initial_hi=(initial.upper()+tailfee).upper()
    if not initial_lo>0:raise ValueError('true full-tail initial data is not strictly positive')
    strict_slack=arb(2)**-128
    ql=(min(initial_lo,min(x[0] for x in roots))*(1-strict_slack)).lower()
    qu=(max(initial_hi,max(x[1] for x in roots))*(1+strict_slack)).upper()
    lower_margin=min((x[2]+x[4]*ql-ql*ql).lower() for x in roots)
    upper_margin=min((qu*qu-x[5]*qu-x[3]).lower() for x in roots)
    if not lower_margin>0 or not upper_margin>0 or not initial_lo>ql or not initial_hi<qu:
        raise ValueError('strict every-frequency inward boundary gate failed')
    gl=min(box_from_record(x['coefficients']['gamma']).lower() for x in rows).lower()
    gu=max(box_from_record(x['coefficients']['gamma']).upper() for x in rows).upper()
    cl=min((-box_from_record(x['coefficients']['Cref'])).lower() for x in rows).lower()
    cu=max((-box_from_record(x['coefficients']['Cref'])).upper() for x in rows).upper()
    al=min(box_from_record(x['coefficients']['a']).lower() for x in rows).lower()
    au=max(box_from_record(x['coefficients']['a']).upper() for x in rows).upper()
    if not all(z>0 and z.is_finite() for z in (ql,qu,gl,gu,cl,cu,al,au)):raise ValueError('positive source-interface coefficient gate failed')
    sigma=(gl*ql).lower();inverse=(1/sigma).upper();same=(inverse/4).upper()
    # d/dt K(t,r)=M*gamma(t)*q(t)*K(t,r), so the triangular
    # integral costs Cplus/qminus, without an extra gamma ratio.
    T=(cu/ql).upper();ci=(1/cl).upper();qi=(qu/cl).upper();unweight=(1/(al*al)).upper()
    # Column order: D_R at order s, V_left at order s,
    # G_D at order s-1, G_V at order s-1.
    D=[arb(1),arb(0),inverse,arb(0)]
    V=[T,arb(1),(T*inverse).upper(),inverse]
    a2c=[(ci*x).upper() for x in V]
    a2b=[(D[i]+qi*V[i]).upper() for i in range(4)]
    report=dict(kind='actual_rotational_cap_full_Codazzi_source_contact_budget',complete=True,
        source_sha256=sha(__file__),input_path=str(a.input),input_sha256=sha(a.input),
        exact_requested_interval=doc['exact_requested_interval'],closed_radial_boxes=len(rows),
        object_sha256=doc['object_sha256'],origin_sha256=doc['origin_sha256'],direction_sha256=doc['direction_sha256'],
        exact_center_parameter=doc['exact_center_parameter'],parameter_half_width=doc['parameter_half_width'],
        whole_affine_parameter_interval=True,whole_real_angular_circle=True,complete_primitive_tail=True,
        all_physical_frequencies='Every m in 4Z minus zero; the complex b row is i sign(m) B_hat.',
        normalized_every_frequency_gate=dict(checked_closed_boxes=len(roots),
            normalized_linear_term='hull(0,-beta*(ell-1)/(4*gamma)) contains -beta*(ell-1)/(M*gamma) for every M>=4',
            original_coarse_q_lower=record(original_ql),original_coarse_q_upper=record(original_qu),
            lower_boundary_margin=record(lower_margin),upper_boundary_margin=record(upper_margin),
            full_true_tail_initial_lower=record(initial_lo),full_true_tail_initial_upper=record(initial_hi),
            lower_root_witness_index=min(roots,key=lambda x:x[0])[6],
            upper_root_witness_index=max(roots,key=lambda x:x[1])[6],
            exact_relative_strict_slack='1/340282366920938463463374607431768211456'),
        norm='sum_(m in 4Z minus zero) |m|^s sup_(r in [.239,25/8]) |F_m(r)|; the order of sup and sum is part of the hypothesis.',
        constants={k:record(v) for k,v in dict(q_lower=ql,q_upper=qu,gamma_lower=gl,gamma_upper=gu,
            abs_Cref_lower=cl,abs_Cref_upper=cu,radius_lower=al,radius_upper=au,
            kernel_rate_per_physical_frequency=sigma,one_angular_derivative_source_gain=inverse,
            same_order_source_gain=same,triangular_coupling=T,inverse_abs_Cref=ci,
            q_over_abs_Cref=qi,unweighted_curvature_extra_factor=unweight).items()},
        boundary_source_columns=['D_R at s','V_left at s','G_D at s-1','G_V at s-1'],
        output_rows=['D at s','V at s','a^2 b at s','a^2 c at s'],
        complete_source_bound_matrix=[[record(v) for v in row] for row in (D,V,a2b,a2c)],
        mean=dict(retained=True,equations=['(a^2 b0)_r=a^2 f_b0','(a^2 Cref c0)_r=a^2 Cref f_c0'],
            forced_mean_inverse_claimed=False,position_height_flux_holonomy_must_still_be_matched=True),
        dependencies={str(source.name):sha(source),str(original.name):sha(original),
            'fourfold_phase_metric_defect.py':sha(Path(__file__).with_name('fourfold_phase_metric_defect.py'))},
        source_conversion_from_metric_defect_instantiated=False,nonlinear_cap_certified=False,full_mixed_inverse=False,
        proof_path='results/R133-supplement-full-Codazzi-source-contact-on-actual-cap.md',
        proof_sha256=sha('results/R133-supplement-full-Codazzi-source-contact-on-actual-cap.md'))
    save(a.out,report)
    print(dict(complete=True,boxes=len(rows),sigma=str(sigma),one_derivative_gain=str(inverse),
        triangular_coupling=str(T),unweighted_extra_factor=str(unweight)),flush=True)


if __name__=='__main__':main()
