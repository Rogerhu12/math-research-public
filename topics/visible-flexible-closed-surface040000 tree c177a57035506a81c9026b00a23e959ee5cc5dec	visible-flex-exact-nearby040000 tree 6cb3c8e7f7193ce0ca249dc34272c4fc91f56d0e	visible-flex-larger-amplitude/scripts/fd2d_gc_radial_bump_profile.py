#!/usr/bin/env python3
"""Physical radial metric design by compact C4 bumps on a fixed s domain.

This changes g=ds^2+a(s)^2 du^2 when delta changes. It is not a clock or a
same-g refinement. The central cylinder and an open cut neighborhood are
unchanged. No second-form component is divided here.
"""
from __future__ import annotations
from fractions import Fraction
from math import comb, factorial
from pathlib import Path
import hashlib
import json
import numpy as np
from fd2d_frozen_ellipse_candidate import Candidate


def identity(path):
    p=Path(path);b=p.read_bytes()
    return dict(path=str(p.resolve()),bytes=len(b),sha256=hashlib.sha256(b).hexdigest())


def rational(value):
    if isinstance(value,Fraction):
        return value
    if isinstance(value,(float,np.floating)):
        return Fraction.from_float(float(value))
    return Fraction(str(value))


def compact_basis_jets(s,supports,derivative=0):
    """1024*q^5*(1-q)^5 on each support, zero outside; derivative <=4.

    Formula uses the product rule in factored form. No cancellation between
    large endpoint polynomial coefficients is needed to get the zero jets.
    """
    if derivative not in range(5):
        raise ValueError('This C4 representation exposes derivatives 0 through 4')
    s=np.atleast_1d(np.asarray(s,float));supports=np.asarray(supports,float)
    width=supports[:,1]-supports[:,0]
    q=(s[...,None]-supports[:,0])/width
    inside=(q>0)&(q<1);t=np.clip(q,0.,1.)
    value=np.zeros_like(q)
    for k in range(derivative+1):
        j=derivative-k
        factor=comb(derivative,k)*factorial(5)//factorial(5-k)
        factor*=((-1)**j)*factorial(5)//factorial(5-j)
        value+=factor*t**(5-k)*(1-t)**(5-j)
    return np.where(inside,1024*value/width**derivative,0.)


class RadialBumpProfile:
    """The supplied base candidate, fixed physical s, and J physical deltas."""
    def __init__(self,source,*,count=7,supports=None,collar_guard=.02,coefficients=None):
        self.source=Path(source);self.source_identity=identity(self.source)
        self.base=Candidate(json.loads(self.source.read_text()))
        self.ellipse,self.a0=self.base.ellipse,self.base.a0
        self.end,self.segments=self.base.end,self.base.segments
        central=self.segments[0]
        if central.get('label')!='central_cylinder' or central['kind']!='coast' or central['p0']!=0.:
            raise ValueError('An actual exact initial cylinder must be identified')
        self.central_end=float(central['s1']);self.collar_guard=float(collar_guard)
        if not 0<self.collar_guard<(self.end-self.central_end)/4:
            raise ValueError('The protected neighborhoods must leave an interior design interval')
        left=self.central_end+self.collar_guard;right=self.end-self.collar_guard
        if supports is None:
            if int(count)!=count or count<1:
                raise ValueError('A positive integer number of physical profile parameters is required')
            knots=np.linspace(left,right,int(count)+4)
            supports=np.array([[knots[j],knots[j+4]] for j in range(int(count))])
        self.supports=np.asarray(supports,float)
        if self.supports.ndim!=2 or self.supports.shape[1]!=2 or len(self.supports)==0:
            raise ValueError('Supports must be a nonempty J by 2 array')
        if not np.all(np.isfinite(self.supports)) or np.any(self.supports[:,1]<=self.supports[:,0]):
            raise ValueError('All supports need finite positive width')
        if np.any(self.supports[:,0]<left) or np.any(self.supports[:,1]>right):
            raise ValueError('A bump may not enter the protected central or cut neighborhood')
        self.parameter_count=len(self.supports)
        self.breaks=np.unique(np.r_[self.base.breaks,self.supports.ravel()])
        self._cache={}
        self.set_parameters(np.zeros(self.parameter_count) if coefficients is None else coefficients)

    def set_parameters(self,coefficients):
        q=np.asarray(coefficients,float)
        if q.shape!=(self.parameter_count,) or not np.all(np.isfinite(q)):
            raise ValueError('The physical delta vector has the wrong size or is nonfinite')
        self.coefficients=q.copy();self._cache={}

    def basis(self,s,derivative=0):
        return compact_basis_jets(s,self.supports,derivative)

    def jet(self,s):
        s=np.atleast_1d(np.asarray(s,float))
        if np.any(s<0.) or np.any(s>self.end) or not np.all(np.isfinite(s)):
            raise ValueError('Outside the fixed physical meridian domain')
        key=(s.shape,s.tobytes())
        if key in self._cache:
            return self._cache[key]
        aa,av,acc=self.base.profile(s)
        B0,B1,B2=(self.basis(s,k) for k in range(3))
        a=aa+B0@self.coefficients;v=av+B1@self.coefficients;b=acc+B2@self.coefficients
        if np.any(a<=0.):
            raise FloatingPointError('The supplied physical metric is not positive at a requested point')
        c=v/a;K=-b/a
        zeros=np.zeros(s.shape+(self.parameter_count,))
        out=dict(a=a,a_s=v,a_ss=b,c=c,K=K,
            a_parameters=B0,a_s_parameters=B1,a_ss_parameters=B2,
            c_parameters=(B1-c[...,None]*B0)/a[...,None],
            K_parameters=(-B2-K[...,None]*B0)/a[...,None],
            inverse_a_parameters=-B0/a[...,None]**2,
            s=s.copy(),s_parameters=zeros.copy(),
            radial_scale=np.ones_like(s),radial_scale_parameters=zeros.copy())
        if len(self._cache)>=4:
            self._cache.pop(next(iter(self._cache)))
        self._cache[key]=out
        return out

    def profile(self,s):
        q=self.jet(s)
        return q['a'],q['a_s'],q['a_ss']

    def jvp(self,s,direction):
        d=np.asarray(direction,float)
        if d.shape!=(self.parameter_count,):
            raise ValueError('Direction dimension mismatch')
        q=self.jet(s)
        return {key:q[key+'_parameters']@d for key in
                ('a','a_s','a_ss','c','K','s','radial_scale')}

    def check_positive(self,*,base_lower_bound=None,base_lower_provenance=None,
                       points_per_piece=9,radius_floor=0.):
        """Actual finite screen plus a separate exact conditional global bound.

        If an already proved base lower bound B is supplied, every support
        interval has a_delta >= B + sum(min(delta_j,0), active j). This uses
        the exact 0<=psi_j<=1 bound, not a sampled maximum. The caller must
        identify the proof of B; this method does not invent that proof.
        """
        s=np.unique(np.concatenate([np.linspace(l,r,points_per_piece)
            for l,r in zip(self.breaks[:-1],self.breaks[1:])]))
        aa,av,acc=self.base.profile(s)
        B0,B1,B2=(self.basis(s,k) for k in range(3))
        a=aa+B0@self.coefficients;v=av+B1@self.coefficients;b=acc+B2@self.coefficients
        finite=bool(np.all(np.isfinite(a)) and np.all(np.isfinite(v)) and np.all(np.isfinite(b)))
        screen=dict(points=len(s),minimum_a=float(a.min()),minimum_at_s=float(s[a.argmin()]),
            maximum_abs_a_s=float(np.max(abs(v))),maximum_abs_a_ss=float(np.max(abs(b))),
            passed=finite and bool(a.min()>radius_floor),continuous_certificate=False)
        continuous=None
        if base_lower_bound is not None:
            if not base_lower_provenance:
                raise ValueError('Identify the already proved base lower bound before using it')
            lower=rational(base_lower_bound);floor=rational(radius_floor)
            nodes=np.unique(np.r_[0.,self.end,self.supports.ravel()]);rows=[]
            for left,right in zip(nodes[:-1],nodes[1:]):
                mid=(left+right)/2
                active=np.flatnonzero((self.supports[:,0]<mid)&(mid<self.supports[:,1]))
                bound=lower+sum((min(rational(self.coefficients[j]),Fraction()) for j in active),Fraction())
                rows.append(dict(interval=[float(left),float(right)],active=active.tolist(),
                    lower_fraction=str(bound),lower_numeric=float(bound)))
            minimum=min(rational(row['lower_fraction']) for row in rows)
            continuous=dict(base_lower_fraction=str(lower),base_lower_provenance=base_lower_provenance,
                lower_fraction=str(minimum),lower_numeric=float(minimum),
                strict_positive_above_floor=minimum>floor,rows=rows,
                scope='Exact sufficient inequality conditional on the identified base bound; not necessary for all deltas')
        return dict(sampled_screen=screen,continuous_sufficient_bound=continuous,
            target_positive_metric='a_delta(s)>0',
            abs_a_s_le_one_not_imposed=True,embedding_or_reach_certified=False)

    def definition(self):
        widths=self.supports[:,1]-self.supports[:,0]
        return dict(kind='fixed-physical-s-compact-C4-radial-bump-outer-design',
            source=identity(__file__),base_candidate=self.source_identity,
            parameters=self.coefficients.tolist(),parameter_count=self.parameter_count,
            supports=self.supports.tolist(),physical_endpoint=self.end,
            protected_cylinder=[0.,self.central_end],
            protected_cut_neighborhood=[self.end-self.collar_guard,self.end],
            basis='psi_j=1024 q_j^5(1-q_j)^5 on 0<q_j<1, zero elsewhere',
            q_j='(s-support_left)/(support_right-support_left)',
            derivative_formula='Leibniz factored polynomial, derivatives 0..4 vanish at support endpoints',
            uniform_basis_bounds=dict(value=1.,first=(81920/19683/widths).tolist(),
                second=(40/widths**2).tolist()),
            delta_scales_for_unit_a_second=(widths**2/40).tolist(),
            physical_metric='ds^2+(a_base(s)+sum(delta_j*psi_j(s)))^2 du^2',
            physical_metric_changes_with_delta=True,radial_clock='s is physical; scale 1; no warp',
            base_coast_T_fixed=True,central_and_cut_all_existing_jets_unchanged=True,
            same_g_refinement=False)


def positive_tail_kappa_yy(family,y):
    """Exact polynomial formula for the positive Bernstein tail kappa_yy.

    This extends the derivative exposed by the existing frozen family,
    without changing that family or numerically differentiating it.
    """
    y=np.asarray(y,float);q=(abs(y)-family.flat_radius)/family.width
    t=np.clip(q,0.,1.);r=1-t;inside=(q>0)&(q<1)
    degree=family.parameter_count-1;cols=[]
    for i in range(degree+1):
        j=degree-i;A=i+4;B=j+4
        value=630*comb(degree,i)*(A*(A-1)*t**(A-2)*r**B-
            2*A*B*t**(A-1)*r**(B-1)+B*(B-1)*t**A*r**(B-2))/family.width**3
        cols.append(np.where(inside,value,0.))
    jac=np.stack(cols,axis=-1)
    return dict(kappa_yy=jac@family.coefficients,kappa_yy_parameters=jac)


def tail_lifting_profile_jacobian(jet,coordinates,tail,weight,weight_s):
    """Analytic delta columns of the exact full tail lifting value/s/xi.

    The angular map and radial weights are fixed independently of delta.
    Returns [angle,node,nml,profile_parameter], without Fourier projection.
    Central seed lifting has zero physical-profile derivative.
    """
    U,Us,Uxi=(np.asarray(coordinates[k],float) for k in ('u','u_s','u_xi'))
    a,av=np.asarray(jet['a'],float),np.asarray(jet['a_s'],float)
    B0,B1=np.asarray(jet['a_parameters'],float),np.asarray(jet['a_s_parameters'],float)
    sn,cs=np.sin(U),np.cos(U)
    y=a[None,:]*sn;ys=av[None,:]*sn+a[None,:]*cs*Us;yx=a[None,:]*cs*Uxi
    q=tail.angle_jets(y);ky=np.asarray(q['kappa_y'],float)
    kyy=positive_tail_kappa_yy(tail,y)['kappa_yy']
    v=np.stack((cs*cs,-sn*cs,sn*sn),axis=-1)
    vu=np.stack((-2*sn*cs,sn*sn-cs*cs,2*sn*cs),axis=-1)
    yd=sn[...,None]*B0[None,:,:]
    ysd=sn[...,None]*B1[None,:,:]+(cs*Us)[...,None]*B0[None,:,:]
    yxd=(cs*Uxi)[...,None]*B0[None,:,:]
    raw=(ky[...,None]*yd)[...,None,:]*v[...,None]
    raw_s=((kyy*ys)[...,None]*yd+ky[...,None]*ysd)[...,None,:]*v[...,None]
    raw_s+=(ky[...,None]*yd)[...,None,:]*vu[...,None]*Us[...,None,None]
    raw_xi=((kyy*yx)[...,None]*yd+ky[...,None]*yxd)[...,None,:]*v[...,None]
    raw_xi+=(ky[...,None]*yd)[...,None,:]*vu[...,None]*Uxi[...,None,None]
    w=np.asarray(weight,float)[None,:,None,None];ws=np.asarray(weight_s,float)[None,:,None,None]
    return dict(values=w*raw,s=w*raw_s+ws*raw,xi=w*raw_xi)
