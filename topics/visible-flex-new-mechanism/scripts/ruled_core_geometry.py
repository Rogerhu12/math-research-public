#!/usr/bin/env python3
"""Exact static R44 ruled saddle core, in a 2*pi material-angle gauge.

This module evaluates the already proved public R44 formula.  Its inexpensive
CLI checks the port implementation, not the original existence proof, and does
not optimize a connector or claim a closed surface.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import numpy as np
from scipy.special import ellipe, ellipeinc


class RuledCore:
    """Z(s,theta)=c(chi(theta))+s*d(chi(theta)).

    rotation=pi/2 is the orientation of new-topic R6, with half-turn
    diag(1,-1,-1). rotation=0 agrees with core_to_tail_bvp's circular tail
    convention (r*sin(theta),-r*cos(theta),C); its half-turn is diag(-1,1,-1).
    """
    def __init__(self, scale=1., rotation=np.pi/2):
        if scale<=0:
            raise ValueError('Ruled scale must be positive')
        self.scale=float(scale)
        self.rotation=float(rotation)
        self.eta=-3+2*np.sqrt(2.)
        self.sigma=np.sqrt(1-self.eta*self.eta)
        self.parameter=-self.sigma*self.sigma/8
        self.q=2*np.sqrt(8.)*ellipe(self.parameter)/np.pi
        self.R=scale*self.sigma*(self.eta+6)/2
        self.P=scale*self.sigma*(self.eta+1)/28
        self.Q=scale*self.sigma*(1-self.eta)/20
        ca,sa=np.cos(rotation),np.sin(rotation)
        rot=np.array([[ca,-sa,0.],[sa,ca,0.],[0.,0.,1.]])
        self.halfturn=rot@np.diag([-1.,1.,-1.])@rot.T

    def phase(self,theta):
        """Return original angle chi, chi_theta, chi_thetatheta, inversion error."""
        theta=np.asarray(theta,dtype=float)
        chi=theta.copy()
        for _ in range(12):
            speed=np.sqrt(8+self.sigma**2*np.sin(3*chi)**2)
            step=(np.sqrt(8.)/3*ellipeinc(3*chi,self.parameter)-self.q*theta)/speed
            chi-=step
            if np.max(np.abs(step))<3e-15:
                break
        error=float(np.max(np.abs(np.sqrt(8.)/3*ellipeinc(3*chi,self.parameter)-self.q*theta)))
        if error>2e-12*max(1.,float(np.max(np.abs(theta)))):
            raise RuntimeError(f'Ruled material-angle inversion failed: {error}')
        speed=np.sqrt(8+self.sigma**2*np.sin(3*chi)**2)
        first=self.q/speed
        second=-3*self.q**2*self.sigma**2*np.sin(3*chi)*np.cos(3*chi)/speed**4
        return chi,first,second,error

    def original_jet(self,chi,derivative=0):
        """c,d and a chosen angular derivative, before material reparametrization."""
        chi=np.asarray(chi)
        rot=np.exp(1j*self.rotation)
        frequencies=np.array([1,7,-5])
        cw=-1j*rot*np.sum(np.array([self.R,self.P,self.Q])[:,None]*
                          (1j*frequencies[:,None])**derivative*
                          np.exp(1j*frequencies[:,None]*chi[None,:]),axis=0)
        frequencies=np.array([4,-2])
        dw=rot*np.sum(np.array([(self.eta+1)/2,(self.eta-1)/2])[:,None]*
                     (1j*frequencies[:,None])**derivative*
                     np.exp(1j*frequencies[:,None]*chi[None,:]),axis=0)
        cz=-self.scale*self.sigma**2/12*6**derivative*np.sin(6*chi+derivative*np.pi/2)
        dz=-self.sigma*3**derivative*np.cos(3*chi+derivative*np.pi/2)
        return np.column_stack((cw.real,cw.imag,cz)),np.column_stack((dw.real,dw.imag,dz))

    def curve_jets(self,theta):
        """c,d and their first two material-angle derivatives."""
        chi,first,second,error=self.phase(theta)
        c0,d0=self.original_jet(chi)
        c1,d1=self.original_jet(chi,1)
        c2,d2=self.original_jet(chi,2)
        c=[c0,c1*first[:,None],c2*first[:,None]**2+c1*second[:,None]]
        d=[d0,d1*first[:,None],d2*first[:,None]**2+d1*second[:,None]]
        return c,d,error

    def metric(self,s):
        """a(s), da/ds and d²a/ds² in the fixed 2*pi gauge."""
        s=np.asarray(s)
        root=np.sqrt(self.scale**2+s*s)
        return self.q*root,self.q*s/root,self.q*self.scale**2/root**3

    def inlet(self,theta,s,derivative=0):
        """Full radial 0/1/2 jet at s, with angular derivative 0/1/2.

        The returned array has shape (3, number_of_angles, 3), matching the
        boundary data arrays consumed by core_to_tail_bvp. No division by any
        coefficient of the second fundamental form occurs.
        """
        if derivative not in (0,1,2):
            raise ValueError('Need angular derivative 0, 1 or 2')
        c,d,_=self.curve_jets(np.asarray(theta))
        return np.stack((c[derivative]+s*d[derivative],d[derivative],np.zeros_like(d[derivative])))

    def identity(self,s):
        aa=self.metric(s)
        return {'profile':'public_R44_static_ruled_saddle','scale':self.scale,
                'cut_s':float(s),'rotation_radians':self.rotation,
                'spherical_length_over_2pi':float(self.q),
                'metric_two_jet':list(map(float,aa)),
                'halfturn_matrix':self.halfturn.tolist(),
                'within_R44_proved_embedded_strip':bool(abs(s)<=self.scale/20+1e-15),
                'unit_revolution_reference_inlet_slope_admissible':bool(abs(aa[1])<1),
                'closed_surface':False,'round_collar_constructed':False,
                'finite_amplitude_ratio_certified':False,'whole_surface_reach_certified':False}


def check(core,cut_s):
    """Fixed small geometry audit; no parameter search or nonlinear solve."""
    theta=np.arange(192)*2*np.pi/192
    sgrid=np.array([-cut_s,0.,cut_s])
    metric_errors=[]
    second_errors=[]
    shape_ranges=[]
    for ss in sgrid:
        j0,j1,j2=[core.inlet(theta,ss,d) for d in range(3)]
        aa=core.metric(ss)[0]
        E=np.sum(j0[1]**2,axis=-1)
        F=np.sum(j0[1]*j1[0],axis=-1)
        G=np.sum(j1[0]**2,axis=-1)
        metric_errors.append({'s':float(ss),'E':float(np.max(np.abs(E-1))),
                              'F_over_a':float(np.max(np.abs(F/aa))),
                              'G_over_a2':float(np.max(np.abs(G/aa**2-1)))})
        normal=np.cross(j0[1],j1[0])/aa
        M=np.sum(normal*j1[1],axis=-1)
        N=np.sum(normal*j2[0],axis=-1)
        chi,_,_,_=core.phase(theta)
        xx=core.sigma**2*np.sin(3*chi)**2
        kappa=-core.sigma*np.cos(3*chi)*(17+3*core.eta+xx)/(8+xx)**1.5
        root=np.sqrt(core.scale**2+ss*ss)
        expected_M=-core.q*core.scale/root
        expected_N=core.q**2*kappa*root
        gauss=-M*M/(aa*aa)
        second_errors.append({'s':float(ss),
            'M_error':float(np.max(np.abs(M-expected_M))),
            'N_error':float(np.max(np.abs(N-expected_N))),
            'K_error':float(np.max(np.abs(gauss+core.scale**2/root**4)))})
        trace=N/(aa*aa)
        maxcurv=(np.abs(trace)+np.sqrt(trace*trace+4*M*M/(aa*aa)))/2
        shape_ranges.append({'s':float(ss),'M_range':[float(M.min()),float(M.max())],
                             'N_range':[float(N.min()),float(N.max())],
                             'sample_max_abs_principal_curvature':float(maxcurv.max()),
                             'coordinate_min':j0[0].min(axis=0).tolist(),
                             'coordinate_max':j0[0].max(axis=0).tolist()})
    halfturn=[]
    for rd in range(3):
        for td in range(3-rd):
            direct=core.inlet(theta,0.,td)[rd]
            opposite=core.inlet(-theta,0.,td)[rd]
            predicted=(-1)**(rd+td)*opposite@core.halfturn.T
            halfturn.append({'radial_derivative':rd,'angular_derivative':td,
                             'error':float(np.max(np.abs(direct-predicted)))})
    h=3e-5
    derivative_errors=[]
    for rd in (0,1):
        for td in (0,1):
            fd=(core.inlet(theta-2*h,cut_s,td)[rd]-8*core.inlet(theta-h,cut_s,td)[rd]+
                8*core.inlet(theta+h,cut_s,td)[rd]-core.inlet(theta+2*h,cut_s,td)[rd])/(12*h)
            exact=core.inlet(theta,cut_s,td+1)[rd]
            derivative_errors.append({'radial_derivative':rd,'angular_derivative':td+1,
                'absolute_error':float(np.max(np.abs(fd-exact))),
                'relative_l2_error':float(np.linalg.norm(fd-exact)/max(np.linalg.norm(exact),1e-30))})
    periodic=[]
    for td in range(3):
        periodic.append(float(np.max(np.abs(core.inlet(theta+2*np.pi,cut_s,td)-core.inlet(theta,cut_s,td)))))
    c,d,error=core.curve_jets(theta)
    closure=float(np.max(np.abs(c[1]-core.scale*np.cross(d[0],d[1]))))
    passed=(max(x[key] for x in metric_errors for key in ('E','F_over_a','G_over_a2'))<1e-12 and
            max(x['error'] for x in halfturn)<1e-12 and max(periodic)<1e-10 and
            max(x['relative_l2_error'] for x in derivative_errors)<1e-8 and
            max(x[key] for x in second_errors for key in ('M_error','N_error','K_error'))<1e-10)
    return {'identity':core.identity(cut_s),'metric_errors':metric_errors,
            'second_fundamental_form_errors':second_errors,'shape_ranges':shape_ranges,
            'R6_complete_central_second_jet_halfturn_errors':halfturn,
            'angular_derivative_checks':derivative_errors,
            'angular_periodicity_errors_by_derivative':periodic,
            'center_derivative_equals_b_cross_d_dtheta_error':closure,
            'material_angle_inversion_error':error,'development_checks_passed':bool(passed)}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--scale',type=float,default=.24)
    parser.add_argument('--cut-fraction',type=float,default=.05)
    parser.add_argument('--rotation-deg',type=float,default=90.)
    parser.add_argument('--out',type=Path,required=True)
    args=parser.parse_args()
    if args.scale<=0 or args.cut_fraction<0:
        parser.error('Need positive scale and nonnegative cut fraction')
    core=RuledCore(args.scale,np.deg2rad(args.rotation_deg))
    report={'status':'exact_R44_static_port_implementation_check_no_optimization',
            'task_complete':False,'source_result':'topics/visible-flexible-closed-surface/results/R44-explicit-flexible-ruled-saddle-annulus.md',
            'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            **check(core,args.cut_fraction*args.scale)}
    args.out.parent.mkdir(parents=True,exist_ok=True)
    args.out.write_text(json.dumps(report,indent=2,allow_nan=False)+'\n')
    print(json.dumps({'out':str(args.out),'passed':report['development_checks_passed'],
                      'identity':report['identity'],'metric_errors':report['metric_errors'],
                      'halfturn_max':max(x['error'] for x in report['R6_complete_central_second_jet_halfturn_errors'])}))
    if not report['development_checks_passed']:
        raise SystemExit(1)


if __name__=='__main__':
    main()
