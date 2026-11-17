#!/usr/bin/env python3
"""Complete sampled weighted-tail Jacobian by Fourier products and one mean row.

No physical mode, nonlinear Fourier product, weighted mean term, or alias is
discarded.  The four pointwise derivatives of the full K equation are analytic.
One local complex directional derivative transports the constraint gradient;
it replaces a complex-step evaluation for every global Fourier state column.
"""
import numpy as np
from parallel_20261117_weighted_tail import WeightedMean


class FastWeightedMean(WeightedMean):
    def __init__(self,M,N,rho_coefficients):
        super().__init__(M,N,rho_coefficients)
        self.minus=(self.freq[:,None]-self.freq[None,:])%N
        self.plus=(self.freq[:,None]+self.freq[None,:])%N

    @staticmethod
    def mean_partials(P,T,K,z):
        E=1+z;yy=1+K;D=1-z*(2*K+K*K+E*P*P);S=1-z*P*P;Q=np.sqrt(D)
        N=1+z*yy*T/S;L=yy+E*T
        BP=E*P*N/Q**3+2*z*yy*T*P/(S*S*Q)
        return BP,yy/(S*Q),L/Q**3

    def coefficient_gradient(self,BP,BT,BK):
        # These are the literal gradients of Q_N[rho*B], not unweighted
        # Fourier means.  The first state is Ptilde, hence its two terms.
        U=np.fft.fft(BP-BT*self.Rp/self.R**2,axis=0)/self.N
        V=np.fft.fft(BT/self.R,axis=0)/self.N
        W=np.fft.fft(self.R*BK,axis=0)/self.N
        return np.vstack((-U[self.freq].imag+self.freq[:,None]*V[self.freq].real,
                          W[self.freq].real,W[0].real))

    def jacobian(self,y,s,ell,z):
        y=np.atleast_2d(y);s=np.asarray(s);ell=np.asarray(ell);z=np.asarray(z)
        F=self.evaluate(y,s,ell,z);P,T,K,V=self.fields(y)
        E=1+z;U=V-P;L=1+K+E*T
        numerator=E*s*U*U+ell*((K+T)**2+z*(2*K*T+T*T-P*P))
        fP=(-2*E*s*U-2*ell*z*P)/L
        fV=2*E*s*U/L
        fK=-2*ell+2*ell*(K+E*T)/L-numerator/L**2
        fT=-ell+2*ell*E*(K+T)/L-E*numerator/L**2
        A=np.fft.fft(fP/self.R-fT*self.Rp/self.R**3,axis=0)/self.N
        B=np.fft.fft(fT/self.R**2,axis=0)/self.N
        C=np.fft.fft(fK,axis=0)/self.N
        D=np.fft.fft(fV/self.R,axis=0)/self.N
        J=np.zeros((self.n,self.n,y.shape[1]));ii=np.arange(self.M);n=self.freq[None,:,None]
        J[ii,ii]=-(s+ell);J[ii,self.M+ii]=-self.freq[:,None]*s
        J[self.M:2*self.M,:self.M]=(-1j*A[self.minus]+1j*A[self.plus]+n*(B[self.minus]+B[self.plus])).real
        J[self.M:2*self.M,self.M:2*self.M]=(C[self.minus]+C[self.plus]+1j*n*(D[self.minus]-D[self.plus])).real
        J[self.M:2*self.M,-1]=2*C[self.freq].real
        BP,BT,BK=self.mean_partials(P,T,K,z);gradient=self.coefficient_gradient(BP,BT,BK)
        pt=self.S@F[:self.M];px=pt/self.R
        tx=(self.C@(self.freq[:,None]*F[:self.M]))/self.R**2-pt*self.Rp/self.R**3
        kx=self.C@F[self.M:2*self.M]+F[-1]
        h=1e-25
        dBP,dBT,dBK=self.mean_partials(P+1j*h*px,T+1j*h*tx,K+1j*h*kx,z+1j*h*2*ell*z)
        transport=self.coefficient_gradient(dBP.imag/h,dBT.imag/h,dBK.imag/h)
        derivative_of_resolved_flow=np.einsum('ap,ajp->jp',gradient[:2*self.M],J[:2*self.M])
        J[-1]=-(transport+derivative_of_resolved_flow)/gradient[-1]
        return J
