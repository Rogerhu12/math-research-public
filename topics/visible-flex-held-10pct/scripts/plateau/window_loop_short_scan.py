"""Screen only post-H loop controls; no nonlinear or continuous certificates."""
import os
for name in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):os.environ[name]='1'
import argparse,itertools,json,time
from pathlib import Path
import numpy as np
from scipy.optimize import brentq
from consumed_window_loop import ConsumedWindowLoop,linear_residual,sampled_geometry

p=argparse.ArgumentParser(description=__doc__);p.add_argument('--out',type=Path,required=True)
p.add_argument('--port-file',type=Path,required=True);a=p.parse_args()
port=json.loads(a.port_file.read_text());roots=[];near=[];began=time.time();cases=0
for ret,stop,L in itertools.product([.60,.65,.70,.75,.80],[-.20,-.10,0.,.10],[.28,.32,.36,.40,.44]):
    previous=None;acmax=min(7.5,8.2*np.sqrt(1-ret*ret));turn=min(5.5,8.0*np.sqrt(1-ret*ret))
    for ac in np.linspace(.6,acmax,7):
        cfg=dict(return_speed=ret,stop_speed=stop,stop_acceleration=ac,final_length=L,turn_acceleration=turn)
        try:
            f=ConsumedWindowLoop(**cfg);geo=sampled_geometry(f)
            if geo['background_kappa']>8.3 or geo['background_root_min']<.02:continue
            val=float(linear_residual(f,port)[0]);near.append(dict(parameters=cfg,residual=val,**geo))
            if previous and previous[1]*val<0:
                root=brentq(lambda z:linear_residual(ConsumedWindowLoop(**{**cfg,'stop_acceleration':z}),port)[0],previous[0],ac,xtol=1e-10)
                fp=ConsumedWindowLoop(**{**cfg,'stop_acceleration':root});row=dict(parameters=fp.parameters,residual=linear_residual(fp,port,4).tolist(),**sampled_geometry(fp));roots.append(row)
                print(json.dumps(dict(event='root',**row)),flush=True)
            previous=(ac,val)
        except (ValueError,RuntimeError,FloatingPointError):previous=None
    cases+=1
    a.out.write_text(json.dumps(dict(scope=__doc__,roots=roots,near=sorted(near,key=lambda x:abs(x['residual']))[:12],cases=cases,seconds=time.time()-began),indent=2)+'\n')
print(json.dumps(dict(event='complete',cases=cases,roots=len(roots),seconds=time.time()-began)),flush=True)
