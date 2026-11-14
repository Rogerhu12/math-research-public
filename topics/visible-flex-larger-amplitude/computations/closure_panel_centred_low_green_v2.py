# Frozen centred-v1 source SHA256 cd2216640b273b75618996eea6ea52026c31246d0fcc749f4f2312612afdd2ee; v2 tightens only PB subpiece real radii and saves completed modal recovery rows.
#!/usr/bin/env python3
"""All-low-mode real Green ledgers centred on the proved auxiliary field.

Four source families are retained separately: the exact linear m2 centre's
quadratic derivative; the wide canonical centre remainder profile epsilon;
the unweighted quadratic material; and that material times V/w for the
complete mean/inverse remainder.  No incomplete Jacobian is called closed.
Author: exact_closure (GPT-6 Astra Pro, AI-assisted), 2026-11-12.
"""
import argparse
import gc
import gzip
import hashlib
import json
from pathlib import Path
import resource
import time
from flint import arb, ctx
from closure_real_head_source_enclosure import RealHead, exact_q, power2, ball_record
from closure_real_linear_head_enclosure import PositiveKernels
from closure_real_head_green_enclosure import load_json, ball, maximum, ceil_log2_upper
from closure_weighted_panel_low_green_v3 import (seed_columns,
    column_panel_bounds, physical_caps, small_record)
from closure_weighted_panel_flow_v4 import prepare_cell


def sha(raw): return hashlib.sha256(raw).hexdigest()


def ordered_family(ph, ps, phi, psi, weights, ratio):
    iphi = [(q[0]*v).upper() for q,v in zip(phi,weights)]
    ipsi = [(q[0]*v).upper() for q,v in zip(psi,weights)]
    suffix = [arb(0)]*(len(weights)+1)
    for j in range(len(weights)-1,-1,-1): suffix[j]=(suffix[j+1]+ipsi[j]).upper()
    prefix=arb(0); pmax=arb(0); kmax=arb(0)
    for j in range(len(weights)):
        prefix=(prefix+iphi[j]).upper()
        pmax=maximum(pmax,ph[j][0]*suffix[j]+ps[j][0]*prefix)
        kmax=maximum(kmax,ph[j][1]*suffix[j]+ps[j][1]*prefix)
    diagonal=(ratio*(pmax+kmax)).upper()
    return dict(phi_Q_source_integral=small_record(prefix),psi_Q_source_integral=small_record(suffix[0]),
        ordered_diagonal=small_record(diagonal),ordered_diagonal_log2_upper=ceil_log2_upper(diagonal))


def prepare_profiles(kernels,n,parents,material,density,reference,box,seeds,qcut):
    X=ball(density['canonical_total_envelope']); B=ball(density['B'])
    a=ball(density['Q_coefficient']); mu_bar=ball(density['mu_upper'])
    mu=seeds[2]['cells'][n]['mu']; root=arb(12).sqrt(); tau_ref=ball(reference['tau'])
    rest=ball(box['correction_radius_multiple']).upper()*ball(reference['reference_X']).upper()
    non2=arb(0)
    for m in qcut:
        if m==2 or not qcut[m]>0: continue
        cq,cx=seeds[m]['cells'][n]['phi_caps']
        non2+=(qcut[m]*((1+m)**3*cq+(1+m)*cx)*(m*tau_ref).exp()).upper()
    rest=(rest+non2).upper()
    centre=column_panel_bounds(kernels,parents,2,seeds[2]['cells'][n],seeds[2]['gain_lower'],True)
    epsmax=arb(0); astar=arb(0); mainmax=arb(0)
    for panel,raw,(q,xi) in zip(parents,material['panels'],centre):
        r=panel['radius']; w=panel['w']; V=ball(raw['V'])
        # Pointwise r^3/V and sqrt12 mu/(r^4 w V), with the two
        # positive summands of the SAME V kept in their exact ratio.
        yl=a.lower()*r.lower()**7*w.lower(); yu=a.upper()*r.upper()**7*w.upper()
        D=root*mu_bar
        tlo=(yl/(yl+D.upper())).lower(); thi=(yu/(yu+D.lower())).upper()
        rq=thi/(X.lower()*a.lower())
        rx=(mu.upper()/mu_bar.lower())*(1-tlo)/X.lower()
        Q=q*qcut[2]; Xi=xi*qcut[2]
        angular=(2*panel['tau'].upper()).exp().upper()
        U2=((4*rq*Q+rx*Xi)*angular).upper()
        S=(4*rq*Q*angular).upper(); T=(2*rq*Q*angular).upper()
        A=(2*(3*rq*Q+rx*Xi)*angular).upper()
        C=(rx*Xi*angular).upper()  # exact Q cancellation in C
        w2=(w.upper()**2).upper(); E=1+w2
        if not w2<=arb(1)/4: raise ArithmeticError('The quadratic material constant3 is unpaid')
        cdelta=max(arb(1)/3,1/B.lower())
        g1=(2*E*A).upper()
        gl=(2*(C*cdelta+w2*(U2/B.lower()+S/3+S/B.lower()+T/(3*B.lower())))).upper()
        material_factor=(r.upper()**4*V.upper()**2/(root*mu.lower())).upper()
        J1=(material_factor*ball(raw['radial_log_increment']).upper()).upper()
        Jl=(material_factor*ball(raw['log_w_variation']).upper()).upper()
        if not tau_ref.lower()>=panel['tau'].upper(): raise ArithmeticError('The wider canonical centre strip is unavailable')
        eps=(rest/X.lower()*(-2*(tau_ref.lower()-panel['tau'].upper())).exp()).upper()
        av=ball(raw['V_over_w']).upper()
        panel.update(main_material=(J1*g1+Jl*gl).upper(),
            corr_material=(panel['J']*eps).upper(),
            remainder_material=(panel['J']*av).upper(),
            main_radial_material=(J1*g1).upper(),main_log_material=(Jl*gl).upper())
        epsmax=maximum(epsmax,eps); astar=maximum(astar,av); mainmax=maximum(mainmax,g1+gl)
    return centre,dict(canonical_auxiliary_correction=small_record(ball(box['correction_radius_multiple']).upper()*ball(reference['reference_X']).upper()),
        canonical_other_linear_modes=small_record(non2),canonical_rest=small_record(rest),
        physical_rest_profile_max=small_record(epsmax),V_over_w_max=small_record(astar),
        main_profile_max=small_record(mainmax),centre_m2_Q_plain_cosine=small_record(qcut[2]),
        convention='The centre hats are FULL cosine/sine amplitudes including exp(2 tau); factor2 in DQ is retained in g1/gl. The two signed centre halves give a common frequency mass convolution of total at most one.')


def evaluate_mode(kernels,parents,m,seed,gain,density,centre2):
    phi=centre2 if m==2 else column_panel_bounds(kernels,parents,m,seed,gain,True)
    psi=column_panel_bounds(kernels,parents,m,seed,gain,False)
    X=ball(density['canonical_total_envelope']); B=ball(density['B'])
    a=ball(density['Q_coefficient']); mu_bar=ball(density['mu_upper'])
    ph=[]; ps=[]; weights={name:[] for name in ('main','corr','base','remainder')}
    for panel,pq,sq in zip(parents,phi,psi):
        ph.append(physical_caps(panel,*pq,m,X,B,a,seed['mu'],mu_bar))
        ps.append(physical_caps(panel,*sq,m,X,B,a,seed['mu'],mu_bar))
        inverse_angle=(-m*panel['tau'].lower()).exp().upper()
        for name,key in [('main','main_material'),('corr','corr_material'),('base','J'),('remainder','remainder_material')]:
            weights[name].append((panel[key]*inverse_angle).upper())
    result=dict(mode=m,phi_physical_p_sup=small_record(max(x[0] for x in ph)),
        phi_physical_kappa_sup=small_record(max(x[1] for x in ph)),
        psi_physical_p_sup=small_record(max(x[0] for x in ps)),
        psi_physical_kappa_sup=small_record(max(x[1] for x in ps)),
        phi_Q_sup=small_record(max(x[0] for x in phi)),psi_Q_sup=small_record(max(x[0] for x in psi)),
        gain_lower=small_record(gain),mu_ratio=small_record(seed['mu_ratio']))
    for name,values in weights.items(): result[name]=ordered_family(ph,ps,phi,psi,values,seed['mu_ratio'])
    return result


def main():
    p=argparse.ArgumentParser(description=__doc__)
    for name in ('columns','ordered','density','reference','box','ready','panels-summary','out-prefix'):
        p.add_argument('--'+name,type=Path,required=True)
    p.add_argument('--height-response',type=Path)
    p.add_argument('--first-cell',type=int,default=12)
    p.add_argument('--last-cell',type=int,default=23)
    p.add_argument('--only-mode',type=int)
    args=p.parse_args();ctx.prec=192;started=time.monotonic()
    docs={};hashes={}
    for name in ('columns','ordered','density','reference','box','ready','panels_summary'):
        path=getattr(args,name);docs[name],raw=load_json(path);hashes[str(path)]=sha(raw)
    D=docs['columns'];O=docs['ordered'];P=docs['density'];R=docs['reference'];X=docs['box'];S=docs['panels_summary']
    if D['modes']!=list(range(2,93,2)):raise ValueError('All46 actual modal columns are required')
    if hashes[str(args.columns)]!=O['input_hashes'].get(str(args.columns)):
        raise ValueError('The true column set differs')
    for name in ('density','ready'):
        if hashes[str(getattr(args,name))] not in S['input_hashes'].values():raise ValueError('Panel source/density identity differs')
    if hashes[str(args.ready)] not in D['input_hashes'].values():raise ValueError('Real backgrounds differ')
    for name in ('reference','box'):
        if hashes[str(getattr(args,name))] not in P['input_hashes'].values():raise ValueError('The physical centre box differs')
    if hashes[str(args.reference)] not in X['input_hashes'].values():raise ValueError('The centre and its auxiliary box differ')
    if not all(P['gates'].values()) or not all(X['gates'].values()):raise ValueError('The existing centre domain is unpaid')
    qcut={r['mode']:abs(ball(r['reference_Q'])).upper() for r in D['endpoint_rows']}
    if args.height_response:
        H,raw=load_json(args.height_response);hsha=sha(raw);hashes[str(args.height_response)]=hsha
        if hsha not in R['input_hashes'].values():raise ValueError('The rebased reference does not certify these full actual heights')
        actual=H['response']['endpointCanonicalTrace']
        if actual['physicalNode']!=12:raise ValueError('The actual heights are at another port')
        if len(actual['Q'])>46:raise ValueError('The actual height vector exceeds the paid low window')
        qcut={m:abs(exact_q(actual['Q'][m//2-1])).upper() if m//2<=len(actual['Q']) else arb(0) for m in D['modes']}
    if not 12<=args.first_cell<=args.last_cell<=23:raise ValueError('Expected cells12..23')
    selected=set(range(args.first_cell,args.last_cell+1));modes=D['modes']
    if args.only_mode is not None:
        if args.only_mode not in modes:raise ValueError('Mode outside the real low window')
        modes=[args.only_mode]
    head=RealHead(docs['ready'],start=12,far=159,exact_through=23);kernels=PositiveKernels(head,225,92)
    refined={(r['mode'],c['cell']):c for r in O['mode_rows'] for c in r['refined_cells']}
    seeds,group_hashes=seed_columns(D,selected,head.rc,head.rho,refined)
    if not any(h in S['input_hashes'].values() for h in group_hashes.values()):raise ValueError('True radius anchors differ')
    density={r['cell']:r for r in P['rows']};reference={r['cell']:r for r in R['cell_rows']}
    box={r['cell']:r for r in X['rows']};material_refs={r['cell']:r for r in S['cells']}
    source_names=[Path(__file__).name,'closure_weighted_panel_low_green_v3.py','closure_weighted_panel_flow_v4.py',
        'closure_real_head_source_enclosure.py','closure_real_linear_head_enclosure.py',
        'closure_real_head_green_enclosure.py','closure_projective_interval_column.py']
    source_hashes={n:sha(Path(__file__).with_name(n).read_bytes()) for n in source_names}
    entries=[]
    for n in sorted(selected):
        ref=material_refs[n];material,raw=load_json(Path(ref['file']))
        if sha(raw)!=ref['sha256']:raise ValueError('Material panels changed')
        parents,pieces,product=prepare_cell(kernels,n,material,power2(-20))
        centre2,profiles=prepare_profiles(kernels,n,parents,material,density[n],reference[n],box[n],seeds,qcut)
        del material,raw;gc.collect()
        print(json.dumps(dict(event='prepared',cell=n,panels=len(parents),PB_pieces=pieces,
            seconds=time.monotonic()-started,RSS_KiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)),flush=True)
        rows=[]
        for m in modes:
            print(json.dumps(dict(event='start_mode',cell=n,mode=m,seconds=time.monotonic()-started)),flush=True)
            rows.append(evaluate_mode(kernels,parents,m,seeds[m]['cells'][n],seeds[m]['gain_lower'],density[n],centre2))
            progress=dict(status='Recovery-only completed modal rows, not a full-cell or full-window certificate',
                cell=n,completed_modes=[r['mode'] for r in rows],rows=rows,profiles=profiles,
                input_hashes={**hashes,ref['file']:ref['sha256']},source_hashes=source_hashes,
                elapsed_seconds=time.monotonic()-started)
            progress_path=args.out_prefix.with_name(args.out_prefix.name+f'-cell{n:03d}-progress.json.gz')
            progress_path.write_bytes(gzip.compress((json.dumps(progress,separators=(',',':'))+'\n').encode(),mtime=0))
            if m%16==0 or m==modes[-1]:
                print(json.dumps(dict(event='mode',cell=n,mode=m,
                    diagonal_log2={k:rows[-1][k]['ordered_diagonal_log2_upper'] for k in ('main','corr','base','remainder')},
                    seconds=time.monotonic()-started)),flush=True)
        result=dict(status='Certified centred four-family low Green data; complete coupled box is not asserted',
            cell=n,modes=modes,rows=rows,profiles=profiles,source_panels=len(parents),PB_pieces=pieces,
            maximum_AB=ball_record(product),strip='The original continuous R33 strip, with no affine reweighting.',
            family_meanings=dict(main='DQ of the actual linear m2 centre, bounded with the exact C=Xi identity and two radial materials; its derivative constants are already included.',
                corr='epsilon(r) times d; multiply by3 for DQ of the complete remaining auxiliary centre.',
                base='d=(1/r+abs(lambda))*V^2/w; quadratic perturbation map <=1.5 R^2 and derivative <=3 R.',
                remainder='(V/w)*d; the full mean/inverse remainder derivative is bounded by216 X^2 times this family.'),
            frequency_mass='Main uses the fixed +/-2 convolution; corr uses the fixed canonical centre modal masses. Both have l1 mass at most the input state norm, independent of radius. Taking max over output Green blocks is therefore legitimate.',
            input_hashes={**hashes,ref['file']:ref['sha256']},group_hashes=group_hashes,source_hashes=source_hashes,
            elapsed_seconds=time.monotonic()-started,peak_RSS_KiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
        payload=gzip.compress((json.dumps(result,separators=(',',':'))+'\n').encode(),mtime=0)
        if len(payload)>=5_000_000:raise ArithmeticError('Repository file size cap exceeded')
        path=args.out_prefix.with_name(args.out_prefix.name+f'-cell{n:03d}.json.gz');path.write_bytes(payload)
        entry=dict(cell=n,path=str(path),sha256=sha(payload),bytes=len(payload),
            diagonal_log2={k:max(r[k]['ordered_diagonal_log2_upper'] for r in rows) for k in ('main','corr','base','remainder')})
        entries.append(entry);print(json.dumps(dict(event='cell',**entry,seconds=time.monotonic()-started)),flush=True)
        del parents,centre2;kernels.release_cell(n);gc.collect()
    summary=dict(status='Completed centred four-family real low Green panel export',modes=modes,cells=entries,
        input_hashes=hashes,group_hashes=group_hashes,source_hashes=source_hashes,
        elapsed_seconds=time.monotonic()-started,peak_RSS_KiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    path=args.out_prefix.with_name(args.out_prefix.name+'-summary.json');path.write_text(json.dumps(summary,indent=2)+'\n')
    print(json.dumps(dict(event='done',output=str(path),seconds=summary['elapsed_seconds'],RSS_KiB=summary['peak_RSS_KiB'])),flush=True)


if __name__=='__main__':main()
