#!/usr/bin/env python3
"""R134: consume only the five complete two-mode acceleration families.

Read the published v4 original factors and one completed translated-G response
block. No forcing, N response, W basis, or old response block is constructed.
The five normal families are exported in full. Only the explicitly bound
response weight is tested modulo R8 plus its one homogeneous G-orbit direction.
"""
from __future__ import annotations

import argparse
import copy
from fractions import Fraction as F
import gzip
import json
import os
from pathlib import Path
import resource
import tempfile
import time

import literature_G_first_translation as first
import literature_local_fourth_derivative_factors as factors

seed,static,dual,poly=first.seed,first.static,first.dual,first.poly
colored,exact,formal,blocks=first.colored,first.exact,first.formal,first.blocks
canonical,sha=first.canonical,first.sha
old=static.old
SCHEMA="visible-flex-complete-acceleration-layer-mixed-v1"
BLOCK_SCHEMA="visible-flex-G-translation-successor-original-v1"
REPOSITORY=static.REPOSITORY
TOPIC=Path(first.__file__).resolve().parents[1]
MODES=(-4,-2)
FAMILIES=("A_hh","A_hk","A_kk","H1","H2")
STATE_NAMES=("h","k","omega","logh")
S0=(0,0,0,0)
FACTORS_RUN="43651096112"
FACTORS_COMMIT="2259b57065cfad67682f4c4319885fd5334c4f76"
FACTORS_DIR=TOPIC/("notes/actions-"+FACTORS_RUN+"-1-local_fourth_derivative_factors")
FACTORS_MAIN={"bytes":5477,"sha256":"42289590f4e8319d2bd4b138497702b701a11c4bcf39ba4c7ed0c2616f3aa927"}
FACTORS_RECEIPT={"bytes":33580,"sha256":"6857ea6edb3b8132147e3c0c698f79aa6f29e3b59272850267875f45a07fe95e"}
FACTORS_DRIVER={"filename":"literature_local_fourth_derivative_factors.py","bytes":22205,
    "sha256":"02785c34bfe35993094cb30cc8508a9695f78116bd4423b3ab5ae4b438295abf"}
FACTORS_EXPORT={"filename":"local-fourth-derivative-factors-original-expressions.json.gz",
    "stored_bytes":2132064,
    "stored_sha256":"9daddeaf6ad8e7aa647df4f8084ec803625c589bfc51f595ff0d9c680ce0dd4a",
    "raw_bytes":11864540,
    "raw_sha256":"58e450c47123fc682f665fffb2bb66829d9d37f502b7163e2875089b72f93fd3"}
BLOCK_DRIVER={"filename":"literature_G_translation_successor.py","bytes":39670,
    "sha256":"a4583ea776facd4ec4d92a121fed2e79af8de20d57bffc5fa22e47a8026ef406"}
FIRST_DRIVER_SHA="331fea2c1aef154c4d5866e4708f067c555f9fb61f02a11ee32a7f44d25f01f5"
MAX_RAW_INPUT=40000000

# Entries are the complete (u,w,a,b,j,ell) exponent pattern of geometric weight 4.
PATTERNS={
    (1,0,0,0,1,0):"beta_hh",(0,1,0,0,1,0):"beta_hk",
    (1,0,0,0,0,1):"beta_kh",(0,1,0,0,0,1):"beta_kk",
    (0,0,2,0,0,0):"A_hh",(0,0,1,1,0,0):"A_hk",(0,0,0,2,0,0):"A_kk",
    (2,0,1,0,0,0):"C_h_20",(1,1,1,0,0,0):"C_h_11",(0,2,1,0,0,0):"C_h_02",
    (2,0,0,1,0,0):"C_k_20",(1,1,0,1,0,0):"C_k_11",(0,2,0,1,0,0):"C_k_02",
}
TAGS=tuple(PATTERNS.values())

def source_identity():
    lower=first.source_identity()
    if lower["driver"]["sha256"]!=FIRST_DRIVER_SHA:
        raise ValueError("rebind the frozen original-expression/evaluation helpers explicitly")
    derivative=factors.dependencies()
    if derivative["driver"]!=FACTORS_DRIVER:
        raise ValueError("do not change the published complete derivative-factor producer")
    return {"driver":static.identity(__file__),"original_expression_helpers":lower,
            "factor_input_interfaces":derivative}

def read_bound_json(path,expected):
    raw=static.checked_bytes(path,100000)
    if len(raw)!=expected["bytes"] or sha(raw)!=expected["sha256"]:
        raise ValueError("bound compact JSON bytes or SHA changed")
    return json.loads(raw)

def require_digest(text,label):
    if not isinstance(text,str) or len(text)!=64 or any(c not in "0123456789abcdef" for c in text):
        raise ValueError(label+" must be an explicit lowercase SHA256")

def check_publication(value,*,run,commit,lane,driver,main_name,main_info,export_info):
    if (value.get("schema")!="visible-new-mechanism-actions-v1"
        or value.get("repository")!=REPOSITORY or str(value.get("run_id"))!=run
        or value.get("source_commit")!=commit or value.get("lane")!=lane):
        raise ValueError("terminal-publication source/run/lane identity changed")
    source_key="topics/visible-flex-new-mechanism/scripts/"+driver["filename"]
    if value.get("source_files",{}).get(source_key)!={"bytes":driver["bytes"],"sha256":driver["sha256"]}:
        raise ValueError("terminal publication does not bind the original producer")
    items=(
        (main_name,{"bytes":main_info["bytes"],"sha256":main_info["sha256"],
                    "raw_bytes":main_info["bytes"],"raw_sha256":main_info["sha256"]}),
        (export_info["filename"],{"bytes":export_info["stored_bytes"],
          "sha256":export_info["stored_sha256"],"raw_bytes":export_info["raw_bytes"],
          "raw_sha256":export_info["raw_sha256"]}))
    for name,wanted in items:
        found=[row for row in value.get("outputs",[]) if row.get("path")==name]
        if len(found)!=1 or any(found[0].get(k)!=v for k,v in wanted.items()):
            raise ValueError("terminal publication does not bind the complete input")
    return {"run":run,"commit":commit,"lane":lane,"driver":driver,
            "matched_main":main_name,"matched_export":export_info["filename"]}

def read_bound_export(path,metadata):
    if Path(metadata["filename"]).name!=metadata["filename"] or path.name!=metadata["filename"]:
        raise ValueError("original export basename changed")
    raw=static.checked_bytes(path,static.TOTAL_BYTES)
    if len(raw)!=metadata["stored_bytes"] or sha(raw)!=metadata["stored_sha256"]:
        raise ValueError("complete original export compressed identity changed")
    with gzip.open(path,"rb") as stream:
        decoded=stream.read(MAX_RAW_INPUT+1)
    if (len(decoded)>MAX_RAW_INPUT or len(decoded)!=metadata["raw_bytes"]
        or sha(decoded)!=metadata["raw_sha256"]):
        raise ValueError("complete original export raw identity changed")
    return json.loads(decoded)

def shape(key):
    if (len(key)!=10 or any(not isinstance(v,int) for v in key)
        or any(key[i]<0 for i in (1,2,3,4,5,6,7,8,9))):
        raise ValueError("full ten-coordinate Laurent/state/jet key required")
    velocity=tuple(key[i] for i in (3,4,5,6,8,9))
    state=tuple(key[i] for i in (0,1,2,7))
    if velocity in PATTERNS:
        return PATTERNS[velocity],state
    if not any(velocity[2:]) and velocity[0]+velocity[1]==4:
        return "velocity_quartic_not_consumed",state
    raise ValueError("the complete v4 contains an unproved geometric jet pattern")

class StateField:
    """Finite original-profile-valued Laurent/log polynomial in (h,k,omega)."""
    def __init__(self,ring,terms=None):
        self.ring=ring
        self.terms={tuple(key):value for key,value in (terms or {}).items() if value.terms}
    def add(self,other,amount=F(1)):
        if other.ring is not self.ring:
            raise ValueError("state fields must use the same original profile ring")
        result=dict(self.terms)
        for key,value in other.terms.items():
            result[key]=result.get(key,self.ring.number(0))+amount*value
        return StateField(self.ring,result)
    def scale(self,amount):
        return StateField(self.ring,{key:amount*value for key,value in self.terms.items()})
    def shift_h(self,amount):
        return StateField(self.ring,{(key[0]+amount,*key[1:]):value for key,value in self.terms.items()})
    def partial(self,index):
        if index not in (0,1,2):
            raise ValueError("only true state derivatives are used")
        result={}
        def put(key,value):
            result[key]=result.get(key,self.ring.number(0))+value
        for key,value in self.terms.items():
            if key[index]:
                changed=list(key);changed[index]-=1
                put(tuple(changed),key[index]*value)
            if index==0 and key[3]:
                changed=list(key);changed[0]-=1;changed[3]-=1
                put(tuple(changed),key[3]*value)
        return StateField(self.ring,result)
    def X(self):
        return self.partial(0)
    def Y(self):
        return self.partial(1).add(self.partial(2).shift_h(-1),F(1,2))
    def digest(self):
        return sha(canonical([[list(key),self.ring.digest(value)] for key,value in sorted(self.terms.items())]))

def normalized_five(groups,ring):
    get=lambda tag:StateField(ring,groups.get(tag,{}))
    bhh,bhk,bkh,bkk=(get(tag) for tag in ("beta_hh","beta_hk","beta_kh","beta_kk"))
    ahh=get("A_hh").add(bhh,-1)
    ahk=get("A_hk").add(bhk,-1).add(bkh,-1)
    akk=get("A_kk").add(bkk,-1)
    # bar C_h coefficients (alpha,beta,gamma), bar C_k (delta,epsilon,zeta).
    beta=get("C_h_11").add(bhh.Y(),-1).add(bhk.X(),-1)
    gamma=get("C_h_02").add(bhk.Y(),-1)
    delta=get("C_k_20").add(bkh.X(),-1)
    epsilon=get("C_k_11").add(bkh.Y(),-1).add(bkk.X(),-1)
    h1=delta.scale(2).add(beta,-1).scale(F(1,3))
    h2=epsilon.add(gamma,-2).scale(F(1,3))
    return {"A_hh":ahh,"A_hk":ahk,"A_kk":akk,"H1":h1,"H2":h2}

def load_v4(args,ring,report):
    main=read_bound_json(args.factor_report,FACTORS_MAIN)
    receipt=read_bound_json(args.factor_publication,FACTORS_RECEIPT)
    if (main.get("schema")!=factors.SCHEMA or main.get("completion")!="complete"
        or str(main.get("github_run_id"))!=FACTORS_RUN or main.get("github_sha")!=FACTORS_COMMIT
        or main.get("source_hashes")!=factors.dependencies()
        or main.get("factored_L2_and_L4_complete") is not True
        or main.get("original_v2_v4_both_modes_present") is not True):
        raise ValueError("the completed original two-mode derivative factors are required")
    metadata=main.get("portable_complete_factor_export") or {}
    if any(metadata.get(key)!=value for key,value in FACTORS_EXPORT.items()):
        raise ValueError("complete original factor metadata changed")
    binding=check_publication(receipt,run=FACTORS_RUN,commit=FACTORS_COMMIT,
        lane="local_fourth_derivative_factors",driver=FACTORS_DRIVER,
        main_name=args.factor_report.name,main_info=FACTORS_MAIN,export_info=metadata)
    data=read_bound_export(args.factor_export,metadata)
    if (data.get("schema")!=factors.SCHEMA+"-original-expressions"
        or data.get("content_scope")!="unreduced-N0-N2-and-complete-two-mode-v2-v4"
        or data.get("source_hashes")!=main["source_hashes"]
        or str(data.get("github_run_id"))!=FACTORS_RUN or data.get("github_sha")!=FACTORS_COMMIT
        or data.get("geometry_names")!=list(factors.GEOMETRY_NAMES)
        or data.get("real_s_derivatives_before_history_zero") is not True):
        raise ValueError("original factor export scope/geometry/anchor identity")
    selected={};selected_rows=[];seen=set()
    counts={mode:{"v4_total":0,"selected_acceleration":0,"omitted_velocity_quartic":0}
            for mode in MODES}
    for row in data["local_generator_records"]:
        if row["geometry_derivative_weight"]!=4:
            continue
        mode,key,name=row["mode"],tuple(row["geometry_key"]),row["root"]
        if mode not in counts or (mode,key) in seen or factors.geometry_weight(key)!=4:
            raise ValueError("complete v4 original record coverage")
        seen.add((mode,key));counts[mode]["v4_total"]+=1
        tag,state=shape(key)
        if tag=="velocity_quartic_not_consumed":
            counts[mode]["omitted_velocity_quartic"]+=1
            continue
        if name in selected or name not in data["roots"]:
            raise ValueError("duplicate or absent original acceleration root")
        selected[name]=data["roots"][name]
        selected_rows.append((mode,tag,state,name,key))
        counts[mode]["selected_acceleration"]+=1
    if any(counts[mode]["v4_total"]!=1236 for mode in MODES):
        raise ValueError("frozen complete v4 coefficient count changed")
    # Confirm the structural premise from published keys, without composing any N response.
    for row in data["potential_records"]:
        if row["geometry_derivative_weight"]==2:
            key=tuple(row["geometry_key"])
            if any(key[i] for i in (5,6,8,9)) or key[3]+key[4]!=2:
                raise ValueError("N2 must be a pure velocity quadratic before using R134")
    for rows in data["pointwise_matrix_original_coefficients"]:
        for row in rows:
            if row["geometry_derivative_weight"]==2:
                key=tuple(row["geometry_key"])
                if any(key[i] for i in (5,6,8,9)) or key[3]+key[4]!=2:
                    raise ValueError("m2 must be a pure velocity quadratic")
    subset={**data,"roots":selected,"original_root_sha256":{
        name:data["original_root_sha256"][name] for name in selected}}
    roots=old.decode_expressions(ring,subset)
    groups={mode:{tag:{} for tag in TAGS} for mode in MODES}
    for mode,tag,state,name,key in selected_rows:
        value=roots[name]
        if any(ring.p.weight(m)!=4 for m in value.terms):
            raise ValueError("the original local v4 lost fourth profile degree")
        if state in groups[mode][tag]:
            raise ValueError("a canonical original state coefficient was duplicated")
        groups[mode][tag][state]=value
    report["factor_input"]={"publication":binding,"main":FACTORS_MAIN,"receipt":FACTORS_RECEIPT,
        "complete_export":metadata,"selected_original_counts":{str(k):v for k,v in counts.items()},
        "selected_records_sha256":sha(canonical([[mode,tag,list(state),name,list(key),
                        data["original_root_sha256"][name]] for mode,tag,state,name,key in selected_rows])),
        "all_selected_v4_original_hashes_verified":True,
        "m2_and_N2_pure_velocity_quadratic_keys_verified":True,
        "N_responses_composed":False,"v2_or_velocity_quartic_targets_evaluated":False,
        "forcing_or_third_basis_recompiled":False}
    return {mode:normalized_five(groups[mode],ring) for mode in MODES}


def load_response_block(args,ring,report):
    if not all((args.response_report,args.response_report_sha256,args.response_publication,
                args.response_publication_sha256,args.response_run,args.response_commit,
                args.response_lane,args.response_export)):
        raise ValueError("a completed portable new response block must be explicitly bound")
    require_digest(args.response_report_sha256,"response main")
    require_digest(args.response_publication_sha256,"response receipt")
    raw=static.checked_bytes(args.response_report,100000)
    receipt_raw=static.checked_bytes(args.response_publication,100000)
    if sha(raw)!=args.response_report_sha256 or sha(receipt_raw)!=args.response_publication_sha256:
        raise ValueError("the explicit new response publication changed")
    main,receipt=json.loads(raw),json.loads(receipt_raw)
    checkpoint=main.get("checkpoint") or {}
    translation=checkpoint.get("original_translation_target") or {}
    upper=checkpoint.get("response_upper_bound") or {}
    metadata=checkpoint.get("portable_new_block_expression_export") or {}
    outcome=checkpoint.get("outcome")
    weight=1-args.response_order
    expected_pairs=[(i,j) for i,wi in enumerate(blocks.PARAMETER_WEIGHTS)
                    for j,wj in enumerate(blocks.THIRD_WEIGHTS) if wi+wj==weight]
    retained=upper.get("retained_original_columns")
    if (main.get("schema")!=BLOCK_SCHEMA or main.get("completion")!="complete"
        or main.get("github_repository")!=REPOSITORY
        or str(main.get("github_run_id"))!=args.response_run
        or main.get("github_sha")!=args.response_commit
        or main.get("source_hashes",{}).get("driver")!=BLOCK_DRIVER
        or checkpoint.get("requested_order")!=args.response_order
        or checkpoint.get("requested_weight")!=weight
        or translation.get("order")!=args.response_order or translation.get("weight")!=weight
        or outcome not in ("nonmember_certified","member_identity_verified","undecided")
        or upper.get("original_columns")!=len(expected_pairs)
        or not isinstance(retained,list) or len(set(retained))!=len(retained)
        or any(not isinstance(i,int) or not 0<=i<len(expected_pairs) for i in retained)
        or upper.get("proved_true_response_dimension_upper_bound")!=len(retained)
        or upper.get("verified_original_dependency_count")!=len(expected_pairs)-len(retained)
        or not metadata.get("persisted")
        or metadata.get("content_scope")!="one-translation-target-and-complete-new-response-block"
        or metadata.get("compiled_original_columns")!=len(expected_pairs)
        or not metadata.get("all_compiled_original_columns_included")):
        raise ValueError("the requested completed full E8 x W36 weight block is required")
    require_digest(upper.get("verified_original_dependencies_sha256"),"completed dependency certificate")
    if outcome=="nonmember_certified":
        witness=checkpoint.get("dual_certificate") or {}
        coefficient=main.get("coefficient_checkpoint") or {}
        if (not checkpoint.get("universal_target_nonmember_in_full_R8")
            or not witness.get("rational_nonmembership_certified")
            or witness.get("control_columns")!=len(retained)
            or witness.get("modular_control_rank")!=len(retained)
            or not witness.get("modular_pivot_determinant")
            or not witness.get("modular_augmented_determinant")
            or not coefficient.get("all_encountered_rational_denominators_invertible")):
            raise ValueError("the published G-orbit independence claim has no complete original witness")
    if outcome=="member_identity_verified" and set(checkpoint.get("fresh_original_checks",{}))!={"-4","-2"}:
        raise ValueError("the published G-orbit membership lacks both original mode checks")
    binding=check_publication(receipt,run=args.response_run,commit=args.response_commit,
        lane=args.response_lane,driver=BLOCK_DRIVER,main_name=args.response_report.name,
        main_info={"bytes":len(raw),"sha256":sha(raw)},export_info=metadata)
    data=read_bound_export(args.response_export,metadata)
    if (data.get("schema")!=BLOCK_SCHEMA+"-original-expressions"
        or data.get("content_scope")!=metadata["content_scope"]
        or data.get("github_repository")!=REPOSITORY
        or str(data.get("github_run_id"))!=args.response_run or data.get("github_sha")!=args.response_commit
        or data.get("source_hashes")!=main["source_hashes"]
        or data.get("translation")!=translation
        or data.get("response_coverage",{}).get("weight")!=weight
        or not data.get("response_coverage",{}).get("full_E8")
        or not data.get("response_coverage",{}).get("all_W36")
        or data.get("response_coverage",{}).get("columns")!=len(expected_pairs)
        or not data.get("all_compiled_original_columns_included")):
        raise ValueError("complete portable response scope differs from its finished certificate")
    roots=old.decode_expressions(ring,data)
    records=data.get("column_records") or []
    if len(records)!=len(expected_pairs) or len(roots)!=2*(len(records)+1):
        raise ValueError("complete original target and all response roots required")
    used=set()
    original=[]
    for index,(row,pair) in enumerate(zip(records,expected_pairs)):
        label=row["label"]
        if (row.get("index")!=index or (label.get("quadratic_index"),label.get("third_index"))!=pair
            or label.get("third_weight")!=blocks.THIRD_WEIGHTS[pair[1]]
            or label.get("v2_original_third_index")!=blocks.EXPECTED_KEPT[pair[1]]):
            raise ValueError("the complete E8 x W36 enumeration changed")
        value={}
        for mode in MODES:
            name=row["roots"][str(mode)]
            if name in used or name not in roots:
                raise ValueError("portable response root is duplicate or missing")
            used.add(name);value[mode]=roots[name]
            if ring.digest(value[mode])!=row["original_mode_sha256"][str(mode)]:
                raise ValueError("portable original response hash changed")
        original.append(value)
    orbit={}
    for mode in MODES:
        name=data["target_roots"][str(mode)]
        if name in used or name not in roots:
            raise ValueError("portable G-orbit root is duplicate or missing")
        used.add(name);orbit[mode]=roots[name]
        if ring.digest(orbit[mode])!=translation["original_target_sha256"][str(mode)]:
            raise ValueError("the new original G-orbit target changed")
    if used!=set(roots):
        raise ValueError("undeclared roots in the response export")
    controls=[original[index] for index in retained]
    labels=[{"role":"R8_original_response","original_column":index,
             "label":records[index]["label"]} for index in retained]
    # A certified member need not be added again. Otherwise it supplies the full
    # one-dimensional homogeneous orbit contribution, whether independent or not.
    if outcome!="member_identity_verified":
        controls.append(orbit)
        labels.append({"role":"G_orbit","order":args.response_order,
                       "original_mode_sha256":translation["original_target_sha256"]})
    grade=blocks.ScalingGrading(ring)
    for value in controls:
        if any(set(grade.split(expr))-{weight} for expr in value.values()):
            raise ValueError("the consumed complete homogeneous controls changed weight")
    report["response_input"]={"publication":binding,"compact_main_bytes":len(raw),
        "compact_main_sha256":sha(raw),"publication_sha256":sha(receipt_raw),
        "complete_export":metadata,"original_response_upper_bound":upper,
        "completed_G_outcome":outcome,"weight":weight,"order":args.response_order,
        "complete_R8_plus_homogeneous_G_orbit_dimension_upper_bound":len(controls),
        "this_upper_bound_already_proved_independent":outcome=="nonmember_certified",
        "retained_original_control_labels":labels,
        "all_original_export_root_hashes_verified":True,
        "response_compositions_rebuilt":False,"old_dependency_proofs_recomputed":False,
        "old_G_orbit_separation_reevaluated":False}
    return controls,labels

def original_targets(families,ring,weight,report):
    grade=blocks.ScalingGrading(ring)
    originals=[];selected=[];dedup={}
    all_weights={}
    for family in FAMILIES:
        keys=sorted(set(families[-4][family].terms)|set(families[-2][family].terms))
        all_weights[family]={}
        for key in keys:
            modes={mode:families[mode][family].terms.get(key,ring.number(0)) for mode in MODES}
            split={mode:grade.split(value) for mode,value in modes.items()}
            weights=sorted(set(split[-4])|set(split[-2]))
            for found in weights:
                all_weights[family][str(found)]=all_weights[family].get(str(found),0)+1
            target={mode:split[mode].get(weight,ring.number(0)) for mode in MODES}
            record={"family":family,"state_key":list(key),"profile_weights":weights,
                "original_mode_sha256":{str(mode):ring.digest(value) for mode,value in modes.items()},
                "requested_weight_original_mode_sha256":{
                    str(mode):ring.digest(value) for mode,value in target.items()}}
            originals.append((record,modes,target))
            if any(value.terms for value in target.values()):
                token=tuple(ring.digest(target[mode]) for mode in MODES)
                alias={"family":family,"state_key":list(key)}
                if token in dedup:
                    selected[dedup[token]]["aliases"].append(alias)
                else:
                    dedup[token]=len(selected)
                    selected.append({"id":len(selected),"aliases":[alias],"modes":target,
                                     "original_mode_sha256":dict(zip(map(str,MODES),token))})
    report["normal_acceleration_extraction"]={
        "state_coordinate_order":list(STATE_NAMES),"families":list(FAMILIES),
        "formula_source":"R129 equations for bar A,H1,H2; R134 v4-only layer",
        "complete_both_modes":True,"full_ungraded_state_coefficients":len(originals),
        "distinct_requested_weight_targets":len(selected),"requested_weight":weight,
        "weight_counts_by_family":all_weights,
        "family_original_state_hashes":{str(mode):{name:value.digest() for name,value in row.items()}
                                       for mode,row in families.items()},
        "no_geometry_coefficients_assumed_independently_actual_before_R130":True,
        "whole_L2_or_L4_computed":False,"N2_dropped_from_Q4":False,
        "only_acceleration_layer_consumed":True}
    return originals,selected

def save_targets(args,ring,originals,selected,report):
    path=args.output.with_name(args.output.stem+"-original-expressions.json.gz")
    info={"filename":path.name,"persisted":False,"supplemental_to_mathematical_certificate":True}
    report["portable_acceleration_expression_export"]=info
    named={};records=[];selected_records=[]
    for index,(record,modes,target) in enumerate(originals):
        roots={str(mode):f"family_{index:04d}_{mode}" for mode in MODES}
        named.update({roots[str(mode)]:value for mode,value in modes.items()})
        records.append({**record,"roots":roots})
    for item in selected:
        roots={str(mode):f"selected_{item['id']:04d}_{mode}" for mode in MODES}
        named.update({roots[str(mode)]:value for mode,value in item["modes"].items()})
        selected_records.append({k:v for k,v in item.items() if k!="modes"}|{"roots":roots})
    count=sum(len(value.terms) for value in named.values())
    info["original_root_term_count"]=count
    if count>300000:
        info["reason"]="supplemental original root serialization ceiling"
        return
    try:
        data={"schema":SCHEMA+"-original-expressions",
            "content_scope":"five-complete-two-mode-normal-acceleration-families",
            "github_repository":report.get("github_repository"),
            "github_run_id":report.get("github_run_id"),"github_sha":report.get("github_sha"),
            "source_hashes":report["source_hashes"],"factor_input":report["factor_input"],
            "state_coordinate_order":list(STATE_NAMES),"family_records":records,
            "selected_weight":report["normal_acceleration_extraction"]["requested_weight"],
            "selected_weight_records":selected_records,
            "contains_no_old_response_roots":True,**old.serialize_expressions(ring,named)}
        raw=canonical(data)
        info.update({"raw_bytes":len(raw),"raw_sha256":sha(raw),"root_count":len(named),
                     "profile_atom_count":len(data["profile_atoms"]),
                     "content_scope":data["content_scope"]})
        if len(raw)>MAX_RAW_INPUT:
            info["reason"]="supplemental raw byte ceiling"
            return
        packed=gzip.compress(raw,mtime=0)
        info.update({"stored_bytes":len(packed),"stored_sha256":sha(packed)})
        if len(packed)>args.max_export_bytes:
            info["reason"]="supplemental compressed byte ceiling"
            return
        path.parent.mkdir(parents=True,exist_ok=True);path.write_bytes(packed)
        info["persisted"]=True
        info["all_five_complete_families_included"]=True
        info["contains_original_expression_not_only_hashes"]=True
    except Exception as error:
        info["reason"]="supplemental export failed; mathematical status remains independent"
        info["error"]={"type":type(error).__name__,"message":str(error)}

def raw_new_target_evaluation(args,ring,target,controls,report,seconds):
    """Evaluate only consumed original roots, never reconstruct a response."""
    context=poly.PolynomialContext(args.prime,2,3,seconds=seconds,
        max_degree=args.max_degree,memory_mib=args.memory_mib,max_operations=args.max_operations)
    try:
        _,_,profiles=dual.fixed_profiles(context,args.bump_power)
        evaluator=poly.RawExpressionEvaluator(ring.p,context,context.colors)
        points=[F(j,args.points+1) for j in range(1,args.points+1)]
        labels=[{"t":str(t),"xi":str(context.left+context.width*t),"mode":mode,"component":component}
            for t in points for mode in MODES for component in ("real","imaginary")]
        def rows(modes):
            return [v for t in points for mode in MODES for v in modes[mode].value(t)]
        values={mode:evaluator.expression(value) for mode,value in target.items()}
        b=rows(values);columns=[]
        hashes=[]
        for index,modes in enumerate(controls):
            value={mode:evaluator.expression(expression) for mode,expression in modes.items()}
            columns.append(rows(value))
            hashes.append({"control":index,"mode_polynomials":{
                str(mode):{"sha256":v.digest(),"degree":len(v.coefficients)-1}
                for mode,v in value.items()}})
            report["checkpoint"]["evaluated_input_controls"]=len(columns)
            context.check(0)
        matrix=[[column[i] for column in columns] for i in range(len(labels))]
        witness=poly.full_column_dual(matrix,b,args.prime)
        if witness["rational_nonmembership_certified"]:
            witness["selected_evaluation_labels"]=[labels[i] for i in witness["selected_augmented_rows"]]
        return {"fixed_profiles":profiles,"same_fixed_pair_for_all_controls_and_modes":True,
            "original_right_integrals_used":True,"word_representatives_evaluated":False,
            "new_response_compositions_constructed":False,"all_evaluation_labels":labels,
            "matrix_sha256":sha(canonical(matrix)),"target_sha256":sha(canonical(b)),
            "original_control_polynomials":hashes,
            "new_target_mode_polynomials":{str(mode):{"sha256":value.digest(),
                "degree":len(value.coefficients)-1} for mode,value in values.items()},
            "dual_certificate":witness}
    finally:
        report["coefficient_checkpoint"]=context.coefficient_report()

def study(args,report,started):
    limits=exact.Limits(args.max_seconds,500000,100000,120000,500000,args.memory_mib,8192)
    ring=colored.ColoredRing(limits);weight=1-args.response_order
    report["phase"]="consume_published_acceleration_and_third_jet_v4_roots"
    families=load_v4(args,ring,report)
    originals,selected=original_targets(families,ring,weight,report)
    report["phase"]="export_five_complete_normal_acceleration_families"
    save_targets(args,ring,originals,selected,report)
    if args.extract_only or not selected:
        report["checkpoint"]={"outcome":("complete_extraction_only" if args.extract_only
                               else "requested_weight_has_no_nonzero_original_coefficients"),
            "requested_weight":weight,"other_weights_paid":False,"full_fourth_cost_paid":False}
        report["completion"]="complete"
        return
    report["phase"]="consume_completed_portable_R8_plus_G_orbit_weight_block"
    controls,labels=load_response_block(args,ring,report)
    regularity=dual.reachable_jet_bound(ring,[value for item in selected for value in item["modes"].values()]
        +[value for modes in controls for value in modes.values()])
    report["input_regularity"]=regularity
    if regularity["maximum_input_jet"]>args.bump_power-1:
        raise ValueError("the fixed test profiles do not meet the actual input jet bound")
    normalizer=colored.ColoredNormalizer(ring)
    vectors=[colored.vector_from_modes(value,normalizer) for value in controls]
    span=colored.JointSpan(vectors,limits)
    report["consumed_control_representatives"]={"columns":len(controls),
        "representative_rank":len(span.independent),
        "actual_span_upper_bound_from_completed_source":len(controls),
        "representative_independence_not_assumed":True}
    outcomes=[];unresolved=[]
    report["new_coefficient_outcomes"]=outcomes
    report["phase"]="only_new_acceleration_coefficient_memberships_at_bound_weight"
    for item in selected:
        target=item["modes"];vector=colored.vector_from_modes(target,normalizer)
        coefficients,remainder=span.reduce(vector)
        row={k:v for k,v in item.items() if k!="modes"}
        row["word_remainder"]={"terms":len(remainder),"sha256":colored.vector_digest(remainder),
                               "nonmembership_claimed":False}
        if not remainder:
            row["outcome"]="original_member_identity_verified"
            row["coefficients_in_consumed_controls"]=[[index,str(value)] for index,value in sorted(coefficients.items())]
            row["fresh_original_checks"]=first.fresh_zero(ring,target,controls,coefficients)
        else:
            row["outcome"]="unresolved_representative"
            unresolved.append(item)
        outcomes.append(row)
        report["checkpoint"]={"processed_new_targets":len(outcomes),"total_new_targets":len(selected),
            "verified_members":len(outcomes)-len(unresolved),"unresolved":len(unresolved)}
        limits.formal.time_check()
    report["new_coefficient_outcomes"]=outcomes
    if not unresolved:
        report["checkpoint"]={"outcome":"all_requested_weight_families_paid_by_original_identities",
            "requested_weight":weight,"verified_distinct_original_targets":len(selected),
            "all_five_complete_families_at_this_weight_paid":True,"other_weights_paid":False,
            "whole_velocity_quartic_or_fourth_cost_paid":False}
        report["completion"]="complete"
        return
    candidate=unresolved[0]
    report["phase"]="one_new_unresolved_original_acceleration_coefficient_dual"
    seconds=args.max_seconds-(time.monotonic()-started)
    if seconds<=0:
        raise poly.PolynomialBudgetExceeded("time before the one selected original new target")
    report["checkpoint"]={"candidate_id":candidate["id"],"candidate_aliases":candidate["aliases"],
        "original_target_sha256":candidate["original_mode_sha256"],
        "requested_weight":weight,"new_unresolved_targets":len(unresolved),"evaluated_input_controls":0}
    report["new_original_evaluation"]=raw_new_target_evaluation(args,ring,candidate["modes"],
                                                                controls,report,seconds)
    witness=report["new_original_evaluation"]["dual_certificate"]
    proved=witness["rational_nonmembership_certified"]
    report["checkpoint"]={"outcome":"new_true_U4_quotient_direction_certified" if proved else "undecided",
        "candidate_id":candidate["id"],"candidate_aliases":candidate["aliases"],
        "original_target_sha256":candidate["original_mode_sha256"],
        "requested_weight":weight,"dual_certificate":witness,
        "actual_U4_membership_source":"R130 and R134; true normalized state coefficients and affine weight projection",
        "outside_complete_R8_plus_G_orbit_at_this_weight":proved,
        "additional_true_quotient_direction_not_actual_signed_control":proved,
        "all_remaining_unresolved_targets_tested":False,
        "other_weights_or_ruling_paid":False}
    report["completion"]="complete"


def small_toy():
    limits=exact.Limits(seconds=30,nodes=10000,atoms=5000,terms=5000,rewrites=10000,memory_mib=256)
    ring=colored.ColoredRing(limits)
    q,qb=ring.color("q"),ring.color("qbar")
    phi=q*q*q*q
    mixed=q*q*qb*qb
    checks={}
    def field(terms):
        return StateField(ring,terms)
    def equal(left,right,label):
        if left.add(right,-1).terms:
            raise AssertionError(label)
        checks[label]=True
    f=field({(2,0,0,1):phi,(0,1,1,0):mixed})
    equal(f.X(),field({(1,0,0,1):2*phi,(1,0,0,0):phi}),
          "horizontal_h_derivative_keeps_Laurent_and_log_terms")
    equal(f.Y(),field({(0,0,1,0):mixed,(-1,1,0,0):mixed/2}),
          "horizontal_k_derivative_includes_true_omega_rate")
    g=field({(-1,2,0,0):mixed})
    h=field({(1,0,1,0):phi})
    z=field({(0,0,0,0):mixed})
    groups={tag:{} for tag in TAGS}
    # Exact D_s[(f u+g w)a+(h u+z w)b].  Velocity quartic parts
    # are outside this test's acceleration layer, exactly as in the real consumer.
    for tag,value in (("beta_hh",f),("beta_hk",g),("beta_kh",h),("beta_kk",z),
                      ("A_hh",f),("A_hk",g.add(h)),("A_kk",z),
                      ("C_h_20",f.X()),("C_h_11",f.Y().add(g.X())),
                      ("C_h_02",g.Y()),("C_k_20",h.X()),
                      ("C_k_11",h.Y().add(z.X())),("C_k_02",z.Y())):
        groups[tag]=value.terms
    result=normalized_five(groups,ring)
    if any(value.terms for value in result.values()):
        raise AssertionError("third-jet potential must have no normal acceleration coefficients")
    checks["complete_artificial_third_jet_potential_removed"]=True
    velocity_potential={tag:{} for tag in TAGS}
    velocity_potential["C_h_11"]=f.scale(2).terms
    velocity_potential["C_k_20"]=f.terms
    if any(value.terms for value in normalized_five(velocity_potential,ring).values()):
        raise AssertionError("D_s(f u squared w) acceleration part")
    checks["cubic_velocity_potential_has_zero_area_multipliers"]=True
    area={tag:{} for tag in TAGS}
    area["C_h_11"]=f.scale(-1).terms
    area["C_k_20"]=f.terms
    area["C_h_02"]=g.scale(-1).terms
    area["C_k_11"]=g.terms
    result=normalized_five(area,ring)
    equal(result["H1"],f,"first_actual_area_multiplier_recovered")
    equal(result["H2"],g,"second_actual_area_multiplier_recovered")
    if any(result[name].terms for name in ("A_hh","A_hk","A_kk")):
        raise AssertionError("area term leaked into acceleration quadratic")
    checks["area_has_no_acceleration_quadratic_part"]=True
    for pattern,tag in PATTERNS.items():
        key=[0]*10
        for index,power in zip((3,4,5,6,8,9),pattern):
            key[index]=power
        key[0]=-2;key[1]=3;key[2]=1;key[7]=2
        if shape(tuple(key))!=(tag,(-2,3,1,2)):
            raise AssertionError("complete physical jet classifier")
    checks["all_thirteen_acceleration_patterns_keep_state_key"]=True
    quartic=(0,0,0,2,2,0,0,0,0,0)
    if shape(quartic)[0]!="velocity_quartic_not_consumed":
        raise AssertionError("the uncomputed velocity quartic layer was not separated")
    checks["velocity_quartic_is_explicitly_not_consumed"]=True
    try:
        shape((0,0,0,0,0,0,0,0,2,0))
    except ValueError:
        checks["unproved_higher_jet_pattern_rejected"]=True
    else:
        raise AssertionError("unsupported physical pattern")
    portable=old.serialize_expressions(ring,{"pure":phi,"mixed":mixed,"right_primitive":(q.D()*qb).I()})
    restored=old.decode_expressions(ring,portable)
    if (restored["pure"]-phi).terms or (restored["mixed"]-mixed).terms:
        raise AssertionError("complete colored original export")
    if ring.digest(restored["pure"])==ring.digest(restored["mixed"]):
        raise AssertionError("independent q/qbar colors collapsed")
    checks["portable_original_export_preserves_independent_phase_colors"]=True
    artificial_driver={"filename":"artificial.py","bytes":11,"sha256":"a"*64}
    main={"bytes":13,"sha256":"b"*64}
    export={"filename":"artificial.gz","stored_bytes":17,"stored_sha256":"c"*64,
            "raw_bytes":19,"raw_sha256":"d"*64}
    receipt={"schema":"visible-new-mechanism-actions-v1","repository":REPOSITORY,
        "run_id":"artificial-run","source_commit":"artificial-commit","lane":"artificial-lane",
        "source_files":{"topics/visible-flex-new-mechanism/scripts/artificial.py":
                        {"bytes":11,"sha256":"a"*64}},
        "outputs":[{"path":"artificial.json","bytes":13,"sha256":"b"*64,
                    "raw_bytes":13,"raw_sha256":"b"*64},
                   {"path":"artificial.gz","bytes":17,"sha256":"c"*64,
                    "raw_bytes":19,"raw_sha256":"d"*64}]}
    arguments={"run":"artificial-run","commit":"artificial-commit","lane":"artificial-lane",
               "driver":artificial_driver,"main_name":"artificial.json","main_info":main,
               "export_info":export}
    check_publication(receipt,**arguments)
    checks["artificial_main_and_complete_export_publication_bound"]=True
    damaged=copy.deepcopy(receipt);damaged["outputs"][1]["raw_sha256"]="bad"
    try:
        check_publication(damaged,**arguments)
    except ValueError:
        checks["changed_original_raw_export_hash_rejected"]=True
    else:
        raise AssertionError("changed raw export")
    return {"checks":checks,"all_passed":all(checks.values()),
        "published_factors_read":False,"research_profile_evaluated":False,
        "original_response_block_read":False,"any_research_target_compiled":False}

def compact_dual(report):
    checkpoint=report.get("checkpoint") or {}
    witness=checkpoint.get("dual_certificate")
    if not witness or "modular_augmented_matrix" not in witness:
        return
    matrix=witness["modular_augmented_matrix"]
    if len(canonical(matrix))<=12000:
        return
    slim=copy.deepcopy(witness)
    del slim["modular_augmented_matrix"]
    slim["original_modular_augmented_matrix"]={"rows":len(matrix),
        "columns":len(matrix[0]) if matrix else 0,"sha256":sha(canonical(matrix)),
        "full_matrix_in_complete_report":True}
    checkpoint["dual_certificate"]=slim

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--toy-only",action="store_true")
    parser.add_argument("--extract-only",action="store_true")
    parser.add_argument("--output",type=Path,required=True)
    parser.add_argument("--factor-report",type=Path,default=FACTORS_DIR/"local-fourth-derivative-factors.json")
    parser.add_argument("--factor-publication",type=Path,default=FACTORS_DIR/"receipt.json")
    parser.add_argument("--factor-export",type=Path,default=FACTORS_DIR/FACTORS_EXPORT["filename"])
    response_dir=TOPIC/"notes/actions-43653293263-1-g_translation_successor"
    parser.add_argument("--response-report",type=Path,default=response_dir/"G-third-translation.json")
    parser.add_argument("--response-report-sha256")
    parser.add_argument("--response-publication",type=Path,default=response_dir/"receipt.json")
    parser.add_argument("--response-publication-sha256")
    parser.add_argument("--response-export",type=Path,default=response_dir/"G-third-translation-original-expressions.json.gz")
    parser.add_argument("--response-run",default="43653293263")
    parser.add_argument("--response-commit",default="2f0add61f44365d713abf836beaa8b0be2806a3d")
    parser.add_argument("--response-lane",default="g_translation_successor")
    parser.add_argument("--response-order",type=int,choices=tuple(range(3,11)),default=3)
    parser.add_argument("--max-seconds",type=float,default=240)
    parser.add_argument("--memory-mib",type=int,default=1024)
    parser.add_argument("--max-degree",type=int,default=256)
    parser.add_argument("--max-operations",type=int,default=10000000)
    parser.add_argument("--points",type=int,default=24)
    parser.add_argument("--bump-power",type=int,default=8)
    parser.add_argument("--prime",type=int,default=2147483647)
    parser.add_argument("--max-main-bytes",type=int,default=90000)
    parser.add_argument("--max-full-report-bytes",type=int,default=2500000)
    parser.add_argument("--max-export-bytes",type=int,default=2000000)
    args=parser.parse_args()
    if (min(args.max_seconds,args.memory_mib,args.max_degree,args.max_operations,args.points,
            args.max_main_bytes,args.max_full_report_bytes,args.max_export_bytes)<=0
        or args.bump_power<8):
        parser.error("positive bounded resources and a sufficiently smooth fixed bump are required")
    if args.prime%4!=3 or args.points+1>=args.prime:
        parser.error("the checked prime must be 3 mod 4 and exceed evaluation denominators")
    if not 10000<=args.max_main_bytes<100000:
        parser.error("the main must remain below 100 KB")
    if args.max_main_bytes+args.max_full_report_bytes+args.max_export_bytes>static.TOTAL_BYTES:
        parser.error("complete reports and supplemental export exceed the output reservation")
    if not args.toy_only and not(os.environ.get("GITHUB_ACTIONS")=="true"
                                 and os.environ.get("GITHUB_REPOSITORY")==REPOSITORY):
        parser.error("genuine coefficient extraction/evaluation only in this public repository Actions")
    if not args.toy_only and not args.extract_only:
        if not args.response_report_sha256 or not args.response_publication_sha256:
            parser.error("bind the real completed G-successor main and publication SHA before this study")
    started=time.monotonic()
    report={"schema":SCHEMA,"completion":"started","phase":"source_binding",
        "github_repository":os.environ.get("GITHUB_REPOSITORY"),
        "github_run_id":os.environ.get("GITHUB_RUN_ID"),"github_sha":os.environ.get("GITHUB_SHA"),
        "source_hashes":{},"completed_blocks":[],
        "scope":"five complete mixed acceleration families; only one bound R8 plus G-orbit weight",
        "limits":{"seconds":args.max_seconds,"memory_polling_mib":args.memory_mib,
            "max_degree":args.max_degree,"max_operations":args.max_operations,
            "main_bytes":args.max_main_bytes,"full_report_bytes":args.max_full_report_bytes,
            "supplemental_export_bytes":args.max_export_bytes,"total_bytes":static.TOTAL_BYTES},
        "old_forcing_recompiled":False,"third_basis_recompiled":False,
        "old_response_compositions_rebuilt":False,"N_responses_composed":False,
        "complete_U4_equals_R8_proved":False,"P0_or_ruling_paid":False,
        "all_derivative_weights_computed":False,"finite_isometric_family_constructed":False}
    code=0
    try:
        report["source_hashes"]=source_identity()
        if args.toy_only:
            report["phase"]="small_artificial_horizontal_IBP_and_original_input_interfaces"
            report["toy"]=small_toy();report["completion"]="toy_passed"
        else:
            study(args,report,started)
    except (formal.CompilationBudgetExceeded,poly.PolynomialBudgetExceeded) as error:
        report["completion"]="resource_limit";report["error"]=str(error);code=2
    except Exception as error:
        report["completion"]="implementation_check_failed"
        report["error"]={"type":type(error).__name__,"message":str(error)};code=1
    checkpoint=report.setdefault("checkpoint",{})
    for key in ("factor_input","response_input","normal_acceleration_extraction",
                "portable_acceleration_expression_export","input_regularity"):
        if key in report:
            checkpoint[key]=report[key]
    if "new_coefficient_outcomes" in report:
        rows=report["new_coefficient_outcomes"]
        checkpoint["new_coefficient_proof_summary"]={
            "processed":len(rows),
            "original_member_identities":sum(row["outcome"]=="original_member_identity_verified" for row in rows),
            "unresolved_representatives":sum(row["outcome"]!="original_member_identity_verified" for row in rows),
            "all_outcomes_sha256":sha(canonical(rows)),"complete_proofs_in_full_report":True}
    compact_dual(report)
    report["elapsed_seconds"]=time.monotonic()-started
    report["peak_rss_mib"]=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1024
    metadata=report.get("portable_acceleration_expression_export") or {}
    used=metadata.get("stored_bytes",0) if metadata.get("persisted") else 0
    written=static.publish_report(args.output,report,args.max_main_bytes,args.max_full_report_bytes,
                                  already_published=used)
    if written["completion"]=="output_limit":
        code=2
    print(json.dumps({"output":str(args.output),**written}),flush=True)
    return code

if __name__=="__main__":
    raise SystemExit(main())
