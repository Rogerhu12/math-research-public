#!/usr/bin/env python3
"""Bind the R143 low boundary height to the exact R173 candidate at node10.

Only the prescribed low46 height is used. Nonlow traces and every true K
trace remain separate debts. Binary background data are not true background.
Author: /root (GPT-6 Astra Pro; AI-assisted), 2026-11-13.
"""
import argparse
from fractions import Fraction as F
import gzip
import hashlib
import json
from pathlib import Path
import resource
import time
from flint import arb, ctx, fmpq

def sha(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def load(p):
    p=Path(p); raw=p.read_bytes()
    return json.loads(gzip.decompress(raw) if p.suffix=='.gz' else raw)
def q(v):
    if isinstance(v,dict): m,e=int(v['mantissa']),int(v['binary_exponent'])
    else: m,e=int(v[0]),int(v[1])
    return F(m)*F(2)**e
def interval(v): return q(v['lower']),q(v['upper'])
def rational(v): return [str(v.numerator),str(v.denominator)]
def record(v): return dict(lower=rational(v[0]),upper=rational(v[1]))
def point(v):
    m,e=v.man_exp(); return [str(m),int(e)]
def ar(v): return arb(fmpq(v.numerator,v.denominator))
def scaled(v,a): return (v[0]*a,v[1]*a) if a>=0 else (v[1]*a,v[0]*a)
def shifted(v,a): return v[0]+a,v[1]+a
def absupper(v): return max(abs(v[0]),abs(v[1]))

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--inputs',type=Path,required=True)
    ap.add_argument('--out',type=Path,required=True)
    a=ap.parse_args(); started=time.monotonic();ctx.prec=256;ctx.threads=1
    if a.out.exists(): raise FileExistsError(a.out)
    ids=load(a.inputs); counts={}
    def gate(k,v):
        counts[k]=counts.get(k,0)+1
        if not v: raise ArithmeticError(k)
    for k,v in ids['files'].items(): gate('input_identity_'+k,sha(v['path'])==v['sha256'])
    get=lambda k:load(ids['files'][k]['path'])
    geom=get('geometry'); cfg=geom['config']; coords=get('coordinates')
    jets=get('jets'); mean=get('mean'); polys=get('polynomials')
    response=get('response'); cp=response['response']['checkpoint']
    gate('original_actual_geometry',geom['all_gates'] and all(geom['gates'].values())
         and cfg['modes']==list(range(2,93,2))
         and cfg['entrypoint_sha256']==ids['files']['geometry_source']['sha256'])
    gate('original_geometry_uses_same_complete_response',
         cfg['input_hashes']['notes/2026-11-12-closure-newg-strong-m20-frozen-d12-f225-response.json.gz']==ids['files']['response']['sha256'])
    gate('original_complete_M20_raw_nodes',len(cp['rawStates'])==13
         and all(len(v)==40 for v in cp['rawStates']) and len(cp['states'])==865
         and cp['rawNode']==[72*i for i in range(13)])
    for key,obj in [('coordinates',coords),('jets',jets),('mean',mean)]:
        gate('actual_owned_'+key,get(key+'_resource')['exitcode']==0 and obj['all_gates'])
    gate('unchanged_mean_candidate_polynomial',mean['candidate_degree']==5
         and mean['polynomial_file']['sha256']==ids['files']['polynomials']['sha256']
         and mean['inputs']['files']['jets']['sha256']==ids['files']['jets']['sha256'])
    gate('jets_are_same_original_coordinates',jets['inputs']['files']['R168_primary']['sha256']==ids['files']['coordinates']['sha256'])
    ep=coords['summary']['endpoint_node10']
    gate('true_saved_node10_identity',ep['saved_node']==cp['rawNode'][10]==720
         and ep['stage_index']==719 and ep['raw_cell']==9 and ep['raw_segment']==0
         and ep['source_x']==0 and ep['same_saved_binary_Q'])
    jp=[v for v in jets['pieces'] if (v['raw_cell'],v['raw_segment'],v['part'])==(9,0,0)]
    pp=[v for v in polys['rows'] if (v['cell'],v['segment'],v['part'])==(9,0,0)]
    gate('unique_original_entry_piece',len(jp)==len(pp)==1 and jp[0]['inner_node']==720)
    jp,pp=jp[0],pp[0]
    R,W=interval(cfg['outer_radius']),interval(cfg['outer_w'])
    gate('strict_true_geometry',0<R[0]<=R[1] and 0<W[0]<=W[1])
    rb,wb=F.from_float(ep['radius']),F.from_float(ep['w'])
    gate('strict_binary_geometry',rb>0 and wb>0)
    truefactor=(R[0]**3/W[1],R[1]**3/W[0]); binaryfactor=rb**3/wb
    modes=list(range(2,93,2)); rows=[]; norms={s:arb(0) for s in ['1/64','0']}
    norms_geometry={s:arb(0) for s in norms};norms_round={s:arb(0) for s in norms}
    nonzero=[]
    for m in modes:
        i=m//2-1; qo=interval(cfg['actual_outer_Q'][str(m)])
        gate('point_valued_original_boundary_height',qo[0]==qo[1])
        rawq=F.from_float(cp['rawStates'][10][i]) if m<=40 else F(0)
        gate('exact_all46_original_outer_height_binding',qo[0]==rawq)
        if m<=40:
            gate('same_binary_Q_in_R168_and_original_raw',F.from_float(ep['Q'][i])==rawq
                 and F.from_float(cp['states'][720][i])==rawq)
            pb=F.from_float(ep['relative_P_sine'][i]); kb=F.from_float(ep['relative_K_cosine'][i])
            gate('same_exact_R169_entry_values',pb==F.from_float(jp['P0'][i]) and kb==F.from_float(jp['K0'][i]))
            gate('same_exact_R173_quintic_endpoint',pb==F(*map(int,pp['exact_P_Bernstein'][i][0]))
                 and kb==F(*map(int,pp['exact_K_Bernstein'][i][0])))
        else:
            pb=kb=F(0)
        trueP=scaled(truefactor,-m*rawq); idealBinaryP=-m*binaryfactor*rawq
        delta=shifted(trueP,-pb); geometry=shifted(trueP,-idealBinaryP); rounding=idealBinaryP-pb
        gate('exact_error_decomposition',shifted(geometry,rounding)==delta)
        if m>40:gate('prescribed_low_extension_exact_zero',rawq==pb==kb==0 and delta==(F(0),F(0)))
        excludes_zero=delta[1]<0 or delta[0]>0
        if excludes_zero:nonzero.append(m)
        for sig in norms:
            weight=(1+m)*(ar(F(sig))*m).exp()
            norms[sig]+=weight*ar(absupper(delta))
            norms_geometry[sig]+=weight*ar(absupper(geometry))
            norms_round[sig]+=weight*ar(abs(rounding))
        rows.append(dict(mode=m,exact_prescribed_Q=rational(rawq),candidate_P=rational(pb),candidate_K=rational(kb),
            true_P_interval=record(trueP),true_minus_candidate_P=record(delta),
            true_geometry_minus_binary_formula=record(geometry),exact_binary_formula_minus_stored_P=rational(rounding),
            absolute_P_error_upper=rational(absupper(delta)),P_error_strictly_excludes_zero=excludes_zero))
    gate('all46_and_no_high_boundary_claim',len(rows)==46 and len(pp['exact_P_Bernstein'])==20)
    result=dict(schema='R177-exact-node10-low46-height-and-P-binding-v1',author='/root (GPT-6 Astra Pro; AI-assisted)',
        source_sha256=sha(__file__),input_manifest_sha256=sha(a.inputs),inputs=ids,
        all_gates=True,gate_count=sum(counts.values()),gate_categories=counts,
        true_radius=record(R),true_w=record(W),binary_radius=rational(rb),binary_w=rational(wb),
        true_minus_binary_radius=record(shifted(R,-rb)),true_minus_binary_w=record(shifted(W,-wb)),
        mode_rows=rows,strictly_nonzero_P_error_modes=nonzero,
        radial_point_strong_P_error_upper={s:point(v.upper())for s,v in norms.items()},
        separate_geometry_error_upper={s:point(v.upper())for s,v in norms_geometry.items()},
        separate_binary_formula_rounding_upper={s:point(v.upper())for s,v in norms_round.items()},
        every_prescribed_low_height_matches_original_M20_exactly=True,
        true_P_does_not_equal_binary_candidate_by_assumption=True,
        low42_to92_entry_P_exactly_zero=True,
        nonlow94_to_infinity_entry_not_set_to_zero=True,
        actual_full_K_trace_not_claimed=True,actual_solution_in_R173_tube_not_claimed=True,
        no_ODE_or_background_quadrature=True,
        elapsed_seconds=time.monotonic()-started,peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    a.out.write_bytes(gzip.compress((json.dumps(result,separators=(',',':'))+'\n').encode(),mtime=0))
    print(json.dumps(dict(primary=str(a.out),sha256=sha(a.out),gate_count=result['gate_count'],
        strong_P_error={s:float(v.upper())for s,v in norms.items()},strict_nonzero_modes=nonzero,
        geometry_error={s:float(v.upper())for s,v in norms_geometry.items()},rounding_error={s:float(v.upper())for s,v in norms_round.items()},
        elapsed_seconds=result['elapsed_seconds'],peak_rss_kib=result['peak_rss_kib'])),flush=True)

if __name__=='__main__':main()
