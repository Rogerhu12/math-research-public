#!/usr/bin/env python3
"""Low46 two-boundary Green on tau_n=1+(n-12)log(2)/4.

Consumes real columns, the ordered cell12/13 diagonal refinement, and the
actual variable-strip reference.  This changes the proof norm only.  All
46 shallow heights and exact linear far subspaces remain unchanged.
"""
import argparse
from fractions import Fraction as Q
import gzip
import hashlib
import json
from pathlib import Path
import resource
import time

from flint import arb,ctx
from closure_real_head_source_enclosure import exact_q,power2,ball_record
from closure_real_head_green_enclosure import (load_json,ball,endpoint,mat,mv,
    inverse_unimodular,ceil_log2_upper,maximum)
from closure_projective_interval_column import ProjectiveColumn


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--columns',type=Path,required=True)
    p.add_argument('--ordered',type=Path,required=True)
    p.add_argument('--reference',type=Path,required=True)
    p.add_argument('--ready',type=Path,required=True)
    p.add_argument('--out-prefix',type=Path,required=True)
    p.add_argument('--relative-radius',default='1/100')
    p.add_argument('--precision',type=int,default=192)
    args=p.parse_args();ctx.prec=args.precision;started=time.monotonic()
    data,raw=load_json(args.columns);order,order_raw=load_json(args.ordered)
    reference,ref_raw=load_json(args.reference);ready,ready_raw=load_json(args.ready)
    digest=hashlib.sha256(raw).hexdigest()
    if order['input_hashes'].get(str(args.columns))!=digest or reference['input_hashes'].get(str(args.columns))!=digest:
        raise ValueError('Different linear reference/ordered data')
    if data['modes']!=list(range(2,93,2)):
        raise ValueError('All original 46 parameters must remain')
    if hashlib.sha256(ready_raw).hexdigest() not in data['input_hashes'].values():
        raise ValueError('Source ready differs')
    rc=exact_q(ready['rationalDeepModel']['physicalParameters']['rCuff']);ln2=arb(2).log();rho=(arb(11)*ln2/4).exp()
    cells=list(range(12,225));count=len(cells);gamma=[[None]*count for _ in cells]
    ordered={(m['mode'],row['cell']):ball(row['kernel_bound']).upper()
        for m in order['mode_rows'] for row in m['refined_cells']}
    dominating_diagonal={};group_hashes={};mode_rows=[]
    for group_ref in data['column_groups']:
        path=Path(group_ref['path']);group,graw=load_json(path);gdigest=hashlib.sha256(graw).hexdigest()
        if gdigest!=group_ref['sha256']:raise ValueError('Column group SHA differs')
        group_hashes[str(path)]=gdigest;rows=group['cell_rows'];mu=[ball(r['mu']) for r in rows]
        ratios=[x/mu[0] for x in mu]
        for col,m in enumerate(group['modes']):
            e=group['endpoint_rows'][col];glo=endpoint(e['Q_gain']['lower']);ghi=endpoint(e['Q_gain']['upper'])
            if not(glo>0 or ghi<0):raise ArithmeticError('Nonzero real height chart not paid')
            gain=glo if glo>0 else -ghi;u=m*m-4
            phiQ=[];phiXi=[];psiQ=[];psiXi=[]
            psi=ProjectiveColumn([arb(0),(ball(rows[0]['r_outer'])/rc)**u])
            for k,row in enumerate(rows):
                lin=row['linear_rows'][col]
                phiQ.append(ball(lin['column_Q_sup']).upper()/gain)
                phiXi.append(ball(lin['column_Xi_sup']).upper()/gain)
                radius=ball(row['r_inner']).union(ball(row['r_outer']))
                within=mv(mat(lin['gauge_backward_majorant']),psi.absolute_uppers())
                psiQ.append(abs((radius/rc)**u).upper()*within[0]);psiXi.append(abs((rc/radius)**u).upper()*within[1])
                psi.advance(inverse_unimodular(mat(lin['gauge_matrix'])))
                if k+1<count:psi.multiply_component(1,rho)
            wq=arb((1+m)**3);wx=arb(1+m)
            ph=[wq*q+wx*x for q,x in zip(phiQ,phiXi)];ps=[wq*q+wx*x for q,x in zip(psiQ,psiXi)]
            for k in range(count):
                for n in range(count):
                    if k>n:value=ratios[n]*ph[k]*psiQ[n]
                    elif k<n:value=ratios[n]*ps[k]*phiQ[n]
                    else:
                        value=ratios[n]*(wq*phiQ[k]*psiQ[n]+wx*maximum(phiXi[k]*psiQ[n],psiXi[k]*phiQ[n]))
                        if (m,cells[n]) in ordered:value=min(value.upper(),ordered[(m,cells[n])])
                    # exp((tau_k-tau_n)*m)=2**(m*(k-n)/4).
                    # Rounding this dyadic/half-dyadic factor upward costs
                    # at most half a bit; k=n has no extra loss.
                    exponent=ceil_log2_upper(value)+(m*(k-n)+3)//4
                    if gamma[k][n] is None or exponent>gamma[k][n]:
                        gamma[k][n]=exponent
                        if k==n:dominating_diagonal[cells[k]]=m
            mode_rows.append(dict(mode=m,cut_psi_Q=ball_record(psiQ[0]),cut_psi_Xi=ball_record(psiXi[0])))
        print(json.dumps(dict(event='column_group',modes=group['modes'],seconds=time.monotonic()-started,
            RSS_KiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)),flush=True)
    refs=reference['cell_rows']
    if [r['cell'] for r in refs]!=cells:raise ValueError('Reference cells differ')
    eta=arb(0);response=[]
    for k,row in enumerate(refs):
        x=ball(row['reference_X']).upper()
        terms=[power2(gamma[k][n])*ball(src['complete_R23_source_L1']).upper() for n,src in enumerate(refs)]
        value=sum(terms,arb(0));ratio=value/x;eta=maximum(eta,ratio)
        worst=max(range(count),key=lambda n:float(terms[n].log()) if terms[n]>0 else -float('inf'))
        response.append(dict(cell=row['cell'],reference_X=ball_record(x),source_response=ball_record(value),
            relative_response=ball_record(ratio),largest_source_cell=cells[worst],
            largest_source_relative_term=ball_record(terms[worst]/x),diagonal_dominating_mode=dominating_diagonal[row['cell']]))
    radius=exact_q(Q(args.relative_radius));mapping=eta*(1+radius)**2;lip=4*eta*(1+radius)
    small=all((1+radius)*ball(row['relative_to_R23_radius']).upper()<1 for row in refs)
    result=dict(status='Validated low46 variable-strip Green envelope with ordered cell12/13 kernels',
        modes=data['modes'],strip_formula=reference['strip_formula'],gamma_log2_upper=gamma,response_rows=response,
        maximum_relative_response=ball_record(eta),mode_rows=mode_rows,
        projected_fixed_point=dict(relative_radius=str(Q(args.relative_radius)),mapping_bound=ball_record(mapping),
            contraction_bound=ball_record(lip),all_R23_balls_paid=small,gate_paid=bool(small and mapping<radius and lip<1)),
        input_hashes={str(args.columns):digest,str(args.ordered):hashlib.sha256(order_raw).hexdigest(),
            str(args.reference):hashlib.sha256(ref_raw).hexdigest(),str(args.ready):hashlib.sha256(ready_raw).hexdigest(),**group_hashes},
        source_hashes={name:hashlib.sha256(Path(__file__).with_name(name).read_bytes()).hexdigest() for name in
            ['closure_variable_strip_green_enclosure.py','closure_real_head_green_enclosure.py',
             'closure_projective_interval_column.py','closure_real_head_source_enclosure.py']},
        elapsed_seconds=time.monotonic()-started,peak_RSS_KiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
        limits=['Only the auxiliary pointwise equation projected into the retained low46 has this Green feedback.',
            'The full R18 nonlinear far graph, high-frequency head source, and outer-prefix matching remain independent.',
            'This norm follows the actual varying-strip reference, not the constant-strip1 correction ball.'])
    out=Path(str(args.out_prefix)+'.json.gz');encoded=gzip.compress((json.dumps(result,separators=(',',':'))+'\n').encode(),mtime=0)
    if len(encoded)>=5_000_000:raise ArithmeticError('Repository file cap exceeded')
    out.write_bytes(encoded)
    summary={k:v for k,v in result.items() if k not in ['gamma_log2_upper','response_rows','mode_rows','input_hashes']}
    worst_rows=sorted(response,key=lambda r:float(ball(r['relative_response']).log()),reverse=True)[:5]
    summary.update(worst_rows=worst_rows,output=str(out),output_sha256=hashlib.sha256(encoded).hexdigest())
    Path(str(args.out_prefix)+'-summary.json').write_text(json.dumps(summary,indent=2)+'\n')
    print(json.dumps(dict(event='done',eta=str(eta),gate=result['projected_fixed_point']['gate_paid'],
        seconds=result['elapsed_seconds'],RSS_KiB=result['peak_RSS_KiB'])),flush=True)


if __name__=='__main__':main()
