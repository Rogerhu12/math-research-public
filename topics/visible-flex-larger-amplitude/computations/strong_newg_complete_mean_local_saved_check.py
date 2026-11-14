#!/usr/bin/env python3
"""Check local background fees as well as the complete saved mean caps.

Author: geometry_audit (GPT-6 Astra Pro; AI-assisted), 2026-11-13.
The existing exact saved-mean consumer is retained. Each new local fee is
additionally reconstructed from the actual background piece and the same
complete state and chart bounds. Its independent transport replay continues
to pay the original global transport caps, hence also covers published
endpoint rounding without reusing an unproved cancellation.
"""
import ast
import hashlib
from pathlib import Path

HERE=Path(__file__).resolve().parent
ORIGINAL=HERE/'strong_newg_complete_mean_repair_saved_check.py'
ORIGINAL_SHA='21960d46bd316121760e6a68a3ef1ca9db46cfc4b8e322ad26ceebd5c6a3ef05'


def unique(s,a,b):
    if s.count(a)!=1:raise ValueError('Frozen saved-mean edit site changed: '+a[:100])
    out=s.replace(a,b,1)
    if out.count(b)!=1 or out.replace(b,a,1)!=s:raise ValueError('Saved-mean exact edit reversal failed')
    return out


def main():
    original=ORIGINAL.read_text()
    if hashlib.sha256(original.encode()).hexdigest()!=ORIGINAL_SHA:raise ValueError('Frozen exact saved-mean consumer changed')
    edits=[
        ("for k in ('certificate','resource','domain','cartesian','out'):","for k in ('certificate','resource','domain','cartesian','background','out'):"),
        ("    errors={r['jet']:dy(r['combined_paid_repair_uniform_Euclidean_upper']) for r in C['jet_rows']}\n",
         "    errors={r['jet']:dy(r['combined_paid_repair_uniform_Euclidean_upper']) for r in C['jet_rows']}\n"
         "    bg=read(a.background);B=next(q for q in bg['profiles'] if q['accepted_primary_sha256']==d['primary_sha256'])\n"
         "    check('same_actual_local_background_comparison',bg['all_gates'] and B['comparison_definition_sha256']==d['background_comparison_definition_sha256'] and d['input_sha256'][str(a.background)]==sha(a.background))\n"
         "    basis={k:F(int(q['numerator']),int(q['denominator'])) for k,q in C['global_dimensionless_base_jet_upper'].items()}\n"
         "    state_errors={r['jet']:dy(r['state_repair_uniform_Euclidean_upper']) for r in C['jet_rows']}\n"),
        ("        old=list(map(dy,r['complete_uniform_mean_Hs_Hss_difference_upper']))\n",
         "        piece=B['piece_rows'][r['background_piece']]\n"
         "        check('same_actual_per_piece_background_repair',r['actual_local_background_repair_C0_C1_C2_upper']==piece['quintic_repair_uniform_C0_C1_C2_upper'])\n"
         "        e0,e1,e2=map(dy,piece['quintic_repair_uniform_C0_C1_C2_upper'])\n"
         "        local=dict(Xpsi=e0*basis['Bpsi']+state_errors['Xpsi'],Xpsipsi=e0*basis['Bpsipsi']+state_errors['Xpsipsi'],Xspsi=e1*basis['Bpsi']+e0*basis['Bspsi']+state_errors['Xspsi'],Xspsipsi=e1*basis['Bpsipsi']+e0*basis['Bspsipsi']+state_errors['Xspsipsi'])\n"
         "        for key,value in local.items():check('every_actual_local_Cartesian_derivative_fee_outward',dy(r['actual_local_nonmean_derivative_repair_upper'][key])>=value and value<=errors[key])\n"
         "        old=list(map(dy,r['complete_uniform_mean_Hs_Hss_difference_upper']))\n"),
        ("for q in (a.certificate,a.resource,a.domain,a.cartesian)","for q in (a.certificate,a.resource,a.domain,a.cartesian,a.background)"),
    ]
    source=original
    for before,after in edits:source=unique(source,before,after)
    ast.parse(source)
    reverse=source
    for before,after in reversed(edits):reverse=unique(reverse,after,before)
    if reverse!=original:raise ValueError('Unlisted saved-mean consumer change')
    namespace=dict(__file__=str(Path(__file__).resolve()),__name__='actual_saved_complete_mean_local_fee_check')
    exec(compile(source,'<exact-saved-mean-consumer-with-actual-local-fees>','exec'),namespace)
    namespace['main']()


if __name__=='__main__':main()
