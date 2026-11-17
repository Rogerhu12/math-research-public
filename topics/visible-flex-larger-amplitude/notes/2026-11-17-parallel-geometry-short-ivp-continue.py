#!/usr/bin/env python3
"""Continue a genuine local IVP endpoint at unchanged M/N, scalar and rho.

Shared stored 0/1/2 jets define the local C2 seam.  This remains a local IVP
candidate, not an accepted complete-prefix BVP or a closed flexible surface.
"""
import argparse,gzip,hashlib,importlib.util,json
from pathlib import Path
import numpy as np
from scipy.integrate import DOP853

BASE=Path(__file__).with_name('2026-11-17-parallel-geometry-short-ivp-field.py')
spec=importlib.util.spec_from_file_location('frozen_local_field',BASE)
base=importlib.util.module_from_spec(spec);spec.loader.exec_module(base)
h=base.h


def main(args):
    parent=json.loads(gzip.decompress(args.input.read_bytes()))
    if not parent.get('ivp_reached_end') or not parent.get('original_core_coefficients'):
        raise ValueError('Need a genuine completed local IVP field with its original rho')
    q=h.Frenet(parent['M'],parent['N']);profile=h.profile_from(parent)
    start=float(parent['mesh'][-1]);initial=np.asarray(parent['states'][-1])
    old_v=np.asarray(parent['rhs'][-1]);old_acc=np.asarray(parent['d2'][-1])
    a,ap,app=profile(start);k=ap/a
    check_v=q.rhs(initial,k)
    check_acc=q.jvp(initial,k,check_v,dk=app/a-k*k)
    initial_checks=dict(first_coefficient_difference_max=float(np.max(abs(check_v-old_v))),
                        second_coefficient_difference_max=float(np.max(abs(check_acc-old_acc))),
                        first_bitwise_equal=bool(np.array_equal(check_v,old_v)),
                        second_bitwise_equal=bool(np.array_equal(check_acc,old_acc)))
    def domain(y,kk,qq=q):
        _,d,e=qq.jet(y);Q=np.sum(d*d,axis=1);W=np.sum(np.cross(d,e)**2,axis=1)
        H=W-kk*kk*Q**3;j=int(np.argmin(H));admissible=np.sqrt(W/Q**3)
        ja=int(np.argmin(admissible))
        return dict(sample_angles=qq.N,Q_min=float(Q.min()),W_min=float(W.min()),H_min=float(H[j]),
                    H_min_angle=float(qq.angle[j]),k_actual=float(kk),
                    k_admissible=float(admissible[ja]),k_admissible_angle=float(qq.angle[ja]),
                    k_margin=float(admissible[ja]-abs(kk)))
    def angular_tail(y,kk,qq=q):
        modes=np.arange(225,q.M+1);tail=np.zeros(q.n)
        tail[modes]=y[modes];tail[q.M+modes]=y[q.M+modes]
        tail[2*q.M+1+modes]=y[2*q.M+1+modes]
        amplitude_R=abs(tail[modes]);amplitude_T=abs(tail[q.M+modes])
        amplitude_Z=abs(tail[2*q.M+1+modes])
        bounds=[float(np.sum((2*modes+1)**order*(amplitude_R+amplitude_T)+(2*modes)**order*amplitude_Z)) for order in range(3)]
        jets=qq.jet(tail)
        return dict(cutoff_mode=224,mode_count=len(modes),sample_angles=qq.N,
            coefficient_max=float(np.max(abs(tail))),
            coefficient_L1_Cartesian_derivative_bounds=bounds,
            sampled_tail_F_Fphi_Fphiphi_max=[float(np.max(np.linalg.norm(jet,axis=1))) for jet in jets],
            same_state_with_modes_above_224_zeroed_domain=domain(y-tail,kk,qq))
    failed_evaluation={}
    def rhs(s,y):
        aa,ap1,_=profile(float(s))
        try:return q.rhs(y,ap1/aa)
        except FloatingPointError:
            failed_evaluation.update(attempted_time=float(s),sample_domain=domain(y,ap1/aa))
            raise
    solver=DOP853(rhs,start,initial,args.end,rtol=args.rtol,atol=args.atol,
                  first_step=min(args.max_step,args.end-start),max_step=args.max_step)
    mesh=[start];states=[initial.copy()];failure=None
    while solver.status=='running':
        try:
            message=solver.step()
        except FloatingPointError as error:
            failure=dict(kind='domain_evaluation_error_in_attempted_step',message=str(error),
                         last_accepted_time=mesh[-1],**failed_evaluation);break
        if solver.t>mesh[-1]:
            mesh.append(float(solver.t));states.append(solver.y.copy())
        if solver.status=='failed':
            failure=dict(kind='integrator_failed',message=message,last_accepted_time=mesh[-1]);break
    success=failure is None and solver.status=='finished'
    integrator_nodes=len(mesh);dropped=[]
    if success:
        threshold=64*abs(np.spacing(float(args.end)))
        while len(mesh)>2 and mesh[-1]-mesh[-2]<threshold:
            dropped.append(mesh[-2]);del mesh[-2];del states[-2]
    velocities=[old_v];accelerations=[old_acc]
    for s,y in zip(mesh[1:],states[1:]):
        aa,ap1,app1=profile(s);kk=ap1/aa;v=q.rhs(y,kk)
        velocities.append(v);accelerations.append(q.jvp(y,kk,v,dk=app1/aa-kk*kk))
    data={key:parent[key] for key in ('M','N','fixed_scalar_profile','analytic_extension_origin',
        'inward_scalar_profile','inward_profile_sha256','original_core_coefficients')}
    data.update(schema='local-ivp-continuation-common-jets-v1',scope=__doc__,
        ivp_reached_end=success,bvp_accepted=False,complete_prefix=False,
        original_M112_prefix_join_completed=False,local_join_uses_shared_stored_jets=True,
        input_sha256=h.sha(args.input),source_sha256=h.sha(__file__),reader_source_sha256=h.sha(BASE),
        start=start,requested_end=args.end,end=mesh[-1],max_step=args.max_step,rtol=args.rtol,atol=args.atol,
        nfev=solver.nfev,integrator_accepted_nodes=integrator_nodes,
        reconstruction_node_policy='keep true endpoint; remove only penultimate nodes within 64 ulp',
        dropped_terminal_node_times=dropped,failure=failure,initial_recomputed_jet_check=initial_checks,
        mesh=mesh,states=np.asarray(states).tolist(),rhs=np.asarray(velocities).tolist(),
        d2=np.asarray(accelerations).tolist(),
        old_cut_jets=dict(value=initial.tolist(),first=old_v.tolist(),second=old_acc.tolist()))
    aa,ap1,_=profile(mesh[-1]);data['last_accepted_sample_domain']=domain(states[-1],ap1/aa)
    read_q=h.Frenet(q.M,args.read_angles)
    data['last_accepted_read_grid_domain']=domain(states[-1],ap1/aa,read_q)
    data['last_accepted_angular_tail_above_224']=angular_tail(states[-1],ap1/aa,read_q)
    path=Path(str(args.output_stem)+'.json.gz')
    path.write_bytes(gzip.compress((json.dumps(data)+'\n').encode(),mtime=0))
    report=dict(scope=__doc__,ivp_reached_end=success,start=start,requested_end=args.end,last_accepted_time=mesh[-1],
        M=q.M,N=q.N,nodes=len(mesh),nfev=solver.nfev,failure=failure,
        initial_recomputed_jet_check=initial_checks,field_path=str(path),field_sha256=h.sha(path),
        source_sha256=h.sha(__file__),reader_source_sha256=h.sha(BASE),
        last_accepted_sample_domain=data['last_accepted_sample_domain'],
        last_accepted_read_grid_domain=data['last_accepted_read_grid_domain'],
        last_accepted_angular_tail_above_224=data['last_accepted_angular_tail_above_224'])
    print(json.dumps(dict(event='local_continuation_nodes_ready',**report)),flush=True)
    if success:
        report['actual_quintic']=base.read_field(data,profile,args.read_angles,args.radial_subdivisions)
        print(json.dumps(dict(event='local_continuation_quintic',**report)),flush=True)
    output=Path(str(args.output_stem)+'-report.json')
    output.write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(dict(event='continuation_report_ready',path=str(output),sha256=h.sha(output))),flush=True)


if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--input',type=Path,required=True);p.add_argument('--output-stem',type=Path,required=True)
    p.add_argument('--end',type=float,default=1.0);p.add_argument('--max-step',type=float,default=.000015625)
    p.add_argument('--rtol',type=float,default=1e-13);p.add_argument('--atol',type=float,default=1e-16)
    p.add_argument('--read-angles',type=int,default=8192);p.add_argument('--radial-subdivisions',type=int,default=4)
    main(p.parse_args())
