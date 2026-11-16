#!/usr/bin/env python3
"""At most64 scalar predictions on one complete168 direction; no actual geometry."""
from __future__ import annotations
import copy
from fractions import Fraction as Q
import math
import numpy as np
from frame_entry_body_subspace import array_digest
from frame_metric_affine_spectral_model import phi
from frame_metric_true56_small168_scope import POLICY, NORM_WEIGHT, require
from frame_metric_true56_small168_solver import vector_record

class Joint168Line:
    def __init__(self,prepared,model,handle,cache,ledger,*,emit=None):
        require(handle is not None and handle["qualified"] is True,
                "one complete first-order-qualified new direction is required")
        self.prepared,self.model,self.handle,self.cache,self.ledger=prepared,model,handle,cache,ledger
        self.emit=emit
        self.direction=np.asarray(handle["direction"],float).copy()
        require(self.direction.shape==(168,) and np.all(np.isfinite(self.direction))
            and cache["direction_sha256"]==array_digest(self.direction)
            and np.array_equal(np.asarray(cache["direction"],float),self.direction),
            "scalar arrays must be the same actual complete168 direction")
        self.interval=copy.deepcopy(handle["interval"]["original_numeric_tolerance_interval"])
        require(self.interval["nonempty"],"the original numerical hard-row interval is required")
        self.lower,self.upper=float(self.interval["lower"]),float(self.interval["upper"])
        require(0<=self.lower<=self.upper<=1,"one legal subinterval of the unit direction required")
        self.epsilon=float(Q(prepared["cfg"]["metric_proposal_epsilon_exact"]))
        self.h=4.*float(np.max(np.abs(np.asarray(prepared["physical_map172x168"],float)@self.direction)))
        self.target=float(cache["target"])
        require(self.target==model.target and self.epsilon==model.epsilon==cache["epsilon"]
            and cache["base_phi"]==model.phi0
            and cache["binding_sha256"]==model.input_binding_sha256,
            "same source56 baseline, complete168 input binding and original metric target/smoothing")
        self.arrays={}
        self.bindings={}
        for label in ("coarse","fine"):
            rows=cache["grids"][label]
            arrays={name:np.asarray(rows[name],float).reshape(-1) for name in ("e","f","de","df")}
            size=prepared["row_grids"][label].point_count
            require(all(a.shape==(size,) and np.all(np.isfinite(a)) for a in arrays.values()),
                    "all points of both original grids required for the scalar oracle")
            self.arrays[label]=arrays
            self.bindings[label]={name:array_digest(a) for name,a in arrays.items()}
        self.records=[]
        self.by_alpha={}
        self.event=None
        self.summary=None
    def query(self,alpha,purpose):
        alpha=float(alpha)
        require(math.isfinite(alpha) and (alpha==0 or self.lower<=alpha<=self.upper),
                "only physical zero or an original-interval scalar query is allowed")
        key=alpha.hex()
        if key in self.by_alpha:
            return self.by_alpha[key]
        event=self.ledger.begin("scalar_queries",alpha=alpha,purpose=purpose)
        row={"number":len(self.records)+1,"alpha":alpha,"alpha_exact":str(Q.from_float(alpha)),
             "purpose":purpose,"status":"started","direction_sha256":array_digest(self.direction),
             "prediction_is_not_current_nonlinear_geometry":True}
        self.records.append(row)
        try:
            maximum=self.target
            branches=[]
            for label in ("coarse","fine"):
                values=self.arrays[label]
                e=values["e"]+alpha*values["de"]
                f=values["f"]+alpha*values["df"]
                count=len(e)
                for group in (0,1):
                    observed=phi(e,f,np.full(count,group,dtype=np.int64),self.epsilon)
                    point=int(np.argmax(observed))
                    value=float(observed[point])
                    maximum=max(maximum,value)
                    branches.append({"grid":label,"group":group,"point_index":point,
                        "flat_row_id":group*count+point,"maximum_phi":value,
                        "original_row":self.prepared["row_grids"][label].coordinate(group*count+point)})
            norm_cost=NORM_WEIGHT*alpha*self.h
            row.update(status="complete",phi=maximum,norm_cost=norm_cost,
                objective=maximum+norm_cost,branches=branches,
                original_target_constant=self.target,
                complete_affine_observable_prediction=True,
                new_geometry_J_JVP_or_master_rows=0)
            self.ledger.end(event,phi=maximum,objective=row["objective"])
            self.by_alpha[key]=row
            if self.emit is not None:
                row["stdout_receipt"]=self.emit("LINE_QUERY",row)
            self.ledger.check("joint168.scalar-query.completed")
            return row
        except Exception as error:
            row.update(status="raised",error={"type":type(error).__name__,"message":str(error)})
            if event.get("status")=="started":
                self.ledger.end(event,error)
            if self.emit is not None and "stdout_receipt" not in row:
                row["stdout_receipt"]=self.emit("LINE_QUERY",row)
            raise
    def run(self):
        self.event=self.ledger.begin("scalar_sessions",direction_sha256=array_digest(self.direction))
        try:
            zero=self.query(0.,"physical-zero-baseline")
            left=self.query(self.lower,"legal-lower-endpoint")
            right=self.query(self.upper,"legal-upper-endpoint")
            a,b=self.lower,self.upper
            ratio=(math.sqrt(5.)-1.)/2.
            c=b-ratio*(b-a);d=a+ratio*(b-a)
            fc=self.query(c,"bounded-golden-search")
            fd=self.query(d,"bounded-golden-search")
            # Leave two of the64 queries for distinct actual backtrack predictions.
            while self.ledger.counts["scalar_queries"]<62:
                self.ledger.check("joint168.scalar-search")
                if b-a<=1.e-12*max(1.,abs(a),abs(b)) or c==d:
                    break
                if fc["objective"]<=fd["objective"]:
                    b,d,fd=d,c,fc
                    c=b-ratio*(b-a)
                    if c==d or c in (a,b):
                        break
                    fc=self.query(c,"bounded-golden-search")
                else:
                    a,c,fc=c,d,fd
                    d=a+ratio*(b-a)
                    if c==d or d in (a,b):
                        break
                    fd=self.query(d,"bounded-golden-search")
            eligible=[row for row in self.records if row["status"]=="complete"
                      and row["alpha"]>0 and self.lower<=row["alpha"]<=self.upper]
            best=min(eligible,key=lambda row:(row["objective"],row["alpha"])) if eligible else None
            gain=None if best is None else zero["phi"]-best["objective"]
            qualified=bool(best is not None and gain>self.model.floor)
            self.summary={"schema":POLICY+"-scalar-search",
                "status":"complete-joint168-affine-observable-scalar-observation",
                "direction168":vector_record(self.direction),"legal_interval":self.interval,
                "physical_zero":copy.deepcopy(zero),"best_query":copy.deepcopy(best),
                "qualified_predicted_descent":qualified,"best_norm_charged_predicted_gain":gain,
                "remaining_search_interval":{"lower":a,"upper":b},
                "scalar_search_query_limit":62,"shared_total_scalar_query_limit":64,
                "new_metric_array_bindings":copy.deepcopy(self.bindings),
                "one_complete_scalar_value_includes_all_four_grid_branches_and_target":True,
                "binary64_bounded_minimization_is_not_an_exact_optimality_or_actual_certificate":True,
                "ordinary_geometry_or_JVP_calls":0}
            self.ledger.end(self.event,qualified_predicted_descent=qualified,
                            scalar_queries=self.ledger.counts["scalar_queries"])
            self.ledger.check("joint168.scalar-search.completed")
            return self.summary
        except Exception as error:
            if self.event.get("status")=="started":
                self.ledger.end(self.event,error)
            raise
    def actual_candidates(self,actual,*,emit=None):
        """Only this qualified predicted direction, at most three real trials."""
        summary=self.summary
        require(summary is not None,"the scalar stage must have returned")
        trace={"schema":POLICY+"-actual-scale-selection","trials":[],
               "policy":"best positive legal alpha, then twice midpoint toward legal lower",
               "new_acceptances":0}
        if not summary["qualified_predicted_descent"]:
            trace["status"]="no-joint168-affine-observable-predicted-descent"
            return trace
        alpha=float(summary["best_query"]["alpha"])
        previous=set()
        for number in range(1,4):
            self.ledger.check("joint168.actual-scale")
            if alpha in previous or alpha<=0 or not self.lower<=alpha<=self.upper:
                trace["status"]="no-distinct-positive-legal-scale"
                break
            previous.add(alpha)
            prediction=self.query(alpha,"actual-trial-scale-"+str(number))
            gain=self.records[0]["phi"]-prediction["objective"]
            if gain<=self.model.floor:
                trace["status"]="backtrack-has-no-qualified-predicted-gain"
                break
            q=self.model.state+alpha*self.direction
            domain=self.model.validate_actual_candidate(q)
            trial={"number":number,"alpha":alpha,"candidate_domain":domain,
                   "scalar_prediction":copy.deepcopy(prediction)}
            trace["trials"].append(trial)
            if not domain["eligible"]:
                trial["status"]="rounded-new168-domain-rejected-before-ordinary"
                trace["status"]=trial["status"]
                break
            result=actual.trial(q,alpha,prediction,emit=emit)
            trial["actual_trial_receipt"]=copy.deepcopy(result.get("stdout_receipt"))
            trial["status"]=result["status"]
            trial["accepted_as_next_iterate"]=result["accepted_as_next_iterate"]
            if result["accepted_as_next_iterate"]:
                trace.update(status="new-actual57-accepted",new_acceptances=1)
                break
            if result["new_row_or_capacity_stop"]:
                trace["status"]="failed-actual-new-row-or-capacity-closes-this-direction"
                break
            alpha=(alpha+self.lower)/2.
        else:
            trace["status"]="three-new-actual-scales-completed-without-acceptance"
        trace.setdefault("status","no-new-actual-acceptance")
        return trace
    def report(self):
        return {"summary":copy.deepcopy(self.summary),"all_queries":copy.deepcopy(self.records),
                "interval":copy.deepcopy(self.interval),"direction168":vector_record(self.direction),
                "shared_scalar_queries":self.ledger.counts["scalar_queries"],
                "no_actual_geometry_is_implied_by_scalar_values":True}
