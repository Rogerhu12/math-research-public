#!/usr/bin/env python3
"""Full C2 double-integrated coordinates and exact-model endpoint projection.

No solver and no geometry sampling.  All A/E/D coordinates are retained.
The caller binds the actual ClosedGram/warm/scalar identities and fixes the
positive coordinate scale before a numerical budget.  The small Gram blocks
implement the published complete endpoint matrix, including core R/T pairs.
"""
import numpy as np


class DoubleIntegrated:
    def __init__(self, problem, scale=None):
        self.problem = problem
        self.J, self.n, self.M, self.K = problem.J, problem.n, problem.M, problem.K
        self.h = np.diff(problem.mesh).copy()
        self.total_length = float(problem.mesh[-1]-problem.mesh[0])
        self.t = self.total_length-(problem.mesh[:-1]+self.h/2)
        if problem.mesh[0] != 0 or not np.all(self.h > 0):
            raise ValueError("The fixed positive mesh must start at zero")
        self.w = np.zeros(self.J)
        self.v = np.zeros(self.J)
        self.w[:-1] += self.h/2
        self.w[1:] += self.h/2
        self.v[:-1] += self.h*self.t/2
        self.v[1:] += self.h*self.t/2
        self.nc = self.M-self.K
        self.na0 = 2*self.M+1
        self.nai = (self.J-2)*self.n
        self.ne = (self.J-1)*self.n
        self.size = self.nc+self.na0+self.nai+2*self.ne+1
        if self.size-2*self.n != problem.free_size:
            raise ValueError("Integrated coordinates lost original free variables")
        self.scale = np.ones(self.size) if scale is None else np.array(scale,dtype=float,copy=True)
        if self.scale.shape != (self.size,) or not np.isfinite(self.scale).all() or not np.all(self.scale > 0):
            raise ValueError("Every declared coordinate scale must be finite and positive")
        self.offset = np.zeros(2*self.n)
        self.offset[2*self.M+1] = 1.
        c = np.zeros(self.n)
        c[0] = 1.
        c[1:1+self.K] = problem.fixed_core
        c[self.M+1:self.M+1+self.K] = -problem.freq[:self.K]*problem.fixed_core
        self.offset[self.n:] = c+self.total_length*self.offset[:self.n]
        self.groups = self._gram_blocks()

    def _parts(self, x):
        x = np.asarray(x)
        if x.shape != (self.size,):
            raise ValueError("Wrong complete integrated-coordinate shape")
        at = self.nc
        core = x[:at]
        A = np.zeros((self.J,self.n),dtype=np.result_type(x.dtype,float))
        A[0,:self.na0] = x[at:at+self.na0]
        at += self.na0
        A[1:-1] = x[at:at+self.nai].reshape(self.J-2,self.n)
        at += self.nai
        E = x[at:at+self.ne].reshape(self.J-1,self.n)
        at += self.ne
        D = x[at:at+self.ne].reshape(self.J-1,self.n)
        return core,A,E,D,x[-1]

    def _pack(self, core, A, E, D, height):
        return np.concatenate((np.asarray(core),A[0,:self.na0],A[1:-1].ravel(),
                               E.ravel(),D.ravel(),np.asarray([height])))

    def raw(self, x, *, affine=False):
        """Return every raw Y/U/A node, before dropping any endpoint error."""
        core,A,E,D,height = self._parts(x)
        dtype = np.result_type(A.dtype,float)
        U = np.zeros_like(A)
        C = np.zeros(self.n,dtype=dtype)
        allc = np.zeros(self.M,dtype=dtype)
        allc[self.K:] = core
        if affine:
            allc[:self.K] = self.problem.fixed_core
            C[0] = 1.
            U[0,2*self.M+1] = 1.
        C[1:self.M+1] = allc
        C[self.M+1:2*self.M+1] = -self.problem.freq*allc
        U[1:] = U[0]+np.cumsum(self.h[:,None]*(.5*(A[:-1]+A[1:])+E),axis=0)
        Y = np.empty_like(A)
        Y[0] = C
        Y[1:] = C+np.cumsum(self.h[:,None]*(.5*(U[:-1]+U[1:])+D),axis=0)
        return np.stack((Y,U,A),axis=1),height

    def extract(self, jets, height):
        """The literal Extract in Jfree Extract T2 S2 Pi2."""
        return np.concatenate((jets[0,0,1+self.K:self.M+1],
                               jets[0,2,:self.na0],jets[1:-1].ravel(),
                               np.asarray([height])))

    def to_free(self, x, *, affine=False):
        jets,height = self.raw(x,affine=affine)
        return self.extract(jets,height)

    def inverse(self, free_x, *, affine=True):
        """Retain every actual trapezoidal defect; never impose E=D=0."""
        jets,height,core = self.problem.unpack(free_x,tangent=not affine)
        Y,U,A = jets[:,0],jets[:,1],jets[:,2]
        E = np.diff(U,axis=0)/self.h[:,None]-.5*(A[:-1]+A[1:])
        D = np.diff(Y,axis=0)/self.h[:,None]-.5*(U[:-1]+U[1:])
        return self._pack(core[self.K:],A,E,D,height)

    def raw_transpose(self, jets_gradient, height_gradient=0.):
        g = np.asarray(jets_gradient)
        if g.shape != (self.J,3,self.n):
            raise ValueError("Need all raw node-jet covectors")
        gY,gU,gA = g[:,0],g[:,1].copy(),g[:,2].copy()
        q = np.cumsum(gY[::-1],axis=0)[::-1][1:]
        D = self.h[:,None]*q
        gU[:-1] += .5*D
        gU[1:] += .5*D
        r = np.cumsum(gU[::-1],axis=0)[::-1][1:]
        E = self.h[:,None]*r
        gA[:-1] += .5*E
        gA[1:] += .5*E
        gC = np.sum(gY,axis=0)
        core = gC[1:self.M+1]-self.problem.freq*gC[self.M+1:2*self.M+1]
        return self._pack(core[self.K:],gA,E,D,height_gradient)

    def free_transpose(self, free_gradient):
        """Extract^T first; no duplicate core chain after Jfree's own VJP."""
        x = np.asarray(free_gradient)
        if x.shape != (self.problem.free_size,):
            raise ValueError("Wrong original free covector")
        jets = np.zeros((self.J,3,self.n),dtype=np.result_type(x.dtype,float))
        at = self.nc
        jets[0,0,1+self.K:self.M+1] = x[:at]
        jets[0,2,:self.na0] = x[at:at+self.na0]
        at += self.na0
        jets[1:-1] = x[at:-1].reshape(self.J-2,3,self.n)
        return self.raw_transpose(jets,x[-1])

    def endpoint(self, x, *, affine=False):
        core,A,E,D,_ = self._parts(x)
        u = self.w@A+self.h@E
        y = self.v@A+(self.h*self.t)@E+self.h@D
        y[1+self.K:self.M+1] += core
        y[self.M+1+self.K:2*self.M+1] -= self.problem.freq[self.K:]*core
        result = np.concatenate((u,y))
        return result+self.offset if affine else result

    def endpoint_transpose(self, weights):
        b = np.asarray(weights)
        if b.shape != (2*self.n,):
            raise ValueError("Need the complete U-end/Y-end covector")
        u,y = b[:self.n],b[self.n:]
        core = y[1:self.M+1]-self.problem.freq*y[self.M+1:2*self.M+1]
        A = self.w[:,None]*u+self.v[:,None]*y
        E = self.h[:,None]*(u+self.t[:,None]*y)
        D = self.h[:,None]*y
        return self._pack(core[self.K:],A,E,D,0.)

    def _gram_blocks(self):
        sc,sA,sE,sD,_ = self._parts(self.scale)
        aa = sA*sA
        ee = sE*sE
        dd = sD*sD
        g11 = (self.w*self.w)@aa+(self.h*self.h)@ee
        g12 = (self.w*self.v)@aa+(self.h*self.h*self.t)@ee
        g22 = (self.v*self.v)@aa+(self.h*self.h*self.t*self.t)@ee+(self.h*self.h)@dd
        if not np.isfinite(np.r_[g11,g12,g22]).all():
            raise ValueError("Numerical endpoint Gram overflows the declared scale")
        paired = set()
        groups = []
        def make(indices, matrix):
            diag = np.sqrt(np.diag(matrix))
            if not np.isfinite(diag).all() or not np.all(diag > 0):
                raise ValueError("Numerical positive scale is too small for endpoint Gram")
            normalized = matrix/diag[:,None]/diag[None,:]
            chol = np.linalg.cholesky(normalized)
            inverse = np.linalg.solve(chol.T,np.linalg.solve(chol,np.eye(len(indices))))
            groups.append(dict(indices=np.asarray(indices,dtype=int),matrix=matrix,
                               diagonal=diag,inverse_normalized=inverse,
                               normalized_condition=float(np.linalg.cond(normalized))))
        for j in range(self.K+1,self.M+1):
            R,T = j,self.M+j
            paired.update((R,T))
            mat = np.array([[g11[R],g12[R],0.,0.],
                            [g12[R],g22[R],0.,0.],
                            [0.,0.,g11[T],g12[T]],
                            [0.,0.,g12[T],g22[T]]])
            vec = np.array([0.,1.,0.,-self.problem.freq[j-1]])
            mat += sc[j-1-self.K]**2*np.outer(vec,vec)
            make([R,self.n+R,T,self.n+T],mat)
        for k in range(self.n):
            if k not in paired:
                make([k,self.n+k],np.array([[g11[k],g12[k]],[g12[k],g22[k]]]))
        covered = sorted(int(i) for group in groups for i in group['indices'])
        if covered != list(range(2*self.n)):
            raise ValueError("Endpoint block partition dropped or duplicated rows")
        return groups

    def gram_action(self, b):
        b = np.asarray(b)
        if b.shape != (2*self.n,):
            raise ValueError("Wrong complete endpoint vector")
        result = np.empty_like(b,dtype=np.result_type(b.dtype,float))
        for group in self.groups:
            ind = group['indices']
            result[ind] = group['matrix']@b[ind]
        return result

    def gram_solve(self, b):
        b = np.asarray(b)
        if b.shape != (2*self.n,):
            raise ValueError("Wrong complete endpoint right hand side")
        result = np.empty_like(b,dtype=np.result_type(b.dtype,float))
        for group in self.groups:
            ind = group['indices']
            d = group['diagonal']
            result[ind] = (group['inverse_normalized']@(b[ind]/d))/d
        return result

    def project(self, z):
        z = np.asarray(z)
        if z.shape != (self.size,):
            raise ValueError("Wrong complete scaled direction")
        return z-self.scale*self.endpoint_transpose(
            self.gram_solve(self.endpoint(self.scale*z)))

    def lift(self, z):
        """Full original free-space direction with both end rows projected."""
        return self.to_free(self.scale*self.project(z),affine=False)

    def pullback(self, free_gradient):
        return self.project(self.scale*self.free_transpose(free_gradient))

    def repair(self, integrated_state):
        """Explicit affine repair in the same declared coordinate norm."""
        x = np.asarray(integrated_state)
        return x-self.scale*self.scale*self.endpoint_transpose(
            self.gram_solve(self.endpoint(x,affine=True)))

    def metadata(self):
        return dict(integrated_coordinates=self.size,
                    original_free_coordinates=self.problem.free_size,
                    projected_endpoint_rows=2*self.n,
                    all_accelerations_and_both_defects_retained=True,
                    blocks2=sum(len(g['indices'])==2 for g in self.groups),
                    blocks4=sum(len(g['indices'])==4 for g in self.groups),
                    normalized_block_condition_max=max(g['normalized_condition'] for g in self.groups),
                    scale_min=float(np.min(self.scale)),scale_max=float(np.max(self.scale)),
                    nonlinear_solve_executed=False,geometry_certified=False)


if __name__ == '__main__':
    raise SystemExit("Import-only: bind the actual fullclosed problem and frozen scale before probing.")
