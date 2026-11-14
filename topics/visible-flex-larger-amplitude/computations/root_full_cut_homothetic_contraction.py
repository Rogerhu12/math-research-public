#!/usr/bin/env python3
"""Exact postprocessing of the complete R141 field on half the expanded domain.
Author: /root (GPT-6 Astra Pro, AI-assisted), 2026-11-13.
No new ODE, solve, source integral, altered axis, or truncated nonlinear source.
"""
from pathlib import Path
from fractions import Fraction as F
import argparse,gzip,hashlib,json,time,resource

def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def read(p):
    p=Path(p);raw=p.read_bytes();return json.loads(gzip.decompress(raw) if p.suffix=='.gz' else raw)
def ex(x):
    if isinstance(x,int):return F(x)
    if isinstance(x,dict):
        if 'upper' in x:return F(int(x['upper']['mantissa']))*F(2)**int(x['upper']['binary_exponent'])
        return F(int(x['numerator']),int(x['denominator']))
    if isinstance(x[1],int):return F(int(x[0]))*F(2)**x[1]
    return F(int(x[0]),int(x[1]))
def exact(x):return {'numerator':str(x.numerator),'denominator':str(x.denominator)}
def upper(x,bits=192):
    assert x>=0
    if not x:return {'upper':{'mantissa':'0','binary_exponent':0},'display':0.0}
    e=x.numerator.bit_length()-x.denominator.bit_length()
    if x<F(2)**e:e-=1
    shift=e-bits+1;scaled=x/F(2)**shift;m=-(-scaled.numerator//scaled.denominator)
    q=F(m)*F(2)**shift;assert q>=x
    return {'upper':{'mantissa':str(m),'binary_exponent':shift},'display':float(q)}

def main():
    p=argparse.ArgumentParser();p.add_argument('--inputs',type=Path,required=True);p.add_argument('--out',type=Path,required=True);a=p.parse_args();started=time.monotonic()
    assert not a.out.exists();ids=read(a.inputs);gates={}
    def gate(name,value):
        gates[name]=bool(value)
        if not value:raise ArithmeticError(name)
    def checked(key):
        rec=ids[key];gate('identity_'+key,sha(rec['path'])==rec['sha256']);return read(rec['path'])
    full=checked('full_field');fr=checked('full_resource');projected=checked('projected_profile');profile=checked('expanded_profile');audit=checked('independent_saved_audit');ar=checked('independent_audit_resource')
    gate('owned_full_and_audit_exit_zero',fr['exitcode']==ar['exitcode']==0 and fr['termination_signal'] is None and ar['termination_signal'] is None)
    gate('independent_complete_saved_audit',audit['all_audit_gates'] and all(audit['gates'].values()) and audit['complete_original_two_cell_parameter_selfmap'] and audit['certificate']['sha256']==ids['full_field']['sha256'] and audit['resource']['sha256']==ids['full_resource']['sha256'] and audit['same_full_R127_field'] and audit['stronger_separately_saved_positive_sum_used'] and audit['complete_T_shared_mass_paid_once'] and audit['all186_windows_and_parent94_mass_constraint_retained'])
    gate('complete_original_field_and_true_selfmap',full['all_gates'] and all(full['gates'].values()) and full['same_existing_R127_field'] and full['original_two_cell_low46_parameter_selfmap_certified'] and full['complete_mean_inverse_and_infinite_high_retained'] and full['all185_windows_and_original_source_materials_retained'] and full['all186_refinement_and_parent94_constraint_retained'])
    gate('same_source_and_original_axes',full['source_sha256']=='31adc4e8163ab69293fcfe3a8c7b134c36d0fdc4f41260babf11669a81c42a12' and full['low_helper_sha256']=='3d4ac8d58f9fe7683a13d29519f379fd6eff15a4cb4a0da6721e02767626a025' and projected['all_gates'] and projected['same_existing_R124_projected_low_solution'] and projected['same_original_axes_and_parameters'] and projected['complete_mean_inverse_and_true_far_retained'] and profile['all_gates'] and profile['original_axis_formulas_unchanged'])
    gate('same_profile_pins',full['inputs']['projected_profile']['sha256']==ids['projected_profile']['sha256'] and full['inputs']['restricted_profile_lift']['sha256']==ids['expanded_profile']['sha256'] and profile['inputs']['projected_profile']['sha256']==ids['projected_profile']['sha256'])
    w=next(x for x in profile['domains'] if x['name']=='R133_working');e=next(x for x in profile['domains'] if x['name']=='expanded_profile')
    modes=list(range(2,93,2));gate('original46_modes',[r['mode'] for r in projected['rows']]==modes and profile['modes']==modes)
    wr=list(map(ex,w['original_normalized_T_coordinate_caps']));er=list(map(ex,e['original_normalized_T_coordinate_caps']))
    KS=F(3,8);KT=F(1,64)
    gate('homothetic_S_T',ex(e['S_linf_radius'])==2*KS and ex(e['T_l1_radius'])==2*KT)
    gate('K_inside_original_working',KS<=ex(w['S_linf_radius']) and KT<=ex(w['T_l1_radius']))
    gate('original_working_inside_expanded',ex(w['S_linf_radius'])<=ex(e['S_linf_radius']) and ex(w['T_l1_radius'])<=ex(e['T_l1_radius']) and all(x<=y for x,y in zip(wr,er)))
    gate('six_T_placeholders_ignored',wr[:6]==er[:6]==[F(0)]*6)
    gate('all40_positive_original_T_axes',len(wr)==len(er)==46 and all(x>0 and y==2*x for x,y in zip(wr[6:],er[6:])))
    gate('complete_bounds_on_exact_expanded_domain',full['bounds_apply_only_to_restricted_parameter_domain'] and ex(full['same_parameter_domain']['S_product_radius'])==ex(e['S_linf_radius']) and ex(full['same_parameter_domain']['T_l1_radius'])==ex(e['T_l1_radius']) and list(map(ex,full['same_parameter_domain']['T_coordinate_caps_by_mode']))==er)
    c=full['final_cut'];components=c['component_mode_caps'];required=['C_low','low_squared','low_middle','middle_squared','middle_high','high_squared','complete_T']
    gate('all_seven_complete_components',set(components)==set(required) and all(len(v)==46 for v in components.values()))
    rows=[];delta=[];ratios=[]
    for i,m in enumerate(modes):
        pieces=[ex(components[k][i]) for k in required];gate('positive_full_components_'+str(m),all(x>0 for x in pieces))
        correction=max(ex(c['mode_caps'][i]),sum(pieces,F(0)));delta.append(correction)
        b=ex(projected['rows'][i]['projected_map_value']);radius=KS if i<6 else wr[i]
        if i>=6:gate('same_axis_2b_'+str(m),radius==2*b)
        value=b+correction;ratio=value/radius;gate('strict_K_axis_'+str(m),value<radius)
        ratios.append(ratio);rows.append({'mode':m,'projected_bound':upper(b),'conservative_full_nonlow_correction':upper(correction),'complete_map_upper':upper(value),'K_radius':exact(radius),'ratio':upper(ratio)})
    gate('all25_shared_T_rows',len(c['source_rows'])==25 and [x['source_block'] for x in c['source_rows']]==list(range(25)))
    common=max(ex(c['complete_T_shared']),sum((ex(x['T_common_mass_paid_once']) for x in c['source_rows']),F(0)))
    t_nonlow=max(ex(c['T_l1']),sum((ex(components[k][i]) for k in required if k!='complete_T' for i in range(6,46)),F(0))+common)
    t_total=ex(projected['T_projected_map'])+t_nonlow;t_ratio=t_total/KT
    gate('strict_K_shared_T',t_total<KT)
    q=max([*ratios,t_ratio]);q_saved=ex(upper(q))
    gate('complete_cauchy_contraction_below_191_over200',q<=q_saved<F(191,200)<1)
    gate('shared_T_is_worst_gauge_component',q==t_ratio)
    # Record the actual failure of an indiscriminate old-hybrid distance bound.
    old_gaps=[ex(e['S_linf_radius'])-ex(w['S_linf_radius']),ex(e['T_l1_radius'])-ex(w['T_l1_radius']),*[y-x for x,y in zip(wr[6:],er[6:])]]
    old_delta=min(old_gaps);old_i=old_gaps.index(old_delta);B=max(max(delta[:6]),t_nonlow)
    old_lip=ex(projected['original_norm_Lipschitz_bound'])+B/old_delta
    gate('old_hybrid_common_distance_test_fails_as_recorded',old_i>=2 and modes[old_i+4]==52 and old_lip>1)
    inv=1/(1-q_saved);gate('inverse_contraction_margin_below22',inv<22)
    out={'schema':'complete-R141-half-expanded-domain-Cauchy-contraction-v1','author':'/root (GPT-6 Astra Pro, AI-assisted)','source_sha256':sha(__file__),'input_manifest_sha256':sha(a.inputs),'inputs':ids,'all_gates':all(gates.values()),'gates':gates,'gate_count':len(gates),'same_complete_R127_field_and_R141_cut':True,'complex_holomorphy_source':'R127 (127.1), (127.2), parameter holomorphy; R124 projected map holomorphy','K':{'S_linf_radius':exact(KS),'T_l1_radius':exact(KT),'T_coordinate_radii':list(map(exact,wr[6:])),'complex_balanced_convex_norm':True},'expanded_exactly_2K':True,'rows':rows,'full_T_correction_common_paid_once':upper(t_nonlow),'full_T_map':upper(t_total),'full_T_K_ratio':upper(t_ratio),'complete_K_image_and_derivative_norm_upper':upper(q),'inverse_I_minus_DPhi_upper':upper(inv),'unique_real_fixed_point_in_K_and_original_working_domain':True,'old_hybrid_common_distance_diagnostic':{'smallest_slack_mode':52,'exact_slack':exact(old_delta),'nonlow_B':upper(B),'B_over_delta':upper(B/old_delta),'projected_plus_nonlow_upper':upper(old_lip),'not_a_contraction_certificate':True},'no_old_hybrid_Lipschitz_transferred_to_new_norm':True,'no_external_t_family_or_closed_surface_claimed':True,'no_new_ODE_or_source_integral':True,'elapsed_seconds':time.monotonic()-started,'peak_rss_kib':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss}
    a.out.parent.mkdir(parents=True,exist_ok=True);a.out.write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({'all_gates':out['all_gates'],'gates':len(gates),'q':float(q),'inverse_margin':float(inv),'old_hybrid_bound':float(old_lip),'primary_sha256':sha(a.out),'bytes':a.out.stat().st_size}),flush=True)
if __name__=='__main__':main()
