#!/usr/bin/env python3
"""R589/R590: exact C2 history, paid positive square, and free-end germs.

New science executes only in the declared public GitHub Actions repository.
The physical input is the same fixed R578 library. No large potential is omitted.
This is a new 29-condition problem with explicit true center parameters, not a
replay of the four fixed-H/L guesses from the original nineteen-state run.
"""
from __future__ import annotations

import argparse
from dataclasses import dataclass
import gc
import hashlib
import json
import os
import time

import numpy as np
from scipy.integrate import cumulative_simpson, solve_bvp, solve_ivp
from scipy.linalg import qr

import r530_full_centered_nineteen_bvp_agent as old


LD = np.longdouble
ODD = old.ODD
EVEN = old.EVEN
JPAR = old.JPAR
PI = LD(str(np.pi))


def emit(tag, value):
    print(tag+" "+json.dumps(value, sort_keys=True, allow_nan=False), flush=True)


def regularized_bundle():
    """Prove the full highest identity before replacing any history row."""
    start = time.time()
    labels, original, original_stats = old.compile_bundle()
    X,U,P,R,T,D = old.X,old.U,old.P,old.R,old.T,old.D
    H,K,E,G,V = old.H,old.K,old.E,old.G,old.V
    z, e = X+E, H*(X+E)-K
    qq, qg = 1+e**2, 1+(H*E-K)**2
    es = G*z-V/2
    qgs = 2*(H*E-K)*(G*E-V/2)
    fzero = qq*(G*P-es*R)/(8*H**3)
    _,a1,a2,b0,b1,b2 = old.e8_coefficients(old.AVAR)
    ha = a1*U+2*a2*P-2*(b0+X*b1+X**2*b2)*R
    m = old.matrix_poly()
    out = list(original[:3])
    outlabels = list(labels[:3])
    potentials = []
    identity_terms = []
    for j in range(3):
        kj = D**2*(qg*X**j*(fzero**2/4+ha**2/16)
                   +(qq*fzero*ha/4 if j==0 else 0))
        fulln = original[3+3*j]+old.ACC*original[4+3*j]+old.BCC*original[5+3*j]
        if any(key[old.IT]>2 for key in fulln.terms):
            raise RuntimeError("Full history has an unexpected power above T^2")
        expected = qg*old.dt(kj,matrix=m)-qgs*kj
        difference = fulln.coefficient(old.IT,2)-expected
        identity_terms.append(len(difference.terms))
        if difference.terms:
            raise RuntimeError(f"R590 exact full highest potential identity failed in component {j}")
        for suffix, polynomial in zip(("0","a","b"),original[3+3*j:6+3*j]):
            low = (polynomial.coefficient(old.IT,0)
                   -old.d0(polynomial.coefficient(old.IT,1).primitive(old.IR)))
            if any(key[old.IT] for key in low.terms):
                raise RuntimeError("A regularized full history row retained T")
            out.append(low)
            outlabels.append(f"C2N{j}_{suffix}")
        potentials.append(kj*T**2)
    out.extend(original[12:16])
    outlabels.extend(labels[12:16])
    out.extend(potentials)
    outlabels.extend(("E0_numerator","E1_numerator","E2_numerator"))
    if any(key[old.IX]+key[old.IJ1]+2*key[old.IJ2]>10
           for p in out for key in p.terms):
        raise RuntimeError("A new complete readout exceeds the matched translation degree")
    stats = {"elapsed_seconds":time.time()-start,
             "original_formal_seconds":original_stats["elapsed_seconds"],
             "full_highest_difference_terms":identity_terms,
             "labels":outlabels,"exact_terms":[len(p.terms) for p in out],
             "whole_history_C2":True,
             "paid_ruling_square_retained":True,
             "new_physical_root_claim":False}
    return outlabels,out,original,stats


@dataclass
class Jet:
    value: object
    derivative: object

    __array_priority__ = 10000

    def __post_init__(self):
        self.value = LD(self.value)
        self.derivative = np.asarray(self.derivative,dtype=LD)

    def coerce(self, other):
        return other if isinstance(other,Jet) else Jet(other,np.zeros_like(self.derivative))

    def __add__(self,other):
        other = self.coerce(other)
        return Jet(self.value+other.value,self.derivative+other.derivative)

    __radd__ = __add__

    def __neg__(self):
        return Jet(-self.value,-self.derivative)

    def __sub__(self,other):
        return self+-self.coerce(other)

    def __rsub__(self,other):
        return self.coerce(other)+-self

    def __mul__(self,other):
        other = self.coerce(other)
        return Jet(self.value*other.value,
                   self.derivative*other.value+self.value*other.derivative)

    __rmul__ = __mul__

    def __truediv__(self,other):
        other = self.coerce(other)
        return Jet(self.value/other.value,
                   (self.derivative*other.value-self.value*other.derivative)/other.value**2)

    def __rtruediv__(self,other):
        return self.coerce(other)/self

    def __pow__(self,n):
        if n==0:
            return self.coerce(1)
        return Jet(self.value**n,n*self.value**(n-1)*self.derivative)


def atan(value):
    if isinstance(value,Jet):
        return Jet(np.arctan(value.value),value.derivative/(1+value.value**2))
    return np.arctan(value)


def constant(value, dimension):
    return Jet(value,np.zeros(dimension,dtype=LD))


def values_and_jacobian(jets):
    return (np.asarray([v.value for v in jets],dtype=LD),
            np.asarray([v.derivative for v in jets],dtype=LD))


class DifferentiableCoefficients(old.Coefficients):
    """Exact monomial derivatives, including zero-valued non-h coordinates."""
    def evaluate_jets(self,geometry,history):
        zero = geometry[0]*0
        jets = list(geometry)+[zero,zero]+list(history)
        values,chain = values_and_jacobian(jets)
        with np.errstate(over="raise",divide="raise",invalid="raise"):
            powers = values[None,:]**self.gkeys
            monomials = np.prod(powers,axis=1,dtype=LD)
            answer = self.coefficients@monomials
            if chain.shape[1]:
                jac = np.zeros((len(monomials),len(values)),dtype=LD)
                for i,value in enumerate(values):
                    if value:
                        jac[:,i] = self.gkeys[:,i]*monomials/value
                    else:
                        chosen = self.gkeys[:,i]==1
                        reduced = powers[chosen].copy()
                        reduced[:,i] = 1
                        jac[chosen,i] = np.prod(reduced,axis=1,dtype=LD)
                derivative = (self.coefficients@jac)@chain
            else:
                derivative = np.zeros((len(answer),0),dtype=LD)
        return [Jet(v,d) for v,d in zip(answer,derivative)]


def polynomial_product(left,right):
    zero = left[0]*0
    result = [zero for _ in range(len(left)+len(right)-1)]
    for i,a in enumerate(left):
        for j,b in enumerate(right):
            result[i+j] = result[i+j]+a*b
    return result


def vector_add(left,right,scale=1):
    return [a+scale*b for a,b in zip(left,right)]


def profile_vectors(geometry,history):
    """18 coefficients in (u,p,r) times y^0,...,y^5.

    HA+2F0 is assembled before the positive Gram is contracted. The prepared
    center cancellation therefore occurs at its actual linear factors.
    """
    h,k,eta,gamma,upsilon = geometry
    p0,p1,p2,t1,r1,s1,s0,r0 = history
    zero = h*0
    dg = h*eta-k
    qq = [1+dg*dg,2*h*dg,h*h]
    ess = [gamma*eta-upsilon/2,gamma]
    qe = polynomial_product(qq,ess)
    aa1 = [p0,p1,p2]
    aa2 = [r1,s1-p0/2,t1-p1/2,-p2/2]
    ca = [r0,r1+s0,3*s1/2,t1-p1/4,-p2/4]
    ha = [zero for _ in range(18)]
    ff = [zero for _ in range(18)]
    for i,value in enumerate(aa1):
        ha[i] = value
    for i,value in enumerate(aa2):
        ha[6+i] = 2*value
    for i,value in enumerate(ca):
        ha[12+i] = -2*value
    for i,value in enumerate(qq):
        ff[6+i] = gamma*value/(8*h**3)
    for i,value in enumerate(qe):
        ff[12+i] = -value/(8*h**3)
    return vector_add(ha,ff,2),ff,ha


def multiply_position(vector,polynomial):
    zero = vector[0]*0
    result = [zero for _ in vector]
    for kind in range(3):
        for power in range(6):
            value = vector[6*kind+power]
            for j,coefficient in enumerate(polynomial):
                if power+j<6:
                    result[6*kind+power+j] = result[6*kind+power+j]+value*coefficient
                elif value.value or np.any(value.derivative):
                    if coefficient.value or np.any(coefficient.derivative):
                        raise RuntimeError("The positive potential exceeded its proven degree-five basis")
    return result


class PositivePotentialGram:
    """Untruncated QR factor of a positive fixed quadrature Gram.

    There is no eigenvalue clipping or rank truncation. The QR is a numerical
    factor of the declared positive quadrature, not an independent physical
    replacement. Refined quadrature and direct positive checks are reported.
    """
    def __init__(self,grid):
        start = time.time()
        y,u,p,r,t,j0,j1,j2,cc,dd = grid.reference_values()
        fields = (u,p,r)
        features = np.stack([value*y**degree for value in fields for degree in range(6)],axis=-1)
        weight = (6*np.asarray(grid.block_weights,dtype=LD)[:,None]
                  *np.asarray(grid.quad,dtype=LD)[None,:]*dd**2*t**2)
        flat = features.reshape(-1,18)
        flatweight = weight.ravel()
        positive = flatweight>0
        weighted = flat[positive]*np.sqrt(flatweight[positive])[:,None]
        self.scales = np.sqrt(np.sum(weighted**2,axis=0,dtype=LD))
        if not np.all(self.scales>0):
            raise RuntimeError("A declared positive potential basis column vanished")
        normalized = weighted/self.scales
        qfactor,rfactor = qr(np.asarray(normalized,dtype=float),mode="economic",check_finite=True)
        del qfactor
        self.factor = np.asarray(rfactor,dtype=LD)
        direct = normalized.T@normalized
        defect = self.factor.T@self.factor-direct
        self.stats = {"order":grid.order,"positive_rows":int(positive.sum()),
                      "basis_columns":18,"untruncated_QR":True,
                      "column_scale_range":[float(self.scales.min()),float(self.scales.max())],
                      "normalized_Gram_max_absolute_QR_defect":float(np.max(np.abs(defect))),
                      "elapsed_seconds":time.time()-start}

    def image(self,vector):
        value,jacobian = values_and_jacobian(vector)
        return self.factor@(self.scales*value),self.factor@(self.scales[:,None]*jacobian)

    def pair(self,left,right):
        lv,ld = self.image(left)
        rv,rd = self.image(right)
        return Jet(lv@rv,ld.T@rv+rd.T@lv)

    def weighted_pair(self,left,right,h,dg):
        eleft = multiply_position(left,[dg,h])
        eright = multiply_position(right,[dg,h])
        return self.pair(left,right)+self.pair(eleft,eright)

    def energy(self,geometry,history):
        h,k,eta,_,_ = geometry
        vector,_,_ = profile_vectors(geometry,history)
        return self.weighted_pair(vector,vector,h,h*eta-k)/(64*h)

    def center_difference(self,geometry,history,center_geometry,center_history):
        """Compute w(S).(E(S,v,A)-Ec) with the center retained exactly.

        DeltaQ=(qg/qgc)Qc-Q has zero constant coefficient because the true
        center has k=eta=0 and qgc=1. The expression uses factored squares.
        """
        h,k,eta,_,_ = geometry
        hc = center_geometry[0]
        dg,qg = h*eta-k,1+(h*eta-k)**2
        current,_,_ = profile_vectors(geometry,history)
        centered,fc,hac = profile_vectors(center_geometry,center_history)
        first = self.weighted_pair(vector_add(current,centered,-1),
                                   vector_add(current,centered),h,dg)
        deltaq = [h*0,-2*h*dg,qg*hc**2-h**2]
        second = self.pair(multiply_position(fc,deltaq),hac)
        return (first-4*second)/(64*h)


def density(geometry):
    h,k,eta,gamma,upsilon = geometry
    dg,ds = h*eta-k,gamma*eta-upsilon/2
    qg = 1+dg*dg
    aa1 = 2*k*eta-(k*k+1)/h
    aa0 = k*eta*eta-(k*k+1)*eta/h
    p0,p1,p2 = -k*qg/(2*h),-k*dg,-k*h/2
    common = gamma*qg/h-2*dg*ds
    r0 = (aa0*qg+ds*common/h**2)/(8*h)
    r1 = (aa1*qg+gamma*common/h**2)/(8*h)
    s0 = (aa0*dg-ds*ds/h**2)/4
    s1 = (aa1*dg-gamma*ds/h**2)/4
    t1 = (h*aa1-gamma*gamma/h**2)/8
    return [p0,p1,p2,t1,r1,s1,s0,r0]


def weights(geometry):
    h,k,eta,_,_ = geometry
    dg = h*eta-k
    return [(1+dg*dg)/(4*h),dg/2,h/4]


def dot(left,right):
    return sum((a*b for a,b in zip(left,right)),left[0]*0)


class FiniteCoordinates:
    hmid,hcap,kcap,etacap,vcap = LD("1.9"),LD("1.1"),LD(2),LD(1),LD(6)
    lmid,lcap,acap = LD(5),LD(3),LD(128)

    def __init__(self,nuhat_scale):
        self.nuhat_scale = LD(nuhat_scale)

    def physical(self,state):
        limits = (self.hcap,self.kcap,self.etacap,self.vcap,self.vcap)
        geometric = [2/PI*lim*atan(q) for lim,q in zip(limits,state[:5])]
        geometric[0] = geometric[0]+self.hmid
        derivatives = [2/PI*lim/(1+q*q) for lim,q in zip(limits,state[:5])]
        return geometric,derivatives

    def encode(self,geometry):
        limits = np.array([self.hcap,self.kcap,self.etacap,self.vcap,self.vcap],dtype=LD)
        shifted = np.asarray(geometry,dtype=LD).copy()
        shifted[0] -= self.hmid
        scaled = shifted/limits
        if np.max(np.abs(scaled))>=1:
            raise ValueError("A new kinematic seed leaves its fixed strict physical box")
        return np.asarray(np.tan(PI*scaled/2),dtype=float)

    def center(self,parameters):
        hp,vp = parameters[0],parameters[1]
        h = self.hmid+2*self.hcap/PI*atan(hp)
        v = 2*self.vcap/PI*atan(vp)
        residual = [2*self.acap/PI*atan(q) for q in parameters[2:6]]
        odd = [v/(12*h)+residual[0],residual[1],
               v/(16*h**3)+residual[2],v/(24*h)+residual[3]]
        zero = h*0
        aa = [zero for _ in range(8)]
        for index,value in zip(ODD,odd):
            aa[index] = value
        geo = [h,zero,zero,zero,v]
        nuhat = [self.nuhat_scale*value for value in parameters[6:9]]
        length = self.lmid+2*self.lcap/PI*atan(parameters[9])
        return geo,aa,nuhat,length


class FullC2RHS:
    """Same physical system, with explicit ten true center parameters.

    The main RHS uses nuhat and current positive energy. The center potential
    enters only recovery and boundary identities, never a new large RHS
    parameter coupling. The fixed linear nuhat scale does not scale defects.
    """
    def __init__(self,coefficients,potential):
        self.coefficients,self.potential = coefficients,potential
        reference_geometry = [constant(v,0) for v in (1.,0.,0.,0.,0.)]
        reference_history = [constant(v,0) for v in (0.,0.,0.,0.,0.,0.,0.,1.)]
        self.nuhat_scale = max(LD(1),potential.energy(reference_geometry,reference_history).value)
        self.coordinates = FiniteCoordinates(self.nuhat_scale)
        self.calls = self.jacobian_calls = self.points = 0
        self.direct_state_evaluations = self.derivative_state_evaluations = 0

    def jets(self,state,parameters,dimension):
        values = list(state)+list(parameters)
        if dimension:
            eye = np.eye(len(values),dtype=LD)
            return [Jet(value,eye[i]) for i,value in enumerate(values)]
        return [constant(value,0) for value in values]

    def one(self,state,parameters,derivatives=False):
        self.direct_state_evaluations += 1
        self.derivative_state_evaluations += int(derivatives)
        if (not np.all(np.isfinite(state)) or not np.all(np.isfinite(parameters))
                or np.max(np.abs(state))>1.e100 or np.max(np.abs(parameters))>1.e100):
            raise FloatingPointError("The finite-coordinate Newton trial is not finite")
        jets = self.jets(state,parameters,29 if derivatives else 0)
        ys,ps = jets[:19],jets[19:]
        geo,chart = self.coordinates.physical(ys)
        center_geo,center_a,nuhat,length = self.coordinates.center(ps)
        h,k,eta,gamma,upsilon = geo
        aa = ys[5:13]
        neg = [h,-k,-eta,-gamma,upsilon]
        aneg = [sign*value for sign,value in zip(JPAR,aa)]
        op = self.coefficients.evaluate_jets(geo,aa)
        om = self.coefficients.evaluate_jets(neg,aneg)
        wp,wm = weights(geo),weights(neg)
        ep = self.potential.energy(geo,aa)
        em = self.potential.energy(neg,aneg)
        hp,kp,hm,km = op[1],op[2],om[1],om[2]
        determinant = -hp*km-hm*kp
        if not (hp.value<0 and hm.value<0 and kp.value>0 and km.value>0
                and determinant.value>0):
            raise FloatingPointError("The actual Ch/Ck sign domain failed")
        fp = op[0]-4*dot(wp,ys[13:16])-4*ep-2*dot(wp,nuhat)
        fm = om[0]-4*dot(wm,ys[16:19])-4*em-2*dot(wm,nuhat)
        acc = (km*fp+kp*fm)/determinant
        bcc = (hm*fp-hp*fm)/determinant
        qg = 1+(h*eta-k)**2
        out = [gamma/chart[0],upsilon/chart[1],upsilon/(2*h*chart[2]),
               acc/chart[3],bcc/chart[4]]
        out.extend(density(geo))
        out.extend((op[3+3*j]+acc*op[4+3*j]+bcc*op[5+3*j])/qg**2 for j in range(3))
        out.extend(-(om[3+3*j]+acc*om[4+3*j]-bcc*om[5+3*j])/qg**2 for j in range(3))
        out = [length*v for v in out]
        value,jacobian = values_and_jacobian(out)
        if not np.all(np.isfinite(value)) or not np.all(np.isfinite(jacobian)):
            raise FloatingPointError("A complete C2 state derivative is not finite")
        return np.asarray(value,dtype=float),np.asarray(jacobian,dtype=float)

    def __call__(self,x,states,parameters):
        self.calls += 1
        self.points += states.shape[1]
        return np.column_stack([self.one(states[:,i],parameters)[0] for i in range(states.shape[1])])

    def jacobian(self,x,states,parameters):
        self.jacobian_calls += 1
        answers = [self.one(states[:,i],parameters,True)[1] for i in range(states.shape[1])]
        stacked = np.stack(answers,axis=2)
        return stacked[:,:19],stacked[:,19:]

    def boundary(self,left,right,parameters):
        zero = lambda values: [constant(v,0) for v in values]
        lgeo,_ = self.coordinates.physical(zero(left))
        rgeo,_ = self.coordinates.physical(zero(right))
        center,aa,nuhat,length = self.coordinates.center(zero(parameters))
        answer = [lgeo[0]-center[0],lgeo[1],lgeo[2],lgeo[3],lgeo[4]-center[4]]
        answer.extend(a-b for a,b in zip(zero(left[5:13]),aa))
        answer.extend(zero(left[13:19]))
        answer.extend(zero(right[5:13]))
        answer.extend(rgeo[3:5])
        return np.asarray([v.value for v in answer],dtype=float)

    def boundary_jacobian(self,left,right,parameters):
        allvalues = list(left)+list(right)+list(parameters)
        eye = np.eye(48,dtype=LD)
        js = [Jet(v,eye[i]) for i,v in enumerate(allvalues)]
        lgeo,_ = self.coordinates.physical(js[:19])
        rgeo,_ = self.coordinates.physical(js[19:38])
        center,aa,nuhat,length = self.coordinates.center(js[38:])
        answer = [lgeo[0]-center[0],lgeo[1],lgeo[2],lgeo[3],lgeo[4]-center[4]]
        answer.extend(a-b for a,b in zip(js[5:13],aa))
        answer.extend(js[13:19])
        answer.extend(js[24:32])
        answer.extend(rgeo[3:5])
        derivative = np.asarray([v.derivative for v in answer],dtype=float)
        return derivative[:,:19],derivative[:,19:38],derivative[:,38:]


def seed(rhs,args):
    """A new three-half-wave guide, with exact analytic integral of h*k zero.

    A and rho guesses are integrated from the true center along this guide.
    They are not adjusted algebraically to fake the original ruling.
    """
    x = np.linspace(0.,1.,args.nodes)
    theta = np.pi*x/2
    sine,cosine = np.sin(theta),np.cos(theta)
    hh,pp,ll,kk = args.height,args.peak,args.length,args.curvature
    delta = pp-hh
    c = (hh/3-8*delta/35)/(hh+8*delta/15)
    h = hh+delta*sine**4
    hx = 2*np.pi*delta*sine**3*cosine
    hxx = np.pi**2*delta*(3*sine**2*cosine**2-sine**4)
    k = kk*(np.sin(3*theta)-c*sine)
    kx = kk*np.pi/2*(3*np.cos(3*theta)-c*cosine)
    kxx = -kk*(np.pi/2)**2*(9*np.sin(3*theta)-c*sine)
    eta = cumulative_simpson(kx/(2*h),x=x,initial=0.)
    gamma,upsilon,aa,bb = hx/ll,kx/ll,hxx/ll**2,kxx/ll**2
    v0 = float(upsilon[0])
    par = np.zeros(10)
    par[0] = np.tan(np.pi*(hh-float(rhs.coordinates.hmid))/(2*float(rhs.coordinates.hcap)))
    par[1] = np.tan(np.pi*v0/(2*float(rhs.coordinates.vcap)))
    par[9] = np.tan(np.pi*(ll-float(rhs.coordinates.lmid))/(2*float(rhs.coordinates.lcap)))
    center_geo,center_history,nuhat,length = rhs.coordinates.center([constant(v,0) for v in par])
    center_values = np.asarray([v.value for v in center_history],dtype=float)
    geometry = np.array([h,k,eta,gamma,upsilon])
    rates = np.array([old.core.matrix_density(*geometry[:,i]) for i in range(len(x))]).T
    history = center_values[:,None]+ll*cumulative_simpson(rates,x=x,axis=1,initial=0.)
    states = np.zeros((19,len(x)))
    for i in range(len(x)):
        states[:5,i] = rhs.coordinates.encode(geometry[:,i])
    states[5:13] = history
    opcenter = rhs.coefficients.evaluate(tuple(v.value for v in center_geo),center_values)
    center_energy = rhs.potential.energy(center_geo,center_history).value
    par[6] = float((opcenter[0]+opcenter[1]*aa[0]-4*center_energy)
                   /(2*old.weights(hh,0.,0.)[0]*rhs.nuhat_scale))
    rp,rm = [],[]
    for i in range(len(x)):
        geo = tuple(geometry[:,i])
        neg = (h[i],-k[i],-eta[i],-gamma[i],upsilon[i])
        op = rhs.coefficients.evaluate(geo,history[:,i])
        om = rhs.coefficients.evaluate(neg,JPAR*history[:,i])
        rp.append(rhs.coefficients.history_rhs(op,geo,aa[i],bb[i]))
        rm.append(-rhs.coefficients.history_rhs(om,neg,aa[i],-bb[i]))
    states[13:16] = ll*cumulative_simpson(np.asarray(rp).T,x=x,axis=1,initial=0.)
    states[16:19] = ll*cumulative_simpson(np.asarray(rm).T,x=x,axis=1,initial=0.)
    meta = {"height":hh,"length":ll,"peak":pp,"curvature":kk,"three_half_wave_c":c,
            "center_v0":v0,"prepared_center_Aodd":center_values[ODD].tolist(),
            "prepared_center_positive_energy":float(center_energy),
            "fixed_nuhat_parameter_scale":float(rhs.nuhat_scale),
            "seed_nuhat":[float(rhs.nuhat_scale*q) for q in par[6:9]],
            "sampled_endpoint_A":history[:,-1].tolist(),
            "sampled_eta_range":[float(eta.min()),float(eta.max())],
            "exact_guide_integral_hk_zero":True,
            "guide_is_actual_ruling_trajectory":False}
    return x,states,par,meta


def derivative_gate(rhs,states,parameters):
    """New derivative check, all in the public run, before the actual BVP."""
    point = states[:,len(states[0])//2]
    value,jac = rhs.one(point,parameters,True)
    joint = np.concatenate((point,parameters))
    directions = [np.sin(np.arange(1,30)*rate) for rate in (0.7,1.3)]
    entries = []
    for d in directions:
        d /= np.linalg.norm(d)
        exact = jac@d
        errors = []
        for step in (1.e-6,1.e-7):
            plus,minus = joint+step*d,joint-step*d
            vp = rhs.one(plus[:19],plus[19:])[0]
            vm = rhs.one(minus[:19],minus[19:])[0]
            numerical = (vp-vm)/(2*step)
            errors.append(float(np.linalg.norm(numerical-exact,np.inf)/
                                max(1.,np.linalg.norm(exact,np.inf),np.linalg.norm(numerical,np.inf))))
        entries.append(errors)
    worst = max(min(row) for row in entries)
    result = {"directional_relative_errors":entries,"best_step_worst_direction":worst,
              "analytic_value_finite":bool(np.all(np.isfinite(value))),
              "actual_ODE_and_boundary_equations_unchanged":True}
    if worst>2.e-5:
        raise RuntimeError("The new analytic Jacobian directional check did not meet its gate")
    return result


def inspect(rhs,solution):
    x = np.unique(np.concatenate((solution.x,(solution.x[:-1]+solution.x[1:])/2)))
    state = solution.sol(x)
    center,ac,nuhat,length = rhs.coordinates.center([constant(v,0) for v in solution.p])
    ll = float(length.value)
    derivative = solution.sol(x,1)/ll
    cg = tuple(v.value for v in center)
    ca = np.asarray([v.value for v in ac],dtype=float)
    center_outputs = rhs.coefficients.evaluate(cg,ca)
    ec = np.asarray(center_outputs[16:19]/(1+(cg[0]*cg[2]-cg[1])**2),dtype=float)
    rc = rhs.coefficients.center_shift(cg,ca)
    nuhat_value = np.asarray([v.value for v in nuhat],dtype=float)
    nubar_value = nuhat_value+2*ec
    original_nu = nubar_value-2*rc
    kin,mat,third,original_third,ruling,recovered_ruling = [],[],[],[],[],[]
    geometries = []
    energy_values = []
    for i in range(len(x)):
        geo,chart = rhs.coordinates.physical([constant(v,0) for v in state[:,i]])
        gp = tuple(v.value for v in geo)
        physical_derivative = np.asarray([v.value for v in chart],dtype=float)*derivative[:5,i]
        h,k,eta,gamma,upsilon = gp
        aa,bb = physical_derivative[3:5]
        an = state[5:13,i]
        gm = (h,-k,-eta,-gamma,upsilon)
        op,om = rhs.coefficients.evaluate(gp,an),rhs.coefficients.evaluate(gm,JPAR*an)
        wp,wm = old.weights(h,k,eta),old.weights(h,-k,-eta)
        posjets=[constant(v,0) for v in gp]
        negjets=[constant(v,0) for v in gm]
        ajets=[constant(v,0) for v in an]
        anjets=[constant(v,0) for v in JPAR*an]
        ep = rhs.potential.energy(posjets,ajets).value
        em = rhs.potential.energy(negjets,anjets).value
        ruling.append([float(op[0]+op[1]*aa+op[2]*bb)-4*wp@state[13:16,i]-4*float(ep)-2*wp@np.asarray([v.value for v in nuhat],dtype=float),
                       float(om[0]+om[1]*aa-om[2]*bb)-4*wm@state[16:19,i]-4*float(em)-2*wm@np.asarray([v.value for v in nuhat],dtype=float)])
        kin.append(physical_derivative[:3]-np.array([gamma,upsilon,upsilon/(2*h)]))
        mat.append(derivative[5:13,i]-old.core.matrix_density(*gp))
        regularized_defect=np.concatenate((
            derivative[13:16,i]-rhs.coefficients.history_rhs(op,gp,aa,bb),
            derivative[16:19,i]+rhs.coefficients.history_rhs(om,gm,aa,-bb)))
        third.append(regularized_defect)
        model_geometry=np.array([gamma,upsilon,upsilon/(2*h),aa,bb])
        model_history=old.core.matrix_density(*gp)
        original_correction=[]
        for sign_geometry,sign_history in ((np.ones(5),np.ones(8)),
                                           (np.array([1.,-1.,-1.,-1.,1.]),JPAR)):
            gj=[Jet(v*sg,[dc*sg,dm*sg]) for v,dc,dm,sg in
                zip(gp,physical_derivative,model_geometry,sign_geometry)]
            aj=[Jet(v*sg,[dc*sg,dm*sg]) for v,dc,dm,sg in
                zip(an,derivative[5:13,i],model_history,sign_history)]
            ej=rhs.coefficients.evaluate_jets(gj,aj)
            qgj=1+(gj[0]*gj[2]-gj[1])**2
            original_correction.extend(float((ej[16+j]/qgj).derivative[0]
                                             -(ej[16+j]/qgj).derivative[1]) for j in range(3))
        original_third.append(regularized_defect+np.asarray(original_correction))
        qgn=1+(h*eta-k)**2
        sp=state[13:16,i]+np.asarray(op[16:19]/qgn,dtype=float)-ec
        sm=state[16:19,i]+np.asarray(om[16:19]/qgn,dtype=float)-ec
        nb=nubar_value
        recovered_ruling.append([float(op[0]+op[1]*aa+op[2]*bb)-4*wp@sp-2*wp@nb,
                                 float(om[0]+om[1]*aa-om[2]*bb)-4*wm@sm-2*wm@nb])
        geometries.append([float(v) for v in gp])
        energy_values.append([float(ep),float(em)])
    geom=np.asarray(geometries).T
    last=geom[:,-1]
    ap=state[5:13,-1]
    gm=(last[0],-last[1],-last[2],-last[3],last[4])
    eplus=rhs.coefficients.evaluate(tuple(last),ap)[16:19]/(1+(last[0]*last[2]-last[1])**2)
    eminus=rhs.coefficients.evaluate(gm,JPAR*ap)[16:19]/(1+(last[0]*last[2]-last[1])**2)
    sigma_plus=state[13:16,-1]+np.asarray(eplus,dtype=float)-ec
    sigma_minus=state[16:19,-1]+np.asarray(eminus,dtype=float)-ec
    rend_plus=rhs.coefficients.center_shift(tuple(last),ap)
    rend_minus=rhs.coefficients.center_shift(gm,JPAR*ap)
    t_end_difference=sigma_plus-sigma_minus-rend_plus+rend_minus
    first=geom[:,0]
    a_first=state[5:13,0]
    first_minus=(first[0],-first[1],-first[2],-first[3],first[4])
    center_t=[]
    for gg,ah,rho_value in ((tuple(first),a_first,state[13:16,0]),
                            (first_minus,JPAR*a_first,state[16:19,0])):
        oo=rhs.coefficients.evaluate(gg,ah)
        ee=np.asarray(oo[16:19]/(1+(gg[0]*gg[2]-gg[1])**2),dtype=float)
        rr=rhs.coefficients.center_shift(gg,ah)
        center_t.append((rho_value+ee-ec-rr+rc).tolist())
    return {"status":int(solution.status),"success":bool(solution.success),"message":str(solution.message),
            "mesh_nodes":len(solution.x),"iterations":int(solution.niter),
            "max_scipy_rms_relative_residual":float(np.max(solution.rms_residuals)),
            "boundary_max_abs":float(np.max(np.abs(rhs.boundary(state[:,0],state[:,-1],solution.p)))),
            "actual_height":float(cg[0]),"actual_length":ll,"center_v0":float(cg[4]),
            "actual_center_Aodd":ca[ODD].tolist(),"center_r":rc.tolist(),"center_E":ec.tolist(),
            "nubar":nubar_value.tolist(),"nuhat":nuhat_value.tolist(),
            "nuhat_parameter_scale":float(rhs.nuhat_scale),
            "actual_fixed_nu":original_nu.tolist(),
            "eight_endpoint":ap.tolist(),"two_velocity_endpoint":last[3:5].tolist(),
            "endpoint_E_plus":np.asarray(eplus,dtype=float).tolist(),
            "endpoint_E_minus":np.asarray(eminus,dtype=float).tolist(),
            "recovered_center_t_plus_minus":center_t,
            "three_T_projection_difference_between_centers":t_end_difference.tolist(),
            "actual_reanchored_chi_Gram":(nubar_value+2*sigma_minus-2*rend_minus).tolist(),
            "full_reanchored_T_period_not_evaluated":True,
            "geometry_ranges":{name:[float(v.min()),float(v.max())]
                               for name,v in zip(("h","k","eta","gamma","upsilon"),geom)},
            "sampled_actual_kinematic_defect_max":float(np.max(np.abs(kin))),
            "sampled_actual_matrix_ODE_defect_max":float(np.max(np.abs(mat))),
            "sampled_complete_regularized_third_ODE_defect_max":float(np.max(np.abs(third))),
            "sampled_original_sigma_third_ODE_defect_max":float(np.max(np.abs(original_third))),
            "sampled_original_ruling_with_paid_square_max":float(np.max(np.abs(ruling))),
            "sampled_original_ruling_via_recovered_sigma_max":float(np.max(np.abs(recovered_ruling))),
            "paid_square_vs_recovered_sigma_discrepancy_max":float(np.max(np.abs(
                np.asarray(ruling)-np.asarray(recovered_ruling)))),
            "sampled_current_positive_energy_max":float(np.max(np.abs(energy_values))),
            "rhs_calls":rhs.calls,"jacobian_calls":rhs.jacobian_calls,"rhs_points":rhs.points,
            "all_direct_state_evaluations":rhs.direct_state_evaluations,
            "all_derivative_state_evaluations":rhs.derivative_state_evaluations,
            "exact_root_rank_pose_period_reach_claim":False}


def pose_readout(rhs,solution):
    center,aa,nuhat,length=rhs.coordinates.center([constant(v,0) for v in solution.p])
    ll=float(length.value)
    def geometry_at(s):
        gg,_=rhs.coordinates.physical([constant(v,0) for v in solution.sol(s/ll)])
        return np.asarray([v.value for v in gg],dtype=float)
    def ode(s,state):
        h,k=geometry_at(s)[:2]
        frame=state[:9].reshape(3,3)
        omega=np.array([[0.,-k,0.],[k,0.,1.],[0.,-1.,0.]])
        return np.concatenate(((frame@omega).ravel(),h*h*frame[:,0]))
    start=np.concatenate((np.eye(3).ravel(),np.zeros(3)))
    recovered=solve_ivp(ode,(0.,ll),start,method="DOP853",rtol=1.e-9,atol=1.e-11,dense_output=True)
    if not recovered.success:
        return {"frame_ODE_success":False,"message":str(recovered.message)}
    times=np.linspace(0.,ll,401)
    posed=recovered.sol(times)
    frame=posed[:9].T.reshape(-1,3,3)
    alpha=posed[9:].T
    geo=np.array([geometry_at(s) for s in times])
    h,eta=geo[:,0],geo[:,2]
    normal=frame[:,:,1]
    edges=[]
    db=np.array([-1.,-1.,1.])
    for y in (4.,6.):
        edges.append(alpha+h[:,None]/(y+eta)[:,None]*normal)
        edges.append(db*(alpha-h[:,None]/(y-eta)[:,None]*normal))
    points=np.concatenate(edges)
    center_b=(points[:,2].min()+points[:,2].max())/2
    radius=np.linalg.norm(points-np.array([0.,0.,center_b]),axis=1).max()
    n,v=normal[-1],alpha[-1]
    return {"frame_ODE_success":True,"sample_count":401,
            "four_actual_edges_sampled_radius":float(radius),"B_axis_ball_center":float(center_b),
            "two_true_pose_readouts":[float(n[2]**2-.5),float(v[0]*n[1]-v[1]*n[0])],
            "frame_orthogonality_defect":float(np.linalg.norm(frame[-1].T@frame[-1]-np.eye(3))),
            "continuous_reach_or_pose_return_claim":False}


def trial(coefficients,potential,args):
    started=time.time()
    rhs=FullC2RHS(coefficients,potential)
    result={"scope":"New actual free-H/L ten-endpoint BVP, full positive square retained",
            "surrogate_or_dropped_potential_used":False,"exact_root_claim":False}
    try:
        x,states,parameters,seedmeta=seed(rhs,args)
        result["seed"]=seedmeta
        emit("R590_NEW_SEED",seedmeta)
        result["new_analytic_derivative_gate"]=derivative_gate(rhs,states,parameters)
        emit("R590_NEW_DERIVATIVE_GATE",result["new_analytic_derivative_gate"])
        sol=solve_bvp(rhs,rhs.boundary,x,states,p=parameters,
                      fun_jac=rhs.jacobian,bc_jac=rhs.boundary_jacobian,
                      tol=args.tol,bc_tol=args.bc_tol,max_nodes=args.max_nodes,verbose=0)
        result["coarse"]=inspect(rhs,sol)
        emit("R590_NEW_COARSE",result["coarse"])
        continue_same=(sol.status==1 and np.all(np.isfinite(sol.y))
                       and float(np.max(sol.rms_residuals))<0.2)
        if sol.success or continue_same:
            fine=solve_bvp(rhs,rhs.boundary,sol.x,sol.y,p=sol.p,
                           fun_jac=rhs.jacobian,bc_jac=rhs.boundary_jacobian,
                           tol=args.refine_tol,bc_tol=args.bc_tol,
                           max_nodes=args.refine_max_nodes,verbose=0)
            result["refined"]=inspect(rhs,fine)
            if fine.success:
                result["pose_readout"]=pose_readout(rhs,fine)
    except Exception as error:
        result["failure"]={"type":type(error).__name__,"message":str(error)}
        result["rhs_calls"],result["jacobian_calls"],result["rhs_points"]=rhs.calls,rhs.jacobian_calls,rhs.points
    result["elapsed_seconds"]=time.time()-started
    result["all_direct_state_evaluations"]=rhs.direct_state_evaluations
    result["all_derivative_state_evaluations"]=rhs.derivative_state_evaluations
    return result


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("--orders",default="96,192")
    parser.add_argument("--gap-order",type=int,default=8)
    parser.add_argument("--height",type=float,default=1.05)
    parser.add_argument("--length",type=float,default=4.)
    parser.add_argument("--peak",type=float,default=2.8)
    parser.add_argument("--curvature",type=float,default=1.8)
    parser.add_argument("--nodes",type=int,default=33)
    parser.add_argument("--max-nodes",type=int,default=321)
    parser.add_argument("--refine-max-nodes",type=int,default=961)
    parser.add_argument("--tol",type=float,default=1.e-4)
    parser.add_argument("--bc-tol",type=float,default=1.e-10)
    parser.add_argument("--refine-tol",type=float,default=1.e-6)
    args=parser.parse_args()
    if (os.environ.get("GITHUB_ACTIONS")!="true"
            or os.environ.get("GITHUB_REPOSITORY")!="Rogerhu12/math-research-public"):
        raise RuntimeError("New science is scheduled only in the public repository Actions")
    started=time.time()
    labels,polynomials,original,formal=regularized_bundle()
    emit("R590_COMPLETE_FORMAL",formal)
    coefficients=potential=None
    previous=None
    probe_geometry=(1.17,.23,.08,.11,-.31)
    probe_history=(.02,-.013,.017,.019,-.007,.011,-.009,.014)
    for order in (int(n) for n in args.orders.split(",")):
        grid=old.ReferenceGrid(order,args.gap_order,5.)
        coefficients=DifferentiableCoefficients(labels,polynomials,grid)
        potential=PositivePotentialGram(grid)
        outputs=np.asarray(coefficients.evaluate(probe_geometry,probe_history),dtype=float)
        geo=[constant(v,0) for v in probe_geometry]
        aa=[constant(v,0) for v in probe_history]
        exact_positive=potential.energy(geo,aa).value
        expanded=old.weights(*probe_geometry[:3])@(outputs[16:19]/(1+(probe_geometry[0]*probe_geometry[2]-probe_geometry[1])**2))
        row={"quadrature_order":order,"coefficient_stats":coefficients.stats,
             "positive_Gram_stats":potential.stats,"labels":labels,"full_probe":outputs.tolist(),
             "complete_C2_history_rhs_probe":coefficients.history_rhs(outputs,probe_geometry,.47,-.29).tolist(),
             "positive_square_probe":float(exact_positive),"expanded_E_pairing_probe":float(expanded),
             "positive_vs_expanded_relative":float(abs(exact_positive-expanded)/max(1.,abs(exact_positive))),
             "old_raw_local_R581_replayed":False}
        if previous is not None:
            row["same_input_probe_difference"]=(outputs-previous).tolist()
        emit("R590_COMPLETE_COEFFICIENTS",row)
        previous=outputs
        gc.collect()
    emit("R590_NEW_ACTUAL_BVP",trial(coefficients,potential,args))
    emit("R590_DONE",{"elapsed_seconds":time.time()-started,
                      "actual_ten_endpoint_root_claim":False,"README_completion_claim":False})


if __name__=="__main__":
    main()

