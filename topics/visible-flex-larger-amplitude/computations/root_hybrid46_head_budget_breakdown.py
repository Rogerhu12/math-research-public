#!/usr/bin/env python3
"""Exact decomposition of the already executed R100 forty-mode head budget.

This locates the actual majorant bottleneck. It does not improve the bound,
discard a source term, or claim a failed majorant proves nonexistence.
"""
import argparse
from fractions import Fraction as Q
import hashlib
import json
from pathlib import Path
import time
import root_hybrid46_cut_consumer as original

SHA={'cut':'cf33eba4dcd1ad4e8fea3e667664b9c356db790851ca8e49d9889a62e408d638',
     'head':'617987048c3a599acb42bcafe8dba99155c5cde82d252706769d5e24340ce1b9',
     'r100':'7e6b3c140c57df34ab10f17facbc624104b39fa9870a4eecfcce06bf3ea62ca9'}
def main():
    ap=argparse.ArgumentParser(description=__doc__)
    for key in (*SHA,'out'): ap.add_argument('--'+key,type=Path,required=True)
    a=ap.parse_args();began=time.monotonic()
    if a.out.exists():raise FileExistsError('Fresh exact audit output required')
    data={};ids={}
    for name,sha in SHA.items():
        p=getattr(a,name); raw=p.read_bytes()
        if hashlib.sha256(raw).hexdigest()!=sha:raise ValueError('Original completed primary differs')
        data[name]=json.loads(raw);ids[name]={'path':str(p),'sha256':sha}
    cut,head,r100=[data[x] for x in ('cut','head','r100')]
    ex,up,rec=original.exact,original.up,original.record
    kt,eta=[ex(r100['constants'][x]) for x in ('KT','eta')]
    ci=ex(head['point_cut_inner_mu12_K_conversion']); tmax=ex(r100['constants']['tmax'])
    if kt!=Q(273259958272,395007) or eta!=4096:raise ValueError('Same parameter extension required')
    radii=[Q(1,64),Q(1,16),Q(1,4)]
    outputs=[]
    for rt in radii:
        q=1+(kt+eta)*rt/256
        factors={'main':q,'corr':q,'quadratic':q*q,'remainder':q*(1+q*tmax+(q*tmax)**2/3)}
        rows=[]
        for h,c in zip(head['mode_rows'],cut['source_mode_rows']):
            m=int(h['mode'])
            if int(c['mode'])!=m:raise ValueError('All46 rows retained in original order')
            angular=original.exp_bounds(Q(m,64))[1]
            pieces={k:up(factors[k]*ex(v)) for k,v in h['old_complete_difference_Xi_pieces'].items()}
            xi=original.sum_up(pieces.values())
            delta=up(ci*(1+m)*angular*xi)
            old=h['both_strips']['Wsigma1']; aux=ex(old['old_auxiliary'])
            old_delta,old_chosen=[ex(old[k]) for k in ('old_complete_difference','old_chosen')]
            far=ex(head['true_far_added_once_per_whole_mass'])
            first=up(aux+delta);second=up(old_chosen+up(delta+old_delta)+far)
            nf=min(first,second); op=ex(c['weighted_beta_cut_operator'])
            normalized=up(op*nf)
            # Account for both finite branch and rounding slack explicitly.
            selected='auxiliary_plus_difference' if first<=second else 'prior_complete_plus_difference'
            base=aux if selected=='auxiliary_plus_difference' else old_chosen+old_delta+far
            contributions={k:up(op*ci*(1+m)*angular*v) for k,v in pieces.items()}
            base_contribution=up(op*base)
            rows.append({'mode':m,'group':c['group'],'selected_valid_branch':selected,
                'normalized_nonfar_bound':rec(normalized),'selected_base_contribution':rec(base_contribution),
                'rescaled_complete_difference_pieces':{k:rec(v) for k,v in contributions.items()},
                'sum_of_component_upper_bounds':rec(base_contribution+sum(contributions.values(),Q(0))),
                'no_actual_signed_inner_source_evaluation':True})
        trows=[r for r in rows if r['group']=='T']
        total=original.sum_up(ex(r['normalized_nonfar_bound']) for r in trows)
        prior=next(r for r in cut['scenarios'] if ex(r['radius_T'])==rt)
        if total!=ex(prior['T_nonfar_head_l1']):raise ArithmeticError('Original complete head budget not exactly reproduced')
        ranked=sorted(trows,key=lambda r:ex(r['normalized_nonfar_bound']),reverse=True)
        totals={'selected_base':sum(ex(r['selected_base_contribution']) for r in trows)}
        for k in factors:totals[k]=sum(ex(r['rescaled_complete_difference_pieces'][k]) for r in trows)
        outputs.append({'radius_T':str(rt),'exact_original_nonfar_T_l1_reproduced':True,
            'normalized_nonfar_T_l1':rec(total),'complete_all46_rows':rows,'ranked_T_modes':[r['mode'] for r in ranked],
            'T_component_totals':{k:rec(v) for k,v in totals.items()},
            'top_ten_display':[{'mode':r['mode'],'upper':r['normalized_nonfar_bound']['display_upward']} for r in ranked[:10]]})
    out={'scope':'Exact accounting of the existing sufficient bound only; no new selfmap or nonexistence claim',
         'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'input_identities':ids,
         'all_three_original_T_budgets_reproduced':True,'scenarios':outputs,'elapsed_seconds':time.monotonic()-began}
    a.out.write_text(json.dumps(out,indent=2)+'\n')
    for r in outputs:print(json.dumps({'radius_T':r['radius_T'],'total':r['normalized_nonfar_T_l1']['display_upward'],
        'top':r['top_ten_display'],'components':{k:v['display_upward'] for k,v in r['T_component_totals'].items()}}),flush=True)
if __name__=='__main__':main()
