#!/usr/bin/env python3
"""Finite positive substitutions for the SAME already existing R100 head.

Author: exact_closure (GPT-6 Astra Pro; AI-assisted), 2026-11-13.
The reference is Cs+Lambda d, the independent far centre remains z_aux.
All641 original rows, full mean/inverse and true far columns are retained.
This consumes the existing solution; it does not assert a new fixed point.
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
from flint import arb,arb_mat,ctx

PINS={
 'jacobian':('2026-11-12-closure-strong-parameter-jacobian-r1.json.gz','7b9d5f6bafe69879246ee5edffbfdd280bfec0b5207c5ea6f79959fc3b61dfc4'),
 'split':('2026-11-12-tail-r42-strong-same-tau-r1-split.json.gz','b31ba4868bf825fe19981af820f92d798161df027519992b9380a4b9f7f6b5dd'),
 'density':('2026-11-12-tail-r42-strong-same-tau-r1-density.json.gz','e640e3e693ca198460de902fc8d9bb1bd909c2a7051ec099aa930a86789e0700'),
 'trace':('2026-11-12-closure-strong-true-cut-trace-r1.json','44db92699bd9bf3d8ba613465b013033c82a7ed9f8fc8e5cc1f6a003539ad494'),
 'r100':('2026-11-13-root-r100-hybrid46-exact-ledger.json','7e6b3c140c57df34ab10f17facbc624104b39fa9870a4eecfcce06bf3ea62ca9'),
}


def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def read(p):
    p=Path(p);b=p.read_bytes();return json.loads(gzip.decompress(b) if p.suffix=='.gz' else b)


def ex(v):
    if isinstance(v,list):return F(int(v[0]))*F(2)**int(v[1])
    if 'upper' in v:return ex(v['upper'])
    if 'mantissa' in v:return F(int(v['mantissa']))*F(2)**int(v['binary_exponent'])
    return F(int(v['numerator']),int(v['denominator']))


def ab(v):
    if isinstance(v,list):return arb(int(v[0]))*arb(2)**int(v[1])
    if 'upper' in v:return ab(v['upper'])
    if 'mantissa' in v:return arb(int(v['mantissa']))*arb(2)**int(v['binary_exponent'])
    return arb(int(v['numerator']))/int(v['denominator'])


def pack(v,bits=160):
    if not v.is_finite():raise ArithmeticError('Every original coefficient must stay finite')
    z=v.upper()
    if not z>=0:raise ArithmeticError('Positive comparison became negative')
    if z==0:return ['0',0]
    m,e=z.man_exp();m,e=int(m),int(e);q=max(0,m.bit_length()-bits)
    if q:m,e=(m+(1<<q)-1)>>q,e+q
    if not arb(m)*arb(2)**e>=z:raise ArithmeticError('Outward rounding went inward')
    return [str(m),e]


def up(z):return ab(pack(z))


def main():
    p=argparse.ArgumentParser(description=__doc__)
    for k in ('topic','modal-input','source-summary','source-resource','out-prefix'):
        p.add_argument('--'+k,type=Path,required=True)
    p.add_argument('--steps',type=int,default=128);p.add_argument('--rss-kib',type=int,default=98304)
    a=p.parse_args();ctx.prec=256;ctx.threads=1;started=time.monotonic()
    if a.steps<1:raise ValueError('At least one actual finite substitution required')
    out=Path(str(a.out_prefix)+'.json.gz')
    if out.exists():raise FileExistsError('Keep original full641 attempts immutable')
    sys.path.insert(0,str(a.topic/'computations'))
    from closure_split_joint_io_v2 import iter_array,metadata_without_array
    paths={k:a.topic/'notes'/v[0] for k,v in PINS.items()};ids={}
    for k,path in paths.items():
        if sha(path)!=PINS[k][1]:raise ArithmeticError('An original actual R100 input changed: '+k)
        ids[k]=dict(path=str(path),sha256=sha(path))
    for k in ('modal_input','source_summary','source_resource'):
        path=getattr(a,k);ids[k]=dict(path=str(path),sha256=sha(path))
    if ids['modal_input']['sha256']!='28161832153c4f0b3e632f4c4fba2741b9b90d198a4d75ff5761a18a72c8fa8f':raise ArithmeticError('Same all213 actual modal input required')
    if ids['source_summary']['sha256']!='403bfc43f44be9c9fa5f03ed968db7eee6165e44f137d473422c9e8481af99a3':raise ArithmeticError('Same complete all213 source required')
    modal,source,usage=read(a.modal_input),read(a.source_summary),read(a.source_resource)
    if not(modal['all_gates'] and source['all_gates'] and all(source['gates'].values()) and source['all213_original_cells']
           and source['cells']==list(range(12,225)) and usage['exitcode']==0 and usage['termination_signal'] is None):raise ArithmeticError('Complete original source run required')
    meta=metadata_without_array(paths['jacobian'],'rows');split=metadata_without_array(paths['split'],'gamma_rows')
    density=read(paths['density']);trace=read(paths['trace']);chart=read(paths['r100'])
    if not(meta['all_rows_contracting'] and meta['complete_mean_inverse_quadratic_and_true_far_retained'] and trace['all_gates'] and chart['all_gates']
           and all(density['gates'].values()) and meta['dimension']==641):raise ArithmeticError('Same existing full R100 head and complete matrices required')
    S=arb(257)/256;Theta=arb(16705)/16384;rt=arb(1)/32;KT=arb(273259958272)/395007;zstar=arb(2)**-2200
    if ex(modal['R100_envelope_scale'])!=F(257,256) or ex(modal['transverse_radius'])!=F(1,32):raise ArithmeticError('Same parameter/envelope domain required')
    W=list(map(ab,meta['metric_weights']))
    if not(len(W)==641 and all(x.is_exact() and x>0 for x in W)):raise ArithmeticError('Every original exact W coordinate required')
    M=arb_mat(641,641);seen=set();nnz=0;maxrows=arb(0)
    for row in iter_array(paths['jacobian'],'rows'):
        i=row['index']
        if i in seen:raise ArithmeticError('Duplicate original derivative row')
        seen.add(i);total=arb(0);colseen=set()
        for j,m,e in row['coefficients']:
            v=ab([m,e])
            if not(v.is_finite() and v>0 and 0<=j<641 and j not in colseen):raise ArithmeticError('Bad original positive coefficient')
            colseen.add(j);M[i,j]=Theta*v;total+=M[i,j];nnz+=1
        maxrows=max(maxrows,total.upper())
    if seen!=set(range(641)) or nnz!=275413 or not maxrows<1:raise ArithmeticError('All original complete641 derivative rows required')
    if resource.getrusage(resource.RUSAGE_SELF).ru_maxrss>a.rss_kib:raise MemoryError('Owned native positive matrix RSS guard')
    # Each parameter axis has its own true radial lift.  The shared l1
    # parameter budget is spent after the entire radial sum, by max column.
    L=arb_mat(213,40);lowmat=arb_mat(214,213)
    for n,row in enumerate(modal['rows']):
        if row['cell']!=12+n:raise ArithmeticError('Original 213 rows reordered')
        for j in range(40):L[n,j]=up(ab(row['transverse_unit_axis_pairs'][j+6])/W[n])
        for i in range(213):lowmat[i,n]=M[i,n]
        lowmat[213,n]=M[640,n]
    B=lowmat*L;b=[arb(0)]*641;bwitness=[]
    for i in range(214):
        idx=i if i<213 else 640;values=[]
        for j in range(40):
            val=B[i,j]
            if idx==640:val+=ab(modal['far_unit_axis_pairs_unscaled_by_S'][j+6])/(zstar*W[640])
            values.append(up(val*rt))
        b[idx]=max(values);bwitness.append(dict(index=idx,maximizing_axis=14+2*values.index(b[idx]),value=pack(b[idx])))
    del B,L,lowmat
    qs={g:[ab(r['source_common_mass']['common_d'][band]) for r in source['rows']]
        for g,band in (('near','near94to184'),('rest','rest186to8190'),('infinite','infinite8192up'))}
    high_constant=[];count=0
    for k,row in enumerate(iter_array(paths['split'],'gamma_rows')):
        if row['output_cell']!=12+k or len(row['sources'])!=213-k:raise ArithmeticError('Complete causal triangles required')
        sums={'near':arb(0),'rest':arb(0)}
        for n,entry in enumerate(row['sources'],k):
            if entry['source_cell']!=12+n:raise ArithmeticError('All causal source cells required')
            for group in sums:sums[group]+=S*ab(entry[group+'_gamma'])*qs[group][n]
            count+=1
        for group,offset in [('near',213),('rest',426)]:
            far=ab(split['cells'][k]['far_boundary_'+group])/S
            val=up(sums[group]+far);b[offset+k]=up(val/W[offset+k])
            high_constant.append(dict(index=offset+k,source=pack(sums[group]),true_aux_far=pack(far),complete=pack(val)))
    if count!=213*214//2:raise ArithmeticError('The entire original high source triangle is missing')
    hinf=S*ab(density['gamma_high'])*sum(qs['infinite'],arb(0));finf=ab(split['deep_high_boundary'])/S
    b[639]=up((hinf+finf)/W[639]);high_constant.append(dict(index=639,source=pack(hinf),true_aux_far=pack(finf),complete=pack(hinf+finf)))
    if not all(x.is_finite() and x>0 for x in b):raise ArithmeticError('Every affine source must be finite and positive')
    initial=up(256+KT*rt);v=arb_mat(641,1);base=arb_mat(641,1)
    for i in range(641):v[i,0]=initial;base[i,0]=b[i]
    records=[];fullvectors=[]
    def checkpoint(step):
        data=[pack(v[i,0]) for i in range(641)]
        heads=[up(v[i,0]*W[i]*S*ab(trace['true_point_epsilon_upper'])) for i in [213,426,639]]
        row=dict(step=step,head_complete_balanced_P_K_by_band=list(map(pack,heads)),
                 low12=pack(v[0,0]*W[0]),near12=pack(v[213,0]*W[213]),rest12=pack(v[426,0]*W[426]),infinite=pack(v[639,0]*W[639]),far_z_normalized=pack(v[640,0]*W[640]))
        records.append(row);fullvectors.append(dict(step=step,all641_W_scaled_caps=data))
        print(json.dumps(dict(event='same_R100_full641_finite_substitution',step=step,head_display=[str(x) for x in heads],elapsed_seconds=time.monotonic()-started,peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)),flush=True)
    checkpoint(0)
    for step in range(1,a.steps+1):
        nxt=M*v+base
        for i in range(641):
            q=up(nxt[i,0])
            if q<v[i,0]:v[i,0]=q
        if step&(step-1)==0 or step==a.steps:checkpoint(step)
        if resource.getrusage(resource.RUSAGE_SELF).ru_maxrss>a.rss_kib:raise MemoryError('Owned complete positive bootstrap RSS guard')
    gates=dict(all641_original_rows=True,all275413_actual_nonzero_entries=True,all_213_causal_sources=True,
      existing_R100_solution_only=True,same_Six_unit_and_transverse_l1_radius1over32=True,
      same_full_Theta_J_domain=True,complete_mean_inverse_far=True,pure_high_source_not_charged_JLambda_twice=True,
      low_auxiliary_source_cancelled_exactly=True,far_E_Lambda_paid_only_in_consistency_row=True,
      every_step_positive_finite_outward=True,all_caps_nonincreasing=True)
    result=dict(schema='visible-flex-same-R100-full641-finite-positive-bootstrap-v1',author='exact_closure (GPT-6 Astra Pro; AI-assisted)',all_gates=True,gates=gates,
      input_identities=ids,source_sha256=sha(__file__),helper_sha256={n:sha(a.topic/'computations'/n) for n in ['closure_split_joint_io_v2.py','closure_split_joint_io.py']},
      steps=a.steps,initial_W_scaled_radius=pack(initial),Theta=pack(Theta),maximum_Theta_Jbar_row_sum=pack(maxrows),
      same_original_metric_weights=meta['metric_weights'],affine_source_W_scaled=list(map(pack,b)),low_far_shared_axis_witnesses=bwitness,high_constant_rows=high_constant,
      point_physical_epsilon_prime=pack(S*ab(trace['true_point_epsilon_upper'])),head_strip=trace['head_strip'],
      head_bands=[[94,184],[186,8190],[8192,None]],checkpoints=records,full641_checkpoints=fullvectors,
      complete_original_field_bound=True,new_fixedpoint_claimed=False,outer_cut_or_closed_surface_claimed=False,
      finite_substitution='e <= previous and e <= b+M previous, hence e <= min(previous, b+M previous), for the same already existing exact field',
      parameter_reference='Cs+Lambda d; independent true far centre remains z_aux; e_z includes E Lambda only through consistency',
      elapsed_seconds=time.monotonic()-started,peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    raw=(json.dumps(result,separators=(',',':'))+'\n').encode();out.write_bytes(gzip.compress(raw,mtime=0))
    if out.stat().st_size>=5_000_000:raise ArithmeticError('Split full original checkpoint artifact')
    print(json.dumps(dict(all_gates=True,steps=a.steps,path=str(out),bytes=out.stat().st_size,sha256=sha(out),elapsed_seconds=result['elapsed_seconds'],peak_rss_kib=result['peak_rss_kib'])),flush=True)


if __name__=='__main__':main()
