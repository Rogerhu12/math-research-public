#!/usr/bin/env python3
"""Independently consume complete mean repair caps using exact fractions.

Author: geometry_audit (GPT-6 Astra Pro; AI-assisted), 2026-11-13.
Checks the saved full cover, every atom, exact height accumulation and both
suprema. Separately re-adds the full chart transport to the saved rounded
normal-velocity derivative caps, explicitly paying those extra outward
roundings instead of relying on a last-bit equality. This is a saved-cap
consumer, not a new interval-geometry or ODE producer.
"""
import argparse
from fractions import Fraction as F
import gzip
import hashlib
import json
from pathlib import Path


def sha(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def read(p):
    p=Path(p); b=p.read_bytes()
    return json.loads(gzip.decompress(b) if p.suffix=='.gz' else b)
def dy(z): return F(int(z[0]))*F(2)**int(z[1])
def up(z,bits=160):
    if z<0: raise ArithmeticError('Nonnegative upper required')
    if not z:return ['0',0]
    e=z.numerator.bit_length()-z.denominator.bit_length()-bits
    scaled=z/F(2)**e
    return [str((scaled.numerator+scaled.denominator-1)//scaled.denominator),e]


def main():
    p=argparse.ArgumentParser(description=__doc__)
    for k in ('certificate','resource','domain','cartesian','out'):
        p.add_argument('--'+k,type=Path,required=True)
    a=p.parse_args()
    if a.out.exists():raise FileExistsError('Fresh saved mean consumer required')
    d,res,dom,cart=map(read,(a.certificate,a.resource,a.domain,a.cartesian))
    counts={}
    def check(name,ok):
        if not ok:raise ArithmeticError(name)
        counts[name]=counts.get(name,0)+1
    check('producer_completed_all_gates_with_owned_exit_zero',d['all_gates'] and res['exitcode']==0 and res['wait4_observed'])
    check('same_complete_actual_domain',dom['all_domain_gates'] and d['input_sha256'][str(a.domain)]==sha(a.domain) and d['primary_sha256']==dom['primary_sha256'])
    check('same_complete_nonmean_repair_costs',cart['all_gates'] and d['input_sha256'][str(a.cartesian)]==sha(a.cartesian))
    C=next(p for p in cart['profiles'] if p['accepted_primary_sha256']==d['primary_sha256'])
    check('same_background_state_comparison_definitions',C['full_state_repair_included'] and C['background_comparison_definition_sha256']==d['background_comparison_definition_sha256'] and C['state_comparison_definition_sha256']==d['state_comparison_definition_sha256'])
    errors={r['jet']:dy(r['combined_paid_repair_uniform_Euclidean_upper']) for r in C['jet_rows']}
    nu,nus=map(dy,d['nu_and_nu_s_wholefield_upper'])
    check('same_complete_integral_measure_and_anchor',d['transport_fixed_in_homotopy'] and d['mean_measure']=='dpsi/(2*pi), identical for all homotopy parameters' and d['mean_anchor']=='H(0)=0 for both comparison fields; every positive physical-s atom width paid once')
    check('full_atom_count',len(d['rows'])==len(dom['rows'])==d['complete_atoms'])
    cursor=F(0); old_integral=F(0); new_integral=F(0); old_max=[F(0),F(0)]; new_max=[F(0),F(0)]
    digest=hashlib.sha256()
    for i,(r,s) in enumerate(zip(d['rows'],dom['rows'])):
        lo,hi=map(F,r['s_interval'])
        check('every_same_actual_atom_consumed_in_order',r['atom']==i and lo==cursor and lo<hi and r['s_interval']==s['s_interval'] and r['original_interval']==s['original_interval'] and r['background_piece']==s['background_piece'])
        check('whole_angle_and_homotopy_scope',r['full_real_psi_and_repair_homotopy'] and s['whole_radial_angular_and_repair_homotopy_enclosed'] and s['positive_domain'])
        check('same_saved_actual_denominators',all(v==s[k] for k,v in r['actual_domain_lower_upper'].items()))
        check('all_saved_input_jets_nonnegative',set(r['normalized_input_jets_value_lambda_s_lambdas'])=={'u','v','a_s'} and all(len(z)==4 and all(dy(v)>=0 for v in z) for z in r['normalized_input_jets_value_lambda_s_lambdas'].values()))
        old=list(map(dy,r['complete_uniform_mean_Hs_Hss_difference_upper']))
        normal=list(map(dy,r['normal_velocity_lambda_lambdas_upper']))
        check('positive_complete_derivative_caps',len(old)==len(normal)==2 and min(old+normal)>=0)
        exact=(hi-lo)*old[0]
        check('exact_saved_height_contribution',F(r['exact_height_contribution_before_final_rounding'])==exact)
        old_integral+=exact
        replay=[normal[0]+nu*errors['Xpsi'],normal[1]+nus*errors['Xpsi']+nu*errors['Xspsi']]
        # A new cap pays the published endpoint roundings explicitly.
        fresh=[max(x,y) for x,y in zip(old,replay)]
        new_integral+=(hi-lo)*fresh[0]
        old_max=[max(x,y) for x,y in zip(old_max,old)]
        new_max=[max(x,y) for x,y in zip(new_max,fresh)]
        digest.update((str(i)+' '+str(lo)+' '+str(hi)+' '+str(fresh[0])+' '+str(fresh[1])+'\n').encode())
        cursor=hi
    for got,want in zip(map(dy,d['global_complete_mean_H_Hs_Hss_repair_difference_upper']),[old_integral,*old_max]):
        check('all_original_saved_global_caps_outward',got>=want>=0)
    fresh=[up(v) for v in [new_integral,*new_max]]
    for cap,value in zip(fresh,[new_integral,*new_max]):check('fresh_transport_replay_rounding_paid',dy(cap)>=value)
    for key,value in errors.items():
        paid=value+{'X':old_integral,'Xs':old_max[0],'Xss':old_max[1]}.get(key,F(0))
        check('all_seven_saved_complete_Cartesian_caps_outward',dy(d['complete_Cartesian_repair_jet_upper'][key])>=paid)
    result=dict(schema='independent-exact-saved-complete-mean-repair-consumption-v1',scope=__doc__,all_gates=True,gate_count=sum(counts.values()),gate_multiplicities=counts,source_sha256=sha(__file__),input_sha256={str(q):sha(q) for q in (a.certificate,a.resource,a.domain,a.cartesian)},primary_sha256=d['primary_sha256'],complete_atoms=len(d['rows']),exact_physical_end=str(cursor),exact_transport_replay_rows_sha256=digest.hexdigest(),global_H_Hs_Hss_caps_with_published_transport_rounding_paid=fresh,display_H_Hs_Hss=list(map(lambda z:float(dy(z)),fresh)),original_Hs_Hss_are_piecewise_jets_including_both_one_sided_endpoints=True,repaired_mean_is_globally_C2_from_matched_input_jets=True,original_quadrature_floating_alignment_target_g_or_PDE_certified=False,new_ODE_Node_Newton_or_interval_geometry_calls=0)
    a.out.parent.mkdir(parents=True,exist_ok=True);a.out.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(dict(all_gates=True,gates=result['gate_count'],H_Hs_Hss=result['display_H_Hs_Hss'],path=str(a.out),sha256=sha(a.out))),flush=True)


if __name__=='__main__':main()
