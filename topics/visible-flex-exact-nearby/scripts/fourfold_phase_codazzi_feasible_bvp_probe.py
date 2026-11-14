#!/usr/bin/env python3
"""Finite Codazzi BVP with a domain-preserving collocation Newton line search.

The equations and boundary rows are unchanged. Trial iterates are rejected
unless the actual sampled C chart remains negative at nodes and collocation
midpoints. No clipping, projected-away mean, or altered curvature is used.
This remains a floating finite model with an artificial outer condition.
"""
from __future__ import annotations
import argparse,inspect,json,time
from pathlib import Path
import numpy as np
import scipy
import scipy.integrate._bvp as bvp
from scipy.integrate import solve_bvp
from scipy.sparse.linalg import splu
from scipy.interpolate import PPoly
from fourfold_phase_symmetric_geometry import load_exact_object
from fourfold_phase_local_correction_probe import sha,scalar_target
from fourfold_phase_codazzi_two_end_probe import save_npz_gz,load_candidate
from fourfold_phase_codazzi_two_end_homotopy_probe import ChunkedTwoEnded,diagnostics


def guarded_newton(system,log,floor,ceiling,max_iterations):
    def feasible(y):
        if not np.all(np.isfinite(y)):return False
        B,C=system.fields(y)
        return bool(np.all(C < -floor) and np.all(C > -ceiling) and np.all(abs(B)<ceiling))

    def newton(n,m,h,col_fun,bc,jac,y,p,singular_projection,bvp_tol,bc_tol):
        threshold=(2/3)*h*.05*bvp_tol
        if not feasible(y):
            log.append(dict(reason='initial iterate leaves chosen finite negative-C search domain',nodes=m))
            return y,p,True
        for iteration in range(max_iterations):
            col,mid,f,fmid=col_fun(y,p);boundary=bc(y[:,0],y[:,-1],p)
            if not feasible(mid) or not all(np.all(np.isfinite(z)) for z in (col,mid,f,fmid,boundary)):
                log.append(dict(reason='current collocation midpoint leaves chosen finite search domain',nodes=m,iteration=iteration))
                return y,p,True
            residual=np.r_[col.ravel(order='F'),boundary]
            if np.all(abs(col)<threshold*(1+abs(fmid))) and np.all(abs(boundary)<bc_tol):
                log.append(dict(reason='collocation Newton tolerance reached',nodes=m,iteration=iteration))
                return y,p,False
            try:factor=splu(jac(y,p,mid,f,fmid,boundary))
            except RuntimeError:
                log.append(dict(reason='linear factorization failed',nodes=m,iteration=iteration))
                return y,p,True
            step=factor.solve(residual);cost=float(step@step)
            if not np.isfinite(cost):
                log.append(dict(reason='nonfinite Newton correction',nodes=m,iteration=iteration))
                return y,p,True
            dy=step[:n*m].reshape(n,m,order='F');dp=step[n*m:]
            accepted=False;alpha=1.
            for trial in range(24):
                proposed=y-alpha*dy;newp=p-alpha*dp
                if singular_projection is not None:proposed[:,0]=singular_projection@proposed[:,0]
                if feasible(proposed):
                    cc,mm,ff,fm=col_fun(proposed,newp);bb=bc(proposed[:,0],proposed[:,-1],newp)
                    if feasible(mm) and all(np.all(np.isfinite(z)) for z in (cc,mm,ff,fm,bb)):
                        rr=np.r_[cc.ravel(order='F'),bb];correction=factor.solve(rr);newcost=float(correction@correction)
                        if np.isfinite(newcost) and newcost<(1-.1*alpha)*cost:
                            accepted=True;break
                alpha*=.5
            log.append(dict(nodes=m,iteration=iteration,accepted=accepted,step_fraction=alpha,
                affine_invariant_cost=cost,next_cost=newcost if accepted else None,
                max_collocation_residual=float(np.max(abs(col))),max_boundary_residual=float(np.max(abs(boundary)))))
            if not accepted:
                # The outer solver's stop flag is used solely to stop here;
                # the report distinguishes this from a singular Jacobian.
                log.append(dict(reason='no admissible decreasing step in 24 backtracks; NOT an asserted singular Jacobian',nodes=m,iteration=iteration))
                return y,p,True
            y,p=proposed,newp
        log.append(dict(reason='per-mesh Newton iteration limit',nodes=m,iterations=max_iterations))
        return y,p,False
    return newton


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--object',type=Path,default=Path('data/phase_ring_continuation/type_fixed_step02_d5_exact_affine_step5_object.json'))
    p.add_argument('--modes',type=int,default=32);p.add_argument('--angles',type=int,default=512)
    p.add_argument('--right',type=float,default=.25);p.add_argument('--radial-nodes',type=int,default=251)
    p.add_argument('--tol',type=float,default=1e-5);p.add_argument('--max-nodes',type=int,default=3000)
    p.add_argument('--newton-iterations',type=int,default=16);p.add_argument('--C-floor',type=float,default=.05)
    p.add_argument('--field-ceiling',type=float,default=20.);p.add_argument('--guess',type=Path)
    p.add_argument('--out',type=Path,required=True);p.add_argument('--candidate',type=Path,required=True)
    args=p.parse_args();start=time.monotonic()
    if args.angles<8*args.modes or args.angles%4:raise ValueError('insufficient angular grid')
    geometry,definition=load_exact_object(args.object,512);system=ChunkedTwoEnded(geometry,args.modes,args.angles)
    m=args.modes;n=2*m+1;r=np.linspace(0.,args.right,args.radial_nodes)
    a0=scalar_target(geometry,0.)['a'];right_old=system.old_fields(args.right)[m+1:]
    guess=np.column_stack([system.old_fields(x) for x in r])
    if args.guess:
        old=load_candidate(args.guess);meta=json.loads(str(old['metadata']))
        if meta['object_sha256']!=sha(args.object) or 'W=' in meta.get('coordinates',''):
            raise ValueError('different target or chart in candidate')
        if not np.all(np.isfinite(old['piece_coefficients'])):raise ValueError('nonfinite initial guess')
        pm=int(meta['modes']);values=PPoly(old['piece_coefficients'],old['radial_nodes'])(r).T;count=min(pm,m)
        guess[:count]=values[:count];guess[m:m+count+1]=values[pm:pm+count+1]
    def bc(left,right):return np.r_[left[:m],left[m]+1/a0,right[m+1:]-right_old]
    def bc_jac(left,right):
        jl=np.zeros((n,n));jr=np.zeros((n,n));jl[np.arange(m+1),np.arange(m+1)]=1
        jr[np.arange(m+1,n),np.arange(m+1,n)]=1
        return jl,jr
    steps=[];original_newton=bvp.solve_newton
    bvp.solve_newton=guarded_newton(system,steps,args.C_floor,args.field_ceiling,args.newton_iterations)
    try:
        result=solve_bvp(system.evaluate,bc,r,guess,fun_jac=system.jacobian,bc_jac=bc_jac,
            tol=args.tol,bc_tol=args.tol/100,max_nodes=args.max_nodes,verbose=1)
    finally:bvp.solve_newton=original_newton
    diagnostic=diagnostics(system,result)
    diagnostic['valid']=bool(all(np.isfinite(v) for v in diagnostic.values()) and diagnostic['C_max']<0 and diagnostic['C_abs_min']>0)
    c0=result.y[m:,0];c1=result.y[m:,-1]
    metadata=dict(kind='floating_feasible_Newton_Codazzi_BVP',coordinates='B,C',modes=m,
        source_sha256=sha(__file__),object_sha256=sha(args.object),boundary_amplitude=1.,physical_frequency_factor=4,
        state_order='B sine k=1..M, C cosine k=0..M',initial_waist_curve_changed=True,original_target_fixed=True,
        right_boundary='old actual nonmean C only; no cap DN, outer C mean free',
        finite_coefficients=bool(np.all(np.isfinite(result.sol.c))))
    save_npz_gz(args.candidate,radial_nodes=result.x,piece_coefficients=result.sol.c,initial_state=result.y[:,0],
        right_boundary_C_nonmean=right_old,metadata=np.array(json.dumps(metadata)))
    doc=dict(**metadata,certified=False,success=bool(result.success and diagnostic['valid']),
        solver_status=int(result.status),solver_message=result.message,guarded_Newton_history=steps,
        guard_stop_interpretation='If history says no admissible step or domain exit, the library singular-stop flag was used to terminate; it is NOT a claim that the actual Jacobian is singular.',
        diagnostics=diagnostic,radial_nodes=len(result.x),right=args.right,tol=args.tol,max_nodes=args.max_nodes,
        initial_radial_nodes=args.radial_nodes,angular_grid=args.angles,diagnostic_angular_grid=2*args.angles,
        sampled_C_guard_floor=args.C_floor,sampled_B_C_guard_ceiling=args.field_ceiling,
        maximum_Newton_steps_per_mesh=args.newton_iterations,
        initial_mean_gap=float(c0[0]+1/a0),initial_turn_number=float(-a0*c0[0]),
        initial_total_turn=float(-2*np.pi*a0*c0[0]),free_outer_C_mean=float(c1[0]),
        initial_B_l1=float(np.sum(abs(result.y[:m,0]))),
        outer_nonmean_C_boundary_gap_l1=float(np.sum(abs(c1[1:]-right_old))),
        exact_center_parameter=definition['delta_fraction'],origin_sha256=definition['origin_inputs']['sha256'],
        direction_sha256=definition['direction']['sha256'],guess_path=str(args.guess) if args.guess else None,
        guess_sha256=sha(args.guess) if args.guess else None,
        scipy_version=scipy.__version__,scipy_collocation_module_sha256=sha(inspect.getsourcefile(bvp)),
        candidate_path=str(args.candidate),candidate_sha256=sha(args.candidate),
        dependency_sha256={s:sha(Path(__file__).with_name(s)) for s in
            ('fourfold_phase_codazzi_two_end_probe.py','fourfold_phase_codazzi_two_end_homotopy_probe.py',
             'fourfold_phase_symmetric_geometry.py','fourfold_phase_geometry.py','fourfold_phase_core_low_block.py',
             'fourfold_phase_local_correction_probe.py')},
        mean_retained=True,regular_trace=None,regular_flux=None,whole_parameter_interval=False,
        whole_real_angular_circle=False,whole_radial_domain=False,wall_seconds=time.monotonic()-start,
        limitations=['Floating finite BVP and sampled search-domain constraints only, not a continuous PDE certificate.',
            'The new line search rejects invalid trial states; it neither clips C nor changes the Codazzi equations.',
            'The outer condition is not the complete cap DN. No regular-port matching or global closed surface is claimed.'])
    args.out.write_text(json.dumps(doc,indent=2,allow_nan=False)+'\n')
    print(dict(success=doc['success'],diagnostics=diagnostic,mean_gap=doc['initial_mean_gap'],
        stop=steps[-1],wall_seconds=doc['wall_seconds']),flush=True)


if __name__=='__main__':main()
