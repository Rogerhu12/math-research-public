#!/usr/bin/env python3
"""Small, source-bound checks of the entire-half consumer interfaces.

Fetches only the original final 1.79 MB block. Two adjacent spans use a
local primitive anchor, explicitly not the unavailable global value sum.
The original derivative data, normalized span lengths, angular modes,
reflected height, and full physical/material two-jet transformations are
checked. No nonlinear solve or continuous metric certificate is claimed.
"""
import argparse,base64,gzip,hashlib,importlib.util,json,time,urllib.request
from fractions import Fraction as Q
from pathlib import Path
from types import SimpleNamespace
import numpy as np

LD=np.longdouble
def load(name,path):
    s=importlib.util.spec_from_file_location(name,path);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def ld(q):return LD(q.numerator)/LD(q.denominator)
def fq(x):return Q.from_float(float(x))

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--scripts',type=Path,required=True);ap.add_argument('--new-scripts',type=Path,default=Path(__file__).parent)
    ap.add_argument('--data',type=Path,required=True);ap.add_argument('--directory',type=Path,required=True)
    args=ap.parse_args();args.directory.mkdir(parents=True,exist_ok=True);began=time.monotonic()
    old=load('interface_old_endpoint',args.scripts/'6a65-m12-stream-tail-exact-endpoint.py')
    query=load('interface_new_queries',args.new_scripts/'6a65-m12-stream-tail-query-cache.py')
    whole=load('interface_entire_half',args.new_scripts/'6a65-m12-entire-half-cartesian-bvp.py')
    joint=load('interface_joint_prefix',args.scripts/'6a65-m12-global-common-cut-position-recovered.py')
    meta_path=args.scripts.parent/'notes/2026-11-09-db6f-tail-inc-flat17-m12-critical-r01-s64-q512-manifest.json'
    meta=json.loads(meta_path.read_text());info=meta['files'][-1];blob=old.BLOBS['000-02'];C=meta['format']['coefficientCount']
    raw_path=args.directory/'original-final-tail-block.f64.gz'
    if not raw_path.exists():
        url='https://api.github.com/repos/'+old.SOURCE_REPOSITORY+'/git/blobs/'+blob
        headers={'User-Agent':'M12-readonly-interface-check','Accept':'application/vnd.github+json'}
        with urllib.request.urlopen(urllib.request.Request(url,headers=headers),timeout=60) as r:payload=json.load(r)
        if payload['sha']!=blob or payload['encoding']!='base64':raise ValueError('Wrong original block response')
        raw_path.write_bytes(base64.b64decode(payload['content']))
    raw=raw_path.read_bytes()
    if len(raw)!=info['bytes'] or sha(raw_path)!=info['sha256']:raise ValueError('Original final block SHA/size mismatch')
    if hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()!=blob:raise ValueError('Original Git framing mismatch')
    data=np.frombuffer(gzip.decompress(raw),dtype='<f8').reshape(info['rows'],info['columns'])
    rows=data[-3:,2:2+4*C].reshape(3,4,C)
    scale=Q(int(meta['radialGeometry']['normalization']['numerator']),int(meta['radialGeometry']['normalization']['denominator']))
    lengths=[scale*fq(x) for x in data[-2:,-1]];outer=Q(meta['radialGeometry']['outerAnchor'])
    tested_t=[Q(0),Q(1,7),Q(1,3),Q(1,2),Q(5,6),Q(1)]
    defects={key:Q(0) for key in ('left_first','right_first','left_second','right_second','midpoint_first','integral','shared_value','shared_first','shared_second')}
    original_anchor=[fq(x) for x in rows[0,0]];anchor=original_anchor.copy();all_jets=[]
    for i,L in enumerate(lengths):
        saved=[];end=[]
        for j in range(C):
            f0,f1=fq(rows[i,1,j]),fq(rows[i+1,1,j]);s0,s1=fq(rows[i,2,j]),fq(rows[i+1,2,j]);mid=fq(rows[i+1,3,j])
            jets=[query.span_jet(anchor[j],f0,f1,s0,s1,mid,L,t) for t in tested_t]
            expected=anchor[j]+L*(7*(f0+f1)+16*mid)/30+L*L*(s0-s1)/60
            values={'left_first':jets[0][1]-f0,'right_first':jets[-1][1]-f1,
                    'left_second':jets[0][2]-s0,'right_second':jets[-1][2]-s1,
                    'midpoint_first':jets[3][1]-mid,'integral':jets[-1][0]-expected}
            if i:
                values.update({'shared_value':jets[0][0]-all_jets[-1][j][-1][0],
                               'shared_first':jets[0][1]-all_jets[-1][j][-1][1],
                               'shared_second':jets[0][2]-all_jets[-1][j][-1][2]})
            for key,value in values.items():defects[key]=max(defects[key],abs(value))
            saved.append(jets);end.append(jets[-1][0])
        all_jets.append(saved);anchor=end
    if any(defects.values()):raise ArithmeticError('Exact two-span interface failed')
    # True cut derivative witness is independent of the unavailable global primitive value.
    P=len(meta['format']['planarModes']);A=sum((fq(x) for x in rows[-1,1,:P]),Q(0));B=sum((fq(x) for x in rows[-1,1,P:]),Q(0))
    fixed_cut_E=((1+A)**2+(Q(1,2)+B)**2)/Q(5,4)-1
    # Feed the actual final derivative jets and a transported local value
    # into the complete public consumer; compare with cylindrical formulas.
    c=np.asarray([[ld(q) for q in anchor],rows[-1,1],rows[-1,2]],LD)
    tail=whole.TailQueries.__new__(whole.TailQueries);tail.pm=np.asarray(meta['format']['planarModes']);tail.hm=np.asarray(meta['format']['heightModes'])
    tail.coefficients=c[None];tail.lookup={whole.exact_key(ld(outer)):0}
    unused,central_c=joint.ad.exact_section(args.data,Q(0));central=joint.ad.NativeCurve(central_c,512,32)
    r=ld(outer);w=LD('.5');wr=-7*w/r
    bg=SimpleNamespace(point=lambda radius:(w,wr,LD(0),LD(0),0,8,LD(1)))
    position=whole.WholePosition(SimpleNamespace(cut_height=LD(0)),central,SimpleNamespace(background=bg),tail,joint)
    N=768;actual,bb=position.tail_point(r,N);u,rho,rhop=map(lambda a:np.asarray(a,LD),position.angular(N))
    er=np.stack((np.cos(u),np.sin(u),np.zeros_like(u)),axis=-1);et=np.stack((-np.sin(u),np.cos(u),np.zeros_like(u)),axis=-1)
    k=np.asarray(tail.pm-1,LD);hm=np.asarray(tail.hm,LD);phase=k[:,None]*u[None,:];zphase=hm[:,None]*u[None,:]
    fields={}
    for dr in range(3):
        for du in range(3-dr):
            z=np.sum(c[dr,:P,None]*(1j*k[:,None])**du*(np.cos(phase)+1j*np.sin(phase)),axis=0)
            height=np.sum(c[dr,P:,None]*np.real((1j*hm[:,None])**du*(np.cos(zphase)+1j*np.sin(zphase))),axis=0)
            fields[dr,du]=(z.real,z.imag,height)
    R,T,Z=fields[0,0];Rr,Tr,Zr=fields[1,0];Rrr,Trr,Zrr=fields[2,0]
    Ru,Tu,Zu=fields[0,1];Rru,Tru,Zru=fields[1,1];Ruu,Tuu,Zuu=fields[0,2]
    def vector(a,b,z):
        v=a[:,None]*er+b[:,None]*et;v[:,2]=z;return v
    X=vector(r+R,T,-Z);Xr=vector(1+Rr,Tr,-w-Zr);Xu=vector(Ru-T,r+R+Tu,-Zu)
    Xrr=vector(Rrr,Trr,-wr-Zrr);Xru=vector(Rru-Tr,1+Rr+Tru,-Zru)
    Xuu=vector(Ruu-r-R-2*Tu,2*Ru+Tuu-T,-Zuu)
    E=1+w*w;rs=-1/np.sqrt(E);rss=-w*wr/(E*E)
    expected=np.stack((X,rs*Xr,rho[:,None]*Xu,rs*rs*Xrr+rss*Xr,
                       rs*rho[:,None]*Xru,rho[:,None]**2*Xuu+rhop[:,None]*Xu))
    jet_difference=np.max(abs(np.asarray(actual,LD)-expected),axis=(1,2))
    cylE=(2*Rr+Rr*Rr+Tr*Tr+Zr*Zr+2*w*Zr)/E
    cylF=-((1+Rr)*(Ru-T)+Tr*(r+R+Tu)+(w+Zr)*Zu)/(r*np.sqrt(E))
    cylG=((Ru-T)**2+2*r*(R+Tu)+(R+Tu)**2+Zu*Zu)/(r*r)
    expected_gram=np.stack((cylE,np.sqrt(LD(2))*cylF,cylG),axis=-1)
    actual_gram=joint.bvp.gram(actual[1],actual[2],bb)
    gram_difference=float(np.max(abs(np.asarray(actual_gram,LD)-expected_gram)))
    if max(jet_difference)>LD('3e-14') or gram_difference>3e-14:raise ArithmeticError('Complete tail jet/Gram transformation mismatch')
    # Exact requested keys survive the final numerical cache conversion.
    roundtrip=whole.exact_key(ld(outer))==str(outer)
    if not roundtrip:raise ArithmeticError('Exact cut query key does not round-trip')
    record={'schema':'6a65-M12-entire-half-interface-check-v1','script_sha256':sha(__file__),
            'query_source_sha256':sha(Path(query.__file__)),'whole_source_sha256':sha(Path(whole.__file__)),
            'source_blob':blob,'source_sha256':sha(raw_path),'source_bytes':len(raw),
            'original_normalization_exact':str(scale),'local_span_lengths_exact':[str(x) for x in lengths],
            'coefficients_checked':C,'adjacent_spans':2,'exact_query_points_per_span':len(tested_t),
            'exact_defects':{k:str(v) for k,v in defects.items()},
            'local_value_anchor_is_not_global_integrated_value':True,
            'angular_points':N,'actual_central_chart_used':True,'six_jet_component_differences':[float(x) for x in jet_difference],
            'full_normalized_gram_difference':gram_difference,'true_cut_query_key_roundtrip':roundtrip,
            'exact_fixed_cut_E_minus_1_at_u_0':str(fixed_cut_E),'exact_fixed_cut_E_minus_1_approx':float(fixed_cut_E),
            'fixed_cut_witness_scope':'Only consumers that freeze the original radius-.6 full first trace; the entire-half correction releases this interior seam.',
            'all_24_block_query_run_performed':False,'whole_half_solve_performed':False,'seconds':time.monotonic()-began}
    target=args.directory/'entire-half-interface-check.json';target.write_text(json.dumps(record,indent=2)+'\n')
    print(json.dumps(record,indent=2))

if __name__=='__main__':main()
