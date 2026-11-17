#!/usr/bin/env python3
"""Select the unique kappa=0 interface S(u)=5/8, then one same-g true IVP.

S'=30u^2(1-u)^2>0 on (0,1). Eighty exact rational bisections specify
the mathematical interface; the solver uses its rounded binary64 time.
The successful unmodified input, all 962 equations, tolerances and step
controls are passed to the frozen continuation source without alteration.
"""
import argparse,contextlib,gzip,hashlib,importlib.util,io,json
from fractions import Fraction as F
from pathlib import Path

RESUME_SHA='e773a7066045fb164894370b9f53e02bb2140b47e4cc23d4e053cca55f2b8c15'
HOLD_SHA='ed6ea7d6590775767be9944d9aa305e93e8f054297648757b70e5aef962295a1'
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def load(p,name):
 s=importlib.util.spec_from_file_location(name,p);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m

def main(a):
 if sha(a.resume_source)!=RESUME_SHA or sha(a.hold_source)!=HOLD_SHA:raise ValueError('Frozen source changed')
 lo,hi=F(0),F(1)
 for _ in range(80):
  m=(lo+hi)/2;v=10*m**3-15*m**4+6*m**5-F(5,8)
  if v<0:lo=m
  else:hi=m
 slo,shi=F(1017,1000)+lo/50,F(1017,1000)+hi/50;a.end=float((slo+shi)/2)
 definition=dict(equation='kappa=-5/2+4S(u)=0; S=10u^3-15u^4+6u^5=5/8',
  uniqueness='S prime=30u^2(1-u)^2>0 on (0,1)',rational_bisections=80,u_lower=str(lo),u_upper=str(hi),
  exact_time_definition='1017/1000+u/50',time_lower=str(slo),time_upper=str(shi),binary64_target=a.end,
  binary64_target_distance_bound=str(max(abs(F(a.end)-slo),abs(F(a.end)-shi))))
 with contextlib.redirect_stdout(io.StringIO()):load(a.resume_source,'frozen_true_hold_resume').main(a)
 report=json.loads(a.out.read_text());parent=json.loads(gzip.decompress(a.input.read_bytes()));h=load(a.hold_source,'frozen_hold_for_interface')
 profile=h.HoldProfile(parent['fixed_scalar_profile']['geometry'],parent['analytic_extension_origin'],parent['hold_scalar_profile']['cut'],parent['hold_scalar_profile']['quadrature'])
 definition['evaluated_reference_jet']=profile.meridian(a.end)
 report.update(interface_selector_sha256=sha(__file__),mathematical_interface=definition,
  interface_limitations='Actual finite true-IVP interface only, if reached. No nonlinear DN, matching BVP, closed cap, or full geometric conclusion is asserted.')
 a.out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2),flush=True);print(json.dumps(dict(final_output_sha256=sha(a.out))),flush=True)

if __name__=='__main__':
 p=argparse.ArgumentParser(description=__doc__)
 for k in ('input','hold-source','resume-source','out'):p.add_argument('--'+k,type=Path,required=True)
 main(p.parse_args())
