"""Core-control homotopy with unchanged represented low Fourier moments.

At lambda=0 each compactly supported f_j is replaced by its first M sine
modes. At lambda=1 the exact compact support and protected circular arc are
restored. Thus numerical design homotopy does not add a spurious low-moment
rank crossing. This does not remove a possible geometric compatibility
obstruction or certify convergence as M grows.
"""
import math
import numpy as np
from plateau_core import PlateauSupportCore

_CACHE={}


class HomotopyPlateauCore(PlateauSupportCore):
    def _projection(self):
        if hasattr(self,'_sine_projection'):return
        M=len(self.c)+1;key=(self.base_mode,M,self.a,self.center)
        if key not in _CACHE:
            x,w=np.polynomial.legendre.leggauss(max(64,6*M))
            phi=self.center+self.a+self.L*(x+1)/2
            compact=PlateauSupportCore._basis(self,phi)[0]
            freq=self.base_mode*np.arange(1,M+1)
            coef=self.L/self.T*(compact*w)@np.sin(freq[:,None]*phi).T
            R=coef*freq*(1-freq**2)
            if len(self.c):
                om=self.omega;P=self.Pmax;L=self.L
                bound=((P[2]+2*om*P[1]+om**2*P[0])/L**2+(P[4]+4*om*P[3]+6*om**2*P[2]+4*om**3*P[1]+om**4*P[0])/L**4)/self.norms
                if np.max(np.sum(abs(R),axis=1))>1 or np.max(np.sum(abs(R)*freq,axis=1)/bound)>1:
                    raise FloatingPointError('Truncated control requires a larger explicit positivity derivative bound')
            _CACHE[key]=(freq,coef)
        self._projection_frequencies,self._sine_projection=_CACHE[key]
    def _truncated_derivative(self,phi,j):
        self._projection();phi=np.asarray(phi).ravel();m=self._projection_frequencies
        return (self._sine_projection*m**j)@np.sin(m[:,None]*phi+j*np.pi/2)
    def _compact_derivative(self,phi,j):
        phi=np.asarray(phi).ravel();z=(phi-self.center-self.a)%self.T
        inside=z<self.L;t=np.clip(z/self.L,0.,1.);om=self.omega[:,None];angle=om*t[None,:]
        out=sum(math.comb(j,k)*self.polys[j-k](t)[None,:]*om**k*np.sin(angle+k*np.pi/2)for k in range(j+1))/self.L**j
        return np.where(inside[None,:],out/self.norms[:,None],0.)
    def _basis(self,phi):
        compact=PlateauSupportCore._basis(self,phi)
        if self.lam==1 or len(self.c)==0:return compact
        return tuple(self.lam*c+(1-self.lam)*self._truncated_derivative(phi,j)for j,c in enumerate(compact))
    def rho_material_jets(self,theta):
        g=super().rho_material_jets(theta)
        if self.lam==1 or len(self.c)==0:return g
        phi=g['phi']
        rp=g['rho_phi']+(1-self.lam)*(self.c@(self._truncated_derivative(phi,2)+self._truncated_derivative(phi,4)-self._compact_derivative(phi,2)-self._compact_derivative(phi,4)))
        rpp=g['rho_phiphi']+(1-self.lam)*(self.c@(self._truncated_derivative(phi,3)+self._truncated_derivative(phi,5)-self._compact_derivative(phi,3)-self._compact_derivative(phi,5)))
        rho=g['rho'];g.update(rho_phi=rp,rho_phiphi=rpp,rho_u=rp/rho,rho_uu=(rpp*rho-rp*rp)/rho**3)
        return g
    def summary(self):
        out=super().summary();out.update(control_homotopy='lambda compact + (1-lambda) identical-low-sine-moment projection',control_projection_order=len(self.c)+1)
        return out
