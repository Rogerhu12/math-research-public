#!/usr/bin/env python3
"""Continuous exact Bernstein bounds for the original M12 tail polynomial.

New recovered source identity after the 2026-11-26 executor loss. This file
does not claim the hash or execution of the lost unpublished helper. Every
input coefficient and normalized span endpoint is a Fraction, supplied by
the checked original-tail streamer. All row interiors and angular values
are covered; these are coordinate derivative bounds, not sampled curvature.
"""
from __future__ import annotations
from fractions import Fraction as Q
import hashlib
import math

FIELDS=('V','Vr','Vu','Vrr','Vru','Vuu')
DEN=10**24


def upper(q):
    q=Q(q)
    return Q(-((-q.numerator*DEN)//q.denominator),DEN)


def packet(q):
    q=Q(q);u=upper(q)
    return {'upper_exact':str(u),'display':float(u)}


def bernstein(power):
    degree=len(power)-1
    return [sum((Q(math.comb(i,k),math.comb(degree,k))*power[k]
                 for k in range(i+1)),Q(0)) for i in range(degree+1)]


def derivative_controls(controls,length):
    degree=len(controls)-1
    if degree==0:return [Q(0)]
    return [degree*(controls[i+1]-controls[i])/length for i in range(degree)]


def span_controls(value,f0,f1,s0,s1,mid,length):
    """F_r quartic controls and the exact integrated F quintic controls."""
    if length<=0:raise ValueError('Nonpositive original span')
    derivative=[f0,f0+length*s0/4,
                (16*mid-5*(f0+f1)-length*(s0-s1))/6,
                f1-length*s1/4,f1]
    position=[value]
    for entry in derivative:position.append(position[-1]+length*entry/5)
    second=derivative_controls(derivative,length)
    return position,derivative,second


class TailContinuousBounds:
    def __init__(self,planar_modes,height_modes,cuff):
        self.modes=tuple(int(k) for k in planar_modes)+tuple(int(k) for k in height_modes)
        self.C=len(self.modes);self.cuff=Q(cuff)
        if self.cuff<=0:raise ValueError('Nonpositive true cuff')
        self.global_bounds=[Q(0)]*6;self.CX=Q(0);self.worst=None
        self.rows=0;self.finite_rows=0;self.blocks=[];self.digest=hashlib.sha256()
        self.active=False;self.deep_done=False

    def begin_block(self,nodes):
        if self.active:raise RuntimeError('Previous exact source block unfinished')
        self.nodes=tuple(Q(v) for v in nodes)
        if len(self.nodes)<2 or any(b<=a for a,b in zip(self.nodes,self.nodes[1:])):
            raise ValueError('Invalid exact source nodes')
        if self.nodes[0]<self.cuff:raise ValueError('Finite source enters below cuff')
        self.acc=[[Q(0)]*6 for unused in range(len(nodes)-1)]
        self.count=[0]*(len(nodes)-1);self.active=True

    def add_span_coefficient(self,i,j,value,f0,f1,s0,s1,mid,length):
        if not self.active or length!=self.nodes[i+1]-self.nodes[i]:
            raise ValueError('Span length identity failed')
        p,b,d=span_controls(value,f0,f1,s0,s1,mid,length)
        self._add(i,j,p,b,d)

    def _add(self,i,j,p,b,d):
        m=abs(self.modes[j])
        a=max(map(abs,p));ar=max(map(abs,b));arr=max(map(abs,d))
        values=(a,ar,m*a,arr,m*ar,m*m*a)
        for k,v in enumerate(values):self.acc[i][k]+=v
        self.count[i]+=1

    def _finish_row(self,left,right,bounds,kind):
        v,vr,vu,vrr,vru,vuu=bounds
        # Original rotational background: |B_ss|<=6, |B_su|<=1,
        # |B_uu|=r, |r_s|<=1, |r_ss|<=6 in physical arclength s.
        # Its true target metric is ds^2+r^2 du^2.
        cx=6+3/left+vrr+6*vr+2*vru/left+vuu/(left*left)
        row=[str(self.rows),kind,str(left),str(right)]+[str(v) for v in bounds]+[str(cx)]
        self.digest.update(('\t'.join(row)+'\n').encode())
        for j,v in enumerate(bounds):self.global_bounds[j]=max(self.global_bounds[j],v)
        if cx>self.CX:
            self.CX=cx;self.worst={'row':self.rows,'kind':kind,'left_exact':str(left),
                                 'right_exact':str(right),'C_X':packet(cx)}
        self.rows+=1
        return cx

    def finish_block(self):
        if not self.active or any(n!=self.C for n in self.count):
            raise ArithmeticError('Incomplete Fourier coefficient coverage')
        blockmax=Q(0)
        for i,bounds in enumerate(self.acc):
            blockmax=max(blockmax,self._finish_row(self.nodes[i],self.nodes[i+1],bounds,'finite'))
        self.finite_rows+=len(self.acc)
        self.blocks.append({'spans':len(self.acc),'left_exact':str(self.nodes[0]),
                            'right_exact':str(self.nodes[-1]),'C_X':packet(blockmax)})
        self.active=False
        del self.acc,self.count,self.nodes

    def add_deep_collar(self,inner,value,first,second):
        if self.active or self.deep_done:raise RuntimeError('Invalid deep collar order')
        if not len(value)==len(first)==len(second)==self.C:raise ValueError('Incomplete collar modes')
        inner=Q(inner);h=inner-self.cuff
        self.begin_block([self.cuff,inner])
        for j,(a0,a1,a2) in enumerate(zip(value,first,second)):
            power=[Q(0),Q(0),Q(0),10*a0-4*h*a1+h*h*a2/2,
                   -15*a0+7*h*a1-h*h*a2,6*a0-3*h*a1+h*h*a2/2]
            p=bernstein(power);b=derivative_controls(p,h);d=derivative_controls(b,h)
            self._add(0,j,p,b,d)
        if self.count[0]!=self.C:raise ArithmeticError('Incomplete deep collar')
        self._finish_row(self.cuff,inner,self.acc[0],'deep-collar')
        self.active=False;self.deep_done=True
        del self.acc,self.count,self.nodes

    def receipt(self):
        if self.active or not self.deep_done:raise ArithmeticError('Incomplete full tail budget')
        return {'schema':'6a65-original-M12-continuous-tail-source-jets-recovered-v2',
                'source_model':'Original integrated quartic Fr and original quintic deep collar',
                'finite_spans':self.finite_rows,'deep_collar_spans':1,'coefficient_count':self.C,
                'arithmetic':'Exact Fraction Bernstein controls; integer outward decimal upper bounds',
                'continuous_all_angles_and_span_interiors':True,
                'coordinate_derivatives_not_new_curvature_certificate':True,
                'inherited_background_hypothesis':'Original full background |kappa_r|<=6, ds^2=E dr^2, E=1+w^2',
                'component_bounds':{k:packet(v) for k,v in zip(FIELDS,self.global_bounds)},
                'original_physical_target_scaled_second_jets_C_X':packet(self.CX),
                'worst_row':self.worst,'exact_row_stream_sha256':self.digest.hexdigest(),
                'blocks':self.blocks}

