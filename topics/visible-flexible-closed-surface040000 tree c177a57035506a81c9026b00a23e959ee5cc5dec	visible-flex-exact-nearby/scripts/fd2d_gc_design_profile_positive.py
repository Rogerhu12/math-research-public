#!/usr/bin/env python3
"""R131: a closed-form positive radial clock for all positive coast lengths.

This is a chart replacement at each fixed T, never a change of the physical
scalar metric.  T itself remains an outer physical design parameter.  For
q=L(T)/L_ref and t=pi*tau, set theta=atan2(sin(t),q*cos(t)) in [0,pi].
Then local_s=L(T)*theta/pi and s_x=q^2/(q^2*cos(t)^2+sin(t)^2).
The formula has exact endpoints, positive derivative, and full explicit JVP.
It does not divide by tail n or b and does not numerically invert a moment.
"""
from __future__ import annotations
import numpy as np
from fd2d_gc_design_profile import CoastDesignProfile


def positive_coast_clock(tau,ratio):
    """Dimensionless local s/Lref, d/dq, s_x, and d(s_x)/dq."""
    tau=np.asarray(tau,dtype=float);q=float(ratio)
    if not q>0.:
        raise ValueError('Physical coast length must be positive')
    t=np.pi*tau;sn,cs=np.sin(t),np.cos(t)
    denominator=q*q*cs*cs+sn*sn
    theta=np.arctan2(sn,q*cs)
    theta=np.where(tau==0.,0.,np.where(tau==1.,np.pi,theta))
    J=q*theta/np.pi
    J_q=theta/np.pi-q*sn*cs/(np.pi*denominator)
    J_q=np.where(tau==0.,0.,np.where(tau==1.,1.,J_q))
    scale=q*q/denominator
    scale_q=2*q*sn*sn/(denominator*denominator)
    scale=np.where((tau==0.)|(tau==1.),1.,scale)
    scale_q=np.where((tau==0.)|(tau==1.),0.,scale_q)
    return J,J_q,scale,scale_q


class PositiveCoastDesignProfile(CoastDesignProfile):
    """Drop-in CoastDesignProfile with no extra coordinate-T restriction."""
    def set_parameter(self,T):
        T=float(T)
        if self.T==T:
            return
        if not 0.<T<self.model.Tmax:
            raise FloatingPointError('Outside the physical positive-length interval')
        candidate=self.model.candidate(T)
        if len(candidate.segments)!=len(self.base.segments):
            raise FloatingPointError('A physical zero-length piece requires another domain')
        clocks={};minimum=1.
        for index in (self.model.shallow,self.model.deep):
            old,new=self.base.segments[index],candidate.segments[index]
            length_T=1. if index==self.model.shallow else self.model.deep_length_derivative
            ratio=new['L']/old['L']
            if not ratio>0.:
                raise FloatingPointError('A physical coast is not positive')
            clocks[index]=dict(ratio=ratio,ratio_T=length_T/old['L'],length_T=length_T)
            minimum=min(minimum,ratio*ratio)
        self.T,self.current,self._clocks=T,candidate,clocks
        self.minimum_radial_scale=minimum;self._cache={}

    def jet(self,x):
        x=np.atleast_1d(np.asarray(x,dtype=float));key=x.tobytes()
        if key in self._cache:
            return self._cache[key]
        if np.any(x < -2e-12) or np.any(x > self.end+2e-12):
            raise ValueError('Outside the fixed computational radial domain')
        ids=np.clip(np.searchsorted(self.breaks,x,side='right')-1,0,len(self.segments)-1)
        keys=('a','a_s','a_ss','a_T','a_s_T','a_ss_T','s','s_T','radial_scale','radial_scale_T')
        out={name:np.empty_like(x) for name in keys}
        for j in np.unique(ids):
            mask=ids==j;old,new=self.base.segments[j],self.current.segments[j]
            tau=np.clip((x[mask]-old['s0'])/old['L'],0.,1.)
            shift_T=0. if j<=self.model.shallow else 1. if j<=self.model.deep else self.model.total_length_derivative
            if j in self._clocks:
                data=self._clocks[j]
                J,J_q,scale,scale_q=positive_coast_clock(tau,data['ratio'])
                local_s=old['L']*J;local_s_T=data['length_T']*J_q
                local_s=np.where(tau==0.,0.,np.where(tau==1.,new['L'],local_s))
                local_s_T=np.where(tau==0.,0.,np.where(tau==1.,data['length_T'],local_s_T))
                physical_tau=local_s/new['L'];scale_T=scale_q*data['ratio_T']
                a_T=self.model.vm*local_s_T if j==self.model.shallow else self.model.vm+self.model.vd*local_s_T
            else:
                local_s=new['L']*tau;local_s_T=np.zeros_like(tau)
                physical_tau=tau;scale=np.ones_like(tau);scale_T=np.zeros_like(tau)
                a_T=np.full_like(tau,self.model.vm if self.model.shallow<j<self.model.deep else 0.)
            aa,ap,app=self.current._jet(new,physical_tau)
            out['a'][mask],out['a_s'][mask],out['a_ss'][mask]=aa,ap,app
            out['a_T'][mask]=a_T;out['a_s_T'][mask]=out['a_ss_T'][mask]=0.
            out['s'][mask]=new['s0']+local_s;out['s_T'][mask]=shift_T+local_s_T
            out['radial_scale'][mask],out['radial_scale_T'][mask]=scale,scale_T
        if np.any(out['radial_scale']<=0.) or not np.all(np.isfinite(out['radial_scale'])):
            raise FloatingPointError('Positive exact clock could not be represented in floating point; no extra physical T condition')
        out['c']=out['a_s']/out['a'];out['c_T']=-out['c']*out['a_T']/out['a']
        out['K']=-out['a_ss']/out['a'];out['K_T']=-out['K']*out['a_T']/out['a']
        out['piece']=ids
        if len(self._cache)>=4:
            self._cache.pop(next(iter(self._cache)))
        self._cache[key]=out
        return out

    def definition(self):
        return dict(kind='coast-T-outer-physical-design-with-positive-closed-form-clock',
            reference_T=self.reference_T,actual_T=self.T,
            physical_T_domain=[0.,self.model.Tmax],
            computational_endpoint=self.end,actual_physical_endpoint=self.current.end,
            minimum_s_x=self.minimum_radial_scale,
            changing_coasts=[int(self.model.shallow),int(self.model.deep)],
            coast_ratio='q=L(T)/L_ref',
            angle='theta=atan2(sin(pi*tau),q*cos(pi*tau)), branch [0,pi]',
            coast_map='s=s0(T)+L(T)*theta/pi',
            radial_scale='q^2/(q^2*cos(pi*tau)^2+sin(pi*tau)^2)',
            exact_minimum_radial_scale='min(1,q_shallow^2,q_deep^2)',
            clocks={int(k):v for k,v in self._clocks.items()},
            other_piece_map='s=s0(T)+L*tau',
            exact_clock_positive_for_every_positive_physical_coast=True,
            physical_metric_changes_with_T=True,
            radial_chart_is_only_a_coordinate_change_at_each_fixed_T=True,
            source_of_endpoint_values='analytic exact endpoint overrides',
            no_scalar_quadrature_or_inverse_is_used_in_the_clock=True)


# Consumers can import the historical class name from this new module.
CoastDesignProfile=PositiveCoastDesignProfile
