#!/usr/bin/env python3
"""Actual all213 transverse lifts under simultaneous R129 axis/mass caps.

Author: /root (GPT-6 Astra Pro, AI-assisted), 2026-11-13.
This is a restricted parameter input, not a full-head or full-cut closure.
The original common-strip columns and their V-prime units are unchanged.
"""
from __future__ import annotations
import argparse
from fractions import Fraction as F
import gzip
import hashlib
import json
from pathlib import Path
import resource
import time
from root_hybrid46_cut_consumer import exact as ex, up, record


def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def read(p):
    p=Path(p);b=p.read_bytes()
    return json.loads(gzip.decompress(b) if p.suffix=='.gz' else b)


def support(coefficients,caps,total):
    value=F(0);left=total
    for i in sorted(range(len(caps)),key=lambda i:coefficients[i],reverse=True):
        take=min(left,caps[i]);value+=coefficients[i]*take;left-=take
        if not left:break
    return up(value)


def pack(v):
    v=up(v,128)
    return [str(v.numerator),-(v.denominator.bit_length()-1)] if v else [0,0]


def exact_domain(v):
    return dict(numerator=str(v.numerator),denominator=str(v.denominator))


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--inputs',type=Path,required=True)
    ap.add_argument('--out',type=Path,required=True)
    a=ap.parse_args();start=time.monotonic();ids=read(a.inputs);gates={}
    def gate(k,v):
        if not v:raise ArithmeticError(k)
        gates[k]=True
    def checked(k):
        r=ids[k];gate('identity_'+k,sha(r['path'])==r['sha256']);return read(r['path'])
    original=checked('original_lift');profile=checked('projected_profile')
    modes=list(range(2,93,2));cells=list(range(12,225))
    gate('complete_original213x46_and_profile',original['all_gates'] and profile['all_gates']
         and original['modes']==modes and original['cells']==cells
         and [r['cell'] for r in original['rows']]==cells and [r['mode'] for r in profile['rows']]==modes)
    gate('identical_original_R100_axes',all(ex(x)==ex(y['original_axis']) for x,y in zip(original['R100_axes'],profile['rows'])))
    gate('exact_original_one_over32_domain',ex(original['transverse_radius'])==F(1,32)
         and original['full_head_correction_e_still_separate'] and not original['full_head_source_or_high_trace_certified'])
    base=[F(0)]*6+[ex(r['projected_map_value']) for r in profile['rows'][6:]]
    far_unit=list(map(ex,original['far_unit_axis_pairs_unscaled_by_S']))
    domains=[]
    for name,factor,Sradius,Tradius in [('R129_working',2,F(1,2),F(1,36)),('expanded_profile',4,F(3,4),F(1,32))]:
        caps=[factor*v for v in base]
        gate('contained_in_R127_'+name,Sradius<=1 and Tradius<=F(1,32))
        rows=[]
        for i,row in enumerate(original['rows']):
            units=list(map(ex,row['transverse_unit_axis_pairs']))
            pair=[up(v*min(c,Tradius)) for v,c in zip(units,caps)]
            shared=support(units,caps,Tradius)
            oldpair=list(map(ex,row['Lambda_pair_caps_at_radius1over32']))
            gate('all46_pairs_restrict_original_'+name+'_'+str(row['cell']),all(0<=x<=y for x,y in zip(pair,oldpair)))
            gate('shared_mass_restrict_original_'+name+'_'+str(row['cell']),0<shared<=ex(row['Lambda_common_cap_at_radius1over32']))
            rows.append(dict(cell=row['cell'],Lambda_pair_caps_on_domain=list(map(pack,pair)),
                Lambda_common_cap_on_domain=pack(shared),original_unit_columns_sha256=ids['original_lift']['sha256'],
                actual_all46_original_unit_columns_retained=True))
        far=support(far_unit,caps,Tradius)
        gate('true_transverse_far_'+name,0<far<=ex(original['far_common_at_radius1over32']))
        domains.append(dict(name=name,S_linf_radius=exact_domain(Sradius),T_l1_radius=exact_domain(Tradius),
            original_normalized_T_coordinate_caps=list(map(exact_domain,caps)),
            coordinate_constraints_and_shared_T_mass_are_simultaneous=True,
            C_S_may_keep_original_unit_S_caps_conservatively=True,
            rows=rows,transverse_far_common_unscaled_by_S=pack(far),
            complete_auxiliary_far_must_be_added_separately=True,full_e_feedback_still_required=True))
    ans=dict(schema='R129-actual213-transverse-lift-profile-v1',author='/root (GPT-6 Astra Pro, AI-assisted)',
        source_sha256=sha(__file__),helper_sha256=sha(Path(__file__).with_name('root_hybrid46_cut_consumer.py')),
        input_manifest_sha256=sha(a.inputs),inputs=ids,all_gates=all(gates.values()),gates=gates,
        modes=modes,cells=cells,normalization=original['normalization'],
        original_continuous_strip_origin=original['exact_original_continuous_strip_origin'],
        original_axis_formulas_unchanged=True,domains=domains,
        full_head_or_full_cut_closed=False,new_ODE_or_source_integrals=0,
        elapsed_seconds=time.monotonic()-start,peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    if a.out.exists():raise FileExistsError(a.out)
    raw=(json.dumps(ans,separators=(',',':'))+'\n').encode()
    if a.out.suffix=='.gz':raw=gzip.compress(raw,compresslevel=9,mtime=0)
    if len(raw)>=5_000_000 or len(raw)>1_000_000 and a.out.suffix!='.gz':raise ArithmeticError('Compress or partition output')
    a.out.parent.mkdir(parents=True,exist_ok=True);a.out.write_bytes(raw)
    print(json.dumps(dict(all_gates=ans['all_gates'],gates=len(gates),sha256=sha(a.out),bytes=len(raw),
        working_cell12_Lambda92=float(ex(domains[0]['rows'][0]['Lambda_pair_caps_on_domain'][-1])),
        working_cell12_common=float(ex(domains[0]['rows'][0]['Lambda_common_cap_on_domain'])),
        expanded_cell12_Lambda92=float(ex(domains[1]['rows'][0]['Lambda_pair_caps_on_domain'][-1])),
        elapsed_seconds=ans['elapsed_seconds'],peak_rss_kib=ans['peak_rss_kib'])),flush=True)


if __name__=='__main__':main()
