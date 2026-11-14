#!/usr/bin/env python3
"""Actual all213 Cs+Lambda DQ two-material frequency-window coefficients.

The same accepted R100 inner auxiliary/lift family and original continuous
strip are used. Each input window has one shared strong Fourier mass. This
constructs source coefficients only; no ODE, Green solve, full nonlinear
bootstrap, contraction, true-cut consistency or surface theorem is claimed.
"""
from __future__ import annotations
import argparse
from fractions import Fraction as Q
import gzip
import hashlib
import io
import json
from pathlib import Path
import resource
import sys
import time
from flint import arb,ctx

INPUT_SHA='0816e8e7d62bb5df1df58848dfe8ab1c9a3699210f5df9b9da7e5e31e6a18d93'
DENSITY_SHA='e640e3e693ca198460de902fc8d9bb1bd909c2a7051ec099aa930a86789e0700'
MODES=list(range(2,93,2))
OUTPUT_WINDOWS=[[94,94],[96,96],[98,104],[106,112],[114,128],[130,184],
    [186,192],[194,256],[258,512],[514,1024],[1026,2048],[2050,4096],[4098,8190]]
INPUT_WINDOWS=[[2,92]]+OUTPUT_WINDOWS+[[8192,None]]

def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def read(p):
    p=Path(p)
    if p.suffix=='.gz':
        with gzip.open(p,'rt') as stream:return json.load(stream)
    return json.loads(p.read_text())
def fraction(v,side='lower'):
    if isinstance(v,list):return Q(int(v[0]))*Q(2)**int(v[1])
    if side in v:return fraction(v[side],side)
    if 'mantissa' in v:return Q(int(v['mantissa']))*Q(2)**int(v['binary_exponent'])
    return Q(int(v['numerator']),int(v['denominator']))
def ab(v):
    if isinstance(v,Q):return arb(v.numerator)/v.denominator
    if isinstance(v,list):return arb(int(v[0]))*arb(2)**int(v[1])
    return ab(fraction(v))
def pack(value,bits=160):
    z=value.upper()
    if not z.is_finite() or not z>=0:raise ArithmeticError('Finite positive coefficient required')
    if z==0:return ['0',0]
    m,e=z.man_exp();m,e=int(m),int(e);drop=max(0,m.bit_length()-bits)
    if drop:m,e=(m+(1<<drop)-1)>>drop,e+drop
    out=[str(m),e]
    if not ab(out)>=z:raise ArithmeticError('Coefficient rounded inward')
    return out
def ranges(window,n):
    lo,hi=window
    a,b=max(2,lo-n),min(92,hi-n)
    plus=None if a>b else (a//2-1,b//2)
    a,b=max(2,n-hi),min(92,n-lo)
    minus=None if a>b else (a//2-1,b//2)
    return plus,minus
def membership(window,n):
    lo,hi=window
    return tuple((lo<=k+n<=hi,lo<=abs(k-n)<=hi) for k in MODES)
def partitions(check):
    out=[];total=0
    for wi,window in enumerate(OUTPUT_WINDOWS):
        row=[]
        for ji,input_window in enumerate(INPUT_WINDOWS):
            left=input_window[0];right=min(input_window[1] if input_window[1] is not None else window[1]+92,window[1]+92)
            if right<left:
                row.append(dict(output_index=wi,input_index=ji,intervals=[],candidate_modes=[],strict_zero=True,
                    zero_reason='Every input mode exceeds output_max+maximum_center_mode.'));continue
            points={left,right+2}
            for k in MODES:
                for x in (window[0]-k,window[1]-k+2,window[0]+k,window[1]+k+2):
                    if left<x<right+2:points.add(x)
            points=sorted(points);intervals=[];candidates=set()
            for first,last in zip(points[:-1],points[1:]):
                last-=2
                check('membership_'+str(wi)+'_'+str(ji)+'_'+str(first),
                      first%2==last%2==0 and first<=last and membership(window,first)==membership(window,last))
                intervals.append([first,last]);candidates.update((first,last));total+=1
            check('partition_'+str(wi)+'_'+str(ji),intervals[0][0]==left and intervals[-1][1]==right and
                all(a[1]+2==b[0] for a,b in zip(intervals[:-1],intervals[1:])))
            row.append(dict(output_index=wi,input_index=ji,intervals=intervals,candidate_modes=sorted(candidates),
                strict_zero=not any(any(a or b for a,b in membership(window,n)) for n in candidates),
                modes_above_output_max_plus92_have_exactly_zero_coefficient=True))
        out.append(row)
    return out,total
def interval_sums(weights):
    result={}
    for i in range(len(weights)):
        total=[arb(0) for _ in range(4)]
        for j in range(i,len(weights)):
            total=[(a+b).upper() for a,b in zip(total,weights[j])]
            result[i,j+1]=tuple(total)
    return result

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    for k in ('input','input-resource','density','out'):ap.add_argument('--'+k,type=Path,required=True)
    ap.add_argument('--rss-kib',type=int,default=98304)
    a=ap.parse_args();started=time.monotonic();ctx.prec=256;ctx.threads=1
    if a.out.exists():raise FileExistsError(a.out)
    gates={}
    def check(name,value):
        if not value:raise ArithmeticError(name)
        gates[name]=True
    check('pinned_improved_actual_input',sha(a.input)==INPUT_SHA)
    check('pinned_original_true_density',sha(a.density)==DENSITY_SHA)
    source=read(a.input);density=read(a.density);usage=read(a.input_resource)
    check('completed_same_R100_actual_input',source['all_gates'] and all(source['gates'].values()) and
          source['canonical_bootstrap_applied'] and source['schema']=='inner-r100-Cs-Lambda-modal-input-v1' and
          source['modes']==MODES and source['cells']==list(range(12,225)) and
          fraction(source['R100_envelope_scale'])==Q(257,256) and fraction(source['transverse_radius'])==Q(1,32) and
          usage['exitcode']==0 and usage['termination_signal'] is None)
    check('original_B_and_continuous_strip',all(density['gates'].values()) and
          source['input_identities']['density']['sha256']==DENSITY_SHA and
          source['exact_original_continuous_strip_origin']['do_not_renormalize_using_new_strong_density'])
    compact=[]
    for index,(r,d) in enumerate(zip(source['rows'],density['rows'])):
        cell=index+12;B=fraction(d['B']);B0=B.numerator//B.denominator;tau=fraction(r['tau_outer_lower'])
        check('same_cell_B_strip_'+str(cell),r['cell']==d['cell']==cell and B0>=120 and
              tau==fraction(d['tau_outer']) and tau>0 and len(r['Cs_plus_Lambda_pair_caps'])==46)
        check('ell_coefficient_exact_reduction_'+str(cell),5*92<=4*B0 and 10*(B0-92)>=1)
        compact.append(dict(cell=cell,B_floor=B0,tau=tau,caps=r['Cs_plus_Lambda_pair_caps'],
            common_cap=r['Cs_plus_Lambda_common_cap']))
    check('all213_rows_retained',len(compact)==213)
    normalization=source['normalization'];domain=source['parameter_domain'];origin=source['exact_original_continuous_strip_origin']
    del source,density
    check('complete_output_window_cover',OUTPUT_WINDOWS[0][0]==94 and OUTPUT_WINDOWS[-1][1]==8190 and
        all(a[1]+2==b[0] for a,b in zip(OUTPUT_WINDOWS[:-1],OUTPUT_WINDOWS[1:])))
    check('complete_input_window_cover',INPUT_WINDOWS[0][0]==2 and INPUT_WINDOWS[-1]==[8192,None] and
        all(a[1]+2==b[0] for a,b in zip(INPUT_WINDOWS[:-1],INPUT_WINDOWS[1:])))
    partition,count=partitions(check)
    rows=[];max_rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    for item in compact:
        cell,B0,tau=item['cell'],item['B_floor'],item['tau'];caps=list(map(ab,item['caps']))
        check('positive_full_reference_caps_'+str(cell),all(c>0 for c in caps))
        decay=[(-2*k*ab(tau)).exp().upper() for k in MODES]
        weights=[]
        for k,c,e in zip(MODES,caps,decay):
            w=(c/(1+k)).upper();weights.append((w,(w*k).upper(),(w*e).upper(),(w*k*e).upper()))
        sums=interval_sums(weights);ks=[];ke=[];ns=[];ne=[]
        for wi,window in enumerate(OUTPUT_WINDOWS):
            rs=[];re=[];rns=[];rne=[]
            for ji,part in enumerate(partition[wi]):
                bests=arb(0);beste=arb(0);at_s=None;at_e=None
                for n in part['candidate_modes']:
                    plus,minus=ranges(window,n);s0=arb(0);s1=arb(0)
                    if plus:s0+=sums[plus][0];s1+=sums[plus][1]
                    if minus:s0+=sums[minus][2];s1+=sums[minus][3]
                    gs=(arb(5*n)*s1/(4*(1+n))).upper()
                    ge=(s0/(1+n) if 5*n<=4*B0 else s0*(5*n)/(4*B0*(1+n))).upper()
                    if gs>bests:bests=gs;at_s=n
                    if ge>beste:beste=ge;at_e=n
                check('exact_zero_support_'+str(cell)+'_'+str(wi)+'_'+str(ji),
                      (bests==0 and beste==0)==part['strict_zero'])
                rs.append(pack(bests));re.append(pack(beste));rns.append(at_s);rne.append(at_e)
            ks.append(rs);ke.append(re);ns.append(rns);ne.append(rne)
        rows.append(dict(cell=cell,B_floor=B0,tau_outer_lower=dict(numerator=str(tau.numerator),denominator=str(tau.denominator)),
            reference_strong_pair_caps=item['caps'],reference_common_cap=item['common_cap'],
            difference_weight_upper=list(map(pack,decay)),kernels_s_upper=ks,kernels_ell_upper=ke,
            maximizing_candidate_mode_s=ns,maximizing_candidate_mode_ell=ne))
        max_rss=max(max_rss,resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
        if max_rss>a.rss_kib:raise MemoryError('Actual all213 DQ window RSS exceeded owned guard')
        if (cell-11)%24==0 or cell==224:
            print(json.dumps(dict(event='complete_true_DQ_cell',cell=cell,completed=cell-11,total=213,
                elapsed=time.monotonic()-started,peak_rss_kib=max_rss)),flush=True)
    # Keep the verbose per-cell support gates in the certificate, while all
    # giant original numerical sources remain at their immutable input paths.
    output=dict(schema='inner-CsLambda-DQ-two-material-window-kernels-v1',scope=__doc__,
        author='geometry_audit (GPT-6 Astra Pro; AI-assisted)',source_sha256=sha(__file__),
        input_identities={k:dict(path=str(getattr(a,k.replace('-','_'))),sha256=sha(getattr(a,k.replace('-','_'))))
                          for k in ('input','input-resource','density')},
        all_gates=True,gates=gates,modes_center=MODES,cells=list(range(12,225)),
        windows_out=OUTPUT_WINDOWS,windows_in=INPUT_WINDOWS,rows=rows,
        parameter_domain=domain,normalization=normalization,original_continuous_strip_origin=origin,
        source_material_units='Original s and abs(ell) materials for the same physical strong (B*p,kappa)/V_prime fields. Output is weak Fourier source mass, with no output 1+m factor.',
        operator_contract='For each cell and output window w, source_mass_material[w] <= sum_j kernels_material_upper[w][j] * input_shared_strong_mass[j]. Each input mass is the sum of its signed-pair strong Fourier masses, not a per-mode supremum.',
        unreduced_coefficients=dict(s='5*k*n/(4*(1+k)*(1+n))',
            ell='max(1,5*k/(4*B0),5*n/(4*B0),(5*k*n+1)/(4*B0^2))/((1+k)*(1+n))'),
        exact_ell_reduction='Since B0>=120 and k<=92, the numerator equals max(1,5*n/(4*B0)); the other two entries are bounded by these for all n>=2.',
        positive_sum_difference_formula='sum_k c_k beta(k,n) [1_{k+n in w}+exp(-2*min(k,n)*tau_outer_lower) 1_{abs(k-n) in w}]. For every nonzero difference contribution here n>k, so min(k,n)=k.',
        membership_partition=partition,membership_intervals=count,
        endpoint_maximization_proof='Membership is constant on each saved even-frequency interval. The s coefficient is increasing in n; the ell coefficient is a positive constant times max(t,5*(1-t)/(4*B0)), t=1/(1+n), a convex function. Both maxima are attained at an interval endpoint. Beyond output_max+92 both indicators vanish exactly.',
        no_input_window_mode_count_multiplier=True,all_reference_positive_modes_retained=True,
        no_shared_Lambda_mass_replaced_by_pointwise_mass=True,
        full_mean_inverse_remainder_or_unknown_quadratic_not_in_this_DQ_kernel=True,
        radial_integrations=0,ODE_Node_Green_calls=0,new_fixedpoint_or_truecut_or_surface_claimed=False,
        precision_bits=ctx.prec,coefficient_storage_significant_bits=160,
        elapsed_seconds=time.monotonic()-started,peak_rss_kib=max_rss,command=sys.argv)
    a.out.parent.mkdir(parents=True,exist_ok=True)
    with a.out.open('xb') as stream:
        with gzip.GzipFile(filename='',mode='wb',fileobj=stream,compresslevel=9,mtime=0) as zipped:
            with io.TextIOWrapper(zipped,encoding='utf-8') as text:
                json.dump(output,text,separators=(',',':'));text.write('\n')
    if a.out.stat().st_size>=5_000_000:raise ArithmeticError('Complete kernel primary exceeds strict file cap')
    if resource.getrusage(resource.RUSAGE_SELF).ru_maxrss>a.rss_kib:
        raise MemoryError('Actual all213 DQ output serialization exceeded owned RSS guard')
    print(json.dumps(dict(out=str(a.out),sha256=sha(a.out),bytes=a.out.stat().st_size,gates=len(gates),all_gates=True,
        rows=len(rows),kernel_shape=[213,2,13,15],membership_intervals=count,
        elapsed=output['elapsed_seconds'],peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)),flush=True)

if __name__=='__main__':main()
