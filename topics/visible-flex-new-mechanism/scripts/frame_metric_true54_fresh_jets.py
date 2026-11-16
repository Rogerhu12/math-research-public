#!/usr/bin/env python3
"""Protocol adapter over the single genuinely new54 first-order model."""
from __future__ import annotations
import copy
import numpy as np
from frame_entry_body_subspace import array_digest
from frame_metric_true54_fresh_scope import POLICY,require

class Fresh54ExchangeJets:
    def __init__(self,model):
        self.model=model
        self.model_binding_sha256=model.binding_sha256
        self.binding=model.binding
        self.binding_sha256=model.binding_sha256
        self.state=model.state
        self.phi0=model.phi0
        self.last_scan=None
        self.gradients={}
    def scan(self,direction,*,phase):
        raw=self.model._direction(direction,phase)
        out=dict(raw)
        out["binding_sha256"]=self.binding_sha256
        out["branches"]=[]
        for branch in raw["branches"]:
            row=copy.deepcopy(branch)
            row["flat_row_id"]=row["original_row"]["flat_row_id"]
            out["branches"].append(row)
        self.last_scan=out
        return out
    def attainer_gradient(self,label,flat,*,scan):
        matches=[r for r in scan["branches"]
                 if r["grid"]==label and r["flat_row_id"]==flat]
        require(len(matches)==1,"one newly attained original metric row required")
        item=matches[0]
        self.model.metric_row(item,scan)
        row=self.model._metric_rows[(label,flat)]
        gradient=np.asarray(row["gradient"],dtype=np.float64)
        group,point=divmod(flat,self.model.grids[label].point_count)
        record={
            "schema":POLICY+"-fresh-attainer-gradient",
            "grid":label,"flat_row_id":flat,
            "original_row":copy.deepcopy(row["tag"]),
            "gradient159":gradient.tolist(),
            "gradient_sha256":array_digest(gradient),
            "base_phi":float(self.model.base[label]["branches"][group]["phi"][point]),
            "source":row["source"],"model_binding_sha256":self.binding_sha256,
            "original_chain_rule_comparison":copy.deepcopy(row.get("last_chain_rule_comparison")),
            "old53_gradient_not_reused":True,
            "evaluation_status":"complete"}
        self.gradients[(label,flat)]=record
        return record
    def new_gradient_records(self):
        return [copy.deepcopy(r) for r in self.gradients.values()]
    def report(self):
        return {"schema":POLICY+"-same-model-exchange-adapter",
                "model_binding_sha256":self.binding_sha256,
                "new_adapter_geometry_or_J_calls":0,
                "last_complete_scan_sha256":None if self.last_scan is None
                    else self.last_scan["direction_sha256"],
                "model_report":self.model.report()}
