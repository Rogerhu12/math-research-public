#!/usr/bin/env python3
"""Bind the original complete solver to the newly prepared 1.03 problem.
Only input identities, the descriptive scope and initial diagnostics differ.
No Newton, equation, Jacobian, boundary, tolerance or budget rule is edited.
"""
import argparse,hashlib,importlib.util,json
from pathlib import Path
BASE='f93d74382ac83bee08079759ca17cace95b3e99cb765e706e6d1ef67c7861d81'
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def main(a):
 if sha(a.base_source)!=BASE:raise ValueError('Frozen complete BVP source changed')
 code=a.base_source.read_text()
 changes={
  'One original-budget full HoldProfile BVP':'One original-budget 1.03 full HoldProfile BVP',
  '7feed9f91f60a28d42a0bce352d742804bf11f9b9e5dd567ea5ad871eacebe74':'1662ee34a820776570c7535ee5735812d7e7a27822901849c211a89992629057',
  '54ee88a8d6d44307431e3ee35dabbc8c907631cfb62512b9bd8b5f59a94260ba':'2d3c4133959e662b87289fb26fd1aa2c73d2a1ddd278e8f0e1d23fbc1b9d6f7e',
  'warm_initial_coefficient_defect=.3270395216151608':'warm_initial_coefficient_defect=.0003393988237490597',
  'warm_initial_relative_vector_rms=.027936526188258648':'warm_initial_relative_vector_rms=2.4999437404316108e-5',
  'warm_collocation_H_sample_lower=6.545488805882082e-9':'warm_collocation_H_sample_lower=.00021241422793829255',
  'terminal_Schur_relative_sep_estimate=4.607105234715574e-11':'terminal_Schur_relative_sep_estimate=1.8484379119530975e-10'}
 for old,new in changes.items():
  if code.count(old)!=1:raise ValueError('Exact source replacement must occur once: '+old)
  code=code.replace(old,new)
 a.generated_source.write_text(code);spec=importlib.util.spec_from_file_location('complete_short_hold_BVP',a.generated_source);module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module);module.main(a)
 rp=a.out.with_suffix('.report.json');report=json.loads(rp.read_text());report.update(solver_patch_generator_sha256=sha(__file__),base_solver_sha256=BASE,generated_solver_sha256=sha(a.generated_source))
 rp.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(dict(final_report_sha256=sha(rp),generated_solver_sha256=sha(a.generated_source),generator_sha256=sha(__file__))),flush=True)
if __name__=='__main__':
 p=argparse.ArgumentParser(description=__doc__)
 for k in ('base-source','generated-source','topic','warm','arrays','hold-source','out'):p.add_argument('--'+k,type=Path,required=True)
 main(p.parse_args())
