# v2: partition only the long energy segment at eight exact original-leaf boundaries; preserve its norm state and every original frame jump across these comparison-block cuts.
#!/usr/bin/env python3
"""Actual whole-leaf three-material comparison on interval frequencies.

Author: exact_closure (GPT-6 Astra Pro; AI-assisted), 2026-11-13.
Use one fixed strip: energy frames on cell10/segment3, a Metzler comparison
elsewhere. All input columns, source origins and frame costs are retained.
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


def digest(p):
    h=hashlib.sha256()
    with Path(p).open('rb') as f:
        for x in iter(lambda:f.read(1<<20),b''):h.update(x)
    return h.hexdigest()


def rational(x):return F(int(x['numerator']),int(x['denominator']))


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    for key in ('summary','leaves','out-prefix'):
        ap.add_argument('--'+key,type=Path,required=True)
    select=ap.add_mutually_exclusive_group(required=True)
    select.add_argument('--windows')
    select.add_argument('--all-middle',action='store_true')
    ap.add_argument('--precision',type=int,default=256)
    ap.add_argument('--rss-kib',type=int,default=98304)
    a=ap.parse_args()
    from flint import arb,ctx
    if a.precision<256:raise ValueError('Retain the complete original interval precision')
    ctx.prec=a.precision;ctx.threads=1;start=time.monotonic()
    def guard():
        if resource.getrusage(resource.RUSAGE_SELF).ru_maxrss>a.rss_kib:
            raise MemoryError('Owned interval-frequency consumer exceeded its original RSS guard')
    def point(v):return arb(int(v[0]))*(arb(2)**int(v[1]))
    def upper96(v):
        if not v.is_finite() or not v>=0:raise ArithmeticError('Finite nonnegative comparison endpoint required')
        mm,ee=v.upper().man_exp();mm=int(mm);ee=int(ee);shift=max(0,abs(mm).bit_length()-96)
        if shift:mm=-((-mm)//(1<<shift));ee+=shift
        return [str(mm),ee]
    def top(v):
        v=v.upper()
        if not v.is_finite() or not v>=0:raise ArithmeticError('Positive comparison matrix lost a finite upper endpoint')
        return v
    def apply(E,v):return [top(E[i][0]*v[0]+E[i][1]*v[1]) for i in range(2)]
    def exponential(aa,bb,cc,dd,dx):
        # Exact 2x2 exponential evaluated by outward Arb arithmetic.
        mu=(aa+dd)/2;h=(aa-dd)/2;discr=h*h+bb*cc
        if discr==0:
            scale=(mu*dx).exp()
            return [[top(scale*(1+h*dx)),top(scale*bb*dx)],
                    [top(scale*cc*dx),top(scale*(1-h*dx))]]
        nu=discr.sqrt()
        if not nu>0:raise ArithmeticError('The comparison exponential radicand is not strictly positive')
        scale=(mu*dx).exp();cs=(nu*dx).cosh();sn=(nu*dx).sinh()/nu
        return [[top(scale*(cs+h*sn)),top(scale*bb*sn)],
                [top(scale*cc*sn),top(scale*(cs-h*sn))]]
    def exprel_upper(z):
        if z==0:return arb(1)
        fallback=(z if z>0 else arb(0)).exp().upper()
        candidate=(z.exp()-1)/z
        return min(fallback,candidate.upper()) if candidate.is_finite() and candidate>0 else fallback
    meta=json.loads(a.summary.read_text())
    if not meta['all_coefficient_gates'] or meta['original_panels']!=10793:
        raise ValueError('The complete actual shared coefficient stream is required')
    if digest(a.leaves)!=meta['leaf_file']['sha256']:raise ValueError('The complete shared leaf stream changed')
    selection=[[10,3]]
    case=next(r for r in meta['phase_cases'] if r['energy_groups']==selection)
    if not case['terminal_strictly_above_one_over64'] or not rational(case['terminal_strip'])>F(1,64):
        raise ValueError('The fixed whole-domain analytic strip is unpaid')
    if a.all_middle:
        windows=[]
        for first,last in ((94,184),(186,5758)):
            lo=first
            while lo<=last:
                hi=min(last,2*((lo*33)//64))
                windows.append((lo,hi));lo=hi+2
    else:
        windows=[tuple(map(int,item.split(':'))) for item in a.windows.split(',')]
    if not windows or len(set(windows))!=len(windows) or any(lo<94 or hi>5758 or lo%2 or hi%2 or lo>hi or F(hi,lo)>F(33,32) or (lo<=184<hi) for lo,hi in windows):
        raise ValueError('Each distinct complete window must obey the same fixed ratio and one true head band')
    cover=[m for lo,hi in windows for m in range(lo,hi+1,2)]
    all_middle=cover==list(range(94,5759,2))
    output=Path(str(a.out_prefix)+'-windows.jsonl.gz');summary=Path(str(a.out_prefix)+'.json')
    if output.exists() or summary.exists():raise FileExistsError('Fresh window output required')
    order=[(n,j) for n in (11,10) for j in range(9)]
    blocks=[]
    for original_group,g in enumerate(meta['groups']):
        pieces=8 if original_group==12 else 1
        edges=[k*g['panels']//pieces for k in range(pieces+1)]
        for k in range(pieces):
            blocks.append(dict(original_group=original_group,cell=g['cell'],segment=g['segment'],
                               first_panel=edges[k],last_panel_exclusive=edges[k+1],
                               panels=edges[k+1]-edges[k]))
    block_for={(g['original_group'],j):i for i,g in enumerate(blocks)
               for j in range(g['first_panel'],g['last_panel_exclusive'])}
    if len(block_for)!=10793 or len(blocks)!=25:raise ValueError('The exact25-block comparison partition is incomplete')
    completed=[];winmax=[]
    with output.open('wb') as raw:
      with gzip.GzipFile(filename='',mode='wb',fileobj=raw,mtime=0,compresslevel=9) as packed:
        for wi,(lo,hi) in enumerate(windows):
            began=time.monotonic();rho=arb(33)/32
            states=[[arb(1),arb(0)],[arb(0),arb(1)]]
            scalar=None;previous_b=None;current_group=-1;count=0;in_group=0;rows=[]
            entry_count=exit_count=jump_count=0;vmax=arb(0)
            def finish_group():
                if current_group<0:return
                expected=blocks[current_group]
                if in_group!=expected['panels']:raise ValueError('An original target group lacks leaves')
                sources=[]
                for src in range(current_group+1):
                    mats=[]
                    for pi,power in enumerate((2,1,0)):
                        z=maxima[2+3*src+pi]
                        mats.append(dict(V_power=power,P_sup=upper96((1+hi)*z[0]),
                            K_sup=upper96((1+hi)*z[1]),
                            localV_strong_output_row=upper96((1+hi)*(z[0]+z[1]))))
                    sources.append(dict(source_cell=blocks[src]['cell'],source_segment=blocks[src]['segment'],
                        source_comparison_block=src,first_panel=blocks[src]['first_panel'],
                        last_panel_exclusive=blocks[src]['last_panel_exclusive'],density_rows=mats))
                rows.append(dict(target_cell=expected['cell'],target_segment=expected['segment'],
                    comparison_block=current_group,first_panel=expected['first_panel'],
                    last_panel_exclusive=expected['last_panel_exclusive'],
                    original_panels=in_group,V_max=upper96(vmax),
                    initial_localV_separate_component_sups=[[upper96(v) for v in pair] for pair in maxima[:2]],
                    source_rows=sources))
            with gzip.open(a.leaves,'rt') as stream:
              for line in stream:
                r=json.loads(line);original_gi=r['group'];gi=block_for[(original_gi,r['panel'])]
                if gi!=current_group:
                    finish_group()
                    if gi!=current_group+1:raise ValueError('The source groups are not consecutive')
                    was_energy=current_group>=0 and blocks[current_group]['original_group']==12
                    if was_energy and original_gi!=12:exit_count+=1
                    current_group=gi;in_group=0;vmax=arb(0)
                    states.extend([[arb(0),arb(0)] for _ in range(3)])
                    maxima=[[arb(0),arb(0)] for _ in states]
                    if original_gi==12 and was_energy:
                        if scalar is None:raise ValueError('Do not reset the energy norm at a comparison-block cut')
                        scalar.extend([arb(0),arb(0),arb(0)])
                    else:
                        scalar=None;previous_b=None
                        if original_gi==12:entry_count+=1
                if (r['cell'],r['segment'])!=order[original_gi] or r['panel']!=blocks[gi]['first_panel']+in_group:
                    raise ValueError('A true source leaf was skipped or reordered')
                dx=arb(int(r['dx'][0]))/arb(int(r['dx'][1]));V=point(r['V'])
                if not dx>0 or not V>0:raise ArithmeticError('Positive exact leaf width and V required')
                vp=[V*V,V,arb(1)];c=point(r['c_upper']);vmax=max(vmax,V)
                energy=original_gi==12
                if energy:
                    b=point(r['b']);rate=point(r['q_energy'])
                    alpha=max(point(r['a_upper']),point(r['d_upper']))+(hi-lo*rho)*rate
                    z=(alpha*dx).upper();growth=z.exp().upper();psi=exprel_upper(z)
                    if scalar is None:
                        scalar=[top((v[0]*v[0]+(v[1]/b)**2).sqrt()) for v in states]
                    else:
                        jump=max(arb(1),(previous_b/b).upper())
                        scalar=[top(v*jump) for v in scalar];jump_count+=1
                    nextscalar=[];whole=[]
                    for ix,q0 in enumerate(scalar):
                        forcing=(c*vp[ix-(2+3*gi)]/b).upper() if ix>=2+3*gi else arb(0)
                        qend=top(growth*q0+forcing*dx*psi);qwhole=max(q0,qend)
                        nextscalar.append(qend);whole.append([qwhole,top(b*qwhole)])
                    scalar=nextscalar;previous_b=b
                    states=[[q,top(b*q)] for q in scalar]
                else:
                    rate=point(r['q_Metzler'])
                    aa=point(r['a_upper'])-lo*rho*rate;dd=point(r['d_upper'])-lo*rho*rate
                    bb=hi*point(r['s_upper']);cc=hi*point(r['abs_ell_upper'])
                    E=exponential(aa,bb,cc,dd,dx)
                    Ep=exponential(max(arb(0),aa.upper()),bb,cc,max(arb(0),dd.upper()),dx)
                    nextstates=[];whole=[]
                    for ix,v in enumerate(states):
                        end=apply(E,v);full=apply(Ep,v)
                        if ix>=2+3*gi:
                            force=top(c*vp[ix-(2+3*gi)]*dx)
                            add=[top(Ep[k][1]*force) for k in range(2)]
                            end=[top(end[k]+add[k]) for k in range(2)]
                            full=[top(full[k]+add[k]) for k in range(2)]
                        nextstates.append(end);whole.append(full)
                    states=nextstates
                for ix,pair in enumerate(whole):
                    for k,v in enumerate(pair):maxima[ix][k]=max(maxima[ix][k],(v/V).upper())
                in_group+=1;count+=1
                if count%64==0:guard()
            finish_group()
            if count!=10793 or len(rows)!=25 or entry_count!=1 or exit_count!=1 or jump_count!=1804:
                raise ArithmeticError('Full source, whole-target or exact energy-interface costs are incomplete')
            record=dict(window=[lo,hi],head_band='near' if hi<=184 else 'rest',
                actual_mode_count=(hi-lo)//2+1,ratio_condition_exact=True,all10793_original_leaves=True,
                all18_original_source_segments_retained=True,comparison_source_origins=25,
                entry_count=entry_count,exit_count=exit_count,frame_jump_count=jump_count,
                both_initial_columns_retained=True,all3_source_materials=True,whole_leaf_targets_before_sup=True,
                source_units='c_bg V_I^p weak Fourier density in the same fixed variable strip',
                output_units='local-V strong Fourier norm in that fixed variable strip; source angular factor1+m_hi paid once',
                rows=rows,elapsed_seconds=time.monotonic()-began)
            packed.write((json.dumps(record,separators=(',',':'))+'\n').encode());packed.flush()
            completed.append([lo,hi]);winmax.append(dict(window=[lo,hi],elapsed_seconds=record['elapsed_seconds']))
            print(json.dumps(dict(event='complete_actual_frequency_window',window=[lo,hi],windows_completed=len(completed),
                                 original_leaves=count,elapsed_seconds=record['elapsed_seconds'],
                                 peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)),flush=True)
    if output.stat().st_size>=5_000_000:raise ArithmeticError('Partition the same completed windows before repository archival')
    result=dict(schema='visible-flex-hybrid-middle-interval-windows-v1',
        author='exact_closure (GPT-6 Astra Pro; AI-assisted)',status='Actual completed whole-leaf interval-frequency linear comparison',
        all_enclosure_gates=True,windows=completed,all_middle_modes94_to5758_paid=all_middle,
        selected_mode_count=len(cover),same_fixed_strip=case,energy_groups=selection,
        source_powers=[2,1,0],original_leaf_count_per_window=10793,original_source_groups=18,
        comparison_source_blocks=25,energy_segment_subblocks=8,comparison_partition=blocks,
        original_window_counts=winmax,primary=dict(path=str(output),bytes=output.stat().st_size,sha256=digest(output)),
        input_hashes={str(a.summary):digest(a.summary),str(a.leaves):digest(a.leaves)},
        source_sha256=digest(__file__),precision=a.precision,nonlinear_fixed_point_claimed=False,
        coupled_low_high_or_cut_claimed=False,elapsed_seconds=time.monotonic()-start,
        peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    guard();summary.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(dict(event='complete_actual_hybrid_windows',windows=len(completed),all_middle_modes=all_middle,
                         elapsed_seconds=result['elapsed_seconds'],peak_rss_kib=result['peak_rss_kib'])),flush=True)


if __name__=='__main__':main()
