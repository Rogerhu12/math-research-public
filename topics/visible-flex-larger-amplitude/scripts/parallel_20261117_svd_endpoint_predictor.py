#!/usr/bin/env python3
"""One isolated endpoint predictor for a fixed SVD boundary; no BVP iterate."""
import argparse,gzip,hashlib,json
from pathlib import Path
import numpy as np
from parallel_20261117_frenet_symbol import Frenet
from parallel_20261117_inward_profile import InwardProfile
from parallel_20261117_omitted_reachable_rows import OmittedRows
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
p=argparse.ArgumentParser(description=__doc__)
for name in ('parent','svd-report','svd-arrays','out'):p.add_argument('--'+name,type=Path,required=True)
p.add_argument('--alpha',type=float,default=1/64);a=p.parse_args()
d=json.loads(gzip.decompress(a.parent.read_bytes()));r=json.loads(a.svd_report.read_bytes());v=np.load(a.svd_arrays)
if sha(a.parent)!=r['parent_sha256'] or sha(a.svd_arrays)!=r['array_sha256']:raise ValueError('Input identity mismatch')
if not d['success'] or sha(Path(__file__).with_name('parallel_20261117_inward_profile.py'))!=d['inward_profile_sha256']:raise ValueError('Parent or scalar mismatch')
q=Frenet(d['M'],d['N']);s=d['inward_scalar_profile'];profile=InwardProfile(d['fixed_scalar_profile']['geometry'],d['analytic_extension_origin'],s['cut'],s['curvature'],s['ramp_in'],s['ramp_out'],s['quadrature'])
radius,ap,_=profile(d['mesh'][-1]);k=ap/radius;y=np.asarray(d['states'][-1]);f=OmittedRows(q,k);U=v['U'];b=v['raw_parent_values']
if not np.array_equal(f.value(y),b):raise ValueError('Stored targets differ from the actual parent')
def read(z):
 local=q.local(z,k);raw=f.value(z);error=local['V']-q.jet(q.project(local['V']))[0]
 return dict(raw=raw,min_H_over_W=float(np.min(local['H']/local['W'])),unretained_velocity_sample_max=float(np.max(np.linalg.norm(error,axis=1))))
initial=read(y);trial=read(y-a.alpha*v['endpoint_correction']);delta=U.T@(trial.pop('raw')-(1-a.alpha)*b);initial.pop('raw')
report=dict(scope=__doc__+' Interior equations and domain are not evaluated; this is only initialization data.',source_sha256=sha(__file__),parent_sha256=sha(a.parent),svd_report_sha256=sha(a.svd_report),svd_arrays_sha256=sha(a.svd_arrays),alpha=a.alpha,beta=1-a.alpha,initial=initial,trial=trial,combined_homotopy_mismatch_l2=float(np.linalg.norm(delta)),combined_homotopy_mismatch_max=float(np.max(abs(delta))))
a.out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report));print(json.dumps(dict(output_sha256=sha(a.out))))
