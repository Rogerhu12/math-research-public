#!/usr/bin/env python3
"""Stable complete true-beta interface after the R121 auxiliary source update.

The auxiliary C_S is only a restriction of the original R74 family.
All R100 transverse d effects are separately retained in its unchanged
four complete difference blocks.  Values are uniform for ||xi||inf<=1
and ||d||v<=rT.  True far is positive and counted once per whole output.
This does not alter the physical source, R100 domain, mean gauge or PDE.
"""
from __future__ import annotations
import argparse
from fractions import Fraction as F
import gzip
import hashlib
import json
from pathlib import Path
import resource
import sys
import time
import root_hybrid46_cut_consumer as original

sys.set_int_max_str_digits(0)
PINS={
 'consumed':('2026-11-13-inner-aux-bootstrap-cut-r1.json.gz','33cdff5738747578aedb22412cf4fd8bd78e087d9df2fde474fbbec59ffdc475'),
 'head':('2026-11-13-root-r100-source-reweight-r1.json','617987048c3a599acb42bcafe8dba99155c5cde82d252706769d5e24340ce1b9'),
 'r100':('2026-11-13-root-r100-hybrid46-exact-ledger.json','7e6b3c140c57df34ab10f17facbc624104b39fa9870a4eecfcce06bf3ea62ca9'),
 'old_cut':('2026-11-13-root-hybrid46-cut-r1.json','cf33eba4dcd1ad4e8fea3e667664b9c356db790851ca8e49d9889a62e408d638'),
}
MODES=list(range(2,93,2))
ex,up,record,sum_up=original.exact,original.up,original.record,original.sum_up

def digest(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--notes',type=Path,default=Path('notes'))
    ap.add_argument('--out',type=Path,required=True)
    args=ap.parse_args();began=time.monotonic()
    if args.out.exists():raise FileExistsError('A fresh complete interface output is required')
    data={};ids={};gates={}
    def check(name,value):
        gates[name]=bool(value)
        if not value:raise ArithmeticError('Unpaid true-beta interface gate: '+name)
    for name,(filename,wanted) in PINS.items():
        path=args.notes/filename;raw=path.read_bytes();got=hashlib.sha256(raw).hexdigest()
        if got!=wanted:raise ValueError('Pinned input changed: '+str(path))
        ids[str(path)]=dict(sha256=got,bytes=len(raw))
        data[name]=json.loads(gzip.decompress(raw) if path.suffix=='.gz' else raw,parse_float=str)
    consumed,head,r100,old_cut=[data[k] for k in ('consumed','head','r100','old_cut')]
    check('original_exact_helper_identity',digest(original.__file__)==old_cut['source_sha256'])
    for name in ('consumed','head','r100'):
        check('all_original_prerequisite_gates_'+name,data[name]['all_gates'] is True and all(data[name]['gates'].values()))
    for name in ('head','r100','old_cut'):
        check('same_consumed_'+name,consumed['input_identities']['notes/'+PINS[name][0]]['sha256']==PINS[name][1])
    check('all46_same_modes',consumed['all46_modes']==MODES
          and [r['mode'] for r in head['mode_rows']]==MODES
          and [r['mode'] for r in consumed['auxiliary_mode_rows']]==MODES)
    ci=ex(consumed['true_cut_K_conversion']);far=ex(consumed['complete_true_far_mass'])
    rem=ex(consumed['complete_canonical_mean_inverse_remainder'])
    check('same_positive_complete_far_and_conversion',far>0 and ci==ex(head['point_cut_inner_mu12_K_conversion'])
          and far==ex(head['true_far_added_once_per_whole_mass']))
    check('complete_mean_inverse_remainder_still_positive',rem>0)
    sigma=F(1,64);tau=ex(head['head_strip'])
    check('same_actual_cut_and_reference_strips',sigma<tau<2)
    kt,eta,tmax=[ex(r100['constants'][k]) for k in ('KT','eta','tmax')]
    check('same_complete_R100_constants',kt==F(273259958272,395007) and eta==4096)
    aux=[ex(r['new_complete_auxiliary_source_Wsigma1']) for r in consumed['auxiliary_mode_rows']]
    shared_base=[ex(r['shared_remainder_decomposition_base_Wsigma1']) for r in consumed['auxiliary_mode_rows']]
    shared_gain=[ex(r['common_remainder_to_Wsigma1_operator']) for r in consumed['auxiliary_mode_rows']]
    wide=[original.exp_bounds(m*(tau-sigma))[1] for m in MODES]
    cut_op=[ex(r['weighted_beta_cut_operator']) for r in old_cut['source_mode_rows']]
    field_op=[ex(r['weighted_beta_field_operator']) for r in old_cut['source_mode_rows']]
    def beta(radius):
        q=1+(kt+eta)*radius/256
        factors=dict(main=q,corr=q,quadratic=q*q,remainder=q*(1+q*tmax+(q*tmax)**2/3))
        nonfar=[];delta=[];bridge=[];piece_rows=[]
        for i,row in enumerate(head['mode_rows']):
            m=row['mode'];pieces={k:up(factors[k]*ex(v)) for k,v in row['old_complete_difference_Xi_pieces'].items()}
            check('all_four_complete_blocks_'+str(m),set(pieces)==set(factors))
            d=up(ci*(1+m)*original.exp_bounds(m*sigma)[1]*sum_up(pieces.values()))
            old=row['both_strips']['Wsigma1'];old_delta=ex(old['old_complete_difference'])
            dif=up(d+old_delta)
            nf=min(up(aux[i]+d),up(ex(old['old_chosen'])+dif+far))
            nonfar.append(nf);delta.append(d);bridge.append(dif)
            piece_rows.append({k:record(v) for k,v in pieces.items()})
        return nonfar,delta,bridge,piece_rows
    def whole(nonfar,delta,weights):
        separate=sum_up(up(weights[i]*nonfar[i]) for i in range(46))
        shared=up(sum_up(up(weights[i]*(shared_base[i]+delta[i])) for i in range(46))
                  +max(weights[i]*shared_gain[i] for i in range(46))*rem)
        return min(separate,shared)
    radii=sorted({ex(r['radius_T']) for r in consumed['scenarios']}|{F(1)})
    outputs=[]
    for rt in radii:
        nf,delta,bridge,pieces=beta(rt)
        matching=[r for r in consumed['scenarios'] if ex(r['radius_T'])==rt]
        if matching:
            check('all46_consumed_nonfar_values_reproduced_'+str(rt),
                  nf==[ex(r['complete_head_nonfar_Wsigma1']) for r in matching[0]['all46_complete_head_rows']])
        rows=[]
        for i,m in enumerate(MODES):
            full_sigma=up(nf[i]+far)
            full_tau=up(wide[i]*nf[i]+far)
            raw=up(full_sigma/((1+m)*original.exp_bounds(m*sigma)[0]))
            rows.append(dict(mode=m,group='S' if m<=12 else 'T',
                complete_nonfar_Wsigma1=record(nf[i]),complete_true_beta_Wsigma1=record(full_sigma),
                complete_true_beta_Wtau_b1=record(full_tau),
                complete_true_beta_cosine_K_coefficient=record(raw),
                complete_difference_Wsigma1=record(delta[i]),
                all_four_R100_difference_Xi_pieces=pieces[i]))
        sigma_nonfar=whole(nf,delta,[F(1)]*46)
        tau_nonfar=whole(nf,delta,wide)
        full_sigma,full_tau=up(sigma_nonfar+far),up(tau_nonfar+far)
        t_modal=sum_up(up(cut_op[i]*nf[i]) for i in range(6,46))
        t_shared=up(sum_up(up(cut_op[i]*(shared_base[i]+delta[i])) for i in range(6,46))+
                    max(cut_op[i]*shared_gain[i] for i in range(6,46))*rem)
        t_nf=min(t_modal,t_shared);t_far=up(max(cut_op[6:])*far)
        field_nf=whole(nf,delta,field_op)
        field_total=up(field_nf+max(field_op)*far)
        if matching:
            check('consumed_T_common_mass_reproduced_'+str(rt),
                  t_nf==ex(matching[0]['new_T_nonfar_head_l1']))
        derivatives=dict(S_at_xi_radius_3over4=dict(
            first_Wsigma1=record(4*full_sigma),second_Wsigma1=record(64*full_sigma),
            first_Wtau_b1=record(4*full_tau),second_Wtau_b1=record(64*full_tau)))
        if 2*rt<=1:
            _,_,outer_bridge,_=beta(2*rt)
            bs=up(sum_up(outer_bridge)+2*far)
            bt=up(sum_up(up(wide[i]*outer_bridge[i]) for i in range(46))+2*far)
            derivatives['T_at_d_radius_rT']=dict(outer_circle=record(2*rt),
                complete_bridge_Wsigma1=record(bs),complete_bridge_Wtau_b1=record(bt),
                first_Wsigma1=record(bs/rt),first_Wtau_b1=record(bt/rt),
                auxiliary_source_cancels_before_absolute_value=True)
        outputs.append(dict(radius_T=record(rt),
            value_domain='All six xi coordinates have complex linf radius1; the forty transverse coordinates share weighted-l1 radius rT',
            all46_mode_rows=rows,
            whole46_nonfar_Wsigma1=record(sigma_nonfar),whole46_true_beta_Wsigma1=record(full_sigma),
            whole46_nonfar_Wtau_b1=record(tau_nonfar),whole46_true_beta_Wtau_b1=record(full_tau),
            true_far_added_once=record(far),
            T_head_nonfar_in_original_cut_norm=record(t_nf),
            T_head_far_in_original_cut_norm=record(t_far),
            T_head_complete_in_original_cut_norm=record(up(t_nf+t_far)),
            whole46_complete_beta_to_original_field_norm=record(field_total),
            derivative_interfaces=derivatives))
    check('all_original_radii_and_full_R100_unit_domain',len(outputs)==11 and radii[-1]==1)
    check('required_three_working_radii_present',all(r in radii for r in (F(1,64),F(1,16),F(1,4))))
    result=dict(schema='visible-flex-larger-R123-true-beta-interface-v1',
        status='Completed exact complete true-beta interfaces on the unchanged R100 domain',
        author='geometry_audit (GPT-6 Astra Pro; AI-assisted)',source_sha256=digest(__file__),
        exact_helper_sha256=digest(original.__file__),input_identities=ids,
        all_gates=all(gates.values()),gates=gates,all46_modes=MODES,
        sigma=record(sigma),true_tau_b=record(tau),
        parameter_domain='R100: max(linf of six R74 coordinates, weighted-l1 of forty original R59 coordinates)<=1',
        auxiliary_domain='R121 is used only for C_S, the restriction of R74 with fourteen old parameter increments zero; the twenty old centre coefficients remain present',
        transverse_source_payment='Every transverse d effect remains in the original four R100 complete difference blocks with q(rT); no transverse lift is inserted in the R121 spectral cap',
        beta_definition='True inner low DN minus exact same-height linear inner DN, in relative physical Kbar cosine coefficients; includes complete mean/inverse feedback and the true far lift',
        common_mass_rule='Per-mode complete bounds and common norms are separate enclosures; whole norms charge the positive true-far mass once and may use a maximum operator for the shared complete source remainder',
        rows=outputs,full_cut_or_new_outer_solution_claimed=False,
        complete_high_and_mean_gauge='Original R100 high blocks, complete mean and common cuff-height gauge remain separately certified and unchanged',
        no_new_ODE=True,no_Arb=True,no_Node=True,no_new_source_integral=True,
        elapsed_seconds=time.monotonic()-began,peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    raw=(json.dumps(result,ensure_ascii=False,indent=2)+'\n').encode()
    payload=gzip.compress(raw,mtime=0) if args.out.suffix=='.gz' else raw
    if len(payload)>=5_000_000 or (len(raw)>1_000_000 and args.out.suffix!='.gz'):
        raise ValueError('Repository file limits exceeded')
    args.out.parent.mkdir(parents=True,exist_ok=True)
    with args.out.open('xb') as stream:stream.write(payload)
    print(json.dumps(dict(out=str(args.out),sha256=digest(args.out),bytes=len(payload),
        all_gates=result['all_gates'],gates=len(gates),seconds=result['elapsed_seconds'],
        selected=[dict(rT=str(ex(r['radius_T'])),T_head=r['T_head_complete_in_original_cut_norm']['display_upward'],
                       Wsigma=r['whole46_true_beta_Wsigma1']['display_upward'],Wtau=r['whole46_true_beta_Wtau_b1']['display_upward'])
                  for r in outputs if ex(r['radius_T']) in (F(1,64),F(1,16),F(1,4),F(1))])),flush=True)

if __name__=='__main__':main()
