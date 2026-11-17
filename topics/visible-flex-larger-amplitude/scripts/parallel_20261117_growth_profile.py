#!/usr/bin/env python3
"""Declared new scalar a_c(s)=1+c(a_base(s)-1), with both true derivatives.

The original exact-rational/quintic/analytic expression defines a_base.
The floating evaluator is not a rigorous interval enclosure.  The positive
constant c is a design parameter, and must be frozen during metric refinement.
"""
import numpy as np
from parallel_20261117_profile import Profile as BaseProfile


class GrowthProfile:
    def __init__(self, geometry, start, growth_scale=1.0):
        if not np.isfinite(growth_scale) or growth_scale<=0:
            raise ValueError('Positive finite radial growth scale is required')
        self.base=BaseProfile(geometry,start);self.growth_scale=growth_scale
        self.start=start;self.geometry=geometry
        self.a0=1+growth_scale*(self.base.a0-1)
        self.v0=growth_scale*self.base.v0;self.u0=growth_scale*self.base.u0
        self.base_K=self.base.K

    def __call__(self,s):
        a,ap,app=self.base(s);c=self.growth_scale
        return 1+c*(a-1),c*ap,c*app
