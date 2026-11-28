#!/usr/bin/env python3
"""Certified point evaluations of exact R250 Q on an actual source recipe.

Original source radii and smoothing windows are exact Fractions. The flat
switch exp() is enclosed with rational alternating Taylor series, dyadic
outward rounding, and repeated squaring. Every final longdouble store is
compared against its exact rational interval, including all 141 channels.
The resulting cache is temporary data, not a new interpolating source.
"""
from __future__ import annotations
import argparse,bisect,gzip,hashlib,importlib.util,json,time
from fractions import Fraction as Q
from pathlib import Path
import numpy as np

MANIFEST_SHA='cc23977e25a09c34db91723dd784cab4b18b89e325fc2ca2fb8dd7ee6866a104'
SMOOTHER_SHA='30b1384fed8e7a6018c99ba688b091bb42dfb2451e2df39531c9df0d88aa34b7'
BITS=256;D=1<<BITS
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def load(name,p):
    sp=importlib.util.spec_from_file_location(name,p);m=importlib.util.module_from_spec(sp);sp.loader.exec_module(m);return m
def floorq(q):return q.numerator//q.denominator
def ceilq(q):return -((-q.numerator)//q.denominator)
def packet(q):return {'exact':str(q),'display':float(q)}

class I:
    __slots__=('lo','hi')
    def __init__(self,lo,hi=None):
        self.lo=int(lo);self.hi=int(lo if hi is None else hi)
        if self.lo>self.hi:raise ArithmeticError('Inverted interval')
    @classmethod
    def exact(cls,q):
        q=Q(q)*D;return cls(floorq(q),ceilq(q))
    def __add__(self,b):
        if not isinstance(b,I):b=I.exact(b)
        return I(self.lo+b.lo,self.hi+b.hi)
    __radd__=__add__
    def __neg__(self):return I(-self.hi,-self.lo)
    def __sub__(self,b):return self+-b if isinstance(b,I) else self+I.exact(-Q(b))
    def __rsub__(self,b):return I.exact(b)+(-self)
    def __mul__(self,b):
        if not isinstance(b,I):return self.mulq(Q(b))
        products=(self.lo*b.lo,self.lo*b.hi,self.hi*b.lo,self.hi*b.hi)
        low,high=min(products),max(products)
        return I(low//D,-((-high)//D))
    __rmul__=__mul__
    def mulq(self,q):
        a=Q(self.lo)*q;b=Q(self.hi)*q
        return I(floorq(min(a,b)),ceilq(max(a,b)))
    def reciprocal(self):
        if self.lo<=0:raise ArithmeticError('Reciprocal interval must be positive')
        return I((D*D)//self.hi,-((-D*D)//self.lo))
    def __truediv__(self,b):
        return self*b.reciprocal() if isinstance(b,I) else self.mulq(1/Q(b))

def negative_exp(a):
    """Enclose exp(-a), a exact nonnegative rational."""
    a=Q(a)
    if a<0:raise ValueError('negative_exp expects a >= 0')
    if a>=BITS:
        # e>2 implies exp(-a)<2**(-BITS), with no giant integer power.
        return I(0,1)
    k=0;y=a
    while y>Q(1,16):y/=2;k+=1
    term=Q(1);total=term
    for n in range(1,41):term*=-y/n;total+=term
    # Degree 40 is even (upper); next partial sum is lower.
    lower=total-term*y/41
    out=I(floorq(lower*D),ceilq(total*D))
    for unused in range(k):out=out*out
    return out

def switch_weight_intervals(x,delta):
    """Q weight S-H and its two physical-r derivatives."""
    if not -delta<x<delta:raise ValueError('Interior window point required')
    if x==0:return None
    t=(x+delta)/(2*delta)
    T=1/(1-t)-1/t
    e=negative_exp(abs(T));small=e/(I.exact(1)+e)
    # Avoid subtracting an exponential from one at a nearly flat endpoint.
    weight=small if x<0 else -small
    product=small*(1-small)
    Tp=1/t**2+1/(1-t)**2
    Tpp=-2/t**3+2/(1-t)**3
    sign=1 if x<0 else -1
    Sp=product*Tp
    Spp=product*(sign*(1-2*small)*Tp**2+Tpp)
    return weight,Sp/(2*delta),Spp/(4*delta**2)

def source_q_at(x,delta,jumps):
    if x==0:return np.zeros((3,len(jumps[0])),np.longdouble),[[Q(0)]*len(jumps[0]) for _ in range(3)]
    w,w1,w2=switch_weight_intervals(x,delta)
    rows=np.empty((3,len(jumps[0])),np.longdouble);errors=[[],[],[]]
    for j in range(len(jumps[0])):
        A3,A4,A5=[jumps[k][j] for k in range(3)]
        v=x**3*A3/6+x**4*A4/24+x**5*A5/120
        v1=x*x*A3/2+x**3*A4/6+x**4*A5/24
        v2=x*A3+x*x*A4/2+x**3*A5/6
        values=(w*v,w1*v+w*v1,w2*v+2*w1*v1+w*v2)
        for d,z in enumerate(values):
            mid=Q(z.lo+z.hi,2*D)
            stored=np.longdouble(mid.numerator)/np.longdouble(mid.denominator)
            if not np.isfinite(stored):raise ArithmeticError('Nonfinite stored Q coefficient')
            exact_stored=Q(*stored.as_integer_ratio())
            error=max(abs(exact_stored-Q(z.lo,D)),abs(exact_stored-Q(z.hi,D)))
            rows[d,j]=stored;errors[d].append(error)
    return rows,errors

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--scripts',type=Path,required=True)
    ap.add_argument('--smoother',type=Path,required=True)
    ap.add_argument('--smoothing-report',type=Path,required=True)
    ap.add_argument('--source-report',type=Path,required=True)
    ap.add_argument('--source-cache',type=Path,required=True)
    ap.add_argument('--cache-dir',type=Path,required=True)
    ap.add_argument('--out',type=Path,required=True)
    args=ap.parse_args();output_cache=Path(str(args.out)+'.npz');began=time.monotonic()
    if args.out.exists() or output_cache.exists():raise FileExistsError('Fresh Q query cache required')
    if sha(args.smoother)!=SMOOTHER_SHA:raise ValueError('Accurate R250 smoothing source changed')
    smoother=load('accurate_smoother',args.smoother)
    proof=json.loads(args.smoothing_report.read_text());source=json.loads(args.source_report.read_text())
    if proof['script_sha256']!=SMOOTHER_SHA or not proof['complete_original_finite_tail']:raise ValueError('Complete same-source smoothing proof required')
    if proof['manifest_sha256']!=MANIFEST_SHA or source['manifest_sha256']!=MANIFEST_SHA:raise ValueError('Source manifest changed')
    if source['endpoint_cache_sha256']!=sha(args.source_cache):raise ValueError('Actual original source cache differs')
    with np.load(args.source_cache,allow_pickle=False) as a:
        original_queries=list(map(str,a['query_fraction']))
        diagnostic_queries=list(map(str,a['diagnostic_fraction'])) if 'diagnostic_fraction' in a else []
        pm=a['planar_modes'].copy();hm=a['height_modes'].copy()
    queries=sorted(set(map(Q,original_queries+diagnostic_queries)));index={q:i for i,q in enumerate(queries)}
    coeff=np.zeros((len(queries),3,141),np.longdouble)
    mp=args.scripts.parent/'notes/2026-11-09-db6f-tail-inc-flat17-m12-critical-r01-s64-q512-manifest.json'
    if sha(mp)!=MANIFEST_SHA:raise ValueError('Original manifest identity')
    manifest=json.loads(mp.read_text());fmt=manifest['format'];C=fmt['coefficientCount']
    if C!=141 or list(pm)!=fmt['planarModes'] or list(hm)!=fmt['heightModes']:raise ValueError('Changed complete modes')
    modes=list(map(int,np.r_[pm,hm]))
    producer=load('original_Q_blob_table',args.scripts/'6a65-m12-stream-tail-exact-endpoint.py')
    reader=load('original_Q_payloads',args.scripts/'6a65-m12-stream-tail-query-and-source-bounds-recovered.py')
    beta=Q(int(manifest['radialGeometry']['normalization']['numerator']),int(manifest['radialGeometry']['normalization']['denominator']))
    pieces=[];lengths=[];previous=None;blobs=[]
    for block,info in enumerate(manifest['files']):
        name=Path(info['path']).name;key=name.split('-raw')[1].split('.f64')[0].replace('-part','-');blob=producer.BLOBS[key]
        p=args.cache_dir/name
        if p.exists():raw=p.read_bytes()
        else:
            raw=reader.recover_payload(producer,blob,info,'raw-known-commit',{})
            p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(raw)
        if len(raw)!=info['bytes'] or hashlib.sha256(raw).hexdigest()!=info['sha256'] or hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()!=blob:
            raise ValueError('Original raw source block identity')
        a=np.frombuffer(gzip.decompress(raw),dtype='<f8').reshape(info['rows'],info['columns'])
        if previous is not None and not np.array_equal(a[0],previous):raise ValueError('Shared original rows differ')
        v=a[:,2:2+4*C].reshape(len(a),4,C)
        pieces.append(v[0 if block==0 else 1:,1:4,:].copy())
        lengths.extend(beta*Q.from_float(float(x)) for x in a[1:,-1]);previous=a[-1].copy()
        blobs.append({'block':block,'git_blob':blob,'sha256':info['sha256']})
    data=np.concatenate(pieces);del pieces
    nodes=[Q(manifest['radialGeometry']['innerAnchor'])]
    for L in lengths:
        if L<=0:raise ValueError('Nonpositive source span')
        nodes.append(nodes[-1]+L)
    if nodes[-1]!=Q(manifest['radialGeometry']['outerAnchor']) or len(lengths)!=18552:raise ValueError('Incomplete exact original physical radius chain')
    native_errors={(d,j):Q(0) for d in range(3) for j in range(3-d)};native_value={k:Q(0) for k in native_errors}
    contributing=0;inside_points=0;node_points=0;assigned=set();digest=hashlib.sha256();maxima={};divisor=proof['divisor']
    for i in range(1,len(nodes)-1):
        center=nodes[i];delta=min(lengths[i-1],lengths[i])/divisor
        lo=bisect.bisect_right(queries,center-delta);hi=bisect.bisect_left(queries,center+delta)
        if lo==hi:continue
        contributing+=1
        left_end=[];right_start=[]
        for j in range(C):
            def fj(k,a):return Q.from_float(float(data[k,a,j]))
            unused,left=smoother.higher_end_jets(fj(i-1,0),fj(i,0),fj(i-1,1),fj(i,1),fj(i,2),lengths[i-1])
            right,unused=smoother.higher_end_jets(fj(i,0),fj(i+1,0),fj(i,1),fj(i+1,1),fj(i+1,2),lengths[i])
            left_end.append(left);right_start.append(right)
        jumps=[[right_start[j][k]-left_end[j][k] for j in range(C)] for k in range(3)]
        for qi in range(lo,hi):
            if qi in assigned:raise ArithmeticError('Overlapping smoothing windows')
            assigned.add(qi);x=queries[qi]-center
            values,errors=source_q_at(x,delta,jumps);coeff[qi]=values
            if x==0:node_points+=1
            else:inside_points+=1
            for d,j in native_errors:
                bound=sum((err*abs(m)**j for err,m in zip(errors[d],modes)),Q(0))
                size=sum((abs(Q(*v.as_integer_ratio()))*abs(m)**j for v,m in zip(values[d],modes)),Q(0))+bound
                if bound>native_errors[d,j]:native_errors[d,j]=bound;maxima[str((d,j))]=str(queries[qi])
                native_value[d,j]=max(native_value[d,j],size)
            digest.update((str(i)+'\t'+str(queries[qi])+'\t'+'\t'.join(str(sum(z,Q(0))) for z in errors)+'\n').encode())
    rmin=nodes[0]
    physical={'Q':native_errors[0,0],'Qs':native_errors[1,0],'Qu':native_errors[0,1],
      'Qss':native_errors[2,0]+6*native_errors[1,0],'Qsu':native_errors[1,1],'Quu':native_errors[0,2]}
    np.savez_compressed(output_cache,query_fraction=np.array(list(map(str,queries))),
      coefficients=coeff,planar_modes=pm,height_modes=hm,
      original_query_indices=np.asarray([index[Q(x)] for x in original_queries],dtype=np.int64),
      diagnostic_query_indices=np.asarray([index[Q(x)] for x in diagnostic_queries],dtype=np.int64))
    record={'schema':'m12-R250-certified-original-source-Q-query-cache-v1','script_sha256':sha(__file__),
      'smoothing_source_sha256':SMOOTHER_SHA,'smoothing_report_sha256':sha(args.smoothing_report),
      'manifest_sha256':MANIFEST_SHA,'original_source_report_sha256':sha(args.source_report),
      'original_source_cache_sha256':sha(args.source_cache),'cache_sha256':sha(output_cache),
      'cache_bytes':output_cache.stat().st_size,'source_blocks':blobs,'original_queries':len(original_queries),
      'original_diagnostic_queries':len(diagnostic_queries),'unique_queries':len(queries),
      'nonzero_window_query_count':inside_points,'exact_original_node_query_count':node_points,
      'contributing_source_windows':contributing,'divisor':divisor,'dyadic_bits':BITS,
      'all_query_radii_and_windows_exact_Fraction':True,'all_141_modes_and_three_radial_jets':True,
      'exact_outside_window_values_zero':True,'same_original_g':True,
      'interval_method':'Even/odd degree40/41 alternating Taylor at exact |T|/2^k<=1/16; outward 256-bit dyadic repeated squaring; rational logistic and two derivatives; actual longdouble store compared to interval.',
      'cache_error_native_r_u_six_jet_upper':{str(k):packet(v) for k,v in native_errors.items()},
      'cache_error_physical_s_u_six_jet_upper':{k:packet(v) for k,v in physical.items()},
      'cache_error_target_differential_upper':packet(physical['Qs']+physical['Qu']/rmin),
      'sampled_exact_Q_native_six_jet_upper':{str(k):packet(v) for k,v in native_value.items()},
      'actual_interval_query_stream_sha256':digest.hexdigest(),'max_error_query_radii':maxima,
      'scope':'Point evaluation and storage error of exact Q at every query in the actual original cache and diagnostics. Finite set only; global candidate bounds remain R250. Angular sin/cos and the original source evaluator retain their separate budgets.',
      'new_nonlinear_acceptance':False,'seconds':time.monotonic()-began}
    args.out.write_text(json.dumps(record,indent=2,allow_nan=False)+'\n')
    print(json.dumps({'report':str(args.out),'queries':len(queries),'nonzero_window_queries':inside_points,
       'source_windows':contributing,'error_physical_s_u_display':{k:float(v) for k,v in physical.items()},'seconds':record['seconds']},indent=2))

if __name__=='__main__':main()
