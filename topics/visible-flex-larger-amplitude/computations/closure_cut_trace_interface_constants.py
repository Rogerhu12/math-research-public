#!/usr/bin/env python3
"""Exact rational cut-interface comparisons; no flow or fixed-point solve.

The strong envelope is explicitly compared in the OLD q003 continuous
strip.  Its originally saved, slightly different strip is never reused
as if identical.  Joint-head and outer-head existence gates stay unpaid.
Author: exact_closure (GPT-6 Astra Pro, AI-assisted), 2026-11-12.
"""
import argparse
from fractions import Fraction as F
import gzip
import hashlib
import json
from pathlib import Path
import resource
import time


def read(path):
    b=path.read_bytes()
    return json.loads(gzip.decompress(b) if path.suffix=='.gz' else b),hashlib.sha256(b).hexdigest()


def dyadic(p):
    m=int(p['mantissa']);e=int(p['binary_exponent'])
    return F(m*(1<<e),1) if e>=0 else F(m,1<<(-e))


def lower(x):return dyadic(x['lower'])
def upper(x):return dyadic(x['upper'])
def rec(x):return {'numerator':str(x.numerator),'denominator':str(x.denominator)}


def main():
    p=argparse.ArgumentParser(description=__doc__)
    for n in ('q-density','strong-density','strong-reference','out'):
        p.add_argument('--'+n,type=Path,required=True)
    a=p.parse_args();started=time.monotonic()
    if a.out.exists():raise FileExistsError('Use a fresh output')
    docs={};hashes={}
    for n in ('q_density','strong_density','strong_reference'):
        path=getattr(a,n);docs[n],hashes[str(path)]=read(path)
    q=docs['q_density'];s=docs['strong_density'];ref=docs['strong_reference']
    if not all(q['gates'].values()) or not all(s['gates'].values()) or not all(ref['checks'].values()):
        raise ValueError('Use the paid physical envelopes and actual same-source strong reference')
    if hashes[str(a.strong_reference)] not in s['input_hashes'].values():
        raise ValueError('The strong physical envelope belongs to another auxiliary reference')
    if [r['cell'] for r in q['rows']]!=list(range(12,225)) or [r['cell'] for r in s['rows']]!=list(range(12,225)):
        raise ValueError('All213 envelope coefficients are required')
    common_fields=('B','Q_coefficient','mu_lower','mu_upper','normalized_width_upper','TV_log_w_upper','w_lower')
    ratios=[]
    for qr,sr in zip(q['rows'],s['rows']):
        for name in common_fields:
            if (lower(qr[name]),upper(qr[name]))!=(lower(sr[name]),upper(sr[name])):
                raise ValueError('The actual common source/envelope shape differs: '+name)
        xq=upper(qr['canonical_total_envelope']);xs=upper(sr['canonical_total_envelope'])
        if not 0<xq or lower(qr['canonical_total_envelope'])!=xq or lower(sr['canonical_total_envelope'])!=xs:
            raise ValueError('Chosen envelope coefficients must be fixed positive dyadics')
        ratios.append(xs/xq)
    tau=lower(q['rows'][0]['tau_outer']);B=lower(q['rows'][0]['B']);Aq=upper(q['rows'][0]['V_over_w_upper'])
    sigma=max(ratios);sigma_min=min(ratios)
    # V_strong=sigma_n V_q in the explicitly selected q strip.
    As=ratios[0]*Aq
    tau_outer=F(1,64);gap=tau-tau_outer;R0=F(1,256)
    e_lower=sum((F(1,d) for d in (1,1,2,6,24)),F(0))
    T=R0+4*R0**2
    eta=2*T+2*T*T
    Llower=1-3*R0
    dA=F(1,4)*(R0*F(5,4)+2*F(3,4)+2*R0*F(1,4))
    dB=26*R0
    rr_lipschitz=12*((F(1,2)+F(1,8))/F(3,4)+(2+16*R0**2)*3/F(3,4)**2)
    checks={
        'all213_same_B_and_real_material_shapes':True,
        'all213_strong_scale_positive':sigma_min>0,
        'all213_strong_scale_below18':sigma<18,
        'common_q_cut_strip_minus_outer1over64_above1over8':gap>F(1,8),
        'cut_balance_B_at_least4':B>=4,
        'q_cut_envelope_below_2minus51':Aq<F(1,2**51),
        'strong_reweighted_cut_envelope_below_2minus46':As<F(1,2**46),
        'all_fields_of_physical_norm_at_most2_fit_R0':2*max(Aq,As)<R0,
        'cauchy_derivative_loss_below3':8/e_lower<3,
        'full_mean_corrected_T_below1over128':T<F(1,128),
        'forward_connection_eta_below1over32':eta<F(1,32),
        'normalized_Darboux_denominator_above_three_quarters':Llower>F(3,4),
        'numerator_A_derivative_below_half':dA<F(1,2),
        'numerator_B_derivative_below_one_eighth':dB<F(1,8),
        'full_radial_second_jet_lipschitz_below144':rr_lipschitz<144,
    }
    result=dict(status='Exact dyadic/rational cut-interface constants paid; joint and outer-head gates remain separate',
        checks=checks,scope='Only the fixed q continuous strip and its explicit same-source strong-envelope rescaling at physical node12.',
        chosen_outer_strip=rec(tau_outer),q_cut_strip_lower=rec(tau),strip_gap_lower=rec(gap),
        cut_B_lower=rec(B),q_cut_A_upper=rec(Aq),strong_reweighted_cut_A_upper=rec(As),
        sigma_min=rec(sigma_min),sigma_max=rec(sigma),
        R0=rec(R0),T_upper=rec(T),connection_eta_upper=rec(eta),
        normalized_radial_denominator_lower=rec(Llower),radial_second_jet_lipschitz_upper=rec(rr_lipschitz),
        background_assumption='R31 exact principal background curvatures <=8 and w<=1/2; therefore |w_r| and E*w/r are <12.',
        derivative_statement='For the same true metric and a complete physical cut difference d, |delta h_rr| <=144*(V(b)/w(b))*d under the declared domains; this is a polar-coordinate jet bound.',
        complete_mean=True,actual_joint_fixed_point_paid=False,outer_continuous_kernel_paid=False,
        operator_solves=0,radial_integrations=0,input_hashes=hashes,
        source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        elapsed_seconds=time.monotonic()-started,peak_RSS_KiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    a.out.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(dict(checks=checks,all_pass=all(checks.values()),
        seconds=result['elapsed_seconds'],RSS_KiB=result['peak_RSS_KiB']),indent=2))
    if not all(checks.values()):raise SystemExit(1)


if __name__=='__main__':main()
