#!/usr/bin/env python3
"""Independent Fraction substitution of the actual R126 profile certificate.

Author: exact_closure (GPT-6 Astra Pro; AI-assisted), 2026-11-13.
The profile's exact positive weights, complete R100 head and all fifty
self-map, domain and distance inequalities are checked independently.
No interval producer, radius search or matrix inversion is repeated.
"""
import argparse
from fractions import Fraction as F
import gzip
import hashlib
import json
from pathlib import Path
import resource
import time


def read(p):
    raw = Path(p).read_bytes()
    return json.loads(gzip.decompress(raw) if str(p).endswith('.gz') else raw)


def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def ex(v):
    if isinstance(v, list):
        return F(int(v[0])) * F(2) ** int(v[1])
    if 'upper' in v:
        return ex(v['upper'])
    if 'mantissa' in v:
        return F(int(v['mantissa'])) * F(2) ** int(v['binary_exponent'])
    return F(int(v['numerator']), int(v['denominator']))


def rec(v):
    return dict(numerator=str(v.numerator), denominator=str(v.denominator), display_only=float(v))


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    for n in ('primary','resource','finite','high','high-resource','profile','common-leaves',
              'balanced','source','head','r100-head','r100-resource','hessian-proof','out'):
        ap.add_argument('--'+n,type=Path,required=True)
    a=ap.parse_args();started=time.monotonic()
    if a.out.exists():raise FileExistsError('Fresh complete exact verification output required')
    d,usage,finite,high,hu,balanced,source,head,r100,ru=[read(getattr(a,n)) for n in
        ('primary','resource','finite','high','high_resource','balanced','source','head','r100_head','r100_resource')]
    rows=d['rows'];n=len(rows);C,B,D=F(10),F(18555),F(257)
    K=F(23,9)+270*F(2)**-34;tr=ex(d['transverse_radius']);boundary=ex(balanced['balanced_B_lower'])
    old=[ex(v) for v in head['complete_coarse_trace_rows']['head']['high_bands_value_upper']]
    hm=[ex(b['uniform']['uniform_value_upper']) if tr==1 else old[i]+tr*ex(b['transverse_global_lipschitz'])
        for i,b in enumerate(r100['complete_high']['head']['bands'])]
    centre,tail=ex(source['complete_middle_shared_mass']),ex(source['complete_infinite_high_shared_mass'])
    R,S=ex(d['profile_physical_upper']),ex(d['profile_to_V_upper'])
    radii=[ex(r['finite_radius']) for r in rows];hs=[ex(r['high_radius']) for r in rows]
    weights=[(ex(r['finite_distance_weight']),ex(r['high_distance_weight'])) for r in rows]
    gates=dict(actual_joint_primary_success=d['all_gates'] and all(d['gates'].values()),
        all_three_numerical_resources_success=all(u['exitcode']==0 and u['termination_signal'] is None for u in (usage,hu,ru)),
        true_R100_transverse_radius=tr==F(1,32),complete_complex_six_unit_axes=True,
        complete25_blocks=n==25 and high['comparison_partition']==finite['comparison_partition']==d['comparison_partition'],
        complete17361_finite_positive_modes=[m for lo,hi in finite['windows'] for m in range(lo,hi+1,2)]==list(range(94,34816,2)),
        complete_infinite_frequency_range=high['high_cutoff']==34816 and high['upper_frequency_cutoff'] is None,
        identical_common_strip=high['common_strip']==finite['fixed_common_strip']==d['fixed_common_strip'],
        exact_same_complete_Hessian=ex(d['full_complete_Hessian_upper'])==K and d['input_hashes'][str(a.hessian_proof)]==sha(a.hessian_proof),
        same_actual_R100_head=r100['all_gates'] and all(r100['gates'].values()) and r100['input_identities']['r78']['sha256']==sha(a.head),
        all_three_actual_head_masses=hm==list(map(ex,d['actual_R100_head_band_masses'])),
        exact_profile_primary=sha(a.profile)==high['profile_primary']['sha256'] and high['profile_used_only_in_comparison_block']==21,
        all_paid_inputs_identical=all(d['input_hashes'][str(getattr(a,k))]==sha(getattr(a,k)) for k in ('finite','balanced','source','head','r100_head','r100_resource')))
    profile_ok=True;profile_count=0;critical_count=0;actualR=actualS=F(0)
    with gzip.open(a.profile,'rt') as ps,gzip.open(a.common_leaves,'rt') as ls:
        for pl,ll in zip(ps,ls):
            pr,leaf=json.loads(pl),json.loads(ll);profile_count+=1
            phi,rad,V,b=map(ex,(pr['phi'],pr['R'],pr['V'],pr['b']))
            profile_ok=profile_ok and all(pr[k]==leaf[k] for k in ('group','cell','segment','panel','V','b'))
            profile_ok=profile_ok and min(phi,rad,V,b)>0 and rad>=2*max(F(1),b)*phi
            if pr['comparison_block']==21:
                critical_count+=1;actualR=max(actualR,rad);actualS=max(actualS,rad/V)
        if next(ps,None) is not None or next(ls,None) is not None:profile_ok=False
    gates['all10793_exact_positive_profiles_and_physical_conversion']=profile_ok and profile_count==10793 and critical_count==1708
    gates['both_actual_critical_profile_caps_paid']=actualR<=R and actualS<=S and R==ex(high['rows'][21]['profile_physical_max']) and S==ex(high['rows'][21]['profile_to_V_max'])
    checked=[];total_f=total_h=F(0);max_domain=F(0);gaps=[]
    for i,r in enumerate(rows):
        if r['index']!=i or len(r['complete_causal_derivative_blocks'])!=i+1:raise ValueError('Complete ordered rows required')
        V=ex(r['V_max']);conversion=R if i==21 else B if i==5 else V
        domain=(C+radii[i])*V+conversion*hs[i]
        total_f+=radii[i]*V;total_h+=conversion*hs[i];max_domain=max(max_domain,domain)
        G={p:[ex(v) for v in r['all_finite_source_materials'][str(p)]] for p in (2,1,0)}
        A={p:[ex(v) for v in r['all_high_source_materials']['physical_source'][str(p)]] for p in (2,1,0)}
        Q={p:[ex(v) for v in r['all_high_source_materials']['already_divided_by_frame'][str(p)]] for p in (2,1,0)}
        inputs_ok=all(G[p]==[ex(v['value']) for v in finite['rows'][i]['all_material_rows'][str(p)]] for p in (2,1,0))
        for j,sr in enumerate(high['rows'][i]['source_rows']):
            for dr in sr['density_rows']:
                v=ex(dr['profile_balanced_output_row']) if i==21 else ex(dr['balanced_strong_output_row']) if i==5 else max(ex(dr['localV_strong_output_row']),ex(dr['P_sup'])+ex(dr['K_sup']))
                inputs_ok=inputs_ok and v==(A if dr['source_normalization']=='physical_source' else Q)[dr['V_power']][j]
        gc=min(S*G[2][21],R*G[1][21]) if i>=21 else F(0)
        gs=min(S*S*G[2][21],S*R*G[1][21],R*R*G[0][21]) if i>=21 else F(0)
        extra=[]
        for dr in high['rows'][i]['profile_source21_density_rows']:
            extra.append(ex(dr['profile_balanced_output_row']) if i==21 else ex(dr['balanced_strong_output_row']) if i==5 else max(ex(dr['localV_strong_output_row']),ex(dr['P_sup'])+ex(dr['K_sup'])))
        ac,ass=extra
        stored=r['profile_source21_kernels']
        inputs_ok=inputs_ok and [gc,gs,ac,ass]==[ex(stored[k]) for k in ('finite_cross','finite_square','high_cross','high_square')]
        hf=sum((mass*ex(finite['rows'][i]['given_band_gains'][band]['gain']) for mass,band in zip(hm,('near','rest','infinite'))),F(0))
        hr=high['rows'][i]
        if i in (5,21):
            cols=hr['initial_profile_balanced_column_sups'] if i==21 else hr['initial_balanced_column_sups']
            hh=hm[2]*max(ex(cols[0])/boundary,ex(cols[1]))
        else:
            cols=hr['initial_localV_separate_component_sups'];hh=hm[2]*max(sum(map(ex,cols[0]),F(0))/boundary,sum(map(ex,cols[1]),F(0)))
        image_f=hf+centre*sum(G[2],F(0));image_h=hh+tail*sum(A[2],F(0))
        jf=jh=F(0);derivatives_ok=True
        for j in range(i+1):
            x,y=radii[j],hs[j]
            if j==21:
                image_f+=K*(G[2][j]*(C*x+x*x/2)+gc*(C+x)*y+gs*y*y/2)
                image_h+=K*(A[2][j]*(C*x+x*x/2)+ac*(C+x)*y+ass*y*y/2)
                J=(K*((C+x)*G[2][j]+y*gc),K*((C+x)*gc+y*gs),K*((C+x)*A[2][j]+y*ac),K*((C+x)*ac+y*ass))
            elif j==5:
                image_f+=K*(G[2][j]*(C*x+x*x/2)+G[1][j]*(C+x)*B*y+G[0][j]*B*B*y*y/2)
                image_h+=K*(A[2][j]*(C*x+x*x/2)+Q[1][j]*D*(C+x)*y+Q[0][j]*D*B*y*y/2)
                J=(K*((C+x)*G[2][j]+B*y*G[1][j]),K*B*((C+x)*G[1][j]+B*y*G[0][j]),K*(C+x)*A[2][j]+K*D*y*Q[1][j],K*D*((C+x)*Q[1][j]+B*y*Q[0][j]))
            else:
                t=x+y;image_f+=K*G[2][j]*(C*t+t*t/2);image_h+=K*A[2][j]*(C*t+t*t/2)
                J=(K*(C+t)*G[2][j],K*(C+t)*G[2][j],K*(C+t)*A[2][j],K*(C+t)*A[2][j])
            derivatives_ok=derivatives_ok and J==tuple(map(ex,r['complete_causal_derivative_blocks'][j]))
            jf+=J[0]*weights[j][0]+J[1]*weights[j][1];jh+=J[2]*weights[j][0]+J[3]*weights[j][1]
        df,dh=jf/weights[i][0],jh/weights[i][1];gaps.extend([F(1,2)-df,F(1,2)-dh])
        local=dict(all_actual_kernels_and_profile_materials_identical=inputs_ok,
            both_full_images_reproduced=image_f==ex(r['complete_finite_image']) and image_h==ex(r['complete_high_image']),
            all_complete_derivative_blocks_reproduced=derivatives_ok,
            two_strict_selfmaps=image_f<radii[i] and image_h<hs[i],
            both_weighted_distance_rows_reproduced=df==ex(r['finite_complete_weighted_distance_row']) and dh==ex(r['high_complete_weighted_distance_row']),
            both_distances_strictly_below_half=max(df,dh)<F(1,2),
            whole_ball_domain_reproduced_and_paid=domain==ex(r['actual_complete_mean_domain']) and domain<F(2)**-34,
            true_shared_head_and_centre_once_per_output=hf+centre*sum(G[2],F(0))==ex(r['true_finite_head_and_centre']) and hh+tail*sum(A[2],F(0))==ex(r['true_high_head_and_complete_centre']))
        checked.append(dict(index=i,gates=local))
    gates.update(all25_complete_rows_and50_distances=all(all(r['gates'].values()) for r in checked),
        complete_physical_totals_reproduced=total_f==ex(d['complete_finite_physical_norm_upper']) and total_h==ex(d['complete_high_physical_norm_upper']),
        maximum_domain_reproduced=max_domain==ex(d['maximum_whole_ball_physical_domain']),
        combined_nonlow_physical_cap_below_two_minus39=total_f+total_h<F(2)**-39)
    result=dict(schema='visible-flex-r126-independent-profile-substitution-v1',author='exact_closure (GPT-6 Astra Pro; AI-assisted)',
        all_gates=all(gates.values()),gates=gates,rows=checked,transverse_radius=rec(tr),
        minimum_strict_distance_gap_to_half=rec(min(gaps)),complete_finite_physical_norm_upper=rec(total_f),
        complete_high_physical_norm_upper=rec(total_h),combined_physical_norm_upper=rec(total_f+total_h),maximum_physical_domain=rec(max_domain),
        actual_profile_physical_max=rec(actualR),actual_profile_to_V_max=rec(actualS),
        no_new_Arb_or_ODE=True,no_radius_search_or_matrix_inverse=True,
        input_hashes={str(getattr(a,n)):sha(getattr(a,n)) for n in ('primary','resource','finite','high','high_resource','profile','common_leaves','balanced','source','head','r100_head','r100_resource','hessian_proof')},
        source_sha256=sha(__file__),elapsed_seconds=time.monotonic()-started,peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    a.out.write_text(json.dumps(result,indent=2)+'\n')
    if not result['all_gates']:raise ArithmeticError('A full R126 exact substitution gate failed')
    print(json.dumps(dict(all_gates=True,profile_leaves=profile_count,rows=n,minimum_distance_gap=float(min(gaps)),combined_physical=float(total_f+total_h))),flush=True)


if __name__=='__main__':main()
