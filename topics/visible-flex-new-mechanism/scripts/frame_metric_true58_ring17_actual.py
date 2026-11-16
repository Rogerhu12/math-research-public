#!/usr/bin/env python3
"""Original whole-grid gates for the true58-ring17 nonlinear complete168 candidates.

Import-only. This owner charges each started ordinary call to the one new
scope. It evaluates the unchanged fourteen gate definitions on current full
geometry, with an explicit exact172 coefficient-box extension. No old159
derivatives, developer suites, independent initial replay or final replay.
Accepted selected position jets are exported only from the same live
ordinary after value-only learning.
"""
from __future__ import annotations
import copy
from fractions import Fraction as Q
import numpy as np
from frame_height_null_coordinates import digest
from frame_entry_body_subspace import array_digest
from frame_metric_epigraph import geometry_values
from frame_metric_spectral_recovery import spectral_proposal_rows
from frame_metric_epigraph_dense import mirror_values
from frame_curvature_epigraph_exchange import curvature_forms, curvature_rows, POSITION_JETS
from frame_metric_budget_recovery import recovery_decision, separation
from frame_metric_spectral_soc_scaling import compact_with_all_actual_gates
from frame_metric_paid_cone_vector import actual_acceptance
from frame_metric_true58_ring17_scope import POLICY, Ring58Ledger, require
from frame_complete_body_extension168 import array_binding
from frame_complete_body_extension168_selected_cache import (
    POLICY as SELECTED_CACHE_POLICY, export_selected_current168_geometry)

EXPECTED_POLICY = "true58-ring17-original-box-curvature-and-one-nonlinear-candidate-v1"
SOURCE_PROVENANCE = {
    "accepted_index": 58,
    "run_id": "43859882465", "research_job_id": "133273598120",
    "source_commit": "0e6fafbf7bce37cd851dfc972b2de1ff3d0d5881",
    "physical_state_sha256":
        "94950b2bd5d7b5241e14333a4315b073f64840f74849a7909d6de8cb3cc29f54",
    "closed_ancestor_scientific_seconds": 2830.778901609,
    "closed_ancestor_full_values": 147,
    "closed_ancestor_costs_are_not_new_scope_debits": True}

def array_record(value):
    a = np.asarray(value)
    require(a.dtype.kind in "fiu" and np.all(np.isfinite(a)), "finite original numeric array")
    return {"dtype":str(a.dtype),"shape":list(a.shape),"array_sha256":array_digest(a),
            "values":a.tolist()}

class Ring58HeightGate:
    """The unchanged null-height gate and an additional literal new9 box."""
    def __init__(self, prepared):
        self.prepared=prepared
        self.original=prepared["gate"]
        self.field=prepared["field168"]
        self.old_lower=np.asarray(prepared["lower"],float).copy()
        self.old_upper=np.asarray(prepared["upper"],float).copy()
        self.lower172=np.asarray(prepared["lower172"],float).copy()
        self.upper172=np.asarray(prepared["upper172"],float).copy()
        self.coordinate_lower=np.r_[self.old_lower,np.full(9,-.25)]
        self.coordinate_upper=np.r_[self.old_upper,np.full(9,.25)]
        self.side=self.original.side
        self.length=self.original.length
        self.target=self.original.target
        self.kind=self.original.kind
        self.nunknown=168
        self.row=np.zeros(168)
        self.physical_sha256=self.original.physical_sha256
        self.definition={
            "schema":POLICY+"-exact172-and-original-cap-gate",
            "original159_gate":self.original.record(),
            "new9_box_lower_exact":["-1/4"]*9,
            "new9_box_upper_exact":["1/4"]*9,
            "same_constant_cap_height_reason":"delta_z=.81*gamma*P8 has zero endpoint values",
            "full168_geometry_is_evaluated_at_actual_candidate":True,
            "candidate_subspace_is_original_ring17":True,
            "original163_box_retained_exactly":True,
            "all172_physical_coefficients_checked_exactly":True}
        self.numerical_sha256=digest(self.definition)
    def assert_context(self,problem,state):
        q=self.field.validate_state(state)
        require(problem is self.field,
                "the complete current168 field must own the original cap gate")
        self.original.assert_context(self.field.original_field,q[:159])
    def height(self,state):
        self.assert_context(self.field,state)
        return self.original.height(np.asarray(state)[:159])
    def margin(self,state):
        return self.height(state)-self.target
    def decision(self,state,data,lower,upper,*,box_tolerance=0.,
                 height_tolerance=0.,reconstruction_tolerance=1e-10):
        self.assert_context(self.field,state)
        require(np.array_equal(lower,self.coordinate_lower)
                and np.array_equal(upper,self.coordinate_upper),
                "literal declared168 envelope required; it does not replace physical172")
        q=np.asarray(state,float)
        original=self.original.decision(
            q[:159],data,self.old_lower,self.old_upper,
            box_tolerance=box_tolerance,height_tolerance=height_tolerance,
            reconstruction_tolerance=reconstruction_tolerance)
        exact=self.field.exact_full_box_decision(q,self.lower172,self.upper172)
        values=self.field.full_coefficients(q,exact=True)
        gap=max([Q(0)]+[
            Q.from_float(float(self.lower172[i]))-values[i] for i in range(172)]+[
            values[i]-Q.from_float(float(self.upper172[i])) for i in range(172)])
        result=copy.deepcopy(original)
        result.update(
            eligible_under_declared_numerical_gate_tolerances=bool(
                original["eligible_under_declared_numerical_gate_tolerances"]
                and exact["exact_full_box_pass"]),
            box_violation=float(gap),box_violation_exact=str(gap),
            exact_full172_physical_box_pass=exact["exact_full_box_pass"],
            full172_box=exact,
            original159_cap_and_box_receipt=original,
            original163_box_was_not_used_as_a_substitute_for_new172=True,
            unchanged_constant_height_includes_complete_new_height_primitive=True)
        return result

def row_tolerances(cfg):
    return np.asarray([cfg["metric_row_tolerance"]]*2+[cfg["signed_height_tolerance"]]
        +[cfg["shape_constraint_tolerance"]]*3+[cfg["mirror_polynomial_tolerance"]]
        +[cfg["curvature_row_tolerance"]]*4)

def rows_from_paid_geometry(data,side,cfg):
    """The original eleven-row order, using this actual ordinary cache."""
    val=geometry_values(data)
    e,f=val["e"],val["f"]
    data.update(e=e,f=f,eta=val["eta"])
    cm,cp=spectral_proposal_rows(e,f,float(Q(cfg["fixed_metric_budget_exact"])),
        float(Q(cfg["metric_proposal_epsilon_exact"])))
    X=data["X"]
    strip=float(Q(cfg["hard_strip_half_width_exact"]))
    radius=float(Q(cfg["hard_ball_radius_exact"]))
    mirror=mirror_values(data,float(Q(cfg["mirror_target_exact"])))
    data["mirror_polynomial"]=mirror["polynomial"]
    scale=float(Q(cfg["curvature_scale_exact"]))
    zeta=float(Q(cfg["fixed_hard_curvature_cap_exact"]))/scale
    cr,_=curvature_rows(data["curvature"],zeta,scale)
    return np.concatenate([np.stack([
        cm,cp,side*X[...,2]-float(Q(cfg["minimum_signed_height_exact"])),
        1-np.sum(X*X,axis=-1)/radius**2,1-X[...,1]/strip,1+X[...,1]/strip,
        mirror["polynomial"]]),np.moveaxis(cr,-1,0)],axis=0)

class Ring58Actual:
    def __init__(self,prepared,completed,ledger):
        require(POLICY==EXPECTED_POLICY, "the new actual58 ring17 policy is required")
        require(isinstance(ledger,Ring58Ledger),"one new600-second ledger required")
        require(ledger.limits.get("science_seconds")==600
                and ledger.limits.get("actual_trial_pairs")==1
                and ledger.limits.get("actual_grid_values")==2,
                "this actual owner requires the frozen 600-second/1-pair/2-value scope")
        self.prepared,self.completed,self.ledger=prepared,completed,ledger
        self.field,self.cfg=prepared["field168"],prepared["cfg"]
        self.gate=Ring58HeightGate(prepared)
        self.source_point=copy.deepcopy(completed["point"])
        require(self.source_point["accepted_index"]==58
                and self.source_point["physical_state_sha256"]==
                "94950b2bd5d7b5241e14333a4315b073f64840f74849a7909d6de8cb3cc29f54",
                "actual58 is the sole starting accepted point")
        self.selected_point=copy.deepcopy(self.source_point)
        self.pools={label:np.asarray(prepared[label+"_pool"],dtype=np.int64).copy()
                    for label in ("coarse","fine")}
        cp=completed["source_stage"]
        self.versions={label:int(cp[label+"_pool_version"]) for label in self.pools}
        self.source_pool_history_sha256={label:digest({
            "paid_prior_history_sha256":cp["source_pool_history_sha256"][label],
            "source58_new_history":cp["new_pool_histories"][label]}) for label in self.pools}
        self.pool_histories={label:[] for label in self.pools}
        self.trials=[]
        self.value_events=[]
        self.accepted_data=None
        self.accepted_state=None
        self._accepted_cache_payload=None
        self.selected_export_captures={}
        self.accepted_cache_export_status={
            "status":"not-started", "selected_export_complete":False,
            "ordinary_geometry_calls":0, "parameter_Jacobian_calls":0,
            "errors":[]}
        self.stopped_for_new_rows=False
        self.evaluation_definition={
            "schema":POLICY+"-ordinary-original-fourteen-gates",
            "new_field":self.field.evaluation_definition(),
            "source58_physical_sha256":self.source_point["physical_state_sha256"],
            "source58_provenance":copy.deepcopy(SOURCE_PROVENANCE),
            "original_cfg_sha256":digest(self.cfg),
            "gate":self.gate.definition,
            "source_accepted_index":58,"new_accepted_index":59,
            "all14_original_whole_grid_predicates_retained":True,
            "exact_new172_box_is_additional":True,
            "accepted_cache_selected_export_schema":SELECTED_CACHE_POLICY,
            "accepted_selected_export_follows_complete_value_only_learning":True,
            "full_U_T_cache_is_retained_in_addition_to_selected_position_jets":True,
            "source_configuration_160_1800_is_not_a_new_task_limit":True,
            "new_scope600_has_at_most1_actual_pair_and2_actual_values":True,
            "necessary_model_work_is_owned_by_the_same_new_scope":True,
            "old159_bank_defect_gamma_and_controller_not_trained_or_applied":True}
        self.evaluation_sha256=digest(self.evaluation_definition)
    def theta(self,label):
        if label=="coarse":
            return self.prepared["theta"]
        require(label=="fine","coarse or fine grid required")
        # Exact original58 complete fine-grid binary64 values, already source-bound.
        return self.prepared["fine_theta"]
    def evaluate(self,state,label):
        q=self.field.validate_state(state)
        self.gate.assert_context(self.field,q)
        physical=digest(self.field.identity(q))
        event=self.ledger.begin("actual_grid_values",grid=label,
            physical_state_sha256=physical,independent_count=168,physical_count=172)
        self.value_events.append(event)
        try:
            data=self.field.geometry(q,self.prepared["radial"],self.theta(label),
                                     self.prepared["order"],jacobian=False)
            data["radial"]=np.asarray(self.prepared["radial"],float)
            data["theta"]=np.asarray(self.theta(label),float)
            expected=(len(data["radial"]),len(data["theta"]),3)
            require(all(np.asarray(data[k]).shape==expected
                        and np.all(np.isfinite(data[k])) for k in POSITION_JETS),
                    "complete finite current six position jets required")
            data["curvature"]=curvature_forms(data,self.cfg)
            decision=recovery_decision(self.field,self.gate,q,data,
                self.gate.coordinate_lower,self.gate.coordinate_upper,
                self.cfg,forms=data["curvature"])
            rows=rows_from_paid_geometry(data,self.gate.side,self.cfg)
            compact=compact_with_all_actual_gates(decision)
            compact["exact_full172_physical_box_pass"]=decision["cap_and_box"][
                "exact_full172_physical_box_pass"]
            self.ledger.end(event,grid_shape=list(expected[:2]),
                original_actual_gate_booleans=compact["actual_gate_booleans"],
                direct_max_eta=decision["direct_max_eta"])
            self.ledger.check("actual-grid.completed")
            return {"data":data,"decision":decision,"compact":compact,"rows":rows,
                    "state":q.copy(),"grid":label,
                    "ordinary_value_event":copy.deepcopy(event)}
        except Exception as error:
            if event.get("status")=="started":
                self.ledger.end(event,error)
            raise
    def learn(self,cache):
        label=cache["grid"]
        missing,detail=separation(cache["rows"],self.pools[label],
                                 row_tolerances(self.cfg),cache["data"]["eta"])
        ids=np.flatnonzero(missing)
        capacity=int(self.cfg["max_pool_rows" if label=="coarse"
                              else "max_fine_physical_pool_rows"])
        record={"grid":label,"detail":detail,"new_original_row_ids":ids.tolist(),
                "old_pool_version":self.versions[label],"new_rows":0,
                "current_actual_cache_only":True,"ordinary_reexecution":False}
        if len(self.pools[label])+len(ids)>capacity:
            record["capacity_would_be_exceeded"]=True
        elif len(ids):
            self.pools[label]=np.r_[self.pools[label],ids]
            self.versions[label]+=1
            record["new_rows"]=len(ids)
            record["new_pool_version"]=self.versions[label]
            self.pool_histories[label].append(copy.deepcopy(record))
        return record
    def trial(self,state,alpha,prediction,*,emit=None):
        require(self.accepted_state is None and not self.stopped_for_new_rows,
                "one acceptance or new rows close this finite-candidate actual stage")
        q=self.field.validate_state(state)
        require(not np.array_equal(q,self.prepared["center168"]),
                "a distinct complete168 actual trial is required")
        event=self.ledger.begin("actual_trial_pairs",alpha=float(alpha))
        record={"number":len(self.trials)+1,"alpha":float(alpha),"status":"started",
                "prediction":copy.deepcopy(prediction),"state":self.field.state_record(q),
                "physical_state_sha256":digest(self.field.identity(q)),
                "accepted_as_next_iterate":False,"coarse":None,"fine":None}
        self.trials.append(record)
        coarse=fine=None
        try:
            coarse=self.evaluate(q,"coarse")
            record["coarse"]=copy.deepcopy(coarse["compact"])
            c=coarse["decision"]
            old=float(self.source_point["maximum_eta_on_both_grids"])
            minimum=float(Q(self.cfg["minimum_accepted_eta_decrease_exact"]))
            possible=bool(c["single_grid_admissible_recovery_point"]
                and c["direct_max_eta"]<old
                and (old-c["direct_max_eta"]>=minimum or c["single_grid_new_target_qualified"]))
            if possible:
                fine=self.evaluate(q,"fine")
                record["fine"]=copy.deepcopy(fine["compact"])
            acceptance=actual_acceptance(old,c,
                None if fine is None else fine["decision"],minimum)
            record["original_acceptance"]=acceptance
            record["learning"]=[self.learn(cache) for cache in (coarse,fine) if cache is not None]
            self.stopped_for_new_rows=any(row["new_rows"] or row.get("capacity_would_be_exceeded")
                                         for row in record["learning"])
            record["new_row_or_capacity_stop"]=self.stopped_for_new_rows
            if acceptance["accepted"]:
                require(fine is not None,"both actual grids required")
                exact=self.field.exact_full_box_decision(q,
                    self.prepared["lower172"],self.prepared["upper172"])
                require(exact["exact_full_box_pass"],"true172 exact box required")
                for row in (coarse["compact"],fine["compact"]):
                    require(len(row["actual_gate_booleans"])==14
                        and all(v is True for v in row["actual_gate_booleans"].values()),
                        "all fourteen original actual predicates must pass")
                point={
                    "schema":POLICY+"-accepted168-point","accepted_index":59,
                    "physical_state_sha256":record["physical_state_sha256"],
                    "coordinate_definition_sha256":self.field.coordinate_definition_sha256,
                    "independent_coordinates_binary64":q.tolist(),
                    "exact_binary64_independent168_coordinates":[str(Q.from_float(float(v))) for v in q],
                    "exact_physical172_coefficients":[str(v) for v in self.field.full_coefficients(q,exact=True)],
                    "source_independent168_exact":copy.deepcopy(self.source_point["exact_binary64_independent168_coordinates"]),
                    "coarse":copy.deepcopy(coarse["compact"]),"fine":copy.deepcopy(fine["compact"]),
                    "maximum_eta_on_both_grids":acceptance["maximum_eta_on_both_grids"],
                    "maximum_curvature_on_both_grids":max(
                        cache["decision"]["direct_maximum_absolute_principal_curvature"]
                        for cache in (coarse,fine)),
                    "new_metric_target_qualified_on_both_grids":acceptance["both_new_metric_targets_qualified"],
                    "objective_evaluation_sha256":self.evaluation_sha256,
                    "complete_new_field_evaluation_sha256":self.field.definition_sha256,
                    "exact_full_box":exact,"reason":"actual58 ring17 candidate original two-grid acceptance",
                    "main_readme_completion_claim":False}
                self.selected_point=point
                self.accepted_state=q.copy()
                self.accepted_data={"coarse":coarse,"fine":fine}
                record.update(accepted_as_next_iterate=True,accepted_index=59,
                              actual_eta_decrease=acceptance["actual_eta_decrease"])
            record["status"]="complete"
            self.ledger.end(event,accepted=record["accepted_as_next_iterate"],
                fine_evaluated=fine is not None,new_row_or_capacity_stop=self.stopped_for_new_rows)
            if emit is not None:
                record["stdout_receipt"]=emit("ACTUAL_TRIAL",record)
            self.ledger.check("actual-pair.completed")
            return record
        except Exception as error:
            record.update(status="raised",error={"type":type(error).__name__,"message":str(error)})
            if event.get("status")=="started":
                self.ledger.end(event,error)
            if emit is not None and "stdout_receipt" not in record:
                record["stdout_receipt"]=emit("ACTUAL_TRIAL",record)
            raise
    def _selected_partial_record(self,label,source_identity,capture):
        """Serialize only arrays that the published exporter already copied."""
        record={
            "schema":POLICY+"-selected-export-partial",
            "grid":label, "source_identity":copy.deepcopy(source_identity),
            "export_capture":{key:copy.deepcopy(value) for key,value in capture.items()
                if key not in ("_selected_arrays","payload")},
            "status":"partial", "complete_selected_cache_reusable":False,
            "no_ordinary_or_derivative_reexecution":True}
        if isinstance(capture.get("payload"),dict):
            # A post-export clock failure may occur after the helper made its payload.
            # Preserve it, but do not relabel the failed export as a reusable success.
            record["completed_payload_before_raise"]=capture["payload"]
            record["partial_arrays"]={}
        else:
            record["partial_arrays"]={}
            record["partial_array_serialization_errors"]=[]
            for name,value in capture.get("_selected_arrays",{}).items():
                try:
                    record["partial_arrays"][name]=array_record(value)
                except Exception as error:
                    record["partial_array_serialization_errors"].append({
                        "array":name,"type":type(error).__name__,"message":str(error)})
        return record
    def accepted_cache_payload(self):
        """Keep paid full first jets and export post-learning selected two-jets once.

        A partial export does not undo a genuine original14 acceptance. Its
        arrays and owner identity are retained with status=partial and cannot
        be consumed as a complete selected cache. All export/serialization
        time still belongs to the same enclosing ledger and final clock.
        """
        if self.accepted_data is None:
            return None
        if self._accepted_cache_payload is not None:
            return self._accepted_cache_payload
        q=self.accepted_state
        started=self.ledger.elapsed()
        payload={
            "schema":POLICY+"-accepted-first-jet-cache",
            "kind":"accepted-point-paid-geometry",
            "available":True,"status":"started",
            "accepted_independent168":None,
            "grids":{}, "selected_current168_geometry":{},
            "selected_export_partial":{}, "selected_export_errors":[],
            "first_jet_serialization_errors":[],
            "no_extra_geometry_or_derivatives_executed":True,
            "full_grid_U_T_retained":True,
            "full_grid_positions_and_two_jets_not_serialized":True,
            "current_parameter_J_not_serialized":True,
            "partial_selected_exports_are_not_reusable_complete_inputs":True,
            "all_export_and_output_time_is_owned_by_the_same600_scope":True}
        # Install the owner capture first: no repeated export is allowed after failure.
        self._accepted_cache_payload=payload
        self.accepted_cache_export_status.update(
            status="started",started_scientific_seconds=started,
            grid_status={},errors=[])
        selected_bindings={}
        ordinary_bindings={}
        pool_bindings={}
        for label in ("coarse","fine"):
            cache=self.accepted_data[label]
            data=cache["data"]
            pool_binding=array_binding(np.asarray(self.pools[label],dtype=np.int64))
            pool_bindings[label]={
                "row_ids":pool_binding,"pool_version":int(self.versions[label]),
                "literal_original_pool_order_preserved":True,
                "source_pool_history_sha256":self.source_pool_history_sha256[label],
                "new_pool_history_sha256":digest(self.pool_histories[label])}
            source_identity={
                "schema":POLICY+"-accepted-selected-owner",
                "kind":"new-actual-current59-ordinary-after-value-only-learning",
                "grid":label,"source_accepted_index":58,"accepted_index":59,
                "physical_state_sha256":self.selected_point["physical_state_sha256"],
                "coordinate_definition_sha256":self.field.coordinate_definition_sha256,
                "field_evaluation_sha256":self.field.definition_sha256,
                "objective_evaluation_sha256":self.evaluation_sha256,
                "source58":copy.deepcopy(SOURCE_PROVENANCE),
                "ordinary_value_event":copy.deepcopy(cache["ordinary_value_event"]),
                "actual_original14_gates":copy.deepcopy(
                    cache["compact"]["actual_gate_booleans"]),
                "after_learning_pool":copy.deepcopy(pool_bindings[label]),
                "ordinary_geometry_was_already_charged":True,
                "this_binding_or_export_adds_no_ordinary_or_J":True}
            capture={}
            self.selected_export_captures[label]={
                "source_identity":source_identity,"capture":capture}
            self.accepted_cache_export_status["grid_status"][label]="started"
            try:
                self.ledger.check("accepted-cache."+label+".before-existing-ordinary-binding")
                ordinary_bound=self.field.bind_ordinary(
                    q,data["radial"],data["theta"],data,source_identity)
                ordinary_bindings[label]=ordinary_bound["binding_sha256"]
                exported=export_selected_current168_geometry(
                    self.field,q,data["radial"],data["theta"],
                    self.pools[label],ordinary_bound,self.cfg,
                    grid_label=label,side=self.gate.side,
                    pool_version=self.versions[label],source_receipt=source_identity,
                    wall=lambda label=label:self.ledger.check(
                        "accepted-cache."+label+".selected-export"),
                    capture=capture)
                payload["selected_current168_geometry"][label]=exported
                selected_bindings[label]={
                    "status":"complete","binding_sha256":exported["binding_sha256"],
                    "ordinary_bound_sha256":ordinary_bound["binding_sha256"],
                    "source_identity_sha256":digest(source_identity),
                    "pool":copy.deepcopy(pool_bindings[label])}
                self.accepted_cache_export_status["grid_status"][label]="complete"
            except Exception as error:
                failure={"grid":label,"stage":"selected-current168-export",
                         "type":type(error).__name__,"message":str(error)}
                payload["selected_export_errors"].append(failure)
                partial=self._selected_partial_record(label,source_identity,capture)
                payload["selected_export_partial"][label]=partial
                selected_bindings[label]={
                    "status":"partial","partial_capture_sha256":digest(partial),
                    "ordinary_bound_sha256":ordinary_bindings.get(label),
                    "source_identity_sha256":digest(source_identity),
                    "pool":copy.deepcopy(pool_bindings[label]),
                    "complete_selected_cache_reusable":False}
                self.accepted_cache_export_status["grid_status"][label]="partial"
                self.accepted_cache_export_status["errors"].append(copy.deepcopy(failure))
        # These are the original already paid full-grid U/T/first-jet arrays.
        # Preserve them even if a selected export or its post-call clock failed.
        bindings={}
        try:
            payload["accepted_independent168"]=array_record(q)
        except Exception as error:
            payload["first_jet_serialization_errors"].append({
                "array":"accepted_independent168","type":type(error).__name__,
                "message":str(error)})
        for label in ("coarse","fine"):
            data=self.accepted_data[label]["data"]
            arrays={"U":data["Xs"],"T":data["T"],
                    "e":np.asarray(data["e"]).reshape(-1),
                    "f":np.asarray(data["f"]).reshape(-1),
                    "radial":data["radial"],"theta":data["theta"]}
            payload["grids"][label]={}
            bindings[label]={}
            for name,value in arrays.items():
                try:
                    row=array_record(value)
                    payload["grids"][label][name]=row
                    bindings[label][name]=row["array_sha256"]
                except Exception as error:
                    payload["first_jet_serialization_errors"].append({
                        "grid":label,"array":name,
                        "type":type(error).__name__,"message":str(error)})
        selected_complete=(
            set(payload["selected_current168_geometry"])=={"coarse","fine"}
            and not payload["selected_export_errors"])
        first_complete=(
            payload["accepted_independent168"] is not None
            and not payload["first_jet_serialization_errors"]
            and all(set(payload["grids"].get(label,{}))==
                    {"U","T","e","f","radial","theta"}
                    for label in ("coarse","fine")))
        payload.update(
            status="complete" if selected_complete and first_complete else "partial",
            first_jet_cache_complete=first_complete,
            selected_export_complete=selected_complete,
            selected_export_is_after_all_trial_learning=True,
            export_seconds_before_binding=float(self.ledger.elapsed()-started))
        binding={
            "schema":POLICY+"-accepted-first-jet-binding","accepted_index":59,
            "physical_state_sha256":self.selected_point["physical_state_sha256"],
            "independent168_array_sha256":array_digest(q),
            "coordinate_definition_sha256":self.field.coordinate_definition_sha256,
            "field_evaluation_sha256":self.field.definition_sha256,
            "objective_evaluation_sha256":self.evaluation_sha256,
            "original_cfg_sha256":digest(self.cfg),"grid_array_sha256":bindings,
            "after_learning_pools":pool_bindings,
            "selected_current168_geometry":selected_bindings,
            "first_jet_cache_complete":first_complete,
            "selected_export_complete":selected_complete,
            "cache_status":payload["status"]}
        payload["binding"]=binding
        payload["binding_sha256"]=digest(binding)
        self.accepted_cache_export_status.update(
            status=payload["status"],first_jet_cache_complete=first_complete,
            selected_export_complete=selected_complete,
            binding_sha256=payload["binding_sha256"],
            completed_scientific_seconds=self.ledger.elapsed(),
            export_seconds_before_return=float(self.ledger.elapsed()-started),
            first_jet_serialization_errors=copy.deepcopy(
                payload["first_jet_serialization_errors"]))
        return payload
    def report(self):
        return {"schema":POLICY+"-actual-stage","trials":copy.deepcopy(self.trials),
            "source_accepted_index":58,"new_acceptances":int(self.accepted_state is not None),
            "selected_two_grid_physical_point":copy.deepcopy(self.selected_point),
            "ordinary_value_events":copy.deepcopy(self.value_events),
            "source58_provenance":copy.deepcopy(SOURCE_PROVENANCE),
            "accepted_cache_export":copy.deepcopy(self.accepted_cache_export_status),
            "coarse_pool":self.pools["coarse"].tolist(),"fine_pool":self.pools["fine"].tolist(),
            "coarse_pool_version":self.versions["coarse"],"fine_pool_version":self.versions["fine"],
            "new_pool_histories":copy.deepcopy(self.pool_histories),
            "source_pool_history_sha256":copy.deepcopy(self.source_pool_history_sha256),
            "original_pool_history_preserved_by_pinned_source_reference":True,
            "new_row_or_capacity_stop":self.stopped_for_new_rows,
            "independent_initial_or_final_ordinary_calls":0,
            "old159_bank_gamma_and_controller_kept_only_as_source_provenance":True,
            "all_original_actual_gates_and_exact172_box_retained":True}

