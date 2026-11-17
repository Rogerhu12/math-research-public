"""Nested complementary core spaces at a fixed positive homotopy value.

Freeze P_J, the projection onto support modes n,...,Jn, and use the same
linear operator T_lambda=lambda I+(1-lambda)P_J at every discretization M>=J.
The compact raw spaces are nested, so their T_lambda images are nested.
This is a separate declared core family, not a modification of old runs.
"""
from functools import lru_cache
import types
import numpy as np
from complementary_moment_basis import ComplementaryMomentBasis
import fixed_bimodal_core as fixed


class NestedProjectionBasis(ComplementaryMomentBasis):
    def __init__(self,*args,projection_order,**kwargs):
        super().__init__(*args,**kwargs)
        self.projection_order=int(projection_order)
        if not 2<=self.projection_order<=self.M:raise ValueError('Require 2 <= J <= M')
        self.projected=(np.arange(2,self.M+1)<=self.projection_order).astype(float)

    def support_jets(self,phi,order=4,homotopy=1.):
        compact=super().support_jets(phi,order,1.)
        if homotopy==1.:return compact
        if not 0<=homotopy<=1:raise ValueError('Invalid homotopy')
        x=self._local(phi).ravel();out=[]
        for k in range(order+1):
            analytic=self.projected[:,None]*self.target_freq[:,None]**k*np.cos(self.target_freq[:,None]*(x+self.center)+k*np.pi/2)
            analytic+=self.fundamental_leakage[:,None]*self.n**k*np.cos(self.n*(x+self.center)+k*np.pi/2)
            out.append(homotopy*compact[k]+(1-homotopy)*analytic)
        return tuple(out)

    def primitive(self,phi,homotopy=1.):
        compact=super().primitive(phi,1.)
        if homotopy==1.:return compact
        if not 0<=homotopy<=1:raise ValueError('Invalid homotopy')
        x=self._local(phi).ravel()
        analytic=self.projected[:,None]*np.sin(self.target_freq[:,None]*(x+self.center))/self.target_freq[:,None]
        analytic+=self.fundamental_leakage[:,None]*np.sin(self.n*(x+self.center))/self.n
        return homotopy*compact+(1-homotopy)*analytic

    def homotopy_rho_bounds(self,homotopy=1.):
        if not 0<=homotopy<=1:raise ValueError('Invalid homotopy')
        out=[]
        for k in range(3):
            compact=self.derivative_bounds[k]+self.derivative_bounds[k+2]
            low=self.projected*self.target_freq**k*(self.target_freq**2-1)+self.fundamental_absolute_upper*self.n**k*(self.n**2-1)
            out.append(homotopy*compact+(1-homotopy)*low)
        return tuple(out)

    def summary(self):
        out=super().summary()
        out.update(frozen_projection_order=self.projection_order,
                   actual_low_moments='At k<=J high support moments are the canonical identity; at J<k<=M they are lambda times that identity. The primary leakage is unchanged.')
        return out


def make_core_class(ReferencePlateauCore,projection_order):
    mod=types.ModuleType('nested_projection_core_literal');mod.__file__=str(fixed.SOURCE)
    exec(compile(fixed.text,str(fixed.SOURCE),'exec'),mod.__dict__)
    mod.ComplementaryMomentBasis=lru_cache(maxsize=32)(
        lambda **kwargs:NestedProjectionBasis(projection_order=projection_order,**kwargs))
    Base=mod.make_core_class(ReferencePlateauCore)
    class NestedCore(Base):
        def __init__(self,*args,**kwargs):
            if not 0<kwargs.get('homotopy',1.)<=1:raise ValueError('Nested fixed-projection refinement requires positive lambda')
            super().__init__(*args,**kwargs)
        def summary(self):
            out=super().summary()
            out.update(control_projection_order=projection_order,
                       control_family='Nested compact controls under one frozen positive-homotopy projection operator')
            return out
    return NestedCore


def embed_compact_coefficients(old_basis,old_coefficients,new_basis):
    """Exact defining moment formula, evaluated at recorded float constants."""
    if old_basis.M>new_basis.M:raise ValueError('Require increasing compact space')
    for name in ('n','a','eps','center','lock_fundamental'):
        if getattr(old_basis,name)!=getattr(new_basis,name):raise ValueError('Different compact control definition: '+name)
    trig=np.zeros(new_basis.M+1);trig[:old_basis.M+1]=np.asarray(old_coefficients)@old_basis.H
    result=2*new_basis.constants['gram'][2:]@trig
    return result,dict(trig_coefficient_error=float(abs(result@new_basis.H-trig).max()),
                       fundamental_error=float(abs(result@new_basis.fundamental_leakage-np.asarray(old_coefficients)@old_basis.fundamental_leakage)))

