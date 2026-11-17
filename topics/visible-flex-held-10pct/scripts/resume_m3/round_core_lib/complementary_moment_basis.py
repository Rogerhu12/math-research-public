"""C4 support controls with exact defining mean/primary constraints.

The mathematical coefficients are defined by explicit integrals and inverses.
The implementation evaluates those constants with mpmath at recorded precision
and returns float64 function values. No Fourier truncation represents support.
Canonical high support moments are cos(2n phi),...,cos(Mn phi).
Locking the primary moment is optional; without that extra constraint its
fixed leakage is included in the lambda=0 represented projection.
"""
from __future__ import annotations
import math
from fractions import Fraction as F
from functools import lru_cache
import numpy as np
from numpy.polynomial import Polynomial
import mpmath as mp
from moment_interval_bounds import coefficient_enclosures,upper_abs,upper_float

_S_COEF=[0,0,0,0,0,126,-420,540,-315,70]
_S=Polynomial(_S_COEF)
_SP=[_S.deriv(k) for k in range(6)]


@lru_cache(None)
def cutoff_derivative_upper(order):
    """Exact rational Bernstein upper bound on |S^(order)|, t in [0,1]."""
    if order==0:return F(1)
    co=[F(_S_COEF[k]*math.factorial(k)//math.factorial(k-order)) for k in range(order,10)]
    deg=len(co)-1;bound=F(0)
    for cell in range(64):
        a,h=F(cell,64),F(1,64);power=[F(0)]*(deg+1)
        for j,v in enumerate(co):
            for k in range(j+1):power[k]+=v*math.comb(j,k)*a**(j-k)*h**k
        bern=[sum(power[j]*F(math.comb(k,j),math.comb(deg,j)) for j in range(k+1)) for k in range(deg+1)]
        bound=max(bound,max(abs(v) for v in bern))
    return bound


@lru_cache(None)
def _constants(n,M,a,eps,center_half_period,precision,lock_fundamental):
    """Closed exponential-polynomial moments at arbitrary precision."""
    with mp.workdps(precision):
        a=mp.mpf(str(a));eps=mp.mpf(str(eps));T=2*mp.pi/n
        W=[1-(2*a+eps)/T]
        for j in range(1,2*M+1):
            omega=mp.mpf(n*j);z=omega*eps;iz=mp.j*z;e=mp.exp(iz)
            I=[mp.expm1(iz)/iz]
            for k in range(1,10):I.append(e/iz-k*I[-1]/iz)
            transition=eps*mp.re(mp.exp(mp.j*omega*a)*sum(_S_COEF[k]*I[k] for k in range(10)))
            val=2/T*(transition-mp.sin(omega*(a+eps))/omega)
            W.append(val*((-1)**(j*center_half_period)))
        G=mp.matrix(M+1,M+1)
        for j in range(M+1):
            for k in range(M+1):G[j,k]=W[k] if j==0 else W[j] if k==0 else (W[abs(j-k)]+W[j+k])/2
        C=mp.matrix(2,M-1);low=G[:2,:2]
        for j in range(M-1):
            if lock_fundamental:
                c=mp.lu_solve(low,G[:2,j+2]);C[0,j]=c[0];C[1,j]=c[1]
            else:
                C[0,j]=G[0,j+2]/G[0,0];C[1,j]=0
        A=2*(G[2:,2:]-G[2:,:2]*C)
        inv=A**-1;H=mp.matrix(M-1,M+1)
        for j in range(M-1):
            H[j,0]=-sum(inv[k,j]*C[0,k] for k in range(M-1))
            H[j,1]=-sum(inv[k,j]*C[1,k] for k in range(M-1))
            for k in range(M-1):H[j,k+2]=inv[k,j]
        eigen=mp.eigsy(A,eigvals_only=True)
        if eigen[0]<=0:raise ArithmeticError('The exact weighted Gram Schur complement must be positive')
        D=mp.diag([1-(n*j)**2 for j in range(2,M+1)])
        singular=mp.svd(D*A,compute_uv=False)
        moment=2*G*H.T
        expected=mp.matrix(M+1,M-1)
        for j in range(M-1):
            expected[j+2,j]=1
            if not lock_fundamental:expected[1,j]=moment[1,j]
        residual=max(abs(moment[i,j]-expected[i,j]) for i in range(M+1) for j in range(M-1))
        conv=lambda mat:np.array([[float(mat[i,j]) for j in range(mat.cols)] for i in range(mat.rows)])
        return dict(raw_constraints=conv(C),raw_support_matrix=conv(A),canonical_trig_coefficients=conv(H),
                    gram=conv(G),fundamental_leakage=np.array([float(moment[1,j]) for j in range(M-1)]),
                    support_condition=float(eigen[eigen.rows-1]/eigen[0]),
                    rho_condition=float(singular[0]/singular[singular.rows-1]),
                    minimum_eigenvalue=float(eigen[0]),maximum_eigenvalue=float(eigen[eigen.rows-1]),
                    high_precision_moment_residual=mp.nstr(residual,12),
                    matrix_decimal=[[mp.nstr(A[i,j],precision-10) for j in range(M-1)] for i in range(M-1)])


class ComplementaryMomentBasis:
    """M-1 controls, indexed by target support frequencies 2n,...,Mn.

    b_j is the support change; f_j'=b_j is the periodic primitive which is
    identically zero on the protected arc. b is C4 and f is C5.
    `support_jets` returns b,b',...,b''''; `primitive_jets` returns f through f^(5).
    At homotopy=0 the support controls are exactly their represented low
    moments. With lock_fundamental=True these are cos(j*n*phi), j=2,...,M.
    """
    def __init__(self,base_mode=4,modes=6,halfwidth=.145,transition=.08,
                 center=0.,precision=80,quadrature_order=64,lock_fundamental=False):
        self.n=int(base_mode);self.M=int(modes);self.a=float(halfwidth);self.eps=float(transition)
        self.T=2*np.pi/self.n;self.center=float(center)
        if self.n<2 or self.M<2 or not 0<self.a<self.a+self.eps<self.T/2:
            raise ValueError('Invalid complementary control geometry')
        self.center_half_period=int(round(self.center/(self.T/2)))
        if self.center_half_period not in (0,1) or abs(self.center-self.center_half_period*self.T/2)>1e-12:
            raise ValueError('Only reflection centers 0 and pi/n are supported')
        self.precision=int(precision)
        self.lock_fundamental=bool(lock_fundamental)
        self.constants=_constants(self.n,self.M,self.a,self.eps,self.center_half_period,self.precision,self.lock_fundamental)
        self.H=self.constants['canonical_trig_coefficients'].copy()
        self.fundamental_leakage=self.constants['fundamental_leakage'].copy()
        if self.lock_fundamental:self.fundamental_leakage.fill(0.)
        self.freq=self.n*np.arange(self.M+1);self.target_freq=self.freq[2:]
        self.gx,self.gw=np.polynomial.legendre.leggauss(int(quadrature_order))
        self.certificate=coefficient_enclosures(self.n,self.M,str(self.a),str(self.eps),self.center_half_period,self.lock_fundamental)
        bounds=self.certificate['coefficients'];eps_exact=F(str(self.eps))
        cutoff=[cutoff_derivative_upper(k)/eps_exact**k for k in range(6)]
        absolute=[[upper_abs(v) for v in row] for row in bounds]
        error=[[max(abs(F.from_float(float(self.H[j,k]))-v) for v in bounds[j][k]) for k in range(self.M+1)] for j in range(self.M-1)]
        def derivative_bounds(coeff):
            trig=[[sum(coeff[j][k]*(int(self.freq[k])**r if r else 1) for k in range(self.M+1)) for j in range(self.M-1)] for r in range(6)]
            return np.array([[upper_float(sum(math.comb(r,l)*cutoff[l]*trig[r-l][j] for l in range(r+1))) for j in range(self.M-1)] for r in range(6)])
        self.cutoff_bounds=np.array([upper_float(v) for v in cutoff])
        self.derivative_bounds=derivative_bounds(absolute)
        self.coefficient_evaluation_error_bounds=derivative_bounds(error)
        self.fundamental_absolute_upper=np.array([upper_float(upper_abs(v)) if upper_abs(v) else 0. for v in self.certificate['fundamental']])
        self.fundamental_evaluation_error=np.array([upper_float(max(abs(F.from_float(float(self.fundamental_leakage[j]))-v) for v in bounds)) for j,bounds in enumerate(self.certificate['fundamental'])])

    def _local(self,phi):
        phi=np.asarray(phi,float)
        delta=phi-self.center
        return delta-np.floor((delta+self.T/2)/self.T)*self.T

    def _cutoff(self,x,max_order):
        d=abs(x);t=np.clip((d-self.a)/self.eps,0.,1.)
        inside=(d>self.a)&(d<self.a+self.eps)
        values=[np.where(d<=self.a,0.,np.where(d>=self.a+self.eps,1.,_SP[0](t)))]
        for k in range(1,max_order+1):
            values.append(np.where(inside,_SP[k](t)*np.sign(x)**k/self.eps**k,0.))
        return values

    def support_jets(self,phi,order=4,homotopy=1.):
        if not 0<=order<=5 or not 0<=homotopy<=1:raise ValueError('Invalid derivative/homotopy')
        x=self._local(phi).ravel();cut=self._cutoff(x,order)
        parity=(-1.)**(np.arange(self.M+1)*self.center_half_period)
        G=[]
        for k in range(order+1):
            freq_power=np.ones_like(self.freq) if k==0 else self.freq**k
            G.append((self.H*(parity*freq_power)[None,:])@np.cos(self.freq[:,None]*x+k*np.pi/2))
        result=[]
        for k in range(order+1):
            compact=sum(math.comb(k,l)*cut[l]*G[k-l] for l in range(k+1))
            if homotopy!=1.:
                analytic=self.target_freq[:,None]**k*np.cos(self.target_freq[:,None]*(x+self.center)+k*np.pi/2)
                analytic+=self.fundamental_leakage[:,None]*self.n**k*np.cos(self.n*(x+self.center)+k*np.pi/2)
                compact=homotopy*compact+(1-homotopy)*analytic
            result.append(compact)
        return tuple(result)

    def primitive(self,phi,homotopy=1.):
        x=self._local(phi).ravel();d=abs(x);out=np.zeros((self.M-1,len(x)))
        transition=(d>self.a)&(d<self.a+self.eps)
        if np.any(transition):
            length=d[transition]-self.a
            t=self.a+length[:,None]*(self.gx+1)/2
            vals=self.support_jets(self.center+t.ravel(),0,1.)[0].reshape(self.M-1,len(length),len(self.gx))
            out[:,transition]=length[None,:]/2*np.einsum('jkq,q->jk',vals,self.gw)
        outside=d>=self.a+self.eps
        if np.any(outside):
            # Use mean-zero and integrate backwards from the reflection point;
            # sinc avoids subtracting nearly equal sine values at the period end.
            length=self.T/2-d[outside]
            parity=(-1.)**(np.arange(1,self.M+1)*(self.center_half_period+1)+1)
            vals=np.sinc(self.freq[1:,None]*length[None,:]/np.pi)
            out[:,outside]=length[None,:]*(-self.H[:,0,None]+(self.H[:,1:]*parity[None,:])@vals)
        out*=np.sign(x)[None,:]
        if homotopy!=1.:
            analytic=np.sin(self.target_freq[:,None]*(x+self.center))/self.target_freq[:,None]
            analytic+=self.fundamental_leakage[:,None]*np.sin(self.n*(x+self.center))/self.n
            out=homotopy*out+(1-homotopy)*analytic
        return out

    def primitive_jets(self,phi,order=5,homotopy=1.):
        if not 0<=order<=5:raise ValueError('Available primitive orders are zero through five')
        first=self.primitive(phi,homotopy)
        return (first,) if order==0 else (first,)+self.support_jets(phi,order-1,homotopy)

    def homotopy_rho_bounds(self,homotopy=1.):
        """Triangle bounds for rho-control and its first two phi derivatives."""
        if not 0<=homotopy<=1:raise ValueError('Invalid homotopy')
        out=[]
        for k in range(3):
            compact=self.derivative_bounds[k]+self.derivative_bounds[k+2]
            low=self.target_freq**k*(self.target_freq**2-1)+self.fundamental_absolute_upper*self.n**k*(self.n**2-1)
            out.append(homotopy*compact+(1-homotopy)*low)
        return tuple(out)

    def summary(self):
        return dict(base_mode=self.n,modes=self.M,halfwidth=self.a,transition=self.eps,
                    center=self.center,precision=self.precision,controls=self.M-1,lock_fundamental=self.lock_fundamental,
                    support_condition=self.constants['support_condition'],rho_condition=self.constants['rho_condition'],
                    high_precision_moment_residual=self.constants['high_precision_moment_residual'],
                    coefficient_neumann_residual_upper=upper_float(self.certificate['neumann_residual']),
                    coefficient_inverse_error_upper=upper_float(self.certificate['inverse_error']),
                    canonical_low_moments='mean=0; support cosine coefficients at 2n,...,Mn form identity; the primary is zero only when explicitly locked',
                    fundamental_leakage=self.fundamental_leakage.tolist(),
                    support_derivative_upper_bounds=self.derivative_bounds[:5].T.tolist(),
                    rho_derivative_upper_bounds=(self.derivative_bounds[1]+self.derivative_bounds[3]).tolist(),
                    scope='Explicit supported functions and high-precision moment preconditioner; numerical evaluation and all reported sampled suprema are not interval geometry certificates.')
