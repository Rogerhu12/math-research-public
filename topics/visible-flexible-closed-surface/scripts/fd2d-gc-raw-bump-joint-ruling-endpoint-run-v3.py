#!/usr/bin/env python3
"""Actual rectangular raw-GC/profile joint branch search, fixed physical s.

Curvature, high-angular Gauss and full angular Codazzi guide a finite search. Original raw F
is always reported separately. Every accepted state is saved immediately.
"""
import os
for name in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[name]='1'
import argparse,json,time,resource,traceback,datetime,platform,gc
from pathlib import Path
import numpy as np
import scipy
from scipy import sparse
from fd2d_gc_raw_bump_ruling_atlas import RulingAtlasRawBumpDAE,checkpoint_arrays
from fd2d_gc_gauss_cell_codazzi_chunked import gauss_cell_codazzi
from fd2d_gc_gauss_cell_codazzi_endpoint_d2 import gauss_cell_codazzi_endpoint_d2
from fd2d_gc_d2_complements import high_gauss_merit_d2
from fd2d_gc_codazzi_complement import codazzi_complement
from fd2d_gc_bump_residual_locations import residual_locations
from fd2d_gc_bump_cylinder_bounded_schur_v2 import bounded_bump_direction
from fd2d_gc_bump_merit import curvature_merit,high_gauss_merit
from fd2d_gc_archive_arrays import identity,load_npz,save_npz


def frozen_reference_identity(definition):
    """Compare frozen functions independently of path and operational cache counts.

    The reference binding SHA already covers exact input/source content and
    numeric precision. All remaining mathematical window/lifting fields are
    compared. Full unmodified metadata is retained in every checkpoint.
    """
    def clean(value):
        if isinstance(value,dict):
            identity_record='sha256' in value and 'bytes' in value
            return {k:clean(v) for k,v in value.items()
                    if k!='cache_statistics' and not (identity_record and k=='path')}
        if isinstance(value,list):return [clean(v) for v in value]
        return value
    return clean(definition)


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--candidate',type=Path,required=True)
    ap.add_argument('--warm-start',type=Path,required=True)
    ap.add_argument('--radius-packet',type=Path,required=True)
    ap.add_argument('--reference-inlet',type=Path,required=True)
    ap.add_argument('--reference-cache',type=Path)
    ap.add_argument('--reference-rim-fraction',type=float,default=.12)
    ap.add_argument('--out-prefix',type=Path,required=True)
    ap.add_argument('--owner-stop-file',type=Path,required=True)
    ap.add_argument('--max-iterations',type=int,default=15)
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
    ap.add_argument('--high-codazzi-weight',type=float,default=1.)
    ap.add_argument('--mesh-relative-tolerance',type=float,default=1e-12)
    ap.add_argument('--damping',type=float,default=1e-5)
    ap.add_argument('--finite-tolerance',type=float,default=2e-7)
    args=ap.parse_args();stem=args.out_prefix
    if list(stem.parent.glob(stem.name+'*')):
        raise FileExistsError('Use a new unique run stem')
    stem.parent.mkdir(parents=True,exist_ok=True);start=time.monotonic()
    here=Path(__file__).resolve().parent
    report=dict(schema='fd2d-physical-bump-global-ruling-atlas-endpoint-chunk-D2-joint-run-v10',source=identity(__file__),
        providers={name:identity(here/name) for name in ('fd2d_gc_frozen_ruling_atlas.py','fd2d_gc_raw_bump_ruling_atlas.py','fd2d_gc_gauss_cell_codazzi_endpoint_d2.py','fd2d_gc_raw_bump_coast_reference.py','fd2d_gc_frozen_coast_reference.py','fd2d_k0_native_gc.py','fd2d_gc_raw_bump_turn_mesh.py','fd2d_gc_gauss_cell_codazzi.py','fd2d_gc_gauss_cell_codazzi_chunked.py',
            'fd2d_gc_gauss_cell_codazzi_d2.py','fd2d_gc_d2_complements.py','fd2d_gc_raw_bump_cylinder.py','fd2d_gc_bump_cylinder_bounded_schur_v2.py','fd2d_gc_raw_bump_clean.py','fd2d_gc_raw_bump_dae.py',
            'fd2d_gc_codazzi_complement.py','fd2d_gc_bump_residual_locations.py',
            'fd2d_gc_radial_bump_profile.py','fd2d_gc_bump_bounded_schur.py',
            'fd2d_gc_bump_merit.py','fd2d_gc_curvature_penalty.py')},
        candidate=identity(args.candidate),warm_input=identity(args.warm_start),reference_inlet=identity(args.reference_inlet),
        settings={k:str(v) if isinstance(v,Path) else v for k,v in vars(args).items()},
        versions=dict(python=platform.python_version(),numpy=np.__version__,scipy=scipy.__version__),
        started_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
        physical_coordinates='fixed physical s, fixed material u, recorded U(s,xi) chart',
        raw_differential_formulas_changed=False,finite_field_representation_changed=True,
        finite_matrix_changed_by_mesh_and_lifting=True,physical_g_changes_with_profile_parameters=True,
        exact_boundary_projection='every exact-cylinder node n=Cc,m=l=0; cut all corrections zero',
        finite_guidance='curvature cap and angular complements of Gauss and both Codazzi equations on the actual grid',
        missing=['continuous radial and angular residual bounds','actual position map and cut rigid alignment',
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
        problem=RulingAtlasRawBumpDAE(args.candidate,modes=args.modes,max_step=args.mesh_step,gap=args.gap,
            reference_inlet=args.reference_inlet,reference_cache=args.reference_cache,
            reference_rim_fraction=args.reference_rim_fraction,
            mesh_relative_tolerance=args.mesh_relative_tolerance,
            base_lower_bound='4/5',base_lower_provenance=witness,radius_floor=args.radius_floor)
        a=load_npz(args.warm_start)
        if str(a['candidate_sha256'])!=report['candidate']['sha256'] or str(a['profile_kind'])!='physical_bumps':
            raise ValueError('Wrong physical warm initializer identity')
        if not np.array_equal(a['mesh'],problem.x) or not np.array_equal(a['profile_supports'],problem.profile.supports):
            raise ValueError('Warm grid/supports differ; explicitly construct a new initial representation')
        if a['corrections'].shape!=(problem.N,problem.q) or len(a['parameters'])!=problem.parameter_count:
            raise ValueError('Warm array dimension mismatch')
        if 'seed_weight_definition' not in a or json.loads(str(a['seed_weight_definition']))!=problem.seed_weight_definition:
            raise ValueError('Explicit new seed-weight identity missing or mismatched')
        report['mesh_coalescence']=problem.mesh_coalescence
        report['seed_weight_definition']=problem.seed_weight_definition
        report['central_field_definition']=problem.central_field_definition
        report['targeted_mesh_definition']=problem.targeted_mesh_definition
        report['coast_reference_definition']=problem.coast_reference_definition
        report['coast_reference_provenance']=problem.coast_reference_provenance
        report['angular_atlas_definition']=problem.angular_atlas_definition
        report['atlas_mesh_definition']=problem.atlas_mesh_definition
        report['reference_evaluation_definition']=problem.reference_evaluation_definition
        report['finite_radial_scheme']='Exact full lifting endpoint difference plus Gauss-Legendre order 2 physical-PDE averages; original node Gauss/boundary/gap rows'
        report['legacy_trapezoid_is_reference_only']=True
        report['finite_equations_changed_by_exact_lifting_integration']=True
        report['finite_angular_representation_changed']=True
        report['assembly_and_row_coordinates']='8 radial-cell blocks, direct complete D2 high Fourier rows; same Gauss2 finite objective on the declared analytic D2 space'
        report['finite_equations_changed_by_chunking_and_D2_rows']=False
        report['assembly_change_from_atlas10']='8-cell blocks, node merits before endpoint cells, promptly release unused full-node lifting and parameter packets; same finite equations and actual warm'
        def project(v):
            z=np.array(v,float,copy=True);_,p=problem.unpack(z)
            p[problem.tail_parameter_slice]=np.clip(p[problem.tail_parameter_slice],0.,1.2)
            p[problem.profile_parameter_slice]=np.clip(p[problem.profile_parameter_slice],-args.profile_box,args.profile_box)
            return problem.impose_linear_boundary_values(z)
        def assembly_phase(name):
            status={}
            for line in Path('/proc/self/status').read_text().splitlines():
                if line.startswith(('VmRSS:','VmHWM:','VmSize:')):
                    key,value,*_=line.split();status[key.rstrip(':')]=int(value)
            event('assembly_phase',phase=name,process_kib=status)
        def objective(v,jacobian=False):
            if jacobian:
                assembly_phase('raw_node_start')
                trap,j,data=problem.evaluate(v,jacobian=True)
            else:trap,data=problem.evaluate(v);j=None
            # Endpoint cells construct their own local lifting. None of the
            # following node merits, diagnostics or Schur map uses this
            # all-node value/x/xi/tail/profile packet again.
            del data['lift']
            if jacobian:assembly_phase('raw_node_after_unused_lift_release')
            curv=curvature_merit(problem,v,cap=args.curvature_cap,weight=args.curvature_weight,data=data,jacobian=jacobian)
            if jacobian:assembly_phase('curvature_done')
            high=high_gauss_merit_d2(problem,v,weight=args.high_gauss_weight,data=data,jacobian=jacobian)
            del data['fields_parameters']
            gc.collect()
            if jacobian:assembly_phase('high_gauss_done_node_parameter_packet_released')
            quadrature=gauss_cell_codazzi(problem,v,order=2,high_weight=args.high_codazzi_weight,jacobian=jacobian,
                block_cells=8,consumer=gauss_cell_codazzi_endpoint_d2)
            if jacobian:assembly_phase('endpoint_cell_done')
            quadrature['info']['nested_symmetry_diagnostic_scope']='First block; full point maxima and matrices aggregated over all blocks'
            count=(problem.N-1)*problem.d
            raw=np.r_[quadrature['retained_residual'],trap[count:]]
            if jacobian:j=sparse.vstack((quadrature['retained_jacobian'],j[count:]),format='csc')
            residual=np.r_[raw,curv['residual'],high['residual'],quadrature['high_residual']]
            if jacobian:j=sparse.vstack((j,curv['jacobian'],high['jacobian'],quadrature['high_jacobian']),format='csc')
            if jacobian:assembly_phase('stack_done')
            data['original_residual']=raw
            data['legacy_trapezoid_residual']=trap
            data['legacy_trapezoid_codazzi_cells']=data['codazzi_cells']
            data['codazzi_cells']=quadrature['retained_cells']
            data['curvature_merit']=curv['info'];data['high_gauss_merit']=high['info']
            data['high_codazzi_merit']=dict(quadrature['info'],
                residual_l2=float(np.linalg.norm(quadrature['high_residual'])),
                sampled_omitted_codazzi_maximum=quadrature['info']['sampled_omitted_average_codazzi_maximum'])
            data['codazzi_complement_result']={'omitted_codazzi_cells':quadrature['omitted_codazzi_cells']}
            return (residual,j,data) if jacobian else (residual,data)
        def diag(v,data):
            raw=data['original_residual'];fields=data['fields'];p=data['parameters']
            n,m,l=(fields[:,:,i] for i in range(3));disc=np.hypot(l-n,2*m);axes=data['axes']
            d=dict(residual_maximum=float(np.max(abs(raw))),
                residual_rms=float(np.linalg.norm(raw)/np.sqrt(len(raw))),
                legacy_trapezoid_residual_maximum=float(np.max(abs(data['legacy_trapezoid_residual']))),
                full_gauss_node_maximum=float(np.max(abs(data['full_gauss']))),
                formal_curvature_node_maximum=float(np.max(np.maximum(abs(l+n+disc),abs(l+n-disc)))/2),
                A=float(axes['A']),B=float(axes['B']),gap=float(axes['gap']),
                base_coast_T_fixed=problem.base_reference_T,
                tail_coefficients=p[problem.tail_parameter_slice].tolist(),
                profile_deltas=p[problem.profile_parameter_slice].tolist(),
                minimum_n=float(n.min()),maximum_n=float(n.max()),
                minimum_central_curvature=float((problem.seed+problem.core_basis@p[:problem.K]).min()),
                minimum_radius_at_nodes=float(data['profile_jet']['a'].min()),
                exact_cut_lifting=True,cut_n_mean_omitted=False,
                cut_correction_maximum=float(np.max(abs(problem.unpack(v)[0][-1]))),
                nonlinear_finite_solution=False,continuous_certificate=False,
                finite_radial_scheme='Exact lifting endpoints plus Gauss2 physical PDE averages',
                curvature_merit=data['curvature_merit'],high_gauss_merit=data['high_gauss_merit'],
                high_codazzi_merit=data['high_codazzi_merit'])
            return d
        def checkpoint(v,suffix,extra=None):
            arrays=checkpoint_arrays(problem,v,report['candidate']['sha256'])
            if extra:arrays.update(extra)
            return save_npz(stem.with_name(stem.name+suffix),**arrays)
        old_vector=np.r_[a['corrections'].ravel(),a['parameters']]
        for key,expected in (('angular_atlas_definition',problem.angular_atlas_definition),
                ('coast_reference_definition',problem.coast_reference_definition),
                ('reference_evaluation_definition',problem.reference_evaluation_definition)):
            if key not in a or frozen_reference_identity(json.loads(str(a[key])))!=frozen_reference_identity(expected):
                raise ValueError('Saved actual field definition differs: '+key)
        initial_vector=old_vector
        report['initial_reference_conversion']=dict(kind='continue_actual_global_ruling_atlas_field',
            source_representation_kind=str(a['representation_kind']),applied_again=False,
            saved_warm_conversion_required=True)
        vector=project(initial_vector)
        report['initial_exact_cylinder_projection_change']=float(np.max(abs(vector-initial_vector)))
        report['initial_change_from_input_coefficient_maximum']=float(np.max(abs(vector-old_vector)))
        if not problem.parameter_domain(vector,args.central_cap,args.central_floor):
            raise ValueError('Initial vector is outside the selected search domain')
        residual,data=objective(vector)
        report['initial_checkpoint']=checkpoint(vector,'-initial.npz')
        report['initial']=diag(vector,data);report['layout']=problem.parameter_layout()
        report['initial_locations']=residual_locations(problem,vector,data,data['codazzi_complement_result'],args.curvature_cap)
        report['angular_chart']=problem.chart.chart_definition();report['radius_proof']=witness
        report['profile_positive_linear_rows']=len(problem.profile_domain['lower'])
        save();event('start',layout={k:v for k,v in report['layout'].items() if k!='physical_profile_definition'},diagnostics=report['initial'])
        for iteration in range(args.max_iterations):
            if stopped():break
            if 'jac' in locals():del jac
            if 'rr' in locals():del rr,dd
            del residual,data
            gc.collect()
            residual,jac,data=objective(vector,True);d=diag(vector,data);report['latest']=d;save()
            event('assembled',iteration=iteration,rows=len(residual),jacobian_nonzeros=jac.nnz,diagnostics=d)
            if d['residual_maximum']<args.finite_tolerance and data['curvature_merit']['residual_l2']<args.finite_tolerance and data['high_gauss_merit']['residual_l2']<args.finite_tolerance and data['high_codazzi_merit']['residual_l2']<args.finite_tolerance:
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
                    if 'rr' in locals():del rr,dd
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
        else:report['stop_reason']='Allocated finite batch finished without success claim; actual final state is available for autonomous continuation'
        if 'jac' in locals():del jac
        if 'rr' in locals():del rr,dd
        del residual,data
        gc.collect()
        residual,data=objective(vector);report['final']=diag(vector,data)
        report['final_locations']=residual_locations(problem,vector,data,data['codazzi_complement_result'],args.curvature_cap)
        report['field']=checkpoint(vector,'-field.npz',dict(full_gauss_nodes=data['full_gauss'],codazzi_cells=data['codazzi_cells'],
            omitted_codazzi_cells=data['codazzi_complement_result']['omitted_codazzi_cells'],
            legacy_trapezoid_codazzi_cells=data['legacy_trapezoid_codazzi_cells']))
        _,p=problem.unpack(vector);problem.profile.set_parameters(p[problem.profile_parameter_slice])
        gp=stem.with_name(stem.name+'-physical-metric.json')
        gp.write_text(json.dumps(problem.profile.definition(),indent=2)+'\n')
        report['actual_physical_metric']=identity(gp)
        report['coast_reference_cache_statistics_at_close']=problem.coast_reference.cache_statistics()
        if args.reference_cache is not None and args.reference_cache.exists():
            report['old_mixed_reference_cache_provenance']=identity(args.reference_cache)
            report['old_mixed_reference_cache_used_for_new_atlas']=False
        report['central_definition']=problem.core(p[:problem.K])[0].definition()
        report['completed']=True;save()
        event('complete',finite_success=report['finite_success'],owner_stop=report['owner_stop'],
            stop_reason=report['stop_reason'],diagnostics=report['final'])
        return 130 if report['owner_stop'] else 0
    except Exception as exc:
        report['exception']=dict(type=type(exc).__name__,message=str(exc),traceback=traceback.format_exc())
        save();event('exception',type=type(exc).__name__,message=str(exc));raise


if __name__=='__main__':raise SystemExit(main())
