#!/usr/bin/env python3
"""Column-equilibrated full Gram LM augmented by a physical coarse space.

The original free space and every original angle-value residual are retained.
Sixteen deterministic Rademacher adjoint probes estimate a positive diagonal
coordinate scale.  The coarse columns are normalized by their actual complete
Gram diagonal.  This changes the LM step norm, not the nonlinear equations.

This source was prepared after local execution became unavailable.  Its first
scientific execution must be recorded separately; no convergence is assumed.
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

def equilibrate(problem,x,base_scale,weight,*,seed,probes,floor_relative):
    """Estimate diag((W J S0)^T(W J S0)); never remove a coordinate."""
    if probes!=16 or seed<0 or not 0<floor_relative<1:
        raise ValueError('This declared experiment uses sixteen probes and a positive relative floor')
    clock=time.monotonic()
    rng=np.random.default_rng(seed)
    diagonal=np.zeros(problem.free_size)
    records=[]
    shape=(problem.P,problem.N,3)
    for j in range(probes):
        signs=rng.integers(0,2,size=shape,dtype=np.int8)
        weights=(2.*signs-1.)*weight
        g=base_scale*problem.vjp(x,weights)
        if not np.isfinite(g).all():
            raise FloatingPointError('Nonfinite current-point column probe')
        diagonal+=g*g/probes
        records.append(dict(index=j,squared_norm=float(g@g),maximum_absolute=float(np.max(np.abs(g)))))
        event(event='column_probe',index=j+1,total=probes,seconds=time.monotonic()-clock)
    maximum=float(diagonal.max())
    if not np.isfinite(maximum) or maximum<=0:
        raise ValueError('No finite positive current Jacobian diagonal estimate')
    floor=max(maximum*floor_relative,np.finfo(float).tiny)
    clipped=np.maximum(diagonal,floor)
    gain=1./np.sqrt(clipped)
    scale=base_scale*gain
    if not np.isfinite(scale).all() or not np.all(scale>0):
        raise FloatingPointError('Equilibrated coordinate scales are not finite and positive')
    return scale,diagonal,dict(seed=seed,probes=probes,
        distribution='independent Rademacher signs on every retained weighted orbit row',
        estimator='mean((S0 J^T W xi)^2)',
        diagonal_min=float(diagonal.min()),diagonal_max=maximum,
        floor_relative=floor_relative,floor_absolute=floor,
        floor_applied_count=int(np.count_nonzero(diagonal<floor)),
        gain_min=float(gain.min()),gain_max=float(gain.max()),
        resulting_scale_min=float(scale.min()),resulting_scale_max=float(scale.max()),
        seconds=time.monotonic()-clock,probe_records=records,
        scope='Stochastic numerical preconditioner only; no deterministic diagonal enclosure is asserted')

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
    parser.add_argument('--angles',type=int,default=2048)
    parser.add_argument('--stage-block',type=int,default=64)
    parser.add_argument('--low-modes',type=int,default=3)
    parser.add_argument('--max-directions',type=int,default=8)
    parser.add_argument('--maxiter',type=int,default=256)
    parser.add_argument('--damping',type=float,default=.01)
    parser.add_argument('--seed',type=int,default=2026112001)
    parser.add_argument('--probes',type=int,default=16)
    parser.add_argument('--diagonal-floor',type=float,default=1e-12)
    parser.add_argument('--coarse-diagonal-floor',type=float,default=1e-12)
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
        helpers=args.helpers or Path(__file__).resolve().with_name('fullclosed_lm.py'))
    paths={key:path.resolve() for key,path in paths.items()}
    if (args.probes!=16 or args.max_directions<1 or args.maxiter<1
            or args.line_trials<1 or args.damping<=0 or args.target<=0):
        raise ValueError('Invalid declared full-space numerical parameters')
    if not 0<args.coarse_diagonal_floor<1:
        raise ValueError('Need a strictly positive coarse diagonal floor')
    if args.outdir.exists():
        raise FileExistsError('Choose a new output directory; do not overwrite a prior numerical budget')
    args.outdir.mkdir(parents=True)
    helper=load('equilibrated_full_gram_helpers',paths['helpers'])
    implementation=load('equilibrated_full_gram_implementation',paths['implementation'])
    coarse_module=load('equilibrated_full_gram_coarse',paths['coarse'])
    data=np.load(args.bundle,allow_pickle=False)
    M=(data['qjets'].shape[-1]-2)//3
    problem=implementation.create(paths['operator'],data['mesh'],data['a_stages'],
        float(data['radius']),data['fixed_core_first3'],M=M,N=args.angles,
        width=float(data['width']),stage_block=args.stage_block,quarter=True)
    x,affine=problem.pack(data['qjets'],float(data['Hcap']),require_affine=True)
    basis=coarse_module.make_space(paths['basis'],problem,low_modes=args.low_modes)
    base_scale=helper.local_scale(problem)
    if base_scale.shape!=x.shape or not np.all(base_scale>0):
        raise ValueError('Original positive free-coordinate scale has wrong shape')
    full_N=getattr(problem,'full_N',problem.N)
    normalizer=problem.P*full_N
    weight=np.array([1.,np.sqrt(2),1.])/np.sqrt(normalizer)
    shape=(problem.P,problem.N,3)
    n=problem.free_size;nc=int(basis.dimension)
    report=dict(schema='fullclosed-equilibrated-augmented-LM-20261120-v1',
        source_sha256=sha(__file__),source_paths={k:str(v)for k,v in paths.items()},
        source_sha256_by_role={k:sha(v)for k,v in paths.items()},
        bundle_sha256=sha(args.bundle),input_bundle=str(args.bundle),
        M=M,N=full_N,J=problem.J,original_variables=n,coarse_variables=nc,
        augmented_variables=n+nc,original_full_rows=3*normalizer,
        evaluated_orbit_rows=3*problem.P*problem.N,affine=affine,
        minimum_mesh_cell=float(np.min(np.diff(problem.mesh))),
        maximum_mesh_cell=float(np.max(np.diff(problem.mesh))),
        coordinate_map='T(zf,zc)=S_local*zf+B(S_coarse*zc); every original free coordinate remains',
        adjoint_map='T^T(g)=(S_local*g,S_coarse*B^T(g))',
        objective='||W(R(x)+J(x)Tz)||^2+mu^2||z||^2; W includes Frobenius and full-grid normalization',
        step_norm_note='New redundant augmented coordinates change the LM step norm; no equality with previous Euclidean or integrated step norms is claimed',
        row_scope='Original finite stage/angle equations, exactly represented by weighted quarter orbits',
        probe_seed=args.seed,probe_count=args.probes,diagonal_floor_relative=args.diagonal_floor,
        coarse_diagonal_floor_relative=args.coarse_diagonal_floor,
        same_probe_seed_at_each_current_point=True,
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
    save();event(event='augmented_initial',statistics=report['initial'],
        curvature_points=report['initial_curvature_points'])
    damping=args.damping
    for index in range(args.max_directions):
        current=report.get('current',report['initial'])
        if current['max_relative_gram']<=args.target:
            break
        started=time.monotonic()
        cache=problem.set_base(x)
        scale,diagonal,probe=equilibrate(problem,x,base_scale,weight,
            seed=args.seed,probes=args.probes,floor_relative=args.diagonal_floor)
        coarse_state=basis.evaluate(problem._base_first,problem._base_p.rho,
            np.zeros(nc),linearize=True)
        G=np.asarray(coarse_state['normal_matrix'])/normalizer
        dB=np.diag(G).copy()
        if dB.shape!=(nc,) or not np.isfinite(dB).all() or dB.max()<=0:
            raise ValueError('No finite positive actual coarse Gram diagonal')
        floorB=max(float(dB.max())*args.coarse_diagonal_floor,np.finfo(float).tiny)
        scaleB=1/np.sqrt(np.maximum(dB,floorB))
        coarse_metadata=dict(diagonal_min=float(dB.min()),diagonal_max=float(dB.max()),
            floor_relative=args.coarse_diagonal_floor,floor_absolute=floorB,
            floor_applied_count=int(np.count_nonzero(dB<floorB)),
            scale_min=float(scaleB.min()),scale_max=float(scaleB.max()),
            raw_sse=coarse_state.get('raw_sse'),dimension=nc)
        def lift(v):
            return scale*v[:n]+basis.free_direction(scaleB*v[n:])
        def transpose(g):
            return np.r_[scale*g,scaleB*basis.transpose_free(g)]
        rhs=-(residual*weight).ravel()
        counts=dict(jvp=0,vjp=0)
        def matvec(v):
            counts['jvp']+=1
            result=(problem.jvp(x,lift(v))*weight).ravel()
            if counts['jvp']%16==0:
                event(event='augmented_linear_progress',direction=index,
                    jvp=counts['jvp'],vjp=counts['vjp'],seconds=time.monotonic()-started)
            return result
        def rmatvec(v):
            counts['vjp']+=1
            return transpose(problem.vjp(x,v.reshape(shape)*weight))
        A=LinearOperator((rhs.size,n+nc),matvec=matvec,rmatvec=rmatvec,dtype=np.float64)
        solution=lsmr(A,rhs,damp=damping,atol=args.lsmr_atol,
            btol=args.lsmr_btol,maxiter=args.maxiter,show=False)
        step=lift(solution[0])
        djet,dheight,_=problem.unpack(step,tangent=True)
        jstep=problem.jvp(x,step)
        old_merit=float(rhs@rhs)
        slope=float(np.sum((residual*weight)*(jstep*weight)))
        linear_merit=float(np.sum(((residual+jstep)*weight)**2))
        record=dict(index=index,damping=damping,probe=probe,coarse_scaling=coarse_metadata,
            cache=cache,inner_counts=counts.copy(),
            outside_inner_calls=dict(diagonal_vjp=args.probes,postsolve_jvp=1),
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
            local_scale=scale,coarse_scale=scaleB,diagonal_estimate=diagonal)
        record['direction_sha256']=sha(checkpoint)
        del solution,jstep,A,rhs,diagonal,djet,G,coarse_state
        event(event='augmented_direction_ready',direction=index,
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
            event(event='augmented_actual_trial',direction=index,**trial)
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
        del step,scale,scaleB
    report['complete']=True
    report['sample_target_reached']=report.get('current',report['initial'])['max_relative_gram']<=args.target
    report['sample_target']=report['sample_target_reached']
    report['limitations']='Finite node/midpoint metric and curvature point values only. No continuous metric, reach, held/E3, all-t, or fixed-g mesh/frequency refinement certificate.'
    final=args.outdir/'final.npz'
    save_bundle(final,x)
    report.update(final_bundle=str(final),final_bundle_sha256=sha(final))
    save()
    event(event='augmented_numerical_batch_complete',report=str(output),
        final_bundle=str(final),sample_target=report['sample_target'],
        statistics=report.get('current',report['initial']))

if __name__=='__main__':
    main()
