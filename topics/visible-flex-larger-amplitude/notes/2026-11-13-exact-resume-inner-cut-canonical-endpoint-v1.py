#!/usr/bin/env python3
"""Intersect actual canonical and physical high endpoint columns at cell12.

Author: exact_closure (GPT-6 Astra Pro; AI-assisted), 2026-11-13.
Reuses completed scalar endpoint source kernels without rerunning them.
All source, complete mean/inverse, far and infinite components retained.
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

PINS={
 'positive':('2026-11-12-closure-positive-highband-38.json.gz','cf293799252e8beb9ef15ff27dba1ebbe698186cee3258b6f9df34ab8dff5600'),
 'density':('2026-11-12-tail-r42-strong-same-tau-r1-density.json.gz','e640e3e693ca198460de902fc8d9bb1bd909c2a7051ec099aa930a86789e0700'),
 'ready':('2026-11-12-closure-scaled-endpoint-q003-m8-d12-f225-exclusive-ready.json','563a99973230a7f15d1c1ba8537edae34bc02158a0cfff90160d37f57e3ab2f6'),
}


def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def read(p):
    p=Path(p);b=p.read_bytes();return json.loads(gzip.decompress(b) if p.suffix=='.gz' else b)


def ab(v,side='upper'):
    if isinstance(v,list):return arb(int(v[0]))*arb(2)**int(v[1])
    if side in v:return ab(v[side],side)
    if 'mantissa' in v:return arb(int(v['mantissa']))*arb(2)**int(v['binary_exponent'])
    return arb(int(v['numerator']))/int(v['denominator'])


def pack(z,bits=160):
    if not z.is_finite():raise ArithmeticError('Every canonical endpoint coefficient must be finite')
    t=z.upper()
    if not t>=0:raise ArithmeticError('Negative positive endpoint upper')
    if t==0:return ['0',0]
    m,e=t.man_exp();m,e=int(m),int(e);q=max(0,m.bit_length()-bits)
    if q:m,e=(m+(1<<q)-1)>>q,e+q
    if not ab([m,e])>=t:raise ArithmeticError('Canonical endpoint rounding went inward')
    return [str(m),e]


def up(z):return ab(pack(z))


def main():
    p=argparse.ArgumentParser(description=__doc__)
    for k in ('topic','scalar-endpoint','scalar-resource','out-prefix'):p.add_argument('--'+k,type=Path,required=True)
    p.add_argument('--rss-kib',type=int,default=98304);a=p.parse_args();ctx.prec=256;ctx.threads=1;started=time.monotonic();out=Path(str(a.out_prefix)+'.json')
    if out.exists():raise FileExistsError('Keep original endpoint attempts immutable')
    scalar,usage=read(a.scalar_endpoint),read(a.scalar_resource);ids={};docs={}
    if not(scalar['all_gates'] and all(scalar['gates'].values()) and usage['exitcode']==0 and usage['termination_signal'] is None):raise ArithmeticError('Completed original physical endpoint kernels required')
    for k,(name,wanted) in PINS.items():
        path=a.topic/'notes'/name
        if sha(path)!=wanted:raise ArithmeticError('Original actual canonical endpoint input changed')
        docs[k]=read(path);ids[k]=dict(path=str(path),sha256=wanted)
    ids['scalar_endpoint']=dict(path=str(a.scalar_endpoint),sha256=sha(a.scalar_endpoint));ids['scalar_resource']=dict(path=str(a.scalar_resource),sha256=sha(a.scalar_resource))
    positive,density,ready=(docs[k] for k in ('positive','density','ready'))
    if PINS['ready'][1] not in positive['input_hashes'].values() or not all(density['gates'].values()):raise ArithmeticError('Same original real geometry required')
    r=next(r for r in density['rows'] if r['cell']==12);matrices=next(r for r in positive['cell_rows'] if r['cell']==12)['positive_cell_matrices']
    frac=F.from_float(ready['rationalDeepModel']['physicalParameters']['rCuff']);rc=arb(frac.numerator)/frac.denominator;R=rc*257/256
    sq12=arb(12).sqrt();B_lo=ab(r['B'],'lower');B_hi=ab(r['B']);mu_lo=ab(r['mu_lower'],'lower');mu_hi=ab(r['mu_upper']);w=ab(scalar['true_w_lower'])
    if not(rc>0 and mu_lo>0 and w>0 and B_lo>=120):raise ArithmeticError('Strict true conversion denominators required')
    drop=(ab(r['tau_inner'],'lower')-ab(r['tau_outer'])).lower()
    if not drop>=0:raise ArithmeticError('The same full cell angular loss is unpaid')
    Vin=ab(scalar['cell13_boundary_Vprime_upper']);jump=ab(scalar['frame_jump']);windows=[]
    for row in scalar['rows']:
        lo,hi=row['window'];covers=[j for j,b in enumerate(positive['bands']) if b['first_mode']<=lo and hi<=b['last_mode']]
        old=ab(row['initial_true_cell13_to_cut']);new=old;detail=None
        if covers:
            j=covers[0];A=[[ab(v) for v in q] for q in matrices[j]]
            if not all(z.is_finite() and z>=0 for q in A for z in q):raise ArithmeticError('Full positive canonical matrix required')
            nulo=arb(lo*lo*(lo*lo-1))/12;nuhi=arb(hi*hi*(hi*hi-1))/12
            win_hi=mu_hi/rc**7
            # Input paired strong mass is split into the same physical Bp,kappa
            # components; the common upper bounds each transformed component.
            cin=[1/(B_lo*lo*rc**3),R**4*win_hi/(sq12*mu_lo*nulo)*max(arb(1),arb(hi)/B_lo)]
            propagated=[up(A[i][0]*cin[0]+A[i][1]*cin[1]) for i in range(2)]
            cout=[(B_hi*hi+hi*hi)*R**3,sq12*mu_hi*nuhi/(rc**4*w)]
            decay=up((-lo*drop).exp())
            canonical=up(2*jump*Vin/w*((arb(1)+hi)/(1+lo))*decay*sum((cout[i]*propagated[i] for i in range(2)),arb(0)))
            new=min(old,canonical);detail=dict(original_matrix_window=[positive['bands'][j]['first_mode'],positive['bands'][j]['last_mode']],canonical_column=pack(canonical),paid_full_angular_decay=pack(decay),input_conversion=list(map(pack,cin)),output_conversion=list(map(pack,cout)))
        windows.append(dict(group=row['group'],window=row['window'],physical_column=row['initial_true_cell13_to_cut'],chosen_initial_column=pack(new),canonical=detail))
    budgets=[];masses=[]
    for old in scalar['complete_band_budgets']:
        group=old['name'];gain=max(ab(r['chosen_initial_column']) for r in windows if r['group']==group)
        incoming=up(gain*ab(old['initial_field']));reference=ab(old['complete_reference_source']);change=ab(old['complete_error_source']);full=up(incoming+reference+change);chosen=min(full,ab(old['chosen_same_field_bound']))
        budgets.append(dict(name=group,initial_gain=pack(gain),incoming=pack(incoming),complete_reference_source=pack(reference),complete_error_source=pack(change),new_endpoint_sum=pack(full),chosen_same_field_bound=pack(chosen)))
        masses.append(pack(chosen))
    masses.append(scalar['actual_R100_head_band_masses'][2])
    if resource.getrusage(resource.RUSAGE_SELF).ru_maxrss>a.rss_kib:raise MemoryError('Owned actual canonical endpoint RSS guard')
    result=dict(schema='same-R100-canonical-physical-high-endpoint-intersection-v1',author='exact_closure (GPT-6 Astra Pro; AI-assisted)',all_gates=True,
      gates=dict(same_complete_R100_field=True,all_original_endpoint_source_terms_retained=True,actual_canonical_matrices_cover_every_used_window=True,
      complete_true_radius_mu_w_and_frame_conversions=True,original_full_cell_angular_loss_paid=True,initial_strong_ratio_paid=True,
      every_coefficient_finite=True,all_shared_band_source_budgets_once=True,full_mean_inverse_far_retained=True,complete_infinite_band_retained=True),
      input_identities=ids,source_sha256=sha(__file__),actual_R100_head_band_masses=masses,domain=scalar['domain'],head_strip=scalar['head_strip'],head_bands=scalar['head_bands'],units=scalar['units'],
      rows=windows,complete_band_budgets=budgets,original_scalar_endpoint_primary=ids['scalar_endpoint'],
      no_scalar_or_ODE_or_Green_rerun=True,new_fixedpoint_or_outer_cut_claimed=False,elapsed_seconds=time.monotonic()-started,peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    out.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(dict(all_gates=True,path=str(out),sha256=sha(out),bytes=out.stat().st_size,head_display=[str(ab(z)) for z in masses],elapsed_seconds=result['elapsed_seconds'],peak_rss_kib=result['peak_rss_kib'])),flush=True)


if __name__=='__main__':main()
