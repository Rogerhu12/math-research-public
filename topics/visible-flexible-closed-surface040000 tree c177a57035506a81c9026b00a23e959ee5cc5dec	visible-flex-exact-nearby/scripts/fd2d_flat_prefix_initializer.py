"""Consume the closed positive-n flat-prefix IVP as an INITIAL GUESS only.

The source has accepted-node finite Fourier n,m and their actual projected
RHS.  Shared-node cubic Hermite interpolation here is an explicit initial
guess, not the original DOP853 dense polynomial or a metric certificate.
No extrapolation or interpretation of phi as material u is automatic.
"""
from __future__ import annotations
import gzip
import hashlib
import io
import json
from pathlib import Path
import numpy as np
from scipy.interpolate import CubicHermiteSpline
from fd2d_balanced_curvature_core import FixedBalancedGeometry
from fd2d_frozen_ellipse_candidate import Candidate


class ActualFlatPrefixInitializer:
    def __init__(self,trajectory,candidate,*,geometry=None):
        self.trajectory_path=Path(trajectory)
        self.candidate_path=Path(candidate)
        if self.trajectory_path.suffix=='.gz':
            raw=gzip.decompress(self.trajectory_path.read_bytes())
            source=np.load(io.BytesIO(raw),allow_pickle=False)
        else:
            source=np.load(self.trajectory_path,allow_pickle=False)
        self.nodes=np.asarray(source['s'],float)
        if np.any(np.diff(self.nodes)<=0):
            raise ValueError('The actual accepted nodes must be strictly ordered')
        self.candidate_sha256=hashlib.sha256(self.candidate_path.read_bytes()).hexdigest()
        if self.candidate_sha256!=str(source['candidate_sha256']):
            raise ValueError('The initializer binds a different physical candidate')
        if str(source['fixed_chart'])!='balanced_seed_normal_phi':
            raise ValueError('Unknown stored angular coordinate')
        self.T=float(source['T'])
        self.candidate=Candidate(json.loads(self.candidate_path.read_text()))
        self.geometry=FixedBalancedGeometry() if geometry is None else geometry
        self.frequencies=np.asarray(source['frequencies'],np.longdouble)
        self.n_polynomial=CubicHermiteSpline(self.nodes,np.asarray(source['n_phi_cos'],float),
            np.asarray(source['n_s_phi_cos'],float),axis=0,extrapolate=False)
        self.m_polynomial=CubicHermiteSpline(self.nodes,np.asarray(source['m_phi_sin'],float),
            np.asarray(source['m_s_phi_sin'],float),axis=0,extrapolate=False)
        self.interval=(float(self.nodes[0]),float(self.nodes[-1]))
        self.source_scope='Actual finite IVP nodes; this shared-node interpolation is only for a BVP initial guess'

    def evaluate_phi(self,s,phi):
        s,phi=np.broadcast_arrays(np.asarray(s,float),np.asarray(phi,np.longdouble))
        if np.any(s<self.interval[0]) or np.any(s>self.interval[1]):
            raise ValueError('Outside the closed actual IVP interval; blend or extrapolate explicitly in the caller')
        shape=s.shape
        sf,pf=s.ravel(),phi.ravel()
        result={key:np.empty(len(sf),float) for key in ('l','m','n','m_s','n_s','l_u','m_u','n_u','phi','u')}
        for start in range(0,len(sf),256):
            stop=min(start+256,len(sf))
            ss,pp=sf[start:stop],pf[start:stop]
            nc=np.asarray(self.n_polynomial(ss),np.longdouble)
            mc=np.asarray(self.m_polynomial(ss),np.longdouble)
            nd=np.asarray(self.n_polynomial(ss,1),np.longdouble)
            md=np.asarray(self.m_polynomial(ss,1),np.longdouble)
            angle=pp[:,None]*self.frequencies[None,:]
            cs,sn=np.cos(angle),np.sin(angle)
            n=np.sum(nc*cs,axis=1)
            m=np.sum(mc*sn[:,1:],axis=1)
            ns=np.sum(nd*cs,axis=1)
            ms=np.sum(md*sn[:,1:],axis=1)
            nphi=-np.sum(nc*sn*self.frequencies,axis=1)
            mphi=np.sum(mc*cs[:,1:]*self.frequencies[None,1:],axis=1)
            coordinate=self.geometry.material_coordinate(pp)
            nu=nphi/coordinate['u_phi']
            mu=mphi/coordinate['u_phi']
            aa,ap,app=self.candidate.profile(ss)
            K=-np.asarray(app,np.longdouble)/np.asarray(aa,np.longdouble)
            if np.any(n<=0):
                raise ArithmeticError('The interpolated positive-n initializer left its coordinate chart')
            l=(K+m*m)/n
            lu=(2*m*mu-l*nu)/n
            for key,value in dict(l=l,m=m,n=n,m_s=ms,n_s=ns,l_u=lu,m_u=mu,n_u=nu,phi=pp,u=coordinate['u']).items():
                result[key][start:stop]=value
        return {key:value.reshape(shape) for key,value in result.items()}

    def evaluate_material(self,s,u):
        s,u=np.broadcast_arrays(np.asarray(s,float),np.asarray(u,np.longdouble))
        return self.evaluate_phi(s,self.geometry.normal_angle(u))

    def definition(self):
        return dict(interval=list(self.interval),physical_T=self.T,candidate_sha256=self.candidate_sha256,
                    angular_coordinate='fixed seed phi; material u=U_seed(phi)',
                    radial_coordinate='physical s; equals reference x at T=.02',
                    representation='n,m real finite Fourier in phi; shared-node cubic Hermite in physical s; l=(K+m^2)/n',
                    derivative_scope='shared-node interpolant derivatives, with source projected RHS at nodes',
                    initializer_only=True,extrapolation=False)
