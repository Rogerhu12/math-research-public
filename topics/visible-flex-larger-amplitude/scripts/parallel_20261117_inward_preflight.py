#!/usr/bin/env python3
"""Actual-cut chord checks for a new inward reference scalar; no tail field."""
import argparse
import gzip
import hashlib
import json
from pathlib import Path
import numpy as np
from parallel_20261117_inward_profile import InwardProfile
from parallel_20261117_frenet_symbol import Frenet


def main(args):
    raw=args.input.read_bytes();data=json.loads(gzip.decompress(raw))
    if not data.get('success'):raise ValueError('An actually accepted prefix is required')
    if data.get('radial_growth_scale',1)!=1 or data.get('inward_scalar_profile'):
        raise ValueError('This preflight expects the original scalar prefix family')
    origin=data['analytic_extension_origin'];geometry=data['fixed_scalar_profile']['geometry']
    cut=data['mesh'][-1];q=Frenet(data['M'],args.angles)
    local=q.jet(np.array(data['states'][-1]))[0];phi=np.arange(q.N)*2*np.pi/q.N
    F=local.copy()
    F[:,0]=local[:,0]*np.cos(phi)-local[:,1]*np.sin(phi)
    F[:,1]=local[:,0]*np.sin(phi)+local[:,1]*np.cos(phi)
    coeff=np.array(data['core']['coefficients']);freq=2*np.arange(1,len(coeff)+1)
    theta=phi+np.sin(phi[:,None]*freq)@((1-freq**2)*coeff/freq)
    rows=[]
    for k in args.curvatures:
        p=InwardProfile(geometry,origin,cut,curvature=k,ramp_in=args.ramp,ramp_out=args.ramp)
        check=InwardProfile(geometry,origin,cut,curvature=k,ramp_in=args.ramp,
                            ramp_out=args.ramp,quadrature=48)
        xy=p.radius*np.stack((np.cos(theta),np.sin(theta)),axis=1)
        dxy=np.linalg.norm(xy-F[:,:2],axis=1);length=p.end-cut
        slack=length**2-dxy**2
        intervals=None
        if np.min(slack)>=0:
            intervals=[float(np.max(F[:,2]-np.sqrt(slack))),
                       float(np.min(F[:,2]+np.sqrt(slack)))]
        distance=np.linalg.norm(np.column_stack((xy,np.full(q.N,args.height)))-F,axis=1)
        rows.append(dict(profile=p.spec(),quadrature_comparison=float(max(abs(p.shift3-check.shift3))),
            radial_arclength=length,maximum_horizontal_chord=float(max(dxy)),
            necessary_height_sample_interval=intervals,height=args.height,
            maximum_full_chord=float(max(distance)),minimum_chord_margin=float(length-max(distance)),
            paired_disk_diameter=float(2*np.hypot(p.radius,args.height)),
            individual_disk_diameter=float(2*p.radius),terminal=p.meridian(p.end)))
    source=Path(__file__)
    result=dict(kind='new_reference_design_and_fixed_material_sampled_necessary_chord_only',
        parent_sha256=hashlib.sha256(raw).hexdigest(),angles=q.N,rows=rows,
        source_sha256=hashlib.sha256(source.read_bytes()).hexdigest(),
        profile_source_sha256=hashlib.sha256(source.with_name('parallel_20261117_inward_profile.py').read_bytes()).hexdigest(),
        scope='No actual nonlinear extension, closed surface, complete diameter, reach, or all-time family')
    output=(json.dumps(result,indent=2)+'\n').encode();args.out.write_bytes(output)
    print(json.dumps(result,indent=2));print('report_sha256',hashlib.sha256(output).hexdigest())


if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--input',type=Path,required=True);p.add_argument('--out',type=Path,required=True)
    p.add_argument('--angles',type=int,default=2048);p.add_argument('--height',type=float,default=1.8)
    p.add_argument('--ramp',type=float,default=.02)
    p.add_argument('--curvatures',nargs='+',type=float,default=[1.25,1.5,1.75,2.])
    main(p.parse_args())
