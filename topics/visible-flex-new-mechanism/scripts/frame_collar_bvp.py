#!/usr/bin/env python3
"""Finite orthonormal-frame collar design with exact open core/flat ports.

The primary ellipse port uses analytic angular derivatives. A general port
may instead request auditable periodic spectral differentiation. The actual
field has exact unit orthogonal target tangents; integrability, reconstructed
metric, shape and curvature are separately audited. Research solves run only
in this public repository Actions. Development checks use artificial inputs.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as Q
import hashlib
import json
import os
from pathlib import Path
import time

import numpy as np
from numpy.polynomial.legendre import leggauss
from numpy.polynomial.polynomial import polyval,polyder
from scipy.interpolate import BSpline
from scipy.optimize import least_squares

from ellipse_frame_port import EllipticCylinderPort
from cosine_connector_radial_seed import NegativeKRadialSeed


def mul(value,vector):return np.asarray(value)[...,None]*vector


def dot(a,b):return np.sum(a*b,axis=-1)


def periodic_operator(values,order):
    values=np.asarray(values,float);n=values.shape[1]
    frequencies=np.fft.fftfreq(n)*n
    factor=np.zeros(n,dtype=complex)
    nonzero=frequencies!=0
    factor[nonzero]=(1j*frequencies[nonzero])**order
    if order==1 and n%2==0:factor[n//2]=0
    shape=(1,n)+((1,)*(values.ndim-2))
    return np.fft.ifft(np.fft.fft(values,axis=1)*factor.reshape(shape),axis=1).real


def smooth_positive(x,epsilon=1e-8):
    x=np.asarray(x,float);r=np.hypot(x,epsilon);positive=x>=0
    value=np.empty_like(x);value[positive]=.5*(x[positive]+r[positive])
    value[~positive]=.5*epsilon**2/(r[~positive]-x[~positive])
    return value,.5*(1+x/r)


class RadialBasis:
    def __init__(self,free_count,left,right,endpoint_weight=False):
        self.count=int(free_count);self.left=float(left);self.right=float(right)
        self.endpoint_weight=bool(endpoint_weight)
        if self.count<0 or self.right<=self.left:raise ValueError('invalid clamped radial basis')
        if self.count:
            interior=np.linspace(self.left,self.right,self.count+2)[1:-1]
            self.knots=np.r_[np.repeat(self.left,6),interior,np.repeat(self.right,6)]
            self.full=BSpline(self.knots,np.eye(self.count+6),5,extrapolate=False)
    def evaluate(self,points,order=0):
        points=np.asarray(points,float)
        if not self.count:return np.zeros(points.shape+(0,))
        value=self.full(np.clip(points,self.left,self.right),nu=order)[...,3:-3]
        if self.endpoint_weight:
            length=self.right-self.left;x=(points-self.left)/length
            weight=16*x*x*(1-x)**2
            if order==0:value=weight[...,None]*value
            else:
                w1=32*x*(1-x)*(1-2*x)/length
                b0=self.full(np.clip(points,self.left,self.right),nu=0)[...,3:-3]
                if order==1:value=weight[...,None]*value+w1[...,None]*b0
                elif order==2:
                    w2=32*(1-6*x+6*x*x)/length**2
                    b1=self.full(np.clip(points,self.left,self.right),nu=1)[...,3:-3]
                    value=weight[...,None]*value+2*w1[...,None]*b1+w2[...,None]*b0
                else:raise ValueError('weighted metric basis jets are implemented through order two')
        return np.where(((points>self.left)&(points<self.right))[...,None],value,0.)


HERMITE=[np.array(x,float) for x in [
    [1,0,0,0,0,-126,420,-540,315,-70],
    [0,1,0,0,0,-70,224,-280,160,-35],
    [0,0,.5,0,0,-17.5,52.5,-63,35,-7.5],
    [0,0,0,0,0,126,-420,540,-315,70]]]


def local_cauchy_factor(points,power,length,order=0):
    """x^power*(1-S9(x/length)), compactly supported in [0,length]."""
    x=np.asarray(points,float);inside=(x>0)&(x<length);y=np.clip(x/length,0,1)
    chi=polyval(y,HERMITE[0]);dchi=polyval(y,polyder(HERMITE[0],1))/length
    ddchi=polyval(y,polyder(HERMITE[0],2))/length**2
    if order==0:value=x**power*chi
    elif order==1:value=power*x**(power-1)*chi+x**power*dchi
    elif order==2:value=power*(power-1)*x**(power-2)*chi+2*power*x**(power-1)*dchi+x**power*ddchi
    else:raise ValueError('local entry jets are available through order two')
    return np.where(inside,value,0.)


class FieldGrid:
    def __init__(self,problem,radial,theta):
        self.problem=problem;self.radial=np.asarray(radial,float);self.theta=np.asarray(theta,float)
        if self.radial.ndim!=1 or self.theta.ndim!=1:raise ValueError('product grids must be one-dimensional')
        self.analytic=problem.port.angular_derivative_mode=='analytic'
        self.bases={order:problem.field_basis.evaluate(self.radial,order) for order in range(3)}
        frequencies=problem.fold*np.arange(1,problem.angular_modes+1)
        beta_frequencies=problem.fold*np.arange(problem.angular_modes+1)
        self.angular={'u':np.sin(self.theta[:,None]*frequencies),
                      'v':np.sin(self.theta[:,None]*frequencies),
                      'beta':np.cos(self.theta[:,None]*beta_frequencies)}
        self.angular_first={'u':np.cos(self.theta[:,None]*frequencies)*frequencies,
                            'v':np.cos(self.theta[:,None]*frequencies)*frequencies,
                            'beta':-np.sin(self.theta[:,None]*beta_frequencies)*beta_frequencies}
        shape=(len(self.radial),len(self.theta))
        self.base={name:{key:np.zeros(shape) for key in ['value','s','ss','theta']}
                   for name in ['u','v','beta']}
        before=self.radial<=problem.active_start;after=self.radial>=problem.active_end
        active=~(before|after)
        if np.any(before):
            original=problem.port.scalar_jets(self.radial[before,None],self.theta[None,:])
            for name in self.base:
                for key in self.base[name]:self.base[name][key][before]=original[name][key]
        for name in self.base:
            self.base[name]['value'][after]=problem.tail_beta if name=='beta' else 0.
        port=problem.port.scalar_jets(problem.active_start,self.theta)
        length=problem.active_end-problem.active_start
        x=(self.radial[active]-problem.active_start)/length
        for order,key in [(0,'value'),(1,'s'),(2,'ss')]:
            weights=np.stack([polyval(x,polyder(poly,order))*length**(j if j<3 else 0)/length**order
                              for j,poly in enumerate(HERMITE)],axis=-1)
            for name in self.base:
                endpoint=np.stack((port[name]['value'],port[name]['s'],port[name]['ss'],
                    np.full(len(self.theta),problem.tail_beta if name=='beta' else 0.)))
                self.base[name][key][active]=weights@endpoint
        if self.analytic:
            weights=np.stack([polyval(x,poly)*length**(j if j<3 else 0)
                              for j,poly in enumerate(HERMITE)],axis=-1)
            for name in self.base:
                endpoint=np.stack((port[name]['theta'],port[name]['st'],port[name]['ss_theta'],np.zeros(len(self.theta))))
                self.base[name]['theta'][active]=weights@endpoint
        # Necessary leading Cauchy terms for the accurate elliptic cylinder.
        # They are a local seed, not a claim that the full Cauchy series exists.
        if problem.entry_cauchy:
            coefficients=problem.entry_coefficients(self.theta)
            physical=self.radial-problem.active_start
            for name,power in [('beta',3),('u',4)]:
                for order,key in [(0,'value'),(1,'s'),(2,'ss')]:
                    factor=local_cauchy_factor(physical,power,problem.entry_length,order)
                    self.base[name][key]+=factor[:,None]*coefficients[name][None,:]
                factor=local_cauchy_factor(physical,power,problem.entry_length,0)
                self.base[name]['theta']+=factor[:,None]*coefficients[name+'_theta'][None,:]
        self._jac={}

    def basis_jacobian(self,name,kind='value'):
        cache=(name,kind)
        if cache in self._jac:return self._jac[cache]
        radial=self.bases[1 if kind=='s' else 0]
        angular=self.angular_first[name] if kind=='theta' else self.angular[name]
        result=np.einsum('ri,tk->rtik',radial,angular).reshape(len(self.radial),len(self.theta),-1)
        self._jac[cache]=result;return result

    def fields(self,state):
        answer={}
        for name in self.base:
            coefficient=np.asarray(state[self.problem.slices[name]]).reshape(self.problem.radial_free,-1)
            values={}
            for order,key in [(0,'value'),(1,'s'),(2,'ss')]:
                values[key]=self.base[name][key]+np.einsum('ri,ik,tk->rt',self.bases[order],coefficient,self.angular[name])
            if self.analytic:
                values['theta']=self.base[name]['theta']+np.einsum('ri,ik,tk->rt',self.bases[0],coefficient,self.angular_first[name])
            else:values['theta']=periodic_operator(values['value'],1)
            answer[name]=values
        return answer


def target_frame(fields):
    u,v,beta=(fields[name]['value'] for name in ['u','v','beta'])
    theta=fields['_theta'];psi=theta+u
    zero=np.zeros_like(u);ez=np.stack((zero,zero,np.ones_like(u)),axis=-1)
    N=np.stack((np.cos(psi),np.sin(psi),zero),axis=-1)
    H=np.stack((-np.sin(psi),np.cos(psi),zero),axis=-1)
    c=1/np.sqrt(1+v*v);d=v*c;C=np.cos(beta);S=np.sin(beta)
    T=mul(c,H)+mul(d,ez);M=mul(d,H)-mul(c,ez)
    V=mul(C,N)+mul(S,M)
    Tu=-mul(c,N);Tv=mul(c**3,ez-v[...,None]*H)
    Tuu=-mul(c,H);Tuv=mul(v*c**3,N)
    Tvv=mul((2*v*v-1)*c**5,H)-mul(3*v*c**5,ez)
    Vu=mul(C,H)-mul(S*d,N)
    Vv=mul(S*c**3,H+v[...,None]*ez)
    Vb=-mul(S,N)+mul(C,M)
    Vuu=-mul(C,N)-mul(S*d,H)
    Vuv=-mul(S*c**3,N);Vub=-mul(S,H)-mul(C*d,N)
    Vvv=mul(-3*S*v*c**5,H)+mul(S*(1-2*v*v)*c**5,ez)
    Vvb=mul(C*c**3,H+v[...,None]*ez);Vbb=-V
    us,vs,bs=(fields[name]['s'] for name in ['u','v','beta'])
    Ts=mul(us,Tu)+mul(vs,Tv)
    Tss=(mul(us*us,Tuu)+mul(2*us*vs,Tuv)+mul(vs*vs,Tvv)+
          mul(fields['u']['ss'],Tu)+mul(fields['v']['ss'],Tv))
    Vs=mul(us,Vu)+mul(vs,Vv)+mul(bs,Vb)
    ut,vt,bt=(fields[name]['theta'] for name in ['u','v','beta'])
    # u_theta is the correction-angle derivative; psi_theta=1+u_theta.
    psi_t=1+ut
    Ttheta=mul(psi_t,Tu)+mul(vt,Tv)
    Vtheta=mul(psi_t,Vu)+mul(vt,Vv)+mul(bt,Vb)
    return {'T':T,'V':V,'Ts':Ts,'Tss':Tss,'Vs':Vs,'Ttheta':Ttheta,'Vtheta':Vtheta,
        'Tpart':{'u':Tu,'v':Tv},'Vpart':{'u':Vu,'v':Vv,'beta':Vb},
        'Ts_value_part':{'u':mul(us,Tuu)+mul(vs,Tuv),'v':mul(us,Tuv)+mul(vs,Tvv)},
        'Vtheta_value_part':{
            'u':mul(psi_t,Vuu)+mul(vt,Vuv)+mul(bt,Vub),
            'v':mul(psi_t,Vuv)+mul(vt,Vvv)+mul(bt,Vvb),
            'beta':mul(psi_t,Vub)+mul(vt,Vvb)+mul(bt,Vbb)}}


def radial_quadrature(points,order):
    nodes,weights=leggauss(order);points=np.asarray(points,float)
    widths=np.diff(points)/2;mid=(points[1:]+points[:-1])/2
    return (mid[:,None]+widths[:,None]*nodes).ravel(),widths[:,None]*weights


class FrameCollarProblem:
    def __init__(self,port,seed,radial_free=4,angular_modes=5,metric_free=0,
                 fixed_metric_coefficients=None,ellipse_envelope=None,height_limit=.45,shape_weight=2.,
                 radial_nodes=29,angular_nodes=96,radial_quadrature_order=4):
        self.port=port;self.seed=seed;self.fold=int(port.fold)
        if self.fold<2:raise ValueError('zero mean from symmetry requires fold >= 2')
        self.radial_free=int(radial_free);self.angular_modes=int(angular_modes)
        self.active_start=seed.core_fraction*seed.length
        self.active_end=(1-seed.flat_fraction)*seed.length
        if self.active_start>port.maximum_exact_prefix:
            raise ValueError('the open core buffer exceeds the port exact-prefix domain')
        self.tail_beta=-port.side*np.pi
        self.entry_cauchy=hasattr(port,'entry_angle_jets')
        self.first_segment_length=seed.length*seed.widths[0]
        self.entry_c3=-10*seed.mu/self.first_segment_length**3
        self.entry_length=self.first_segment_length/4
        self.field_basis=RadialBasis(self.radial_free,self.active_start,self.active_end)
        self.metric_free=int(metric_free)
        self.fixed_metric=np.asarray([] if fixed_metric_coefficients is None else fixed_metric_coefficients,float)
        if self.metric_free and len(self.fixed_metric):raise ValueError('metric design and frozen metric coefficients are mutually exclusive')
        self.metric_basis=RadialBasis(self.metric_free or len(self.fixed_metric),self.active_start,self.active_end,
                                      endpoint_weight=True)
        self.slices={};offset=0
        for name,modes in [('u',self.angular_modes),('v',self.angular_modes),('beta',self.angular_modes+1)]:
            count=self.radial_free*modes;self.slices[name]=slice(offset,offset+count);offset+=count
        self.slices['metric']=slice(offset,offset+self.metric_free);self.field_count=offset
        self.nunknown=offset+self.metric_free
        self.envelope=ellipse_envelope;self.height_limit=float(height_limit);self.shape_weight=float(shape_weight)
        self.radial_quadrature_order=int(radial_quadrature_order)
        if self.height_limit<=0 or self.radial_free<1 or self.angular_modes<1:raise ValueError('positive dimensions and height bound required')
        if angular_nodes%(2*self.fold):raise ValueError('angular grid must be divisible by twice the symmetry fold')
        self.radial=np.linspace(0,seed.length,int(radial_nodes));self.theta=np.arange(angular_nodes)*2*np.pi/angular_nodes
        self._grids={};self.grid=self.grid_for(self.radial,self.theta)
        qnodes,self.quad_weights=radial_quadrature(self.radial,self.radial_quadrature_order)
        self.quad_grid=self.grid_for(qnodes,self.theta)
        self._cache=None

    def entry_coefficients(self,theta):
        angle=self.port.entry_angle_jets(theta)
        k,kt,ktt=(angle[key] for key in ['k','k_theta','k_thetatheta'])
        c=self.entry_c3;a0=self.port.a0;side=self.port.side
        return {'beta':side*c/k,'beta_theta':-side*c*kt/k**2,
                'u':c*kt/(4*a0*k**2),
                'u_theta':c/(4*a0)*(ktt/k**2-2*kt*kt/k**3)}

    def grid_for(self,radial,theta):
        key=(np.asarray(radial,float).tobytes(),np.asarray(theta,float).tobytes())
        if key not in self._grids:self._grids[key]=FieldGrid(self,radial,theta)
        return self._grids[key]

    def frame(self,state,grid):
        fields=grid.fields(state);fields['_theta']=grid.theta[None,:]
        result=target_frame(fields)
        if not grid.analytic:
            result['Vtheta']=periodic_operator(result['V'],1)
            result['Ttheta']=periodic_operator(result['T'],1)
        return result

    def metric(self,state,radial,jacobian=False):
        base=self.seed.evaluate(radial)
        coefficient=np.asarray(state[self.slices['metric']]) if self.metric_free else self.fixed_metric
        B=self.metric_basis.evaluate(radial,0);Bs=self.metric_basis.evaluate(radial,1);Bss=self.metric_basis.evaluate(radial,2)
        h=B@coefficient;hs=Bs@coefficient;hss=Bss@coefficient
        e=np.exp(h);a=base['a']*e
        ap=e*(base['a_s']+base['a']*hs)
        app=e*(base['a_ss']+2*base['a_s']*hs+base['a']*(hss+hs*hs))
        answer={'a':a,'a_s':ap,'a_ss':app,'K':-app/a}
        if jacobian:
            answer['jac_a']=a[:,None]*B if self.metric_free else np.zeros((len(radial),0))
            answer['jac_as']=(ap[:,None]*B+a[:,None]*Bs) if self.metric_free else np.zeros((len(radial),0))
        return answer

    def frame_parameter_jacobian(self,state,grid,frame,with_R=False,metric=None):
        answer={}
        for name in ['u','v','beta']:
            B=grid.basis_jacobian(name)
            dV=frame['Vpart'][name][...,None]*B[:,:,None,:]
            block={'V':dV}
            if name!='beta':
                dT=frame['Tpart'][name][...,None]*B[:,:,None,:]
                dTs=(frame['Ts_value_part'][name][...,None]*B[:,:,None,:]+
                     frame['Tpart'][name][...,None]*grid.basis_jacobian(name,'s')[:,:,None,:])
                block.update(T=dT,Ts=dTs)
            if with_R:
                if grid.analytic:
                    dVtheta=(frame['Vtheta_value_part'][name][...,None]*B[:,:,None,:]+
                              frame['Vpart'][name][...,None]*grid.basis_jacobian(name,'theta')[:,:,None,:])
                else:dVtheta=periodic_operator(dV,1)
                if name!='beta':
                    dVtheta=dVtheta-metric['a_s'][:,None,None,None]*block['T']-metric['a'][:,None,None,None]*block['Ts']
                block['R']=dVtheta
            answer[name]=block
        return answer

    def geometry(self,state,grid,quadrature_order=None,jacobian=False,with_R=False):
        if len(grid.radial)<2 or grid.radial[0]!=0 or np.any(np.diff(grid.radial)<=0):
            raise ValueError('position reconstruction must integrate from physical t=0 over a strictly increasing radial grid')
        order=self.radial_quadrature_order if quadrature_order is None else quadrature_order
        frame=self.frame(state,grid);metric=self.metric(state,grid.radial,jacobian)
        a,ap,app=(metric[key] for key in ['a','a_s','a_ss'])
        primitive=periodic_operator(frame['T'],-1)
        qnodes,weights=radial_quadrature(grid.radial,order);qgrid=self.grid_for(qnodes,grid.theta)
        qframe=self.frame(state,qgrid);means=qframe['V'][...,2].mean(axis=1)
        increments=np.sum(means.reshape(len(grid.radial)-1,order)*weights,axis=1)
        center=self.port.initial_center_z+np.r_[0.,np.cumsum(increments)]
        X=a[:,None,None]*primitive;X[...,2]+=center[:,None]
        meanV=frame['V'].mean(axis=1);meanVs=frame['Vs'].mean(axis=1)
        PiTs=periodic_operator(frame['Ts'],-1);PiTss=periodic_operator(frame['Tss'],-1)
        Xs=ap[:,None,None]*primitive+a[:,None,None]*PiTs;Xs[...,2]+=meanV[:,None,2]
        Xss=(app[:,None,None]*primitive+2*ap[:,None,None]*PiTs+a[:,None,None]*PiTss)
        Xss[...,2]+=meanVs[:,None,2]
        Xt=a[:,None,None]*frame['T'];Xst=ap[:,None,None]*frame['T']+a[:,None,None]*frame['Ts']
        Xtt=a[:,None,None]*frame['Ttheta']
        R=frame['Vtheta']-ap[:,None,None]*frame['T']-a[:,None,None]*frame['Ts']
        answer={'X':X,'Xs':Xs,'Xt':Xt,'Xss':Xss,'Xst':Xst,'Xtt':Xtt,
                'R':R,'metric':metric,'frame':frame,'center':center,'primitive':primitive}
        if jacobian:
            blocks=self.frame_parameter_jacobian(state,grid,frame,with_R,metric)
            qblocks=self.frame_parameter_jacobian(state,qgrid,qframe)
            dX=[];dR=[]
            for name in ['u','v','beta']:
                count=self.slices[name].stop-self.slices[name].start
                mean=qblocks[name]['V'][:,:,2,:].mean(axis=1)
                integrals=np.sum(mean.reshape(len(grid.radial)-1,order,count)*weights[...,None],axis=1)
                dc=np.vstack((np.zeros((1,count)),np.cumsum(integrals,axis=0)))
                if name!='beta':dx=a[:,None,None,None]*periodic_operator(blocks[name]['T'],-1)
                else:dx=np.zeros(X.shape+(count,))
                dx[:,:,2,:]+=dc[:,None,:];dX.append(dx)
                if with_R:dR.append(blocks[name]['R'])
            if self.metric_free:
                dX.append(primitive[...,None]*metric['jac_a'][:,None,None,:])
                if with_R:dR.append(-frame['T'][...,None]*metric['jac_as'][:,None,None,:]-
                                    frame['Ts'][...,None]*metric['jac_a'][:,None,None,:])
            answer['jac_X']=np.concatenate(dX,axis=-1)
            if with_R:answer['jac_R']=np.concatenate(dR,axis=-1)
        return answer

    def residual_and_jacobian(self,state):
        state=np.asarray(state,float)
        if self._cache is not None and np.array_equal(self._cache[0],state):return self._cache[1:]
        data=self.geometry(state,self.grid,jacobian=True,with_R=True)
        count=len(self.radial)*len(self.theta);scale=1/np.sqrt(count)
        residual=[data['R'].ravel()*scale]
        jacobian=[data['jac_R'].reshape(-1,self.nunknown)*scale]
        if self.shape_weight>0:
            X=data['X'];dX=data['jac_X'];weight=self.shape_weight*scale
            if self.envelope is not None:
                A,B=self.envelope
                radial=(X[...,0]/A)**2+(X[...,1]/B)**2-1
                d_radial=2*X[...,0,None]*dX[:,:,0,:]/A**2+2*X[...,1,None]*dX[:,:,1,:]/B**2
                positive,derivative=smooth_positive(radial)
                residual.append(weight*positive.ravel());jacobian.append(weight*(derivative[...,None]*d_radial).reshape(-1,self.nunknown))
            for sign in [1,-1]:
                value=sign*X[...,2]/self.height_limit-1
                positive,derivative=smooth_positive(value)
                residual.append(weight*positive.ravel())
                jacobian.append(weight*(derivative[...,None]*sign*dX[:,:,2,:]/self.height_limit).reshape(-1,self.nunknown))
        rr=np.concatenate(residual);jj=np.vstack(jacobian)
        self._cache=(state.copy(),rr,jj,data)
        return rr,jj,data

    def residual(self,state):return self.residual_and_jacobian(state)[0]
    def jacobian(self,state):return self.residual_and_jacobian(state)[1]

    def metric_model(self,state):
        coefficients=np.asarray(state[self.slices['metric']]) if self.metric_free else self.fixed_metric
        exact=[str(Q.from_float(float(x))) for x in coefficients]
        seed=self.seed.frozen_definition()
        mathematical={'seed_definition_sha256':seed['definition_sha256'],
            'positive_radius_definition':'a_seed(t)*exp(sum(c_j*B_j(t)))',
            'log_basis_degree':5,'log_basis_free_count':len(exact),
            'log_basis_interval':'[core_fraction*L,(1-flat_fraction)*L]',
            'log_basis_endpoint_weight':'16*x^2*(1-x)^2; x is normalized active coordinate',
            'log_basis_coefficients_exact':exact}
        digest=hashlib.sha256(json.dumps(mathematical,sort_keys=True,separators=(',',':')).encode()).hexdigest()
        return {'seed':seed,'mathematical_definition':mathematical,'mathematical_definition_sha256':digest,
                'metric_is_being_designed':bool(self.metric_free),
                'a0_is_exact_core_perimeter_not_frozen_float':True}


def audit_geometry(problem,state,grid,data=None,quadrature_order=8):
    if data is None:data=problem.geometry(state,grid,quadrature_order=quadrature_order)
    X,Xs,Xt=(data[name] for name in ['X','Xs','Xt'])
    a=data['metric']['a'][:,None]
    E=dot(Xs,Xs);F=dot(Xs,Xt);G=dot(Xt,Xt)
    A=E-1;D=G/a**2-1;off=F/a
    op=(abs(A+D)+np.sqrt((A-D)**2+4*off**2))/2
    cross=np.cross(Xs,Xt);area=np.linalg.norm(cross,axis=-1)
    curvature=None;gauss_min=None;gauss_max=None;discriminant_min=None
    if np.min(area)>0:
        with np.errstate(over='ignore',invalid='ignore',divide='ignore'):
            normal=cross/area[...,None]
            l=dot(normal,data['Xss']);m=dot(normal,data['Xst']);n=dot(normal,data['Xtt'])
            K=(l*n-m*m)/area**2;H=(E*n-2*F*m+G*l)/(2*area**2)
            disc=H*H-K;principal=abs(H)+np.sqrt(np.maximum(disc,0))
        if np.all(np.isfinite(principal)):
            curvature=float(np.max(principal));gauss_min=float(np.min(K));gauss_max=float(np.max(K))
            discriminant_min=float(np.min(disc))
    Rmax=float(np.max(np.linalg.norm(data['R'],axis=-1)))
    e=np.pi*Rmax/2
    primitiveR=periodic_operator(data['R'],-1)
    identity_error=float(np.max(np.linalg.norm(Xs-data['frame']['V']+primitiveR,axis=-1)))
    target=problem.port.position_jets(0,grid.theta)
    endpoint={'core':{},'tail':{}}
    for produced,expected in [('X','X'),('Xs','Xs'),('Xt','Xtheta'),('Xss','Xss'),('Xst','Xst'),('Xtt','Xtt')]:
        endpoint['core'][produced]=float(np.max(np.linalg.norm(data[produced][0]-target[expected],axis=-1)))
    er=np.stack((np.cos(grid.theta),np.sin(grid.theta),np.zeros_like(grid.theta)),axis=-1)
    et=np.stack((-np.sin(grid.theta),np.cos(grid.theta),np.zeros_like(grid.theta)),axis=-1)
    tail_x=problem.seed.cut_radius*er;tail_x[:,2]=data['center'][-1]
    tail={'X':tail_x,'Xs':-er,'Xt':problem.seed.cut_radius*et,'Xss':np.zeros_like(er),
          'Xst':-et,'Xtt':-problem.seed.cut_radius*er}
    for name in tail:endpoint['tail'][name]=float(np.max(np.linalg.norm(data[name][-1]-tail[name],axis=-1)))
    envelope=None
    if problem.envelope is not None:
        aa,bb=problem.envelope
        ell=(X[...,0]/aa)**2+(X[...,1]/bb)**2
        envelope={'normalized_ellipse_radius_squared_max_sample':float(np.max(ell)),
                  'positive_violation_sample':float(max(0,np.max(ell)-1)),
                  'ellipse_major':aa,'ellipse_minor':bb}
    return {'radial_nodes':len(grid.radial),'angular_nodes':len(grid.theta),
        'radial_center_quadrature_order':quadrature_order,
        'integrability_residual_max_sample':Rmax,
        'metric_relative_operator_error_max_sample':float(np.max(op)),
        'E_error_max_sample':float(np.max(abs(A))),'F_over_a_max_sample':float(np.max(abs(off))),
        'G_over_a_squared_error_max_sample':float(np.max(abs(D))),
        'minimum_area_sample':float(np.min(area)),
        'principal_curvature_absolute_max_sample':curvature,
        'induced_Gauss_curvature_min_sample':gauss_min,'induced_Gauss_curvature_max_sample':gauss_max,
        'shape_operator_discriminant_min_before_roundoff_clip':discriminant_min,
        'radial_metric_min_sample':float(np.min(a)),'radial_metric_max_sample':float(np.max(a)),
        'target_Gauss_curvature_min_sample':float(np.min(data['metric']['K'])),
        'target_Gauss_curvature_max_sample':float(np.max(data['metric']['K'])),
        'target_frame_unit_error_max':float(max(np.max(abs(dot(data['frame']['T'],data['frame']['T'])-1)),
                                               np.max(abs(dot(data['frame']['V'],data['frame']['V'])-1)))),
        'target_frame_orthogonality_max':float(np.max(abs(dot(data['frame']['T'],data['frame']['V'])))),
        'target_T_angle_mean_max':float(np.max(np.linalg.norm(data['frame']['T'].mean(axis=1),axis=-1))),
        'primitive_identity_error_max_sample':identity_error,
        'metric_bound_from_sampled_R_not_continuous':2*e+e*e,
        'metric_bound_is_not_a_continuous_certificate':True,
        'position_abs_max_sample':np.max(abs(X),axis=(0,1)).tolist(),
        'position_min_sample':np.min(X,axis=(0,1)).tolist(),
        'position_max_sample':np.max(X,axis=(0,1)).tolist(),
        'signed_side_height_minus_core_width_min_sample':float(np.min(problem.port.side*X[...,2])-problem.port.width),
        'signed_side_height_margin_is_only_sampled':True,
        'height_limit':problem.height_limit,
        'height_positive_violation_sample':float(max(0,np.max(abs(X[...,2]))-problem.height_limit)),
        'center_height_first_last':[float(data['center'][0]),float(data['center'][-1])],
        'ellipse_projection_envelope':envelope,'position_two_jet_endpoint_errors':endpoint,
        'continuous_metric_bound_proved':False,'continuous_shape_bound_proved':False,
        'embedding_proved':False,'whole_surface_reach_proved':False,'task_complete':False}


def primitive_gauss_audit(problem,state,angular_nodes=192,cells=24,order=8):
    gx,gw=leggauss(order);angles=np.array([0.,.71,2.13,3.77,5.41])
    radial=np.array([0.,problem.active_start+.41*(problem.active_end-problem.active_start),problem.seed.length])
    theta=np.arange(angular_nodes)*2*np.pi/angular_nodes
    grid=problem.grid_for(radial,theta);T=problem.frame(state,grid)['T']
    freq=np.fft.fftfreq(angular_nodes)*angular_nodes;coeff=np.fft.fft(T,axis=1)/angular_nodes
    nonzero=freq!=0;coeff[:,nonzero,:]/=(1j*freq[nonzero])[None,:,None];coeff[:,~nonzero,:]=0
    fft_values=np.einsum('rkx,kt->rtx',coeff,np.exp(1j*freq[:,None]*angles)).real
    def integrate(upper,weighted=False):
        if upper==0:return np.zeros((len(radial),3))
        edges=np.linspace(0,upper,cells+1);width=np.diff(edges)/2;mid=(edges[:-1]+edges[1:])/2
        nodes=(mid[:,None]+width[:,None]*gx).ravel();weights=(width[:,None]*gw).ravel()
        values=problem.frame(state,problem.grid_for(radial,nodes))['T']
        if weighted:weights=weights*(2*np.pi-nodes)/(2*np.pi)
        return np.einsum('rtx,t->rx',values,weights)
    mean_primitive=integrate(2*np.pi,True)
    direct=np.stack([integrate(angle)-mean_primitive for angle in angles],axis=1)
    return {'radial_positions':radial.tolist(),'angles':angles.tolist(),'gauss_cells':cells,'gauss_order':order,
        'uniform_spectral_nodes':angular_nodes,
        'primitive_finite_point_difference_max':float(np.max(np.linalg.norm(direct-fft_values,axis=-1))),
        'gauss_full_angle_T_integral_max':float(np.max(np.linalg.norm(integrate(2*np.pi),axis=-1))),
        'fixed_physical_fields':True,'continuous_error_bound_proved':False}


def developer_check():
    checks=[]
    for side,metric_count in [(1,1),(-1,0)]:
        port=EllipticCylinderPort('9/10','18/25','1/50',side)
        seed=NegativeKRadialSeed.from_core(port,Q('11/10'),Q('11/50'))
        problem=FrameCollarProblem(port,seed,radial_free=2,angular_modes=2,metric_free=metric_count,
            ellipse_envelope=(.6,.4),height_limit=.1,radial_nodes=9,angular_nodes=24,radial_quadrature_order=3)
        rng=np.random.default_rng(4149+side);state=rng.normal(size=problem.nunknown)*.015
        direction=rng.normal(size=problem.nunknown);direction/=np.linalg.norm(direction);h=2e-7
        residual,jac,data=problem.residual_and_jacobian(state)
        fd=(problem.residual(state+h*direction)-problem.residual(state-h*direction))/(2*h)
        analytic=jac@direction
        error=float(np.linalg.norm(fd-analytic)/max(1e-30,np.linalg.norm(fd)))
        fixed_metric=None
        if metric_count:
            frozen=FrameCollarProblem(port,seed,radial_free=2,angular_modes=2,
                fixed_metric_coefficients=state[problem.slices['metric']],ellipse_envelope=(.6,.4),height_limit=.1,
                radial_nodes=9,angular_nodes=24,radial_quadrature_order=3)
            metric0=problem.metric(state,problem.radial);metric1=frozen.metric(state[:problem.field_count],problem.radial)
            fixed_metric={'exact_evaluation_match':all(np.array_equal(metric0[k],metric1[k]) for k in ['a','a_s','a_ss']),
                'mathematical_identity_match':problem.metric_model(state)['mathematical_definition_sha256']==
                                              frozen.metric_model(state[:problem.field_count])['mathematical_definition_sha256']}
        refined_grid=problem.grid_for(np.linspace(0,seed.length,17),np.arange(96)*2*np.pi/96)
        audit=audit_geometry(problem,state,refined_grid,quadrature_order=6)
        primitive=primitive_gauss_audit(problem,state,96,12,8)
        entry_rows=[];zero=np.zeros(problem.nunknown)
        for relative in [.01,.005]:
            x=relative*problem.first_segment_length;t=problem.active_start+x
            entry_grid=problem.grid_for(np.array([t]),np.arange(96)*2*np.pi/96)
            entry_frame=problem.frame(zero,entry_grid);entry_metric=problem.metric(zero,np.array([t]))
            RR=(entry_frame['Vtheta']-entry_metric['a_s'][:,None,None]*entry_frame['T']-
                entry_metric['a'][:,None,None]*entry_frame['Ts'])
            expected=problem.entry_c3*x**3*(1-1.5*relative+.6*relative**2)
            entry_rows.append({'distance_over_first_seed_segment':relative,
                'integrability_residual_max':float(np.max(np.linalg.norm(RR,axis=-1))),
                'a_prime_piecewise_polynomial_difference':float(abs(entry_metric['a_s'][0]-expected))})
        ratio=entry_rows[0]['integrability_residual_max']/entry_rows[1]['integrability_residual_max']
        checks.append({'side':side,'metric_design_variables':metric_count,'unknowns':problem.nunknown,
            'residual_entries':len(residual),'directional_jacobian_relative_error':error,
            'unit_frame_error':audit['target_frame_unit_error_max'],
            'orthogonality_error':audit['target_frame_orthogonality_max'],
            'endpoint_two_jet_errors':audit['position_two_jet_endpoint_errors'],
            'fixed_metric_reconstruction':fixed_metric,'primitive_crosscheck':primitive,
            'entry_leading_residual_scaling':entry_rows,'entry_residual_halving_ratio':ratio})
    passed=all(row['directional_jacobian_relative_error']<2e-5 and row['unit_frame_error']<1e-12 and
               row['orthogonality_error']<1e-12 and
               max(row['endpoint_two_jet_errors']['tail'].values())<1e-10 and
               max(row['endpoint_two_jet_errors']['core'].values())<1e-10 and
               8<row['entry_residual_halving_ratio']<32 and
               max(x['a_prime_piecewise_polynomial_difference'] for x in row['entry_leading_residual_scaling'])<1e-12 and
               (row['fixed_metric_reconstruction'] is None or all(row['fixed_metric_reconstruction'].values()))
               for row in checks)
    return {'schema':'orthonormal-frame-collar-development-v1','artificial_inputs_only':True,
        'research_geometry_evaluated':False,'nonlinear_optimization_performed':False,
        'checks':checks,'passed':bool(passed)}


def atomic_save(path,value):
    path.parent.mkdir(parents=True,exist_ok=True);temporary=path.with_suffix('.tmp')
    temporary.write_text(json.dumps(value,indent=2,allow_nan=False)+'\n');temporary.replace(path)


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--major',default='1');p.add_argument('--minor',default='.28');p.add_argument('--half-width',default='.02')
    p.add_argument('--side',type=int,choices=[-1,1],default=1)
    p.add_argument('--length',default='.9');p.add_argument('--cut-radius',default='.22')
    p.add_argument('--core-fraction',default='1/25');p.add_argument('--flat-fraction',default='3/50')
    p.add_argument('--negative-curvature-drop',default='.3')
    p.add_argument('--radial-free',type=int,default=4);p.add_argument('--angular-modes',type=int,default=5)
    p.add_argument('--mode',choices=['fixed','design'],default='fixed');p.add_argument('--metric-free',type=int,default=3)
    p.add_argument('--frozen-metric-from',type=Path)
    p.add_argument('--radial-nodes',type=int,default=29);p.add_argument('--angular-nodes',type=int,default=96)
    p.add_argument('--quadrature-order',type=int,default=4)
    p.add_argument('--audit-radial-nodes',type=int,default=121);p.add_argument('--audit-angular-nodes',type=int,default=384)
    p.add_argument('--height-limit',type=float,default=.45);p.add_argument('--shape-weight',type=float,default=2.)
    p.add_argument('--field-bound',type=float,default=3.);p.add_argument('--metric-log-bound',type=float,default=.5)
    p.add_argument('--max-nfev',type=int,default=200)
    p.add_argument('--checkpoint-every',type=int,default=10);p.add_argument('--checkpoint-seconds',type=float,default=60.)
    p.add_argument('--check-only',action='store_true');p.add_argument('--out',type=Path,required=True)
    args=p.parse_args();started=time.monotonic()
    hashes={name:hashlib.sha256(Path(__file__).with_name(name).read_bytes()).hexdigest()
            for name in ['frame_collar_bvp.py','ellipse_frame_port.py','cosine_connector_radial_seed.py']}
    if args.check_only:
        result=developer_check();result['source_files_sha256']=hashes;atomic_save(args.out,result)
        print(json.dumps({'out':str(args.out),'passed':result['passed']}),flush=True)
        if not result['passed']:raise SystemExit(1)
        return
    if os.environ.get('GITHUB_ACTIONS')!='true' or os.environ.get('GITHUB_REPOSITORY')!='Rogerhu12/math-research-public':
        p.error('actual frame collar solves run only in this public repository Actions')
    if min(args.radial_free,args.angular_modes,args.radial_nodes-2,args.max_nfev,args.checkpoint_every,
           args.field_bound,args.metric_log_bound,args.height_limit,args.quadrature_order)<=0:
        p.error('positive basis sizes, grid dimensions, iteration and checkpoint budgets required')
    if (args.audit_radial_nodes<args.radial_nodes or args.audit_angular_nodes<args.angular_nodes or
        args.audit_angular_nodes%4 or args.shape_weight<0):
        p.error('audit grids must refine collocation, preserve twofold symmetry, and shape weight must be nonnegative')
    if args.mode=='design' and args.frozen_metric_from:p.error('choose metric design OR fixed metric replay')
    if args.mode=='design' and args.metric_free<1:p.error('metric design needs at least one log-radius coefficient')
    port=EllipticCylinderPort(args.major,args.minor,args.half_width,args.side)
    seed=NegativeKRadialSeed.from_core(port,Q(args.length),Q(args.cut_radius),
        {'core_fraction':args.core_fraction,'flat_fraction':args.flat_fraction,
         'negative_curvature_drop':args.negative_curvature_drop})
    fixed=None;frozen_source=None
    if args.frozen_metric_from:
        repo=Path(__file__).resolve().parents[3]
        allowed=[repo/'topics'/'visible-flex-new-mechanism'/'notes']
        if os.environ.get('RUNNER_TEMP'):allowed.append(Path(os.environ['RUNNER_TEMP']))
        if not any(args.frozen_metric_from.resolve().is_relative_to(root.resolve()) for root in allowed):
            p.error('frozen metric input must be a public topic note or current Actions temporary output')
        raw=args.frozen_metric_from.read_bytes();frozen=json.loads(raw)['metric_model']
        mathematical=frozen['mathematical_definition']
        digest=hashlib.sha256(json.dumps(mathematical,sort_keys=True,separators=(',',':')).encode()).hexdigest()
        if digest!=frozen['mathematical_definition_sha256']:
            raise ValueError('frozen metric mathematical identity hash mismatch')
        if frozen['seed']['definition_sha256']!=seed.frozen_definition()['definition_sha256']:
            raise ValueError('frozen metric seed/core identity differs; do not silently redefine g')
        fixed=[float(Q(x)) for x in mathematical['log_basis_coefficients_exact']]
        if (mathematical['log_basis_degree']!=5 or mathematical['log_basis_free_count']!=len(fixed) or
            mathematical.get('log_basis_endpoint_weight')!='16*x^2*(1-x)^2; x is normalized active coordinate'):
            raise ValueError('unsupported frozen metric basis definition')
        frozen_source={'path':str(args.frozen_metric_from),'sha256':hashlib.sha256(raw).hexdigest(),
                       'mathematical_definition_sha256':frozen['mathematical_definition_sha256']}
    problem=FrameCollarProblem(port,seed,args.radial_free,args.angular_modes,
        metric_free=args.metric_free if args.mode=='design' else 0,fixed_metric_coefficients=fixed,
        ellipse_envelope=(port.major,port.minor),height_limit=args.height_limit,shape_weight=args.shape_weight,
        radial_nodes=args.radial_nodes,angular_nodes=args.angular_nodes,radial_quadrature_order=args.quadrature_order)
    initial=np.zeros(problem.nunknown)
    if frozen_source and problem.metric_model(initial)['mathematical_definition_sha256']!=frozen_source['mathematical_definition_sha256']:
        raise ValueError('fixed metric replay changed its exact basis or coefficient identity')
    bounds=np.full(problem.nunknown,args.field_bound)
    if problem.metric_free:bounds[problem.slices['metric']]=args.metric_log_bound
    definition={key:str(value) if isinstance(value,Path) else value for key,value in vars(args).items()}
    checkpoint=args.out.with_name(args.out.stem+'-checkpoint.json');history=[];best={};evaluations=[0];last_save=[0.]
    initial_audit=audit_geometry(problem,initial,problem.grid,quadrature_order=args.quadrature_order)
    def payload(state,status,final=False):
        data=problem.residual_and_jacobian(state)[2]
        out={'schema':'orthonormal-frame-collar-design-v1','status':status,'definition':definition,
            'port_identity':port.port_identity,'port_identity_sha256':port.port_identity_sha256,
            'core_physical_identity':port.identity,'core_physical_identity_sha256':port.identity_sha256,
            'fold':problem.fold,'tail_beta_multiple_of_pi':-port.side,
            'ellipse_opposite_half_reflection':{'position':'(x,y,z) -> (x,y,-z)',
                'scalar_fields':'u -> u, v -> -v, beta -> -beta',
                'accurate_cylinder_and_C2_ports_match':True,
                'cross_half_injectivity_or_reach_proved':False},
            'field_unknown_count':problem.field_count,'metric_design_unknown_count':problem.metric_free,
            'core_port_is_extended_exactly_through_open_buffer':True,
            'active_interval':[problem.active_start,problem.active_end],
            'open_core_length':problem.active_start,'open_flat_tail_length':seed.length-problem.active_end,
            'frame_parameterization':'T=(-sin(theta+u),cos(theta+u),v)/sqrt(1+v^2); V=cos(beta)*N0+sin(beta)*(T cross N0)',
            'field_basis':'clamped degree-five B splines with first/last three coefficients omitted; sin/cos(fold*k*theta)',
            'base_blending':'degree-nine Hermite with third/fourth radial jets zero, plus compact necessary ellipse Cauchy leading terms',
            'entry_cauchy_seed':{'enabled':problem.entry_cauchy,
                'a_prime_cubic_coefficient_numerical':problem.entry_c3,
                'first_seed_segment_length':problem.first_segment_length,
                'compact_entry_length':problem.entry_length,
                'beta_cubic_definition':'side*c3/psi_theta_at_core',
                'u_quartic_definition':'c3*psi_thetatheta_at_core/(4*a0*psi_theta_at_core^2)',
                'full_Cauchy_solution_or_series_not_proved':True,
                'free_fields_still_match_exact_position_two_jet_not_all_higher_Cauchy_orders':True},
            'exact_field_coefficients':[str(Q.from_float(float(x))) for x in state[:problem.field_count]],
            'field_coefficients_binary64':state[:problem.field_count].tolist(),
            'metric_model':problem.metric_model(state),'frozen_metric_source':frozen_source,
            'angular_derivative_method':port.angular_derivative_mode,
            'strong_core_angular_functions_projected_to_free_modes':False,
            'initial_collocation_audit':initial_audit,
            'collocation_audit':audit_geometry(problem,state,problem.grid,data,args.quadrature_order),
            'source_files_sha256':hashes,'github_repository':os.environ.get('GITHUB_REPOSITORY'),
            'github_sha':os.environ.get('GITHUB_SHA'),'github_run_id':os.environ.get('GITHUB_RUN_ID'),
            'evaluations_seen':evaluations[0],'history':history,'elapsed_seconds':time.monotonic()-started,
            'parameter_change_during_design_is_not_fixed_g_refinement':bool(problem.metric_free),
            'continuous_metric_certificate':False,'embedding_proved':False,'whole_surface_reach_proved':False,
            'closed_surface_constructed':False,'task_complete':False}
        if final:
            grid=problem.grid_for(np.linspace(0,seed.length,args.audit_radial_nodes),
                                  np.arange(args.audit_angular_nodes)*2*np.pi/args.audit_angular_nodes)
            fine=problem.geometry(state,grid,quadrature_order=8)
            doubled=problem.grid_for(grid.radial,np.arange(2*args.audit_angular_nodes)*np.pi/args.audit_angular_nodes)
            finer=problem.geometry(state,doubled,quadrature_order=8)
            out['fixed_parameter_audit']=audit_geometry(problem,state,grid,fine,8)
            out['fixed_parameter_double_angle_audit']=audit_geometry(problem,state,doubled,finer,8)
            out['angle_refinement_same_radial_position_difference_max']=float(np.max(np.linalg.norm(fine['X']-finer['X'][:,::2],axis=-1)))
            out['primitive_gauss_crosscheck']=primitive_gauss_audit(problem,state,args.audit_angular_nodes)
            out['interval_certification_not_replaced_by_finite_refinement']=True
        return out
    def objective(state):
        residual,jac,data=problem.residual_and_jacobian(state);evaluations[0]+=1
        cost=float(np.dot(residual,residual)/2)
        if not best or cost<best['cost']:best.update(cost=cost,state=np.array(state,copy=True))
        now=time.monotonic()
        if evaluations[0]==1 or evaluations[0]%args.checkpoint_every==0 or now-last_save[0]>=args.checkpoint_seconds:
            selected=best['state'];audit=audit_geometry(problem,selected,problem.grid,
                problem.residual_and_jacobian(selected)[2],args.quadrature_order)
            entry={'evaluation':evaluations[0],'selected_cost':best['cost'],
                'R_max_sample':audit['integrability_residual_max_sample'],
                'metric_error_sample':audit['metric_relative_operator_error_max_sample'],
                'area_min_sample':audit['minimum_area_sample'],
                'height_violation_sample':audit['height_positive_violation_sample'],
                'ellipse_projection':audit['ellipse_projection_envelope'],'seconds':now-started}
            history.append(entry);atomic_save(checkpoint,payload(selected,'checkpoint_frame_collar_candidate'))
            print(json.dumps(entry),flush=True);last_save[0]=now
        return residual
    result=least_squares(objective,initial,jac=problem.jacobian,bounds=(-bounds,bounds),
        x_scale='jac',max_nfev=args.max_nfev,ftol=1e-11,xtol=1e-11,gtol=1e-11,method='trf')
    objective(result.x);selected=best['state'];report=payload(selected,'finite_frame_collar_candidate',True)
    report['solver']={'success':bool(result.success),'message':str(result.message),'status':int(result.status),
        'nfev':int(result.nfev),'njev':int(result.njev) if result.njev is not None else None,
        'cost':float(result.cost),'selected_cost':best['cost'],'optimality':float(result.optimality),
        'termination_success_is_not_geometric_feasibility':True}
    atomic_save(args.out,report);atomic_save(checkpoint,report)
    print(json.dumps({'out':str(args.out),'audit':report['fixed_parameter_double_angle_audit'],'task_complete':False}),flush=True)


if __name__=='__main__':main()
