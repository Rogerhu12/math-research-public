#!/usr/bin/env python3
"""Original whole-grid gates for the true55 fixed159 plus new9 family.

Import-only. This owner charges each started ordinary call to the one new
scope. It evaluates the unchanged fourteen gate definitions on current full
geometry, with an explicit exact172 coefficient-box extension. No old159
derivatives, developer suites, independent initial replay or final replay.
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
from frame_metric_true55_nine_fiber_scope import POLICY, NineFiberLedger, require

def array_record(value):
    a = np.asarray(value)
    require(a.dtype.kind in "fiu" and np.all(np.isfinite(a)), "finite original numeric array")
    return {"dtype":str(a.dtype),"shape":list(a.shape),"array_sha256":array_digest(a),
            "values":a.tolist()}

class NineFiberHeightGate:
    """The unchanged null-height gate and an additional literal new9 box."""
    def __init__(self, prepared):
        self.prepared=prepared
        self.original=prepared["gate"]
        self.field=prepared["field168"]
        self.old_state=np.asarray(prepared["initial159"],float).copy()
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
            "original159_are_fixed_to_true55":True,
            "original163_box_retained_exactly":True,
            "all172_physical_coefficients_checked_exactly":True}
        self.numerical_sha256=digest(self.definition)
    def assert_context(self,problem,state):
        q=self.field.validate_state(state)
        require(problem is self.field and q[:159].tobytes()==self.old_state.tobytes(),
                "the complete old159 state must remain the actual55 point")
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

class NineFiberActual:
    def __init__(self,prepared,completed,ledger):
        require(isinstance(ledger,NineFiberLedger),"one new600-second ledger required")
        self.prepared,self.completed,self.ledger=prepared,completed,ledger
        self.field,self.cfg=prepared["field168"],prepared["cfg"]
        self.gate=NineFiberHeightGate(prepared)
        self.source_point=copy.deepcopy(completed["point"])
        require(self.source_point["accepted_index"]==55
                and self.source_point["physical_state_sha256"]==
                "39e71805432d8e1814032200b8cb70973e95475b4ec02696233a7bb37e57746e",
                "actual55 is the sole starting accepted point")
        self.selected_point=copy.deepcopy(self.source_point)
        self.pools={label:np.asarray(prepared[label+"_pool"],dtype=np.int64).copy()
                    for label in ("coarse","fine")}
        cp=completed["checkpoint"]
        self.versions={label:int(cp[label+"_pool_version"]) for label in self.pools}
        self.source_pool_history_sha256={label:digest(cp[label+"_pool_history"]) for label in self.pools}
        self.pool_histories={label:[] for label in self.pools}
        self.trials=[]
        self.value_events=[]
        self.accepted_data=None
        self.accepted_state=None
        self.stopped_for_new_rows=False
        self.evaluation_definition={
            "schema":POLICY+"-ordinary-original-fourteen-gates",
            "new_field":self.field.evaluation_definition(),
            "source55_physical_sha256":self.source_point["physical_state_sha256"],
            "original_cfg_sha256":digest(self.cfg),
            "gate":self.gate.definition,
            "source_accepted_index":55,"new_accepted_index":56,
            "all14_original_whole_grid_predicates_retained":True,
            "exact_new172_box_is_additional":True,
            "source_configuration_160_1800_is_not_a_new_task_limit":True,
            "new_scope600_has_model2_and_actual6_values":True,
            "old159_bank_defect_gamma_and_controller_not_trained_or_applied":True}
        self.evaluation_sha256=digest(self.evaluation_definition)
    def theta(self,label):
        if label=="coarse":
            return self.prepared["theta"]
        require(label=="fine","coarse or fine grid required")
        # Exact original55 complete fine-grid binary64 values, already source-bound.
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
                    "state":q.copy(),"grid":label}
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
                "one acceptance or new rows close this fixed-direction actual stage")
        q=self.field.validate_state(state)
        require(not np.array_equal(q[159:],np.zeros(9)),"a true new nonzero trial required")
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
                    "schema":POLICY+"-accepted168-point","accepted_index":56,
                    "physical_state_sha256":record["physical_state_sha256"],
                    "coordinate_definition_sha256":self.field.coordinate_definition_sha256,
                    "independent_coordinates_binary64":q.tolist(),
                    "exact_binary64_independent168_coordinates":[str(Q.from_float(float(v))) for v in q],
                    "exact_physical172_coefficients":[str(v) for v in self.field.full_coefficients(q,exact=True)],
                    "source_old159_exact":copy.deepcopy(self.source_point["exact_binary64_independent_coordinates"]),
                    "coarse":copy.deepcopy(coarse["compact"]),"fine":copy.deepcopy(fine["compact"]),
                    "maximum_eta_on_both_grids":acceptance["maximum_eta_on_both_grids"],
                    "maximum_curvature_on_both_grids":max(
                        cache["decision"]["direct_maximum_absolute_principal_curvature"]
                        for cache in (coarse,fine)),
                    "new_metric_target_qualified_on_both_grids":acceptance["both_new_metric_targets_qualified"],
                    "objective_evaluation_sha256":self.evaluation_sha256,
                    "complete_new_field_evaluation_sha256":self.field.definition_sha256,
                    "exact_full_box":exact,"reason":"true55 new9 fiber original two-grid acceptance",
                    "main_readme_completion_claim":False}
                self.selected_point=point
                self.accepted_state=q.copy()
                self.accepted_data={"coarse":coarse,"fine":fine}
                record.update(accepted_as_next_iterate=True,accepted_index=56,
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
    def accepted_cache_payload(self):
        if self.accepted_data is None:
            return None
        grids={}
        bindings={}
        for label,cache in self.accepted_data.items():
            data=cache["data"]
            arrays={"U":data["Xs"],"T":data["T"],
                    "e":np.asarray(data["e"]).reshape(-1),"f":np.asarray(data["f"]).reshape(-1),
                    "radial":data["radial"],"theta":data["theta"]}
            grids[label]={name:array_record(value) for name,value in arrays.items()}
            bindings[label]={name:row["array_sha256"] for name,row in grids[label].items()}
        q=self.accepted_state
        binding={"schema":POLICY+"-accepted-first-jet-binding","accepted_index":56,
            "physical_state_sha256":self.selected_point["physical_state_sha256"],
            "independent168_array_sha256":array_digest(q),
            "coordinate_definition_sha256":self.field.coordinate_definition_sha256,
            "field_evaluation_sha256":self.field.definition_sha256,
            "objective_evaluation_sha256":self.evaluation_sha256,
            "original_cfg_sha256":digest(self.cfg),"grid_array_sha256":bindings}
        return {"schema":POLICY+"-accepted-first-jet-cache","kind":"accepted-point-paid-geometry",
            "available":True,"status":"complete","binding":binding,"binding_sha256":digest(binding),
            "accepted_independent168":array_record(q),"grids":grids,
            "no_extra_geometry_or_derivatives_executed":True,
            "positions_curvature_two_jets_and_new9_J_not_serialized":True}
    def report(self):
        return {"schema":POLICY+"-actual-stage","trials":copy.deepcopy(self.trials),
            "source_accepted_index":55,"new_acceptances":int(self.accepted_state is not None),
            "selected_two_grid_physical_point":copy.deepcopy(self.selected_point),
            "ordinary_value_events":copy.deepcopy(self.value_events),
            "coarse_pool":self.pools["coarse"].tolist(),"fine_pool":self.pools["fine"].tolist(),
            "coarse_pool_version":self.versions["coarse"],"fine_pool_version":self.versions["fine"],
            "new_pool_histories":copy.deepcopy(self.pool_histories),
            "source_pool_history_sha256":copy.deepcopy(self.source_pool_history_sha256),
            "original_pool_history_preserved_by_pinned_source_reference":True,
            "new_row_or_capacity_stop":self.stopped_for_new_rows,
            "independent_initial_or_final_ordinary_calls":0,
            "old159_bank_gamma_and_controller_kept_only_as_source_provenance":True,
            "all_original_actual_gates_and_exact172_box_retained":True}
