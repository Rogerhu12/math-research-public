#!/usr/bin/env python3
"""R584/R586 full nineteen-state boundary value experiment.

Exact rational Laurent compilation precedes fixed-profile quadrature.
All six original third-history projections remain, in the reversible centered
coordinates of R584. No R480 outer quotient or fourth-period claim is used.
New scientific execution is restricted to the declared public Actions repository.
"""
from __future__ import annotations

import argparse
from dataclasses import dataclass
from fractions import Fraction as QF
import gc
import hashlib
import json
import os
import time

import numpy as np
from scipy.integrate import cumulative_simpson, solve_bvp, solve_ivp

import r530_c2_r578_evaluator_agent as c2
import r530_compact_history_v2_agent as core


# Profile coordinates, then geometry, then the eight actual A coordinates.
IX, IU, IP, IR, IT, IJ0, IJ1, IJ2, IC, ID = range(10)
IH, IK, IE, IG, IV, IA, IB = range(10, 17)
AA = tuple(range(17, 25))
NV = 25
ZERO = (0,)*NV


class Poly:
    """Exact sparse Laurent polynomial; negative powers only in h."""
    def __init__(self, terms=None):
        self.terms = {k: QF(v) for k, v in (terms or {}).items() if v}

    @classmethod
    def constant(cls, value):
        return cls({ZERO: QF(value)})

    @classmethod
    def variable(cls, index):
        key = list(ZERO)
        key[index] = 1
        return cls({tuple(key): QF(1)})

    @staticmethod
    def coerce(value):
        return value if isinstance(value, Poly) else Poly.constant(value)

    def __add__(self, other):
        other = self.coerce(other)
        out = dict(self.terms)
        for key, value in other.terms.items():
            new = out.get(key, QF(0)) + value
            if new:
                out[key] = new
            else:
                out.pop(key, None)
        return Poly(out)

    __radd__ = __add__

    def __neg__(self):
        return Poly({key: -value for key, value in self.terms.items()})

    def __sub__(self, other):
        return self + (-self.coerce(other))

    def __rsub__(self, other):
        return self.coerce(other) - self

    def __mul__(self, other):
        other = self.coerce(other)
        out = {}
        for x, a in self.terms.items():
            for y, b in other.terms.items():
                key = tuple(i+j for i, j in zip(x, y))
                out[key] = out.get(key, QF(0)) + a*b
        return Poly(out)

    __rmul__ = __mul__

    def __truediv__(self, other):
        other = self.coerce(other)
        if len(other.terms) != 1:
            raise TypeError("Only exact Laurent monomial division is allowed")
        key, value = next(iter(other.terms.items()))
        out = {}
        for old, coefficient in self.terms.items():
            new = tuple(i-j for i, j in zip(old, key))
            if any(power < 0 for i, power in enumerate(new) if i != IH):
                raise TypeError("Negative Laurent exponent outside h")
            out[new] = coefficient/value
        return Poly(out)

    def __rtruediv__(self, other):
        return self.coerce(other)/self

    def __pow__(self, n):
        if not isinstance(n, int):
            raise TypeError("Integer power required")
        if n < 0:
            return Poly.constant(1)/(self**(-n))
        out = Poly.constant(1)
        factor = self
        while n:
            if n & 1:
                out = out*factor
            n //= 2
            if n:
                factor = factor*factor
        return out

    def partial(self, index):
        out = {}
        for key, value in self.terms.items():
            power = key[index]
            if power:
                new = list(key)
                new[index] -= 1
                out[tuple(new)] = value*power
        return Poly(out)

    def primitive(self, index):
        out = {}
        for key, value in self.terms.items():
            new = list(key)
            new[index] += 1
            if new[index] == 0:
                raise TypeError("Logarithmic primitive is not in this compiler")
            out[tuple(new)] = value/new[index]
        return Poly(out)

    def coefficient(self, index, degree):
        out = {}
        for key, value in self.terms.items():
            if key[index] == degree:
                new = list(key)
                new[index] = 0
                out[tuple(new)] = value
        return Poly(out)


X,U,P,R,T,J0,J1,J2,C,D,H,K,E,G,V,ACC,BCC = [Poly.variable(i) for i in range(17)]
AVAR = [Poly.variable(i) for i in AA]


def d0(poly):
    return (poly.partial(IX)+P*poly.partial(IU)+R*poly.partial(IP)
            -D*R**2*poly.partial(IJ0)-X*D*R**2*poly.partial(IJ1)
            -D*(X**2*R**2+2*P**2)*poly.partial(IJ2))


def dx_c2(poly):
    if any(key[IT] for key in poly.terms):
        raise ValueError("dx_c2 was asked to differentiate a third derivative")
    return d0(poly)+T*poly.partial(IR)


def matrix_poly():
    dg = H*E-K
    ds = G*E-V/2
    qg = 1+dg**2
    a1 = 2*K*E-(K*K+1)/H
    a0 = K*E*E-(K*K+1)*E/H
    p0,p1,p2 = -K*qg/(2*H),-K*dg,-K*H/2
    common = G*qg/H-2*dg*ds
    r0 = (a0*qg+ds*common/H**2)/(8*H)
    r1 = (a1*qg+G*common/H**2)/(8*H)
    s0 = (a0*dg-ds**2/H**2)/4
    s1 = (a1*dg-G*ds/H**2)/4
    t1 = (H*a1-G**2/H**2)/8
    return [p0,p1,p2,t1,r1,s1,s0,r0]


def dt(poly, matrix=None):
    out = (G*poly.partial(IH)+V*poly.partial(IK)
           +V*poly.partial(IE)/(2*H)
           +ACC*poly.partial(IG)+BCC*poly.partial(IV))
    if matrix is not None:
        for index, density in zip(AA, matrix):
            out += density*poly.partial(index)
    return out


def dot(left, right):
    return sum((a*b for a,b in zip(left,right)), Poly())


def omega(vector):
    return (-K*vector[1], K*vector[0]+vector[2], -vector[1])


def covariant(vector):
    return tuple(dt(a)+b for a,b in zip(vector,omega(vector)))


def e8_coefficients(m):
    p0,p1,p2,t1,r1,s1,s0,r0 = m
    t0 = p0/4+s1/2
    return (-p1/2-p2*X,
            p0+p1*X+p2*X**2,
            r1+(s1-p0/2)*X+(t1-p1/2)*X**2-p2*X**3/2,
            r0+r1*X-p0*X**2/4,
            s0+s1*X-p1*X**2/4,
            t0+t1*X-p2*X**2/4)


def q_profile(m):
    a0,a1,a2,b0,b1,b2 = e8_coefficients(m)
    return a0*D*U**2+a1*D*U*P+a2*D*P**2+b0*J0+b1*J1+b2*J2


def fields():
    z = X+E
    e = H*z-K
    q = 1+e**2
    es = G*z-V/2
    dg = H*E-K
    ah = (2*q*D*P*R-z*q*D*R**2-2*H*e*D*P**2
          +(1+K*K-H*H*E*E)*J0-2*H*H*E*J1-H*H*J2)/(16*H**2)
    ak = (q*D*R**2+2*H*(H*J1+dg*J0))/(32*H**2)
    eta = G*ah+V*ak
    etax = D*q*(G*P-es*R)*T/(8*H**2)
    ptail = ((1+dg*dg)*J0+2*H*dg*J1+H*H*J2)/(8*H)+e*D*P**2/8
    bb = D*(P**2/4+(H*U-e*P/2)**2)/(2*H)
    px = -D*(R**2/4+(H*P/2-e*R/2)**2)/(2*H)
    bx = D*(P*R/4+(H*U-e*P/2)*(H*P/2-e*R/2))/H
    ky0 = (eta/H,z*ptail+bb,e*eta/H)
    ky1 = (etax/H,ptail+z*px+bx,eta+e*etax/H)
    gy0 = (-C*P/2,Poly(),C*(H*U-e*P/2))
    gy1 = (-C*R/2,Poly(),C*(H*P/2-e*R/2))
    return dict(z=z,e=e,q=q,es=es,ky0=ky0,ky1=ky1,gy0=gy0,gy1=gy1,
                kc0=covariant(ky0),kc1=covariant(ky1),
                gc0=covariant(gy0),gc1=covariant(gy1))


def local_ruling(ff, m):
    e,q,es = ff["e"],ff["q"],ff["es"]
    gy0,gy1,ky0,ky1 = (ff[k] for k in ("gy0","gy1","ky0","ky1"))
    gc0,gc1,kc0,kc1 = (ff[k] for k in ("gc0","gc1","kc0","kc1"))
    tt = dot(gy1,ky1)
    uu = dot(gy1,ky0)+dot(gy0,ky1)
    vv = dot(gc0,ky1)+dot(kc0,gy1)
    ww = dot(gc1,ky1)+dot(gy1,kc1)
    fp = C*(q*R-2*H*e*P+2*H**2*U)
    fpx = C*q*T
    qm = q_profile(m)
    qmx = dx_c2(qm)
    raw = (-dot(ky1,ky1)/H-fpx*vv/(2*H**3)-es*fpx*tt/(2*H**4)
           +G*fpx*uu/(2*H**4)-fp*ww/(2*H**3)+G*fp*tt/(2*H**4)
           -fp*C*T*(q*qmx-2*H*e*qm)/(8*H**3))
    expected = -(D**2+2*C**2*D)*q**3*(G*P-es*R)**2/(64*H**7)
    if (raw.coefficient(IT,2)-expected).terms:
        raise RuntimeError("Exact R581 highest coefficient identity failed")
    if any(key[IT]>2 for key in raw.terms):
        raise RuntimeError("Unexpected high spatial derivative degree")
    low = raw.coefficient(IT,0)-d0(raw.coefficient(IT,1).primitive(IR))
    return low


def test_primitive(j, aa):
    if any(key[IX]>2 or any(key[i] for i in range(1,10)) for key in aa.terms):
        raise ValueError("R586 transposed coefficient is not quadratic in position")
    w = X**j*aa
    v = 2*j*X**(j-1)*aa if j else Poly()
    w1,w2,w3 = w.partial(IX),w.partial(IX).partial(IX),w.partial(IX).partial(IX).partial(IX)
    v1,v2 = v.partial(IX),v.partial(IX).partial(IX)
    if (w3.partial(IX)-v2.partial(IX)).terms:
        raise RuntimeError("Exact transposed primitive identity failed")
    return w*C*T+(v-w1)*C*R+(w2-v1)*C*P+(v2-w3)*C*U


def third_local(ff,m):
    z,e,q,es = (ff[k] for k in ("z","e","q","es"))
    gy0,gy1,ky0,ky1 = (ff[k] for k in ("gy0","gy1","ky0","ky1"))
    gc0,gc1,kc0,kc1 = (ff[k] for k in ("gc0","gc1","kc0","kc1"))
    tt = dot(gy1,ky1)
    ww = dot(gc1,ky1)+dot(gy1,kc1)
    u0 = dot(gy0,ky0)
    v0 = dot(gc0,ky0)+dot(gy0,kc0)
    n0 = dot(gc0,kc0)
    mu = V/(2*H)-G*K/H**2
    v = q_profile(m)
    vp = dx_c2(v)
    vpp = dx_c2(vp)
    cloc = (n0/(2*H**2)+(K*z-(K*K+1)/H)*u0/(2*H)
            -G*v0/(2*H**3)+G*G*u0/(2*H**4)
            -mu*C*P*v/4+G*q*C*P*vp/(8*H**3))
    at = (K*z*z-(K*K+1)*z/H)/(2*H)+G*es/(2*H**4)
    aw,aj = -es/(2*H**3),es/(8*H**3)
    return [-test_primitive(j,Poly.constant(1))*dx_c2(cloc)
            +test_primitive(j,at)*tt+test_primitive(j,aw)*ww
            +test_primitive(j,aj)*(q*C*R*vpp+2*H*H*C*P*vp)
            for j in range(3)]


def ordered_B(m,qa,qap,qapp):
    a0,a1,a2,b0,b1,b2 = e8_coefficients(m)
    loc = a0*C*U*qa+a1*(C*U*qap+C*P*qa)/2+a2*C*P*qap
    return [-test_primitive(j,Poly.constant(1))*dx_c2(loc)
            +(test_primitive(j,b0)+X*test_primitive(j,b1)
              +X**2*test_primitive(j,b2))*C*R*qapp
            +2*test_primitive(j,b2)*C*P*qap
            for j in range(3)]


def gram(leftp,leftpp,rightp,rightpp):
    return [X**j*leftpp*rightpp+(2*leftp*rightp if j==2 else 0)
            for j in range(3)]


def linear_history(ff,qa,qap,qapp):
    e,q,es = ff["e"],ff["q"],ff["es"]
    h1 = D*(q**2*(2*G*P*R-es*R**2)-2*H*G*e*q*P**2)
    h2 = D*((G*q-2*H*e*es)*R**2-2*H*H*G*P**2)
    tq = (-qapp*dx_c2(h1)+(q*qapp-2*H*e*qap+2*H*H*qa)*h2)/(32*H**4)
    fg = C*(q*R-2*H*e*P+2*H*H*U)
    tg = (q**2*C*T*(G*(C*P*qapp+C*R*qap)-es*C*R*qapp)
          -2*H*G*e*q*C*T*C*P*qap
          +fg*((G*q-2*H*e*es)*C*R*qapp-2*H*H*G*C*P*qap))/(32*H**4)
    return 2*tq-4*tg


def angular_average(poly):
    out = {}
    for key,coefficient in poly.terms.items():
        degree = key[ID]+key[IJ0]+key[IJ1]+key[IJ2]
        profile_degree = sum(key[i] for i in (IU,IP,IR,IT))+2*sum(key[i] for i in (IJ0,IJ1,IJ2))
        if profile_degree != 4:
            raise RuntimeError("A complete readout lost its quartic profile degree")
        new = list(key)
        if key[IC]==0 and degree==2:
            factor = QF(1,2)
        elif key[IC]==2 and degree==1:
            factor = QF(-1,4)
            new[IC] = 0
            new[ID] += 1
        else:
            raise RuntimeError("A complete readout left the QQ/LLQ classes")
        new = tuple(new)
        out[new] = out.get(new,QF(0))+factor*coefficient
    return Poly(out)


def accel_split(poly):
    if any(key[IA]+key[IB]>1 for key in poly.terms):
        raise RuntimeError("An acceleration dependence is not affine")
    return (poly.coefficient(IA,0).coefficient(IB,0),
            poly.coefficient(IA,1).coefficient(IB,0),
            poly.coefficient(IB,1).coefficient(IA,0))


def compile_bundle():
    started = time.time()
    print('R530_FULL_STAGE '+json.dumps({'stage':'exact rational local fields','elapsed_seconds':0.0}),flush=True)
    m = matrix_poly()
    ff = fields()
    local = angular_average(local_ruling(ff,m))
    print('R530_FULL_STAGE '+json.dumps({'stage':'complete third local and ordered terms','elapsed_seconds':time.time()-started}),flush=True)
    qa = q_profile(AVAR)
    qap,qapp = dx_c2(qa),None
    qapp = dx_c2(qap)
    qm = q_profile(m)
    qmp = dx_c2(qm)
    qmpp = dx_c2(qmp)
    cc = third_local(ff,m)
    bb = ordered_B(m,qa,qap,qapp)
    gg = gram(qmp,qmpp,qap,qapp)
    la = linear_history(ff,qa,qap,qapp)
    dg,qg = H*E-K,1+(H*E-K)**2
    qgs = 2*dg*(G*E-V/2)
    total_ldot = dt(la,matrix=m)
    quotient_numerator = (G*la+H*total_ldot)*qg-H*la*qgs
    print('R530_FULL_STAGE '+json.dumps({'stage':'centered numerator and exact angular projection','elapsed_seconds':time.time()-started}),flush=True)
    nn = [angular_average(qg**2*(cc[j]-bb[j]+gg[j]/2)
                          -(quotient_numerator if j==0 else 0))
          for j in range(3)]
    labels = ["R0","Ch","Ck"]
    polynomials = list(accel_split(local))
    for j in range(3):
        labels.extend([f"N{j}_0",f"N{j}_a",f"N{j}_b"])
        polynomials.extend(accel_split(nn[j]))
    for j,value in enumerate(gram(qap,qapp,qap,qapp)):
        labels.append(f"G{j}_AA")
        polynomials.append(angular_average(value))
    labels.append("L_A")
    polynomials.append(angular_average(la))
    for poly in polynomials:
        if any(key[IC] or key[IA] or key[IB] for key in poly.terms):
            raise RuntimeError("An extracted coefficient retained eliminated variables")
        if any(key[IX]+key[IJ1]+2*key[IJ2]>10 for key in poly.terms):
            raise RuntimeError("A complete readout exceeds the matched translation degree")
    stats = {"elapsed_seconds":time.time()-started,"labels":labels,
             "exact_rational_terms":[len(p.terms) for p in polynomials],
             "maximum_translation_degree":max(
                 (key[IX]+key[IJ1]+2*key[IJ2] for p in polynomials for key in p.terms),default=0),
             "exact_highest_identity":True,"QQ_LLQ_projection":True,
             "source":"R581, R584, R586; complete ordered history retained"}
    return labels,polynomials,stats


class ReferenceGrid(c2.R578Grid):
    """One actual group's six nodes used only via the R586 exact identity."""
    def __post_init__(self):
        super().__post_init__()
        self.actual_blocks = self.blocks
        self.blocks = 6
        self.y = self.y[:6].copy()
        self.block_weights = self.block_weights[:6].copy()
        self.raw = self.raw[:,:6].copy()
        self.f = self.f[:,:6].copy()
        self.g = self.g[:,:6].copy()
        self.fcoef = self.fcoef[:6].copy()
        self.gcoef = self.gcoef[:6].copy()
        self.rho4 = self.rho4[:6].copy()
        self.q_basis = self.q_basis[:,:,:6].copy()
        self.third_test = self.third_test[:,:6].copy()

    def right_extended(self, values):
        result = np.empty_like(values,dtype=np.longdouble)
        suffix = np.zeros(values.shape[:-1],dtype=np.longdouble)
        quad = np.asarray(self.quad,dtype=np.longdouble)
        for sl,scale,jm in reversed(self.segments):
            vals = values[...,sl]
            result[...,sl] = np.longdouble(scale)*(vals@np.asarray(jm.T,dtype=np.longdouble))+suffix[...,None]
            suffix += np.sum(vals*quad[sl],axis=-1,dtype=np.longdouble)
        return result

    def reference_values(self):
        raw = np.asarray(self.raw,dtype=np.longdouble)
        dd = np.asarray(self.fcoef**2-self.gcoef**2,dtype=np.longdouble)
        y = np.asarray(self.y,dtype=np.longdouble)
        rr,pp = dd*raw[2]**2,dd*raw[1]**2
        jj0 = self.right_extended(rr)
        jj1 = self.right_extended(y*rr)
        jj2 = self.right_extended(y*y*rr+2*pp)
        return (y,raw[0],raw[1],raw[2],raw[3],jj0,jj1,jj2,
                np.asarray(self.gcoef,dtype=np.longdouble),dd)

    def reference_integral(self, values):
        row = np.sum(values*np.asarray(self.quad,dtype=np.longdouble),axis=-1,dtype=np.longdouble)
        return 6*np.sum(row*np.asarray(self.block_weights,dtype=np.longdouble),dtype=np.longdouble)


class Coefficients:
    def __init__(self,labels,polynomials,grid):
        started = time.time()
        self.labels,self.grid = labels,grid
        pkeys = sorted({key[:10] for poly in polynomials for key in poly.terms})
        gkeys = sorted({key[10:] for poly in polynomials for key in poly.terms})
        self.gkeys = np.asarray(gkeys,dtype=np.int16)
        gi = {key:j for j,key in enumerate(gkeys)}
        values = grid.reference_values()
        maxima = [max((key[i] for key in pkeys),default=0) for i in range(10)]
        powers = []
        for value,degree in zip(values,maxima):
            row = [np.ones_like(values[0],dtype=np.longdouble)]
            for _ in range(degree):
                row.append(row[-1]*value)
            powers.append(row)
        moments = {}
        for key in pkeys:
            val = np.ones_like(values[0],dtype=np.longdouble)
            for i,power in enumerate(key):
                if power:
                    val *= powers[i][power]
            moments[key] = grid.reference_integral(val)
        self.coefficients = np.zeros((len(polynomials),len(gkeys)),dtype=np.longdouble)
        for row,poly in enumerate(polynomials):
            for key,value in poly.terms.items():
                fraction = np.longdouble(str(value.numerator))/np.longdouble(str(value.denominator))
                self.coefficients[row,gi[key[10:]]] += fraction*moments[key[:10]]
        self.stats = {"quadrature_order":grid.order,"gap_order":grid.gap_order,
                      "reference_blocks":6,"actual_blocks":36,
                      "profile_moments":len(pkeys),"geometry_monomials":len(gkeys),
                      "coefficient_float64_sha256":hashlib.sha256(
                          self.coefficients.astype("<f8").tobytes()).hexdigest(),
                      "elapsed_seconds":time.time()-started}

    def evaluate(self,geometry,history):
        values = np.asarray((*geometry,0.0,0.0,*history),dtype=np.longdouble)
        with np.errstate(over="raise",divide="raise",invalid="raise"):
            monomials = np.prod(values[None,:]**self.gkeys,axis=1,dtype=np.longdouble)
            result = self.coefficients@monomials
        return result

    def history_rhs(self,outputs,geometry,a,b):
        h,k,eta,_,_ = geometry
        qg = 1+(h*eta-k)**2
        return np.asarray([(outputs[3+3*j]+a*outputs[4+3*j]+b*outputs[5+3*j])/qg**2
                           for j in range(3)],dtype=float)

    def center_shift(self,geometry,history):
        outputs = self.evaluate(geometry,history)
        h,k,eta,_,_ = geometry
        w0 = (1+(h*eta-k)**2)/(4*h)
        out = np.asarray(outputs[12:15]/4,dtype=float)
        out[0] -= float(outputs[15]/(4*w0))
        return out


ODD = np.array([0,2,7,5])
EVEN = np.array([1,3,4,6])
JPAR = np.array([1.,-1.,1.,-1.,-1.,1.,-1.,1.])


def weights(h,k,eta):
    dg = h*eta-k
    return np.array([(1+dg*dg)/(4*h),dg/2,h/4])


@dataclass
class BoundedGeometry:
    hmid: float = 1.9
    hradius: float = 1.1
    kcap: float = 2.0
    etacap: float = 1.0

    def decode(self,q):
        scaled = 2/np.pi*np.arctan(q)
        physical = np.array([self.hmid+self.hradius*scaled[0],
                             self.kcap*scaled[1],self.etacap*scaled[2]])
        derivatives = np.array([self.hradius,self.kcap,self.etacap])*(2/np.pi)/(1+q*q)
        return physical,derivatives

    def encode(self,physical):
        scaled = np.array([(physical[0]-self.hmid)/self.hradius,
                           physical[1]/self.kcap,physical[2]/self.etacap])
        if np.max(np.abs(scaled))>=1:
            raise ValueError("A seed leaves the fixed strict R530 box")
        return np.tan(np.pi*scaled/2)


class NineteenRHS:
    def __init__(self,coefficients,length):
        self.coefficients,self.length = coefficients,length
        self.map = BoundedGeometry()
        self.calls = 0
        self.points = 0

    def physical(self,state):
        geometric,derivatives = self.map.decode(state[:3])
        return (*geometric,*state[3:5]),derivatives

    def one(self,state,nubar):
        geometry,coordinate_derivatives = self.physical(state)
        h,k,eta,gamma,upsilon = geometry
        if not np.all(np.isfinite(state)) or max(abs(gamma),abs(upsilon))>1.e6:
            raise FloatingPointError("Finite velocity/history continuation left its declared numerical range")
        history = state[5:13]
        negative = (h,-k,-eta,-gamma,upsilon)
        plus = self.coefficients.evaluate(geometry,history)
        minus = self.coefficients.evaluate(negative,JPAR*history)
        hp,kp = float(plus[1]),float(plus[2])
        hm,km = float(minus[1]),float(minus[2])
        determinant = -hp*km-hm*kp
        if not (hp<0 and hm<0 and kp>0 and km>0 and determinant>0):
            raise FloatingPointError("Computed acceleration coefficients left their strict actual sign domain")
        fp = float(plus[0])-4*weights(h,k,eta)@state[13:16]-2*weights(h,k,eta)@nubar
        fm = float(minus[0])-4*weights(h,-k,-eta)@state[16:19]-2*weights(h,-k,-eta)@nubar
        a = (km*fp+kp*fm)/determinant
        b = (hm*fp-hp*fm)/determinant
        out = np.empty(19)
        out[:3] = np.array([gamma,upsilon,upsilon/(2*h)])/coordinate_derivatives
        out[3:5] = a,b
        out[5:13] = core.matrix_density(*geometry)
        out[13:16] = self.coefficients.history_rhs(plus,geometry,a,b)
        out[16:19] = -self.coefficients.history_rhs(minus,negative,a,-b)
        if not np.all(np.isfinite(out)):
            raise FloatingPointError("Nonfinite complete nineteen-state derivative")
        return out

    def __call__(self,x,states,nubar):
        self.calls += 1
        self.points += states.shape[1]
        return self.length*np.column_stack([self.one(states[:,i],nubar)
                                           for i in range(states.shape[1])])


def make_seed(rhs,height,peak,curvature,power,nodes):
    x = np.linspace(0.,1.,nodes)
    length = rhs.length
    ss,cc = np.sin(np.pi*x/2),np.cos(np.pi*x/2)
    dh = peak-height
    h = height+dh*ss**power
    hx = dh*power*ss**(power-1)*cc*np.pi/2
    hxx = dh*power*((power-1)*ss**(power-2)*cc**2-ss**power)*(np.pi/2)**2
    k = curvature*np.sin(np.pi*x)
    kx = curvature*np.pi*np.cos(np.pi*x)
    kxx = -curvature*np.pi**2*np.sin(np.pi*x)
    eta = cumulative_simpson(kx/(2*h),x=x,initial=0.)
    gamma,upsilon,a,b = hx/length,kx/length,hxx/length**2,kxx/length**2
    densities = np.array([core.matrix_density(*geo) for geo in zip(h,k,eta,gamma,upsilon)]).T
    history = length*cumulative_simpson(densities,x=x,axis=1,initial=0.)
    history[ODD] -= history[ODD,-1,None]
    states = np.zeros((19,nodes))
    for i in range(nodes):
        states[:3,i] = rhs.map.encode([h[i],k[i],eta[i]])
    states[3:5] = gamma,upsilon
    states[5:13] = history
    center_geometry = (h[0],0.,0.,0.,upsilon[0])
    center_outputs = rhs.coefficients.evaluate(center_geometry,history[:,0])
    nubar = np.array([(float(center_outputs[0])+float(center_outputs[1])*a[0])/
                      (2*weights(h[0],0.,0.)[0]),0.,0.])
    for i in range(nodes):
        gp = (h[i],k[i],eta[i],gamma[i],upsilon[i])
        gm = (h[i],-k[i],-eta[i],-gamma[i],upsilon[i])
        op = rhs.coefficients.evaluate(gp,history[:,i])
        om = rhs.coefficients.evaluate(gm,JPAR*history[:,i])
        wp,wm = weights(h[i],k[i],eta[i]),weights(h[i],-k[i],-eta[i])
        states[13,i] = (float(op[0]+op[1]*a[i]+op[2]*b[i])-2*wp@nubar)/(4*wp[0])
        states[16,i] = (float(om[0]+om[1]*a[i]-om[2]*b[i])-2*wm@nubar)/(4*wm[0])
    states[13:19,0] = 0.
    return x,states,nubar


def boundary_function(rhs,height):
    def bc(left,right,nubar):
        geometry,_ = rhs.physical(left)
        return np.concatenate(([geometry[0]-height,left[1],left[2],left[3]],
                               left[5+EVEN],left[13:19],right[5:13]))
    return bc


def inspect_solution(rhs,solution,height):
    x = np.unique(np.concatenate((solution.x,(solution.x[:-1]+solution.x[1:])/2)))
    values,derivatives = solution.sol(x),solution.sol(x,1)/rhs.length
    geometries = np.array([rhs.physical(values[:,i])[0] for i in range(len(x))]).T
    h,k,eta,gamma,upsilon = geometries
    ruling,kinematic,matrix_defect,third_defect = [],[],[],[]
    for i in range(len(x)):
        gp = tuple(geometries[:,i])
        gm = (h[i],-k[i],-eta[i],-gamma[i],upsilon[i])
        history = values[5:13,i]
        op = rhs.coefficients.evaluate(gp,history)
        om = rhs.coefficients.evaluate(gm,JPAR*history)
        a,b = derivatives[3:5,i]
        wp,wm = weights(h[i],k[i],eta[i]),weights(h[i],-k[i],-eta[i])
        ruling.append([float(op[0]+op[1]*a+op[2]*b)-4*wp@values[13:16,i]-2*wp@solution.p,
                       float(om[0]+om[1]*a-om[2]*b)-4*wm@values[16:19,i]-2*wm@solution.p])
        _,coordinate_derivatives = rhs.physical(values[:,i])
        kinematic.append(derivatives[:3,i]*coordinate_derivatives
                         -np.array([gamma[i],upsilon[i],upsilon[i]/(2*h[i])]))
        matrix_defect.append(derivatives[5:13,i]-core.matrix_density(*gp))
        third_defect.append(np.concatenate((
            derivatives[13:16,i]-rhs.coefficients.history_rhs(op,gp,a,b),
            derivatives[16:19,i]+rhs.coefficients.history_rhs(om,gm,a,-b))))
    endpoint = values[5:13,-1]
    center = tuple(geometries[:,0])
    rc = rhs.coefficients.center_shift(center,values[5:13,0])
    return {
        "status":int(solution.status),"success":bool(solution.success),"message":str(solution.message),
        "mesh_nodes":len(solution.x),"iterations":int(solution.niter),
        "max_scipy_rms_relative_residual":float(np.max(solution.rms_residuals)),
        "boundary_max_abs":float(np.max(np.abs(boundary_function(rhs,height)(
            values[:,0],values[:,-1],solution.p)))),
        "eight_endpoint":endpoint.tolist(),
        "initial_v0":float(upsilon[0]),"initial_Aodd":values[5+ODD,0].tolist(),
        "nubar":solution.p.tolist(),"actual_fixed_nu":(solution.p-2*rc).tolist(),
        "center_r":rc.tolist(),
        "sampled_geometry_ranges":{
            name:[float(v.min()),float(v.max())] for name,v in
            zip(("h","k","eta","gamma","upsilon"),geometries)},
        "sampled_actual_kinematic_defect_max":float(np.max(np.abs(kinematic))),
        "sampled_actual_matrix_ODE_defect_max":float(np.max(np.abs(matrix_defect))),
        "sampled_complete_third_ODE_defect_max":float(np.max(np.abs(third_defect))),
        "sampled_original_ruling_from_collocation_acceleration_max":float(np.max(np.abs(ruling))),
        "rhs_calls":rhs.calls,"rhs_points":rhs.points,
        "sigma_endpoint_plus":values[13:16,-1].tolist(),
        "sigma_endpoint_minus":values[16:19,-1].tolist(),
        "full_T_period_and_fourth_period_claim":False,
    }


def sample_pose(rhs,solution):
    def ode(s,state):
        geo,_ = rhs.physical(solution.sol(s/rhs.length))
        h,k = geo[:2]
        frame = state[:9].reshape(3,3)
        omega = np.array([[0.,-k,0.],[k,0.,1.],[0.,-1.,0.]])
        return np.concatenate(((frame@omega).ravel(),h*h*frame[:,0]))
    init = np.concatenate((np.eye(3).ravel(),np.zeros(3)))
    sol = solve_ivp(ode,(0.,rhs.length),init,rtol=1.e-9,atol=1.e-11,
                    dense_output=True,method="DOP853")
    sample = np.linspace(0.,rhs.length,401)
    pose = sol.sol(sample)
    frame = pose[:9].T.reshape(-1,3,3)
    alpha = pose[9:].T
    geo = np.array([rhs.physical(solution.sol(s/rhs.length))[0] for s in sample])
    h,eta = geo[:,0],geo[:,2]
    normal = frame[:,:,1]
    edges = []
    for y in (4.,6.):
        edges.append(alpha+h[:,None]/(y+eta)[:,None]*normal)
        edges.append(alpha-h[:,None]/(y-eta)[:,None]*normal)
    points = np.concatenate(edges)
    center = (points[:,2].min()+points[:,2].max())/2
    radius = np.linalg.norm(points-np.array([0.,0.,center]),axis=1).max()
    n,v = normal[-1],alpha[-1]
    return {"frame_ODE_success":bool(sol.success),"sample_count":401,
            "four_edge_sampled_radius":float(radius),"B_axis_ball_center":float(center),
            "pose_two_endpoint_values":[float(n[2]**2-.5),float(v[0]*n[1]-v[1]*n[0])],
            "frame_orthogonality_defect":float(np.linalg.norm(frame[-1].T@frame[-1]-np.eye(3))),
            "continuous_diameter_or_reach_certificate":False}


def run_trial(coefficients,args,height,length,power):
    start = time.time()
    rhs = NineteenRHS(coefficients,length)
    result = {"height":height,"length":length,"seed_peak":args.peak,
              "seed_curvature":args.curvature,"seed_power":power,
              "fixed_model":True,"exact_root_claim":False,"response_rank_claim":False}
    try:
        x,states,nubar = make_seed(rhs,height,args.peak,args.curvature,power,args.nodes)
        sol = solve_bvp(rhs,boundary_function(rhs,height),x,states,p=nubar,
                        tol=args.tol,bc_tol=args.bc_tol,max_nodes=args.max_nodes,verbose=0)
        result["coarse"] = inspect_solution(rhs,sol,height)
        # Continue a finite near-solution at the mesh ceiling on the same input.
        # This does not promote a failed coarse solve to an actual root.
        continue_same = (sol.status==1 and np.all(np.isfinite(sol.y))
                         and float(np.max(sol.rms_residuals))<0.5)
        if sol.success or continue_same:
            refined = solve_bvp(rhs,boundary_function(rhs,height),sol.x,sol.y,p=sol.p,
                                tol=args.refine_tol,bc_tol=args.refine_tol,
                                max_nodes=args.refine_max_nodes,verbose=0)
            result["refined"] = inspect_solution(rhs,refined,height)
            if refined.success:
                result["pose_readout"] = sample_pose(rhs,refined)
    except Exception as error:
        result["failure"] = {"type":type(error).__name__,"message":str(error)}
        result["rhs_calls"],result["rhs_points"] = rhs.calls,rhs.points
    result["elapsed_seconds"] = time.time()-start
    return result


def emit(tag,value):
    print(tag+" "+json.dumps(value,sort_keys=True,allow_nan=False),flush=True)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--orders",default="96,192")
    parser.add_argument("--gap-order",type=int,default=8)
    parser.add_argument("--heights",default="1.1,1.3")
    parser.add_argument("--lengths",default="3,5")
    parser.add_argument("--powers",default="4")
    parser.add_argument("--peak",type=float,default=2.8)
    parser.add_argument("--curvature",type=float,default=1.8)
    parser.add_argument("--nodes",type=int,default=25)
    parser.add_argument("--max-nodes",type=int,default=401)
    parser.add_argument("--refine-max-nodes",type=int,default=1201)
    parser.add_argument("--tol",type=float,default=1.e-4)
    parser.add_argument("--bc-tol",type=float,default=1.e-8)
    parser.add_argument("--refine-tol",type=float,default=1.e-6)
    parser.add_argument("--coefficients-only",action="store_true")
    args = parser.parse_args()
    if (os.environ.get("GITHUB_ACTIONS")!="true"
            or os.environ.get("GITHUB_REPOSITORY")!="Rogerhu12/math-research-public"):
        raise RuntimeError("This full scientific entry is scheduled only in the public repository Actions.")
    if any(int(p)<2 or int(p)%2 for p in args.powers.split(",")):
        raise ValueError("Seed height powers must be positive even integers at least two")
    started = time.time()
    labels,polynomials,stats = compile_bundle()
    emit("R530_FULL_FORMAL",stats)
    probe_geometry = (1.17,.23,.08,.11,-.31)
    probe_history = (.02,-.013,.017,.019,-.007,.011,-.009,.014)
    previous = None
    coefficients = None
    for order in (int(n) for n in args.orders.split(",")):
        grid = ReferenceGrid(order,args.gap_order,5.)
        coefficients = Coefficients(labels,polynomials,grid)
        probe = np.asarray(coefficients.evaluate(probe_geometry,probe_history),dtype=float)
        row = dict(coefficients.stats)
        row.update({"geometry":probe_geometry,"history":probe_history,"labels":labels,
                    "complete_coefficient_probe":probe.tolist(),
                    "centered_history_rhs_probe":coefficients.history_rhs(
                        probe,probe_geometry,.47,-.29).tolist(),
                    "elapsed_seconds_from_start":time.time()-started,
                    "scope":"New complete R584/R586 coefficient compilation, no replay of raw R581 diagnostics."})
        if previous is not None:
            row["probe_change_from_previous"] = (probe-previous).tolist()
        emit("R530_FULL_COEFFICIENTS",row)
        previous = probe
        gc.collect()
    if not args.coefficients_only:
        for height in (float(v) for v in args.heights.split(",")):
            for length in (float(v) for v in args.lengths.split(",")):
                for power in (int(v) for v in args.powers.split(",")):
                    emit("R530_FULL_BVP_TRIAL",run_trial(coefficients,args,height,length,power))
    emit("R530_FULL_DONE",{"elapsed_seconds":time.time()-started,
                           "README_completion_claim":False,
                           "full_fourth_period_claim":False,"response_rank_claim":False})


if __name__=="__main__":
    main()

