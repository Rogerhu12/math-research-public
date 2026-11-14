#!/usr/bin/env python3
"""True low46 Green in the common physical variable-strip state norm.

The low unknown now uses (B p/V, kappa_perp/V) on the continuous R33 strip.
The old plateau reference remains only the fixed wide analytic reference.
An independent far-z source row and nonlinear boundary lift are exported;
this does not infer a width38 far norm from the weaker state norm.
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


def sha(raw):return hashlib.sha256(raw).hexdigest()


def main():
    p=argparse.ArgumentParser(description=__doc__)
    for name in ['columns','ordered','reference','box','density','ready','out-prefix']:
        p.add_argument('--'+name,type=Path,required=True)
    p.add_argument('--precision',type=int,default=192)
    args=p.parse_args();ctx.prec=args.precision;started=time.monotonic()
    records={};raws={}
    for name in ['columns','ordered','reference','box','density','ready']:
        records[name],raws[name]=load_json(getattr(args,name))
    D=records['columns'];O=records['ordered'];R=records['reference'];Box=records['box']
    P=records['density'];ready=records['ready']
    if D['modes']!=list(range(2,93,2)):
        raise ValueError('The complete low46 true column set is required')
    if O['input_hashes'].get(str(args.columns))!=sha(raws['columns']) or R['input_hashes'].get(str(args.columns))!=sha(raws['columns']):
        raise ValueError('Different true linear columns')
    if Box['input_hashes'].get(str(args.reference))!=sha(raws['reference']) or not all(Box['gates'].values()):
        raise ValueError('The original wide low box is not paid')
    if sha(raws['reference']) not in P['input_hashes'].values() or sha(raws['box']) not in P['input_hashes'].values():
        raise ValueError('The physical envelope has different wide data')
    if sha(raws['ready']) not in D['input_hashes'].values():
        raise ValueError('The ready source is different')
    cells=list(range(12,225));N=len(cells)
    if [r['cell'] for r in P['rows']]!=cells:
        raise ValueError('The full physical envelope is required')
    params=ready['rationalDeepModel']['physicalParameters']
    rc=exact_q(params['rCuff']);eps=exact_q(params['epsilonScale'])/rc**7
    delta=exact_q(params['delta0'])*power2(-224);ln2=arb(2).log();rho=(arb(11)*ln2/4).exp()
    Sf=eps/rc**3*(arb(11)*delta.log()/2).exp();sq12=arb(12).sqrt();rmax=rc*arb(257)/256
    tau_in=[ball(r['tau_inner']).upper() for r in P['rows']]
    tau_out=[ball(r['tau_outer']).lower() for r in P['rows']]
    tau_ref=[ball(r['tau']) for r in R['cell_rows']]
    Xbar=[ball(r['canonical_total_envelope']).upper() for r in P['rows']]
    B=[ball(r['B']).upper() for r in P['rows']]
    a=[ball(r['Q_coefficient']).upper() for r in P['rows']]
    J=[];density_rows=[]
    for k,row in enumerate(P['rows']):
        mu=ball(row['mu_lower']).lower();muup=ball(row['mu_upper']).upper()
        wmin=ball(row['w_lower']).lower()
        Vsup=(Xbar[k]*(a[k]*rmax**3+sq12*muup/(rc**4*wmin))).upper()
        cint=(ball(row['normalized_width_upper']).upper()+ball(row['TV_log_w_upper']).upper()).upper()
        value=(rmax**4*Vsup**2*cint/(sq12*mu)).upper();J.append(value)
        density_rows.append(dict(cell=row['cell'],canonical_source_density_integral=ball_record(value),
            relative_physical_domain_coefficient=row['V_over_w_upper']))
    refined={(m['mode'],r['cell']):r for m in O['mode_rows'] for r in m['refined_cells']}
    gamma=[[None]*N for _ in cells];modes=[[None]*N for _ in cells]
    refgamma=[[None]*N for _ in cells];far_source=[None]*N;far_ref=[None]*N
    boundary=[arb(0) for _ in cells];boundary_z=arb(0);group_hashes={}
    for gr in D['column_groups']:
        path=Path(gr['path']);group,graw=load_json(path)
        if sha(graw)!=gr['sha256']:raise ValueError('A true column group changed')
        group_hashes[str(path)]=sha(graw);rows=group['cell_rows']
        mu=[ball(r['mu']) for r in rows];ratios=[x/mu[0] for x in mu]
        for j,m in enumerate(group['modes']):
            e=group['endpoint_rows'][j];lo=endpoint(e['Q_gain']['lower']);hi=endpoint(e['Q_gain']['upper'])
            if not(lo>0 or hi<0):raise ArithmeticError('The exact height chart is not paid')
            gain=lo if lo>0 else -hi;u=m*m-4
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
            # Pointwise r^3/V <= 1/(Xbar*a), and
            # sqrt(12)*mu/(r^4*w*V) <= 1/Xbar.  These bounds preserve
            # the common physical component order and its one angular weight.
            cq=[(1+m)*m*(bb+m)/(xx*aa) for bb,xx,aa in zip(B,Xbar,a)]
            cx=[arb(1+m)/xx for xx in Xbar]
            ph=[q*p+x*y for q,x,p,y in zip(cq,cx,phiQ,phiXi)]
            ps=[q*p+x*y for q,x,p,y in zip(cq,cx,psiQ,psiXi)]
            out=[(m*t).exp().upper() for t in tau_in]
            inn=[(-m*t).exp().upper() for t in tau_out]
            wide=[(-m*t).exp().upper() for t in tau_ref]
            for k in range(N):
                bd=(ratios[-1]/gain*Sf*ps[k]*out[k]*(-38*m).exp()).upper()
                boundary[k]=maximum(boundary[k],bd)
                for n in range(N):
                    if k>n:value=ratios[n]*ph[k]*psiQ[n]
                    elif k<n:value=ratios[n]*ps[k]*phiQ[n]
                    else:
                        value=ratios[n]*(cq[k]*phiQ[k]*psiQ[n]+cx[k]*maximum(phiXi[k]*psiQ[n],psiXi[k]*phiQ[n]))
                        cap=refined.get((m,cells[n]))
                        if cap:value=min(value.upper(),ball(cap['kernel_bound']).upper()/Xbar[k])
                    exponent=ceil_log2_upper(value*out[k]*inn[n]*J[n])
                    if gamma[k][n] is None or exponent>gamma[k][n]:
                        gamma[k][n]=exponent;modes[k][n]=m
                    re=ceil_log2_upper(value*out[k]*wide[n])
                    if refgamma[k][n] is None or re>refgamma[k][n]:refgamma[k][n]=re
            for n in range(N):
                common=ratios[n]/gain*psiQ[n]*(arb(38*m)).exp()/Sf
                z=ceil_log2_upper(common*inn[n]*J[n])
                zr=ceil_log2_upper(common*wide[n])
                if far_source[n] is None or z>far_source[n]:far_source[n]=z
                if far_ref[n] is None or zr>far_ref[n]:far_ref[n]=zr
            rfar=ball(rows[-1]['r_inner'])
            psi_far_Q=(abs((rfar/rc)**u).upper()*psi.absolute_uppers()[0]).upper()
            boundary_z=maximum(boundary_z,ratios[-1]/gain*psi_far_Q)
        print(json.dumps(dict(event='group',modes=group['modes'],seconds=time.monotonic()-started)),flush=True)
    source_ref=[ball(r['complete_R23_source_L1']).upper() for r in R['cell_rows']]
    output=[]
    for k,n in enumerate(cells):
        residual=sum((power2(refgamma[k][j])*source_ref[j] for j in range(N)),arb(0)).upper()
        row=sum((power2(gamma[k][j]) for j in range(N)),arb(0)).upper()
        worst=max(range(N),key=lambda j:gamma[k][j])
        output.append(dict(cell=n,wide_reference_residual=ball_record(residual),
            density_Green_row_sum=ball_record(row),diagonal_gamma_log2_upper=gamma[k][k],
            diagonal_maximizing_mode=modes[k][k],largest_source_cell=cells[worst],
            largest_source_mode=modes[k][worst],largest_source_log2_upper=gamma[k][worst],
            normalized_R18_low_boundary_lift=ball_record(boundary[k])))
    z0=ball(R['reference_far_z_bound']).upper()
    zref=sum((power2(far_ref[n])*source_ref[n] for n in range(N)),arb(0)).upper()
    result=dict(status='Actual conditional Green ledger in a NEW common physical low46 norm; no box or joint closure is asserted',
        modes=D['modes'],source_density_rows=density_rows,gamma_log2_upper=gamma,
        maximizing_modes=modes,wide_reference_gamma_log2_upper=refgamma,rows=output,
        state_norm='Per cell sum_m (1+|m|) [sup exp(tau(r)|m|)|B p_m|/V + sup exp(tau(r)|m|)|kappa_m|/V].',
        source_norm='Per cell sum_m sup exp(tau(r)|m|)|f_m|/(c V^2/w).',
        approximation='True columns and ordered cells12/13, then whole-cell tau_inner/tau_outer and separate pointwise V-ratio bounds. These can be conservative.',
        augmented_fixed_point='T_low=G N(Y0+V_low+H)+B D_low(z); T_z=z0+E G N(Y0+V_low+H)+E B D_low(z). At a fixed point z=E(Y0+V_low).',
        far_reference_z_bound=ball_record(z0),far_wide_reference_source_bound=ball_record(zref),
        far_density_source_log2_upper=far_source,far_wide_reference_source_log2_upper=far_ref,
        normalized_R18_far_boundary_lift=ball_record(boundary_z),
        maximum_diagonal_gamma_log2_upper=max(gamma[k][k] for k in range(N)),
        maximum_row_sum=max(output,key=lambda r:float(ball(r['density_Green_row_sum']).log())),
        input_hashes={str(getattr(args,name)):sha(raws[name]) for name in raws},group_hashes=group_hashes,
        source_hashes={name:sha(Path(__file__).with_name(name).read_bytes()) for name in
            ['closure_physical_low_green_enclosure.py','closure_real_head_green_enclosure.py',
             'closure_projective_interval_column.py','closure_real_head_source_enclosure.py']},
        elapsed_seconds=time.monotonic()-started,peak_RSS_KiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
        limits=['The old R38/R39 low-box theorem is unchanged. This is a different candidate proof norm for the joint problem.',
            'Every low frequency through92 and its real Dirichlet Green is retained; no high shallow height condition has been removed.',
            'The far-z row is computed from the actual far Green trace; width38 control is not inferred without this row.',
            'A large diagonal or row is a failure of this explicit enclosure, not of the exact boundary problem.'])
    encoded=gzip.compress((json.dumps(result,separators=(',',':'))+'\n').encode(),mtime=0)
    if len(encoded)>=5_000_000:raise ArithmeticError('Repository file cap exceeded')
    out=Path(str(args.out_prefix)+'.json.gz');out.write_bytes(encoded)
    summary={k:v for k,v in result.items() if k not in ['source_density_rows','gamma_log2_upper','maximizing_modes','wide_reference_gamma_log2_upper','rows']}
    summary.update(output=str(out),output_sha256=sha(encoded),
        worst_diagonal_rows=sorted(output,key=lambda r:r['diagonal_gamma_log2_upper'],reverse=True)[:8])
    Path(str(args.out_prefix)+'-summary.json').write_text(json.dumps(summary,indent=2)+'\n')
    print(json.dumps(dict(event='done',max_diagonal_log2=result['maximum_diagonal_gamma_log2_upper'],
        max_row_cell=result['maximum_row_sum']['cell'],far_ref_log2=str(zref.log()/ln2),
        seconds=result['elapsed_seconds'],RSS_KiB=result['peak_RSS_KiB'])),flush=True)


if __name__=='__main__':main()
