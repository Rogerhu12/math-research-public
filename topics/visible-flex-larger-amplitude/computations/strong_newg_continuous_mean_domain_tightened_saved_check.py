#!/usr/bin/env python3
"""Consume the actual small-denominator refinement of the positive q106 cover.

Author: geometry_audit (GPT-6 Astra Pro; AI-assisted), 2026-11-13.
The frozen exact saved-cover consumer is retained, with explicit adaptation
from a partly unpaid prior to the already positive 3152-box prior. New leaves
must belong only to boxes below D=1/1024; retained prior data are unchanged.
"""
import ast
import hashlib
from pathlib import Path

HERE=Path(__file__).resolve().parent
ORIGINAL=HERE/'strong_newg_continuous_mean_domain_saved_check.py'
ORIGINAL_SHA='811a2654c14f799d6c424b004826991b29acf1b204370555fff3367f67444b37'


def unique(s,a,b):
    if s.count(a)!=1:raise ValueError('Frozen saved-check site changed: '+a[:90])
    result=s.replace(a,b,1)
    if result.count(b)!=1 or result.replace(b,a,1)!=s:raise ValueError('Saved-check edit reversal failed')
    return result


def main():
    original=ORIGINAL.read_text()
    if hashlib.sha256(original.encode()).hexdigest()!=ORIGINAL_SHA:raise ValueError('Original saved-cover checker changed')
    edits=[
        ("check('prior_negative_conclusion_retained',prior['complete_original_interval_cover'] and not prior['all_domain_gates'] and prior['failed_atoms']==135)",
         "check('complete_positive_prior_retained',prior['complete_original_interval_cover'] and prior['all_domain_gates'] and prior['failed_atoms']==0 and len(prior['rows'])==3152 and sha(a.prior)=='a7342234eb1ce94569f7de40f1fa084701da35b87dbf4bdcec82be1e84cde39d')"),
        ("sha(Path('computations/strong_newg_continuous_mean_domain_refine_v2.py'))==d[name]",
         "sha(Path('computations/strong_newg_continuous_mean_domain_tighten.py'))==d[name]"),
        ("sha(Path('computations/strong_newg_continuous_mean_domain.py'))==prior[name]",
         "sha(Path('computations/strong_newg_continuous_mean_domain_refine_v2.py'))==prior[name]"),
        ("        if not r['positive_domain']:failed_by_index.setdefault((r['original_interval'],r['background_piece']),[]).append(r)\n",
         "        if saved(r['normalized_D_lower'])<F(1,1024):failed_by_index.setdefault((r['original_interval'],r['background_piece']),[]).append(r)\n"),
        ("            check('positive_prior_box_reused_exactly',key in old and old[key]['positive_domain'] and other==old[key]);seen_old.add(key);reused+=1\n",
         "            original_row=dict(old.get(key,{}));original_row.pop('retained_original_positive_box_verbatim',None)\n"
         "            check('positive_prior_box_reused_exactly',key in old and old[key]['positive_domain'] and saved(old[key]['normalized_D_lower'])>=F(1,1024) and other==original_row);seen_old.add(key);reused+=1\n"),
        ("check('refined_only_a_genuinely_unpaid_original_box',len(matches)==1)",
         "check('refined_only_a_genuinely_small_denominator_prior_box',len(matches)==1)"),
        ("    output=dict(schema='independent-saved-continuous-mean-domain-consumption-v1',scope=__doc__,\n",
         "    quality_failures=sum(saved(r['normalized_D_lower'])<F(1,1024) for r in d['rows'])\n"
         "    check('explicit_quality_target_not_assumed',d['denominator_tightening']['quality_target_failures']==quality_failures and d['denominator_tightening']['target_is_not_a_mathematical_assumption'])\n"
         "    output=dict(schema='independent-saved-continuous-mean-domain-consumption-v1',scope=__doc__,denominator_quality_target=['1',-10],quality_target_failures=quality_failures,\n"),
    ]
    source=original
    for a,b in edits:source=unique(source,a,b)
    ast.parse(source)
    reverse=source
    for a,b in reversed(edits):reverse=unique(reverse,b,a)
    if reverse!=original:raise ValueError('Unlisted saved-check change')
    namespace=dict(__file__=str(Path(__file__).resolve()),__name__='actual_tightened_q106_saved_cover_check')
    exec(compile(source,'<complete-saved-domain-check-with-positive-prior>','exec'),namespace)
    namespace['main']()


if __name__=='__main__':main()
