#!/usr/bin/env python3
"""Thin physical-flow adapter for the independent R300 numerical profile.

Only scalar_jets is replaced: every column uses that profile's shared raw
polynomial body before the original physical finite/domain handling.
The complete FFT RHS, physical rows, zero constant rows, Jacobian formulas
and original invalid-column NaN policy remain inherited.  No tail map,
Robin operator, accepted state or old scalar schema is manufactured.
"""
from __future__ import annotations
import hashlib
import os
from pathlib import Path

REPOSITORY="Rogerhu12/math-research-public"
SCHEMA="R300-current-continuous-nine-profile-original-physical-flow-v1"
PROFILE_NAME="geometry_20261115_continuous_nine_scalar_numeric.py"
PROFILE_SHA="93cc6608244deedd63beef8b1bb98aa308c4b3533067c103e8aeb652be66c89d"
ORIGINAL_NAME="geometry_20261114_full_dn_augmented.py"
ORIGINAL_SHA="f76b9c37b8549bc670ad5fe95ccc2da6c1da1a967256f21d23eba4973495d87e"


def require_actions():
    if (os.environ.get("GITHUB_ACTIONS")!="true"
            or os.environ.get("GITHUB_REPOSITORY")!=REPOSITORY):
        raise RuntimeError("Run the new physical profile only in this public repository Actions")


def source_receipt(path,expected_name,expected_sha):
    path=Path(path)
    raw=path.read_bytes()
    digest=hashlib.sha256(raw).hexdigest()
    if path.name!=expected_name or digest!=expected_sha:
        raise ValueError("The actual loaded physical/profile source differs: "+expected_name)
    return dict(file=path.name,bytes=len(raw),sha256=digest)


def wrap_augmented_flow(original_module,profile_module,probe,profile,workers=1):
    """Wrap the actual original module and explicit new profile, without setup().

    The caller retains the real source closure for the supplied original
    module/probe.  This adapter does not create a fake old prepared checkpoint.
    Direct calls to probe.profile outside this returned flow are outside this
    interface; no shared probe method or original module is monkey-patched.
    """
    require_actions()
    import numpy as np
    original_source=source_receipt(original_module.__file__,ORIGINAL_NAME,ORIGINAL_SHA)
    profile_source=source_receipt(profile_module.__file__,PROFILE_NAME,PROFILE_SHA)
    classes=(profile_module.NumericContinuousNineProfile,
        profile_module.FrozenShapes,profile_module.FrozenNine)
    if not isinstance(profile,classes):
        raise TypeError("Use the actual independently loaded R300 profile or frozen view")
    if not hasattr(profile,"raw_jet") or profile.parameter_count not in (0,3,9):
        raise ValueError("The complete current scalar view contract differs")

    class SameProfileAugmentedFlow(original_module.AugmentedFlow):
        def scalar_jets(self,x,parameters):
            x=np.asarray(x,dtype=float)
            parameters=np.asarray(parameters)
            if x.ndim!=1 or parameters.shape!=(self.k,len(x)):
                raise ValueError("Supply every actual node's current complete active parameters")
            answer=np.empty((len(x),3),dtype=np.result_type(parameters,float))
            for index,s in enumerate(x):
                # raw_jet never replaces the original physical domain policy.
                # In particular, a nonpositive radius/slope-domain failure is
                # handled by inherited physical(), after the complete jet.
                answer[index]=self.profile.raw_jet(s,parameters[:,index])
            return answer

    flow=SameProfileAugmentedFlow(probe,profile,workers)
    flow.r300_original_module=original_module
    flow.r300_profile_module=profile_module
    flow.r300_source_binding=dict(schema=SCHEMA,
        adapter_source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        original_augmented_flow=original_source,actual_profile_source=profile_source,
        actual_profile=profile.description(),field_modes=flow.M,
        active_scalar_parameters=flow.k,complete_physical_rows=flow.n,
        augmented_dimension=flow.dimension,
        changed_method="scalar_jets only: shared current raw polynomial body",
        original_physical_rhs_method_inherited=True,
        original_physical_invalid_columns_become_NaN=True,
        original_constant_core_and_scalar_rows_retained=True,
        original_complex_parameter_Jacobian_algorithm_inherited=True,
        baseline_cache_from_a_previous_profile_not_reused=True,
        direct_probe_profile_or_original_module_replaced=False,
        scalar_evaluation_order_changed_from_old_einsum_declared=True,
        accurate_target_evaluator_error_or_C2_proved=False,
        current_continuous_tail_boundary_or_J_supplied=False,
        actual_BVP_or_native_success=False)
    return flow


def frozen_six_shape_flow(flow,actual_nine_parameters):
    """New square-check view at the actual current nine-vector.

    Nothing in the input state, source flow, probe or old profile is changed.
    Only a new profile view and a new inherited-flow object are returned.
    """
    require_actions()
    import numpy as np
    p=np.asarray(actual_nine_parameters)
    if p.shape!=(9,) or not np.isrealobj(p) or not np.all(np.isfinite(p)):
        raise ValueError("Retain the complete actual real current nine coefficients")
    profile=flow.profile
    designed=profile if profile.parameter_count==9 else profile.designed
    view=designed.frozen_shapes(p[3:9])
    # The view's no-argument initial guess is the actual passed p, not the
    # design recipe's earlier active guess.  Explicit state rows still own p.
    view.initial_parameters=np.asarray(p[:3],float).copy()
    return wrap_augmented_flow(flow.r300_original_module,
        flow.r300_profile_module,flow.q,view,flow.workers)


def fully_frozen_flow(flow,actual_nine_parameters):
    """A new zero-active-parameter flow for same-new-g full physical checks."""
    require_actions()
    profile=flow.profile
    designed=profile if profile.parameter_count==9 else profile.designed
    view=designed.frozen_nine(actual_nine_parameters)
    return wrap_augmented_flow(flow.r300_original_module,
        flow.r300_profile_module,flow.q,view,flow.workers)
