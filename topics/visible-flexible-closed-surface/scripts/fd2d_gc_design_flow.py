#!/usr/bin/env python3
"""Positive-normal finite Codazzi equations/JVP in a smooth T-design chart."""
import numpy as np
from fd2d_gc_logshape_stable import LogShapeGC


class DesignLogShapeGC(LogShapeGC):
    def fields(self, x, state):
        f = super().fields(x, state)
        design = self.candidate.jet(x)
        f['radial_scale'] = design['radial_scale']
        f['radial_scale_T'] = design['radial_scale_T']
        f['a_T_over_a'] = design['a_T']/design['a']
        f['c_T'] = design['c_T']
        # a_s,a_ss are independent of T in the unchanged phase pieces and
        # constant in either changing coast, at this chosen radial chart.
        f['beta_T'] = f['beta']*f['a_T_over_a']
        f['physical_s'] = design['s']
        return f

    def rhs(self, x, state):
        f = self.fields(x, state)
        eta, zeta, q = f['eta'], f['zeta'], f['inverse_exponential']
        dx = self.derivative(np.stack((eta,zeta), axis=1))
        ex, zx = dx[:,0], dx[:,1]
        B = zeta*zeta+f['beta']
        Lx = q*(2*zeta*zx-B*ex)
        reaction = zeta*zeta*q*q+f['beta']*np.expm1(-2*eta)
        scale = f['radial_scale']
        velocity = np.stack((scale*(q*zx*f['inverse_b']+f['c']*reaction)+f['advection']*ex,
                             scale*(Lx*f['inverse_b']-f['c']*(1+f['beta'])*zeta)+f['advection']*zx), axis=1)
        answer = self.encode(velocity)
        self.calls += 1
        if not np.all(np.isfinite(answer)):
            raise FloatingPointError('Nonfinite physical-design Codazzi velocity')
        return answer[:,0] if f['single'] else answer

    def jvp(self, x, state, direction):
        state,direction=np.asarray(state),np.asarray(direction)
        if state.ndim!=1:raise ValueError('JVP accepts one radial state')
        single=direction.ndim==1
        if single:direction=direction[:,None]
        f=self.fields(x,state)
        eta,zeta,q=f['eta'],f['zeta'],f['inverse_exponential']
        dx=self.derivative(np.stack((eta,zeta),axis=1));ex,zx=dx[:,0],dx[:,1]
        delta=self.decode(direction);de,dz=delta[:,0],delta[:,1]
        delta_dx=self.derivative(delta);dex,dzx=delta_dx[:,0],delta_dx[:,1]
        B=zeta*zeta+f['beta'];dQ=2*zeta*dz-B*de
        dQx=2*zx*dz+2*zeta*dzx-2*zeta*zx*de-B*dex
        dLx=q*(dQx-ex*dQ);scale=f['radial_scale']
        velocity=np.stack((scale*(q*(dzx-de*zx)*f['inverse_b']+2*f['c']*q*q*(zeta*dz-B*de))+f['advection']*dex,
                           scale*(dLx*f['inverse_b']-f['c']*(1+f['beta'])*dz)+f['advection']*dzx),axis=1)
        answer=self.encode(velocity);self.jvp_calls+=1
        if not np.all(np.isfinite(answer)):raise FloatingPointError('Nonfinite design state JVP')
        return answer[:,0] if single else answer

    def parameter_derivative(self,x,state):
        f=self.fields(x,state)
        eta,zeta,q=f['eta'],f['zeta'],f['inverse_exponential']
        dx=self.derivative(np.stack((eta,zeta),axis=1));ex,zx=dx[:,0],dx[:,1]
        B=zeta*zeta+f['beta'];Lx=q*(2*zeta*zx-B*ex)
        expm=np.expm1(-2*eta);reaction=zeta*zeta*q*q+f['beta']*expm
        scale=f['radial_scale'];scale_T=f['radial_scale_T']
        common=scale_T-scale*f['a_T_over_a']
        eta_T=common*q*zx*f['inverse_b']+(scale_T*f['c']+scale*f['c_T'])*reaction+scale*f['c']*f['beta_T']*expm
        zeta_T=(common*Lx-scale*q*f['beta_T']*ex)*f['inverse_b']-(
            (scale_T*f['c']+scale*f['c_T'])*(1+f['beta'])+scale*f['c']*f['beta_T'])*zeta
        answer=self.encode(np.stack((eta_T,zeta_T),axis=1))
        return answer[:,0] if f['single'] else answer

    def physical_values_and_derivatives(self,x,state,first):
        f=self.fields(x,state);native=self.decode(first)
        if native.ndim==2:native=native[:,:,None]
        log_ref_x=f['radial_scale']*f['dlog_n_reference']
        n_x=f['n']*(native[:,0]+log_ref_x)
        m_x=f['n_reference']*(native[:,1]+log_ref_x*f['zeta'])
        angular=self.derivative(np.stack((f['eta'],f['zeta']),axis=1))
        n_xi=f['n']*angular[:,0];m_xi=f['n_reference']*angular[:,1]
        l_xi=f['n_reference']*f['inverse_exponential']*(
            2*f['zeta']*angular[:,1]-(f['zeta']**2+f['beta'])*angular[:,0])
        physical_fixed_xi=np.stack((n_x,m_x),axis=1)/f['radial_scale']
        material=np.stack((n_x-f['advection']*n_xi,m_x-f['advection']*m_xi),axis=1)/f['radial_scale']
        return dict(fields=f,values=np.stack((f['n'],f['m']),axis=1),first_x=np.stack((n_x,m_x),axis=1),
                    first_physical_fixed_xi=physical_fixed_xi,first_material=material,
                    angular=np.stack((n_xi,m_xi,l_xi),axis=1))
