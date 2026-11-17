#!/usr/bin/env python3
"""Use the complete frozen Frenet BVP for an explicitly new inward metric.

Only the scalar evaluator is replaced. All residuals, analytic Jacobian,
separated boundary rows, feasibility policy and solver tolerances are those
of parallel_20261117_continue.py. New scalar metadata is mandatory for later
readers; the old Profile alone does not describe these output fields.
"""
import argparse
import gzip
import hashlib
import json
from pathlib import Path
import parallel_20261117_continue as solver
from parallel_20261117_inward_profile import InwardProfile


def main(args):
    raw=args.input.read_bytes();data=json.loads(gzip.decompress(raw))
    if data.get('radial_growth_scale',1)!=1:
        raise ValueError('This driver does not combine a radial-growth metric')
    prior=data.get('inward_scalar_profile')
    if prior:
        cut=prior['cut'];curvature=prior['curvature'];rin=prior['ramp_in'];rout=prior['ramp_out']
        if args.curvature is not None and args.curvature!=curvature:
            raise ValueError('Refinement/extension must retain the frozen new metric')
    else:
        cut=float(data['mesh'][-1]);curvature=args.curvature or 1.5
        rin=rout=args.ramp
    if args.boundary_input:
        boundary=json.loads(gzip.decompress(args.boundary_input.read_bytes()))
        bp=boundary.get('inward_scalar_profile')
        if bp and any(bp[k]!=v for k,v in [('cut',cut),('curvature',curvature),('ramp_in',rin),('ramp_out',rout)]):
            raise ValueError('Boundary input belongs to another inward metric')
        if not bp and boundary['mesh'][-1]>cut:
            raise ValueError('Old scalar boundary lies beyond the changed cut')
    origin=data['analytic_extension_origin'];geometry=data['fixed_scalar_profile']['geometry']
    profile=InwardProfile(geometry,origin,cut,curvature,rin,rout)
    if data['mesh'][-1]+args.duration>profile.end:
        raise ValueError('This driver stops at the inward flat cuff, before the disk chart')
    solver.Profile=lambda geom,start: InwardProfile(geom,start,cut,curvature,rin,rout)
    solver.main(args)
    result=json.loads(gzip.decompress(args.out.read_bytes()))
    result['inward_scalar_profile']=profile.spec()
    result['inward_driver_sha256']=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    result['inward_profile_sha256']=hashlib.sha256(Path(__file__).with_name('parallel_20261117_inward_profile.py').read_bytes()).hexdigest()
    result['metric_reader_requirement']='Use inward_scalar_profile with InwardProfile; original Profile is only its unchanged prefix'
    args.out.write_bytes(gzip.compress(json.dumps(result).encode(),mtime=0))
    print(json.dumps(dict(event='inward_metric_bound',inward_scalar_profile=result['inward_scalar_profile'],
        output_sha256=hashlib.sha256(args.out.read_bytes()).hexdigest(),success=result['success'])),flush=True)


if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--input',type=Path,required=True);p.add_argument('--out',type=Path,required=True)
    p.add_argument('--duration',type=float,default=.002);p.add_argument('--step',type=float,default=.00025)
    p.add_argument('--modes',type=int);p.add_argument('--angles',type=int)
    p.add_argument('--fixed-modes',type=int,default=3);p.add_argument('--core-first',nargs='+',type=float)
    p.add_argument('--boundary-input',type=Path);p.add_argument('--curvature',type=float)
    p.add_argument('--ramp',type=float,default=.02)
    p.add_argument('--tol',type=float,default=1e-8);p.add_argument('--max-nodes',type=int,default=1800)
    p.add_argument('--linear-solver',choices=['separated-qr','direct-csc'],default='separated-qr')
    main(p.parse_args())
