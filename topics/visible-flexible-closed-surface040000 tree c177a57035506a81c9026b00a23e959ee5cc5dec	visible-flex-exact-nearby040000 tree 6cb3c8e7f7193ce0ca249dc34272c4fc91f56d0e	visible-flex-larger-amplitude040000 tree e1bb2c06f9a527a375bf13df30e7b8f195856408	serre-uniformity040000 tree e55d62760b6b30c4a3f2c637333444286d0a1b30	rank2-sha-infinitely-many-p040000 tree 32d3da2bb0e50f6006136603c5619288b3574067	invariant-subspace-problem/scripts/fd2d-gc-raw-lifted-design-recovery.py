#!/usr/bin/env python3
"""Raw independent three-field branch finder recovered after executor loss.

Original projected Gauss and both Codazzi equations are unchanged. Optional
sampled formal-curvature rows guide the search only. Exact linear endpoint
conditions are imposed explicitly and every actual residual is reevaluated.
"""
import os
for _name in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[_name]='1'
import argparse,json,time,resource,traceback
from pathlib import Path
import numpy as np
from scipy import sparse
from fd2d_gc_raw_lifted_dae import RawLiftedDAE
from fd2d_gc_archive_arrays import identity,load_npz,save_npz
from fd2d_gc_bounded_direction_recovery import bounded_schur_direction
from fd2d_gc_curvature_penalty import curvature_penalty

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--candidate',type=Path,required=True)
    ap.add_argument('--out-prefix',type=Path,required=True)
    ap.add_argument('--warm-start',type=Path)
    ap.add_argument('--prefix-initializer',type=Path)
    ap.add_argument('--modes',type=int,default=15)
    ap.add_argument('--mesh-step',type=float,default=.04)
    ap.add_argument('--gap',type=float,default=.9)
    ap.add_argument('--amplitude',type=float,default=1.)
    ap.add_argument('--base-kind',choices=('balanced_seed','circle'),default='balanced_seed')
    ap.add_argument('--profile-kind',choices=('legacy_coast','positive_clock'),default='positive_clock')
    ap.add_argument('--tail-kind',choices=('signed_bubble','positive_bernstein'),default='positive_bernstein')
    ap.add_argument('--central-curvature-floor',type=float,default=.1)
    ap.add_argument('--central-curvature-cap',type=float,default=1/.136)
    ap.add_argument('--curvature-merit-cap',type=float,default=7.2)
    ap.add_argument('--curvature-merit-weight',type=float,default=1.)
    ap.add_argument('--direction-damping',type=float,default=1e-5)
    ap.add_argument('--max-iterations',type=int,default=80)
    ap.add_argument('--finite-tolerance',type=float,default=2e-7)
    args=ap.parse_args()
    stem=args.out_prefix
    if list(stem.parent.glob(stem.name+'*')):
        raise FileExistsError('Use a new actual-run stem')
    stem.parent.mkdir(parents=True,exist_ok=True)
    start=time.monotonic()
    report=dict(schema='fd2d-recovered-raw-bounded-curvature-merit-v1',
        source=identity(__file__),candidate_input=identity(args.candidate),
        parameters={k:str(v) if isinstance(v,Path) else v for k,v in vars(args).items()},
        providers={name:identity(Path(__file__).with_name(name)) for name in
            ('fd2d_gc_raw_lifted_dae.py','fd2d_gc_bounded_direction_recovery.py',
             'fd2d_gc_curvature_penalty.py','fd2d_positive_flat_developable_family.py',
             'fd2d_gc_design_profile_positive.py')},
        finite_scheme='Trapezoidal Codazzi and projected Gauss; exact functional tail lifting',
        explicit_boundary_definition='cut correction=0; central n=C*c, m=l=0, followed by full residual evaluation',
        curvature_merit_scope='Optional node formal-eigenvalue search objective only',
        line_search='Armijo for half squared combined residual norm using the actual directional derivative',
        original_gauss_codazzi_equations_changed=False,
        missing=['full angular/radial residual','actual Cartesian map and cut alignment',
                 'continuous full metric and all-time geometry','caps and complete meshes','same-g refinement'],
        completed=False,success=False,accepted_steps=0,exception=None)
    def save():
        report['seconds']=time.monotonic()-start
        report['maximum_rss_kib']=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
        stem.with_name(stem.name+'-report.json').write_text(json.dumps(report,indent=2,allow_nan=False)+'\n')
    def event(kind,**values):
        row=dict(event=kind,seconds=time.monotonic()-start,**values)
        with stem.with_name(stem.name+'-progress.jsonl').open('a') as f:
            f.write(json.dumps(row,allow_nan=False)+'\n')
        print(json.dumps(row,allow_nan=False),flush=True)
    save()
    try:
        problem=RawLiftedDAE(args.candidate,modes=args.modes,max_step=args.mesh_step,
            gap=args.gap,base_kind=args.base_kind,
            profile_kind=args.profile_kind,tail_kind=args.tail_kind)
        def project(v):
            z=np.array(v,float,copy=True)
            y,p=problem.unpack(z)
            if problem.tail_kind=='positive_bernstein':
                p[problem.K:-1]=np.clip(p[problem.K:-1],0.,1.2)
            edge=1e-12*problem.profile.model.Tmax
            p[-1]=np.clip(p[-1],edge,problem.profile.model.Tmax-edge)
            y[-1]=0.;y[0]=0.
            y[0,:problem.e]=problem.core_coefficients@p[:problem.K]
            return z
        def objective(v,jacobian=False):
            if jacobian:
                raw,j,data=problem.evaluate(v,jacobian=True)
            else:
                raw,data=problem.evaluate(v)
                j=None
            if args.curvature_merit_cap>0 and args.curvature_merit_weight>0:
                extra=curvature_penalty(problem,v,cap=args.curvature_merit_cap,
                    weight=args.curvature_merit_weight,data=data,jacobian=jacobian)
                residual=np.r_[raw,extra['residual']]
                if jacobian:j=sparse.vstack((j,extra['jacobian']),format='csc')
                info=extra['info']
            else:
                residual=raw
                info=dict(active_rows=0,residual_l2=0.,actual_geometry_certified=False)
            data['original_residual']=raw
            data['curvature_merit']=info
            problem.profile.set_parameter(float(problem.unpack(v)[1][-1]))
            return (residual,j,data) if jacobian else (residual,data)
        def diagnostics(v,data):
            d=problem.diagnostics(v,data)
            d.pop('exact_cut_lifting',None)
            y,p=problem.unpack(v)
            d.update(exact_cut_lifting_function=True,
                cut_correction_maximum=float(np.max(np.abs(y[-1]))),
                actual_field_cut_exact=bool(np.all(y[-1]==0.)),
                curvature_merit=data['curvature_merit'])
            return d
        if args.warm_start:
            a=load_npz(args.warm_start)
            if a['corrections'].shape[1]!=problem.q or len(a['parameters'])!=problem.parameter_count:
                raise ValueError('Warm dimensions differ; use explicit degree elevation first')
            for key in ('profile_kind','tail_kind','base_kind'):
                if key in a and str(a[key])!=getattr(args,key):
                    raise ValueError('Initializer chart/family mismatch: '+key)
            if 'candidate_sha256' in a and str(a['candidate_sha256'])!=identity(args.candidate)['sha256']:
                raise ValueError('Initializer belongs to another physical candidate')
            mesh=a['mesh'] if 'mesh' in a else a['x']
            y=np.column_stack([np.interp(problem.x,mesh,a['corrections'][:,k]) for k in range(problem.q)])
            vector=np.r_[y.ravel(),a['parameters']]
            report['warm_start_input']=identity(args.warm_start)
        else:
            vector=problem.initializer(args.amplitude,prefix_trajectory=args.prefix_initializer)
        vector=project(vector)
        if not problem.parameter_domain(vector,args.central_curvature_cap):
            raise ValueError('Initial parameters outside selected search domain')
        residual,data=objective(vector)
        y,p=problem.unpack(vector)
        report['initial_checkpoint']=save_npz(stem.with_name(stem.name+'-initial.npz'),
            mesh=problem.x,corrections=y,parameters=p,
            profile_kind=np.array(args.profile_kind),tail_kind=np.array(args.tail_kind),
            base_kind=np.array(args.base_kind),
            candidate_sha256=np.array(identity(args.candidate)['sha256']))
        report['initial']=diagnostics(vector,data)
        report['dimensions']=dict(nodes=problem.N,frequencies=problem.K,correction=problem.q,
            parameters=problem.parameter_count,unknowns=problem.size)
        report['angular_chart']=problem.chart.chart_definition()
        report['radial_chart']=problem.profile.definition()
        save();event('start',**report['dimensions'],diagnostics=report['initial'])
        for iteration in range(args.max_iterations):
            residual,jac,data=objective(vector,True)
            diag=diagnostics(vector,data);report['latest']=diag;save()
            event('assembled',iteration=iteration,objective_rows=len(residual),entries=jac.nnz,diagnostics=diag)
            if diag['residual_maximum']<args.finite_tolerance and data['curvature_merit']['residual_l2']<args.finite_tolerance:
                report.update(success=True,stop_reason='Finite original equations and chosen optional penalty reach tolerance; full continuous metric/geometry remain unpaid')
                break
            cost=.5*float(residual@residual)
            accepted=False
            for damping in (args.direction_damping,max(args.direction_damping*100,1e-3),
                            max(args.direction_damping*10000,.1)):
                direction,info=bounded_schur_direction(problem,vector,residual,jac,
                    damping=damping,central_floor=args.central_curvature_floor,
                    central_cap=args.central_curvature_cap,preserve_gap=True)
                direction=project(vector+direction)-vector
                slope=float(residual@(jac@direction))
                event('direction',iteration=iteration,directional_merit_derivative=slope,**info)
                if not np.isfinite(slope) or slope>=0:continue
                for back in range(22):
                    alpha=2.**(-back)
                    trial=project(vector+alpha*direction)
                    if not problem.parameter_domain(trial,args.central_curvature_cap):continue
                    try:rr,dd=objective(trial)
                    except (FloatingPointError,ValueError,OverflowError):continue
                    trial_cost=.5*float(rr@rr)
                    if np.isfinite(trial_cost) and trial_cost<cost+1e-4*alpha*slope:
                        vector=trial;accepted=True;report['accepted_steps']+=1
                        yy,pp=problem.unpack(vector)
                        report['latest_checkpoint']=save_npz(stem.with_name(stem.name+'-accepted-%04d.npz'%report['accepted_steps']),
                            mesh=problem.x,corrections=yy,parameters=pp,
                            profile_kind=np.array(args.profile_kind),tail_kind=np.array(args.tail_kind),
                            base_kind=np.array(args.base_kind),
                            candidate_sha256=np.array(identity(args.candidate)['sha256']))
                        report['latest']=diagnostics(vector,dd)
                        save();event('accepted',iteration=iteration,alpha=alpha,
                            checkpoint=report['latest_checkpoint'],objective_norm=float(np.sqrt(2*trial_cost)),
                            diagnostics=report['latest'])
                        break
                if accepted:break
            if not accepted:
                report['stop_reason']='No recorded constrained direction gives actual merit descent'
                break
        else:
            report['stop_reason']='Recorded finite iteration allocation ended without convergence'
        residual,data=objective(vector)
        y,p=problem.unpack(vector)
        report['final']=diagnostics(vector,data)
        report['field']=save_npz(stem.with_name(stem.name+'-field.npz'),
            mesh=problem.x,corrections=y,parameters=p,full_gauss_nodes=data['full_gauss'],
            codazzi_cell_residual=data['codazzi_cells'],
            profile_kind=np.array(args.profile_kind),tail_kind=np.array(args.tail_kind),
            base_kind=np.array(args.base_kind),
            candidate_sha256=np.array(identity(args.candidate)['sha256']))
        cp=stem.with_name(stem.name+'-candidate.json')
        cp.write_text(json.dumps(problem.profile.model.bundle(float(p[-1])),indent=2)+'\n')
        report['actual_candidate']=identity(cp)
        report['central_definition']=problem.core(p[:problem.K])[0].definition()
        report['completed']=True
        save();event('complete',success=report['success'],stop_reason=report['stop_reason'],diagnostics=report['final'])
    except Exception as exc:
        report['exception']=dict(type=type(exc).__name__,message=str(exc),traceback=traceback.format_exc())
        save();event('exception',type=type(exc).__name__,message=str(exc))
        raise

if __name__=='__main__':main()
