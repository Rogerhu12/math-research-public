#!/usr/bin/env python3
"""A complete value/first/second-jet bridge for a finite shooting field.

The old prefix is retained. This changes the local map, so the bridged
field is explicitly not labelled as the accepted finite BVP.
"""
import argparse,gzip,hashlib,importlib.util,json
from pathlib import Path
import numpy as np

p=argparse.ArgumentParser(description=__doc__)
for key in ('topic','parent','field','out'):p.add_argument('--'+key,type=Path,required=True)
p.add_argument('--join-width',type=float,default=.0005)
p.add_argument('--angles',type=int,default=8192);p.add_argument('--radial-subdivisions',type=int,default=4)
args=p.parse_args()
def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()
reader_path=args.topic/'notes/2026-11-17-parallel-geometry-short-ivp-field.py'
if sha(reader_path)!='ed0de0d513f28e1d227ba4f49a2ac2b2379107ca200c50f0d43f933e0edfd924':
 raise ValueError('The frozen common-jet reader changed')
spec=importlib.util.spec_from_file_location('value_bridge_reader',reader_path)
reader=importlib.util.module_from_spec(spec);spec.loader.exec_module(reader)
parent=json.loads(gzip.decompress(args.parent.read_bytes()));field=json.loads(gzip.decompress(args.field.read_bytes()))
if not parent.get('success') or not field.get('bvp_accepted'):raise ValueError('Accepted original prefix and finite shooting field required')
if field['reference_sha256']!=sha(args.parent):raise ValueError('Wrong original prefix')
profile=reader.h.profile_from(field);old=reader.h.Frenet(parent['M'],parent['N']);M=field['M']
mesh=np.array(field['mesh']);Y=np.array(field['states']);V=np.array(field['rhs']);A=np.array(field['d2'])
old_y=np.array(parent['states'][-1]);old_v=np.array(parent['rhs'][-1]);a,ap,app=profile(mesh[0]);k=ap/a
old_a=old.jvp(old_y,k,old_v,dk=app/a-k*k)
Y0,V0,A0=[reader.lift(v,old.M,M) for v in (old_y,old_v,old_a)]
if mesh[0]!=parent['mesh'][-1]:raise ValueError('The cut is not the exact shared node')
core=np.pad(np.array(parent['core']['coefficients']),(0,M-old.M))
if not np.array_equal(core,np.array(field['original_core_coefficients'])):raise ValueError('Physical density changed')
j=int(np.argmin(abs(mesh-(mesh[0]+args.join_width))))
if not 0<j<len(mesh):raise ValueError('Invalid actual join node')
width=mesh[j]-mesh[0];deltas=[Y[0]-Y0,V[0]-V0,A[0]-A0]
basis=np.array([[1.,0.,0.,-10.,15.,-6.],[0.,1.,0.,-6.,8.,-3.],[0.,0.,.5,-1.5,1.5,-.5]])
coeff=sum((width**ell)*basis[ell,:,None]*deltas[ell][None,:] for ell in range(3))
resultY=Y.copy();resultV=V.copy();resultA=A.copy()
for i in range(1,j):
 u=(mesh[i]-mesh[0])/width
 resultY[i]-=np.polynomial.polynomial.polyval(u,coeff)
 resultV[i]-=np.polynomial.polynomial.polyval(u,np.arange(1,6)[:,None]*coeff[1:])/width
 resultA[i]-=np.polynomial.polynomial.polyval(u,(np.arange(2,6)*np.arange(1,5))[:,None]*coeff[2:])/width**2
resultY[0]=Y0;resultV[0]=V0;resultA[0]=A0
definition=dict(source_sha256=sha(__file__),reader_sha256=sha(reader_path),parent_sha256=sha(args.parent),
 source_field_sha256=sha(args.field),source_shooting_definition=field.get('finite_shooting_definition'),
 join_index=j,join_width=float(width),requested_width=args.join_width,
 formula='Fnew=Flocal-p0(u)*delta0-width*p1(u)*delta1-width^2*p2(u)*delta2',basis=basis.tolist(),
 initial_shared_jet_equal=[bool(np.array_equal(a,b)) for a,b in zip((resultY[0],resultV[0],resultA[0]),(Y0,V0,A0))],
 terminal_shared_jet_equal=[bool(np.array_equal(a[j:],b[j:])) for a,b in zip((resultY,resultV,resultA),(Y,V,A))],
 common_original_density=True,old_prefix_unchanged=True)
bridged=dict(field);bridged.update(states=resultY.tolist(),rhs=resultV.tolist(),d2=resultA.tolist(),
 source_sha256=sha(__file__),bvp_accepted=False,ivp_reached_end=False,source_finite_bvp_accepted=True,
 old_prefix_C2_join_completed=True,actual_C2_join_completed=True,complete_prefix=False,
 old_cut_jets=dict(value=Y0.tolist(),first=V0.tolist(),second=A0.tolist()),
 explicit_value_jet_bridge=definition,geometry_definition='Unique quintic matching all stored common 0/1/2 jets')
args.out.write_bytes(gzip.compress(json.dumps(bridged,separators=(',',':')).encode(),mtime=0))
report=dict(scope=__doc__,bridge=definition,field_sha256=sha(args.out),
 unbridged_actual_quintic=reader.read_field(field,profile,args.angles,args.radial_subdivisions),
 bridged_actual_quintic=reader.read_field(bridged,profile,args.angles,args.radial_subdivisions),
 full_old_prefix_resampled=False,closed_surface=False,reach_certified=False,fixed_metric_refinement_complete=False)
report_path=args.out.with_suffix('.readout.json');report_path.write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report),flush=True);print(json.dumps(dict(report_sha256=sha(report_path))),flush=True)
