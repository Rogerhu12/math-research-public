#!/usr/bin/env python3
"""Compare saved source jets and finite C2 tail jets at the same physical points.

The source packets are scratch outputs of probe_tail_spatial_jets.mjs. Common
angles are selected exactly; no rigid alignment or angular interpolation is used.
The finite map includes its actual outer one-ulp radius reparametrization.
"""
from pathlib import Path
import argparse,hashlib,importlib.util,json
import numpy as np
p=argparse.ArgumentParser(description=__doc__)
for k in ['coarse-jets','fine-jets','coarse-manifest','fine-manifest','tail-reader','out']:p.add_argument('--'+k,type=Path,required=True)
a=p.parse_args();spec=importlib.util.spec_from_file_location('peak_tail_reader',a.tail_reader);reader=importlib.util.module_from_spec(spec);spec.loader.exec_module(reader)
ft=[reader.IntegratedTail(p)for p in [a.coarse_manifest,a.fine_manifest]];data=[json.loads(p.read_text())for p in [a.coarse_jets,a.fine_jets]];rows=[]
assert len(data[0])==len(data[1])
for j in range(len(data[0])):
 radius=data[0][j]['radius'];assert data[1][j]['radius']==radius
 theta=np.array([z['theta']for z in data[0][j]['jets']]);finite=[];source=[]
 for f,d in zip(ft,data):
  R=np.longdouble(radius);cut=np.longdouble(f.meta['parameters']['rCut']);c=np.longdouble(f.meta['radialGeometry']['outerAnchor']);W=np.longdouble('.02');t=np.clip((R-(cut-W))/W,0,1)
  rv=R+(c-cut)*t**3*(10+t*(-15+6*t));r1=1+(c-cut)*30*t*t*(1-t)**2/W;r2=(c-cut)*60*t*(1-t)*(1-2*t)/(W*W)
  co=f.coefficients(rv);v=co[2]*r1*r1+co[1]*r2
  xy=v[:f.P]@np.exp(1j*f.planar_modes[:,None]*theta);z=v[f.P:]@np.cos(f.height_modes[:,None]*theta)
  finite.append(np.array([xy.real,xy.imag,z],float).T)
  assert len(d[j]['jets'])%len(theta)==0
  step=len(d[j]['jets'])//len(theta);selected=d[j]['jets'][::step]
  assert all(abs(v['theta']-th)<1e-15 for v,th in zip(selected,theta))
  source.append(np.array([v['Vrr']for v in selected],float))
 rows.append(dict(radius=radius,common_angles=len(theta),finite_actual_second_difference=float(np.linalg.norm(finite[0]-finite[1],axis=1).max()),source_actual_second_difference=float(np.linalg.norm(source[0]-source[1],axis=1).max()),coarse_finite_to_source_rr_difference=float(np.linalg.norm(finite[0]-source[0],axis=1).max()),fine_finite_to_source_rr_difference=float(np.linalg.norm(finite[1]-source[1],axis=1).max())))
record=dict(scope=__doc__,source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),inputs={str(p.resolve()):hashlib.sha256(p.read_bytes()).hexdigest()for p in [a.coarse_jets,a.fine_jets,a.coarse_manifest,a.fine_manifest,a.tail_reader]},rows=rows,numerical_evidence_only=True)
a.out.write_text(json.dumps(record,indent=2)+'\n');print(json.dumps(rows))
