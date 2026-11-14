#!/usr/bin/env python3
"""True high endpoint readout through the saved complete cell12 panels.

Author: exact_closure (GPT-6 Astra Pro; AI-assisted), 2026-11-13.
Initial true high data come from the already certified complete cell13
field.  Cell12 complete source is paid separately; all deeper source/far
dependence is already in that same field, not erased or integrated twice.
"""
import argparse
from fractions import Fraction as F
import gzip
import hashlib
import json
from pathlib import Path
import resource
import sys
import time
from flint import arb,ctx

PINS={
 'panels12':('2026-11-12-tail-r33-plateau2-continuous-strip-panels-cell012.json.gz','d0dc6791001a1668afa2f9442bbefbe7e6644e73b0b753943df5a9bc12258181'),
 'panels13':('2026-11-12-tail-r33-plateau2-continuous-strip-panels-cell013.json.gz','7397ebc436ae5c4cd396ae2e6d5d27c4f2b45e17fae5e75f94eb0acb9e95dc22'),
 'qdensity':('2026-11-12-tail-r33-plateau2-density-window.json.gz','0b493a5278ce08d12ed1d83add9dd3214125d971e746c750dfa42efa0729ace9'),
 'density':('2026-11-12-tail-r42-strong-same-tau-r1-density.json.gz','e640e3e693ca198460de902fc8d9bb1bd909c2a7051ec099aa930a86789e0700'),
 'trace':('2026-11-12-closure-strong-true-cut-trace-r1.json','44db92699bd9bf3d8ba613465b013033c82a7ed9f8fc8e5cc1f6a003539ad494'),
}
NEAR=[(94,96),(98,104),(106,112),(114,128),(130,184)]
REST=[(186,192),(194,256),(258,512),(514,1024),(1026,2048),(2050,4096),(4098,8190)]


def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def read(p):
    p=Path(p);b=p.read_bytes();return json.loads(gzip.decompress(b) if p.suffix=='.gz' else b)


def ab(v,side='upper'):
    if isinstance(v,list):return arb(int(v[0]))*arb(2)**int(v[1])
    if side in v:return ab(v[side],side)
    if 'mantissa' in v:return arb(int(v['mantissa']))*arb(2)**int(v['binary_exponent'])
    return arb(int(v['numerator']))/int(v['denominator'])


def ex(v,side='upper'):
    if isinstance(v,list):return F(int(v[0]))*F(2)**int(v[1])
    if side in v:return ex(v[side],side)
    if 'mantissa' in v:return F(int(v['mantissa']))*F(2)**int(v['binary_exponent'])
    return F(int(v['numerator']),int(v['denominator']))


def ball(v):
    lo,hi=ab(v,'lower'),ab(v,'upper')
    return lo.union(hi)


def pack(z,bits=160):
    if not z.is_finite():raise ArithmeticError('Every actual endpoint coefficient must be finite')
    t=z.upper()
    if not t>=0:raise ArithmeticError('Positive endpoint comparison became negative')
    if t==0:return ['0',0]
    m,e=t.man_exp();m,e=int(m),int(e);shift=max(0,m.bit_length()-bits)
    if shift:m,e=(m+(1<<shift)-1)>>shift,e+shift
    if not ab([m,e])>=t:raise ArithmeticError('Endpoint rounding went inward')
    return [str(m),e]


def up(z):return ab(pack(z))


def main():
    p=argparse.ArgumentParser(description=__doc__)
    for k in ('topic','complete-field','field-resource','source-summary','source-resource','out-prefix'):p.add_argument('--'+k,type=Path,required=True)
    p.add_argument('--rss-kib',type=int,default=98304);a=p.parse_args();ctx.prec=256;ctx.threads=1;start=time.monotonic();out=Path(str(a.out_prefix)+'.json')
    if out.exists():raise FileExistsError('Use a fresh true endpoint readout artifact')
    sys.path.insert(0,str(a.topic/'computations'))
    from closure_split_joint_io_v2 import iter_array,metadata_without_array
    paths={k:a.topic/'notes'/v[0] for k,v in PINS.items()};ids={}
    for k,v in paths.items():
        if sha(v)!=PINS[k][1]:raise ArithmeticError('An original actual endpoint input changed: '+k)
        ids[k]=dict(path=str(v),sha256=sha(v))
    for k in ('complete_field','field_resource','source_summary','source_resource'):
        q=getattr(a,k);ids[k]=dict(path=str(q),sha256=sha(q))
    field,usage,source,susage=(read(getattr(a,k)) for k in ('complete_field','field_resource','source_summary','source_resource'))
    if not(field['all_gates'] and all(field['gates'].values()) and field['schema']=='same-R100-complete-nonlinear641-finite-bootstrap-v1'
           and usage['exitcode']==0 and usage['termination_signal'] is None and source['all_gates'] and all(source['gates'].values())
           and susage['exitcode']==0 and susage['termination_signal'] is None
           and field['input_identities']['source_summary']['sha256']==sha(a.source_summary)):raise ArithmeticError('Same actual complete field and complete source required')
    density,qdensity,trace=(read(paths[k]) for k in ('density','qdensity','trace'))
    if not(all(density['gates'].values()) and all(qdensity['gates'].values()) and trace['all_gates']):raise ArithmeticError('Original source and true cut identities required')
    rr={x['cell']:x for x in density['rows']};qr={x['cell']:x for x in qdensity['rows']}
    meta={n:metadata_without_array(paths['panels'+str(n)],'panels') for n in (12,13)}
    S=arb(257)/256;sigma={}
    for n in (12,13):
        if not(ex(qr[n]['canonical_total_envelope'],'lower')==ex(qr[n]['canonical_total_envelope'])>0 and ex(rr[n]['canonical_total_envelope'],'lower')==ex(rr[n]['canonical_total_envelope'])>0):raise ArithmeticError('Exact actual cell scales required')
        ratio=ex(rr[n]['canonical_total_envelope'])/ex(qr[n]['canonical_total_envelope']);sigma[n]=arb(ratio.numerator)/ratio.denominator
        for key in ('B','tau_inner','tau_outer'):
            if not(meta[n][key]['lower']==qr[n][key]['lower'] and meta[n][key]['upper']==qr[n][key]['upper'] and qr[n][key]==rr[n][key]):raise ArithmeticError('The entire same continuous strip/frame is required')
    if not(ex(rr[12]['tau_inner'])<=ex(rr[13]['tau_outer'],'lower') and ex(rr[12]['tau_outer'])==ex(trace['head_strip'])):raise ArithmeticError('The exact boundary angular width is unpaid')
    wcut=ab(trace['true_w'],'lower')
    if not wcut>0:raise ArithmeticError('Strict actual positive w at the true cut required')
    # Last true cell13 panel gives a positive bound at its outer endpoint.
    last=None;last_segment=0;last_x=F(0);count13=0
    for g in iter_array(paths['panels13'],'panels'):
        segment=g['segment'];left,right=F(*g['x_left']),F(*g['x_right'])
        if segment==last_segment:
            if left!=last_x:raise ArithmeticError('Actual cell13 panel gap')
        elif segment==last_segment+1 and last_x==1 and left==0:last_segment=segment
        else:raise ArithmeticError('Actual cell13 panel order')
        last_x=right;last=g;count13+=1
    if not(last_segment==8 and last_x==1):raise ArithmeticError('Complete original cell13 required')
    V13=up(S*sigma[13]*ab(last['V']));jump=up(max(arb(1),ab(rr[12]['B'])/ab(rr[13]['B'],'lower')))
    W=list(map(ab,field['same_original_metric_weights']));v=list(map(ab,field['full641_checkpoints'][-1]['all641_W_scaled_caps']))
    initial={g:up(v[i]*W[i]) for g,i in [('near',214),('rest',427)]}
    source12=source['rows'][0]
    if source12['cell']!=12 or field['last_source_rows'][0]['cell']!=12:raise ArithmeticError('Actual source12 row required')
    variation={g:ab(field['last_source_rows'][0]['high_sources'][g]) for g in ('near','rest')}
    parts={g:{mat:ab(source12['source_common_mass'][mat][band]) for mat in ('d1','d_lambda')} for g,band in [('near','near94to184'),('rest','rest186to8190')]}
    result_rows=[];kappa=ball(meta[12]['k']);B=ball(rr[12]['B'])
    if not(kappa.is_finite() and kappa.lower()>0 and B.lower()>=120):raise ArithmeticError('Strict original damping/frame lower required')
    for group,bands in [('near',NEAR),('rest',REST)]:
        for lo,hi in bands:
            q=max(arb(0),(1-arb(lo)/B).upper());G=arb(1);H={z:arb(0) for z in ('d1','d_lambda')};last_segment=0;last_x=F(0);count=0
            for g in iter_array(paths['panels12'],'panels'):
                segment=g['segment'];left,right=F(*g['x_left']),F(*g['x_right'])
                if segment==last_segment:
                    if left!=last_x:raise ArithmeticError('Actual cell12 panel gap')
                elif segment==last_segment+1 and last_x==1 and left==0:last_segment=segment
                else:raise ArithmeticError('Actual cell12 panel order')
                last_x=right;count+=1
                V,aa=ball(g['V']),ball(g['V_over_w']);material=ball(g['material_cV_over_w']);radial=ball(g['radial_log_increment']);variation_w=ball(g['log_w_variation']);down=ab(g['log_w_down_variation'])
                if not(all(z.is_finite() for z in (V,aa,material,radial,variation_w,down)) and V.lower()>0 and aa.lower()>0 and material.lower()>0 and radial.lower()>0 and variation_w.lower()>=0 and down>=0):raise ArithmeticError('Every original true positive panel required')
                Jlo=(material.lower()/kappa.upper()).lower();Jhi=(material.upper()/kappa.lower()).upper()
                growth=up((q*down).exp());prop=up((q*down-lo*Jlo).exp())
                common=up(kappa.upper()*V.upper()*(-(-lo*Jhi).expm1())/lo)
                raw={'d1':up(V.upper()*aa.upper()*radial.upper()),'d_lambda':up(V.upper()*aa.upper()*variation_w.upper())}
                for mat in H:H[mat]=up(prop*H[mat]+growth*min(raw[mat],common))
                G=up(prop*G)
            if not(last_segment==8 and last_x==1):raise ArithmeticError('The complete original cell12 range is missing')
            # Initial data are already in the strong(1+m) norm, so the
            # source multiplier(1+hi) is not charged to the initial column.
            init=up(2*jump*V13*G/wcut)
            kern={z:up(2*(1+hi)*(S*sigma[12])**2*H[z]/wcut) for z in H}
            result_rows.append(dict(group=group,window=[lo,hi],panels=count,homogeneous_factor=pack(G),initial_true_cell13_to_cut=pack(init),source_two_material_to_cut={z:pack(kern[z]) for z in kern},source_common_to_cut=pack(kern['d1']+kern['d_lambda'])))
            print(json.dumps(dict(event='true_cell12_endpoint_high_kernel',group=group,window=[lo,hi],panels=count,elapsed_seconds=time.monotonic()-start,peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)),flush=True)
            if resource.getrusage(resource.RUSAGE_SELF).ru_maxrss>a.rss_kib:raise MemoryError('Owned actual endpoint readout RSS guard')
    bands=[]
    for group in ('near','rest'):
        rows=[r for r in result_rows if r['group']==group]
        ig=max(ab(r['initial_true_cell13_to_cut']) for r in rows);kg={z:max(ab(r['source_two_material_to_cut'][z]) for r in rows) for z in ('d1','d_lambda')};kc=max(ab(r['source_common_to_cut']) for r in rows)
        incoming=up(ig*initial[group]);reference=up(sum((kg[z]*parts[group][z] for z in kg),arb(0)));change=up(kc*variation[group]);val=up(incoming+reference+change)
        idx=0 if group=='near' else 1;oldhead=ab(field['checkpoints'][-1]['head_complete_balanced_P_K_by_band'][idx]);chosen=min(val,oldhead)
        bands.append(dict(name=group,initial_field=pack(initial[group]),initial_column=pack(ig),incoming=pack(incoming),complete_reference_source=pack(reference),complete_error_source=pack(change),endpoint_bound=pack(val),previous_whole_cell_bound=pack(oldhead),chosen_same_field_bound=pack(chosen),each_common_band_mass_shared_once=True))
    masses=[b['chosen_same_field_bound'] for b in bands]+[field['checkpoints'][-1]['head_complete_balanced_P_K_by_band'][2]]
    output=dict(schema='same-R100-truecut-high-endpoint-readout-v1',author='exact_closure (GPT-6 Astra Pro; AI-assisted)',all_gates=True,
      gates=dict(same_R100_six_unit_transverse_l1_1over32=True,same_actual_complete_field=True,complete_original_cell12_and13_panels=True,
      full_original_variable_strip_and_frame_jump=True,initial_strong_weight_paid_once=True,source_strong_weight_paid=True,
      complete_cell12_mean_inverse_source=True,deeper_all_sources_and_true_far_in_initial_field=True,
      every_endpoint_coefficient_finite=True,whole_near_rest_even_frequency_ranges=True,infinite_high_retained_from_complete_field=True),
      input_identities=ids,source_sha256=sha(__file__),head_strip=field['head_strip'],actual_R100_head_band_masses=masses,
      domain=dict(S_product_radius=['1',0],T_l1_radius=['1',-5]),head_bands=[[94,184],[186,8190],[8192,None]],
      units='Exactly the original R100 head balanced P/K strong pair masses at tau_b; original617987048c3a599acb42bcafe8dba99155c5cde82d252706769d5e24340ce1b9 units',
      rows=result_rows,complete_band_budgets=bands,infinite_readout_method='Retain the previous full-field same-point complete bound, no infinite frequencies dropped',
      true_w_lower=pack(wcut),cell13_boundary_Vprime_upper=pack(V13),frame_jump=pack(jump),cell13_original_panels=count13,
      no_new_ODE_or_radial_quadrature=True,new_fixedpoint_or_outer_cut_claimed=False,elapsed_seconds=time.monotonic()-start,peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    out.write_text(json.dumps(output,indent=2)+'\n')
    print(json.dumps(dict(all_gates=True,path=str(out),sha256=sha(out),bytes=out.stat().st_size,head_display=[str(ab(x)) for x in masses],elapsed_seconds=output['elapsed_seconds'],peak_rss_kib=output['peak_rss_kib'])),flush=True)


if __name__=='__main__':main()
