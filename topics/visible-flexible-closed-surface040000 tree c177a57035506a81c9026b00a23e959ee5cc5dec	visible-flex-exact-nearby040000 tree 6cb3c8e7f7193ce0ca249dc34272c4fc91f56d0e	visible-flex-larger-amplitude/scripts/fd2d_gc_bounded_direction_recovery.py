"""Constrained raw-GC direction recovered from the recorded Schur implementation.
This solves a finite regularized quadratic direction, not different equations.
"""
import time
import numpy as np
from scipy import sparse
from scipy.sparse.linalg import splu
from scipy.optimize import minimize, LinearConstraint, Bounds

def bounded_schur_direction(problem,vector,residual,jacobian,*,damping=1e-5,
                            central_floor=.1,central_cap=1/.136,preserve_gap=True):
    started=time.monotonic()
    y,p=problem.unpack(vector)
    total=problem.N*problem.q
    free=np.arange(problem.q,total-problem.q)
    count=len(free)
    jf=jacobian[:,free]
    jp=jacobian[:,total:].tolil(copy=True)
    jp[:,:problem.K]=jp[:,:problem.K]+jacobian[:,:problem.e]@sparse.csc_matrix(problem.core_coefficients)
    jp=jp.tocsc()
    reduced=sparse.hstack((jf,jp),format='csc')
    norms=np.sqrt(np.asarray(reduced.multiply(reduced).sum(axis=0)).ravel())
    scale=1/np.maximum(norms,1e-12)
    jf=jf@sparse.diags(scale[:count]);jp=jp@sparse.diags(scale[count:])
    hff=(jf.T@jf+sparse.eye(count,format='csc')*damping).tocsc()
    hfp=(jf.T@jp).toarray()
    hpp=(jp.T@jp).toarray()+np.eye(problem.parameter_count)*damping
    gf=np.asarray(jf.T@residual).ravel();gp=np.asarray(jp.T@residual).ravel()
    lu=splu(hff)
    solved=lu.solve(np.column_stack((gf,hfp)))
    inverse_gradient,inverse_cross=solved[:,0],solved[:,1:]
    schur=hpp-hfp.T@inverse_cross
    schur=.5*(schur+schur.T)
    gradient=gp-hfp.T@inverse_gradient
    eigenvalues=np.linalg.eigvalsh(schur)
    shift=max(0.,damping*.1-float(eigenvalues[0]))
    schur+=np.eye(problem.parameter_count)*shift
    ps=scale[count:]
    lower=np.full(problem.parameter_count,-np.inf)
    upper=np.full(problem.parameter_count,np.inf)
    if problem.tail_kind=='positive_bernstein':
        lower[problem.K:-1]=-p[problem.K:-1]
        upper[problem.K:-1]=1.2-p[problem.K:-1]
    edge=1e-12*problem.profile.model.Tmax
    lower[-1]=edge-p[-1];upper[-1]=problem.profile.model.Tmax-edge-p[-1]
    curvature=problem.seed+problem.core_basis@p[:problem.K]
    matrix=np.zeros((problem.work,problem.parameter_count))
    matrix[:,:problem.K]=problem.core_basis*ps[None,:problem.K]
    constraints=[LinearConstraint(matrix,central_floor-curvature,central_cap-curvature)]
    _,axes=problem.core(p[:problem.K])
    if preserve_gap:
        row=np.zeros((1,problem.parameter_count))
        row[0,:problem.K]=np.asarray(axes['gap_jacobian'],float)*ps[:problem.K]
        target=problem.gap-float(axes['gap'])
        constraints.append(LinearConstraint(row,target,target))
    ans=minimize(lambda z:.5*z@schur@z+gradient@z,np.zeros(problem.parameter_count),
        jac=lambda z:schur@z+gradient,method='SLSQP',bounds=Bounds(lower/ps,upper/ps),
        constraints=constraints,options=dict(ftol=1e-10,maxiter=1000))
    zp=ans.x;zf=-inverse_gradient-inverse_cross@zp
    direction=np.zeros(problem.size)
    direction[free]=scale[:count]*zf
    direction[total:]=ps*zp
    direction[:problem.e]=problem.core_coefficients@direction[total:total+problem.K]
    proposed=curvature+matrix@zp
    info=dict(method='boundary-eliminated bounded Schur least-squares',
        direction_seconds=time.monotonic()-started,free_field_unknowns=count,
        parameter_unknowns=problem.parameter_count,damping=damping,
        schur_added_shift=shift,schur_minimum_eigenvalue=float(eigenvalues[0]),
        optimizer_success=bool(ans.success),optimizer_status=int(ans.status),
        optimizer_message=str(ans.message),optimizer_iterations=int(ans.nit),
        linear_residual_norm=float(np.linalg.norm(residual+jacobian@direction)),
        proposed_minimum_central_curvature=float(proposed.min()),
        proposed_maximum_central_curvature=float(proposed.max()),
        central_sample_floor=central_floor,central_sample_cap=central_cap,
        linear_gap_constraint=preserve_gap,exact_linear_boundary_direction=True,
        original_nonlinear_equations_unchanged=True)
    return direction,info
