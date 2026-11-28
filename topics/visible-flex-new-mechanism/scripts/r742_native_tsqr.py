"""Native sparse physical curl operator: all original rows, Householder TSQR and full small SVD."""
import numpy as np
from scipy.sparse import csr_matrix


def tsqr_factor(raw, residual, identity, stage=None):
    """Call stage(kind, subkey, compute) for each independent resumable operation.

    The caller prefixes subkey with its own source, phase, q, grid and degree key.
    The final factor is stage("tsqr_svd",["complete"],...). Do not wrap the whole
    function in another paid transaction when using stage.
    """
    if stage is None:
        def stage(kind, subkey, compute):
            return compute()
    J=csr_matrix((raw["data"],raw["indices"],raw["indptr"]),shape=raw["shape"])
    y=np.asarray(residual,dtype=float).reshape(-1)
    m,n=J.shape
    if m!=len(y) or m%3 or not m or not n or not np.isfinite(y).all() or not np.isfinite(J.data).all():
        raise ValueError("invalid physical three-component operator or residual")
    count=m//3
    den=np.sqrt(float(count))

    def scales():
        # A positive lower bound only on the equilibration factor; every
        # original column, including exact zero columns, remains in the matrix.
        csc=J.tocsc()
        norm=np.zeros(n)
        for j in range(n):
            lo,hi=csc.indptr[j:j+2]
            v=csc.data[lo:hi]
            a=np.max(np.abs(v)) if len(v) else 0.
            if a:
                norm[j]=a*np.linalg.norm(v/a)/den
        bound=np.maximum(norm,max(1.e-300,float(np.max(norm))*1.e-10))
        return dict(norm=norm,bound=bound)
    scale=stage("tsqr_scale",["columns"],scales)
    inv=1/scale["bound"]
    stride=max(2048,4*(n+1))
    blocks=[]

    def triangular(a):
        # mode='r' invokes QR without materializing a tall Q. This retains
        # the residual column, hence the projected right-hand side as well.
        r=np.linalg.qr(a,mode="r")
        if not np.isfinite(r).all():
            raise ArithmeticError("nonfinite Householder factor")
        return r
    for lo in range(0,m,stride):
        hi=min(m,lo+stride)
        def leaf():
            a=np.empty((hi-lo,n+1))
            a[:,:n]=J[lo:hi].toarray()*inv[None,:]/den
            a[:,n]=y[lo:hi]/den
            return triangular(a)
        blocks.append((lo,hi,stage("tsqr_leaf",[lo,hi],leaf)))
    while len(blocks)>1:
        nxt=[]
        for i in range(0,len(blocks),2):
            left=blocks[i]
            if i+1==len(blocks):
                nxt.append(left)
                continue
            right=blocks[i+1]
            if left[1]!=right[0]:
                raise AssertionError("noncontiguous physical row cover")
            val=stage("tsqr_merge",[left[0],left[1],right[1]],
                      lambda:triangular(np.concatenate((left[2],right[2]))))
            nxt.append((left[0],right[1],val))
        blocks=nxt
    if blocks[0][:2]!=(0,m):
        raise AssertionError("incomplete native row cover")
    r=blocks[0][2]

    def finalize():
        a=r[:,:n]; b=r[:,n]
        u,s,v=np.linalg.svd(a,full_matrices=False)
        ru,rs,rv=np.linalg.svd(a*scale["bound"][None,:],full_matrices=False)
        projected=u.T@b
        rank_tol=np.finfo(float).eps*max(m,n)
        label=dict(format="csr",rows=m,shape=list(J.shape),nnz=J.nnz,
               arrays={k:identity(raw[k]) for k in ("data","indices","indptr")},
               method="all physical CSR rows, augmented Householder TSQR and complete thin SVD",
               supplied_vector_samples=count,original_row_stride=stride,
               original_unscaled_singular_values=rs.tolist(),
               scaled_rank_above_diagnostic_resolution=int(np.sum(s>s[0]*rank_tol)),
               raw_rank_above_diagnostic_resolution=int(np.sum(rs>rs[0]*rank_tol)),
               rank_only_relative_resolution=rank_tol,
               j_normalization="both spectra prefix J/sqrt(vector_samples); solver uses column equilibration",
               singular_values_removed=0,raw_column_norms=identity(scale["norm"]),
               equilibration=identity(scale["bound"]),columns_nonzero=int(np.sum(scale["norm"]>0)),
               independent_columns=raw["sampled_columns"].tolist(),
               max_independent_scaled_defect=max(raw["scaled_check_defects"]))
        return dict(s=s, Vt=v*inv[None,:], projected=projected, raw=label,
                    augmented_householder_R=r, response_projection_norm=float(np.linalg.norm(b)),
                    raw_svd_u=ru,raw_svd_s=rs,raw_svd_vt=rv,raw_svd_rhs=ru.T@b,
                    scaled_svd_u=u,scaled_svd_vt=v,column_norm=scale["norm"],
                    equilibration=scale["bound"])
    return stage("tsqr_svd",["complete"],finalize)
