#!/usr/bin/env python3
"""Exact elliptic-cylinder ports for a twofold orthonormal-frame connector.

The physical model is gamma=(A cos(phi),B sin(phi),0), extruded vertically.
Material theta is defined by the exact arclength integral; scipy's elliptic
integral and a monotone solve evaluate it numerically, without refitting the
curve. Both outward sides have complete scalar and position two-jets.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as Q
import hashlib
import json
from pathlib import Path

import numpy as np
from scipy.special import ellipe,ellipeinc


def exact(value):
    return Q.from_float(float(value)) if isinstance(value,(float,np.floating)) else Q(value)


class EllipticCylinderPort:
    fold=2
    angular_derivative_mode='analytic'
    maximum_exact_prefix=float('inf')

    def __init__(self,major='1',minor='7/25',half_width='1/50',side=1):
        self.A_exact,self.B_exact,self.width_exact=map(exact,(major,minor,half_width))
        if not self.A_exact>=self.B_exact>0 or self.width_exact<0 or side not in [-1,1]:
            raise ValueError('need major >= minor > 0, nonnegative width and side +/-1')
        self.major=float(self.A_exact);self.minor=float(self.B_exact);self.width=float(self.width_exact)
        self.side=int(side);self.parameter=1-(self.minor/self.major)**2
        self.quarter_perimeter=self.major*float(ellipe(self.parameter))
        self.perimeter=4*self.quarter_perimeter;self.a0=self.perimeter/(2*np.pi)
        self.identity={'kind':'exact-elliptic-cylinder-v1','major':str(self.A_exact),
            'minor':str(self.B_exact),'half_width':str(self.width_exact),
            'material_angle_definition':'ell(phi)=a0*theta, a0=exact ellipse perimeter/(2*pi)',
            'position_definition':'(A*cos(phi),B*sin(phi),s)',
            'extrusion_is_exact_for_every_real_s':True}
        self.identity_sha256=hashlib.sha256(json.dumps(self.identity,sort_keys=True,separators=(',',':')).encode()).hexdigest()
        self.port_identity={'core_identity_sha256':self.identity_sha256,'side':self.side,
            'physical_s_definition':'side*(half_width+t)','fold':2}
        self.port_identity_sha256=hashlib.sha256(json.dumps(self.port_identity,sort_keys=True,separators=(',',':')).encode()).hexdigest()
        self.initial_center_z=self.side*self.width

    def arc_length(self,phi):
        phi=np.asarray(phi,float)
        return self.major*ellipeinc(phi-np.pi/2,self.parameter)+self.quarter_perimeter

    def phase(self,theta):
        theta=np.asarray(theta,float);local=np.mod(theta,2*np.pi)
        target=self.a0*local;lo=np.zeros_like(local);hi=np.full_like(local,2*np.pi)
        phi=local.copy();tolerance=2e-14*max(1.,self.perimeter)
        for _ in range(48):
            value=self.arc_length(phi)-target
            done=np.abs(value)<=tolerance
            if np.all(done):break
            lo=np.where(value<0,phi,lo);hi=np.where(value>0,phi,hi)
            speed=np.sqrt(self.major**2*np.sin(phi)**2+self.minor**2*np.cos(phi)**2)
            candidate=phi-value/speed
            candidate=np.where((candidate>lo)&(candidate<hi)&np.isfinite(candidate),candidate,(lo+hi)/2)
            phi=np.where(done,phi,candidate)
        error=float(np.max(abs(self.arc_length(phi)-target),initial=0.))
        if error>10*tolerance:raise RuntimeError('ellipse material-angle solve did not meet its stated tolerance')
        return phi,error

    def scalar_jets(self,t,theta):
        t,theta=np.broadcast_arrays(np.asarray(t,float),np.asarray(theta,float))
        phi,error=self.phase(theta);c,s=np.cos(phi),np.sin(phi)
        speed=np.sqrt(self.major**2*s*s+self.minor**2*c*c)
        psi=phi+np.arctan((self.major-self.minor)*s*c/(self.major*s*s+self.minor*c*c))
        psi_theta=self.a0*self.major*self.minor/speed**3
        psi_tt=-3*self.major*self.minor*self.a0**2*(self.major**2-self.minor**2)*s*c/speed**6
        zero=np.zeros_like(t)
        u={'value':psi-np.mod(theta,2*np.pi),'s':zero,'theta':psi_theta-1,'ss':zero,'st':zero,'tt':psi_tt,
           'ss_theta':zero}
        v={key:zero for key in ['value','s','theta','ss','st','tt','ss_theta']}
        beta={key:zero for key in ['s','theta','ss','st','tt','ss_theta']}
        beta['value']=np.full_like(t,-self.side*np.pi/2)
        return {'u':u,'v':v,'beta':beta,'material_theta':theta,'construction_phi':phi,
            'outward_side':self.side,'material_equation_residual_max':error,
            'frozen_physical_identity':self.identity,'frozen_physical_identity_sha256':self.identity_sha256,
            'port_identity':self.port_identity,'port_identity_sha256':self.port_identity_sha256,
            'a0_numerical':self.a0,'numerical_evaluation_is_not_interval_certificate':True}

    def entry_angle_jets(self,theta):
        """k=psi_theta and its next two angular derivatives, analytically."""
        phi,_=self.phase(theta);c,s=np.cos(phi),np.sin(phi)
        speed=np.sqrt(self.major**2*s*s+self.minor**2*c*c)
        difference=self.major**2-self.minor**2
        k=self.a0*self.major*self.minor/speed**3
        kt=-3*self.major*self.minor*self.a0**2*difference*s*c/speed**6
        ktt=-3*self.major*self.minor*self.a0**3*difference*((c*c-s*s)/speed**7-
                                                            6*difference*s*s*c*c/speed**9)
        return {'k':k,'k_theta':kt,'k_thetatheta':ktt}

    def position_jets(self,t,theta):
        t,theta=np.broadcast_arrays(np.asarray(t,float),np.asarray(theta,float))
        phi,error=self.phase(theta);c,s=np.cos(phi),np.sin(phi)
        speed=np.sqrt(self.major**2*s*s+self.minor**2*c*c)
        raw1=np.stack((-self.major*s,self.minor*c,np.zeros_like(phi)),axis=-1)
        raw2=np.stack((-self.major*c,-self.minor*s,np.zeros_like(phi)),axis=-1)
        speed_phi=(self.major**2-self.minor**2)*s*c/speed
        phi_theta=self.a0/speed;phi_tt=-self.a0**2*speed_phi/speed**3
        X=np.stack((self.major*c,self.minor*s,self.side*(self.width+t)),axis=-1)
        Xtheta=raw1*phi_theta[...,None]
        Xtt=raw2*(phi_theta**2)[...,None]+raw1*phi_tt[...,None]
        Xs=np.zeros_like(X);Xs[...,2]=self.side
        zero=np.zeros_like(X)
        return {'X':X,'Xs':Xs,'Xtheta':Xtheta,'Xss':zero,'Xst':zero,'Xtt':Xtt,
            'material_equation_residual_max':error,'a0_numerical':self.a0,
            'frozen_physical_identity_sha256':self.identity_sha256,
            'position_definition_is_exact':True,'floating_values_are_not_interval_bounds':True}


def developer_check():
    theta=np.array([.17,.51,1.03,1.57,2.31,3.23,5.73]);h=2e-6
    checks=[]
    for side in [1,-1]:
        core=EllipticCylinderPort('9/10','18/25','1/50',side)
        f=core.scalar_jets(.017,theta);xp=core.position_jets(.017,theta+h);xm=core.position_jets(.017,theta-h)
        x=core.position_jets(.017,theta)
        up=core.scalar_jets(.017,theta+h)['u'];um=core.scalar_jets(.017,theta-h)['u']
        diff=lambda a,b:float(np.max(abs(a-b))/max(1.,float(np.max(abs(b)))))
        scalar1=diff(f['u']['theta'],(up['value']-um['value'])/(2*h))
        scalar2=diff(f['u']['tt'],(up['theta']-um['theta'])/(2*h))
        entry=core.entry_angle_jets(theta)
        ep=core.entry_angle_jets(theta+h);em=core.entry_angle_jets(theta-h)
        scalar3=diff(entry['k_thetatheta'],(ep['k_theta']-em['k_theta'])/(2*h))
        position1=diff(x['Xtheta'],(xp['X']-xm['X'])/(2*h))
        position2=diff(x['Xtt'],(xp['Xtheta']-xm['Xtheta'])/(2*h))
        periodic=core.scalar_jets(.017,theta+np.pi)
        reflected=core.scalar_jets(.017,-theta)
        symmetry=max(diff(periodic['u']['value'],f['u']['value']),diff(reflected['u']['value'],-f['u']['value']))
        checks.append({'side':side,'scalar_first_error':scalar1,'scalar_second_error':scalar2,
            'entry_third_angular_error':scalar3,
            'position_first_error':position1,'position_second_error':position2,'periodic_odd_error':symmetry,
            'material_equation_residual_max':f['material_equation_residual_max'],
            'a0_numerical':core.a0,'identity_sha256':core.identity_sha256})
    return {'schema':'ellipse-frame-port-development-v1','artificial_inputs_only':True,
        'research_geometry_evaluated':False,'optimization_performed':False,'checks':checks,
        'passed':all(max(v for k,v in row.items() if k.endswith('error'))<2e-6 for row in checks)}


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--check-only',action='store_true',required=True)
    p.add_argument('--out',type=Path,required=True);args=p.parse_args();result=developer_check()
    result['source_sha256']=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    args.out.parent.mkdir(parents=True,exist_ok=True);args.out.write_text(json.dumps(result,indent=2,allow_nan=False)+'\n')
    print(json.dumps({'out':str(args.out),'passed':result['passed']}),flush=True)
    if not result['passed']:raise SystemExit(1)


if __name__=='__main__':main()
