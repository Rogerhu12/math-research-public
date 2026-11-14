#!/usr/bin/env python3
"""Diagnose full Cartesian cut jets between saved prefix and explicit tail.

Only scalar summaries are printed. This is a floating diagnostic, not an
exact seam or a continuous metric certificate. The tail's horizontal gauge
is kept; only its constant vertical background height is aligned.
"""
import argparse
from fractions import Fraction as Q
import gzip
import hashlib
import importlib.util
import io
import json
import math
from pathlib import Path
import numpy as np
from db6f_tail_integrated import IntegratedTail


def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--geometry',type=Path,required=True)
    p.add_argument('--tail',type=Path,required=True)
    p.add_argument('--out',type=Path,required=True)
    p.add_argument('--blend-width',type=float,default=.1)
    args=p.parse_args()
    meta=json.loads(args.geometry.read_text());data=args.geometry.parent/meta['data_file']
    if sha(data)!=meta['data_sha256']:raise ValueError('Prefix data hash mismatch')
    raw=np.load(io.BytesIO(gzip.decompress(data.read_bytes())),allow_pickle=False)
    t=IntegratedTail(args.tail)
    M=max(meta['modes'],max(abs((t.planar_modes-1)//3)),max(t.height_modes//3))
    old=np.zeros((3,3*M+2),dtype=np.longdouble)
    Ms=meta['modes'];jets=raw['jets'][:,-1,:].astype(np.longdouble)
    old[:,0]=jets[:,0]
    for axis in range(3):old[:,axis*M+1:(axis+1)*M+1][:,:Ms]=jets[:,axis*Ms+1:(axis+1)*Ms+1]
    old[:,-1]=jets[:,-1]
    mean=sum((Q.from_float(float(v))for v in raw['mean_increments']),Q(0))
    old[0,-1]=np.longdouble(mean.numerator)/np.longdouble(mean.denominator)
    tail=np.zeros_like(old)
    source=[t.value_nodes[-1],t.first[-1],t.second[-1]]
    for order,v in enumerate(source):
        bymode={int(k):np.longdouble(x)for k,x in zip(t.planar_modes,v[:t.P])}
        tail[order,0]=bymode.get(1,0.)
        for j in range(1,M+1):
            a,b=bymode.get(1+3*j,0.),bymode.get(1-3*j,0.)
            tail[order,j]=a+b;tail[order,M+j]=a-b
        for k,x in zip(t.height_modes,v[t.P:]):
            # Exporter's background has h'(r)=+w. The upper inward piece
            # reflects its entire height, including every perturbation jet.
            if k==0:tail[order,-1]=-x
            else:tail[order,2*M+k//3]=-x
    c=np.longdouble(t.meta['parameters']['rCut']);w=np.longdouble(t.meta['parameters']['wCut'])
    wr=-7*w/c;E=1+w*w;k=-1/np.sqrt(E);k2=-w*wr/(E*E)
    tail[0,0]+=c;tail[1,0]+=1
    # background H'(r)=-w, H''(r)=-w_r for the upper inward tail
    background_cut=old[0,-1]-tail[0,-1]
    tail[0,-1]+=background_cut;tail[1,-1]-=w;tail[2,-1]-=wr
    tail[2]=tail[2]*k*k+tail[1]*k2
    tail[1]*=k
    delta=tail-old
    rows=[]
    for order,d in enumerate(delta):
        axes=[np.sum(abs(d[:M+1])),np.sum(abs(d[M+1:2*M+1])),abs(d[-1])+np.sum(abs(d[2*M+1:3*M+1]))]
        rows.append({'order':order,'coefficient_max':float(max(abs(d))),
                     'component_fourier_l1':[float(x)for x in axes],
                     'cartesian_sup_l1_diagnostic':float(np.linalg.norm(axes))})
    width=np.longdouble(args.blend_width)
    if not 0<width<raw['mesh'][-1]:raise ValueError('Invalid blend width')
    # Quintic endpoint Hermite extension, zero through second order at start.
    d0,d1,d2=delta
    c3=10*d0-4*width*d1+width*width*d2/2
    c4=-15*d0+7*width*d1-width*width*d2
    c5=6*d0-3*width*d1+width*width*d2/2
    rough={}
    for order in range(3):
        powers=[c3,c4,c5]
        coeff=sum((np.abs(v)*np.longdouble(math.factorial(i+3)//math.factorial(i+3-order))/width**order for i,v in enumerate(powers)),np.zeros_like(d0))
        rough[str(order)]=float(np.sum(coeff))
    report={'scope':__doc__,'script_sha256':sha(__file__),'geometry':str(args.geometry),
            'geometry_sha256':sha(args.geometry),'tail':str(args.tail),'tail_sha256':sha(args.tail),
            'prefix_modes':Ms,'common_cylindrical_modes':int(M),'background_cut_height':float(background_cut),
            'tail_height_gauge':'Reflect the entire exported height by z -> constant-z, including all V height jets.',
            'cut_jet_differences':rows,'blend_width':args.blend_width,
            'rough_power_l1_correction_derivative_diagnostics':rough,
            'exact_seam_certified':False,'metric_certified':False,
            'tail_curvature_certified':False,'complete_closed_surface':False}
    args.out.write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps({k:report[k]for k in ('common_cylindrical_modes','background_cut_height','cut_jet_differences','rough_power_l1_correction_derivative_diagnostics')},indent=2))


if __name__=='__main__':main()
