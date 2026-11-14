#!/usr/bin/env python3
"""Exact consumer: actual signed residual plus full R100 head gives a tiny low46 ball."""
import argparse
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path

PINS={
 'ordered':('notes/2026-11-13-root-signed46-ordered-v2-summary.json','e30a95b57dc4ba7b64af5f6e95ea30b233611c3703b5f5111793482b368a8ca3'),
 'fields':('notes/2026-11-12-root-linear-centre-local-restored-r1-summary.json','94fb941354dbb4769cb7ce80d5f7fd14eed6bdbce893842881c5c949c460288a'),
 'head':('notes/2026-11-13-root-r100-source-reweight-r1.json','617987048c3a599acb42bcafe8dba99155c5cde82d252706769d5e24340ce1b9'),
 'budget':('notes/2026-11-12-closure-physical-green-budget-actions-43303787139-1-interval.json','86c9b5604a765a50028865a4f3edae3171d9582052e2b7e7515d0471d8685d45'),
 'geometry':('notes/2026-11-12-closure-physical-green-actions-43303787139-1-interval.json','e3bb0bad3afac3e19d6b811ad068d0b4251b2a1214718dcbd14a2eb98e1aaa03'),
 'r94':('notes/2026-11-12-root-r94-full46-cut-exact-ledger.json','5eb45673a9080ae251e77c3203cfc2142ba31850fc244c7e2c8500df774249bc')}

def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()

def number(x):
    if isinstance(x,bool) or isinstance(x,float):raise TypeError('No display numeric input')
    if isinstance(x,(str,int)):return F(x)
    if isinstance(x,list):return F(x[0])*F(2)**x[1]
    if 'upper' in x:return number(x['upper'])
    if 'numerator' in x:return F(int(x['numerator']),int(x['denominator']))
    return F(int(x['mantissa']))*F(2)**int(x['binary_exponent'])

def record(x):
    return {'numerator':str(x.numerator),'denominator':str(x.denominator),'display_only':float(x)}

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--topic',type=Path,required=True)
    ap.add_argument('--out',type=Path,required=True)
    a=ap.parse_args()
    if a.out.exists():raise FileExistsError('Fresh output required')
    gates={};docs={};inputs={}
    def gate(k,b):
        gates[k]=bool(b)
        if not b:raise ArithmeticError(k)
    for k,(rel,wanted) in PINS.items():
        p=a.topic/rel;gate('identity_'+k,sha(p)==wanted)
        docs[k]=json.loads(p.read_text());inputs[k]={'path':rel,'sha256':wanted}
        gate('all_gates_'+k,docs[k]['all_gates'] and all(docs[k]['gates'].values()))
    op,fields,head,budget,geometry,r94=[docs[k] for k in ('ordered','fields','head','budget','geometry','r94')]
    resource=a.topic/'notes/2026-11-13-root-signed46-ordered-v2-resource.json'
    rd=json.loads(resource.read_text());inputs['resource']={'path':str(resource.relative_to(a.topic)),'sha256':sha(resource)}
    gate('ordered_actual_exit_zero',rd['exitcode']==0 and rd['termination_signal'] is None)
    gate('complete_18_groups_10793_materials_10878_subpanels',len(op['groups'])==18 and op['original_source_panels']==10793 and op['whole_geometry_subpanels']==10878 and sum(g['subpanels'] for g in op['groups'])==10878)
    modes=list(range(2,93,2));gate('all46_modes',op['modes']==modes and [r['mode'] for r in op['cut_rows']]==modes and [r['mode'] for r in budget['mode_rows']]==modes)
    gate('same_fixed_centre',PINS['fields'][1] in op['input_hashes'].values())
    gate('same_true_Green_operator',budget['geometry_sha256']==PINS['geometry'][1] and geometry['config']['source_tau']=='1/64')
    gate('complete_head_on_R100_domain',head['parameter_norm']=='max(linf_S,weighted_l1_T)' and head['complete_mean_inverse_and_far_retained'])
    centre=number(fields['original_rest_excluding2and4_strong_mass_upper'])+sum(number(x) for row in fields['true_linear_selected_component_mass'].values() for x in row.values())
    residual=max(number(op['joint_strong_PK_residual_upper']),sum(number(op['mode_residual_norms'][str(m)][z]) for m in modes for z in ('P','K')))
    headmass=number(head['whole_low46']['Wsigma1']['complete']['chosen_complete_true_DN_minus_exact_linear']['uniform_value_upper'])
    headop=max(number(r['complete_weighted_inner_K_trace_to_field_norm']) for r in budget['mode_rows'])
    betafield=headop*headmass
    density=next(r for r in budget['densities'] if r['density']=='weak_local_rho_16')
    gamma=2*number(density['all46_sum_of_separate_component_suprema'])
    gate('same_paid_whole_ball_contraction',gamma==number(r94['same_low_contraction']) and gamma<F(1,400))
    rho=F(1,10**9)
    gate('centre_plus_radius_inside_absolute_nine',centre+rho<9)
    gate('old_density_covers_absolute_nine',4*9<=4*(F(17,16)+16))
    olddomain=number(geometry['maximum_mean_input_radius'])
    gate('complete_mean_inverse_physical_domain',olddomain<F(1,64))
    image=residual+betafield+gamma*rho
    gate('strict_full_mean_inverse_and_head_selfmap',image<rho)
    effective=(residual+betafield)/(1-gamma)
    gate('a_posteriori_radius_below_1e_minus9',effective<rho)
    weakC=max(number(op['weak_C_residual_upper']),sum(number(op['mode_residual_norms'][str(m)]['C']) for m in modes))
    weakU=max(number(op['weak_U_residual_upper']),sum(number(op['mode_residual_norms'][str(m)]['U']) for m in modes))
    gate('simple_signed_residual_bounds',residual<F(9258,10**13) and weakC<F(5960,10**13) and weakU<F(1988,10**13))
    result={'schema':'signed46-r105-true-projected-ball-v1','scope':'True low46 projected solution on the complete R100 parameter domain, within 1e-9 of the fixed R88 mixed centre; no cut consistency or low/high coupling claimed',
      'all_gates':all(gates.values()),'gates':gates,'inputs':inputs,'source_sha256':sha(Path(__file__)),
      'centre_norm_upper':record(centre),'signed_complete_affine_residual':record(residual),
      'weak_C_signed_affine_residual':record(weakC),'weak_U_signed_affine_residual':record(weakU),
      'complete_head_mass':record(headmass),'head_trace_to_field_operator':record(headop),'complete_head_field':record(betafield),
      'full_ball_contraction':record(gamma),'chosen_radius':record(rho),'complete_image':record(image),
      'strict_selfmap_slack':record(rho-image),'a_posteriori_radius':record(effective),
      'complete_mean_input_radius_old':record(olddomain),'head_far_paid_once_in_complete_mass':True,
      'independent_of_rejected_DN4_r1':True,'full46_cut_consistency_paid':False,'full_frequency_PDE_paid':False}
    a.out.parent.mkdir(parents=True,exist_ok=True);a.out.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({'all_gates':result['all_gates'],'gates':len(gates),'centre':float(centre),'residual':float(residual),'beta':float(betafield),'gamma':float(gamma),'effective_radius':float(effective),'sha256':sha(a.out)}))

if __name__=='__main__':main()
