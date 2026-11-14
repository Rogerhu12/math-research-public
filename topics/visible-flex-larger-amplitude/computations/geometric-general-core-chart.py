#!/usr/bin/env python3
"""General finite-support core chart and exact reference jets for Frenet BVPs.

theta(s,psi)=psi+b(s)*sum((1-n^2)*q_n*sin(n*psi)/n).
The default core-blend reference represents the entire fixed core exactly at
the inlet; its initial perturbation vector is zero at every Fourier resolution.
This module is a numerical coordinate interface, not a closed-surface solution.
"""
from __future__ import annotations
from dataclasses import dataclass
import types
from typing import Callable
import numpy as np


def vector(z):
    return np.stack((z.real,z.imag,np.zeros_like(z.real)),axis=-1)


@dataclass
class GeneralCoreChart:
    coefficients: object
    frequencies: object
    length: float
    reference: str = "core-blend"
    transition_start: float = 0.0
    transition_end: float = 1.0

    def __post_init__(self):
        self.coefficients=np.asarray(self.coefficients,dtype=float)
        original_frequencies=np.asarray(self.frequencies)
        self.frequencies=np.asarray(self.frequencies,dtype=int)
        if np.any(original_frequencies!=self.frequencies):
            raise ValueError("Frequencies must be integers")
        if self.coefficients.ndim!=1 or self.frequencies.shape!=self.coefficients.shape:
            raise ValueError("coefficients and frequencies must be matching one-dimensional arrays")
        if not np.all(np.isfinite(self.coefficients)):
            raise ValueError("Support coefficients must be finite")
        if np.any(self.frequencies<2) or len(set(self.frequencies.tolist()))!=len(self.frequencies):
            raise ValueError("Distinct integer frequencies >=2 are required")
        if self.length<=0 or not 0<=self.transition_start<self.transition_end<=1:
            raise ValueError("Need length>0 and 0<=transition_start<transition_end<=1")
        if self.reference not in ("round","core-blend"):
            raise ValueError("Unknown reference")

    def weight(self,s):
        """b,b_s,b_ss: a C2 quintic, constant outside its transition."""
        s=np.atleast_1d(np.asarray(s,dtype=float))
        lo=self.transition_start*self.length
        span=(self.transition_end-self.transition_start)*self.length
        x=np.clip((s-lo)/span,0.,1.)
        b=1-x**3*(10-15*x+6*x*x)
        bp=-30*x*x*(1-x)**2/span
        bpp=-60*x*(1-x)*(1-2*x)/span**2
        return b[:,None],bp[:,None],bpp[:,None]

    def core(self,psi,direction=None):
        """Exact support, arc map, and normal-angle position jets."""
        psi=np.atleast_1d(np.asarray(psi,dtype=float))
        n=self.frequencies
        co=np.cos(psi[:,None]*n[None,:])
        si=np.sin(psi[:,None]*n[None,:])
        q=self.coefficients if direction is None else np.asarray(direction,dtype=float)
        if q.shape!=n.shape:raise ValueError("Coefficient direction has wrong shape")
        mean=1. if direction is None else 0.
        h=mean+co@q
        hp=-si@(n*q)
        rho=mean+co@((1-n*n)*q)
        rhop=-si@(n*(1-n*n)*q)
        arc_offset=si@((1-n*n)*q/n)
        er=np.exp(1j*psi)
        C=(h+1j*hp)*er
        Cp=1j*rho*er
        Cpp=(1j*rhop-rho)*er
        return dict(h=h,hp=hp,rho=rho,rhop=rhop,arc_offset=arc_offset,
                    C=C,Cp=Cp,Cpp=Cpp)

    def angle(self,s,psi,direction=None):
        s=np.atleast_1d(np.asarray(s,dtype=float))
        psi=np.atleast_1d(np.asarray(psi,dtype=float))
        b,bp,bpp=self.weight(s)
        c=self.core(psi,direction)
        A=c['arc_offset'][None,:]
        if direction is None:
            d=c['rho'][None,:]-1
            theta=psi[None,:]+b*A
            rho=1+b*d
        else:
            d=c['rho'][None,:]
            theta=b*A
            rho=b*d
        rhop=b*c['rhop'][None,:]
        theta_s=bp*A
        theta_ss=bpp*A
        rho_s=bp*d
        rhop_s=bp*c['rhop'][None,:]
        return dict(theta=theta,rho=rho,rhop=rhop,theta_s=theta_s,
                    theta_ss=theta_ss,rho_s=rho_s,rhop_s=rhop_s,
                    b=b,bp=bp,bpp=bpp,core=c)

    @staticmethod
    def _exponential_jets(g,dg=None):
        th=g['theta'];rho=g['rho'];rp=g['rhop']
        ts=g['theta_s'];tss=g['theta_ss'];rs=g['rho_s'];rps=g['rhop_s']
        z=np.exp(1j*th)
        k2=1j*rp-rho*rho
        ks2=1j*rps-2*rho*rs+1j*ts*k2
        jets=dict(p0=z,p1=1j*rho*z,p2=k2*z,
                  s1=1j*ts*z,s2=(1j*tss-ts*ts)*z,
                  sp=(1j*rs-ts*rho)*z,spp=ks2*z)
        if dg is None:return jets
        dt=dg['theta'];dr=dg['rho'];drp=dg['rhop']
        dts=dg['theta_s'];dtss=dg['theta_ss'];drs=dg['rho_s'];drps=dg['rhop_s']
        dz=1j*dt*z
        dk2=1j*drp-2*rho*dr
        dks2=1j*drps-2*dr*rs-2*rho*drs+1j*dts*k2+1j*ts*dk2
        return dict(p0=dz,
                    p1=1j*dr*z+1j*rho*dz,
                    p2=dk2*z+k2*dz,
                    s1=1j*dts*z+1j*ts*dz,
                    s2=(1j*dtss-2*ts*dts)*z+(1j*tss-ts*ts)*dz,
                    sp=(1j*drs-dts*rho-ts*dr)*z+(1j*rs-ts*rho)*dz,
                    spp=dks2*z+ks2*dz)

    def _reference_jets(self,g,zjets,direction=None):
        if self.reference=='round':return zjets
        b,bp,bpp=g['b'],g['bp'],g['bpp']
        c=g['core'] if direction is None else self.core(direction[0],direction[1])
        C,Cp,Cpp=[c[k][None,:]for k in ('C','Cp','Cpp')]
        z=zjets
        return dict(p0=(1-b)*z['p0']+b*C,
                    p1=(1-b)*z['p1']+b*Cp,
                    p2=(1-b)*z['p2']+b*Cpp,
                    s1=(1-b)*z['s1']+bp*(C-z['p0']),
                    s2=(1-b)*z['s2']-2*bp*z['s1']+bpp*(C-z['p0']),
                    sp=(1-b)*z['sp']+bp*(Cp-z['p1']),
                    spp=(1-b)*z['spp']+bp*(Cpp-z['p2']))

    @staticmethod
    def _multiply_profile(jets,profile):
        a,ap,app=[np.atleast_1d(np.asarray(x))[:,None]for x in profile]
        B=jets
        return dict(pos=vector(a*B['p0']),p1=vector(a*B['p1']),p2=vector(a*B['p2']),
                    s1=vector(ap*B['p0']+a*B['s1']),
                    s2=vector(app*B['p0']+2*ap*B['s1']+a*B['s2']),
                    sp=vector(ap*B['p1']+a*B['sp']),
                    spp=vector(ap*B['p2']+a*B['spp']))

    def geometry(self,s,psi,profile:Callable,direction=None):
        """All fields expected by the adaptive Frenet frame, or their q JVP.

        Output shapes: scalar fields (len(s),len(psi)); vector fields add 3.
        Coefficient JVP keeps profile, length and b fixed.
        """
        s=np.atleast_1d(np.asarray(s,dtype=float))
        psi=np.atleast_1d(np.asarray(psi,dtype=float))
        g=self.angle(s,psi)
        if np.min(g['rho'])<=0:raise FloatingPointError("General core angle chart is not invertible at evaluation points")
        rho=g['rho'];ts=g['theta_s'];rs=g['rho_s'];rp=g['rhop']
        v=ts/rho
        vs=(g['theta_ss']-v*rs)/rho
        vp=(rs-v*rp)/rho
        if direction is None:
            zjets=self._exponential_jets(g)
            ref=self._reference_jets(g,zjets)
            out=self._multiply_profile(ref,profile(s))
            out.update({k:g[k]for k in ('theta','rho','rhop','theta_s','theta_ss','rho_s','rhop_s')})
            out.update(v=v,vs=vs,vp=vp,b=g['b'][:,0],e=g['b'][:,0])
            # e is a compatibility diagnostic only: it denotes b, not a single-mode amplitude.
            return out
        dg=self.angle(s,psi,direction)
        dzjets=self._exponential_jets(g,dg)
        dref=self._reference_jets(g,dzjets,(psi,direction))
        out=self._multiply_profile(dref,profile(s))
        dr=dg['rho'];dv=(dg['theta_s']-v*dr)/rho
        dvs=(dg['theta_ss']-dv*rs-v*dg['rho_s']-vs*dr)/rho
        dvp=(dg['rho_s']-dv*rp-v*dg['rhop']-vp*dr)/rho
        out.update({k:dg[k]for k in ('theta','rho','rhop','theta_s','theta_ss','rho_s','rhop_s')})
        out.update(v=dv,vs=dvs,vp=dvp,b=np.zeros(len(s)),e=np.zeros(len(s)))
        return out

    def geo(self,s,N,profile):
        return self.geometry(s,2*np.pi*np.arange(N)/N,profile)

    def parameter_jvp(self,s,N,profile,direction):
        return self.geometry(s,2*np.pi*np.arange(N)/N,profile,direction)

    def profile_jvp(self,s,N,profile_direction):
        """Reference-vector JVP for (a,a_s,a_ss), keeping chart/length fixed.

        Return vector jets only; angle and transport-field variations are zero.
        If a parameter changes length, its b variation must also be included.
        """
        s=np.atleast_1d(np.asarray(s,dtype=float))
        psi=2*np.pi*np.arange(N)/N
        g=self.angle(s,psi)
        ref=self._reference_jets(g,self._exponential_jets(g))
        return self._multiply_profile(ref,profile_direction(s))

    def inlet_geometry(self,N):
        psi=2*np.pi*np.arange(N)/N
        c=self.core(psi)
        return dict(psi=psi,theta=psi+c['arc_offset'],rho=c['rho'],rhop=c['rhop'],
                    pos=vector(c['C']),p1=vector(c['Cp']),p2=vector(c['Cpp']))

    def initial(self,flow):
        """Exact zero perturbation for fixed core-blend, a(0)=1.

        Do not use for round reference: that would require a Fourier projection.
        The separately integrated height mean starts at zero as in the source.
        """
        if self.reference!='core-blend':raise ValueError("Exact zero inlet requires core-blend reference")
        a,ap,app=flow.profile(np.array([0.]))
        if abs(float(a[0])-1)>4e-15:raise ValueError("Core normalization requires a(0)=1")
        return np.zeros(flow.n)


def attach_to_adaptive_flow(flow,coefficients,frequencies,reference='core-blend',**kwargs):
    """Attach geo and physical_base to an existing adaptive-frame Flow instance.

    The caller MUST use the adaptive frame/RHS that consumes geo, not the old
    constant-angle PlanarSymmetryFlow frame. This function refuses other frames.
    The existing finite basis/project methods and physical profile stay unchanged.
    """
    if not hasattr(flow,'geo'):
        raise TypeError("Need adaptive-chart Flow whose frame and RHS consume geo")
    chart=GeneralCoreChart(coefficients,frequencies,float(flow.end),reference,**kwargs)
    flow.general_core_chart=chart
    def geo(self,s,N):return self.general_core_chart.geo(s,N,self.profile)
    def physical_base(self,s,N,derivative=0):
        return self.geo(s,N)[('pos','s1','s2')[derivative]]
    flow.geo=types.MethodType(geo,flow)
    flow.physical_base=types.MethodType(physical_base,flow)
    return chart


def fixed_core_initial_factory(flow_provider):
    """BVP initial(p) hook when support coefficients are fixed design data.

    flow_provider(p) should return the actual profile-dependent adaptive Flow.
    Root may set initial_jac to zero: every parameter gives the same zero vector.
    """
    def initial(p):
        flow=flow_provider(p)
        return flow.general_core_chart.initial(flow)
    return initial


def smoke_checks():
    """Meaningful differential and exact-inlet checks for this interface."""
    q=np.array([34/75,-17/375,34/6125,-17/44100])
    n=2*np.arange(1,5)
    chart=GeneralCoreChart(q,n,2.3)
    profile=lambda s:(1+.08*np.sin(np.asarray(s)),.08*np.cos(np.asarray(s)),-.08*np.sin(np.asarray(s)))
    s=np.array([.13,.55,1.24,2.05]);psi=np.linspace(.03,6.2,31)
    g=chart.geometry(s,psi,profile)
    h=2e-6
    gp=chart.geometry(s+h,psi,profile);gm=chart.geometry(s-h,psi,profile)
    pp=chart.geometry(s,psi+h,profile);pm=chart.geometry(s,psi-h,profile)
    errors={
        's1':float(np.max(abs((gp['pos']-gm['pos'])/(2*h)-g['s1']))),
        's2':float(np.max(abs((gp['s1']-gm['s1'])/(2*h)-g['s2']))),
        'p1':float(np.max(abs((pp['pos']-pm['pos'])/(2*h)-g['p1']))),
        'p2':float(np.max(abs((pp['p1']-pm['p1'])/(2*h)-g['p2']))),
        'sp':float(np.max(abs((gp['p1']-gm['p1'])/(2*h)-g['sp']))),
        'spp':float(np.max(abs((gp['p2']-gm['p2'])/(2*h)-g['spp']))),
    }
    direction=np.array([.27,-.09,.015,.004])
    dg=chart.geometry(s,psi,profile,direction)
    plus=GeneralCoreChart(q+h*direction,n,2.3).geometry(s,psi,profile)
    minus=GeneralCoreChart(q-h*direction,n,2.3).geometry(s,psi,profile)
    errors['parameter_jvp']=max(float(np.max(abs((plus[k]-minus[k])/(2*h)-dg[k])))
                                for k in ('pos','p1','p2','s1','s2','sp','spp','theta','rho','rhop','v','vs','vp'))
    constant=lambda s:(np.ones(len(s)),np.zeros(len(s)),np.zeros(len(s)))
    ends=chart.geometry(np.array([0.,chart.length]),psi,constant)
    core=chart.core(psi)
    errors['inlet_position']=float(np.max(abs(ends['pos'][0]-vector(core['C']))))
    errors['inlet_metric']=float(np.max(abs(np.sum(ends['p1'][0]**2,axis=-1)/core['rho']**2-1)))
    errors['cut_identity']=float(np.max(abs(ends['theta'][1]-psi)))
    errors['endpoint_angle_s']=float(np.max(abs(ends['theta_s'])))
    errors['endpoint_angle_ss']=float(np.max(abs(ends['theta_ss'])))
    if max(errors.values())>2e-7:raise AssertionError(errors)
    return errors


if __name__=='__main__':
    import json
    print(json.dumps(smoke_checks(),indent=2))
