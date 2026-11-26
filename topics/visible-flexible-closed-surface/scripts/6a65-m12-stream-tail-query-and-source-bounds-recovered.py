#!/usr/bin/env python3
"""Recovered full-tail source bound and exact diagnostic-query consumer.

New source identity after the 2026-11-26 local executor loss. The earlier
unpublished C_X streamer is not claimed to have this file identity.
Recover exact rational coefficients at requested radii of the original tail.

The 24 original blobs are streamed and verified. Every requested value,
first derivative, and second derivative is evaluated in Fraction arithmetic
from the original integrated-quartic source, including exact normalized
radial increments. The true deep collar is the original quintic C2 field.
Only the final numerical evaluation cache is rounded to long double.

This cache is an evaluator of one fixed source, not a new interpolation or
a replacement of the same source between queried points. No raw payload is
written into the repository, a release, or an artifact by this program.
"""
from __future__ import annotations
import argparse,base64,bisect,gzip,hashlib,importlib.util,json,os,time,urllib.request
from fractions import Fraction as Q
from pathlib import Path
import numpy as np

LD=np.longdouble
MANIFEST_SHA='cc23977e25a09c34db91723dd784cab4b18b89e325fc2ca2fb8dd7ee6866a104'
def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def ld(q):return LD(q.numerator)/LD(q.denominator)
def fraction(v):return Q.from_float(v) if isinstance(v,float) else Q(v)


def span_jet(value,f0,f1,second0,second1,midpoint,length,t):
    v0,v1=length*second0,length*second1
    bubble=16*midpoint-8*(f0+f1)-2*(v0-v1)
    c=[f0,v0,-3*f0+3*f1-2*v0-v1+bubble,2*f0-2*f1+v0+v1-2*bubble,bubble]
    F=sum((a*t**k for k,a in enumerate(c)),Q(0))
    FF=sum((k*c[k]*t**(k-1) for k in range(1,5)),Q(0))/length
    X=value+length*sum((a*t**(k+1)/(k+1) for k,a in enumerate(c)),Q(0))
    return X,F,FF



def recover_payload(producer,blob,info,transport,headers):
    name=Path(info['path']).name
    if transport=='git-blob-api':
        url='https://api.github.com/repos/'+producer.SOURCE_REPOSITORY+'/git/blobs/'+blob
        with urllib.request.urlopen(urllib.request.Request(url,headers=headers),timeout=60) as response:
            payload=json.load(response)
        if payload['sha']!=blob or payload['encoding']!='base64':raise ValueError('Wrong Git blob response')
        raw=base64.b64decode(payload['content'])
    else:
        commit='aed993f7bd33fc6f545f941171c1b78d67258cca'
        url=('https://raw.githubusercontent.com/'+producer.SOURCE_REPOSITORY+'/'+commit+
             '/topics/visible-flexible-closed-surface/notes/'+name)
        public_headers={'User-Agent':'M12-original-source-verified-public-raw','Accept':'application/octet-stream'}
        with urllib.request.urlopen(urllib.request.Request(url,headers=public_headers),timeout=60) as response:
            raw=response.read()
    if len(raw)!=info['bytes'] or hashlib.sha256(raw).hexdigest()!=info['sha256']:
        raise ValueError('Wrong manifest payload')
    if hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()!=blob:
        raise ValueError('Wrong Git blob framing')
    return raw

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--manifest',type=Path,required=True);ap.add_argument('--queries',type=Path,required=True)
    ap.add_argument('--endpoint-producer',type=Path,default=Path(__file__).with_name('6a65-m12-stream-tail-exact-endpoint.py'))
    ap.add_argument('--out',type=Path,required=True)
    ap.add_argument('--source-transport',choices=('git-blob-api','raw-known-commit'),default='git-blob-api')
    ap.add_argument('--diagnostic-window',nargs=2,metavar=('R_MIN','R_MAX'))
    ap.add_argument('--diagnostic-subdivisions',type=int,default=4)
    ap.add_argument('--diagnostic-limit',type=int,default=8192)
    args=ap.parse_args()
    helper_path=Path(__file__).with_name('6a65-m12-tail-polynomial-continuous-bounds-recovered.py')
    spec=importlib.util.spec_from_file_location('original_tail_continuous_bounds',helper_path)
    helper=importlib.util.module_from_spec(spec);spec.loader.exec_module(helper)
    if args.out.exists() or Path(str(args.out)+'.npz').exists():raise FileExistsError('Fresh query cache required')
    if sha(args.manifest)!=MANIFEST_SHA:raise ValueError('Wrong original tail manifest')
    spec=importlib.util.spec_from_file_location('original_endpoint_blob_table',args.endpoint_producer)
    producer=importlib.util.module_from_spec(spec);spec.loader.exec_module(producer)
    meta=json.loads(args.manifest.read_text());query_record=json.loads(args.queries.read_text())
    radii=sorted(set(fraction(v) for v in query_record['radii']))
    if not radii or len(radii)>12000:raise ValueError('Require 1..12000 distinct requested radii')
    fmt=meta['format'];C=fmt['coefficientCount'];radial=meta['radialGeometry']
    scale=Q(int(radial['normalization']['numerator']),int(radial['normalization']['denominator']))
    inner,outer=Q(radial['innerAnchor']),Q(radial['outerAnchor']);cuff=Q.from_float(meta['parameters']['rCuff'])
    if radii[0]<cuff or radii[-1]>outer:raise ValueError('Requested radius leaves the true tail/collar domain')
    budget=helper.TailContinuousBounds(fmt['planarModes'],fmt['heightModes'],cuff)
    diagnostic_window=None if args.diagnostic_window is None else tuple(Q(v) for v in args.diagnostic_window)
    if diagnostic_window is not None and not inner<=diagnostic_window[0]<diagnostic_window[1]<=outer:
        raise ValueError('Diagnostic window must lie in the original finite tail')
    if not 1<=args.diagnostic_subdivisions<=32 or not 1<=args.diagnostic_limit<=12000:
        raise ValueError('Invalid small diagnostic request')
    diag_radii=[];diag_values=[];diag_lookup={};diag_spans=[]
    diag_point_span=[]
    out=np.full((len(radii),3,C),np.nan,dtype=LD);filled=np.zeros(len(radii),dtype=bool)
    S1=[Q(0)]*C;S2=[Q(0)]*C;first_value=None;previous=None;first_first=None;first_second=None
    last_first=None;last_second=None;count=0;receipts=[];current_radius=inner
    token=os.environ.get('M12_RECOVERY_TOKEN');headers={'User-Agent':'M12-exact-rational-tail-queries','Accept':'application/vnd.github+json'}
    if token:headers['Authorization']='Bearer '+token
    start=time.monotonic()
    for block,info in enumerate(meta['files']):
        name=Path(info['path']).name;key=name.split('-raw')[1].split('.f64')[0].replace('-part','-')
        blob=producer.BLOBS[key]
        raw=recover_payload(producer,blob,info,args.source_transport,headers)
        array=np.frombuffer(gzip.decompress(raw),dtype='<f8').reshape(info['rows'],info['columns'])
        if not np.all(np.isfinite(array)):raise ValueError('Nonfinite original source')
        if previous is not None and not np.array_equal(array[0],previous):raise ValueError('Shared original rows differ')
        values=array[:,2:2+4*C].reshape(len(array),4,C)
        if first_value is None:
            first_value=[Q.from_float(float(v)) for v in values[0,0]]
            first_first=[Q.from_float(float(v)) for v in values[0,1]]
            first_second=[Q.from_float(float(v)) for v in values[0,2]]
        lengths=[Q.from_float(float(v)) for v in array[1:,-1]]
        if min(lengths)<=0:raise ValueError('Nonpositive exact source increment')
        nodes=[current_radius]
        for length in lengths:nodes.append(nodes[-1]+scale*length)
        budget.begin_block(nodes)
        diag_assignments={}
        if diagnostic_window is not None:
            for i,(left,right) in enumerate(zip(nodes,nodes[1:])):
                if right<diagnostic_window[0] or left>diagnostic_window[1]:continue
                global_span=count+i
                diag_spans.append({'source_span':global_span,'source_file':name,'local_span':i,
                                   'left_exact':str(left),'right_exact':str(right)})
                for k in range(args.diagnostic_subdivisions+1):
                    t=Q(k,args.diagnostic_subdivisions);r=left+t*(right-left)
                    if r in diag_lookup:continue
                    qi=len(diag_radii)
                    if qi>=args.diagnostic_limit:raise ValueError('Diagnostic query limit exceeded')
                    diag_lookup[r]=qi;diag_radii.append(r)
                    diag_values.append(np.full((3,C),np.nan,dtype=LD));diag_point_span.append(global_span)
                    diag_assignments.setdefault(i,[]).append((qi,t))
        assignments={}
        qstart=bisect.bisect_left(radii,nodes[0]);qstop=bisect.bisect_right(radii,nodes[-1])
        for qi in range(qstart,qstop):
            if filled[qi]:continue
            span=min(len(lengths)-1,max(0,bisect.bisect_right(nodes,radii[qi])-1))
            t=(radii[qi]-nodes[span])/(scale*lengths[span])
            if not 0<=t<=1:raise ArithmeticError('Exact source query localization failed')
            assignments.setdefault(span,[]).append((qi,t))
        for j in range(C):
            first=[Q.from_float(float(v)) for v in values[:,1,j]]
            second=[Q.from_float(float(v)) for v in values[:,2,j]]
            mid=[Q.from_float(float(v)) for v in values[1:,3,j]]
            aa,bb=S1[j],S2[j]
            for i,ell in enumerate(lengths):
                value=first_value[j]+scale*aa/30+scale*scale*bb/60
                budget.add_span_coefficient(i,j,value,first[i],first[i+1],second[i],second[i+1],mid[i],scale*ell)
                for qi,t in assignments.get(i,()):
                    jet=span_jet(value,first[i],first[i+1],second[i],second[i+1],mid[i],scale*ell,t)
                    out[qi,:,j]=[ld(v) for v in jet]
                for qi,t in diag_assignments.get(i,()):
                    jet=span_jet(value,first[i],first[i+1],second[i],second[i+1],mid[i],scale*ell,t)
                    diag_values[qi][:,j]=[ld(v) for v in jet]
                aa+=ell*(7*(first[i]+first[i+1])+16*mid[i])
                bb+=ell*ell*(second[i]-second[i+1])
            S1[j],S2[j]=aa,bb
        for assigned in assignments.values():
            for qi,unused in assigned:filled[qi]=True
        budget.finish_block()
        current_radius=nodes[-1];previous=array[-1].copy()
        last_first=values[-1,1].copy();last_second=values[-1,2].copy();count+=len(lengths)
        receipts.append({'file':name,'git_blob':blob,'sha256':info['sha256'],'bytes':len(raw),'rows':len(array)})
        print(json.dumps({'block':block+1,'blocks':len(meta['files']),'integrated_spans':count,
                          'filled_finite_queries':int(filled.sum()),'seconds':time.monotonic()-start}),flush=True)
    if current_radius!=outer:raise ArithmeticError('Exact radial normalization misses the original cut')
    budget.add_deep_collar(inner,first_value,first_first,first_second)
    h=inner-cuff
    for qi,r in enumerate(radii):
        if r>=inner:continue
        t=(r-cuff)/h
        for j,(a0,a1,a2) in enumerate(zip(first_value,first_first,first_second)):
            c3=10*a0-4*h*a1+h*h*a2/2;c4=-15*a0+7*h*a1-h*h*a2;c5=6*a0-3*h*a1+h*h*a2/2
            out[qi,0,j]=ld(c3*t**3+c4*t**4+c5*t**5)
            out[qi,1,j]=ld((3*c3*t*t+4*c4*t**3+5*c5*t**4)/h)
            out[qi,2,j]=ld((6*c3*t+12*c4*t*t+20*c5*t**3)/(h*h))
        filled[qi]=True
    if not np.all(filled) or not np.all(np.isfinite(out)):raise ArithmeticError('Incomplete exact tail query coverage')
    endpoint=[v+scale*a/30+scale*scale*b/60 for v,a,b in zip(first_value,S1,S2)]
    diagnostic_array=np.asarray(diag_values,dtype=LD).reshape(len(diag_radii),3,C)
    if not np.all(np.isfinite(diagnostic_array)):raise ArithmeticError('Incomplete original-span diagnostic queries')
    cache=Path(str(args.out)+'.npz')
    np.savez_compressed(cache,query_fraction=np.asarray([str(r) for r in radii]),query_radius=np.asarray([ld(r) for r in radii]),
                        coefficients=out,endpoint_numerator=np.asarray([str(q.numerator) for q in endpoint]),
                        endpoint_denominator=np.asarray([str(q.denominator) for q in endpoint]),
                        endpoint_numerical=np.asarray([ld(q) for q in endpoint]),first=last_first,second=last_second,
                        planar_modes=np.asarray(fmt['planarModes']),height_modes=np.asarray(fmt['heightModes']),
                        diagnostic_fraction=np.asarray([str(r) for r in diag_radii]),
                        diagnostic_radius=np.asarray([ld(r) for r in diag_radii],LD),
                        diagnostic_coefficients=diagnostic_array,
                        diagnostic_source_span=np.asarray(diag_point_span,dtype=np.int64))
    report={'schema':'6a65-original-M12-exact-tail-queries-and-continuous-source-recovered-v2','script_sha256':sha(__file__),
            'continuous_bounds_helper_sha256':sha(helper_path),'source_transport':args.source_transport,
            'continuous_original_source_second_jets':budget.receipt(),
            'diagnostic_window_exact':None if diagnostic_window is None else [str(v) for v in diagnostic_window],
            'diagnostic_subdivisions':args.diagnostic_subdivisions,'diagnostic_query_count':len(diag_radii),
            'diagnostic_source_spans':diag_spans,
            'manifest_sha256':MANIFEST_SHA,'endpoint_cache_sha256':sha(cache),'query_file_sha256':sha(args.queries),
            'endpoint_blob_table_sha256':sha(args.endpoint_producer),'queries':len(radii),'integrated_spans':count,
            'true_cuff_exact':str(cuff),'finite_inner_exact':str(inner),'outer_cut_exact':str(outer),
            'coefficient_arithmetic':'Exact Fraction through value/first/second derivative, then numerical long-double evaluation cache',
            'cache_is_not_a_new_interpolating_field':True,'same_original_tail_including_deep_collar':True,
            'continuous_metric_certificate':False,'source_blocks':receipts,'seconds':time.monotonic()-start}
    args.out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2))


if __name__=='__main__':main()

