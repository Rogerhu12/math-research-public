#!/usr/bin/env python3
"""Recover all original 46x213 raw-material true-cut source columns.

Author: geometry_audit (GPT-6 Astra Pro; AI-assisted), 2026-11-13.
Uses the already completed R82 base phi source integrals, without any
nonlinear multiplier or wide-reference source gain. No ODE or quadrature.
"""
import argparse
from fractions import Fraction as F
import gzip
import hashlib
import json
from pathlib import Path
import resource
import time
from flint import arb,ctx

ARCHIVE='2026-11-12-root-r82-complete-stable-manifest.json'
ARCHIVE_SHA='9b2971944041c2964bfee1cc9d1d7fa40e5392f28b401a9c2ace22618e681a1a'
DENSITY='2026-11-12-tail-r42-strong-same-tau-r1-density.json.gz'
DENSITY_SHA='e640e3e693ca198460de902fc8d9bb1bd909c2a7051ec099aa930a86789e0700'
TRACE='2026-11-12-closure-strong-true-cut-trace-r1.json'
TRACE_SHA='44db92699bd9bf3d8ba613465b013033c82a7ed9f8fc8e5cc1f6a003539ad494'
R82_SOURCE_SHA='d2cf76d0aa5202b37a0123f4f8d4e743c99ec1f74fe576c177f8ab5d7d86dfc3'
FROZEN_R63_SHA='ce42ce8a3dc40f8d03afc810ba33a215dcacd032b06f15433cea5fe38b3ba038'


def sha(p):
    h=hashlib.sha256()
    with Path(p).open('rb') as f:
        for b in iter(lambda:f.read(1024*1024),b''):h.update(b)
    return h.hexdigest()


def read(p):
    p=Path(p)
    with (gzip.open(p,'rt') if p.suffix=='.gz' else p.open()) as f:return json.load(f)


def exact(v,side='upper'):
    if isinstance(v,list):return F(int(v[0]))*F(2)**int(v[1])
    if side in v:return exact(v[side],side)
    if 'mantissa' in v:return F(int(v['mantissa']))*F(2)**int(v['binary_exponent'])
    return F(int(v['numerator']),int(v['denominator']))


def aq(v):return arb(v.numerator)/v.denominator
def ab(v,side='upper'):return aq(exact(v,side))


def pack(z,bits=160):
    if not(z.is_finite() and z.lower()>=0):raise ArithmeticError('Finite positive cut coefficient required')
    t=z.upper()
    if not t:return ['0',0]
    m,e=t.man_exp();m,e=int(m),int(e);s=max(0,m.bit_length()-bits)
    if s:m,e=(m+(1<<s)-1)>>s,e+s
    result=[str(m),e]
    if not ab(result)>=t:raise ArithmeticError('Cut coefficient rounded inward')
    return result


def up(z):return ab(pack(z))


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--inputs',type=Path,required=True)
    parser.add_argument('--out-prefix',type=Path,required=True)
    parser.add_argument('--rss-kib',type=int,default=98304)
    args=parser.parse_args();ctx.prec=256;ctx.threads=1;started=time.monotonic()
    out=Path(str(args.out_prefix)+'.json.gz')
    if out.exists():raise FileExistsError('A fresh immutable cut-kernel output is required')
    checks=0;counts={}
    def check(name,condition):
        nonlocal checks
        checks+=1
        if not condition:raise ArithmeticError(name)
        counts[name]=counts.get(name,0)+1
    paths={name:args.inputs/name for name in (ARCHIVE,DENSITY,TRACE)}
    for name,wanted in ((ARCHIVE,ARCHIVE_SHA),(DENSITY,DENSITY_SHA),(TRACE,TRACE_SHA)):
        check('original_prerequisite_hash',sha(paths[name])==wanted)
    archive,density,trace=(read(paths[name]) for name in (ARCHIVE,DENSITY,TRACE))
    check('original_full46_archive_completed',archive['all46_resource_exits']==0 and archive['source_window_tool_exit']==0)
    check('original_density_and_true_cut_gates',all(density['gates'].values()) and trace['all_gates'] and all(trace['checks'].values()))
    pinned={Path(r['path']).name:r for r in archive['files']}
    modes=list(range(2,93,2));cells=list(range(12,225))
    dr={r['cell']:r for r in density['rows']}
    check('original_complete213_source_domain',sorted(dr)==cells)
    sigma=arb(1)/64;head=ab(trace['head_strip'])
    check('exact_head_width_above_sigma',exact(trace['head_strip'],'lower')==exact(trace['head_strip'])>F(1,64))
    S=arb(257)/256
    geometry_conversion=(arb(12).sqrt().upper()*ab(dr[12]['mu_upper'])/
                         (ab(trace['true_radius'],'lower')**4*ab(trace['true_w'],'lower')**2)).upper()
    check('strict_actual_cut_conversion',geometry_conversion>0)
    rows=[{'cell':n,'tau_inner':dr[n]['tau_inner'],'tau_outer':dr[n]['tau_outer'],
           'base_phi_source_integral_upper':[],'mu_ratio_upper':[],
           'Kbar_pair_upper':[],'W_sigma1_upper':[],'W_head1_upper':[]} for n in cells]
    identities={name:{'path':str(path),'sha256':sha(path),'bytes':path.stat().st_size} for name,path in paths.items()}
    original_inputs=original_panels=None;groups={};ci_saved=None
    for m in modes:
        name=f'2026-11-12-root-r82-source-m{m:03d}-r2.json.gz'
        resource_name=f'2026-11-12-root-r82-source-m{m:03d}-r2-resource.json'
        for fn in (name,resource_name):
            path=args.inputs/fn
            check('complete_manifest_pinned_mode_file',fn in pinned and sha(path)==pinned[fn]['sha256'] and path.stat().st_size==pinned[fn]['bytes'])
            identities[fn]={'path':str(path),'sha256':sha(path),'bytes':path.stat().st_size}
        data,usage=read(args.inputs/name),read(args.inputs/resource_name)
        check('formal_original_mode_success',usage['exitcode']==0 and usage['termination_signal'] is None and data['all_gates'] and all(data['checks'].values()))
        check('complete_original_mode_and_source_cover',data['selected_modes']==[m] and data['auxiliary_input_modes']==modes and data['cells']==cells and len(data['rows'])==1 and data['rows'][0]['mode']==m and [r['cell'] for r in data['rows'][0]['source_rows']]==cells)
        check('raw_material_source_producer_identity',data['source_sha256']==R82_SOURCE_SHA and data['frozen_R63_v3_source_sha256']==FROZEN_R63_SHA and data['new_source_quadrature']==0 and data['new_flow_solves']==0)
        check('same_original_trace_density_and_sigma',
              data['input_hashes'].get('notes/'+DENSITY)==DENSITY_SHA and data['input_hashes'].get('notes/'+TRACE)==TRACE_SHA and data['outer_strip']=='1/64')
        if original_inputs is None:
            original_inputs=data['input_hashes'];original_panels=data['panel_hashes'];ci_saved=data['point_cut_K_conversion']
        check('one_actual_problem_for_all46',data['input_hashes']==original_inputs and data['panel_hashes']==original_panels and data['point_cut_K_conversion']==ci_saved)
        for path,h in data['group_hashes'].items():
            check('unchanged_original_linear_group',path not in groups or groups[path]==h)
            groups[path]=h
        ci=ab(ci_saved)
        check('saved_true_w_squared_conversion_dominates_recomputed',ci>=geometry_conversion)
        weights={'W_sigma1_upper':up((1+m)*(m*sigma).exp()),
                 'W_head1_upper':up((1+m)*(m*head).exp())}
        for row,source in zip(rows,data['rows'][0]['source_rows']):
            I=ab(source['phi_source_integrals']['base']);mu=ab(source['mu_ratio_upper'])
            check('strict_positive_original_base_material_and_mu',I>0 and mu>0 and I.is_finite() and mu.is_finite())
            K=up(S*S*ci*mu*I)
            row['base_phi_source_integral_upper'].append(pack(I));row['mu_ratio_upper'].append(pack(mu))
            row['Kbar_pair_upper'].append(pack(K))
            for key,weight in weights.items():row[key].append(pack(K*weight))
            check('all_three_saved_cut_units_positive',all(exact(row[key][-1])>0 for key in ('Kbar_pair_upper','W_sigma1_upper','W_head1_upper')))
        check('small_single_thread_RSS_guard',resource.getrusage(resource.RUSAGE_SELF).ru_maxrss<=args.rss_kib)
        if m%8==0 or m==92:print(json.dumps({'event':'original_low_cut_modes_extracted','mode':m,'completed_modes':m//2,'elapsed_seconds':time.monotonic()-started,'peak_rss_kib':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss}),flush=True)
    check('all_six_original_real_linear_groups',len(groups)==6)
    check('all_twelve_original_shallow_panel_providers',len(original_panels)==12)
    for row in rows:
        check('all46_complete_row_columns',all(len(row[k])==46 for k in ('base_phi_source_integral_upper','mu_ratio_upper','Kbar_pair_upper','W_sigma1_upper','W_head1_upper')))
        for key in ('Kbar_pair_upper','W_sigma1_upper','W_head1_upper'):
            row[key+'_max_for_one_shared_low46_mass']=pack(max(ab(z) for z in row[key]))
            row[key+'_sum_for_independent_unit_each_mode']=pack(sum((ab(z) for z in row[key]),arb(0)))
    result={'schema':'same-original-inner-low46-common-material-truecut-kernels-v1','author':'geometry_audit (GPT-6 Astra Pro; AI-assisted)',
        'all_gates':True,'gate_count':checks,'gates':{k:True for k in counts},'gate_multiplicities':counts,
        'source_sha256':sha(__file__),'input_identities':identities,
        'original_R82_complete_source_dependencies':original_inputs,'original_shallow_panel_identities':original_panels,'original_six_linear_group_identities':groups,
        'modes':modes,'cells':cells,'rows':rows,
        'normalization_S':['257',-8],'source_Vprime_over_Vs_squared':pack(S*S),
        'point_cut_K_conversion':ci_saved,'sigma':['1',-6],'head_strip':trace['head_strip'],
        'source_material':'dprime=Vprime^2/(r*w)+abs(w_r/w)*Vprime^2/w, Vprime=(257/256)*Vs, original continuous tau(r)',
        'source_input_norm':'For each cell and positive even mode, the complete signed-pair weak mass is sum over +/-m of radial sup exp(|m|tau(r))*|physical_kappa_source_m|/dprime.',
        'raw_output':'Kbar_pair_upper multiplies that per-mode input to bound the cut pair of delta(kappa_perp)/true_w, for zero shallow Dirichlet source response.',
        'strong_output':'W_sigma1_upper and W_head1_upper add exactly (1+m)*exp(m*sigma) or (1+m)*exp(m*tau_b).',
        'kernel_formula':'S^2 * original_R82_point_cut_K_conversion * original_mu_ratio_upper * phi_source_integrals.base; no nonlinear constant and no reference-strip spectral gain are included.',
        'point_conversion_formula':'sqrt(12)*mu12_upper/(true_b_lower^4*true_w_lower^2), with the accurate inner mu12 convention',
        'pair_convention':'A real sine/cosine amplitude equals the complete +/- Fourier pair mass; no additional factor2.',
        'all9798_source_entries_strictly_positive':True,
        'common_mass_rule':'max over modes is valid against one summed per-mode radial-supremum-first source mass; sum of columns assumes an independent unit input in every mode and is not that same norm.',
        'same_original_inner_geometry_only':True,'new_g_or_new_H_certificate_transfer':False,
        'auxiliary_or_true_far_boundary_included':False,
        'far_boundary_requirement':'The complete nonlinear far lift is a separate nonzero contribution; include it once under its correct same-field common mass.',
        'full_mean_inverse_or_other_nonlinearity_already_paid':False,
        'source_requirement':'Supply the complete actual source on the stated domain. The raw base kernel is reusable but proves no source bound or field existence by itself.',
        'new_ODE_radial_quadrature_Node_calls':0,'new_fixedpoint_or_cut_closure_claimed':False,
        'elapsed_seconds':time.monotonic()-started,'peak_rss_kib':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss}
    out.parent.mkdir(parents=True,exist_ok=True)
    payload=gzip.compress((json.dumps(result,separators=(',',':'))+'\n').encode(),compresslevel=9,mtime=0)
    check('artifact_below_5MB',len(payload)<5_000_000)
    out.write_bytes(payload)
    print(json.dumps({'all_gates':True,'saved_gate_count':result['gate_count'],'path':str(out),'sha256':sha(out),'bytes':len(payload),
                      'elapsed_seconds':time.monotonic()-started,'peak_rss_kib':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss}),flush=True)


if __name__=='__main__':main()
