#!/usr/bin/env python3
"""Linear physical-mode transversality at a planar core; diagnostic only."""
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[key]='1'
import argparse
import json
import math
from pathlib import Path
import sys
import numpy as np


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source-root',type=Path,required=True)
    parser.add_argument('--config',type=Path,required=True)
    parser.add_argument('--out',type=Path,required=True)
    args=parser.parse_args()
    sys.path.insert(0,str(args.source_root/'topics/large-amplitude-twist-flex/scripts'))
    from f6curve_outward_bridge_linear import read_port,BackwardLine
    from repo_scan_gentle import scaled_port
    from repo_scan_ellipse_line import CycleBridgeProfile
    cfg=json.loads(args.config.read_text())
    source=read_port(args.source_root/'topics/large-amplitude-twist-flex/notes/f6curve_wide_m2_r2_m16_linear_port.json')
    port=scaled_port(source,cfg['cut_radius'],cfg['cut_slope'])
    profile=CycleBridgeProfile(cfg,port)
    rows=[]
    for index,D in enumerate(port['linearSlope']):
        m=2*(index+1);r=port['cut']['radius'];w=port['cut']['backgroundSlope']
        terminal=[profile.bridge.sigma*w*(r*D-m*m)/(m*m-1),1.]
        def rhs(s,y):
            a,v,_=profile.profile(np.array([s]));a=float(a[0]);v=float(v[0]);b=math.sqrt(1-v*v)
            return np.array([-(m*m-1)*v*y[0]-m*m*b*y[1],
                             (m*m-1)*v*v*y[0]/b+m*m*v*y[1]])/a
        line=BackwardLine(rhs,profile.breaks,terminal)
        rows.append(dict(mode=m,unit_initial=line.core.tolist(),
            radial_planar_transversality=abs(float(line.core[1])),
            rho=float(line.rho),logscale=line.logscale))
    out=dict(scope=__doc__,config=cfg,rows=rows)
    args.out.write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out),flush=True)


if __name__=='__main__':
    main()
