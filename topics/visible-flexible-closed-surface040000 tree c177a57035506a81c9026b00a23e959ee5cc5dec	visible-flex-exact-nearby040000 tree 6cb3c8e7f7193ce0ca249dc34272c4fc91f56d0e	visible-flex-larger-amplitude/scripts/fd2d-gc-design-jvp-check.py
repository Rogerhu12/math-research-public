#!/usr/bin/env python3
"""Small actual check of the smooth T chart and its Codazzi parameter JVP."""
import os
for _key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[_key]='1'
import argparse,json
from pathlib import Path
import numpy as np
from fd2d_gc_intrinsic import FixedNormalReference,identity
from fd2d_balanced_oval_core import BalancedOvalCore
from fd2d_gc_design_profile import CoastDesignProfile
from fd2d_gc_design_flow import DesignLogShapeGC


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--candidate',type=Path,required=True);p.add_argument('--out',type=Path,required=True)
    a=p.parse_args()
    if a.out.exists():raise FileExistsError('Use a new check path')
    profile=CoastDesignProfile(a.candidate);flow=DesignLogShapeGC(profile,31,2,reference=FixedNormalReference(BalancedOvalCore()))
    y=np.zeros(flow.dimension);y[0]=.001;y[1]=.004;y[3]=-.001;y[flow.K+1]=.002
    direction=np.cos(np.arange(flow.dimension)*1.31)/(1+np.arange(flow.dimension));direction/=np.linalg.norm(direction)
    rows=[];T=profile.T
    for index in [profile.model.shallow,profile.model.down,profile.model.deep,profile.model.brake]:
        piece=profile.base.segments[index];x=piece['s0']+.37*piece['L']
        native=flow.jvp(x,y,direction);parameter=flow.parameter_derivative(x,y);checks=[]
        for step in [1e-4,1e-5,1e-6]:
            state_fd=(flow.rhs(x,y+step*direction)-flow.rhs(x,y-step*direction))/(2*step)
            profile.set_parameter(T+step);plus=flow.rhs(x,y)
            profile.set_parameter(T-step);minus=flow.rhs(x,y)
            profile.set_parameter(T);fd=(plus-minus)/(2*step)
            checks.append(dict(step=step,state_jvp_relative_l2=float(np.linalg.norm(state_fd-native)/np.linalg.norm(native)),
                parameter_jvp_absolute_maximum=float(abs(fd-parameter).max()),
                parameter_jvp_relative_l2=float(np.linalg.norm(fd-parameter)/max(1e-300,np.linalg.norm(parameter)))))
        rows.append(dict(piece=int(index),x=float(x),checks=checks))
    sample=np.unique(np.r_[profile.breaks,(profile.breaks[:-1]+profile.breaks[1:])/2])
    background=flow.rhs(sample,np.zeros((flow.dimension,len(sample))))
    report=dict(schema='fd2d-smooth-coast-T-Codazzi-JVP-check-v1',scope=__doc__,candidate=identity(a.candidate),
        source=identity(__file__),profile_source=identity(Path(__file__).with_name('fd2d_gc_design_profile.py')),
        flow_source=identity(Path(__file__).with_name('fd2d_gc_design_flow.py')),radial_chart=profile.definition(),
        exact_rotational_rhs_maximum=float(abs(background).max()),rows=rows,BVP_solved=False)
    a.out.write_text(json.dumps(report,indent=2,allow_nan=False)+'\n');print(json.dumps(report,allow_nan=False),flush=True)


if __name__=='__main__':main()
