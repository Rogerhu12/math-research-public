#!/usr/bin/env python3
"""Exact independent executed-summary gates for R101, no ODE or Arb.

Consumes the whole fresh R100 spectral and wide-tail primaries without
editing or splitting them. All mathematical comparisons use Fraction.
Author: exact_closure, GPT-6 Astra Pro (AI-assisted), 2026-11-13.
"""
from pathlib import Path
from fractions import Fraction as F
from decimal import Decimal, localcontext, ROUND_CEILING
import argparse, hashlib, json, resource, time

PIN = {
    'spectral':'1c12cde9889048daaced137a79a1504a4780d7f5315a5950c5fde4fda0d38651',
    'wide':'46543934513c1c0ba147c676a0a52daaaf683c4bdda364f1b33bb1bf469a88a2',
}
SOURCE = {
    'spectral':'eac90d6f7c816a67590c2c07d031e24d27af0adfd21e1b5ef5411891943b903e',
    'wide':'0eba517db1b0b3bae68c3a2b7e5891166bb81468eb03b50e2679cb1b3460f9f5',
}
HEAD='617987048c3a599acb42bcafe8dba99155c5cde82d252706769d5e24340ce1b9'
DOMAIN='Real restriction of R100 six original R74 axes times40 original R59 weighted-l1 axes; same fixed R74 outer targets'
def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def p2(n):
    return F(2)**n
def dyad(x):
    return F(int(x[0]))*p2(int(x[1]))
def record(x):
    x=F(x)
    with localcontext() as ctx:
        ctx.prec=28;ctx.rounding=ROUND_CEILING
        shown=str(Decimal(x.numerator)/Decimal(x.denominator))
    return dict(numerator=str(x.numerator),denominator=str(x.denominator),
                decimal_upward_display=shown)
def ceil_log2(x):
    x=F(x)
    if x<=0:raise ValueError('Strict positive bound required')
    k=x.numerator.bit_length()-x.denominator.bit_length()
    if x>p2(k):k+=1
    if not p2(k-1)<x<=p2(k):raise ArithmeticError('Exact log2 bracket')
    return k
def main():
    ap=argparse.ArgumentParser(description=__doc__)
    for k in ('spectral','wide','spectral-resource','wide-resource','out'):
        ap.add_argument('--'+k,type=Path,required=True)
    args=ap.parse_args();began=time.monotonic()
    if args.out.exists():raise FileExistsError('Keep all primary results immutable')
    docs={};ids={}
    for name,sha in PIN.items():
        path=getattr(args,name);got=digest(path)
        if got!=sha:raise ValueError('Whole actual primary changed')
        docs[name]=json.loads(path.read_text())
        ids[str(path)]=dict(sha256=got,bytes=path.stat().st_size)
    s,w=docs['spectral'],docs['wide']
    rs=json.loads(args.spectral_resource.read_text())
    rw=json.loads(args.wide_resource.read_text())
    for path in (args.spectral_resource,args.wide_resource):
        ids[str(path)]=dict(sha256=digest(path),bytes=path.stat().st_size)
    gates={}
    def ck(key,value):
        gates[key]=bool(value)
        if not value:raise ArithmeticError('Unpaid exact R101 gate: '+key)
    ck('actual_spectral_30_gates',s['all_gates'] is True and len(s['gates'])==30 and all(s['gates'].values()))
    ck('actual_wide_14_gates',w['all_gates'] is True and len(w['gates'])==14 and all(w['gates'].values()))
    ck('actual_owned_wait4_both0',all(r['exitcode']==0 and r['termination_signal'] is None for r in (rs,rw)))
    ck('two_frozen_mathematical_sources',s['source_sha256']==SOURCE['spectral'] and w['source_sha256']==SOURCE['wide'])
    ck('fresh_whole_R100_head_identity',s['complete_R100_primary_sha256']==HEAD and w['complete_R100_primary_sha256']==HEAD)
    ck('new_six_times40_domain_explicit',s['parameter_domain']==DOMAIN and w['parameter_domain']==DOMAIN and s['parameter_norm']=='max(linf_S,weighted_l1_T)')
    ck('wide_consumes_this_complete_spectral',w['exact_unpartitioned_v2_sha256']==PIN['spectral'])
    modes=list(range(2,93,2))
    ck('all46_ordered_field_caps',[r['mode'] for r in s['final_caps']]==modes)
    ck('all46_complete_low_sources',[r['mode'] for r in s['low_complete_sources']]==modes)
    ck('all230_complete_middle_rows',[r['mode'] for r in w['source_rows94_to552']]==list(range(94,553,2)))
    coverage=[]
    for b in w['complete_middle554_to5758_blocks']:
        ck('block_formula_'+str(b['first_mode']),b['formula']=='common_factor*(3/8)^mode' and dyad(b['common_factor'])>0)
        coverage.extend(range(b['first_mode'],b['last_mode']+1,2))
    ck('complete_middle554_to5758_cover',coverage==list(range(554,5759,2)))
    caps={r['mode']:dyad(r['bound']) for r in s['final_caps']}
    low={r['mode']:dyad(r['complete_source_upper']) for r in s['low_complete_sources']}
    mid={r['mode']:dyad(r['chosen_source_upper']) for r in w['source_rows94_to552']}
    total=sum(caps.values())
    ck('exact_cap_sum_below_saved_total',total<=dyad(s['final_total']))
    ck('initial_complete_norm_below9_689',dyad(s['initial_total'])<F(9689,1000))
    ck('final_complete_norm_below9_084',dyad(s['final_total'])<F(2271,250))
    ck('same_actual_wide_centre',dyad(w['same_actual_low_centre_norm'])==dyad(s['final_total']))
    ck('extra_strip_norm_below67_154',dyad(w['wide_centre_norm'])<F(33577,500))
    ck('complete_inverse_below_two_minus33',dyad(w['wide_inverse_norm'])<p2(-33))
    ck('full_pointwise_complex_mean_domain',dyad(w['full_point_radius_in_wider_strip'])<F(1,64))
    low_limits={2:F(879,10**6),4:F(12033,500),6:F(879,10**6),8:F(1433,10**11),40:F(2656,10**26),92:p2(-137)}
    for m,a in low_limits.items():ck('complete_low_source_'+str(m),low[m]<a)
    for m,e in {94:-137,96:-153,184:-282,186:-318,552:-936}.items():
        ck('complete_middle_source_'+str(m),mid[m]<p2(e))
    ck('field_mode92_below_two_minus140',caps[92]<p2(-140))
    ck('all_quadratic_middle_above184_zero',all(dyad(r['quadratic'])==0 for r in s['middle_complete_sources'] if r['mode']>=186))
    ck('positive_complete_inverse_tail_retained',dyad(s['complete_Neumann_tail_mass'])>0 and s['omitted_Neumann_terms_from']==5)
    ck('no_cheap_unknown_strip_upgrade',w['no_width_gain_for_unknown_middle_or_high_fields'] is True)
    out=dict(
        status='Actual exact post-check of the new R100 spectral enclosure; not a middle/full-PDE closure',
        author='exact_closure (GPT-6 Astra Pro, AI-assisted)',date='2026-11-13',
        all_gates=all(gates.values()),gates=gates,input_identities=ids,
        source_sha256=digest(__file__),parameter_domain=DOMAIN,
        final_field_norm=record(dyad(s['final_total'])),
        wide_field_norm=record(dyad(w['wide_centre_norm'])),
        wide_inverse_norm=record(dyad(w['wide_inverse_norm'])),
        complete_Neumann_tail=record(dyad(s['complete_Neumann_tail_mass'])),
        field_caps=[dict(mode=m,upper=record(caps[m]),exact_power2_upper_exponent=ceil_log2(caps[m])) for m in modes],
        complete_low_source_caps=[dict(mode=m,upper=record(low[m]),exact_power2_upper_exponent=ceil_log2(low[m])) for m in modes],
        selected_middle_sources=[dict(mode=m,upper=record(mid[m]),exact_power2_upper_exponent=ceil_log2(mid[m])) for m in (94,96,184,186,552)],
        source_units='signed pair Fourier mass e^(18m/125) |N_m|/((s+abs(ell))*V_I^2), source-x; full mean/inverse',
        actual_numeric_domain_claim='real R100 grouped domain; complex parity extension is a separately proved analytic consequence',
        low_middle_high_joint_paid=False,all46_cut_paid=False,closed_surface_claimed=False,
        no_new_Arb_ODE_or_source_integral=True,
        elapsed_seconds=time.monotonic()-began,
        peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    args.out.parent.mkdir(parents=True,exist_ok=True)
    with args.out.open('x') as f:json.dump(out,f,ensure_ascii=False,indent=2);f.write('\n')
    print(json.dumps(dict(event='R101_exact_summary_complete',all_gates=out['all_gates'],
        gates=len(gates),output=str(args.out),sha256=digest(args.out),
        seconds=out['elapsed_seconds'],RSS_KiB=out['peak_rss_kib'])),flush=True)
if __name__=='__main__':
    main()
