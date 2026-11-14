#!/usr/bin/env python3
"""Co-design a multi-mode exact saddle core and a circular flat collar.

c1 remains fixed; higher core modes and the positive radial metric can vary
during design. Open exact core and plane-collar intervals are pinned. Every
metric residual is the actual E/F/G error relative to ds^2+a(s)^2 dtheta^2.
The complete field, including the protected central witness, is screened
against a fixed baseline filled projection and a full-height budget.

Only public GitHub Actions may run a nonlinear solve. --check-only is a small
artificial derivative/interface check. Soft geometry penalties are not reach
or embedding certificates. Checkpoints preserve the best objective candidate
at least every ten evaluations or sixty seconds by default.
"""
from __future__ import annotations

import argparse
from math import comb
import hashlib
import json
import os
from pathlib import Path
import time

import numpy as np
from numpy.polynomial import polynomial as poly
from scipy.interpolate import BSpline
from scipy.optimize import least_squares

from core_to_tail_bvp import fourier, SCOEF
from warped_ruled_core_controls import WarpedRuledCoreControls


KEYS={'x':(0,0),'xs':(1,0),'xt':(0,1),'xss':(2,0),'xst':(1,1),'xtt':(0,2)}
ROT=np.array([[0.,1.,0.],[-1.,0.,0.],[0.,0.,1.]])


def rotation(axis,angle,derivative=False):
    c,s=np.cos(angle),np.sin(angle)
    if axis==0:
        return np.array([[0,0,0],[0,-s,-c],[0,c,-s]]) if derivative else np.array([[1,0,0],[0,c,-s],[0,s,c]])
    if axis==1:
        return np.array([[-s,0,c],[0,0,0],[-c,0,-s]]) if derivative else np.array([[c,0,s],[0,1,0],[-s,0,c]])
    return np.array([[-s,-c,0],[c,-s,0],[0,0,0]]) if derivative else np.array([[c,-s,0],[s,c,0],[0,0,1]])


class RadialSpace:
    def __init__(self,count,start,stop,knots=None):
        self.count,self.start,self.stop=int(count),float(start),float(stop)
        self.width=self.stop-self.start
        if self.count<1 or self.width<=0:
            raise ValueError('positive radial dimension and active interval required')
        self.knots=(np.r_[np.zeros(6),np.arange(1,count+1)/(count+1),np.ones(6)]
                    if knots is None else np.asarray(knots,float))
        self.spline=BSpline(self.knots,np.eye(self.count+6),5)

    def evaluate(self,s,order=0):
        z=(np.asarray(s)-self.start)/self.width
        value=self.spline.derivative(order)(np.clip(z,0.,1.))[:,3:-3]/self.width**order
        return np.where(((z>=0)&(z<=1))[:,None],value,0.)

    def collocation(self,order):
        g,_=np.polynomial.legendre.leggauss(order)
        k=np.unique(self.knots)
        z=np.concatenate([(a+b)/2+(b-a)*g/2 for a,b in zip(k[:-1],k[1:])])
        return self.start+self.width*z


class ProjectionPenalty:
    """Distance outside a fixed numerical Jordan polygon, for design only.

    The rigorous baseline Fill and curve-error proof lives in R12/Actions.
    This floating finite-node penalty is never reported as that proof.
    """
    def __init__(self,vertices):
        self.a=np.asarray(vertices,float)[:,:2]
        self.b=np.roll(self.a,-1,axis=0)
        self.v=self.b-self.a
        self.vv=np.sum(self.v*self.v,axis=-1)
        if np.min(self.vv)<=0:
            raise ValueError('projection penalty polygon has a zero-length edge')

    def evaluate(self,points):
        shape=points.shape[:-1];flat=points.reshape(-1,3)[:,:2]
        distances=np.zeros(len(flat));gradient=np.zeros((len(flat),3))
        for first in range(0,len(flat),256):
            p=flat[first:first+256]
            w=p[:,None,:]-self.a[None,:,:]
            t=np.clip(np.sum(w*self.v[None,:,:],axis=-1)/self.vv[None,:],0.,1.)
            delta=w-t[:,:,None]*self.v[None,:,:]
            dist2=np.sum(delta*delta,axis=-1)
            index=np.argmin(dist2,axis=1);rows=np.arange(len(p))
            nearest=delta[rows,index];distance=np.sqrt(dist2[rows,index])
            crosses=(self.a[None,:,1]>p[:,None,1])!=(self.b[None,:,1]>p[:,None,1])
            intercept=np.zeros_like(crosses,dtype=float)
            np.divide((p[:,None,1]-self.a[None,:,1])*self.v[None,:,0],self.v[None,:,1],
                      out=intercept,where=crosses)
            intercept+=self.a[None,:,0]
            inside=np.sum(crosses&(p[:,None,0]<intercept),axis=1)%2==1
            distance=np.where(inside,0.,distance)
            good=(~inside)&(distance>1e-14)
            distances[first:first+len(p)]=distance
            gradient[first:first+len(p),:2]=np.divide(nearest,distance[:,None],
                out=np.zeros_like(nearest),where=good[:,None])
        return distances.reshape(shape),gradient.reshape((*shape,3))


class WarpedCollarProblem:
    def __init__(self,args,frozen=None):
        self.args=args;self.frozen=frozen
        self.radial=RadialSpace(args.radial_free,args.core_width,args.length-args.flat_length)
        self.J,self.K=args.radial_free,2*args.modes+1
        self.nfield=3*self.J*self.K
        self.metric_radial=self.radial
        if frozen is not None:
            old=frozen['configuration']
            for key in ['scale','c1','core_modes','length','core_width','flat_length','cut_radius','port_pose']:
                if old[key]!=getattr(args,key):
                    raise ValueError('frozen design changes metric/boundary parameter '+key)
            self.fixed_core=np.asarray(frozen['design']['core_coefficients'],float)
            self.fixed_metric=np.asarray(frozen['design']['metric_log_coefficients'],float)
            self.fixed_pose=np.asarray(frozen['design']['port_parameters'],float)
            self.metric_radial=RadialSpace(len(self.fixed_metric),args.core_width,args.length-args.flat_length,
                                          frozen['design']['metric_radial_knots'])
        self.nmetric=0 if frozen else self.J
        self.ncontrol=0 if frozen else args.core_modes-1
        self.npose=0 if frozen else (2 if args.port_pose=='canonical' else 6)
        self.metric_slice=slice(self.nfield,self.nfield+self.nmetric)
        self.control_slice=slice(self.metric_slice.stop,self.metric_slice.stop+self.ncontrol)
        self.pose_slice=slice(self.control_slice.stop,self.control_slice.stop+self.npose)
        self.size=self.pose_slice.stop
        baseline=[args.c1]+[0.]*(args.core_modes-1)
        self.baseline_core=WarpedRuledCoreControls(baseline,args.scale,args.core_arc_cells,args.core_quadrature)
        phi=np.arange(args.projection_vertices)*2*np.pi/args.projection_vertices
        self.projection=ProjectionPenalty(self.baseline_core.center(phi)@ROT.T)
        self.baseline_anchor=float(self.baseline_core.anchor)
        self._core_cache=(None,None)
        self._cache=None

    def prepare(self,s,angular):
        s=np.asarray(s,float);theta=np.arange(angular)*2*np.pi/angular
        z=(s-self.args.core_width)/(self.args.length-self.args.flat_length-self.args.core_width)
        width=self.radial.width
        blend=[]
        for k in range(3):
            value=poly.polyval(np.clip(z,0.,1.),poly.polyder(SCOEF,k))/width**k
            if k==0:
                value=np.where(z<=0,0.,np.where(z>=1,1.,value))
            else:
                value=np.where((z>0)&(z<1),value,0.)
            blend.append(value)
        return {'s':s,'theta':theta,'blend':blend,
                'radial':[self.radial.evaluate(s,k) for k in range(3)],
                'metric_radial':[self.metric_radial.evaluate(s,k) for k in range(3)],
                'fourier':[fourier(theta,self.args.modes,k) for k in range(3)]}

    def collocation(self):
        left=np.linspace(0,self.args.core_width,4)
        right=np.linspace(self.args.length-self.args.flat_length,self.args.length,4)
        return np.unique(np.r_[left,self.radial.collocation(self.args.radial_gauss),right])

    def unpack(self,z):
        field=z[:self.nfield].reshape(3,self.J,self.K)
        if self.frozen is None:
            metric=z[self.metric_slice];coeff=np.r_[self.args.c1,z[self.control_slice]];pose=z[self.pose_slice]
        else:
            metric,coeff,pose=self.fixed_metric,self.fixed_core,self.fixed_pose
        return field,metric,coeff,pose

    def core(self,coeff):
        key=tuple(coeff)
        if key!=self._core_cache[0]:
            self._core_cache=(key,WarpedRuledCoreControls(coeff,self.args.scale,
                                self.args.core_arc_cells,self.args.core_quadrature))
        return self._core_cache[1]

    def port_frame(self,pose):
        if self.args.port_pose=='canonical':
            height,phase=pose;C=np.array([0.,0.,height]);Q=rotation(2,phase)
            partials=[(np.array([0.,0.,1.]),np.zeros((3,3))),
                      (np.zeros(3),rotation(2,phase,True))]
        else:
            C=pose[:3];rx,ry,rz=pose[3:]
            X,Y,Z=rotation(0,rx),rotation(1,ry),rotation(2,rz)
            Q=Z@Y@X
            partials=[(np.eye(3)[k],np.zeros((3,3))) for k in range(3)]
            partials.extend([(np.zeros(3),Z@Y@rotation(0,rx,True)),
                             (np.zeros(3),Z@rotation(1,ry,True)@X),
                             (np.zeros(3),rotation(2,rz,True)@Y@X)])
        return C,Q,partials

    def geometry(self,z,grid,parameter_jacobian=False):
        field,alpha,coeff,pose=self.unpack(z)
        core=self.core(coeff);s=grid['s'];theta=grid['theta'];S=grid['blend']
        c=[];d=[];cj=[];dj=[]
        for order in range(3):
            inlet=core.inlet(theta,0.,order)@ROT.T
            c.append(inlet[0]);d.append(inlet[1])
            if parameter_jacobian and self.ncontrol:
                partial=core.inlet_control_jacobian(theta,0.,order)[1:]@ROT.T
                cj.append(partial[:,0]);dj.append(partial[:,1])
        C,Q,pose_partials=self.port_frame(pose)
        er=[np.column_stack((np.sin(theta+k*np.pi/2),-np.cos(theta+k*np.pi/2),np.zeros_like(theta)))
            for k in range(3)]
        e=[value@Q.T for value in er]
        radius=self.args.cut_radius+self.args.length-s
        data={};params={}
        def interpolate(Cjets,Tjets,rd):
            value=Cjets[rd].copy()
            for k in range(rd+1):
                value+=comb(rd,k)*S[k][:,None,None]*(Tjets[rd-k]-Cjets[rd-k])
            return value
        for key,(rd,td) in KEYS.items():
            cjet=[c[td][None,:,:]+s[:,None,None]*d[td][None,:,:],
                  np.broadcast_to(d[td],(len(s),len(theta),3)),np.zeros((len(s),len(theta),3))]
            tjet=[radius[:,None,None]*e[td][None,:,:],
                  np.broadcast_to(-e[td],(len(s),len(theta),3)),np.zeros((len(s),len(theta),3))]
            if td==0:tjet[0]=tjet[0]+C
            base=interpolate(cjet,tjet,rd)
            free=np.einsum('rj,cjk,uk->ruc',grid['radial'][rd],field,grid['fourier'][td])
            data[key]=base+free
            if parameter_jacobian:
                blocks=[]
                for index in range(self.ncontrol):
                    jets=[cj[td][index][None,:,:]+s[:,None,None]*dj[td][index][None,:,:],
                          np.broadcast_to(dj[td][index],(len(s),len(theta),3)),np.zeros_like(base)]
                    blocks.append(interpolate(jets,[np.zeros_like(base)]*3,rd))
                for pc,pq in pose_partials[:self.npose]:
                    ej=er[td]@pq.T
                    jets=[radius[:,None,None]*ej[None,:,:],np.broadcast_to(-ej,base.shape),np.zeros_like(base)]
                    if td==0:jets[0]=jets[0]+pc
                    blocks.append(interpolate([np.zeros_like(base)]*3,jets,rd))
                params[key]=np.stack(blocks,axis=-1) if blocks else np.zeros((*base.shape,0))
        b=self.args.scale;r=np.sqrt(b*b+s*s)
        rj=[r,s/r,b*b/r**3];flat=[radius,-np.ones_like(s),np.zeros_like(s)]
        U=[];V=[]
        for rd in range(3):
            u=rj[rd].copy();v=np.zeros_like(s)
            for k in range(rd+1):
                u-=comb(rd,k)*S[k]*rj[rd-k]
                v+=comb(rd,k)*S[k]*flat[rd-k]
            U.append(u);V.append(v)
        A=[core.q*u+v for u,v in zip(U,V)]
        ff=[mat@alpha for mat in grid['metric_radial']];exp=np.exp(ff[0])
        aa=[A[0]*exp,exp*(A[1]+A[0]*ff[1]),
            exp*(A[2]+2*A[1]*ff[1]+A[0]*(ff[2]+ff[1]**2))]
        data.update(a=aa[0],ap=aa[1],app=aa[2],core=core,pose=pose,
                    core_anchor_shift=float(core.anchor-self.baseline_anchor),
                    metric_q_derivative=exp*U[0],parameter_derivatives=params)
        return data

    def evaluate(self,z,grid):
        if self._cache is not None and self._cache[0] is grid and np.array_equal(self._cache[1],z):
            return self._cache[2]
        d=self.geometry(z,grid)
        A,B,U,V,W=[d[k] for k in ['xs','xt','xss','xst','xtt']]
        E,F,G=[np.sum(x*y,axis=-1) for x,y in [(A,A),(A,B),(B,B)]]
        cross=np.cross(A,B);actual_det=np.sum(cross*cross,axis=-1)
        # A tiny analytic regularization keeps trial penalties finite. Its
        # gradient below differentiates this same formula. Final curvature
        # audits use the unregularized normal and reject tiny-area fields.
        det=actual_det+(1e-12*self.args.scale)**2;area=np.sqrt(det);normal=cross/area[:,:,None]
        ell,mixed,nn=[np.sum(normal*x,axis=-1) for x in [U,V,W]]
        H=(G*ell+E*nn-2*F*mixed)/(2*det);K=(ell*nn-mixed*mixed)/det
        frob=np.sqrt(np.maximum(4*H*H-2*K,0.))
        a=d['a'][:,None]
        metric=np.stack((E-1,np.sqrt(2)*F/a,G/(a*a)-1),axis=-1)
        outside,projection_gradient=self.projection.evaluate(d['x'])
        curvature=self.args.curvature_weight*np.maximum(frob/self.args.curvature_limit-1,0.)
        height=self.args.height_weight*np.maximum(abs(d['x'][:,:,2])-self.args.height_ceiling,0.)/self.args.scale
        projection=self.args.projection_weight*np.maximum(outside-self.args.projection_padding,0.)/self.args.scale
        point=np.concatenate((metric,curvature[:,:,None],height[:,:,None],projection[:,:,None]),axis=-1)
        radius=self.args.radius_weight*np.sqrt(len(grid['theta']))*np.stack(
            (np.maximum(self.args.radius_floor-d['a'],0.),np.maximum(d['a']-self.args.radius_ceiling,0.)),axis=-1)/self.args.scale
        anchor=d['core_anchor_shift'];eps=self.args.anchor_budget
        anchor_res=self.args.anchor_weight*np.array([max(anchor-eps,0.),max(-anchor-eps,0.)])/self.args.scale
        qres=np.array([]) if self.args.q_target is None else np.array([self.args.q_weight*(d['core'].q-self.args.q_target)])
        residual=np.r_[point.ravel(),radius.ravel(),anchor_res,qres]
        d.update(E=E,F=F,G=G,actual_det=actual_det,det=det,area=area,normal=normal,
                 ell=ell,mixed=mixed,nn=nn,H=H,K=K,frob=frob,metric=metric,
                 outside=outside,projection_gradient=projection_gradient,residual=residual)
        self._cache=(grid,np.array(z,copy=True),d)
        return d

    def residual(self,z,grid):
        return self.evaluate(z,grid)['residual']

    def local_gradients(self,d):
        shape=d['x'].shape;zero=np.zeros(shape)
        # Gradients with respect to X, Xs, Xt, Xss, Xst, Xtt and a.
        gradients=[{key:zero.copy() for key in KEYS} for _ in range(6)]
        A,B,U,V,W=[d[k] for k in ['xs','xt','xss','xst','xtt']];a=d['a'][:,None,None]
        gradients[0]['xs']=2*A
        gradients[1]['xs']=np.sqrt(2)*B/a;gradients[1]['xt']=np.sqrt(2)*A/a
        gradients[2]['xt']=2*B/(a*a)
        ar=np.zeros((*d['E'].shape,6))
        ar[:,:,1]=-np.sqrt(2)*d['F']/a[:,:,0]**2;ar[:,:,2]=-2*d['G']/a[:,:,0]**3
        E,F,G,ell,mixed,nn,H,K,det=[d[k] for k in ['E','F','G','ell','mixed','nn','H','K','det']]
        factor=2*K-8*H*H
        qE=(4*H*nn+factor*G)/det;qF=(-8*H*mixed-2*factor*F)/det;qG=(4*H*ell+factor*E)/det
        ql=(4*H*G-2*nn)/det;qm=(-8*H*F+4*mixed)/det;qn=(4*H*E-2*ell)/det
        ng=ql[:,:,None]*U+qm[:,:,None]*V+qn[:,:,None]*W;n=d['normal']
        projected=(ng-n*np.sum(n*ng,axis=-1)[:,:,None])/d['area'][:,:,None]
        active=d['frob']>self.args.curvature_limit
        cf=np.divide(self.args.curvature_weight,2*self.args.curvature_limit*d['frob'],
                     out=np.zeros_like(d['frob']),where=active)[:,:,None]
        gradients[3]['xs']=(2*qE[:,:,None]*A+qF[:,:,None]*B+np.cross(B,projected))*cf
        gradients[3]['xt']=(qF[:,:,None]*A+2*qG[:,:,None]*B+np.cross(projected,A))*cf
        for key,qv in zip(['xss','xst','xtt'],[ql,qm,qn]):gradients[3][key]=qv[:,:,None]*n*cf
        gradients[4]['x'][:,:,2]=self.args.height_weight*np.sign(d['x'][:,:,2])*(abs(d['x'][:,:,2])>self.args.height_ceiling)/self.args.scale
        gradients[5]['x']=self.args.projection_weight*(d['outside']>self.args.projection_padding)[:,:,None]*d['projection_gradient']/self.args.scale
        return gradients,ar

    def jacobian(self,z,grid):
        d=self.evaluate(z,grid);grad,ar=self.local_gradients(d)
        nr,nu=d['E'].shape;jac=np.zeros((nr,nu,6,self.size))
        basis={key:(grid['radial'][rd][:,None,:,None]*grid['fourier'][td][None,:,None,:]).reshape(nr,nu,-1)
               for key,(rd,td) in KEYS.items()}
        nk=self.J*self.K
        for coordinate in range(3):
            sl=slice(coordinate*nk,(coordinate+1)*nk)
            for channel in range(6):
                jac[:,:,channel,sl]=sum(grad[channel][key][:,:,coordinate,None]*basis[key] for key in KEYS)
        if self.nmetric:
            da=d['a'][:,None]*grid['metric_radial'][0]
            jac[:,:,:,self.metric_slice]=ar[:,:,:,None]*da[:,None,None,:]
        dynamic=self.geometry(z,grid,True)['parameter_derivatives']
        ids=np.r_[np.arange(self.control_slice.start,self.control_slice.stop),np.arange(self.pose_slice.start,self.pose_slice.stop)]
        for channel in range(6):
            for offset,index in enumerate(ids):
                jac[:,:,channel,index]=sum(np.sum(grad[channel][key]*dynamic[key][:,:,:,offset],axis=-1) for key in KEYS)
        if self.ncontrol:
            da=d['metric_q_derivative'][:,None]*d['core'].q_controls[None,1:]
            jac[:,:,:,self.control_slice]+=ar[:,:,:,None]*da[:,None,None,:]
        radius=np.zeros((nr,2,self.size));fac=self.args.radius_weight*np.sqrt(nu)/self.args.scale
        apart=np.zeros((nr,self.size))
        if self.nmetric:apart[:,self.metric_slice]=d['a'][:,None]*grid['metric_radial'][0]
        if self.ncontrol:apart[:,self.control_slice]=d['metric_q_derivative'][:,None]*d['core'].q_controls[None,1:]
        radius[:,0]=-fac*(d['a']<self.args.radius_floor)[:,None]*apart
        radius[:,1]=fac*(d['a']>self.args.radius_ceiling)[:,None]*apart
        extra=np.zeros((2+(self.args.q_target is not None),self.size))
        if self.ncontrol:
            value=d['core'].anchor_controls[1:]*self.args.anchor_weight/self.args.scale
            extra[0,self.control_slice]=value*(d['core_anchor_shift']>self.args.anchor_budget)
            extra[1,self.control_slice]=-value*(d['core_anchor_shift']<-self.args.anchor_budget)
            if self.args.q_target is not None:extra[2,self.control_slice]=self.args.q_weight*d['core'].q_controls[1:]
        return np.vstack((jac.reshape(-1,self.size),radius.reshape(-1,self.size),extra))

    def seed(self,grid,warm=None):
        z=np.zeros(self.size)
        if self.frozen is None:
            higher=[float(x) for x in self.args.core_higher.split(',')] if self.args.core_higher else []
            if len(higher)>self.ncontrol:raise ValueError('too many higher core controls')
            z[self.control_slice]=np.r_[higher,np.zeros(self.ncontrol-len(higher))]
            z[self.pose_slice]=([self.args.cap_height,0.] if self.args.port_pose=='canonical' else
                                [0.,0.,self.args.cap_height,0.,0.,0.])
            if self.args.seed_metric=='average-g':
                d=self.geometry(z,grid);mean=np.mean(np.sum(d['xt']**2,axis=-1),axis=1)
                target=np.maximum(np.sqrt(mean),self.args.radius_floor)
                desired=np.log(target/d['a'])
                z[self.metric_slice]=np.clip(np.linalg.lstsq(grid['metric_radial'][0],desired,rcond=None)[0],
                                             -self.args.metric_coefficient_bound,self.args.metric_coefficient_bound)
        if warm is not None:
            for key in ['scale','c1','core_modes','length','core_width','flat_length','cut_radius','port_pose']:
                if warm['configuration'][key]!=getattr(self.args,key):
                    raise ValueError('warm candidate changes a geometric or metric identity parameter '+key)
            old=warm['discretization'];oldj=old['radial_free'];oldk=2*old['modes']+1
            oldfield=np.asarray(warm['design']['field_coefficients']).reshape(3,oldj,oldk)
            oldspace=RadialSpace(oldj,self.args.core_width,self.args.length-self.args.flat_length,old['radial_knots'])
            s=np.linspace(self.args.core_width,self.args.length-self.args.flat_length,max(101,8*(oldj+self.J)))
            transfer=np.linalg.lstsq(self.radial.evaluate(s),oldspace.evaluate(s),rcond=None)[0]
            out=np.zeros((3,self.J,self.K));keep=min(oldk,self.K)
            out[:,:,:keep]=np.einsum('ij,cjk->cik',transfer,oldfield[:,:,:keep])
            z[:self.nfield]=out.ravel()
            if self.frozen is None:
                if oldj!=self.J or len(warm['design']['core_coefficients'])!=self.args.core_modes:
                    raise ValueError('design warm start changes metric/core representation; freeze first or project explicitly')
                z[self.metric_slice]=warm['design']['metric_log_coefficients']
                z[self.control_slice]=warm['design']['core_coefficients'][1:]
                z[self.pose_slice]=warm['design']['port_parameters']
        return z

    def bounds(self):
        lower=np.full(self.size,-self.args.field_coefficient_bound*self.args.scale)
        upper=-lower
        if self.nmetric:
            lower[self.metric_slice]=-self.args.metric_coefficient_bound;upper[self.metric_slice]=self.args.metric_coefficient_bound
        if self.ncontrol:
            lower[self.control_slice]=-self.args.core_control_bound;upper[self.control_slice]=self.args.core_control_bound
        if self.npose:
            if self.args.port_pose=='canonical':
                lower[self.pose_slice]=[self.args.cap_height_min,-np.pi]
                upper[self.pose_slice]=[self.args.cap_height_max,np.pi]
            else:
                lower[self.pose_slice]=[-self.args.port_offset_bound,-self.args.port_offset_bound,self.args.cap_height_min,
                                        -self.args.port_tilt_bound,-self.args.port_tilt_bound,-np.pi]
                upper[self.pose_slice]=[self.args.port_offset_bound,self.args.port_offset_bound,self.args.cap_height_max,
                                        self.args.port_tilt_bound,self.args.port_tilt_bound,np.pi]
        return lower,upper

    def audit(self,z,grid):
        d=self.evaluate(z,grid);m=d['metric'];aa,bb,cc=m[:,:,0],m[:,:,1]/np.sqrt(2),m[:,:,2]
        disc=np.sqrt((aa-cc)**2+4*bb*bb);metric=float(np.max(np.maximum(abs(aa+cc+disc),abs(aa+cc-disc))/2))
        area=np.sqrt(d['actual_det']);regular=bool(np.min(area)>1e-10*self.args.scale)
        principal=None;frob=None;actual_K=None
        if regular:
            normal=np.cross(d['xs'],d['xt'])/area[:,:,None]
            ell,mixed,nn=[np.sum(normal*d[key],axis=-1) for key in ['xss','xst','xtt']]
            H=(d['G']*ell+d['E']*nn-2*d['F']*mixed)/(2*d['actual_det'])
            K=(ell*nn-mixed*mixed)/d['actual_det']
            principal=float(np.max(abs(H)+np.sqrt(np.maximum(H*H-K,0.))))
            frob=float(np.max(np.sqrt(np.maximum(4*H*H-2*K,0.))))
            actual_K=[float(np.min(K)),float(np.max(K))]
        return {'radial_points':len(grid['s']),'angular_points':len(grid['theta']),
                'relative_metric_operator_sample_max':metric,'E_error_sample_max':float(np.max(abs(aa))),
                'F_normalized_error_sample_max':float(np.max(abs(bb))),'G_error_sample_max':float(np.max(abs(cc))),
                'relative_metric_frobenius_rms':float(np.sqrt(np.mean(aa*aa+2*bb*bb+cc*cc))),
                'min_area_density_sample':float(np.min(area)),'area_resolved_for_true_curvature':regular,
                'actual_principal_curvature_abs_sample_max':principal,'actual_shape_frobenius_sample_max':frob,
                'actual_Gauss_curvature_sample_range':actual_K,
                'target_intrinsic_K_sample_range':[float(np.min(-d['app']/d['a'])),float(np.max(-d['app']/d['a']))],
                'radius_range':[float(np.min(d['a'])),float(np.max(d['a']))],
                'height_absolute_sample_max':float(np.max(abs(d['x'][:,:,2]))),
                'outside_baseline_polygon_distance_sample_max':float(np.max(d['outside'])),
                'projection_padding':self.args.projection_padding,'core_anchor_shift':d['core_anchor_shift'],
                'core_anchor_budget':self.args.anchor_budget,'q_numeric':float(d['core'].q),
                'q_target_residual':None if self.args.q_target is None else float(d['core'].q-self.args.q_target),
                'upper_band_coordinate_min':d['x'].min(axis=(0,1)).tolist(),
                'upper_band_coordinate_max':d['x'].max(axis=(0,1)).tolist(),
                'continuous_metric_bound':False,'projection_certificate':False,'global_embedding_proved':False,
                'core_updated_parameters_geometry_certified':False,'whole_closed_surface_reach_proved':False,
                'soft_shape_penalty_is_not_reach':True,'task_complete':False}

    def design_record(self,z):
        field,alpha,coeff,pose=self.unpack(z);core=self.core(coeff);C,Q,_=self.port_frame(pose)
        return {'field_coefficients':field.ravel().tolist(),'metric_log_coefficients':alpha.tolist(),
                'metric_radial_knots':self.metric_radial.knots.tolist(),'core_coefficients':coeff.tolist(),
                'core_identity':core.identity(),'port_parameters':pose.tolist(),'port_center':C.tolist(),
                'port_frame':Q.tolist(),'port_rotation_axis':(Q@np.array([0.,0.,1.])).tolist(),
                'core_uniform_ambient_rotation':ROT.tolist(),
                'metric_definition':'a=(q*(1-S)*sqrt(b^2+s^2)+S*(rc+L-s))*exp(sum(alpha_j B_j)); radial only',
                'open_accurate_core_interval':[0.,self.args.core_width],
                'open_flat_collar_interval':[self.args.length-self.args.flat_length,self.args.length],
                'final_fixed_metric_stage':self.frozen is not None,
                'parameters_are_not_refitted_by_audit':True}


def configuration(args):
    return {key:str(value) if isinstance(value,Path) else value for key,value in vars(args).items()}


def endpoint_check(problem,z):
    a=problem.args
    s=np.array([0.,a.core_width/2,a.core_width,a.length-a.flat_length,a.length-a.flat_length/2,a.length])
    grid=problem.prepare(s,32);data=problem.geometry(z,grid)
    _,_,coeff,pose=problem.unpack(z);core=problem.core(coeff);C,Q,_=problem.port_frame(pose)
    errors={}
    for key,(rd,td) in KEYS.items():
        expected=np.empty_like(data[key])
        for j,ss in enumerate(s):
            if j<3:expected[j]=core.inlet(grid['theta'],ss,td)[rd]@ROT.T
            else:
                theta=grid['theta']
                e=np.column_stack((np.sin(theta+td*np.pi/2),-np.cos(theta+td*np.pi/2),np.zeros_like(theta)))@Q.T
                expected[j]=((a.cut_radius+a.length-ss)*e+(C if td==0 else 0) if rd==0 else
                             -e if rd==1 else np.zeros_like(e))
        errors[key]=float(np.max(abs(data[key]-expected)))
    return errors


def check_only(args):
    # The CLI overrides research defaults with one small artificial case.
    args=argparse.Namespace(**vars(args));args.c1=.11;args.core_higher='.017,-.006,.0025';args.core_modes=4
    args.radial_free=2;args.modes=3;args.angular=24;args.radial_gauss=3
    args.core_arc_cells=48;args.core_quadrature=12;args.projection_vertices=48
    args.curvature_weight=.02;args.height_ceiling=1.1;args.anchor_budget=.0001;args.q_target=3.
    problem=WarpedCollarProblem(args);grid=problem.prepare(np.linspace(0,args.length,13),24)
    z=problem.seed(grid);rng=np.random.default_rng(815210)
    z[:problem.nfield]+=rng.normal(size=problem.nfield)*.002
    errors=endpoint_check(problem,z)
    jac=problem.jacobian(z,grid);checks=[]
    for mask in ['all','field','metric','core','pose']:
        direction=rng.normal(size=problem.size)
        if mask!='all':
            keep={'field':slice(0,problem.nfield),'metric':problem.metric_slice,'core':problem.control_slice,'pose':problem.pose_slice}[mask]
            temp=np.zeros(problem.size);temp[keep]=direction[keep];direction=temp
        direction/=np.linalg.norm(direction);eps=2e-7
        fd=(problem.residual(z+eps*direction,grid)-problem.residual(z-eps*direction,grid))/(2*eps)
        relative=float(np.linalg.norm(fd-jac@direction)/max(np.linalg.norm(fd),1e-30))
        checks.append({'variables':mask,'relative_error':relative})
    g=problem.geometry(z,grid)
    metric_end=max(abs(g['a'][0]-g['core'].metric(0)[0]),abs(g['ap'][0]),
                   abs(g['app'][0]-g['core'].metric(0)[2]),abs(g['a'][-1]-args.cut_radius),
                   abs(g['ap'][-1]+1),abs(g['app'][-1]))
    report={'schema':'warped-collar-design-development-check-v1','development_check_only':True,
            'research_scan_or_nonlinear_solve_performed':False,'artificial_configuration':configuration(args),
            'complete_position_second_jet_errors_on_open_pieces':errors,
            'metric_endpoint_second_jet_error':float(metric_end),'jacobian_directional_checks':checks,
            'artificial_min_area':problem.audit(z,grid)['min_area_density_sample'],
            'unknown_count':problem.size,'residual_count':len(problem.residual(z,grid))}
    # Freezing carries the entire old radial metric basis, not a new angular
    # average of the refined trial field. A richer field space changes only X.
    saved={'configuration':configuration(args),'design':problem.design_record(z),
           'discretization':{'radial_free':problem.J,'modes':args.modes,'radial_knots':problem.radial.knots.tolist()}}
    refined=argparse.Namespace(**vars(args));refined.radial_free=5;refined.modes=5
    frozen=WarpedCollarProblem(refined,saved)
    dense=np.linspace(0,args.length,43)
    oldgrid=problem.prepare(dense,32);newgrid=frozen.prepare(dense,32)
    warm=frozen.seed(newgrid,saved)
    go=problem.geometry(z,oldgrid);gn=frozen.geometry(warm,newgrid)
    metric_freeze=max(float(np.max(abs(go[key]-gn[key]))) for key in ['a','ap','app'])
    field_transfer=max(float(np.max(abs(go[key]-gn[key]))) for key in KEYS)
    report['frozen_metric_complete_two_jet_transfer_error']=metric_freeze
    report['nested_field_transfer_complete_two_jet_error']=field_transfer
    report['frozen_stage_metric_core_pose_unknown_counts']=[frozen.nmetric,frozen.ncontrol,frozen.npose]
    report['passed']=bool(max(errors.values())<1e-10 and metric_end<1e-10 and max(x['relative_error'] for x in checks)<3e-5)
    report['passed']=bool(report['passed'] and metric_freeze<1e-12 and field_transfer<1e-9)
    return report


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--c1',type=float,default=.8);p.add_argument('--core-modes',type=int,default=4)
    p.add_argument('--core-higher',default='');p.add_argument('--core-control-bound',type=float,default=.08)
    p.add_argument('--scale',type=float,default=1.);p.add_argument('--core-width',type=float,default=.05)
    p.add_argument('--length',type=float,default=3.6);p.add_argument('--flat-length',type=float,default=.15)
    p.add_argument('--cut-radius',type=float,default=.9);p.add_argument('--cap-height',type=float,default=1.4)
    p.add_argument('--cap-height-min',type=float,default=.5);p.add_argument('--cap-height-max',type=float,default=1.5)
    p.add_argument('--port-pose',choices=['canonical','rigid'],default='canonical')
    p.add_argument('--port-offset-bound',type=float,default=.3);p.add_argument('--port-tilt-bound',type=float,default=.3)
    p.add_argument('--height-ceiling',type=float,default=1.5);p.add_argument('--height-weight',type=float,default=1.)
    p.add_argument('--projection-padding',type=float,default=.05);p.add_argument('--projection-weight',type=float,default=1.)
    p.add_argument('--projection-vertices',type=int,default=384)
    p.add_argument('--anchor-budget',type=float,default=.04);p.add_argument('--anchor-weight',type=float,default=3.)
    p.add_argument('--curvature-limit',type=float,default=4.8);p.add_argument('--curvature-weight',type=float,default=.02)
    p.add_argument('--radius-floor',type=float,default=.7);p.add_argument('--radius-ceiling',type=float,default=3.5)
    p.add_argument('--radius-weight',type=float,default=10.)
    p.add_argument('--metric-coefficient-bound',type=float,default=3.);p.add_argument('--field-coefficient-bound',type=float,default=5.)
    p.add_argument('--q-target',type=float);p.add_argument('--q-weight',type=float,default=1.)
    p.add_argument('--seed-metric',choices=['average-g','blend'],default='average-g')
    p.add_argument('--radial-free',type=int,default=5);p.add_argument('--modes',type=int,default=8)
    p.add_argument('--angular',type=int,default=64);p.add_argument('--radial-gauss',type=int,default=5)
    p.add_argument('--core-arc-cells',type=int,default=192);p.add_argument('--core-quadrature',type=int,default=16)
    p.add_argument('--max-nfev',type=int,default=150)
    p.add_argument('--checkpoint-every',type=int,default=10);p.add_argument('--checkpoint-seconds',type=float,default=60.)
    p.add_argument('--warm',type=Path);p.add_argument('--freeze-design',type=Path)
    p.add_argument('--check-only',action='store_true');p.add_argument('--out',type=Path,required=True)
    args=p.parse_args()
    if args.check_only:
        result=check_only(args);result['source_sha256']=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
        args.out.parent.mkdir(parents=True,exist_ok=True);args.out.write_text(json.dumps(result,indent=2,allow_nan=False)+'\n')
        print(json.dumps({'passed':result['passed'],'checks':result['jacobian_directional_checks']}),flush=True)
        if not result['passed']:raise SystemExit(1)
        return
    if os.environ.get('GITHUB_ACTIONS')!='true' or os.environ.get('GITHUB_REPOSITORY')!='Rogerhu12/math-research-public':
        p.error('Nonlinear solves run in this public repository Actions; use --check-only locally')
    if not (args.scale>0 and 0<args.core_width<args.length-args.flat_length<args.length and args.cut_radius>0):
        p.error('need positive scale/core/flat/radius and a nonempty active interval')
    if args.core_modes<2 or args.angular<4*args.modes+4 or args.radial_free<1 or args.checkpoint_every<1:
        p.error('invalid core/trial dimensions or checkpoint interval')
    frozen=json.loads(args.freeze_design.read_text()) if args.freeze_design else None
    warm=json.loads(args.warm.read_text()) if args.warm else frozen
    problem=WarpedCollarProblem(args,frozen);grid=problem.prepare(problem.collocation(),args.angular)
    seed=problem.seed(grid,warm);lower,upper=problem.bounds();seed=np.maximum(lower+1e-12,np.minimum(upper-1e-12,seed))
    started=time.monotonic();last_saved=[0.];count=[0];best={'cost':np.inf};history=[]
    checkpoint=args.out.with_name(args.out.stem+'-checkpoint.json')
    sources=['warped_core_collar_design.py','warped_ruled_core_controls.py','core_to_tail_bvp.py']
    hashes={name:hashlib.sha256(Path(__file__).with_name(name).read_bytes()).hexdigest() for name in sources}
    def payload(z,status,solver=None,fine=False):
        audits=[problem.audit(z,grid)]
        if fine:
            for nr,nt in [(81,128),(161,256)]:
                audits.append(problem.audit(z,problem.prepare(np.linspace(0,args.length,nr),nt)))
        return {'schema':'warped-core-collar-design-v1','status':status,'configuration':configuration(args),
                'source_sha256':hashes,'github_repository':os.environ.get('GITHUB_REPOSITORY'),
                'github_sha':os.environ.get('GITHUB_SHA'),'github_run_id':os.environ.get('GITHUB_RUN_ID'),
                'discretization':{'radial_free':problem.J,'modes':args.modes,'angular_basis':'material',
                                  'radial_knots':problem.radial.knots.tolist(),'unknowns':problem.size},
                'design':problem.design_record(z),'audits':audits,'solver':solver,
                'conditional_phase_family':{'construction':'ambient rotation around the upper cap axis after material theta translation',
                                            'canonical_rotation_range':[0.,float(np.pi/3)],
                                            'requires_static_exact_radial_metric_and_global_embedding':True},
                'evaluations_seen':count[0],'history':history,'elapsed_seconds':time.monotonic()-started,
                'claim':{'fixed_complete_metric':frozen is not None,'fixed_metric_refinement_demonstrated':False,
                         'canonical_phase_axis':args.port_pose=='canonical','updated_core_geometry_certified':False,
                         'closed_embedded_family':False,'held_displacement_certified':False,'reach_certified':False,
                         'soft_penalties_are_not_certificates':True,'task_complete':False}}
    def save(path,value):
        path.parent.mkdir(parents=True,exist_ok=True);tmp=path.with_suffix('.tmp')
        tmp.write_text(json.dumps(value,indent=2,allow_nan=False)+'\n');tmp.replace(path)
    def fun(z):
        rr=problem.residual(z,grid);count[0]+=1;cost=float(rr@rr)/2
        if cost<best['cost']:best.update(cost=cost,z=np.array(z,copy=True))
        now=time.monotonic()
        if count[0]==1 or count[0]%args.checkpoint_every==0 or now-last_saved[0]>=args.checkpoint_seconds:
            a=problem.audit(best['z'],grid)
            entry={'evaluation':count[0],'best_cost':best['cost'],'metric_max':a['relative_metric_operator_sample_max'],
                   'shape_frobenius':a['actual_shape_frobenius_sample_max'],'projection_outside':a['outside_baseline_polygon_distance_sample_max'],
                   'height_max':a['height_absolute_sample_max'],'anchor_shift':a['core_anchor_shift'],'seconds':now-started}
            history.append(entry);save(checkpoint,payload(best['z'],'checkpoint_best_objective'))
            print(json.dumps(entry),flush=True);last_saved[0]=now
        return rr
    initial=problem.audit(seed,grid)
    result=least_squares(fun,seed,jac=lambda z:problem.jacobian(z,grid),bounds=(lower,upper),
                         x_scale='jac',max_nfev=args.max_nfev,ftol=2e-10,xtol=2e-10,gtol=2e-10)
    chosen=best['z'] if best['cost']<result.cost else result.x
    solver={'success':bool(result.success),'status':int(result.status),'message':str(result.message),
            'nfev':int(result.nfev),'njev':int(result.njev),'cost':float(result.cost),'optimality':float(result.optimality),
            'saved_best_cost':best['cost'],'chosen_best_objective_not_assumed_metric_feasible':True}
    report=payload(chosen,'finite_design_candidate' if frozen is None else 'finite_frozen_metric_candidate',solver,True)
    report['initial_audit']=initial;report['open_piece_jet_audit']=endpoint_check(problem,chosen)
    save(args.out,report);save(checkpoint,report)
    print(json.dumps({'out':str(args.out),'metric':report['audits'][-1]['relative_metric_operator_sample_max'],
                      'task_complete':False}),flush=True)


if __name__=='__main__':
    main()
