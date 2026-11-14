#!/usr/bin/env python3
"""Analytic balanced-curvature oval with the ORIGINAL fixed perimeter.

Three exact moment corrections impose axis supports 1.405 and .495 and the
same a0 as the (1.4,.5) ellipse. Corrections are defined by integrals; numerical
quadrature here evaluates that exact definition. The separate interval
certificate proves global curvature-radius bounds without relying on a root
finder. Optional zero-mean support modes retain a0 exactly.
"""
from __future__ import annotations
import os
for _key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[_key]='1'
import argparse,json,math,importlib.util,hashlib
from pathlib import Path
import numpy as np

HERE=Path(__file__).resolve().parent
sp=importlib.util.spec_from_file_location('fd2d_balanced_support_base',HERE/'fd2d_ellipse_support_core.py')
support=importlib.util.module_from_spec(sp);sp.loader.exec_module(support)

PARAMETERS=dict(r='0.22921358484022447',D='2.9353699772701836',c='-0.6589229731934492',k='6',
                A='1.405',B='0.495',reference_A='1.4',reference_B='0.5')


class BalancedOvalCore(support.EllipseSupportCore):
    def __init__(self,coefficients=(0.,0.,0.,0.),quadrature=128):
        self.parameters=dict(PARAMETERS);self.A=float(PARAMETERS['A']);self.B=float(PARAMETERS['B'])
        self.reference=support.fm.ExactEllipse(float(PARAMETERS['reference_A']),float(PARAMETERS['reference_B']))
        self.a0=self.reference.a0;self.r=float(PARAMETERS['r']);self.D=float(PARAMETERS['D'])
        self.c=float(PARAMETERS['c']);self.k=float(PARAMETERS['k'])
        self.coefficients=np.asarray(coefficients,dtype=float)
        self.frequencies=2*np.arange(1,len(self.coefficients)+1,dtype=float);self.weights=self.frequencies**2-1
        x,w=np.polynomial.legendre.leggauss(256);phi=(x+1)*math.pi/4;w=w*math.pi/4
        rho=self.raw_radius(phi);mean=2/math.pi*np.dot(rho,w)
        da=self.A-np.dot(rho*np.sin(phi),w);db=self.B-np.dot(rho*np.cos(phi),w)
        u0=self.a0-mean;u2=1.5*(db-da);u4=-7.5*(da+db-2*u0)
        self.moment_corrections=np.array([u0,u2,u4])
        x,w=np.polynomial.legendre.leggauss(quadrature);self.gx=(x+1)/2;self.gw=w/2
        self.quadrature=quadrature
        # Exact global bounds proved independently by fd2d_balanced_oval_certificate.py.
        self.rho_lower=.228-float(np.sum(self.weights*abs(self.coefficients)))
        self.rho_upper=3.17+float(np.sum(self.weights*abs(self.coefficients)))
        if self.rho_lower<=0:raise ValueError('Support corrections leave the certified convexity domain')

    def raw_radius(self,phi):
        phi=np.asarray(phi,dtype=float)
        return self.r+self.D*(1-np.tanh(self.k*(np.cos(2*phi)-self.c)))/2

    def reference_radius(self,phi):
        phi=np.asarray(phi,dtype=float);u0,u2,u4=self.moment_corrections
        return self.raw_radius(phi)+u0+u2*np.cos(2*phi)+u4*np.cos(4*phi)

    def reference_radius_derivative(self,phi):
        phi=np.asarray(phi,dtype=float);u0,u2,u4=self.moment_corrections
        th=np.tanh(self.k*(np.cos(2*phi)-self.c))
        return self.D*self.k*np.sin(2*phi)*(1-th*th)-2*u2*np.sin(2*phi)-4*u4*np.sin(4*phi)

    def quarter_integrals(self,q):
        q=np.asarray(q,dtype=float);v=q[...,None]*self.gx
        rho=self.reference_radius(v);weight=q[...,None]*self.gw
        return (np.sum(rho*weight,axis=-1),np.sum(rho*np.sin(v)*weight,axis=-1),
                np.sum(rho*np.cos(v)*weight,axis=-1))

    def normal_geometry(self,phi):
        phi=np.asarray(phi,dtype=float);co=np.cos(phi);si=np.sin(phi)
        q=np.arctan2(abs(si),abs(co));_,Is,Ic=self.quarter_integrals(q)
        x=np.sign(co)*(self.A-Is);y=np.sign(si)*Ic
        base=np.stack((x,y,np.zeros_like(phi)),axis=-1)
        n=np.stack((co,si,np.zeros_like(phi)),axis=-1);t=np.stack((-si,co,np.zeros_like(phi)),axis=-1)
        h0=np.sum(base*n,axis=-1);hp0=np.sum(base*t,axis=-1)
        angles=phi[...,None]*self.frequencies;m=self.frequencies;p=self.coefficients
        h=h0+np.cos(angles)@p;hp=hp0-np.sin(angles)@(m*p)
        rho=self.reference_radius(phi)+np.cos(angles)@((1-m*m)*p)
        rhop=self.reference_radius_derivative(phi)-np.sin(angles)@(m*(1-m*m)*p)
        return dict(F=h[...,None]*n+hp[...,None]*t,h=h,hp=hp,rho=rho,rhop=rhop,n=n,t=t)

    def arc(self,phi):
        phi=np.asarray(phi,dtype=float);period=2*math.pi;turns=np.floor(phi/period)
        reduced=phi-turns*period;quadrant=np.floor(reduced/(math.pi/2)).astype(int)
        q=np.arctan2(abs(np.sin(reduced)),abs(np.cos(reduced)));I0,_,_=self.quarter_integrals(q)
        quarter=self.a0*math.pi/2
        base=np.where(quadrant%2==0,quadrant*quarter+I0,(quadrant+1)*quarter-I0)+turns*4*quarter
        return base+np.sin(phi[...,None]*self.frequencies)@((1-self.frequencies**2)*self.coefficients/self.frequencies)

    def reference_coordinate(self,theta):
        theta=np.asarray(theta,dtype=float);A=self.reference.A;B=self.reference.B
        speed=np.sqrt(A*A*np.sin(theta)**2+B*B*np.cos(theta)**2)
        speedp=(A*A-B*B)*np.sin(theta)*np.cos(theta)/speed
        return self.reference.arc(theta)/self.a0,speed/self.a0,speedp/self.a0

    def evaluate(self,sigma):
        # A merely in-bracket Newton step can alternate near the two ends for
        # a steep analytic radius transition. Require central bracket progress.
        sigma=np.asarray(sigma,dtype=float);target=np.mod(sigma,2*math.pi)*self.a0
        phi=np.mod(sigma,2*math.pi).copy();lo=np.zeros_like(phi);hi=np.zeros_like(phi)+2*math.pi
        for iteration in range(80):
            g=self.normal_geometry(phi);residual=self.arc(phi)-target
            done=abs(residual)<=3e-15*np.maximum(1,abs(target))
            if np.all(done):break
            lo=np.where((residual<0)&~done,phi,lo);hi=np.where((residual>0)&~done,phi,hi)
            trial=phi-residual/g['rho'];width=hi-lo
            bad=(trial<=lo+.1*width)|(trial>=hi-.1*width)|~np.isfinite(trial)
            phi=np.where(done,phi,np.where(bad,(lo+hi)/2,trial))
        g=self.normal_geometry(phi);residual=self.arc(phi)-target
        if np.max(abs(residual))>4e-13:raise RuntimeError('Balanced-oval arclength inversion did not converge')
        Xs=np.zeros_like(g['F']);Xs[...,2]=1.
        return dict(F=g['F'],Ft=self.a0*g['t'],Ftt=-self.a0**2*g['n']/g['rho'][...,None],
                    X_s=Xs,X_ss=np.zeros_like(Xs),X_s_sigma=np.zeros_like(Xs),phi=phi,rho=g['rho'],
                    rhop=g['rhop'],n=g['n'],t=g['t'],arc_residual=residual,arc_iterations=iteration+1)

    def gauss_codazzi_initial(self,coordinate,reference_angle=False):
        """Return material jets under unambiguous names on either input grid.

        X_u/X_uu ALWAYS mean material sigma derivatives, including when their
        sample locations are given by baseline ellipse theta. The optional
        X_theta/X_thetatheta fields are then the distinct theta derivatives.
        """
        if reference_angle:
            sigma,first,second=self.reference_coordinate(coordinate)
        else:
            sigma=coordinate
        g=self.evaluate(sigma);T=g['t'];e1=g['X_s']
        normal=np.cross(e1,T)  # inward normal, R116 convention
        out=dict(X=g['F'],X_u=g['Ft'],X_uu=g['Ftt'],e1=e1,e2=T,N=normal,
                 n=1/g['rho'],m=np.zeros_like(g['rho']),l=np.zeros_like(g['rho']),
                 a0=self.a0,material_sigma=np.asarray(sigma),
                 coordinate='reference_eccentric_angle' if reference_angle else 'material_sigma')
        if reference_angle:
            out['X_theta']=g['Ft']*first[...,None]
            out['X_thetatheta']=g['Ftt']*first[...,None]**2+g['Ft']*second[...,None]
            out['X_coordinate']=out['X_theta'];out['X_coordinatecoordinate']=out['X_thetatheta']
        else:
            out['X_coordinate']=out['X_u'];out['X_coordinatecoordinate']=out['X_uu']
        return out

    def inlet(self,flow,angular=2048):
        C,diagnostic=super().inlet(flow,angular)
        diagnostic['core_kind']='fixed_perimeter_balanced_oval'
        return C,diagnostic

    def summary(self):
        p=self.coefficients;j=np.arange(1,len(p)+1);weighted=float(np.sum(self.weights*abs(p)))
        return dict(reference='analytic balanced oval with exact moment correction',parameters=self.parameters,
            a0=self.a0,coefficients=p.tolist(),numerical_moment_corrections=self.moment_corrections.tolist(),
            exact_moment_correction_definition=dict(u0='a0-mean(raw_rho)',
                u2='3/2*(B-int(raw_rho*cos)-A+int(raw_rho*sin))',
                u4='-15/2*(A-int(raw_rho*sin)+B-int(raw_rho*cos)-2*u0)'),
            rho_lower=self.rho_lower,rho_upper=self.rho_upper,curvature_lower=1/self.rho_upper,
            curvature_upper=1/self.rho_lower,long_axis_support=self.A+float(p.sum()),
            short_axis_support=self.B+float(np.dot((-1.)**j,p)),
            axis_gap=self.A-self.B+float(np.dot(1-(-1.)**j,p)),
            correction_weighted_l1=weighted,inside_uniform_strong_core_window=weighted<=.012,
            full_held_protection_verified=False,full_slab_verified=False,whole_surface_reach_verified=False)


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--out',type=Path,required=True)
    args=p.parse_args();core=BalancedOvalCore();u=2*np.pi*np.arange(1024)/1024
    g=core.evaluate(u);theta=2*np.pi*np.arange(1024)/1024;gt=core.evaluate_reference_angle(theta)
    ell=np.sqrt(1.4**2*np.sin(theta)**2+.5**2*np.cos(theta)**2)
    initial=core.gauss_codazzi_initial(theta,reference_angle=True)
    material=core.evaluate(initial['material_sigma'])
    out=dict(scope=__doc__,source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),summary=core.summary(),
        finite_checks=dict(arc_residual=float(abs(g['arc_residual']).max()),
            material_speed_error=float(abs(np.linalg.norm(g['Ft'],axis=1)-core.a0).max()),
            reference_angle_speed_error=float(abs(np.linalg.norm(gt['Ft'],axis=1)-ell).max()),
            initial_material_first_jet_error=float(np.linalg.norm(initial['X_u']-material['Ft'],axis=1).max()),
            initial_material_second_jet_error=float(np.linalg.norm(initial['X_uu']-material['Ftt'],axis=1).max()),
            initial_reference_first_jet_error=float(np.linalg.norm(initial['X_theta']-gt['Ft'],axis=1).max()),
            initial_reference_second_jet_error=float(np.linalg.norm(initial['X_thetatheta']-gt['Ftt'],axis=1).max()),
            rho_min_sample=float(g['rho'].min()),rho_max_sample=float(g['rho'].max()),
            curvature_min_sample=float((1/g['rho']).min()),curvature_max_sample=float((1/g['rho']).max()),
            maximum_abs_y=float(abs(g['F'][:,1]).max()),maximum_radius=float(np.linalg.norm(g['F'],axis=1).max())),
        certificate_file='2026-11-12-fd2d-balanced-oval-moment-certificate.json',closed_surface=False)
    args.out.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))


if __name__=='__main__':main()
