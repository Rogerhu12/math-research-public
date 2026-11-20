#!/usr/bin/env python3
"""Complete DoubleIntegrated H2-type Gram LM in a current geometric tangent slice.

All original variables, A/E/D defects, endpoint constraints and Gram rows stay.
The positive norm weights A and E in radial L2 and D/h in radial L2, with the
same angular factor sqrt(1+nu**2).  It controls the scale of cellwise second
jets without claiming an exact geometric bending energy.  The physical coarse
columns are whitened in that same integrated norm, never by weak Gram columns.
This is a new step norm; the nonlinear fixed-metric equations are unchanged.
"""
import argparse
import hashlib
import importlib.util
import json
from pathlib import Path
import sys
import time
import numpy as np
from scipy.sparse.linalg import LinearOperator, lsmr
from scipy.linalg import solve_triangular

def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()

def load(name,path):
    spec=importlib.util.spec_from_file_location(name,path)
    module=importlib.util.module_from_spec(spec)
    sys.modules[name]=module
    spec.loader.exec_module(module)
    return module

def event(**values):
    print(json.dumps(values),flush=True)

def point_geometry(problem,x):
    """Actual common-quintic six jets at every existing node/midpoint angle."""
    p=problem.prepare(x);maximum=-1.;where=None;minimum_area=float('inf')
    maximum_radius=0.;radius_where=None
    for stage in range(problem.P):
        z=problem.six_jets(p,stage)
        radius=np.linalg.norm(z['F'],axis=1)
        kr=int(np.argmax(radius))
        if radius[kr]>maximum_radius:
            maximum_radius=float(radius[kr])
            radius_where=dict(stage=stage,s=float(problem.times[stage]),phi=float(problem.phi[kr]))
        V,d=z['Fs'],z['Fphi'];normal=np.cross(V,d)
        area=np.linalg.norm(normal,axis=1);minimum_area=min(minimum_area,float(area.min()))
        if not np.isfinite(area).all() or np.any(area<=0):
            return dict(complete=False,first_invalid_stage=stage,min_area=minimum_area)
        normal/=area[:,None]
        E=np.sum(V*V,axis=1);F=np.sum(V*d,axis=1);G=np.sum(d*d,axis=1)
        e=np.sum(z['Fss']*normal,axis=1);f=np.sum(z['Fsphi']*normal,axis=1);g=np.sum(z['Fphiphi']*normal,axis=1)
        determinant=area*area
        trace=(e*G+g*E-2*f*F)/determinant;gauss=(e*g-f*f)/determinant
        k=(np.abs(trace)+np.sqrt(np.maximum(0.,trace*trace-4*gauss)))/2
        loc=int(np.argmax(k))
        if k[loc]>maximum:
            maximum=float(k[loc]);where=dict(stage=stage,s=float(problem.times[stage]),phi=float(problem.phi[loc]))
    return dict(complete=True,maximum_absolute_principal_curvature=maximum,
        closed_body_diameter_point_lower=2*maximum_radius,maximum_radius_point=radius_where,
        diameter_scope='Reflected closed body with pi symmetry and the declared axial phase family; D0 lower bound from actual +/-F point pairs, not a replacement by current Ft diameter',
        worst=where,min_area=minimum_area,evaluated_points=problem.P*problem.N,
        original_full_orbit_points=problem.P*getattr(problem,'full_N',problem.N),
        scope='All current nodes and common-quintic midpoints only; ordinary point values, not a continuous upper bound or reach certificate')

def coarse_norm(basis, coordinates):
    """Exact norm Gram of inverse(B)/scale, by separated coefficient channel."""
    h=coordinates.h;w=coordinates.w
    jets=basis.node_jets
    Y,U,A=jets[:,:,0],jets[:,:,1],jets[:,:,2]
    E=np.diff(U,axis=1)/h[None,:]-.5*(A[:,:-1]+A[:,1:])
    D=np.diff(Y,axis=1)/h[None,:]-.5*(U[:,:-1]+U[:,1:])
    radial=(A*w[None,:])@A.T+(E*h[None,:])@E.T+(D/h[None,:])@D.T
    gram=np.zeros((basis.dimension,basis.dimension))
    radial_index,channel=basis.pairs.T
    for j,(_,mode,_) in enumerate(basis.channels):
        indices=np.flatnonzero(channel==j)
        ri=radial_index[indices]
        gram[np.ix_(indices,indices)]=(1.+(2*mode)**2)*radial[np.ix_(ri,ri)]
    gram[-1,-1]+=1./coordinates.problem.width**2
    diagonal=np.sqrt(np.diag(gram))
    normalized=gram/diagonal[:,None]/diagonal[None,:]
    chol=np.linalg.cholesky(normalized)
    # One necessary check of this new separated norm implementation.
    # This does not repeat the already registered lift/transpose certificate.
    probe=np.sin(np.arange(basis.dimension)+.125)
    exact=coordinates.inverse(basis.free_direction(probe),affine=False)/coordinates.scale
    literal=float(exact@exact);separated=float(probe@gram@probe)
    difference=abs(literal-separated)/max(1.,abs(literal))
    if difference>2e-10:
        raise ValueError('New separated coarse-norm Gram disagrees with the actual coordinate norm')
    metadata=dict(norm='||DoubleIntegrated.inverse(B alpha, affine=False)/scale||^2',
        diagonal_min=float(diagonal.min()),diagonal_max=float(diagonal.max()),
        normalized_condition=float(np.linalg.cond(normalized)),
        separated_to_literal_probe_relative_difference=difference,
        whitening='R=diag(diagonal)^(-1) chol(normalized)^(-T); R^T G R=I',
        dimension=basis.dimension,geometry_calls=0)
    return diagonal,chol,metadata

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--repo',type=Path,required=True)
    parser.add_argument('--bundle',type=Path,required=True)
    parser.add_argument('--outdir',type=Path,required=True)
    parser.add_argument('--operator',type=Path)
    parser.add_argument('--implementation',type=Path)
    parser.add_argument('--basis-source',type=Path)
    parser.add_argument('--coarse-source',type=Path)
    parser.add_argument('--helpers',type=Path)
    parser.add_argument('--coordinate-source',type=Path)
    parser.add_argument('--scale-source',type=Path)
    parser.add_argument('--geometry-source',type=Path)
    parser.add_argument('--point-source',type=Path)
    parser.add_argument('--active-band',type=float,default=.025)
    parser.add_argument('--active-max-rows',type=int,default=16)
    parser.add_argument('--active-rank-tolerance',type=float,default=1e-10)
    parser.add_argument('--active-top-curvature',type=int,default=16)
    parser.add_argument('--active-top-radius',type=int,default=2)
    parser.add_argument('--angles',type=int,default=2048)
    parser.add_argument('--stage-block',type=int,default=64)
    parser.add_argument('--low-modes',type=int,default=3)
    parser.add_argument('--coarse-centers',type=str)
    parser.add_argument('--curvature-cap',type=float)
    parser.add_argument('--reach-ratio',type=float)
    parser.add_argument('--reach-safety-factor',type=float,default=.99)
    parser.add_argument('--max-directions',type=int,default=8)
    parser.add_argument('--maxiter',type=int,default=256)
    parser.add_argument('--damping',type=float,default=.01)
    parser.add_argument('--lsmr-atol',type=float,default=1e-6)
    parser.add_argument('--lsmr-btol',type=float,default=1e-6)
    parser.add_argument('--line-trials',type=int,default=15)
    parser.add_argument('--target',type=float,default=5e-7)
    args=parser.parse_args()
    repo=args.repo.resolve()
    topic=repo/'topics/visible-flex-larger-amplitude'
    args.bundle=args.bundle.resolve();args.outdir=args.outdir.resolve()
    paths=dict(
        operator=args.operator or topic/'notes/2026-11-17-parallel-geometry-fullclosed-gram-operator.py',
        implementation=args.implementation or topic/'scripts/resume_20261120_batched_closed_gram.py',
        basis=args.basis_source or topic/'scripts/resume_20261120_physical_subspace.py',
        coarse=args.coarse_source or topic/'scripts/resume_20261120_physical_subspace_v2.py',
        helpers=args.helpers or Path(__file__).resolve().with_name('fullclosed_lm.py'),
        coordinates=args.coordinate_source or topic/'notes/2026-11-17-parallel-root-fullclosed-integrated-coordinates.py',
        scale=args.scale_source or topic/'scripts/integrated_l2_scale_20261120.py',
        geometry=args.geometry_source or topic/'scripts/resume_20261120_curvature_qp.py',
        point=args.point_source or Path(__file__).resolve().with_name('fullclosed_point_cotangent.py'))
    paths={key:path.resolve() for key,path in paths.items()}
    if (args.max_directions<1 or args.maxiter<1
            or args.line_trials<1 or args.damping<=0 or args.target<=0):
        raise ValueError('Invalid declared full-space numerical parameters')
    if args.curvature_cap is not None and args.curvature_cap<=0:
        raise ValueError('A requested sampled curvature cap must be positive')
    if args.reach_ratio is None:
        raise ValueError('This active-geometry experiment requires an explicit reach ratio')
    if not 0<args.active_band<args.reach_safety_factor or args.active_max_rows<1 or not 0<args.active_rank_tolerance<1:
        raise ValueError('Invalid declared tangent-row selection or numerical rank cutoff')
    if args.reach_ratio is not None and args.reach_ratio<=0:
        raise ValueError('A requested reach ratio must be positive')
    if not 0<args.reach_safety_factor<1:
        raise ValueError('The numerical reach-screening safety factor must lie between zero and one')
    centers=None if args.coarse_centers is None else [float(t) for t in args.coarse_centers.split(',')]
    if centers is not None and (not centers or not np.isfinite(centers).all()):
        raise ValueError('Coarse centers must be a finite nonempty list')
    if args.outdir.exists():
        raise FileExistsError('Choose a new output directory; do not overwrite a prior numerical budget')
    args.outdir.mkdir(parents=True)
    helper=load('integrated_h2_full_gram_helpers',paths['helpers'])
    implementation=load('integrated_h2_full_gram_implementation',paths['implementation'])
    coarse_module=load('integrated_h2_full_gram_coarse',paths['coarse'])
    geometry_module=load('full_free_active_geometry',paths['geometry'])
    point_module=load('full_free_point_cotangent',paths['point'])
    data=np.load(args.bundle,allow_pickle=False)
    M=(data['qjets'].shape[-1]-2)//3
    problem=implementation.create(paths['operator'],data['mesh'],data['a_stages'],
        float(data['radius']),data['fixed_core_first3'],M=M,N=args.angles,
        width=float(data['width']),stage_block=args.stage_block,quarter=True)
    x,affine=problem.pack(data['qjets'],float(data['Hcap']),require_affine=True)
    options=dict(low_modes=args.low_modes)
    if centers is not None:
        options['desired_centers']=centers
    basis=coarse_module.make_space(paths['basis'],problem,**options)
    coordinate_module=load('h2_full_gram_coordinates',paths['coordinates'])
    scale_module=load('h2_full_gram_scale',paths['scale'])
    norm_scale=scale_module.make_scale(problem)
    nc0=problem.M-problem.K;na0=2*problem.M+1
    nai=(problem.J-2)*problem.n;ne=(problem.J-1)*problem.n
    at=nc0+na0+nai+ne
    norm_scale[at:at+ne].reshape(problem.J-1,problem.n)[:]*=np.diff(problem.mesh)[:,None]
    coordinates=coordinate_module.DoubleIntegrated(problem,scale=norm_scale)
    if not np.isfinite(norm_scale).all() or not np.all(norm_scale>0):
        raise ValueError('The declared complete H2-type scale must be finite and positive')
    coarse_diagonal,coarse_chol,coarse_metadata=coarse_norm(basis,coordinates)
    def coarse_lift(v):
        coefficients=solve_triangular(coarse_chol.T,v,lower=False)/coarse_diagonal
        return basis.free_direction(coefficients)
    def coarse_transpose(g):
        return solve_triangular(coarse_chol,basis.transpose_free(g)/coarse_diagonal,lower=True)
    def lift(v):
        return coordinates.lift(v[:coordinates.size])+coarse_lift(v[coordinates.size:])
    def transpose(g):
        return np.r_[coordinates.pullback(g),coarse_transpose(g)]
    full_N=getattr(problem,'full_N',problem.N)
    normalizer=problem.P*full_N
    weight=np.array([1.,np.sqrt(2),1.])/np.sqrt(normalizer)
    shape=(problem.P,problem.N,3)
    n=problem.free_size;ni=coordinates.size;nc=int(basis.dimension)
    report=dict(schema='fullclosed-integrated-H2-projected-LM-20261120-v4',
        source_sha256=sha(__file__),source_paths={k:str(v)for k,v in paths.items()},
        source_sha256_by_role={k:sha(v)for k,v in paths.items()},
        diameter_diagnostic_source=str(topic/'scripts/read_closed_residual_spectrum_20261120.py'),
        diameter_diagnostic_sha256=sha(topic/'scripts/read_closed_residual_spectrum_20261120.py'),
        bundle_sha256=sha(args.bundle),input_bundle=str(args.bundle),
        M=M,N=full_N,J=problem.J,original_variables=n,coarse_variables=nc,
        integrated_variables=ni,augmented_variables=ni+nc,original_full_rows=3*normalizer,
        evaluated_orbit_rows=3*problem.P*problem.N,affine=affine,
        minimum_mesh_cell=float(np.min(np.diff(problem.mesh))),
        maximum_mesh_cell=float(np.max(np.diff(problem.mesh))),
        coordinate_map='T(zi,zc)=DoubleIntegrated.lift(zi)+B R zc; all original A/E/D and exact-model endpoint rows retained',
        adjoint_map='T^T(g)=(DoubleIntegrated.pullback(g),R^T B^T g)',
        objective='||W(R(x)+J(x)T Pz)||^2+mu^2||z||^2; P is the current selected homogeneous active-geometry tangent projector',
        projection_scope='Only the current update is restricted to a selected tangent slice. Original nonlinear field coordinates and every original Gram equation remain; no current field modes are frozen',
        active_band=args.active_band,active_max_rows=args.active_max_rows,
        active_rank_tolerance=args.active_rank_tolerance,active_top_curvature=args.active_top_curvature,
        active_top_radius=args.active_top_radius,
        step_norm_note='H2-type integrated norm differs from earlier local or L2 norms. Coarse columns are orthonormal in this same norm, so augmentation lowers its induced squared norm by at most a factor two',
        scale_formula='A=1/sqrt(w*(1+nu^2)); E=1/sqrt(h*(1+nu^2)); D=sqrt(h)/sqrt(1+nu^2); core=1/(1+nu^2); H=width',
        coordinate_preparation=coordinates.metadata(),coarse_norm=coarse_metadata,
        coarse_low_modes=args.low_modes,requested_coarse_centers=centers,
        actual_coarse_center_nodes=basis.center_nodes,
        sampled_curvature_cap=args.curvature_cap,
        requested_reach_ratio=args.reach_ratio,numerical_reach_safety_factor=args.reach_safety_factor,
        necessary_reference_diameter_lower_bound='max(2,2*abs(H),2*max_sample|F|); actual body +/-F pairs under pi symmetry plus mirror, inherited by the declared axial phase family',
        curvature_cap_scope='Additional numerical pointwise trial filter only. This is not a continuous curvature or reach certificate. The theorem uses D of the reference family member, not each current surface diameter',
        row_scope='Original finite stage/angle equations, exactly represented by weighted quarter orbits',

        max_directions=args.max_directions,max_lsmr_iterations=args.maxiter,
        initial_damping=args.damping,lsmr_atol=args.lsmr_atol,lsmr_btol=args.lsmr_btol,
        target=args.target,max_line_trials=args.line_trials,directions=[],
        continuous_geometry_certified=False,closed_isometry_accepted=False)
    output=args.outdir/'report.json'
    def save():
        output.write_text(json.dumps(report,indent=2)+'\n')
    def save_bundle(path,point):
        jets,height,_=problem.unpack(point)
        keys=('mesh','a_stages','radius','width','fixed_core_first3',
              'a_stage_absolute_error','stage_time_absolute_error')
        arrays={key:np.array(data[key])for key in keys if key in data.files}
        arrays.update(qjets=jets,Hcap=np.array(height))
        np.savez_compressed(path,**arrays)
    def curvature_filter(point,curvature):
        _,height,_=problem.unpack(point)
        diameter_lower=max(2.,2*abs(float(height)),curvature.get('closed_body_diameter_point_lower',0.))
        cap=args.curvature_cap
        if args.reach_ratio is not None:
            dynamic=args.reach_safety_factor/(args.reach_ratio*diameter_lower)
            cap=dynamic if cap is None else min(cap,dynamic)
        value=curvature.get('maximum_absolute_principal_curvature',float('inf'))
        passed=bool(curvature['complete'] and (cap is None or value<=cap))
        return dict(passed=passed,height=float(height),
            reference_diameter_lower_bound=diameter_lower,applied_curvature_cap=cap,
            sampled_curvature=value,
            necessary_reach_product=None if args.reach_ratio is None else args.reach_ratio*diameter_lower*value,
            scope='Necessary numerical point screen for the declared mirrored phase family only; no continuous reach certification')
    residual=problem.residual(x)
    report['initial']=helper.statistics(problem,x,residual)
    report['initial_curvature_points']=point_geometry(problem,x)
    report['initial_curvature_filter']=curvature_filter(x,report['initial_curvature_points'])
    save();event(event='projected_h2_initial',statistics=report['initial'],
        curvature_points=report['initial_curvature_points'])
    damping=args.damping
    for index in range(args.max_directions):
        if not report['initial_curvature_filter']['passed']:
            report['stopped_before_linear_iteration']='Initial point fails the declared necessary curvature filter; select an actually qualifying parent'
            break
        current=report.get('current',report['initial'])
        if current['max_relative_gram']<=args.target:
            break
        started=time.monotonic()
        cache=problem.set_base(x)
        project,active_rows,Q,active_metadata,active_locations=point_module.build_tangent_projector(
            problem,x,geometry_module,transpose,ni+nc,reach_ratio=args.reach_ratio,
            safety=args.reach_safety_factor,active_band=args.active_band,
            max_rows=args.active_max_rows,rank_tolerance=args.active_rank_tolerance,
            top_curvature=args.active_top_curvature,top_radius=args.active_top_radius)
        if index==0:
            report['new_point_transpose_checks']=point_module.derivative_checks(problem,x,geometry_module,
                helper.local_scale(problem),active_locations[0])
            save()
        event(event='active_projector_ready',direction=index,selected=active_metadata['selected_rows'],
            rank=active_metadata['retained_rank'],orthogonality=active_metadata['orthonormal_rows_error'])
        rhs=-(residual*weight).ravel()
        counts=dict(jvp=0,vjp=0)
        def matvec(v):
            counts['jvp']+=1
            result=(problem.jvp(x,lift(project(v)))*weight).ravel()
            if counts['jvp']%16==0:
                event(event='projected_h2_linear_progress',direction=index,
                    jvp=counts['jvp'],vjp=counts['vjp'],seconds=time.monotonic()-started)
            return result
        def rmatvec(v):
            counts['vjp']+=1
            return project(transpose(problem.vjp(x,v.reshape(shape)*weight)))
        A=LinearOperator((rhs.size,ni+nc),matvec=matvec,rmatvec=rmatvec,dtype=np.float64)
        solution=lsmr(A,rhs,damp=damping,atol=args.lsmr_atol,
            btol=args.lsmr_btol,maxiter=args.maxiter,show=False)
        coordinate_step=project(solution[0])
        step=lift(coordinate_step)
        djet,dheight,_=problem.unpack(step,tangent=True)
        jstep=problem.jvp(x,step)
        old_merit=float(rhs@rhs)
        slope=float(np.sum((residual*weight)*(jstep*weight)))
        linear_merit=float(np.sum(((residual+jstep)*weight)**2))
        integrated_point=coordinates.scale*coordinates.project(coordinate_step[:ni])
        projected_endpoint_error=float(np.max(np.abs(coordinates.endpoint(integrated_point))))
        record=dict(index=index,damping=damping,projected_endpoint_error=projected_endpoint_error,
            active_geometry=active_metadata,
            normalized_active_linear_residuals=(active_rows@coordinate_step).tolist(),
            projected_coordinate_norm=float(np.linalg.norm(coordinate_step)),
            final_projection_change_norm=float(np.linalg.norm(coordinate_step-solution[0])),
            restoration='z0=0; homogeneous compatible tangency at an already screened parent',
            cache=cache,inner_counts=counts.copy(),
            outside_inner_calls=dict(postsolve_jvp=1),
            lsmr_stop=int(solution[1]),lsmr_iterations=int(solution[2]),
            lsmr_normr=float(solution[3]),lsmr_normar=float(solution[4]),
            lsmr_normA=float(solution[5]),lsmr_condA=float(solution[6]),lsmr_normx=float(solution[7]),
            old_merit=old_merit,half_objective_slope=slope,
            linear_residual_merit=linear_merit,
            nodal_jet_step_max_by_Y_U_A=np.max(np.abs(djet),axis=(0,2)).tolist(),
            height_step=float(dheight),accepted=False,trials=[],
            preparation_and_linear_seconds=time.monotonic()-started)
        checkpoint=args.outdir/f'direction-{index:03d}.npz'
        np.savez_compressed(checkpoint,step=step,augmented_step=coordinate_step,
            integrated_scale=coordinates.scale,coarse_diagonal=coarse_diagonal,coarse_cholesky=coarse_chol)
        record['direction_sha256']=sha(checkpoint)
        del solution,jstep,A,rhs,djet,integrated_point,coordinate_step,active_rows,Q
        event(event='projected_h2_direction_ready',direction=index,
            lsmr_stop=record['lsmr_stop'],iterations=record['lsmr_iterations'],
            old_merit=old_merit,linear_merit=linear_merit,slope=slope)
        alpha=1.
        for trial_index in range(args.line_trials):
            point=x+alpha*step
            error=None
            try:
                trial_residual=problem.residual(point)
                finite=bool(np.isfinite(trial_residual).all())
                stats=helper.statistics(problem,point,trial_residual) if finite else {}
            except (FloatingPointError,OverflowError) as exception:
                trial_residual=None;finite=False;stats={};error=repr(exception)
            merit=stats.get('raw_frobenius_sse',float('inf'))/normalizer
            feasible=(finite and stats['rho_sample_min']>0 and
                      stats['min_relative_E']>0 and stats['min_relative_determinant']>0)
            descent=merit<old_merit and (slope>=0 or merit<=old_merit+2e-4*alpha*slope)
            curvature=None;curvature_feasible=True;filter_result=None
            if feasible and descent and (args.curvature_cap is not None or args.reach_ratio is not None):
                curvature=point_geometry(problem,point)
                filter_result=curvature_filter(point,curvature)
                curvature_feasible=filter_result['passed']
            trial=dict(index=trial_index,alpha=alpha,merit=merit,finite=finite,
                feasible=feasible,descent=descent,curvature_feasible=curvature_feasible,
                curvature_points=curvature,curvature_filter=filter_result,statistics=stats,arithmetic_error=error)
            record['trials'].append(trial)
            event(event='projected_h2_actual_trial',direction=index,**trial)
            if feasible and descent and curvature_feasible:
                x=point;residual=trial_residual
                record.update(accepted=True,accepted_alpha=alpha,new_merit=merit)
                report['current']=stats
                record['accepted_curvature_points']=curvature if curvature is not None else point_geometry(problem,x)
                record['accepted_curvature_filter']=curvature_filter(x,record['accepted_curvature_points'])
                candidate=args.outdir/f'accepted-{index:03d}.npz'
                save_bundle(candidate,x)
                record.update(accepted_bundle=str(candidate),accepted_bundle_sha256=sha(candidate))
                predicted=old_merit-linear_merit
                ratio=(old_merit-merit)/predicted if predicted>0 else None
                record['actual_to_full_step_predicted_decrease']=ratio
                if alpha==1 and ratio is not None and ratio>.75:
                    damping=max(1e-8,damping/2)
                break
            alpha/=2
        if not record['accepted']:
            damping*=4
        record['seconds']=time.monotonic()-started
        report['directions'].append(record);save()
        problem.clear_base()
        del step
    report['complete']=True
    report['sample_target_reached']=report.get('current',report['initial'])['max_relative_gram']<=args.target
    report['sample_target']=report['sample_target_reached']
    final_geometry=report['directions'][-1].get('accepted_curvature_points') if report['directions'] else None
    if final_geometry is None:
        final_geometry=point_geometry(problem,x)
    report['final_curvature_filter']=curvature_filter(x,final_geometry)
    report['limitations']='Finite node/midpoint metric and curvature point values only. No continuous metric, reach, held/E3, all-t, or fixed-g mesh/frequency refinement certificate.'
    final=args.outdir/'final.npz'
    save_bundle(final,x)
    report.update(final_bundle=str(final),final_bundle_sha256=sha(final))
    save()
    event(event='projected_h2_numerical_batch_complete',report=str(output),
        final_bundle=str(final),sample_target=report['sample_target'],
        statistics=report.get('current',report['initial']))

if __name__=='__main__':
    main()
