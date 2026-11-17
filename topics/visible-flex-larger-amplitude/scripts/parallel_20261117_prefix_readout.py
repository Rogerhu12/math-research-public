#!/usr/bin/env python3
"""Actual jets of a C2 quintic reconstruction of one accepted open prefix.

All extrema are sampled, with the normalized 2x2 Gram operator norm.  The
field is defined by the unique quintic matching common nodal 0/1/2 jets;
those binary nodal data interpreted as exact reals define C2 seams.  Finite
double evaluation is not a continuous interval enclosure or reach proof.
"""
import argparse
import gzip
import hashlib
import json
from pathlib import Path
import numpy as np
from parallel_20261117_frenet_symbol import Frenet
from parallel_20261117_profile import Profile


def main(args):
    raw=args.input.read_bytes();data=json.loads(gzip.decompress(raw))
    if not data.get('success'):raise ValueError('Need an actually accepted field')
    q=Frenet(data['M'],args.angles or data['N']);old=Frenet(data['M'],data['N'])
    geometry=data.get('fixed_scalar_profile',data.get('inherited_profile'))['geometry']
    origin=float(data.get('analytic_extension_origin',data.get('extension_scalar',{}).get('start',data['mesh'][-1])))
    profile=Profile(geometry,origin)
    x=np.array(data['mesh']);y=np.array(data['states']);dy=np.array(data['rhs']);ddy=[]
    for s,state,velocity in zip(x,y,dy):
        a,ap,app=profile(float(s));k=ap/a
        ddy.append(old.jvp(state,k,velocity,dk=app/a-k*k))
    ddy=np.array(ddy);core=y[0,1:q.M+1]
    rho=1+np.cos(q.angle[:,None]*q.freq[None,1:])@((1-q.freq[1:]**2)*core)
    major=1+np.sum(core);gap=2*np.sum(core[::2]);witness=np.array([0.,major,0.])
    worst_metric=dict(value=0.);max_curvature=0.;Dproxy=0.;witness_min=float('inf');minimum_det=float('inf')
    points=0
    for i,h in enumerate(np.diff(x)):
        c0=y[i];c1=h*dy[i];c2=h*h*ddy[i]/2
        aa=y[i+1]-c0-c1-c2;bb=h*dy[i+1]-c1-2*c2;cc=h*h*ddy[i+1]-2*c2
        coefficients=np.array([c0,c1,c2,10*aa-4*bb+cc/2,-15*aa+7*bb-cc,6*aa-3*bb+cc/2])
        for u in np.linspace(0,1,args.radial_subdivisions+1):
            s=x[i]+u*h
            state=np.polynomial.polynomial.polyval(u,coefficients)
            vs=np.polynomial.polynomial.polyval(u,np.arange(1,6)[:,None]*coefficients[1:])/h
            acc=np.polynomial.polynomial.polyval(u,(np.arange(2,6)*np.arange(1,5))[:,None]*coefficients[2:])/(h*h)
            F,d,e=q.jet(state);V,dV,_=q.jet(vs);Acc,_,_=q.jet(acc)
            E=np.sum(V*V,axis=1);mixed=np.sum(V*d,axis=1);G=np.sum(d*d,axis=1)
            a,_,_=profile(float(s));g=(a*rho)**2
            er=E-1;gr=G/g-1;fr=mixed/np.sqrt(g)
            error=(abs(er+gr)+np.sqrt((er-gr)**2+4*fr*fr))/2
            j=int(np.argmax(error))
            if error[j]>worst_metric['value']:worst_metric=dict(value=float(error[j]),s=float(s),angle=float(q.angle[j]),cell=i,u=float(u))
            normal=np.cross(V,d);normal/=np.linalg.norm(normal,axis=1)[:,None]
            e2=np.sum(Acc*normal,axis=1);f2=np.sum(dV*normal,axis=1);g2=np.sum(e*normal,axis=1)
            determinant=E*G-mixed*mixed;minimum_det=min(minimum_det,float(np.min(determinant)))
            tr=(e2*G+g2*E-2*f2*mixed)/determinant;kd=(e2*g2-f2*f2)/determinant
            max_curvature=max(max_curvature,float(np.max((abs(tr)+np.sqrt(np.maximum(0,tr*tr-4*kd)))/2)))
            cp,sp=np.cos(q.angle),np.sin(q.angle)
            xyz=np.c_[cp*F[:,0]-sp*F[:,1],sp*F[:,0]+cp*F[:,1],F[:,2]]
            Dproxy=max(Dproxy,float(2*np.max(np.linalg.norm(xyz,axis=1))))
            witness_min=min(witness_min,float(np.min(np.linalg.norm(xyz-witness,axis=1))))
            points+=q.N
    report=dict(scope=__doc__,input_sha256=hashlib.sha256(raw).hexdigest(),M=q.M,N=q.N,radial_subdivisions=args.radial_subdivisions,
                sampled_points=points,quintic_cells=len(x)-1,end=float(x[-1]),max_sample_relative_gram_operator=worst_metric,
                max_sample_principal_curvature=max_curvature,minimum_sample_gram_determinant=minimum_det,
                reflected_prefix_D_proxy=Dproxy,core_gap=float(gap),minimum_sample_witness_distance=witness_min,
                sampled_core_rho_min=float(rho.min()),source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
    args.out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2))


if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--input',type=Path,required=True);p.add_argument('--out',type=Path,required=True)
    p.add_argument('--angles',type=int);p.add_argument('--radial-subdivisions',type=int,default=2)
    main(p.parse_args())
