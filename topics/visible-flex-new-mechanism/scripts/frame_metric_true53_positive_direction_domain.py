#!/usr/bin/env python3
"""Read the paid true53 hard domain and qualify its genuinely new direction."""
from __future__ import annotations
import copy
from fractions import Fraction as Q
import numpy as np
from frame_height_null_coordinates import digest
from frame_entry_body_subspace import array_digest
from frame_entry_tail_height_blocks import _physical_gaps
from frame_metric_true53_paid_master_input import array, vector_record
from frame_metric_complete_maximin_projection import guard_compatible_interval
from frame_metric_true53_positive_direction_scope import (
    POLICY, require, SOURCE_CFG_SHA, SOURCE_PHYSICAL_SHA, SOURCE_DIRECTION_SHA)

def finite(value, shape, name):
    a=np.asarray(value,dtype=np.float64)
    require(a.shape==shape and np.all(np.isfinite(a)), "finite "+name+" required")
    return a

class PaidOriginalDomain:
    """No old model constructor, backend, hard-J build or ordinary value call."""
    def __init__(self,prepared,model,ledger):
        self.ledger=ledger
        ledger.check()
        self.field=prepared["problem"]
        self.cfg=copy.deepcopy(prepared["cfg"])
        self.cfg_sha256=digest(self.cfg)
        self.state=array(model["source_current_independent159"],(159,))
        require(np.array_equal(self.state,prepared["initial159"])
                and digest(self.field.identity(self.state))==SOURCE_PHYSICAL_SHA
                and self.cfg_sha256==SOURCE_CFG_SHA,
                "only the paid exact current53 physical point/domain is permitted")
        self.source_binding_sha256=model["binding_sha256"]
        self.source_binding=copy.deepcopy(model["binding"])
        d=model["original_domain"]
        self.M=array(d["physical_M"],(163,159))
        self.width=array(d["physical_width"],(163,))
        self.qscale=array(d["original_qscale"],(159,))
        self.step_scale=array(d["actual_step_scale"],(159,))
        self.K=(self.M*self.qscale[None,:])/self.width[:,None]
        require(np.all(self.width>0) and np.all(self.qscale>0)
                and np.all(self.step_scale>0)
                and array_digest(self.K)==d["normalized_K_sha256"]
                ==self.source_binding["K_sha256"],
                "the original coupled163 map/norm must be preserved")
        self.hard_J=array(d["hard_unscaled_physical159_J"],(2937,159))
        self.hard_base=array(d["hard_base_values"],(2937,))
        self.hard_targets=array(d["hard_frozen_targets"],(2937,))
        self.hard_h=array(d["hard_original_h_column"],(2937,))
        self.physical_rhs=array(d["physical_and_norm_original_rhs"],(652,))
        self.lower_x=array(d["outer_x_lower_z_then_h"],(160,))
        self.upper_x=array(d["outer_x_upper_z_then_h"],(160,))
        self.physical_lower=array(d["physical_original_lower163"],(163,))
        self.physical_upper=array(d["physical_original_upper163"],(163,))
        self.mu=float(model["physical_norm_cost_mu"])
        self.phi0=float(model["complete_original_phi0"])
        self.epsilon=float(Q(self.cfg["metric_proposal_epsilon_exact"]))
        self.target=float(model["constant_target"])
        self.tolerance=float(self.cfg["linear_model_residual_limit"])
        self.floor=float(self.cfg["linear_model_improvement_floor"])
        require(self.mu==1e-6 and self.epsilon==1e-8 and self.target==.26
                and self.phi0==.26601514422985395 and self.tolerance==1e-7
                and float(d["trust_B"])==.00025
                and np.array_equal(self.step_scale,.001*self.qscale),
                "the original mathematical scales or gates changed")
        self.grids=prepared["row_grids"]
        self.binding=copy.deepcopy(self.source_binding)
        self.binding_sha256=self.source_binding_sha256
        self.jets=None
        self.original_guard=copy.deepcopy(d["original_guard"])
        self.direction_history=[]
        ledger.check()

    def bind_jets(self,jets):
        require(jets.model_binding_sha256==self.source_binding_sha256
                and np.array_equal(jets.state,self.state)
                and jets.phi0==self.phi0,
                "necessary first-jet inputs must belong to this exact paid domain")
        self.jets=jets
        self.binding=copy.deepcopy(jets.binding)
        self.binding_sha256=jets.binding_sha256

    def residual(self,delta):
        self.ledger.check()
        delta=finite(delta,(159,),"actual independent159 displacement")
        z=delta/self.step_scale
        kz=self.K@z
        h=float(np.max(np.abs(kz),initial=0.))
        x=np.r_[z,h]
        parts={
            "hard":-self.hard_J@delta+self.hard_h*h-(self.hard_base-self.hard_targets),
            "physical_norm":np.r_[kz,-kz,kz-h,-kz-h]-self.physical_rhs,
            "upper_bound":x-self.upper_x,
            "lower_bound":self.lower_x-x}
        require(all(np.all(np.isfinite(v)) for v in parts.values()),
                "finite original-unit row residuals required")
        groups={key:{
            "count":len(value),
            "maximum_original_residual":float(np.max(value,initial=-np.inf)),
            "positive_tolerance_excess":float(np.max(value-self.tolerance,initial=0.)),
            "passes_original_tolerance":bool(np.all(value<=self.tolerance))}
            for key,value in parts.items()}
        return {
            "all_original_hard_physical_norm_bound_rows_passed":
                all(row["passes_original_tolerance"] for row in groups.values()),
            "maximum_original_row_residual":max(row["maximum_original_residual"] for row in groups.values()),
            "maximum_excess_over_original_tolerance":
                max(row["positive_tolerance_excess"] for row in groups.values()),
            "strict_model_all_rows_nonpositive":
                all(row["maximum_original_residual"]<=0 for row in groups.values()),
            "original_residual_tolerance":self.tolerance,
            "actual_physical_norm_h":h,"groups":groups,
            "row_count":2937+652+320}

    def validate_actual_candidate(self,candidate):
        self.ledger.check()
        candidate=finite(candidate,(159,),"new actual candidate")
        self.field.coordinates.validate(candidate)
        delta=candidate-self.state
        rows=self.residual(delta)
        linear_hard=self.hard_targets-(self.hard_base+self.hard_J@delta)
        box=self.field.coordinates.exact_box_decision(
            candidate,self.physical_lower,self.physical_upper)
        maximum=float(np.max(linear_hard,initial=-np.inf))
        eligible=bool(box["exact_original_box_pass"]
            and rows["all_original_hard_physical_norm_bound_rows_passed"]
            and maximum<=self.tolerance)
        return {
            "eligible":eligible,"model_binding_sha256":self.binding_sha256,
            "actual_delta_record":vector_record(delta),
            "actual_state_exact159":[str(Q.from_float(float(v))) for v in candidate],
            "actual_physical_exact163":[str(v) for v in self.field.coordinates.physical_exact(candidate)],
            "exact163_box":copy.deepcopy(box),"original_hard_margin_max_violation":maximum,
            "original_hard_tolerance":self.tolerance,"original_domain":rows,
            "no_current_geometry_JVP_or_derivative_recomputation":True,
            "affine_prediction_is_not_actual_geometry":True}

    def rounded_direction(self,paid_candidate):
        r=paid_candidate["unrounded_independent159_direction"]
        ideal=finite(r["binary64"],(159,),"paid new finite direction")
        require(r["length"]==159 and r["array_sha256"]==SOURCE_DIRECTION_SHA
                and array_digest(ideal)==SOURCE_DIRECTION_SHA
                and [str(Q.from_float(float(v))) for v in ideal]==r["exact_binary64"],
                "the actually paid full159 direction must be consumed unchanged")
        # All159 columns are independent, and the original subspace.apply is state+step.
        candidate=self.state+ideal
        actual=candidate-self.state
        preliminary=self.validate_actual_candidate(candidate)
        result={"candidate":candidate,"direction":actual,"ideal_direction":ideal,
            "preliminary_original_domain":preliminary,
            "actual_rounding_changed_direction":not np.array_equal(ideal,actual)}
        self.direction_history.append({
            "paid_direction_sha256":SOURCE_DIRECTION_SHA,
            "actual_direction_sha256":array_digest(actual),
            "rounding_changed":result["actual_rounding_changed_direction"],
            "untried_unit_candidate_exact159":[str(Q.from_float(float(v))) for v in candidate],
            "physical_unit_candidate_not_evaluated":True})
        return result

    def finish_direction(self,rounded,scan):
        require(self.jets is not None and scan["binding_sha256"]==self.binding_sha256
                and np.array_equal(scan["direction"],rounded["direction"]),
                "one completed rounded same-model full scan required")
        p=rounded["direction"]
        rows=rounded["preliminary_original_domain"]
        h=rows["original_domain"]["actual_physical_norm_h"]
        gain=self.phi0-float(scan["linear_maximum"])-self.mu*h
        qualified=bool(rows["eligible"] and gain>self.floor)
        upper,lower=_physical_gaps(self.field.coordinates,self.state,
                                  self.physical_lower,self.physical_upper)
        physical_step=self.M@p
        physical=[(float(gap),-float(delta),0.) for gap,delta in zip(upper,physical_step)]
        physical.extend((float(gap),float(delta),0.) for gap,delta in zip(lower,physical_step))
        interval=guard_compatible_interval(
            self.hard_base,self.hard_J@p,self.hard_targets,
            residual_tolerance=self.tolerance,physical_bounds=physical)
        report={
            "schema":POLICY+"-final-rounded-complete-direction",
            "paid_finite_direction_sha256":SOURCE_DIRECTION_SHA,
            "input_binding_sha256":self.binding_sha256,
            "source_model_binding_sha256":self.source_binding_sha256,
            "actual_rounded_direction":vector_record(p),
            "untried_unit_candidate":vector_record(rounded["candidate"]),
            "rounding_changed_paid_direction":rounded["actual_rounding_changed_direction"],
            "original_domain":copy.deepcopy(rows),"actual_physical_norm_h":h,
            "physical_norm_cost":self.mu*h,"complete_repaired_gain_d":gain,
            "complete_first_order_maximum":float(scan["linear_maximum"]),
            "original_complete_phi0":self.phi0,"original_minimum_gain":self.floor,
            "complete_two_grid_coverage":copy.deepcopy(scan["coverage"]),
            "complete_branch_attainers":copy.deepcopy(scan["branches"]),
            "guard_compatible_alpha_interval":copy.deepcopy(interval),
            "qualified_first_order_direction":qualified,
            "actual_unit_candidate_evaluated_or_accepted":False}
        return {"qualified":qualified,"direction":p,"candidate":rounded["candidate"],
                "scan":scan,"interval":interval,"report":report}

    def report(self):
        return {
            "schema":POLICY+"-paid-domain","source_model_binding_sha256":self.source_binding_sha256,
            "current_input_binding_sha256":self.binding_sha256,
            "original_domain_rows":2937+652+320,
            "new_hard_J_calls":0,"new_finite_LP_calls":0,"new_base_geometry_calls":0,
            "original_guard":copy.deepcopy(self.original_guard),
            "direction_history":copy.deepcopy(self.direction_history)}
