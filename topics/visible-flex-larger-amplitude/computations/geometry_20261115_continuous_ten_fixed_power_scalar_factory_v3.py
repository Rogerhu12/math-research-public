#!/usr/bin/env python3
"""Independent accurate R323 continuous ten-control fixed-power constructor.

This creates a NEW target family from an actual exact shared-jet core and a
bound v3 convention-C complete-point two-jet enclosure.  It does not relabel the old finite
Gauss/mask scalar, an old field, or a numerical BVP solution.  Exact real
coefficients keep E0/E1/E2 as semantic leaves; interval endpoints or midpoints
are never installed as the target coefficients.

All mathematical arithmetic is public repository Actions only.  Raw outputs
are request-owned temporary recomputable data.  No native/scientific
acceptance gate is added, no field is created, and no API is called.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as Q
import gzip
import hashlib
import importlib.util
import json
from math import isfinite, isqrt
import os
from pathlib import Path
import sys
import time

REPOSITORY = "Rogerhu12/math-research-public"
HERE = Path(__file__).resolve().parent
SCHEMA = "R300-continuous-ten-fixed-support1-power4-v3-cut-exact-expression-construction-v1"
RECIPE_SCHEMA = "R300-new-continuous-ten-fixed-support1-power4-model-recipe-v1"
NINE_RECIPE_SCHEMA = "R300-new-continuous-nine-scalar-model-recipe-v1"
MODEL_SCHEMA = "R300-new-continuous-ten-fixed-support1-power4-target-family-v3-cut-v1"
BASELINE_FACTORY_NAME = "geometry_20261115_continuous_nine_scalar_factory_v3.py"
BASELINE_FACTORY_SHA = "0d89370df95c6063cb336182d87137705d5e4ddb87625a3fb1b58b35695a621e"
CORE_SOURCE = "geometry_20261114_full_prefix_operator.py"
CORE_SOURCE_SHA = "a9a25d96eeb286d9f2214f997c992e50e42f6e6ec2bc59c136a183febe2a0703"
E_SOURCE = "geometry_20261115_stored_continuous_E_cover_v3.py"
E_SOURCE_SHA = "f12f747041783dbb54b16ac2bdb0c3aeeade93e6bc7f276bde9dd81f424df7df"
E_BASE_SHA = "9aa0da45027afa37ca329eab73e5e93e788f2bbafb908b9e8c2960f537a427ed"
E_SCHEMA = "R286-original-stored-convention-C-continuous-E-cover-v3"
E_V2_SHA = "004010b681aa35635e15b229a3e5b78602b3ec480a631a761e42f6c7d563b6ea"
E_MODEL_SCHEMA = "R286-original-stored-continuous-model-convention-C-v1"
CUT_READER_NAME = "geometry_20261115_stored_C_v3_cut_twojet_readout.py"
CUT_READER_SHA = "1c39b242224824b361cbe5d28ea838b7e4824f5506a05302c662f045f735aeed"
CUT_READER_SCHEMA = "R286-v3-original-binary-cut-complete-twojet-hull-v1"
CUT_QUERY_ID = "original-binary-config-cut-point"
PRESERVED_EXPRESSION_CHECKPOINT_SHA = "650a03101c33313aad00b4e84e98d47735f2878065c73e44653992093b985147"
R300_PROOF_NAME = "R300-continuous-nine-control-scalar-family-and-cut-calibration.md"
R300_PROOF_SHA = "5df99d5de2296fe830b8a51e76f27ea41cce217dd343a9803f7f1a830fec3147"
NINE_PARAMETERS = ["p1", "p2", "p3", "theta1", "theta2", "theta3", "eta1", "eta2", "eta3"]
PARAMETERS = NINE_PARAMETERS+["xi"]
CONTROL_TERMS = json.loads(r'''[{"parameter_index":0,"support_index":0,"power":0},{"parameter_index":1,"support_index":1,"power":0},{"parameter_index":2,"support_index":2,"power":0},{"parameter_index":3,"support_index":0,"power":1},{"parameter_index":4,"support_index":1,"power":1},{"parameter_index":5,"support_index":2,"power":1},{"parameter_index":6,"support_index":0,"power":2},{"parameter_index":7,"support_index":1,"power":2},{"parameter_index":8,"support_index":2,"power":2},{"parameter_index":9,"support_index":1,"power":4}]''')
ROOT_CHOICES = ("R286-dovetailed-rational-middle-third",
                "uniform-original-admissible-root-family")


def require_actions():
    if (os.environ.get("GITHUB_ACTIONS") != "true"
            or os.environ.get("GITHUB_REPOSITORY") != REPOSITORY):
        raise RuntimeError("All mathematical evaluation is restricted to this public repository's Actions")


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def canonical(value):
    return (json.dumps(value, sort_keys=True, separators=(",", ":"),
        ensure_ascii=False, allow_nan=False)+"\n").encode()


def read_json(path, expected=None):
    path = Path(path)
    raw = path.read_bytes()
    if expected is not None and sha(raw) != expected:
        raise ValueError("Actual input SHA differs: "+str(path))
    decoded = gzip.decompress(raw) if raw.startswith(b"\x1f\x8b") else raw
    value = json.loads(decoded)
    return value, dict(file=str(path), bytes=len(raw), sha256=sha(raw),
        decoded_bytes=len(decoded), decoded_sha256=sha(decoded))


def member(root, descriptor):
    root = Path(root).resolve()
    name = descriptor["file"]
    candidate = Path(name)
    if candidate.is_absolute() or ".." in candidate.parts:
        raise ValueError("A result member is not a safe relative path")
    path = (root/candidate).resolve()
    if not path.is_relative_to(root):
        raise ValueError("A result member escaped its original directory")
    raw = path.read_bytes()
    if len(raw) != descriptor["bytes"] or sha(raw) != descriptor["sha256"]:
        raise ValueError("A complete actual result member differs: "+name)
    return raw


def parsed_member(root, descriptor):
    raw = member(root, descriptor)
    return json.loads(gzip.decompress(raw) if raw.startswith(b"\x1f\x8b") else raw)


def rational(value):
    if isinstance(value, bool):
        raise ValueError("A boolean is not a mathematical scalar")
    if isinstance(value, Q):
        return value
    if isinstance(value, int):
        return Q(value)
    if isinstance(value, float):
        if not isfinite(value):
            raise ValueError("Nonfinite original input")
        return Q.from_float(value)
    if isinstance(value, str):
        return Q(value)
    raise TypeError("Use exact rational strings or actual finite original numbers")


def dyadic(record):
    return Q(int(record["mantissa"]))*Q(2)**int(record["binary_exponent"])


class Box:
    """Closed exact rational interval; no floating midpoint substitutes."""
    def __init__(self, lo, hi=None):
        self.lo, self.hi = rational(lo), rational(lo if hi is None else hi)
        if self.lo > self.hi:
            raise ValueError("Reversed closed interval")

    @staticmethod
    def lift(value):
        return value if isinstance(value, Box) else Box(value)

    def __add__(self, value):
        value = Box.lift(value)
        return Box(self.lo+value.lo, self.hi+value.hi)

    __radd__ = __add__

    def __neg__(self):
        return Box(-self.hi, -self.lo)

    def __sub__(self, value):
        return self+-Box.lift(value)

    def __rsub__(self, value):
        return Box.lift(value)+-self

    def __mul__(self, value):
        value = Box.lift(value)
        endpoints = [a*b for a in (self.lo,self.hi) for b in (value.lo,value.hi)]
        return Box(min(endpoints),max(endpoints))

    __rmul__ = __mul__

    def __truediv__(self, value):
        value = Box.lift(value)
        if value.lo <= 0 <= value.hi:
            raise ArithmeticError("The exact denominator enclosure contains zero")
        return self*Box(1/value.hi,1/value.lo)

    def __pow__(self, n):
        if not isinstance(n,int) or n < 0:
            raise ValueError("Use a nonnegative integer interval power")
        out = Box(1)
        for _ in range(n):
            out = out*self
        return out

    def hull(self, value):
        value = Box.lift(value)
        return Box(min(self.lo,value.lo),max(self.hi,value.hi))

    def absolute_upper(self):
        return max(abs(self.lo),abs(self.hi))

    def sqrt(self, bits):
        if self.lo < 0:
            raise ArithmeticError("Square root input is not nonnegative")
        scale = 1 << bits

        def lower(q):
            k = isqrt((q.numerator << (2*bits))//q.denominator)
            return Q(k,scale)

        lo, hi_floor = lower(self.lo), lower(self.hi)
        hi = hi_floor if hi_floor*hi_floor == self.hi else hi_floor+Q(1,scale)
        return Box(lo,hi)

    def record(self):
        return dict(lower=str(self.lo),upper=str(self.hi))


def ball_record(value):
    return Box(dyadic(value["lower"]),dyadic(value["upper"]))


def pointer(value, path):
    if not path:
        return value
    if not path.startswith("/"):
        raise ValueError("Use an explicit RFC6901 pointer")
    for part in path[1:].split("/"):
        part = part.replace("~1","/").replace("~0","~")
        value = value[int(part)] if isinstance(value,list) else value[part]
    return value


def load_core_kernel(directory):
    path = Path(directory)/CORE_SOURCE
    raw = path.read_bytes()
    if sha(raw) != CORE_SOURCE_SHA:
        raise ValueError("The original exact shared-node constructor source differs")
    spec = importlib.util.spec_from_file_location("_r300_original_core",path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module, dict(file=CORE_SOURCE,bytes=len(raw),sha256=sha(raw))


def cut_jet_from_actual_cover(root, expected_result_sha, directory, cut,
                              cut_readout_file, cut_readout_sha):
    """Consume the actual v3 result and its independently bound full-point hull.

    No old v2 source/result is relabelled. The original complete point-query
    leaf stream was hashed and every point leaf was hulled by the fixed
    readout producer. This consumer binds that actual readout and the original
    small cover files; it does not repeat the large leaf stream arithmetic.
    E0/E1/E2 remain semantic C leaves, not independent literal midpoint data.
    """
    result, result_receipt = read_json(Path(root)/"result.json",expected_result_sha)
    for name,expected in ((E_SOURCE,E_SOURCE_SHA),(CUT_READER_NAME,CUT_READER_SHA)):
        if sha((Path(directory)/name).read_bytes()) != expected:
            raise ValueError("The actual v3 cover/readout source differs: "+name)
    if (result.get("schema") != E_SCHEMA
            or result.get("source_sha256") != E_SOURCE_SHA
            or result.get("target_model_schema") != E_MODEL_SCHEMA
            or result.get("preserved_original_producer_source",{}).get("sha256") != E_BASE_SHA
            or result.get("preserved_unit_panel_producer_source",{}).get("sha256") != E_V2_SHA):
        raise ValueError("Use the actual frozen v3 result and its unchanged source ancestry")
    binding = parsed_member(root,result["input_binding"])
    queries = parsed_member(root,result["query_results"])
    plan = parsed_member(root,result["query_plan"])
    if (queries.get("schema") != E_SCHEMA+"-queries"
            or plan.get("schema") != "R286-original-stored-convention-C-closed-queries-v1"):
        raise ValueError("Actual complete v3 continuous query schemas differ")
    if (binding.get("schema") != E_SCHEMA+"-input-binding"
            or binding.get("source_sha256") != E_SOURCE_SHA
            or binding.get("preserved_original_producer_source",{}).get("sha256") != E_BASE_SHA
            or binding.get("preserved_unit_panel_producer_source",{}).get("sha256") != E_V2_SHA
            or binding.get("convention",{}).get("schema") != E_MODEL_SCHEMA
            or binding.get("convention",{}).get("deep_definition") != "original-exact-root-family"):
        raise ValueError("The actual original continuous target binding differs")
    required = ("full_finite_head_complete",
        "declared_continuous_model_family_conditions_proved",
        "all_admissible_original_root_choices_uniformly_enclosed",
        "original_real_profile_and_model_C_unchanged",
        "model_choice_is_explicit_and_not_original_finite_output_relabel")
    if any(result.get(key) is not True for key in required):
        raise ArithmeticError("The complete actual continuous tail premises remain unpaid")
    if result.get("global_warp_alpha_or_original_cut_renormalised") is not False:
        raise ValueError("Do not replace the original natural domain or frozen warp")
    p = binding["physical_parameters"]
    if cut != rational(p["rCut"]):
        raise ValueError("The current mode preserves the original declared cut exactly")
    cuff = rational(p["rCuff"])
    outer = ball_record(result["natural_outer_radius"])
    if not cuff < cut <= outer.lo:
        raise ArithmeticError("Actual cut containment in the natural domain is unpaid; no extension")
    readout, readout_receipt = read_json(cut_readout_file,cut_readout_sha)
    if (readout.get("schema") != CUT_READER_SCHEMA
            or readout.get("source_sha256") != CUT_READER_SHA
            or readout.get("target_model_schema") != E_MODEL_SCHEMA
            or readout.get("continuous_model_choice_is_explicit") is not True
            or readout.get("actual_producer",{}).get("file") != E_SOURCE
            or readout.get("actual_producer",{}).get("sha256") != E_SOURCE_SHA
            or readout.get("actual_producer",{}).get("schema") != E_SCHEMA):
        raise ValueError("Use the independently bound actual v3 complete-point readout")
    if (readout.get("run_id") != result.get("run_id")
            or readout.get("source_commit") != result.get("source_commit")):
        raise ValueError("The cut readout and original cover came from different runs")
    for key in ("bytes","sha256"):
        if readout["actual_source_result"][key] != result_receipt[key]:
            raise ValueError("The cut readout does not bind this actual result")
        if readout["actual_original_config"][key] != binding["config"][key]:
            raise ValueError("The cut readout does not bind this original config")
        if readout["actual_original_query_recipe"][key] != binding["query_input"][key]:
            raise ValueError("The cut readout does not bind this original query recipe")
    for key,original in (("actual_input_binding",result["input_binding"]),
                         ("actual_query_results",result["query_results"]),
                         ("complete_original_query_leaf_stream",result["ledgers"]["query_inverse_cover"])):
        supplied=readout[key]
        fields=("file","bytes","sha256","rows") if "rows" in original else ("file","bytes","sha256")
        if any(supplied[name] != original[name] for name in fields):
            raise ValueError("The cut readout changed a complete original member: "+key)
    if (readout.get("point_twojet_enclosure_complete") is not True
            or readout.get("all_point_leaf_rows_retained_in_hull") is not True
            or readout.get("original_point_domain_certificate_exact_bounds_cross_checked") is not True):
        raise ArithmeticError("The actual complete cut two-jet scope remains unpaid")
    chosen=readout["actual_point_query"]
    candidates=[row for row in queries["results"] if row["query"]["id"]==CUT_QUERY_ID]
    if len(candidates)!=1 or chosen!=candidates[0]:
        raise ValueError("The original point query was not retained verbatim")
    q=chosen["query"]
    if (q["id"]!=CUT_QUERY_ID or q["index"]!=0
            or q["kind"]!="closed-rational-radius-interval"
            or q["left_closed"] is not True or q["right_closed"] is not True
            or rational(q["left"])!=cut or rational(q["right"])!=cut):
        raise ValueError("The actual point query changed the original binary cut")
    if any(chosen.get(key) is not True for key in
           ("complete_closed_domain_bound","domain_containment_proved",
            "continuous_model_family_conditions_proved")):
        raise ArithmeticError("The original point-domain premises remain unpaid")
    actual_plan=next((row for row in plan["queries"] if row["id"]==CUT_QUERY_ID),None)
    if actual_plan!=q:
        raise ValueError("The original complete query plan and its point result differ")
    span=chosen["leaf_ledger_rows"]
    if (type(span["first"]) is not int or type(span["stop"]) is not int
            or not 0<=span["first"]<span["stop"]<=result["ledgers"]["query_inverse_cover"]["rows"]
            or readout["selected_leaf_span"]!=span
            or readout["selected_original_leaf_count"]!=span["stop"]-span["first"]):
        raise ValueError("The complete point-leaf span changed")
    if (rational(readout["original_binary_cut"]["exact_rational"])!=cut
            or readout["original_binary_cut"]["query_value_not_renormalised"] is not True
            or readout["original_natural_outer_radius"]!=result["natural_outer_radius"]
            or readout["original_natural_outer_radius_minus_nominal_binary_cut"]!=
                result["natural_outer_radius_minus_nominal_binary_cut"]):
        raise ValueError("The original cut or natural outer radius was reinterpreted")
    enclosed=readout["same_point_E_Er_Err_enclosures"]
    if not isinstance(enclosed,dict) or set(enclosed)!={"E","E_r","E_rr"}:
        raise ValueError("Retain all three original actual point enclosures")
    hulls=[ball_record(enclosed[key]) for key in ("E","E_r","E_rr")]
    for key,box in zip(("E","E_r","E_rr"),hulls):
        if dyadic(enclosed[key]["exact_full_width"]) != box.hi-box.lo:
            raise ValueError("An actual exact full-width record differs: "+key)
    original_E=ball_record(chosen["E"])
    if not original_E.lo<=hulls[0].lo<=hulls[0].hi<=original_E.hi:
        raise ValueError("The inherited complete-point hull escaped the original E enclosure")
    if hulls[0].lo <= 1:
        raise ArithmeticError("The inherited cut enclosure has not proved E0>1")
    identity = dict(actual_result=result_receipt,
        source_sha256=E_SOURCE_SHA,preserved_original_source_sha256=E_BASE_SHA,
        preserved_unit_panel_source_sha256=E_V2_SHA,
        input_binding=result["input_binding"],actual_input_binding=binding,
        original_query_plan=result["query_plan"],original_query_results=result["query_results"],
        original_complete_leaf_ledger=result["ledgers"]["query_inverse_cover"],
        actual_complete_cut_twojet_readout=readout_receipt,
        actual_cut_twojet_readout_source_sha256=CUT_READER_SHA,
        actual_cut_twojet_readout_schema=CUT_READER_SCHEMA,
        original_readout_run_id=readout["run_id"],
        original_readout_source_commit=readout["source_commit"],
        original_binary_cut=readout["original_binary_cut"],
        selected_complete_query=q,selected_complete_span=span,
        selected_complete_point_leaf_count=readout["selected_original_leaf_count"],
        selected_complete_point_leaf_kind_counts=readout["selected_leaf_kind_counts"],
        selected_original_work_resolution_unmet_count=
            readout["selected_original_work_resolution_unmet_count"],
        original_point_work_resolution_complete=chosen["work_resolution_complete"],
        original_all_query_domain_bounds_complete=result["all_requested_closed_query_bounds_complete"],
        original_all_query_work_resolution_complete=result["numerical_work_resolution_complete"],
        original_unvisited_query_suffix=result["unvisited_query_suffix"],
        original_error=result["error"],cut_radius=str(cut),cuff_radius=str(cuff),
        natural_outer_radius=result["natural_outer_radius"],
        actual_cut_twojet_enclosures=enclosed,
        semantic_leaves=["E(R)","dE/dr(R)","d2E/dr2(R)"],
        coefficient_midpoints_substituted=False,
        one_finite_cover_used_as_arbitrarily_refinable_name=False,
        arbitrarily_refinable_cut_oracle_supplied=False,
        effective_window_selection_or_termination_claimed=False,
        exact_root_values_computed=False,
        original_producer_encloses_every_admissible_root_sequence=True,
        complete_original_leaf_arithmetic_repeated_by_this_factory=False,
        complete_original_leaf_payload_not_required_again=True,
        v2_result_or_factory_identity_relabelled=False)
    return dict(zip(("E0","E1","E2"),hulls)),identity


class Expression:
    def __init__(self,tree,index):
        self.tree,self.index=tree,index

    def _value(self,value):
        if isinstance(value,Expression):
            if value.tree is not self.tree:
                raise ValueError("Expressions belong to distinct model identities")
            return value
        return self.tree.constant(value)

    def __add__(self,value):
        return self.tree.operation("add",self,self._value(value))

    __radd__=__add__

    def __neg__(self):
        return self.tree.operation("neg",self)

    def __sub__(self,value):
        return self+-self._value(value)

    def __rsub__(self,value):
        return self._value(value)+-self

    def __mul__(self,value):
        return self.tree.operation("mul",self,self._value(value))

    __rmul__=__mul__

    def __truediv__(self,value):
        return self.tree.operation("div",self,self._value(value))

    def __rtruediv__(self,value):
        return self._value(value)/self

    def __pow__(self,n):
        if not isinstance(n,int) or n < 0:
            raise ValueError("Use a nonnegative exact power")
        out=self.tree.constant(1)
        for _ in range(n):
            out=out*self
        return out

    def sqrt(self):
        return self.tree.operation("sqrt",self)


class Tree:
    def __init__(self):
        self.nodes=[];self.constants={}

    def constant(self,value):
        key=str(rational(value))
        if key not in self.constants:
            self.constants[key]=len(self.nodes)
            self.nodes.append(dict(op="rational",value=key))
        return Expression(self,self.constants[key])

    def leaf(self,name):
        index=len(self.nodes);self.nodes.append(dict(op="semantic-cut-leaf",name=name))
        return Expression(self,index)

    def operation(self,kind,*args):
        index=len(self.nodes)
        self.nodes.append(dict(op=kind,args=[x.index for x in args]))
        return Expression(self,index)

    def evaluate(self,leaves,bits):
        values=[]
        for node in self.nodes:
            kind=node["op"]
            if kind=="rational":
                value=Box(node["value"])
            elif kind=="semantic-cut-leaf":
                value=leaves[node["name"]]
            else:
                args=[values[i] for i in node["args"]]
                if kind=="add": value=args[0]+args[1]
                elif kind=="mul": value=args[0]*args[1]
                elif kind=="div": value=args[0]/args[1]
                elif kind=="neg": value=-args[0]
                elif kind=="sqrt": value=args[0].sqrt(bits)
                else: raise AssertionError("Unknown exact expression operation")
            values.append(value)
        return values


def polynomial_value(coefficients,x):
    out=x*0
    for c in reversed(coefficients):
        out=out*x+c
    return out


def differentiated(coefficients,order):
    values=list(coefficients)
    for _ in range(order):
        values=[j*values[j] for j in range(1,len(values))]
        if not values:
            values=[0]
    return values


def core_pieces(kernel,geometry,end):
    x,coefficients=kernel.prefix_coefficients(geometry)
    if not 0 < end <= x[-1] or x[0] < 0:
        raise ValueError("The actual core endpoint is outside its exact original domain")
    law=geometry["initial_law"]
    length,velocity,k0=(rational(float(law[key])) for key in ("length","velocity","k0"))
    if length <= 0:
        raise ValueError("The original core law length is not positive")
    rows=[]
    first=min(x[0],end)
    if first > 0:
        polynomial=[Q(1),Q(0),k0/2,
            (3*velocity-2*k0*length)/(3*length**2),
            (k0*length-2*velocity)/(4*length**3)]
        stop=min(first,length)
        if stop > 0:
            rows.append(dict(left=Q(0),right=stop,anchor=Q(0),width=Q(1),coefficients=polynomial))
        if first > length:
            rows.append(dict(left=length,right=first,anchor=Q(0),width=Q(1),
                coefficients=[1-length*velocity/2+k0*length**2/12,velocity]))
    for j,row in enumerate(coefficients):
        lo,hi=x[j],min(x[j+1],end)
        if hi > lo:
            rows.append(dict(left=lo,right=hi,anchor=x[j],width=x[j+1]-x[j],coefficients=row))
    if not rows or rows[0]["left"]!=0 or rows[-1]["right"]!=end:
        raise ValueError("The complete core partition was not retained")

    def jets(row,s):
        t=(s-row["anchor"])/row["width"]
        return [polynomial_value(differentiated(row["coefficients"],k),t)/row["width"]**k
                for k in range(3)]

    for left,right in zip(rows[:-1],rows[1:]):
        if left["right"]!=right["left"] or jets(left,left["right"])!=jets(right,right["left"]):
            raise ValueError("This actual exact shared core is not C2 at every retained seam")
    if jets(rows[0],0)[1] != 0:
        raise ValueError("The original accurate core has nonzero central derivative")
    return rows,jets(rows[-1],end)


def recipe_from_actual_nine(nine_recipe_raw,expected_sha256,*,xi,parameter_origin):
    """Extend the actual accurate nine recipe; choose no coefficient or width here.

    xi is an explicit exact-rational/finite input, never an implicit zero.
    The actual180 selected recipe is a permissible source, not an old BVP
    result or a fabricated ten-domain certificate. The accurate xi=0
    restriction is the original accurate nine function, not its IEEE words.
    """
    require_actions()
    if not isinstance(nine_recipe_raw,bytes) or sha(nine_recipe_raw)!=expected_sha256:
        raise ValueError("Bind the complete actual accurate nine recipe bytes")
    old=json.loads(nine_recipe_raw)
    if (old.get("schema")!=NINE_RECIPE_SCHEMA
            or old.get("parameter_order")!=NINE_PARAMETERS
            or not isinstance(old.get("nine_parameters"),list)
            or len(old["nine_parameters"])!=9
            or not isinstance(parameter_origin,dict) or not parameter_origin):
        raise ValueError("An actual independently identified accurate nine recipe is required")
    exact=[rational(value) for value in old["nine_parameters"]]
    extra=rational(xi)
    new=dict(old)
    new.pop("nine_parameters")
    new.update(schema=RECIPE_SCHEMA,parameter_order=list(PARAMETERS),
        ten_parameters=[str(value) for value in exact]+[str(extra)],
        control_terms=[dict(term) for term in CONTROL_TERMS],
        independent_tenth_coefficient_origin=parameter_origin,
        original_accurate_nine_recipe=dict(bytes=len(nine_recipe_raw),sha256=sha(nine_recipe_raw),
            schema=NINE_RECIPE_SCHEMA,source_text_baseline=BASELINE_FACTORY_NAME,
            source_text_baseline_sha256=BASELINE_FACTORY_SHA),
        zero_xi_is_original_accurate_nine_restriction=(extra==0),
        old_nine_domain_result_not_relabelled_ten=True,
        new_native_J_metric_or_accepted_field_not_supplied=True)
    return new


def build_expression(kernel,geometry,recipe,cut_boxes,cut):
    if (recipe.get("schema")!=RECIPE_SCHEMA or recipe.get("parameter_order")!=PARAMETERS
            or recipe.get("control_terms")!=CONTROL_TERMS
            or recipe.get("collar_mode")!="cut-cubic-jet-collar"
            or recipe.get("root_choice") not in ROOT_CHOICES):
        raise ValueError("Use the independent R300 model recipe with explicit target choice")
    parameters=list(map(rational,recipe["ten_parameters"]))
    if len(parameters)!=10:
        raise ValueError("Retain all ten accurate coefficients and the declared fixed support1/power4 term")
    end=rational(recipe["core_end"])
    original,jet=core_pieces(kernel,geometry,end)
    radiusA,speedA,accA=jet
    kappa,d,da,db=map(rational,(recipe["kappa"],recipe["collar_width"],
        recipe["first_transition_width"],recipe["last_transition_width"]))
    if not 0 < kappa < 1 or min(d,da,db)<=0:
        raise ValueError("The explicit new model lengths/speed are inadmissible")
    first_left,first_width=map(rational,(recipe["first_support"]["left"],
        recipe["first_support"]["stored_width"]))
    if not 0 < first_left < first_left+first_width < end:
        raise ValueError("Keep the first true support strictly inside the accurate core")
    tree=Tree()
    E0,E1,E2=(tree.leaf(key) for key in ("E0","E1","E2"))
    root=E0.sqrt()
    v=-1/root
    b=-E1/(2*E0**2)
    q=E2/(2*E0**2*root)-E1**2/(E0**3*root)
    RA,VA,BA=map(tree.constant,jet)
    R=tree.constant(cut)
    RB=R-v*d+b*d*d/2-q*d**3/6
    VB=v-b*d+q*d*d/2
    BB=b-q*d
    IA=da*(VA-kappa)/2+da*da*BA/12
    IB=db*(-kappa+VB)/2-db*db*BB/12
    LC=(RA-RB+IA+IB)/kappa
    S1=tree.constant(end+da)
    S2=S1+LC
    S3=S2+db
    length=S3+d
    pieces=[]

    def append(name,anchor,width,coefficients,lo=Q(0),hi=Q(1)):
        pieces.append(dict(name=name,anchor=anchor.index,width=width.index,
            coefficients=[tree.constant(x).index if not isinstance(x,Expression) else x.index
                          for x in coefficients],
            local_interval=[str(lo),str(hi)]))

    for j,row in enumerate(original):
        append("core-"+str(j),tree.constant(row["anchor"]),tree.constant(row["width"]),
            row["coefficients"],(row["left"]-row["anchor"])/row["width"],
            (row["right"]-row["anchor"])/row["width"])
    velocityA=[VA,da*BA,-3*VA-3*kappa-2*da*BA,2*VA+2*kappa+da*BA]
    append("first-velocity-transition",tree.constant(end),tree.constant(da),
        [RA]+[da*x/(j+1) for j,x in enumerate(velocityA)])
    append("negative-speed-coast",S1,LC,[RA+IA,-kappa*LC])
    velocityB=[tree.constant(-kappa),tree.constant(0),
        3*kappa+3*VB-db*BB,-2*kappa-2*VB+db*BB]
    append("last-velocity-transition",S2,tree.constant(db),
        [RA+IA-kappa*LC]+[db*x/(j+1) for j,x in enumerate(velocityB)])
    append("canonical-cubic-cut-collar",S3,tree.constant(d),
        [RB,d*VB,d*d*BB/2,d**3*q/6])
    supports=[dict(left=tree.constant(first_left).index,width=tree.constant(first_width).index),
        dict(left=tree.constant(end).index,width=tree.constant(da).index),
        dict(left=S1.index,width=LC.index)]
    roots=dict(RA=RA.index,vA=VA.index,bA=BA.index,R=cut,
        v=v.index,b=b.index,q=q.index,RB=RB.index,vB=VB.index,bB=BB.index,
        IA=IA.index,IB=IB.index,coast_length=LC.index,total_length=length.index)
    return dict(tree=tree,pieces=pieces,supports=supports,roots=roots,
        control_terms=[dict(term) for term in CONTROL_TERMS],
        parameters=parameters,recipe=recipe,original_core=original,
        explicit_lengths=(kappa,d,da,db),cut=cut,core_end=end)


def construction_conditions(model,values):
    roots=model["roots"]; kappa,d,da,db=model["explicit_lengths"]
    V=lambda key: values[roots[key]]
    RA,VA,BA,RB,VB,BB,v,b,q=map(V,("RA","vA","bA","RB","vB","bB","v","b","q"))
    gap=RA-Box(model["cut"]);D=RA-RB
    mA=min(1-VA.absolute_upper(),1-kappa)
    mB=min(1-VB.absolute_upper(),1-kappa)
    cut_margin=min(-v.hi,1-v.absolute_upper())
    conditions=dict(
        true_core_end_radius_above_same_cut=gap.lo>0,
        true_cut_speed_strictly_inward_and_subunit=v.lo>-1 and v.hi<0,
        cut_collar_radius_gap=d<gap.lo/2,
        cut_collar_derivative_bound=b.absolute_upper()*d+q.absolute_upper()*d*d/2<cut_margin/2,
        positive_bridge_gap=D.lo>0,
        transition_total_width=da+db<D.lo/2,
        first_transition_radius=da<RA.lo/2,
        last_transition_radius=db<RB.lo/2,
        first_transition_derivative=Q(4,27)*da*BA.absolute_upper()<mA/2,
        last_transition_derivative=Q(4,27)*db*BB.absolute_upper()<mB/2,
        exact_coast_length_has_positive_enclosure=V("coast_length").lo>0)
    return dict(all_strict_conditions_proved=all(conditions.values()),conditions=conditions,
        canonical_cut_jet={key:V(key).record() for key in ("v","b","q")},
        derived_endpoint_intervals={key:V(key).record() for key in
            ("RA","RB","vA","vB","bA","bB","IA","IB","coast_length","total_length")},
        independent_float_endpoint_values_inserted=False)


def convolution(a,b):
    out=[Q(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            out[i+j]+=x*y
    return out


def bump_polynomial(order):
    coefficients=[Q(0),Q(0),Q(0),Q(64),Q(-192),Q(192),Q(-64)]
    for _ in range(order):
        coefficients=convolution(coefficients,[Q(-1),Q(2)])
    return coefficients


def piece_range(model,values,piece,t,include_controls):
    anchor,width=values[piece["anchor"]],values[piece["width"]]
    if width.lo<=0:
        raise ArithmeticError("A derived accurate piece width is not proved positive")
    coefficients=[values[index] for index in piece["coefficients"]]
    result=[polynomial_value(differentiated(coefficients,j),t)/width**j for j in range(3)]
    if not include_controls:
        return result
    s=anchor+width*t
    if model.get("control_terms")!=CONTROL_TERMS or len(model["parameters"])!=10:
        raise ValueError("Use all declared ten control terms in the accurate domain enclosure")
    for item in CONTROL_TERMS:
        poly=bump_polynomial(item["power"])
        support=model["supports"][item["support_index"]]
        p=model["parameters"][item["parameter_index"]]
        if not p:
            continue
        left,w=values[support["left"]],values[support["width"]]
        if w.lo<=0:
            raise ArithmeticError("An actual full control support lost its positive width")
        x=(s-left)/w
        lo,hi=max(Q(0),x.lo),min(Q(1),x.hi)
        if lo>hi:
            continue
        inside=Box(lo,hi)
        for j in range(3):
            term=p*w*w*polynomial_value(differentiated(poly,j),inside)/w**j
            if x.lo<0 or x.hi>1:
                term=term.hull(Box(0))
            result[j]=result[j]+term
    return result


class ResourceStop(Exception):
    pass


def prove_domain(model,values,*,include_controls,max_cells,max_depth,budget_seconds,out):
    started=time.monotonic();processed=0;passed=0;unpaid=0
    minimum=None;maximum=None;rows=[]
    stack=[(i,Q(p["local_interval"][0]),Q(p["local_interval"][1]),0)
           for i,p in reversed(list(enumerate(model["pieces"])))]
    while stack:
        if processed>=max_cells or time.monotonic()-started>=budget_seconds:
            break
        index,lo,hi,depth=stack.pop();processed+=1
        boxes=piece_range(model,values,model["pieces"][index],Box(lo,hi),include_controls)
        ok=boxes[0].lo>0 and boxes[1].lo>-1 and boxes[1].hi<1
        if not ok and depth<max_depth:
            mid=(lo+hi)/2
            stack.append((index,mid,hi,depth+1))
            stack.append((index,lo,mid,depth+1))
            continue
        passed+=int(ok);unpaid+=int(not ok)
        minimum=boxes[0].lo if minimum is None else min(minimum,boxes[0].lo)
        absolute=boxes[1].absolute_upper()
        maximum=absolute if maximum is None else max(maximum,absolute)
        rows.append(dict(piece=index,name=model["pieces"][index]["name"],
            closed_local_interval=[str(lo),str(hi)],depth=depth,
            a_ap_app=[box.record() for box in boxes],proved=ok,
            include_complete_ten_controls=include_controls))
    suffix=[dict(piece=i,closed_local_interval=[str(a),str(b)],depth=d)
            for i,a,b,d in reversed(stack)]
    payload=dict(schema=SCHEMA+"-closed-domain-ledger",leaves=rows,
        whole_unvisited_stack=suffix,complete_piece_count=len(model["pieces"]),
        interval_support_restriction_changes_function=False,
        false_certificate_is_not_a_proof_of_invalid_geometry=True)
    raw=canonical(payload);out.write_bytes(raw)
    return dict(complete=not stack and unpaid==0,processed_nodes=processed,passed_leaves=passed,
        unresolved_terminal_leaves=unpaid,unvisited_stack_entries=len(stack),
        closed_coverage_kept=True,minimum_enclosed_radius=None if minimum is None else str(minimum),
        maximum_enclosed_absolute_speed=None if maximum is None else str(maximum),
        ledger=dict(file="large-arrays/"+out.name,bytes=len(raw),sha256=sha(raw)),
        elapsed_seconds=time.monotonic()-started,all_parameter_values_retained=include_controls,
        only_a_sufficient_interval_certificate_no_new_BVP_gate=True)


def definition(model,tail_identity,core_identity,recipe_identity):
    tree=model["tree"]
    roots={key: (str(value) if key=="R" else value) for key,value in model["roots"].items()}
    return dict(schema=MODEL_SCHEMA,
        exact_definition="R300 canonical cut-cubic collar, two cubic velocities, exact cumulative coast calibration",
        source_sha256=sha(Path(__file__).read_bytes()),core_input=core_identity,
        model_recipe_input=recipe_identity,continuous_tail=tail_identity,
        parameter_order=PARAMETERS,ten_parameters=[str(p) for p in model["parameters"]],
        control_terms=[dict(term) for term in CONTROL_TERMS],
        source_text_baseline=dict(file=BASELINE_FACTORY_NAME,sha256=BASELINE_FACTORY_SHA,
            original_nine_producer_not_relabelled=True),
        added_term=dict(parameter_index=9,support_index=1,power=4,polynomial_degree=10,
            formula="w^2*64*x^3*(1-x)^3*(2*x-1)^4; x=(s-left)/w; zero outside",
            support_left_expression=model["supports"][1]["left"],
            support_width_expression=model["supports"][1]["width"],
            derivatives_are_same_radius_polynomial_derivatives=True,
            endpoint_zero_two_jets_follow_from_order3_factors=True,
            no_parameter_dependent_support_or_natural_length=True,
            zero_xi_restriction_is_original_accurate_nine_family=True,
            function_independence_does_not_assert_response_rank=True),
        expression_nodes=tree.nodes,pieces=model["pieces"],three_true_supports=model["supports"],
        derived_expression_roots=roots,core_end=str(model["core_end"]),cut_radius=str(model["cut"]),
        chosen_root_scope=model["recipe"]["root_choice"],
        polynomial_coefficients_are_expressions_not_cut_interval_midpoints=True,
        accurate_cumulative_radius_not_reset_to_old_a0=True,
        no_early_segment_mask_or_primal_clip=True,
        true_derivatives_from_the_same_radius_expression=True,
        natural_outer_radius_not_flat_extended=True,
        original_finite_Gauss_target_identified_with_this_new_family=False,
        actual_floating_point_BVP_evaluator_error_certified=False,
        same_model_identity_does_not_assert_actual_old_controlled_core_match=True,
        all_actual_ten_coefficients_preserved=True)


def main(argv=None):
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--core-file",type=Path,required=True)
    parser.add_argument("--core-file-sha256",required=True)
    parser.add_argument("--core-geometry-pointer",required=True)
    parser.add_argument("--tail-cover-directory",type=Path,required=True)
    parser.add_argument("--tail-result-sha256",required=True)
    parser.add_argument("--cut-twojet-readout",type=Path,required=True)
    parser.add_argument("--cut-twojet-readout-sha256",required=True)
    parser.add_argument("--model-recipe",type=Path,required=True)
    parser.add_argument("--model-recipe-sha256",required=True)
    parser.add_argument("--code-directory",type=Path,default=HERE)
    parser.add_argument("--r300-proof",type=Path,default=HERE.parent/"results"/R300_PROOF_NAME)
    parser.add_argument("--sqrt-bits",type=int,default=256)
    parser.add_argument("--max-domain-cells",type=int,default=65536)
    parser.add_argument("--max-domain-depth",type=int,default=32)
    parser.add_argument("--domain-budget-seconds",type=float,default=300)
    parser.add_argument("--out",type=Path,required=True)
    args=parser.parse_args(argv);require_actions()
    if (not 64<=args.sqrt_bits<=8192 or args.max_domain_cells<=0
            or not 0<=args.max_domain_depth<=80
            or not isfinite(args.domain_budget_seconds) or args.domain_budget_seconds<=0):
        raise ValueError("Invalid explicit source-expression work resources")
    if args.out.exists():
        raise FileExistsError("Use a fresh request-owned temporary output")
    destination=args.out.resolve()
    for path in (args.core_file,args.model_recipe,args.tail_cover_directory,args.cut_twojet_readout):
        if path.resolve()==destination or path.resolve().is_relative_to(destination):
            raise ValueError("Fresh output must not own an original input")
    if sha((args.code_directory/BASELINE_FACTORY_NAME).read_bytes())!=BASELINE_FACTORY_SHA:
        raise ValueError("The explicitly preserved nine factory source baseline differs")
    proof_raw=args.r300_proof.read_bytes()
    if sha(proof_raw)!=R300_PROOF_SHA:
        raise ValueError("The published R300 proof, including effective-oracle scope, differs")
    proof_receipt=dict(file=args.r300_proof.name,bytes=len(proof_raw),sha256=sha(proof_raw))
    core,core_identity=read_json(args.core_file,args.core_file_sha256)
    recipe,recipe_identity=read_json(args.model_recipe,args.model_recipe_sha256)
    geometry=pointer(core,args.core_geometry_pointer)
    core_identity["geometry_pointer"]=args.core_geometry_pointer
    core_identity["selected_geometry_canonical_sha256"]=sha(canonical(geometry))
    kernel,core_source=load_core_kernel(args.code_directory)
    core_identity["original_exact_shared_jet_source"]=core_source
    cut=rational(recipe["cut_radius"])
    args.out.mkdir(parents=True);large=args.out/"large-arrays";large.mkdir()
    error=None;tail_identity=None;conditions=None;base_domain=None;parameter_domain=None;model_receipt=None
    try:
        leaves,tail_identity=cut_jet_from_actual_cover(args.tail_cover_directory,
            args.tail_result_sha256,args.code_directory,cut,
            args.cut_twojet_readout,args.cut_twojet_readout_sha256)
        model=build_expression(kernel,geometry,recipe,leaves,cut)
        values=model["tree"].evaluate(leaves,args.sqrt_bits)
        conditions=construction_conditions(model,values)
        if not conditions["all_strict_conditions_proved"]:
            raise ArithmeticError("Inherited cut bounds/explicit widths leave R300 construction conditions unpaid")
        base_domain=prove_domain(model,values,include_controls=False,
            max_cells=args.max_domain_cells,max_depth=args.max_domain_depth,
            budget_seconds=args.domain_budget_seconds,out=large/"base-complete-domain.json")
        data=definition(model,tail_identity,core_identity,recipe_identity)
        data["construction_conditions"]=conditions
        data["published_structural_and_effective_scope_proof"]=proof_receipt
        data["given_finite_enclosure_is_not_an_effective_real_name"]=True
        data["automatic_width_search_performed"]=False
        data["actual_enclosure_leaves"]={key:value.record() for key,value in leaves.items()}
        data["base_complete_domain"]=base_domain
        raw=canonical(data);path=large/"accurate-new-model-definition.json";path.write_bytes(raw)
        model_receipt=dict(file="large-arrays/"+path.name,bytes=len(raw),sha256=sha(raw))
        # This second check retains the provided ten starting coefficients.
        # A coarse/unpaid certificate is not recast as a failed nonlinear solve.
        parameter_domain=prove_domain(model,values,include_controls=True,
            max_cells=args.max_domain_cells,max_depth=args.max_domain_depth,
            budget_seconds=args.domain_budget_seconds,out=large/"requested-ten-parameter-domain.json")
    except (ArithmeticError,ValueError,KeyError,TypeError,AssertionError) as exc:
        error=dict(type=type(exc).__name__,message=str(exc))
    result=dict(schema=SCHEMA,source_sha256=sha(Path(__file__).read_bytes()),
        repository=REPOSITORY,run_id=os.environ.get("GITHUB_RUN_ID"),source_commit=os.environ.get("GITHUB_SHA"),
        published_R300_proof=proof_receipt,
        actual_core_input=core_identity,actual_model_recipe=recipe_identity,
        actual_tail_result_sha256=args.tail_result_sha256,
        declared_tail_source_sha256=E_SOURCE_SHA,
        actual_cut_twojet_readout_sha256=args.cut_twojet_readout_sha256,
        declared_cut_twojet_readout_source_sha256=CUT_READER_SHA,
        preserved_expression_implementation_checkpoint_sha256=PRESERVED_EXPRESSION_CHECKPOINT_SHA,
        original_v2_factory_or_result_relabelled=False,
        model_definition=model_receipt,construction_conditions=conditions,
        base_domain=base_domain,requested_parameter_domain=parameter_domain,
        exact_model_definition_created=model_receipt is not None,
        nonempty_family_conditions_paid=bool(base_domain and base_domain["complete"]),
        full_current_ten_domain_certificate_complete=bool(parameter_domain and parameter_domain["complete"]),
        starting_parameters=[] if recipe.get("ten_parameters") is None else recipe["ten_parameters"],
        complete_control_terms=[dict(term) for term in CONTROL_TERMS],
        preserved_nine_factory_source_baseline_sha256=BASELINE_FACTORY_SHA,
        original_nine_factory_result_relabelled=False,
        root_choice_is_new_model_declaration=recipe.get("root_choice"),
        tail_root_values_numerically_selected=0,
        source_expression_evaluation_only=True,
        arbitrarily_refinable_real_names_supplied=False,
        automatic_width_selection_or_termination_certified=False,
        explicit_given_widths_tested_with_valid_finite_enclosures=True,
        construction_is_uniform_over_all_retained_semantic_leaf_values=True,
        sqrt_precision_is_interval_arithmetic_work_not_target_data=True,
        interval_domain_budget_seconds_per_pass=args.domain_budget_seconds,
        maximum_domain_passes=2,
        raw_outputs_are_temporary_recomputable=True,
        literal_old_g_preserved=False,old_finite_result_relabelled=False,
        actual_old_controlled_core_identity_verified=False,
        original_cut_or_warp_renormalised=False,
        original_ap_app_used_as_true_derivative=False,
        cut_interval_midpoint_used_as_model_coefficient=False,
        same_field_relative_metric_or_global_C2_geometry_certified=False,
        actual_native_calls=0,actual_nonlinear_trials=0,actual_shooting_J_calls=0,
        actual_accepted_field_created=False,actual_BVP_or_fullDN_success=False,
        method_failure_is_not_a_new_scientific_rejection=True,error=error)
    raw=canonical(result);(args.out/"result.json").write_bytes(raw)
    if len(raw)>90000:
        print(json.dumps(dict(event="continuous-ten-fixed-power-summary-too-large",bytes=len(raw),sha256=sha(raw),
            original_result_written=True)),flush=True)
        return 70
    print("BEGIN_R300_NEW_CONTINUOUS_TEN_FIXED_POWER_V3_MODEL_SUMMARY",flush=True)
    print(raw.decode(),end="",flush=True)
    print("END_R300_NEW_CONTINUOUS_TEN_FIXED_POWER_V3_MODEL_SUMMARY",flush=True)
    print(json.dumps(dict(event="continuous-ten-fixed-power-model-summary-identity",bytes=len(raw),sha256=sha(raw))),flush=True)
    return 2 if error else 0


if __name__=="__main__":
    try:
        raise SystemExit(main())
    except Exception as error:
        print(json.dumps(dict(event="continuous-ten-fixed-power-input-or-output-failure",
            type=type(error).__name__,message=str(error))),file=sys.stderr,flush=True)
        raise
