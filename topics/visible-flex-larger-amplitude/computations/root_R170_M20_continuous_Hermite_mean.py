#!/usr/bin/env python3
"""Exact-binary continuous strong M20 centre and complete original mean domain.

All 216 polynomial pieces are explicit definitions, not certified ODE traces.
The original 3940 real-background leaves are reused without integration.
Author: /root (GPT-6 Astra Pro; AI-assisted), 2026-11-13.
"""
import argparse
from fractions import Fraction as F
import gzip
import hashlib
import json
from pathlib import Path
import resource
import sys
import time
from flint import arb, ctx, fmpq

MODEL_KEYS=['definition','sourceRevision','sourceHashes','start','deepAlpha','exactSourceConstants','frozenWarpAlpha','headFingerprint']
GEOMETRY_KEYS=['rCut','wCut','width','curvatureBound','delta0','R','a','etaPower','etaRatioAtN0','orientation','prefixR','prefixEnd','prefixReturnStart','protectCell','calibrationSteps','warpSteps','quadratureTolerance','slopeCap','capTransition','capMode','cuspAwareQuadrature','valleyControls','rejoinR20At','rejoinIndexOffset','pulseCaps','valleyCaps','flatOuterThroughCell','flatSlope','flatOuterStartSegment','warpWeightLevels','rCuff','oldCut','epsilonScale','prefixRByCell','constructor']
DEFAULTS=dict(flatOuterThroughCell=None,flatSlope=None,flatOuterStartSegment=2,rejoinR20At=None,rejoinIndexOffset=4,pulseCaps=None,valleyCaps=None,warpWeightLevels=[])

def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def read(p):
    p=Path(p);raw=p.read_bytes()
    return json.loads(gzip.decompress(raw) if p.suffix=='.gz' else raw)
def ar(q):return arb(fmpq(q.numerator,q.denominator))
def endpoint(v):
    m,e=v.man_exp();return [str(m),int(e)]
def rec(v):return dict(lower=endpoint(v.lower()),upper=endpoint(v.upper()))
def ep(v):
    if isinstance(v,list):return arb((int(v[0]),int(v[1])))
    return arb((int(v['mantissa']),int(v['binary_exponent'])))
def ball(v):return ep(v['lower']).union(ep(v['upper']))
def up(v):return v.upper()
def hull(values):
    q=values[0]
    for v in values[1:]:q=q.union(v)
    return q
def split(b,t):
    rows=[b]
    while len(rows[-1])>1:rows.append([(1-t)*a+t*c for a,c in zip(rows[-1],rows[-1][1:])])
    return [r[0] for r in rows],[r[-1] for r in reversed(rows)]
def restrict(b,a,c):
    if a==0 and c==1:return b
    left=split(b,c)[0]
    return left if a==0 else split(left,a/c)[1]
def hermite(v0,v1,d0,d1):
    v0,v1,d0,d1=map(F.from_float,(v0,v1,d0,d1))
    return [v0,v0+d0/3,v1-d1/3,v1]
def derivative(b):return [3*(b[i+1]-b[i]) for i in range(3)]
def f_and_g(q):
    s=(1-q).sqrt()
    return up(q*(2+s)/(2*s*(1+s)**2)),up(q/(s*(1+s)))

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--inputs',type=Path,required=True)
    ap.add_argument('--out-prefix',type=Path,required=True)
    ap.add_argument('--rss-kib',type=int,default=131072)
    a=ap.parse_args();started=time.monotonic();ctx.prec,ctx.threads=256,1
    if any(a.out_prefix.parent.glob(a.out_prefix.name+'*')):raise FileExistsError('Fresh complete result prefix required')
    ids=read(a.inputs);counts={};failures=[]
    def gate(k,v):
        counts[k]=counts.get(k,0)+1
        if not v:raise ArithmeticError(k)
    def mg(k,v,ident):
        counts[k]=counts.get(k,0)+1
        if not v:failures.append(dict(gate=k,**ident))
    for k,r in ids['files'].items():gate('input_identity_'+k,sha(r['path'])==r['sha256'])
    get=lambda k:read(ids['files'][k]['path'])
    jets=get('jets');jres=get('jets_resource');jids=get('jets_inputs')
    gate('actual_owned_jets',jres['exitcode']==0 and jets['all_gates'] and len(jets['pieces'])==216
         and jets['source_sha256']==ids['files']['jets_source']['sha256']
         and jets['input_manifest_sha256']==ids['files']['jets_inputs']['sha256'])
    base=get('original_source_manifest')
    for r in base['source_files']:gate('original_real_source_file',sha(r['path'])==r['sha256'])
    oldready=get('original_ready');actual=get('actual_response')['ready']
    gate('original_ready_identity',base['inputs']['ready']['sha256']==ids['files']['original_ready']['sha256'])
    oldmodel,newmodel=oldready['rationalDeepModel'],actual['rationalDeepModel']
    for k in MODEL_KEYS:gate('same_mathematical_model_'+k,oldmodel[k]==newmodel[k])
    for k in GEOMETRY_KEYS:gate('same_physical_geometry_'+k,oldmodel['physicalParameters'].get(k,DEFAULTS.get(k))==newmodel['physicalParameters'].get(k,DEFAULTS.get(k)))
    gate('same_complete160_source_table',len(oldready['shallowSourceParameters']['cells'])==160
         and oldready['shallowSourceParameters']==actual['shallowSourceParameters'])
    sys.path.insert(0,ids['original_sources_directory'])
    from tail_r33_middle_ordered_physical import SourceValues
    from closure_real_linear_head_enclosure import PositiveKernels
    h=SourceValues(oldready);ker=PositiveKernels(h,12,92);h.cells={n:ker.source_cell(n) for n in (7,8,9)}
    modes=list(range(2,41,2));sigma=arb(1)/64;eta=arb(1)/16;d=arb(1)/8
    weights=[up((m*sigma).exp()) for m in modes]
    pieces={};poly_records=[]
    for row in jets['pieces']:
        n,j,k=row['raw_cell'],row['raw_segment'],row['part']
        gate('original_stage_partition',row['raw_left']==k/8 and row['raw_right']==(k+1)/8)
        P=[hermite(*x) for x in zip(row['P0'],row['P1'],row['dP0'],row['dP1'])]
        K=[hermite(*x) for x in zip(row['K0'],row['K1'],row['dK0'],row['dK1'])]
        pieces[n,j,k]=(P,K)
        poly_records.append(dict(cell=n,segment=j,part=k,stage_index=row['stage_index'],
            exact_P_Bernstein=[[[str(v.numerator),str(v.denominator)] for v in q] for q in P],
            exact_K_Bernstein=[[[str(v.numerator),str(v.denominator)] for v in q] for q in K]))
    gate('all216_distinct_pieces',len(pieces)==216 and set(pieces)=={(n,j,k) for n in (7,8,9) for j in range(9) for k in range(8)})
    ordered=list(reversed(jets['pieces']))
    for aa,bb in zip(ordered,ordered[1:]):
        P,K=pieces[aa['raw_cell'],aa['raw_segment'],aa['part']]
        p,k=pieces[bb['raw_cell'],bb['raw_segment'],bb['part']]
        gate('exact_rational_C0_join',all(x[-1]==y[0] for x,y in zip(P,p)) and all(x[-1]==y[0] for x,y in zip(K,k)))
    pp=Path(str(a.out_prefix)+'-polynomials.json.gz')
    pp.write_bytes(gzip.compress((json.dumps(dict(schema='exact-binary-rational-Hermite216-v1',rows=poly_records),separators=(',',':'))+'\n').encode(),mtime=0))
    del poly_records
    rows=[];old_count=new_count=0;worst={};best={};cell_caps={n:[[arb(0),arb(0)] for m in modes] for n in (7,8,9)}
    def worst_up(k,v,ident):
        v=up(v)
        if k not in worst or v>ep(worst[k]['upper']):worst[k]=dict(upper=endpoint(v),where=ident)
    def best_lo(k,v,ident):
        v=v.lower()
        if k not in best or v<ep(best[k]['lower']):best[k]=dict(lower=endpoint(v),where=ident)
    for n in (9,8,7):
        prof=get('profile_'+str(n));res=get('profile_resource_'+str(n))
        gate('actual_original_complete_profile',res['exitcode']==0 and prof['all_gates'] and all(prof['gates'].values())
             and prof['config']['input_manifest_sha256']==ids['files']['original_source_manifest']['sha256'])
        last={j:F(0) for j in range(9)};local_seen=0
        for ref in prof['profile_chunks']:
            gate('original_wholeleaf_file',sha(ref['path'])==ref['sha256'])
            for r in read(ref['path'])['rows']:
                j=r['segment'];lo,hi=F(r['left']),F(r['right']);old_count+=1;local_seen+=1
                gate('complete_old_leaf_coverage',r['cell']==n and lo==last[j] and hi>lo);last[j]=hi
                cuts=[lo]+[F(k,8) for k in range(1,8) if lo<F(k,8)<hi]+[hi]
                radius=ball(r['whole_radius']);w=ball(r['whole_w']);E=1+w*w;zmax=up(w*w);Emax=up(E)
                gate('original_real_background_domain',radius>0 and w>0 and w<arb(1)/2 and Emax<=arb(5)/4)
                for lft,rgt in zip(cuts,cuts[1:]):
                    part=min(7,int(lft*8));t0,t1=lft*8-part,rgt*8-part
                    P,K=pieces[n,j,part];centres=[];pc=kc=tc=ps=ks=ts=ls=us=q0=arb(0)
                    ident=dict(cell=n,segment=j,part=part,left=str(lft),right=str(rgt));new_count+=1
                    for mi,m in enumerate(modes):
                        pb,kb=restrict(P[mi],t0,t1),restrict(K[mi],t0,t1)
                        pv,kv=hull([ar(v) for v in pb]),hull([ar(v) for v in kb])
                        pa,ka=up(abs(pv)),up(abs(kv));ta=m*pa;weight=weights[mi]
                        lamb=hull([ar(kk)+E*m*ar(vv) for kk,vv in zip(kb,pb)])
                        uu=hull([m*ar(kk)+ar(vv) for kk,vv in zip(kb,pb)])
                        pc+=pa;kc+=ka;tc+=ta;ps+=pa*weight;ks+=ka*weight;ts+=ta*weight
                        ls+=up(abs(lamb))*weight;us+=up(abs(uu))*weight
                        q0+=(kv*kv+E*pv*pv)/4+m*kv*pv/2
                        cell_caps[n][mi][0]=max(cell_caps[n][mi][0],pa);cell_caps[n][mi][1]=max(cell_caps[n][mi][1],ka)
                        centres.append(dict(mode=m,P=rec(pv),K=rec(kv)))
                    pc,kc,tc,ps,ks,ts,ls,us=map(up,(pc,kc,tc,ps,ks,ts,ls,us))
                    dq=up(eta*max(up(Emax*pc/3+kc),up((kc+tc)/3))+eta*eta/8)
                    qb=up(abs(q0)+dq);pu,ku,tu=map(up,(pc+eta/3,kc+eta/3,tc+eta))
                    pstrip,kstrip,tstrip=map(up,(ps+eta/3,ks+eta/3,ts+eta))
                    Ac=up(2*(ku+d)+(ku+d)**2+Emax*pu*pu);U=up(zmax*Ac);V=up(zmax*pu*pu);Y=up((1+d+ku)*tu)
                    As=up(2*(kstrip+d)+(kstrip+d)**2+Emax*pstrip*pstrip);Us=up(zmax*As);Vs=up(zmax*pstrip*pstrip)
                    gate('complete_complex_series_domain',0<=U<1 and 0<=V<1 and 0<=Us<1 and 0<=Vs<1)
                    f,g=f_and_g(U);err=up(Ac*f+Y*(g+V)/(1-V));rouche=up(qb+d*d/2+err);root=up((qb+err)/(1-d/2))
                    gap=1-d-ls-Emax*eta;ymin=1-d-ku;Lmin=1-d-ls-Emax*eta;Nmin=1-zmax*Y/(1-V)
                    checks={'complete_Rouche_unique_simple_mean':rouche<d,'real_S':1-V>0,'real_D':1-U>0,'real_y':ymin>0,'real_L':Lmin>0,'real_N':Nmin>0,'complete_strip_inverse':gap>0}
                    for name,ok in checks.items():mg(name,ok,ident)
                    Ns=Nell=None
                    if gap>0:
                        Ns=up(Emax*(us+eta)**2/gap)
                        fullK=kstrip+d;Nell=up(((fullK+tstrip)**2+zmax*(2*fullK*tstrip+tstrip*tstrip+pstrip*pstrip))/gap)
                    rows.append(dict(**ident,source_original_leaf=[r['left'],r['right']],source_profile_sha256=ref['sha256'],
                        centre_weak_P=endpoint(pc),centre_weak_K=endpoint(kc),centre_weak_Ptheta=endpoint(tc),centre_strip_P=endpoint(ps),centre_strip_K=endpoint(ks),
                        correlated_strip_lambda=endpoint(ls),quadratic_mean=rec(q0),root_absolute=endpoint(root),Rouche_left=endpoint(rouche),
                        complete_mean_remainder=endpoint(err),strip_inverse_gap=endpoint(gap.lower()),
                        complete_Ns=None if Ns is None else endpoint(Ns),complete_Nell=None if Nell is None else endpoint(Nell),all_domain_gates=all(checks.values())))
                    for key,v in [('weak_K',kc),('correlated_lambda_strip',ls),('root_absolute',root),('Rouche_left',rouche)]:worst_up(key,v,ident)
                    if Ns is not None:worst_up('complete_Ns',Ns,ident);worst_up('complete_Nell',Nell,ident)
                    for key,v in [('S',1-V),('D',1-U),('y',ymin),('L',Lmin),('N',Nmin),('strip_inverse',gap)]:best_lo(key,v,ident)
            if resource.getrusage(resource.RUSAGE_SELF).ru_maxrss>a.rss_kib:raise MemoryError('Preserve declared128MiB budget')
        gate('all_original_nine_segments',all(v==1 for v in last.values()))
        gate('original_wholeleaf_count',local_seen==prof['counts']['taylor']+prof['counts']['root_brackets'])
        print(json.dumps(dict(event='complete_original_mean_domain',cell=n,original_leaves=local_seen,refined_leaves=new_count,failures=len(failures),elapsed_seconds=time.monotonic()-started)),flush=True)
    gate('all3940_original_leaves',old_count==3940)
    whole=[]
    for n in (9,8,7):
        norm=sum(((1+m)*weights[i]*(v[0]+v[1]) for i,(m,v) in enumerate(zip(modes,cell_caps[n]))),arb(0))
        whole.append(dict(cell=n,radial_first_strong_sigma1over64=endpoint(up(norm)),mode_caps=[dict(mode=m,P=endpoint(v[0]),K=endpoint(v[1])) for m,v in zip(modes,cell_caps[n])]))
    result=dict(schema='exact-continuous-Hermite-M20-original9to7-full-mean-domain-v1',author='/root (GPT-6 Astra Pro; AI-assisted)',
        all_gates=not failures,gate_count=sum(counts.values()),gate_categories=counts,failures=failures,
        inputs=ids,input_manifest_sha256=sha(a.inputs),source_sha256=sha(__file__),precision_bits=ctx.prec,
        polynomial_file=dict(path=str(pp),sha256=sha(pp),bytes=pp.stat().st_size),pieces=216,original_background_leaves=old_count,refined_leaves=new_count,
        exact_binary_rational_C0_centre=True,same_original_mathematical_background_and_all160_source_rows=True,
        tube=dict(sigma='1/64',complete_nonmean_strong_radius='1/16',mean_root_disk='1/8',all_infinite_even_modes=True),
        centre_whole_cell_norms=whole,strongest_upper=worst,strict_lower=best,rows=rows,
        complete_mean_and_angle_inverse_not_finite_quadrature=True,
        no_new_ODE_BVP_or_background_integration=True,actual_R143_solution_in_tube_not_claimed=True,
        original_full_equation_residual_not_yet_paid=True,full_nonlinear_outer_or_closed_surface_claimed=False,
        elapsed_seconds=time.monotonic()-started,peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    out=Path(str(a.out_prefix)+'-certificate.json.gz');out.write_bytes(gzip.compress((json.dumps(result,separators=(',',':'))+'\n').encode(),mtime=0))
    print(json.dumps(dict(primary=str(out),sha256=sha(out),all_gates=result['all_gates'],gate_count=result['gate_count'],failure_count=len(failures),whole_cell_norms=[(v['cell'],float(ep(v['radial_first_strong_sigma1over64']))) for v in whole],elapsed_seconds=result['elapsed_seconds'],peak_rss_kib=result['peak_rss_kib'])),flush=True)
    if failures:raise SystemExit(1)

if __name__=='__main__':main()
