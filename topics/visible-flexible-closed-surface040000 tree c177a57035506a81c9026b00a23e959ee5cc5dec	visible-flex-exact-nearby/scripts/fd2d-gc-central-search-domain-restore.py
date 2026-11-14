#!/usr/bin/env python3
"""Small explicit central initializer change after actual angular injection.

Restore the sampled central search inequalities and exact nonlinear axis
gap by a closest-coefficient constrained problem. Tail controls, profile
parameters, numerical mesh, atlas and all noncentral raw coefficients are
kept. This is a new initializer, not a same-field embedding or a BVP solve.
"""
import os
for name in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[name]='1'
import argparse,json,time,datetime,resource,traceback
from pathlib import Path
import numpy as np
from scipy.optimize import minimize,LinearConstraint,NonlinearConstraint
from fd2d_gc_archive_arrays import identity,load_npz,save_npz
from fd2d_gc_midpoint_refined_positive_trace_v3 import create_midpoint_refined_problem,checkpoint_arrays


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    for n in ('candidate','warm-start','radius-packet','reference-inlet','out-prefix'):
        ap.add_argument('--'+n,type=Path,required=True)
    ap.add_argument('--reference-cache',type=Path)
    ap.add_argument('--floor',type=float,default=.1)
    ap.add_argument('--cap',type=float,default=1/.136)
    ap.add_argument('--gap',type=float,default=.9)
    args=ap.parse_args();stem=args.out_prefix;start=time.monotonic()
    if list(stem.parent.glob(stem.name+'*')):raise FileExistsError('Use a fresh stem')
    report=dict(schema='fd2d-explicit-central-search-domain-restoration-v1',source=identity(__file__),
        input=identity(args.warm_start),candidate=identity(args.candidate),
        started_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),completed=False,
        BVP_performed=False,physical_metric_changed=False,actual_central_field_changed=True,
        continuous_geometric_certificate=False)
    def save():
        report['seconds']=time.monotonic()-start
        report['peak_rss_kib']=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
        stem.with_name(stem.name+'-report.json').write_text(json.dumps(report,indent=2,allow_nan=False)+'\n')
    save()
    try:
        a=load_npz(args.warm_start);proof=json.loads(args.radius_packet.read_text())
        if not proof['passed'] or proof['candidate_sha256']!=report['candidate']['sha256']:
            raise ValueError('Wrong physical radius packet')
        problem=create_midpoint_refined_problem(args.candidate,saved_field=a,split_cells=(),
            reference_inlet=args.reference_inlet,reference_cache=args.reference_cache,
            reference_rim_fraction=.12,max_step=.04,gap=args.gap,mesh_relative_tolerance=1e-12,
            base_lower_bound='4/5',base_lower_provenance=dict(**identity(args.radius_packet),
                candidate_sha256=proof['candidate_sha256']),radius_floor=.1)
        old=np.r_[a['corrections'].ravel(),a['parameters']]
        y,p=problem.unpack(old);c=p[:problem.K].copy()
        B=problem.core_basis;n0=problem.seed+B@c
        margin=1e-9
        def axes(d):return problem.core(c+d)[1]
        cons=[LinearConstraint(B,args.floor+margin-n0,args.cap-n0),
            NonlinearConstraint(lambda d:np.array([float(axes(d)['gap'])]),args.gap,args.gap,
                jac=lambda d:np.asarray(axes(d)['gap_jacobian'],float)[None,:])]
        solution=minimize(lambda d:.5*float(d@d),np.zeros(problem.K),jac=lambda d:d,
            method='SLSQP',constraints=cons,options=dict(maxiter=1000,ftol=1e-14))
        new=old.copy();new_y,new_p=problem.unpack(new);new_p[:problem.K]=c+solution.x
        new_y[problem.fixed_central_nodes,:]=0.
        new_y[problem.fixed_central_nodes,:problem.e]=problem.core_coefficients@new_p[:problem.K]
        n1=problem.seed+B@new_p[:problem.K];aa=problem.core(new_p[:problem.K])[1]
        if not problem.parameter_domain(new,args.cap,args.floor) or abs(float(aa['gap'])-args.gap)>2e-12:
            raise ArithmeticError('Actual restored state does not satisfy its declared finite search conditions')
        noncentral=np.setdiff1d(np.arange(problem.N),problem.fixed_central_nodes)
        if y[noncentral].tobytes()!=new_y[noncentral].tobytes():
            raise ArithmeticError('A noncentral raw coefficient changed')
        if p[problem.K:].tobytes()!=new_p[problem.K:].tobytes():
            raise ArithmeticError('Tail or physical profile parameters changed')
        definition=dict(schema='fd2d-central-finite-domain-initializer-change-v1',input=report['input'],
            source=report['source'],floor=args.floor,QP_lower_target=args.floor+margin,
            cap=args.cap,gap_target=args.gap,old_minimum=float(n0.min()),
            new_minimum=float(n1.min()),new_maximum=float(n1.max()),
            A=float(aa['A']),B=float(aa['B']),gap=float(aa['gap']),
            central_delta_l2=float(np.linalg.norm(solution.x)),central_delta_max=float(np.max(abs(solution.x))),
            central_curvature_maximum_change=float(np.max(abs(n1-n0))),
            changed_raw_nodes=problem.fixed_central_nodes.tolist(),
            changed_raw_coefficient_maximum=float(np.max(abs(new_y-y))),
            tail_and_profile_bytes_unchanged=True,noncentral_raw_bytes_unchanged=True,
            SLSQP_success=bool(solution.success),SLSQP_status=int(solution.status),
            SLSQP_message=str(solution.message),iterations=int(solution.nit),
            not_claimed_same_field=True,physical_g_unchanged=True,no_whole_F_or_J=True)
        arrays=checkpoint_arrays(problem,new,report['candidate']['sha256'],
            refinement_definition=problem.radial_refinement_definition)
        arrays['search_domain_restore_definition']=np.array(json.dumps(definition,sort_keys=True))
        report['definition']=definition
        report['field']=save_npz(stem.with_name(stem.name+'-field.npz'),**arrays)
        report['completed']=True;save()
        print(json.dumps(dict(event='central_domain_restored',field=report['field'],definition=definition)),flush=True)
        return 0
    except Exception as exc:
        report['exception']=dict(type=type(exc).__name__,message=str(exc),traceback=traceback.format_exc())
        save();raise


if __name__=='__main__':raise SystemExit(main())
