#!/usr/bin/env python3
"""Numerical material-angle interface for an exact frozen cosine rectifying core.

The physical model uses exact rational coefficients and the exact arclength
integral. This module evaluates that model by fixed Gauss quadrature and a
monotone scalar solve; floating values are not interval certificates. Full
position two-jets use the exact R9 formulas. No higher mixed jets are invented.
"""
from __future__ import annotations

from fractions import Fraction as R
import hashlib
import json

import numpy as np
from numpy.polynomial.legendre import leggauss


def exact_rational(value):
    if isinstance(value, dict):
        if set(value) != {'numerator', 'denominator'}:
            raise ValueError('rational objects need numerator and denominator only')
        return R(int(value['numerator']), int(value['denominator']))
    if isinstance(value, str):
        return R(value)
    if isinstance(value, int) and not isinstance(value, bool):
        return R(value)
    raise TypeError('use exact rational objects or strings, not unlabelled float values')


def rational_json(value):
    value=R(value)
    return {'numerator':str(value.numerator),'denominator':str(value.denominator)}


def canonical_identity(identity):
    if identity.get('height_basis')!='cosine':
        raise ValueError('this interface accepts frozen cosine heights only')
    a=exact_rational(identity['a']);b=exact_rational(identity['b'])
    width=exact_rational(identity['half_width'])
    heights=[exact_rational(x) for x in identity['height_coefficients']]
    offset=exact_rational(identity['height_offset'])
    if width<=0 or not 1<=len(heights)<=32:
        raise ValueError('need positive half width and 1 through 32 height modes')
    # This sufficient radial bound covers the intended public star parameters.
    if 1-abs(a)-abs(b)<=0:
        raise ValueError('r>0 is not certified by the current radial bound')
    out={'height_basis':'cosine','a':str(a),'b':str(b),'half_width':str(width),
         'height_coefficients':[rational_json(x) for x in heights],
         'height_offset':rational_json(offset)}
    return out


def identity_hash(identity):
    canonical=canonical_identity(identity)
    return hashlib.sha256(json.dumps(canonical,sort_keys=True,separators=(',',':')).encode()).hexdigest()


class CosineRectifyingCore:
    def __init__(self,identity,arc_cells=512,quadrature=16,certificate=None):
        self.identity=canonical_identity(identity)
        self.identity_sha256=identity_hash(self.identity)
        self.a_exact=R(self.identity['a']);self.b_exact=R(self.identity['b'])
        self.width_exact=R(self.identity['half_width'])
        self.heights_exact=[exact_rational(x) for x in self.identity['height_coefficients']]
        self.offset_exact=exact_rational(self.identity['height_offset'])
        self.a=float(self.a_exact);self.b=float(self.b_exact);self.width=float(self.width_exact)
        self.heights=np.array([float(x) for x in self.heights_exact])
        self.offset=float(self.offset_exact);self.frequencies=3*np.arange(1,len(self.heights)+1)
        self.arc_cells=int(arc_cells);self.quadrature=int(quadrature)
        if self.arc_cells<8 or self.quadrature<4:
            raise ValueError('arclength quadrature needs at least 8 cells and order 4')
        self.gauss_x,self.gauss_w=leggauss(self.quadrature)
        self.step=2*np.pi/self.arc_cells
        mid=(np.arange(self.arc_cells)+.5)*self.step
        points=mid[:,None]+self.step*self.gauss_x[None,:]/2
        speeds=np.linalg.norm(self.raw_jets(points)[1],axis=-1)
        integrals=self.step/2*(speeds@self.gauss_w)
        self.arc_prefix=np.r_[0.,np.cumsum(integrals)]
        self.perimeter=float(self.arc_prefix[-1]);self.a0=self.perimeter/(2*np.pi)
        self.q0=float(self.frame(np.asarray(0.))['q'])
        self.certificate=certificate
        if certificate is not None and certificate.get('physical_identity_sha256')!=self.identity_sha256:
            raise ValueError('continuous certificate belongs to a different physical identity')
        self.global_J_certificate_available=bool(certificate is not None and
            certificate.get('whole_core_immersion_and_angular_closure_certified',False))
        if self.global_J_certificate_available:
            enclosure=certificate['a0_exact_enclosure']
            if not float(enclosure['lower'])<=self.a0<=float(enclosure['upper']):
                raise ValueError('numerical arclength is outside the supplied continuous enclosure')

    @classmethod
    def from_verified_report(cls,report,**kwargs):
        if report.get('schema')!='space-star-frozen-cosine-verification-v1':
            raise ValueError('need an independent frozen cosine verification report')
        identity=report['frozen_physical_identity']
        if identity_hash(identity)!=report['frozen_physical_identity_sha256']:
            raise ValueError('physical identity hash mismatch')
        certificate=report['continuous_certificate']
        if not certificate['whole_core_immersion_and_angular_closure_certified']:
            raise ValueError('whole-width J and curvature have not been certified')
        return cls(identity,certificate=certificate,**kwargs)

    def raw_jets(self,phi):
        """Physical Cartesian derivatives gamma^(0)..gamma^(4), at fixed phi."""
        phi=np.asarray(phi,float)
        c,s=np.cos(phi),np.sin(phi)
        c3,s3=np.cos(3*phi),np.sin(3*phi)
        c6,s6=np.cos(6*phi),np.sin(6*phi)
        r=[1+self.a*c3+self.b*c6,-3*self.a*s3-6*self.b*s6,
           -9*self.a*c3-36*self.b*c6,27*self.a*s3+216*self.b*s6,
           81*self.a*c3+1296*self.b*c6]
        radial=[r[0],r[1],r[2]-r[0],r[3]-3*r[1],r[4]-6*r[2]+r[0]]
        angular=[np.zeros_like(phi),r[0],2*r[1],3*r[2]-r[0],4*r[3]-4*r[1]]
        phase=phi[...,None]*self.frequencies
        cc,ss=np.cos(phase),np.sin(phase)
        cycle=[cc,-ss,-cc,ss]
        result=[]
        for order in range(5):
            z=np.sum(cycle[order%4]*(self.heights*self.frequencies**order),axis=-1)
            if order==0:z=z+self.offset
            result.append(np.stack((radial[order]*c-angular[order]*s,
                                    radial[order]*s+angular[order]*c,z),axis=-1))
        return result

    def frame(self,phi):
        x,v1,v2,v3,v4=self.raw_jets(phi)
        speed=np.linalg.norm(v1,axis=-1)
        C=np.cross(v1,v2);W=np.linalg.norm(C,axis=-1)
        if np.any(speed<=0) or np.any(W<=0):
            raise ValueError('the numerical point has zero speed or curvature; no regularization is used')
        T=v1/speed[...,None];B=C/W[...,None];N=np.cross(B,T)
        determinant=np.sum(C*v3,axis=-1)
        determinant_p=np.sum(v1*np.cross(v2,v4),axis=-1)
        vp=np.sum(v1*v2,axis=-1)/speed
        Wp=np.sum(C*np.cross(v1,v3),axis=-1)/W
        kappa=W/speed**3;tau=determinant/W**2;q=tau/kappa
        qphi=(determinant_p*speed**3/W**3+3*determinant*speed**2*vp/W**3
              -3*determinant*speed**3*Wp/W**4)
        return {'x':x,'speed':speed,'T':T,'N':N,'B':B,'kappa':kappa,
                'tau':tau,'q':q,'q_phi':qphi,'q_ell':qphi/speed}

    def arc_length(self,phi):
        phi=np.asarray(phi,float)
        if np.any(phi<0) or np.any(phi>2*np.pi):
            raise ValueError('arclength primitive expects phi in [0,2*pi]')
        index=np.minimum((phi/self.step).astype(int),self.arc_cells-1)
        left=index*self.step;half=(phi-left)/2
        points=left[...,None]+half[...,None]*(1+self.gauss_x)
        speed=np.linalg.norm(self.raw_jets(points)[1],axis=-1)
        return self.arc_prefix[index]+half*np.sum(speed*self.gauss_w,axis=-1)

    def phase(self,s,theta):
        s,theta=np.broadcast_arrays(np.asarray(s,float),np.asarray(theta,float))
        if np.any(np.abs(s)>self.width):
            raise ValueError('do not extrapolate outside the frozen half width')
        start=s*self.q0
        target=start+np.mod(self.a0*theta-start,self.perimeter)
        lo=np.zeros_like(target);hi=np.full_like(target,2*np.pi)
        phi=(target-start)/self.perimeter*(2*np.pi)
        tolerance=5e-14*max(1.,self.perimeter)
        for _ in range(48):
            frame=self.frame(phi)
            residual=self.arc_length(phi)+s*frame['q']-target
            done=np.abs(residual)<=tolerance
            if np.all(done):break
            derivative=frame['speed']+s*frame['q_phi']
            if np.any(derivative<=0):
                raise ValueError('nonpositive sampled material-angle Jacobian')
            lo=np.where(residual<0,phi,lo);hi=np.where(residual>0,phi,hi)
            candidate=phi-residual/derivative
            candidate=np.where((candidate>lo)&(candidate<hi)&np.isfinite(candidate),
                               candidate,(lo+hi)/2)
            phi=np.where(done,phi,candidate)
        final=self.arc_length(phi)+s*self.frame(phi)['q']-target
        error=float(np.max(np.abs(final),initial=0.))
        if error>10*tolerance:
            raise RuntimeError('material-angle inversion did not reach its stated tolerance')
        return phi,error

    def evaluate(self,s,theta):
        s,theta=np.broadcast_arrays(np.asarray(s,float),np.asarray(theta,float))
        phi,residual=self.phase(s,theta);f=self.frame(phi)
        J=1+s*f['q_ell']
        if np.any(J<=0):
            raise ValueError('nonpositive sampled J; no two-jet is certified here')
        X=f['x']+s[...,None]*(f['B']+f['q'][...,None]*f['T'])
        N=f['N'];kappa=f['kappa'];tau=f['tau']
        return {'X':X,'Xs':f['B'],'Xtheta':self.a0*f['T'],
                'Xss':(tau*tau/(kappa*J))[...,None]*N,
                'Xst':(-self.a0*tau/J)[...,None]*N,
                'Xtt':(self.a0*self.a0*kappa/J)[...,None]*N,
                'normal':N,'phi':phi,'q_ell':f['q_ell'],'J':J,
                'kappa':kappa,'tau':tau,'a0_numerical':self.a0,
                'material_equation_residual_max':residual,
                'floating_evaluation_is_not_interval_certificate':True}

    def jet(self,s,theta,radial_order=0,angular_order=0):
        lookup={(0,0):'X',(1,0):'Xs',(0,1):'Xtheta',
                (2,0):'Xss',(1,1):'Xst',(0,2):'Xtt'}
        key=(radial_order,angular_order)
        if key not in lookup:
            raise ValueError('only complete position jets of total order at most two are provided')
        return self.evaluate(s,theta)[lookup[key]]

    def metric(self):
        return {'E':1.,'F':0.,'G_numerical':self.a0**2,
                'a0_exact_definition':'integral_0^(2*pi) |gamma_phi| dphi / (2*pi)',
                'arclength_quadrature_cells':self.arc_cells,
                'arclength_quadrature_order':self.quadrature,
                'a0_numerical':self.a0,'global_J_certificate_available':self.global_J_certificate_available}
