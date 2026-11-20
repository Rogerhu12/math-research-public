#!/usr/bin/env python3
"""Refresh known arbitrary curvature/radius basins in one actual closed field.

Reuses the already published literal six-jet local reader. Every returned
point is only a lower witness. The optimizer is not a maximum certificate.
"""
import argparse
import hashlib
import importlib.util
import json
from pathlib import Path
import sys

import numpy as np
from scipy.optimize import minimize


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def load(name,path):
    spec=importlib.util.spec_from_file_location(name,path)
    module=importlib.util.module_from_spec(spec);sys.modules[name]=module
    spec.loader.exec_module(module)
    return module


def point(text):
    cell,u,phi=text.split(',')
    result=(int(cell),float(u),float(phi))
    if not 0<=result[1]<=1 or not 0<=result[2]<=np.pi/2:
        raise ValueError('A local seed must be in its declared original cell and angular quarter')
    return result


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--repo',type=Path,required=True)
    parser.add_argument('--bundle',type=Path,required=True)
    parser.add_argument('--carrier',type=Path,required=True)
    parser.add_argument('--local-reader',type=Path,required=True)
    parser.add_argument('--curvature-point',type=point,action='append',required=True)
    parser.add_argument('--radius-point',type=point,action='append',required=True)
    parser.add_argument('--fixed-manifest',type=Path,action='append',default=[])
    parser.add_argument('--grid-curvature',type=float,required=True)
    parser.add_argument('--grid-diameter',type=float,required=True)
    parser.add_argument('--reach-ratio',type=float,default=.03)
    parser.add_argument('--safety',type=float,default=.98)
    parser.add_argument('--out',type=Path,required=True)
    a=parser.parse_args()
    if a.out.exists():
        raise FileExistsError('Do not overwrite an existing actual readout')
    topic=a.repo/'topics/visible-flex-larger-amplitude'
    dense_path=topic/'notes/2026-11-17-parallel-geometry-fullclosed-gram-operator.py'
    observed_path=topic/'scripts/resume_20261120/gauss_observed_closed_gram.py'
    local=load('known_basin_literal_local_reader',a.local_reader)
    dense=load('known_basin_dense_source',dense_path)
    observed=load('known_basin_observation_source',observed_path)
    with np.load(a.bundle,allow_pickle=False) as data:
        field=local.LocalField(dense,observed,data)
    searches=[];curvature=float(a.grid_curvature)
    diameter=max(2.,2*abs(float(field.height)),float(a.grid_diameter))
    fixed=[];fixed_sources=[];seen=set()
    with np.load(a.carrier,allow_pickle=False)as carrier:
        cells=carrier['observation_cells'];us=carrier['observation_u']
    for path in a.fixed_manifest:
        if path.stat().st_size>100000:
            raise ValueError('Pass a compact fixed-location manifest')
        manifest=json.loads(path.read_text())
        declared=manifest.get('carrier_sha256',manifest.get('observation_carrier_sha256'))
        if declared is not None and declared!=sha(a.carrier):
            raise ValueError('The fixed manifest refers to a different scalar carrier')
        locations=[]
        for kind,key in [('curvature','curvature_points'),('diameter','radius_points')]:
            locations.extend((kind,*value)for value in manifest.get(key,[]))
        grid=manifest.get('grid_memory',{})
        full_angles=grid.get('full_angles',2048)
        for kind,key in [('curvature','curvature_locations'),('diameter','radius_locations')]:
            for stage,angle in grid.get(key,[]):
                locations.append((kind,int(cells[stage]),float(us[stage]),float(2*np.pi*angle/full_angles)))
        count=0
        for kind,cell,u,phi in locations:
            key=(int(cell),round(float(u),13),round(float(phi),13))
            if key in seen:continue
            seen.add(key);count+=1
            value=field.read(int(cell),float(u),float(phi))
            fixed.append(dict(kind=kind,**value))
            curvature=max(curvature,value['maximum_absolute_principal_curvature'])
            diameter=max(diameter,2*value['radius'])
        fixed_sources.append(dict(path=str(path),sha256=sha(path),new_locations=count))
    for kind,seeds in [('curvature',a.curvature_point),('diameter',a.radius_point)]:
        for cell,u,phi in seeds:
            if not 0<=cell<field.o.J-1:
                raise ValueError('The local seed is outside the original mesh')
            initial=field.read(cell,u,phi)
            key='maximum_absolute_principal_curvature' if kind=='curvature' else 'radius'
            result=minimize(lambda v:-field.read(cell,*v)[key], [u,phi],
                method='Nelder-Mead',bounds=((0.,1.),(0.,np.pi/2)),
                options=dict(xatol=2e-10,fatol=2e-10,maxiter=300))
            final=field.read(cell,*result.x)
            for value in (initial,final):
                curvature=max(curvature,value['maximum_absolute_principal_curvature'])
                diameter=max(diameter,2*value['radius'])
            searches.append(dict(kind=kind,initial=initial,final=final,
                optimizer=dict(method='Nelder-Mead',success=bool(result.success),
                    message=str(result.message),iterations=int(result.nit),
                    evaluations=int(result.nfev),xatol=2e-10,fatol=2e-10,maxiter=300)))
    product=a.reach_ratio*diameter*curvature
    record=dict(schema='closed-known-basins-and-fixed-points-refresh-v2',source_sha256=sha(__file__),
        bundle_sha256=sha(a.bundle),carrier_sha256=sha(a.carrier),
        source_paths=dict(local_reader=str(a.local_reader),dense=str(dense_path),observed=str(observed_path)),
        source_sha256_by_role=dict(local_reader=sha(a.local_reader),dense=sha(dense_path),observed=sha(observed_path)),
        grid_curvature=a.grid_curvature,grid_diameter=a.grid_diameter,height=float(field.height),
        searches=searches,fixed_sources=fixed_sources,fixed_witnesses=fixed,combined_curvature_point_lower=curvature,
        combined_diameter_point_lower=diameter,necessary_reach_product=product,
        numerical_safety=a.safety,numerical_screen_passed=bool(product<=a.safety),
        continuous_geometry_certified=False,local_optimizer_is_global_bound=False,
        reach_certified=False,scope='Known basins refreshed on this actual field; no continuous upper enclosure or proof of reach')
    a.out.write_text(json.dumps(record,indent=2)+'\n')
    print(json.dumps(record),flush=True)


if __name__=='__main__':
    main()
