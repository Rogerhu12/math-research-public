#!/usr/bin/env python3
"""Regenerate the numerical angle chart from a frozen scalar m3 profile.
The 65 chart samples and finite DN arrays are generated in scratch only.
"""
import os
for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):os.environ[k]='1'
import argparse,importlib.util,json,math
from pathlib import Path
import numpy as np
p=argparse.ArgumentParser(description=__doc__)
for k in ('source-topic','short-bridge','profile','port','out'):p.add_argument('--'+k,type=Path,required=True)
a=p.parse_args()
def module(name,path):
 s=importlib.util.spec_from_file_location(name,path);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
ad=module('m3_reference_adaptive',a.source_topic/'scripts/950f-prefix-adaptive-chart-bvp-v2.py');module('m3_reference_flat',a.source_topic/'scripts/db6f-prefix-flat-profile.py').install(ad);ad.old.install_source(a.source_topic/'repro/source-root');module('m3_reference_short',a.short_bridge).install()
cfg=json.loads(a.profile.read_text());port=json.loads(a.port.read_text());port['cut']['_prefix_bridge']=cfg['prefix_bridge']
if port['modes']!=list(3*np.arange(1,len(port['modes'])+1)):raise ValueError('Physical base mode must be 3')
Flow,_=ad.build_classes(dict(knots=[0.,1.],values=[1.,1.],final_derivative=0.));f=Flow(cfg,port,4,.02,128,3);line=f.backward_line()
x=np.linspace(0,1,65);s=x*f.end;fg=np.empty((2,len(s)))
for j,(lo,hi,sol,scale)in enumerate(line.segments):
 mask=(s>=lo)&((s<hi)if j+1<len(line.segments)else(s<=hi))
 if np.any(mask):fg[:,mask]=sol(s[mask])*math.exp(scale-line.logscale)/line.core[0]
ar,ap,_=f.profile(s);h=fg[0]/ar;rhs=f.linear_rhs(f.end,fg[:,-1]);hp=(rhs[0]*ar[-1]-fg[0,-1]*ap[-1])/ar[-1]**2*f.end
chart=dict(scope='Normalized linear m3 f/a; numerical chart only, frozen when used in one design.',reference_profile=cfg,knots=x.tolist(),values=h.tolist(),final_derivative=float(hp))
a.out.mkdir(parents=True,exist_ok=True)
for name,data in [('profile',cfg),('port',port),('chart',chart)]: (a.out/(name+'.json')).write_text(json.dumps(data,indent=2)+'\n')
print(json.dumps(dict(out=str(a.out),height_first_mode_per_q=float(fg[1,-1]),core_transversality=float(line.core[1]))))
