#!/usr/bin/env python3
"""Stream verified historical M12 tail blobs into the exact cut endpoint.

Only one compressed source block is held at a time; binary payloads are not
saved to disk. The exact endpoint is the finite integrated-derivative sum
in db6f_tail_integrated.py, evaluated as Fractions here. Its tiny cache is
an evaluation input, never a replacement mathematical definition.
"""
from __future__ import annotations
import argparse,base64,gzip,hashlib,json,os,time,urllib.request
from fractions import Fraction as Q
from pathlib import Path
import numpy as np

SOURCE_REPOSITORY='Rogerhu12/math-research-public'
SOURCE_COMMIT='aed993f7bd33fc6f545f941171c1b78d67258cca'
SOURCE_NOTES_TREE='b15d0eaf9ab23bb70f4fb7a0a77dd3d9c1af45ad'
BLOBS={
    '000-00': 'c706e8235eca11b8def049afe55ca2ee6b36cf4a',
    '000-01': '5f9c90c55334de4a757b7c88708b7b454951585d',
    '000-02': '1a9cce86c3ad6e88bc07dedb465a08066a62a5ab',
    '001-00': 'cab8375a3d3293050361603a276f6975ff4b9962',
    '001-01': '94f907f44df822c84df25d9a5dc78946f9cbfee3',
    '001-02': 'fc71c0c2316bf647ec09d82bed0c41a508053862',
    '002-00': '6a26e9951a003e535bc944a58dc85ab4ffd895c1',
    '002-01': 'a88c2c8b639d741a025fff5a307e894e86a42ac1',
    '002-02': 'ebd1a3835f9903c45f98c914d66fc4c35b677b6d',
    '003-00': 'aec1723ce66d9cc7bc9407871fdf9f4faf1fe64c',
    '003-01': '9514756f463e0cf03e41ca02e577b9a737a283ed',
    '003-02': 'f9d9b422eb2fd45ceef707e97f0be57fc9bc5708',
    '004-00': '55fa6e78001aac1ca310f3e2ceab6adacb9056a3',
    '004-01': '5e9fa9ac9fb936fcd31da3e12424ef60edc22ba0',
    '004-02': 'd975668d787d989fec0dcf9e26a4a43ef6157448',
    '005-00': '167eddc3ff955d25076bc19e5046d6c064ae9778',
    '005-01': '3fed9cc37ee845b81cadff3d6ff949c7d808ad77',
    '005-02': '1eee161bb4b0767f69fbeaf8344c392fadd593f6',
    '006-00': '34e3db8f99ae9a0911c6ea59071c417bfe43f047',
    '006-01': '2c12db50f44a09c93506e1e86f3a32eff74667b2',
    '006-02': '0aa9d3903c823821c2eb59e8919e59e6a52fa456',
    '007-00': '961c048cd6937f9c7170c096bab88ad7d1048f51',
    '007-01': 'b8f70b9ce797f826bf73f918569b6442ebd1cda4',
    '007-02': '685bf639c2dab9c9bf1474fc937363dff0b030c7',
}

def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def ld(q):return np.longdouble(q.numerator)/np.longdouble(q.denominator)

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--manifest',type=Path,required=True)
    ap.add_argument('--out',type=Path,required=True)
    args=ap.parse_args()
    if args.out.exists():raise FileExistsError('Fresh output required')
    start=time.monotonic();meta=json.loads(args.manifest.read_text())
    if not meta.get('finished'):raise ValueError('Incomplete source manifest')
    fmt=meta['format'];C=fmt['coefficientCount']
    radial=meta['radialGeometry']
    scale=Q(int(radial['normalization']['numerator']),int(radial['normalization']['denominator']))
    inner,outer=Q(radial['innerAnchor']),Q(radial['outerAnchor'])
    S1=[Q(0)]*C;S2=[Q(0)]*C;raw_length=Q(0)
    first_value=None;previous=None;last_first=None;last_second=None
    count=0;receipts=[]
    token=os.environ.get('M12_RECOVERY_TOKEN')
    headers={'User-Agent':'M12-exact-endpoint-restoration','Accept':'application/vnd.github+json'}
    if token:headers['Authorization']='Bearer '+token
    for index,info in enumerate(meta['files']):
        name=Path(info['path']).name
        key=name.split('-raw')[1].split('.f64')[0].replace('-part','-')
        blob=BLOBS[key]
        url='https://api.github.com/repos/'+SOURCE_REPOSITORY+'/git/blobs/'+blob
        req=urllib.request.Request(url,headers=headers)
        with urllib.request.urlopen(req,timeout=60) as response:data=json.load(response)
        if data['sha']!=blob or data['encoding']!='base64':raise ValueError('Wrong GitHub blob identity')
        raw=base64.b64decode(data['content'])
        if len(raw)!=info['bytes'] or hashlib.sha256(raw).hexdigest()!=info['sha256']:raise ValueError('Manifest payload hash mismatch')
        actual_git=hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()
        if actual_git!=blob:raise ValueError('Git blob framing identity mismatch')
        array=np.frombuffer(gzip.decompress(raw),dtype='<f8').reshape(info['rows'],info['columns'])
        if previous is not None and not np.array_equal(array[0],previous):raise ValueError('Tail block interface is not byte-identical')
        values=array[:,2:2+4*C].reshape(len(array),4,C)
        if first_value is None:first_value=[Q.from_float(float(x)) for x in values[0,0]]
        lengths=[Q.from_float(float(x)) for x in array[1:,-1]]
        raw_length+=sum(lengths,Q(0))
        for j in range(C):
            first=[Q.from_float(float(x)) for x in values[:,1,j]]
            second=[Q.from_float(float(x)) for x in values[:,2,j]]
            mid=[Q.from_float(float(x)) for x in values[1:,3,j]]
            aa=Q(0);bb=Q(0)
            for r,(ell,z) in enumerate(zip(lengths,mid)):
                aa+=ell*(7*(first[r]+first[r+1])+16*z)
                bb+=ell*ell*(second[r]-second[r+1])
            S1[j]+=aa;S2[j]+=bb
        count+=len(array)-1
        previous=array[-1].copy()
        last_first=values[-1,1].copy();last_second=values[-1,2].copy()
        receipts.append({'file':name,'git_blob':blob,'sha256':info['sha256'],'bytes':len(raw),'rows':len(array)})
        print(json.dumps({'block':index+1,'blocks':len(meta['files']),'integrated_spans':count,'seconds':time.monotonic()-start}),flush=True)
    if inner+scale*raw_length!=outer:raise ArithmeticError('Exact tail increment normalization misses the outer anchor')
    endpoint=[x+scale*a/30+scale*scale*b/60 for x,a,b in zip(first_value,S1,S2)]
    payload=Path(str(args.out)+'.endpoint.npz')
    np.savez_compressed(payload,endpoint_numerator=np.asarray([str(x.numerator) for x in endpoint]),
                        endpoint_denominator=np.asarray([str(x.denominator) for x in endpoint]),
                        endpoint_numerical=np.asarray([ld(x) for x in endpoint]),first=last_first,second=last_second,
                        planar_modes=np.asarray(fmt['planarModes']),height_modes=np.asarray(fmt['heightModes']))
    out={'schema':'6a65-verified-streaming-M12-tail-exact-rational-cut-endpoint-v1',
         'script_sha256':sha(__file__),'manifest_sha256':sha(args.manifest),'source_repository':SOURCE_REPOSITORY,
         'source_commit':SOURCE_COMMIT,'source_notes_tree':SOURCE_NOTES_TREE,'source_blocks':receipts,
         'source_compressed_bytes':sum(x['bytes'] for x in receipts),'integrated_spans':count,
         'endpoint_coefficients':C,'exact_radial_normalization_checked':True,'outer_radius_exact':str(outer),
         'endpoint_definition':'source first value + scale*S1/30 + scale^2*S2/60, all Fractions; S1=sum ell*(7*(Fr0+Fr1)+16*Frmid), S2=sum ell^2*(Frr0-Frr1)',
         'endpoint_cache_sha256':sha(payload),'binary_source_payloads_saved':False,'seconds':time.monotonic()-start}
    args.out.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))

if __name__=='__main__':main()

