#!/usr/bin/env python3
"""Exact position attribution of a completed two-cell source functional.

Retains each original signed geometry kernel. Separates source-quadratic
interval width, complete remainder/rounding width, and geometry width.
This is a valid further enclosure and an attribution of that enclosure;
it does not assert any bound is the actual mathematical error.
"""
import argparse
from decimal import Decimal, localcontext
from fractions import Fraction
import hashlib
import json
from pathlib import Path
import resource
import time

from closure_split_joint_io_v2 import iter_array


def sha(path):
    h=hashlib.sha256()
    with Path(path).open('rb') as f:
        for b in iter(lambda:f.read(1024*1024),b''):h.update(b)
    return h.hexdigest()


def dyadic(d):
    if isinstance(d,list):m,k=int(d[0]),int(d[1])
    else:m,k=int(d['mantissa']),int(d['binary_exponent'])
    return Fraction(m << k) if k>=0 else Fraction(m,1 << -k)


def bounds(d):
    lo,hi=dyadic(d['lower']),dyadic(d['upper'])
    if lo>hi:raise ValueError('Reversed input interval')
    return lo,hi


def rec(x):
    with localcontext() as c:
        c.prec=30
        s=str(Decimal(x.numerator)/Decimal(x.denominator))
    return dict(numerator=str(x.numerator),denominator=str(x.denominator),display=s)


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--functional',type=Path,required=True)
    p.add_argument('--mode',type=int,default=4)
    p.add_argument('--out',type=Path,required=True)
    p.add_argument('--rss-kib',type=int,default=40960)
    a=p.parse_args();began=time.monotonic()
    if a.out.exists():raise FileExistsError('Use a fresh attribution output')
    d=json.loads(a.functional.read_text())
    if not d['all_gates'] or d['counts']['original_material']!=10793:raise ValueError('The entire completed function is required')
    target=next(row for row in d['rows'] if row['mode']==a.mode)
    flo,fhi=bounds(target['canonical_cut_geometry_factor'])
    factor=max(abs(flo),abs(fhi))
    fmid=(flo+fhi)/2;frad=(fhi-flo)/2
    names=['nominal','geometry_width','quadratic_source_width','complete_remainder_and_rounding_width','absolute_nominal_sum']
    total={name:Fraction(0) for name in names}
    rows=[];top=[];counts=0;hashes={str(a.functional):sha(a.functional)}
    for group in d['kernel_groups']:
        n,j=group['cell'],group['segment']
        gp,sp=Path(group['path']),Path(group['source_group_path'])
        if sha(gp)!=group['sha256'] or sha(sp)!=group['source_group_sha256']:raise ValueError('An original source/kernel group changed')
        hashes[str(gp)]=group['sha256'];hashes[str(sp)]=group['source_group_sha256']
        source={}
        for r in iter_array(sp,'panels'):
            c=next(x for x in r['selected_cosine_sources'] if x['mode']==a.mode)
            ql,qh=bounds(c['quadratic_cosine']);nl,nh=bounds(c['complete_source_cosine'])
            nc=(ql+qh)/2;qr=(qh-ql)/2;nr=max(abs(nl-nc),abs(nh-nc))
            if nr<qr:raise ArithmeticError('The complete source must contain the quadratic uncertainty')
            source[r['panel']]=(nc,qr,nr-qr,r['x_left'],r['x_right'])
        accum={name:Fraction(0) for name in names};seen=0
        for r in iter_array(gp,'panels'):
            index=r['panel'];nc,qr,rr,xl,xr=source.pop(index)
            if r['x_left']!=xl or r['x_right']!=xr:raise ValueError('The same true material position is required')
            w=next(x for x in r['weights'] if x['mode']==a.mode and x['readout']==0)
            kl,kh=map(dyadic,w['signed']);ka=dyadic(w['absolute'])
            if ka<0 or kl>kh:raise ValueError('Invalid geometry enclosure')
            kl,kh=max(kl,-ka),min(kh,ka)
            if kl>kh:raise ArithmeticError('Signed/absolute geometry enclosures do not intersect')
            kc,kr=(kl+kh)/2,(kh-kl)/2
            v=dict(nominal=nc*kc,geometry_width=abs(nc)*kr,
                quadratic_source_width=qr*ka,complete_remainder_and_rounding_width=rr*ka,
                absolute_nominal_sum=abs(nc*kc))
            for name in names:accum[name]+=v[name]
            uncertainty=v['geometry_width']+v['quadratic_source_width']+v['complete_remainder_and_rounding_width']
            item=dict(cell=n,segment=j,panel=index,x_left=xl,x_right=xr,
                source_nominal=rec(nc),source_quadratic_radius=rec(qr),
                source_complete_remainder_rounding_radius=rec(rr),
                cut_Q_nominal=rec(fmid*v['nominal']),
                cut_Q_geometry_width=rec(factor*v['geometry_width']),
                cut_Q_quadratic_source_width=rec(factor*v['quadratic_source_width']),
                cut_Q_complete_remainder_rounding_width=rec(factor*v['complete_remainder_and_rounding_width']),
                cut_Q_total_width=rec(factor*uncertainty))
            top.append((uncertainty,item))
            if len(top)>48:top=sorted(top,key=lambda x:x[0],reverse=True)[:24]
            seen+=1
        if source or seen!=group['panels']:raise ValueError('The complete original group is required')
        counts+=seen
        for name in names:total[name]+=accum[name]
        uncertainty=sum((accum[name] for name in names[1:4]),Fraction(0))
        rows.append(dict(cell=n,segment=j,panels=seen,
            cut_Q_nominal=rec(fmid*accum['nominal']),
            cut_Q_geometry_width=rec(factor*accum['geometry_width']),
            cut_Q_quadratic_source_width=rec(factor*accum['quadratic_source_width']),
            cut_Q_complete_remainder_rounding_width=rec(factor*accum['complete_remainder_and_rounding_width']),
            cut_Q_total_width=rec(factor*uncertainty),
            cut_Q_absolute_nominal_sum=rec(factor*accum['absolute_nominal_sum'])))
        if resource.getrusage(resource.RUSAGE_SELF).ru_maxrss>a.rss_kib:raise MemoryError('The exact attribution exceeded its owned RSS guard')
    if counts!=10793:raise ValueError('No radial source position may be omitted')
    error=sum((total[name] for name in names[1:4]),Fraction(0))
    lo,hi=total['nominal']-error,total['nominal']+error
    oldlo,oldhi=bounds(target['true_global_qv_forcing_vector'][0])
    if max(lo,oldlo)>min(hi,oldhi):raise ArithmeticError('The independent true source enclosures do not intersect')
    cut_nom=fmid*total['nominal']
    cut_error=factor*error+frad*abs(total['nominal'])
    output=dict(status='Complete same-position interval-width attribution, not an actual-error lower bound',
        mode=a.mode,readout='terminal_global_q_then_cut_Q',cells=[11,10],panels=counts,
        gates=dict(all_original_positions=True,source_kernel_identity=True,
            complete_mean_and_inverse_source_retained=True,signed_and_absolute_geometry_intersect=True,
            original_complete_source_integral_intersects=True,no_new_ODE_or_source_evaluation=True),
        all_gates=True,cut_Q_source_enclosure=dict(lower=rec(cut_nom-cut_error),upper=rec(cut_nom+cut_error)),
        cut_Q_nominal=rec(cut_nom),cut_Q_total_width=rec(cut_error),
        cut_Q_width_decomposition={name:rec(factor*total[name]) for name in names[1:4]},
        cut_Q_factor_width=rec(frad*abs(total['nominal'])),
        cut_Q_absolute_nominal_sum=rec(factor*total['absolute_nominal_sum']),
        groups=rows,largest_original_panels=[row for unused,row in sorted(top,key=lambda x:x[0],reverse=True)[:24]],
        includes_head_far_completion=False,
        scope='Only the candidate source functional is attributed. The R63 nonzero head far supplement is separate and does not alter any source kernel.',
        input_hashes=hashes,source_sha256=sha(__file__),
        elapsed_seconds=time.monotonic()-began,peak_RSS_KiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    a.out.write_text(json.dumps(output,indent=2)+'\n')
    print(json.dumps(dict(output=str(a.out),all_gates=True,panels=counts,
        nominal=output['cut_Q_nominal']['display'],width=output['cut_Q_total_width']['display'],
        components={k:v['display'] for k,v in output['cut_Q_width_decomposition'].items()},
        peak_RSS_KiB=output['peak_RSS_KiB'])),flush=True)


if __name__=='__main__':main()
