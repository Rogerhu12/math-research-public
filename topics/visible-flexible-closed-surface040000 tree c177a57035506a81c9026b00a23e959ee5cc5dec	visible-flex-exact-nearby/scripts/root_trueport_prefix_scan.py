#!/usr/bin/env python3
"""Screen physical linear prefixes against a newly computed tail DN.

Background geometry and first-order amplitude only. No nonlinear annulus,
closed surface, or reach certificate is claimed. All failures are retained.
"""
import os
for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[k]='1'
import argparse
import json
import math
from pathlib import Path
import sys
import time
import numpy as np
from scipy.optimize import brentq


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--source-root',type=Path,required=True)
    p.add_argument('--ellipse-notes',type=Path,required=True)
    p.add_argument('--linear-port',type=Path,required=True)
    p.add_argument('--out',type=Path,required=True)
    a=p.parse_args()
    sys.path.insert(0,str(a.ellipse_notes))
    sys.path.insert(0,str(a.source_root/'topics/large-amplitude-twist-flex/scripts'))
    from repo_scan_ellipse_line import backward,describe
    data=json.loads(a.linear_port.read_text());r=data['config']['rCut'];w=data['config']['wCut']
    port={'cut':dict(radius=r,backgroundSlope=w,backgroundSecond=-7*w/r,E=1+w*w,Ep=-14*w*w/r),
          'linearSlope':[row['cutSlope'] for row in data['rows']]}
    tail_threshold=data['rows'][0].get('linearTPositivityAmplitudeThreshold')
    report={'scope':__doc__,'port':port,'input':str(a.linear_port),'tail_threshold':tail_threshold,'rows':[]}
    start=time.time()
    configs=[dict(direction='outward',vu=u,vd=v,ramp=.4,cycles=n,cut_radius=r,cut_slope=w)
        for u,v in [(0.25,.4),(.35,.5),(.5,.7),(.6,.8)] for n in [1,2,3,4,6]]
    grid=[.015,.03,.06,.1,.16,.24,.36,.54,.8]
    for cfg in configs:
        previous=None;roots=[];errors=[]
        for d in grid:
            try:
                prof,line=backward({**cfg,'delta':d},port);f=float(line.core[1])
                if previous and previous[1]*f<0:
                    root=brentq(lambda t:float(backward({**cfg,'delta':t},port)[1].core[1]),previous[0],d,xtol=2e-10)
                    row=describe({**cfg,'delta':root},port,verify=False)
                    # First-order q=.13 and ell=.26 are just comparison scales.
                    row['linear_terminal_height_q013']=.13*abs(row['physical_endpoint_gain'])
                    row['threshold_ratio']=row['linear_terminal_height_q013']/tail_threshold if tail_threshold else None
                    row['conditional_D_cylinder']=2*math.hypot(row['background_radius_max']+.14,row['background_height']+.26+.12)
                    row['conditional_background_kappaD']=row['background_kappa_max']*row['conditional_D_cylinder']
                    roots.append(row)
                previous=(d,f)
            except Exception as exc:
                errors.append({'delta':d,'error':repr(exc)});previous=None
        item={'config':cfg,'roots':roots,'errors':errors};report['rows'].append(item)
        report['elapsed_seconds']=time.time()-start
        a.out.write_text(json.dumps(report,indent=2)+'\n')
        print(json.dumps({'config':cfg,'roots':[{'delta':x['config']['delta'],
             'gain':x['physical_endpoint_gain'],'H':x['background_height'],'K':x['background_kappa_max'],
             'comparison_KD':x['conditional_background_kappaD'],'tail_ratio':x['threshold_ratio']} for x in roots],
             'errors':len(errors),'seconds':report['elapsed_seconds']}),flush=True)


if __name__=='__main__':main()
