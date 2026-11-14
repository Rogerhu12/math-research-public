#!/usr/bin/env python3
"""Assemble all213 real low46 four-family Green matrices and far-z rows.

Recovered after the second executor loss.  The mathematical assembly below
is transcribed from the complete pre-loss tool read.  The final output
serialization is reconstructed, so this file has a NEW source hash; it
does not masquerade as the previous 7ae887b4974b9e2897625030b77b9da74befbc5c57356e19753f3763fd66b8b1.
All numerical output must be regenerated with a fresh prefix.
Original author: exact_closure (GPT-6 Astra Pro, AI-assisted), 2026-11-12.
Observer additions: /root (GPT-6 Astra Pro, AI-assisted), 2026-11-13.
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
    inverse_unimodular,maximum,ceil_log2_upper)
from closure_projective_interval_column import ProjectiveColumn


FAMILIES=('main','corr','base','remainder')


def sha(raw):return hashlib.sha256(raw).hexdigest()


def compact_upper(x,bits=24):
    y=x.upper()
    if not y>=0:raise ArithmeticError('A negative positive-kernel bound')
    if y==0:return [0,0]
    m,e=y.man_exp();m=int(m);e=int(e);shift=max(m.bit_length()-bits,0)
    q=(m+(1<<shift)-1)>>shift; e+=shift
    if q==1<<bits:q>>=1;e+=1
    return [q,e]


def positive_min(a,b):return min(a.upper(),b.upper())


def main():
    p=argparse.ArgumentParser(description=__doc__)
    for name in ('columns','ordered','density','reference','box','ready','panel-summary','low-far-lift','out-prefix'):
        p.add_argument('--'+name,type=Path,required=True)
    p.add_argument('--height-response',type=Path)
    args=p.parse_args();ctx.prec=192;started=time.monotonic()
    out=args.out_prefix.with_name(args.out_prefix.name+'.json.gz')
    summary_path=args.out_prefix.with_name(args.out_prefix.name+'-summary.json')
    if out.exists() or summary_path.exists():raise FileExistsError('Use a fresh complete-output prefix')
    docs={};hashes={}
    for name in ('columns','ordered','density','reference','box','ready','panel_summary','low_far_lift'):
        path=getattr(args,name);docs[name],raw=load_json(path);hashes[str(path)]=sha(raw)
    D=docs['columns'];O=docs['ordered'];P=docs['density'];R=docs['reference'];X=docs['box']
    S=docs['panel_summary'];L=docs['low_far_lift'];ready=docs['ready'];cells=list(range(12,225));N=len(cells)
    if D['modes']!=list(range(2,93,2)) or S['modes']!=D['modes']:
        raise ValueError('The complete actual46-mode panel window is required')
    for name in ('columns','ordered','density','reference','box','ready'):
        if hashes[str(getattr(args,name))] not in S['input_hashes'].values():
            raise ValueError('Completed panels use different source/domain inputs')
    for name in ('reference','box'):
        if hashes[str(getattr(args,name))] not in P['input_hashes'].values():
            raise ValueError('The physical envelope belongs to another auxiliary centre')
    if hashes[str(args.ready)] not in D['input_hashes'].values():raise ValueError('The real background differs')
    if not all(P['gates'].values()) or not all(X['gates'].values()) or not all(L['gates'].values()):
        raise ValueError('An auxiliary domain or its real low far lift is unpaid')
    for name in ('reference','box'):
        if hashes[str(getattr(args,name))] not in L['input_hashes'].values():raise ValueError('The auxiliary far bound belongs to another box')
    if [r['cell'] for r in P['rows']]!=cells or [r['cell'] for r in R['cell_rows']]!=cells:
        raise ValueError('All213 physical source cells are required')
    if [r['cell'] for r in X['rows']]!=cells:raise ValueError('The auxiliary box is incomplete')
    qcut={r['mode']:abs(ball(r['reference_Q'])).upper() for r in D['endpoint_rows']}
    if args.height_response:
        H,raw=load_json(args.height_response);hh=sha(raw);hashes[str(args.height_response)]=hh
        if hh not in R['input_hashes'].values():raise ValueError('Actual full heights differ')
        actual=H['response']['endpointCanonicalTrace']
        if actual['physicalNode']!=12 or len(actual['Q'])>46:raise ValueError('Actual full height window differs')
        qcut={m:abs(exact_q(actual['Q'][m//2-1])).upper() if m//2<=len(actual['Q']) else arb(0) for m in D['modes']}
    params=ready['rationalDeepModel']['physicalParameters'];rc=exact_q(params['rCuff'])
    eps=exact_q(params['epsilonScale'])/rc**7;ln2=arb(2).log();rho=(arb(11)*ln2/4).exp()
    delta=exact_q(params['delta0'])*power2(-224);Sf=eps/rc**3*(arb(11)*delta.log()/2).exp()
    sq12=arb(12).sqrt();rmax=rc*arb(257)/256
    tauin=[ball(r['tau_inner']).upper() for r in P['rows']]
    tauout=[ball(r['tau_outer']).lower() for r in P['rows']]
    tauref=[ball(r['tau']).lower() for r in R['cell_rows']]
    Xbar=[ball(r['canonical_total_envelope']).upper() for r in P['rows']]
    B=[ball(r['B']).upper() for r in P['rows']];a=[ball(r['Q_coefficient']).upper() for r in P['rows']]
    Astar=[ball(r['V_over_w_upper']).upper() for r in P['rows']]
    J=[]
    for k,row in enumerate(P['rows']):
        mu=ball(row['mu_lower']).lower();muup=ball(row['mu_upper']).upper();wmin=ball(row['w_lower']).lower()
        Vsup=(Xbar[k]*(a[k]*rmax**3+sq12*muup/(rc**4*wmin))).upper()
        cint=(ball(row['normalized_width_upper']).upper()+ball(row['TV_log_w_upper']).upper()).upper()
        J.append((rmax**4*Vsup**2*cint/(sq12*mu)).upper())
    refined={(r['mode'],c['cell']):c for r in O['mode_rows'] for c in r['refined_cells']}
    panelrows={};panel_hashes={};panel_cells=[];profiles={}
    for ref in S['cells']:
        path=Path(ref['path']);data,raw=load_json(path)
        if sha(raw)!=ref['sha256']:raise ValueError('A completed panel package changed')
        if data['modes']!=D['modes']:raise ValueError('A completed cell omits low frequencies')
        for name in ('columns','density','reference','box','ready'):
            if hashes[str(getattr(args,name))] not in data['input_hashes'].values():raise ValueError('A cell panel has a different domain')
        n=data['cell'];panel_cells.append(n);profiles[n]=data['profiles'];panel_hashes[str(path)]=sha(raw)
        for row in data['rows']:panelrows[(row['mode'],n)]=row
    if sorted(panel_cells)!=list(range(12,24)):raise ValueError('The precise shallow-head coverage must include cells12..23')
    # Compute the true canonical masses of the main and remaining linear
    # modes.  They are independent of the later output Green mode.
    R2=[arb(0) for _ in cells];Rother=[arb(0) for _ in cells];group_hashes={}
    for gr in D['column_groups']:
        group,raw=load_json(Path(gr['path']));digest=sha(raw)
        if digest!=gr['sha256']:raise ValueError('A true column group changed')
        group_hashes[gr['path']]=digest
        for j,m in enumerate(group['modes']):
            e=group['endpoint_rows'][j];lo=endpoint(e['Q_gain']['lower']);hi=endpoint(e['Q_gain']['upper'])
            if not(lo>0 or hi<0):raise ArithmeticError('The exact height chart contains zero')
            gain=lo if lo>0 else -hi
            for k,row in enumerate(group['cell_rows']):
                linear=row['linear_rows'][j];q=ball(linear['column_Q_sup']).upper()/gain;xi=ball(linear['column_Xi_sup']).upper()/gain
                old=refined.get((m,row['cell']))
                if old:
                    q=positive_min(q,ball(old['refined_phi_Q_sup']));xi=positive_min(xi,ball(old['refined_phi_Xi_sup']))
                value=(qcut[m]*((1+m)**3*q+(1+m)*xi)*(m*tauref[k]).exp()).upper()
                if m==2:R2[k]=value
                else:Rother[k]=(Rother[k]+value).upper()
    rest=[];factors={name:[] for name in FAMILIES};source_profiles=[]
    for k,n in enumerate(cells):
        if not tauref[k]>=tauin[k]:raise ArithmeticError('The wider centre strip was lost')
        rest.append((Rother[k]+ball(X['rows'][k]['correction_radius_multiple']).upper()*ball(R['cell_rows'][k]['reference_X']).upper()).upper())
        cauchy=(-2*(tauref[k]-tauin[k])).exp().upper()
        main=(3*R2[k]/Xbar[k]*cauchy).upper();corr=(rest[k]/Xbar[k]*cauchy).upper()
        for key,value in [('main',main),('corr',corr),('base',arb(1)),('remainder',Astar[k])]:factors[key].append(value)
        source_profiles.append(dict(cell=n,Xbar=ball_record(Xbar[k]),canonical_m2=ball_record(R2[k]),
            canonical_rest=ball_record(rest[k]),whole_cell_main_coefficient=ball_record(main),
            whole_cell_corr_coefficient=ball_record(corr),Astar=ball_record(Astar[k]),
            tau_inner=P['rows'][k]['tau_inner'],tau_outer=P['rows'][k]['tau_outer'],
            canonical_source_integral=ball_record(J[k]),
            source_material='Exact ordered source panels' if n in panel_cells else 'Whole-cell real positive source material and constant wide-centre mass bound'))
    gamma={name:[[arb(0) for _ in cells] for _ in cells] for name in FAMILIES}
    witnesses={name:[[0 for _ in cells] for _ in cells] for name in FAMILIES}
    far={name:[arb(0) for _ in cells] for name in FAMILIES}
    boundary=[arb(0) for _ in cells];boundary_z=arb(0);radius_rows=None
    modal_observer=[]
    for gr in D['column_groups']:
        group,raw=load_json(Path(gr['path']))
        if sha(raw)!=gr['sha256']:raise ValueError('A true column group changed during assembly')
        rows=group['cell_rows'];radius_rows=rows
        mu=[ball(r['mu']) for r in rows];ratios=[v/mu[0] for v in mu]
        for j,m in enumerate(group['modes']):
            e=group['endpoint_rows'][j];lo=endpoint(e['Q_gain']['lower']);hi=endpoint(e['Q_gain']['upper']);gain=lo if lo>0 else -hi
            u=m*m-4;phiQ=[];phiXi=[];psiQ=[];psiXi=[]
            psi=ProjectiveColumn([arb(0),(ball(rows[0]['r_outer'])/rc)**u])
            for k,row in enumerate(rows):
                lin=row['linear_rows'][j];phiQ.append(ball(lin['column_Q_sup']).upper()/gain);phiXi.append(ball(lin['column_Xi_sup']).upper()/gain)
                r=ball(row['r_inner']).union(ball(row['r_outer']));within=mv(mat(lin['gauge_backward_majorant']),psi.absolute_uppers())
                psiQ.append(abs((r/rc)**u).upper()*within[0]);psiXi.append(abs((rc/r)**u).upper()*within[1])
                cap=refined.get((m,row['cell']))
                if cap:
                    phiQ[-1]=positive_min(phiQ[-1],ball(cap['refined_phi_Q_sup']));phiXi[-1]=positive_min(phiXi[-1],ball(cap['refined_phi_Xi_sup']))
                    psiQ[-1]=positive_min(psiQ[-1],ball(cap['refined_psi_Q_sup']));psiXi[-1]=positive_min(psiXi[-1],ball(cap['refined_psi_Xi_sup']))
                psi.advance(inverse_unimodular(mat(lin['gauge_matrix'])))
                if k+1<N:psi.multiply_component(1,rho)
            PH=[];PS=[];Iphi={name:[] for name in FAMILIES};Ipsi={name:[] for name in FAMILIES};diag={name:[] for name in FAMILIES}
            for k,n in enumerate(cells):
                angle=(m*tauin[k]).exp().upper();inverse=(-m*tauout[k]).exp().upper()
                cp=(1+m)*B[k]*m/(Xbar[k]*a[k]);cq=(1+m)*m*m/(Xbar[k]*a[k]);cx=(1+m)/Xbar[k]
                php=cp*phiQ[k]*angle;phk=(cq*phiQ[k]+cx*phiXi[k])*angle
                psp=cp*psiQ[k]*angle;psk=(cq*psiQ[k]+cx*psiXi[k])*angle
                cap=panelrows.get((m,n))
                if cap:
                    php=positive_min(php,ball(cap['phi_physical_p_sup']));phk=positive_min(phk,ball(cap['phi_physical_kappa_sup']))
                    psp=positive_min(psp,ball(cap['psi_physical_p_sup']));psk=positive_min(psk,ball(cap['psi_physical_kappa_sup']))
                PH.append((php+phk).upper());PS.append((psp+psk).upper())
                rawdiag=ratios[k]*((cp+cq)*phiQ[k]*psiQ[k]+cx*maximum(phiXi[k]*psiQ[k],psiXi[k]*phiQ[k]))*angle*inverse
                for name in FAMILIES:
                    material=J[k]*factors[name][k]
                    ip=phiQ[k]*material*inverse;isp=psiQ[k]*material*inverse;local=rawdiag*material
                    if cap:
                        ip=positive_min(ip,ball(cap[name]['phi_Q_source_integral']))
                        isp=positive_min(isp,ball(cap[name]['psi_Q_source_integral']))
                        local=positive_min(local,ball(cap[name]['ordered_diagonal']))
                    Iphi[name].append(ip.upper());Ipsi[name].append(isp.upper());diag[name].append(local.upper())
                boundary[k]=maximum(boundary[k],ratios[-1]/gain*Sf*(arb(-38*m)).exp()*PS[k])
            modal_observer.append(dict(mode=m, cells=cells,
                phi_target_strong=[ball_record(z.upper()) for z in PH],
                psi_target_strong=[ball_record(z.upper()) for z in PS],
                mu_ratio=[ball_record(z.upper()) for z in ratios],
                base_phi_source=[ball_record(z.upper()) for z in Iphi['base']],
                base_psi_source=[ball_record(z.upper()) for z in Ipsi['base']],
                base_ordered_diagonal=[ball_record(z.upper()) for z in diag['base']],
                far_source=[ball_record((ratios[n]/gain*Ipsi['base'][n]*(arb(38*m)).exp()/Sf).upper()) for n in range(N)],
                far_homogeneous=[ball_record((ratios[-1]/gain*Sf*(arb(-38*m)).exp()*PS[k]).upper()) for k in range(N)],
                source_material='original q d=Vq^2/(r*w)+abs(w_r/w)*Vq^2/w; no nonlinear multiplier',
                field_norm='original q continuous strip, strong physical P+K divided by Vq',
                field_kernel_rule='diagonal=base_ordered_diagonal[k]; k>n uses mu_ratio[n]*phi_target_strong[k]*base_psi_source[n]; k<n uses mu_ratio[n]*psi_target_strong[k]*base_phi_source[n]',
                observer_only=True, no_new_ODE_or_integral=True))
            for name in FAMILIES:
                matrix=gamma[name];witness=witnesses[name]
                for k in range(N):
                    for n in range(N):
                        value=diag[name][k] if k==n else (ratios[n]*(PH[k]*Ipsi[name][n] if k>n else PS[k]*Iphi[name][n])).upper()
                        if value>matrix[k][n]:matrix[k][n]=value;witness[k][n]=m
                for n in range(N):
                    far[name][n]=maximum(far[name][n],ratios[n]/gain*Ipsi[name][n]*(arb(38*m)).exp()/Sf)
            rfar=ball(rows[-1]['r_inner']);psi_far_Q=abs((rfar/rc)**u).upper()*psi.absolute_uppers()[0]
            boundary_z=maximum(boundary_z,ratios[-1]/gain*psi_far_Q)
        print(json.dumps(dict(event='group',modes=group['modes'],seconds=time.monotonic()-started,
            diagonal_log2={name:max(ceil_log2_upper(gamma[name][k][k]) for k in range(N)) for name in FAMILIES},
            RSS_KiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)),flush=True)
    row_summaries=[]
    for k,n in enumerate(cells):
        r=dict(cell=n,r_inner=radius_rows[k]['r_inner'],r_outer=radius_rows[k]['r_outer'],
            B_low=ball_record(boundary[k]),families={})
        for name in FAMILIES:
            worst=max(range(N),key=lambda j:gamma[name][k][j])
            r['families'][name]=dict(diagonal=ball_record(gamma[name][k][k]),
                diagonal_mode=witnesses[name][k][k],row_sum=ball_record(sum(gamma[name][k],arb(0))),
                largest_source_cell=cells[worst],largest_source_mode=witnesses[name][k][worst],
                largest_entry=ball_record(gamma[name][k][worst]))
        row_summaries.append(r)
    source_names=[Path(__file__).name,'closure_real_head_source_enclosure.py',
        'closure_real_head_green_enclosure.py','closure_projective_interval_column.py']
    result=dict(status='Complete certified real low46 four-family Green matrices; a joint nonlinear box is a separate next gate',
        cells=cells,modes=D['modes'],full_range_covered=True,exact_panel_cells=sorted(panel_cells),
        whole_cell_cells=list(range(24,225)),gamma_upper={name:[[compact_upper(x) for x in row] for row in gamma[name]] for name in FAMILIES},
        far_z_source_upper={name:[compact_upper(x) for x in far[name]] for name in FAMILIES},
        compact_number='Each [mantissa,binary_exponent] is the exact nonnegative dyadic upper bound mantissa*2^binary_exponent; at most24 mantissa bits, upward relative inflation <=2^-23.',
        family_meanings=dict(main='Full DQ factor2 included for the actual true linear m2 centre.',
            corr='epsilon*d only; multiply by3 for the other complete auxiliary centre.',
            base='d; perturbation quadratic map1.5*t^2 and derivative3*t.',
            remainder='(V/w)*d; complete mean/inverse remainder derivative216*X^2.'),
        source_profiles=source_profiles,rows=row_summaries,E_B_low=ball_record(boundary_z),
        far_scale_S=ball_record(Sf),far_strip=38,far_physical_node=225,
        auxiliary_far_z_bound=L['far_z_dyadic_bound'],raw_D_constant=L['raw_D_constant'],
        input_hashes=hashes,panel_hashes=panel_hashes,group_hashes=group_hashes,
        source_hashes={n:sha(Path(__file__).with_name(n).read_bytes()) for n in source_names},
        elapsed_seconds=time.monotonic()-started,peak_RSS_KiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
        limits=['The complete low centre has been shifted out exactly; no pure-low residual is inserted into the correction equation.',
            'Every low mode and every source/target cell is retained; compact dyadics are upward bounds.',
            'A full joint low/middle/infinite/far box remains a separate numerical and mathematical gate.',
            'The actual far evaluation is computed directly and does not upgrade a narrow physical norm for free.',
            'This source was recovered with a new SHA after executor replacement; every output uses fresh computation.'])
    original_proved, original_raw = load_json(Path('notes/2026-11-12-closure-recovery2-centred-four-green-r1.json.gz'))
    if sha(original_raw) != '31c65d6c8053325502542c008720f880d7386cd39168be79ca466851e76bb7ee':
        raise ArithmeticError('Original complete aggregate identity changed')
    for key in ('gamma_upper','far_z_source_upper','rows','source_profiles','E_B_low'):
        if result[key] != original_proved[key]:
            raise ArithmeticError('Observer modified original exact aggregate: '+key)
    result['all_original_aggregate_math_fields_bitwise_identical'] = True
    result['original_aggregate_sha256'] = sha(original_raw)
    result['original_producer_sha256'] = '9e420455ef59285219422bdbd1fc82d7d3f15a2af9178a25fd89a2c86faee809'
    result['modal_observer'] = modal_observer
    result['observer_source_sha256'] = sha(Path(__file__).read_bytes())
    payload=gzip.compress((json.dumps(result,separators=(',',':'))+'\n').encode(),mtime=0)
    if len(payload)>=5_000_000:raise ArithmeticError('Repository file size cap exceeded')
    out.write_bytes(payload)
    summary={k:v for k,v in result.items() if k not in ('gamma_upper','source_profiles','rows')}
    summary.update(output=str(out),output_sha256=sha(payload),bytes=len(payload),
        worst_diagonal={name:max(ceil_log2_upper(gamma[name][k][k]) for k in range(N)) for name in FAMILIES},
        first_rows=row_summaries[:3])
    summary_path.write_text(json.dumps(summary,indent=2)+'\n')
    print(json.dumps(dict(event='done',output=str(out),output_sha256=sha(payload),bytes=len(payload),
        worst_diagonal=summary['worst_diagonal'],seconds=result['elapsed_seconds'],
        RSS_KiB=result['peak_RSS_KiB'])),flush=True)


if __name__=='__main__':main()
