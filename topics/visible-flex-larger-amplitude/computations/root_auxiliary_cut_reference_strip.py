# R82 source-only refinement of frozen R63 v3 ce42ce8a3dc40f8d03afc810ba33a215dcacd032b06f15433cea5fe38b3ba038; original source and primary outputs remain unchanged.
# Frozen v2 4827eadd3975db270c51c931ee5a7929de58080061283005236bb104a10e4ed0; v3 adds the exact m2 difference-frequency gain and streams compact gzip output, checking the RSS cap after serialization.
# v1 source 0eabada91b50855ab9e78e02a964d92202941ce0b15a0cfb060c313feacdc22c failed only its40MiB RSS guard after loading. v2 streams unused fields and adds explicit source-factor identity checks; the mathematical formulas are unchanged.
#!/usr/bin/env python3
"""Actual auxiliary SOURCE-ONLY shallow momentum with wider-strip spectral gains.

At the cut psi_Q=0,psi_Xi12=1, so the source functional is
sum_n(mu_n/mu12) integral(phi_Q,m F_n,m).  Saved R42 ordered phi integrals
are reused, with the already certified actual-strong source factors.
For Laux=C2+Rc, Q(C2) has only modes0/4. At m>=6 the cross/rest
quadratic gains exp(-(m-4)*(tau_ref-tau_inner)); the COMPLETE mean/inverse
remainder and generic source use the canonical-strip gain exp(-m*gap).
R33(33.51)-(33.52) supplies the full unit ball at tau_ref. The auxiliary
nonlinear far lift is deliberately a separate positive term, not included
in this source-only output. No new ODE or quadrature.
Author: exact_closure (GPT-6 Astra Pro, AI-assisted),2026-11-12.
"""
import argparse
import gc
import gzip
import json
from pathlib import Path
import resource
import time
from flint import arb,ctx
from closure_real_head_source_enclosure import exact_q,ball_record as full_ball_record
from closure_real_head_green_enclosure import ball,endpoint
from closure_split_joint_io_v2 import read,digest,iter_array,metadata_without_array,read_field


def ball_record(v):
    d=full_ball_record(v);d.pop('display',None);return d


def top(v):return endpoint(v['upper'])


def guard(cap):
    if resource.getrusage(resource.RUSAGE_SELF).ru_maxrss>cap*1024:
        raise MemoryError('The shallow-functional assembly exceeded its owned RSS cap')


def main():
    p=argparse.ArgumentParser(description=__doc__)
    for name in ('columns','ordered','q-density','strong-density','q-panel-summary','strong-low','reference','box','cut','ready','out'):
        p.add_argument('--'+name,type=Path,required=True)
    p.add_argument('--mode',type=int,action='append',required=True)
    p.add_argument('--rss-limit-mib',type=int,default=40)
    args=p.parse_args();ctx.prec=192;start=time.monotonic()
    if args.out.exists() or args.out.suffix!='.gz':raise FileExistsError('Use a fresh compressed cut-functional output')
    names=('columns','ordered','q_density','strong_density','q_panel_summary','strong_low','reference','box','cut','ready')
    hashes={str(getattr(args,k)):digest(getattr(args,k)) for k in names}
    modes=sorted(set(args.mode));allm=list(range(2,93,2));cells=list(range(12,225))
    if len(modes)!=len(args.mode) or any(m not in allm for m in modes):raise ValueError('Use distinct paid low modes')
    columns=metadata_without_array(args.columns,'cell_rows');panel_summary=read(args.q_panel_summary)
    qdensity=metadata_without_array(args.q_density,'rows');sdensity=metadata_without_array(args.strong_density,'rows')
    reference={key:read_field(args.reference,key) for key in ('modes','checks')}
    box={key:read_field(args.box,key) for key in ('modes','gates','input_hashes')}
    cut=metadata_without_array(args.cut,'nonlinear_derivative_columns')
    physical=read_field(args.ready,'physicalParameters')
    guard(args.rss_limit_mib)
    if columns['modes']!=allm or reference['modes']!=allm or box['modes']!=allm or panel_summary['modes']!=allm:
        raise ValueError('The auxiliary field and background must retain all46 modes')
    if not all(reference['checks'].values()) or not all(box['gates'].values()) or not all(qdensity['gates'].values()) or not all(sdensity['gates'].values()) or not cut['all_gates']:
        raise ValueError('An original true head/domain certificate is unpaid')
    for name in ('columns','ordered','q_density','ready'):
        if hashes[str(getattr(args,name))] not in panel_summary['input_hashes'].values():raise ValueError('A real ordered panel dependency differs')
    if box['input_hashes'].get(str(args.reference))!=hashes[str(args.reference)]:raise ValueError('The actual auxiliary centre differs')
    for name in ('reference','box','strong_density','ready'):
        if cut['input_hashes'].get(str(getattr(args,name)))!=hashes[str(getattr(args,name))]:raise ValueError('The cut and actual source/domain differ')
    origin=sdensity['continuous_strip_origin']
    if origin['path']!=str(args.q_density) or origin['sha256']!=hashes[str(args.q_density)]:raise ValueError('The entire continuous strip identity is required')
    lowdeps=read_field(args.strong_low,'input_hashes')
    for name in ('columns','ordered','q_density','reference','box','strong_density'):
        if lowdeps.get(str(getattr(args,name)))!=hashes[str(getattr(args,name))]:raise ValueError('The actual strong source-factor provider changed')
    profile_keys=('Xbar','canonical_actual_m2','canonical_rest','source_factors')
    strong_profiles={r['cell']:{key:r[key] for key in profile_keys} for r in iter_array(args.strong_low,'source_profiles')}
    if sorted(strong_profiles)!=cells:raise ValueError('Every actual source-profile cell is required')
    fields=('B','Q_coefficient','mu_lower','mu_upper','normalized_width_upper','TV_log_w_upper','w_lower','tau_inner','tau_outer','canonical_total_envelope','V_over_w_upper')
    qd={r['cell']:{key:r[key] for key in fields} for r in iter_array(args.q_density,'rows')}
    sd={r['cell']:{key:r[key] for key in fields} for r in iter_array(args.strong_density,'rows')}
    ref={r['cell']:{'tau':r['tau']} for r in iter_array(args.reference,'cell_rows')}
    guard(args.rss_limit_mib)
    if sorted(qd)!=cells or sorted(sd)!=cells or sorted(ref)!=cells:raise ValueError('The213 real cells are required')
    common=('B','Q_coefficient','mu_lower','mu_upper','normalized_width_upper','TV_log_w_upper','w_lower','tau_inner','tau_outer')
    for n in cells:
        for key in common:
            if qd[n][key]['lower']!=sd[n][key]['lower'] or qd[n][key]['upper']!=sd[n][key]['upper']:raise ValueError('The common real source or strip changed')
        if sd[n]['canonical_total_envelope']!=strong_profiles[n]['Xbar']:raise ValueError('The physical source norm changed')
        if not top(sd[n]['B'])>=120 or not top(sd[n]['V_over_w_upper'])<arb(1)/64:raise ValueError('The complete two-material mean domain is unpaid')
    rc=exact_q(physical['rCuff'])
    b=ball(cut['true_radius']);w=ball(cut['true_w']);root=arb(12).sqrt()
    mu0=endpoint(sd[12]['mu_lower']['lower']);ci=(root.upper()*top(sd[12]['mu_upper'])/(b.lower()**4*w.lower()**2)).upper()
    sigma=arb(1)/64
    refined={}
    for row in iter_array(args.ordered,'mode_rows'):
        if row['mode'] in modes:
            for entry in row['refined_cells']:refined[(row['mode'],entry['cell'])]=entry
    caps={};panel_hashes={}
    if [r['cell'] for r in panel_summary['cells']]!=list(range(12,24)):raise ValueError('All12 precise shallow source providers are required')
    for item in panel_summary['cells']:
        path=Path(item['path']);h=digest(path)
        if h!=item['sha256']:raise ValueError('A saved source integral provider changed')
        panel_hashes[str(path)]=h
        for row in iter_array(path,'rows'):
            if row['mode'] in modes:caps[(row['mode'],item['cell'])]={key:{'phi_Q_source_integral':row[key]['phi_Q_source_integral']} for key in ('main','corr','base','remainder')}
    guard(args.rss_limit_mib)
    per_mode={m:[] for m in modes};group_hashes={}
    for group_ref in columns['column_groups']:
        selected=[m for m in group_ref['modes'] if m in modes]
        if not selected:continue
        path=Path(group_ref['path']);h=digest(path)
        if h!=group_ref['sha256']:raise ValueError('A true linear column group changed')
        group_hashes[str(path)]=h;meta=metadata_without_array(path,'cell_rows');gains={}
        for er in meta['endpoint_rows']:
            if er['mode'] not in selected:continue
            lo,hi=endpoint(er['Q_gain']['lower']),endpoint(er['Q_gain']['upper'])
            if not(lo>0 or hi<0):raise ArithmeticError('The true low height chart contains0')
            gains[er['mode']]=lo if lo>0 else -hi
        seen=[]
        for raw in iter_array(path,'cell_rows'):
            n=raw['cell'];seen.append(n);dn=sd[n];profile=strong_profiles[n]
            X=top(dn['canonical_total_envelope']);aa=top(dn['Q_coefficient']);mulo=endpoint(dn['mu_lower']['lower']);muhi=top(dn['mu_upper']);wl=endpoint(dn['w_lower']['lower'])
            mu_ratio=(top(raw['mu'])/mu0).upper()
            if not mulo>0 or not wl>0:raise ArithmeticError('A positive true source bound is missing')
            Vsup=(X*(aa*b.upper()**3+root.upper()*muhi/(rc**4*wl))).upper()
            cint=(top(dn['normalized_width_upper'])+top(dn['TV_log_w_upper'])).upper()
            J=(b.upper()**4*Vsup**2*cint/(root.lower()*mulo)).upper()
            tauin=top(dn['tau_inner']);tauout=endpoint(dn['tau_outer']['lower']);tauref=endpoint(ref[n]['tau']['lower'])
            if not tauref>=tauin:raise ArithmeticError('The wider canonical source strip is required')
            shrink=(-2*(tauref-tauin)).exp().upper()
            eps=(top(profile['canonical_rest'])/X*shrink).upper()
            x2=(top(profile['canonical_actual_m2'])/X*shrink).upper()
            A=top(dn['V_over_w_upper'])
            factors=dict(main=(3*x2).upper(),corr=eps,base=arb(1),remainder=A)
            if not eps<1 or not x2<1:raise ArithmeticError('The auxiliary decomposition does not fit its paid full physical unit ball')
            for lr in raw['linear_rows']:
                m=lr['mode']
                if m not in selected:continue
                phi=(top(lr['column_Q_sup'])/gains[m]).upper()
                old=refined.get((m,n))
                if old:phi=min(phi,top(old['refined_phi_Q_sup']))
                whole=(phi*J*(-m*tauout).exp()).upper()
                integrals={key:(whole*fac).upper() for key,fac in factors.items()}
                cap=caps.get((m,n))
                if cap:
                    for key in integrals:
                        saved=(top(cap[key]['phi_Q_source_integral'])*top(profile['source_factors'][key])).upper()
                        integrals[key]=min(integrals[key],saved)
                # R33(33.99), (33.96); Q(C2) is exactly absent at m!=4.
                pure=(x2*integrals['main']/2).upper() if m==4 else arb(0)
                gain2=(-2*tauref-2*tauout).exp().upper() if m==2 else arb(1)
                gap=tauref-tauin
                gain_quadratic=(-(m-4)*gap).exp().upper() if m>=6 else gain2
                gain_reference=(-m*gap).exp().upper()
                if not 0<gain_quadratic<=1 or not 0<gain_reference<=1:
                    raise ArithmeticError('The complete canonical strip gain is invalid')
                cross=(gain_quadratic*eps*integrals['main']).upper()
                quadratic_rest=(gain_quadratic*arb(3)/2*eps*integrals['corr']).upper()
                full_remainder=(27*gain_reference*integrals['remainder']).upper()
                support_value=(mu_ratio*(pure+cross+quadratic_rest+full_remainder)).upper()
                generic_value=(mu_ratio*gain_reference*(arb(3)/2+27*A)*integrals['base']).upper()
                value=min(support_value,generic_value)
                per_mode[m].append(dict(cell=n,phi_source_integrals={k:ball_record(v) for k,v in integrals.items()},
                    mu_ratio_upper=ball_record(mu_ratio),rest_physical_norm_upper=ball_record(eps),m2_physical_norm_upper=ball_record(x2),
                    pure_m2_quadratic_output_is_zero=m!=4,
                    low2_difference_frequency_angular_gain=ball_record(gain2),
                    nonprincipal_quadratic_reference_strip_gain=ball_record(gain_quadratic),
                    complete_remainder_and_generic_reference_strip_gain=ball_record(gain_reference),
                    source_pieces_before_mu_ratio=dict(pure_m2=ball_record(pure),cross=ball_record(cross),quadratic_rest=ball_record(quadratic_rest),complete_remainder=ball_record(full_remainder)),
                    auxiliary_cut_Xi_contribution_upper=ball_record(value),canonical_strip_generic_source_Xi_upper=ball_record(generic_value),
                    exact_ordered_source_panels_used=cap is not None))
            if (n-12)%32==0:guard(args.rss_limit_mib)
        if seen!=cells:raise ValueError('A true source column skipped a physical cell')
    rows=[]
    for m in modes:
        terms=per_mode[m]
        if [t['cell'] for t in terms]!=cells:raise ValueError('An output functional lacks a source cell')
        Xi=sum((top(t['auxiliary_cut_Xi_contribution_upper']) for t in terms),arb(0)).upper()
        K=(ci*Xi).upper();weighted=((1+m)*(m*sigma).exp()*K).upper()
        er=next(r for r in cut['B0'] if r['mode']==m)
        linear=(abs(ball(er['linear_minus_saved_candidate_K'])).upper()*(1+m)*(m*sigma).exp()).upper()
        remainder=top(cut['beta']['outer']['full_head_low_correction_K'])
        final=(weighted+linear+remainder).upper()
        old=top(cut['beta']['outer']['auxiliary_low_correction_K'])
        rows.append(dict(mode=m,auxiliary_Xi_inner_coefficient_upper=ball_record(Xi),auxiliary_Kbar_coefficient_upper=ball_record(K),
            auxiliary_Kbar_Wsigma1_upper=ball_record(weighted),previous_valid_same_mode_upper_from_full_low_box=ball_record(old),
            log2_auxiliary_bound_improvement=ball_record((old/weighted).log()/arb(2).log()),
            known_linear_minus_candidate_Wsigma1_upper=ball_record(linear),
            complete_auxiliary_far_and_full_head_correction_not_in_this_source_bound=True,
            largest_source_cell=max(terms,key=lambda r:top(r['auxiliary_cut_Xi_contribution_upper']))['cell'],source_rows=terms))
    checks=dict(all213_source_cells_retained=all(len(per_mode[m])==213 for m in modes),
        full46_auxiliary_centre_retained=True,whole_mean_and_inverse_remainder_retained=True,
        real_phi_columns_and_cut_Wronskian=True,identical_continuous_q_strip=True,
        actual_strong_source_rescaling=True,pure_m2_quadratic_frequency_support_retained=True,
        no_auxiliary_nonlinear_far_boundary_added=True,
        low2_difference_frequency_gain_applied_only_to_cross_and_Rc_squared=True,
        wider_reference_strip_unit_ball_from_full_R39_auxiliary_box=True,
        complete_mean_and_inverse_remainder_uses_reference_strip=True,
        all_high_selected_quadratic_frequency_support_gains_retained=True)
    result=dict(status='Actual auxiliary source-only cut momentum; explicit wider-reference-strip gains, with nonlinear far lift still separate',checks=checks,all_gates=all(checks.values()),
        selected_modes=modes,full46_output_paid=modes==allm,auxiliary_input_modes=allm,cells=cells,
        source_functional='Xi12(b)=+/-sum_n(mu_n/mu12) integral phi_Q,m F_n,m dr; psi_Q(b)=0, psi_Xi12(b)=1. Absolute bounds do not assert that the true nonlinear correction vanishes.',
        source_bound='R63 exact source functional; m>=6 cross/Rc-squared additionally gain exp(-(m-4)*(tau_ref-tau_inner)). Complete mean/inverse cubic and generic source use the full canonical-reference unit ball and gain exp(-m*(tau_ref-tau_inner)). Original m2 difference gain is retained. All fixed modal masses precede radial sup. This output does not include B D(z_aux).',
        point_cut_K_conversion=ball_record(ci),outer_strip='1/64',rows=rows,
        whole_head_new_solution_claimed=False,actual_outer_Schur_paid=False,signed_outer_source_cancellation_evaluated=False,
        input_hashes=hashes,panel_hashes=panel_hashes,group_hashes=group_hashes,source_sha256=digest(__file__),frozen_R63_v3_source_sha256='ce42ce8a3dc40f8d03afc810ba33a215dcacd032b06f15433cea5fe38b3ba038',
        helper_hashes={name:digest(Path(__file__).with_name(name)) for name in ('closure_split_joint_io_v2.py','closure_real_head_source_enclosure.py','closure_real_head_green_enclosure.py')},
        new_source_quadrature=0,new_flow_solves=0,elapsed_seconds=time.monotonic()-start,peak_RSS_KiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    guard(args.rss_limit_mib)
    del cut,qd,sd,reference,box,columns,physical
    gc.collect()
    with gzip.open(args.out,'wt',encoding='utf-8',compresslevel=6) as f:json.dump(result,f,separators=(',',':'))
    guard(args.rss_limit_mib)
    print(json.dumps(dict(event='done',modes=modes,all_gates=result['all_gates'],rows=[dict(mode=r['mode'],auxiliary_Wsigma1=str(ball(r['auxiliary_Kbar_Wsigma1_upper'])),improvement_bits=str(ball(r['log2_auxiliary_bound_improvement'])),source_only=True) for r in rows],seconds=result['elapsed_seconds'],RSS_KiB=result['peak_RSS_KiB'],sha256=digest(args.out))),flush=True)


if __name__=='__main__':main()
