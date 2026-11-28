#!/usr/bin/env python3
"""Measure the actual positive-y material meridian, its radial variation, and off-axis leakage."""
import argparse
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import sys

for k in ("OPENBLAS_NUM_THREADS","MKL_NUM_THREADS","OMP_NUM_THREADS"):os.environ[k]="1"
import numpy as np


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def load(path,name):
    sp=importlib.util.spec_from_file_location(name,path)
    mod=importlib.util.module_from_spec(sp);sys.modules[name]=mod;sp.loader.exec_module(mod)
    return mod


def run(args):
    here=Path(__file__).resolve().parent
    prepare=load(here/"2ecf-polar-raw-ramp-source-compose.py","radial_provenance")
    prep,definition,basis,caches,mods,*_=prepare.validate_prepared(args)
    coarse=load(here/"2ecf-polar-fixed-prefix-position-basis.py","base_sfx").restrict(basis)[0]
    fine=load(here/"2ecf-polar-local-suffix-boehm.py","fine_sfx").build(coarse)[0]
    srcs=[("source",None,None,None)]
    for p in args.states:
        state=json.loads(p.read_text())
        if state["preparedSHA256"]!=sha(args.prepared) or state["modelDefinition"]["basis"] not in (coarse.definition,fine.definition):
            raise ValueError("Incompatible actual H65 field")
        b=coarse if state["modelDefinition"]["basis"]==coarse.definition else fine
        srcs.append((p.name,sha(p),b,np.asarray(state["z"]).reshape(b.nb,b.na)))
    data={}
    sstar=.8156151788040041
    for key,cache in caches.items():
        grid=cache.nodes
        i=np.flatnonzero((grid>=coarse.c)&(grid<=coarse.end))
        j=int(np.argmin(np.abs(cache.u-np.pi/2)))
        if abs(cache.u[j]-np.pi/2)>1e-14:raise ValueError("True material side axis required")
        nodes=grid[i];ang=cache.u[j]
        direct=load(here/"2ecf-polar-c2-independent-g11-resume-observe.py","meridian_direct")
        source=cache.jets[i,:,j,:]
        baseline=source.copy()
        table=[]
        for name,digest,basis,z in srcs:
            field=source if basis is None else source+direct.direct_packet(basis,nodes,z,np.array([ang]))[:,:,0,:]
            pos=field[:,0];rho=np.linalg.norm(pos[:,:2],axis=1)
            dr=np.diff(rho);dz=np.diff(pos[:,2]);polyline=np.linalg.norm(np.diff(pos,axis=0),axis=1)
            row=int(np.argmin(abs(nodes-sstar)))
            # The base's fixed-polar-azimuth tangent along the original path.
            def azimuth_derivative(packet,idx):
                p=packet[:,0,:2];v=packet[:,idx,:2]
                return (p[:,0]*v[:,1]-p[:,1]*v[:,0])/np.sum(p*p,axis=1)
            speed=field[:,1]
            base_ratio=azimuth_derivative(baseline,1)/azimuth_derivative(baseline,2)
            corr=field-baseline
            corr_w=corr[:,1]-base_ratio[:,None]*corr[:,2]
            S_ratio=azimuth_derivative(field,1)/azimuth_derivative(field,2)
            new_w=field[:,1]-S_ratio[:,None]*field[:,2]
            table.append(dict(name=name,stateSHA256=digest,materialU=float(ang),
                materialAxisMaxAbsX=float(abs(pos[:,0]).max()),minY=float(pos[:,1].min()),
                radialVariationPolygonal=float(sum(abs(dr))),heightVariationPolygonal=float(sum(abs(dz))),
                startEndHeightDifference=float(pos[-1,2]-pos[0,2]),largestNegativeHeightIncrement=float(min(dz)),
                spatialPolygonalLength=float(polyline.sum()),meridionalLength=basis.end-basis.c if basis is not None else coarse.end-coarse.c,
                closestActualNode=float(nodes[row]),actualCorrectionOnBaseFixedRayTangent=float(np.linalg.norm(corr_w[row])),
                actualBaseTangentRatio=float(base_ratio[row]),ownFixedPolarTangentialRatio=float(S_ratio[row]),
                ownFixedPolarSpeed=float(np.linalg.norm(new_w[row])),ownMaterialMeridianSpeed=float(np.linalg.norm(speed[row])),
                actualCorrectionAmplitudeInfinity=float(np.linalg.norm(corr[:,0],axis=-1).max())))
        data[key]=dict(radials=len(nodes),table=table)
    out=dict(schema="actual-sampled-H65-positive-y-axis-meridian-side-ray-correction-v1",
        entrySHA256=sha(__file__),preparedSHA256=sha(args.prepared),data=data,
        finiteOnly=True,originalCertifiedRayHasTinyNonzeroAzimuthOffset=True,
        sampledMaterialPathAtPiOverTwoNotDeclaredEqualToEveryCorrectedFixedAzimuthRay=True,
        noContinuousVariationUpperFromSamples=True)
    with args.output.open("x") as f:json.dump(out,f,indent=2);f.write("\n")
    for row in data["training"]["table"]:
        print(row["name"],row["radialVariationPolygonal"],row["heightVariationPolygonal"],row["spatialPolygonalLength"],row["actualCorrectionOnBaseFixedRayTangent"],row["materialAxisMaxAbsX"])


if __name__=="__main__":
    p=argparse.ArgumentParser()
    for k in ("scripts","prepared","output"):p.add_argument("--"+k,required=True,type=Path)
    p.add_argument("--states",nargs="+",type=Path,required=True)
    run(p.parse_args())
