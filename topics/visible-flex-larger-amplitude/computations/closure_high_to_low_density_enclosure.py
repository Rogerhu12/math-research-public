#!/usr/bin/env python3
"""Enclose complete high-to-low source feedback with explicit angular loss.

This first sufficient ledger retains every low output mode and every source
cell, but uses the complete R33 quadratic/Lipschitz density estimate before
projecting. It does NOT use a frequency-local Taylor/convolution improvement.
Failure is a failure of this named majorant, not of the exact joint problem.
"""
import argparse
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


def digest(raw):return hashlib.sha256(raw).hexdigest()


def main():
    p=argparse.ArgumentParser(description=__doc__)
    for name in ['columns','ordered','reference','box','density','high-box','ready','out-prefix']:
        p.add_argument('--'+name,type=Path,required=True)
    p.add_argument('--precision',type=int,default=192)
    args=p.parse_args();ctx.prec=args.precision;started=time.monotonic()
    records={};raws={}
    for name in ['columns','ordered','reference','box','density','high_box','ready']:
        records[name],raws[name]=load_json(getattr(args,name))
    D=records['columns'];O=records['ordered'];R=records['reference'];Box=records['box']
    P=records['density'];High=records['high_box'];ready=records['ready']
    if D['modes']!=list(range(2,93,2)) or not all(Box['gates'].values()):
        raise ValueError('The complete paid low46 box is required')
    if O['input_hashes'].get(str(args.columns))!=digest(raws['columns']):
        raise ValueError('Ordered kernel and real columns differ')
    if R['input_hashes'].get(str(args.columns))!=digest(raws['columns']):
        raise ValueError('Reference and real columns differ')
    if Box['input_hashes'].get(str(args.reference))!=digest(raws['reference']):
        raise ValueError('Box and reference differ')
    if digest(raws['reference']) not in P['input_hashes'].values() or digest(raws['box']) not in P['input_hashes'].values():
        raise ValueError('The density envelope is not built from this same low box')
    if digest(raws['density']) not in High['input_hashes'].values() or not all(High['gates'].values()):
        raise ValueError('The high joint box has not paid this same physical density')
    if digest(raws['ready']) not in D['input_hashes'].values():
        raise ValueError('The ready source differs from the real columns')
    cells=list(range(12,225));N=len(cells)
    if [r['cell'] for r in P['rows']]!=cells or [r['cell'] for r in High['rows']]!=cells:
        raise ValueError('Complete 213-cell high-state envelopes are required')
    rc=exact_q(ready['rationalDeepModel']['physicalParameters']['rCuff'])
    rmax=rc*arb(257)/256;ln2=arb(2).log();rho=(arb(11)*ln2/4).exp();sq12=arb(12).sqrt()
    tau=[ball(r['tau']) for r in R['cell_rows']]
    tau_outer=[ball(r['tau_outer']).lower() for r in P['rows']]
    X=[ball(r['reference_X']).upper() for r in R['cell_rows']]
    W=[ball(r['metric_weight_multiple']) for r in Box['rows']]
    # The high joint ledger keeps a separate infinite-window metric weight.
    high_radius=ball(High['infinite_radius']).upper()
    hw=High['infinite_metric_weight']
    high_weight=(ball(hw) if isinstance(hw,dict) else arb(hw)).upper()
    middle_radius=[ball(r['middle_radius']).upper() for r in High['rows']]
    middle_weight=[ball(r['middle_metric_weight']).upper() for r in High['rows']]
    J=[];density_rows=[]
    for row in P['rows']:
        xb=ball(row['canonical_total_envelope']).upper()
        a=ball(row['Q_coefficient']).upper();mu=ball(row['mu_lower']).lower()
        muup=ball(row['mu_upper']).upper();wmin=ball(row['w_lower']).lower()
        Vsup=(xb*(a*rmax**3+sq12*muup/(rc**4*wmin))).upper()
        cint=(ball(row['normalized_width_upper']).upper()+ball(row['TV_log_w_upper']).upper()).upper()
        value=(rmax**4*Vsup**2*cint/(sq12*mu)).upper();J.append(value)
        density_rows.append(dict(cell=row['cell'],canonical_source_density_integral=ball_record(value),
            V_sup=ball_record(Vsup),c_integral_upper=ball_record(cint)))
    refined={(m['mode'],r['cell']):r for m in O['mode_rows'] for r in m['refined_cells']}
    gamma=[[None]*N for _ in cells];mode_at=[[None]*N for _ in cells];group_hashes={}
    for gr in D['column_groups']:
        path=Path(gr['path']);group,graw=load_json(path)
        if digest(graw)!=gr['sha256']:raise ValueError('True column group hash changed')
        group_hashes[str(path)]=digest(graw);rows=group['cell_rows']
        mu=[ball(r['mu']) for r in rows];ratios=[x/mu[0] for x in mu]
        for j,m in enumerate(group['modes']):
            e=group['endpoint_rows'][j];glo=endpoint(e['Q_gain']['lower']);ghi=endpoint(e['Q_gain']['upper'])
            if not(glo>0 or ghi<0):raise ArithmeticError('The exact height chart is not paid')
            gain=glo if glo>0 else -ghi;u=m*m-4
            phiQ=[];phiXi=[];psiQ=[];psiXi=[]
            psi=ProjectiveColumn([arb(0),(ball(rows[0]['r_outer'])/rc)**u])
            for k,row in enumerate(rows):
                lin=row['linear_rows'][j]
                phiQ.append(ball(lin['column_Q_sup']).upper()/gain)
                phiXi.append(ball(lin['column_Xi_sup']).upper()/gain)
                r=ball(row['r_inner']).union(ball(row['r_outer']))
                within=mv(mat(lin['gauge_backward_majorant']),psi.absolute_uppers())
                psiQ.append(abs((r/rc)**u).upper()*within[0]);psiXi.append(abs((rc/r)**u).upper()*within[1])
                cap=refined.get((m,row['cell']))
                if cap:
                    phiQ[-1]=min(phiQ[-1].upper(),ball(cap['refined_phi_Q_sup']).upper())
                    phiXi[-1]=min(phiXi[-1].upper(),ball(cap['refined_phi_Xi_sup']).upper())
                    psiQ[-1]=min(psiQ[-1].upper(),ball(cap['refined_psi_Q_sup']).upper())
                    psiXi[-1]=min(psiXi[-1].upper(),ball(cap['refined_psi_Xi_sup']).upper())
                psi.advance(inverse_unimodular(mat(lin['gauge_matrix'])))
                if k+1<N:psi.multiply_component(1,rho)
            wq=arb((1+m)**3);wx=arb(1+m)
            ph=[wq*q+wx*x for q,x in zip(phiQ,phiXi)]
            ps=[wq*q+wx*x for q,x in zip(psiQ,psiXi)]
            angle_out=[(m*t).exp().upper() for t in tau]
            angle_in=[(-m*t).exp().upper() for t in tau_outer]
            for k in range(N):
                for n in range(N):
                    if k>n:value=ratios[n]*ph[k]*psiQ[n]
                    elif k<n:value=ratios[n]*ps[k]*phiQ[n]
                    else:
                        value=ratios[n]*(wq*phiQ[k]*psiQ[n]+wx*maximum(phiXi[k]*psiQ[n],psiXi[k]*phiQ[n]))
                        cap=refined.get((m,cells[n]))
                        if cap:value=min(value.upper(),ball(cap['kernel_bound']).upper())
                    exponent=ceil_log2_upper(value*angle_out[k]*angle_in[n])
                    if gamma[k][n] is None or exponent>gamma[k][n]:
                        gamma[k][n]=exponent;mode_at[k][n]=m
        print(json.dumps(dict(event='group',modes=group['modes'],seconds=time.monotonic()-started)),flush=True)
    radius=[r+high_radius for r in middle_radius]
    domain_source=[64*J[n]*radius[n]*(1+radius[n]) for n in range(N)]
    derivative_middle=[64*J[n]*(1+2*radius[n])*middle_weight[n] for n in range(N)]
    derivative_infinite=[64*J[n]*(1+2*radius[n])*high_weight for n in range(N)]
    output=[];max_fraction=arb(0);middle_lip=arb(0);infinite_lip=arb(0)
    for k,n in enumerate(cells):
        terms=[power2(gamma[k][j])*domain_source[j] for j in range(N)]
        extra=sum(terms,arb(0)).upper();slack=ball(Box['rows'][k]['map_slack']).lower()
        frac=(extra/(X[k]*slack)).upper();max_fraction=maximum(max_fraction,frac)
        lm=(sum((power2(gamma[k][j])*derivative_middle[j] for j in range(N)),arb(0))/(W[k]*X[k])).upper()
        li=(sum((power2(gamma[k][j])*derivative_infinite[j] for j in range(N)),arb(0))/(W[k]*X[k])).upper()
        middle_lip=maximum(middle_lip,lm);infinite_lip=maximum(infinite_lip,li)
        worst=max(range(N),key=lambda j:float(terms[j].log()) if terms[j]>0 else -float('inf'))
        output.append(dict(cell=n,map_added=ball_record(extra),fraction_of_available_low_slack=ball_record(frac),
            log2_slack_fraction=ball_record(frac.log()/ln2),middle_metric_Lipschitz_column=ball_record(lm),
            infinite_metric_Lipschitz_column=ball_record(li),largest_source_cell=cells[worst],
            largest_output_mode=mode_at[k][worst],largest_source_term=ball_record(terms[worst])))
    result=dict(status='Complete-source projection majorant with paid source-cell and low-output angular weights; inspect gates rather than process exit',
        source_formula='J_n >= integral r^4*c(r)*V(r)^2/(sqrt(12)*mu_n) dr; complete high difference <=64*J_n*R_n*(1+R_n)',
        projection_formula='max_m gamma_raw(k,n,m)*exp(m*tau_low(k)-m*tau_outer(n)); all physical m=2..92 are retained',
        source_density_rows=density_rows,gamma_log2_upper=gamma,maximizing_output_modes=mode_at,rows=output,
        gates=dict(original_low_box_slack_pays_high_source=bool(max_fraction<1)),
        maximum_slack_fraction=ball_record(max_fraction),log2_maximum_slack_fraction=ball_record(max_fraction.log()/ln2),
        middle_to_low_metric_column=ball_record(middle_lip),infinite_to_low_metric_column=ball_record(infinite_lip),
        input_hashes={str(getattr(args,name)):digest(raws[name]) for name in raws},group_hashes=group_hashes,
        source_hashes={name:digest(Path(__file__).with_name(name).read_bytes()) for name in
            ['closure_high_to_low_density_enclosure.py','closure_real_head_green_enclosure.py',
             'closure_projective_interval_column.py','closure_real_head_source_enclosure.py']},
        elapsed_seconds=time.monotonic()-started,peak_RSS_KiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
        limits=['The high nonlinear source is fully bounded, including the mean root and rational factors; no finite polynomial truncation is used.',
            'This majorant does not exploit input-frequency support or individual high-band radii; a failed gate may need those sharper interfaces.',
            'The global rmin/rmax and wmin source-density integral can be improved by ordered physical panels; no such improvement is claimed here.',
            'Lipschitz columns use the exact units of the supplied low/high metric weights; they are not by themselves a joint contraction theorem.'])
    encoded=gzip.compress((json.dumps(result,separators=(',',':'))+'\n').encode(),mtime=0)
    out=Path(str(args.out_prefix)+'.json.gz');out.write_bytes(encoded)
    summary={k:v for k,v in result.items() if k not in ['source_density_rows','gamma_log2_upper','maximizing_output_modes','rows']}
    summary.update(worst_rows=sorted(output,key=lambda r:float(ball(r['log2_slack_fraction'])),reverse=True)[:8],
        output=str(out),output_sha256=digest(encoded))
    Path(str(args.out_prefix)+'-summary.json').write_text(json.dumps(summary,indent=2)+'\n')
    print(json.dumps(dict(event='done',gates=result['gates'],log2_slack_fraction=str(max_fraction.log()/ln2),
        seconds=result['elapsed_seconds'],RSS_KiB=result['peak_RSS_KiB'])),flush=True)


if __name__=='__main__':main()
