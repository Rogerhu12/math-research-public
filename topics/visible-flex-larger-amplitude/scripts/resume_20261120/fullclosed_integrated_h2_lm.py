#!/usr/bin/env python3
"""Complete DoubleIntegrated H2-type Gram LM with physical coarse columns.

All original variables, A/E/D defects, endpoint constraints and Gram rows stay.
The positive norm weights A and E in radial L2 and D/h in radial L2, with the
same angular factor sqrt(1+nu**2).  It controls the scale of cellwise second
jets without claiming an exact geometric bending energy.  The 173 coarse
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
    parser.add_argument('--angles',type=int,default=2048)
    parser.add_argument('--stage-block',type=int,default=64)
    parser.add_argument('--low-modes',type=int,default=3)
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
        scale=args.scale_source or topic/'scripts/integrated_l2_scale_20261120.py')
    paths={key:path.resolve() for key,path in paths.items()}
    if (args.max_directions<1 or args.maxiter<1
            or args.line_trials<1 or args.damping<=0 or args.target<=0):
        raise ValueError('Invalid declared full-space numerical parameters')
    if args.outdir.exists():
        raise FileExistsError('Choose a new output directory; do not overwrite a prior numerical budget')
    args.outdir.mkdir(parents=True)
    helper=load('integrated_h2_full_gram_helpers',paths['helpers'])
    implementation=load('integrated_h2_full_gram_implementation',paths['implementation'])
    coarse_module=load('integrated_h2_full_gram_coarse',paths['coarse'])
    data=np.load(args.bundle,allow_pickle=False)
    M=(data['qjets'].shape[-1]-2)//3
    problem=implementation.create(paths['operator'],data['mesh'],data['a_stages'],
        float(data['radius']),data['fixed_core_first3'],M=M,N=args.angles,
        width=float(data['width']),stage_block=args.stage_block,quarter=True)
    x,affine=problem.pack(data['qjets'],float(data['Hcap']),require_affine=True)
    basis=coarse_module.make_space(paths['basis'],problem,low_modes=args.low_modes)
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
    report=dict(schema='fullclosed-integrated-H2-augmented-LM-20261120-v1',
        source_sha256=sha(__file__),source_paths={k:str(v)for k,v in paths.items()},
        source_sha256_by_role={k:sha(v)for k,v in paths.items()},
        bundle_sha256=sha(args.bundle),input_bundle=str(args.bundle),
        M=M,N=full_N,J=problem.J,original_variables=n,coarse_variables=nc,
        integrated_variables=ni,augmented_variables=ni+nc,original_full_rows=3*normalizer,
        evaluated_orbit_rows=3*problem.P*problem.N,affine=affine,
        minimum_mesh_cell=float(np.min(np.diff(problem.mesh))),
        maximum_mesh_cell=float(np.max(np.diff(problem.mesh))),
        coordinate_map='T(zi,zc)=DoubleIntegrated.lift(zi)+B R zc; all original A/E/D and exact-model endpoint rows retained',
        adjoint_map='T^T(g)=(DoubleIntegrated.pullback(g),R^T B^T g)',
        objective='||W(R(x)+J(x)Tz)||^2+mu^2||z||^2; W includes Frobenius and full-grid normalization',
        step_norm_note='H2-type integrated norm differs from earlier local or L2 norms. Coarse columns are orthonormal in this same norm, so augmentation lowers its induced squared norm by at most a factor two',
        scale_formula='A=1/sqrt(w*(1+nu^2)); E=1/sqrt(h*(1+nu^2)); D=sqrt(h)/sqrt(1+nu^2); core=1/(1+nu^2); H=width',
        coordinate_preparation=coordinates.metadata(),coarse_norm=coarse_metadata,
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
    residual=problem.residual(x)
    report['initial']=helper.statistics(problem,x,residual)
    report['initial_curvature_points']=helper.point_curvatures(problem,x)
    save();event(event='integrated_h2_initial',statistics=report['initial'],
        curvature_points=report['initial_curvature_points'])
    damping=args.damping
    for index in range(args.max_directions):
        current=report.get('current',report['initial'])
        if current['max_relative_gram']<=args.target:
            break
        started=time.monotonic()
        cache=problem.set_base(x)
        rhs=-(residual*weight).ravel()
        counts=dict(jvp=0,vjp=0)
        def matvec(v):
            counts['jvp']+=1
            result=(problem.jvp(x,lift(v))*weight).ravel()
            if counts['jvp']%16==0:
                event(event='integrated_h2_linear_progress',direction=index,
                    jvp=counts['jvp'],vjp=counts['vjp'],seconds=time.monotonic()-started)
            return result
        def rmatvec(v):
            counts['vjp']+=1
            return transpose(problem.vjp(x,v.reshape(shape)*weight))
        A=LinearOperator((rhs.size,ni+nc),matvec=matvec,rmatvec=rmatvec,dtype=np.float64)
        solution=lsmr(A,rhs,damp=damping,atol=args.lsmr_atol,
            btol=args.lsmr_btol,maxiter=args.maxiter,show=False)
        step=lift(solution[0])
        djet,dheight,_=problem.unpack(step,tangent=True)
        jstep=problem.jvp(x,step)
        old_merit=float(rhs@rhs)
        slope=float(np.sum((residual*weight)*(jstep*weight)))
        linear_merit=float(np.sum(((residual+jstep)*weight)**2))
        integrated_point=coordinates.scale*coordinates.project(solution[0][:ni])
        projected_endpoint_error=float(np.max(np.abs(coordinates.endpoint(integrated_point))))
        record=dict(index=index,damping=damping,projected_endpoint_error=projected_endpoint_error,
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
        np.savez_compressed(checkpoint,step=step,augmented_step=solution[0],
            integrated_scale=coordinates.scale,coarse_diagonal=coarse_diagonal,coarse_cholesky=coarse_chol)
        record['direction_sha256']=sha(checkpoint)
        del solution,jstep,A,rhs,djet,integrated_point
        event(event='integrated_h2_direction_ready',direction=index,
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
            trial=dict(index=trial_index,alpha=alpha,merit=merit,finite=finite,
                feasible=feasible,descent=descent,statistics=stats,arithmetic_error=error)
            record['trials'].append(trial)
            event(event='integrated_h2_actual_trial',direction=index,**trial)
            if feasible and descent:
                x=point;residual=trial_residual
                record.update(accepted=True,accepted_alpha=alpha,new_merit=merit)
                report['current']=stats
                record['accepted_curvature_points']=helper.point_curvatures(problem,x)
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
    report['limitations']='Finite node/midpoint metric and curvature point values only. No continuous metric, reach, held/E3, all-t, or fixed-g mesh/frequency refinement certificate.'
    final=args.outdir/'final.npz'
    save_bundle(final,x)
    report.update(final_bundle=str(final),final_bundle_sha256=sha(final))
    save()
    event(event='integrated_h2_numerical_batch_complete',report=str(output),
        final_bundle=str(final),sample_target=report['sample_target'],
        statistics=report.get('current',report['initial']))

if __name__=='__main__':
    main()
