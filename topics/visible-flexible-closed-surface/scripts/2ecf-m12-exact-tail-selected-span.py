#!/usr/bin/env python3
"""Reconstruct selected original integrated tail polynomials without refitting.

The source data and exact normalized span increments are the original
manifest definition. All coefficients and their accumulated left value
remain Fractions. The output is temporary analysis data, not a new field.
"""
from __future__ import annotations
import argparse, gzip, hashlib, importlib.util, json, time
from fractions import Fraction as Q
from pathlib import Path
import numpy as np

MANIFEST_SHA='cc23977e25a09c34db91723dd784cab4b18b89e325fc2ca2fb8dd7ee6866a104'
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def load(name,p):
    sp=importlib.util.spec_from_file_location(name,p);m=importlib.util.module_from_spec(sp);sp.loader.exec_module(m);return m

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    for k in ('scripts','raw-cache','out'):ap.add_argument('--'+k,type=Path,required=True)
    ap.add_argument('--spans',type=int,nargs='+',required=True)
    a=ap.parse_args();start=time.monotonic()
    if a.out.exists():raise FileExistsError('Fresh exact selected source output required')
    manifest=a.scripts.parent/'notes/2026-11-09-db6f-tail-inc-flat17-m12-critical-r01-s64-q512-manifest.json'
    if sha(manifest)!=MANIFEST_SHA:raise ValueError('Original complete tail definition changed')
    helper=load('selected_original_tail_polynomials',a.scripts/'6a65-m12-tail-polynomial-continuous-bounds-recovered.py')
    producer=load('selected_original_blob_identities',a.scripts/'6a65-m12-stream-tail-exact-endpoint.py')
    meta=json.loads(manifest.read_text());C=meta['format']['coefficientCount'];radial=meta['radialGeometry']
    beta=Q(int(radial['normalization']['numerator']),int(radial['normalization']['denominator']))
    selected=sorted(set(a.spans))
    if not selected or selected[0]<0:raise ValueError('Nonnegative original finite span indices required')
    S1=[Q(0)]*C;S2=[Q(0)]*C;first_value=None;previous=None
    current=Q(radial['innerAnchor']);count=0;rows={};sources=[]
    for block,info in enumerate(meta['files']):
        name=Path(info['path']).name;raw=(a.raw_cache/name).read_bytes()
        key=name.split('-raw')[1].split('.f64')[0].replace('-part','-');blob=producer.BLOBS[key]
        if len(raw)!=info['bytes'] or hashlib.sha256(raw).hexdigest()!=info['sha256'] or hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()!=blob:
            raise ValueError('Original blob identity changed: '+name)
        data=np.frombuffer(gzip.decompress(raw),dtype='<f8').reshape(info['rows'],info['columns'])
        if not np.all(np.isfinite(data)) or (previous is not None and not np.array_equal(data[0],previous)):
            raise ValueError('Original finite source data or shared seam changed')
        values=data[:,2:2+4*C].reshape(len(data),4,C)
        if first_value is None:first_value=[Q.from_float(float(v)) for v in values[0,0]]
        lengths=[Q.from_float(float(v)) for v in data[1:,-1]]
        if not all(v>0 for v in lengths):raise ValueError('Nonpositive original radial increment')
        nodes=[current]
        for ell in lengths:nodes.append(nodes[-1]+beta*ell)
        chosen=[i for i in range(len(lengths)) if count+i in selected]
        for i in chosen:
            rows[count+i]={'source_span':count+i,'left_exact':str(nodes[i]),'right_exact':str(nodes[i+1]),
              'source_file':name,'local_span':i,'V_controls':[],'Vr_controls':[],'Vrr_controls':[]}
        # Cumulative dyadic sums are required only through the last selected
        # span. Remaining raw blocks are still verified and radii checked.
        upto=min(len(lengths),max(0,selected[-1]-count+1))
        if upto:
            for j in range(C):
                first=[Q.from_float(float(v)) for v in values[:upto+1,1,j]]
                second=[Q.from_float(float(v)) for v in values[:upto+1,2,j]]
                mid=[Q.from_float(float(v)) for v in values[1:upto+1,3,j]]
                aa,bb=S1[j],S2[j]
                for i,ell in enumerate(lengths[:upto]):
                    if i in chosen:
                        value=first_value[j]+beta*aa/30+beta*beta*bb/60
                        controls=helper.span_controls(value,first[i],first[i+1],second[i],second[i+1],mid[i],beta*ell)
                        row=rows[count+i]
                        for key,items in zip(('V_controls','Vr_controls','Vrr_controls'),controls):row[key].append([str(v) for v in items])
                    aa+=ell*(7*(first[i]+first[i+1])+16*mid[i])
                    bb+=ell*ell*(second[i]-second[i+1])
                S1[j],S2[j]=aa,bb
        count+=len(lengths);current=nodes[-1];previous=data[-1].copy()
        sources.append({'file':name,'sha256':info['sha256'],'git_blob':blob,'bytes':len(raw)})
        print(json.dumps({'verified_blocks':block+1,'verified_spans':count,'selected_found':sorted(rows),'seconds':time.monotonic()-start}),flush=True)
    if current!=Q(radial['outerAnchor']) or sorted(rows)!=selected:raise ArithmeticError('Incomplete exact selected source reconstruction')
    if any(len(row[key])!=C for row in rows.values() for key in ('V_controls','Vr_controls','Vrr_controls')):
        raise ArithmeticError('Missing exact source Fourier columns')
    out={'schema':'2ecf-M12-original-exact-selected-tail-span-polynomials-v1','script_sha256':sha(__file__),
      'manifest_sha256':MANIFEST_SHA,'polynomial_helper_sha256':sha(helper.__file__),
      'original_blob_table_sha256':sha(producer.__file__),'source_blocks':sources,
      'planar_modes':meta['format']['planarModes'],'height_modes':meta['format']['heightModes'],
      'integrated_value_from_exact_original_cumulative_sums':True,'not_refitted_and_no_nonlinear_field_created':True,
      'exact_all_source_nodes_and_normalization_checked':True,'verified_original_spans':count,
      'selected_spans':[rows[i] for i in selected],'seconds':time.monotonic()-start}
    a.out.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'output':str(a.out),'sha256':sha(a.out),'seconds':out['seconds']}),flush=True)

if __name__=='__main__':main()
