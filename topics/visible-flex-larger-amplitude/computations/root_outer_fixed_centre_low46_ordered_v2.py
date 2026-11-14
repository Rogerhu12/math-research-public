#!/usr/bin/env python3
"""Prepared v2 consumer pinned to the distinct R107/R108 source v3.

The original consumer and sourcev2 remain in Git history. Neither version
has been executed. Only producer identity and executable name change here;
all ordered physical Green, affine-centre, coverage and resource gates stay.

Prepared ordered all46 fixed-centre source and affine residual consumer.

Use only the actual signed geometry v3 and the actually completed fixed-R88
source v2. Keep all10793 original source rows and every actual geometry
subpanel. Complete signed source contributions are accumulated first;
whole target panels then receive the exact remaining endpoint sums plus
the possible partial current-panel integrals. No actual nonlinear outer
solution, beta cancellation, unknown-field error, or cut selfmap is claimed.
Author: /root (GPT-6 Astra Pro; AI-assisted),2026-11-13.
"""
from __future__ import annotations
import argparse
from fractions import Fraction as Q
import gzip
import hashlib
import json
from pathlib import Path
import resource
import sys
import time
from itertools import zip_longest

import closure_outer_linear_centre_ordered_cut_recovered_v1 as exact
from closure_outer_linear_centre_ordered_cut_recovered_v1 import (
    point,pair,add,sub,mul,div,norm,intersection,remove_summand,exp_bounds)

if hasattr(sys,'set_int_max_str_digits'):
    sys.set_int_max_str_digits(0)
MODES=list(range(2,93,2))
ORIGINAL=list(range(2,41,2))
GROUPS=[(n,j) for n in (11,10) for j in range(9)]
ZERO=(Q(0),Q(0))
HELPER_SHA='5cc4e1d628d4676edb11f704846347cd260e374875315e5c9564c28175c92c38'
FIELDS_SHA='94fb941354dbb4769cb7ce80d5f7fd14eed6bdbce893842881c5c949c460288a'
FIELDS_SOURCE='306b2bc0c49635d731f3bbe91653310f2b2ecba19bcb7437f8ef932f37a5d75b'
GEOMETRY_SOURCE='98b5e8a0b06688830b7aee69df9f6a76f39f94d8b259a093d476bbf78abee642'
SOURCE_V3='3a19cb838f256cc9dd454267b5a32c2e280df927cc21820a2a8a867ad160eb59'
SHARED_INPUTS=(
 'notes/2026-11-12-closure-outer-source-cell11-r1-summary.json',
 'notes/2026-11-12-closure-outer-source-cell10-refined-moments-r1-summary.json',
 'notes/2026-11-12-closure-newg-strong-m20-frozen-d12-f225-response.json.gz',
 'notes/2026-11-12-closure-scaled-endpoint-q003-m8-d12-f225-exclusive-ready.json')

def digest(p):
    h=hashlib.sha256()
    with open(p,'rb') as f:
        for b in iter(lambda:f.read(1024*1024),b''):
            h.update(b)
    return h.hexdigest()

def p2(n):
    return Q(1<<n) if n>=0 else Q(1,1<<(-n))

def packed_endpoint(x,direction,bits=128):
    x=Q(x)
    if not x:
        return [0,0]
    z=abs(x)
    k=z.numerator.bit_length()-z.denominator.bit_length()
    if z<p2(k):
        k-=1
    e=k-bits+1
    v=x/p2(e)
    mantissa=v.numerator//v.denominator
    if direction>0 and v.numerator%v.denominator:
        mantissa+=1
    return [mantissa,e]

def pack(x):
    return [packed_endpoint(x[0],-1),packed_endpoint(x[1],1)]

def rounded(x):
    # The resulting endpoints are the explicit summands used in both passes.
    return pair(pack(x))

def bound(x):
    if x<0:
        raise ArithmeticError('Nonnegative upper bound required')
    return packed_endpoint(x,1)

def same_scalar(x):
    a,b=pair(x)
    if a!=b:
        raise ArithmeticError('The original dyadic envelope must be a point')
    return a

def resolve(p,root):
    p=Path(p)
    return p if p.is_absolute() else root/p

def loaded(path,wanted,hashes):
    got=digest(path)
    if got!=wanted:
        raise ValueError('Input hash mismatch: '+str(path))
    hashes[str(path)]=got
    return json.loads(Path(path).read_text())

def formal_zero(path,output,kind,hashes):
    hashes[str(path)]=digest(path)
    d=json.loads(Path(path).read_text())
    if d.get('exitcode')!=0 or d.get('termination_signal') is not None:
        raise ValueError('The owned producer has no actual formal-zero result')
    argv=d.get('command')
    if not isinstance(argv,list) or '--out-prefix' not in argv:
        raise ValueError('Exact owned producer argv required')
    expected=str(output)
    ending='-summary.json' if kind=='source' else '.json'
    if not expected.endswith(ending):
        raise ValueError('Expected original producer output naming')
    expected=expected[:-len(ending)]
    if argv[argv.index('--out-prefix')+1]!=expected:
        raise ValueError('Resource record belongs to another output prefix')
    script=('root_outer_fixed_centre_low46_source_v3.py' if kind=='source'
            else 'closure_outer_physical_green_signed_profiles_v3.py')
    if not any(Path(x).name==script for x in argv if isinstance(x,str)):
        raise ValueError('Resource record uses another source entrypoint')

def source_rows(g,root,hashes):
    count=0
    for ch in g['chunks']:
        path=resolve(ch['path'],root)
        if digest(path)!=ch['sha256']:
            raise ValueError('Complete signed source chunk changed')
        hashes[str(path)]=ch['sha256']
        with gzip.open(path,'rt') as f:
            h=json.loads(next(f))
            if (h['kind']!='header' or h['cell']!=g['cell'] or
                h['segment']!=g['segment'] or h['modes']!=MODES or
                not h['complete_mean_numerator_zero_mode_retained'] or
                h['neumann_terms']!=4):
                raise ValueError('Wrong complete fixed-centre source header')
            local=0
            trailer=False
            for line in f:
                r=json.loads(line)
                if r['kind']=='trailer':
                    if trailer or not r['complete'] or r['subpanels']!=local:
                        raise ValueError('Incomplete signed source trailer')
                    trailer=True
                    if any(x.strip() for x in f):
                        raise ValueError('Unexpected trailing source data')
                    break
                if trailer or r['kind']!='complete_fixed_centre_source':
                    raise ValueError('Unexpected signed source row')
                local+=1
                count+=1
                yield r
            if not trailer or local!=ch['subpanels']:
                raise ValueError('Incomplete source chunk')
    if count!=g['source_panels']:
        raise ValueError('Complete source group row count mismatch')

def field_rows(g,root,hashes):
    count=0
    for ch in g['chunks']:
        path=resolve(ch['path'],root)
        if digest(path)!=ch['sha256']:
            raise ValueError('An original field chunk changed')
        hashes[str(path)]=ch['sha256']
        with gzip.open(path,'rt') as f:
            d=json.load(f)
        if d['cell']!=g['cell'] or d['segment']!=g['segment']:
            raise ValueError('Original field group differs')
        if len(d['panels'])!=ch['panels']:
            raise ValueError('Original field chunk incomplete')
        for r in d['panels']:
            count+=1
            yield r
    if count!=g['panels']:
        raise ValueError('All original field rows required')

def geometry_rows(g,root,hashes):
    count=0
    # Producer groups and chunks are reverse ordered; invert both locally.
    for ch in reversed(g['chunks']):
        path=resolve(ch['path'],root)
        if digest(path)!=ch['sha256']:
            raise ValueError('Actual signed whole-geometry chunk changed')
        hashes[str(path)]=ch['sha256']
        with gzip.open(path,'rt') as f:
            d=json.load(f)
        if (d['cell']!=g['cell'] or d['segment']!=g['segment'] or
            not d['reverse_radial_order'] or len(d['panels'])!=ch['subpanels']):
            raise ValueError('Incomplete signed geometry group')
        for r in reversed(d['panels']):
            if (r['signed_mode_fields']!=['mode','phi_Y1','phi_Y2','chi_Y1','chi_Y2']
                or [int(v[0]) for v in r['signed_modes']]!=MODES or
                not r['signed_integrals_use_whole_subpanel_enclosure_times_exact_dx']):
                raise ValueError('Whole signed physical columns are required')
            count+=1
            yield r
    if count!=g['subpanels']:
        raise ValueError('Actual geometry count mismatch')

def joined(g,s,f,root,hashes):
    gi=iter(geometry_rows(g,root,hashes))
    gr=next(gi,None)
    previous=Q(0)
    rows=0
    for sr,fr in zip_longest(source_rows(s,root,hashes),field_rows(f,root,hashes)):
        if sr is None or fr is None:
            raise ValueError('Original field and complete source lengths differ')
        i=int(sr['panel'])
        if (int(fr['panel'])!=i or i!=rows or
            sr['cell']!=g['cell'] or fr['cell']!=g['cell'] or
            sr['segment']!=g['segment'] or fr['segment']!=g['segment'] or
            (sr['x_left'],sr['x_right'])!=(fr['x_left'],fr['x_right'])):
            raise ValueError('Complete source and fixed centre are different leaves')
        left,right=Q(sr['x_left']),Q(sr['x_right'])
        if left!=previous or not left<right<=1:
            raise ValueError('Original source cover is not continuous')
        V=same_scalar(sr['source_envelope'])
        if V<=0 or same_scalar(fr['source_envelope'])!=V:
            raise ValueError('Original fixed physical envelope differs')
        if [int(x['mode']) for x in sr['sources']]!=MODES:
            raise ValueError('All46 complete source coefficients required')
        ns={int(x['mode']):pair(x['complete_source_cosine']) for x in sr['sources']}
        if [int(x['mode']) for x in fr['original_candidate_PK']]!=ORIGINAL:
            raise ValueError('All20 original candidate modes required')
        old={int(x['mode']):(pair(x['P']),pair(x['K']))
             for x in fr['original_candidate_PK']}
        at=left
        while gr is not None and int(gr['panel'])==i:
            lo,hi=Q(gr['x_left']),Q(gr['x_right'])
            if lo!=at or not left<=lo<hi<=right:
                raise ValueError('Whole geometry does not refine the same original leaf')
            if point(gr['local_V'])!=V:
                raise ValueError('Geometry and original source have different V')
            F=pair(gr['physical_source_F'])
            if F[0]<=0:
                raise ArithmeticError('The true physical conversion is not positive')
            yield gr,V,F,ns,old
            at=hi
            gr=next(gi,None)
        if at!=right:
            raise ValueError('A source leaf lacks complete geometry coverage')
        previous=right
        rows+=1
    if gr is not None or previous!=1 or rows!=f['panels']:
        raise ValueError('A whole original group has been omitted')

def contributions(gr,F,ns):
    dx=Q(gr['x_right'])-Q(gr['x_left'])
    out={}
    for row in gr['signed_modes']:
        m=int(row[0])
        phi=(pair(row[1]),pair(row[2]))
        chi=(pair(row[3]),pair(row[4]))
        value={}
        for name,col in (('phi',phi),('chi',chi)):
            density=mul(mul(col[0],F),ns[m])
            full=rounded(mul(density,(dx,dx)))
            # Any prefix OR suffix of the current panel lies in this hull.
            partial=(min(Q(0),full[0]),max(Q(0),full[1]))
            value[name]=(full,partial)
        out[m]=(phi,chi,value)
    return out

class Writer:
    def __init__(self,prefix,cell,segment,limit=32):
        self.prefix,self.cell,self.segment=prefix,cell,segment
        self.limit,self.number,self.count=limit,0,0
        self.handle=None
        self.files=[]
    def add(self,row):
        if self.handle is None:
            self.path=Path(str(self.prefix)+f'-cell{self.cell:03d}-segment{self.segment}-part{self.number:03d}.jsonl.gz')
            self.partial=Path(str(self.path)+'.partial')
            if self.path.exists() or self.partial.exists():
                raise FileExistsError('Use a fresh bounded output chunk')
            self.handle=gzip.open(self.partial,'wt',compresslevel=9)
            self.handle.write(json.dumps({'kind':'header','cell':self.cell,
                'segment':self.segment,'modes':MODES,
                'meaning':'Complete fixed-centre source response and affine residual only'})+'\n')
            self.count=0
        self.handle.write(json.dumps(row,separators=(',',':'))+'\n')
        self.count+=1
        if self.count==self.limit:
            self.close()
    def close(self):
        if self.handle is None:
            return
        self.handle.write(json.dumps({'kind':'trailer','complete':True,'subpanels':self.count})+'\n')
        self.handle.close()
        self.handle=None
        if self.partial.stat().st_size>=5_000_000:
            raise ValueError('A complete primary chunk exceeds5MB')
        self.partial.rename(self.path)
        self.files.append({'path':str(self.path),'sha256':digest(self.path),
                           'bytes':self.path.stat().st_size,'subpanels':self.count})
        self.number+=1

def save(path,d):
    b=(json.dumps(d,separators=(',',':'))+'\n').encode()
    path=Path(path)
    if len(b)>1_000_000:
        path=Path(str(path)+'.gz')
        b=gzip.compress(b,mtime=0)
    if len(b)>=5_000_000 or path.exists():
        raise ValueError('Fresh bounded complete output required')
    t=Path(str(path)+'.partial')
    if t.exists():
        raise FileExistsError('Do not overwrite an interrupted write')
    t.write_bytes(b)
    t.rename(path)
    return str(path)

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    for name in ('geometry','source','fields-summary','geometry-resource',
                 'source-resource','input-root','out-prefix'):
        ap.add_argument('--'+name,type=Path,required=True)
    ap.add_argument('--geometry-sha256',required=True)
    ap.add_argument('--source-sha256',required=True)
    ap.add_argument('--rss-kib',type=int,default=98304)
    a=ap.parse_args()
    a.out_prefix.parent.mkdir(parents=True,exist_ok=True)
    if any(Path(str(a.out_prefix)+x).exists() for x in
           ('-summary.json','-summary.json.gz','-failure.json')):
        raise FileExistsError('Fresh immutable consumer prefix required')
    if digest(Path(exact.__file__))!=HELPER_SHA:
        raise ValueError('Frozen exact ordered interval helper changed')
    hashes={}
    geo=loaded(a.geometry,a.geometry_sha256,hashes)
    src=loaded(a.source,a.source_sha256,hashes)
    fields=loaded(a.fields_summary,FIELDS_SHA,hashes)
    formal_zero(a.geometry_resource,a.geometry,'geometry',hashes)
    formal_zero(a.source_resource,a.source,'source',hashes)
    for d in (geo,src,fields):
        if not d['all_gates'] or not all(d['gates'].values()):
            raise ValueError('All completed producer gates are required')
    if (geo['config']['entrypoint_sha256']!=GEOMETRY_SOURCE or
        src['source_sha256']!=SOURCE_V3 or
        fields['source_sha256']!=FIELDS_SOURCE or
        src['original_field_source_sha256']!=FIELDS_SOURCE or
        FIELDS_SHA not in src['input_hashes'].values() or
        src['processed_source_panels']!=10793 or
        src['underlying_original_profile_subpanels']!=10933 or
        fields['original_panels']!=10793 or fields['actual_subpanels']!=10933 or
        geo['counts']['original_material']!=10793):
        raise ValueError('Exact completed source/field/geometry identities required')
    if src['modes']!=MODES or geo['config']['modes']!=MODES:
        raise ValueError('Keep all46 outputs')
    for p in SHARED_INPUTS:
        if fields['input_hashes'][p] not in geo['config']['input_hashes'].values():
            raise ValueError('The real metric, candidate or source has changed')
    gm={(int(g['cell']),int(g['segment'])):g for g in geo['profile_groups']}
    sm={(int(g['cell']),int(g['segment'])):g for g in src['groups']}
    fm={(int(g['cell']),int(g['segment'])):g for g in fields['groups']}
    if any(set(x)!=set(GROUPS) or len(x)!=18 for x in (gm,sm,fm)):
        raise ValueError('All18 source groups are required')
    if [(g['cell'],g['segment']) for g in geo['profile_groups']]!=list(reversed(GROUPS)):
        raise ValueError('Original reverse geometry group order changed')
    cfg=geo['config']
    W={m:pair(cfg['true_physical_Wronskians'][str(m)]) for m in MODES}
    lin={m:div(pair(cfg['actual_outer_Q'][str(m)]),
               pair(cfg['actual_true_S0_Q'][str(m)])) for m in MODES}
    for m in (2,4):
        intersection(lin[m],pair(fields['linear_factors_Qout_over_S0'][str(m)]))
    axes={int(v['mode']):v for v in cfg['parameter_axes']}
    if sorted(axes)!=ORIGINAL:
        raise ValueError('All20 original nonzero cut centres required')
    for m in MODES:
        if W[m][0]<=0<=W[m][1]:
            raise ArithmeticError('True Wronskian contains0')
    ang={m:exp_bounds(Q(m,64)) for m in MODES}
    totals={m:{z:ZERO for z in ('phi','chi')} for m in MODES}
    total_abs={m:{z:Q(0) for z in ('phi','chi')} for m in MODES}
    began=time.monotonic()
    active=None
    groups=[]
    count=0
    def guard():
        if resource.getrusage(resource.RUSAGE_SELF).ru_maxrss>a.rss_kib:
            raise MemoryError('Owned pure-rational RSS guard')
    try:
        for key in GROUPS:
            active={'pass':1,'cell':key[0],'segment':key[1]}
            for gr,V,F,ns,old in joined(gm[key],sm[key],fm[key],a.input_root,hashes):
                for m,(_,_,v) in contributions(gr,F,ns).items():
                    for z in ('phi','chi'):
                        totals[m][z]=add(totals[m][z],v[z][0])
                        total_abs[m][z]+=norm(v[z][0])
                count+=1
                if count%64==0:
                    guard()
            print(json.dumps({'event':'signed46_complete_source_group',
                              'cell':key[0],'segment':key[1],'subpanels_so_far':count}),flush=True)
        expected=geo['counts']['taylor']+geo['counts']['root_brackets']
        if count!=expected or count!=sum(g['subpanels'] for g in gm.values()):
            raise ValueError('Incomplete first-pass whole geometry')
        prefix={m:ZERO for m in MODES}
        suffix={m:totals[m]['chi'] for m in MODES}
        maxima={m:{z:Q(0) for z in ('P','K','C','U')} for m in MODES}
        green_max={m:{z:Q(0) for z in ('P','K','C','U')} for m in MODES}
        visited=0
        for key in GROUPS:
            active={'pass':2,'cell':key[0],'segment':key[1]}
            writer=Writer(a.out_prefix,*key)
            local=0
            for gr,V,F,ns,old in joined(gm[key],sm[key],fm[key],a.input_root,hashes):
                rows=[]
                for m,(phi,chi,v) in contributions(gr,F,ns).items():
                    after=remove_summand(suffix[m],v['chi'][0])
                    left=add(prefix[m],v['phi'][1])
                    right=add(after,v['chi'][1])
                    # Read signed C and U columns before absolute values.
                    pc=add(mul((Q(m),Q(m)),phi[0]),phi[1])
                    cc=add(mul((Q(m),Q(m)),chi[0]),chi[1])
                    pu=sub(mul((Q(-m),Q(-m)),phi[1]),phi[0])
                    cu=sub(mul((Q(-m),Q(-m)),chi[1]),chi[0])
                    fp=[phi[0],phi[1],pc,pu]
                    cp=[chi[0],chi[1],cc,cu]
                    qleft,qright=div(left,W[m]),div(right,W[m])
                    qcombined=add(lin[m],qright)
                    if m in old:
                        op,ok=old[m]
                        orig=[op,ok,add(ok,mul((Q(m),Q(m)),op)),
                              sub(mul((Q(-m),Q(-m)),ok),op)]
                    else:
                        orig=[ZERO]*4
                    green,residual={},{}
                    for k,z in enumerate(('P','K','C','U')):
                        response=div(add(mul(cp[k],qleft),mul(fp[k],qright)),F)
                        if m in (2,4):
                            defect=response
                        else:
                            mapped=div(add(mul(cp[k],qleft),mul(fp[k],qcombined)),F)
                            defect=sub(mapped,orig[k])
                        green[z]=pack(response)
                        residual[z]=pack(defect)
                        weight=ang[m][1]*((1+m) if z in ('P','K') else 1)
                        maxima[m][z]=max(maxima[m][z],weight*norm(defect)/V)
                        green_max[m][z]=max(green_max[m][z],weight*norm(response)/V)
                    rows.append({'mode':m,'signed_green_physical':green,
                        'signed_affine_fixed_centre_residual':residual,
                        'phi_complete_panel_source_integral':pack(v['phi'][0]),
                        'chi_complete_panel_source_integral':pack(v['chi'][0])})
                    prefix[m]=add(prefix[m],v['phi'][0])
                    suffix[m]=after
                writer.add({'kind':'actual_signed_fixed_centre_response',
                    'cell':key[0],'segment':key[1],'panel':gr['panel'],
                    'subpanel':gr['subpanel'],'x_left':gr['x_left'],'x_right':gr['x_right'],
                    'local_V':gr['local_V'],'modes':rows})
                visited+=1
                local+=1
                if visited%64==0:
                    guard()
            writer.close()
            if local!=gm[key]['subpanels']:
                raise ValueError('Incomplete second-pass group')
            groups.append({'cell':key[0],'segment':key[1],
                           'subpanels':local,'chunks':writer.files})
            print(json.dumps({'event':'signed46_whole_residual_group',
                              'cell':key[0],'segment':key[1],'subpanels':local}),flush=True)
        if visited!=count or any(suffix[m]!=ZERO or prefix[m]!=totals[m]['phi'] for m in MODES):
            raise ArithmeticError('Exact complete prefix/suffix identity failed')
        cuts=[]
        for m in MODES:
            oldcentre=pair(axes[m]['exact_centre']) if m in axes else ZERO
            sourcecut=div(totals[m]['chi'],W[m])
            qvalue=sub(add(lin[m],sourcecut),oldcentre)
            cuts.append({'mode':m,'linear_cut_Q':pack(lin[m]),
                'original_cut_Q':pack(oldcentre),
                'signed_fixed_centre_source_cut_Q':pack(sourcecut),
                'signed_affine_cut_minus_original_Q':pack(qvalue),
                'absolute_unsummed_source_cut_upper':bound(total_abs[m]['chi']/exact.minimum_abs(W[m]))})
        gates={
            'actual_formal_zero_geometry_and_complete_source':True,
            'unchanged_true_metric_candidate_and_original_source':True,
            'all10793_source_rows_and_all_actual_geometry_subpanels':visited==expected,
            'all18_groups_and46_modes_retained':len(groups)==18,
            'all_original_signed_source_and_mean_inverse_terms_retained':True,
            'signed_sums_before_absolute_values':True,
            'same_partial_panel_prefix_and_suffix_bounds':True,
            'exact_endpoint_sum_removal_identity':True,
            'true_F_and_signed_Wronskian_used_once':True,
            'no_extra_source_radius_derivative_inserted':True,
            'physical_C_U_read_before_absolute_value':True,
            'radial_component_sup_before_mode_sum':True,
            'old_R88_selected_linear_centre_cancels_exactly':True}
        result={'schema':'visible-flex-fixed-centre-signed46-ordered-consumer-v1',
            'status':'Actual fixed-centre response and affine residual only',
            'all_gates':all(gates.values()),'gates':gates,'modes':MODES,
            'source_sha256':digest(Path(__file__)),'helper_sha256':HELPER_SHA,
            'input_hashes':hashes,'groups':groups,'whole_geometry_subpanels':visited,
            'original_source_panels':10793,'underlying_original_R88_profile_subpanels':10933,
            'source_integrals':{str(m):{z:pack(v) for z,v in rr.items()} for m,rr in totals.items()},
            'cut_rows':cuts,
            'mode_residual_norms':{str(m):{z:bound(v) for z,v in rr.items()} for m,rr in maxima.items()},
            'mode_green_norms':{str(m):{z:bound(v) for z,v in rr.items()} for m,rr in green_max.items()},
            'joint_strong_PK_residual_upper':bound(sum(rr['P']+rr['K'] for rr in maxima.values())),
            'weak_C_residual_upper':bound(sum(rr['C'] for rr in maxima.values())),
            'weak_U_residual_upper':bound(sum(rr['U'] for rr in maxima.values())),
            'complete_beta_or_unknown_field_or_full46_cut_paid':False,
            'all_frequency_outer_PDE_or_closed_surface_claimed':False,
            'actual_Arb_ODE_Node_calls':0,
            'elapsed_seconds':time.monotonic()-began,
            'peak_RSS_KiB':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss}
        guard()
        out=save(str(a.out_prefix)+'-summary.json',result)
        print(json.dumps({'event':'signed46_ordered_complete','all_gates':result['all_gates'],
            'output':out,'sha256':digest(out),'subpanels':visited}),flush=True)
    except BaseException as error:
        save(str(a.out_prefix)+'-failure.json',{'status':'Incomplete; no mathematical nonexistence claim',
            'error_type':type(error).__name__,'error':str(error),'active':active,
            'completed_groups':groups,'input_hashes':hashes,'source_sha256':digest(Path(__file__)),
            'elapsed_seconds':time.monotonic()-began})
        raise

if __name__=='__main__':
    main()
