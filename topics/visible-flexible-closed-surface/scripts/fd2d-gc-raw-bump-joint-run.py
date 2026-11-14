#!/usr/bin/env python3
"""Actual rectangular raw-GC/profile joint branch search, fixed physical s.

Curvature and high-angular-Gauss rows guide a finite search. Original raw F
is always reported separately. Every accepted state is saved immediately.
"""
import os
for name in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[name]='1'
import argparse,json,time,resource,traceback,datetime,platform
from pathlib import Path
import numpy as np
import scipy
from scipy import sparse
from fd2d_gc_raw_bump_dae import RawBumpDAE
from fd2d_gc_bump_bounded_schur import bounded_bump_direction
from fd2d_gc_bump_merit import curvature_merit,high_gauss_merit
from fd2d_gc_archive_arrays import identity,load_npz,save_npz


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--candidate',type=Path,required=True)
    ap.add_argument('--warm-start',type=Path,required=True)
    ap.add_argument('--radius-packet',type=Path,required=True)
    ap.add_argument('--out-prefix',type=Path,required=True)
    ap.add_argument('--owner-stop-file',type=Path,required=True)
    ap.add_argument('--max-iterations',type=int,default=40)
    ap.add_argument('--modes',type=int,default=15)
    ap.add_argument('--mesh-step',type=float,default=.04)
    ap.add_argument('--gap',type=float,default=.9)
    ap.add_argument('--central-floor',type=float,default=.1)
    ap.add_argument('--central-cap',type=float,default=1/.136)
    ap.add_argument('--profile-box',type=float,default=.08)
    ap.add_argument('--radius-floor',type=float,default=.1)
    ap.add_argument('--curvature-cap',type=float,default=7.2)
    ap.add_argument('--curvature-weight',type=float,default=1.)
    ap.add_argument('--high-gauss-weight',type=float,default=1.)
    ap.add_argument('--damping',type=float,default=1e-5)
    ap.add_argument('--finite-tolerance',type=float,default=2e-7)
    args=ap.parse_args();stem=args.out_prefix
    if list(stem.parent.glob(stem.name+'*')):
        raise FileExistsError('Use a new unique run stem')
    stem.parent.mkdir(parents=True,exist_ok=True);start=time.monotonic()
    here=Path(__file__).resolve().parent
    report=dict(schema='fd2d-physical-bump-raw-joint-run-v1',source=identity(__file__),
        providers={name:identity(here/name) for name in ('fd2d_gc_raw_bump_dae.py',
            'fd2d_gc_radial_bump_profile.py','fd2d_gc_bump_bounded_schur.py',
            'fd2d_gc_bump_merit.py','fd2d_gc_curvature_penalty.py')},
        candidate=identity(args.candidate),warm_input=identity(args.warm_start),
        settings={k:str(v) if isinstance(v,Path) else v for k,v in vars(args).items()},
        versions=dict(python=platform.python_version(),numpy=np.__version__,scipy=scipy.__version__),
        started_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
        physical_coordinates='fixed physical s, fixed material u, recorded U(s,xi) chart',
        original_raw_equations_changed=False,physical_g_changes_with_profile_parameters=True,
        exact_boundary_projection='central n=Cc,m=l=0; cut all corrections zero',
        finite_guidance='curvature cap and angular complement of Gauss on the actual node grid',
        missing=['full radial and angular Codazzi residual','actual position map and cut rigid alignment',
            'continuous metric, whole geometry and reach','same-g refinement and closed meshes'],
        accepted_steps=0,completed=False,finite_success=False,owner_stop=False,exception=None)
    def save():
        report['seconds']=time.monotonic()-start
        report['peak_rss_kib']=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
        stem.with_name(stem.name+'-report.json').write_text(json.dumps(report,indent=2,allow_nan=False)+'\n')
    def event(kind,**values):
        row=dict(event=kind,seconds=time.monotonic()-start,**values)
        with stem.with_name(stem.name+'-progress.jsonl').open('a') as f:f.write(json.dumps(row,allow_nan=False)+'\n')
        print(json.dumps(row,allow_nan=False),flush=True)
    def stopped():
        if args.owner_stop_file.exists():
            report['owner_stop']=True
            report['stop_reason']='Owner stop file observed; latest complete accepted state retained'
            return True
        return False
    save()
    try:
        proof=json.loads(args.radius_packet.read_text())
        if not proof['passed'] or proof['candidate_sha256']!=report['candidate']['sha256']:
            raise ValueError('Radius proof packet does not bind the actual base candidate')
        witness=dict(**identity(args.radius_packet),candidate_sha256=proof['candidate_sha256'])
        problem=RawBumpDAE(args.candidate,modes=args.modes,max_step=args.mesh_step,gap=args.gap,
            base_lower_bound='4/5',base_lower_provenance=witness,radius_floor=args.radius_floor)
        a=load_npz(args.warm_start)
        if str(a['candidate_sha256'])!=report['candidate']['sha256'] or str(a['profile_kind'])!='physical_bumps':
            raise ValueError('Wrong physical warm initializer identity')
        if not np.array_equal(a['mesh'],problem.x) or not np.array_equal(a['profile_supports'],problem.profile.supports):
            raise ValueError('Warm grid/supports differ; explicitly construct a new initial representation')
        if a['corrections'].shape!=(problem.N,problem.q) or len(a['parameters'])!=problem.parameter_count:
            raise ValueError('Warm array dimension mismatch')
        def project(v):
            z=np.array(v,float,copy=True);_,p=problem.unpack(z)
            p[problem.tail_parameter_slice]=np.clip(p[problem.tail_parameter_slice],0.,1.2)
            p[problem.profile_parameter_slice]=np.clip(p[problem.profile_parameter_slice],-args.profile_box,args.profile_box)
            return problem.impose_linear_boundary_values(z)
        def objective(v,jacobian=False):
            if jacobian:raw,j,data=problem.evaluate(v,jacobian=True)
            else:raw,data=problem.evaluate(v);j=None
            curv=curvature_merit(problem,v,cap=args.curvature_cap,weight=args.curvature_weight,data=data,jacobian=jacobian)
            high=high_gauss_merit(problem,v,weight=args.high_gauss_weight,data=data,jacobian=jacobian)
            r=np.r_[raw,curv['residual'],high['residual']]
            if jacobian:j=sparse.vstack((j,curv['jacobian'],high['jacobian']),format='csc')
            data['original_residual']=raw;data['curvature_merit']=curv['info'];data['high_gauss_merit']=high['info']
            return (r,j,data) if jacobian else (r,data)
        def diag(v,data):
            d=problem.diagnostics(v,data)
            d['curvature_merit']=data['curvature_merit'];d['high_gauss_merit']=data['high_gauss_merit']
            return d
        def checkpoint(v,suffix,extra=None):
            y,p=problem.unpack(v)
            arrays=dict(mesh=problem.x,corrections=y,parameters=p,modes=np.array(problem.K),
                profile_supports=problem.profile.supports,profile_count=np.array(problem.J),
                fixed_base_T=np.array(problem.fixed_base_T),profile_kind=np.array(problem.profile_kind),
                tail_kind=np.array(problem.tail_kind),base_kind=np.array(problem.base_kind),
                candidate_sha256=np.array(report['candidate']['sha256']),blend=np.array(problem.blend))
            if extra:arrays.update(extra)
            return save_npz(stem.with_name(stem.name+suffix),**arrays)
        vector=project(np.r_[a['corrections'].ravel(),a['parameters']])
        if not problem.parameter_domain(vector,args.central_cap,args.central_floor):
            raise ValueError('Initial vector is outside the selected search domain')
        residual,data=objective(vector)
        report['initial_checkpoint']=checkpoint(vector,'-initial.npz')
        report['initial']=diag(vector,data);report['layout']=problem.parameter_layout()
        report['angular_chart']=problem.chart.chart_definition();report['radius_proof']=witness
        report['profile_positive_linear_rows']=len(problem.profile_domain['lower'])
        save();event('start',layout={k:v for k,v in report['layout'].items() if k!='physical_profile_definition'},diagnostics=report['initial'])
        for iteration in range(args.max_iterations):
            if stopped():break
            residual,jac,data=objective(vector,True);d=diag(vector,data);report['latest']=d;save()
            event('assembled',iteration=iteration,rows=len(residual),jacobian_nonzeros=jac.nnz,diagnostics=d)
            if d['residual_maximum']<args.finite_tolerance and data['curvature_merit']['residual_l2']<args.finite_tolerance and data['high_gauss_merit']['residual_l2']<args.finite_tolerance:
                report['finite_success']=True;report['stop_reason']='Recorded finite raw and guidance rows reach tolerance; whole strong-target conditions remain unpaid';break
            cost=.5*float(residual@residual);accepted=False
            for damping in (args.damping,max(args.damping*100,1e-3),max(args.damping*10000,.1)):
                if stopped():break
                direction,info=bounded_bump_direction(problem,vector,residual,jac,damping=damping,
                    central_floor=args.central_floor,central_cap=args.central_cap,profile_box=args.profile_box,preserve_gap=True)
                direction=project(vector+direction)-vector;slope=float(residual@(jac@direction))
                event('direction',iteration=iteration,merit_directional_derivative=slope,**info)
                if not np.isfinite(slope) or slope>=0:continue
                for back in range(22):
                    if stopped():break
                    alpha=2.**(-back);trial=project(vector+alpha*direction)
                    if not problem.parameter_domain(trial,args.central_cap,args.central_floor):continue
                    try:rr,dd=objective(trial)
                    except (FloatingPointError,ValueError,OverflowError):continue
                    value=.5*float(rr@rr)
                    if np.isfinite(value) and value<cost+1e-4*alpha*slope:
                        vector=trial;accepted=True;report['accepted_steps']+=1
                        report['latest_checkpoint']=checkpoint(vector,'-accepted-%04d.npz'%report['accepted_steps'])
                        report['latest']=diag(vector,dd);save()
                        event('accepted',iteration=iteration,alpha=alpha,objective_norm=float(np.sqrt(2*value)),
                            checkpoint=report['latest_checkpoint'],diagnostics=report['latest'])
                        break
                if accepted or report['owner_stop']:break
            if report['owner_stop']:break
            if not accepted:
                report['stop_reason']='No recorded constrained direction gives full actual Armijo descent';break
        else:report['stop_reason']='Allocated forty-or-requested finite iterations finished without success claim'
        residual,data=objective(vector);report['final']=diag(vector,data)
        report['field']=checkpoint(vector,'-field.npz',dict(full_gauss_nodes=data['full_gauss'],codazzi_cells=data['codazzi_cells']))
        _,p=problem.unpack(vector);problem.profile.set_parameters(p[problem.profile_parameter_slice])
        gp=stem.with_name(stem.name+'-physical-metric.json')
        gp.write_text(json.dumps(problem.profile.definition(),indent=2)+'\n')
        report['actual_physical_metric']=identity(gp)
        report['central_definition']=problem.core(p[:problem.K])[0].definition()
        report['completed']=True;save()
        event('complete',finite_success=report['finite_success'],owner_stop=report['owner_stop'],
            stop_reason=report['stop_reason'],diagnostics=report['final'])
        return 130 if report['owner_stop'] else 0
    except Exception as exc:
        report['exception']=dict(type=type(exc).__name__,message=str(exc),traceback=traceback.format_exc())
        save();event('exception',type=type(exc).__name__,message=str(exc));raise


if __name__=='__main__':raise SystemExit(main())
