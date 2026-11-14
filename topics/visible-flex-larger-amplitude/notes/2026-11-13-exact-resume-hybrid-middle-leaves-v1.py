#!/usr/bin/env python3
"""Same true leaves for a mixed Metzler/energy finite-mode comparison.

Author: exact_closure (GPT-6 Astra Pro; AI-assisted), 2026-11-13.
This produces whole-leaf coefficient upper bounds and exact strip budgets,
not a new nonlinear solution. All original source/frame inputs remain fixed.
"""
import argparse
from fractions import Fraction as F
import gzip
import hashlib
import json
from pathlib import Path
import re
import resource
import sys
import time


def digest(p):
    h=hashlib.sha256()
    with Path(p).open('rb') as f:
        for b in iter(lambda:f.read(1<<20),b''): h.update(b)
    return h.hexdigest()


def frac(v):
    return F(int(v[0]))*F(2)**int(v[1])


def rec(v):
    return dict(numerator=str(v.numerator),denominator=str(v.denominator),display_only=float(v))


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    for key in ('computations','primary','frame','out-prefix'):
        ap.add_argument('--'+key,type=Path,required=True)
    ap.add_argument('--precision',type=int,default=256)
    ap.add_argument('--rss-kib',type=int,default=98304)
    a=ap.parse_args()
    if a.precision<256: raise ValueError('Retain the paid input interval precision')
    sys.path.insert(0,str(a.computations))
    from flint import arb,ctx
    from closure_outer_whole_field_profiles import derivative_density
    from closure_taylor_cut_slope_v2 import ball
    from closure_real_head_source_enclosure import exact_q,power2
    from closure_split_joint_io_v2 import iter_array
    ctx.prec=a.precision;ctx.threads=1;start=time.monotonic()
    def guard():
        if resource.getrusage(resource.RUSAGE_SELF).ru_maxrss>a.rss_kib:
            raise MemoryError('Owned coefficient producer exceeded its original RSS guard')
    def upper96(v):
        if not v.is_finite(): raise ArithmeticError('Finite real endpoint required')
        mm,ee=v.upper().man_exp();mm=int(mm);ee=int(ee)
        shift=max(0,abs(mm).bit_length()-96)
        if shift: mm=-((-mm)//(1<<shift));ee+=shift
        return [str(mm),ee]
    def point(v): return arb(int(v[0]))*power2(int(v[1]))
    raw=a.primary.read_bytes()
    if a.primary.suffix=='.gz':raw=gzip.decompress(raw)
    if hashlib.sha256(raw).hexdigest()!='9e28fcf3ea53003e16ec8720a2fd4c52da0d16a40c8a90398c0b847d0f2fc317':
        raise ValueError('Use the complete fresh actual R104 source identity')
    primary=json.loads(raw);del raw
    if not primary['all_enclosure_gates'] or not all(primary['enclosure_gates'].values()):
        raise ValueError('The original source and complete true coverage must be paid')
    if digest(a.frame)!='e726b2006b27c84ac61d73e0d899d504da7997fd7c3775c7ca3b35e175261751':
        raise ValueError('Keep the complete original optimal-frame packet')
    frames=json.loads(a.frame.read_text())
    if not all(frames['gates'].values()) or frames['panels']!=10793:
        raise ValueError('Every original positive frame must be paid')
    hashes={str(a.primary):digest(a.primary),str(a.frame):digest(a.frame)}
    for name,want in primary['config']['source_hashes'].items():
        if digest(a.computations/name)!=want:raise ValueError('A frozen coefficient helper changed: '+name)
    groups={}
    for path,want in primary['config']['input_hashes'].items():
        if path.endswith('-summary.json') and 'outer-source-cell' in path:
            if digest(path)!=want:raise ValueError('A true source summary changed')
            d=json.loads(Path(path).read_text())
            if not d['all_gates'] or not all(d['gates'].values()):raise ValueError('An original source gate is unpaid')
            hashes[path]=want
            for g in d['groups']:groups[d['cell'],g['segment']]=g
    fg={}
    for r in frames['files']:
        m=re.search(r'-cell(\d{3})-seg([0-8])-panels\.jsonl\.gz$',r['path'])
        if m:fg[int(m[1]),int(m[2])]=r
    order=[(n,j) for n in (11,10) for j in range(9)]
    if set(groups)!=set(order) or set(fg)!=set(order):raise ValueError('The complete18 source/frame groups are required')
    output=Path(str(a.out_prefix)+'-leaves.jsonl.gz')
    summary=Path(str(a.out_prefix)+'.json')
    if output.exists() or summary.exists():raise FileExistsError('Use a fresh full coefficient output')
    totals=[];count=0
    with output.open('wb') as rawout:
      with gzip.GzipFile(filename='',mode='wb',fileobj=rawout,mtime=0,compresslevel=9) as out:
        for gi,pos in enumerate(order):
            g,f=groups[pos],fg[pos]
            for item in (g,f):
                if digest(item['path'])!=item['sha256']:raise ValueError('A complete source/frame stream changed')
                hashes[item['path']]=item['sha256']
            sm,se=F(0),F(0);idx=0;prev=F(0)
            with gzip.open(f['path'],'rt') as ff:
              it=(json.loads(line) for line in ff if line.strip())
              for row in iter_array(Path(g['path']),'panels'):
                fr=next(it);left,right=F(row['x_left']),F(row['x_right']);dx=right-left
                if row['panel']!=idx or row['segment']!=pos[1] or fr['index']!=idx or F(fr['x_left'])!=left or F(fr['x_right'])!=right or left!=prev or not dx>0:
                    raise ValueError('Exact true leaf/frame ordering failed')
                prev=right
                V,_,_,_=derivative_density(row,arb(17)/16,arb(1)/16,92)
                r,rx,w,ell=(ball(row[k]) for k in ('radius','radius_x','w','log_w_x'))
                if not r>0 or not rx>0 or not w>0 or not w.upper()<=arb(1)/2 or not V>0 or not V<=power2(-40):
                    raise ArithmeticError('A true full-leaf domain bound failed')
                s=rx/r;b=ball(fr['chosen_frame']).upper()
                if not b>0:raise ArithmeticError('The exact original positive frame is required')
                sh,eh=upper96(s),upper96(abs(ell))
                qm=upper96((point(sh)*point(eh)).sqrt())
                qe=upper96(abs(s*b+ell/b)/2)
                aa,dd=upper96(-s-ell),upper96(-2*ell)
                vm,ve=V.man_exp();bm,be=b.man_exp()
                payload=dict(group=gi,cell=pos[0],segment=pos[1],panel=idx,
                    dx=[str(dx.numerator),str(dx.denominator)],
                    V=[str(vm),int(ve)],b=[str(bm),int(be)],
                    s_upper=sh,abs_ell_upper=eh,a_upper=aa,d_upper=dd,
                    c_upper=upper96(point(sh)+point(eh)),q_Metzler=qm,q_energy=qe)
                out.write((json.dumps(payload,separators=(',',':'))+'\n').encode())
                sm+=frac(qm)*dx;se+=frac(qe)*dx;idx+=1;count+=1
                if idx%64==0:guard()
              if next(it,None) is not None:raise ValueError('Unused original frame rows')
            if prev!=1 or idx!=g['panels'] or idx!=f['panels']:raise ValueError('An original source segment is incomplete')
            totals.append(dict(cell=pos[0],segment=pos[1],panels=idx,Metzler_phase=rec(sm),energy_phase=rec(se)))
            print(json.dumps(dict(event='true_hybrid_coefficients_group',cell=pos[0],segment=pos[1],panels=idx,total=count)),flush=True)
    if count!=10793 or output.stat().st_size>=5_000_000:raise ArithmeticError('Coverage or compressed output limit failed')
    rho=F(33,32);start_strip=F(18,125);end_floor=F(1,64)
    choices=[[],[(10,3)],[(11,3)],[(11,7),(10,7)],[(10,3),(11,7)],[(10,3),(10,7)],[(11,3),(10,3)]]
    cases=[]
    for choice in choices:
        phase=sum((F(int(r['energy_phase' if (r['cell'],r['segment']) in choice else 'Metzler_phase']['numerator']),int(r['energy_phase' if (r['cell'],r['segment']) in choice else 'Metzler_phase']['denominator'])) for r in totals),F(0))
        end=start_strip-rho*phase
        cases.append(dict(energy_groups=choice,phase_upper=rec(phase),strip_loss=rec(rho*phase),terminal_strip=rec(end),terminal_strictly_above_one_over64=end>end_floor))
    result=dict(schema='visible-flex-true-hybrid-middle-leaves-v1',author='exact_closure (GPT-6 Astra Pro; AI-assisted)',
        status='Complete shared whole-leaf comparison coefficients and exact candidate strip budgets; no middle kernel yet',
        all_coefficient_gates=True,original_panels=count,groups=totals,phase_cases=cases,
        fixed_strip_start='18/125',window_ratio_upper='33/32',required_strip_floor='1/64',
        leaf_file=dict(path=str(output),bytes=output.stat().st_size,sha256=digest(output)),
        input_hashes=hashes,source_sha256=digest(__file__),precision=a.precision,
        all_frame_entry_exit_and_jumps_still_required=True,
        full_middle_kernel_claimed=False,full_nonlinear_solution_claimed=False,
        elapsed_seconds=time.monotonic()-start,peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    guard();summary.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(dict(event='complete_true_hybrid_coefficients',all_gates=True,
        phase_cases=[dict(energy_groups=r['energy_groups'],terminal_strip=r['terminal_strip']['display_only'],paid=r['terminal_strictly_above_one_over64']) for r in cases],
        elapsed_seconds=result['elapsed_seconds'],peak_rss_kib=result['peak_rss_kib'])),flush=True)


if __name__=='__main__':main()
