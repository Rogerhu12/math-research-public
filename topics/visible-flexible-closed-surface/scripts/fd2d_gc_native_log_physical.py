#!/usr/bin/env python3
"""Floating physical n,m,l and fixed-material access to an actual native field.

This evaluates the same exact shared-Hermite/exponential definition. It does
not evolve a BVP, frame, or position, and its point values are not intervals.
"""
from __future__ import annotations
import json
from pathlib import Path
import numpy as np
from fd2d_gc_native_log_field import NativeLogField,identity,locate_near
from fd2d_balanced_curvature_core import FixedBalancedGeometry,LD,EPS
from fd2d_gc_design_profile import CoastDesignProfile

HERE=Path(__file__).resolve().parent


class PhysicalNativeLogField:
    def __init__(self,manifest):
        self.native=NativeLogField(manifest);self.meta=self.native.meta;self.manifest=Path(manifest)
        self.report_path=locate_near(self.manifest,self.meta['source_report'])
        self.report=json.loads(self.report_path.read_text())
        for row in self.meta['source_inputs']:
            name=Path(row.get('path',row.get('file'))).name
            if name in ('fd2d_gc_design_profile.py','fd2d_partial_return_parameter.py','fd2d_frozen_ellipse_candidate.py'):
                if identity(HERE/name)['sha256']!=row['sha256']:raise ValueError('Bound target source changed')
        source=locate_near(self.report_path,self.meta['target_input'])
        self.profile=CoastDesignProfile(source,reference_T=self.meta['radial_chart']['reference_T'])
        self.profile.set_parameter(self.meta['actual_T'])
        self.geometry=FixedBalancedGeometry()
        if identity(self.geometry.moments_path)['sha256']!=self.meta['initial_geometry']['exact_moments']['sha256']:
            raise ValueError('Exact seed moments do not match the central geometry')
        self.blend_left,self.blend_right=map(LD,self.meta['angular_chart']['blend_interval'])

    def blend(self,x):
        x=np.atleast_1d(np.asarray(x,dtype=LD))
        t=np.clip((x-self.blend_left)/(self.blend_right-self.blend_left),0,1)
        beta=t**3*(10-15*t+6*t*t)
        first=30*t*t*(1-t)**2/(self.blend_right-self.blend_left)
        return beta,first

    def coordinates(self,x,xi):
        xi=np.atleast_1d(np.asarray(xi,dtype=LD));seed=self.geometry.material_coordinate(xi)
        displacement=seed['u']-xi;beta,first=self.blend(x)
        U=xi[None,:]+(1-beta[:,None])*displacement[None,:]
        q=1+(1-beta[:,None])*(seed['u_phi'][None,:]-1)
        Ux=-first[:,None]*displacement[None,:]
        return dict(u=U,q=q,Ux=Ux,beta=beta,beta_x=first)

    def evaluate(self,x,xi):
        """Outer evaluation: field arrays have shape (len(x),len(xi))."""
        x=np.atleast_1d(np.asarray(x,dtype=LD));xi=np.atleast_1d(np.asarray(xi,dtype=LD))
        native=self.native.evaluate(x,xi);chart=self.coordinates(x,xi)
        p=self.profile.jet(np.asarray(x,dtype=float))
        a,ap,app,J=(np.asarray(p[key],dtype=LD)[:,None] for key in ('a','a_s','a_ss','radial_scale'))
        q,Ux=chart['q'],chart['Ux'];v2=1-ap*ap
        if np.any(a<=0) or np.any(J<=0) or np.any(q<=0) or np.any(v2<=0):raise ArithmeticError('Nonpositive physical normalization')
        nr=np.sqrt(v2)/a;chi=-a*app/v2;c=ap/a
        eta,zeta=native['eta'],native['zeta'];positive=np.exp(eta);inverse=np.exp(-eta)
        n,m,l=nr*positive,nr*zeta,nr*inverse*(zeta*zeta+chi)
        nxi=n*native['eta_xi'];mxi=nr*native['zeta_xi']
        lxi=nr*inverse*(2*zeta*native['zeta_xi']-(zeta*zeta+chi)*native['eta_xi'])
        dlognr=c*(chi-1)
        nx=n*(native['eta_x']+J*dlognr);mx=nr*(native['zeta_x']+J*dlognr*zeta)
        out=dict(x=x,xi=xi,physical_s=np.asarray(p['s'],dtype=LD),a=a[:,0],ap=ap[:,0],app=app[:,0],J=J[:,0],
            n=n,m=m,l=l,n_reference=nr,n_xi=nxi,m_xi=mxi,l_xi=lxi,
            n_u=nxi/q,m_u=mxi/q,l_u=lxi/q,
            n_s_material=(nx-(Ux/q)*nxi)/J,m_s_material=(mx-(Ux/q)*mxi)/J,
            n_x_fixed_xi=nx,m_x_fixed_xi=mx,**native,**chart)
        return out

    def inverse_material(self,x,u):
        """Invert U(x,xi)=u at one fixed x; return xi and the numerical residual."""
        if np.ndim(x)!=0:raise ValueError('Fixed-material inverse accepts one radial x')
        u=np.atleast_1d(np.asarray(u,dtype=LD));beta=LD(self.blend(x)[0][0])
        if beta==1:return dict(xi=u.copy(),residual=np.zeros_like(u),iterations=0)
        seed=self.geometry.normal_angle(u)
        if beta==0:
            residual=self.geometry.material_coordinate(seed)['u']-u
            return dict(xi=seed,residual=residual,iterations=0)
        left,right=np.minimum(u,seed),np.maximum(u,seed)
        xi=(1-beta)*seed+beta*u
        tolerance=64*EPS*np.maximum(1,abs(u))
        for iteration in range(40):
            coordinate=self.coordinates(LD(x),xi);residual=coordinate['u'][0]-u
            done=abs(residual)<=tolerance
            if np.all(done):break
            left=np.where((residual<0)&~done,xi,left);right=np.where((residual>0)&~done,xi,right)
            proposed=xi-residual/coordinate['q'][0]
            bad=(proposed<=left)|(proposed>=right)|~np.isfinite(proposed)
            xi=np.where(done,xi,np.where(bad,(left+right)/2,proposed))
        residual=self.coordinates(LD(x),xi)['u'][0]-u
        if np.any(abs(residual)>512*EPS*np.maximum(1,abs(u))):raise ArithmeticError('Material chart inversion did not converge')
        return dict(xi=xi,residual=residual,iterations=iteration+1)

    def evaluate_material(self,x,u):
        """One x, many fixed material u: n/m/l and their u,s derivatives are vectors.

        A fixed-u frame ODE parameterized by x uses J times its original
        physical-s skew matrix. It must not add a moving-angle connection.
        """
        inverse=self.inverse_material(x,u);out=self.evaluate(x,inverse['xi'])
        for key,value in list(out.items()):
            if key!='xi' and isinstance(value,np.ndarray) and value.shape[0]==1:out[key]=value[0]
        out.update(material_u=np.atleast_1d(np.asarray(u,dtype=LD)),material_angle_residual=inverse['residual'],
                   material_inverse_iterations=inverse['iterations'])
        return out
