"""Finite nonzero B32 initializer, not a claimed Gauss--Codazzi solution.

Choose a true convex central curve at the requested gap, strictly positive
tail controls, and zero physical deltas. The terminal initializer uses a
complete positive trace reference before explicitly projecting its added
scalar trace to the declared raw angular space. That projection and P1
interpolation are measured by the actual objective, never called exact.
"""
from __future__ import annotations
from fractions import Fraction
import numpy as np
from scipy.optimize import brentq
from fd2d_gc_raw_lifted_dae import step5
from fd2d_gc_r181_b_round_raw_recovery import REPRESENTATION
from fd2d_gc_r181_b_point_objective_recovery import small_gap_parameter_certificate


def restore_gap_on_first_mode(problem,parameters,target,*,maximum_coefficient=.4):
    """Explicitly change the first central control; report the true change."""
    p=np.asarray(parameters,float).copy()
    if problem.base_kind!='circle' or problem.representation_kind!=REPRESENTATION:
        raise ValueError('Use the declared new circle-base B32 family')
    target=float(target);start=float(p[0])
    # This numerical bracket is an initialization choice, not an
    # infeasibility certificate for other central coefficients or curves.
    def gap(value):
        c=p[problem.central_slice].copy();c[0]=value
        return float(problem.core(c)[1]['gap'])-target
    lo,hi=-float(maximum_coefficient),float(maximum_coefficient)
    gl,gh=gap(lo),gap(hi)
    if not gl<=0<=gh:
        raise ValueError('The declared first-mode bracket does not contain this gap')
    root=brentq(gap,lo,hi,xtol=5e-15,rtol=8*np.finfo(float).eps)
    p[0]=root
    _,axes=problem.core(p[problem.central_slice])
    return p,dict(operation='finite actual first central coefficient root',
        before=start,after=float(root),parameter_change=float(root-start),
        actual_gap=float(axes['gap']),target_gap=target,bracket=[lo,hi],
        original_parameters_modified_in_place=False)


def finite_nonzero_seed(problem,*,tail_amplitude=None):
    if problem.representation_kind!=REPRESENTATION or problem.base_kind!='circle':
        raise ValueError('Select explicit new B32 circle-base source')
    if problem.gap<=0:raise ValueError('Use initial_vector for the exact zero-gap circle')
    amplitude=.4*problem.gap if tail_amplitude is None else float(tail_amplitude)
    if not 0<amplitude<1.2:raise ValueError('This nonzero seed uses an interior positive constant tail')
    z=problem.initial_vector();y,p=problem.unpack(z)
    p[:],gap_info=restore_gap_on_first_mode(problem,p,problem.gap)
    p[problem.tail_slice]=amplitude;p[problem.profile_slice]=0.
    # This scalar taper remains in the unchanged seed angular chart.
    left=float(problem.profile.central_end)
    right=min(left+.12,problem.blend[0])
    if not right>left:raise ValueError('New central taper has no room')
    taper=1-step5((problem.x-left)/(right-left))[0]
    coefficients=problem.core_coefficients@p[problem.central_slice]
    y[:,:problem.e]=taper[:,None]*coefficients
    ops=problem.operators(p[problem.profile_slice])
    lift=problem.lifting(p[problem.profile_slice],p[problem.tail_slice])
    # The unchanged positive-K terminal brake is an explicit named piece.
    final=problem.profile.base.segments[-1]
    if final.get('exact_endpoint_phase')!='-pi/2':
        raise ValueError('A declared true flat final phase is required')
    beginning=float(final['s0']);width=float(final['L'])
    mask=problem.x>=beginning
    full=lift['values'][:,mask]
    n,m,l=(full[...,j] for j in range(3));K=ops['jet']['K'][mask]
    radicand=(n-l)**2+4*m*m+4*K[None,:]
    if np.min(radicand)<0:raise FloatingPointError('Actual terminal trace radicand is negative')
    E=.5*(np.sqrt(radicand)-n-l)
    window=step5((problem.x[mask]-beginning)/(.5*width))[0]
    values=E*window[None,:]
    projection=(problem.PE@values).T
    y[mask,:problem.e]+=projection;y[mask,problem.d:]+=projection
    reconstructed=problem.E@projection.T
    difference=float(np.max(abs(reconstructed-values)))
    z=problem.impose_linear_boundary_values(z)
    certificate=small_gap_parameter_certificate(problem,z)
    if not certificate['passed']:raise ValueError('Explicit finite seed fails the continuous parameter domain')
    return z,dict(schema='fd2d-R181-B32-finite-nonzero-seed-v1',
        central_gap_root=gap_info,tail_constant=amplitude,profile_deltas=[0.]*7,
        central_taper=[left,right],terminal_reference_support=[beginning,problem.profile.end],
        terminal_full_reference='d=n-l,m unchanged; h=sqrt(d*d+4*m*m+4*K); add (h-n-l)/2 to n,l',
        terminal_window_full_on=[beginning+.5*width,problem.profile.end],
        maximum_actual_trace_projection_error=difference,
        raw_P1_between_saved_nodes=True,parameter_certificate=certificate,
        exact_boundary_map_reimposed=True,
        original_zero_reference_replaced_by_explicit_nonzero_field=True,
        actual_Codazzi_and_Gauss_not_claimed_zero=True,
        branch_existence_or_C1_continuation_not_assumed=True)
