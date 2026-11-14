#!/usr/bin/env python3
"""A two-dimensional interval column with a retained common scale.

An exact column is represented by scale*(1,ratio) or scale*(ratio,1).
Each matrix step chooses an output component whose entire interval excludes
zero.  Dividing only that normalized output, rather than independently
propagating two enormous coordinate boxes, retains the common amplitude.
The advanced exact matrix must have positive determinant (all uses here are
determinant-one exact flows).  The projective map is then monotone in the input
ratio.  Evaluating its two endpoint ratios retains the numerator/denominator
correlation which a quotient of two full ratio-interval evaluations would lose.
No midpoint is substituted for the exact column.
"""
from flint import arb


class ProjectiveColumn:
    def __init__(self, vector):
        self.pivot=self.choose(vector)
        scale=vector[self.pivot]
        self.sign=1 if scale>0 else -1
        self.absolute_lower=abs(scale).lower()
        self.absolute_upper=abs(scale).upper()
        self.ratio=vector[1-self.pivot]/scale

    @staticmethod
    def choose(vector):
        candidates=[i for i in range(2) if not vector[i].contains(0)]
        if not candidates:
            raise ArithmeticError('Both normalized projective components contain zero')
        return max(candidates,key=lambda i:abs(vector[i]).lower())

    def unit(self):
        return [arb(1),self.ratio] if self.pivot==0 else [self.ratio,arb(1)]

    def values(self):
        return [lo.union(hi) for lo,hi in (self.component_bounds(0),self.component_bounds(1))]

    def absolute_uppers(self):
        return [(self.absolute_upper*abs(x).upper()).upper() for x in self.unit()]

    def component_bounds(self,index):
        value=self.unit()[index];lo=value.lower();hi=value.upper()
        if lo>=0:
            lower=(self.absolute_lower*lo).lower()
            upper=(self.absolute_upper*hi).upper()
        elif hi<=0:
            lower=(self.absolute_upper*lo).lower()
            upper=(self.absolute_lower*hi).upper()
        else:
            lower=(self.absolute_upper*lo).lower()
            upper=(self.absolute_upper*hi).upper()
        return (lower,upper) if self.sign>0 else (-upper,-lower)

    def multiply_scale(self,factor):
        if factor.contains(0):
            raise ArithmeticError('A common scale factor contains zero')
        if factor<0:self.sign=-self.sign
        self.absolute_lower=(self.absolute_lower*abs(factor).lower()).lower()
        self.absolute_upper=(self.absolute_upper*abs(factor).upper()).upper()
        if not self.absolute_lower>0:
            raise ArithmeticError('A positive separate scale lower endpoint was lost')

    def advance(self,matrix):
        unit=self.unit()
        value=[matrix[i][0]*unit[0]+matrix[i][1]*unit[1] for i in range(2)]
        pivot=self.choose(value)
        images=[]
        for endpoint in (self.ratio.lower(),self.ratio.upper()):
            boundary=[arb(1),endpoint] if self.pivot==0 else [endpoint,arb(1)]
            out=[matrix[i][0]*boundary[0]+matrix[i][1]*boundary[1] for i in range(2)]
            images.append(out[1-pivot]/out[pivot])
        ratio=images[0].union(images[1])
        self.multiply_scale(value[pivot])
        self.ratio=ratio
        self.pivot=pivot

    def multiply_component(self,index,factor):
        if factor.contains(0):
            raise ArithmeticError('A canonical port factor contains zero')
        if self.pivot==index:
            self.multiply_scale(factor)
            self.ratio/=factor
        else:
            self.ratio*=factor
