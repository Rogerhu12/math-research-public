"""Bounded Schur directions for rectangular RawBumpDAE, with explicit p layout."""
import time,resource
import numpy as np
from scipy import sparse
from scipy.sparse.linalg import splu
from scipy.optimize import minimize,LinearConstraint,Bounds


def bounded_bump_direction(problem,vector,residual,jacobian,*,damping=1e-5,
        central_floor=.1,central_cap=1/.136,profile_box=.08,preserve_gap=True):
    start=time.monotonic();_,p=problem.unpack(vector)
    total=problem.N*problem.q
    central_nodes=np.asarray(getattr(problem,'fixed_central_nodes',[0]),dtype=int)
    fixed=np.r_[np.concatenate([j*problem.q+np.arange(problem.q) for j in central_nodes]),
                np.arange(total-problem.q,total)]
    free=np.setdiff1d(np.arange(total),fixed,assume_unique=False);count=len(free)
    jf=jacobian[:,free]
    jp=jacobian[:,total:].tolil(copy=True)
    for node in central_nodes:
        jp[:,:problem.K]=jp[:,:problem.K]+jacobian[:,node*problem.q:node*problem.q+problem.e]@sparse.csc_matrix(problem.core_coefficients)
    jp=jp.tocsc()
    # No concatenated copy of the tall guidance matrix and no sparse
    # elementwise-square copy. Each nonempty CSC column is contiguous.
    def norms_and_scale_in_place(matrix):
        nonempty=np.diff(matrix.indptr)>0
        sums=np.zeros(matrix.shape[1])
        if len(matrix.data):
            sums[nonempty]=np.add.reduceat(matrix.data*matrix.data,matrix.indptr[:-1][nonempty])
        factors=1/np.maximum(np.sqrt(sums),1e-12)
        for column in range(matrix.shape[1]):
            matrix.data[matrix.indptr[column]:matrix.indptr[column+1]]*=factors[column]
        return factors
    scale=np.r_[norms_and_scale_in_place(jf),norms_and_scale_in_place(jp)]
    hff=(jf.T@jf+sparse.eye(count,format='csc')*damping).tocsc()
    hfp=(jf.T@jp).toarray();hpp=(jp.T@jp).toarray()+np.eye(problem.parameter_count)*damping
    gf=np.asarray(jf.T@residual).ravel();gp=np.asarray(jp.T@residual).ravel()
    del jf,jp
    rss_before_lu=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    lu=splu(hff);solved=lu.solve(np.column_stack((gf,hfp)))
    ig,ic=solved[:,0],solved[:,1:]
    schur=hpp-hfp.T@ic;schur=.5*(schur+schur.T);gradient=gp-hfp.T@ig
    ev=np.linalg.eigvalsh(schur);shift=max(0.,damping*.1-float(ev[0]));schur+=np.eye(problem.parameter_count)*shift
    ps=scale[count:];lower=np.full(problem.parameter_count,-np.inf);upper=-lower.copy()
    ts=problem.tail_parameter_slice;ds=problem.profile_parameter_slice
    lower[ts]=-p[ts];upper[ts]=1.2-p[ts]
    lower[ds]=-profile_box-p[ds];upper[ds]=profile_box-p[ds]
    curvature=problem.seed+problem.core_basis@p[:problem.K]
    cm=np.zeros((problem.work,problem.parameter_count));cm[:,:problem.K]=problem.core_basis*ps[None,:problem.K]
    constraints=[LinearConstraint(cm,central_floor-curvature,central_cap-curvature)]
    dom=problem.profile_domain
    if dom is not None:
        pm=np.zeros((len(dom['lower']),problem.parameter_count));pm[:,ds]=dom['matrix']*ps[None,ds]
        constraints.append(LinearConstraint(pm,dom['lower']-dom['matrix']@p[ds],np.inf))
    _,axes=problem.core(p[:problem.K])
    if preserve_gap:
        row=np.zeros((1,problem.parameter_count));row[0,:problem.K]=np.asarray(axes['gap_jacobian'],float)*ps[:problem.K]
        target=problem.gap-float(axes['gap']);constraints.append(LinearConstraint(row,target,target))
    ans=minimize(lambda z:.5*z@schur@z+gradient@z,np.zeros(problem.parameter_count),
        jac=lambda z:schur@z+gradient,method='SLSQP',bounds=Bounds(lower/ps,upper/ps),constraints=constraints,
        options=dict(ftol=1e-10,maxiter=1000))
    zp=ans.x;zf=-ig-ic@zp;direction=np.zeros(problem.size)
    direction[free]=scale[:count]*zf;direction[total:]=ps*zp
    for node in central_nodes:
        direction[node*problem.q:node*problem.q+problem.e]=problem.core_coefficients@direction[total:total+problem.K]
    proposed=curvature+cm@zp
    info=dict(method='exact-cylinder boundary-eliminated bounded Schur least squares; separate in-place CSC scaling',
        direction_seconds=time.monotonic()-start,free_field_unknowns=count,parameter_unknowns=problem.parameter_count,
        exact_central_field_nodes=central_nodes.tolist(),
        damping=damping,schur_shift=shift,schur_minimum_eigenvalue=float(ev[0]),
        optimizer_success=bool(ans.success),optimizer_status=int(ans.status),optimizer_message=str(ans.message),
        optimizer_iterations=int(ans.nit),linear_residual_norm=float(np.linalg.norm(residual+jacobian@direction)),
        proposed_minimum_central_curvature=float(proposed.min()),proposed_maximum_central_curvature=float(proposed.max()),
        profile_box=profile_box,profile_linear_rows=0 if dom is None else len(dom['lower']),
        maximum_profile_direction=float(np.max(abs(direction[total:][ds]))),
        lu_nonzeros=int(lu.L.nnz+lu.U.nnz),original_raw_equations_unchanged=True,
        peak_rss_kib_before_lu=int(rss_before_lu),peak_rss_kib_after_direction=int(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss),
        concatenated_tall_matrix_copy_used=False)
    return direction,info
