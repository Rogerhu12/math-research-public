#!/usr/bin/env python3
"""The original cap/physical-box gate restricted to five exact null-height coordinates.

No geometry or optimizer is invoked by this module. The physical R66 condition
and its target are inherited. The numerical zero cap row and exact coupled-box
evaluation are explicit, separately identified changes of coordinate interface.
"""
from __future__ import annotations
import copy
from fractions import Fraction as Q
import math
import numpy as np
from frame_height_null_coordinates import digest

P=163
N=159


def coordinate_outer_bounds(coordinates,physical_lower,physical_upper):
    """Necessary pivot bounds only; these never replace the original coupled box."""
    lo=np.asarray(physical_lower,float);hi=np.asarray(physical_upper,float)
    if lo.shape!=(P,) or hi.shape!=(P,) or not np.all(np.isfinite([lo,hi])) or np.any(lo>=hi):
        raise ValueError('strict finite original physical coefficient bounds required')
    exact=coordinates.reference_exact
    a=list(lo[:154]);b=list(hi[:154])
    for j in range(3):
        a.append(float(exact[j]-Q.from_float(float(hi[154+j]))))
        b.append(float(exact[j]-Q.from_float(float(lo[154+j]))))
    for j in [6,7]:
        a.append(float(Q.from_float(float(lo[154+j]))-exact[j]))
        b.append(float(Q.from_float(float(hi[154+j]))-exact[j]))
    # Expand rounded pivot bounds outward by one representable number. They are
    # merely a necessary coordinate envelope; exact original boxes decide trials.
    a=np.array(a,float);b=np.array(b,float)
    a[154:]=np.nextafter(a[154:],-np.inf);b[154:]=np.nextafter(b[154:],np.inf)
    return a,b


class FiveNullHeightGate:
    def __init__(self,original_gate,field,physical_lower,physical_upper):
        original=field.original_problem;reference=field.coordinates.reference_state
        original_gate.assert_context(original,reference)
        if original_gate.nunknown!=P or original_gate.kind!='frozen-frame':
            raise ValueError('the validated original frozen-frame cap gate is required')
        if np.any(np.asarray(original_gate.row)[:154]!=0):
            raise ValueError('original cap height must be independent of all tangent coefficients')
        self.original_gate=original_gate
        self.coordinates=field.coordinates
        self.reference_height=float(original_gate.height(reference))
        self.family=copy.deepcopy(original_gate.family)
        self.kind='frozen-frame';self.nunknown=N
        self.side=int(original_gate.side);self.length=float(original_gate.length)
        self.target=float(original_gate.target);self.intercept=self.reference_height
        self.row=np.zeros(N);self.row.flags.writeable=False
        self.weights=np.zeros(5);self.weights.flags.writeable=False
        self.height_slice=slice(154,N)
        self.physical_definition=copy.deepcopy(original_gate.physical_definition)
        self.physical_sha256=original_gate.physical_sha256
        self.coordinate_definition_sha256=field.coordinate_definition_sha256
        self.original_lower=np.asarray(physical_lower,float).copy()
        self.original_upper=np.asarray(physical_upper,float).copy()
        self.coordinate_lower,self.coordinate_upper=coordinate_outer_bounds(
            field.coordinates,self.original_lower,self.original_upper)
        self.problem_evaluation=copy.deepcopy(field.evaluation_definition())
        self.problem_evaluation_sha256=digest(self.problem_evaluation)
        self.numerical_definition={
            'schema':'exact-null-height-coordinate-restriction-of-original-cap-gate-v1',
            'original_numerical_gate_sha256':original_gate.numerical_sha256,
            'original_physical_gate_sha256':self.physical_sha256,
            'coordinate_definition_sha256':self.coordinate_definition_sha256,
            'reference_constant_cap_height_evaluated':str(Q.from_float(self.reference_height)),
            'target_evaluated':str(Q.from_float(self.target)),
            'independent_cap_row_exact':['0']*N,
            'null_reason':'exact rational integral row times H is zero',
            'no_rounded_original_row_times_H_used_as_the_mathematical_cap_row':True,
            'problem_evaluation':self.problem_evaluation,
            'original_physical_lower_exact':[str(Q.from_float(float(x))) for x in self.original_lower],
            'original_physical_upper_exact':[str(Q.from_float(float(x))) for x in self.original_upper],
            'coordinate_bounds_are_only_necessary_pivot_envelopes':True,
            'candidate_box_gate_uses_exact_full163_rational_coefficients':True,
            'no_validated_reference_primitive_error_enclosure_is_claimed':True}
        self.numerical_sha256=digest(self.numerical_definition)
        self.reference_provenance={'original_gate_reference':copy.deepcopy(original_gate.reference_provenance),
            'restriction_reference_physical_sha256':field.coordinates.reference_sha256,
            'zero_coordinates_have_the_same_original_physical_identity':True}
        for a in [self.original_lower,self.original_upper,self.coordinate_lower,self.coordinate_upper]:
            a.flags.writeable=False

    def assert_context(self,problem,state):
        q=problem.coordinates.validate(state)
        if problem.coordinate_definition_sha256!=self.coordinate_definition_sha256:
            raise ValueError('exact five-height coordinate map or reference changed')
        self.original_gate.assert_context(problem.original_problem,
            problem.coordinates.reference_evaluation_state(q))
        if problem.evaluation_definition()!=self.problem_evaluation:
            raise ValueError('height primitive or exact-polynomial evaluation changed during this stage')

    def height(self,state):
        q=np.asarray(state,float)
        if q.shape!=(N,) or not np.all(np.isfinite(q)):
            raise ValueError('finite full159 independent state required')
        return self.reference_height

    def margin(self,state):return self.height(state)-self.target

    def reconstructed_height(self,data):
        return self.original_gate.reconstructed_height(data)

    def decision(self,state,data,lower,upper,*,box_tolerance=0.,height_tolerance=0.,
                 reconstruction_tolerance=1e-10):
        """Same cap tolerances; exact affine physical boxes rather than independent tau boxes."""
        q=np.asarray(state,float);lo=np.asarray(lower,float);hi=np.asarray(upper,float)
        if (q.shape!=(N,) or not np.all(np.isfinite(q)) or lo.shape!=(N,) or hi.shape!=(N,)
                or not np.array_equal(lo,self.coordinate_lower) or not np.array_equal(hi,self.coordinate_upper)):
            raise ValueError('the declared159 pivot envelope and complete independent state are required')
        if min(box_tolerance,height_tolerance,reconstruction_tolerance)<0:
            raise ValueError('nonnegative inherited gate tolerances required')
        # The exact map is supplied by the field at construction and is immutable.
        coordinates=self.coordinates
        exact_box=coordinates.exact_box_decision(q,self.original_lower,self.original_upper)
        physical=coordinates.physical_exact(q)
        gaps=[Q.from_float(float(self.original_lower[j]))-physical[j] for j in range(P)]
        gaps += [physical[j]-Q.from_float(float(self.original_upper[j])) for j in range(P)]
        violation=max([Q(0),*gaps])
        affine=self.height(q);actual=self.reconstructed_height(data)
        row_margin=affine-self.target;geometry_margin=actual-self.target;difference=abs(actual-affine)
        eligible=(exact_box['exact_original_box_pass'] and row_margin>=-height_tolerance
            and geometry_margin>=-height_tolerance and difference<=reconstruction_tolerance)
        return {'eligible_under_declared_numerical_gate_tolerances':bool(eligible),
            'box_violation':float(violation),'box_violation_exact':str(violation),
            'exact_original_physical_box_pass':exact_box['exact_original_box_pass'],
            'violating_original_physical_box_indices':exact_box['violating_physical_indices'],
            'affine_height_evaluated':affine,'reconstructed_common_cap_height_evaluated':actual,
            'target_height_evaluated':self.target,'affine_height_margin':row_margin,
            'reconstructed_height_margin':geometry_margin,
            'reconstructed_minus_affine_height_absolute':difference,
            'box_tolerance':box_tolerance,'height_tolerance':height_tolerance,
            'height_reconstruction_consistency_tolerance':reconstruction_tolerance,
            'box_test_is_exact_and_does_not_use_coordinate_envelope_as_a_substitute':True,
            'both_height_margins_nonnegative_in_current_arithmetic':bool(row_margin>=0 and geometry_margin>=0),
            'constant_cap_not_inserted_as_an_exact_zero_margin_LP_row':True,
            'gate_is_not_a_continuous_height_integral_or_reach_certificate':True}

    def record(self):
        return {'physical_definition':self.physical_definition,'physical_gate_sha256':self.physical_sha256,
            'numerical_definition':self.numerical_definition,'numerical_gate_sha256':self.numerical_sha256,
            'initial_reference_provenance':self.reference_provenance}

    @classmethod
    def from_original(cls,original_gate,field,physical_lower,physical_upper):
        gate=cls(original_gate,field,physical_lower,physical_upper)
        if not field.coordinates.exact_box_decision(field.initial_state(),physical_lower,physical_upper)['exact_original_box_pass']:
            raise ValueError('the restoration reference is outside the original exact physical box')
        return gate
