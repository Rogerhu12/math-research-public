"""Augmented Householder TSQR, consuming every eligible original R746 triangular subtree."""
import numpy as np
from scipy.sparse import csr_matrix


def tsqr_factor(raw, residual, identity, stage, donor=None):
    """Call stage(kind, subkey, compute) for each independent resumable operation.

    The caller prefixes subkey with its own source, phase, q, grid and degree key.
    The final factor is stage("tsqr_svd",["complete"],...). Do not wrap the whole
    function in another paid transaction when using stage.
    """
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
    def new_leaf(lo,hi):
        def compute():
            a=np.empty((hi-lo,n+1))
            a[:,:n]=J[lo:hi].toarray()*inv[None,:]/den
            a[:,n]=y[lo:hi]/den
            return triangular(a)
        blocks.append((lo,hi,stage('tsqr_leaf',[lo,hi],compute)))

    imported=[]
    old_end=0
    if donor is not None:
        nold=donor['columns'];old_end=3*len(donor['support']);old_stride=max(2048,4*(nold+1))
        if not 0<nold<n or not 0<old_end<=m or not donor['has']('tsqr_scale',['columns']):
            raise ValueError('inconsistent original QR inheritance')
        # The old leaf boundaries need not be multiples of three scalar rows.
        # A scalar row is eligible only if its complete physical material label
        # is disjoint from every additional field and derivative.
        occupied=np.r_[0,np.cumsum(np.repeat(donor['support'],3),dtype=np.int64)]
        oldtree=[(lo,min(lo+old_stride,old_end),None,None) for lo in range(0,old_end,old_stride)]
        while len(oldtree)>1:
            nxt=[]
            for i in range(0,len(oldtree),2):
                x=oldtree[i]
                if i+1==len(oldtree):nxt.append(x);continue
                y0=oldtree[i+1];nxt.append((x[0],y0[1],x,y0))
            oldtree=nxt
        oldscale=None
        def walk(node):
            nonlocal oldscale
            lo,hi,left,right=node
            kind='tsqr_leaf' if left is None else 'tsqr_merge'
            sub=[lo,hi] if left is None else [lo,left[1],hi]
            if occupied[hi]==occupied[lo] and donor['has'](kind,sub):
                if oldscale is None:
                    oldscale=donor['load']('tsqr_scale',['columns'])['bound']
                    if oldscale.shape!=(nold,) or not np.all(oldscale>0):
                        raise ValueError('invalid original R746 column equilibration')
                def transport():
                    tail=J[lo:hi,nold:]
                    if np.any(tail.data!=0):
                        raise ValueError('an inherited row block has a nonzero appended physical column')
                    prev=donor['load'](kind,sub)
                    if prev.ndim!=2 or prev.shape[1]!=nold+1 or not np.isfinite(prev).all():
                        raise ValueError('invalid original R746 triangular factor')
                    # A_old=[J_old D_old,y_old]/sqrt(Nold).  At these exact
                    # rows, D_old^{-1}D_new is diagonal and all new J columns
                    # vanish.  This leaves the original left orthogonal map valid.
                    R=np.zeros((len(prev),n+1));ratio=np.sqrt(old_end/m)
                    R[:,:nold]=prev[:,:nold]*(oldscale*inv[:nold]*ratio)
                    R[:,n]=prev[:,nold]*ratio
                    return R
                value=stage('r754_transported_householder',[lo,hi],transport)
                blocks.append((lo,hi,value));imported.append(dict(kind=kind,key=sub,rows=hi-lo))
            elif left is None:
                new_leaf(lo,hi)
            else:
                walk(left);walk(right)
        walk(oldtree[0])
    for lo in range(old_end,m,stride):
        new_leaf(lo,min(m,lo+stride))
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
               method="all augmented physical rows with compatible R746 Householder subtrees and complete thin SVD",
               reweighted_original_householder_rows=sum(z['rows'] for z in imported),
               reweighted_original_subtrees=imported,explicit_new_householder_input_rows=m-sum(z['rows'] for z in imported),
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
