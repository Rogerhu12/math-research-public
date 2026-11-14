#!/usr/bin/env python3
"""Exact fixed-perimeter support-function family around the B=.5 ellipse.

h(phi)=sqrt(A^2*cos(phi)^2+B^2*sin(phi)^2)+sum p_j*cos(2*j*phi).
Zero-mean corrections preserve perimeter 2*pi*a0 exactly. Parameters are
extrinsic core freedoms for a frozen-g BVP. No complete surface is asserted.
"""
from __future__ import annotations
import os
for _key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[_key]='1'
import argparse,json,math,hashlib,importlib.util
from pathlib import Path
import numpy as np

HERE=Path(__file__).resolve().parent
sp=importlib.util.spec_from_file_location('fd2d_exact_ellipse_support',HERE/'fd2d_frozen_ellipse_candidate.py')
fm=importlib.util.module_from_spec(sp);sp.loader.exec_module(fm)


class EllipseSupportCore:
    def __init__(self,coefficients=(.005,0.,0.,0.),A=1.4,B=.5):
        self.A=float(A);self.B=float(B);self.reference=fm.ExactEllipse(A,B);self.a0=self.reference.a0
        self.coefficients=np.asarray(coefficients,dtype=float)
        self.frequencies=2*np.arange(1,len(self.coefficients)+1,dtype=float)
        self.weights=self.frequencies**2-1
        self.rho_lower=self.B**2/self.A-float(np.sum(self.weights*abs(self.coefficients)))
        self.rho_upper=self.A**2/self.B+float(np.sum(self.weights*abs(self.coefficients)))
        if self.rho_lower<=0:raise ValueError('Support family leaves the certified strictly convex parameter domain')

    def normal_geometry(self,phi):
        phi=np.asarray(phi,dtype=float);co=np.cos(phi);si=np.sin(phi)
        h0=np.sqrt(self.A*self.A*co*co+self.B*self.B*si*si)
        hp0=(self.B*self.B-self.A*self.A)*si*co/h0
        rho0=(self.A*self.B)**2/h0**3;rhop0=-3*rho0*hp0/h0
        modes=phi[...,None]*self.frequencies;c=self.coefficients;m=self.frequencies
        h=h0+np.cos(modes)@c;hp=hp0-np.sin(modes)@(m*c)
        rho=rho0+np.cos(modes)@((1-m*m)*c)
        rhop=rhop0-np.sin(modes)@(m*(1-m*m)*c)
        n=np.stack((co,si,np.zeros_like(phi)),axis=-1)
        t=np.stack((-si,co,np.zeros_like(phi)),axis=-1)
        return dict(F=h[...,None]*n+hp[...,None]*t,h=h,hp=hp,rho=rho,rhop=rhop,n=n,t=t)

    def arc(self,phi):
        phi=np.asarray(phi,dtype=float);period=2*math.pi;turns=np.floor(phi/period)
        reduced=phi-turns*period
        theta=np.mod(np.arctan2(self.B*np.sin(reduced),self.A*np.cos(reduced)),period)
        out=turns*period*self.a0+self.reference.arc(theta)
        return out+np.sin(phi[...,None]*self.frequencies)@((1-self.frequencies**2)*self.coefficients/self.frequencies)

    def evaluate(self,sigma):
        sigma=np.asarray(sigma,dtype=float);target=np.mod(sigma,2*math.pi)*self.a0
        phi=np.mod(sigma,2*math.pi).copy();lo=np.zeros_like(phi);hi=np.zeros_like(phi)+2*math.pi
        for iteration in range(80):
            g=self.normal_geometry(phi);residual=self.arc(phi)-target
            done=abs(residual)<=3e-15*np.maximum(1,abs(target))
            if np.all(done):break
            lo=np.where((residual<0)&~done,phi,lo);hi=np.where((residual>0)&~done,phi,hi)
            trial=phi-residual/g['rho'];bad=(trial<=lo)|(trial>=hi)|~np.isfinite(trial)
            phi=np.where(done,phi,np.where(bad,(lo+hi)/2,trial))
        g=self.normal_geometry(phi);residual=self.arc(phi)-target
        if np.max(abs(residual))>4e-13:raise RuntimeError('Arclength inversion did not converge')
        Xs=np.zeros_like(g['F']);Xs[...,2]=1.
        return dict(F=g['F'],Ft=self.a0*g['t'],Ftt=-self.a0**2*g['n']/g['rho'][...,None],
                    X_s=Xs,X_ss=np.zeros_like(Xs),X_s_sigma=np.zeros_like(Xs),
                    phi=phi,rho=g['rho'],rhop=g['rhop'],n=g['n'],t=g['t'],
                    arc_residual=residual,arc_iterations=iteration+1)

    def parameter_derivatives(self,sigma,angular_order=0):
        g=self.evaluate(sigma);phi=g['phi'];m=self.frequencies[:,None];c=1-m*m
        co=np.cos(m*phi[None,:]);si=np.sin(m*phi[None,:]);rho=g['rho'][None,:]
        if angular_order==0:
            return co[:,:,None]*g['n'][None,:,:]-(si/m)[:,:,None]*g['t'][None,:,:]
        if angular_order==1:
            return (c*self.a0*si/(m*rho))[:,:,None]*g['n'][None,:,:]
        if angular_order==2:
            normal=c*self.a0**2/m*(m*co/rho**2-si*g['rhop'][None,:]/rho**3)
            tangent=c*self.a0**2/m*si/rho**2
            return normal[:,:,None]*g['n'][None,:,:]+tangent[:,:,None]*g['t'][None,:,:]
        raise ValueError('Only angular derivative orders 0, 1, 2 are supplied')

    def parameter_hessian(self,sigma):
        g=self.evaluate(sigma);m=self.frequencies[:,None]
        f=(1-m*m)*np.sin(m*g['phi'][None,:])/m
        return -(f[:,None,:]*f[None,:,:]/g['rho'][None,None,:])[:,:,:,None]*g['n'][None,None,:,:]

    def reference_coordinate(self,theta):
        theta=np.asarray(theta,dtype=float)
        speed=np.sqrt(self.A**2*np.sin(theta)**2+self.B**2*np.cos(theta)**2)
        speedp=(self.A**2-self.B**2)*np.sin(theta)*np.cos(theta)/speed
        return self.reference.arc(theta)/self.a0,speed/self.a0,speedp/self.a0

    def evaluate_reference_angle(self,theta):
        """Use one fixed baseline eccentric coordinate for every p.

        This is not the p-dependent normal angle. The angular target metric is
        ell_E(theta)^2 for every core, and a(s)^2*ell_E(theta)^2/a0^2 later.
        """
        sigma,first,second=self.reference_coordinate(theta);g=self.evaluate(sigma)
        out=dict(g);out['Ft']=g['Ft']*first[...,None]
        out['Ftt']=g['Ftt']*first[...,None]**2+g['Ft']*second[...,None]
        out['reference_sigma']=sigma
        return out

    def parameter_derivatives_reference_angle(self,theta,angular_order=0):
        sigma,first,second=self.reference_coordinate(theta)
        if angular_order==0:return self.parameter_derivatives(sigma,0)
        if angular_order==1:return self.parameter_derivatives(sigma,1)*first[None,:,None]
        if angular_order==2:
            return (self.parameter_derivatives(sigma,2)*first[None,:,None]**2
                    +self.parameter_derivatives(sigma,1)*second[None,:,None])
        raise ValueError('Only angular derivative orders 0, 1, 2 are supplied')

    def inlet(self,flow,angular=2048):
        sigma=2*np.pi*np.arange(angular)/angular;g=self.evaluate(sigma)
        B,B1,B2=flow.basis(angular);C=flow.project(g['F'][None,:,:],B)[:,0]
        X=flow.values(C[:,None],B)[0];first=flow.values(C[:,None],B1)[0];second=flow.values(C[:,None],B2)[0]
        return C,dict(core_kind='fixed_perimeter_ellipse_support',a0=self.a0,coefficients=self.coefficients.tolist(),
            curvature_radius_lower=self.rho_lower,curvature_radius_upper=self.rho_upper,
            position_projection_error=float(np.linalg.norm(X-g['F'],axis=1).max()),
            first_jet_projection_error=float(np.linalg.norm(first-g['Ft'],axis=1).max()),
            second_jet_projection_error=float(np.linalg.norm(second-g['Ftt'],axis=1).max()),
            relative_angular_metric_error=float(abs(np.sum(first*first,axis=1)/self.a0**2-1).max()))

    def inlet_jacobian(self,flow,angular=2048):
        sigma=2*np.pi*np.arange(angular)/angular;B,_,_=flow.basis(angular)
        return flow.project(self.parameter_derivatives(sigma),B)

    def summary(self):
        p=self.coefficients;j=np.arange(1,len(p)+1);reference=np.zeros_like(p)
        if len(reference):reference[0]=.005
        correction=p-reference;weighted=float(np.sum(self.weights*abs(correction)))
        return dict(A=self.A,B=self.B,a0=self.a0,coefficients=p.tolist(),frequencies=self.frequencies.tolist(),
            perimeter_definition='2*pi*a0, independent of p',rho_lower=self.rho_lower,rho_upper=self.rho_upper,
            curvature_upper=1/self.rho_lower,long_axis_support=self.A+float(p.sum()),
            short_axis_support=self.B+float(np.dot((-1.)**j,p)),
            axis_gap=self.A-self.B+float(np.dot(1-(-1.)**j,p)),
            correction_weighted_l1=weighted,inside_uniform_strong_core_window=weighted<=.012,
            full_held_protection_verified=False,full_slab_verified=False,whole_surface_reach_verified=False)


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--out',type=Path,required=True)
    args=p.parse_args();sigma=2*np.pi*np.arange(513)/513
    coefficients=np.array([.005,.0001,-.00005,.00001]);core=EllipseSupportCore(coefficients)
    g=core.evaluate(sigma);rows=[];step=1e-6
    for j in range(len(coefficients)):
        plus=coefficients.copy();minus=coefficients.copy();plus[j]+=step;minus[j]-=step
        gp=EllipseSupportCore(plus).evaluate(sigma);gm=EllipseSupportCore(minus).evaluate(sigma)
        row=dict(parameter=j+1)
        for order,key in enumerate(('F','Ft','Ftt')):
            fd=(gp[key]-gm[key])/(2*step);actual=core.parameter_derivatives(sigma,order)[j]
            row[key+'_jacobian_difference']=float(np.linalg.norm(fd-actual,axis=1).max())
        rows.append(row)
    out=dict(scope=__doc__,source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        example=core.summary(),exact_ellipse=EllipseSupportCore(np.zeros(4)).summary(),
        baseline=EllipseSupportCore().summary(),
        finite_checks=dict(arclength_speed_error=float(abs(np.linalg.norm(g['Ft'],axis=1)-core.a0).max()),
            arc_residual=float(abs(g['arc_residual']).max()),rho_min_sample=float(g['rho'].min()),
            parameter_difference_step=step,parameter_jet_checks=rows),
        uniform_parameter_window=dict(reference_first_coefficient=.005,weighted_l1_radius=.012,
            rho_lower_exact='1061/7000',curvature_upper_exact='7000/1061',
            long_support_lower=1.401,short_support_upper=.499,axis_gap_lower=.902),
        nonlinear_prefix_solved=False,closed_surface=False)
    args.out.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))


if __name__=='__main__':main()
