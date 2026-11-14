#!/usr/bin/env python3
"""Real node12 B0, full trace mismatch, nonlinear derivative and mean position.

Uses only already paid true source/columns/auxiliary and full-frequency boxes.
All46 low Q identities are exact; high traces remain outputs. The candidate
K is exactly the R48 saved-Q/L definition, not an asserted exact DN. The
mu11 worker coordinate and mu12 head coordinate are kept distinct.
The cuff height convention is retained in the full mean-position integral.
Author: exact_closure (GPT-6 Astra Pro, AI-assisted),2026-11-12.
"""
import argparse
from fractions import Fraction
import json
from pathlib import Path
import resource
import time
from flint import arb,ctx
from closure_real_head_source_enclosure import power2,exact_q,ball_record
from closure_real_head_green_enclosure import ball
from closure_split_joint_io_v2 import read,digest,iter_array,metadata_without_array
from closure_two_material_joint_verify import compact


def main():
    p=argparse.ArgumentParser(description=__doc__)
    for name in ('columns-summary','columns','joint','density','reference','box','ports','real-source','ready','out'):
        p.add_argument('--'+name,type=Path,required=True)
    p.add_argument('--rss-limit-mib',type=int,default=40)
    args=p.parse_args();ctx.prec=192;start=time.monotonic()
    if args.out.exists():raise FileExistsError('Use a fresh complete true-cut output')
    keys=('columns_summary','columns','joint','density','reference','box','ports','real_source','ready')
    hashes={str(getattr(args,k)):digest(getattr(args,k)) for k in keys}
    cols=read(args.columns_summary)
    if not cols['all_gates'] or not all(cols['gates'].values()) or cols['output']!=str(args.columns) or cols['output_sha256']!=hashes[str(args.columns)]:
        raise ValueError('All original641x46 strict super-solutions are required')
    for k in ('joint','density'):
        if cols['input_hashes'].get(str(getattr(args,k)))!=hashes[str(getattr(args,k))]:
            raise ValueError('The complete true parameter columns use another head')
    reference,box,source,ready=map(read,(args.reference,args.box,args.real_source,args.ready))
    joint=metadata_without_array(args.joint,'rows')
    ports_meta=metadata_without_array(args.ports,'rows')
    if not all(reference['checks'].values()) or not all(box['gates'].values()) or not all(source['checks'].values()) or not joint['whole_head_closed']:
        raise ValueError('Every real background, auxiliary, and full head certificate must be paid')
    if box['input_hashes'].get(str(args.reference))!=hashes[str(args.reference)]:raise ValueError('The true low auxiliary centre changed')
    if hashes[str(args.ready)] not in reference['input_hashes'].values() or hashes[str(args.ready)] not in ports_meta['input_hashes'].values():
        raise ValueError('The candidate and head use another actual source')
    response='notes/2026-11-12-closure-newg-strong-m20-frozen-d12-f225-response.json.gz'
    if reference['input_hashes'].get(response)!=ports_meta['input_hashes'].get(response) or digest(Path(response))!=reference['input_hashes'].get(response):
        raise ValueError('The preserved actual binary centre and candidate differ')
    expected_cells=list(range(12,225)); modes=list(range(2,93,2))
    if reference['modes']!=modes or box['modes']!=modes or cols['parameter_modes']!=modes:
        raise ValueError('Every real46 mode must be retained')
    refs={r['cell']:r for r in reference['cell_rows']};boxes={r['cell']:r for r in box['rows']}
    if sorted(refs)!=expected_cells or sorted(boxes)!=expected_cells:raise ValueError('The whole actual auxiliary head is required')
    candidate=next(r for r in iter_array(args.ports,'rows') if r['physical_node']==12)
    if candidate['source_cell']!=11 or len(candidate['candidate_L_orthonormal_cosine'])!=21:
        raise ValueError('Use the complete actual M20 outer-cell11 endpoint candidate')
    port=source['ports']['12']; b,w,mu11=map(ball,(port['radius'],port['w'],port['mu']))
    ratio=ball(port['next_inner_cell_Xi_factor'])
    if not 0<b<1 or not 0<w<arb(1)/2 or port['normalization_cell']!=11:raise ValueError('The true endpoint is not the specified regular source point')
    rc=exact_q(ready['rationalDeepModel']['physicalParameters']['rCuff'])
    ep=exact_q(ready['rationalDeepModel']['physicalParameters']['epsilonScale'])/rc**7
    d0=exact_q(Fraction(ready['rationalDeepModel']['exactSourceConstants']['delta0']))
    if not 0<rc<b or not power2(14)<ep<power2(15) or not d0*power2(-224)<power2(-231):
        raise ValueError('The actual R18 mean-height scaling inputs changed')
    density_rows=[];mean_integrals=[];aux_means=[];Rref0=None
    for row in iter_array(args.density,'rows'):
        n=row['cell']
        if n!=12+len(density_rows):raise ValueError('The complete physical density range is required')
        X=ball(row['canonical_total_envelope']);aa=ball(row['Q_coefficient']);muhi=ball(row['mu_upper'])
        wl=ball(row['w_lower']).lower();D=ball(row['density_integral_upper']).upper()
        if not wl>0 or not D>0:raise ValueError('A paid physical mean integral ingredient is invalid')
        Vmax=(X*(aa*b.upper()**3+arb(12).sqrt().upper()*muhi/(rc**4*wl))).upper()
        I=(b.upper()*Vmax*D).upper()
        mean_integrals.append(I)
        aux_means.append((ball(refs[n]['complete_R23_mean_increment']).upper()*ball(boxes[n]['total_radius_multiple'])**2).upper())
        density_rows.append(dict(cell=n,I=I))
        if n==12:Rref0=row
    if len(density_rows)!=213:raise ValueError('The finite true head mean integral lacks a cell')
    row=Rref0; B=ball(row['B']);tau=ball(row['tau_outer']);tau_ref=ball(row['reference_tau']);sigma=arb(1)/64;gap=tau-sigma
    if not gap>arb(1)/8 or not B>120 or not tau_ref>tau:raise ValueError('The actual full trace strip and balanced norm changed')
    mu12lo,mu12hi=ball(row['mu_lower']),ball(row['mu_upper'])
    if not (mu12lo*ratio).lower()<=mu11.upper() or not mu11.lower()<=(mu12hi*ratio).upper():
        raise ValueError('The outer mu11 and inner mu12 source coordinates do not overlap correctly')
    V=(ball(row['canonical_total_envelope'])*(ball(row['Q_coefficient'])*b**3+arb(12).sqrt()*mu12hi/(b**4*w))).upper()
    eps=(V/w).upper()
    co=(arb(12).sqrt()*mu11/(b**4*w**2))
    ci=(arb(12).sqrt().upper()*mu12hi/(b.lower()**4*w.lower()**2)).upper()
    Xcorr=((ball(boxes[12]['total_radius_multiple'])-1)*ball(refs[12]['reference_X']).upper()).upper()
    wanted={0,213,426,639,640};r={};W={};all_t=[];rparts={}
    for jr in iter_array(args.joint,'rows'):
        i=jr['index']
        if i in wanted:r[i]=ball(jr['radius']);W[i]=ball(jr['metric_weight'])
        if i<639:rparts[i]=ball(jr['radius'])
    for n in range(213):all_t.append((rparts[n]+rparts[213+n]+rparts[426+n]+r[639]).upper())
    del rparts
    beta_lin={};candidate_norm={};linear_norm={};base_rows=[]
    for name,t in [('outer',sigma),('head',tau)]:
        err=Pnorm=Knorm=Lnorm=arb(0)
        for j,er in enumerate(reference['endpoint_rows']):
            m=er['mode'];q=ball(er['reference_Q']);slope=ball(er['raw_worker_slope'])
            if m!=modes[j]:raise ValueError('A real low trace mode was reordered')
            L=exact_q(candidate['candidate_L_orthonormal_cosine'][j+1]) if j<20 else arb(0)
            pcoef=m*b**3/w;kcoef=m*m*b**3/w+co*slope
            kc=arb(2).sqrt()*L+m*m*b**3/w*q
            difference=co*slope*q-arb(2).sqrt()*L
            weight=(1+m)*(t*m).exp()
            err+=weight*abs(difference).upper()
            Pnorm+=weight*abs(pcoef*q).upper();Knorm+=weight*abs(kc).upper();Lnorm+=weight*abs(kcoef*q).upper()
            if name=='outer':
                axis=cols['axes'][j];unit=ball(axis['canonical_Q_axis'])
                base_rows.append(dict(mode=m,canonical_Q_identity_column=j+1,
                    Xi_mu11_over_Q=er['raw_worker_slope'],P_full_sine_coefficient_per_Q=ball_record(-pcoef),
                    Kbar_full_cosine_coefficient_per_Q=ball_record(kcoef),
                    canonical_Q_axis=axis['canonical_Q_axis'],canonical_Q_axis_log2=axis['canonical_Q_axis_log2'],
                    B0_P_axis_amplitude=ball_record(-pcoef*unit),B0_K_axis_amplitude=ball_record(kcoef*unit),
                    linear_minus_saved_candidate_K=ball_record(difference)))
        beta_lin[name]=err.upper();candidate_norm[name]=(Pnorm+Knorm).upper();linear_norm[name]=(Pnorm+Lnorm).upper()
    beta={};joint_error={}
    for name,t in [('outer',sigma),('head',tau)]:
        gg=tau-t
        aux=(ci*Xcorr*(-2*(tau_ref-t)).exp()).upper()
        low=(eps*r[0]*(-2*gg).exp()).upper()
        hi=[(eps*r[i]*(-minimum*gg).exp()).upper() for i,minimum in [(213,94),(426,186),(639,8192)]]
        high=sum(hi,arb(0)).upper();lowtotal=(beta_lin[name]+aux+low).upper()
        joint_error[name]=(lowtotal+high).upper()
        beta[name]=dict(linear_reference_minus_saved_candidate_K=ball_record(beta_lin[name]),
            auxiliary_low_correction_K=ball_record(aux),full_head_low_correction_K=ball_record(low),
            complete_low_K=ball_record(lowtotal),high_bands_joint=[ball_record(v) for v in hi],
            complete_high_joint=ball_record(high),complete_high_P=ball_record((high/B).upper()),
            complete_low_P_identically_zero=True,complete_low_Q_identically_zero=True,
            complete_nonmean_joint=ball_record(joint_error[name]))
    Rbase=(candidate_norm['head']+joint_error['head']).upper()
    Drows=[];largest_direction=arb(0)
    for j,axis in enumerate(cols['axes']):
        m=modes[j];unit=ball(axis['canonical_Q_axis']);scale=power2(axis['enlargement_bits'])
        lo=ball(axis['enlarged_unit_nonlinear_cut_low']).upper()
        near=scale*ball(axis['original_unit_nonlinear_cut_near']);rest=scale*ball(axis['original_unit_nonlinear_cut_rest']);infinite=scale*ball(axis['original_unit_nonlinear_cut_infinite'])
        dl=(eps*lo*(-2*gap).exp()).upper()
        dh=(eps*(near*(-94*gap).exp()+rest*(-186*gap).exp()+infinite*(-8192*gap).exp())).upper()
        p0=abs(ball(base_rows[j]['B0_P_axis_amplitude'])).upper()
        k0=abs(ball(base_rows[j]['B0_K_axis_amplitude'])).upper()
        direct=((1+m)*(tau*m).exp()*(p0+k0)).upper()
        broad=(direct+eps*(lo+near+rest+infinite)).upper()
        largest_direction=max(largest_direction,broad)
        # Each individual output coefficient is bounded; the shared modal
        # mass is at most lo, so these46 caps are NOT independent full masses.
        low_caps=[compact_pair((eps*lo*(-tau*k).exp()/(1+k)).upper()) for k in modes]
        Drows.append(dict(input_mode=m,new_canonical_axis_log2=axis['canonical_Q_axis_log2'],
            nonlinear_low_Q_and_P_identically_zero=True,
            low_K_derivative_minus_B0_W_sigma1=ball_record(dl),
            high_P_K_derivative_W_sigma1=ball_record(dh),
            high_P_derivative_W_sigma1=ball_record((dh/B).upper()),
            broad_complete_P_K_derivative=ball_record(broad),
            low_K_output_coefficient_caps=low_caps,
            low_modal_mass_budget=ball_record(lo)))
    Rfamily=(Rbase+largest_direction).upper()
    if not Rfamily<arb(1)/256 or not eps*(1+ball(cols['physical_domain']))<arb(1)/256:
        raise ArithmeticError('The actual full mean/connection root domain failed')
    mean_beta=(16*Rbase*joint_error['head']).upper()
    for rowd in Drows:
        rowd['complete_mean_slope_derivative']=ball_record((16*Rfamily*ball(rowd['broad_complete_P_K_derivative'])).upper())
    mean_position0=sum((aux_means[n]+16*(1+ball(cols['physical_domain']))*mean_integrals[n]*all_t[n] for n in range(213)),arb(0)).upper()+power2(-4975)
    mean_der=[arb(0) for _ in modes];seen=[]
    for cell in iter_array(args.columns,'cells'):
        n=cell['cell']-12
        if n!=len(seen):raise ValueError('A complete derivative source cell was omitted')
        if len(cell['original_unit_complete_field_upper'])!=46:raise ValueError('A physical derivative field omitted an input mode')
        seen.append(n)
        for j,v in enumerate(cell['original_unit_complete_field_upper']):
            mean_der[j]+=16*(1+ball(cols['physical_domain']))*mean_integrals[n]*compact(v)*power2(cols['axes'][j]['enlargement_bits'])
    if seen!=list(range(213)):raise ValueError('The entire finite mean-height derivative is required')
    farrow=next(row for row in iter_array(args.columns,'rows') if row['index']==640)
    if len(farrow['scaled_derivative_upper'])!=46:raise ValueError('A true far derivative input mode was omitted')
    if not ball(cols['complete_far_normalized_domain_upper'])<arb(1)/2:
        raise ArithmeticError('The R18 first-derivative mean-height margin needs z<Z/2')
    for j in range(46):
        Dz=(W[640]*compact(farrow['scaled_derivative_upper'][j])*power2(cols['axes'][j]['enlargement_bits'])).upper()
        mean_der[j]=(mean_der[j]+power2(-4973)*Dz).upper()
        Drows[j]['cuff_normalized_mean_height_derivative']=ball_record(mean_der[j])
    beta['complete_mean_slope_difference']=ball_record(mean_beta)
    beta['cuff_normalized_mean_height_vs_background_at_zero']=ball_record(mean_position0.upper())
    beta['mean_height_reference']='The axisymmetric background height uses the same cuff value0. The actual mean-height scalar is not freely shifted at node12.'
    beta['candidate_second_radial_jet_not_declared_exact']=True
    checks=dict(original_full641x46_columns_paid=cols['all_gates'],all46_true_B0_columns_present=len(base_rows)==46,
        exact_low_Q_identity_and_zero_mismatch=True,outer_mu11_and_inner_mu12_distinguished=True,
        same_saved_binary_candidate_and_true_source=True,positive_true_cut_and_complete_angle_loss=gap>arb(1)/8,
        complete_mean_small_branch=Rfamily<arb(1)/256,
        all213_finite_mean_integrals_paid=len(mean_integrals)==213,
        R18_infinite_mean_height_and_derivative_included=True,
        actual_parameter_far_stays_inside_half_R18_ball=ball(cols['complete_far_normalized_domain_upper'])<arb(1)/2)
    result=dict(status='Actual strong node12 complete B0/beta/nonlinear derivative/mean-position interface',checks=checks,all_gates=all(checks.values()),
        true_radius=ball_record(b),true_w=ball_record(w),outer_mu11=ball_record(mu11),inner_mu12_interval=dict(lower=row_endpoint(mu12lo.lower()),upper=row_endpoint(mu12hi.upper())),
        normalization_factor=ball_record(ratio),B=ball_record(B),head_strip=ball_record(tau),outer_strip='1/64',gap=ball_record(gap),
        true_point_V_upper=ball_record(V),true_point_epsilon_upper=ball_record(eps),
        whole_cell_epsilon_upper=row['V_over_w_upper'],
        canonical_auxiliary_correction_X=ball_record(Xcorr),candidate_broad_nonmean_norm=ball_record(candidate_norm['head']),
        actual_zero_parameter_broad_nonmean_norm=ball_record(Rbase),actual_full_parameter_family_broad_nonmean_norm=ball_record(Rfamily),
        B0=base_rows,beta=beta,nonlinear_derivative_columns=Drows,
        parameter_norm='The response-based axes from closure-strong-parameter-columns-r2; sum_j |delta Q_j|/axis_j<=1. Every derivative column is per one normalized input axis.',
        derivative_decomposition='D true_trace = B0 + DeltaB. Low Q/P rows of DeltaB are exactly0. Low K, all high P/K, full mean slope and cuff-normalized mean height are retained separately.',
        low_coefficient_cap_semantics='For each parameter column there are fixed nonnegative output modal masses nu_m with sum_m nu_m<=low_modal_mass_budget; |DeltaK_m|<=epsilon_b exp(-tau_b m) nu_m/(1+m). The listed individual caps do not grant independent full mass to each output.',
        beta_scope='At a=0 compare the true R58 all-frequency trace to the exact R48 saved-Q/L candidate at the same real radius. The finite worker slope and its mean are not substituted for the exact true DN.',
        mean_position_formula='Finite: sum_n[H_R23,n X_aux,n^2+16(1+rho) I_n t_n], I_n<=b Vmax_n integral(cV/w). Infinite: R18(9.8)<2^-4975. Parameter derivative uses16(1+rho)sum I_n field_column_n plus2^-4973 times normalized far column.',
        mean_position_cuff_normalization=True,no_per_cell_mean_translation=True,
        outer_Schur_inverse_paid=False,outer_residual_in_parameter_norm_paid=False,
        input_hashes=hashes,source_sha256=digest(Path(__file__)),
        helper_hashes={name:digest(Path(__file__).with_name(name)) for name in ('closure_split_joint_io_v2.py','closure_real_head_source_enclosure.py','closure_real_head_green_enclosure.py','closure_two_material_joint_verify.py')},
        new_radial_integrations=0,new_flow_solves=0,new_matrix_inverses=0,
        elapsed_seconds=time.monotonic()-start,peak_RSS_KiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    if result['peak_RSS_KiB']>args.rss_limit_mib*1024:raise MemoryError('The short true-cut interface exceeded its40MiB owned budget')
    args.out.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(dict(event='done',all_gates=result['all_gates'],epsilon_b=str(eps),beta_low_K=str(ball(beta['outer']['complete_low_K'])),beta_high_joint=str(ball(beta['outer']['complete_high_joint'])),mean_slope_beta=str(mean_beta),mean_height0=str(mean_position0),maximum_nonlinear_low_derivative=str(max(ball(x['low_K_derivative_minus_B0_W_sigma1']) for x in Drows)),seconds=result['elapsed_seconds'],RSS_KiB=result['peak_RSS_KiB'],sha256=digest(args.out),bytes=args.out.stat().st_size)),flush=True)


def row_endpoint(x):
    m,e=x.man_exp();return dict(mantissa=str(m),binary_exponent=int(e))


def compact_pair(x):
    m,e=x.upper().man_exp();return [int(m),int(e)]


if __name__=='__main__':main()
