#!/usr/bin/env python3
"""Full428 common-strip check with an exact214-dimensional proposal factor.

This is a new, independently hashed recovery entry point.  The previous
session90734 had no observed final result.  Every original low/middle/
infinite/far radius and Lipschitz row is still verified directly here.
Only the two proposal linear solves are reduced using J=C B, where B
sums low+middle+infinite in each cell and retains the far coordinate.
Author: exact_closure (GPT-6 Astra Pro, AI-assisted), 2026-11-12.
"""
import argparse
from fractions import Fraction
import gzip
import hashlib
import json
from pathlib import Path
import resource
import time
from flint import arb,arb_mat,ctx
from closure_real_head_source_enclosure import exact_q,power2,ball_record
from closure_real_head_green_enclosure import load_json,ball


def sha(raw):return hashlib.sha256(raw).hexdigest()


def compact(x):return arb(int(x[0]))*power2(int(x[1]))


def dyadic_text(s):
    if not isinstance(s,str) or not s.startswith('2^'):raise ValueError('Expected an exact dyadic radius')
    return power2(int(s[2:]))


def K(t,a):return (3*t+arb(3)/2*t*t+216*a*(t+t*t+t*t*t/3)).upper()


def main():
    p=argparse.ArgumentParser(description=__doc__)
    for name in ('low','high','density','out'):
        p.add_argument('--'+name,type=Path,required=True)
    p.add_argument('--physical-domain-log2',type=int,default=-30)
    p.add_argument('--metric-target',default='3/4')
    args=p.parse_args();ctx.prec=192;started=time.monotonic()
    summary_path=args.out.with_name(args.out.name.removesuffix('.json.gz')+'-summary.json')
    if args.out.exists() or summary_path.exists():raise FileExistsError('Use a fresh output prefix')
    docs={};hashes={}
    for name in ('low','high','density'):
        path=getattr(args,name);docs[name],raw=load_json(path);hashes[str(path)]=sha(raw)
    low=docs['low'];high=docs['high'];density=docs['density'];cells=list(range(12,225));N=len(cells)
    if low['cells']!=cells or low['modes']!=list(range(2,93,2)) or not low['full_range_covered']:
        raise ValueError('The full real low Green window is unavailable')
    if not all(high['gates'].values()) or not all(density['gates'].values()):
        raise ValueError('An existing high/material input has unpaid stated gates')
    for data in (low,high):
        if hashes[str(args.density)] not in data['input_hashes'].values():raise ValueError('The common physical norm differs')
    if not high['independent_far_parameter'] or not high['complete_mean_and_pointwise_inverse']:
        raise ValueError('The high response must retain an independent far ball and the complete source')
    middle_path=Path(high['gamma_source']);middle,raw=load_json(middle_path);mh=sha(raw);hashes[str(middle_path)]=mh
    if mh not in high['input_hashes'].values():raise ValueError('The high causal kernel changed')
    if hashes[str(args.density)] not in middle['input_hashes'].values():raise ValueError('The high causal norm differs')
    if not all(middle['gates'].values()):raise ValueError('The middle kernel has unpaid stated input gates')
    G={name:[[compact(x) for x in row] for row in low['gamma_upper'][name]] for name in ('main','corr','base','remainder')}
    F={name:[compact(x) for x in low['far_z_source_upper'][name]] for name in G}
    if any(len(G[name])!=N or any(len(row)!=N for row in G[name]) or len(F[name])!=N for name in G):
        raise ValueError('The complete low/far matrices are required')
    H=[[arb(0) for _ in cells] for _ in cells];count=0
    for row in middle['gamma_rows']:
        k=row['output_cell']-12
        for src in row['sources']:
            n=src['source_cell']-12
            if not 0<=k<=n<N:raise ValueError('A high causal entry has the wrong order')
            H[k][n]=ball(src['gamma']).upper();count+=1
    if count!=N*(N+1)//2:raise ValueError('The full high causal triangle is required')
    dr={r['cell']:r for r in density['rows']};hr={r['cell']:r for r in high['rows']}
    if sorted(dr)!=cells or sorted(hr)!=cells or [r['cell'] for r in low['rows']]!=cells:
        raise ValueError('All213 cell domains and boundary lifts are required')
    A=[ball(dr[n]['V_over_w_upper']).upper() for n in cells]
    ghi=ball(density['gamma_high']).upper();rho=power2(args.physical_domain_log2)
    zstar=power2(high['z_log2']);zaux=dyadic_text(low['auxiliary_far_z_bound'])
    CD=dyadic_text(low['raw_D_constant'])
    if not zstar<=power2(-2200) or not zaux<zstar/2:raise ValueError('The declared R18 domain is unavailable')
    if low['far_strip']!=38 or low['far_physical_node']!=225:raise ValueError('The exact far normalization differs')
    beta_low=[(ball(r['B_low']).upper()*4*CD*zstar*zstar).upper() for r in low['rows']]
    beta_z=(ball(low['E_B_low']).upper()*4*CD*zstar).upper()
    pure=[ball(hr[n]['pure_low_residual']).upper() for n in cells]
    far=[ball(hr[n]['far_boundary']).upper() for n in cells]
    deep=ball(high['deep_high_boundary']).upper();pure_inf=ball(high['pure_low_infinite_residual']).upper()
    inf=2*N;zi=inf+1;dim=zi+1
    L=[[ (G['main'][k][n]+3*G['corr'][k][n]+3*rho*G['base'][k][n]
          +216*(1+rho)**2*G['remainder'][k][n]).upper() for n in range(N)] for k in range(N)]
    Z=[((F['main'][n]+3*F['corr'][n]+3*rho*F['base'][n]
          +216*(1+rho)**2*F['remainder'][n])/zstar).upper() for n in range(N)]
    slopes=[(3*(1+rho)+216*a*(1+rho)**2).upper() for a in A]
    HC=[[ (H[k][n]*slopes[n]).upper() for n in range(N)] for k in range(N)]
    IC=[(ghi*s).upper() for s in slopes]
    b=[arb(0) for _ in range(dim)]
    for k in range(N):b[N+k]=(pure[k]+far[k]).upper()
    b[inf]=(pure_inf+deep).upper()

    def B_apply(x):
        return [(x[n]+x[N+n]+x[inf]).upper() for n in range(N)]+[x[zi]]

    def C_apply(y):
        t=y[:N];z=y[N];out=[arb(0) for _ in range(dim)]
        for k in range(N):
            out[k]=(sum((L[k][n]*t[n] for n in range(N)),arb(0))+beta_low[k]*z).upper()
            out[N+k]=(sum((HC[k][n]*t[n] for n in range(k,N)),arb(0))+4*far[k]*z).upper()
        out[inf]=(sum((IC[n]*t[n] for n in range(N)),arb(0))+4*deep*z).upper()
        out[zi]=(sum((Z[n]*t[n] for n in range(N)),arb(0))+beta_z*z).upper()
        return out

    # BC has N+1 coordinates.  No original budget coordinate is discarded.
    reduced=[[arb(0) for _ in range(N+1)] for _ in range(N+1)]
    for k in range(N):
        for n in range(N):reduced[k][n]=(L[k][n]+HC[k][n]+IC[n]).upper()
        reduced[k][N]=(beta_low[k]+4*far[k]+4*deep).upper()
    reduced[N]=Z+[beta_z]
    previous=[ball(hr[n].get('proposal_radius',hr[n].get('radius'))).upper() for n in cells]
    previous_inf=ball(high.get('proposal_infinite_radius',high.get('infinite_radius'))).upper()
    initial_t=[v+previous_inf for v in previous]
    initial_low=[sum((L[k][n]*initial_t[n] for n in range(N)),arb(0)).upper() for k in range(N)]
    initial_z=sum((v*t for v,t in zip(Z,initial_t)),arb(0)).upper()
    tiny=power2(-10000)
    proposal_seed=[max(v,tiny) for v in initial_low]+[max(v,tiny) for v in previous]+[max(previous_inf,tiny),max(initial_z,tiny)]
    S=B_apply(proposal_seed)
    scaled=[[(reduced[i][j]*S[j]/S[i]).upper() for j in range(N+1)] for i in range(N+1)]
    b_reduced=B_apply(b)
    print(json.dumps(dict(event='assembled',original_dimension=dim,proposal_dimension=N+1,
        seconds=time.monotonic()-started,RSS_KiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)),flush=True)
    failure=None;radius=[];weights=[];images=[];liprows=[];t=[]
    try:
        M=arb_mat([[arb(1 if i==j else 0)-scaled[i][j] for j in range(N+1)] for i in range(N+1)])
        solution=M.solve(arb_mat([[(b_reduced[i]/S[i]).upper()] for i in range(N+1)]))
        if not all(solution[i,0].lower()>0 for i in range(N+1)):
            failure='The reduced radius proposal has an unproved positive coordinate'
        else:
            y=[(S[i]*solution[i,0].upper()).upper() for i in range(N+1)]
            cy=C_apply(y);radius=[(2*(b[i]+cy[i])).upper() for i in range(dim)]
    except Exception as e:failure='Reduced radius proposal: '+repr(e)
    if failure is None:
        t=B_apply(radius)[:N]
        poly=[(v+v*v+v*v*v/3).upper() for v in t]
        square=[(arb(3)/2*v*v).upper() for v in t]
        kval=[K(v,a) for v,a in zip(t,A)]
        images=[arb(0) for _ in range(dim)]
        for k in range(N):
            images[k]=(sum(((G['main'][k][n]+3*G['corr'][k][n])*t[n]
                +G['base'][k][n]*square[n]+216*G['remainder'][k][n]*poly[n]
                for n in range(N)),arb(0))+beta_low[k]*radius[zi]).upper()
            images[N+k]=(pure[k]+far[k]+sum((H[k][n]*kval[n] for n in range(k,N)),arb(0))).upper()
        images[inf]=(pure_inf+deep+ghi*sum(kval,arb(0))).upper()
        images[zi]=(sum(((F['main'][n]+3*F['corr'][n])*t[n]
            +F['base'][n]*square[n]+216*F['remainder'][n]*poly[n]
            for n in range(N)),arb(0))/zstar+beta_z*radius[zi]).upper()
        print(json.dumps(dict(event='radius_proposal',maximum_cell_radius_log2=str(max(t).log()/arb(2).log()),
            far_normalized_radius_log2=str(radius[zi].log()/arb(2).log()),
            direct_all428_invariance=all(images[i]<radius[i] for i in range(dim)),
            seconds=time.monotonic()-started)),flush=True)
        target=exact_q(Fraction(args.metric_target))
        if not 0<target<1:raise ValueError('The metric target must lie strictly between zero and one')
        try:
            M=arb_mat([[target*(1 if i==j else 0)-scaled[i][j] for j in range(N+1)] for i in range(N+1)])
            proposal=M.solve(arb_mat([[1] for _ in range(N+1)]))
            if not all(proposal[i,0].lower()>0 for i in range(N+1)):
                failure='The reduced metric proposal has an unproved positive coordinate'
            else:
                y=[(S[i]*proposal[i,0].upper()).upper() for i in range(N+1)]
                cy=C_apply(y);weights=[((proposal_seed[i]+cy[i])/target).upper() for i in range(dim)]
                jw=C_apply(B_apply(weights))
                liprows=[(jw[i]/weights[i]).upper() for i in range(dim)]
        except Exception as e:failure='Reduced metric proposal: '+repr(e)
    gates=dict(radius_proposal_positive=bool(radius) and all(v>0 for v in radius),
        all428_map_inclusions=bool(images) and all(images[i]<radius[i] for i in range(dim)),
        physical_correction_domain=bool(t) and max(t)<rho,
        complete_mean_domain=bool(t) and all(A[n]*(1+t[n])<arb(1)/64 for n in range(N)),
        exact_R18_parameter_domain=bool(radius) and zaux+zstar*radius[zi]<zstar,
        all_metric_weights_positive=bool(weights) and all(v>0 for v in weights),
        full_joint_Lipschitz=bool(liprows) and max(liprows)<1)
    rows=[]
    for i in range(dim):
        kind='low' if i<N else ('middle' if i<2*N else ('infinite' if i==inf else 'far_z'))
        cell=cells[i] if i<N else (cells[i-N] if i<2*N else None)
        row=dict(index=i,block=kind,cell=cell,constant_term=ball_record(b[i]))
        if radius:row['radius']=ball_record(radius[i])
        if images:row.update(image=ball_record(images[i]),map_slack=ball_record((radius[i]-images[i]).lower()))
        if weights:row['metric_weight']=ball_record(weights[i])
        if liprows:row['weighted_derivative_row']=ball_record(liprows[i])
        rows.append(row)
    result=dict(status='Complete true common-strip head box proved' if all(gates.values()) else 'Completed joint positive-majorant attempt; explicit gates remain unpaid',
        whole_head_closed=all(gates.values()),scope='Physical cells12..224 and actual R18 infinite tail; outer0..11, full prefix family and closed-surface geometry remain separate.',
        centred_at='The real auxiliary low46 solution certified by the input box and its actual nonlinear low far lift.',
        complete_mean_and_pointwise_inverse=True,independent_far_parameter=True,
        all46_shallow_heights_fixed=True,high_shallow_heights_free=True,
        dimension=dim,proposal_dimension=N+1,reduction='J=C B, B(low,middle,infinite,z)=(low+middle+infinite,z); only proposals use BC. All428 original rows are directly checked.',
        physical_domain=ball_record(rho),independent_far_z=ball_record(zstar),auxiliary_far_z=ball_record(zaux),
        far_metric='Weighted R18 parameter |delta z|_1 / zstar, with width38 already included in z.',
        low_map='(main+3corr)t +1.5 base*t^2 +216 remainder*(t+t^2+t^3/3) + B_low*(D(z)-D(zaux))',
        high_map='Paid wide-centre residual plus full true far boundary plus gamma*[3t+1.5t^2+216A*(t+t^2+t^3/3)]',
        proposal_only='Neither a positive proposal nor the reduced inverse is a certificate; all original nonlinear map, mean, far, radius and derivative inequalities must pass.',
        gates=gates,failure=failure,rows=rows,
        maximum_cell_total_radius=ball_record(max(t)) if t else None,
        maximum_joint_Lipschitz=ball_record(max(liprows)) if liprows else None,
        source_hash=sha(Path(__file__).read_bytes()),
        helper_hashes={name:sha(Path(__file__).with_name(name).read_bytes()) for name in ('closure_real_head_source_enclosure.py','closure_real_head_green_enclosure.py')},
        input_hashes=hashes,elapsed_seconds=time.monotonic()-started,
        peak_RSS_KiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    payload=gzip.compress((json.dumps(result,separators=(',',':'))+'\n').encode(),mtime=0)
    if len(payload)>=5_000_000:raise ArithmeticError('Repository file size cap exceeded')
    args.out.write_bytes(payload)
    summary={k:v for k,v in result.items() if k!='rows'}
    summary.update(output=str(args.out),output_sha256=sha(payload),bytes=len(payload))
    summary_path.write_text(json.dumps(summary,indent=2)+'\n')
    print(json.dumps(dict(event='done',gates=gates,failure=failure,
        maximum_Lipschitz=str(max(liprows)) if liprows else None,
        seconds=result['elapsed_seconds'],RSS_KiB=result['peak_RSS_KiB'])),flush=True)


if __name__=='__main__':main()
