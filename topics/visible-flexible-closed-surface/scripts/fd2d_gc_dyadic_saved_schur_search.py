"""The R170 parameter QP on an unchanged saved normal Schur complement.

No sparse field matrix, LU, residual, or Jacobian is assembled here.  The
field solves are supplied by the separate same-normal block solver.  All
QP bounds/linear constraints and its eigenshift are the frozen R159 ones.
"""
import time
import resource
import numpy as np
from scipy.optimize import minimize,LinearConstraint,Bounds
from fd2d_gc_dyadic_tail_problem import scaled_tail_linear_constraints


def make_schur_packet(normal,field_solution,*,damping):
    """Preserve the complete field solves and the original small Schur QP."""
    damping=float(damping)
    if not np.isfinite(damping) or damping<=0:raise ValueError('Use strictly positive original damping')
    solved=field_solution['solved'];hfp=field_solution['hfp'];hpp=field_solution['hpp']
    gf,gp=field_solution['gf'],field_solution['gp']
    if solved.shape!=(normal.mapping.count,normal.mapping.P+1):
        raise ValueError('The saved solve must contain gradient plus every physical parameter RHS')
    ig,ic=solved[:,0],solved[:,1:]
    schur=hpp-hfp.T@ic;schur=.5*(schur+schur.T)
    gradient=gp-hfp.T@ig
    eigenvalues=np.linalg.eigvalsh(schur)
    shift=max(0.,damping*.1-float(eigenvalues[0]))
    unshifted=schur.copy();schur+=np.eye(normal.mapping.P)*shift
    packet=dict(solved=np.array(solved,copy=True),schur=schur,unshifted_schur=unshifted,
        gradient=gradient,field_scale=np.array(field_solution['field_scale'],copy=True),
        parameter_scale=np.array(field_solution['parameter_scale'],copy=True),
        scaled_field_gradient=np.array(gf,copy=True),scaled_parameter_gradient=np.array(gp,copy=True),
        damping=damping,schur_shift=shift,schur_minimum_eigenvalue=float(eigenvalues[0]),
        normal_residual_squared=float(normal.residual_squared),
        field_solve_information=field_solution['info'])
    return packet


def normal_direction_quadratic(normal,direction):
    """Evaluate the ORIGINAL normal quadratic directly in its small blocks."""
    m=normal.mapping;direction=np.asarray(direction,float)
    if direction.shape!=(m.total+m.P,):raise ValueError('Wrong full actual direction')
    df,dp=direction[m.free],direction[m.total:]
    terms=[np.longdouble(normal.residual_squared),
           2*np.longdouble(normal.gf@df+normal.gp@dp)]
    for j,block in enumerate(normal.diagonal):
        a,b=map(int,m.offsets[j:j+2]);v=df[a:b]
        terms.append(np.longdouble(v@block@v))
    for j,block in enumerate(normal.upper):
        a,b,c=map(int,m.offsets[j:j+3])
        terms.append(2*np.longdouble(df[a:b]@block@df[b:c]))
    terms.append(2*np.longdouble(df@normal.Hfp@dp))
    terms.append(np.longdouble(dp@normal.Hpp@dp))
    terms=np.array(terms,dtype=np.longdouble)
    value=float(np.sum(terms,dtype=np.longdouble));scale=float(np.sum(abs(terms),dtype=np.longdouble))
    if value < -256*np.finfo(float).eps*max(scale,1.):
        raise FloatingPointError('Original normal quadratic has severe floating cancellation')
    return dict(linear_residual_norm=float(np.sqrt(max(value,0.))),
        linear_residual_squared_unclamped=value,normal_quadratic_cancellation_scale=scale,
        actual_merit_slope=float(normal.gf@df+normal.gp@dp),
        linear_residual_norm_source='Original unscaled normal blocks; no sparse matrix or new F/J')


def bounded_direction_from_schur(problem,vector,normal,packet,*,central_floor=.1,
        central_cap=1/.136,profile_box=.08,preserve_gap=True,iteration_callback=None):
    """Original 54-parameter SLSQP, followed by the saved field back solve."""
    started=time.monotonic();_,p=problem.unpack(vector)
    m=normal.mapping;ps=np.asarray(packet['parameter_scale']);fs=np.asarray(packet['field_scale'])
    schur=np.asarray(packet['schur']);gradient=np.asarray(packet['gradient'])
    if ps.shape!=(m.P,) or fs.shape!=(m.count,) or schur.shape!=(m.P,m.P):
        raise ValueError('Saved Schur layout differs from the actual eliminated field')
    lower=np.full(problem.parameter_count,-np.inf);upper=-lower.copy()
    ts,ds=problem.tail_parameter_slice,problem.profile_parameter_slice
    # The explicit global tail variable box is replaced, not supplemented.
    tail_rows=scaled_tail_linear_constraints(problem,p,ps)
    lower[ds],upper[ds]=-profile_box-p[ds],profile_box-p[ds]
    curvature=problem.seed+problem.core_basis@p[:problem.K]
    cm=np.zeros((problem.work,problem.parameter_count))
    cm[:,:problem.K]=problem.core_basis*ps[None,:problem.K]
    constraints=[LinearConstraint(cm,central_floor-curvature,central_cap-curvature),
        LinearConstraint(tail_rows['matrix'],tail_rows['lower'],tail_rows['upper'])]
    dom=problem.profile_domain
    if dom is not None:
        pm=np.zeros((len(dom['lower']),problem.parameter_count))
        pm[:,ds]=dom['matrix']*ps[None,ds]
        constraints.append(LinearConstraint(pm,dom['lower']-dom['matrix']@p[ds],np.inf))
    _,axes=problem.core(p[:problem.K])
    if preserve_gap:
        row=np.zeros((1,problem.parameter_count))
        row[0,:problem.K]=np.asarray(axes['gap_jacobian'],float)*ps[:problem.K]
        target=problem.gap-float(axes['gap'])
        constraints.append(LinearConstraint(row,target,target))
    observed_iterations=0
    def observe(z):
        nonlocal observed_iterations
        observed_iterations+=1
        if iteration_callback is not None:
            iteration_callback(observed_iterations,np.array(z,copy=True))
    answer=minimize(lambda z:.5*z@schur@z+gradient@z,np.zeros(problem.parameter_count),
        jac=lambda z:schur@z+gradient,method='SLSQP',bounds=Bounds(lower/ps,upper/ps),
        constraints=constraints,options=dict(ftol=1e-10,maxiter=1000),callback=observe)
    zp=answer.x;solved=packet['solved'];zf=-solved[:,0]-solved[:,1:]@zp
    direction=m.expand(fs*zf,ps*zp)
    proposed=curvature+cm@zp
    info=dict(method='R170 dyadic-tail bounded parameter QP from the unchanged same-normal block Schur solve',
        direction_seconds=time.monotonic()-started,free_field_unknowns=m.count,
        tail_linear_rows=128,old_global_tail_bounds_removed=True,
        tail_search_domain_definition=problem.tail_search_domain_definition,
        parameter_unknowns=problem.parameter_count,damping=float(packet['damping']),
        schur_shift=float(packet['schur_shift']),schur_minimum_eigenvalue=float(packet['schur_minimum_eigenvalue']),
        optimizer_success=bool(answer.success),optimizer_status=int(answer.status),
        optimizer_message=str(answer.message),optimizer_iterations=int(answer.nit),
        proposed_minimum_central_curvature=float(proposed.min()),
        proposed_maximum_central_curvature=float(proposed.max()),central_floor=float(central_floor),
        central_cap=float(central_cap),profile_box=float(profile_box),preserve_gap=bool(preserve_gap),
        profile_linear_rows=0 if dom is None else len(dom['lower']),
        maximum_profile_direction=float(np.max(abs(direction[m.total:][ds]))),
        no_whole_sparse_field_matrix=True,no_residual_or_Jacobian_evaluation=True,
        field_solve_information=packet['field_solve_information'],
        peak_rss_kib=int(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss),
        exact_central_field_nodes=m.central_nodes.tolist(),
        exact_coupled_trace_gauge_pairs=m.pairs.tolist(),
        additional_exact_inactive_field_indices=m.extra.tolist())
    info.update(normal_direction_quadratic(normal,direction))
    return direction,info,dict(schur=schur,gradient=gradient,field_scale=fs,parameter_scale=ps,
        scaled_parameter_direction=zp,scaled_field_direction=zf)
