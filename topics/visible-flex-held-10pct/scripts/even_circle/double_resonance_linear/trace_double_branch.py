"""Locate actual two-mode roots by continuation on the primary-root branch."""
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):os.environ[key]='1'
import argparse,json,time
from pathlib import Path
import numpy as np
from scipy.optimize import brentq
from physical_linear_design import PhysicalDesign,geometry


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--source-root',type=Path,required=True);p.add_argument('--port',type=Path,required=True)
    p.add_argument('--out',type=Path,required=True)
    args=p.parse_args();args.out.mkdir(parents=True,exist_ok=True);start=time.monotonic()
    design=PhysicalDesign(args.source_root,args.port)
    common=dict(direction='outward',ramp_eta=.05,ramp_law='flat',cycles=1,
        prefix_bridge=dict(kind='turn_plateau_v1',curvature=4.,peak_fraction=.2))
    report=dict(scope=__doc__,provenance=design.provenance,cases=[],roots=[])
    for vu,eps in ((.2,.4),(.2,.45),(.3,.45),(.4,.45),(.17,.45),(.25,.45)):
        cfg=dict(common,vu=vu,ramp=eps);cache={};probes=[]
        def on_primary(vd,rtol=2e-10):
            key=(float(vd),rtol)
            if key in cache:return cache[key]
            c=dict(cfg,vd=float(vd))
            def first(delta):return float(design.linear(dict(c,delta=float(delta)),2,rtol)['core'][0,1])
            delta=brentq(first,.015,.07,xtol=2e-13)
            c['delta']=delta;lin=design.linear(c,2,rtol)
            value=dict(profile=c,tau=lin['core'][:,1].tolist(),core=lin['core'].tolist(),logs=lin['logs'].tolist())
            cache[key]=value;return value
        previous=None;brackets=[]
        for vd in (.08,.12,.15,.18,.19,.20,.21,.23,.26,.30,.36,.45,.55):
            try:
                row=on_primary(vd);probes.append(row);val=row['tau'][1]
                if previous is not None and previous[1]*val<0:brackets.append((previous[0],vd))
                previous=(vd,val)
            except Exception as exc:probes.append(dict(vd=vd,error=repr(exc)));previous=None
        case=dict(vu=vu,ramp=eps,probes=probes,brackets=brackets);report['cases'].append(case)
        for lo,hi in brackets:
            vd=brentq(lambda x:on_primary(x)['tau'][1],lo,hi,xtol=2e-13)
            # Re-match both equations with a stricter physical integration.
            near=(max(lo,vd-.001),min(hi,vd+.001))
            vd=brentq(lambda x:on_primary(x,2e-12)['tau'][1],*near,xtol=1e-14)
            candidate=on_primary(vd,2e-12);c=candidate['profile']
            lin=design.linear(c,24,rtol=2e-12)
            check=design.linear(c,24,rtol=2e-13)
            geo=geometry(design.profile(c));record=dict(profile=c,physical_modes=design.port['modes'],
                tau=check['core'][:,1].tolist(),H_per_unit_core_support=check['H_per_unit_core_support'].tolist(),
                rtol_2e12_to_2e13_tau_difference=float(abs(lin['core'][:,1]-check['core'][:,1]).max()),
                primary_pair_max=float(abs(check['core'][:2,1]).max()),geometry=geo,
                accepted_finite_linear_double_root=bool(abs(check['core'][:2,1]).max()<1e-7))
            index=len(report['roots']);report['roots'].append(record)
            (args.out/f'root-{index:02d}-profile.json').write_text(json.dumps(c,indent=2)+'\n')
            print(json.dumps(dict(event='double_root',index=index,profile=c,tau_first6=record['tau'][:6],
                H_first6=record['H_per_unit_core_support'][:6],precision_difference=record['rtol_2e12_to_2e13_tau_difference'],geometry=geo)),flush=True)
        report['elapsed_seconds']=time.monotonic()-start
        (args.out/'summary.json').write_text(json.dumps(report,indent=2)+'\n')
        print(json.dumps(dict(event='case',vu=vu,ramp=eps,brackets=len(brackets),roots=len(report['roots']),elapsed=report['elapsed_seconds'])),flush=True)


if __name__=='__main__':main()
