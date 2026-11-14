#!/usr/bin/env python3
"""Independent formula/representation checks for the new planar mode3 flow.
No comparison of altered physical metrics is treated as convergence.
"""
import os
for n in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):os.environ[n]='1'
import argparse,json,sys
from pathlib import Path
import numpy as np
p=argparse.ArgumentParser();p.add_argument('--source-root',type=Path,required=True);p.add_argument('--out',type=Path,required=True);a=p.parse_args()
sys.path.insert(0,str(a.source_root/'topics/large-amplitude-twist-flex/scripts'))
from fixed_metric_mode3_core import PlanarSupportCore
from fixed_metric_mode3_flow import PlanarSymmetryFlow
from curve_stable_prefix_bvp import CylindricalPrefix
here=Path(__file__).parent
cfg=json.loads((here/'fixed_metric_mode3_design_profile.json').read_text());port=json.loads((here/'fixed_metric_mode3_p160_linear_port.json').read_text())
flow=PlanarSymmetryFlow(cfg,port,4,.001,128)
s=np.array([.003,.018,.07,.12,.21,.43,.6]);s=s[s<flow.end]
rng=np.random.default_rng(20261109);y=rng.normal(size=(flow.n,len(s)))*1e-5
# Compare to the inherited general Cartesian formula as an independent frame representation.
cart=CylindricalPrefix.fun(flow,s,y,np.zeros(flow.M));local=flow.fun(s,y,np.zeros(flow.M))
J=flow.fun_jac(s,y,np.zeros(flow.M))[0];v=rng.normal(size=y.shape)
actual=flow.fun(s,y.astype(complex)+1e-25j*v,np.zeros(flow.M)).imag/1e-25
pred=np.einsum('ijk,jk->ik',J,v)
zero=flow.fun(s,np.zeros_like(y),np.zeros(flow.M))
coef=np.array([.05,.0002,-.00005,.00001]);theta=2*np.pi*np.arange(1024)/1024
core=PlanarSupportCore(coef[0],coef[1:]);analytic=core.parameter_derivatives(theta);errors=[]
step=2e-7
for j in range(len(coef)):
 d=np.zeros_like(coef);d[j]=step
 def F(c):return PlanarSupportCore(c[0],c[1:]).evaluate(theta)['F']
 derivative=(-F(coef+2*d)+8*F(coef+d)-8*F(coef-d)+F(coef-2*d))/(12*step)
 errors.append(float(abs(derivative-analytic[j]).max()))
report=dict(scope=__doc__,flow_cartesian_local_max_abs=float(abs(cart-local).max()),state_jvp_max_abs=float(abs(actual-pred).max()),
    state_jvp_relative=float(abs(actual-pred).max()/max(1,abs(actual).max())),background_flow_nonmean=float(abs(zero[1:]).max()),
    background_flow_mean=float(abs(zero[0]).max()),core_parameter_fixed_theta_fd_errors=errors,core_fd_step=step,
    note='FD check independently reinverts the arc map at each perturbed coefficient; no normal-angle coordinate is held fixed.')
a.out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2))
