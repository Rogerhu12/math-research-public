#!/usr/bin/env python3
"""Read the complete negative-hold prefix after an explicit C2 jet bridge.

The saved local IVP is not rerun. Its first 32 cells receive the R637
quintic correction, using the old M112 velocity and JVP acceleration.
All old cells are exactly zero-lifted with their original second jets.
The frozen arclength engine then constructs one fixed q_N normalization
on the complete common-quintic field, using the correct HoldProfile.
This creates an open C2 geometric candidate, not a new accepted BVP.
"""
import argparse,contextlib,gzip,hashlib,importlib.util,io,json
from pathlib import Path
import numpy as np
import parallel_20261117_frenet_symbol as symbol
import parallel_20261117_profile as original_scalar

ENGINE_SHA='31782ba06d5414a7851284ce330a89d208b8d56c4f1d99421a804e2a78271266'
HOLD_SHA='ed6ea7d6590775767be9944d9aa305e93e8f054297648757b70e5aef962295a1'
SYMBOL_SHA='7fea9a209e8dc9785b4672787805db6a44c96884f3b455cfc62d8ff6f0d0b831'
SCALAR_SHA='08b1894ca407a0c49b0de80427c669cafe702ab5878b1abf7b346994138d79b3'

def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def module(p,name):
 spec=importlib.util.spec_from_file_location(name,p);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);return m
def write_field(path,data):path.write_bytes(gzip.compress((json.dumps(data)+'\n').encode(),mtime=0))

def assemble(a):
 parent=json.loads(gzip.decompress(a.parent.read_bytes()));local=json.loads(gzip.decompress(a.local.read_bytes()))
 if not parent.get('success') or not local.get('ivp_reached_end'):raise ValueError('Require the actual accepted parent and completed local IVP')
 if local['reference_sha256']!=sha(a.parent) or local['hold_profile_sha256']!=sha(a.hold_source):raise ValueError('Parent or scalar identity differs')
 if local['fixed_scalar_profile']!=parent['fixed_scalar_profile'] or local['analytic_extension_origin']!=parent['analytic_extension_origin']:raise ValueError('Different inherited scalar')
 if parent['mesh'][-1]!=local['mesh'][0]:raise ValueError('The cut is not a common exact node')
 hold=module(a.hold_source,'frozen_hold_scalar')
 profile=hold.HoldProfile(parent['fixed_scalar_profile']['geometry'],parent['analytic_extension_origin'],local['hold_scalar_profile']['cut'],local['hold_scalar_profile']['quadrature'])
 if profile.spec()!=local['hold_scalar_profile']:raise ValueError('Different HoldProfile definition')
 base=original_scalar.Profile(parent['fixed_scalar_profile']['geometry'],parent['analytic_extension_origin'])
 old=symbol.Frenet(parent['M'],parent['N']);M=local['M'];m=old.M
 if M<m:raise ValueError('Every old Fourier mode must be retained')
 def lift(v):
  out=np.zeros(3*M+2);out[:m+1]=v[:m+1];out[M+1:M+m+1]=v[m+1:2*m+1];out[2*M+1:2*M+m+2]=v[2*m+1:];return out
 X=np.array(parent['mesh']);oldY=np.array(parent['states']);oldV=np.array(parent['rhs']);oldA=[]
 for s,y,v in zip(X,oldY,oldV):
  r,ap,app=base(s);k=ap/r;oldA.append(old.jvp(y,k,v,dk=app/r-k*k))
 oldY=np.array([lift(v)for v in oldY]);oldV=np.array([lift(v)for v in oldV]);oldA=np.array([lift(v)for v in oldA])
 x=np.array(local['mesh']);Y,V,A=[np.array(local[k])for k in ('states','rhs','d2')];j=a.join_index
 if not 1<=j<len(x):raise ValueError('Join index must be an actual interior or terminal node')
 if not np.array_equal(Y[0],oldY[-1]):raise ValueError('Initial positions differ')
 if not np.array_equal(oldY[0,1:M+1],np.array(local['original_core_coefficients'])):raise ValueError('The material density changed')
 recorded=[float(np.max(abs(np.array(local['old_cut_jets'][key])-v[-1])))for key,v in zip(('value','first','second'),(oldY,oldV,oldA))]
 if any(recorded):raise ValueError('Recorded old jets differ from the original operator: '+str(recorded))
 dv=V[0]-oldV[-1];da=A[0]-oldA[-1];width=float(x[j]-x[0])
 p1=np.array([0.,1.,0.,-6.,8.,-3.]);p2=np.array([0.,0.,.5,-1.5,1.5,-.5])
 d1=np.arange(1,6)*p1[1:];d2=np.arange(1,6)*p2[1:]
 dd1=np.arange(2,6)*np.arange(1,5)*p1[2:];dd2=np.arange(2,6)*np.arange(1,5)*p2[2:]
 for i in range(1,j):
  u=(x[i]-x[0])/width;ev=np.polynomial.polynomial.polyval
  Y[i]-=width*ev(u,p1)*dv+width**2*ev(u,p2)*da
  V[i]-=ev(u,d1)*dv+width*ev(u,d2)*da
  A[i]-=ev(u,dd1)/width*dv+ev(u,dd2)*da
 Y[0]=oldY[-1];V[0]=oldV[-1];A[0]=oldA[-1]
 unchanged=[bool(np.array_equal(v[j:],np.array(local[key])[j:]))for v,key in zip((Y,V,A),('states','rhs','d2'))]
 differences=[float(np.max(abs(v[-1]-z[0])))for v,z in zip((oldY,oldV,oldA),(Y,V,A))]
 if any(differences) or not all(unchanged):raise ValueError('C2 interface identity failed')
 bridge=dict(join_index=j,cut=float(x[0]),end=float(x[j]),width=width,first_basis=p1.tolist(),second_basis=p2.tolist(),
  formula='F_local-width*p1(u)*delta_first-width^2*p2(u)*delta_second',delta_first_max=float(max(abs(dv))),delta_second_max=float(max(abs(da))),
  original_recorded_jet_differences=recorded,cut_jet_differences=differences,all_jets_from_join_on_unchanged=unchanged)
 local.update(schema='negative-hold-explicit-C2-bridge-v1',scope=__doc__,source_ivp_sha256=sha(a.local),source_ivp_reached_end=True,ivp_reached_end=False,
  bvp_accepted=False,old_prefix_C2_join_completed=True,source_sha256=sha(__file__),explicit_jet_bridge=bridge,states=Y.tolist(),rhs=V.tolist(),d2=A.tolist())
 write_field(a.corrected,local)
 data=dict(schema='assembled-negative-hold-common-quintic-v1',scope=__doc__,bvp_accepted=False,complete_prefix=True,old_prefix_C2_join_completed=True,
  source_sha256=sha(__file__),source_ivp_sha256=sha(a.local),parent_sha256=sha(a.parent),local_sha256=sha(a.corrected),hold_profile_source_sha256=sha(a.hold_source),
  arclength_engine_sha256=sha(a.arclength_source),frenet_source_sha256=sha(symbol.__file__),old_profile_source_sha256=sha(original_scalar.__file__),
  fixed_scalar_profile=parent['fixed_scalar_profile'],analytic_extension_origin=parent['analytic_extension_origin'],hold_scalar_profile=profile.spec(),
  M=M,N=local['N'],cut_jet_differences=differences,explicit_jet_bridge=bridge,original_core_coefficients=local['original_core_coefficients'],
  mesh=np.r_[X,x[1:]].tolist(),states=np.r_[oldY,Y[1:]].tolist(),rhs=np.r_[oldV,V[1:]].tolist(),d2=np.r_[oldA,A[1:]].tolist())
 write_field(a.assembled,data);a.input=a.assembled;a.bridge=bridge
 print(json.dumps(dict(event='assembled',old_cells=len(X)-1,local_cells=len(x)-1,complete_cells=len(X)+len(x)-2,cut_jet_differences=differences,corrected_sha256=sha(a.corrected),assembled_sha256=sha(a.assembled))),flush=True)
 return data,profile

def main(a):
 for p,expected in ((a.arclength_source,ENGINE_SHA),(a.hold_source,HOLD_SHA),(symbol.__file__,SYMBOL_SHA),(original_scalar.__file__,SCALAR_SHA)):
  if sha(p)!=expected:raise ValueError('A frozen scientific source changed: '+str(p))
 engine=module(a.arclength_source,'frozen_full_arclength_engine');engine.assemble=assemble;a.pulse_source=a.hold_source
 # The unchanged engine's pulse-specific metadata is replaced before delivery.
 with contextlib.redirect_stdout(io.StringIO()):engine.main(a)
 report=json.loads(a.out.read_text());report.update(scope=__doc__,source_sha256=sha(__file__),arclength_engine_sha256=sha(a.arclength_source),
  source_ivp_sha256=sha(a.local),local_sha256=sha(a.corrected),hold_profile_source_sha256=report.pop('pulse_source_sha256'),explicit_jet_bridge=a.bridge,
  old_prefix_second_jets='Computed with the original M112/N2048 operator and original scalar before exact zero-lift; not recomputed at M320.',
  ivp_rerun=False,new_BVP_solved=False)
 a.out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2));print(json.dumps(dict(output_sha256=sha(a.out))))

if __name__=='__main__':
 p=argparse.ArgumentParser(description=__doc__)
 for key in ('parent','local','hold-source','arclength-source','corrected','assembled','out'):p.add_argument('--'+key,type=Path,required=True)
 p.add_argument('--join-index',type=int,default=32);p.add_argument('--construction-angles',type=int,default=4096)
 p.add_argument('--angles',type=int,default=8192);p.add_argument('--radial-subdivisions',type=int,default=4);main(p.parse_args())
