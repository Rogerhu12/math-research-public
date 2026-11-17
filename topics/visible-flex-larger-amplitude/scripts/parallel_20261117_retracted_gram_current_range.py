#!/usr/bin/env python3
"""One fixed actual-parent range probe for normalized endpoint er/fr.

Reuse the frozen full endpoint Jacobian, transport no new range here, and
require the supplied range report to belong to the same accepted parent.
No BVP, interior nonlinear update, or new accepted field is produced.
"""
import argparse,gzip,hashlib,importlib.util,json,sys,time
from pathlib import Path
import numpy as np

def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()

def main(a):
 t=time.perf_counter();sys.path.insert(0,str(a.scripts))
 from parallel_20261117_frenet_symbol import Frenet
 from parallel_20261117_inward_profile import InwardProfile
 parent=json.loads(gzip.decompress(a.input.read_bytes()));identity=sha(a.input)
 probe=json.loads(a.probe_report.read_bytes());transfer=json.loads(a.transfer_report.read_bytes())
 if not parent.get('success')or probe['input_sha256']!=identity or transfer['input_sha256']!=identity:
  raise ValueError('The state, endpoint Jacobian, and complete transport must share one accepted parent')
 if sha(a.probe_module)!=probe['source_sha256']:raise ValueError('Endpoint function source changed')
 spec=importlib.util.spec_from_file_location('fixed_retracted_gram',a.probe_module)
 module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
 pa=a.probe_report.parent/probe['array_path'];ta=a.transfer_report.parent/transfer['array_path']
 if sha(pa)!=probe['array_sha256']or sha(ta)!=transfer['array_sha256']:raise ValueError('Frozen arrays changed')
 with np.load(pa,allow_pickle=False)as d:values=d['values'];J=d['jacobian'];oldZ=d['old_terminal_basis']
 with np.load(ta,allow_pickle=False)as d:Z=d['terminal_basis']
 q=Frenet(parent['M'],parent['N']);p=parent['inward_scalar_profile']
 profile=InwardProfile(parent['fixed_scalar_profile']['geometry'],parent['analytic_extension_origin'],p['cut'],p['curvature'],p['ramp_in'],p['ramp_out'],p['quadrature'])
 r,ap,_=profile(parent['mesh'][-1]);model=module.RetractedGram(q,r,ap);y=np.array(parent['states'][-1])
 if max(abs(model.value(y)-values))>1e-15:raise ValueError('Frozen endpoint functional no longer agrees')
 A=J@Z;U,s,Vt=np.linalg.svd(A,full_matrices=False)
 threshold=max(A.shape)*np.finfo(float).eps*s[0]
 coordinates=Vt.T@((U.T@values)/s);delta=Z@coordinates;remainder=values-A@coordinates
 trials=[]
 for alpha in (1.,.25,.0625,.015625):
  try:
   yy=y-alpha*delta;f=model.value(yy);v=model.metrics(yy)
   v.update(alpha=alpha,nonlinear_linearization_remainder_inf=float(max(abs(f-(values-alpha*A@coordinates)))),
    residual_to_scaled_parent_inf=float(max(abs(f-(1-alpha)*values))))
  except FloatingPointError as e:v=dict(alpha=alpha,domain_error=str(e))
  trials.append(v)
 angles=np.linalg.svd(oldZ.T@Z,compute_uv=False)
 arrays=a.out.with_suffix('.arrays.npz')
 np.savez_compressed(arrays,terminal_basis=Z,reduced_jacobian=A,U=U,singular_values=s,endpoint_correction=delta,linear_remainder=remainder)
 report=dict(scope=__doc__,input_sha256=identity,source_sha256=sha(__file__),
  probe_module_sha256=sha(a.probe_module),probe_report_sha256=sha(a.probe_report),probe_array_sha256=sha(pa),
  actual_transfer_report_sha256=sha(a.transfer_report),actual_transfer_array_sha256=sha(ta),
  actual_transfer_seconds=transfer['seconds'],actual_transfer_collocation_residual_max=transfer['collocation_residual_max'],
  actual_transfer_relative_error=transfer['transfer_relative_frobenius_max'],actual_transfer_orthogonality=transfer['orthogonality_max'],
  full_ODE_components=q.n,left_rows=transfer['left_rows'],intervals=transfer['nodes']-1,free_dimensions=Z.shape[1],
  function_rows=len(values),initial=model.metrics(y),reduced_singular_max=float(s[0]),reduced_singular_min=float(s[-1]),
  reduced_condition=float(s[0]/s[-1]),reduced_numerical_rank=int(sum(s>threshold)),rank_threshold=float(threshold),
  correction_inf=float(max(abs(delta))),correction_l2=float(np.linalg.norm(delta)),
  linear_remainder_inf=float(max(abs(remainder))),linear_remainder_l2_fraction=float(np.linalg.norm(remainder)/np.linalg.norm(values)),
  smallest_old_current_subspace_cosine=float(angles[-1]),endpoint_only_nonlinear_trials=trials,
  array_path=str(arrays),array_sha256=sha(arrays),seconds=time.perf_counter()-t)
 a.out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2));print(json.dumps(dict(output_sha256=sha(a.out))))

if __name__=='__main__':
 p=argparse.ArgumentParser(description=__doc__)
 for key in ('scripts','input','probe-module','probe-report','transfer-report','out'):p.add_argument('--'+key,type=Path,required=True)
 main(p.parse_args())
