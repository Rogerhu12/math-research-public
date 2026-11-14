#!/usr/bin/env python3
"""Pay R47's positive46 parameter radius from an ACTUAL successful joint box.

No inverse, flow, new fixed-point proposal or changed domain is used.
The original428 radii/metric are retained and every lifted inclusion
and total-state domain is checked directly with outward arithmetic.
Author: exact_closure (GPT-6 Astra Pro, AI-assisted), 2026-11-12.
"""
import argparse,gzip,hashlib,json,resource,time
from pathlib import Path
from flint import arb,ctx
from closure_real_head_source_enclosure import power2,ball_record
from closure_real_head_green_enclosure import load_json,ball


def sha(b):return hashlib.sha256(b).hexdigest()
def compact(x):return arb(int(x[0]))*power2(int(x[1]))


def main():
    p=argparse.ArgumentParser(description=__doc__)
    for name in ('low','high','density','joint','lifts','out'):
        p.add_argument('--'+name,type=Path,required=True)
    args=p.parse_args();ctx.prec=192;started=time.monotonic()
    if args.out.exists():raise FileExistsError('Use a fresh actual parameter-ball output')
    docs={};hashes={}
    for name in ('low','high','density','joint','lifts'):
        path=getattr(args,name);docs[name],raw=load_json(path);hashes[str(path)]=sha(raw)
    low=docs['low'];high=docs['high'];den=docs['density'];joint=docs['joint'];lifts=docs['lifts']
    cells=list(range(12,225));N=len(cells);dim=2*N+2;inf=2*N;zi=inf+1
    if not joint['whole_head_closed'] or not all(joint['gates'].values()):
        raise ValueError('R47 requires an actual successful complete joint certificate')
    if joint['dimension']!=dim or len(joint['rows'])!=dim:
        raise ValueError('All428 original rows must be present')
    if low['cells']!=cells or lifts['cells']!=cells or low['modes']!=list(range(2,93,2)) or lifts['modes']!=low['modes']:
        raise ValueError('The full213 cell / actual46 parameter lift is required')
    for name in ('low','high','density'):
        if hashes[str(getattr(args,name))] not in joint['input_hashes'].values():
            raise ValueError('The actual successful joint domain differs: '+name)
    for name in ('low','density'):
        if hashes[str(getattr(args,name))] not in lifts['input_hashes'].values():
            raise ValueError('The parameter lifts use another exact field or norm')
    if not all(high['gates'].values()) or not all(den['gates'].values()):raise ValueError('The material or high-domain input is unpaid')
    Z=ball(joint['independent_far_z']);rho=ball(joint['physical_domain'])
    if not Z==ball(lifts['parameter_far_scale']):raise ValueError('The independent exact far parameter norm differs')
    middle_path=Path(high['gamma_source']);middle,raw=load_json(middle_path);mh=sha(raw)
    if mh not in joint['input_hashes'].values() or mh not in high['input_hashes'].values():
        raise ValueError('The actual complete high causal kernel differs')
    hashes[str(middle_path)]=mh
    G={name:[[compact(v) for v in row] for row in low['gamma_upper'][name]] for name in ('main','corr','base','remainder')}
    F={name:[compact(v) for v in low['far_z_source_upper'][name]] for name in G}
    if any(len(G[name])!=N or any(len(r)!=N for r in G[name]) or len(F[name])!=N for name in G):
        raise ValueError('A complete four-family matrix or far row is absent')
    H=[[arb(0) for _ in cells] for _ in cells];count=0
    for row in middle['gamma_rows']:
        k=row['output_cell']-12
        for source in row['sources']:
            n=source['source_cell']-12
            if not 0<=k<=n<N:raise ValueError('The high causal order differs')
            H[k][n]=ball(source['gamma']).upper();count+=1
    if count!=N*(N+1)//2:raise ValueError('The complete high triangle is required')
    if [r['cell'] for r in den['rows']]!=cells or [r['cell'] for r in lifts['parameter_cell_lift']]!=cells:
        raise ValueError('A physical source cell is omitted')
    A=[ball(r['V_over_w_upper']).upper() for r in den['rows']]
    l=[ball(r['l']).upper() for r in lifts['parameter_cell_lift']]
    e=ball(lifts['parameter_far_lift']).upper();gamma=ball(den['gamma_high']).upper()
    radius=[ball(r['radius']).lower() for r in joint['rows']]
    images=[ball(r['image']).upper() for r in joint['rows']]
    slack=[ball(r['map_slack']).lower() for r in joint['rows']]
    if not all(v>0 for v in radius) or not all(v>0 for v in slack):raise ValueError('The original strict inclusion margin is absent')
    t=[(radius[n]+radius[N+n]+radius[inf]).upper() for n in range(N)]
    c=[arb(0) for _ in range(dim)]
    slopes=[(3*(1+rho.upper())+216*a*(1+rho.upper())**2).upper() for a in A]
    # The remainder kernel already contains pointwise V/w; do not multiply it again.
    for k in range(N):
        c[k]=sum(((G['main'][k][n]+3*G['corr'][k][n]+3*rho.upper()*G['base'][k][n]
                   +216*(1+rho.upper())**2*G['remainder'][k][n])*l[n] for n in range(N)),arb(0)).upper()
        c[N+k]=sum((H[k][n]*slopes[n]*l[n] for n in range(k,N)),arb(0)).upper()
    c[inf]=(gamma*sum((slopes[n]*l[n] for n in range(N)),arb(0))).upper()
    c[zi]=(sum(((F['main'][n]+3*F['corr'][n]+3*rho.upper()*F['base'][n]
                +216*(1+rho.upper())**2*F['remainder'][n])*l[n] for n in range(N)),arb(0))/Z.lower()+e).upper()
    limits=[(arb(1),'unit_parameter_ball',None)]
    for n in range(N):
        if l[n]>0:
            limits.append((((rho.lower()-t[n])/l[n]).lower(),'total_state_rho',cells[n]))
            limits.append((((1/(64*A[n])-1-t[n])/l[n]).lower(),'complete_mean_domain',cells[n]))
    for i in range(dim):
        if c[i]>0:limits.append(((slack[i]/c[i]).lower(),'map_slack',i))
    if not all(v[0]>0 for v in limits):raise ArithmeticError('An original strict parameter margin is absent')
    chosen=min(limits,key=lambda row:row[0]);bound=(chosen[0]/2).lower()
    mantissa,exponent=bound.man_exp();log2=int(mantissa).bit_length()-1+int(exponent)
    R=power2(log2)
    if not 0<R<=bound:raise ArithmeticError('The inward dyadic parameter radius failed')
    lifted_t=[(t[n]+R*l[n]).upper() for n in range(N)]
    lifted_image=[(images[i]+R*c[i]).upper() for i in range(dim)]
    gates=dict(positive_dyadic_parameter_radius=R>0,
        all46_parameter_units_positive=len(lifts['parameter_units'])==46 and all(ball(v).lower()>0 for v in lifts['parameter_units']),
        all428_lifted_map_inclusions=all(lifted_image[i]<radius[i] for i in range(dim)),
        all213_lifted_total_states_below_original_rho=all(v<rho.lower() for v in lifted_t),
        all213_complete_mean_domains=all((A[n]*(1+lifted_t[n])).upper()<arb(1)/64 for n in range(N)),
        original_full_far_domain=ball(joint['auxiliary_far_z']).upper()+Z.upper()*radius[zi]<Z.lower(),
        original_joint_metric_still_strict=ball(joint['maximum_joint_Lipschitz']).upper()<1)
    result=dict(status='Positive full46 true-head parameter ball paid from the original strict428 certificate' if all(gates.values()) else 'Actual parameter-ball attempt completed with explicit failed gates',
        all_gates=all(gates.values()),gates=gates,parameter_radius=ball_record(R),parameter_radius_log2=log2,
        parameter_units=lifts['parameter_units'],parameter_norm=lifts['norm'],
        original_radii_unchanged=True,original_J_and_W_unchanged=True,
        domain_reason='All lifted total states remain below the original rho and inside A_n*(1+t_n+R*l_n)<1/64; the same complete positive derivative matrix therefore applies throughout the parameter ball.',
        limiting_constraint=dict(kind=chosen[1],cell_or_row=chosen[2],unhalved_upper_radius=ball_record(chosen[0])),
        original_joint_Lipschitz=joint['maximum_joint_Lipschitz'],
        rows=[dict(index=i,block=joint['rows'][i]['block'],cell=joint['rows'][i]['cell'],
                   parameter_column=ball_record(c[i]),lifted_image=ball_record(lifted_image[i]),
                   retained_map_slack=ball_record((radius[i]-lifted_image[i]).lower())) for i in range(dim)],
        cells=[dict(cell=n,lifted_total_radius=ball_record(lifted_t[k]),
                    full_mean_domain=ball_record((A[k]*(1+lifted_t[k])).upper())) for k,n in enumerate(cells)],
        input_hashes=hashes,source_hashes={name:sha(Path(__file__).with_name(name).read_bytes()) for name in
            (Path(__file__).name,'closure_real_head_source_enclosure.py','closure_real_head_green_enclosure.py')},
        inverse_solves=0,radial_integrations=0,new_fixed_point_proposals=0,
        limits=['This pays the inner node12-to-cuff parameter family only. The continuous outer0..11 and full strong-prefix matching remain separate.',
                'All high shallow heights are actual outputs; no zero high Dirichlet data have been imposed.'],
        elapsed_seconds=time.monotonic()-started,peak_RSS_KiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    payload=gzip.compress((json.dumps(result,separators=(',',':'))+'\n').encode(),mtime=0)
    if len(payload)>=5_000_000:raise ArithmeticError('Repository file cap exceeded')
    args.out.write_bytes(payload)
    print(json.dumps(dict(event='done',all_gates=all(gates.values()),gates=gates,
        parameter_radius_log2=log2,output=str(args.out),sha256=sha(payload),bytes=len(payload),
        seconds=result['elapsed_seconds'],RSS_KiB=result['peak_RSS_KiB'])),flush=True)
    if not all(gates.values()):raise SystemExit(1)


if __name__=='__main__':main()
