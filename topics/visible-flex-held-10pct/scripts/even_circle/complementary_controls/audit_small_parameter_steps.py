"""Small-step check of the sharpest new fixed-material parameter column."""
import argparse
import importlib.util
import json
import time
from pathlib import Path
import numpy as np
from audit_uniform_core import refined_evaluation, sha
from uniform_complement_core import make_core_class


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--reference-core',type=Path,required=True)
    parser.add_argument('--out',type=Path,required=True)
    args=parser.parse_args();start=time.monotonic()
    spec=importlib.util.spec_from_file_location('small_step_reference_core',args.reference_core)
    module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
    Core=make_core_class(module.PlateauSupportCore)
    common=dict(base_mode=4,halfwidth=.145,transition=.08,control_transition=.08,arc_nodes=512)
    params=np.array([.005,1e-5,-2e-6,3e-7,-4e-8,5e-9])
    theta=np.linspace(.013,2*np.pi-.019,71)
    rows=[]
    for lam in (0.,.4,1.):
        core=Core(q=params[0],corrections=params[1:],homotopy=lam,**common)
        analytic=core.parameter_derivatives(theta)[5]
        scale=float(np.max(np.linalg.norm(analytic,axis=1)))
        errors=[]
        for h in (1.25e-6,6.25e-7,3.125e-7,1.5625e-7,7.8125e-8):
            plus=params.copy();minus=params.copy();plus[5]+=h;minus[5]-=h
            cp=Core(q=plus[0],corrections=plus[1:],homotopy=lam,**common)
            cm=Core(q=minus[0],corrections=minus[1:],homotopy=lam,**common)
            fp=refined_evaluation(cp,theta)[0]['F'];fm=refined_evaluation(cm,theta)[0]['F']
            fd=(fp-fm)/(2*h)
            err=float(np.max(np.linalg.norm(fd-analytic,axis=1)))
            errors.append(dict(correction_step=h,absolute_error=err,relative_error=err/scale))
        rows.append(dict(homotopy=lam,parameter_index=5,analytic_max_norm=scale,steps=errors))
    out=dict(scope='Finite-difference check of the existing analytic parameter Jacobian; no BVP and no geometric certificate.',
        reference_sha256=sha(args.reference_core),
        source_sha256={n:sha(Path(__file__).with_name(n)) for n in ('audit_small_parameter_steps.py','audit_uniform_core.py','uniform_complement_core.py','complementary_moment_basis.py','moment_interval_bounds.py')},
        normal_angle_inverse='Five Newton refinements after the inherited safeguarded arc inverse.',
        coefficients=params.tolist(),rows=rows,elapsed_seconds=time.monotonic()-start)
    args.out.write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(dict(rows=rows,elapsed_seconds=out['elapsed_seconds'])))


if __name__=='__main__':main()
