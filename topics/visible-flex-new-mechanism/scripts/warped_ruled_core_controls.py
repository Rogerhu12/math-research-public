#!/usr/bin/env python3
"""Closed multi-mode psi-warp cores with material-coordinate control Jacobians.

psi(phi)=phi+sum_j c_j*sin(3*j*phi), chi=3*phi.  Only c_2 enters
the exact vertical closure equation.  All coefficient derivatives below
include that closure root, the C3 center anchor, spherical total length q,
and the inverse material-angle map.  Changing q changes the metric and is
design work unless a separate fixed-q constraint is imposed.

This is a numerical interface to an exact integral-defined family, not an
interval geometry certificate.  Research optimizations belong in the
public repository Actions.  The CLI only runs small artificial checks.
"""
from __future__ import annotations

import argparse
from math import comb
import hashlib
import json
from pathlib import Path

import numpy as np


def parameter_text(value):
    return value if isinstance(value,str) else format(float(value),'.17g')


def closure_root(c2):
    a=.5-1.5*c2
    root=np.sqrt(9-4*a+4*a*a)
    eta=-2*a/(3+root)
    sigma=np.sqrt(1-eta*eta)
    eta_c2=1.5*sigma*sigma/root
    sigma_c2=-eta*eta_c2/sigma
    return eta,sigma,eta_c2,sigma_c2


class WarpedRuledCoreControls:
    """All controls are c1,...,cM; callers may hold any subset fixed.

    inlet(theta,s,k) has shape (3,*broadcast(theta,s).shape,3): radial
    derivative 0/1/2 first, Cartesian coordinate last.  k is the angular
    derivative 0/1/2.  inlet_control_jacobian adds a leading control axis,
    so it has shape (M,3,*broadcast(theta,s).shape,3).  Every control
    derivative is at fixed material theta and fixed s.
    """
    def __init__(self,coefficients,scale=1.,arc_cells=192,quadrature=16):
        self.coefficient_text=[parameter_text(x) for x in coefficients]
        self.coefficients=np.array([float(x) for x in self.coefficient_text])
        self.scale_text=parameter_text(scale);self.scale=float(scale)
        self.modes=len(self.coefficients)
        if self.modes<1 or not np.all(np.isfinite(self.coefficients)) or not np.isfinite(self.scale) or self.scale<=0:
            raise ValueError('need at least one finite coefficient and a positive finite scale')
        if arc_cells<max(12,6*self.modes) or arc_cells%6 or quadrature<4:
            raise ValueError('arc_cells must be a multiple of six, at least max(12,6M); quadrature >= 4')
        c2=self.coefficients[1] if self.modes>=2 else 0.
        self.eta,self.sigma,eta_c2,sigma_c2=closure_root(c2)
        if not np.isfinite(self.sigma) or self.sigma<=0:
            raise ValueError('the closure branch must satisfy |eta|<1')
        self.eta_controls=np.zeros(self.modes);self.sigma_controls=np.zeros(self.modes)
        if self.modes>=2:
            self.eta_controls[1]=eta_c2;self.sigma_controls[1]=sigma_c2
        j=np.arange(1,self.modes+1)
        end_p=1+np.array([np.sum(3*j*self.coefficients),np.sum(3*j*(-1.)**j*self.coefficients)])
        self.regularity_endpoint_factors=3+self.eta*end_p
        if np.min(abs(self.regularity_endpoint_factors))<1e-12:
            raise ValueError('a characteristic endpoint is singular or numerically unresolved')
        self.control_names=[f'c{j}' for j in range(1,self.modes+1)]
        self.arc_cells,self.quadrature=int(arc_cells),int(quadrature)
        self.gl,self.gw=np.polynomial.legendre.leggauss(quadrature)
        self.step=2*np.pi/arc_cells
        self._prepare_vertical()
        left=np.arange(arc_cells)*self.step
        grid=left[:,None]+self.step*(self.gl[None,:]+1)/2
        d,dj=self._direction_data(grid,True)
        c,cj=self._center_derivative_data(d,dj)
        inc=self.step/2*np.einsum('ijk,j->ik',c[0],self.gw)
        incj=self.step/2*np.einsum('mijk,j->mik',cj[0],self.gw)
        self.position_prefix=np.concatenate((np.zeros((1,3)),np.cumsum(inc,axis=0)))
        self.position_control_prefix=np.concatenate((np.zeros((self.modes,1,3)),np.cumsum(incj,axis=1)),axis=1)
        sector=self.position_prefix[arc_cells//3]
        sectorj=self.position_control_prefix[:,arc_cells//3]
        self.anchor=-sector[0]/2+np.sqrt(3)*sector[1]/6
        self.anchor_controls=-sectorj[:,0]/2+np.sqrt(3)*sectorj[:,1]/6
        complex_anchor=(sector[0]+1j*sector[1])/(np.exp(2j*np.pi/3)-1)
        self.anchor_imaginary_error=float(abs(complex_anchor.imag))
        self.center_derivative_closure=self.position_prefix[-1].copy()
        self.center_control_derivative_closure=self.position_control_prefix[:,-1].copy()
        speed=np.linalg.norm(d[1],axis=-1)
        speedj=np.sum(d[1][None,...]*dj[1],axis=-1)/speed[None,...]
        sinc=self.step/2*(speed@self.gw)
        sincj=self.step/2*(speedj@self.gw)
        self.arc_prefix=np.r_[0.,np.cumsum(sinc)]
        self.arc_control_prefix=np.concatenate((np.zeros((self.modes,1)),np.cumsum(sincj,axis=1)),axis=1)
        self.sphere_length=float(self.arc_prefix[-1]);self.q=self.sphere_length/(2*np.pi)
        self.sphere_length_controls=self.arc_control_prefix[:,-1].copy()
        self.q_controls=self.sphere_length_controls/(2*np.pi)

    def _prepare_vertical(self):
        # c_z'/b = 3eta + A*p - B*p*cos(6phi).  Its constant
        # coefficient is zero by closure; the remaining cosine coefficients
        # have frequencies 3,...,3(M+2), and integrate to sine modes.
        n=max(2,self.modes+2);coef=np.zeros(n);jac=np.zeros((self.modes,n))
        A=(1+self.eta*self.eta)/2;B=(1-self.eta*self.eta)/2
        Aj=self.eta*self.eta_controls;Bj=-Aj
        coef[1]-=B;jac[:,1]-=Bj
        for index,value in enumerate(self.coefficients):
            j=index+1;k=3*j
            unit=np.zeros(self.modes);unit[index]=1
            coef[index]+=A*k*value
            jac[:,index]+=k*(Aj*value+A*unit)
            coefficient=-B*k*value/2
            derivative=-k*(Bj*value+B*unit)/2
            coef[j+1]+=coefficient;jac[:,j+1]+=derivative
            if j!=2:
                target=abs(j-2)-1
                coef[target]+=coefficient;jac[:,target]+=derivative
        frequencies=3*np.arange(1,n+1)
        self.vertical_coefficients=coef/frequencies
        self.vertical_coefficient_controls=jac/frequencies[None,:]
        self.vertical_frequencies=frequencies
        c2=self.coefficients[1] if self.modes>=2 else 0.
        self.vertical_mean_residual=3*self.eta+A-3*B*c2

    def _direction_data(self,phi,controls=False):
        phi=np.asarray(phi,float);shape=(self.modes,)+(1,)*phi.ndim
        freq=(3*np.arange(1,self.modes+1)).reshape(shape)
        coefficient=self.coefficients.reshape(shape)
        basis=[freq**k*np.sin(freq*phi[None,...]+k*np.pi/2) for k in range(4)]
        psi=phi+np.sum(coefficient*basis[0],axis=0)
        p=1+np.sum(coefficient*basis[1],axis=0)
        p1=np.sum(coefficient*basis[2],axis=0)
        p2=np.sum(coefficient*basis[3],axis=0)
        exponential=np.exp(1j*psi)
        B=[np.ones_like(psi,dtype=complex),1j*p,1j*p1-p*p,1j*p2-3*p*p1-1j*p**3]
        E=[exponential*x for x in B]
        chi=3*phi
        f=[3**k*(-np.sin(chi+k*np.pi/2)+1j*self.eta*np.cos(chi+k*np.pi/2)) for k in range(4)]
        horizontal=[sum(comb(k,r)*E[r]*f[k-r] for r in range(k+1)) for k in range(4)]
        values=[np.stack((horizontal[k].real,horizontal[k].imag,
                          -self.sigma*3**k*np.cos(chi+k*np.pi/2)),axis=-1) for k in range(4)]
        if not controls:
            return values,None
        p_j,p1_j,p2_j=basis[1:]
        Bj=[np.zeros_like(basis[0],dtype=complex),1j*p_j,
            1j*p1_j-2*p[None,...]*p_j,
            1j*p2_j-3*(p_j*p1[None,...]+p[None,...]*p1_j)-3j*p[None,...]**2*p_j]
        Ej=[exponential[None,...]*(Bj[k]+1j*basis[0]*B[k][None,...]) for k in range(4)]
        eta_j=self.eta_controls.reshape(shape);sigma_j=self.sigma_controls.reshape(shape)
        fj=[1j*eta_j*3**k*np.cos(chi[None,...]+k*np.pi/2) for k in range(4)]
        hj=[sum(comb(k,r)*(Ej[r]*f[k-r][None,...]+E[r][None,...]*fj[k-r])
                for r in range(k+1)) for k in range(4)]
        partials=[np.stack((hj[k].real,hj[k].imag,
                    -sigma_j*3**k*np.cos(chi[None,...]+k*np.pi/2)),axis=-1) for k in range(4)]
        return values,partials

    def direction_jets(self,phi):
        return self._direction_data(phi,False)[0]

    def direction_control_jets(self,phi):
        """Partial derivatives at fixed construction phi; one array per phi order."""
        return self._direction_data(phi,True)[1]

    def _center_derivative_data(self,d,dj=None):
        d0,d1,d2,d3=d;b=self.scale
        c=[b*np.cross(d0,d1),b*np.cross(d0,d2),b*(np.cross(d1,d2)+np.cross(d0,d3))]
        if dj is None:
            return c,None
        def cross_j(i,j):
            return np.cross(dj[i],d[j][None,...])+np.cross(d[i][None,...],dj[j])
        return c,[b*cross_j(0,1),b*cross_j(0,2),b*(cross_j(1,2)+cross_j(0,3))]

    def center_derivatives(self,phi):
        return self._center_derivative_data(self.direction_jets(phi))[0]

    def vertical(self,phi,derivative=0):
        phi=np.asarray(phi,float)
        basis=np.sin(phi[...,None]*self.vertical_frequencies+derivative*np.pi/2)*self.vertical_frequencies**derivative
        return self.scale*(basis@self.vertical_coefficients)

    def vertical_control_jacobian(self,phi,derivative=0):
        phi=np.asarray(phi,float)
        basis=np.sin(phi[...,None]*self.vertical_frequencies+derivative*np.pi/2)*self.vertical_frequencies**derivative
        return self.scale*np.einsum('...n,mn->m...',basis,self.vertical_coefficient_controls)

    def _cell_data(self,phi):
        phi=np.asarray(phi,float);turns=np.floor(phi/(2*np.pi));rem=phi-turns*2*np.pi
        index=np.minimum(np.floor(rem/self.step).astype(int),self.arc_cells-1)
        left=index*self.step;length=rem-left
        grid=left[...,None]+length[...,None]*(self.gl+1)/2
        return turns,index,length,grid

    def center(self,phi):
        _,index,length,grid=self._cell_data(phi)
        integral=np.einsum('...jk,j->...k',self.center_derivatives(grid)[0],self.gw)
        value=self.position_prefix[index]+length[...,None]*integral/2
        value=value+np.array([self.anchor,0.,0.]);value[...,2]=self.vertical(phi)
        return value

    def center_control_partials(self,phi):
        """Position control partials at fixed construction phi, including anchor."""
        _,index,length,grid=self._cell_data(phi)
        d,dj=self._direction_data(grid,True);_,cj=self._center_derivative_data(d,dj)
        integral=np.einsum('m...jk,j->m...k',cj[0],self.gw)
        value=self.position_control_prefix[:,index]+length[None,...,None]*integral/2
        anchor=np.zeros((self.modes,)+(1,)*np.ndim(phi)+(3,));anchor[...,0]=self.anchor_controls.reshape((self.modes,)+(1,)*np.ndim(phi))
        value=value+anchor;value[...,2]=self.vertical_control_jacobian(phi)
        return value

    def center_jets(self,phi):
        return [self.center(phi),*self.center_derivatives(phi)]

    def center_control_jets(self,phi):
        d,dj=self._direction_data(phi,True)
        return [self.center_control_partials(phi),*self._center_derivative_data(d,dj)[1]]

    def arclength(self,phi):
        turns,index,length,grid=self._cell_data(phi)
        speed=np.linalg.norm(self.direction_jets(grid)[1],axis=-1)
        return turns*self.sphere_length+self.arc_prefix[index]+length*(speed@self.gw)/2

    def arclength_control_partials(self,phi):
        turns,index,length,grid=self._cell_data(phi)
        d,dj=self._direction_data(grid,True);speed=np.linalg.norm(d[1],axis=-1)
        speedj=np.sum(d[1][None,...]*dj[1],axis=-1)/speed[None,...]
        shape=(self.modes,)+(1,)*np.ndim(phi)
        return (turns[None,...]*self.sphere_length_controls.reshape(shape)+
                self.arc_control_prefix[:,index]+length[None,...]*(speedj@self.gw)/2)

    def phase(self,theta):
        theta=np.asarray(theta,float);turns=np.floor(theta/(2*np.pi));reduced=theta-turns*2*np.pi
        target=self.q*reduced;lo=np.zeros_like(target);hi=np.full_like(target,2*np.pi);phi=reduced.copy()
        for _ in range(50):
            d=self.direction_jets(phi);speed=np.linalg.norm(d[1],axis=-1)
            residual=self.arclength(phi)-target;active=abs(residual)>=3e-14
            if not np.any(active):
                break
            lo=np.where(residual<0,phi,lo);hi=np.where(residual>=0,phi,hi)
            newton=phi-residual/speed
            update=np.where((newton>lo)&(newton<hi),newton,(lo+hi)/2)
            phi=np.where(active,update,phi)
        error=float(np.max(abs(self.arclength(phi)-target)))
        if error>3e-11:
            raise RuntimeError('material-angle inverse did not converge')
        d=self.direction_jets(phi);speed=np.linalg.norm(d[1],axis=-1)
        speed_phi=np.sum(d[1]*d[2],axis=-1)/speed
        return phi+turns*2*np.pi,self.q/speed,-self.q**2*speed_phi/speed**3,error

    def phase_control_jacobian(self,theta,phase=None):
        theta=np.asarray(theta,float)
        phi,phi_theta,phi_thetatheta,_=self.phase(theta) if phase is None else phase
        d,dj=self._direction_data(phi,True)
        k=np.linalg.norm(d[1],axis=-1);kp=np.sum(d[1]*d[2],axis=-1)/k
        kpp=(np.sum(d[2]*d[2]+d[1]*d[3],axis=-1)/k-
             np.sum(d[1]*d[2],axis=-1)**2/k**3)
        kj=np.sum(d[1][None,...]*dj[1],axis=-1)/k[None,...]
        kpj=(np.sum(dj[1]*d[2][None,...]+d[1][None,...]*dj[2],axis=-1)/k[None,...]-
             kp[None,...]*kj/k[None,...])
        qj=self.q_controls.reshape((self.modes,)+(1,)*theta.ndim)
        phij=(qj*theta[None,...]-self.arclength_control_partials(phi))/k[None,...]
        total_kj=kj+kp[None,...]*phij
        total_kpj=kpj+kpp[None,...]*phij
        p_j=qj/k[None,...]-self.q*total_kj/k[None,...]**2
        pp_j=(-2*self.q*qj*kp[None,...]/k[None,...]**3-
              self.q**2*total_kpj/k[None,...]**3+
              3*self.q**2*kp[None,...]*total_kj/k[None,...]**4)
        return phij,p_j,pp_j

    def _material_jets(self,theta):
        phase=self.phase(theta);phi,p,pp,_=phase
        cc=self.center_jets(phi);dd=self.direction_jets(phi)
        c=[cc[0],cc[1]*p[...,None],cc[2]*p[...,None]**2+cc[1]*pp[...,None]]
        d=[dd[0],dd[1]*p[...,None],dd[2]*p[...,None]**2+dd[1]*pp[...,None]]
        return phase,cc,dd,c,d

    def inlet(self,theta,s,derivative=0):
        if derivative not in (0,1,2):
            raise ValueError('angular derivative is 0, 1, or 2')
        theta,s=np.broadcast_arrays(np.asarray(theta,float),np.asarray(s,float))
        _,_,_,c,d=self._material_jets(theta)
        return np.stack((c[derivative]+s[...,None]*d[derivative],d[derivative],np.zeros_like(d[derivative])))

    def inlet_control_jacobian(self,theta,s,derivative=0):
        if derivative not in (0,1,2):
            raise ValueError('angular derivative is 0, 1, or 2')
        theta,s=np.broadcast_arrays(np.asarray(theta,float),np.asarray(s,float))
        phase,cc,dd,_,_=self._material_jets(theta);phi,p,pp,_=phase
        phij,pj,ppj=self.phase_control_jacobian(theta,phase)
        ccj=self.center_control_jets(phi);ddj=self.direction_control_jets(phi)
        def compose(f,fj):
            total=[fj[k]+f[k+1][None,...]*phij[...,None] for k in range(3)]
            return [total[0],total[1]*p[None,...,None]+f[1][None,...]*pj[...,None],
                    total[2]*p[None,...,None]**2+2*f[2][None,...]*p[None,...,None]*pj[...,None]+
                    total[1]*pp[None,...,None]+f[1][None,...]*ppj[...,None]]
        cj=compose(cc,ccj);dj=compose(dd,ddj)
        return np.stack((cj[derivative]+s[None,...,None]*dj[derivative],dj[derivative],np.zeros_like(dj[derivative])),axis=1)

    def inlet_scale_jacobian(self,theta,s,derivative=0):
        theta,s=np.broadcast_arrays(np.asarray(theta,float),np.asarray(s,float))
        _,_,_,c,d=self._material_jets(theta)
        return np.stack((c[derivative]/self.scale,np.zeros_like(d[derivative]),np.zeros_like(d[derivative])))

    def metric(self,s):
        s=np.asarray(s,float);r=np.sqrt(self.scale**2+s*s)
        return self.q*r,self.q*s/r,self.q*self.scale**2/r**3

    def metric_control_jacobian(self,s):
        """Returns (M,3,*s.shape) for derivatives of (a,a_s,a_ss)."""
        s=np.asarray(s,float);r=np.sqrt(self.scale**2+s*s)
        base=np.stack((r,s/r,self.scale**2/r**3))
        return self.q_controls.reshape((self.modes,)+(1,)*base.ndim)*base[None,...]

    def metric_scale_jacobian(self,s):
        s=np.asarray(s,float);b=self.scale;r=np.sqrt(b*b+s*s)
        return self.q*np.stack((b/r,-b*s/r**3,2*b/r**3-3*b**3/r**5))

    def identity(self):
        return {'schema':'warped-ruled-core-controls-v1','coefficients':self.coefficient_text,
            'coefficient_order':self.control_names,'scale':self.scale_text,
            'construction_phase':'psi=phi+sum(c_j*sin(3*j*phi)); chi=3*phi',
            'closure_root':'a=1/2-3*c2/2; eta=-2*a/(3+sqrt(9-4*a+4*a*a))',
            'normalization':'C3 center anchor on x axis; center_z(0)=0; no fitted ambient rotation',
            'ambient_rotation':np.eye(3).tolist(),'q_definition':'integral_0^(2*pi)|d_phi|dphi/(2*pi)',
            'q_numeric':self.q,'q_control_jacobian_numeric':self.q_controls.tolist(),
            'metric':'ds^2+q^2*(scale^2+s^2)*dtheta^2','curvature':'-scale^2/(scale^2+s^2)^2',
            'coefficient_changes_are_design_unless_q_is_fixed':True,
            'all_control_jacobians_hold_material_theta_fixed':True,
            'arclength_numeric_quadrature_certified':False,'arc_cells':self.arc_cells,'quadrature':self.quadrature,
            'closed_surface_constructed':False,'task_complete':False}


def check_only():
    # One artificial four-mode input, not a geometry search or candidate fit.
    coefficients=np.array([.11,.017,-.006,.0025]);b=.9
    core=WarpedRuledCoreControls(coefficients,b,48,12)
    phi=(np.arange(13)+.27)*2*np.pi/13;theta=(np.arange(9)+.31)*2*np.pi/9;s=.013
    dd=core.direction_jets(phi);eps=2e-5
    raw_errors=[]
    for order in range(3):
        fd=(core.direction_jets(phi-2*eps)[order]-8*core.direction_jets(phi-eps)[order]+
            8*core.direction_jets(phi+eps)[order]-core.direction_jets(phi+2*eps)[order])/(12*eps)
        raw_errors.append(float(np.linalg.norm(fd-dd[order+1])/np.linalg.norm(dd[order+1])))
    vertical_error=float(np.max(abs(core.vertical(phi,1)-core.center_derivatives(phi)[0][...,2])))
    jets=[core.inlet(theta,s,k) for k in range(3)];aa=core.metric(s)[0]
    metric_error=max(float(np.max(abs(np.sum(jets[0][1]**2,axis=-1)-1))),
        float(np.max(abs(np.sum(jets[0][1]*jets[1][0],axis=-1)/aa))),
        float(np.max(abs(np.sum(jets[1][0]**2,axis=-1)/aa**2-1))))
    A=np.array([1.,-1.,-1.]);symmetry=0.
    for r in range(3):
        for t in range(3-r):
            symmetry=max(symmetry,float(np.max(abs(core.inlet(-theta,-s,t)[r]-(-1)**(r+t)*core.inlet(theta,s,t)[r]*A))))
    from warped_ruled_core import WarpedRuledCore
    legacy=WarpedRuledCore(.13,.02,1.,48,12);two=WarpedRuledCoreControls([.13,.02],1.,48,12)
    legacy_error=max(float(np.max(abs(legacy.inlet(theta,s,k)-two.inlet(theta,s,k)))) for k in range(3))
    jac=[core.inlet_control_jacobian(theta,s,k) for k in range(3)]
    q_errors=[];port_errors=[[],[],[]];metric_jac_errors=[];phase_jac_errors=[]
    h=2e-6;phase_jac=core.phase_control_jacobian(theta);metric_jac=core.metric_control_jacobian(np.array([-.03,0.,.02]))
    for j in range(core.modes):
        plus=coefficients.copy();minus=coefficients.copy();plus[j]+=h;minus[j]-=h
        cp=WarpedRuledCoreControls(plus,b,48,12);cm=WarpedRuledCoreControls(minus,b,48,12)
        q_fd=(cp.q-cm.q)/(2*h);q_errors.append(float(abs(q_fd-core.q_controls[j])))
        for k in range(3):
            fd=(cp.inlet(theta,s,k)-cm.inlet(theta,s,k))/(2*h)
            port_errors[k].append(float(np.linalg.norm(fd-jac[k][j])/max(1.,np.linalg.norm(fd))))
        fd=(np.array(cp.metric(np.array([-.03,0.,.02])))-np.array(cm.metric(np.array([-.03,0.,.02]))))/(2*h)
        metric_jac_errors.append(float(np.linalg.norm(fd-metric_jac[j])/max(1.,np.linalg.norm(fd))))
        for k in range(3):
            fd=(cp.phase(theta)[k]-cm.phase(theta)[k])/(2*h)
            phase_jac_errors.append(float(np.linalg.norm(fd-phase_jac[k][j])/max(1.,np.linalg.norm(fd))))
    cp=WarpedRuledCoreControls(coefficients,b+h,48,12);cm=WarpedRuledCoreControls(coefficients,b-h,48,12)
    scale_errors=[]
    for k in range(3):
        fd=(cp.inlet(theta,s,k)-cm.inlet(theta,s,k))/(2*h)
        scale_errors.append(float(np.linalg.norm(fd-core.inlet_scale_jacobian(theta,s,k))/max(1.,np.linalg.norm(fd))))
    metric_scale_fd=(np.array(cp.metric(np.array([-.03,0.,.02])))-np.array(cm.metric(np.array([-.03,0.,.02]))))/(2*h)
    metric_scale_error=float(np.max(abs(metric_scale_fd-core.metric_scale_jacobian(np.array([-.03,0.,.02])))))
    result={'schema':'warped-ruled-controls-development-check-v1','development_check_only':True,
        'research_optimization_or_scan_performed':False,'artificial_identity':core.identity(),
        'unit_direction_error':float(np.max(abs(np.sum(dd[0]**2,axis=-1)-1))),
        'direction_raw_derivative_relative_errors':raw_errors,'vertical_primitive_derivative_error':vertical_error,
        'vertical_mean_closure_float_residual':float(core.vertical_mean_residual),
        'center_derivative_integral_closure_norm':float(np.linalg.norm(core.center_derivative_closure)),
        'center_control_derivative_integral_closure_norm':float(np.max(np.linalg.norm(core.center_control_derivative_closure,axis=-1))),
        'metric_error':metric_error,'full_halfturn_two_jet_error':symmetry,'legacy_two_mode_port_error':legacy_error,
        'q_control_jacobian_absolute_errors':q_errors,'material_phase_jacobian_relative_errors':phase_jac_errors,
        'material_port_control_jacobian_relative_errors_by_angular_order':port_errors,
        'metric_control_jacobian_relative_errors':metric_jac_errors,
        'port_scale_jacobian_relative_errors':scale_errors,'metric_scale_jacobian_absolute_error':metric_scale_error,
        'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    result['passed']=bool(max(raw_errors)<1e-8 and vertical_error<1e-10 and metric_error<1e-10 and symmetry<1e-9 and
        legacy_error<1e-9 and max(q_errors)<1e-7 and max(phase_jac_errors)<1e-7 and max(map(max,port_errors))<1e-7 and
        max(metric_jac_errors)<1e-7 and max(scale_errors)<1e-7 and metric_scale_error<1e-7 and
        result['center_derivative_integral_closure_norm']<1e-10 and result['center_control_derivative_integral_closure_norm']<1e-9)
    return result


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check-only',action='store_true',required=True)
    parser.add_argument('--out',type=Path,required=True)
    args=parser.parse_args();report=check_only()
    args.out.parent.mkdir(parents=True,exist_ok=True)
    args.out.write_text(json.dumps(report,indent=2,allow_nan=False)+'\n')
    print(json.dumps({'passed':report['passed'],'out':str(args.out),
                     'max_port_control_error':max(map(max,report['material_port_control_jacobian_relative_errors_by_angular_order']))}),flush=True)
    if not report['passed']:
        raise SystemExit(1)


if __name__=='__main__':
    main()
