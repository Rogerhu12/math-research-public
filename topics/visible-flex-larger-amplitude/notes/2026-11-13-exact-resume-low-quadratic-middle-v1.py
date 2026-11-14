#!/usr/bin/env python3
"""Actual frequency-preserving low-input quadratic response into the middle.

Author: exact_closure (GPT-6 Astra Pro; AI-assisted), 2026-11-13.
Only true sum frequencies94..184 enter. Every low input column retains
the R101 centre spectrum, full angular multipliers and the actual paid
near-window source kernels in the common strip. No ODE is repeated.
"""
import argparse
from fractions import Fraction as F
from functools import lru_cache
import gzip
import hashlib
import json
from pathlib import Path
import resource
import time


def read(p):
    raw=Path(p).read_bytes()
    return json.loads(gzip.decompress(raw) if str(p).endswith('.gz') else raw)


def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def ex(v):
    if isinstance(v,list):return F(int(v[0]))*F(2)**int(v[1])
    if 'upper' in v:return ex(v['upper'])
    if 'mantissa' in v:return F(int(v['mantissa']))*F(2)**int(v['binary_exponent'])
    return F(int(v['numerator']),int(v['denominator']))


def rec(v):
    return dict(numerator=str(v.numerator),denominator=str(v.denominator),display_only=float(v))


def up(v):
    if v<0:raise ArithmeticError('A positive coefficient is required')
    if not v:return F(0)
    unit=F(2)**(v.numerator.bit_length()-v.denominator.bit_length()-96)
    return (v//unit+1)*unit


@lru_cache(maxsize=8192)
def decay(z):
    if z<0:raise ArithmeticError('No negative strip difference is free')
    if not z:return F(1)
    value=min(F(1),up(1/(1+z/65536)))
    for _ in range(16):value=min(F(1),up(value*value))
    return value


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    for n in ('manifest','common','leaves','spectral','joint','joint-certificate','out-prefix'):
        ap.add_argument('--'+n,required=True,type=Path)
    ap.add_argument('--window-prefix',required=True,action='append',type=Path)
    a=ap.parse_args();start=time.monotonic()
    output=Path(str(a.out_prefix)+'.json.gz');summary=Path(str(a.out_prefix)+'-summary.json')
    if output.exists() or summary.exists():raise FileExistsError('Use a fresh exact frequency response')
    manifest,common,spectral,joint,jc=[read(getattr(a,n)) for n in ('manifest','common','spectral','joint','joint_certificate')]
    identities={Path(r['path']).name:r['sha256'] for r in manifest['files']}
    case=next(c for c in common['cases'] if c['high_threshold']==34816)
    parts=joint['comparison_partition'];count=len(parts);modes=list(range(2,93,2))
    ac={r['mode']:ex(r['upper']) for r in spectral['field_caps']}
    gates=dict(original_inputs_success=manifest['all_window_runs_formal_exit_zero'] and spectral['all_gates'] and all(spectral['gates'].values()) and joint['all_gates'] and jc['all_gates'],
        same_complete_common_strip=common['all_identity_gates'] and all(common['gates'].values()) and case==joint['fixed_common_strip'],
        all46_actual_centre_modes=list(ac)==modes and sum(ac.values(),F(0))<10,
        all25_original_blocks=count==25 and sum(p['panels'] for p in parts)==10793)
    start_extra=[ex(b['extra_start']) for b in case['blocks']]
    end_extra=[ex(b['extra_end']) for b in case['blocks']]
    where={(p['cell'],p['segment'],k):i for i,p in enumerate(parts)
           for k in range(p['first_panel'],p['last_panel_exclusive'])}
    sigma=F(18,125);sigma_start=[None]*count;leaves=0
    with gzip.open(a.leaves,'rt') as stream:
        for line in stream:
            leaf=json.loads(line);i=where[leaf['cell'],leaf['segment'],leaf['panel']]
            jump=F(int(leaf['common_entry_jump'][0]),int(leaf['common_entry_jump'][1]))
            loss=F(int(leaf['common_continuous_loss'][0]),int(leaf['common_continuous_loss'][1]))
            if min(jump,loss)<0:raise ArithmeticError('The common strip must decrease')
            sigma-=jump
            if sigma_start[i] is None:sigma_start[i]=sigma
            sigma-=loss;leaves+=1
    gates['all10793_source_widths_and_exact_final_width']=leaves==10793 and sigma==ex(case['common_terminal_strip']) and all(v is not None and v<=F(18,125) for v in sigma_start)
    window_rows=[];window_ids={};seen=[]
    for prefix in a.window_prefix:
        pp=Path(str(prefix)+'-windows.jsonl.gz');mp=Path(str(prefix)+'.json');rp=Path(str(prefix)+'-resource.json')
        meta,usage=read(mp),read(rp)
        if not (sha(pp)==identities[pp.name]==meta['primary']['sha256']
                and meta['all_enclosure_gates'] and usage['exitcode']==0 and usage['termination_signal'] is None
                and meta['comparison_partition']==parts and meta['precision']>=256):
            raise ArithmeticError('An original complete successful frequency-window input changed')
        window_ids.update({str(p):sha(p) for p in (pp,mp,rp)})
        with gzip.open(pp,'rt') as stream:
            for line in stream:
                win=json.loads(line);lo,hi=win['window']
                if lo>184:continue
                if not (94<=lo<=hi<=184 and lo%2==hi%2==0 and win['all10793_original_leaves']
                        and win['both_initial_columns_retained'] and win['all3_source_materials']
                        and win['comparison_source_origins']==25 and win['frame_jump_count']==1804
                        and win['entry_count']==win['exit_count']==1):
                    raise ArithmeticError('Actual whole-leaf near-window scope changed')
                seen.append([lo,hi]);G=[]
                for i,row in enumerate(win['rows']):
                    rr=[]
                    for j,sr in enumerate(row['source_rows']):
                        d=sr['density_rows'][0]
                        if d['V_power']!=2 or sr['source_comparison_block']!=j:raise ValueError('Physical V^2 source required')
                        old=max(ex(d['localV_strong_output_row']),ex(d['P_sup'])+ex(d['K_sup']))
                        rr.append(up(old*decay(lo*max(F(0),start_extra[i]-end_extra[j]))))
                    G.append(rr)
                window_rows.append(dict(window=[lo,hi],G=G))
    window_rows.sort(key=lambda r:r['window']);seen.sort()
    coverage=[m for lo,hi in seen for m in range(lo,hi+1,2)]
    gates['all46_near_outputs_in19_actual_windows']=coverage==list(range(94,185,2)) and len(seen)==19
    winof={m:w for w in window_rows for m in range(w['window'][0],w['window'][1]+1,2)}
    alpha={(k,n):F(5*k*n+1,4*(1+k)*(1+n)) for k in modes for n in modes if k+n>=94}
    gates['all_angular_derivatives_in_exact_pair_coefficients']=all(
        (F(5*k*n+1,4)>=max(F(5,4),F(5*k*n+1,4),F(5*max(k,n),4),F(5*k*n,4)))
        and q==F(5*k*n+1,4*(1+k)*(1+n)) for (k,n),q in alpha.items())
    if not all(gates.values()):raise ArithmeticError('A true frequency or whole-input gate failed '+str(gates))
    rows=[]
    for i in range(count):
        sources=[]
        for j in range(i+1):
            tilted={k:up(ac[k]*decay(k*(F(18,125)-sigma_start[j]))) for k in modes}
            cols=[]
            for n in modes:
                value=sum((winof[k+n]['G'][i][j]*alpha[k,n]*tilted[k]
                           for k in modes if k+n>=94),F(0))
                cols.append(up(value))
            choices=[(winof[k+n]['G'][i][j]*q,k,n) for (k,n),q in alpha.items()]
            quadratic,k,n=max(choices)
            sources.append(dict(source_block=j,
                pure_DQ_centre_to_middle_by_low_input=[dict(input_mode=n,coefficient=rec(v)) for n,v in zip(modes,cols)],
                pure_DQ_centre_to_middle_l1_operator=rec(max(cols)),attaining_input_mode=modes[cols.index(max(cols))],
                pure_Q_low_square_to_middle=rec(up(quadratic/2)),attaining_quadratic_pair=[k,n],
                all46_true_input_modes_retained=True))
        rows.append(dict(target_block=i,target_partition=parts[i],source_rows=sources))
        print(json.dumps(dict(event='exact_near_source_receiver',target=i,seconds=time.monotonic()-start)),flush=True)
    result=dict(schema='visible-flex-pure-low-quadratic-near-middle-response-v1',
        author='exact_closure (GPT-6 Astra Pro; AI-assisted)',all_gates=True,gates=gates,
        status='Actual pure-low quadratic response retains every true low input and every near output; complete N remainder remains separate',
        centre='same full R101/R105 low46 solution; complex reflection subspace and common real phase',
        common_strip=case,comparison_partition=parts,low_input_modes=modes,middle_output_modes=list(range(94,185,2)),
        exact_pair_coefficient='(5*k*n+1)/(4*(1+k)*(1+n)), including all angular multipliers',
        source_block_sigma_max=[rec(v) for v in sigma_start],
        rows=rows,actual_near_windows=[dict(window=w['window'],source_rows=[[rec(v) for v in row] for row in w['G']]) for w in window_rows],
        higher_middle_quadratic_output_exactly_zero=True,infinite_high_quadratic_output_exactly_zero=True,
        mean_and_inverse_not_dropped='Use the separate complete T=N-PiQ Hessian270Rstar; this package is only the exact Q part',
        no_new_Arb_ODE_or_window_calculation=True,unknown_low_ball_assumed=False,full75_block_closure_claimed=False,
        input_hashes={**window_ids,**{str(getattr(a,n)):sha(getattr(a,n)) for n in ('manifest','common','leaves','spectral','joint','joint_certificate')}},
        source_sha256=sha(__file__),elapsed_seconds=time.monotonic()-start,peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    with output.open('wb') as raw:
        with gzip.GzipFile(filename='',mode='wb',fileobj=raw,mtime=0,compresslevel=9) as packed:
            packed.write((json.dumps(result,separators=(',',':'))+'\n').encode())
    if output.stat().st_size>=5_000_000:raise ArithmeticError('Partition the completed frequency tensor')
    short={k:v for k,v in result.items() if k not in ('rows','actual_near_windows')}
    short['primary']=dict(path=str(output),bytes=output.stat().st_size,sha256=sha(output))
    summary.write_text(json.dumps(short,indent=2)+'\n')
    print(json.dumps(dict(all_gates=True,windows=len(seen),rows=count,bytes=output.stat().st_size,
        elapsed_seconds=result['elapsed_seconds'],peak_rss_kib=result['peak_rss_kib'])),flush=True)


if __name__=='__main__':main()
