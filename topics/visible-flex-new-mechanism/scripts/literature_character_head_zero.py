#!/usr/bin/env python3
"""Complete weight-zero character head from published originals.

R190/R192 reduce missing N responses to at most sixteen. All N projections
are read from the completed -2 cache; no old N projection, W/forcing, old
evaluation, or old normal-form target is rerun. R126's sixteen missing raw
response roots alone are restored and checked against their published hashes.

New full-function relations use the proved R178/R179 common word map and
R159 pure/balanced faithfulness. Computation is Actions-only. Recomputable
data/certificates are not published: emit a bounded summary and hashes only.
"""
from __future__ import annotations
import argparse
from collections import Counter
from fractions import Fraction as F
import json
from math import lcm
import os
from pathlib import Path
import resource
import time

import literature_character_head_minus2 as head
import literature_character_head_literal_relations as literal
import literature_color_priority_words as priority

layer,old,static=head.layer,head.old,head.static
colored,exact,blocks,formal=head.colored,head.exact,head.blocks,head.formal
Field=head.Field
canonical,sha=head.canonical,head.sha
MODES=(-4,-2)
REPOSITORY=head.REPOSITORY
SCHEMA="visible-flex-complete-character-head-zero-v1"
TOPIC=head.TOPIC
R0_KEEP=(0,1,2,3,4,5,7,8,9,10,11,12,13,15,17,19)
FROZEN={
 "head":("literature_character_head_minus2.py",58856,
   "fcc41b4d5a640a1ac411e7f6f29622db81c39cb2be37aed7811136418a045f11"),
 "literal":("literature_character_head_literal_relations.py",58885,
   "80ab553a2dbb35fd4547beaf1b7ad094e831a2cb7f02e4968b867c4654cd9995"),
 "priority":("literature_color_priority_words.py",21642,
   "ec2022d8f9ba764dad05350b6fd2084d0c8fdc4bb9a26550f65f1f95f504a9b9"),
}
R0_INPUT={
 "run":"43649525432","commit":"5852d7d4400859e53dde789b4d63f200d0e0acce",
 "lane":"g_first_translation","schema":"visible-flex-G-first-translation-original-v1",
 "main":{"filename":"G-first-translation.json","bytes":23923,
   "sha256":"9926a1f7026064c95c297b34da60ed5f1b345bc37753a23e75295cf44792fe82"},
 "receipt":{"filename":"receipt.json","bytes":33085,
   "sha256":"06e5d82a7e7db8922d42347920609c83a3ad0114050cdbbdafc72084c3e25bec"},
 "artifact":{"filename":"G-first-translation-complete-report.json.gz",
   "stored_bytes":17734,"stored_sha256":"511431508d58a1b6fe3fb783efe6d9c0b9be9005c86c08796d992ad19441a30b",
   "raw_bytes":74559,"raw_sha256":"4f88bc5fa5af321c57953c1eb7316efbd53d7f4d2da21d2b9c933bcaf617ab45"},
 "metadata_key":"complete_report_file",
 "driver":{"filename":"literature_G_first_translation.py","bytes":26885,
   "sha256":"331fea2c1aef154c4d5866e4708f067c555f9fb61f02a11ee32a7f44d25f01f5"},
}
ZERO=(0,0,0,0)


def source_identity():
    value=head.source_identity()
    value["frozen_head_driver"]=value.pop("driver")
    value["driver"]=static.identity(__file__)
    value["new_complete_head_helpers"]={}
    directory=Path(head.__file__).resolve().parent
    for name,(filename,size,digest) in FROZEN.items():
        found=static.identity(directory/filename)
        if found!={"filename":filename,"bytes":size,"sha256":digest}:
            raise ValueError("frozen complete-head helper changed: "+name)
        value["new_complete_head_helpers"][name]=found
    return value


def geometry_index(key):
    key=tuple(key)+(0,0) if len(key)==8 else tuple(key)
    if len(key)!=10:
        raise ValueError("ten geometry coordinates required")
    return key[0]-key[2]+key[3]+key[5]+key[8]


def check_cached_head(main,data):
    if (data.get("schema")!=head.SCHEMA+"-original-expressions"
        or data.get("github_repository")!=REPOSITORY
        or str(data.get("github_run_id"))!=literal.HEAD["run"]
        or data.get("github_sha")!=literal.HEAD["commit"]
        or data.get("target_weight")!=-2
        or data.get("all_fourteen_families_complete") is not True
        or data.get("all_planned_contractions_present") is not True
        or data.get("planned_contractions")!=78 or data.get("completed_contractions")!=78
        or len(data.get("contraction_plan",[]))!=78
        or len(data.get("cache_records",[]))!=78):
        raise ValueError("complete already-published N projection cache required")
    counts=main.get("contraction_plan",{})
    if (counts.get("declared_requests_before_filtering")!=1139
        or counts.get("exact_zero_projected_requests")!=1057
        or counts.get("distinct_nonzero_projected_inputs")!=78):
        raise ValueError("old complete 1139-request projection coverage changed")
    if sha(canonical(data["contraction_plan"]))!=data.get("contraction_plan_sha256"):
        raise ValueError("old complete contraction plan hash changed")
    if counts.get("sha256")!=data["contraction_plan_sha256"]:
        raise ValueError("published main and complete cache plan differ")
    factor_binding=data.get("input_bindings",{}).get("factors",{})
    if any((factor_binding.get("original_export") or {}).get(k)!=v
           for k,v in head.INPUTS["factors"]["export"].items()):
        raise ValueError("old cache did not consume the same unreduced factor export")


def old_projection_index(data):
    cache={r["token"]:r for r in data["cache_records"]}
    if len(cache)!=78:
        raise ValueError("duplicate archived response-cache token")
    result={}
    for entry in data["contraction_plan"]:
        item=cache.get(entry["token"])
        if (item is None or item["plan_index"]!=entry["plan_index"]
            or item["projected_third_sha256"]!=entry["projected_third_sha256"]):
            raise ValueError("uncompleted old contraction is not an empty input")
        for use in entry["uses"]:
            token=(use["root"],entry["third_weight"])
            found={"input_root":item["projected_input_root"],
                "sha256":entry["projected_third_sha256"],
                "original_sha256":use["original_sha256"],
                "geometry_key":use["geometry_key"],
                "derivative_weight":use["potential_derivative_weight"]}
            if token in result:
                previous=result[token]
                if any(previous[k]!=found[k] for k in found if k!="input_root"):
                    raise ValueError("two archived projections of one raw input differ")
            else:
                result[token]=found
    return result


def selected_potential_metadata(factors):
    rows=factors.get("potential_records",[])
    if Counter(r["geometry_derivative_weight"] for r in rows)!=Counter({0:79,2:93}):
        raise ValueError("complete original N0/N2 coverage changed")
    selected=[r for r in rows if
        (r["geometry_derivative_weight"]==2 and geometry_index(r["geometry_key"]) in (-1,0))
        or (r["geometry_derivative_weight"]==0 and geometry_index(r["geometry_key"]) in (0,1))]
    counts=Counter((r["geometry_derivative_weight"],geometry_index(r["geometry_key"])) for r in selected)
    if counts!=Counter({(0,0):10,(0,1):1,(2,-1):3,(2,0):1}):
        raise ValueError("R190/R192 complete geometric support changed")
    for row in selected:
        if row["geometry_derivative_weight"]==2 and geometry_index(row["geometry_key"])==0:
            if tuple(row["geometry_key"])!=(-2,0,0,2,0,0,0,0,0,0):
                raise ValueError("the unique top N2 key changed")
        if row["geometry_derivative_weight"]==0 and geometry_index(row["geometry_key"])==1:
            if tuple(row["geometry_key"])!=(1,1,0,0,0,0,0,0,0,0):
                raise ValueError("the unique top N0 key changed")
    return selected


def restore_reduced_potential(ring,factors,cache_data,report):
    selected=selected_potential_metadata(factors)
    lookup=old_projection_index(cache_data)
    names=set();descriptors=[];empty=[]
    for row in selected:
        weight=geometry_index(row["geometry_key"])
        token=(row["root"],weight)
        oldrow=lookup.get(token)
        wanted=factors["original_root_sha256"][row["root"]]
        if oldrow is None:
            # The old COMPLETE plan enumerated this exact root and weight:
            # N0 weight 1: old r0; weight 0: old r1/s0.
            # N2 weight -1: old p0/s1; weight 0: old r1/s0.
            empty.append({"root":row["root"],"third_weight":weight,
                "raw_sha256":wanted,"proof":"complete-old-1139-request-plan-exact-empty"})
            continue
        if (oldrow["original_sha256"]!=wanted
            or oldrow["geometry_key"]!=row["geometry_key"]
            or oldrow["derivative_weight"]!=row["geometry_derivative_weight"]):
            raise ValueError("cached projected input is not the same original N factor")
        names.add(oldrow["input_root"])
        descriptors.append((row,weight,oldrow))
    roots=head.subset_decode(ring,cache_data,names)
    out=[]
    for row,weight,bound in descriptors:
        value=roots[bound["input_root"]]
        if not value.terms or ring.digest(value)!=bound["sha256"]:
            raise ValueError("saved third-input original hash changed")
        if any(d!= (("a",1),("b",1),("c",1)) for d in ring.color_degrees(value)):
            raise ValueError("the archived third input lost its typed slots")
        state,jets=head.split_key(row["geometry_key"])
        base={"root":row["root"]+"@"+str(weight),"original_root":row["root"],
            "geometry_derivative_weight":row["geometry_derivative_weight"],
            "third_weight":weight,"state":state,"velocity":jets[:2],
            "factor":F(1),"value":value,"input_sha256":bound["sha256"],
            "archived_input_root":bound["input_root"],"geometry_key":row["geometry_key"]}
        out.append(base)
        if row["geometry_derivative_weight"]==0 and weight==1:
            # R192: (hk-1)*tau_1, with the SAME input and response cache.
            out.append({**base,"root":base["root"]+":reference-subtraction",
                "state":ZERO,"factor":F(-1),"geometry_key":[0]*10})
    report["reused_N_projections"]={"selected_raw_factors":len(selected),
        "nonzero_projected_inputs_read":len(names),"already_proved_exact_empty_inputs":empty,
        "new_N_projections_computed":0,"old_full_response_outputs_recomputed":0,
        "R190_R192_quotient_representative":True,
        "N0_weight_one_reference_constant_retained":True}
    return out


def restore_new_zero_v(ring,grade,factors,report):
    patterns2={(0,0,1,0,0,0):"p",(0,0,0,1,0,0):"q",
        (2,0,0,0,0,0):"q20",(1,1,0,0,0,0):"q11",(0,2,0,0,0,0):"q02"}
    records=factors["local_generator_records"]
    if Counter((r["mode"],r["geometry_derivative_weight"]) for r in records)!=Counter(
        {(-4,2):665,(-2,2):665,(-4,4):1236,(-2,4):1236}):
        raise ValueError("complete v2/v4 coverage changed")
    selected=[];counts=Counter()
    for row in records:
        if geometry_index(row["geometry_key"])!=0:
            continue
        mode,dw=row["mode"],row["geometry_derivative_weight"]
        counts[(mode,dw)]+=1
        state,jets=head.split_key(row["geometry_key"])
        if dw==2:
            tag=patterns2[jets]
        else:
            tag,found=layer.shape(tuple(row["geometry_key"]))
            if tuple(found)!=state:
                raise ValueError("state coordinates changed")
            if tag in ("A_hh","A_hk","A_kk"):
                continue
            if tag=="velocity_quartic_not_consumed":
                tag="q4_"+str(jets[0])
        selected.append((mode,dw,tag,state,row["root"]))
    if counts!=Counter({(-4,2):10,(-2,2):10,(-4,4):4,(-2,4):4}):
        raise ValueError("complete geometric-index-zero v support changed")
    roots=head.subset_decode(ring,factors,[r[-1] for r in selected])
    groups={m:{2:{},4:{}} for m in MODES}
    for mode,dw,tag,state,name in selected:
        terms=groups[mode][dw].setdefault(tag,{})
        if state in terms:
            raise ValueError("duplicate selected raw v state")
        terms[state]=grade.project(roots[name],0)
    report["new_v_projection"]={"target_weight":0,"complete_geometric_support_counts":
        {str(k):v for k,v in counts.items()},"selected_original_roots":len(selected),
        "old_v_producer_or_derivatives_recompiled":False,
        "other_geometric_indices_removed_by_R89_R190_strict_covariance":True}
    return groups


def restore_static_and_W(ring,grade,data,needed_W):
    if Counter(r["mode"] for r in data["local_roots"])!=Counter({-4:197,-2:197}):
        raise ValueError("complete static two-mode coverage changed")
    names=[r["root"] for r in data["local_roots"]]+["W"+str(j) for j in needed_W]
    roots=head.subset_decode(ring,data,names)
    fields={m:{} for m in MODES}
    for row in data["local_roots"]:
        state,jets=head.split_key(row["geometry_key"])
        if any(jets) or state in fields[row["mode"]]:
            raise ValueError("static source geometry changed")
        fields[row["mode"]][state]=grade.project(roots[row["root"]],0)
    W={j:roots["W"+str(j)] for j in needed_W}
    return {m:Field(ring,terms) for m,terms in fields.items()},W


def restore_zero_acceleration(ring,grade,data):
    rows=[r for r in data["family_records"] if 0 in r["profile_weights"]]
    if len(rows)!=1 or rows[0]["family"]!="A_hh" or rows[0]["state_key"]!=[-2,0,0,0]:
        raise ValueError("published complete weight-zero A/H support changed")
    row=rows[0]
    roots=head.subset_decode(ring,data,list(row["roots"].values()))
    result={m:{name:Field(ring) for name in layer.FAMILIES} for m in MODES}
    for mode in MODES:
        result[mode]["A_hh"]=Field(ring,{(-2,0,0,0):
            grade.project(roots[row["roots"][str(mode)]],0)})
    return result


def read_R0_definition(directory,report):
    main,data,binding=literal.consume_bound(directory,R0_INPUT)
    upper=data.get("response_upper_bound",{})
    columns=data.get("all_original_response_columns",[])
    witness=(main.get("checkpoint") or {}).get("dual_certificate",{})
    if (upper.get("retained_original_columns")!=list(R0_KEEP)
        or upper.get("original_columns")!=20
        or upper.get("proved_true_response_dimension_upper_bound")!=16
        or len(upper.get("verified_original_dependencies",[]))!=4
        or len(columns)!=20 or witness.get("modular_control_rank")!=16
        or witness.get("modular_pivot_determinant")!=775740714
        or witness.get("rational_nonmembership_certified") is not True):
        raise ValueError("the completed original R0 basis proof changed")
    if sha(canonical(upper["verified_original_dependencies"]))!="1fc11b2b550b4554021be768ff1db9854c218e8bebb2983709c915b910f08e72":
        raise ValueError("the four old complete original dependencies changed")
    report["inputs"]["R0_definition"]=binding
    return [columns[i] for i in R0_KEEP]


def restore_missing_R0_roots(ring,W,labels,report):
    quadratics=exact.operator_basis(ring)
    result=[]
    for old_index,label in zip(R0_KEEP,labels):
        j=label["third_index"];a=label["quadratic_index"]
        if (not 0<=j<36 or not 0<=a<8
            or label["quadratic_name"]!=exact.PARAMETERS[a]
            or blocks.PARAMETER_WEIGHTS[a]+blocks.THIRD_WEIGHTS[j]!=0):
            raise ValueError("bound old R0 label changed its full E8/W36 scope")
        if ring.digest(W[j])!=label["third_original_sha256"]:
            raise ValueError("old R0 third source changed")
        modes=blocks.full_response(ring,colored.ThirdOperator(ring,W[j]),
            quadratics[label["quadratic_index"]])
        if {str(m):ring.digest(v) for m,v in modes.items()}!=label["original_mode_sha256"]:
            raise ValueError("restored missing R0 raw roots do not match the published originals")
        result.append(modes)
    report["R0_missing_original_restore"]={"restored_response_columns":16,"restored_raw_mode_roots":32,"known_true_dimension":16,
        "old_labels":list(R0_KEEP),"all_old_mode_hashes_matched":True,
        "old_four_dependencies_recomputed":False,"old_normal_forms_recomputed":False,
        "old_profile_evaluations_repeated":False,
        "reason":"R126 stored hashes and rank proof but no portable raw-expression DAG"}
    return result


def make_new_plan(ring,nrows,matrix):
    entries={}
    for row in nrows:
        directions=range(8) if row["geometry_derivative_weight"]==2 else range(3,8)
        for a in directions:
            if row["third_weight"]+blocks.PARAMETER_WEIGHTS[a]!=0:
                continue
            if row["geometry_derivative_weight"]==0 and not matrix[2][a]:
                continue
            token=(a,row["input_sha256"])
            entries.setdefault(token,{"parameter":a,"input":row["value"],
                "input_sha256":row["input_sha256"],"uses":[]})["uses"].append(row["root"])
    if len(entries)>16:
        raise ValueError("R192 declared at-most-sixteen missing contractions exceeded")
    return entries


def subtract_reduced(fields,degree,nrows,nweight,matrix,mweight,cache):
    for row in nrows:
        if row["geometry_derivative_weight"]!=nweight:
            continue
        for a,scalar in enumerate(matrix[mweight]):
            if not scalar or row["third_weight"]+blocks.PARAMETER_WEIGHTS[a]!=0:
                continue
            token=(a,row["input_sha256"])
            if token not in cache:
                raise ValueError("an uncompleted new response must not be silently dropped")
            for (mstate,mvelocity),coefficient in scalar.items():
                velocity=tuple(x+y for x,y in zip(row["velocity"],mvelocity))
                if sum(velocity)!=degree:
                    raise ValueError("new full contraction changed its derivative weight")
                state=tuple(x+y for x,y in zip(row["state"],mstate))
                for mode in MODES:
                    head.add_term(fields[mode][velocity[0]],state,
                        -row["factor"]*coefficient*cache[token][mode])


def assemble(ring,groups,nrows,matrix,coordinates,cache,static_fields,acceleration):
    refs={m:[head.evaluate_field(static_fields[m],s) for s in head.constrained.BASIS_STATES] for m in MODES}
    q2={m:{i:dict(f.terms) for i,f in head.normalize_v2(groups[m][2],ring).items()} for m in MODES}
    q4={m:{i:dict(f.terms) for i,f in head.normalize_v4_quartic(groups[m][4],ring).items()} for m in MODES}
    subtract_reduced(q2,2,nrows,2,matrix,0,cache)
    subtract_reduced(q2,2,nrows,0,matrix,2,cache)
    subtract_reduced(q4,4,nrows,2,matrix,2,cache)
    families={m:{} for m in MODES}
    for mode in MODES:
        f0=static_fields[mode]
        for i,value in enumerate(refs[mode]):
            f0=f0.add(head.scalar_times(head.coefficient_scalar(coordinates[0],i,(0,0)),value),-1)
            for j in range(3):
                field=head.scalar_times(head.coefficient_scalar(coordinates[2],i,(j,2-j)),value)
                for key,term in field.terms.items():
                    head.add_term(q2[mode][j],key,-term)
        if any(head.evaluate_field(f0,s).terms for s in head.constrained.BASIS_STATES):
            raise ValueError("the same eight-reference static normalization changed")
        families[mode]["F0"]=f0
        families[mode].update({"Q2_"+str(i):Field(ring,q2[mode][i]) for i in range(3)})
        families[mode].update(acceleration[mode])
        families[mode].update({"Q4_"+str(i):Field(ring,q4[mode][i]) for i in range(5)})
        if set(families[mode])!=set(head.FAMILIES):
            raise ValueError("all fourteen complete normal families required")
    return families


def list_coefficients(ring,families):
    records=[];values=[];linear={};lin=head.LinearRing()
    for name in head.FAMILIES:
        keys=sorted(set(families[-4][name].terms)|set(families[-2][name].terms))
        terms={}
        for key in keys:
            modes={m:families[m][name].terms.get(key,ring.number(0)) for m in MODES}
            if not any(v.terms for v in modes.values()):
                continue
            i=len(records)
            records.append({"index":i,"family":name,"state_key":list(key),"weight":0,
                "original_mode_sha256":{str(m):ring.digest(v) for m,v in modes.items()}})
            values.append(modes);terms[key]=lin.unit(i)
        linear[name]=Field(lin,terms)
    return records,values,linear


def faithful_parts(ring,modes):
    parts={}
    for mode in MODES:
        terms={}
        for monomial,coefficient in modes[mode].terms.items():
            degree=Counter()
            for atom in monomial[1]:
                degree.update(ring.atom_color_degree(atom))
            if set(degree)-{"q","qbar"} or sum(degree.values())!=4:
                raise ValueError("a canonical column reached a producer-only color or nonquartic term")
            pair=(degree.get("q",0),degree.get("qbar",0))
            if mode==-4 and pair!=(4,0):
                raise ValueError("canonical pure mode is not q degree four")
            if mode==-4 or pair==(2,2):
                terms[monomial]=coefficient
        parts[mode]=exact.Expr(ring,terms)
    return parts


def fraction_rows(row):
    return [[i,str(c)] for i,c in sorted(row.items()) if c]


def joint_function_kernel(ring,columns,args,budget,report):
    mapper=priority.PriorityWords(ring,max_calls=args.max_IBP_calls,max_terms=args.max_terms,
        max_shuffle_entries=args.max_cache_entries,max_cache_entries=args.max_cache_entries)
    dictionary={};basis={};relations=[];converted=[];vectors=[];basis_columns=[]
    for index,modes in enumerate(columns):
        parts=faithful_parts(ring,modes)
        joint={};proof={}
        for mode in MODES:
            word=mapper.expression(parts[mode])
            if not all(priority.is_remainder_letter(letter)
                       for local,letters in word.terms for letter in letters):
                raise ValueError("a produced word lies outside the proved remainder grammar")
            for (local,letters),coefficient in word.terms.items():
                key=(mode,local,letters)
                if key not in dictionary:
                    if len(dictionary)>=args.max_terms:
                        raise literal.Limit("new joint dictionary ceiling")
                    dictionary[key]=len(dictionary)
                joint[dictionary[key]]=coefficient
            proof[str(mode)]={"original_mode_sha256":ring.digest(modes[mode]),
                "faithful_projection_sha256":ring.digest(parts[mode]),
                "representative_sha256":priority.digest(priority.rows(word)),
                "representative_terms":len(word.terms),
                "R178_sound_and_R179_remainder_grammar":True}
        converted.append(proof);vectors.append(joint)
        denominator=1
        for c in joint.values():
            denominator=lcm(denominator,c.denominator)
            budget.check((denominator,))
        vec={j:int(c*denominator) for j,c in joint.items()}
        vec,comb=literal.normalize_integer_pair(vec,{index:denominator})
        budget.check(vec.values());budget.check(comb.values())
        while vec and min(vec) in basis:
            vec,comb=literal.exact_reduce_step(vec,comb,basis,budget)
        if vec:
            pivot=min(vec);basis[pivot]={"vector":vec,"combination":comb}
            basis_columns.append(index)
        else:
            check={}
            for j,c in comb.items():
                literal.add_fraction_row(check,vectors[j],F(c))
            if check:
                raise AssertionError("fresh transported sum of original column identities is nonzero")
            raw_sum={m:sum((F(c)*columns[j][m] for j,c in comb.items()),ring.number(0)) for m in MODES}
            relations.append({"dependent_column":index,"coefficients":fraction_rows(comb),
                "full_original_difference_sha256":{str(m):ring.digest(v) for m,v in raw_sum.items()},
                "full_original_difference_terms":{str(m):len(v.terms) for m,v in raw_sum.items()},
                "both_faithful_word_sums_exact_zero":True})
        if index==15 and len(basis)!=16:
            raise AssertionError("known true R0 basis lost rank in the proved faithful dictionary")
        report["progress"]={"mapped_columns":index+1,"all_columns":len(columns),
            "current_true_rank":len(basis),"proved_original_relations":len(relations)}
        budget.check()
    report["new_common_word_matrix"]={"columns":len(columns),"rank":len(basis),
        "basis_columns":basis_columns,"word_rows":len(dictionary),"complete_kernel_relations":len(relations),
        "conversions_sha256":sha(canonical(converted)),
        "relations_sha256":sha(canonical(relations)),
        "all_columns_and_both_faithful_roots_completed":True,
        "word_dictionary_is_injective_by_R179":True,"old_word_targets_repeated":False,
        "mapper_statistics":mapper.stats}
    return relations,len(basis),converted


def exact_dual_parameterization(rows,dimension,budget):
    echelon={}
    for index,row in enumerate(rows):
        literal.reduce_small(row,echelon,budget,insert=index)
    pivots=sorted(echelon);free=[j for j in range(dimension) if j not in echelon]
    forms=[{} for _ in range(dimension)]
    for j,i in enumerate(free):
        forms[i]={j:F(1)}
    for pivot in reversed(pivots):
        for j,c in echelon[pivot]["row"].items():
            if j!=pivot:
                literal.add_fraction_row(forms[pivot],forms[j],-c)
                budget.check(forms[pivot].values())
    for row in rows:
        check={}
        for j,c in row.items():
            literal.add_fraction_row(check,forms[j],c)
        if check:
            raise AssertionError("new full-head free forms fail an original equation")
    return free,forms,echelon


def compose_form(row,forms):
    out={}
    for j,c in row.items():
        literal.add_fraction_row(out,forms[j],F(c))
    return out


def character_head(records,relations,translation,cref,sref,inverse,budget,rank,report):
    n=len(records);kernel=[]
    for relation in relations:
        row={int(i)-16:F(c) for i,c in relation["coefficients"] if int(i)>=16}
        if not row:
            raise AssertionError("a nontrivial relation used only the proved independent R0 basis")
        kernel.append(row)
    rows=kernel+[dict((int(i),F(c)) for i,c in item["coefficients"]) for item in translation]
    free,forms,echelon=exact_dual_parameterization(rows,n,budget)
    cforms=[];dforms=[]
    for j in range(8):
        c={};d={}
        for i in range(8):
            literal.add_fraction_row(c,dict((int(k),F(v)) for k,v in cref[i]["coefficients"]),inverse[i][j])
            literal.add_fraction_row(d,dict((int(k),F(v)) for k,v in sref[i]["coefficients"]),inverse[i][j])
        cforms.append(compose_form(c,forms));dforms.append(compose_form(d,forms))
    output={
        "normal_records":records,"free_normal_indices":free,
        "normal_coordinates_in_true_head":[fraction_rows(f) for f in forms],
        "static_c_in_true_head":[fraction_rows(f) for f in cforms],
        "static_d_in_true_head":[fraction_rows(f) for f in dforms],
        "positive_character_covariant_multiplier_obstruction_d_p1":fraction_rows(dforms[1]),
        "multiplier_free_parameter_is_not_a_head_coordinate":True,
        "true_U0_dimension":rank,"known_true_R0_dimension":16,
        "true_U0_mod_R0_dimension":rank-16,"true_H0_dimension":len(free),
        "true_translation_image_mod_R0_dimension":rank-16-len(free),
        "all_function_relations_and_same_weight_D_completed":True,
        "full_H0_was_not_pre_restricted_by_positive_covariant_multiplier_conditions":True,
        "positive_character_decided":False,
    }
    if rank-16-len(free)<0 or len(relations)!=n+16-rank:
        raise AssertionError("complete function-kernel and head dimension accounting disagree")
    report["complete_true_weight_zero_head"]=output
    return output


def actual(args,report):
    budget=literal.Budget(args.max_seconds,args.memory_mib,args.integer_bits)
    limits=exact.Limits(seconds=args.max_seconds,nodes=500000,atoms=120000,
        terms=args.max_terms,rewrites=args.max_IBP_calls,memory_mib=args.memory_mib,
        rational_bits=args.integer_bits)
    ring=colored.ColoredRing(limits);grade=blocks.ScalingGrading(ring)
    report["phase"]="bind_existing_complete_inputs"
    _,factors=head.bind_input("factors",args.factors_directory,report)
    hmain,hdata,hbinding=literal.consume_bound(args.cache_directory,literal.HEAD)
    check_cached_head(hmain,hdata);report["inputs"]["completed_N_projection_cache"]=hbinding
    matrix=head.read_matrix(factors)
    nrows=restore_reduced_potential(ring,factors,hdata,report);del hdata,hmain
    groups=restore_new_zero_v(ring,grade,factors,report);del factors
    labels=read_R0_definition(args.R0_directory,report)
    needed_W=sorted({row["third_index"] for row in labels})
    _,sdata=head.bind_input("static",args.static_directory,report)
    static_fields,W=restore_static_and_W(ring,grade,sdata,needed_W);del sdata
    _,adata=head.bind_input("acceleration",args.acceleration_directory,report)
    acceleration=restore_zero_acceleration(ring,grade,adata);del adata
    report["phase"]="restore_only_sixteen_missing_R0_originals"
    responses=restore_missing_R0_roots(ring,W,labels,report);del W
    report["phase"]="new_at_most_sixteen_required_weight_zero_responses"
    plan=make_new_plan(ring,nrows,matrix);quadratics=exact.operator_basis(ring);cache={}
    plan_public=[]
    for (a,digest),entry in sorted(plan.items()):
        value=blocks.full_response(ring,colored.ThirdOperator(ring,entry["input"]),quadratics[a])
        if any(set(grade.split(v))-{0} for v in value.values()):
            raise ValueError("a new full response changed its declared true weight zero")
        cache[(a,digest)]=value
        plan_public.append({"parameter":a,"input_sha256":digest,"uses":sorted(entry["uses"]),
            "full_mode_sha256":{str(m):ring.digest(v) for m,v in value.items()}})
        report["new_contractions_completed"]=len(cache);budget.check()
    report["new_contraction_plan"]={"count":len(plan),"complete":len(cache)==len(plan),
        "sha256":sha(canonical(plan_public)),"entries":plan_public}
    report["phase"]="complete_fourteen_families_and_same_cocycle"
    _,reference=head.constrained.reference_coordinates()
    inverse=[[F(v) for v in row] for row in reference["inverse"]]
    coordinates=head.coordinate_polynomials(matrix,inverse)
    families=assemble(ring,groups,nrows,matrix,coordinates,cache,static_fields,acceleration)
    records,values,linear=list_coefficients(ring,families)
    translation,cref,sref=head.translation_presentation(linear,coordinates,head.constrained.BASIS_STATES)
    report["normal_presentation"]={"complete_fourteen_families":True,
        "records":len(records),"by_family":dict(Counter(r["family"] for r in records)),
        "D_records":len(translation),"true_weight":0,"reduced_mod_R_by_R190_R192":True,
        "same_Gamma_m0_and_Gamma_m2":True,"all_eight_reference_static_values_zero":True,
        "low_D_is_domega_minus_the_same_cocycle":True}
    report["phase"]="new_complete_faithful_word_kernel"
    relations,rank,converted=joint_function_kernel(ring,responses+values,args,budget,report)
    report["phase"]="full_head_quotient_before_any_positive_restriction"
    result=character_head(records,relations,translation,cref,sref,inverse,budget,rank,report)
    # Recomputable certificate exists only in memory. No artifact or repository output.
    certificate={"schema":SCHEMA+"-reproducible-certificate",
        "source_hashes":report["source_hashes"],"input_bindings":report["inputs"],
        "new_contraction_plan":plan_public,"normal_records":records,
        "D_presentation":translation,"reference_c":cref,"reference_d":sref,
        "reference_inverse":reference["inverse"],"conversions":converted,
        "complete_original_relations":relations,"complete_true_head":result}
    raw=canonical(certificate)
    if len(raw)>args.max_certificate_bytes:
        raise literal.Limit("in-memory reproducible certificate byte ceiling")
    report["reproducible_certificate"]={"bytes":len(raw),"sha256":sha(raw),
        "persisted":False,"reproduce_by_same_script_and_parameters":True}
    report.update(completion="complete",phase="complete_true_weight_zero_character_head",
        positive_character_decided=False,period_or_ruling_paid=False,task_complete=False,
        old_N_projections_recomputed=0,old_original_profile_evaluations_repeated=0,
        old_normal_form_targets_recomputed=0,old_3974_generator_recompiled=False,
        new_function_kernel_complete=True,exact_integer_operations=budget.operations,
        maximum_integer_bits=budget.maximum_bits)


def toy_only(args):
    checks={}
    # New support selector: metadata only, never real inputs.
    fake=[]
    for i in range(10):
        fake.append({"root":"s"+str(i),"geometry_derivative_weight":0,
                     "geometry_key":[0,i,0,0,0,0,0,0,0,0]})
    fake.append({"root":"top0","geometry_derivative_weight":0,
                 "geometry_key":[1,1,0,0,0,0,0,0,0,0]})
    for i in range(68):
        fake.append({"root":"lo"+str(i),"geometry_derivative_weight":0,
                     "geometry_key":[-5,i,0,0,0,0,0,0,0,0]})
    fake.append({"root":"top2","geometry_derivative_weight":2,
                 "geometry_key":[-2,0,0,2,0,0,0,0,0,0]})
    for i in range(3):
        fake.append({"root":"n"+str(i),"geometry_derivative_weight":2,
                     "geometry_key":[-3,i,0,2,0,0,0,0,0,0]})
    for i in range(89):
        fake.append({"root":"ln"+str(i),"geometry_derivative_weight":2,
                     "geometry_key":[-6,i,0,2,0,0,0,0,0,0]})
    checks["new_R192_selected_support_15"]=(len(selected_potential_metadata({"potential_records":fake}))==15)
    budget=literal.Budget(30,512,2048)
    free,forms,_=exact_dual_parameterization([{0:F(-2),1:F(1)},{0:F(-4),1:F(2)}],2,budget)
    checks["new_full_head_dual_parameterization_preserves_one_free_coordinate"]=(
        free==[1] and forms==[{0:F(1,2)},{0:F(1)}])
    free2,_,_=exact_dual_parameterization([{0:F(-2),1:F(1)},{0:F(1)}],2,budget)
    checks["new_D_can_kill_the_entire_true_quotient"]=(free2==[])
    limits=exact.Limits(seconds=30,memory_mib=512,terms=6000,rewrites=30000)
    ring=colored.ColoredRing(limits);q=ring.color("q");qb=ring.color("qbar")
    full={-4:q**4,-2:q**3*qb+q*q*qb*qb}
    parts=faithful_parts(ring,full)
    checks["new_joint_projection_keeps_pure_and_balanced"]=(not (parts[-4]-q**4).terms and not (parts[-2]-q*q*qb*qb).terms)
    try:
        faithful_parts(ring,{-4:q**3*qb,-2:q*q*qb*qb})
    except ValueError:
        checks["wrong_canonical_pure_scope_is_rejected"]=True
    else:
        checks["wrong_canonical_pure_scope_is_rejected"]=False
    # Reference subtraction must share the very same response, not negate time.
    nrows=[{"geometry_derivative_weight":0,"third_weight":1,"input_sha256":"toy",
        "state":(1,1,0,0),"velocity":(0,0),"factor":F(1)},
       {"geometry_derivative_weight":0,"third_weight":1,"input_sha256":"toy",
        "state":ZERO,"velocity":(0,0),"factor":F(-1)}]
    matrix={2:[{} for _ in range(8)]}
    matrix[2][6][(ZERO,(2,0))]=F(3)
    fields={m:{0:{},1:{},2:{}} for m in MODES}
    subtract_reduced(fields,2,nrows,0,matrix,2,{(6,"toy"):{m:q**4 for m in MODES}})
    checks["new_N0_hk_minus_one_constant_is_kept"]=all(
        not (fields[m][2][(1,1,0,0)]+3*q**4).terms and not (fields[m][2][ZERO]-3*q**4).terms for m in MODES)
    try:
        subtract_reduced({m:{0:{},1:{},2:{}} for m in MODES},2,nrows,0,matrix,2,{})
    except ValueError:
        checks["missing_new_contraction_is_not_a_proved_R_discard"]=True
    else:
        checks["missing_new_contraction_is_not_a_proved_R_discard"]=False
    # Artificial complete-cache metadata, including harmless extra export fields.
    dummy_plan=[{"token":"toy"+str(i),"plan_index":i,"third_weight":0,
        "projected_third_sha256":"a"*64,"uses":[]} for i in range(78)]
    dummy_records=[{"token":"toy"+str(i),"plan_index":i,
        "projected_third_sha256":"a"*64,"projected_input_root":"input"+str(i)}
        for i in range(78)]
    dummy={"schema":head.SCHEMA+"-original-expressions","github_repository":REPOSITORY,
        "github_run_id":literal.HEAD["run"],"github_sha":literal.HEAD["commit"],
        "target_weight":-2,"all_fourteen_families_complete":True,
        "all_planned_contractions_present":True,"planned_contractions":78,
        "completed_contractions":78,"contraction_plan":dummy_plan,
        "contraction_plan_sha256":sha(canonical(dummy_plan)),"cache_records":dummy_records,
        "input_bindings":{"factors":{"original_export":{
            **head.INPUTS["factors"]["export"],"artificial_extra_metadata":True}}}}
    dummy_main={"contraction_plan":{"declared_requests_before_filtering":1139,
        "exact_zero_projected_requests":1057,"distinct_nonzero_projected_inputs":78,
        "sha256":dummy["contraction_plan_sha256"]}}
    check_cached_head(dummy_main,dummy)
    checks["new_complete_cache_gate_binds_fields_and_allows_extra_metadata"]=True
    try:
        check_cached_head(dummy_main,{**dummy,"completed_contractions":77})
    except ValueError:
        checks["partial_old_cache_never_proves_an_absent_projection_zero"]=True
    else:
        checks["partial_old_cache_never_proves_an_absent_projection_zero"]=False
    use={"root":"artificial_raw","original_sha256":"b"*64,
         "geometry_key":[0]*10,"potential_derivative_weight":0}
    for i in (0,1):
        dummy_plan[i]["uses"]=[dict(use)]
    equal_lookup=old_projection_index(dummy)
    if len(equal_lookup)!=1:
        raise AssertionError("same archived input aliases must not produce extra N projections")
    dummy_plan[1]["projected_third_sha256"]="c"*64
    dummy_records[1]["projected_third_sha256"]="c"*64
    try:
        old_projection_index(dummy)
    except ValueError:
        checks["conflicting_archived_projection_aliases_are_rejected"]=True
    else:
        checks["conflicting_archived_projection_aliases_are_rejected"]=False
    if not all(checks.values()):
        raise AssertionError("new artificial check failed: "+str(checks))
    return {"checks":checks,"all_passed":True,"real_inputs_read":False,
        "old_toy_suites_repeated":False,"research_evaluation_performed":False}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--toy-only",action="store_true")
    parser.add_argument("--output",type=Path,help="optional ephemeral runner file; never publish/upload it")
    for name in ("static","factors","acceleration"):
        parser.add_argument("--"+name+"-directory",type=Path,
            default=TOPIC/"notes"/head.INPUTS[name]["directory"])
    parser.add_argument("--cache-directory",type=Path,
        default=TOPIC/"notes"/"actions-43665345551-1-character_head_minus2")
    parser.add_argument("--R0-directory",type=Path,
        default=TOPIC/"notes"/"actions-43649525432-1-g_first_translation")
    parser.add_argument("--max-seconds",type=float,default=240)
    parser.add_argument("--memory-mib",type=int,default=1024)
    parser.add_argument("--integer-bits",type=int,default=8192)
    parser.add_argument("--max-terms",type=int,default=150000)
    parser.add_argument("--max-IBP-calls",type=int,default=500000)
    parser.add_argument("--max-cache-entries",type=int,default=500000)
    parser.add_argument("--max-summary-bytes",type=int,default=95000)
    parser.add_argument("--max-certificate-bytes",type=int,default=16000000)
    args=parser.parse_args()
    if min(args.max_seconds,args.memory_mib,args.integer_bits,args.max_terms,
           args.max_IBP_calls,args.max_cache_entries,args.max_summary_bytes,
           args.max_certificate_bytes)<=0 or args.max_summary_bytes>=100000:
        parser.error("positive budgets and summary below 100KB required")
    if not args.toy_only and not(os.environ.get("GITHUB_ACTIONS")=="true"
                                 and os.environ.get("GITHUB_REPOSITORY")==REPOSITORY):
        parser.error("actual complete weight-zero research only in this public repository Actions")
    started=time.monotonic()
    report={"schema":SCHEMA,"completion":"started","phase":"source_binding",
        "github_repository":os.environ.get("GITHUB_REPOSITORY"),
        "github_run_id":os.environ.get("GITHUB_RUN_ID"),"github_sha":os.environ.get("GITHUB_SHA"),
        "scope":"complete_weight_zero_head_not_a_single_column",
        "recomputable_artifacts_to_repository_or_release":False}
    code=0
    try:
        report["source_hashes"]=source_identity()
        if args.toy_only:
            report["development"]=toy_only(args);report["completion"]="complete"
            report["phase"]="new_artificial_interfaces_only"
        else:
            actual(args,report)
    except (literal.Limit,formal.CompilationBudgetExceeded,MemoryError) as error:
        report.update(completion="resource_limit",error=str(error),
            new_function_kernel_complete=False,partial_is_not_a_complete_head=True)
        code=2
    except Exception as error:
        report.update(completion="implementation_check_failed",
            error={"type":type(error).__name__,"message":str(error)},
            new_function_kernel_complete=False)
        code=1
    report["elapsed_seconds"]=time.monotonic()-started
    report["peak_rss_mib"]=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1024
    body=canonical(report)+b"\n"
    if len(body)>args.max_summary_bytes:
        # Preserve the complete in-memory mathematical result's identity, not an incomplete claim.
        report={"schema":SCHEMA,"completion":"summary_output_limit",
            "complete_summary_bytes":len(body),"complete_summary_sha256":sha(body),
            "github_run_id":report["github_run_id"],"github_sha":report["github_sha"],
            "source_hashes":report.get("source_hashes"),"no_data_persisted":True,
            "new_function_kernel_complete":False}
        body=canonical(report)+b"\n";code=2
    if len(body)>args.max_summary_bytes:
        raise ValueError("minimal summary exceeds declared byte cap")
    if args.output:
        args.output.parent.mkdir(parents=True,exist_ok=True)
        args.output.write_bytes(body)
    print(body.decode().rstrip(),flush=True)
    print(json.dumps({"summary_bytes":len(body),"summary_sha256":sha(body),
        "repository_or_release_data_publication_permitted":False},sort_keys=True),flush=True)
    raise SystemExit(code)


if __name__=="__main__":
    main()
