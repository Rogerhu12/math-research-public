#!/usr/bin/env python3
"""Continuous coordinate two-jet bound for the original exact common-cut M12.

This consumes the original prefix payload and the same exact tail endpoint
cache used by the whole-half solver. It includes the M64 quintic common-cut
correction, the complete cubic material chart and its x>.75 cutoff, and the
certified exact bridge scale. It is a bound on the old R21 map; the central
normalization and learned Cartesian field are separate R226 changes.
"""
from __future__ import annotations
import argparse
from fractions import Fraction as Q
import gzip,hashlib,importlib.util,io,json,math,time
from pathlib import Path
import numpy as np

DATA_SHA='359d491cd592962d467fdd538013977ee9a92070346de41c227d9ca3e1ef3bd0'
META_SHA='253179d585d4ac0e59206d4e579de5663943f126473668c45a3bbda665c9c8f2'
BRIDGE_SHA='1389cf1a339b0a0d749beb666b6def24a31e766eff0abf63289217728ceacdaa'
MANIFEST_SHA='cc23977e25a09c34db91723dd784cab4b18b89e325fc2ca2fb8dd7ee6866a104'
DEN=10**24


def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def fq(v):return Q.from_float(float(v))
def load(name,p):
    spec=importlib.util.spec_from_file_location(name,p)
    m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);return m
def outward(q):return Q(-((-Q(q).numerator*DEN)//Q(q).denominator),DEN)
def packet(q):
    value=outward(q);return {'upper_exact':str(value),'display':float(value)}


class I:
    def __init__(self,a,b=None):
        self.a=Q(a);self.b=Q(a if b is None else b)
        if self.a>self.b:raise ValueError('Reversed interval')
    def __add__(self,o):
        o=as_i(o);return I(self.a+o.a,self.b+o.b)
    __radd__=__add__
    def __neg__(self):return I(-self.b,-self.a)
    def __sub__(self,o):return self+-as_i(o)
    def __rsub__(self,o):return as_i(o)+-self
    def __mul__(self,o):
        o=as_i(o);v=[self.a*o.a,self.a*o.b,self.b*o.a,self.b*o.b];return I(min(v),max(v))
    __rmul__=__mul__
    def __truediv__(self,o):
        o=as_i(o)
        if o.a<=0<=o.b:raise ZeroDivisionError('Interval crosses zero')
        return self*I(1/o.b,1/o.a)
    def __rtruediv__(self,o):return as_i(o)/self
    def abs_upper(self):return max(abs(self.a),abs(self.b))

def as_i(x):return x if isinstance(x,I) else I(x)
def box(x):return I(Q(x['lo']),Q(x['hi']))
def sqrt_box(q,bits=128):
    q=Q(q)
    if q<0:raise ValueError('Negative radicand')
    n=math.isqrt((q.numerator<<(2*bits))//q.denominator)
    a=Q(n,1<<bits)
    return I(a,a if a*a==q else Q(n+1,1<<bits))

def compose(poly,a,h):
    return [sum((poly[k]*math.comb(k,j)*a**(k-j)*h**j for k in range(j,len(poly))),Q(0))
            for j in range(len(poly))]
def product(a,b):
    out=[Q(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):out[i+j]+=x*y
    return out
def bernstein(poly):
    n=len(poly)-1
    return [sum((poly[k]*Q(math.comb(i,k),math.comb(n,k)) for k in range(i+1)),Q(0))
            for i in range(n+1)]
def deriv(poly,d=1):
    return [poly[k]*Q(math.factorial(k),math.factorial(k-d)) for k in range(d,len(poly))]
def poly_bound(poly,h,d):
    return max(map(abs,bernstein(deriv(poly,d))))/(h**d)
def angle_bound(row,M,order):
    return row[0]+sum(((3*j+1)**order*(row[j]+row[M+j])+
                       (3*j)**order*row[2*M+j] for j in range(1,M+1)),Q(0))

def full_chart(meta,end,screen):
    knots,polys=screen.exact_clamped_spline(meta['chart'])
    warp=8*fq(meta['warp_reference_q']);bounds=[Q(0)]*3;pieces=0
    digest=hashlib.sha256()
    for left0,right0,p in zip(knots[:-1],knots[1:],polys):
        cuts=sorted(set([left0,right0]+([Q(3,4)] if left0<Q(3,4)<right0 else [])))
        for left,right in zip(cuts[:-1],cuts[1:]):
            h=right-left
            base=compose(p,left-left0,h)
            if left>=Q(3,4):
                cutoff=compose([Q(1),Q(0),Q(0),Q(-10),Q(15),Q(-6)],4*left-3,4*h)
                base=product(base,cutoff)
            base=[warp*v for v in base]
            values=[poly_bound(base,end*h,d) for d in range(3)]
            for d in range(3):bounds[d]=max(bounds[d],values[d])
            digest.update(('\t'.join(map(str,[left,right]+values))+'\n').encode());pieces+=1
    if bounds[0]>=1:raise ArithmeticError('Original full material chart bound does not prove positivity')
    return bounds,pieces,digest.hexdigest()

def bridge_radius_floor(bridge):
    L,pt,ps=(box(bridge[k]) for k in ('exact_L','exact_pt','exact_ps'))
    if min(L.a,pt.a)<=0 or ps.b>=0:raise ValueError('Unexpected original bridge phase signs')
    power=[I(0),I(0),3*pt-L*ps,-2*pt+L*ps]
    phase_upper=Q(0)
    for j in range(64):
        controls=bernstein(compose(power,Q(j,64),Q(1,64)))
        phase_upper=max(phase_upper,max(v.b for v in controls))
    if phase_upper>=Q(3,2):raise ArithmeticError('Bridge monotone-radius proof unresolved')
    # phi=t^2[pt(3-2t)-L ps(1-t)]>=0. phi<3/2<pi/2, so
    # f'=-sin(phi)<=0; the existing exact bridge root fixes f(1)=c.
    return Q(bridge['physical_cut_radius_exact']),phase_upper

def correction_bounds(raw,meta,bridge,tail_cache):
    oldM=(raw['jets'].shape[-1]-2)//3;M=int(meta['modes']);C=3*M+2
    with np.load(tail_cache,allow_pickle=False) as z:
        V=[Q(int(a),int(b)) for a,b in zip(z['endpoint_numerator'],z['endpoint_denominator'])]
        rows=[V,[fq(v) for v in z['first']],[fq(v) for v in z['second']]]
        pm=list(map(int,z['planar_modes']));hm=list(map(int,z['height_modes']))
    P=len(pm);lookup={v:i for i,v in enumerate(pm)}
    if M<max(oldM,max(abs((v-1)//3) for v in pm),max(v//3 for v in hm)):
        raise ValueError('Incomplete endpoint Fourier modes')
    T=[[Q(0)]*C for unused in range(3)]
    for d,row in enumerate(rows):
        def get(m):return row[lookup[m]] if m in lookup else Q(0)
        T[d][0]=get(1)
        for j in range(1,M+1):
            a,b=get(1+3*j),get(1-3*j);T[d][j]=a+b;T[d][M+j]=a-b
        for j,n in enumerate(hm):T[d][-1 if n==0 else 2*M+n//3]=-row[P+j]
    Y=[[Q(0)]*C for unused in range(3)]
    for d in range(3):
        Y[d][0]=fq(raw['jets'][d,-1,0]);Y[d][-1]=fq(raw['jets'][d,-1,-1])
        for axis in range(3):
            for j in range(1,oldM+1):Y[d][axis*M+j]=fq(raw['jets'][d,-1,axis*oldM+j])
    Y[0][-1]=sum(map(fq,raw['mean_increments']),Q(0))
    c=Q(bridge['physical_cut_radius_exact']);w=Q(1,2);wr=-7*w/c;E=Q(5,4)
    lam=box(bridge['arclength_rescale']);k=-1/sqrt_box(E);k2=-w*wr/(E*E)
    T[0][0]+=c;T[1][0]+=1;T[0][-1]=Y[0][-1];T[1][-1]-=w;T[2][-1]-=wr
    delta=[]
    for j in range(C):
        delta.append([(I(T[0][j])-Y[0][j]).abs_upper(),
                      (k/lam*T[1][j]-Y[1][j]).abs_upper(),
                      ((Q(4,5)*T[2][j]+k2*T[1][j])/(lam*lam)-Y[2][j]).abs_upper()])
    if delta[-1][0]!=0:raise ArithmeticError('Cut height gauge changed')
    start=int(meta['correction_start_index'])
    width=fq(raw['mesh'][-1])-fq(raw['mesh'][start])
    H=[[Q(1),2*width/5,width*width/20],
       [5/width,Q(2),width/4],[20/(width*width),12/width,Q(2)]]
    bounds=[[sum((H[d][k]*row[k] for k in range(3)),Q(0)) for row in delta] for d in range(3)]
    return {'Xpsi':angle_bound(bounds[0],M,1),'Xss':sum(bounds[2],Q(0)),
            'Xspsi':angle_bound(bounds[1],M,1),'Xpsipsi':angle_bound(bounds[0],M,2)},width,M,delta

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--scripts',type=Path,required=True);ap.add_argument('--data',type=Path,required=True)
    ap.add_argument('--tail-report',type=Path,required=True);ap.add_argument('--tail-cache',type=Path,required=True)
    ap.add_argument('--out',type=Path,required=True);args=ap.parse_args()
    if args.out.exists():raise FileExistsError('Fresh continuous-source report required')
    began=time.monotonic();notes=args.scripts.parent/'notes'
    meta_path=notes/'2026-11-09-db6f-root-flat17-common-cut-m12-critical-r01.json'
    bridge_path=notes/'2026-11-09-db6f-root-exact-bridge-m12.json'
    for p,h in ((args.data,DATA_SHA),(meta_path,META_SHA),(bridge_path,BRIDGE_SHA)):
        if sha(p)!=h:raise ValueError('Original source identity changed: '+str(p))
    meta=json.loads(meta_path.read_text());bridge=json.loads(bridge_path.read_text())
    tail=json.loads(args.tail_report.read_text())
    if tail['endpoint_cache_sha256']!=sha(args.tail_cache) or tail['manifest_sha256']!=MANIFEST_SHA:
        raise ValueError('Wrong exact original tail endpoint')
    tail_budget=tail['continuous_original_source_second_jets']
    if tail_budget['finite_spans']!=18552 or tail_budget['deep_collar_spans']!=1 or not tail_budget['continuous_all_angles_and_span_interiors']:
        raise ValueError('Full original tail source budget is missing')
    screen=load('full_original_chart_source',args.scripts/'6a65-m12-weak-stress-recovered-v2.py')
    old=load('full_original_prefix_polynomials',args.scripts/'6a65-m12-up-patch-exact-geometry-budget.py')
    with np.load(io.BytesIO(gzip.decompress(args.data.read_bytes())),allow_pickle=False) as f:
        raw={k:f[k].copy() for k in ('mesh','jets','mean_increments')}
    if raw['jets'].shape!=(3,2570,74):raise ValueError('Wrong original prefix dimensions')
    M=24;B={k:Q(0) for k in ('Xpsi','Xss','Xspsi','Xpsipsi')};digest=hashlib.sha256()
    for i in range(len(raw['mesh'])-1):
        h,power=old.span_power(raw,i)
        b0,b1,b2=[[poly_bound(row,h,d) for row in power] for d in range(3)]
        row={'Xpsi':angle_bound(b0,M,1),'Xss':sum(b2,Q(0)),
             'Xspsi':angle_bound(b1,M,1),'Xpsipsi':angle_bound(b0,M,2)}
        for k,v in row.items():B[k]=max(B[k],v)
        digest.update(('\t'.join(map(str,[i]+list(row.values())))+'\n').encode())
    original=dict(B)
    corr,width,fullM,delta=correction_bounds(raw,meta,bridge,args.tail_cache)
    for k in B:B[k]+=corr[k]
    end=fq(raw['mesh'][-1]);(e0,e1,e2),pieces,chart_hash=full_chart(meta,end,screen)
    rho=1-e0;A=e1/(3*rho)
    Css=(e2/3+2*e1*A+3*e0*A*A)/rho
    Csu=(e1+3*e0*A)/(rho*rho);Cuu=3*e0/(rho**3)
    Hss=B['Xss']+2*A*B['Xspsi']+A*A*B['Xpsipsi']+Css*B['Xpsi']
    Hsu=(B['Xspsi']+A*B['Xpsipsi'])/rho+Csu*B['Xpsi']
    Huu=B['Xpsipsi']/(rho*rho)+Cuu*B['Xpsi']
    floor,phase_upper=bridge_radius_floor(bridge);lam=Q(bridge['arclength_rescale']['hi'])
    prefix_CX=lam*lam*Hss+2*lam*Hsu/floor+Huu/(floor*floor)
    tail_CX=Q(tail_budget['original_physical_target_scaled_second_jets_C_X']['upper_exact'])
    full_CX=max(prefix_CX,tail_CX)
    report={'schema':'6a65-original-M12-entire-half-continuous-source-CX-v1',
            'script_sha256':sha(__file__),'data_sha256':DATA_SHA,'common_meta_sha256':META_SHA,
            'bridge_sha256':BRIDGE_SHA,'tail_manifest_sha256':MANIFEST_SHA,
            'tail_report_sha256':sha(args.tail_report),'tail_cache_sha256':sha(args.tail_cache),
            'original_prefix_polynomial_helper_sha256':sha(Path(old.__file__)),
            'original_chart_helper_sha256':sha(Path(screen.__file__)),
            'original_prefix_cells':len(raw['mesh'])-1,'original_prefix_modes':M,'common_cut_modes':fullM,
            'common_cut_correction_start_index':int(meta['correction_start_index']),
            'common_cut_correction_width_exact':str(width),
            'old_prefix_native_jets':{k:packet(v) for k,v in original.items()},
            'common_cut_correction_native_jets':{k:packet(v) for k,v in corr.items()},
            'combined_prefix_native_jets':{k:packet(v) for k,v in B.items()},
            'complete_chart_bounds':{k:packet(v) for k,v in zip(('e','es','ess'),(e0,e1,e2))},
            'complete_chart_pieces':pieces,'chart_piece_stream_sha256':chart_hash,
            'prefix_source_cell_stream_sha256':digest.hexdigest(),
            'bridge_phase_upper':packet(phase_upper),'prefix_target_radius_lower_exact':str(floor),
            'bridge_scale_upper_exact':str(lam),'prefix_original_C_X':packet(prefix_CX),
            'tail_original_C_X':packet(tail_CX),'entire_half_original_C_X':packet(full_CX),
            'continuous_all_spans_and_all_angles':True,
            'exact_common_cut_change_included':True,'central_normalization_not_included':True,
            'learned_solver_field_not_included':True,
            'inherited_hypotheses':'Original R21 map and exact root bridge definition; original background |kappa_r|<=6; exact normalized source increments.',
            'new_isometry_proved':False,'new_field_geometry_proved':False,'seconds':time.monotonic()-began}
    args.out.write_text(json.dumps(report,indent=2,allow_nan=False)+'\n')
    print(json.dumps(report,indent=2,allow_nan=False))

if __name__=='__main__':main()

