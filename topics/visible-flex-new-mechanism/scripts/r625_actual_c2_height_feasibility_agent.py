#!/usr/bin/env python3
"""The original actual C2 height at its existing true-readout points.

No true eta/A/rho/ruling or old fine qualification is reevaluated here. The
new direction needs the previously unstored height values and their exact
fixed-length linear map. The complete L chain is retained as the exact
cubic polynomial along a full mixed-coordinate increment. Scientific work
is restricted to the declared public Actions by the original guard.
"""
from __future__ import annotations

from collections import defaultdict
import hashlib
from pathlib import Path
import time

import numpy as np

import r620_free_center_full_feedback_bvp_agent as original

ORIGINAL_SOURCE_SHA = '2edc5a8047153e4e1803da8e010590bd94452d5d5c7a52c6bec81428cfb29b22'
COUNTS = defaultdict(int)


def _array_sha(value):
    return hashlib.sha256(np.ascontiguousarray(value,dtype=np.float64).tobytes()).hexdigest()


class ActualC2HeightRows:
    """One source-bound operator on exactly the original integral grid."""
    def __init__(self,x,readout_points,size,clock):
        original.reduced.require_public_science()
        if hashlib.sha256(Path(original.__file__).read_bytes()).hexdigest()!=ORIGINAL_SOURCE_SHA:
            raise ValueError('the exact original actual-C2 source is required')
        self.clock=clock
        self.x=np.asarray(x,dtype=float).copy()
        self.points=np.asarray(readout_points,dtype=float).copy()
        self.size=int(size)
        n=len(self.x)
        if (n<3 or self.x.ndim!=1 or self.points.ndim!=1 or
                np.any(np.diff(self.x)<=0) or np.any(np.diff(self.points)<=0) or
                self.x[0]!=0 or self.x[-1]!=1 or self.points[0]!=0 or self.points[-1]!=1 or
                not np.all(np.isin(self.x,self.points)) or self.size!=19*(n-1)+10):
            raise ValueError('same original mesh, all observation points and mixed packing required')
        self.h_indices=19*np.arange(n-1)
        self.gamma_indices=self.h_indices+3
        self.H_index=self.size-10
        self.a0_index=self.size-4
        self.L_index=self.size-1
        started=time.monotonic()
        COUNTS['height_operator_construction_attempts']+=1
        try:
            self.clock.check('before_original_C2_height_linear_basis')
            identity=np.eye(n)
            # SciPy's original not-a-knot spline is linear in its ordinates.
            derivative=original.CubicSpline(self.x,identity,axis=0).derivative()(self.x)
            h_data=np.zeros((n,3,n));h_data[:,0,:]=identity
            gamma_data=np.zeros((n,3,n))
            gamma_data[:,1,:]=identity
            gamma_data[:,2,:]=derivative
            # The real constructor OVERWRITES its first second derivative.
            gamma_data[0,2,:]=0.
            a0_data=np.zeros((n,3));a0_data[0,2]=1.
            self.h_basis=original.BPoly.from_derivatives(self.x,h_data)(self.points)
            self.gamma_basis=original.BPoly.from_derivatives(self.x,gamma_data)(self.points)
            self.a0_basis=original.BPoly.from_derivatives(self.x,a0_data)(self.points)
            if (self.h_basis.shape!=(len(self.points),n) or
                    self.gamma_basis.shape!=(len(self.points),n) or
                    self.a0_basis.shape!=(len(self.points),) or
                    not all(np.all(np.isfinite(a)) for a in
                            (self.h_basis,self.gamma_basis,self.a0_basis))):
                raise FloatingPointError('nonfinite original-C2 height basis')
            COUNTS['height_operator_basis_points']+=len(self.points)*(2*n+1)
            COUNTS['height_operator_constructions_completed']+=1
            self.clock.check('after_original_C2_height_linear_basis')
        finally:
            COUNTS['height_operator_construction_seconds']+=time.monotonic()-started
        self.identity={'original_source_sha256':ORIGINAL_SOURCE_SHA,
            'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'collocation_x_float64_sha256':_array_sha(self.x),
            'actual_readout_x_float64_sha256':_array_sha(self.points),
            'all_original_readout_points':len(self.points),'original_unknowns':self.size,
            'first_gamma_spline_acceleration_replaced_by_a0':True,
            'fixed_L_height_map_linear_on_entire_actual_C2_curve':True,
            'free_L_cubic_chain_retained':True,'continuous_or_roundoff_enclosure':False}

    def at_current(self,current):
        original.reduced.require_public_science()
        self.clock.check('before_same_state_new_height_constraint_values')
        started=time.monotonic();COUNTS['new_height_constraint_state_attempts']+=1
        try:
            states=np.asarray(current['states'],dtype=float)
            parameters=np.asarray(current['parameters'],dtype=float)
            z=np.asarray(current['z'],dtype=float)
            if (states.shape!=(19,len(self.x)) or parameters.shape!=(10,) or z.shape!=(self.size,) or
                    states[0,0]!=parameters[0] or states[3,0]!=0.):
                raise ValueError('same source-bound mixed center and full current state required')
            L=float(parameters[-1]);a0=float(parameters[6])
            # This is the original actual interpolant, needed once for the
            # new constraints. No original history or fine gate is called.
            curve=original.ActualC2StateCurve(self.x,states,parameters)
            h=np.asarray(curve.h(self.points),dtype=float)
            if not np.all(np.isfinite(h)) or np.any(h<=.8) or np.any(h>=3.):
                raise FloatingPointError('current actual height leaves its unchanged sampled physical box')
            C=np.zeros((len(self.points),self.size))
            C[:,self.H_index]=self.h_basis[:,0]
            C[:,self.h_indices]=self.h_basis[:,1:]
            C[:,self.gamma_indices]=L*self.gamma_basis[:,1:]
            C[:,self.a0_index]=L*L*self.a0_basis
            gamma_image=self.gamma_basis@states[3]
            imin=int(np.argmin(h));imax=int(np.argmax(h))
            result={'state_float64_sha256':_array_sha(z),'height':h,
                'fixed_length_height_matrix':C,'gamma_image':gamma_image,
                'length':L,'a0':a0,'height_point_min':float(h[imin]),
                'height_point_max':float(h[imax]),
                'height_min_at_index_x':[imin,float(self.points[imin])],
                'height_max_at_index_x':[imax,float(self.points[imax])],
                'all_original_height_points':len(self.points),'operator_identity':dict(self.identity)}
            COUNTS['new_height_constraint_actual_point_values']+=len(h)
            COUNTS['new_height_constraint_matrix_entries']+=int(C.size)
            COUNTS['new_height_constraint_states_completed']+=1
            self.clock.check('after_same_state_new_height_constraint_values')
            return result
        finally:
            COUNTS['new_height_constraint_state_seconds']+=time.monotonic()-started

    def polynomial_direction(self,current,geometry,direction):
        """h(z+t*d,L+t*dL)=h(z,L)+t*a1+t²*a2+t³*a3 exactly in real arithmetic."""
        self.clock.check('before_complete_original_L_height_chain')
        direction=np.asarray(direction,dtype=float)
        if (direction.shape!=(self.size,) or not np.all(np.isfinite(direction)) or
                geometry['state_float64_sha256']!=_array_sha(current['z'])):
            raise ValueError('finite actual direction and identical current height state required')
        L,a0=geometry['length'],geometry['a0']
        dL,da0=float(direction[self.L_index]),float(direction[self.a0_index])
        dg=np.r_[0.,direction[self.gamma_indices]]
        Gdg=self.gamma_basis@dg
        A=self.a0_basis
        a1=geometry['fixed_length_height_matrix']@direction+dL*(geometry['gamma_image']+2*L*a0*A)
        a2=dL*Gdg+(2*L*dL*da0+dL*dL*a0)*A
        a3=dL*dL*da0*A
        if not all(np.all(np.isfinite(a)) for a in (a1,a2,a3)):
            raise FloatingPointError('nonfinite full original length/height increment polynomial')
        COUNTS['complete_height_direction_polynomials']+=1
        COUNTS['height_polynomial_point_coefficients']+=3*len(self.points)
        return a1,a2,a3

    def sufficient_fraction(self,current,geometry,direction,fraction,safety):
        """A prefix-step bound on the SAME sampled height, with all L terms.

        For t<=t0 and nonnegative q, each t^j is at most (t/t0)*t0^j.
        Positive first-order growth and absolute quadratic/cubic terms
        therefore give a sufficient one-pass fraction. With dL=0 it is the
        usual exact affine fraction-to-boundary formula, up to roundoff.
        """
        original.reduced.require_public_science()
        if not np.isfinite(fraction) or fraction<0 or not 0<safety<1:
            raise ValueError('explicit finite trust fraction and physical-bound safety required')
        a1,a2,a3=self.polynomial_direction(current,geometry,direction)
        h=geometry['height'];t=float(fraction)
        nonlinear=abs(a2)*t*t+abs(a3)*t*t*t
        rise=np.maximum(a1,0)*t+nonlinear
        fall=np.maximum(-a1,0)*t+nonlinear
        best=1.;point=None;side=None
        for bound,margin,name in ((rise,3.-h,'upper'),(fall,h-.8,'lower')):
            positive=bound>0
            ratios=np.full(len(h),np.inf)
            ratios[positive]=safety*margin[positive]/bound[positive]
            index=int(np.argmin(ratios));value=float(ratios[index])
            if value<best:
                best=max(0.,value);point=index;side=name
        value=t*best
        COUNTS['same_point_height_fraction_predictions']+=1
        return {'input_fraction':t,'height_sufficient_fraction':value,
            'height_limits_fraction':bool(best<1.),'limiting_point_index':point,
            'limiting_point_x':None if point is None else float(self.points[point]),
            'limiting_height_before':None if point is None else float(h[point]),
            'limiting_side':side,'original_height_box':[.8,3.],
            'limiting_increment_polynomial':None if point is None else
                [float(a1[point]),float(a2[point]),float(a3[point])],
            'delta_length':float(direction[self.L_index]),
            'fixed_length_affine_case':bool(direction[self.L_index]==0.),
            'complete_cubic_L_chain_not_just_linearized_free_length':True,
            'all_original_actual_readout_height_points_checked':len(h),
            'no_eta_k_or_velocity_constraint_added':True,
            'sufficient_prefix_step_in_exact_arithmetic':True,
            'roundoff_or_continuous_curve_between_readout_points_certified':False}
