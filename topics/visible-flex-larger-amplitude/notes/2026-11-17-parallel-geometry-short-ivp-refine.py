#!/usr/bin/env python3
"""Zero-lift the true M112 cut and perform only a higher-M short finite IVP.

The scalar evaluator and original core rho stay fixed.  Initial derivative
jets change with M; no complete BVP or C2 join to the M112 prefix is claimed.
"""
import argparse,gzip,hashlib,importlib.util,json
from pathlib import Path
import numpy as np
from scipy.integrate import DOP853

BASE=Path(__file__).with_name('2026-11-17-parallel-geometry-terminal-target-probe.py')
spec=importlib.util.spec_from_file_location('frozen_target_probe',BASE)
base=importlib.util.module_from_spec(spec);spec.loader.exec_module(base)
h=base.h


def integrate(q,profile,start,end,y,rtol,atol,max_step=None):
    def rhs(t,state):
        a,ap,_=profile(float(t));return q.rhs(state,ap/a)
    options={} if max_step is None else dict(max_step=max_step,first_step=min(max_step,end-start))
    try:
        solver=DOP853(rhs,start,y,end,rtol=rtol,atol=atol,**options)
    except FloatingPointError as error:
        return dict(ivp_reached_end=False,last_accepted_time=start,
            domain_evaluation_error=str(error),accepted_nodes=1,
            failure_stage='initial_step_selection'),y
    count=1
    while solver.status=='running':
        last_t=float(solver.t);last_y=solver.y.copy()
        try:
            message=solver.step()
        except FloatingPointError as error:
            return dict(ivp_reached_end=False,last_accepted_time=last_t,
                domain_evaluation_error=str(error),accepted_nodes=count,nfev=solver.nfev),last_y
        count+=1
    return dict(ivp_reached_end=solver.status=='finished',status=solver.status,
        message=message,last_accepted_time=float(solver.t),accepted_nodes=count,nfev=solver.nfev),solver.y


def main(args):
    ref=json.loads(gzip.decompress(args.reference.read_bytes()))
    metric=json.loads(gzip.decompress(args.metric.read_bytes()))
    if not ref.get('success') or not metric.get('inward_scalar_profile'):
        raise ValueError('Need accepted original cut and an explicit inward metric')
    profile=h.profile_from(metric);start=float(ref['mesh'][-1]);end=args.end
    old=h.Frenet(ref['M'],ref['N']);old_y=np.asarray(ref['states'][-1])
    a,ap,app=profile(start);k=ap/a;kp=app/a-k*k
    old_v=old.rhs(old_y,k);old_acc=old.jvp(old_y,k,old_v,dk=kp)
    out=dict(scope=__doc__,source_sha256=h.sha(__file__),base_sha256=h.sha(BASE),
        reference_sha256=h.sha(args.reference),metric_sha256=h.sha(args.metric),
        start=start,end=end,N=args.angles,read_angles=args.read_angles,
        integration_max_step=args.max_step,
        fixed_original_core_rho=True,valid_new_BVP_parent=False,resolutions=[])
    for M in args.modes:
        q=h.Frenet(M,args.angles);reader=h.Frenet(M,args.read_angles)
        y=base.lift_states(old_y,old.M,M)
        core=np.pad(np.asarray(ref['core']['coefficients']),(0,M-old.M))
        v=q.rhs(y,k);acc=q.jvp(y,k,v,dk=kp)
        dv=v-base.lift_states(old_v,old.M,M)
        da=acc-base.lift_states(old_acc,old.M,M)
        dv_field=reader.jet(dv)[0];da_field=reader.jet(da)[0]
        record=dict(M=M,dimension=q.n,initial_value_difference=0.,
            initial_velocity_coefficient_difference_max=float(np.max(abs(dv))),
            initial_velocity_field_difference_max=float(np.max(np.linalg.norm(dv_field,axis=1))),
            initial_acceleration_field_difference_max=float(np.max(np.linalg.norm(da_field,axis=1))),
            initial_RHS_gram=base.gram(reader,y,v,a,core),runs=[])
        endpoints=[]
        for rtol,atol in [(1e-12,1e-15),(1e-13,1e-16)]:
            report,last=integrate(q,profile,start,end,y,rtol,atol,args.max_step)
            report.update(rtol=rtol,atol=atol)
            if report['ivp_reached_end']:
                ae,ape,_=profile(end);vel=q.rhs(last,ape/ae)
                local=q.local(last,ape/ae)
                report.update(endpoint_RHS_gram=base.gram(reader,last,vel,ae,core),
                    endpoint_sample_Q_min=float(local['Q'].min()),
                    endpoint_sample_W_min=float(local['W'].min()),
                    endpoint_sample_H_min=float(local['H'].min()),
                    endpoint_coefficients=last.tolist())
                endpoints.append(last)
            record['runs'].append(report)
            print(json.dumps(dict(M=M,**{k:v for k,v in report.items() if k!='endpoint_coefficients'})),flush=True)
        if len(endpoints)==2:
            record['two_tolerance_endpoint_coefficient_difference_max']=float(np.max(abs(endpoints[1]-endpoints[0])))
        out['resolutions'].append(record)
    args.out.write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(dict(output=str(args.out),sha256=h.sha(args.out))),flush=True)


if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--reference',type=Path,required=True)
    p.add_argument('--metric',type=Path,required=True)
    p.add_argument('--out',type=Path,required=True)
    p.add_argument('--modes',nargs='+',type=int,default=[160,224])
    p.add_argument('--angles',type=int,default=2048)
    p.add_argument('--read-angles',type=int,default=8192)
    p.add_argument('--end',type=float,default=.997)
    p.add_argument('--max-step',type=float)
    main(p.parse_args())
