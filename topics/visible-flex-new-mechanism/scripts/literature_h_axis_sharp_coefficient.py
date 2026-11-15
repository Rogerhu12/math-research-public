#!/usr/bin/env python3
"""R148/R150: one complete h-axis sharp-action coefficient.

Consume published N2/v4, the completed weight -2 original response block,
and the published J coefficient. Only two missing N2 contractions are new.
The primary target is D0 in both modes; K0=D0+25J/9 is also exported.
A failed sound reduction is only undecided, never a nonmembership claim.
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
import time

import literature_acceleration_layer_mixed as layer

first,static,old=layer.first,layer.static,layer.old
colored,exact,formal,blocks=layer.colored,layer.exact,layer.formal,layer.blocks
canonical,sha=layer.canonical,layer.sha
MODES=(-4,-2)
SCHEMA="visible-flex-h-axis-sharp-coefficient-v1"
REPOSITORY=layer.REPOSITORY
TOPIC=Path(layer.__file__).resolve().parents[1]
LAYER_DRIVER={"filename":"literature_acceleration_layer_mixed.py","bytes":47656,
    "sha256":"271dd150fe95d280fdf3cad0f5bbb5b5fde6f81631a96e7fdbfeb628711ebf7c"}
J_RUN="43654534244"
J_COMMIT="1177f251dc3d9455adf88b585e4c0e4bd6f7e69b"
J_MAIN={"bytes":57753,"sha256":"baccbf48f39a7fb3296ca4e8a933d18f246a8db317423846e66d9c46374b2745"}
J_RECEIPT={"bytes":35241,"sha256":"3c147ca2edaa03d4c27fa0694adca26764c0f98c8fde363387359d8fddccc494"}
J_EXPORT={"filename":"acceleration-layer-mixed-original-expressions.json.gz",
    "stored_bytes":318634,"stored_sha256":"b3227509c891a2e86e9bcc7823e3d6b3abb0a9ff80975b2e1162a0911739146e",
    "raw_bytes":1909429,"raw_sha256":"7c1e0bda999d2c8958d7e5fdf6d9460f30eb6003eb1c69172ba1ca948dfeac38"}
J_HASH={"-4":"2efefe7d9d902bb0050e4f19fc16b09060216c2376530d920ef265ee9ce96ad3",
        "-2":"70f565c5c6d7075ec99bc383fc0ee66e914aff06fbc273bc3c1e431123d7c979"}
RESPONSE_RUN="43653293263"
RESPONSE_COMMIT="2f0add61f44365d713abf836beaa8b0be2806a3d"
RESPONSE_MAIN_SHA="b183b6815e831b989bca6a09ff3da5818462ed613acfd417a704683106992eb3"
RESPONSE_RECEIPT_SHA="a7709ce89ca7ead632a13c14ac0c0a5d906ef34c03f22e499952518c807ee523"
AXIS_PATTERNS={(1,0,1):"beta",(0,2,0):"A",(2,1,0):"C",(4,0,0):"Q"}
ZERO=(0,)*10
N_KEYS={p:(p,0,0,2,0,0,0,0,0,0) for p in (-2,-4)}


def source_identity():
    previous=layer.source_identity()
    if previous.get("driver")!=LAYER_DRIVER:
        raise ValueError("the published normal-acceleration consumer is frozen")
    return {"driver":static.identity(__file__),"published_layer_helpers":previous}


def subset_decode(ring,data,names):
    names=set(names)
    if not names.issubset(data["roots"]) or not names.issubset(data["original_root_sha256"]):
        raise ValueError("missing original root or SHA in the complete export")
    subset={**data,"roots":{k:data["roots"][k] for k in names},
        "original_root_sha256":{k:data["original_root_sha256"][k] for k in names}}
    answer=old.decode_expressions(ring,subset)
    if set(answer)!=names:
        raise ValueError("original-expression subset decoder changed its scope")
    return answer


def axis_v4_record(key):
    if len(key)!=10 or any(not isinstance(x,int) for x in key):
        raise ValueError("complete ten-coordinate geometry key required")
    if any(key[i]<0 for i in range(1,10)):
        raise ValueError("only h has negative Laurent powers")
    # At k=omega=w=b=ell=0 these terms vanish before the h-only derivative.
    if any(key[i] for i in (1,2,4,6,9)):
        return None
    tag=AXIS_PATTERNS.get((key[3],key[5],key[8]))
    if tag is None:
        raise ValueError("unproved h-only geometric weight-four pattern")
    return tag,(key[0],0,0,key[7])


def matrix_axis_check(rows,coordinate_names):
    if tuple(coordinate_names)!=tuple(exact.PARAMETERS) or len(rows)!=8:
        raise ValueError("the eight real matrix coordinates changed")
    found=[]
    for i,entries in enumerate(rows):
        for row in entries:
            key=tuple(row["geometry_key"])
            if row["geometry_derivative_weight"]!=2:
                continue
            if len(key)!=10:
                raise ValueError("raw m2 key is not complete")
            if any(key[j] for j in (1,2,4,5,6,8,9)):
                continue
            if key[3]!=2:
                raise ValueError("raw m2 axis is not quadratic in h_s")
            coefficient=F(row["coefficient"])
            if coefficient:
                found.append((coordinate_names[i],key,coefficient))
    expected=[("r1",(-4,0,0,2,0,0,0,0,0,0),F(1,8)),
              ("t1",(-2,0,0,2,0,0,0,0,0,0),-F(1,8))]
    if sorted(found)!=sorted(expected):
        raise ValueError("published m2 axis differs from the proved two-coordinate identity")
    return {"formula":"m2/u^2 = r1/(8*h^4) - t1/(8*h^2)",
            "original_rational_records":[[name,list(key),str(v)] for name,key,v in found],
            "exact_metadata_identity_verified":True}


def axis_normalized(groups,ring):
    get=lambda tag:layer.StateField(ring,groups.get(tag,{}))
    beta,A,C,Q=(get(tag) for tag in ("beta","A","C","Q"))
    cbar=C.add(beta.X(),-1)
    return A.add(beta,-1),Q.add(cbar.X(),-F(1,3)),cbar


def load_axis_factors(args,ring,report):
    main=layer.read_bound_json(args.factor_report,layer.FACTORS_MAIN)
    receipt=layer.read_bound_json(args.factor_publication,layer.FACTORS_RECEIPT)
    if (main.get("schema")!=layer.factors.SCHEMA or main.get("completion")!="complete"
        or str(main.get("github_run_id"))!=layer.FACTORS_RUN
        or main.get("github_sha")!=layer.FACTORS_COMMIT
        or main.get("source_hashes")!=layer.factors.dependencies()
        or not main.get("factored_L2_and_L4_complete")
        or not main.get("original_v2_v4_both_modes_present")):
        raise ValueError("completed original N2 and v4 producer required")
    metadata=main.get("portable_complete_factor_export") or {}
    if any(metadata.get(k)!=v for k,v in layer.FACTORS_EXPORT.items()):
        raise ValueError("original complete-factor identity changed")
    binding=layer.check_publication(receipt,run=layer.FACTORS_RUN,commit=layer.FACTORS_COMMIT,
        lane="local_fourth_derivative_factors",driver=layer.FACTORS_DRIVER,
        main_name=args.factor_report.name,main_info=layer.FACTORS_MAIN,export_info=metadata)
    data=layer.read_bound_export(args.factor_export,metadata)
    if (data.get("schema")!=layer.factors.SCHEMA+"-original-expressions"
        or data.get("content_scope")!="unreduced-N0-N2-and-complete-two-mode-v2-v4"
        or data.get("source_hashes")!=main["source_hashes"]
        or str(data.get("github_run_id"))!=layer.FACTORS_RUN
        or data.get("github_sha")!=layer.FACTORS_COMMIT
        or data.get("geometry_names")!=list(layer.factors.GEOMETRY_NAMES)
        or not data.get("real_s_derivatives_before_history_zero")
        or data.get("potential_two_assumed_in_W") is not False):
        raise ValueError("complete original factors have different geometry/anchor semantics")
    matrix=matrix_axis_check(data["pointwise_matrix_original_coefficients"],
                             data["pointwise_matrix_coordinate_order"])
    selected=[];names=set();seen=set();counts={m:0 for m in MODES}
    for row in data["local_generator_records"]:
        if row["geometry_derivative_weight"]!=4:
            continue
        mode,key,name=row["mode"],tuple(row["geometry_key"]),row["root"]
        if mode not in counts or (mode,key) in seen or layer.factors.geometry_weight(key)!=4:
            raise ValueError("duplicate or invalid full v4 record")
        seen.add((mode,key));counts[mode]+=1
        selected_axis=axis_v4_record(key)
        if selected_axis is not None:
            tag,state=selected_axis
            selected.append((mode,tag,state,name,key));names.add(name)
    if any(x!=1236 for x in counts.values()):
        raise ValueError("the completed original v4 coverage changed")
    potential={};potential_coverage=0;potential_seen=set()
    for row in data["potential_records"]:
        if row["geometry_derivative_weight"]!=2:
            continue
        key,name=tuple(row["geometry_key"]),row["root"]
        if key in potential_seen or layer.factors.geometry_weight(key)!=2:
            raise ValueError("duplicate or invalid complete N2 state key")
        potential_seen.add(key);potential_coverage+=1
        if any(key[i] for i in (5,6,8,9)) or key[3]+key[4]!=2:
            raise ValueError("unreduced N2 is not a pure velocity quadratic")
        for power,wanted in N_KEYS.items():
            if key==wanted:
                potential[power]=name;names.add(name)
    if potential_coverage!=93:
        raise ValueError("unreduced original N2 coverage changed")
    roots=subset_decode(ring,data,names)
    groups={m:{tag:{} for tag in AXIS_PATTERNS.values()} for m in MODES}
    records=[]
    for mode,tag,state,name,key in selected:
        value=roots[name]
        if state in groups[mode][tag] or any(ring.p.weight(term)!=4 for term in value.terms):
            raise ValueError("axis coefficient has duplicate state or changed profile degree")
        groups[mode][tag][state]=value
        records.append({"mode":mode,"tag":tag,"state_key":list(state),"geometry_key":list(key),
                        "root":name,"original_sha256":ring.digest(value)})
    nvalues={power:roots[potential[power]] if power in potential else ring.number(0)
             for power in N_KEYS}
    for value in nvalues.values():
        if any(x!=(("a",1),("b",1),("c",1)) for x in ring.color_degrees(value)):
            raise ValueError("unreduced N2 lost the actual outer/inner profile slots")
    normal={mode:axis_normalized(groups[mode],ring) for mode in MODES}
    report["factor_input"]={"publication":binding,"main":layer.FACTORS_MAIN,
        "receipt":layer.FACTORS_RECEIPT,"complete_export":metadata,
        "completed_v4_records_by_mode":{str(k):v for k,v in counts.items()},
        "completed_N2_records":potential_coverage,"selected_axis_records":records,
        "selected_N2_records":[{"h_power":p,"geometry_key":list(N_KEYS[p]),
            "root":potential.get(p),"absent_complete_record_means_exact_zero":p not in potential,
            "original_sha256":ring.digest(nvalues[p])} for p in sorted(nvalues)],
        "raw_matrix_axis":matrix,"original_s_derivatives_not_recomputed":True,
        "N2_reduced_mod_W":False,"old_forcing_or_potential_recompiled":False,
        "all_selected_original_hashes_verified":True}
    return normal,nvalues


def load_J(args,ring,report):
    main=layer.read_bound_json(args.J_report,J_MAIN)
    receipt=layer.read_bound_json(args.J_publication,J_RECEIPT)
    checkpoint=main.get("checkpoint") or {}
    metadata=checkpoint.get("portable_acceleration_expression_export") or {}
    witness=checkpoint.get("dual_certificate") or {}
    if (main.get("schema")!=layer.SCHEMA or main.get("completion")!="complete"
        or str(main.get("github_run_id"))!=J_RUN or main.get("github_sha")!=J_COMMIT
        or main.get("source_hashes")!=layer.source_identity()
        or checkpoint.get("candidate_id")!=0 or checkpoint.get("requested_weight")!=-2
        or checkpoint.get("candidate_aliases")!=[{"family":"A_hh","state_key":[-4,0,0,0]}]
        or checkpoint.get("original_target_sha256")!=J_HASH
        or not checkpoint.get("outside_complete_R8_plus_G_orbit_at_this_weight")
        or not witness.get("rational_nonmembership_certified")
        or witness.get("control_columns")!=41 or witness.get("modular_control_rank")!=41
        or not witness.get("modular_augmented_determinant")
        or any(metadata.get(k)!=v for k,v in J_EXPORT.items())):
        raise ValueError("the exact published J independence certificate is required")
    binding=layer.check_publication(receipt,run=J_RUN,commit=J_COMMIT,
        lane="acceleration_layer_mixed",driver=LAYER_DRIVER,
        main_name=args.J_report.name,main_info=J_MAIN,export_info=metadata)
    data=layer.read_bound_export(args.J_export,metadata)
    if (data.get("schema")!=layer.SCHEMA+"-original-expressions"
        or data.get("content_scope")!="five-complete-two-mode-normal-acceleration-families"
        or data.get("source_hashes")!=main["source_hashes"]
        or str(data.get("github_run_id"))!=J_RUN or data.get("github_sha")!=J_COMMIT
        or data.get("selected_weight")!=-2):
        raise ValueError("published J original expression has changed identity")
    found=[x for x in data["selected_weight_records"] if x["id"]==0]
    if len(found)!=1 or found[0]["aliases"]!=checkpoint["candidate_aliases"] or found[0]["original_mode_sha256"]!=J_HASH:
        raise ValueError("published J selected-record binding failed")
    names=found[0]["roots"]
    roots=subset_decode(ring,data,names.values())
    result={m:roots[names[str(m)]] for m in MODES}
    if {str(m):ring.digest(v) for m,v in result.items()}!=J_HASH:
        raise ValueError("published J original mode hash mismatch")
    report["J_input"]={"publication":binding,"main":J_MAIN,"receipt":J_RECEIPT,
        "complete_export":metadata,"candidate_id":0,"original_mode_sha256":J_HASH,
        "already_proved_independent_of_old_41":True,"old_raw_separation_repeated":False}
    return result,checkpoint["response_input"]


def compose_axis_target(ring,normal,nvalues,J,report):
    basis=exact.operator_basis(ring)
    calls=[];responses={}
    for power,name in ((-2,"r1"),(-4,"t1")):
        value=nvalues[power]
        if value.terms:
            responses[name]=blocks.full_response(ring,colored.ThirdOperator(ring,value),
                                                  basis[exact.PARAMETERS.index(name)])
            calls.append(name)
        else:
            responses[name]=blocks.mode_zero(ring)
    correction={m:responses["r1"][m]/8-responses["t1"][m]/8 for m in MODES}
    ungraded={m:normal[m][1].terms.get((-6,0,0,0),ring.number(0))-correction[m] for m in MODES}
    grade=blocks.ScalingGrading(ring)
    D={m:grade.project(value,-2) for m,value in ungraded.items()}
    K={m:D[m]+F(25,9)*J[m] for m in MODES}
    # This is a direct check between two already specified constructions of J,
    # not a new membership or an old modular calculation.
    axis_J={m:normal[m][0].terms.get((-4,0,0,0),ring.number(0)) for m in MODES}
    if any((axis_J[m]-J[m]).terms for m in MODES):
        raise ValueError("actual axis A-beta does not reproduce the bound original J")
    report["axis_target"]={"primary_target":"D0", "derived_target":"K0=D0+25*J/9",
        "complete_formula":"[h^-6 log(h)^0] (Q-(C-beta_h)_h/3-B_m2(N2)), then true weight -2",
        "matrix_contraction":"B_r1(N2[h^-2*u^2])/8 - B_t1(N2[h^-4*u^2])/8",
        "new_response_compositions":len(calls),"new_response_coordinates":calls,
        "complete_outer_inner_slots_preserved":True,"both_modes_share_same_target":True,
        "N2_assumed_in_W":False,"log_chain_rule_performed_before_coefficient_selection":True,
        "axis_J_matches_published_original_exactly":True,
        "ungraded_weights":{str(m):sorted(grade.split(value)) for m,value in ungraded.items()},
        "original_D0_sha256":{str(m):ring.digest(v) for m,v in D.items()},
        "original_K0_sha256":{str(m):ring.digest(v) for m,v in K.items()},
        "remaining_L4_or_other_axes_computed":False}
    named={"N2_axis_hm2":nvalues[-2],"N2_axis_hm4":nvalues[-4]}
    for m in MODES:
        named.update({f"D0_{m}":D[m],f"K0_{m}":K[m],f"axis_ungraded_{m}":ungraded[m],
            f"new_response_r1_{m}":responses["r1"][m],f"new_response_t1_{m}":responses["t1"][m]})
    return D,K,named


def save_originals(args,ring,named,report):
    path=args.output.with_name(args.output.stem+"-original-expressions.json.gz")
    info={"filename":path.name,"persisted":False,"mathematical_status_independent":True}
    report["portable_axis_expression_export"]=info
    data={"schema":SCHEMA+"-original-expressions",
        "content_scope":"one-complete-h-axis-D0-K0-and-two-unreduced-N2-contractions",
        "github_repository":report["github_repository"],"github_run_id":report["github_run_id"],
        "github_sha":report["github_sha"],"source_hashes":report["source_hashes"],
        "axis_target":report["axis_target"],"factor_input":report["factor_input"],
        "J_input":report["J_input"],"old_response_roots_repeated":False,
        **old.serialize_expressions(ring,named)}
    raw=canonical(data);packed=gzip.compress(raw,mtime=0)
    info.update({"stored_bytes":len(packed),"stored_sha256":sha(packed),"raw_bytes":len(raw),
        "raw_sha256":sha(raw),"root_count":len(named),"profile_atom_count":len(data["profile_atoms"]),
        "content_scope":data["content_scope"]})
    if len(packed)>args.max_export_bytes or len(raw)>layer.MAX_RAW_INPUT:
        info["reason"]="supplemental original-expression budget; completed target status retained"
        return
    path.parent.mkdir(parents=True,exist_ok=True);path.write_bytes(packed);info["persisted"]=True


def study(args,report):
    limits=exact.Limits(args.max_seconds,500000,100000,120000,500000,args.memory_mib,8192)
    ring=colored.ColoredRing(limits)
    report["phase"]="read_only_published_axis_v4_and_two_unreduced_N2_roots"
    normal,nvalues=load_axis_factors(args,ring,report)
    report["phase"]="consume_published_J_original_and_its_true_independence"
    J,j_old_response=load_J(args,ring,report)
    report["phase"]="only_two_new_N2_axis_response_contractions"
    D,K,named=compose_axis_target(ring,normal,nvalues,J,report)
    save_originals(args,ring,named,report)
    report["phase"]="read_only_completed_weight_minus_two_original_responses"
    controls,labels=layer.load_response_block(args,ring,report)
    if (len(controls)!=41 or report["response_input"]["weight"]!=-2
        or report["response_input"]["completed_G_outcome"]!="nonmember_certified"
        or j_old_response["retained_original_control_labels"]!=report["response_input"]["retained_original_control_labels"]
        or j_old_response["publication"]!=report["response_input"]["publication"]):
        raise ValueError("new comparison columns do not match the published J certificate")
    controls.append(J);labels.append({"role":"published_J","candidate_id":0,"original_mode_sha256":J_HASH})
    report["comparison_space"]={"true_dimension":42,"prior_R8_dimension":40,
        "prior_orbit_order":3,"J_column":41,"same_real_coefficients_for_both_modes":True,
        "original_column_labels":labels,"old_responses_reconstructed":False,
        "old_dependencies_or_modular_matrices_recomputed":False}
    report["phase"]="one_complete_D0_sound_membership_in_existing_42_dimensional_space"
    normalizer=colored.ColoredNormalizer(ring)
    vectors=[colored.vector_from_modes(value,normalizer) for value in controls]
    span=colored.JointSpan(vectors,limits)
    if len(span.independent)!=42:
        raise ValueError("sound representative rank contradicts the bound original 42-dimensional certificate")
    vector=colored.vector_from_modes(D,normalizer)
    coefficients,remainder=span.reduce(vector)
    report["word_remainder"]={"terms":len(remainder),"sha256":colored.vector_digest(remainder),
        "nonmembership_inferred":False}
    report["representative_candidate_coefficients"]=[[i,str(v)] for i,v in sorted(coefficients.items())]
    if not remainder:
        fresh=first.fresh_zero(ring,D,controls,coefficients)
        c=coefficients.get(41,F(0));sharp=c+F(25,9)
        report["checkpoint"]={"outcome":"complete_original_D0_identity_verified",
            "original_D0_sha256":report["axis_target"]["original_D0_sha256"],
            "same_real_coefficients_for_both_modes":[[i,str(v)] for i,v in sorted(coefficients.items())],
            "fresh_original_checks":fresh,"coefficient_of_J":str(c),
            "sharp_K0_coefficient_mod_R8_and_G_orbit":str(sharp),
            "sharp_coefficient_sign":-1 if sharp<0 else 1 if sharp>0 else 0,
            "weight_minus_two_positive_character_forced_to_kill_J":sharp<0,
            "all_general_positive_functionals_forced_to_kill_J":False,
            "actual_signed_J_control_proved":False,"full_cost_cone_or_ruling_paid":False}
    else:
        report["checkpoint"]={"outcome":"undecided_sound_remainder",
            "original_D0_sha256":report["axis_target"]["original_D0_sha256"],
            "word_remainder":report["word_remainder"],"rational_nonmembership_certified":False,
            "weight_minus_two_positive_character_forced_to_kill_J":False,
            "actual_signed_J_control_proved":False,"full_cost_cone_or_ruling_paid":False}
    report["completion"]="complete";report["phase"]="complete"


def small_toy():
    limits=exact.Limits(30,10000,5000,10000,10000,256,8192)
    ring=colored.ColoredRing(limits)
    q,qb=ring.color("q"),ring.color("qbar");phi=q*q*qb*qb
    checks={}
    def field(rows): return layer.StateField(ring,rows)
    def eq(a,b,name):
        if (a-b).terms: raise AssertionError(name)
        checks[name]=True
    beta=field({(-4,0,0,1):phi})
    groups={"beta":beta.terms,"A":beta.terms,"C":beta.X().terms,"Q":{}}
    A,Q,_=axis_normalized(groups,ring)
    if A.terms or Q.terms: raise AssertionError("D_s(beta*u*a) must cancel in both normal coefficients")
    checks["complete_third_jet_total_derivative_removed"]=True
    v=field({(-5,0,0,2):phi})
    A,Q,_=axis_normalized({"C":v.scale(3).terms,"Q":v.X().terms},ring)
    if A.terms or Q.terms: raise AssertionError("D_s(v*u^3) must cancel")
    checks["complete_cubic_velocity_total_derivative_removed"]=True
    _,Q,_=axis_normalized({"beta":beta.terms},ring)
    eq(Q.terms[(-6,0,0,0)],-3*phi,"log_derivative_constant_term_kept")
    _,Q,_=axis_normalized({"Q":{(-6,0,0,0):7*phi},"C":{(-5,0,0,0):5*phi},
                          "beta":{(-4,0,0,0):3*phi}},ring)
    eq(Q.terms[(-6,0,0,0)],F(106,3)*phi,"five_thirds_and_twenty_thirds_axis_signs")
    for pattern,tag in AXIS_PATTERNS.items():
        key=[0]*10;key[0]=-4;key[7]=2
        key[3],key[5],key[8]=pattern
        if axis_v4_record(tuple(key))!=(tag,(-4,0,0,2)): raise AssertionError("axis classifier")
    checks["all_four_axis_patterns_keep_log_state"]=True
    key=(-4,1,0,1,0,0,0,0,1,0)
    if axis_v4_record(key) is not None: raise AssertionError("nonaxis state leaked")
    checks["positive_k_state_is_excluded_only_before_h_derivatives"]=True
    try: axis_v4_record((0,0,0,0,0,0,0,0,2,0))
    except ValueError: checks["unproved_axis_jet_pattern_rejected"]=True
    else: raise AssertionError("invalid pattern accepted")
    rows=[[] for _ in range(8)]
    for name,p,vv in (("r1",-4,F(1,8)),("t1",-2,-F(1,8))):
        rows[exact.PARAMETERS.index(name)].append({"geometry_key":[p,0,0,2,0,0,0,0,0,0],
            "geometry_derivative_weight":2,"coefficient":str(vv)})
    matrix_axis_check(rows,list(exact.PARAMETERS));checks["two_exact_axis_matrix_entries"]=True
    damaged=copy.deepcopy(rows);damaged[exact.PARAMETERS.index("t1")][0]["coefficient"]="1/8"
    try: matrix_axis_check(damaged,list(exact.PARAMETERS))
    except ValueError: checks["wrong_N2_contraction_sign_rejected"]=True
    else: raise AssertionError("wrong sign accepted")
    eq(Q.terms[(-6,0,0,0)]-2*phi/8+3*phi/8,
       (F(106,3)+F(1,8))*phi,"unreduced_two_N2_contraction_orientation")
    a,b,c=(ring.color(x) for x in ("a","b","c"))
    template=a.D()*b*c+a*(b.D()*c+b*c.D())/3
    third=colored.ThirdOperator(ring,template)
    quadratic=lambda x,y:x.D()*y.D()+x*y
    response=blocks.full_response(ring,third,quadratic)
    reference=blocks.reference_response(ring,third,quadratic)
    for mode in MODES:
        eq(response[mode],reference[mode],"artificial_nonsymmetric_outer_slot_mode_"+str(mode))
    portable=old.serialize_expressions(ring,{"N":template,"D0":response[-2]})
    decoded=old.decode_expressions(ring,portable)
    eq(decoded["N"],template,"portable_exterior_inner_slots_preserved")
    eq(decoded["D0"],response[-2],"portable_complete_mixed_mode_preserved")
    return {"checks":checks,"all_passed":all(checks.values()),
        "published_inputs_read":False,"research_expression_evaluated":False,
        "real_N2_contractions_constructed":False,"old_response_block_read":False}


def write_reports(args,report):
    args.output.parent.mkdir(parents=True,exist_ok=True)
    raw=canonical(report);packed=gzip.compress(raw,mtime=0)
    full=args.output.with_name(args.output.stem+"-complete-report.json.gz")
    metadata=report.get("portable_axis_expression_export") or {}
    used=metadata.get("stored_bytes",0) if metadata.get("persisted") else 0
    full_info={"filename":full.name,"stored_bytes":len(packed),"stored_sha256":sha(packed),
        "raw_bytes":len(raw),"raw_sha256":sha(raw),"persisted":False}
    if len(packed)<=args.max_full_report_bytes and used+len(packed)+args.max_main_bytes<=static.TOTAL_BYTES:
        full.write_bytes(packed);full_info["persisted"]=True
    compact={k:report[k] for k in ("schema","completion","phase","github_repository","github_run_id",
        "github_sha","source_hashes","scope","limits","elapsed_seconds","peak_rss_mib") if k in report}
    for key in ("toy","error","checkpoint","factor_input","J_input","axis_target",
                "portable_axis_expression_export","word_remainder","consumed_control_summary"):
        if key in report: compact[key]=report[key]
    compact["complete_report_file"]=full_info
    compact["all_old_forcing_and_response_compilers_skipped"]=True
    compact["all_general_positive_functionals_or_ruling_paid"]=False
    data=canonical(compact)
    if len(data)>args.max_main_bytes:
        # Do not discard a mathematical certificate merely because diagnostics grew.
        for key in ("factor_input","J_input","consumed_control_summary"):
            value=compact.pop(key,None)
            if value is not None:
                compact[key+"_in_complete_report"]={"sha256":sha(canonical(value))}
        data=canonical(compact)
    if len(data)>args.max_main_bytes or not full_info["persisted"]:
        compact["report_storage_limit"]=True
        compact["mathematical_completion_before_storage"]=report.get("completion")
        if len(data)>args.max_main_bytes:
            compact={k:compact[k] for k in ("schema","completion","phase","github_repository",
                "github_run_id","github_sha","checkpoint","complete_report_file",
                "portable_axis_expression_export") if k in compact}
            compact["report_storage_limit"]=True
        data=canonical(compact)
    if len(data)>=100000: raise ValueError("compact main exceeded the repository small-text limit")
    args.output.write_bytes(data+b"\n")
    return {"output":str(args.output),"completion":report["completion"],
        "bytes":len(data)+1,"sha256":sha(data+b"\n"),"complete_report":full_info,
        "report_storage_limit":compact.get("report_storage_limit",False)}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--toy-only",action="store_true")
    parser.add_argument("--output",type=Path,required=True)
    parser.add_argument("--factor-report",type=Path,default=layer.FACTORS_DIR/"local-fourth-derivative-factors.json")
    parser.add_argument("--factor-publication",type=Path,default=layer.FACTORS_DIR/"receipt.json")
    parser.add_argument("--factor-export",type=Path,default=layer.FACTORS_DIR/layer.FACTORS_EXPORT["filename"])
    rdir=TOPIC/("notes/actions-"+RESPONSE_RUN+"-1-g_translation_successor")
    parser.add_argument("--response-report",type=Path,default=rdir/"G-third-translation.json")
    parser.add_argument("--response-publication",type=Path,default=rdir/"receipt.json")
    parser.add_argument("--response-export",type=Path,default=rdir/"G-third-translation-original-expressions.json.gz")
    jdir=TOPIC/("notes/actions-"+J_RUN+"-1-acceleration_layer_mixed")
    parser.add_argument("--J-report",type=Path,default=jdir/"acceleration-layer-mixed.json")
    parser.add_argument("--J-publication",type=Path,default=jdir/"receipt.json")
    parser.add_argument("--J-export",type=Path,default=jdir/J_EXPORT["filename"])
    parser.add_argument("--max-seconds",type=float,default=180)
    parser.add_argument("--memory-mib",type=int,default=1024)
    parser.add_argument("--max-main-bytes",type=int,default=90000)
    parser.add_argument("--max-full-report-bytes",type=int,default=2000000)
    parser.add_argument("--max-export-bytes",type=int,default=2500000)
    args=parser.parse_args()
    if min(args.max_seconds,args.memory_mib,args.max_main_bytes,args.max_full_report_bytes,args.max_export_bytes)<=0:
        parser.error("positive bounded resources required")
    if args.max_main_bytes>=100000 or args.max_main_bytes+args.max_full_report_bytes+args.max_export_bytes>static.TOTAL_BYTES:
        parser.error("main and total artifact reservations exceed their bounds")
    if not args.toy_only and not(os.environ.get("GITHUB_ACTIONS")=="true" and os.environ.get("GITHUB_REPOSITORY")==REPOSITORY):
        parser.error("real original-coefficient consumption only in this public repository Actions")
    # The comparison block is fixed; paths may change, identities may not.
    args.response_report_sha256=RESPONSE_MAIN_SHA
    args.response_publication_sha256=RESPONSE_RECEIPT_SHA
    args.response_run=RESPONSE_RUN;args.response_commit=RESPONSE_COMMIT
    args.response_lane="g_translation_successor";args.response_order=3
    started=time.monotonic()
    report={"schema":SCHEMA,"completion":"started","phase":"source_binding",
        "github_repository":os.environ.get("GITHUB_REPOSITORY"),"github_run_id":os.environ.get("GITHUB_RUN_ID"),
        "github_sha":os.environ.get("GITHUB_SHA"),"source_hashes":{},
        "scope":"one full two-mode D0 in the h axis; no actual negative/positive cost claim",
        "limits":{"seconds":args.max_seconds,"memory_soft_polling_mib":args.memory_mib,
            "main_bytes":args.max_main_bytes,"full_report_bytes":args.max_full_report_bytes,
            "new_original_export_bytes":args.max_export_bytes,"total_bytes":static.TOTAL_BYTES}}
    code=0
    try:
        report["source_hashes"]=source_identity()
        if args.toy_only:
            report["phase"]="new_artificial_h_axis_IBP_and_two_slot_contraction_checks"
            report["toy"]=small_toy();report["completion"]="toy_passed"
        else:
            study(args,report)
    except formal.CompilationBudgetExceeded as error:
        report["completion"]="resource_limit";report["error"]=str(error);code=2
    except Exception as error:
        report["completion"]="implementation_check_failed"
        report["error"]={"type":type(error).__name__,"message":str(error)};code=1
    if "comparison_space" in report:
        report["consumed_control_summary"]={"true_dimension":42,"R8":40,"G_order":3,"J":1,
            "original_column_labels_sha256":sha(canonical(report["comparison_space"]["original_column_labels"])),
            "complete_labels_in_full_report":True,"old_response_compositions_rebuilt":False}
    report["elapsed_seconds"]=time.monotonic()-started
    report["peak_rss_mib"]=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1024
    result=write_reports(args,report)
    if result["report_storage_limit"]: code=2
    print(json.dumps(result),flush=True)
    return code

if __name__=="__main__":
    raise SystemExit(main())

