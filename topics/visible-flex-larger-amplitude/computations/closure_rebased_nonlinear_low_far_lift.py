#!/usr/bin/env python3
"""Pay the actual R18 nonlinear low far boundary in a rebased plateau2 box.

Independent generic-radius adapter of closure_plateau2_nonlinear_low_far_lift.py
SHA256 8f81ad3111939b441c77e8892f31561b532ea7ea700db9d4867f829506f01b17. The real radius is supplied explicitly and checked.

Independent adapter of closure_nonlinear_low_far_lift.py, SHA256 ad4c3ff2efa58dd9091a004d742fa455e60f7394a18c979210d713e8fdc6af78.
The only mathematical changes are reading all actual reference strip widths
and choosing the paid dyadic far radius 2^-2231.

The high boundary trace remains present in the R18 map defining D, but only
its low slope components are lifted into this auxiliary projected head.
No assertion of complete high-frequency matching is made.
"""
import argparse
import hashlib
import json
from pathlib import Path
import resource
import time

from flint import arb,ctx
from closure_real_head_source_enclosure import exact_q,power2,ball_record
from closure_real_head_green_enclosure import load_json,ball,endpoint,mat,mv,inverse_unimodular,maximum,ceil_log2_upper
from closure_projective_interval_column import ProjectiveColumn


def main():
    p=argparse.ArgumentParser(description=__doc__)
    for name in ['columns','ordered','reference','box','ready','out']:
        p.add_argument('--'+name,type=Path,required=True)
    p.add_argument('--precision',type=int,default=192)
    p.add_argument('--far-log2-bound',type=int,default=-2200)
    args=p.parse_args();ctx.prec=args.precision;started=time.monotonic()
    records={};raws={}
    for name in ['columns','ordered','reference','box','ready']:
        records[name],raws[name]=load_json(getattr(args,name))
    D=records['columns'];O=records['ordered'];R=records['reference'];Box=records['box'];ready=records['ready']
    if D['modes']!=list(range(2,93,2)) or not all(Box['gates'].values()):
        raise ValueError('The complete R35 box is required')
    digest=hashlib.sha256(raws['columns']).hexdigest()
    if O['input_hashes'].get(str(args.columns))!=digest or R['input_hashes'].get(str(args.columns))!=digest:
        raise ValueError('Different real columns in the supplied packages')
    if Box['input_hashes'].get(str(args.reference))!=hashlib.sha256(raws['reference']).hexdigest():
        raise ValueError('Box and reference differ')
    params=ready['rationalDeepModel']['physicalParameters']
    rc=exact_q(params['rCuff']);eps=exact_q(params['epsilonScale'])/rc**7
    delta=exact_q(params['delta0'])*power2(-224);ln2=arb(2).log();rho=(arb(11)*ln2/4).exp()
    Sf=eps/rc**3*(arb(11)*delta.log()/2).exp()
    cells=list(range(12,225));count=len(cells);K=[arb(0) for _ in cells];worst_modes=[None]*count
    refined={(m['mode'],r['cell']):r for m in O['mode_rows'] for r in m['refined_cells']}
    group_hashes={}
    for gr in D['column_groups']:
        path=Path(gr['path']);group,graw=load_json(path);gdigest=hashlib.sha256(graw).hexdigest()
        if gdigest!=gr['sha256']:raise ValueError('Column group hash differs')
        group_hashes[str(path)]=gdigest;rows=group['cell_rows']
        mu_ratio=ball(rows[-1]['mu'])/ball(rows[0]['mu'])
        for j,m in enumerate(group['modes']):
            e=group['endpoint_rows'][j];glo=endpoint(e['Q_gain']['lower']);ghi=endpoint(e['Q_gain']['upper'])
            if not(glo>0 or ghi<0):raise ArithmeticError('The exact height chart is not nonzero')
            gain=glo if glo>0 else -ghi;u=m*m-4
            psi=ProjectiveColumn([arb(0),(ball(rows[0]['r_outer'])/rc)**u])
            for k,row in enumerate(rows):
                lin=row['linear_rows'][j];r=ball(row['r_inner']).union(ball(row['r_outer']))
                within=mv(mat(lin['gauge_backward_majorant']),psi.absolute_uppers())
                q=abs((r/rc)**u).upper()*within[0];xi=abs((rc/r)**u).upper()*within[1]
                cap=refined.get((m,row['cell']))
                if cap:
                    q=min(q.upper(),ball(cap['refined_psi_Q_sup']).upper())
                    xi=min(xi.upper(),ball(cap['refined_psi_Xi_sup']).upper())
                tau=ball(R['cell_rows'][k]['tau'])
                value=mu_ratio/gain*Sf*((1+m)**3*q+(1+m)*xi)*((tau-38)*m).exp()
                if value>K[k]:worst_modes[k]=m
                K[k]=maximum(K[k],value)
                psi.advance(inverse_unimodular(mat(lin['gauge_matrix'])))
                if k+1<count:psi.multiply_component(1,rho)
    X=[ball(r['reference_X']).upper() for r in R['cell_rows']]
    W=[ball(r['metric_weight_multiple']) for r in Box['rows']]
    if args.far_log2_bound>-1948:raise ValueError('The Cauchy derivative bound requires Z <= 2^-1948')
    Zstar=power2(args.far_log2_bound)
    if not ball(Box['complete_far_z_bound']).upper()<Zstar:raise ValueError('The R35 far bound is not inside the chosen dyadic radius')
    Cd=power2(1967);Dmax=Cd*Zstar*Zstar
    eD=(W[-1]*X[-1]*ball(R['far_conversion_factor']).upper()/Sf).upper()
    bD=arb(0);row_results=[];map_gate=True;max_fraction=arb(0)
    for k,n in enumerate(cells):
        operator=K[k]/(W[k]*X[k]);bD=maximum(bD,operator)
        extra=(K[k]*Dmax/X[k]).upper()
        slack=ball(Box['rows'][k]['map_slack']).lower()
        frac=extra/slack;max_fraction=maximum(max_fraction,frac)
        map_gate=map_gate and bool(extra<slack)
        row_results.append(dict(cell=n,boundary_operator=ball_record(K[k]),worst_mode=worst_modes[k],
            additional_map_bound_relative_to_reference=ball_record(extra),
            fraction_of_R35_map_slack=ball_record(frac)))
    low_lip=(4*bD*Cd*Zstar*eD).upper()
    total_lip=(ball(Box['maximum_contraction']).upper()+low_lip).upper()
    mean_slope=power2(99)*eps*(arb(33)*delta.log()/4).exp()*Zstar*Zstar
    mean_height=rc*power2(853)*eps*(arb(25)*delta.log()/4).exp()*Zstar*Zstar
    gates=dict(same_R35_box_invariant=map_gate,nonlinear_low_boundary_contraction=bool(total_lip<arb(4)/5))
    result=dict(status='Actual nonlinear low projection of the R18 far graph is absorbed into the same R35 auxiliary low46 box' if all(gates.values()) else 'The nonlinear-low-far sufficient gates were not all paid',
        gates=gates,far_z_dyadic_bound='2^'+str(args.far_log2_bound),raw_D_constant='2^1967',
        low_boundary_formula='B_m d(r)=mu_F/(mu_12*phi_Q(cut))*psi_m(r)*S_F*exp(-38*m)*d_m',
        bD=ball_record(bD),log2_bD=ball_record(bD.log()/ln2),
        eD=ball_record(eD),log2_eD=ball_record(eD.log()/ln2),
        low_boundary_map_metric_bound=ball_record(bD*Dmax),
        maximum_fraction_of_available_map_slack=ball_record(max_fraction),
        log2_maximum_fraction_of_available_map_slack=ball_record(max_fraction.log()/ln2),
        added_Lipschitz_bound=ball_record(low_lip),log2_added_Lipschitz_bound=ball_record(low_lip.log()/ln2),
        total_Lipschitz_bound=ball_record(total_lip),
        full_R18_mean_slope_bound=ball_record(mean_slope),full_R18_mean_height_bound=ball_record(mean_height),
        mean_scope='These are complete true deep-tail bounds; the projected head mean and high boundary components are not thereby matched.',
        rows=row_results,input_hashes={str(getattr(args,n)):hashlib.sha256(raws[n]).hexdigest() for n in raws},
        group_hashes=group_hashes,
        source_hashes={name:hashlib.sha256(Path(__file__).with_name(name).read_bytes()).hexdigest() for name in
            ['closure_rebased_nonlinear_low_far_lift.py','closure_real_head_green_enclosure.py',
             'closure_projective_interval_column.py','closure_real_head_source_enclosure.py']},
        elapsed_seconds=time.monotonic()-started,peak_RSS_KiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
        limits=['The full R18 nonlinear map, including high modes, defines its low slope projection D_low; it is not replaced by a finite Robin equality.',
            'Only D_low is installed in this auxiliary low46 head. The nonzero high far trace and full head-generated high source still require the joint R33 construction.',
            'Only the exact binary shallow node12 heights in the supplied rebased reference are fixed; the exterior numerical trajectory and actual prefix are not thereby certified.'])
    args.out.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(dict(gates=gates,log2_bD=str(bD.log()/ln2),log2_eD=str(eD.log()/ln2),
        log2_slack_fraction=str(max_fraction.log()/ln2),log2_added_lip=str(low_lip.log()/ln2),
        total_lip=str(total_lip),seconds=result['elapsed_seconds'],RSS_KiB=result['peak_RSS_KiB'])),flush=True)
    if not all(gates.values()):raise SystemExit(1)


if __name__=='__main__':main()
