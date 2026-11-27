#!/usr/bin/env python3
"""Complete source-bound closed/phase/grip evidence from actual fixed-Fejer whole leaves.

This is an independent Actions-only consumer. It reads the complete original
accurate normal-chain, sixjet and continuous geometry journals. It constructs
no new working field, root, derivative, integrand or sampled surface. A
complete connected C2 parameter sphere and continuous oriented normal are
instantiated from the source-specific port proof. Positive A-support then
proves embedding/outwardness by R650, never the other way round. Its original
eight evidence roles, exact lower-reflection extension and original e0b44
consumer input are actually written only after their assumptions are paid.

The four exact phase-core witnesses are compared to EVERY upper/lower
position box and BOTH complete marked caps. Delta_hold has no rigid alignment.
A wide target cover gives an unpaid lower bound, not a material displacement.
Delta_E, exact-isometry existence, convergence and mesh exports remain separate.
After the original complete closed/outward/support package is paid, R718 adds
a pure rational whole-image flow bound. It reads every actual current core
coefficient, retains the complete original box bound, and takes their maximum.
No mutable progress or unreturned field is accepted as an accurate input.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as F
import gzip
import hashlib
import importlib.util
import itertools
import json
import math
import os
from pathlib import Path
import subprocess
import sys
import time
import uuid

SCHEMA = "actual-fixed-fejer-meridian-batched-complete-closed-phase-grip-evidence-v1"
TOPIC = "topics/visible-flex-larger-amplitude"
BRIDGE = ("fixed_fejer_meridian_batched_complete_geometry_support_beta_bridge.py",
    "d0b72820b7a7f8f872d2cb460e6f2fba3a685804e200ac4f35f7f12bf33cb0e7")
GEOMETRY = ("fixed_fejer_meridian_batched_continuous_gram_curvature_support.py",
    "d0d0f45332ece0a63192b4e80c7c318635ba1068208bad45bec2a136781934a5")
BETA = ("same_field_positive_support_parameter.py",
    "e0b44e22fa9e41109ccdeb1c3908aeca60c5c4a18f90dca088f8c9e0243b5991")
PROOFS = {
    "fixed_fejer_current_source_adapter": (
        TOPIC+"/notes/2026-11-27-meridian-batched-closed-phase-grip-r718-source-adapter.md",
        "4eb8967fbb7e5ad5a6220825320b943fca306db124c4c5225f2e4de6c3561f21"),
    "fixed_fejer_stage_observed_algorithm_parent_adapter": (
        TOPIC+"/notes/2026-11-27-stage-observed-closed-phase-grip-r718-source-adapter.md",
        "1ae4af46df209bff88922a2c620ff8f2baf5e71a4001ecc745d8926c24781c6f"),
    "fixed_fejer_closed_algorithm_parent_adapter": (
        TOPIC+"/notes/2026-11-27-fixed-fejer-closed-phase-grip-source-adapter.md",
        "16c15c597359b3017c9e050b5ddef94950d508e88a9c05fa726300cd129b726e"),
    "R718_complete_flow_distance": (
        TOPIC+"/results/R718-positive-definite-flow-distance-and-whole-image-held-witness.md",
        "fd92e569e7d793367f96a0748be5cfc54670a6333c18f413f8cce27da1083feb"),
    "R719_all_current_core_modes": (
        TOPIC+"/results/R719-fixed-first-three-fejer-modes-preserve-current-axis-gap.md",
        "f043c75457173c9cfa5bbf7b0b9710049edfcb075d31d474231554285768cff7"),
    "R717_fixed_chart_design_only": (
        TOPIC+"/results/R717-fixed-fejer-seven-mode-chart-and-whole-image-bounds.md",
        "9727ed8b7e48d9aa4a343c1d3dcd666a9fbc0d74f876df1ee80494df7b337378"),
    "run10_algorithm_parent_adapter": (
        TOPIC+"/notes/2026-11-27-run10-closed-phase-grip-source-adapter.md",
        "b378593327e31a91385d4f5397c8fbb9294147febb843060941bfbaba92584e7"),
    "source_specific_ports": (
        TOPIC+"/notes/2026-11-27-complete-normal-closed-phase-and-grip-source-interface-audit.md",
        "e111e190224b0b8d6194f90411adb23062c77e71e54ff9d52ea712d19b7129c0"),
    "R248": (TOPIC+"/results/R248-finite-C2-phase-family-and-global-reductions.md",
        "7b6dd9566b024484c5908366ff3f78321cd6ec28a8d0c65df1a4a680b9f9c731"),
    "R650": (TOPIC+"/results/R650-positive-definite-flow-support-reach.md",
        "35d79e32b8ca18d391576bff4f6b5427e67218a3dadc22e404de0680c2e7982f"),
    "R661_components_only": (TOPIC+"/results/R661-complete-nonplanar-activity-and-four-fixed-markers.md",
        "b3a2eda488719544a0fc1a57cf83a306a2c3d9b6df638b823379e0c45170ddcd"),
    "R715": (TOPIC+"/results/R715-reference-centred-normal-sixjets-and-error-ledger.md",
        "e220528af01982c543da46f64541dc18c2a57bbb17bac4afbd7fee5db6e7e1c0"),
    "R716": (TOPIC+"/results/R716-asymmetric-fixed-caps-and-centred-volume-moment.md",
        "5e3ebdf00fa7fcef33e7ae7e58dcd81dadd77bde2b87f618726d1ee6af444989"),
    "original_problem": ("topics/visible-flexible-closed-surface/README.md",
        "d0119679e6c4d855f1f322fa6daa68cd2a30c795b14d0b124e6674459855fc23"),
}
FLOW_LOG_TERMS = 32
FLOW_EXP_TERMS = 32
FLOW_BINARY_BITS = 96
GRIP_RADIUS = F(9,20)
MARK_HEIGHT = F(1,1000)
MARK_CENTRE = F(3,20)
MARK_RADII = (F(1,25), F(9,200), F(1,20), F(11,200))
SUPPORT_RADIUS = F(1,5)
RADIAL_EXTENSION = "same_field_lower_reflection_and_all_activity_seams"
PORT_SCHEMA = SCHEMA+"-exact-ports-and-phase"
IMAGE_SCHEMA = SCHEMA+"-whole-target-distance"
ACCURATE_CLAIM_SCOPE = dict(
    mathematical_object="the same fixed accurate physical sixjet field on the entire exact domain",
    all_original_root_boxes_and_32_stage_chains_rechecked=True,
    full_angular_branch_glue_and_periodicity_rechecked=True,
    all_whole_radial_cells_and_accurate_affine_domains_rechecked=True,
    exact_scalar_reference_and_all_original_lift_terms_retained=True,
    all_errors_needed_for_the_actual_outward_enclosures_included=True,
    working_field_word_error_bound_produced=False,
    ordinary_working_sixjet_words_used_as_an_accurate_enclosure=False)
EIGHT_ROLES = (
    "current_field_binding", "physical_six_jets",
    "complete_activity_domain_and_seams", "closed_sphere_immersion",
    "all_physical_phases", "diameter_bound", "activity_curvature_bound",
    "fixed_cap_parameters",
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


def proof_files(repo, files, r):
    result={}
    for role,(name,digest) in PROOFS.items():
        source_path=Path(repo).resolve()/name
        if role=="original_problem" and not source_path.exists():
            # The controller checks out this topic sparsely. Materialize only
            # this declared public proof from the same frozen source commit.
            raw=subprocess.check_output(["git","show","HEAD:"+name],cwd=Path(repo).resolve())
            if hashlib.sha256(raw).hexdigest()!=digest:
                raise ValueError("The complete original problem source changed")
            source_path.parent.mkdir(parents=True,exist_ok=True)
            with source_path.open("xb") as handle:
                handle.write(raw)
        record=r.file_record(source_path)
        if record["sha256"]!=digest:
            raise ValueError("The complete mathematical proof source changed: "+role)
        files.verify(record)
        result[role]=record
    return result


def literal_word(value):
    if not isinstance(value,str):
        raise ValueError("The full core provenance retains canonical binary64 hex words")
    word=float.fromhex(value)
    if not math.isfinite(word) or word.hex()!=value:
        raise ValueError("A current coefficient is not a canonical finite binary64 word")
    return F(word)


def current_core(geometry, files, r):
    """Read all x again; no old reference core is used for the free 157 slots."""
    import numpy as np
    context=geometry["context"]
    actual=context["actual"]
    record=actual["current_point_arrays_file"]
    path=files.verify(record)
    with np.load(path,allow_pickle=False) as data:
        if set(data.files)!={"x"}:
            raise ValueError("Use the original full free-point packet")
        x=np.array(data["x"],copy=True)
    files.verify(record,force=True)
    expected=(160-3)+(3*923-3)*482+1
    if x.dtype!=np.dtype("float64") or x.shape!=(expected,) or not np.isfinite(x).all():
        raise ValueError("The entire original M160/J923/free-height layout changed")
    digest=hashlib.sha256(str(x.dtype).encode())
    digest.update(json.dumps(list(x.shape)).encode())
    digest.update(np.ascontiguousarray(x).tobytes())
    if digest.hexdigest()!=actual["current_full_point_sha256"]:
        raise ValueError("The actual full point differs from the complete geometry input")
    base=actual["complete_model"]["base_complete_model"]
    fixed=base.get("fixed_core_first3")
    if not isinstance(fixed,list) or len(fixed)!=3:
        raise ValueError("All three actual fixed coefficients are required")
    words=list(fixed)+[float(v).hex() for v in x[:157]]
    coefficients=[literal_word(v) for v in words]
    H=F(float(x[-1]))
    if H!=context["H"].lo or context["H"].lo!=context["H"].hi:
        raise ValueError("The current cap height must be the same actual final free word")
    if (base.get("M")!=160 or base.get("J")!=923
            or base.get("fixed_chart_core_sha256")!=actual["fixed_chart_core_sha256"]
            or base.get("omega_basis",{}).get("fixed_zero_radial_slots")!=[0,2766,2767]):
        raise ValueError("The source-specific whole point/port layout changed")
    # This is the actual support-function curve, not radial graph sampling.
    X=1+sum(coefficients,F(0))
    Y=1+sum((c if (j+1)%2==0 else -c for j,c in enumerate(coefficients)),F(0))
    return dict(complete_point=record,current_full_point_sha256=digest.hexdigest(),
        current_core_binary64_hex=words,current_core_rational=[str(v) for v in coefficients],
        fixed_coefficient_count=3,free_core_coefficient_count=157,
        current_core_word_identity_sha256=canonical(words),
        height_binary64_hex=float(x[-1]).hex(),H=H,X=X,Y=Y,
        phase_one_core_points=[[F(0),X,F(0)],[F(0),-X,F(0)],
            [Y,F(0),F(0)],[-Y,F(0),F(0)]],
        phase_one_alpha_over_pi="1/2",phase_one_t="1",
        endpoint_values_use_all_current_coefficients=True,
        material_point_displacement_used_as_image_distance=False)


def exact_ports(geometry, core, r, beta):
    c=geometry["context"]
    a=c["actual"]
    model=a["complete_model"]
    base=model["base_complete_model"]
    fixed_reference=base["complete_axisymmetric_reference_model"]
    if (model.get("source_sha256")!=r.ACTUAL_MODEL_SOURCE
            or base.get("source_sha256")!=r.ACTUAL_BASE
            or base.get("original_axisymmetric_reference_source_sha256")!=
                r.ACTUAL_INPUT_SOURCE_PINS["reference"][1]
            or canonical(model)!=a["model_identity_sha256"]
            or fixed_reference.get("source_sha256")!=
                r.ACTUAL_INPUT_SOURCE_PINS["reference"][1]):
        raise ValueError("The complete source-specific endpoint proof does not match this field")
    if (c["point"]["exact_zero_rotation_rows"]!=[0,2766,2767]
            or c["point"]["M"]!=160 or c["point"]["J"]!=923
            or c["point"]["current_point_sha256"]!=core["current_full_point_sha256"]
            or c["point"]["complete_free_variable_count"]!=(160-3)+(3*923-3)*482+1):
        raise ValueError("The full source mask proof and current point disagree")
    supports={}
    for key in ("exact_relative_bubble_nodes","exact_relative_gamma_nodes"):
        values=model[key] if key=="exact_relative_bubble_nodes" else [model[key]]
        triples=[[F(v) for v in t] for t in values]
        if ((key=="exact_relative_bubble_nodes" and len(triples)!=2)
                or any(len(t)!=3 or not 0<t[0]<t[1]<t[2]<1 for t in triples)):
            raise ValueError("Every complete control support stays strictly inside (0,S)")
        supports[key]=values
    seed=base["fixed_supported_unit_seed_model"]
    regions=seed["exact_relative_support_intervals"]
    if len(regions)!=2 or any(len(t)!=2 or not 0<F(t[0])<F(t[1])<1 for t in regions):
        raise ValueError("The fixed reference must return to its original law near both endpoints")
    supports["exact_relative_seed_support_intervals"]=regions
    unit=c["geometry"]["unit_reference_provenance"]
    if (unit.get("complete_reference_source_sha256")!=r.ACTUAL_INPUT_SOURCE_PINS["reference"][1]
            or unit.get("actual_complete_model_T0")!=fixed_reference["T0"]
            or not 0<=F(unit["old_prefix_ap_bound"])<1
            or not 0<F(unit["exact_tail_width"])<F(1,40)
            or F(unit["exact_tail_kappa"])!=F(3,2)
            or unit.get("structural_unit_and_nonnegative_vertical") is not True
            or unit.get("sampled_norm_or_working_clamp_used_as_proof") is not False):
        raise ValueError("The accurate original scalar endpoint law lost its complete branch provenance")
    branch=geometry["report"]["original_complete_angle_branch"]
    if (branch.get("complete") is not True
            or branch.get("exact_angle_domain_over_pi")!=["0","2"]
            or branch.get("actual_branch_check_recomputed_from_complete_original_journals") is not True
            or branch.get("periodic_equation_source_proof_retained") is not True):
        raise ValueError("A complete, glued and periodic accurate selected field is required")
    for name in ("fixed_rho_proof","current_rho_proof"):
        proof=c["geometry"][name]
        if proof.get("all_coefficients_used") is not True or F(proof["lower"])<=0:
            raise ValueError("Use the exact positive chart with every actual coefficient")
    # Structural p4 checks use all true rational components; R661 supplies
    # their whole graph derivative inequalities, never the old activity field.
    centres=[(MARK_CENTRE,F(0)),(F(0),MARK_CENTRE),(-MARK_CENTRE,F(0))]
    for i in range(3):
        for j in range(i):
            ds=sum((centres[i][v]-centres[j][v])**2 for v in range(2))
            if ds<=(MARK_RADII[i]+MARK_RADII[j])**2:
                raise ArithmeticError("The original complete upper p4 support disks are not disjoint")
    strict_cuff=c["R"].lo>SUPPORT_RADIUS
    immersed=(geometry["stats"].normal_unproved==0
        and F(geometry["report"]["accurate_global_bounds"]["normal_norm_lower"])>0)
    c2=bool(strict_cuff and immersed)
    return dict(schema=PORT_SCHEMA,
        current_full_point_sha256=a["current_full_point_sha256"],
        complete_model_identity_sha256=a["model_identity_sha256"],
        accurate_geometry_binding_identity_sha256=geometry["identity"],
        all_actual_32_stages_and_full_circle_glued=True,
        exact_normal_partition=[str(v) for v in c["partition"]],
        exact_zero_omega_radial_rows=[0,2766,2767],
        core_first_second_and_cap_second_omega_jets_remain_free=True,
        compact_support_proof=supports,original_unit_scalar_provenance=unit,
        source_specific_physical_formula="U=(1-h)P+h*Gamma+integral_0^s T-(1-h)*integral_0^S T",
        h="1-10(s/S)^3+15(s/S)^4-6(s/S)^5",
        complete_raw_closure_lift_retained=True,raw_defects_forced_to_zero=False,
        core_port=dict(F="Gamma in z=0",Fs="ez",Fss="horizontal",Fsphi="0",
            Fphi="Gamma_phi",Fphiphi="Gamma_phiphi"),
        cap_port=dict(F="R*er(Theta0)+H*ez",Fs="-er(Theta0)",Fss="0",
            Fphi="R*rho0*et(Theta0)",Fsphi="-rho0*et(Theta0)",
            Fphiphi="R*(rho0_prime*et(Theta0)-rho0^2*er(Theta0))"),
        signed_lower_chart="F(u,phi)=Jz*U(-u,phi), u<=0; Jz=diag(1,1,-1)",
        signed_lower_sixjets=["Jz*U","-Jz*Us","Jz*Uphi","Jz*Uss","-Jz*Usphi","Jz*Uphiphi"],
        lower_oriented_normal="Jz*(Uphi cross Us)",
        lower_positive_s_chart_cross_order="Fs cross Fphi",
        cap_radius_coordinate="r=R+S-s; use Cartesian charts at disk centres",
        material_topology="[-S,S] x S1 with two Cartesian closed disks attached",
        connected_closed_parameter_surface_is_S2=True,
        fixed_p4_recipe=beta.CAP_RECIPE,
        exact_p4_disks_disjoint_within_each_cap=True,
        cap_support_strictly_inside_current_radius=strict_cuff,
        complete_upper_immersion_proved_from_actual_boxes=immersed,
        complete_closed_C2_immersion_certified=c2,
        continuous_global_oriented_unit_normal_certified=c2,
        outwardness_or_embedding_assumed_in_port_proof=False,
        phase=dict(t_interval=["0","1"],alpha="pi*t/2",
            zeta="Theta0^{-1}(Theta0(phi)-alpha)",
            zeta_phi="rho0(phi)/rho0(zeta)",
            zeta_phiphi="rho0_prime(phi)/rho0(zeta)-rho0(phi)^2*rho0_prime(zeta)/rho0(zeta)^3",
            upper="R_alpha U(s,zeta)",lower="Jz R_alpha U(s,zeta)",
            whole_image="R_alpha(activity_upper union activity_lower) union fixed_marked_caps",
            cap_material_points_fixed=True,all_phases_by_exact_formula=True,
            time_C2_strong_continuity_certified=c2,
            time_C2_Banach_differentiability_claimed=False,
            half_turn_normal_root_covariance_assumed=False,
            relative_Gram_supremum_preserved_on_activity=True,
            fixed_cap_induced_metric_error="0",
            actual_principal_curvature_preserved_on_activity=True,
            ordinary_all_phase_marked_reach_invariance_claimed=False),
        remaining=[] if c2 else ["Strict cap collar or full upper immersion is not paid"])


def rational_box(value, dimension):
    if (not isinstance(value,list) or len(value)!=dimension
            or any(not isinstance(v,list) or len(v)!=2 for v in value)):
        raise ValueError("Retain every coordinate of the accurate whole position box")
    box=[[F(v) for v in row] for row in value]
    if any(lo>hi for lo,hi in box):
        raise ValueError("A whole position enclosure is reversed")
    return box


def distance_square(point, box):
    if len(point)!=3 or len(box)!=3:
        raise ValueError("Use all three actual spatial coordinates")
    return sum((max(lo-p,F(0),p-hi)**2 for p,(lo,hi) in zip(point,box)),F(0))


class CompleteTargetDistance:
    """Every target patch contributes to a minimum, including both entire caps."""
    def __init__(self,core,geometry):
        c=geometry["context"]
        self.points=core["phase_one_core_points"]
        self.minimum=[None]*4
        self.witness=[None]*4
        self.upper_count=0
        self.lower_count=0
        H=core["H"]
        R=c["R"].hi
        for name,z in (("complete-upper-flat-and-p4-cap",[H,H+MARK_HEIGHT]),
                ("complete-lower-flat-and-p4-cap",[-H-MARK_HEIGHT,-H])):
            self.add(name,[[-R,R],[-R,R],z])

    def add(self,name,box):
        for i,point in enumerate(self.points):
            q=distance_square(point,box)
            if self.minimum[i] is None or q<self.minimum[i]:
                self.minimum[i]=q
                self.witness[i]=name

    def leaf(self,name,box):
        self.add(name+"/upper",box)
        self.upper_count+=1
        self.add(name+"/lower",[box[0],box[1],[-box[2][1],-box[2][0]]])
        self.lower_count+=1

    def result(self,core,geometry,k):
        expected=geometry["stats"].count
        if self.upper_count!=expected or self.lower_count!=expected:
            raise ValueError("The full target-image distance omitted an upper or lower leaf")
        if any(v is None or v<0 for v in self.minimum):
            raise ValueError("Every witness needs the complete compact target")
        c=geometry["context"]
        lower=[k.sqrt_bounds(q,c["bits"])[0] for q in self.minimum]
        pos=geometry["stats"].position
        R=c["R"].hi
        hull=[[min(pos[i][0],-R),max(pos[i][1],R)] for i in range(2)]
        X,Y=core["X"],core["Y"]
        axis_terms=[X-hull[1][1],X+hull[1][0],Y-hull[0][1],Y+hull[0][0]]
        whole_hull=max([F(0)]+axis_terms)
        per_patch=max(lower)
        paid=max(whole_hull,per_patch)
        return dict(schema=IMAGE_SCHEMA,actual_point_sha256=core["current_full_point_sha256"],
            source_phase_t="1",source_phase_alpha_over_pi="1/2",
            complete_current_core_word_identity_sha256=core["current_core_word_identity_sha256"],
            source_points=self.points,all_upper_target_leaves_read=self.upper_count,
            all_lower_target_leaves_included=self.lower_count,
            entire_fixed_caps_including_all_p4_components=2,
            target_box_minimum_square_lower=self.minimum,
            minimum_box_identifiers=self.witness,
            per_witness_whole_target_distance_lower=lower,
            complete_target_horizontal_hull=hull,
            whole_hull_axis_expression_lowers=axis_terms,
            whole_hull_distance_lower=whole_hull,
            whole_patch_distance_lower=per_patch,
            rigorous_delta_hold_lower=paid if paid>0 else None,
            computed_nonnegative_lower_including_unpaid_zero=paid,
            positive_lower_paid=paid>0,
            target_is_the_entire_same_S0=True,
            same_material_point_displacement_used=False,
            rigid_alignment_or_grip_stabilizer_quotient_used=False,
            target_only_core_or_activity_used=False,
            proof="For every target patch S_j subset B_j, dist(p,S_j)>=dist(p,B_j). Take the minimum over ALL upper, lower and cap patches, then the maximum over four genuine S_1 core points. The global xy hull supplies a second independent lower bound.",
            zero_means_current_cover_unseparated_not_zero_Hausdorff_distance=True)


def original_leaves(geometry,files,r,g,k):
    """Reread every original whole leaf, not the small report summary alone."""
    total=0
    combined=g.Statistics()
    for block in geometry["blocks"]:
        d=block["definition"]
        record=d["whole_leaf_geometry_stream"]
        path=files.verify(record)
        stats=g.Statistics()
        footer=None
        with gzip.open(path,"rb") as stream:
            raw=stream.readline()
            if not raw.endswith(b"\n"):
                raise ValueError("A whole geometry stream header is incomplete")
            header=r.strict_json(raw)
            if (header.get("schema")!=g.STREAM_SCHEMA
                    or header.get("geometry_binding_identity_sha256")!=geometry["identity"]
                    or header.get("producer_source_sha256")!=GEOMETRY[1]
                    or header.get("current_full_point_sha256")!=
                        geometry["context"]["actual"]["current_full_point_sha256"]):
                raise ValueError("The complete geometry stream source/point changed")
            for raw in stream:
                if not raw.endswith(b"\n"):
                    raise ValueError("An incomplete target or support leaf is not usable")
                item=r.strict_json(raw)
                if item.get("kind")=="complete_continuous_geometry_footer":
                    footer=item
                    break
                if item.get("kind")!="complete_continuous_geometry_leaf":
                    raise ValueError("Unknown whole target/support stream item")
                body=item["whole_cell_geometry"]
                row=item["support_cell"]
                if row["patch"]!=g.PATCH:
                    raise ValueError("This is not the original complete upper patch")
                support=body["support"]
                for key in ("a_lower","b_lower","normal_norm_lower","normal_norm_upper"):
                    if F(row[key])!=F(support[key]):
                        raise ValueError("Support values differ from their own whole physical leaf")
                if (F(row["a_lower"])!=F(support["horizontal_numerator"][0])
                        or F(row["b_lower"])!=F(support["vertical_numerator"][0])
                        or support.get("candidate_normal_convention")!=g.NORMAL_CONVENTION
                        or support.get("closed_surface_outward_orientation_certified") is not False
                        or body.get("all_six_physical_jet_vectors_used") is not True
                        or body.get("all_original_raw_lift_terms_retained") is not True
                        or body.get("accurate_field_enclosure_replaced_by_working_words") is not False):
                    raise ValueError("The entire accurate physical support/lift provenance changed")
                pos=rational_box(body["position_hull"],3)
                decoded=dict(body)
                decoded["position_hull"]=[k.Interval(lo,hi,geometry["context"]["bits"]) for lo,hi in pos]
                decoded["target_metric"]=dict(body["target_metric"])
                for name in ("a_deep","rho0"):
                    decoded["target_metric"][name]=k.box(body["target_metric"][name],
                        geometry["context"]["bits"])
                stats.add(decoded,row["id"])
                total+=1
                yield item,row,pos
            if stream.read(1):
                raise ValueError("No target leaf may follow a complete stream footer")
        files.verify(record,force=True)
        if (footer is None or stats.metadata()!=d["complete_statistics"]
                or footer.get("complete_statistics")!=stats.metadata()
                or footer.get("complete_leaf_count")!=stats.count
                or footer.get("all_original_radial_leaves_processed") is not True):
            raise ValueError("Full stream values do not reproduce their original complete statistics")
        combined.absorb(stats.metadata())
    if total!=geometry["stats"].count or combined.metadata()!=geometry["stats"].metadata():
        raise ValueError("The complete target/support union differs from the true whole geometry")


def new_intervals(beta):
    return {kind:dict(
        beta_le_one=beta.RationalInterval(F(0),F(1),True,False,"0<beta<=1"),
        beta_ge_one=beta.RationalInterval(F(1),None,False,False,"1<=beta"))
        for kind in ("weak","strict")}


def impose_rows(intervals,row,tau,*,strict_only=False):
    a,b,w=F(row["a_lower"]),F(row["b_lower"]),F(row["normal_norm_upper"])
    if w<=0 or F(row["normal_norm_lower"])<=0:
        raise ArithmeticError("The complete current field must have proved positive normal norm")
    for kind,branches in intervals.items():
        strict=strict_only or kind=="strict"
        branches["beta_le_one"].impose(b,tau*w-a,strict,row["id"])
        branches["beta_ge_one"].impose(b-tau*w,-a,strict,row["id"])


def impose_caps(intervals,H,tau,beta,*,strict_only=False):
    for kind,branches in intervals.items():
        strict=strict_only or kind=="strict"
        branches["beta_le_one"].impose(H,tau*beta.CAP_DENOMINATOR+beta.CAP_G,
            strict,"complete-fixed-p4-caps")
        branches["beta_ge_one"].impose(H-tau*beta.CAP_DENOMINATOR,beta.CAP_G,
            strict,"complete-fixed-p4-caps")


def preview(geometry,core,files,r,g,k,beta):
    # This is the formerly formal full-set bound, now attached to the actual
    # closed parameter-image construction, not to a sampled diameter.
    D=F(geometry["report"]["accurate_global_bounds"][
        "formal_reflection_fixed_caps_all_rotation_set_diameter_upper"])
    if D<=0:
        raise ArithmeticError("A complete closed diameter upper bound must be positive")
    tau=beta.REACH_RATIO*D
    intervals=new_intervals(beta)
    positive=new_intervals(beta)
    distance=CompleteTargetDistance(core,geometry)
    count=0
    for item,row,pos in original_leaves(geometry,files,r,g,k):
        count+=1
        impose_rows(intervals,row,tau)
        impose_rows(positive,row,F(0),strict_only=True)
        distance.leaf(row["id"],pos)
    impose_caps(intervals,core["H"],tau,beta)
    impose_caps(positive,core["H"],F(0),beta,strict_only=True)
    selected,kind,branch=beta.choose_parameter(intervals)
    target_selected=selected
    if selected is None:
        selected,kind,branch=beta.choose_parameter(positive)
        purpose="strict-positive-support-only" if selected is not None else None
    else:
        purpose="original-three-percent-diameter-support-budget"
    return dict(D=D,tau=tau,count=count,beta=selected,selection_kind=kind,
        selection_branch=branch,selection_purpose=purpose,target_beta=target_selected,
        original_target_intervals={a:{b:v.metadata() for b,v in branches.items()}
            for a,branches in intervals.items()},
        strict_positive_support_intervals={a:{b:v.metadata() for b,v in branches.items()}
            for a,branches in positive.items()},
        holding=distance.result(core,geometry,k))


def second_pass_support(geometry,selected,files,r,g,k,beta):
    if selected is None or selected<=0:
        return None
    sigma=None
    witness=None
    count=0
    for item,row,pos in original_leaves(geometry,files,r,g,k):
        count+=1
        numerator=F(row["a_lower"])+selected*F(row["b_lower"])
        if numerator<=0:
            raise ArithmeticError("A selected common beta failed the exact full second pass")
        bound=numerator/F(row["normal_norm_upper"])
        if sigma is None or bound<sigma:
            sigma,witness=bound,row["id"]
    activity_sigma,activity_witness=sigma,witness
    cap_numerator=selected*geometry["context"]["H"].lo-beta.CAP_G
    if cap_numerator<=0:
        raise ArithmeticError("Do not divide a negative cap numerator by an upper denominator")
    cap_sigma=cap_numerator/beta.CAP_DENOMINATOR
    if cap_sigma<sigma:
        sigma,witness=cap_sigma,"complete-fixed-p4-caps"
    if count!=geometry["stats"].count:
        raise ValueError("A positive support second pass omitted a whole cell")
    KA=F(geometry["report"]["accurate_global_bounds"]["principal_curvature_absolute_upper"])
    K=max(KA,beta.CAP_K)
    L=max(F(1),selected)
    reach=min(sigma/L,1/K)
    return dict(common_beta=selected,centre=[F(0)]*3,A_diagonal=[F(1),F(1),selected],
        lambda_max=L,complete_activity_and_cap_sigma_lower=sigma,
        complete_activity_sigma_lower=activity_sigma,
        complete_activity_sigma_witness=activity_witness,
        sigma_lower_witness=witness,cap_numerator_lower=cap_numerator,
        cap_support_lower=cap_sigma,complete_marked_curvature_upper=K,
        activity_curvature_upper=KA,all_original_support_rows_reread=count,
        all_physical_phases_by_commuting_rotation_and_reflection=True,
        literal_beta_changes_actual_field=False,
        R650_reach_lower=reach,strict_positive_support_paid=True,
        embedding_and_outwardness_assumed_before_positive_support=False)


def unmarked_body_interpretation(geometry,core,ports,support,prepass,proofs,sources,report_path):
    """Instantiate existing R716 section 6 from its own unmarked R650 bounds.

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
            ("source_specific_ports","R248","R650","R661_components_only","R716","fixed_fejer_current_source_adapter")},
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
        raise ArithmeticError("The actual complete unmarked R650 hypotheses changed")
    reach=sigma/L
    if curvature>0:
        reach=min(reach,1/curvature)
    margin=reach-MARK_HEIGHT
    tube=margin>0
    result.update(unmarked_closed_C2_immersion_certified=True,
        unmarked_all_phase_embedding_and_outwardness_certified=True,
        common_beta=selected,lambda_max=L,complete_activity_sigma_lower=activity,
        unmarked_flat_cap_support_lower=flat,unmarked_global_sigma_lower=sigma,
        unmarked_complete_curvature_upper=curvature,unmarked_reach_lower=reach,
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
        unmarked_R650_bound_recomputed_without_using_marked_family_embedding=True)
    if tube:
        result.update(all_four_fixed_mark_components_in_uniform_outward_normal_tube=True,
            added_column_interiors_disjoint_from_every_unmarked_body=True,
            distinct_added_mark_interiors_disjoint=True,
            actual_marked_boundary_equals_unmarked_body_union_fixed_added_body=True,
            R716_volume_and_all_twelve_raw_moment_additivity_interpretation_certified=True,
            zero_volume_intersections_only_at_cap_bases_or_support_boundaries=True,
            accurate_body_relation="Omega_marked_alpha = R_alpha Omega_unmarked_0 union B, up to their common boundary",
            accurate_moment_relation="V=V_Omega+V_B; m_alpha=R_alpha*m_Omega+m_B; Q_alpha=R_alpha*Q_Omega*R_alpha^T+Q_B",
            proof="R650 first gives the UNMARKED complete closed family a common reach lower bound. Each p4 added point is p+v*n_p with 0<v<=1/1000 below that bound. The full exterior normal tube is injective and stays on the outside for every phase. Its base disks are fixed and distinct. R716 section 6 therefore identifies the complete marked boundary and pays all additive raw moment interpretations.")
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

    R650/R718 apply to the entire marked target, including both fixed caps.
    This is an additional lower bound; the original complete box scan remains.
    """
    if (ports.get("complete_closed_C2_immersion_certified") is not True
            or ports.get("continuous_global_oriented_unit_normal_certified") is not True
            or main_report.get("all_physical_phases_embedded") is not True
            or main_report.get("outward_orientation_certified") is not True
            or main_report.get("all_eight_original_beta_evidence_roles_paid") is not True
            or not isinstance(main_report.get("actual_outward_beta_package"),dict)
            or support is None or support.get("strict_positive_support_paid") is not True):
        raise ValueError("R718 requires the original complete closed/outward/support evidence")
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
             "R650","R248","fixed_fejer_current_source_adapter")})


def grip(geometry,core,D,holding,closed_family_paid):
    Rlo=geometry["context"]["R"].lo
    enough_radius=Rlo>=GRIP_RADIUS
    proved=bool(enough_radius and closed_family_paid)
    points=[[GRIP_RADIUS,F(0),core["H"]],[-GRIP_RADIUS,F(0),core["H"]],
        [F(0),GRIP_RADIUS,core["H"]],[MARK_CENTRE,F(0),core["H"]+MARK_HEIGHT]]
    determinant=2*GRIP_RADIUS**2*MARK_HEIGHT
    # Exact margins show the first three points are on the flat collar,
    # while the fourth is the first peak, unaffected by the other two bumps.
    centres=[(MARK_CENTRE,F(0)),(F(0),MARK_CENTRE),(-MARK_CENTRE,F(0))]
    for point in points[:3]:
        if any(sum((point[j]-c[j])**2 for j in range(2))<=b*b
                for c,b in zip(centres,MARK_RADII[:3])):
            raise ArithmeticError("A declared flat grip point lies in a p4 support")
    if any(sum((centres[0][j]-c[j])**2 for j in range(2))<=b*b
            for c,b in zip(centres[1:],MARK_RADII[1:3])):
        raise ArithmeticError("The first fixed peak overlaps another upper mark")
    diameter=2*GRIP_RADIUS
    positive=holding["rigorous_delta_hold_lower"]
    return dict(grip_radius=GRIP_RADIUS,actual_R_lower=Rlo,
        complete_closed_C2_family_assumptions_paid=closed_family_paid,
        radius_condition_alone=enough_radius,
        actual_upper_closed_material_graph_disk_exists=True if proved else None,
        closed_subset_with_nonempty_interior=True if proved else None,
        fixed_pointwise_for_all_physical_phases=True if proved else None,
        actual_four_fixed_image_points=points if proved else None,
        affine_difference_determinant_absolute=determinant if proved else None,
        pointwise_grip_stabilizer_including_reflections_is_identity=True if proved else None,
        stabilization_is_not_delta_hold_or_delta_E_quotient=True,
        grip_image_diameter_lower=diameter if proved else None,
        grip_diameter_over_D_lower=diameter/D if proved else None,
        required_grip_fraction="1/5",
        grip_size_standard_sufficient=proved and diameter>=D/5,
        delta_hold_lower=positive,
        delta_hold_over_D_lower=None if positive is None else positive/D,
        delta_hold_standard_sufficient=positive is not None and positive>=D/20,
        delta_hold_stronger_target_sufficient=positive is not None and positive>=D/5,
        lack_of_grip_stabilizer_never_used_to_suppress_image_distance=True,
        delta_E_positive=None,delta_E_lower=None,
        R661_old_activity_nonplanarity_not_inherited=True)


def complete_sources(geometry,files,r,paths):
    sources={("runtime_"+role):dict(record) for role,record in
        geometry["context"]["actual"]["full_scientific_runtime_source_records"].items()}
    sources.update({role:dict(value) for role,value in geometry["source_files"].items()})
    for role,path in paths.items():
        sources[role]=r.file_record(path)
    required={name for name,_ in r.ACTUAL_INPUT_SOURCE_PINS.values()}
    required.update((r.NORMAL_FEE_SOURCE[0],
        "fixed_fejer_meridian_batched_normal_packet_accurate_field_input.py",
        "fixed_fejer_meridian_batched_accurate_reference_control_radial_boxes.py"))
    by_name={Path(v["path"]).name:v for v in files.records.values()}
    if not required.issubset(by_name):
        raise ValueError("Every original full scientific/accurate dependency is required")
    for name in sorted(required):
        sources["accurate_"+name]=dict(by_name[name])
    for record in sources.values():
        files.verify(record)
    return sources


def field_and_cover(geometry,sources,beta,g,r):
    a=geometry["context"]["actual"]
    definition=dict(schema=beta.FIELD_SCHEMA,mathematical_model=a["complete_model"],
        mathematical_model_identity_sha256=a["model_identity_sha256"],
        current_full_point_sha256=a["current_full_point_sha256"],
        checkpoint_sha256=a["current_point_arrays_file"]["sha256"],
        fixed_metric_identity_sha256=a["fixed_scalar_metric_identity_sha256"],
        fixed_material_chart_identity_sha256=a["fixed_chart_core_sha256"],
        normal_convention=beta.NORMAL_CONVENTION,fixed_cap_recipe=beta.CAP_RECIPE,
        source_by_role={key:value["sha256"] for key,value in sources.items()},
        closed_phase_assembly_source_sha256=sha(__file__),
        original_upper_geometry_binding_identity_sha256=geometry["identity"],
        physical_phase_formula="R_alpha U(s,Theta0^{-1}(Theta0(phi)-alpha)); fixed Cartesian p4 caps",
        physical_phase_alpha_over_pi_interval=["0","1/2"],
        complete_old_field_and_target_unchanged=True,
        original_field_in_this_statement_is_the_actual_fixed_fejer_field=True,
        mathematical_target_identity_sha256=a["mathematical_target_identity_sha256"],
        previous_target_field_or_certificate_inherited=False,
        same_mathematical_g_as_run10_claimed=False,
        cross_run09_target_point_or_certificate_inherited=False,
        same_mathematical_g_as_run09_claimed=False,
        complete_current_source_adapter_proof_sha256="4eb8967fbb7e5ad5a6220825320b943fca306db124c4c5225f2e4de6c3561f21",
        closed_target_metric="same activity diag(1,(a_deep*rho0)^2), reflected lower, and fixed p4 caps with their own induced metric",
        accurate_sixjet_evidence_scope=ACCURATE_CLAIM_SCOPE,
        working_field_word_error_bound_produced=False,
        old_continuous_certificate_or_old_nonplanarity_reused=False)
    field=dict(definition=definition,identity_sha256=canonical(definition))
    cover_definition=dict(schema=beta.COVER_SCHEMA,
        field_identity_sha256=field["identity_sha256"],
        normal_convention=beta.NORMAL_CONVENTION,
        box_boundary_convention="all rectangles closed",
        exact_S_enclosure=geometry["binding"]["accurate_S"],
        patches=[dict(id=g.PATCH,
            mesh_affine=geometry["binding"]["complete_exact_radial_mesh_affine"],
            exact_parameter_interval_affine=[["0","0"],["1","0"]],
            angular_mode="full-circle",phi_over_pi_interval=["0","2"],
            radial_mode="proved-radial-fundamental-domain",
            radial_extension_evidence_role=RADIAL_EXTENSION)])
    return field,dict(definition=cover_definition,identity_sha256=canonical(cover_definition))


def make_support_chunks(geometry,field,cover,outdir,execution_record,files,outputs,r,g,k,beta,maximum):
    chunks=[]
    rows=[]
    count=0
    def finish():
        if not rows:
            return
        body=dict(schema=beta.CHUNK_SCHEMA,field_identity_sha256=field["identity_sha256"],
            coverage_identity_sha256=cover["identity_sha256"],
            producer_source_sha256=GEOMETRY[1],
            numeric_bound_producer_source_sha256=GEOMETRY[1],
            packaging_and_closed_orientation_producer_source_sha256=sha(__file__),
            original_geometry_binding_identity_sha256=geometry["identity"],
            normal_convention=beta.NORMAL_CONVENTION,
            all_values_are_accurate_outward_bounds=True,
            execution=execution_record,boxes=list(rows))
        record=write_json(outdir/("support-"+str(len(chunks)).zfill(6)+".json"),
            body,r,outputs)
        chunks.append(record)
        rows.clear()
    for item,row,pos in original_leaves(geometry,files,r,g,k):
        rows.append({key:row[key] for key in ("id","patch","cell","u_interval",
            "phi_over_pi_interval","a_lower","b_lower","normal_norm_lower","normal_norm_upper")})
        count+=1
        if len(rows)>=maximum:
            finish()
    finish()
    if count!=geometry["stats"].count:
        raise ValueError("The outward support package omits original whole cells")
    return chunks,count


def claims(field,cover,bounds,chunks,beta):
    d=field["definition"]
    values=dict(
        current_field_binding=dict(current_full_point_sha256=d["current_full_point_sha256"],
            checkpoint_sha256=d["checkpoint_sha256"],
            mathematical_model_identity_sha256=d["mathematical_model_identity_sha256"]),
        physical_six_jets=dict(normal_convention=beta.NORMAL_CONVENTION,
            coverage_identity_sha256=cover["identity_sha256"],
            support_producer_source_sha256=GEOMETRY[1],
            complete_support_chunk_records=[dict(sha256=v["sha256"],bytes=v["bytes"]) for v in chunks],
            complete_current_physical_lift_retained=True,
            all_root_scalar_quadrature_node_rounding_and_arithmetic_errors_included=True),
        complete_activity_domain_and_seams=dict(coverage_identity_sha256=cover["identity_sha256"],
            complete_original_radial_piece_set=True,all_accurate_tail_included=True,
            all_physical_domain_seams_C2=True),
        closed_sphere_immersion=dict(surface="complete-marked-closed-connected-C2-sphere-immersion",
            actual_activity_caps_and_cuffs_match=True),
        all_physical_phases=dict(formula="S_alpha = R_alpha A union C",axis="z",
            rotation_centre=["0","0","0"],activity_rotates=True,caps_are_fixed=True,
            full_physical_phase_range=True),
        diameter_bound=dict(D_upper=bounds["D_upper"],
            scope="complete-marked-surface-all-physical-phases"),
        activity_curvature_bound=dict(K_A_upper=bounds["K_A_upper"],
            scope="complete-accurate-activity-at-base-phase",all_pieces_and_tail=True),
        fixed_cap_parameters=dict(H_lower=bounds["H_lower"],R_lower=bounds["R_lower"],
            recipe_identity_sha256=canonical(beta.CAP_RECIPE),
            physical_height_fixed_along_all_phases=True,own_induced_cap_metric_and_C2_attachment=True))
    values[RADIAL_EXTENSION]=dict(kind="complete-radial-extension-and-C2-seams",
        patch=cover["definition"]["patches"][0]["id"],
        coverage_identity_sha256=cover["identity_sha256"],
        all_omitted_original_pieces_and_accurate_tail_accounted_for=True,
        extension_preserves_outward_support_for_every_positive_beta=True,
        complete_extension_uses_compatible_C2_parameter_diffeomorphisms=True,
        outward_unit_normals_transform_by_origin_fixed_orthogonal_maps_commuting_with_A_beta=True,
        all_reflection_core_cap_and_tail_seams_C2=True)
    if set(values)!=set(EIGHT_ROLES)|{RADIAL_EXTENSION}:
        raise ValueError("Retain all eight original proof roles and the separate radial extension")
    return values


def evidence_package(geometry,core,ports,prepass,support,sources,proofs,outdir,actual_execution,
        files,outputs,r,g,k,beta,bridge,chunk_rows):
    if (ports["complete_closed_C2_immersion_certified"] is not True
            or support is None or support["strict_positive_support_paid"] is not True):
        raise ValueError("Do not manufacture outward evidence before full C2 and positive support")
    field,cover=field_and_cover(geometry,sources,beta,g,r)
    chunks,count=make_support_chunks(geometry,field,cover,outdir/"support",
        actual_execution,files,outputs,r,g,k,beta,chunk_rows)
    KA=geometry["report"]["accurate_global_bounds"]["principal_curvature_absolute_upper"]
    bounds=dict(D_upper=str(prepass["D"]),K_A_upper=str(F(KA)),
        H_lower=str(geometry["context"]["H"].lo),R_lower=str(geometry["context"]["R"].lo))
    base_claims=claims(field,cover,bounds,chunks,beta)
    proof_records=[dict(proofs[name]) for name in ("source_specific_ports","R248","R650",
        "R661_components_only","R715","original_problem","fixed_fejer_current_source_adapter")]
    proof_short=[dict(sha256=p["sha256"],bytes=p["bytes"]) for p in proof_records]
    derivation=dict(schema=SCHEMA+"-actual-instantiation",source_sha256=sha(__file__),
        field_identity_sha256=field["identity_sha256"],ports=ports,
        strict_support_and_R650=support,
        actual_full_geometry_report=geometry["record"],
        actual_geometry_binding_identity_sha256=geometry["identity"],
        actual_full_normal_fee_report=geometry["context"]["record"],
        full_angle_branch=geometry["report"]["original_complete_angle_branch"],
        complete_source_records=sources,
        actual_radius=geometry["binding"]["accurate_R"],actual_height=str(core["H"]),
        actual_all_phase_D_upper=str(prepass["D"]),
        actual_complete_fixed_target_identity_sha256=geometry["context"]["actual"]["exact_fixed_target_identity_sha256"],
        original_geometry_formal_bound_now_has_complete_family_instantiation=True,
        candidate_normal_becomes_outward_by_R650_single_layer_and_upper_cap_orientation=True,
        no_external_truth_inferred_from_unchecked_booleans=True,
        no_prior_old_activity_nonplanarity_or_delta_E_certificate_used=True)
    derivation_record=write_json(outdir/"complete-closed-instantiation.json",derivation,r,outputs)
    evidence={}
    for role,claim in base_claims.items():
        certificate=dict(schema=beta.EVIDENCE_SCHEMA,role=role,
            field_identity_sha256=field["identity_sha256"],
            producer_source_sha256=sha(__file__),claim=claim,proof_sources=proof_short,
            complete=True,remaining_responsibilities=0,execution=actual_execution,
            complete_actual_instantiation=derivation_record,
            role_scope_does_not_include_delta_E_or_exact_solution_existence=True,
            claim_scope=ACCURATE_CLAIM_SCOPE if role=="physical_six_jets" else
                dict(accurate_same_field_instantiation_only=True,
                    working_field_word_error_bound_produced=False))
        record=write_json(outdir/"evidence"/(role+".json"),certificate,r,outputs)
        evidence[role]=dict(producer_source_role="closed_phase_producer",
            proof_sources=proof_records,certificate=record)
    document=dict(schema=beta.INPUT_SCHEMA,field=field,cover=cover,
        source_files=sources,checkpoint=geometry["context"]["actual"]["current_point_arrays_file"],
        bounds=bounds,support_producer_source_role="geometry_producer",
        support_chunks=chunks,declared_box_count=count,evidence=evidence,
        actual_closed_family_instantiation=derivation_record,
        original_target_field_unchanged=True)
    input_record=write_json(outdir/"complete-beta-input.json",document,r,outputs)
    bound=beta.read_input(argparse.Namespace(input=Path(input_record["path"]),
        expected_input_sha256=input_record["sha256"]))
    scope=bridge.bind_beta(bound,geometry,beta,r,g,files,Path(input_record["path"]))
    result=beta.consume(bound)
    if result.get("selected_global_beta")!=(
            None if prepass["target_beta"] is None else str(prepass["target_beta"])):
        raise ArithmeticError("The unchanged original beta consumer differs from the complete exact preview")
    beta.recheck_used(bound["used"])
    result_record=write_json(outdir/"complete-beta-result.json",result,r,outputs)
    return dict(field_identity_sha256=field["identity_sha256"],
        coverage_identity_sha256=cover["identity_sha256"],field=field,cover=cover,
        complete_beta_input=input_record,complete_beta_result=result_record,
        complete_actual_instantiation=derivation_record,complete_evidence_roles=evidence,
        complete_support_chunks=chunks,complete_support_row_count=count,
        all_eight_original_evidence_roles_actually_instantiated=True,
        additional_radial_extension_actually_instantiated=True,
        original_complete_consumer_read_input_and_consume_executed=True,
        original_geometry_bridge_full_rows_and_sources_compared=scope,
        original_beta_result=result)


def empty_report(execution_record):
    return dict(schema=SCHEMA,source_sha256=sha(__file__),execution=execution_record,
        complete=False,status="initializing",reason=None,geometry_report=None,
        complete_scope="complete same-field bound consumption, not a solved nonlinear construction",
        actual_current_full_point_sha256=None,actual_snapshot_identity_sha256=None,
        input_geometry_report_sha256=None,original_geometry_binding_identity_sha256=None,
        complete_geometry_leaf_count=None,full_target_upper_leaf_count=None,
        full_target_lower_leaf_count=None,beta_selection_purpose=None,
        complete_original_model_identity_sha256=None,exact_fixed_target_identity_sha256=None,
        complete_closed_C2_immersion_certified=None,
        all_physical_phases_C2_continuous=None,
        all_physical_phases_embedded=None,outward_orientation_certified=None,
        all_phase_same_target_relative_Gram_operator_error_upper=None,
        all_phase_relative_Gram_standard_sufficient=None,
        complete_marked_surface_D_upper=None,complete_marked_curvature_upper=None,
        formal_constructed_image_D_upper=None,
        working_field_word_error_bound_produced=False,
        complete_closed_geometry_scope="C2/embedding/outwardness/D/K/all-phase reach; metric, grip and Hausdorff separation are separate fields",
        common_positive_beta=None,common_sigma_lower=None,R650_reach_lower=None,
        reach_over_D_lower=None,reach_standard_sufficient=None,
        grip_radius=str(GRIP_RADIUS),grip_exists=None,grip_diameter_lower=None,
        grip_size_standard_sufficient=None,
        pointwise_grip_stabilizer_including_reflections_is_identity=None,
        delta_hold_lower=None,delta_hold_over_D_lower=None,
        delta_hold_standard_sufficient=None,delta_hold_stronger_target_sufficient=None,
        original_complete_box_distance_lower=None,
        R718_flow_distance_lower=None,R718_flow_distance_evidence=None,
        R718_flow_distance_used=None,
        R718_optional_bound_status="complete-closed-support-not-yet-paid",
        R719_uniform_axis_ratio_proved=None,
        delta_E_positive=None,delta_E_lower=None,
        unmarked_all_phase_embedding_certified=None,unmarked_reach_lower=None,
        mark_height_strictly_below_unmarked_reach=None,
        R716_body_and_twelve_moment_additivity_interpretation_certified=None,
        R716_outward_tube_evidence=None,
        complete_closed_geometry_certified=None,
        all_eight_original_beta_evidence_roles_paid=False,
        actual_outward_beta_package=None,closed_assembly=None,
        whole_target_distance=None,grip_evidence=None,
        source_files=None,proof_sources=None,
        all_bound_input_and_generated_evidence_bytes_rechecked=False,
        new_working_F_J_root_calls=0,new_accurate_root_or_integrand_calls=0,
        local_or_phase_samples_used_as_whole_domain=False,
        delta_hold_definition="max_t d_H(F_t(M),F_0(M)); no rigid alignment",
        same_g_convergence_or_exact_solution_existence_certified=False,
        final_mesh_exports_produced=False,research_goal_completed=False,
        original_solver_admission_gate=False,
        remaining=["The actual complete upper report must first be bound"])


def parse_args():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--repo",type=Path,required=True)
    p.add_argument("--geometry-report",type=Path,required=True)
    p.add_argument("--expected-geometry-report-sha256")
    p.add_argument("--outdir",type=Path,required=True)
    p.add_argument("--support-chunk-rows",type=int,default=4096)
    a=p.parse_args()
    if a.support_chunk_rows<1:
        p.error("--support-chunk-rows must be positive; it changes packaging only")
    return a


def main():
    args=parse_args()
    require_actions()
    started=time.monotonic()
    args.repo=args.repo.resolve()
    root=args.repo/TOPIC/"scripts/resume_20261126"
    bridge,bridge_path=load(root/BRIDGE[0],BRIDGE[1],"_closed_actual_geometry_bridge")
    g,gpath=load(root/GEOMETRY[0],GEOMETRY[1],"_closed_actual_continuous_geometry")
    r,rpath=g.load_reader(args.repo)
    r.require_actions()
    files=r.Files()
    outputs=r.Files()
    files.add(__file__)
    for path in (bridge_path,gpath,rpath):
        files.add(path)
    k,krecord=r.load_arithmetic(args.repo,files)
    actual_execution=execution(args.repo)
    report=empty_report(actual_execution)
    outdir=files.protect_output(args.outdir)
    if outdir.exists() and any(outdir.iterdir()):
        raise ValueError("Use a fresh namespace; prior partial evidence is not silently reused")
    outdir.mkdir(parents=True,exist_ok=True)
    report_path=outdir/"report.json"

    def save():
        report["elapsed_seconds_binary64_hex"]=float(time.monotonic()-started).hex()
        return write_json(report_path,report,r,outputs,replace=True)

    save()
    try:
        proofs=proof_files(args.repo,files,r)
        report["proof_sources"]=proofs
        beta,bpath=load(root/BETA[0],BETA[1],"_closed_original_positive_support")
        files.add(bpath)
        record=r.file_record(args.geometry_report)
        if (args.expected_geometry_report_sha256 is not None
                and record["sha256"]!=args.expected_geometry_report_sha256):
            raise ValueError("The caller's expected entire geometry report differs")
        raw,_=files.read_json(record)
        report["geometry_report"]=record
        report["input_geometry_report_sha256"]=record["sha256"]
        if raw.get("schema")!=g.SCHEMA or raw.get("source_sha256")!=GEOMETRY[1]:
            raise ValueError("Use the exact whole actual fixed-Fejer geometry producer")
        complete_keys=("complete","all_input_and_output_bytes_rechecked",
            "full_upper_cover_processed","continuous_curvature_bound_complete",
            "continuous_support_numerator_bounds_complete")
        missing=[key for key in complete_keys if raw.get(key) is not True]
        if missing:
            files.recheck()
            report.update(status="upstream-global-conditions-unpaid",
                reason="The genuine report has not paid all original complete geometry prerequisites",
                remaining=missing,all_bound_input_and_generated_evidence_bytes_rechecked=True)
            output=save()
            print(json.dumps(dict(schema=SCHEMA,report=output,complete=False,
                status=report["status"],new_field_root_calls=0),sort_keys=True))
            return 0
        scoped=argparse.Namespace(repo=args.repo,geometry_report=args.geometry_report,
            expected_geometry_report_sha256=record["sha256"])
        geometry=bridge.load_geometry(scoped,g,r,k,files)
        files.protect_output(outdir)
        r.verify_geometry_identity(geometry["context"],k)
        core=current_core(geometry,files,r)
        ports=exact_ports(geometry,core,r,beta)
        prepass=preview(geometry,core,files,r,g,k,beta)
        holding=prepass["holding"]
        closed_family_paid=ports["complete_closed_C2_immersion_certified"]
        holding["complete_closed_C2_family_assumptions_paid"]=closed_family_paid
        holding["formal_constructed_compact_image_distance_lower"]=holding["rigorous_delta_hold_lower"]
        holding["embedding_assumed_in_image_distance_bound"]=False
        if not closed_family_paid:
            holding["rigorous_delta_hold_lower"]=None
            holding["positive_lower_paid"]=False
        holding["original_complete_box_distance_lower"]=holding["rigorous_delta_hold_lower"]
        report["original_complete_box_distance_lower"]=encoded(holding["rigorous_delta_hold_lower"])
        gripping=grip(geometry,core,prepass["D"],holding,closed_family_paid)
        paths=dict(closed_phase_producer=Path(__file__).resolve(),
            geometry_bridge=bridge_path,positive_support_consumer=bpath)
        sources=complete_sources(geometry,files,r,paths)
        c=geometry["context"]
        a=c["actual"]
        report.update(actual_current_full_point_sha256=a["current_full_point_sha256"],
            actual_snapshot_identity_sha256=a["actual_snapshot_identity_sha256"],
            complete_original_model_identity_sha256=a["model_identity_sha256"],
            exact_fixed_target_identity_sha256=a["exact_fixed_target_identity_sha256"],
            complete_closed_C2_immersion_certified=True if closed_family_paid else None,
            all_physical_phases_C2_continuous=True if closed_family_paid else None,
            source_files=sources,closed_assembly=ports,whole_target_distance=holding,
            current_complete_core=core,grip_evidence=gripping,
            formal_constructed_image_D_upper=str(prepass["D"]),
            complete_marked_surface_D_upper=str(prepass["D"]) if closed_family_paid else None,
            original_geometry_binding_identity_sha256=geometry["identity"],
            complete_geometry_leaf_count=geometry["stats"].count,
            full_target_upper_leaf_count=holding["all_upper_target_leaves_read"],
            full_target_lower_leaf_count=holding["all_lower_target_leaves_included"],
            original_target_beta_intervals=prepass["original_target_intervals"],
            strict_positive_support_beta_intervals=prepass["strict_positive_support_intervals"],
            beta_selection_purpose=prepass["selection_purpose"],
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
        if closed_family_paid and gram is not None:
            report["all_phase_same_target_relative_Gram_operator_error_upper"]=str(F(gram))
            report["all_phase_relative_Gram_standard_sufficient"]=F(gram)<=F(1,1000000)
        support=second_pass_support(geometry,prepass["beta"],files,r,g,k,beta)
        package=None
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
        if not ports["complete_closed_C2_immersion_certified"]:
            remaining.extend(ports["remaining"])
        if support is None:
            remaining.append("No common strictly positive A_beta support was certified by the full boxes")
        if ports["complete_closed_C2_immersion_certified"] and support is not None:
            package=evidence_package(geometry,core,ports,prepass,support,sources,proofs,
                outdir/"beta",actual_execution,files,outputs,r,g,k,beta,bridge,args.support_chunk_rows)
            report.update(all_physical_phases_embedded=True,
                outward_orientation_certified=True,common_positive_beta=str(support["common_beta"]),
                common_sigma_lower=str(support["complete_activity_and_cap_sigma_lower"]),
                complete_marked_curvature_upper=str(support["complete_marked_curvature_upper"]),
                R650_reach_lower=str(support["R650_reach_lower"]),
                reach_over_D_lower=str(support["R650_reach_lower"]/prepass["D"]),
                reach_standard_sufficient=support["R650_reach_lower"]>=prepass["tau"],
                all_eight_original_beta_evidence_roles_paid=True,
                actual_outward_beta_package=package)
            try:
                flow=flow_image_distance(geometry,core,ports,support,proofs,report,report_path)
            except MemoryError:
                report["R718_optional_bound_status"]="unavailable-memory-original-box-bound-retained"
            else:
                original=holding["original_complete_box_distance_lower"]
                old=F(0) if original is None else F(original)
                flow_bound=flow["rigorous_delta_hold_lower"]
                combined=max(old,flow_bound)
                holding.update(R718_flow_distance_lower=flow_bound,
                    R718_flow_distance_evidence=flow,
                    R718_flow_distance_used=flow_bound>old,
                    combined_lower_bound_rule="max(original complete box lower, paid R718 flow lower)",
                    rigorous_delta_hold_lower=combined,positive_lower_paid=combined>0)
                gripping=grip(geometry,core,prepass["D"],holding,closed_family_paid)
                report.update(R718_flow_distance_lower=encoded(flow_bound),
                    R718_flow_distance_evidence=flow,
                    R718_flow_distance_used=flow_bound>old,
                    R718_optional_bound_status="complete-directed-rational-lower-bound",
                    R719_uniform_axis_ratio_proved=flow["R719_uniform_axis_ratio_proved"],
                    whole_target_distance=holding,grip_evidence=gripping,
                    delta_hold_lower=encoded(gripping["delta_hold_lower"]),
                    delta_hold_over_D_lower=encoded(gripping["delta_hold_over_D_lower"]),
                    delta_hold_standard_sufficient=gripping["delta_hold_standard_sufficient"],
                    delta_hold_stronger_target_sufficient=gripping["delta_hold_stronger_target_sufficient"])
        else:
            report["all_physical_phases_embedded"]=None
            report["outward_orientation_certified"]=None
        if report["reach_standard_sufficient"] is not True:
            remaining.append("The common all-phase reach lower bound has not met 0.03 times the complete D upper")
        if gripping["grip_size_standard_sufficient"] is not True:
            remaining.append("The actual r_h=9/20 grip radius/0.2D size condition is unpaid")
        if gripping["delta_hold_standard_sufficient"] is not True:
            remaining.append("The complete-image witness has not paid delta_hold >= 0.05D")
        if gripping["delta_hold_stronger_target_sufficient"] is not True:
            remaining.append("The complete-image witness has not paid the stronger delta_hold >= 0.2D target")
        if report["all_phase_relative_Gram_standard_sufficient"] is not True:
            remaining.append("The whole closed/all-phase relative Gram error has not paid 1e-6")
        remaining.extend(["Delta_E positivity needs its separate full same-field R716 or other valid evidence",
            "Same-target convergent nonlinear refinement and exact-solution approximation are not proved here",
            "Required exported meshes are not produced here"])
        files.recheck()
        outputs.recheck()
        report.update(complete=True,status="complete-same-field-consumption",
            remaining=remaining,
            complete_closed_geometry_certified=True if (
                ports["complete_closed_C2_immersion_certified"] and support is not None
                and support["R650_reach_lower"]>=prepass["tau"]) else None,
            all_bound_input_and_generated_evidence_bytes_rechecked=True,
            strict_positive_support_proof=encoded(support) if closed_family_paid else None,
            formal_common_support_calculation=encoded(support),
            complete_accurate_sixjet_evidence_scope=ACCURATE_CLAIM_SCOPE,
            actual_complete_input_records=list(files.records.values()),
            generated_evidence_records=list(outputs.records.values()),
            support_chunk_rows=args.support_chunk_rows,
            support_chunk_partition_does_not_change_any_mathematical_domain=True)
        output=save()
        print(json.dumps(dict(schema=SCHEMA,report=output,complete=True,
            closed_C2=report["complete_closed_C2_immersion_certified"],
            all_phase_embedded=report["all_physical_phases_embedded"],
            reach_paid=report["reach_standard_sufficient"],
            grip_paid=report["grip_size_standard_sufficient"],
            delta_hold_paid=report["delta_hold_standard_sufficient"],
            beta_evidence=report["all_eight_original_beta_evidence_roles_paid"],
            research_goal_completed=False),sort_keys=True))
        return 0
    except Exception as error:
        promoted=("complete_closed_C2_immersion_certified","all_physical_phases_C2_continuous",
            "all_physical_phases_embedded","outward_orientation_certified",
            "all_phase_same_target_relative_Gram_operator_error_upper",
            "all_phase_relative_Gram_standard_sufficient","complete_marked_surface_D_upper",
            "complete_marked_curvature_upper","common_positive_beta","common_sigma_lower",
            "R650_reach_lower","reach_over_D_lower","reach_standard_sufficient",
            "grip_exists","grip_diameter_lower","grip_size_standard_sufficient",
            "pointwise_grip_stabilizer_including_reflections_is_identity","delta_hold_lower",
            "delta_hold_over_D_lower","delta_hold_standard_sufficient",
            "delta_hold_stronger_target_sufficient","complete_closed_geometry_certified",
            "original_complete_box_distance_lower","R718_flow_distance_lower",
            "R718_flow_distance_evidence","R718_flow_distance_used","R719_uniform_axis_ratio_proved",
            "unmarked_all_phase_embedding_certified","unmarked_reach_lower",
            "mark_height_strictly_below_unmarked_reach",
            "R716_body_and_twelve_moment_additivity_interpretation_certified")
        report["uncommitted_provisional_claims_before_failure"]={
            key:report.get(key) for key in promoted}
        for key in promoted:
            report[key]=None
        report["R718_optional_bound_status"]="invalidated-by-complete-consumption-failure"
        report["all_eight_original_beta_evidence_roles_paid"]=False
        report["actual_outward_beta_package"]=None
        report.update(complete=False,status="source-or-complete-bound-consumption-failed",
            reason=str(error),exception_type=type(error).__name__,
            all_bound_input_and_generated_evidence_bytes_rechecked=False,
            failure_is_not_geometric_impossibility=True)
        save()
        raise


if __name__=="__main__":
    raise SystemExit(main())
