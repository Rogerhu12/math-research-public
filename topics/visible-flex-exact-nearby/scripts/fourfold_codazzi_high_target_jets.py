#!/usr/bin/env python3
"""Actual target through K_rr, differentiated before any radial interval.

The original complete unit primitive and its tail are retained. Five radial
jets of that same primitive pay E''' and therefore K''. No high derivative
is inferred from an error bound that paid only lower derivative orders.
"""
from __future__ import annotations
import math
import numpy as np
from flint import arb, acb
from fourfold_phase_codazzi_coefficients import CodazziCoefficientTarget, real_part
from fourfold_phase_beta_bulk_box import (
    CBox, Box, zeros, cstack, cdot, reduce_box, complex_sincos)


def trig_derivatives(value):
    count = len(value.real.lo)
    ss, cc = [None]*count, [None]*count
    ss[0], cc[0] = complex_sincos(value[0])
    for n in range(1, count):
        ss[n] = sum((math.comb(n-1,j)*cc[j]*value[n-j]
                     for j in range(n)), CBox(0.))
        cc[n] = -sum((math.comb(n-1,j)*ss[j]*value[n-j]
                      for j in range(n)), CBox(0.))
    return cstack(ss), cstack(cc)


def derivative_product(left, right):
    count = min(len(left.real.lo), len(right.real.lo))
    return cstack([sum((math.comb(n,j)*left[j]*right[n-j]
                       for j in range(n+1)), CBox(0.)) for n in range(count)])


def series_mul(a, b):
    return [sum((a[j]*b[i-j] for j in range(i+1)), arb(0))
            for i in range(min(len(a),len(b)))]


def series_inv(a):
    out = [1/a[0]]
    for i in range(1,len(a)):
        out.append(-out[0]*sum((a[j]*out[i-j] for j in range(1,i+1)), arb(0)))
    return out


def series_dr(a):
    return [(i+1)*a[i+1] for i in range(len(a)-1)]


class HighCodazziTarget(CodazziCoefficientTarget):
    def unit_finite_data(self, radial):
        delta = CBox.from_acb(radial-acb(self.anchor))
        count = 5
        jet = zeros((count,2*self.modes+2))
        for n in range(20,-1,-1):
            jet = jet*delta+cstack([self.scalar_poly[n]]+
                                  [j*jet[j-1] for j in range(1,count)])
        beta, vertical = jet[:,:self.modes], jet[:,self.modes:2*self.modes]
        radius, height = jet[:,-2], jet[:,-1]
        self.last_scalar = beta, vertical, radius, height
        sines = self.fast_sines.reshape(1,self.modes,self.nodes)
        b = (beta.reshape(count,self.modes,1)*sines).sum(1)
        g = (vertical.reshape(count,self.modes,1)*sines).sum(1)
        sb,_ = trig_derivatives(b)
        sg,_ = trig_derivatives(g)
        shb,_ = trig_derivatives(b/2)
        shg,_ = trig_derivatives(g/2)
        cmb = -2*derivative_product(shb,shb)
        cmg = -2*derivative_product(shg,shg)
        one = zeros((count,self.nodes)); one[0] = 1
        tangent = cstack([-derivative_product(one+cmg,sb),
                          cmg+cmb+derivative_product(cmg,cmb),sg],-1)
        coefficient = self.fast_fourier.fft(tangent,1)/self.nodes
        primitive = zeros((count,self.nodes,3))
        n = np.asarray(self.frequency)
        ii = CBox(0.,Box(n.reshape(1,-1)))
        denominator = Box((1-n*n).reshape(1,-1))
        primitive[:,:,0] = (ii*coefficient[:,:,0]+coefficient[:,:,1])/denominator
        primitive[:,:,1] = (-coefficient[:,:,0]+ii*coefficient[:,:,1])/denominator
        nz = np.flatnonzero(n)
        primitive[:,nz,2] = coefficient[:,nz,2]/CBox(0.,Box(n[nz].reshape(1,-1)))
        primitive[:,self.nodes//2,:] = 0
        primitive[:,0,1], primitive[:,0,2] = 0,0
        pos = np.arange(1,self.nodes//2)
        for component, parity in enumerate((1,-1,1)):
            v = (primitive[:,pos,component]+parity*primitive[:,-pos,component])/2
            primitive[:,pos,component],primitive[:,-pos,component] = v,parity*v
        self.unit_primitive = primitive
        return primitive,radius

    def scalar_jets_and_fourier(self, radial):
        P,_ = self.unit_finite_data(radial)
        _,_,a,z = self.last_scalar
        F = []
        for j in range(5):
            v = sum((math.comb(j,h)*a[j-h]*P[h] for h in range(j+1)),
                    zeros((self.nodes,3)))
            v[0,0],v[0,2] = v[0,0]+a[j],v[0,2]+z[j]
            F.append(v)
        tail = self.unit_tail_errors(radial,self.metric_tail_strip)[0]
        EF = []
        for j in range(5):
            errors = []
            for q in range(5):
                bound = arb(0)
                for h in range(j+1):
                    primitive = (math.factorial(h)/self.tail_radius**h
                                 *math.factorial(q)*(4/self.metric_tail_strip)**q*tail)
                    magnitude = arb(float(np.max(a[j-h].magnitude_upper()))).upper()
                    bound += math.comb(j,h)*magnitude*primitive
                errors.append(bound.upper())
            EF.append(errors)
        self.last_complete_high_jets = F,a,EF
        # Only radial target means are consumed by the parent coefficient
        # method; no angular geometry jet is silently supplied here.
        return F,[],a,EF,[],tail

    def coefficients(self,left,right):
        values = super().coefficients(left,right)
        F,a,EF = self.last_complete_high_jets
        reverse = (-np.arange(self.nodes)) % self.nodes
        norms = [arb(float(np.max(reduce_box(Box(f.magnitude_upper())).hi))).upper()
                 for f in F]
        def product_mean(i,j):
            finite = cdot(F[i],F[j][reverse]).sum().to_acb()
            if not finite.imag.contains(0):
                raise ValueError("true high target mean lost reality")
            error = 3*(norms[i]*EF[j][0]+norms[j]*EF[i][0]+EF[i][0]*EF[j][0])
            return finite.real+arb(0,error.upper())
        E3 = 6*product_mean(2,3)+2*product_mean(1,4)
        aa = [real_part(a[j],f"a{j}") for j in range(5)]
        ar = [v/math.factorial(j) for j,v in enumerate(aa)]
        er = [values["E"],values["E1"],values["E2"]/2,E3/6]
        ia,ie = series_inv(ar),series_inv(er)
        first = series_mul(series_mul(series_dr(series_dr(ar)),ia),ie)
        second = series_mul(series_mul(series_mul(series_mul(
            series_dr(ar),series_dr(er)),ia),ie),ie)
        Kjet = [-x+y/2 for x,y in zip(first,second)]
        if not Kjet[0].overlaps(values["K"]) or not Kjet[1].overlaps(values["K1"]):
            raise ValueError("independent true curvature-jet identity failed")
        beta = values["beta"]
        values.update(a4=aa[4],E3=E3,K2=2*Kjet[2],
                      beta1=aa[2]/aa[0]-beta*beta,
                      beta2=aa[3]/aa[0]-3*aa[1]*aa[2]/aa[0]**2+2*beta**3)
        return values
