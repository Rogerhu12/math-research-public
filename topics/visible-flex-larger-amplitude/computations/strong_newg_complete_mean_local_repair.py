#!/usr/bin/env python3
"""Use the tightened actual domain and the actual per-piece repair costs.

Author: geometry_audit (GPT-6 Astra Pro; AI-assisted), 2026-11-13.
Every mean formula and full state derivative is the already executed complete
consumer. Only the newly proved D boxes and existing per-background-piece
C0/C1/C2 repair caps replace their coarser global counterparts. Full global
Cartesian fees remain unchanged. This does not change either comparison.
"""
import ast
import hashlib
from pathlib import Path

HERE=Path(__file__).resolve().parent
ORIGINAL=HERE/'strong_newg_complete_mean_repair_transfer.py'
ORIGINAL_SHA='bca68d259c3c8ac2d505dbe8b1cdfe8c1daaeaf03368db325755adec60b6a6aa'


def unique(s,a,b):
    if s.count(a)!=1:raise ValueError('Frozen full-mean edit site changed: '+a[:100])
    result=s.replace(a,b,1)
    if result.count(b)!=1 or result.replace(b,a,1)!=s:raise ValueError('Exact full-mean reversal failed')
    return result


def main():
    original=ORIGINAL.read_text()
    if hashlib.sha256(original.encode()).hexdigest()!=ORIGINAL_SHA:
        raise ValueError('Frozen complete mean producer changed')
    edits=[
        ("'domain': 'a7342234eb1ce94569f7de40f1fa084701da35b87dbf4bdcec82be1e84cde39d'",
         "'domain': 'd9c057155600660827770378e9a55054bfad06003fb74405d5cb2a285cb1040f'"),
        ("'domain_check': 'e1b31766b465956cc9f337cf9921d2cde4b1641c8362ad6f622e8443837456ac'",
         "'domain_check': 'abbe6b3c292af7a46df07438f10a104042540eba47c0b61b10948e717220714b'"),
        ("    identities = {}\n", "    identities = {str(FROZEN_MEAN_PARENT):sha(FROZEN_MEAN_PARENT)}\n"),
        ("    errors = {r['jet']: dy(r['combined_paid_repair_uniform_Euclidean_upper']) for r in C['jet_rows']}\n",
         "    errors = {r['jet']: dy(r['combined_paid_repair_uniform_Euclidean_upper']) for r in C['jet_rows']}\n"
         "    state_errors = {r['jet']: dy(r['state_repair_uniform_Euclidean_upper']) for r in C['jet_rows']}\n"),
        ("        piece = B['piece_rows'][row['background_piece']]\n",
         "        piece = B['piece_rows'][row['background_piece']]\n"
         "        be0,be1,be2 = map(dy,piece['quintic_repair_uniform_C0_C1_C2_upper'])\n"
         "        local_errors = dict(Xpsi=be0*base['Bpsi']+state_errors['Xpsi'],\n"
         "            Xpsipsi=be0*base['Bpsipsi']+state_errors['Xpsipsi'],\n"
         "            Xspsi=be1*base['Bpsi']+be0*base['Bspsi']+state_errors['Xspsi'],\n"
         "            Xspsipsi=be1*base['Bpsipsi']+be0*base['Bspsipsi']+state_errors['Xspsipsi'])\n"
         "        check('all_actual_local_repair_fees_paid_and_below_global_caps',all(local_errors[k]<=errors[k] for k in local_errors) and be0<=e0 and be1<=e1 and be2<=e2)\n"),
        ("        Ul = (aq(errors['Xpsi']) + aq(e0)*U) / a\n"
         "        Vl = (aq(errors['Xpsipsi']) + aq(e0)*V) / a\n"
         "        Uls = (aq(errors['Xspsi']) + aq(e1)*U + t*Ul + aq(e0)*Us) / a\n"
         "        Vls = (aq(errors['Xspsipsi']) + aq(e1)*V + t*Vl + aq(e0)*Vs) / a\n"
         "        uj = [U, Ul, Us, Uls]\n"
         "        vj = [V, Vl, Vs, Vls]\n"
         "        tj = [t, aq(e1), ts, aq(e2)]\n",
         "        Ul = (aq(local_errors['Xpsi']) + aq(be0)*U) / a\n"
         "        Vl = (aq(local_errors['Xpsipsi']) + aq(be0)*V) / a\n"
         "        Uls = (aq(local_errors['Xspsi']) + aq(be1)*U + t*Ul + aq(be0)*Us) / a\n"
         "        Vls = (aq(local_errors['Xspsipsi']) + aq(be1)*V + t*Vl + aq(be0)*Vs) / a\n"
         "        uj = [U, Ul, Us, Uls]\n"
         "        vj = [V, Vl, Vs, Vls]\n"
         "        tj = [t, aq(be1), ts, aq(be2)]\n"),
        ("        full_lambda = Fj[1] + aq(nu*errors['Xpsi'])\n"
         "        full_lambda_s = Fj[3] + aq(nu_s*errors['Xpsi'] + nu*errors['Xspsi'])\n",
         "        full_lambda = Fj[1] + aq(nu*local_errors['Xpsi'])\n"
         "        full_lambda_s = Fj[3] + aq(nu_s*local_errors['Xpsi'] + nu*local_errors['Xspsi'])\n"),
        ("            s_interval=row['s_interval'], full_real_psi_and_repair_homotopy=True,\n",
         "            s_interval=row['s_interval'], full_real_psi_and_repair_homotopy=True,\n"
         "            actual_local_background_repair_C0_C1_C2_upper=piece['quintic_repair_uniform_C0_C1_C2_upper'],\n"
         "            actual_local_nonmean_derivative_repair_upper={k:upper(aq(v)) for k,v in local_errors.items()},\n"),
        ("len(results) == domain['continuous_product_atoms'] == 3152", "len(results) == domain['continuous_product_atoms'] == 3326"),
        ("schema='actual-q106-complete-uniform-mean-C2-repair-transfer-v1',scope=__doc__,",
         "schema='actual-q106-complete-uniform-mean-local-C2-repair-transfer-v1',scope=__doc__,actual_per_background_piece_repair_fees_paid=True,tightened_actual_denominator_domain_used=True,global_Cartesian_repair_fees_retained=True,"),
    ]
    source=original
    for before,after in edits:source=unique(source,before,after)
    ast.parse(source)
    reverse=source
    for before,after in reversed(edits):reverse=unique(reverse,after,before)
    if reverse!=original:raise ValueError('Unlisted complete mean formula change')
    namespace=dict(__file__=str(Path(__file__).resolve()),__name__='actual_complete_mean_with_local_repair_fees',FROZEN_MEAN_PARENT=ORIGINAL)
    exec(compile(source,'<complete-mean-actual-local-repair-fees>','exec'),namespace)
    namespace['main']()


if __name__=='__main__':main()
