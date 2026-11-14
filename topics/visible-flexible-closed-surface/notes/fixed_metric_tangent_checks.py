#!/usr/bin/env python3
"""Analytic tangent-angle Jacobian and profile-chart checks."""
import os
for n in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):os.environ[n]='1'
import argparse,json,sys
from pathlib import Path
import numpy as np
p=argparse.ArgumentParser();p.add_argument('--source-root',type=Path,required=True);p.add_argument('--out',type=Path,required=True);a=p.parse_args()
sys.path.insert(0,str(a.source_root/'topics/large-amplitude-twist-flex/scripts'))
from fixed_metric_mode3_tangent_core import PlanarTangentCore
from fixed_metric_mode3_bvp import SupportBVP
here=Path(__file__).parent
c=np.array([.04,.01,-.001,.0001]);theta=2*np.pi*np.arange(1024)/1024
core=PlanarTangentCore(c[0],c[1:]);analytic=core.parameter_derivatives(theta);err=[];step=1e-6
for j in range(len(c)):
 d=np.zeros_like(c);d[j]=step
 def F(v):return PlanarTangentCore(v[0],v[1:]).evaluate(theta)['F']
 numerical=(-F(c+2*d)+8*F(c+d)-8*F(c-d)+F(c-2*d))/(12*step)
 err.append(float(abs(numerical-analytic[j]).max()))
g=core.evaluate(theta);phi,kappa=core.angle(theta);jerr=[]
for j,(_,freq,coef) in enumerate(core.parameter_coefficient_derivatives(),start=1):
 derivative=core._evaluate_coefficients(theta,freq,1j*freq*coef)
 scale=core.primary_to_angle if j==1 else 1
 direct=-np.exp(1j*phi)*np.sin(3*j*theta)*scale
 jerr.append(float(abs(derivative-direct).max()))
first=core._evaluate_coefficients(theta,core.coordinate_frequencies,1j*core.coordinate_frequencies*core.coordinate_coefficients)
second=core._evaluate_coefficients(theta,core.coordinate_frequencies,-core.coordinate_frequencies**2*core.coordinate_coefficients)
closed=core.evaluate(np.array([0.,2*np.pi]))['F']
port=json.loads((here/'fixed_metric_mode3_p160_linear_port.json').read_text());cfg=json.loads((here/'fixed_metric_mode3_design_profile.json').read_text());bvp=SupportBVP(cfg,port,.01,4,128,3,False,'tangent');chart=[]
for factor in [.8,.9,1.,1.1,1.8]:
 p0=cfg['delta']*(factor-1);t=np.unique(np.r_[np.linspace(0,1,300),bvp.chart_breaks]);s,ds=bvp.chart(t,p0);back=bvp.inverse_chart(s,p0)
 chart.append(dict(delta_factor=factor,inverse_error=float(abs(t-back).max()),minimum_ds=float(ds.min()),maximum_ds=float(ds.max()),end_error=float(abs(s[-1]-bvp.flow(p0).end))))
out=dict(scope=__doc__,parameter_fd_errors=err,parameter_fd_step=step,parameter_theta_derivative_errors=jerr,
    series_first_jet_error=float(abs(first-1j*np.exp(1j*phi)).max()),series_second_jet_error=float(abs(second+kappa*np.exp(1j*phi)).max()),
    closure_error=float(np.linalg.norm(closed[1]-closed[0])),chart=chart)
a.out.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
