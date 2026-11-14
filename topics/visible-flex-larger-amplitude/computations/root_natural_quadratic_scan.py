#!/usr/bin/env python3
"""Measure the actual small-amplitude natural cos(4 phi) coefficient.

This scans design parameters and solves finite linear-DN prefixes. It does
not freeze a common metric, close a surface, or solve the nonlinear tail.
"""
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[key]='1'
import argparse,importlib.util,json,subprocess,sys,time
from pathlib import Path
import numpy as np
from scipy.optimize import brentq
HERE=Path(__file__).resolve().parent

def main():
    p=argparse.ArgumentParser(description=__doc__)
    for key in ('source-topic','port','out-prefix'):
        p.add_argument('--'+key,type=Path,required=True)
    p.add_argument('--vd',type=float,nargs='+',default=[.35,.4,.42,.47])
    p.add_argument('--vu',type=float,default=.55)
    p.add_argument('--q',type=float,default=.02)
    a=p.parse_args();a.out_prefix.parent.mkdir(parents=True,exist_ok=True)
    spec=importlib.util.spec_from_file_location('root_natural_linear',HERE/'root_profile_scan.py')
    design=importlib.util.module_from_spec(spec);spec.loader.exec_module(design)
    port=json.loads(a.port.read_text());cut,slope=design.parse_port(port,2)
    bridge=design.Bridge(cut,2,slope)
    chart=a.out_prefix.with_name(a.out_prefix.name+'-chart.json')
    chart.write_text(json.dumps(dict(knots=[0.,1.],values=[1.,1.],final_derivative=0.))+'\n')
    report=dict(scope=__doc__,q=a.q,vu=a.vu,rows=[])
    def save():a.out_prefix.with_suffix('.json').write_text(json.dumps(report,indent=2)+'\n')
    for vd in a.vd:
        started=time.time();stem=a.out_prefix.with_name(a.out_prefix.name+f'-vd{vd:.3f}'.replace('.','p'))
        cfg=dict(direction='outward',vu=a.vu,vd=vd,delta=.15,ramp=.4,ramp_eta=.05,ramp_law='flat',cycles=1)
        def residual(delta):return design.Design({**cfg,'delta':delta},bridge).core_line(rtol=2e-10)[0][1]
        grid=np.linspace(.07,.27,31);rv=[residual(x)for x in grid]
        roots=[brentq(residual,x,y,xtol=2e-11)for x,y,fx,fy in zip(grid[:-1],grid[1:],rv[:-1],rv[1:])if fx*fy<0]
        if not roots:
            report['rows'].append(dict(vd=vd,linear_roots=[],status='No root in stated interval'))
            save();continue
        cfg['delta']=min(roots,key=lambda x:abs(x-.16))
        profile=stem.with_name(stem.name+'-profile.json');profile.write_text(json.dumps(cfg,indent=2)+'\n')
        cmd=[sys.executable,str(HERE/'numerical-m2-prefix.py'),'--source-topic',str(a.source_topic),
             '--profile',str(profile),'--chart',str(chart),'--port',str(a.port),
             '--amplitude',str(a.q),'--warp-reference',str(a.q),'--modes','6',
             '--angular','160','--tol','1e-6','--max-nodes','1800','--out-prefix',str(stem)]
        run=subprocess.run(cmd,capture_output=True,text=True)
        row=dict(vd=vd,linear_roots=roots,returncode=run.returncode,seconds=time.time()-started)
        summary=stem.with_name(stem.name+'-summary.json')
        if summary.exists():
            r=json.loads(summary.read_text());row.update(solver_success=r.get('solver_success',False),error=r.get('error'))
            if r.get('solver_success'):
                core=r['summary']['core'];row.update(q4=core['coefficients'][1],q4_over_q2=core['coefficients'][1]/a.q**2,
                    delta=r['frozen_profile']['delta'],metric_l1=r['summary']['metric_l1'],
                    height=r['summary']['height_max'],kappa=r['summary']['kappa_sample'])
        else:row['stderr_tail']=run.stderr[-1000:]
        report['rows'].append(row);save();print(json.dumps(row),flush=True)

if __name__=='__main__':main()
