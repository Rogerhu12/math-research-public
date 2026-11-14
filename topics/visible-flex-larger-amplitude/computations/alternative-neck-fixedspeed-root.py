#!/usr/bin/env python3
"""One targeted linear neck redesign: fix vd and solve delta/boost length.

The complete finite C2 neck is propagated. This is a two-mode linear
matching calculation, not a nonlinear prefix or closed-surface result.
It is intended to move the K7 seed away from vd almost equal to one.
"""
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[key]='1'
import argparse,hashlib,importlib.util,json,time
from pathlib import Path
import numpy as np
from scipy.optimize import least_squares
P=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('alternative_fixedspeed_provider',P/'alternative-neck-provider.py')
neck=importlib.util.module_from_spec(spec);spec.loader.exec_module(neck)

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--port',type=Path,required=True)
    p.add_argument('--profile',type=Path,required=True)
    p.add_argument('--vd',type=float,default=.98)
    p.add_argument('--out',type=Path,required=True)
    p.add_argument('--profile-out',type=Path)
    a=p.parse_args();start=time.time()
    cfg=json.loads(a.profile.read_text());port=json.loads(a.port.read_text())
    calls=[]
    def evaluate(x,details=False):
        c={**cfg,'delta':float(x[0]),'boost_length':float(x[1]),'vd':a.vd}
        answer=neck.LinearScreen(port,c).evaluate([x[0],a.vd],details)
        if not details:calls.append(dict(delta=float(x[0]),boost_length=float(x[1]),residual=answer.tolist()))
        return answer
    seed=[cfg['delta'],cfg['boost_length']]
    z=least_squares(evaluate,seed,bounds=([.025,.08],[.25,.5]),
                    x_scale=[.05,.1],xtol=3e-10,ftol=3e-10,gtol=3e-10,max_nfev=65)
    row=evaluate(z.x,True)
    out=dict(scope=__doc__,vd=a.vd,seed=seed,solver_success=bool(z.success),
             message=z.message,nfev=int(z.nfev),row=row,calls=calls,
             seconds=time.time()-start,
             source_sha256={name:hashlib.sha256((P/name).read_bytes()).hexdigest()
               for name in ['alternative-neck-fixedspeed-root.py','alternative-neck-provider.py','alternative-neck-flatturn.py','alternative-neck-excursion.py','alternative-angle-plateau-connector.py','alternative-direct-tail-connector.py']},
             input_profile_sha256=hashlib.sha256(a.profile.read_bytes()).hexdigest(),
             port_sha256=hashlib.sha256(a.port.read_bytes()).hexdigest())
    a.out.write_text(json.dumps(out,indent=2)+'\n')
    if a.profile_out and row['residual_max']<2e-6:
        a.profile_out.write_text(json.dumps(row['profile'],indent=2)+'\n')
    print(json.dumps(dict(seconds=out['seconds'],nfev=int(z.nfev),
        profile=row['profile'],residual=row['residual'],
        height=row['total_background_height'],
        H_at_A038=row['terminal_height_at_core_A038'])))

if __name__=='__main__':main()
