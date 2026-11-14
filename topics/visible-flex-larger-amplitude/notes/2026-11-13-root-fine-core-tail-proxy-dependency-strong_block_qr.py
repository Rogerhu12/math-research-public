"""Balanced orthogonal elimination for the exact first-order BVP Jacobian.

The matrix must have n equations per adjacent node pair, k parameter
columns, and n+k boundary rows supported only at the two endpoints and
parameters. This factors that same matrix, without transfer products,
regularization, clipping, or a changed nonlinear equation. It is optional.
"""
from dataclasses import dataclass
import numpy as np
from scipy.linalg import lu_factor,lu_solve,solve_triangular
from scipy.linalg.lapack import dgeqrf,dormqr

class _Node:
    def __init__(self,lo,hi):
        self.lo,self.hi=lo,hi
        self.left=self.right=None
        self.a=self.b=self.c=None
        self.qr=self.tau=self.top_a=self.top_b=self.top_c=None
        self.work=1

    def qt(self,values):
        values=np.array(values,dtype=float,order='F',copy=True)
        if values.ndim==1:values=values[:,None]
        out,_,info=dormqr('L','T',self.qr,self.tau,values,lwork=self.work,overwrite_c=True)
        if info:raise np.linalg.LinAlgError('dormqr failed: '+str(info))
        return out

class BlockQRFactor:
    """splu-compatible solve(rhs) interface for a real BVP block Jacobian."""
    def __init__(self,matrix,n,nodes,parameters):
        self.n,self.nodes,self.parameters=int(n),int(nodes),int(parameters)
        n,m,k=self.n,self.nodes,self.parameters
        if m<2 or n<1 or k<0:raise ValueError('Invalid BVP dimensions')
        if matrix.shape!=(n*m+k,n*m+k):raise ValueError('Unexpected Jacobian shape')
        J=matrix.tocsr();self.dimension=n*m+k
        # Refuse a matrix outside the exact claimed block structure.
        for i in range(m-1):
            row=J[i*n:(i+1)*n]
            low=row[:,:i*n];high=row[:,(i+2)*n:n*m]
            if np.any(low.data) or np.any(high.data):raise ValueError('Interior coupling is not adjacent')
        if np.any(J[n*(m-1):,n:n*(m-1)].data):raise ValueError('Boundary has interior-node coupling')
        def build(lo,hi):
            node=_Node(lo,hi)
            if hi==lo+1:
                rows=slice(lo*n,(lo+1)*n)
                node.a=J[rows,lo*n:(lo+1)*n].toarray()
                node.b=J[rows,hi*n:(hi+1)*n].toarray()
                node.c=J[rows,n*m:].toarray()
                return node
            mid=(lo+hi)//2;node.left=build(lo,mid);node.right=build(mid,hi)
            L,R=node.left,node.right
            center=np.asfortranarray(np.vstack((L.b,R.a)))
            qr,tau,work,info=dgeqrf(center,lwork=-1,overwrite_a=False)
            qr,tau,work,info=dgeqrf(center,lwork=max(n,int(work[0])),overwrite_a=True)
            if info:raise np.linalg.LinAlgError('dgeqrf failed: '+str(info))
            node.qr,node.tau=qr,tau
            sides=np.zeros((2*n,2*n+k),order='F');sides[:n,:n]=L.a;sides[n:,n:2*n]=R.b
            sides[:n,2*n:]=L.c;sides[n:,2*n:]=R.c
            _,work,info=dormqr('L','T',qr,tau,sides,lwork=-1,overwrite_c=False)
            if info:raise np.linalg.LinAlgError('dormqr workspace query failed')
            node.work=max(2*n+k,int(work[0]));transformed=node.qt(sides)
            node.top_a=transformed[:n,:n].copy();node.top_b=transformed[:n,n:2*n].copy();node.top_c=transformed[:n,2*n:].copy()
            node.a=transformed[n:,:n].copy();node.b=transformed[n:,n:2*n].copy();node.c=transformed[n:,2*n:].copy()
            for child in (L,R):child.a=child.b=child.c=None
            return node
        try:self.root=build(0,m-1)
        finally:build=None  # Break recursive closure -> CSR Jacobian cycle.
        rows=slice(n*(m-1),n*m+k)
        boundary=np.hstack((J[rows,:n].toarray(),J[rows,n*(m-1):n*m].toarray(),J[rows,n*m:].toarray()))
        final=np.vstack((np.hstack((self.root.a,self.root.b,self.root.c)),boundary))
        self.final_lu=lu_factor(final,check_finite=True)
        self.root.a=self.root.b=self.root.c=None
        self.stats=dict(kind='balanced-local-QR',n=n,nodes=m,parameters=k,root_dimension=2*n+k,internal_nodes=m-2)

    def solve(self,rhs):
        rhs=np.asarray(rhs,float)
        vector=rhs.ndim==1
        if vector:rhs=rhs[:,None]
        if rhs.shape[0]!=self.dimension:raise ValueError('Wrong RHS length')
        n,m,k=self.n,self.nodes,self.parameters;nr=rhs.shape[1];tops={}
        def forward(node):
            if node.left is None:return rhs[node.lo*n:(node.lo+1)*n]
            transformed=node.qt(np.vstack((forward(node.left),forward(node.right))))
            tops[id(node)]=transformed[:n].copy();return transformed[n:]
        try:coarse=forward(self.root)
        finally:forward=None  # Do not retain the RHS through a recursive cell.
        edge=lu_solve(self.final_lu,np.vstack((coarse,rhs[n*(m-1):])),check_finite=True)
        answer=np.empty((n*m+k,nr));answer[:n]=edge[:n];answer[n*(m-1):n*m]=edge[n:2*n];answer[n*m:]=edge[2*n:]
        params=edge[2*n:]
        def backward(node):
            if node.left is None:return
            left=answer[node.lo*n:(node.lo+1)*n];right=answer[node.hi*n:(node.hi+1)*n]
            mid=node.left.hi
            value=tops.pop(id(node))-node.top_a@left-node.top_b@right-node.top_c@params
            answer[mid*n:(mid+1)*n]=solve_triangular(node.qr[:n,:],value,lower=False,check_finite=False)
            backward(node.left);backward(node.right)
        try:backward(self.root)
        finally:backward=None  # Do not retain the returned answer by a cycle.
        return answer[:,0] if vector else answer
