#!/usr/bin/env python3
"""Export immutable geometry-only locations from actual QP histories.

All values are discarded: descendants must reread these locations. The
fixed geometry list is not the active QP list and is not a global bound.
"""
import argparse
import hashlib
import json
from pathlib import Path
import numpy as np


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--report',action='append',type=Path,required=True)
    p.add_argument('--input-manifest',action='append',type=Path,default=[])
    p.add_argument('--carrier',type=Path,required=True)
    p.add_argument('--bundle',type=Path,required=True)
    p.add_argument('--out',type=Path,required=True)
    a=p.parse_args()
    if a.out.exists():
        raise FileExistsError('Use a fresh immutable output')
    carrier=np.load(a.carrier,allow_pickle=False)
    curves,radii,protected={},{},{}
    carrier_sha=sha(a.carrier)
    def put(target,point):
        key=(int(point[0]),min(1.,max(0.,round(float(point[1]),12))),
             min(float(np.pi/2),max(0.,round(float(point[2]),12))))
        target[key]=None
    def grid(target,stage,angle,N):
        put(target,(carrier['observation_cells'][stage],
                    carrier['observation_u'][stage],2*np.pi*angle/N))
    def memory(value,N):
        for which,target in [('curvature',curves),('radius',radii)]:
            for key in (which+'_points','fixed_'+which+'_points'):
                for point in value.get(key,[]):put(target,point)
            for stage,angle in value.get(which+'_locations',[]):grid(target,stage,angle,N)
        for point in value.get('protected_curvature_points',[]):
            put(protected,point);put(curves,point)
        for nested in ('grid','arbitrary'):
            if nested in value:memory(value[nested],N)
    def geometry(value,N):
        for key,target in [('curvature_witnesses',curves),('radius_witnesses',radii)]:
            for row in value.get(key,[]):put(target,row['point'])
        for key,target in [('best_arbitrary_curvature',curves),('best_arbitrary_diameter',radii)]:
            if key in value:put(target,value[key]['point'])
        for key,target in [('worst',curves),('farthest',radii)]:
            if key in value:
                row=value[key];grid(target,row['stage'],row['angle'],N)
        for row in value.get('local_searches',[]):
            put(curves if row['kind']=='curvature' else radii,row['final']['point'])
    sources=[]
    for path in a.input_manifest:
        d=json.loads(path.read_text())
        if d.get('carrier_sha256',carrier_sha)!=carrier_sha:
            raise ValueError('Witness carrier mismatch')
        memory(d,d.get('optimization_full_angles',2048))
        N=d.get('optimization_full_angles',2048)
        for key,target in [('grid_curvature_locations',curves),('grid_radius_locations',radii)]:
            for stage,angle in d.get(key,[]):grid(target,stage,angle,N)
        sources.append(dict(path=str(path),sha256=sha(path)))
    last=None
    for path in a.report:
        d=json.loads(path.read_text());last=d
        if d['dependency_sha256']['carrier']!=carrier_sha:
            raise ValueError('Report observation carrier mismatch')
        N=d['observation_metadata']['full_angles']
        memory(d.get('initial_memory',{}),N);memory(d.get('final_memory',{}),N)
        for key in ('initial_gauss_geometry','final_gauss_geometry',
                    'initial_arbitrary_geometry','final_arbitrary_geometry'):
            geometry(d.get(key,{}),N)
        for row in d['iterations']:
            memory(row.get('memory_before',{}),N);memory(row.get('memory_after',{}),N)
            geometry(row.get('gauss_geometry_before',{}),N)
            geometry(row.get('arbitrary_geometry_before',{}),N)
            for point in row.get('pinned_curvature_points',[]):put(curves,point)
            for point in row.get('pinned_radius_points',[]):put(radii,point)
            for item in row.get('active_constraints',[]):
                for key,target in [('curvature_point',curves),('diameter_point',radii)]:
                    item0=item[key]
                    if item0['kind']=='arbitrary':put(target,item0['point'])
                    elif item0['kind']=='grid':grid(target,item0['stage'],item0['angle'],N)
            for trial in row.get('trials',[]):
                geometry(trial.get('gauss_geometry',{}),N)
                geometry(trial.get('arbitrary_geometry',{}),N)
        sources.append(dict(path=str(path),sha256=sha(path)))
    bundle_sha=sha(a.bundle)
    if last['output_bundle_sha256']!=bundle_sha:
        raise ValueError('Final supplied history does not end at the supplied actual field')
    result=dict(schema='immutable-curvature-history-locations-v1',
        carrier_sha256=carrier_sha,bundle_sha256=bundle_sha,sources=sources,
        curvature_points=list(curves),radius_points=list(radii),
        protected_curvature_points=list(protected),
        scope='Only locations, no inherited values. Includes rejected trials and prior pins. Reread all; active linear constraints may remain bounded. No continuous coverage claim.')
    a.out.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(dict(out=str(a.out),sha256=sha(a.out),
        curvature_points=len(curves),radius_points=len(radii),protected_points=len(protected))))


if __name__=='__main__':
    main()

