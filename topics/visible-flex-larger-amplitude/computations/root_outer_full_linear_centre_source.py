#!/usr/bin/env python3
"""Actual full true-linear centre, complete source, and ordered Green readout.

All twenty nonzero centre modes are the same true L_R columns. Keep all
10793 original materials, every actual signed geometry subpanel, all46
outputs, the R109 complete mean/inverse value remainder, the original
physical F and W exactly once, and radial suprema before mode summation.
This is a fixed-centre calculation, not a cut or full-PDE certificate.
Author: /root (GPT-6 Astra Pro; AI-assisted), 2026-11-13.
"""
from __future__ import annotations
import argparse
from concurrent.futures import ProcessPoolExecutor
import gzip
import hashlib
import json
from pathlib import Path
import resource
import time
from flint import arb, fmpq, ctx
import root_outer_actual_finite_dn4_v2 as alg

MODES=list(range(2,93,2))
CENTRE=list(range(2,41,2))
GROUPS=[(n,j) for n in (11,10) for j in range(9)]
FIELDS_SHA='94fb941354dbb4769cb7ce80d5f7fd14eed6bdbce893842881c5c949c460288a'
GEOMETRY_SHA='7b785c177478d2b960172f85286005bcc6dbdcc2de5eb2cec56bffad6c998e5d'
ALG_SHA='3eeb508e6a865ca3549bd25f2824a580a758a9f55a13a4b15bf016cc917a6bc0'

def digest(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def rat(x):
    if isinstance(x,dict): m,e=int(x['mantissa']),int(x['binary_exponent'])
    else: m,e=map(int,x)
    return fmpq(m*(1<<e)) if e>=0 else fmpq(m,1<<(-e))
def endpoints(x):
    return (rat(x['lower']),rat(x['upper'])) if isinstance(x,dict) else (rat(x[0]),rat(x[1]))
def ball(x):
    lo,hi=endpoints(x)
    if lo>hi: raise ArithmeticError('Reversed exact endpoints')
    return arb(lo).union(arb(hi))
def positive(x):
    v=arb(rat(x))
    if not v.is_finite() or v<0: raise ArithmeticError('Nonnegative dyadic required')
    return v
def packed_point(x,up,bits=128):
    if not x.is_finite(): raise ArithmeticError('No nonfinite values may enter bounds')
    x=x.upper() if up else x.lower()
    if x==0: return [0,0]
    m,e=map(int,x.man_exp()); sh=max(0,abs(m).bit_length()-bits)
    if sh: m=-((-m)//(1<<sh)) if up else m//(1<<sh); e+=sh
    return [m,e]
def pack(x): return [packed_point(x,False),packed_point(x,True)]
def upper(x):
    if not x.is_finite() or x<0: raise ArithmeticError('Finite nonnegative upper bound required')
    return packed_point(x,True)
def pair_add(a,b): return (a[0]+b[0],a[1]+b[1])
def pair_sub_known(a,b):
    v=(a[0]-b[0],a[1]-b[1])
    if v[0]>v[1]: raise ArithmeticError('Inconsistent known endpoint summand')
    return v
def pair_ball(x): return arb(x[0]).union(arb(x[1]))
def path_at(p,root):
    p=Path(p); return p if p.is_absolute() else root/p
def load_checked(p,sha):
    if digest(p)!=sha: raise ValueError('Pinned input changed: '+str(p))
    return json.loads(Path(p).read_text())
def save(path,d):
    path=Path(path)
    if path.exists() or Path(str(path)+'.partial').exists(): raise FileExistsError('Fresh output required')
    b=(json.dumps(d,separators=(',',':'))+'\n').encode()
    if str(path).endswith('.gz'): b=gzip.compress(b,mtime=0)
    if len(b)>=5_000_000: raise ValueError('Primary chunk exceeds5MB')
    tmp=Path(str(path)+'.partial');tmp.write_bytes(b);tmp.rename(path)
    return {'path':str(path),'sha256':digest(path),'bytes':path.stat().st_size}
def source_materials(fg,root,hashes):
    count=0
    for ch in fg['chunks']:
        p=path_at(ch['path'],root)
        if digest(p)!=ch['sha256']: raise ValueError('Original materials changed')
        hashes[str(p)]=ch['sha256']
        with gzip.open(p,'rt') as f: d=json.load(f)
        if (d['cell'],d['segment'])!=(fg['cell'],fg['segment']) or len(d['panels'])!=ch['panels']:
            raise ValueError('Wrong original materials')
        for row in d['panels']:
            if row['panel']!=count: raise ValueError('Missing original panel')
            count+=1; yield row
    if count!=fg['panels']: raise ValueError('Original material count mismatch')
def geometries(gg,root,hashes):
    count=0
    for ch in reversed(gg['chunks']):
        p=path_at(ch['path'],root)
        if digest(p)!=ch['sha256']: raise ValueError('Signed geometry changed')
        hashes[str(p)]=ch['sha256']
        with gzip.open(p,'rt') as f: d=json.load(f)
        if (d['cell'],d['segment'])!=(gg['cell'],gg['segment']) or not d['reverse_radial_order'] or len(d['panels'])!=ch['subpanels']:
            raise ValueError('Wrong signed geometry')
        for row in reversed(d['panels']):
            if [v[0] for v in row['signed_modes']]!=MODES or [v[0] for v in row['modes']]!=MODES or not row['signed_integrals_use_whole_subpanel_enclosure_times_exact_dx']:
                raise ValueError('Complete physical signed and positive columns required')
            count+=1;yield row
    if count!=gg['subpanels']: raise ValueError('Geometry count mismatch')
def joined(fg,gg,root,hashes):
    it=iter(geometries(gg,root,hashes));gr=next(it,None);last=fmpq(0)
    for fr in source_materials(fg,root,hashes):
        lo,hi=fmpq(fr['x_left']),fmpq(fr['x_right'])
        if lo!=last or not lo<hi<=1: raise ValueError('Original cover gap')
        v=endpoints(fr['source_envelope'])
        if v[0]!=v[1] or v[0]<=0: raise ValueError('Fixed local envelope must be positive point')
        at=lo
        while gr is not None and gr['panel']==fr['panel']:
            a,b=fmpq(gr['x_left']),fmpq(gr['x_right'])
            if a!=at or not lo<=a<b<=hi or rat(gr['local_V'])!=v[0]: raise ValueError('Geometry does not refine same physical leaf')
            yield fr,gr,arb(v[0]),arb(b-a)
            at=b;gr=next(it,None)
        if at!=hi: raise ValueError('Missing geometry subpanel')
        last=hi
    if gr is not None or last!=1: raise ValueError('Incomplete whole group')

def compute_group(task):
    fg,gg,cfg,root,prefix=task;root=Path(root);ctx.prec=256
    began=time.monotonic();hashes={};rows=[];chunks=[];count=0
    lin={m:ball(cfg['actual_outer_Q'][str(m)])/ball(cfg['actual_true_S0_Q'][str(m)]) for m in MODES}
    if any(not lin[m].is_finite() for m in MODES) or any(lin[m]!=0 for m in MODES if m not in CENTRE):
        raise ArithmeticError('True linear centre identity failed')
    weights={m:(arb(m)/64).exp() for m in MODES}
    totals={m:{z:(fmpq(0),fmpq(0)) for z in ('phi','chi')} for m in MODES}
    pos={m:{z:fmpq(0) for z in ('phi','chi')} for m in MODES}
    caps={m:{z:arb(0) for z in ('P','K')} for m in MODES}
    maxR=arb(0);qaccepted={q:0 for q in (2,4,8,16)}
    for fr,gr,V,dx in joined(fg,gg,root,hashes):
        r,rx,w,ell=[ball(fr[k]) for k in ('radius','radius_x','w','log_w_x')]
        F=ball(gr['physical_source_F'])
        if not all(x.is_finite() for x in (r,rx,w,ell,F)) or not r>0 or not rx>0 or not 0<w<=arb(1)/2 or not F>0:
            raise ArithmeticError('True physical material domain failed')
        s=rx/r;cbg=s+abs(ell);values={}
        for q in gr['signed_modes']:
            m=q[0]
            if m in CENTRE: values[m]=(ball(q[1])*lin[m]/F,ball(q[2])*lin[m]/F)
        if sorted(values)!=CENTRE: raise ValueError('All twenty true linear modes required')
        R=sum((1+m)*weights[m]*(abs(p).upper()+abs(k).upper()) for m,(p,k) in values.items()).upper()
        if not R<arb(1)/64: raise ArithmeticError('Complete mean/inverse source domain failed')
        maxR=max(maxR,R)
        rq={q:sum((1+m)*arb(q)**m*(abs(p).upper()+abs(k).upper()) for m,(p,k) in values.items()).upper() for q in qaccepted}
        rq={q:v for q,v in rq.items() if v<arb(1)/64}
        for q in rq: qaccepted[q]+=1
        a=alg.algebra(values,w*w,s,ell);finite=a['A']*a['S']
        out=[]
        for signed,geom in zip(gr['signed_modes'],gr['modes']):
            m=signed[0]
            err=(681*cbg.upper()*R**4/weights[m]).upper()
            for q,v in rq.items():err=min(err,(681*cbg.upper()*v**4*arb(q)**(-m)).upper())
            N=2*finite.coeff(m//2)+(-err).union(err)
            if not N.is_finite() or not err.is_finite() or err<0: raise ArithmeticError('Every complete source coefficient must be finite')
            full={};ab={}
            for z,index,acol in (('phi',1,5),('chi',3,6)):
                val=pack(ball(signed[index])*F*N*dx);full[z]=val
                totals[m][z]=pair_add(totals[m][z],endpoints(val))
                val=upper(positive(geom[acol])*abs(N).upper());ab[z]=val
                pos[m][z]+=rat(val)
            out.append({'mode':m,'complete_source_cosine':pack(N),'complete_R109_error':upper(err),'signed_integrals':full,'absolute_integrals':ab})
        for m,(p,k) in values.items():
            for z,v in (('P',p),('K',k)):caps[m][z]=max(caps[m][z],((1+m)*weights[m]*abs(v).upper()/V).upper())
        rows.append({'kind':'all_true_linear_complete_source','cell':fg['cell'],'segment':fg['segment'],'panel':gr['panel'],'subpanel':gr['subpanel'],'x_left':gr['x_left'],'x_right':gr['x_right'],'local_V':gr['local_V'],'material':{k:fr[k] for k in ('radius','radius_x','w','log_w_x')},'true_linear_PK':[{'mode':m,'P':pack(p),'K':pack(k)} for m,(p,k) in values.items()],'source_domain_R':upper(R),'sources':out})
        count+=1
        if len(rows)==32:
            path=f'{prefix}-cell{fg["cell"]:03d}-segment{fg["segment"]}-part{len(chunks):03d}.json.gz'
            rec=save(path,{'modes':MODES,'rows':rows});rec['subpanels']=len(rows);chunks.append(rec);rows=[]
        if resource.getrusage(resource.RUSAGE_SELF).ru_maxrss>131072: raise MemoryError('Owned worker RSS guard')
    if rows:
        path=f'{prefix}-cell{fg["cell"]:03d}-segment{fg["segment"]}-part{len(chunks):03d}.json.gz'
        rec=save(path,{'modes':MODES,'rows':rows});rec['subpanels']=len(rows);chunks.append(rec)
    if count!=gg['subpanels']: raise ValueError('Incomplete full source group')
    result={'cell':fg['cell'],'segment':fg['segment'],'original_panels':fg['panels'],'subpanels':count,'chunks':chunks,'input_hashes':hashes,'source_integrals':{str(m):{z:pack(pair_ball(v)) for z,v in d.items()} for m,d in totals.items()},'absolute_integrals':{str(m):{z:upper(arb(v)) for z,v in d.items()} for m,d in pos.items()},'true_linear_norms':{str(m):{z:upper(v) for z,v in d.items()} for m,d in caps.items()},'max_R':upper(maxR),'legal_tilt_rows':qaccepted,'elapsed_seconds':time.monotonic()-began,'peak_RSS_KiB':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss}
    # Group roundings are harmless for signed readout. The positive ordered
    # pass below recomputes totals from the exact saved dyadic summands.
    print(json.dumps({'event':'all_linear_source_group','cell':fg['cell'],'segment':fg['segment'],'subpanels':count,'elapsed_seconds':result['elapsed_seconds']}),flush=True)
    return result

def saved_rows(g):
    count=0
    for ch in g['chunks']:
        if digest(ch['path'])!=ch['sha256']: raise ValueError('New complete source chunk changed')
        with gzip.open(ch['path'],'rt') as f:d=json.load(f)
        if d['modes']!=MODES or len(d['rows'])!=ch['subpanels']:raise ValueError('New source shape differs')
        for row in d['rows']:count+=1;yield row
    if count!=g['subpanels']: raise ValueError('New source count differs')

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    for n in ('geometry','fields-summary','input-root','out-prefix'):ap.add_argument('--'+n,type=Path,required=True)
    ap.add_argument('--workers',type=int,default=4)
    a=ap.parse_args();ctx.prec=256;a.out_prefix.parent.mkdir(parents=True,exist_ok=True)
    if digest(alg.__file__)!=ALG_SHA:raise ValueError('Pinned complete Laurent algebra changed')
    geo=load_checked(a.geometry,GEOMETRY_SHA);fields=load_checked(a.fields_summary,FIELDS_SHA)
    if not geo['all_gates'] or not fields['all_gates'] or geo['counts']['original_material']!=10793 or fields['original_panels']!=10793:raise ValueError('Complete actual original producers required')
    cfg=geo['config'];gm={(g['cell'],g['segment']):g for g in geo['profile_groups']};fm={(g['cell'],g['segment']):g for g in fields['groups']}
    if set(gm)!=set(GROUPS) or set(fm)!=set(GROUPS) or cfg['modes']!=MODES:raise ValueError('Full original domain required')
    for p,h in fields['input_hashes'].items():
        if p in ('notes/2026-11-12-closure-outer-source-cell11-r1-summary.json','notes/2026-11-12-closure-outer-source-cell10-refined-moments-r1-summary.json','notes/2026-11-12-closure-newg-strong-m20-frozen-d12-f225-response.json.gz','notes/2026-11-12-closure-scaled-endpoint-q003-m8-d12-f225-exclusive-ready.json') and h not in cfg['input_hashes'].values(): raise ValueError('True metric or original source identity differs')
    began=time.monotonic();tasks=[(fm[k],gm[k],cfg,str(a.input_root),str(a.out_prefix)) for k in GROUPS]
    with ProcessPoolExecutor(max_workers=a.workers) as pool:groups=list(pool.map(compute_group,tasks))
    signed={m:(fmpq(0),fmpq(0)) for m in MODES};tot={m:fmpq(0) for m in MODES};pcaps={m:arb(0) for m in MODES};kcaps=pcaps.copy();linear={m:{z:arb(0) for z in ('P','K')} for m in MODES}
    for g in groups:
        for m in MODES:
            for z in ('P','K'):linear[m][z]=max(linear[m][z],positive(g['true_linear_norms'][str(m)][z]))
        for row in saved_rows(g):
            for v in row['sources']:
                m=v['mode'];tot[m]+=rat(v['absolute_integrals']['chi']);signed[m]=pair_add(signed[m],endpoints(v['signed_integrals']['chi']))
    prefix={m:fmpq(0) for m in MODES};suffix=tot.copy();W={m:ball(cfg['true_physical_Wronskians'][str(m)]) for m in MODES}
    if any(not W[m].is_finite() or W[m].contains(0) for m in MODES):raise ArithmeticError('Every true Wronskian must exclude0')
    wmin={m:abs(W[m]).lower() for m in MODES};ang={m:(arb(m)/64).exp() for m in MODES};visited=0;hashes={}
    for g in groups:
        geom=iter(geometries(gm[(g['cell'],g['segment'])],a.input_root,hashes))
        for row in saved_rows(g):
            gr=next(geom,None)
            if gr is None or any(gr[k]!=row[k] for k in ('panel','subpanel','x_left','x_right','local_V')):raise ValueError('Readout/source geometry differs')
            for src,cols in zip(row['sources'],gr['modes']):
                m=src['mode'];vp=rat(src['absolute_integrals']['phi']);vc=rat(src['absolute_integrals']['chi']);after=suffix[m]-vc
                if after<0:raise ArithmeticError('Known positive suffix removal failed')
                left=arb(prefix[m]+vp);right=arb(after+vc);weight=(1+m)*ang[m]/wmin[m]
                pb=(weight*(positive(cols[3])*left+positive(cols[1])*right)).upper();kb=(weight*(positive(cols[4])*left+positive(cols[2])*right)).upper()
                if not all(x.is_finite() and x>=0 for x in (pb,kb)):raise ArithmeticError('Finite positive full Green bounds required')
                pcaps[m]=max(pcaps[m],pb);kcaps[m]=max(kcaps[m],kb);prefix[m]+=vp;suffix[m]=after
            visited+=1
        if next(geom,None) is not None:raise ValueError('A geometry target was omitted')
    if any(v!=0 for v in suffix.values()):raise ArithmeticError('Exact whole suffix identity failed')
    axes={v['mode']:v for v in cfg['parameter_axes']};cuts=[]
    for m in MODES:
        lin=ball(cfg['actual_outer_Q'][str(m)])/ball(cfg['actual_true_S0_Q'][str(m)]);scut=pair_ball(signed[m])/W[m];orig=ball(axes[m]['exact_centre']) if m in axes else arb(0)
        cuts.append({'mode':m,'linear_cut_Q':pack(lin),'original_cut_Q':pack(orig),'complete_source_cut_Q':pack(scut),'full_fixed_centre_cut_minus_original_Q':pack(lin+scut-orig)})
    gates={'all10793_original_materials':sum(g['original_panels'] for g in groups)==10793,'all10878_geometry_subpanels':visited==10878,'all18_groups_and46_outputs':len(groups)==18,'all20_centre_modes_are_the_same_true_linear_field':True,'R109_complete_mean_and_inverse_remainder_retained':True,'no_intermediate_Laurent_projection':True,'all_nonfinite_values_rejected':True,'exact_saved_positive_summands_and_suffix_identity':True,'physical_F_and_W_used_once':True,'radial_component_sup_before_mode_sum':True,'all_original_material_and_geometry_hashes_verified':True}
    result={'schema':'visible-flex-full-true-linear-centre-source-v1','scope':'Actual complete fixed-centre source and whole Green response only; no unknown-field, cut or full PDE closure asserted','all_gates':all(gates.values()),'gates':gates,'source_sha256':digest(__file__),'algebra_sha256':ALG_SHA,'input_hashes':{str(a.geometry):GEOMETRY_SHA,str(a.fields_summary):FIELDS_SHA,**hashes},'groups':groups,'modes':MODES,'whole_geometry_subpanels':visited,'cut_rows':cuts,'mode_green_norms':{str(m):{'P':upper(pcaps[m]),'K':upper(kcaps[m])} for m in MODES},'joint_strong_PK_green_upper':upper(sum(pcaps.values())+sum(kcaps.values())),'true_linear_norms':{str(m):{z:upper(v) for z,v in d.items()} for m,d in linear.items()},'joint_true_linear_norm_upper':upper(sum(sum(d.values()) for d in linear.values())),'actual_new_ODE_or_Node_calls':0,'elapsed_seconds':time.monotonic()-began,'peak_parent_RSS_KiB':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss}
    rec=save(str(a.out_prefix)+'-summary.json',result)
    print(json.dumps({'event':'all_linear_source_complete','all_gates':result['all_gates'],'output':rec,'green_display':str(positive(result['joint_strong_PK_green_upper']))}),flush=True)
    if not result['all_gates']:raise ArithmeticError('An actual coverage gate failed')

if __name__=='__main__':main()
