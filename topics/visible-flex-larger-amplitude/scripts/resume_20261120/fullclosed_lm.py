#!/usr/bin/env python3
"""Complete finite angle-value Gram LM in positive scaled free coordinates.

This is a numerical solver for the documented shared-quintic/analytic-lift
model. It retains every original free variable, stage and angle residual.
Trials are still approximations, never complete geometric certificates.
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

def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def load(name,p):
    sp=importlib.util.spec_from_file_location(name,p);m=importlib.util.module_from_spec(sp)
    sys.modules[name]=m;sp.loader.exec_module(m);return m

def local_scale(problem):
    """Positive local H1-sized jet scales; a bijective coordinate change."""
    q=problem;h=np.diff(q.mesh);nodal=np.r_[h[0],(h[:-1]+h[1:])/2,h[-1]]
    freq=np.r_[2*np.arange(q.M+1),2*np.arange(1,q.M+1),2*np.arange(q.M+1)]
    ell=nodal[:,None]/np.sqrt(1+(nodal[:,None]*(1+freq))**2)
    jet=np.stack((ell,ell/nodal[:,None],ell/nodal[:,None]**2),axis=1)
    core=1/(1+q.freq[q.K:]**2)
    return np.r_[core,jet[0,2,:2*q.M+1],jet[1:-1].ravel(),q.width]

def statistics(problem,x,residual):
    physical=problem.unweight(residual) if hasattr(problem,'unweight') else residual
    e,f,g=physical[...,0],physical[...,1],physical[...,2]
    gram=(np.abs(e+g)+np.sqrt((e-g)**2+4*f*f))/2
    location=np.unravel_index(int(np.argmax(gram)),gram.shape)
    prepared=problem.prepare(x)
    derivative_bound=float(np.sum(np.abs(problem.freq*problem.qfreq*prepared.core)))
    return dict(max_relative_gram=float(gram[location]),worst_stage=int(location[0]),
        worst_s=float(problem.times[location[0]]),worst_phi=float(problem.phi[location[1]]),
        min_relative_determinant=float(np.min((1+e)*(1+g)-f*f)),
        min_relative_E=float(np.min(1+e)),rho_sample_min=float(np.min(prepared.rho)),
        rho_lipschitz_lower=float(np.min(prepared.rho)-np.pi/getattr(problem,'full_N',problem.N)*derivative_bound),
        ss_max=float(np.max(np.abs(e))),sphi_max=float(np.max(np.abs(f))),phiphi_max=float(np.max(np.abs(g))),
        raw_frobenius_sse=float(np.sum(residual[...,0]**2+2*residual[...,1]**2+residual[...,2]**2)))

def point_curvatures(problem,x):
    """Actual common-quintic six jets at every existing node/midpoint angle."""
    p=problem.prepare(x);maximum=-1.;where=None;minimum_area=float('inf')
    for stage in range(problem.P):
        z=problem.six_jets(p,stage)
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
        worst=where,min_area=minimum_area,evaluated_points=problem.P*problem.N,
        original_full_orbit_points=problem.P*getattr(problem,'full_N',problem.N),
        scope='All current nodes and common-quintic midpoints only; ordinary point values, not a continuous upper bound or reach certificate')

def main():
    p=argparse.ArgumentParser(description=__doc__)
    for key in ('operator','implementation','bundle','outdir'):
        p.add_argument('--'+key,type=Path,required=True)
    p.add_argument('--angles',type=int,default=2048)
    p.add_argument('--stage-block',type=int,default=64)
    p.add_argument('--full-angle-rows',action='store_true')
    p.add_argument('--max-directions',type=int,default=1)
    p.add_argument('--maxiter',type=int,default=128)
    p.add_argument('--damping',type=float,default=.001)
    p.add_argument('--lsmr-atol',type=float,default=1e-5)
    p.add_argument('--lsmr-btol',type=float,default=1e-5)
    p.add_argument('--line-trials',type=int,default=13)
    p.add_argument('--target',type=float,default=5e-7)
    a=p.parse_args()
    if a.outdir.exists():raise ValueError('Use a fresh output directory; inspect any old run before resuming')
    a.outdir.mkdir(parents=True)
    data=np.load(a.bundle,allow_pickle=False)
    module=load('fullclosed_current_implementation',a.implementation)
    M=(data['qjets'].shape[-1]-2)//3
    q=module.create(a.operator,data['mesh'],data['a_stages'],float(data['radius']),data['fixed_core_first3'],
        M=M,N=a.angles,width=float(data['width']),stage_block=a.stage_block,quarter=not a.full_angle_rows)
    x,affine=q.pack(data['qjets'],float(data['Hcap']),require_affine=True)
    scale=local_scale(q)
    if scale.shape!=x.shape or not np.all(scale>0):raise RuntimeError('Scale is not a positive bijective free coordinate change')
    full_N=getattr(q,'full_N',q.N)
    weight=np.array([1.,np.sqrt(2),1.])/np.sqrt(q.P*full_N)
    report=dict(schema='fullclosed-finite-Gram-LM-20261120-v1',
        source_sha256=sha(__file__),operator_sha256=sha(a.operator),implementation_sha256=sha(a.implementation),
        bundle_sha256=sha(a.bundle),input_bundle=str(a.bundle),M=M,N=a.angles,J=q.J,
        variables=q.free_size,rows=q.P*q.N*3,full_angle_rows=q.P*full_N*3,affine=affine,
        minimum_mesh_cell=float(np.min(np.diff(q.mesh))),maximum_mesh_cell=float(np.max(np.diff(q.mesh))),
        scale_formula='ell_i,k=h_i/sqrt(1+(h_i*(1+nu_k))^2); Y=ell,U=ell/h,A=ell/h^2; core=1/(1+nu^2); H=width',
        scale_min=float(scale.min()),scale_max=float(scale.max()),
        row_weight='Frobenius (1,sqrt(2),1)/sqrt(stage_count*full_angle_count); implementation preserves orbit multiplicity',
        max_directions=a.max_directions,max_lsmr_iterations=a.maxiter,
        lsmr_atol=a.lsmr_atol,lsmr_btol=a.lsmr_btol,
        initial_damping=a.damping,max_line_trials=a.line_trials,target=a.target,directions=[],
        continuous_geometry_certified=False,closed_isometry_accepted=False)
    output=a.outdir/'report.json'
    def save():output.write_text(json.dumps(report,indent=2)+'\n')
    def event(**kw):print(json.dumps(kw),flush=True)
    def candidate_bundle(path,xvalue):
        jets,height,_=q.unpack(xvalue)
        keys=['mesh','a_stages','radius','width','fixed_core_first3','a_stage_absolute_error','stage_time_absolute_error']
        arrays={k:np.array(data[k])for k in keys if k in data.files}
        arrays.update(qjets=jets,Hcap=np.array(height))
        np.savez_compressed(path,**arrays)
    clock=time.monotonic();r=q.residual(x);report['initial']=statistics(q,x,r)
    report['initial_curvature_points']=point_curvatures(q,x)
    report['initial_seconds']=time.monotonic()-clock;save();event(event='initial_complete_residual',**report['initial'])
    damping=a.damping
    for direction_index in range(a.max_directions):
        if report.get('current',report['initial'])['max_relative_gram']<=a.target:
            report['sample_target_reached']=True;break
        clock=time.monotonic();cache=q.set_base(x);rhs=-(r*weight).ravel()
        counts=dict(jvp=0,vjp=0);shape=(q.P,q.N,3)
        def matvec(v):
            counts['jvp']+=1
            out=(q.jvp(x,scale*v)*weight).ravel()
            if counts['jvp']%16==0:event(event='linear_progress',direction=direction_index,**counts,seconds=time.monotonic()-clock)
            return out
        def rmatvec(w):
            counts['vjp']+=1
            return scale*q.vjp(x,w.reshape(shape)*weight)
        A=LinearOperator((rhs.size,x.size),matvec=matvec,rmatvec=rmatvec,dtype=np.float64)
        sol=lsmr(A,rhs,damp=damping,atol=a.lsmr_atol,btol=a.lsmr_btol,maxiter=a.maxiter,show=False)
        step=scale*sol[0]
        step_jets,step_height,_=q.unpack(step,tangent=True)
        linear_step=q.jvp(x,step);old_merit=float(rhs@rhs)
        slope=float(np.sum((r*weight)*(linear_step*weight)))
        d=dict(index=direction_index,damping=damping,lsmr_stop=int(sol[1]),lsmr_iterations=int(sol[2]),
            lsmr_normr=float(sol[3]),lsmr_normar=float(sol[4]),lsmr_normA=float(sol[5]),lsmr_condA=float(sol[6]),lsmr_normx=float(sol[7]),
            cache=cache,counts=counts.copy(),linear_seconds=time.monotonic()-clock,
            old_merit=old_merit,half_objective_slope=slope,step_max=float(np.max(np.abs(step))),
            nodal_jet_step_max_by_Y_U_A=np.max(np.abs(step_jets),axis=(0,2)).tolist(),height_step=float(step_height),
            linear_residual_merit=float(np.sum(((r+linear_step)*weight)**2)),trials=[],accepted=False)
        np.savez_compressed(a.outdir/f'direction-{direction_index:03d}.npz',step=step,scaled_step=sol[0])
        del linear_step,sol,A,rhs
        event(event='direction_ready',**{k:v for k,v in d.items()if k not in ('cache','trials')})
        alpha=1.
        for line_index in range(a.line_trials):
            trial=x+alpha*step
            arithmetic_error=None
            try:
                tr=q.residual(trial)
                finite=bool(np.isfinite(tr).all());stats=statistics(q,trial,tr) if finite else {}
            except (FloatingPointError,OverflowError) as error:
                tr=None;finite=False;stats={};arithmetic_error=repr(error)
            merit=stats.get('raw_frobenius_sse',float('inf'))/(q.P*full_N)
            feasible=finite and stats['rho_sample_min']>0 and stats['min_relative_E']>0 and stats['min_relative_determinant']>0
            descent=merit<old_merit and (slope>=0 or merit<=old_merit+2e-4*alpha*slope)
            td=dict(index=line_index,alpha=alpha,merit=merit,finite=finite,feasible=feasible,
                descent=descent,statistics=stats,arithmetic_error=arithmetic_error);d['trials'].append(td)
            event(event='actual_trial',direction=direction_index,**td)
            if feasible and descent:
                x=trial;r=tr;d.update(accepted=True,accepted_alpha=alpha,new_merit=merit)
                report['current']=stats
                d['accepted_curvature_points']=point_curvatures(q,x)
                path=a.outdir/f'accepted-{direction_index:03d}.npz';candidate_bundle(path,x)
                d.update(accepted_bundle=str(path),accepted_bundle_sha256=sha(path))
                damping=max(1e-8,damping/2) if alpha==1 else damping
                break
            alpha/=2
        if not d['accepted']:damping*=4
        d['seconds']=time.monotonic()-clock;report['directions'].append(d);save()
        q.clear_base();del step
    report['complete']=True
    report['sample_target_reached']=report.get('current',report['initial'])['max_relative_gram']<=a.target
    report['limitations']='Finite nodes and common-quintic midpoints only. No continuous metric, all-t embeddedness/reach, held/E3, or fixed-g refinement conclusion.'
    final=a.outdir/'final.npz';candidate_bundle(final,x)
    report['final_bundle']=str(final);report['final_bundle_sha256']=sha(final);save()
    event(event='finite_solver_budget_complete',report=str(output),final_bundle=str(final),sample_target_reached=report['sample_target_reached'],statistics=report.get('current',report['initial']))

if __name__=='__main__':main()
