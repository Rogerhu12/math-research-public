#!/usr/bin/env python3
"""Complete moving finite system at the actual R=25/8 regular entrance.

q is an explicitly recorded floating proposal for the true physical-theta
regular linear graph. Its native all-eta/tail fees and the nonlinear mean
and nonmean graph remainders remain separate posterior obligations.
"""
from fractions import Fraction
import json
from pathlib import Path
import numpy as np
from fourfold_codazzi_moving_polynomial_system import MovingPolynomial
from fourfold_codazzi_reciprocal_polynomial_system import ReciprocalPolynomial

class MovingRegularEndpoint(MovingPolynomial):
    def __init__(self,geometry,modes,angles,body,graft,*,q_path,mean_boundary='outer'):
        ReciprocalPolynomial.__init__(self,geometry,modes,angles,body,graft,
            mean_boundary=mean_boundary,right=25/8)
        self.q_path=Path(q_path);data=json.loads(self.q_path.read_text())
        if (data['kind']!='floating_actual_R74_regular_endpoint_q_vector'
            or any(Fraction(str(data[name]))!=Fraction(25,8) for name in ('left','right','right_boundary'))
            or data['physical_material_angle']!='theta'):
            raise ValueError('the actual true-entrance physical q identity is required')
        frequencies=np.asarray(data['physical_frequencies'],dtype=int)
        values=np.asarray(data['q_values'],dtype=float)
        if len(values)<modes or len(values)!=len(frequencies) or not np.all(frequencies==4*np.arange(1,len(values)+1)):
            raise ValueError('a complete consecutive true-entrance physical q vector is required')
        if np.any(values<=0) or not np.all(np.isfinite(values)):
            raise ValueError('invalid true-entrance q proposal')
        self.q_vector=values[:modes].copy();self.q_data=data
        self.q_tail_bound=float(data['all_nonmean_q_abs_upper'])
        if self.q_tail_bound<np.max(self.q_vector):raise ValueError('full q bound does not cover the proposals')
