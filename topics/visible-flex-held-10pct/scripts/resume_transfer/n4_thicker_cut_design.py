#!/usr/bin/env python3
"""Actual double-root design for a newly generated, thicker physical tail cut.

The port must come from the original worker under the new physical metric.
No nonlinear embedding or finite-amplitude geometry is established here.
"""
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[key]='1'
import argparse, hashlib, json, sys, time
from pathlib import Path
import numpy as np
from scipy.optimize import root
HERE=Path(__file__).resolve().parent
sys.path[:0]=[str(HERE.parent/'even_circle/double_resonance_linear'),str(HERE.parent/'resume_n4')]
from physical_linear_design import PhysicalDesign, geometry
from linear_profile_amplification import amplification

def main():
    p=argparse.ArgumentParser(description=__doc__)
    for name in ('source-root','port','profile','out'):
        p.add_argument('--'+name,type=Path,required=True)
    p.add_argument('--circle-radius',type=float,default=1.882)
    p.add_argument('--peaks',type=float,nargs='+',default=[.2,.01])
    a=p.parse_args();a.out.mkdir(parents=True,exist_ok=True)
    design=PhysicalDesign(a.source_root,a.port)
    base=json.loads(a.profile.read_text());rows=[];started=time.monotonic()
    report=dict(scope=__doc__,argv=sys.argv,source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                dependencies=design.provenance,input_profile_sha256=hashlib.sha256(a.profile.read_bytes()).hexdigest(),
                amplification_source_sha256=hashlib.sha256((HERE.parent/'resume_n4/linear_profile_amplification.py').read_bytes()).hexdigest(),rows=rows)
    for peak in a.peaks:
        cfg={**base,'prefix_bridge':{**base['prefix_bridge'],'peak_fraction':peak}}
        trace=[]
        def residual(x):
            test={**cfg,'delta':float(x[0]),'vd':float(x[1])}
            values=design.linear(test,2,2e-11)['core'][:,1]
            trace.append(dict(delta=test['delta'],vd=test['vd'],tau=values.tolist()))
            return values
        row=dict(peak_fraction=peak,trace=trace)
        try:
            solved=root(residual,[cfg['delta'],cfg['vd']],tol=2e-10)
            chosen={**cfg,'delta':float(solved.x[0]),'vd':float(solved.x[1])}
            linear=design.linear(chosen,12,2e-12)
            row.update(profile=chosen,optimizer_success=bool(solved.success),optimizer_message=str(solved.message),
                       tau=linear['core'][:,1].tolist(),H_per_unit_core_support=linear['H_per_unit_core_support'].tolist(),
                       double_root=bool(np.max(abs(linear['core'][:2,1]))<1e-7))
            physical=design.profile(chosen)
            row['background']=geometry(physical,circle_radius=a.circle_radius,halfwidth=.147,cylinder_length=.54,nominal_tail_rise=.05)
            row['background']['assumed_circle_radius']=a.circle_radius
            row['background']['scope']='Actual new round background samples and characteristic-window diagnostics. Tail rise .05 is a nominal budget, not an enclosure. No full candidate diameter/reach claim.'
            if row['double_root']:
                row['along_rows']=amplification(design,chosen)['rows']
                (a.out/f'peak{peak:g}-profile.json').write_text(json.dumps(chosen,indent=2)+'\n')
        except Exception as exc:
            row.update(double_root=False,error=repr(exc))
        rows.append(row);report['seconds']=time.monotonic()-started
        (a.out/'summary.json').write_text(json.dumps(report,indent=2)+'\n')
        print(json.dumps({k:v for k,v in row.items()if k!='trace'}),flush=True)

if __name__=='__main__':
    main()
