#!/usr/bin/env python3
"""Search smooth m=2/m=4 double linear resonance, without asserting closure.

This solves two linear matching conditions with two meridian design controls.
It does not prove a multiple-kernel nonlinear bifurcation or a closed surface.
"""
import argparse
import json
import time
from pathlib import Path
import numpy as np
from scipy.optimize import brentq
from root_profile_scan import Bridge, Design, parse_port


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--port',type=Path,required=True)
    parser.add_argument('--out',type=Path,required=True)
    parser.add_argument('--vu',type=float,nargs='+',default=[.3,.45,.55,.65,.75])
    parser.add_argument('--ramp',type=float,default=.4)
    a=parser.parse_args()
    port=json.loads(a.port.read_text())
    b2=Bridge(*parse_port(port,2)[:1],2,parse_port(port,2)[1])
    b4=Bridge(*parse_port(port,4)[:1],4,parse_port(port,4)[1])
    report=dict(scope=__doc__,rows=[])
    start=time.time()
    for vu in a.vu:
        cache={}
        def at(vd):
            vd=float(vd)
            if vd in cache:return cache[vd]
            cfg=dict(direction='outward',vu=vu,vd=vd,ramp=a.ramp,ramp_eta=.05,cycles=1)
            def mode2(delta):
                return float(Design({**cfg,'delta':delta},b2).core_line(rtol=2e-12)[0][1])
            ds=np.linspace(.03,.4,13)
            old=ds[0],mode2(ds[0]);bracket=None
            for delta in ds[1:]:
                v=mode2(delta)
                if old[1]*v<0:
                    bracket=(old[0],delta);break
                old=delta,v
            if bracket is None:raise ValueError('No first m2 root in the search window')
            delta=brentq(mode2,*bracket,xtol=8e-15,rtol=8e-15)
            cfg['delta']=delta
            y4=Design(cfg,b4).core_line(rtol=2e-12)[0]
            cache[vd]=(cfg,float(y4[1]),float(y4[0]))
            return cache[vd]
        probes=[];roots=[];last=None
        for vd in [.12,.18,.25,.32,.4,.48,.56,.65,.75,.85]:
            cfg,g,f=at(vd);probes.append(dict(vd=vd,delta=cfg['delta'],g4=g,f4=f))
            if last is not None and last[1]*g<0:
                vroot=brentq(lambda v:at(v)[1],last[0],vd,xtol=2e-12,rtol=2e-12)
                cfg,gg,ff=at(vroot)
                y2=Design(cfg,b2).core_line(rtol=4e-13)[0]
                y4=Design(cfg,b4).core_line(rtol=4e-13)[0]
                summary=Design(cfg,b2).summary()
                roots.append(dict(config=cfg,root_residual_g4=gg,
                  tighter_mode2_core=y2.tolist(),tighter_mode4_core=y4.tolist(),
                  background_height=summary['background_height'],
                  meridian_length=summary['meridian_length'],
                  background_kappa_sample=summary['background_kappa_sample'],
                  accepted_linear_diagnostic=bool(max(abs(y2[1]),abs(y4[1]))<1e-5)))
            last=vd,g
        row=dict(vu=vu,ramp=a.ramp,probes=probes,roots=roots)
        report['rows'].append(row);report['seconds']=time.time()-start
        a.out.parent.mkdir(parents=True,exist_ok=True)
        a.out.write_text(json.dumps(report,indent=2)+'\n')
        print(json.dumps(dict(vu=vu,roots=roots,seconds=report['seconds'])),flush=True)


if __name__=='__main__':main()
