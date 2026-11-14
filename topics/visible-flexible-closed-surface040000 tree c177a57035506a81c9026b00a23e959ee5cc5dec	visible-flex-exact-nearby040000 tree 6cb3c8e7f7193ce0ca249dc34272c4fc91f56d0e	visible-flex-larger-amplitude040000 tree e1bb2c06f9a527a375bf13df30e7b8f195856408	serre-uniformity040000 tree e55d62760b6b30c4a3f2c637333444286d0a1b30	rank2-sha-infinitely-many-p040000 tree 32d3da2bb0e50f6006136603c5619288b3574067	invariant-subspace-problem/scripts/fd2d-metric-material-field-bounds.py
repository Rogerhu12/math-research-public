#!/usr/bin/env python3
"""Continuous bounds for actual saved shared-two-jet material fields.

Every native radial polynomial is bounded by its Bernstein hull, and all
finite angular modes by a full Fourier coefficient sum. Prefix derivatives
are converted through the exact frozen material chart, and through the
exact bridge's native/physical meridian scale. Tail derivatives use the
same physical arclength direction and the existing target curvature <=6.
This certifies the field bounds only, never its repaired metric residual.
"""
from __future__ import annotations
import os
for _key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[_key]='1'
import argparse
from fractions import Fraction as Q
import gzip
import hashlib
import importlib.util
import io
import json
import math
from pathlib import Path
import sys
import time
import numpy as np

HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE))
sp=importlib.util.spec_from_file_location('fd2d_material_field_diff',HERE/'fd2d-metric-prefix-c2-difference.py')
diff=importlib.util.module_from_spec(sp);sys.modules[sp.name]=diff;sp.loader.exec_module(diff)
I,qb,poly=diff.I,diff.qb,diff.backend


def read_field(path):
    meta=json.loads(Path(path).read_text())
    if meta['schema']!='fd2d-shared-twojet-finite-fourier-material-field-v1':raise ValueError('Unknown field definition')
    mesh=[];jets=[];next_node=0;bindings=[]
    for part in meta['shards']:
        p=Path(part['file'])
        if not p.exists():p=Path(path).parent/p.name
        binding=diff.identity(p)
        if binding['sha256']!=part['sha256'] or part['first_node']!=next_node:
            raise ValueError('Changed or discontinuous field storage')
        with np.load(io.BytesIO(gzip.decompress(p.read_bytes())),allow_pickle=False) as raw:
            x,y=raw['mesh'].copy(),raw['jets'].copy()
        if len(x)!=part['node_count'] or y.shape!=(len(x),2,3,meta['modes']+1,2):
            raise ValueError('Invalid defining field array shape')
        mesh.append(x);jets.append(y);bindings.append(binding);next_node+=len(x)
    x,y=np.concatenate(mesh),np.concatenate(jets)
    if len(x)!=meta['nodes'] or not np.all(np.diff(x)>0) or not np.isfinite(y).all():
        raise ValueError('Invalid field mesh or data')
    if np.any(y[:,:,:,0,1]!=0):raise ValueError('Zero-frequency sine coefficient is not zero')
    return meta,x,y,bindings


def powers(jets,mesh,start,stop):
    values=I(jets[start:stop+1])
    y=values[:,:,0].lo.shape
    hq=[Q(float(mesh[i+1]))-Q(float(mesh[i])) for i in range(start,stop)]
    H=diff.rational_column(hq);H=I(H.lo[:,None,:,None],H.hi[:,None,:,None])
    a,b=values[:-1,:,0],values[1:,:,0]
    d0,d1=values[:-1,:,1],values[1:,:,1]
    q0,q1=values[:-1,:,2],values[1:,:,2]
    c1=H*d0;c2=H.square()*q0/2
    e0=b-a-c1-c2;e1=H*(d1-d0)-H.square()*q0;e2=H.square()*(q1-q0)
    c=diff.base.stack([a,c1,c2,10*e0-4*e1+e2/2,-15*e0+7*e1-e2,6*e0-3*e1+e2/2],1)
    return c,H,hq


def native_bounds(mesh,jets,modes,batch=32):
    names={(0,0):'v',(1,0):'x',(0,1):'u',(2,0):'xx',(1,1):'xu',(0,2):'uu'}
    maxima=[{name:0. for name in names.values()} for _ in range(2)]
    for start in range(0,len(mesh)-1,batch):
        stop=min(len(mesh)-1,start+batch);c,H,hq=powers(jets,mesh,start,stop)
        for d in range(3):
            factors=np.array([math.factorial(k)//math.factorial(k-d) for k in range(d,6)],dtype=float)
            powerscale=diff.rational_column([Q(1)/(h**d) for h in hq])
            scale=I(powerscale.lo[:,None,None,:,None],powerscale.hi[:,None,None,:,None])
            raw=c[:,d:]*factors[None,:,None,None,None]*scale
            count,degree=raw.lo.shape[:2]
            flat=I(raw.lo.transpose(1,0,2,3,4).reshape(degree,-1),raw.hi.transpose(1,0,2,3,4).reshape(degree,-1))
            bern=poly.interval_matmul(poly.bernstein_matrix(degree-1),flat)
            lo=bern.lo.reshape(degree,count,2,modes+1,2)
            hi=bern.hi.reshape(degree,count,2,modes+1,2)
            magnitude=np.maximum(abs(lo),abs(hi)).max(axis=0)
            for angle in range(3-d):
                name=names[(d,angle)];weights=(3*np.arange(modes+1,dtype=float))**angle
                for field in range(2):
                    for row in magnitude[:,field]:
                        value=poly.positive_sum_upper((I(row)*weights[:,None]).hi)
                        maxima[field][name]=max(maxima[field][name],value)
    return maxima


def fraction_bernstein(c):
    n=len(c)-1
    values=[sum((c[j]*Q(math.comb(k,j),math.comb(n,j)) for j in range(k+1)),Q(0)) for k in range(n+1)]
    return min(values),max(values)


def warp_bounds(geometry,target):
    meta=json.loads(Path(geometry).read_text());tar=json.loads(Path(target).read_text())
    src=diff.module('fd2d_material_field_target',HERE/'78718-prefix-metric-supplier-storage-v1.py')
    knots,coeff=src.exact_clamped_spline(meta['chart']);end=Q(tar['frozen_total_end'])
    warp=8*Q(float(meta['warp_reference_q']));cuts=sorted(set(knots+[Q(3,4)]))
    maxima=[Q(0),Q(0),Q(0)];panels=0
    for left,right in zip(cuts[:-1],cuts[1:]):
        index=max(i for i,x in enumerate(knots[:-1]) if x<=left)
        base=src.compose(coeff[index],[-knots[index],Q(1)])
        if left>=Q(3,4):
            cutoff=src.compose([Q(1),Q(0),Q(0),Q(-10),Q(15),Q(-6)],[Q(-3),Q(4)])
            base=src.mul(base,cutoff)
        e=src.scale(base,warp)
        derivatives=[e,src.scale(src.der(e),1/end),src.scale(src.der(src.der(e)),1/(end*end))]
        for j in range(8):
            a=left+(right-left)*Q(j,8);b=left+(right-left)*Q(j+1,8)
            for order,c in enumerate(derivatives):
                limits=fraction_bernstein(src.compose(c,[a,b-a]));maxima[order]=max(maxima[order],*(abs(v) for v in limits))
            panels+=1
    if not maxima[0]<1:raise ValueError('No global positive material chart')
    return dict(e=maxima[0],ep=maxima[1],epp=maxima[2],rho=1-maxima[0],panels=panels,
                supplier=diff.identity(HERE/'78718-prefix-metric-supplier-storage-v1.py'))


def physical_prefix(native,warp,bridge):
    R=qb(warp['rho']);E0,E1,E2=(qb(warp[k]) for k in ('e','ep','epp'))
    b=E1/(3*R);bp=E1/R.square();bs=E2/(3*R)+E1.square()/(3*R.square())
    br=json.loads(Path(bridge).read_text())['arclength_rescale'];lo,hi=Q(br['lo']),Q(br['hi'])
    if lo<=0:raise ValueError('Nonpositive bridge scale')
    L=qb(max(hi,1/lo));out=[]
    for x in native:
        z={k:I(v) for k,v in x.items()}
        vals=dict(v=z['v'],s=z['x']+b*z['u'],u=z['u']/R,
            ss=z['xx']+2*b*z['xu']+b.square()*z['uu']+(bs+b*bp)*z['u'],
            su=(z['xu']+b*z['uu']+bp*z['u'])/R,
            uu=z['uu']/R.square()+3*E0*z['u']/(R.square()*R))
        # L^2 simultaneously covers native/physical coordinate and component
        # conversions of both p and q through order two (L>=1).
        out.append({k:float((v*L.square()).hi) for k,v in vals.items()})
    return out,dict(scale_factor_upper=float(L.hi),bridge=diff.identity(bridge))


def physical_tail(native):
    # k=dr/dsigma=-1/sqrt(1+w^2), |k|<=1.
    # |k*k_r|=|w*w_r|/(1+w^2)^2<=6 from the SAME target meridian curvature.
    return [dict(v=x['v'],s=x['x'],u=x['u'],
                 ss=float((I(x['xx'])+6*I(x['x'])).hi),su=x['xu'],uu=x['uu']) for x in native]


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--field',action='append',type=Path,required=True);p.add_argument('--geometry',type=Path,required=True)
    p.add_argument('--target',type=Path,required=True);p.add_argument('--bridge',type=Path,required=True)
    p.add_argument('--out',type=Path,required=True);args=p.parse_args();started=time.monotonic()
    if args.out.exists():raise FileExistsError('Use a new output')
    warp=warp_bounds(args.geometry,args.target);regions=[];combined={}
    for path in args.field:
        meta,mesh,jets,bindings=read_field(path);native=native_bounds(mesh,jets,meta['modes'])
        if meta['region']=='prefix':
            if np.any(jets[0,0,0]) or np.any(jets[0,0,2]) or np.any(jets[0,1,1]):raise ValueError('Mirror C2 identities fail')
            if np.any(jets[-1]):raise ValueError('No zero two-jet at prefix cut')
            bounds,conversion=physical_prefix(native,warp,args.bridge)
        elif meta['region']=='tail':
            if np.any(jets[0]) or np.any(jets[-1]):raise ValueError('Tail endpoint two-jet is not zero')
            bounds=physical_tail(native);conversion={'target_curvature_upper_used':6.}
        else:raise ValueError('Unknown material field region')
        for field,letter in enumerate(('p','q')):
            for order,value in bounds[field].items():
                key=letter if order=='v' else letter+'_'+order;combined[key]=max(combined.get(key,0.),value)
        active=np.flatnonzero(np.any(jets!=0,axis=(1,2,3,4)))
        support=None if not len(active) else [float(mesh[max(0,active[0]-1)]),float(mesh[min(len(mesh)-1,active[-1]+1)])]
        regions.append(dict(field=diff.identity(path),bindings=bindings,region=meta['region'],
            complete_native_domain=True,native_bounds=native,physical_bounds=bounds,conversion=conversion,
            field_support_native_enclosure=support,exact_zero_endpoint_jets_verified=True))
    d1=sum((I(combined[k]).square() for k in ('p_s','p_u','q_s','q_u')),I(0.))
    d2=sum((I(combined[k]).square()*(2 if k.endswith('_su') else 1)
            for k in ('p_ss','p_su','p_uu','q_ss','q_su','q_uu')),I(0.))
    J=float(I(np.maximum(0,d1.lo),d1.hi).sqrt().hi);H=float(I(np.maximum(0,d2.lo),d2.hi).sqrt().hi)
    report=dict(schema='fd2d-continuous-actual-material-field-bounds-v1',scope=__doc__,script=diff.identity(__file__),
        geometry=diff.identity(args.geometry),target=diff.identity(args.target),bridge=diff.identity(args.bridge),
        warp={k:(str(v) if isinstance(v,Q) else v) for k,v in warp.items()},regions=regions,bounds=combined,
        Dv_operator_upper=J,D2v_bilinear_upper=H,
        all_finite_angular_modes_covered=True,all_native_radial_intervals_covered=True,
        material_derivative_coordinates='physical meridian arclength sigma and physical angle u',
        global_field_components_present=sorted(r['region'] for r in regions)==['prefix','tail'],
        sufficient_field_boxes=dict(p=combined['p']<=1e-10,q=combined['q']<=1e-10,Dv=J<=1e-6,D2v=H<=.01),
        continuous_linear_residual_not_computed=True,nonlinear_metric_not_certified=True,seconds=time.monotonic()-started)
    args.out.write_text(json.dumps(report,indent=2,allow_nan=False)+'\n')
    print(json.dumps(dict(out=str(args.out),bounds=combined,Dv=J,D2v=H,
                         boxes=report['sufficient_field_boxes'],seconds=report['seconds'])),flush=True)


if __name__=='__main__':main()
