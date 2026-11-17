#!/usr/bin/env python3
"""Screen the raw compact core at a fixed accepted cosine anchor.

This verifies the lambda-zero interface, original complete core rho guards,
and the sampled complete controls.  It never claims a solved prefix.
"""
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[key]='1'
import argparse
import gzip
import hashlib
import json
from pathlib import Path
import sys
import numpy as np
from couple_m3_smallcut_secant import accepted_anchor


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--prefix',type=Path,required=True)
    p.add_argument('--source-topic',type=Path,required=True)
    p.add_argument('--out',type=Path,required=True)
    p.add_argument('--samples',type=int,default=32768)
    p.add_argument('--control-transition',type=float,default=.16)
    a=p.parse_args();lib=Path(__file__).with_name('round_raw_lib');sys.path.insert(0,str(lib))
    from plateau_core import PlateauSupportCore
    from fixed_large_radius_core import make_core_class
    from tight_moment_interval_bounds import install
    install();Core=make_core_class(PlateauSupportCore)
    r=json.load(gzip.open(a.prefix,'rt'));accepted_anchor(r,a.prefix)
    if r.get('core_round_settings'):raise ValueError('Use the cosine anchor for this path screen')
    q=r['actual_primary_amplitude'];c=np.asarray(r['parameters'][1:])*r['central_correction_scales']
    settings=dict(halfwidth=.21,transition=.08,control_transition=a.control_transition,
        center=np.pi/3,bimodal_eta=0.,lock_fundamental=True,coefficient_precision=80,
        positivity_grid_max=32768,arc_nodes=1024)
    x=2*np.pi/3*np.arange(a.samples)/a.samples;rows=[]
    for lam in [0,.02,.1,.25,.5,1.]:
        core=Core(q,c,3,homotopy=lam,**settings);b=core.basis.support_jets(x,2,lam)
        cc=c@(b[0]+b[2]);g=core.normal_geometry(x)
        row=dict(homotopy=lam,rho_lower=core.rho_lower,rho_min_sample=float(min(g['rho'])),
          rho_max_sample=float(max(g['rho'])),grid_used=core.positivity_grid_per_sector,
          full_control_rho_linf=float(max(abs(cc))),full_control_support_linf=float(max(abs(c@b[0]))),
          coefficient_projection_residual_upper=float(core.basis.certificate['neumann_residual']))
        rows.append(row);print(json.dumps(row),flush=True)
        if lam==0:zero=core
        if lam==1:final=core
    sys.path.insert(0,str(a.source_topic/'notes'))
    from fixed_metric_mode3_core import PlanarSupportCore
    old=PlanarSupportCore(q,c,3);u=np.linspace(.001,2*np.pi-.002,513)
    zg,og=zero.evaluate(u),old.evaluate(u)
    checks={k:float(np.max(abs(zg[k]-og[k]))) for k in ('F','Ft','Ftt','kappa')}
    checks['parameter_F']=float(np.max(abs(zero.parameter_derivatives(u)-old.parameter_derivatives(u))))
    arc=final.center+np.linspace(-.20,.20,513);flat=final.normal_geometry(arc)
    checks['lambda_one_arc_rho_max_abs_difference']=float(max(abs(flat['rho']-(1+8*q))))
    result=dict(scope=__doc__,command=sys.argv,input=str(a.prefix.resolve()),
      input_sha256=hashlib.sha256(a.prefix.read_bytes()).hexdigest(),settings=settings,
      source_sha256={str(f.resolve()):hashlib.sha256(f.read_bytes()).hexdigest() for f in
       [Path(__file__),a.source_topic/'notes/fixed_metric_mode3_core.py',*sorted(lib.glob('*.py'))]},
      q=q,physical_controls=c.tolist(),samples_per_sector=a.samples,rows=rows,
      interface_checks=checks,core_summary=final.summary(),
      source_definition='Mean/primary projection only; the higher low moments vary with lambda. Lambda-one control span agrees with the canonical compact space.')
    a.out.parent.mkdir(parents=True,exist_ok=True);a.out.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(checks),flush=True)


if __name__=='__main__':main()
