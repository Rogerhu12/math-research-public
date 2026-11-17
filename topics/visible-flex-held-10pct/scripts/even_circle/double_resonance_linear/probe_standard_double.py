"""Finite two-mode resonance search in literal flat-loop physical profiles."""
import os
for name in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):os.environ[name]='1'
import argparse,json,time
from pathlib import Path
import numpy as np
from scipy.optimize import least_squares
from physical_linear_design import PhysicalDesign,geometry


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--source-root',type=Path,required=True)
    p.add_argument('--port',type=Path,required=True)
    p.add_argument('--out',type=Path,required=True)
    a=p.parse_args();a.out.mkdir(parents=True,exist_ok=True)
    design=PhysicalDesign(a.source_root,a.port);start=time.monotonic()
    common=dict(direction='outward',ramp=.45,ramp_eta=.05,cycles=1,
                prefix_bridge=dict(kind='turn_plateau_v1',curvature=4.,peak_fraction=.2))
    baseline=dict(common,vu=.4,vd=.4,delta=.030150157904596426)
    r0=design.linear(baseline,6);jac=np.zeros((2,2))
    for k,(name,h)in enumerate((('delta',1e-6),('vd',1e-4))):
        plus=dict(baseline);minus=dict(baseline);plus[name]+=h;minus[name]-=h
        jac[:,k]=(design.linear(plus,2)['core'][:,1]-design.linear(minus,2)['core'][:,1])/(2*h)
    report=dict(scope=__doc__,provenance=design.provenance,
        baseline=dict(profile=baseline,tau=r0['core'][:,1].tolist(),jacobian_delta_vd=jac.tolist(),
            linear_Newton_step=np.linalg.solve(jac,-r0['core'][:2,1]).tolist(),geometry=geometry(design.profile(baseline))),rows=[])
    print(json.dumps(dict(event='baseline',**report['baseline'])),flush=True)
    for vu,eps,seed in ((.4,.45,(.03015,.4)),(.3,.45,(.03,.4)),(.5,.45,(.04,.5)),(.4,.35,(.03,.4))):
        cfg=dict(common,vu=vu,ramp=eps);trace=[]
        def residual(x):
            candidate=dict(cfg,delta=float(x[0]),vd=float(x[1]));r=design.linear(candidate,2)['core'][:,1]
            trace.append(dict(delta=float(x[0]),vd=float(x[1]),tau=r.tolist()))
            return r
        sol=least_squares(residual,seed,bounds=([.003,.08],[.2,.9]),x_scale=[.03,.4],diff_step=2e-5,
                          ftol=2e-10,xtol=2e-10,gtol=2e-10,max_nfev=70)
        config=dict(cfg,delta=float(sol.x[0]),vd=float(sol.x[1]));lin=design.linear(config,8,rtol=2e-11)
        geo=geometry(design.profile(config));success=bool(abs(lin['core'][:2,1]).max()<1e-7)
        record=dict(profile=config,optimizer_status=int(sol.status),optimizer_message=sol.message,nfev=sol.nfev,
                    accepted_linear_double_root=success,tau=lin['core'][:,1].tolist(),
                    H_per_q=lin['H_per_unit_core_support'].tolist(),geometry=geo,
                    sampled_background_budget_pass=bool(geo['sample_ball_D_with_nominal_tail']<=2.5 and geo['elementary_background_curvature_upper']<=13.2 and geo['characteristic_window_consumed_elementary']),trace=trace)
        report['rows'].append(record);report['elapsed_seconds']=time.monotonic()-start
        (a.out/'summary.json').write_text(json.dumps(report,indent=2)+'\n')
        print(json.dumps(dict(event='completed_design',**{k:v for k,v in record.items()if k!='trace'})),flush=True)
    print(json.dumps(dict(event='complete',elapsed_seconds=time.monotonic()-start)),flush=True)


if __name__=='__main__':main()
