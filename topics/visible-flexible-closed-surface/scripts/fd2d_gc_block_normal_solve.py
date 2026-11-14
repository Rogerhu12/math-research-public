"""Solve the original scaled, positively damped R159 field normal in blocks.

No whole Hff, sparse COO/CSC, sparse LU, or normal.scaled() is constructed.
All columns use the original global norm squares. The block Cholesky work
matrices are symmetrized for floating arithmetic; the returned solution is
checked against the original separately left/right-scaled block equation.
No pivot floor, eigenvalue clipping, extra damping, or physical solve occurs.
"""
from __future__ import annotations
import time
import numpy as np
from scipy.linalg import cho_factor, cho_solve


def _maximum(value):
    return float(np.max(np.abs(value),initial=0.))


def _diagonal(normal,node,scale,damping):
    a=(scale[:,None]*normal.diagonal[node])*scale[None,:]
    if len(scale):a.flat[::len(scale)+1]+=damping
    return a


def solve_scaled_normal_field(normal,damping=1e-7,progress=None):
    """Return solved=[ig,ic], original scales/small blocks, and observations.

    solved[:,0] = (S_f Hff S_f + damping I)^(-1) (S_f gf)
    solved[:,1:] = (S_f Hff S_f + damping I)^(-1) (S_f Hfp S_p)

    Empty field-node blocks are valid, including consecutive central nodes
    and the fixed terminal node. `progress` receives Python scalars only.
    Residual observations are finite floating computations, not interval
    enclosures. Scaling or damping of a normal tile before summing remains
    invalid; pass the already completed unscaled normal.
    """
    started=time.monotonic();damping=float(damping)
    if not np.isfinite(damping) or damping<=0:
        raise ValueError('Use the original finite strictly positive damping')
    mapping=normal.mapping;N=int(mapping.N);P=int(mapping.P);count=int(mapping.count)
    widths=np.asarray(mapping.widths,dtype=int);offsets=np.asarray(mapping.offsets,dtype=int)
    if (widths.shape!=(N,) or offsets.shape!=(N+1,) or offsets[0]!=0
            or offsets[-1]!=count or np.any(widths<0) or not np.array_equal(np.diff(offsets),widths)):
        raise ValueError('The actual field-node block map is inconsistent')
    if (normal.Hfp.shape!=(count,P) or normal.Hpp.shape!=(P,P)
            or normal.gf.shape!=(count,) or normal.gp.shape!=(P,)
            or normal.field_norm_squared.shape!=(count,) or normal.parameter_norm_squared.shape!=(P,)
            or len(normal.diagonal)!=N or len(normal.upper)!=max(0,N-1)):
        raise ValueError('The actual complete normal has incompatible block shapes')
    for q in (normal.field_norm_squared,normal.parameter_norm_squared):
        if not np.all(np.isfinite(q)) or np.any(q<0):
            raise FloatingPointError('Original accumulated column norm squares are invalid')
    fs=1/np.maximum(np.sqrt(normal.field_norm_squared),1e-12)
    ps=1/np.maximum(np.sqrt(normal.parameter_norm_squared),1e-12)
    hfp=(fs[:,None]*normal.Hfp)*ps[None,:]
    hpp=(ps[:,None]*normal.Hpp)*ps[None,:]+np.eye(P)*damping
    gf=fs*normal.gf;gp=ps*normal.gp
    solved=np.empty((count,P+1),dtype=float)
    solved[:,0]=gf;solved[:,1:]=hfp
    if not all(np.all(np.isfinite(a)) for a in (hfp,hpp,gf,gp)):
        raise FloatingPointError('The original scaled arrow/gradient is nonfinite')
    couplings=[];previous_upper=None
    min_cholesky_diagonal=None;max_diagonal_asymmetry=0.;max_schur_asymmetry=0.
    max_symmetrization_change=0.;max_lower_transpose_rounding=0.
    largest_local_dense_entries=0;factorized_blocks=0;empty_nodes=[]
    for node in range(N):
        begin,end=map(int,offsets[node:node+2]);width=int(widths[node]);s=fs[begin:end]
        if np.shape(normal.diagonal[node])!=(width,width):
            raise ValueError('Wrong original node diagonal shape')
        D=_diagonal(normal,node,s,damping)
        max_diagonal_asymmetry=max(max_diagonal_asymmetry,_maximum(D-D.T))
        if node<N-1:
            next_end=int(offsets[node+2]);next_scale=fs[end:next_end]
            if np.shape(normal.upper[node])!=(width,len(next_scale)):
                raise ValueError('Wrong original adjacent block shape')
            upper=(s[:,None]*normal.upper[node])*next_scale[None,:]
        else:
            upper=np.empty((width,0))
        if not np.all(np.isfinite(D)) or not np.all(np.isfinite(upper)):
            raise FloatingPointError('Nonfinite original scaled field block at node '+str(node))
        if node:
            before=int(offsets[node-1]);previous_scale=fs[before:begin]
            lower=(s[:,None]*normal.upper[node-1].T)*previous_scale[None,:]
            max_lower_transpose_rounding=max(max_lower_transpose_rounding,_maximum(lower-previous_upper.T))
            D-=previous_upper.T@couplings[node-1]
            solved[begin:end]-=previous_upper.T@solved[before:begin]
        max_schur_asymmetry=max(max_schur_asymmetry,_maximum(D-D.T))
        if width:
            # This changes only the floating representative of the symmetric
            # Schur block. The real-arithmetic problem and damping are intact.
            symmetric=.5*D+.5*D.T
            max_symmetrization_change=max(max_symmetrization_change,_maximum(symmetric-D))
            factor,lower_flag=cho_factor(symmetric,lower=True,overwrite_a=True,check_finite=False)
            pivot=float(np.min(np.diag(factor)))
            min_cholesky_diagonal=pivot if min_cholesky_diagonal is None else min(min_cholesky_diagonal,pivot)
            C=cho_solve((factor,lower_flag),upper,overwrite_b=False,check_finite=False)
            solved[begin:end]=cho_solve((factor,lower_flag),solved[begin:end],overwrite_b=False,check_finite=False)
            factorized_blocks+=1
            if not np.all(np.isfinite(C)) or not np.all(np.isfinite(solved[begin:end])):
                raise FloatingPointError('Nonfinite block forward solution at node '+str(node))
            del factor,symmetric
        else:
            C=np.empty((0,upper.shape[1]));empty_nodes.append(node)
        if node<N-1:couplings.append(C)
        largest_local_dense_entries=max(largest_local_dense_entries,
            int(3*width*width+2*upper.size+width*(P+1)))
        previous_upper=upper
        if progress is not None:
            progress('block_factor',int(node),int(N),int(width))
        del D,C
    coupling_bytes=int(sum(a.nbytes for a in couplings))
    for node in range(N-2,-1,-1):
        begin,middle,end=map(int,offsets[node:node+3])
        solved[begin:middle]-=couplings[node]@solved[middle:end]
    del couplings,previous_upper
    factor_seconds=time.monotonic()-started
    # Independently evaluate the unaveraged original scaled block equation.
    # The lower block is scaled in its original orientation, so its last-bit
    # difference from upper.T is included in this residual observation.
    residual_squares=np.zeros(P+1);rhs_squares=np.zeros(P+1)
    residual_maxima=np.zeros(P+1);componentwise_backward=np.zeros(P+1)
    block_records=[]
    for node in range(N):
        begin,end=map(int,offsets[node:node+2]);s=fs[begin:end];width=end-begin
        rhs=np.empty((width,P+1));rhs[:,0]=gf[begin:end];rhs[:,1:]=hfp[begin:end]
        diagonal=_diagonal(normal,node,s,damping)
        action=diagonal@solved[begin:end]
        magnitude=np.abs(diagonal)@np.abs(solved[begin:end])+np.abs(rhs)
        if node:
            before=int(offsets[node-1])
            lower=(s[:,None]*normal.upper[node-1].T)*fs[None,before:begin]
            action+=lower@solved[before:begin]
            magnitude+=np.abs(lower)@np.abs(solved[before:begin])
        if node<N-1:
            after=int(offsets[node+2])
            upper=(s[:,None]*normal.upper[node])*fs[None,end:after]
            action+=upper@solved[end:after]
            magnitude+=np.abs(upper)@np.abs(solved[end:after])
        residual=action-rhs
        if not np.all(np.isfinite(residual)) or not np.all(np.isfinite(magnitude)):
            raise FloatingPointError('Nonfinite actual block residual observation')
        relative=np.divide(np.abs(residual),magnitude,out=np.zeros_like(residual),where=magnitude>0)
        residual_squares+=np.sum(residual*residual,axis=0)
        rhs_squares+=np.sum(rhs*rhs,axis=0)
        residual_maxima=np.maximum(residual_maxima,np.max(np.abs(residual),axis=0,initial=0.))
        componentwise_backward=np.maximum(componentwise_backward,np.max(relative,axis=0,initial=0.))
        block_records.append(dict(node=int(node),width=int(width),absolute_residual_maximum=_maximum(residual),
            componentwise_backward_maximum=_maximum(relative)))
    residual_l2=np.sqrt(residual_squares);rhs_l2=np.sqrt(rhs_squares)
    relative_l2=np.divide(residual_l2,rhs_l2,out=np.zeros_like(residual_l2),where=rhs_l2>0)
    if np.any((rhs_l2==0)&(residual_l2>0)):
        raise FloatingPointError('Nonzero residual observed for a zero original right-hand side')
    info=dict(schema='fd2d-R159-scaled-SPD-block-normal-solve-v1',
        field_unknowns=count,parameter_unknowns=P,right_hand_sides=P+1,
        total_nodes=N,factorized_nonempty_nodes=factorized_blocks,empty_nodes=empty_nodes,
        damping=damping,column_scale_floor=1e-12,original_global_column_norm_squares_used=True,
        whole_Hff_constructed=False,whole_sparse_matrix_constructed=False,sparse_LU_called=False,
        normal_scaled_method_called=False,normal_modified=False,new_F_or_J_computed=False,
        numerical_symmetrization='(D + D.T)/2 evaluated as .5*D + .5*D.T before local Cholesky',
        maximum_scaled_diagonal_asymmetry=max_diagonal_asymmetry,
        maximum_forward_Schur_asymmetry=max_schur_asymmetry,
        maximum_local_symmetrization_change=max_symmetrization_change,
        maximum_opposite_orientation_scaling_rounding=max_lower_transpose_rounding,
        minimum_Cholesky_diagonal=min_cholesky_diagonal,
        eigenvalue_clipping_or_added_damping=False,
        coupling_workspace_bytes=coupling_bytes,solution_array_bytes=int(solved.nbytes),
        largest_local_dense_entry_estimate=largest_local_dense_entries,
        factor_and_substitution_seconds=factor_seconds,seconds=time.monotonic()-started,
        residual_definition='Original unaveraged diagonal and independently left/right-scaled lower/upper blocks applied to returned solution, minus original scaled [gf,hfp]',
        residual_evaluation_is_interval_certificate=False,
        absolute_residual_maximum=_maximum(residual_maxima),
        relative_residual_l2_maximum=_maximum(relative_l2),
        componentwise_backward_maximum=_maximum(componentwise_backward),
        absolute_residual_maxima_by_rhs=residual_maxima.tolist(),
        residual_l2_by_rhs=residual_l2.tolist(),rhs_l2_by_rhs=rhs_l2.tolist(),
        relative_residual_l2_by_rhs=relative_l2.tolist(),
        componentwise_backward_by_rhs=componentwise_backward.tolist(),block_residuals=block_records)
    return dict(solved=solved,field_scale=fs,parameter_scale=ps,hfp=hfp,hpp=hpp,gf=gf,gp=gp,info=info)
