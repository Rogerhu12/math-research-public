"""Complete physical normal in independent refined XYZ and coarse log-radius spaces."""
import numpy as np
from scipy.linalg import cho_factor, cho_solve, cho_solve_banded


class MixedLinear:
    def __init__(self,full,transform):
        self.full=full
        self.transform=np.asarray(transform,float)
        self.residual=full.residual
        self.basis=full.basis
        self.shape=(full.shape[0],self.basis.dimension+self.transform.shape[1])
        if self.transform.shape[0]!=self.basis.nb:
            raise ValueError("The coarse radius must embed in the actual Cartesian radial space")

    def combine(self,z,alpha):
        return np.concatenate((np.asarray(z).ravel(),np.asarray(alpha).ravel()))

    def split(self,vector):
        v=np.asarray(vector)
        if v.shape!=(self.shape[1],):
            raise ValueError("Every mixed-space parameter is required")
        n=self.basis.dimension
        return v[:n].reshape(self.basis.nb,self.basis.na),v[n:]

    def lift(self,vec):
        z,a=self.split(vec)
        return self.full.pack(z,self.transform@a)

    def restrict(self,vec):
        z,a=self.full.split(vec)
        return self.combine(z,self.transform.T@a)

    def matvec(self,vec):
        return self.full.matvec(self.lift(vec))

    def transpose(self,vec):
        return self.restrict(self.full.transpose(vec))

    def sobolev_apply(self,vec):
        return self.restrict(self.full.sobolev_apply(self.lift(vec)))


class MixedSchur:
    def __init__(self,linear,damping):
        self.linear=linear
        self.damping=damping
        full=linear.full
        normal=full.deps["normal"]
        self.A=normal.CompleteAreaRadialNormal(full.position,eta=damping)
        self.released=self.A.normal_band.nbytes
        del self.A.normal_band
        cross,gram=full.cross_normal()
        transform=linear.transform
        self.B=cross@transform
        radius_lower=full.position.preconditioner.factors[0][0]
        st=normal.triangular_apply(radius_lower,normal.triangular_apply(radius_lower,transform,True),False)
        C=transform.T@(gram@transform+damping*st)
        self.inverse_cross=self.position_solve(self.B)
        reduced=C-self.B.T@self.inverse_cross
        asym=np.linalg.norm(reduced-reduced.T)/np.linalg.norm(reduced)
        self.factor=cho_factor((reduced+reduced.T)*.5,lower=True)
        self.receipt=dict(schema="complete-two-space-XYZ-and-log-radius-Schur-v1",
            cartesian=self.A.receipt,fullRadiusColumns=len(transform),
            coarseRadiusColumns=transform.shape[1],physicalColumns=linear.shape[1],
            completeCartesianRadiusCrossRetained=True,schurRelativeAsymmetry=float(asym),
            minimumCholeskyPivot=float(np.diag(self.factor[0]).min()))

    def position_solve(self,rhs):
        scale=self.A.diagonal_scale
        if rhs.ndim==2:
            scale=scale[:,None]
        return scale*cho_solve_banded((self.A.factor,True),scale*rhs)

    def solve(self,rhs):
        x,a=self.linear.split(rhs)
        base=self.position_solve(x.ravel())
        radius=cho_solve(self.factor,a-self.B.T@base)
        return self.linear.combine(base-self.inverse_cross@radius,radius)

    def residual(self,direction):
        l=self.linear
        return l.transpose(l.matvec(direction))+self.damping*l.sobolev_apply(direction)+l.transpose(l.residual)
