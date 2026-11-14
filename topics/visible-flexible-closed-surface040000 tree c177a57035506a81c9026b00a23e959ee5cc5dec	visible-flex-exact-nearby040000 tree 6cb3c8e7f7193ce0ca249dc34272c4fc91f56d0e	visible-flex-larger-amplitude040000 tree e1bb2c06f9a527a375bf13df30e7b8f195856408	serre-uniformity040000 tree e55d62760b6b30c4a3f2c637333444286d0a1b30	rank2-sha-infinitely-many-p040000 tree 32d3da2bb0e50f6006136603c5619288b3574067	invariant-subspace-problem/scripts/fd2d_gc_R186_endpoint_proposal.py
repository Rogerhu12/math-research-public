"""R186 endpoint-QP proposal on an already saved signed36 normal.

This unexecuted recovery source changes parameter search constraints only.
It does not modify the actual Context, current field, finite residual,
normal, scales, damping, Schur packet, or Armijo threshold.

The added row is a proposal for the FULL direction endpoint. Backtracking
may stay outside the R186 interval. Its actual membership must be reported
separately; no K-sign conclusion follows merely from this QP being solved.
"""
from __future__ import annotations
import copy
import numpy as np
from fd2d_gc_archive_arrays import identity

CANDIDATE_SHA256='7c3f31de4b230e8d98b99c3e3914d65ae69daa3cb5c54ae22f585a36a888bfd1'
ORIGIN_SHA256='b075e4e5c3dd11b3725eaec47e4d0a5e681d12dd400a4a2e3aff0c3b2f5bd13f'
MID_BREAKS=(.90,.915,.985,.99)


def endpoint_profile_proposal(problem,*,lower=.027,profile_box=.08):
    """Return a shallow structural copy with one additional QP profile row.

    The copied object is for bounded_direction_from_schur only. The actual
    trial evaluator must keep its independently declared Context/domain.
    The root R182 provider, unknown map and all field methods are untouched.
    """
    lower,box=float(lower),float(profile_box)
    if not (np.isfinite(lower) and np.isfinite(box) and .027<=lower<=box<=.08):
        raise ValueError('Use an explicit endpoint lower bound within the proved binary interval')
    section=problem.profile_parameter_slice
    if section.stop-section.start!=7 or problem.parameter_count!=section.stop:
        raise ValueError('This proposal binds the current seven-profile-parameter layout')
    if getattr(problem,'_signed_origin_identity',{}).get('sha256')!=ORIGIN_SHA256:
        raise ValueError('The proved support family must bind the original immutable b075 archive')
    original=getattr(problem,'_signed_origin_arrays',{})
    if str(original.get('candidate_sha256',''))!=CANDIDATE_SHA256:
        raise ValueError('The physical base candidate differs from R186')
    if not np.array_equal(problem.profile.supports,original.get('profile_supports')):
        raise ValueError('The seven physical bump supports changed')
    windows=problem.signed_windows
    if len(windows)!=1 or tuple(map(float,windows[0]['breaks']))!=MID_BREAKS or int(windows[0]['sign'])!=1:
        raise ValueError('This explicit proposal is for the selected middle-positive-only branch')
    domain=problem.profile_domain
    matrix=np.asarray(domain['matrix'],float)
    rhs=np.asarray(domain['lower'],float)
    if matrix.ndim!=2 or matrix.shape[1]!=7 or rhs.shape!=(matrix.shape[0],):
        raise ValueError('The actual profile constraint packet has a different layout')
    row=np.zeros((1,7));row[0,-1]=1.
    target=copy.copy(problem)
    target.profile_domain=dict(domain,matrix=np.vstack((matrix,row)),lower=np.r_[rhs,lower])
    definition=dict(schema='fd2d-R186-explicit-same-normal-endpoint-proposal-v1',
        source=identity(__file__),candidate_sha256=CANDIDATE_SHA256,
        original_structural_field_sha256=ORIGIN_SHA256,
        profile_parameter_slice=[section.start,section.stop],
        constrained_global_parameter=section.stop-1,
        endpoint_lower=lower,endpoint_lower_exact=list(lower.as_integer_ratio()),
        actual_profile_box=box,actual_profile_box_exact=list(box.as_integer_ratio()),
        added_matrix_row=row[0].tolist(),old_profile_linear_rows=len(rhs),
        active_signed_windows=copy.deepcopy(windows),
        existing_radius_and_middle_K_rows_preserved=True,
        all_raw_field_variables_still_adjusted_through_original_Schur=True,
        endpoint_QP_constraint_only=True,actual_Context_domain_changed=False,
        original_normal_or_scaled_Schur_modified=False,
        actual_F_J_or_body_evaluations=0,
        backtracked_trial_R186_membership_must_be_checked_separately=True,
        continuous_K_claim_from_QP_success=False,strong_target_complete=False)
    return target,definition


def actual_profile_interval_membership(problem,actual_vector):
    """Read actual binary64 coefficients, without inventing a line-search result."""
    _,p=problem.unpack(np.asarray(actual_vector,float))
    delta=np.asarray(p[problem.profile_parameter_slice],float)
    if delta.shape!=(7,) or not np.all(np.isfinite(delta)):
        raise ValueError('Require the actual complete seven-delta trial values')
    inside=bool(np.all(np.abs(delta[:6])<=.08) and .027<=delta[6]<=.08)
    return dict(schema='fd2d-R186-actual-binary-profile-interval-membership-v1',
        actual_delta=delta.tolist(),
        actual_delta_exact=[list(float(x).as_integer_ratio()) for x in delta],
        proved_interval_membership=inside,
        profile_support_and_candidate_binding_required=True,
        actual_full_field_or_Armijo_evaluated_here=False,
        accepted_state_claimed=False,strong_target_complete=False)
