#!/usr/bin/env python3
"""Independent R723 complete directional-flow closed/phase/grip evidence.

Read the entire same-field accurate geometry and original normal32/radial/
whole-circle closure. Reuse the pinned complete 002eb source for all physical
ports, target-image boxes, grip, source/input binding and domain re-reading.
The R723 branch does not require an old R650 target or eight-role certificate.
No new F/J/root/integrand, finite sample, model or scientific field is made.
All derived sidecars remain conditional on this final complete main report.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as F
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import subprocess
import sys
import time
import uuid

SCHEMA = "actual-fixed-fejer-R723-directional-closed-phase-grip-evidence-v1"
TOPIC = "topics/visible-flex-larger-amplitude"
PARENT = ("fixed_fejer_meridian_batched_producer_R722_closed_phase_grip_evidence.py",
    "002eb1b91c99ea212255d14a4e929e876e09f34c38c78ffb7fc4f806b8799c5f")
GEOMETRY = ("fixed_fejer_meridian_batched_producer_R722_continuous_gram_curvature_support.py",
    "6c57f78a9c8b80805e8e551a8fba50a089687cea164bd192c8bead845dda29b4")
BRIDGE = ("fixed_fejer_meridian_batched_producer_R722_complete_geometry_support_beta_bridge.py",
    "c6b07b17ba9c25985faae62cd5db0991cd27bc4927d22fdd9e56a6c5ac7ae4e1")
BETA = ("same_field_positive_support_parameter.py",
    "e0b44e22fa9e41109ccdeb1c3908aeca60c5c4a18f90dca088f8c9e0243b5991")
R723 = (TOPIC+"/results/R723-directional-normal-flow-support-reach.md",
    "0edbd1039706186d07412a53c8e5c10411c5966dc36e38a7a504cf923d43e7eb")
FLOW_LOG_TERMS = 32
FLOW_EXP_TERMS = 32
FLOW_BINARY_BITS = 96
GRIP_RADIUS = F(9,20)
MARK_HEIGHT = F(1,1000)
CAP_GRADIENT_SQUARED = F(1,400)
CAP_G = F(1,100)
CAP_D_PLUS = F(801,800)
CAP_D_MINUS = F(1281599,1280000)
CAP_K = F(5)
REACH_RATIO = F(3,100)
DIRECTIONAL_ROLES = (
    "same_accurate_field_and_complete_source_binding",
    "whole_normal32_sixjet_radial_circle_cover",
    "closed_C2_sphere_and_exact_all_phase_family",
    "common_directional_support_actual_curvature_and_diameter",
    "complete_fixed_marked_caps_and_oriented_lower_extension",
)

def require_actions():
    if (os.environ.get("GITHUB_ACTIONS") != "true"
            or os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public"):
        raise RuntimeError("All complete bound consumption runs only in public repository Actions")


def sha(path):
    result=hashlib.sha256()
    with Path(path).open("rb") as stream:
        for block in iter(lambda:stream.read(1<<20),b""):
            result.update(block)
    return result.hexdigest()


def canonical(value):
    return hashlib.sha256(json.dumps(value,sort_keys=True,separators=(",",":"),
        allow_nan=False).encode()).hexdigest()


def encoded(value):
    if isinstance(value,F):
        return str(value)
    if isinstance(value,dict):
        return {str(key):encoded(item) for key,item in value.items()}
    if isinstance(value,(list,tuple)):
        return [encoded(item) for item in value]
    return value


def load(path, expected, name):
    path=Path(path).resolve()
    if sha(path)!=expected:
        raise ValueError("The whole closed-family dependency changed: "+str(path))
    spec=importlib.util.spec_from_file_location(name,path)
    module=importlib.util.module_from_spec(spec)
    sys.modules[name]=module
    spec.loader.exec_module(module)
    if Path(module.__file__).resolve()!=path or sha(path)!=expected:
        raise ValueError("A complete source changed during import")
    return module,path


def execution(repo):
    source=subprocess.check_output(["git","rev-parse","HEAD"],cwd=repo,text=True).strip()
    result=dict(platform="GitHub Actions",repository=os.environ["GITHUB_REPOSITORY"],
        run_id=os.environ["GITHUB_RUN_ID"],attempt=int(os.environ["GITHUB_RUN_ATTEMPT"]),
        source_commit=source)
    if (len(source)!=40 or any(v not in "0123456789abcdef" for v in source)
            or not result["run_id"].isdigit() or result["attempt"]<1):
        raise ValueError("Retain the actual public execution and checkout identity")
    return result


def write_json(path, value, r, outputs, *, replace=False):
    path=Path(path).resolve()
    if not replace and path.exists():
        raise ValueError("An immutable generated evidence object already exists: "+str(path))
    path.parent.mkdir(parents=True,exist_ok=True)
    raw=(json.dumps(encoded(value),sort_keys=True,indent=2,allow_nan=False)+"\n").encode()
    if replace:
        tmp=path.with_name(path.name+".partial-"+uuid.uuid4().hex)
        with tmp.open("xb") as handle:
            handle.write(raw)
        os.replace(tmp,path)
    else:
        with path.open("xb") as handle:
            handle.write(raw)
    record=r.file_record(path)
    if not replace:
        outputs.verify(record)
    return record




def pair(value, name):
    if not isinstance(value,(list,tuple)) or len(value)!=2:
        raise ValueError("A complete finite rational enclosure is required: "+name)
    lo,hi=F(value[0]),F(value[1])
    if lo>hi:
        raise ArithmeticError("An enclosure is reversed: "+name)
    return lo,hi


def p_add(a,b):
    return a[0]+b[0],a[1]+b[1]


def p_sub(a,b):
    return a[0]-b[1],a[1]-b[0]


def p_mul(a,b):
    values=(a[0]*b[0],a[0]*b[1],a[1]*b[0],a[1]*b[1])
    return min(values),max(values)


def p_scale(a,t):
    t=F(t)
    return p_mul(a,(t,t))


def p_square(a):
    lo,hi=a
    return (F(0) if lo<=0<=hi else min(lo*lo,hi*hi),
        max(lo*lo,hi*hi))


def p_intersect(a,b,name):
    result=max(a[0],b[0]),min(a[1],b[1])
    if result[0]>result[1]:
        raise ArithmeticError("Independent same-field enclosures disagree: "+name)
    return result


def directional_leaf(item,row,tau):
    """Exact rational interval operations on ALL persisted F/N/w components."""
    body=item["whole_cell_geometry"]
    position=body["position_hull"]
    normals=body["same_field_normal"]
    if len(position)!=3 or len(normals)!=3:
        raise ValueError("Retain every physical position and normal component")
    f=[pair(x,"F") for x in position]
    n=[pair(x,"N") for x in normals]
    w=pair(body["normal_norm"],"normal norm")
    if w[0]<=0 or w[1]!=F(row["normal_norm_upper"]) or w[0]!=F(row["normal_norm_lower"]):
        raise ArithmeticError("The entire same-field normal must be strictly positive")
    support=body["support"]
    a_saved=pair(support["horizontal_numerator"],"horizontal numerator")
    b_saved=pair(support["vertical_numerator"],"vertical numerator")
    if a_saved[0]!=F(row["a_lower"]) or b_saved[0]!=F(row["b_lower"]):
        raise ValueError("The original support row and its whole leaf disagree")
    a=p_intersect(a_saved,p_add(p_mul(f[0],n[0]),p_mul(f[1],n[1])),"Fxy dot Nxy")
    b=p_intersect(b_saved,p_mul(f[2],n[2]),"Fz Nz")
    qh=p_add(p_square(n[0]),p_square(n[1]))
    qv=p_square(n[2])
    total=p_intersect(p_add(qh,qv),p_square(w),"normal squared")
    total=p_intersect(total,pair(body["squared_normal_lagrange_intersection"],
        "same-field Lagrange determinant"),"normal/Gram determinant")
    qh=p_intersect(qh,p_sub(total,qv),"horizontal normal square")
    qv=p_intersect(qv,p_sub(total,qh),"vertical normal square")
    qh=p_intersect(qh,(F(0),qh[1]),"nonnegative horizontal square")
    qv=p_intersect(qv,(F(0),qv[1]),"nonnegative vertical square")
    c0=p_sub(p_mul(w,a),p_scale(qh,tau))
    c1=p_sub(p_mul(w,b),p_scale(qv,tau))
    return dict(id=row["id"],source_complete_geometry_item_sha256=canonical(item),
        original_geometry_stream_ordinal=item["ordinal"],
        source_physical_stream_ordinal=item["source_physical_stream_ordinal"],
        exact_radial_leaf=item["exact_radial_leaf"],
        accurate_phi_interval=item["accurate_phi_interval"],
        source_domain={key:row[key] for key in
            ("patch","cell","u_interval","phi_over_pi_interval")},
        F=f,N=n,w=w,a=a,b=b,qh=qh,qv=qv,normal_squared=total,
        C0=c0,C1=c1,requested_tau=F(tau),
        full_sixjet_source_retained_in_original_geometry_stream=True,
        signed_interval_products_evaluated_without_positive_endpoint_assumptions=True)


def leaf_key(value):
    return dict(id=value["id"],
        source_complete_geometry_item_sha256=value["source_complete_geometry_item_sha256"],
        original_geometry_stream_ordinal=value["original_geometry_stream_ordinal"],
        source_physical_stream_ordinal=value["source_physical_stream_ordinal"],
        exact_radial_leaf=value["exact_radial_leaf"],
        accurate_phi_interval=value["accurate_phi_interval"],
        source_domain=value["source_domain"])


def append_sequence(digest,value):
    digest.update(canonical(encoded(value)).encode("ascii"))
    digest.update(b"\n")


def impose_directional(intervals,value):
    for kind,branches in intervals.items():
        for interval in branches.values():
            interval.impose(value["C1"][0],-value["C0"][0],
                kind=="strict",value["id"])


def impose_directional_caps(intervals,H,tau):
    H,tau=F(H),F(tau)
    for kind,branches in intervals.items():
        for interval in branches.values():
            strict=kind=="strict"
            interval.impose(H-tau,CAP_G,strict,"both-complete-p4-caps-z0")
            interval.impose(CAP_D_MINUS*H-tau,
                CAP_D_MINUS*CAP_G+tau*CAP_GRADIENT_SQUARED,strict,
                "both-complete-p4-caps-zmax")


def interval_metadata(intervals):
    return {kind:{name:interval.metadata() for name,interval in branches.items()}
        for kind,branches in intervals.items()}


def preview_directional(geometry,core,files,r,g,k,beta,parent):
    D=F(geometry["report"]["accurate_global_bounds"][
        "formal_reflection_fixed_caps_all_rotation_set_diameter_upper"])
    if D<=0:
        raise ArithmeticError("The complete accurate R717 diameter must be positive")
    tau=REACH_RATIO*D
    target=parent.new_intervals(beta)
    legacy=parent.new_intervals(beta)
    positive=parent.new_intervals(beta)
    distance=parent.CompleteTargetDistance(core,geometry)
    sequence=hashlib.sha256()
    count=0
    for item,row,pos in parent.original_leaves(geometry,files,r,g,k):
        value=directional_leaf(item,row,tau)
        append_sequence(sequence,leaf_key(value))
        impose_directional(target,value)
        parent.impose_rows(legacy,row,tau)
        parent.impose_rows(positive,row,F(0),strict_only=True)
        distance.leaf(row["id"],pos)
        count+=1
    if count!=geometry["stats"].count or count==0:
        raise ValueError("Do not reduce the original complete angular/radial leaf union")
    impose_directional_caps(target,core["H"],tau)
    parent.impose_caps(legacy,core["H"],tau,beta)
    parent.impose_caps(positive,core["H"],F(0),beta,strict_only=True)
    selected,kind,branch=beta.choose_parameter(target)
    directional_selected=selected
    legacy_selected,legacy_kind,legacy_branch=beta.choose_parameter(legacy)
    if selected is not None:
        purpose="R723-directional-three-percent-complete-D"
    elif legacy_selected is not None:
        selected,kind,branch=legacy_selected,legacy_kind,legacy_branch
        purpose="retained-legacy-support-target-without-a-legacy-certificate-prerequisite"
    else:
        selected,kind,branch=beta.choose_parameter(positive)
        purpose="strict-positive-support-for-a-possibly-smaller-directional-tube" if selected is not None else None
    return dict(D=D,tau=tau,count=count,beta=selected,selection_kind=kind,
        selection_branch=branch,selection_purpose=purpose,
        directional_target_beta=directional_selected,
        retained_legacy_target_beta=legacy_selected,
        directional_target_intervals=interval_metadata(target),
        retained_legacy_target_intervals=interval_metadata(legacy),
        strict_positive_support_intervals=interval_metadata(positive),
        original_leaf_sequence_sha256=sequence.hexdigest(),
        beta_branch_split_is_selection_only_same_affine_law_on_both_branches=True,
        holding=distance.result(core,geometry,k))


def selected_leaf(value,selected):
    selected=F(selected)
    if selected<=0:
        raise ValueError("The common flow matrix must be strictly positive definite")
    w=value["w"]
    numerator=p_add(value["a"],p_scale(value["b"],selected))
    if numerator[0]<=0:
        raise ArithmeticError("The selected whole-surface support numerator is not positive")
    m,L=min(F(1),selected),max(F(1),selected)
    denominator=p_add(value["qh"],p_scale(value["qv"],selected))
    denominator=p_intersect(denominator,
        (m*w[0]**2,L*w[1]**2),"positive directional denominator")
    if denominator[0]<=0 or denominator[1]<=0:
        raise ArithmeticError("The entire same-field directional denominator is not positive")
    weighted=p_mul(w,numerator)
    if weighted[0]<=0:
        raise ArithmeticError("A positive same-field product lost its sign")
    sigma=numerator[0]/w[1]
    direct=weighted[0]/denominator[1]
    legacy=sigma/L
    affine=value["C0"][0]+selected*value["C1"][0]
    target_paid=affine>=0
    rho=max(direct,legacy,value["requested_tau"] if target_paid else F(0))
    return dict(id=value["id"],common_beta=selected,unit_support_lower=sigma,
        directional_numerator_lower=weighted[0],
        directional_denominator_positive_lower=denominator[0],
        directional_denominator_upper=denominator[1],
        direct_directional_ratio_lower=direct,legacy_sigma_over_L_lower=legacy,
        requested_target_affine_margin_lower=affine,
        requested_target_affine_condition_paid=target_paid,
        directional_ratio_lower=rho,
        source_complete_geometry_item_sha256=value["source_complete_geometry_item_sha256"])


def new_chunk(index,start):
    return dict(index=index,start_ordinal=start,end_ordinal=start-1,leaf_count=0,
        directional_ratio_lower=None,directional_ratio_witness=None,
        unit_support_lower=None,unit_support_witness=None,
        target_affine_margin_lower=None,target_affine_margin_witness=None,
        all_target_affine_conditions_paid=True,
        directional_denominator_positive_lower=None,
        directional_denominator_positive_witness=None)


def add_chunk(chunk,value,selected_result,ordinal,digest):
    if ordinal!=chunk["end_ordinal"]+1:
        raise ValueError("The complete original leaf sequence cannot skip or reorder")
    chunk["end_ordinal"]=ordinal
    chunk["leaf_count"]+=1
    append_sequence(digest,dict(source=leaf_key(value),derived=selected_result,
        C0=encoded(value["C0"]),C1=encoded(value["C1"])))
    for source,target,witness in (
        ("directional_ratio_lower","directional_ratio_lower","directional_ratio_witness"),
        ("unit_support_lower","unit_support_lower","unit_support_witness"),
        ("requested_target_affine_margin_lower","target_affine_margin_lower","target_affine_margin_witness"),
        ("directional_denominator_positive_lower","directional_denominator_positive_lower",
            "directional_denominator_positive_witness")):
        number=selected_result[source]
        if chunk[target] is None or number<chunk[target]:
            chunk[target],chunk[witness]=number,value["id"]
    chunk["all_target_affine_conditions_paid"] &= selected_result["requested_target_affine_condition_paid"]


def second_pass_directional(geometry,core,prepass,files,r,g,k,parent,chunk_rows,emit):
    selected=prepass["beta"]
    if selected is None:
        return None,[]
    selected=F(selected)
    if selected<=0 or chunk_rows<1:
        raise ValueError("Positive beta and a complete packaging count are required")
    sequence=hashlib.sha256()
    chunks=[]
    chunk=new_chunk(0,0)
    chunk_digest=hashlib.sha256()
    count=0
    minimum_rho=minimum_sigma=minimum_margin=None
    rho_witness=sigma_witness=margin_witness=None
    all_target=True
    def finish():
        nonlocal chunk,chunk_digest
        if chunk["leaf_count"]==0:
            return
        definition=dict(chunk,complete_derived_leaf_sequence_sha256=chunk_digest.hexdigest(),
            schema=SCHEMA+"-directional-whole-leaf-range",
            current_full_point_sha256=geometry["context"]["actual"]["current_full_point_sha256"],
            actual_snapshot_identity_sha256=geometry["context"]["actual"]["actual_snapshot_identity_sha256"],
            complete_geometry_binding_identity_sha256=geometry["identity"],
            original_geometry_report=geometry["record"],
            common_beta=selected,requested_tau=prepass["tau"],
            same_source_ordered_original_leaf_union_retained=True,
            original_complete_F_N_w_sixjet_and_domain_streams_are_the_numeric_inputs=True,
            no_leaf_or_vector_or_field_component_sampled_or_dropped=True,
            grouping_changes_packaging_only=True)
        record=emit(definition)
        chunks.append(record)
        chunk=new_chunk(len(chunks),count)
        chunk_digest=hashlib.sha256()
    for item,row,pos in parent.original_leaves(geometry,files,r,g,k):
        value=directional_leaf(item,row,prepass["tau"])
        append_sequence(sequence,leaf_key(value))
        result=selected_leaf(value,selected)
        add_chunk(chunk,value,result,count,chunk_digest)
        for key in ("directional_ratio_lower","unit_support_lower","requested_target_affine_margin_lower"):
            number=result[key]
            if key=="directional_ratio_lower" and (minimum_rho is None or number<minimum_rho):
                minimum_rho,rho_witness=number,value["id"]
            elif key=="unit_support_lower" and (minimum_sigma is None or number<minimum_sigma):
                minimum_sigma,sigma_witness=number,value["id"]
            elif key=="requested_target_affine_margin_lower" and (minimum_margin is None or number<minimum_margin):
                minimum_margin,margin_witness=number,value["id"]
        all_target &= result["requested_target_affine_condition_paid"]
        count+=1
        if chunk["leaf_count"]>=chunk_rows:
            finish()
    finish()
    if (count!=geometry["stats"].count or count!=prepass["count"] or count==0
            or sequence.hexdigest()!=prepass["original_leaf_sequence_sha256"]):
        raise ValueError("The complete directional second pass differs from the original full first pass")
    H=F(core["H"])
    B=selected*H-CAP_G
    if B<=0:
        raise ArithmeticError("The complete marked cap support numerator is not positive")
    cap_sigma=B/CAP_D_PLUS
    cap_rho=min(B/selected,B*CAP_D_MINUS/(selected+CAP_GRADIENT_SQUARED))
    cap0=selected*(H-prepass["tau"])-CAP_G
    cap1=selected*(CAP_D_MINUS*H-prepass["tau"])-CAP_D_MINUS*CAP_G-prepass["tau"]*CAP_GRADIENT_SQUARED
    cap_target=cap0>=0 and cap1>=0
    if cap_target:
        cap_rho=max(cap_rho,prepass["tau"])
    activity_K=F(geometry["report"]["accurate_global_bounds"]["principal_curvature_absolute_upper"])
    if activity_K<0 or minimum_rho is None or minimum_rho<=0 or minimum_sigma<=0:
        raise ArithmeticError("The complete activity curvature/support bounds are invalid")
    K=max(activity_K,CAP_K)
    L=max(F(1),selected)
    sigma=min(minimum_sigma,cap_sigma)
    rho=min(minimum_rho,cap_rho)
    reach=min(rho,1/K)
    legacy_reach=min(sigma/L,1/K)
    if reach<legacy_reach:
        raise ArithmeticError("The retained complete legacy bound must remain available")
    return dict(common_beta=selected,centre=[F(0)]*3,A_diagonal=[F(1),F(1),selected],
        lambda_min=min(F(1),selected),lambda_max=L,
        complete_activity_and_cap_sigma_lower=sigma,
        complete_activity_sigma_lower=minimum_sigma,complete_activity_sigma_witness=sigma_witness,
        sigma_lower_witness=sigma_witness if minimum_sigma<=cap_sigma else "both-complete-p4-caps",
        cap_numerator_lower=B,cap_support_lower=cap_sigma,
        complete_activity_directional_ratio_lower=minimum_rho,
        complete_activity_directional_ratio_witness=rho_witness,
        complete_cap_directional_ratio_lower=cap_rho,
        complete_marked_directional_ratio_lower=rho,
        directional_ratio_witness=rho_witness if minimum_rho<=cap_rho else "both-complete-p4-caps",
        requested_activity_affine_margin_lower=minimum_margin,
        requested_activity_affine_margin_witness=margin_witness,
        all_activity_requested_affine_conditions_paid=all_target,
        cap_target_endpoint_margins=[cap0,cap1],
        all_marked_caps_requested_directional_conditions_paid=cap_target,
        complete_marked_curvature_upper=K,activity_curvature_upper=activity_K,
        complete_marked_R723_reach_lower=reach,
        R650_reach_lower=legacy_reach,
        legacy_R650_lower_is_a_direct_same_field_comparison_not_an_eight_role_certificate=True,
        all_original_support_rows_reread=count,
        complete_original_leaf_sequence_sha256=sequence.hexdigest(),
        directional_chunk_count=len(chunks),
        requested_tau=prepass["tau"],complete_D_upper=prepass["D"],
        requested_curvature_condition_paid=K*prepass["tau"]<=1,
        requested_directional_support_paid=rho>=prepass["tau"],
        requested_complete_reach_condition_paid=reach>=prepass["tau"],
        all_physical_phases_by_commuting_rotation_and_reflection=True,
        literal_beta_changes_actual_field=False,strict_positive_support_paid=True,
        complete_R723_directional_assumptions_computed=True,
        embedding_and_outwardness_assumed_before_support=False,
        support_sigma_is_not_replaced_by_directional_ratio=True,
        cap_component_constants=dict(gradient_square_upper=CAP_GRADIENT_SQUARED,
            horizontal_loss_upper=CAP_G,root_lower=CAP_D_MINUS,root_upper=CAP_D_PLUS,
            actual_fixed_p4_curvature_upper=CAP_K),
        original_whole_physical_scope_and_all_mixed_pairs_retained=True),chunks


def unmarked_body_interpretation(geometry,core,ports,support,prepass,proofs,sources,report_path):
    """Instantiate existing R716 section 6 from its own unmarked R723 bounds.

    This does not infer an outside tube from marked embedding. It first replaces
    the cap support by beta*H and the cap curvature by zero, leaving the entire
    actual activity and its positive support unchanged.
    """
    a=geometry["context"]["actual"]
    result=dict(schema=SCHEMA+"-R716-unmarked-outward-tube",
        source_sha256=sha(__file__),current_full_point_sha256=a["current_full_point_sha256"],
        complete_model_identity_sha256=a["model_identity_sha256"],
        exact_fixed_target_identity_sha256=a["exact_fixed_target_identity_sha256"],
        complete_geometry_binding_identity_sha256=geometry["identity"],
        complete_binding_identity_sha256=geometry["identity"],
        complete_binding_kind="complete-continuous-geometry-cover-and-source-binding",
        actual_current_full_point_sha256=a["current_full_point_sha256"],
        actual_model_identity_sha256=a["model_identity_sha256"],
        actual_snapshot_identity_sha256=a["actual_snapshot_identity_sha256"],
        complete_actual_input_identity_sha256=geometry["context"]["actual_identity"],
        complete_original_normal_binding_identity_sha256=geometry["context"]["binding_identity"],
        actual_complete_model=a["complete_model"],
        actual_complete_point_arrays=a["current_point_arrays_file"],
        actual_complete_snapshot=a["actual_snapshot_file"],
        original_complete_normal_report=geometry["context"]["record"],
        original_complete_normal_binding=geometry["context"]["report"]["complete_binding"],
        original_complete_normal_input_and_request=
            geometry["context"]["report"]["complete_input_and_request"],
        complete_geometry_report=geometry["record"],
        complete_source_records=sources,
        complete_original_angle_branch=geometry["report"]["original_complete_angle_branch"],
        original_stage_count=32,whole_circle_phi_over_pi=["0","2"],
        exact_full_radial_mesh_affine=geometry["binding"]["complete_exact_radial_mesh_affine"],
        final_complete_producer_report_required=True,
        required_final_report_path=str(Path(report_path).resolve()),
        intermediate_sidecar_without_final_complete_report_is_not_a_certificate=True,
        proof_sources={name:proofs[name] for name in
            ("source_specific_ports","R248","R650","R723_directional_flow","R661_components_only","R716","fixed_fejer_current_source_adapter")},
        unmarked_closed_C2_immersion_certified=None,
        unmarked_all_phase_embedding_and_outwardness_certified=None,
        common_beta=None,lambda_max=None,complete_activity_sigma_lower=None,
        unmarked_flat_cap_support_lower=None,unmarked_global_sigma_lower=None,
        unmarked_complete_curvature_upper=None,unmarked_reach_lower=None,
        fixed_mark_height=MARK_HEIGHT,strict_outward_tube_margin=None,
        mark_height_strictly_below_unmarked_reach=None,
        all_four_fixed_mark_components_in_uniform_outward_normal_tube=None,
        added_column_interiors_disjoint_from_every_unmarked_body=None,
        distinct_added_mark_interiors_disjoint=None,
        actual_marked_boundary_equals_unmarked_body_union_fixed_added_body=None,
        R716_volume_and_all_twelve_raw_moment_additivity_interpretation_certified=None,
        actual_unmarked_body_rotates_about_origin_z_axis=None,
        marked_embedding_assumed_to_prove_unmarked_reach=False,
        all_activity_whole_boxes_reread_for_the_common_support=True,
        fixed_cap_metric_or_mathematical_target_modified=False,
        unmarked_auxiliary_surface_claimed_isometric_to_marked_target=False,
        unmarked_caps_use_their_flat_induced_metric_only_for_the_auxiliary_geometric_proof=True,
        independent_auxiliary_mark_amplitude_scientific_field_constructed=False,
        half_turn_symmetry_or_centroid_vanishing_assumed=False,
        unmarked_flux_integral_or_any_new_integrand_evaluated=False,
        twelve_actual_integrals_or_nonzero_centred_moment_witness_paid_here=False,
        delta_E_positive=None,remaining=[])
    if not ports["complete_closed_C2_immersion_certified"] or support is None:
        result["remaining"]=["The same full closed immersion and positive activity support are not paid"]
        return result
    selected=support["common_beta"]
    L=support["lambda_max"]
    activity=support["complete_activity_sigma_lower"]
    flat=selected*core["H"]
    sigma=min(activity,flat)
    curvature=support["activity_curvature_upper"]
    if selected<=0 or sigma<=0 or L!=max(F(1),selected) or curvature<0:
        raise ArithmeticError("The actual complete unmarked support hypotheses changed")
    if (support.get("complete_R723_directional_assumptions_computed") is not True
            or support["all_original_support_rows_reread"]!=geometry["stats"].count):
        raise ValueError("The full actual activity directional proof is missing")
    activity_rho=F(support["complete_activity_directional_ratio_lower"])
    rho=min(activity_rho,core["H"])
    if rho<=0:
        raise ArithmeticError("The complete unmarked directional radius must be positive")
    reach=rho
    legacy_reach=sigma/L
    if curvature>0:
        reach=min(reach,1/curvature)
        legacy_reach=min(legacy_reach,1/curvature)
    margin=reach-MARK_HEIGHT
    tube=margin>0
    result.update(unmarked_closed_C2_immersion_certified=True,
        unmarked_all_phase_embedding_and_outwardness_certified=True,
        common_beta=selected,lambda_max=L,complete_activity_sigma_lower=activity,
        unmarked_flat_cap_support_lower=flat,unmarked_global_sigma_lower=sigma,
        unmarked_complete_curvature_upper=curvature,unmarked_reach_lower=reach,
        unmarked_directional_flow_ratio_lower=rho,
        complete_activity_directional_ratio_lower=activity_rho,
        complete_flat_caps_directional_ratio_lower=core["H"],
        unmarked_R650_comparison_reach_lower=legacy_reach,
        unmarked_reach_theorem="R723 applied directly to activity plus both unmarked flat disks",
        zero_activity_curvature_means_no_curvature_upper_constraint=curvature==0,
        strict_outward_tube_margin=margin,
        mark_height_strictly_below_unmarked_reach=tube,
        actual_unmarked_body_rotates_about_origin_z_axis=True,
        complete_p4_support_radius=SUPPORT_RADIUS,
        actual_cap_radius_lower=geometry["context"]["R"].lo,
        complete_D_upper=prepass["D"],requested_reach_ratio=F(3,100),
        complete_D_upper_at_least_twice_accurate_R_lower=
            prepass["D"]>=2*geometry["context"]["R"].lo,
        target_three_percent_D_is_strictly_larger_than_mark_height=
            prepass["tau"]>MARK_HEIGHT,
        flat_cap_outward_normals=["+ez","-ez"],
        added_body_definition="Union of all three upper and one lower p4 normal columns 0<=v<=h*(1-distance_squared/radius_squared)^4 over their complete fixed disks",
        all_tube_base_points_and_normals_fixed_in_every_phase=True,
        unmarked_R650_comparison_recomputed_without_using_marked_family_embedding=True,
        unmarked_R723_bound_recomputed_without_using_marked_family_embedding=True,
        marked_reach_substituted_for_unmarked_reach=False)
    if tube:
        result.update(all_four_fixed_mark_components_in_uniform_outward_normal_tube=True,
            added_column_interiors_disjoint_from_every_unmarked_body=True,
            distinct_added_mark_interiors_disjoint=True,
            actual_marked_boundary_equals_unmarked_body_union_fixed_added_body=True,
            R716_volume_and_all_twelve_raw_moment_additivity_interpretation_certified=True,
            zero_volume_intersections_only_at_cap_bases_or_support_boundaries=True,
            accurate_body_relation="Omega_marked_alpha = R_alpha Omega_unmarked_0 union B, up to their common boundary",
            accurate_moment_relation="V=V_Omega+V_B; m_alpha=R_alpha*m_Omega+m_B; Q_alpha=R_alpha*Q_Omega*R_alpha^T+Q_B",
            proof="R723 independently gives the UNMARKED complete closed family its own common reach lower bound. Each p4 added point is p+v*n_p with 0<v<=1/1000 below that bound. The full exterior normal tube is injective and stays on the outside for every phase. Its base disks are fixed and distinct. R716 section 6 therefore identifies the complete marked boundary and pays all additive raw moment interpretations.")
    else:
        result["remaining"].append(
            "The actual unmarked reach lower bound does not strictly exceed the mark height; outside-tube/additive-body interpretation remains unpaid")
    result["remaining"].append(
        "The same-field complete twelve flux integrals, their errors and a nonzero centred invariant remain independent input responsibilities")
    return result



def flow_round_down(value):
    """Exact nonnegative dyadic floor; used only for the optional R718 bound."""
    value=F(value)
    if value<0:
        raise ArithmeticError("The positive-series bound cannot round a negative input")
    scale=1<<FLOW_BINARY_BITS
    return F((value.numerator*scale)//value.denominator,scale)


def flow_power_lower(ratio,m):
    """Prove 1 <= result <= ratio**m by positive terms, without floating pow."""
    ratio,m=F(ratio),F(m)
    if ratio<1 or not 0<m<=1:
        raise ArithmeticError("The R718 ratio and normalized least eigenvalue changed")
    if m==1:
        return dict(lower=ratio,method="exact-rational-first-power",
            accurate_ratio=ratio,least_eigenvalue=m,
            least_eigenvalue_numerator=m.numerator,
            least_eigenvalue_denominator=m.denominator,
            log_lower=None,scaled_log_lower=None,
            logarithm_positive_terms=0,exponential_positive_terms=0,
            directed_rounding_binary_bits=FLOW_BINARY_BITS,
            integer_power_comparison_executed=False,
            directed_positive_series_proof_used=False)
    z=flow_round_down((ratio-1)/(ratio+1))
    z2=flow_round_down(z*z)
    power=z
    log_lower=F(0)
    for j in range(FLOW_LOG_TERMS):
        term=flow_round_down(2*power/(2*j+1))
        log_lower=flow_round_down(log_lower+term)
        power=flow_round_down(power*z2)
    scaled=flow_round_down(m*log_lower)
    term=F(1)
    lower=F(1)
    for j in range(1,FLOW_EXP_TERMS+1):
        term=flow_round_down(term*scaled/j)
        lower=flow_round_down(lower+term)
    if lower<1:
        raise ArithmeticError("The exact positive exponential constant term was lost")
    return dict(lower=lower,method="positive-log-and-exp-series-with-exact-dyadic-floors",
        accurate_ratio=ratio,least_eigenvalue=m,
        least_eigenvalue_numerator=m.numerator,
        least_eigenvalue_denominator=m.denominator,
        log_lower=log_lower,scaled_log_lower=scaled,
        logarithm_positive_terms=FLOW_LOG_TERMS,
        exponential_positive_terms=FLOW_EXP_TERMS,
        directed_rounding_binary_bits=FLOW_BINARY_BITS,
        integer_power_comparison_executed=False,
        directed_positive_series_proof_used=True)


def flow_image_distance(geometry,core,ports,support,proofs,main_report,report_path):
    """Read only the already paid same-field closed support and exact core.

    R723 proves the closed family; R718 uses its separate actual marked sigma.
    This is an additional lower bound; the original complete box scan remains.
    """
    if (ports.get("complete_closed_C2_immersion_certified") is not True
            or ports.get("continuous_global_oriented_unit_normal_certified") is not True
            or main_report.get("all_physical_phases_embedded") is not True
            or main_report.get("outward_orientation_certified") is not True
            or main_report.get("all_R723_directional_evidence_roles_paid") is not True
            or not isinstance(main_report.get("actual_R723_directional_evidence_package"),dict)
            or support is None or support.get("strict_positive_support_paid") is not True):
        raise ValueError("R718 requires this complete R723 closed/outward and actual sigma evidence")
    selected=F(support["common_beta"])
    sigma=F(support["complete_activity_and_cap_sigma_lower"])
    if (selected<=0 or sigma<=0 or support["centre"]!=[F(0)]*3
            or support["A_diagonal"]!=[F(1),F(1),selected]
            or support["all_original_support_rows_reread"]!=geometry["stats"].count
            or support["all_physical_phases_by_commuting_rotation_and_reflection"] is not True):
        raise ValueError("The complete common marked-surface flow support changed")
    if (ports["core_port"]["F"]!="Gamma in z=0"
            or ports["phase"]["alpha"]!="pi*t/2"
            or ports["phase"]["cap_material_points_fixed"] is not True
            or core["phase_one_t"]!="1" or core["phase_one_alpha_over_pi"]!="1/2"
            or core["endpoint_values_use_all_current_coefficients"] is not True):
        raise ValueError("Use the actual zero-height core and complete fixed-chart phase")
    c=geometry["context"]
    actual=c["actual"]
    if (core["current_full_point_sha256"]!=actual["current_full_point_sha256"]
            or ports["current_full_point_sha256"]!=actual["current_full_point_sha256"]
            or main_report["actual_current_full_point_sha256"]!=actual["current_full_point_sha256"]
            or main_report["actual_snapshot_identity_sha256"]!=actual["actual_snapshot_identity_sha256"]
            or main_report["complete_original_model_identity_sha256"]!=actual["model_identity_sha256"]
            or main_report["exact_fixed_target_identity_sha256"]!=actual["exact_fixed_target_identity_sha256"]):
        raise ValueError("The optional flow bound cannot borrow another field or point")
    coefficients=[F(v) for v in core["current_core_rational"]]
    X=F(1)+sum(coefficients,F(0))
    Y=F(1)+sum((v if (j+1)%2==0 else -v
        for j,v in enumerate(coefficients)),F(0))
    if (len(coefficients)!=160 or X!=core["X"] or Y!=core["Y"] or X<=0 or Y<=0):
        raise ValueError("Use every current coefficient and two positive exact support axes")
    rho=dict(c["geometry"]["current_rho_proof"])
    first_three=(actual["complete_model"]["base_complete_model"]["fixed_core_first3"]
        ==core["current_core_binary64_hex"][:3]
        and coefficients[0]==F(7,16)
        and abs(coefficients[1]+F(3,40))<=F(1,1<<53)
        and abs(coefficients[2]-F(3,112))<=F(1,1<<53))
    rho_positive=(rho.get("all_coefficients_used") is True and F(rho["lower"])>0)
    uniform=bool(first_three and rho_positive)
    if uniform and X/Y<=F(7,3):
        raise ArithmeticError("The actual full core contradicts its paid R719 hypotheses")
    if X>=Y:
        ratio=X/Y
        p=[F(0),Y,F(0)]
        q=[F(0),X,F(0)]
    else:
        ratio=Y/X
        p=[-X,F(0),F(0)]
        q=[-Y,F(0),F(0)]
    m=min(F(1),selected)
    power=flow_power_lower(ratio,m)
    bound=flow_round_down(sigma*(power["lower"]-1)/m)
    return dict(schema=SCHEMA+"-R718-whole-image-flow-distance",
        source_sha256=sha(__file__),
        final_complete_producer_report_required=True,
        required_final_report_path=str(Path(report_path).resolve()),
        final_all_input_and_generated_output_bytes_recheck_required=True,
        actual_current_full_point_sha256=actual["current_full_point_sha256"],
        actual_snapshot_identity_sha256=actual["actual_snapshot_identity_sha256"],
        complete_original_model_identity_sha256=actual["model_identity_sha256"],
        exact_fixed_target_identity_sha256=actual["exact_fixed_target_identity_sha256"],
        complete_actual_input_identity_sha256=c["actual_identity"],
        complete_original_normal_binding_identity_sha256=c["binding_identity"],
        original_geometry_binding_identity_sha256=geometry["identity"],
        current_core_word_identity_sha256=core["current_core_word_identity_sha256"],
        complete_current_coefficient_count=len(coefficients),
        current_X=X,current_Y=Y,actual_axis_ratio=ratio,
        reference_axis_point_on_complete_S0=p,phase_one_point_on_complete_S1=q,
        phase_one_t=F(1),phase_one_alpha_over_pi=F(1,2),
        exact_source_and_witness_height=F(0),
        exact_origin=[F(0)]*3,A_diagonal=[F(1),F(1),selected],
        common_beta=selected,least_eigenvalue=m,
        complete_marked_sigma_lower=sigma,
        complete_marked_support_record=support,
        full_target_including_every_upper_lower_leaf_and_both_marked_caps=True,
        core_only_target_distance_used=False,
        same_material_displacement_used_as_image_distance=False,
        rigid_alignment_or_grip_stabilizer_quotient_used=False,
        unmarked_sigma_substituted_for_marked_sigma=False,
        all_original_normal_stages=32,whole_circle_phi_over_pi=["0","2"],
        exact_current_rho_proof=rho,
        R719_first_three_current_coefficients_match_complete_fixed_model=first_three,
        R719_entire_current_continuous_rho_positive=rho_positive,
        R719_uniform_X_over_Y_strict_lower=F(7,3) if uniform else None,
        R719_uniform_axis_ratio_proved=True if uniform else None,
        R719_uniform_bound_replaces_actual_coefficient_ratio=False,
        power_lower_evidence=power,
        rigorous_delta_hold_lower=bound,
        exact_pre_rounding_distance_lower=sigma*(power["lower"]-1)/m,
        all_directed_rounding_weakens_the_lower_bound=True,
        new_F_J_root_or_integrand_calls=0,
        original_complete_box_bound_retained=True,
        proof_sources={name:proofs[name] for name in
            ("R718_complete_flow_distance","R719_all_current_core_modes",
             "R650","R723_directional_flow","R248","fixed_fejer_current_source_adapter")})




def load_environment(repo):
    repo=Path(repo).resolve()
    root=repo/TOPIC/"scripts/resume_20261126"
    parent,ppath=load(root/PARENT[0],PARENT[1],"_R723_complete_closed_algorithm_parent")
    if parent.GEOMETRY!=GEOMETRY or parent.BRIDGE!=BRIDGE or parent.BETA!=BETA:
        raise ValueError("The complete pinned parent source family changed")
    g,gpath=load(root/GEOMETRY[0],GEOMETRY[1],"_R723_complete_accurate_geometry")
    bridge,bpath=load(root/BRIDGE[0],BRIDGE[1],"_R723_complete_accurate_geometry_bridge")
    r,rpath=g.load_reader(repo)
    r.require_actions()
    files=r.Files()
    outputs=r.Files()
    for path in (Path(__file__).resolve(),ppath,gpath,bpath,rpath):
        files.add(path)
    k,krecord=r.load_arithmetic(repo,files)
    beta,betapath=load(root/BETA[0],BETA[1],"_R723_original_rational_parameter_selection")
    files.add(betapath)
    if (beta.CAP_G!=CAP_G or beta.CAP_DENOMINATOR!=CAP_D_PLUS
            or beta.CAP_K!=CAP_K or beta.REACH_RATIO!=REACH_RATIO
            or CAP_D_MINUS**2>1+CAP_GRADIENT_SQUARED
            or CAP_D_MINUS*CAP_D_PLUS<1+CAP_GRADIENT_SQUARED):
        raise ArithmeticError("The complete exact p4 component parameters changed")
    proofs=parent.proof_files(repo,files,r)
    proof_record=r.file_record(repo/R723[0])
    if proof_record["sha256"]!=R723[1]:
        raise ValueError("The full R723 theorem source changed")
    files.verify(proof_record)
    proofs["R723_directional_flow"]=proof_record
    paths=dict(closed_phase_producer=Path(__file__).resolve(),
        complete_closed_algorithm_parent=ppath,
        geometry_bridge=bpath,positive_support_interval_algorithm=betapath)
    return dict(repo=repo,parent=parent,g=g,bridge=bridge,r=r,k=k,beta=beta,
        files=files,outputs=outputs,proofs=proofs,paths=paths)


def bind_geometry(env,record):
    r,g,bridge,k,files=(env[name] for name in ("r","g","bridge","k","files"))
    raw,_=files.read_json(record)
    if raw.get("schema")!=g.SCHEMA or raw.get("source_sha256")!=GEOMETRY[1]:
        raise ValueError("Use the exact whole current fixed-Fejer R722 geometry producer")
    required=("complete","all_input_and_output_bytes_rechecked",
        "full_upper_cover_processed","continuous_curvature_bound_complete",
        "continuous_support_numerator_bounds_complete")
    missing=[key for key in required if raw.get(key) is not True]
    if missing:
        return None,missing
    scoped=argparse.Namespace(repo=env["repo"],geometry_report=Path(record["path"]),
        expected_geometry_report_sha256=record["sha256"])
    geometry=bridge.load_geometry(scoped,g,r,k,files)
    r.verify_geometry_identity(geometry["context"],k)
    actual=geometry["context"]["actual"]
    if len(actual["full_scientific_runtime_source_records"])!=137:
        raise ValueError("Retain every one of the 137 complete actual scientific source roles")
    return geometry,[]


def build_field_cover(geometry,sources,beta,parent):
    a=geometry["context"]["actual"]
    field_definition=dict(schema=SCHEMA+"-accurate-full-field-definition",
        mathematical_model=a["complete_model"],
        mathematical_model_identity_sha256=a["model_identity_sha256"],
        current_full_point_sha256=a["current_full_point_sha256"],
        actual_snapshot_identity_sha256=a["actual_snapshot_identity_sha256"],
        complete_point_arrays=a["current_point_arrays_file"],
        complete_snapshot=a["actual_snapshot_file"],
        fixed_metric_identity_sha256=a["fixed_scalar_metric_identity_sha256"],
        fixed_material_chart_identity_sha256=a["fixed_chart_core_sha256"],
        exact_fixed_target_identity_sha256=a["exact_fixed_target_identity_sha256"],
        mathematical_target_identity_sha256=a["mathematical_target_identity_sha256"],
        normal_convention="candidate Fphi cross Fs on the entire upper meridian",
        fixed_cap_recipe=beta.CAP_RECIPE,
        source_by_role={name:dict(record) for name,record in sources.items()},
        R723_producer_source_sha256=sha(__file__),
        complete_closed_algorithm_parent_source_sha256=PARENT[1],
        original_upper_geometry_binding_identity_sha256=geometry["identity"],
        physical_phase_formula="R_alpha U(s,Theta0^{-1}(Theta0(phi)-alpha)); fixed Cartesian p4 caps",
        physical_phase_alpha_over_pi_interval=["0","1/2"],
        target_metric="same activity diag(1,(a_deep*rho0)^2), reflected lower, fixed p4 caps with their own induced metric",
        accurate_sixjet_evidence_scope=parent.ACCURATE_CLAIM_SCOPE,
        working_field_word_error_bound_produced=False,
        all_137_scientific_source_roles_retained=True,
        new_scientific_field_or_normal_root_constructed=False,
        previous_point_target_or_certificate_inherited=False)
    field_definition=encoded(field_definition)
    field=dict(definition=field_definition,identity_sha256=canonical(field_definition))
    cover_definition=dict(schema=SCHEMA+"-complete-original-cover-definition",
        field_identity_sha256=field["identity_sha256"],
        exact_S_enclosure=geometry["binding"]["accurate_S"],
        complete_exact_radial_mesh_affine=geometry["binding"]["complete_exact_radial_mesh_affine"],
        complete_original_geometry_report=geometry["record"],
        complete_original_normal_report=geometry["context"]["record"],
        original_complete_angle_branch=geometry["report"]["original_complete_angle_branch"],
        original_whole_geometry_streams=[dict(block["definition"]["whole_leaf_geometry_stream"])
            for block in geometry["blocks"]],
        complete_accurate_upper_leaf_count=geometry["stats"].count,
        exact_radial_affine_interval=[["0","0"],["1","0"]],
        exact_phi_over_pi_interval=["0","2"],
        all_original_normal_stages=32,
        all_closed_radial_and_angular_boundaries_retained=True,
        lower_extension="same signed-u reflected C2 lower family with Jz N",
        caps="both complete Cartesian fixed p4 caps, including flat remainder",
        physical_t_interval=["0","1"],physical_alpha_over_pi_interval=["0","1/2"])
    cover_definition=encoded(cover_definition)
    return field,dict(definition=cover_definition,identity_sha256=canonical(cover_definition))


def chunk_document(definition,field,cover,actual_execution,report_path):
    return dict(schema=SCHEMA+"-directional-leaf-range-evidence",
        producer_source_sha256=sha(__file__),
        field_identity_sha256=field["identity_sha256"],
        coverage_identity_sha256=cover["identity_sha256"],
        execution=actual_execution,
        final_complete_producer_report_required=True,
        required_final_report_path=str(Path(report_path).resolve()),
        final_all_bound_input_and_generated_evidence_bytes_recheck_required=True,
        original_full_stream_records=cover["definition"]["original_whole_geometry_streams"],
        range_definition=definition,
        all_original_leaf_and_F_N_w_data_retained_in_exact_original_files=True,
        range_minima_require_full_ordered_reread_not_sampling=True,
        original_R650_eight_role_claims_not_relabelled=True)


def directional_instantiation(geometry,core,ports,prepass,support,sources,proofs,
        field,cover,chunks,actual_execution,report_path):
    if (ports.get("complete_closed_C2_immersion_certified") is not True
            or ports.get("continuous_global_oriented_unit_normal_certified") is not True
            or support is None or support.get("strict_positive_support_paid") is not True
            or support.get("complete_R723_directional_assumptions_computed") is not True):
        raise ValueError("A complete R723 closed proof needs genuine ports and directional bounds")
    a=geometry["context"]["actual"]
    claims=dict(
        same_accurate_field_and_complete_source_binding=dict(
            current_point=a["current_full_point_sha256"],
            model=a["model_identity_sha256"],snapshot=a["actual_snapshot_identity_sha256"],
            target=a["exact_fixed_target_identity_sha256"],complete_original_source_role_count=137),
        whole_normal32_sixjet_radial_circle_cover=dict(
            normal_stages=32,exact_phi_over_pi=["0","2"],
            exact_radial_affine=[["0","0"],["1","0"]],
            complete_upper_leaf_count=geometry["stats"].count,
            all_original_accurate_root_scalar_integral_arithmetic_attribution_retained=True,
            working_field_word_error_bound_produced=False),
        closed_C2_sphere_and_exact_all_phase_family=dict(
            complete_C2_sphere=True,all_phase_C2=True,
            orientation_becomes_outward_by_global_R723_flow=True,
            full_mixed_pairs_follow_from_joint_normal_tube_injectivity=True,
            separate_component_reach_minimum_used_as_a_global_proof=False),
        common_directional_support_actual_curvature_and_diameter=dict(
            common_beta=support["common_beta"],centre=support["centre"],
            A_diagonal=support["A_diagonal"],
            marked_directional_ratio_lower=support["complete_marked_directional_ratio_lower"],
            marked_actual_curvature_upper=support["complete_marked_curvature_upper"],
            complete_D_upper=prepass["D"],requested_tau=prepass["tau"],
            marked_R723_reach_lower=support["complete_marked_R723_reach_lower"],
            target_reach_paid=support["requested_complete_reach_condition_paid"]),
        complete_fixed_marked_caps_and_oriented_lower_extension=dict(
            complete_original_p4_recipe=True,all_upper_lower_and_both_caps=True,
            same_beta_on_every_component_and_phase=True,
            cap_directional_ratio_lower=support["complete_cap_directional_ratio_lower"],
            cap_curvature_upper=CAP_K,
            unmarked_tube_not_inferred_from_marked_reach=True))
    if set(claims)!=set(DIRECTIONAL_ROLES):
        raise ArithmeticError("Every distinct R723 evidence role is required")
    return dict(schema=SCHEMA+"-complete-directional-instantiation",
        producer_source_sha256=sha(__file__),execution=actual_execution,
        complete=True,field=field,cover=cover,claims=claims,
        complete_source_records=sources,complete_proof_records=proofs,
        complete_actual_core=core,complete_original_ports_and_phase_proof=ports,
        complete_common_directional_support=support,
        complete_directional_range_records=chunks,
        declared_complete_original_leaf_count=geometry["stats"].count,
        original_leaf_sequence_sha256=prepass["original_leaf_sequence_sha256"],
        complete_accurate_geometry_report=geometry["record"],
        complete_original_normal_report=geometry["context"]["record"],
        complete_original_normal_input_and_request=
            geometry["context"]["report"]["complete_input_and_request"],
        original_complete_normal_binding=geometry["context"]["report"]["complete_binding"],
        accurate_input_identity_sha256=geometry["context"]["actual_identity"],
        original_normal_binding_identity_sha256=geometry["context"]["binding_identity"],
        original_geometry_binding_identity_sha256=geometry["identity"],
        actual_current_full_point_sha256=a["current_full_point_sha256"],
        actual_snapshot_identity_sha256=a["actual_snapshot_identity_sha256"],
        actual_model_identity_sha256=a["model_identity_sha256"],
        exact_fixed_target_identity_sha256=a["exact_fixed_target_identity_sha256"],
        final_complete_producer_report_required=True,
        required_final_report_path=str(Path(report_path).resolve()),
        final_all_bound_input_and_generated_evidence_bytes_recheck_required=True,
        joint_all_parallel_faces_and_normal_offsets_injective_by_R723=True,
        original_R650_target_pass_required_before_this_branch=False,
        original_eight_beta_roles_claimed_paid=False,
        old_beta_input_or_old_exact_claim_dictionary_fabricated=False,
        new_F_J_root_integrand_or_sampled_surface_calls=0)


def empty_directional_report(actual_execution,parent):
    report=parent.empty_report(actual_execution)
    report.update(schema=SCHEMA,source_sha256=sha(__file__),
        complete_closed_algorithm_parent_source_sha256=PARENT[1],
        complete_scope="complete same-field R723 directional flow consumption; no nonlinear solve",
        R723_directional_reach_lower=None,
        R723_marked_directional_ratio_lower=None,
        R723_activity_directional_ratio_lower=None,
        R723_cap_directional_ratio_lower=None,
        R723_curvature_target_paid=None,R723_directional_support_target_paid=None,
        all_R723_directional_evidence_roles_paid=False,
        actual_R723_directional_evidence_package=None,
        R723_field_identity_sha256=None,R723_coverage_identity_sha256=None,
        directional_range_evidence_records=[],
        original_R650_target_pass_required=False,
        original_eight_role_beta_consumer_executed=False,
        legacy_R650_lower_is_a_same_field_comparison_only=True)
    return report


def prepare_holding(prepass,ports):
    holding=dict(prepass["holding"])
    paid=ports["complete_closed_C2_immersion_certified"]
    holding["complete_closed_C2_family_assumptions_paid"]=paid
    holding["formal_constructed_compact_image_distance_lower"]=holding["rigorous_delta_hold_lower"]
    holding["embedding_assumed_in_image_distance_bound"]=False
    if not paid:
        holding["rigorous_delta_hold_lower"]=None
        holding["positive_lower_paid"]=False
    holding["original_complete_box_distance_lower"]=holding["rigorous_delta_hold_lower"]
    return holding


def apply_flow_bound(geometry,core,ports,support,proofs,report,report_path,
        holding,parent,D):
    flow=flow_image_distance(geometry,core,ports,support,proofs,report,report_path)
    original=holding["original_complete_box_distance_lower"]
    old=F(0) if original is None else F(original)
    bound=flow["rigorous_delta_hold_lower"]
    combined=max(old,bound)
    holding.update(R718_flow_distance_lower=bound,R718_flow_distance_evidence=flow,
        R718_flow_distance_used=bound>old,
        combined_lower_bound_rule="max(original complete box lower, paid R718 flow lower)",
        rigorous_delta_hold_lower=combined,positive_lower_paid=combined>0)
    gripping=parent.grip(geometry,core,D,holding,True)
    report.update(R718_flow_distance_lower=encoded(bound),
        R718_flow_distance_evidence=flow,R718_flow_distance_used=bound>old,
        R718_optional_bound_status="complete-directed-rational-lower-bound",
        R719_uniform_axis_ratio_proved=flow["R719_uniform_axis_ratio_proved"],
        whole_target_distance=holding,grip_evidence=gripping,
        delta_hold_lower=encoded(gripping["delta_hold_lower"]),
        delta_hold_over_D_lower=encoded(gripping["delta_hold_over_D_lower"]),
        delta_hold_standard_sufficient=gripping["delta_hold_standard_sufficient"],
        delta_hold_stronger_target_sufficient=gripping["delta_hold_stronger_target_sufficient"])
    return gripping



def _record_key(record):
    if not isinstance(record,dict):
        raise ValueError("A complete original whole-file record is required")
    path=str(Path(record["path"]).resolve())
    size=record["bytes"]
    digest=record["sha256"]
    if (type(size) is not int or size<0 or not isinstance(digest,str)
            or len(digest)!=64 or any(c not in "0123456789abcdef" for c in digest)):
        raise ValueError("The complete source/input/output record is invalid")
    return path,size,digest


def _original_records(records,files,kind):
    if not isinstance(records,list):
        raise ValueError("Read every complete original "+kind+" record")
    result={}
    for record in records:
        key=_record_key(record)
        if key[0] in result:
            raise ValueError("An original "+kind+" path is listed twice")
        files.verify(record)
        result[key[0]]=dict(record)
    return result


def _declared(record,records,kind):
    path=_record_key(record)[0]
    if path not in records or records[path]!=record:
        raise ValueError("The exact original "+kind+" record is not uniquely declared")
    return record


def _bind_complete_source_copies(original,current,files,inputs,kind):
    if not isinstance(original,dict) or set(original)!=set(current):
        raise ValueError("Retain every original "+kind+" role")
    for role,record in original.items():
        _declared(record,inputs,kind)
        old=_record_key(record)
        new=_record_key(current[role])
        if old[1:]!=new[1:]:
            raise ValueError("Only a complete byte-identical current source copy is permitted: "+role)
        files.verify(record)
        files.verify(current[role])
    return original


def _equal(actual,expected,label):
    if actual!=encoded(expected):
        raise ValueError("The full R723 evidence disagrees with actual re-consumption: "+label)


def validate_complete_report(repo,report_path,*,expected_report_sha256=None):
    """Re-consume the complete original field/streams; never trust sidecar flags.

    This pure evidence API adds no solver gate. Incomplete main reports are
    refused before sidecars are opened. A completed consumption with unpaid
    geometric conditions is validly returned with R723_evidence_available=False.
    All original paths are actually read; current code copies must match whole
    SHA/bytes and never replace those original path identities.
    """
    require_actions()
    env=load_environment(repo)
    parent,r,g,k,beta,files=(env[name] for name in ("parent","r","g","k","beta","files"))
    report_path=Path(report_path).resolve()
    record=r.file_record(report_path)
    if expected_report_sha256 is not None and record["sha256"]!=expected_report_sha256:
        raise ValueError("The exact final main report SHA differs")
    main,_=files.read_json(record)
    if (main.get("schema")!=SCHEMA or main.get("source_sha256")!=sha(__file__)
            or main.get("complete") is not True
            or main.get("status")!="complete-same-field-consumption"
            or main.get("all_bound_input_and_generated_evidence_bytes_rechecked") is not True):
        raise ValueError("A residual or incomplete R723 sidecar is not a final certificate")
    if (main.get("all_eight_original_beta_evidence_roles_paid") is not False
            or main.get("actual_outward_beta_package") is not None
            or main.get("original_eight_role_beta_consumer_executed") is not False
            or main.get("original_R650_target_pass_required") is not False):
        raise ValueError("The distinct R723 route cannot forge legacy exact beta claims")
    inputs=_original_records(main["actual_complete_input_records"],files,"input")
    outputs=_original_records(main["generated_evidence_records"],files,"output")
    geometry_record=_declared(main["geometry_report"],inputs,"geometry")
    if geometry_record["sha256"]!=main["input_geometry_report_sha256"]:
        raise ValueError("The main report's original geometry identity changed")
    geometry,missing=bind_geometry(env,geometry_record)
    if geometry is None or missing:
        raise ValueError("A final R723 report lost its complete original geometry prerequisites")
    core=parent.current_core(geometry,files,r)
    ports=parent.exact_ports(geometry,core,r,beta)
    prepass=preview_directional(geometry,core,files,r,g,k,beta,parent)
    current_sources=parent.complete_sources(geometry,files,r,env["paths"])
    sources=_bind_complete_source_copies(main["source_files"],current_sources,files,inputs,"source")
    proofs=_bind_complete_source_copies(main["proof_sources"],env["proofs"],files,inputs,"proof")
    field,cover=build_field_cover(geometry,sources,beta,parent)
    _equal(main["current_complete_core"],core,"all current core words")
    _equal(main["closed_assembly"],ports,"complete exact ports/phase proof")
    _equal(main["original_full_leaf_sequence_sha256"],prepass["original_leaf_sequence_sha256"],
        "complete original ordered leaf union")
    _equal(main["original_target_beta_intervals"],prepass["retained_legacy_target_intervals"],
        "retained legacy sufficient interval")
    _equal(main["R723_directional_target_beta_intervals"],prepass["directional_target_intervals"],
        "R723 full exact parameter interval")
    _equal(main["strict_positive_support_beta_intervals"],prepass["strict_positive_support_intervals"],
        "positive support fallback interval")
    _equal(main["beta_selection_purpose"],prepass["selection_purpose"],"actual parameter choice")
    listed=main["directional_range_evidence_records"]
    if not isinstance(listed,list):
        raise ValueError("Every complete directional range record is required")
    index=0
    def check_range(definition):
        nonlocal index
        if index>=len(listed):
            raise ValueError("The R723 evidence omitted a complete original range")
        child=_declared(listed[index],outputs,"directional range")
        target=report_path.parent/"directional-ranges"/("range-"+str(index).zfill(6)+".json")
        if Path(child["path"]).resolve()!=target:
            raise ValueError("Preserve the actual range's original same-output-directory path")
        document,_=files.read_json(child)
        expected=chunk_document(definition,field,cover,main["execution"],report_path)
        _equal(document,expected,"complete original directional range "+str(index))
        index+=1
        return child
    chunk_rows=main["support_chunk_rows"]
    if type(chunk_rows) is not int or chunk_rows<1:
        raise ValueError("The exact positive range packaging count changed")
    support,chunks=second_pass_directional(geometry,core,prepass,files,r,g,k,
        parent,chunk_rows,check_range)
    if index!=len(listed) or chunks!=listed:
        raise ValueError("The final range sequence has omitted or extra records")
    _equal(main["formal_common_support_calculation"],support,"full same-field directional calculation")
    closed_paid=ports["complete_closed_C2_immersion_certified"]
    paid=closed_paid and support is not None
    _equal(main["strict_positive_support_proof"],support if closed_paid else None,
        "closed support attribution")
    a=geometry["context"]["actual"]
    expected=dict(
        actual_current_full_point_sha256=a["current_full_point_sha256"],
        actual_snapshot_identity_sha256=a["actual_snapshot_identity_sha256"],
        complete_original_model_identity_sha256=a["model_identity_sha256"],
        exact_fixed_target_identity_sha256=a["exact_fixed_target_identity_sha256"],
        complete_current_scientific_source_role_count=137,
        complete_geometry_leaf_count=geometry["stats"].count,
        full_target_upper_leaf_count=geometry["stats"].count,
        full_target_lower_leaf_count=geometry["stats"].count,
        original_geometry_binding_identity_sha256=geometry["identity"],
        complete_closed_C2_immersion_certified=True if closed_paid else None,
        all_physical_phases_C2_continuous=True if closed_paid else None,
        formal_constructed_image_D_upper=str(prepass["D"]),
        complete_marked_surface_D_upper=str(prepass["D"]) if closed_paid else None,
        all_R723_directional_evidence_roles_paid=bool(paid),
        all_physical_phases_embedded=True if paid else None,
        outward_orientation_certified=True if paid else None)
    if paid:
        package_record=_declared(main["actual_R723_directional_evidence_package"],outputs,"R723 instantiation")
        if Path(package_record["path"]).resolve()!=report_path.parent/"complete-R723-directional-evidence.json":
            raise ValueError("The original complete R723 package path changed")
        package,_=files.read_json(package_record)
        recomputed=directional_instantiation(geometry,core,ports,prepass,support,sources,proofs,
            field,cover,chunks,main["execution"],report_path)
        _equal(package,recomputed,"entire independent R723 instantiation")
        expected.update(R723_field_identity_sha256=field["identity_sha256"],
            R723_coverage_identity_sha256=cover["identity_sha256"],
            common_positive_beta=str(support["common_beta"]),
            common_sigma_lower=str(support["complete_activity_and_cap_sigma_lower"]),
            complete_marked_curvature_upper=str(support["complete_marked_curvature_upper"]),
            R723_marked_directional_ratio_lower=str(support["complete_marked_directional_ratio_lower"]),
            R723_activity_directional_ratio_lower=str(support["complete_activity_directional_ratio_lower"]),
            R723_cap_directional_ratio_lower=str(support["complete_cap_directional_ratio_lower"]),
            R723_directional_reach_lower=str(support["complete_marked_R723_reach_lower"]),
            R650_reach_lower=str(support["R650_reach_lower"]),
            reach_over_D_lower=str(support["complete_marked_R723_reach_lower"]/prepass["D"]),
            reach_standard_sufficient=support["requested_complete_reach_condition_paid"],
            R723_curvature_target_paid=support["requested_curvature_condition_paid"],
            R723_directional_support_target_paid=support["requested_directional_support_paid"])
    else:
        package_record=None
        for key in ("actual_R723_directional_evidence_package","R723_field_identity_sha256",
                "R723_coverage_identity_sha256","common_positive_beta","common_sigma_lower",
                "complete_marked_curvature_upper","R723_marked_directional_ratio_lower",
                "R723_activity_directional_ratio_lower","R723_cap_directional_ratio_lower",
                "R723_directional_reach_lower","R650_reach_lower","reach_over_D_lower",
                "reach_standard_sufficient","R723_curvature_target_paid","R723_directional_support_target_paid"):
            expected[key]=None
    gram=geometry["report"]["accurate_global_bounds"]["relative_Gram_error_operator_norm_upper"]
    expected.update(
        all_phase_same_target_relative_Gram_operator_error_upper=
            str(F(gram)) if closed_paid and gram is not None else None,
        all_phase_relative_Gram_standard_sufficient=
            F(gram)<=F(1,1000000) if closed_paid and gram is not None else None,
        complete_closed_geometry_certified=True if
            (paid and support["requested_complete_reach_condition_paid"]) else None)
    for key,value in expected.items():
        _equal(main.get(key),value,"main "+key)
    tube_record=_declared(main["R716_outward_tube_evidence"],outputs,"unmarked tube")
    if Path(tube_record["path"]).resolve()!=report_path.parent/"R716-unmarked-outward-tube.json":
        raise ValueError("The unmarked sidecar must remain beside its actual complete main report")
    tube,_=files.read_json(tube_record)
    recomputed_tube=unmarked_body_interpretation(geometry,core,ports,support,prepass,
        proofs,sources,report_path)
    _equal(tube,recomputed_tube,"entire independently unmarked R716 sidecar")
    for key,value in {
        "unmarked_all_phase_embedding_certified":recomputed_tube["unmarked_all_phase_embedding_and_outwardness_certified"],
        "unmarked_reach_lower":recomputed_tube["unmarked_reach_lower"],
        "mark_height_strictly_below_unmarked_reach":recomputed_tube["mark_height_strictly_below_unmarked_reach"],
        "R716_body_and_twelve_moment_additivity_interpretation_certified":
            recomputed_tube["R716_volume_and_all_twelve_raw_moment_additivity_interpretation_certified"],
    }.items():
        _equal(main.get(key),value,"main "+key)
    holding=prepare_holding(prepass,ports)
    gripping=parent.grip(geometry,core,prepass["D"],holding,closed_paid)
    original=holding["original_complete_box_distance_lower"]
    _equal(main["original_complete_box_distance_lower"],original,"original all-target box bound")
    expected_flow=dict(main)
    if paid and main["R718_optional_bound_status"]=="complete-directed-rational-lower-bound":
        gripping=apply_flow_bound(geometry,core,ports,support,proofs,expected_flow,
            report_path,holding,parent,prepass["D"])
        for key in ("R718_flow_distance_lower","R718_flow_distance_evidence","R718_flow_distance_used",
                "R719_uniform_axis_ratio_proved","R718_optional_bound_status"):
            _equal(main.get(key),expected_flow[key],"optional "+key)
    else:
        allowed=("unavailable-memory-original-box-bound-retained",) if paid else (
            "complete-closed-support-not-yet-paid",)
        if main["R718_optional_bound_status"] not in allowed:
            raise ValueError("The complete optional-bound status is inconsistent")
        for key in ("R718_flow_distance_lower","R718_flow_distance_evidence",
                "R718_flow_distance_used","R719_uniform_axis_ratio_proved"):
            if main.get(key) is not None:
                raise ValueError("An unpaid optional flow claim must remain null")
    _equal(main["whole_target_distance"],holding,"all upper/lower/cap image boxes and optional flow")
    _equal(main["grip_evidence"],gripping,"entire fixed grip")
    for key,value in {
        "grip_exists":gripping["actual_upper_closed_material_graph_disk_exists"],
        "grip_diameter_lower":gripping["grip_image_diameter_lower"],
        "grip_size_standard_sufficient":gripping["grip_size_standard_sufficient"],
        "pointwise_grip_stabilizer_including_reflections_is_identity":
            gripping["pointwise_grip_stabilizer_including_reflections_is_identity"],
        "delta_hold_lower":gripping["delta_hold_lower"],
        "delta_hold_over_D_lower":gripping["delta_hold_over_D_lower"],
        "delta_hold_standard_sufficient":gripping["delta_hold_standard_sufficient"],
        "delta_hold_stronger_target_sufficient":gripping["delta_hold_stronger_target_sufficient"],
    }.items():
        _equal(main.get(key),value,"main "+key)
    expected_output_paths={str(Path(v["path"]).resolve()) for v in chunks}
    expected_output_paths.add(str(Path(tube_record["path"]).resolve()))
    if package_record is not None:
        expected_output_paths.add(str(Path(package_record["path"]).resolve()))
    if set(outputs)!=expected_output_paths:
        raise ValueError("Every generated evidence output must be accounted for exactly")
    for key in ("new_working_F_J_root_calls","new_accurate_root_or_integrand_calls"):
        if type(main.get(key)) is not int or main[key]!=0:
            raise ValueError("This source only consumes already accurate complete fields")
    if (main.get("delta_E_positive") is not None or main.get("delta_E_lower") is not None
            or main.get("research_goal_completed") is not False
            or main.get("working_field_word_error_bound_produced") is not False):
        raise ValueError("Do not promote independent noncongruence or working-word error obligations")
    files.recheck()
    return dict(schema=SCHEMA+"-complete-consumption-validation",
        final_main_report=record,complete_main_and_exact_sidecars_reread=True,
        original_full_streams_and_normal32_and_domain_reread=True,
        source_copies_checked_by_entire_SHA_and_bytes_with_original_paths_retained=True,
        actual_current_full_point_sha256=a["current_full_point_sha256"],
        actual_model_identity_sha256=a["model_identity_sha256"],
        actual_snapshot_identity_sha256=a["actual_snapshot_identity_sha256"],
        exact_fixed_target_identity_sha256=a["exact_fixed_target_identity_sha256"],
        original_geometry_binding_identity_sha256=geometry["identity"],
        original_normal_binding_identity_sha256=geometry["context"]["binding_identity"],
        R723_evidence_available=bool(paid),
        R723_reach_lower=None if not paid else support["complete_marked_R723_reach_lower"],
        R718_actual_marked_sigma=None if not paid else support["complete_activity_and_cap_sigma_lower"],
        R716_sidecar_record=tube_record,R716_independently_recomputed_sidecar=tube,
        complete_directional_package=package_record,
        complete_source_records=sources,complete_proof_records=proofs,
        original_eight_role_beta_claims_not_fabricated=True,
        all_bound_input_and_generated_output_bytes_rechecked=True,
        new_F_J_root_or_integrand_calls=0)



def parse_args():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo",type=Path,required=True)
    parser.add_argument("--geometry-report",type=Path,required=True)
    parser.add_argument("--expected-geometry-report-sha256")
    parser.add_argument("--outdir",type=Path,required=True)
    parser.add_argument("--support-chunk-rows",type=int,default=4096)
    args=parser.parse_args()
    if args.support_chunk_rows<1:
        parser.error("--support-chunk-rows must be positive and changes packaging only")
    return args


def main():
    args=parse_args()
    require_actions()
    started=time.monotonic()
    args.repo=args.repo.resolve()
    env=load_environment(args.repo)
    parent,r,g,k,beta,files,outputs=(env[name] for name in
        ("parent","r","g","k","beta","files","outputs"))
    actual_execution=execution(args.repo)
    report=empty_directional_report(actual_execution,parent)
    outdir=files.protect_output(args.outdir)
    if outdir.exists() and any(outdir.iterdir()):
        raise ValueError("Use a fresh R723 namespace; prior partial evidence is not reused")
    outdir.mkdir(parents=True,exist_ok=True)
    report_path=outdir/"report.json"

    def save():
        report["elapsed_seconds_binary64_hex"]=float(time.monotonic()-started).hex()
        return write_json(report_path,report,r,outputs,replace=True)

    save()
    try:
        proofs=env["proofs"]
        report["proof_sources"]=proofs
        record=r.file_record(args.geometry_report)
        if (args.expected_geometry_report_sha256 is not None
                and record["sha256"]!=args.expected_geometry_report_sha256):
            raise ValueError("The caller's expected whole geometry report changed")
        report.update(geometry_report=record,input_geometry_report_sha256=record["sha256"])
        geometry,missing=bind_geometry(env,record)
        if geometry is None:
            files.recheck()
            report.update(status="upstream-global-conditions-unpaid",
                reason="The complete original geometry prerequisites are not paid",
                remaining=missing,all_bound_input_and_generated_evidence_bytes_rechecked=True,
                actual_complete_input_records=list(files.records.values()),
                generated_evidence_records=[])
            output=save()
            print(json.dumps(dict(schema=SCHEMA,report=output,complete=False,
                status=report["status"],new_field_root_calls=0),sort_keys=True))
            return 0
        files.protect_output(outdir)
        core=parent.current_core(geometry,files,r)
        ports=parent.exact_ports(geometry,core,r,beta)
        prepass=preview_directional(geometry,core,files,r,g,k,beta,parent)
        holding=prepare_holding(prepass,ports)
        closed_paid=ports["complete_closed_C2_immersion_certified"]
        gripping=parent.grip(geometry,core,prepass["D"],holding,closed_paid)
        sources=parent.complete_sources(geometry,files,r,env["paths"])
        field,cover=build_field_cover(geometry,sources,beta,parent)
        context=geometry["context"]
        actual=context["actual"]
        report.update(actual_current_full_point_sha256=actual["current_full_point_sha256"],
            actual_snapshot_identity_sha256=actual["actual_snapshot_identity_sha256"],
            complete_original_model_identity_sha256=actual["model_identity_sha256"],
            exact_fixed_target_identity_sha256=actual["exact_fixed_target_identity_sha256"],
            complete_current_scientific_source_role_count=137,
            complete_closed_C2_immersion_certified=True if closed_paid else None,
            all_physical_phases_C2_continuous=True if closed_paid else None,
            source_files=sources,closed_assembly=ports,current_complete_core=core,
            whole_target_distance=holding,grip_evidence=gripping,
            original_complete_box_distance_lower=encoded(holding["rigorous_delta_hold_lower"]),
            formal_constructed_image_D_upper=str(prepass["D"]),
            complete_marked_surface_D_upper=str(prepass["D"]) if closed_paid else None,
            original_geometry_binding_identity_sha256=geometry["identity"],
            complete_geometry_leaf_count=geometry["stats"].count,
            full_target_upper_leaf_count=holding["all_upper_target_leaves_read"],
            full_target_lower_leaf_count=holding["all_lower_target_leaves_included"],
            original_target_beta_intervals=prepass["retained_legacy_target_intervals"],
            R723_directional_target_beta_intervals=prepass["directional_target_intervals"],
            strict_positive_support_beta_intervals=prepass["strict_positive_support_intervals"],
            beta_selection_purpose=prepass["selection_purpose"],
            original_full_leaf_sequence_sha256=prepass["original_leaf_sequence_sha256"],
            grip_exists=gripping["actual_upper_closed_material_graph_disk_exists"],
            grip_diameter_lower=encoded(gripping["grip_image_diameter_lower"]),
            grip_size_standard_sufficient=gripping["grip_size_standard_sufficient"],
            pointwise_grip_stabilizer_including_reflections_is_identity=
                gripping["pointwise_grip_stabilizer_including_reflections_is_identity"],
            delta_hold_lower=encoded(gripping["delta_hold_lower"]),
            delta_hold_over_D_lower=encoded(gripping["delta_hold_over_D_lower"]),
            delta_hold_standard_sufficient=gripping["delta_hold_standard_sufficient"],
            delta_hold_stronger_target_sufficient=gripping["delta_hold_stronger_target_sufficient"])
        gram=geometry["report"]["accurate_global_bounds"]["relative_Gram_error_operator_norm_upper"]
        if closed_paid and gram is not None:
            report["all_phase_same_target_relative_Gram_operator_error_upper"]=str(F(gram))
            report["all_phase_relative_Gram_standard_sufficient"]=F(gram)<=F(1,1000000)
        def emit(definition):
            number=definition["index"]
            document=chunk_document(definition,field,cover,actual_execution,report_path)
            return write_json(outdir/"directional-ranges"/("range-"+str(number).zfill(6)+".json"),
                document,r,outputs)
        support,chunks=second_pass_directional(geometry,core,prepass,files,r,g,k,
            parent,args.support_chunk_rows,emit)
        report["directional_range_evidence_records"]=chunks
        package=None
        if closed_paid and support is not None:
            document=directional_instantiation(geometry,core,ports,prepass,support,sources,proofs,
                field,cover,chunks,actual_execution,report_path)
            package=write_json(outdir/"complete-R723-directional-evidence.json",document,r,outputs)
            report.update(all_physical_phases_embedded=True,
                outward_orientation_certified=True,
                all_R723_directional_evidence_roles_paid=True,
                actual_R723_directional_evidence_package=package,
                R723_field_identity_sha256=field["identity_sha256"],
                R723_coverage_identity_sha256=cover["identity_sha256"],
                common_positive_beta=str(support["common_beta"]),
                common_sigma_lower=str(support["complete_activity_and_cap_sigma_lower"]),
                complete_marked_curvature_upper=str(support["complete_marked_curvature_upper"]),
                R723_marked_directional_ratio_lower=str(support["complete_marked_directional_ratio_lower"]),
                R723_activity_directional_ratio_lower=str(support["complete_activity_directional_ratio_lower"]),
                R723_cap_directional_ratio_lower=str(support["complete_cap_directional_ratio_lower"]),
                R723_directional_reach_lower=str(support["complete_marked_R723_reach_lower"]),
                R650_reach_lower=str(support["R650_reach_lower"]),
                reach_over_D_lower=str(support["complete_marked_R723_reach_lower"]/prepass["D"]),
                reach_standard_sufficient=support["requested_complete_reach_condition_paid"],
                R723_curvature_target_paid=support["requested_curvature_condition_paid"],
                R723_directional_support_target_paid=support["requested_directional_support_paid"])
        tube=unmarked_body_interpretation(geometry,core,ports,support,prepass,proofs,sources,report_path)
        tube_record=write_json(outdir/"R716-unmarked-outward-tube.json",tube,r,outputs)
        report.update(unmarked_all_phase_embedding_certified=
                tube["unmarked_all_phase_embedding_and_outwardness_certified"],
            unmarked_reach_lower=encoded(tube["unmarked_reach_lower"]),
            mark_height_strictly_below_unmarked_reach=
                tube["mark_height_strictly_below_unmarked_reach"],
            R716_body_and_twelve_moment_additivity_interpretation_certified=
                tube["R716_volume_and_all_twelve_raw_moment_additivity_interpretation_certified"],
            R716_outward_tube_evidence=tube_record)
        remaining=list(tube["remaining"])
        if not closed_paid:
            remaining.extend(ports["remaining"])
        if support is None:
            remaining.append("No single positive beta was proved from every complete original activity leaf and both fixed marked caps")
        if closed_paid and support is not None:
            try:
                gripping=apply_flow_bound(geometry,core,ports,support,proofs,report,
                    report_path,holding,parent,prepass["D"])
            except MemoryError:
                # The optional bound may fail after allocating some result data.
                # Restore the whole original box/grip state, never a partial gain.
                holding=prepare_holding(prepass,ports)
                gripping=parent.grip(geometry,core,prepass["D"],holding,closed_paid)
                report.update(
                    R718_optional_bound_status="unavailable-memory-original-box-bound-retained",
                    R718_flow_distance_lower=None,R718_flow_distance_evidence=None,
                    R718_flow_distance_used=None,R719_uniform_axis_ratio_proved=None,
                    whole_target_distance=holding,grip_evidence=gripping,
                    delta_hold_lower=encoded(gripping["delta_hold_lower"]),
                    delta_hold_over_D_lower=encoded(gripping["delta_hold_over_D_lower"]),
                    delta_hold_standard_sufficient=gripping["delta_hold_standard_sufficient"],
                    delta_hold_stronger_target_sufficient=gripping["delta_hold_stronger_target_sufficient"])
        if report["reach_standard_sufficient"] is not True:
            remaining.append("The complete R723 all-phase reach lower has not met 0.03 times the same complete D upper")
        if gripping["grip_size_standard_sufficient"] is not True:
            remaining.append("The actual fixed grip has not paid its radius and 0.2D size")
        if gripping["delta_hold_standard_sufficient"] is not True:
            remaining.append("The complete-image lower has not met the original 0.05D standard")
        if gripping["delta_hold_stronger_target_sufficient"] is not True:
            remaining.append("The complete-image lower has not met the stronger 0.2D target")
        if report["all_phase_relative_Gram_standard_sufficient"] is not True:
            remaining.append("The complete closed/all-phase relative Gram error has not met 1e-6")
        remaining.extend(["Delta_E positivity requires its separate complete same-field evidence",
            "The actual twelve R716 flux channels and centred moment are not computed here",
            "Same-target nonlinear convergence and exact-solution approximation remain unproved",
            "Required full mesh exports are not produced here",
            "No old eight-role beta claim or old beta-consumer success is asserted by this distinct branch"])
        files.recheck()
        outputs.recheck()
        report.update(complete=True,status="complete-same-field-consumption",remaining=remaining,
            complete_closed_geometry_certified=True if
                (closed_paid and support is not None and
                    support["requested_complete_reach_condition_paid"]) else None,
            all_bound_input_and_generated_evidence_bytes_rechecked=True,
            strict_positive_support_proof=encoded(support) if closed_paid else None,
            formal_common_support_calculation=encoded(support),
            complete_accurate_sixjet_evidence_scope=parent.ACCURATE_CLAIM_SCOPE,
            actual_complete_input_records=list(files.records.values()),
            generated_evidence_records=list(outputs.records.values()),
            support_chunk_rows=args.support_chunk_rows,
            support_chunk_partition_does_not_change_any_mathematical_domain=True,
            all_eight_original_beta_evidence_roles_paid=False,
            actual_outward_beta_package=None)
        output=save()
        print(json.dumps(dict(schema=SCHEMA,report=output,complete=True,
            R723_evidence_paid=report["all_R723_directional_evidence_roles_paid"],
            all_phase_embedded=report["all_physical_phases_embedded"],
            reach_paid=report["reach_standard_sufficient"],
            R650_eight_roles_paid=False,research_goal_completed=False),sort_keys=True))
        return 0
    except Exception as error:
        promoted=("complete_closed_C2_immersion_certified","all_physical_phases_C2_continuous",
            "all_physical_phases_embedded","outward_orientation_certified",
            "all_phase_same_target_relative_Gram_operator_error_upper",
            "all_phase_relative_Gram_standard_sufficient","complete_marked_surface_D_upper",
            "complete_marked_curvature_upper","common_positive_beta","common_sigma_lower",
            "R650_reach_lower","R723_directional_reach_lower",
            "R723_marked_directional_ratio_lower","R723_activity_directional_ratio_lower",
            "R723_cap_directional_ratio_lower","R723_curvature_target_paid",
            "R723_directional_support_target_paid","reach_over_D_lower","reach_standard_sufficient",
            "grip_exists","grip_diameter_lower","grip_size_standard_sufficient",
            "pointwise_grip_stabilizer_including_reflections_is_identity","delta_hold_lower",
            "delta_hold_over_D_lower","delta_hold_standard_sufficient",
            "delta_hold_stronger_target_sufficient","complete_closed_geometry_certified",
            "original_complete_box_distance_lower","R718_flow_distance_lower",
            "R718_flow_distance_evidence","R718_flow_distance_used","R719_uniform_axis_ratio_proved",
            "unmarked_all_phase_embedding_certified","unmarked_reach_lower",
            "mark_height_strictly_below_unmarked_reach",
            "R716_body_and_twelve_moment_additivity_interpretation_certified")
        report["uncommitted_provisional_claims_before_failure"]={key:report.get(key) for key in promoted}
        for key in promoted:
            report[key]=None
        report.update(complete=False,status="source-or-complete-bound-consumption-failed",
            reason=str(error),exception_type=type(error).__name__,
            R718_optional_bound_status="invalidated-by-complete-consumption-failure",
            all_R723_directional_evidence_roles_paid=False,
            actual_R723_directional_evidence_package=None,
            R723_field_identity_sha256=None,R723_coverage_identity_sha256=None,
            directional_range_evidence_records=[],strict_positive_support_proof=None,
            all_eight_original_beta_evidence_roles_paid=False,actual_outward_beta_package=None,
            all_bound_input_and_generated_evidence_bytes_rechecked=False,
            failure_is_not_geometric_impossibility=True)
        save()
        raise


if __name__ == "__main__":
    raise SystemExit(main())
