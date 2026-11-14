#!/usr/bin/env python3
"""Independently consume every saved continuous q106 domain and cover gate.

Author: geometry_audit (GPT-6 Astra Pro; AI-assisted), 2026-11-13.
Exact Fraction arithmetic verifies saved positivity, identities, original
interval membership, full refined coverage, retained prior rows and every
binary radial subdivision. It does not repeat any ODE or interval geometry.
"""
import argparse
from fractions import Fraction as F
import gzip
import hashlib
import json
import math
from pathlib import Path


def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def read(p):
    p=Path(p);b=p.read_bytes();return json.loads(gzip.decompress(b) if p.suffix=='.gz' else b)
def rat(z):return F(int(z['numerator']),int(z['denominator']))
def saved(x):
    if not isinstance(x,(float,int)) or not math.isfinite(x):raise ArithmeticError('Finite binary endpoint required')
    return F.from_float(float(x))


def main():
    p=argparse.ArgumentParser(description=__doc__)
    for name in ('certificate','resource','prior','prior-resource','background','primary','out'):
        p.add_argument('--'+name,type=Path,required=True)
    a=p.parse_args()
    if a.out.exists():raise FileExistsError('Fresh independent full-domain saved check required')
    d,res,prior,pres,bg,primary=map(read,(a.certificate,a.resource,a.prior,a.prior_resource,a.background,a.primary))
    counts={}
    def check(name,ok):
        if not ok:raise ArithmeticError(name)
        counts[name]=counts.get(name,0)+1
    check('complete_original_and_refined_owned_exit_zero',res['exitcode']==pres['exitcode']==0 and res['wait4_observed'] and pres['wait4_observed'])
    check('same_actual_accepted_primary',d['primary_sha256']==prior['primary_sha256']==sha(a.primary) and primary['solver_success'] and not primary.get('audit_pending',True))
    check('final_complete_domain_and_no_failed_atoms',d['all_domain_gates'] and d['complete_original_interval_cover'] and not d['failed_atoms'])
    check('prior_negative_conclusion_retained',prior['complete_original_interval_cover'] and not prior['all_domain_gates'] and prior['failed_atoms']==135)
    for name in ('source_sha256',):
        check('actual_final_source_exists',sha(Path('computations/strong_newg_continuous_mean_domain_refine_v2.py'))==d[name])
        check('actual_prior_source_exists',sha(Path('computations/strong_newg_continuous_mean_domain.py'))==prior[name])
    for path,h in d['input_sha256'].items():check('all_pinned_actual_inputs_still_match',sha(path)==h)
    profile=next(r for r in bg['profiles'] if r['accepted_primary_sha256']==sha(a.primary))
    check('same_explicit_background_comparison',profile['comparison_definition_sha256']==d['background_comparison_definition_sha256'])
    mesh=list(map(saved,primary['mesh']));pieces=[tuple(map(rat,r['physical_interval'])) for r in profile['piece_rows']]
    old={(r['original_interval'],*r['s_interval']):r for r in prior['rows']}
    check('original_atoms_unique',len(old)==len(prior['rows']))
    seen_original=set();seen_old=set();cursor=F(0);reused=0;new=0;failed_by_index={}
    for r in prior['rows']:
        if not r['positive_domain']:failed_by_index.setdefault((r['original_interval'],r['background_piece']),[]).append(r)
    strict_keys=['radius_lower','chart_rho_lower','normalized_P_lower','normalized_W_lower','normalized_D_lower','frenet_margin_lower']
    minima={k:None for k in strict_keys};maxima={k:F(0) for k in ('normalized_P_upper','normalized_W_upper','normalized_D_upper','speed_absolute_upper')}
    for row in d['rows']:
        j=row['original_interval'];k=row['background_piece'];lo,hi=map(F,row['s_interval'])
        check('exact_complete_refined_physical_cover',lo==cursor and lo<hi);cursor=hi
        check('same_original_physical_quintic_interval',0<=j<len(mesh)-1 and mesh[j]<=lo<hi<=mesh[j+1]);seen_original.add(j)
        check('same_actual_background_piece',0<=k<len(pieces) and pieces[k][0]<=lo<hi<=pieces[k][1])
        check('full_real_angular_interval_cover_used',row['angular_intervals']>=512 and row['angular_intervals']&(row['angular_intervals']-1)==0)
        check('whole_interval_homotopy_domain_passed',row['positive_domain'] and row['whole_radial_angular_and_repair_homotopy_enclosed'])
        for key in strict_keys:
            value=saved(row[key]);check('saved_strict_domain_endpoint',value>0)
            minima[key]=value if minima[key] is None else min(minima[key],value)
        for key in maxima:maxima[key]=max(maxima[key],saved(row[key]))
        for prefix in ('normalized_P','normalized_W','normalized_D'):
            check('ordered_finite_domain_interval',saved(row[prefix+'_lower'])<=saved(row[prefix+'_upper']))
        for key in ('normalized_u_absolute_upper','normalized_v_absolute_upper'):
            check('all_three_saved_rotating_components_nonnegative',len(row[key])==3 and all(saved(x)>=0 for x in row[key]))
        if row.get('retained_original_positive_box_verbatim'):
            key=(j,str(lo),str(hi));other=dict(row);other.pop('retained_original_positive_box_verbatim')
            check('positive_prior_box_reused_exactly',key in old and old[key]['positive_domain'] and other==old[key]);seen_old.add(key);reused+=1
        else:
            matches=[r for r in failed_by_index.get((j,k),[]) if F(r['s_interval'][0])<=lo<hi<=F(r['s_interval'][1])]
            check('refined_only_a_genuinely_unpaid_original_box',len(matches)==1)
            root=matches[0];a0,a1=map(F,root['s_interval']);depth=row['radial_subdivision_depth']
            unit=(a1-a0)/2**depth;offset=(lo-a0)/unit
            check('exact_binary_radial_subdivision',0<=depth<=d['adaptive_exact_radial_refinement']['max_depth'] and hi-lo==unit and offset.denominator==1)
            check('actual_original_quintic_Bernstein_restriction_used',row['original_binary_quintic_exact_Bernstein_restricted'])
            seen_old.add((j,*root['s_interval']));new+=1
    check('both_global_endpoints_and_every_original_interval_covered',cursor==saved(primary['meridian_length']) and seen_original==set(range(len(mesh)-1)))
    check('every_original_positive_or_failed_atom_consumed',seen_old==set(old))
    info=d['adaptive_exact_radial_refinement']
    check('saved_refinement_counts_match',reused==info['retained_positive_prior_atoms'] and new==info['refined_leaves'] and len(d['rows'])==d['continuous_product_atoms'])
    check('prior_and_final_binding_exact',info['original_full_pass_sha256']==sha(a.prior) and d['original_intervals']==len(mesh)-1)
    output=dict(schema='independent-saved-continuous-mean-domain-consumption-v1',scope=__doc__,
        all_gates=True,gate_count=sum(counts.values()),gate_multiplicities=counts,
        source_sha256=sha(__file__),input_sha256={str(p):sha(p) for p in (a.certificate,a.resource,a.prior,a.prior_resource,a.background,a.primary)},
        original_intervals=len(mesh)-1,final_complete_atoms=len(d['rows']),retained_positive_prior_atoms=reused,exact_refined_leaves=new,
        strict_global_minima_exact={k:str(v) for k,v in minima.items()},strict_global_minima_display={k:float(v) for k,v in minima.items()},
        global_maxima_exact={k:str(v) for k,v in maxima.items()},complete_mean_float_alignment_or_target_g_error_certified=False,
        no_ODE_Node_Newton_or_geometry_recomputation=True)
    a.out.parent.mkdir(parents=True,exist_ok=True);a.out.write_text(json.dumps(output,indent=2)+'\n')
    print(json.dumps(dict(all_gates=True,gates=output['gate_count'],atoms=len(d['rows']),minima=output['strict_global_minima_display'],path=str(a.out),sha256=sha(a.out))),flush=True)


if __name__=='__main__':main()
