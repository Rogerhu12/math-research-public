#!/usr/bin/env sage-python
"""The original R883 full shadow through R931 complete thick Artinian norms.

Each phase is accepted only after all preceding original gates are recomputed
in this same offline public Actions process.  Objects remain in memory; only
proof receipts and hashes are emitted.  No coefficient database is written.
"""
import os
if (os.environ.get("GITHUB_ACTIONS") != "true" or
        os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public"):
    raise SystemExit("Run mathematical computations only in the public research Actions.")

import argparse
import hashlib
import importlib.util
import json
import sys
import time
from pathlib import Path
from sage.env import SAGE_VERSION
from section_quotient_algebra import canonical,digest
from original_shadow_receipt_tools import add_pinned_arguments,pinned_request,validate_envelope
from original_cube_compact_sections import build_original_compact_cube_sections
from original_affine_fast_operations import build_original_affine_fast_operations
from original_ys_fraction_bridge import (
    build_original_ys_fraction_maps,prepare_original_ys_geometry,
    build_original_four_intersections)
from original_ys_artinian_shadow_consumer import consume_original_artinian_shadow
from original_ys_artinian_norm_tools import OriginalArtinianNormTools
from original_ys_divisor_ideal_tools import OriginalAffineIdealEngine
from sage.all import vector

HERE=Path(__file__).resolve().parent
STARTED=time.monotonic()
CURRENT_STAGE="initialization"


def progress(stage,**record):
    global CURRENT_STAGE
    CURRENT_STAGE=stage
    print("RANK2_ARTINIAN_CONSUMER_STAGE "+canonical(dict(
        stage=stage,elapsed_seconds=time.monotonic()-STARTED,**record)),flush=True)


def emit(name,receipt):
    payload=canonical(receipt)
    print(name+"_RESULT "+payload,flush=True)
    print(name+"_SHA256 "+hashlib.sha256(payload.encode()).hexdigest(),flush=True)


def load_source(name,alias):
    path=HERE/name
    spec=importlib.util.spec_from_file_location(alias,str(path))
    module=importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def original_thick_norm_preflight(six):
    """Actual rank-306 Y, two charts, mixed thick support and relative k norm.

    For a primitive c in the CALLER'S k, pi=xi^2-c is irreducible. The
    original algebra A is R-free of rank 306, so I=pi^2*(xi-1)A has full
    k-length 1530. Its true xi norm is (-c)^612, which is not in F_r for
    r=29 or 41. The original fraction (pi*xi)/pi has an everywhere common
    pi zero on the bad component: its whole graph must still return xi.
    """
    affine = six["original_affine_context"]
    identity = {
        "original_curve":"X0(3468)",
        "original_complete_normalization_signature":affine["certificate"]["exact_multiplication_signature_sha256"],
        "original_Y_M2_basis":six["embedding_context"]["coordinate_basis_id"],
    }
    records = []
    for flag in (False,True):
        engine = OriginalAffineIdealEngine(
            six["model"].operations["chart"](infinity=flag),
            progress=progress,kernel_method="minimal")
        norm_tools = OriginalArtinianNormTools(
            engine,affine,identity,six["omega"],progress=progress)
        R,k = engine.R,engine.k
        xi,c = R.gen(),k.multiplicative_generator()
        assert c**((int(k.cardinality())-1)//2) == -1
        pi,rho = xi**2-c,xi-1
        assert pi.is_irreducible() and pi.degree()==2
        whole = engine.ideal_from_rows(pi**2*rho*engine.identity,
                                      "same original mixed thick preflight ideal")
        bad_expected = engine.ideal_from_rows(pi**2*engine.identity,
                                             "same original full pi squared divisor")
        good_expected = engine.ideal_from_rows(rho*engine.identity,
                                              "same original full rho divisor")
        support = engine.ideal_from_rows(pi*engine.identity,
                                        "same original entire pi support")
        assert whole.length==1530 and bad_expected.length==1224 and good_expected.length==306
        split,split_record = norm_tools.split_support(
            whole,support,label="original mixed thick preflight split")
        assert split["bad"].basis==bad_expected.basis
        assert split["good"].basis==good_expected.basis
        h = vector(R,xi*engine.unit)
        inverse,inverse_record = norm_tools.inverse_unit(whole,h)
        assert whole.contains(engine.multiply(h,inverse)-engine.unit)
        recovered,fraction_record = norm_tools.recover_fraction(
            whole,(vector(R,pi*h),vector(R,pi*engine.unit)),
            label="original complete pi common-zero fraction preflight")
        assert recovered==whole.reduce(h)
        actual,norm_record = norm_tools.norm_unit(
            whole,h,label="original two-chart relative thick norm preflight")
        expected = k((-c)**612)
        assert actual==expected and actual**int(k.characteristic())!=actual
        empty,empty_record = norm_tools.norm_unit(engine.unit_ideal(),h)
        assert empty==k.one()
        records.append({
            "infinity_chart":flag,"full_k_length":whole.length,
            "full_bad_length":split["bad"].length,
            "full_good_length":split["good"].length,
            "complete_mixed_support_split":split_record,
            "complete_unit_inverse":inverse_record,
            "full_common_zero_graph_return":fraction_record,
            "all_pi_layers_relative_norm":norm_record,
            "exact_central_norm_formula_returned":True,
            "relative_norm_is_not_in_prime_field":True,
            "empty_divisor_norm":empty_record,
        })
    return {
        "kind":"same_original_Y_two_chart_complete_Artinian_preflight",
        "status":"all_original_thick_preflight_gates_completed",
        "both_actual_original_charts":records,
        "alternate_curve_or_reduced_support_used":False,
        "same_original_omega_and_quadratic_base_retained":True,
        "four_large_intersections_or_shadow_claimed":False,
    }


def main():
    parser=argparse.ArgumentParser(allow_abbrev=False)
    add_pinned_arguments(parser)
    parser.add_argument("--phase",choices=("maps","geometry","intersections","shadow"),default="maps")
    parser.add_argument("--trace-method",choices=("artinian",),default="artinian")
    parser.add_argument("--q-precision",type=int,default=2453)
    parser.add_argument("--batch-size",type=int,default=64)
    parser.add_argument("--kernel-method",choices=("minimal","hermite"),default="minimal")
    args=parser.parse_args()
    assert args.q_precision>=2453 and args.batch_size>0
    request=pinned_request(args)
    incoming=sys.stdin.buffer.read(2*1024*1024+1)
    assert len(incoming)<=2*1024*1024
    envelope=json.loads(incoming.decode("utf-8"))
    host_hash=hashlib.sha256((HERE/"read-original-shadow-pass-receipts.py").read_bytes()).hexdigest()
    first,packet=validate_envelope(envelope,request,host_hash)
    progress("both original complete characteristic-zero PASS authenticated",
             requested_phase=args.phase,requested_trace_method=args.trace_method,
             public_pass_envelope_sha256=envelope["envelope_sha256"])
    cube_module=load_source("produce-original-cube-section-fractions.py","ys_consumer_original_cube")
    cube,cube_receipt=cube_module.build_original_cube_section_fractions(args.prime,first,packet)
    emit("RANK2_CUBE_SECTIONS",cube_receipt)
    progress("same original roots in lower section degrees start")
    compact,compact_receipt=build_original_compact_cube_sections(cube,progress=progress)
    assert compact["cube_context"] is cube
    emit("RANK2_COMPACT_CUBE_SECTIONS",compact_receipt)
    normalization_module=load_source("produce-original-y-affine-normalization.py","ys_consumer_original_normalization")
    affine,normalization_receipt=normalization_module.build_original_y_affine_normalization(
        prime=args.prime,q_precision=args.q_precision,batch_size=args.batch_size)
    emit("RANK2_Y_AFFINE",normalization_receipt)
    progress("complete original coefficient-operation adapter start")
    affine,fast_receipt=build_original_affine_fast_operations(affine,progress=progress)
    emit("RANK2_Y_FAST_OPERATIONS",fast_receipt)
    progress("same original maps and both endpoints start")
    six,map_receipt=build_original_ys_fraction_maps(
        affine,cube,progress=progress,compact_context=compact)
    emit("RANK2_ARTINIAN_CONSUMER_MAPS",map_receipt)
    phase_receipts={"maps":digest(map_receipt)}
    preflight_receipt=original_thick_norm_preflight(six)
    emit("RANK2_ARTINIAN_PREFLIGHT",preflight_receipt)
    retained={"cube":cube,"compact_cube":compact,"affine":affine,"six":six}
    geometry=intersections=shadow=None
    all_intersection_support_accounted=False
    if args.phase in ("geometry","intersections","shadow"):
        progress("same complete boundary and all original map pole divisors start")
        geometry,geometry_receipt=prepare_original_ys_geometry(
            six,progress=progress,kernel_method=args.kernel_method)
        retained["geometry"]=geometry
        phase_receipts["geometry"]=digest(geometry_receipt)
        emit("RANK2_ARTINIAN_CONSUMER_GEOMETRY",geometry_receipt)
    if args.phase in ("intersections","shadow"):
        progress("all four original complete effective divisor ideals start")
        intersections,intersection_receipt=build_original_four_intersections(
            six,geometry_context=geometry,progress=progress,
            kernel_method=args.kernel_method,decompose_intersections=False)
        retained["intersections"]=intersections
        phase_receipts["intersections"]=digest(intersection_receipt)
        emit("RANK2_ARTINIAN_CONSUMER_INTERSECTIONS",intersection_receipt)
    if args.phase=="shadow":
        # Complete thick ideals and every pi layer retain the full support,
        # residue degrees and multiplicities without decomposing E into points.
        progress("all original thick Artin values and complete norm traces start",
                 trace_method=args.trace_method)
        shadow,shadow_receipt=consume_original_artinian_shadow(
            intersections,trace_method=args.trace_method,progress=progress)
        assert shadow["original_intersection_context"] is intersections
        assert shadow_receipt["status"]=="complete_original_shadow"
        assert shadow_receipt["trace_method"]==args.trace_method
        assert shadow_receipt["all_nine_original_pairs_accounted"] is True
        assert shadow_receipt["all_cusps_common_zeros_and_residue_degrees_retained"] is True
        assert shadow_receipt["ordinary_nonvanishing_or_infinitely_many_p_claimed"] is False
        accounts=shadow["complete_pair_length_accounts"]
        assert set(accounts)==set(intersections["intersections"])
        assert len(accounts)==4
        for pair,item in intersections["intersections"].items():
            account=accounts[pair]
            assert account["endpoint_pair"]==list(pair)
            full=int(item["complete_degree"])
            assert account["full_original_intersection_degree"]==full
            assert account["accounted_full_k_length"]==full
            assert account["finite_original_intersection_length"]==item["finite_ideal"].length
            assert account["infinity_original_intersection_length"]==item["infinity_boundary_ideal"].length
            assert account["finite_original_intersection_length"]+account["infinity_original_intersection_length"]==full
            classes=("ramified_finite_length","ramified_infinity_length",
                     "common_pole_length","common_zero_length",
                     "output_O_length","finite_extra_length")
            assert all(type(account[key]) is int and account[key]>=0 for key in classes)
            assert sum(account[key] for key in classes)==full
        assert shadow_receipt["complete_pair_length_accounts"]==[accounts[pair] for pair in intersections["intersections"]]
        all_intersection_support_accounted=True
        retained["shadow"]=shadow
        phase_receipts["shadow"]=digest(shadow_receipt)
        emit("RANK2_ARTINIAN_CONSUMER_SHADOW",shadow_receipt)
    dependencies=[
        "launch-original-artinian-shadow.py","produce-original-artinian-shadow.py",
        "produce-original-cube-section-fractions.py","original_cube_compact_sections.py",
        "original_ys_artinian_norm_tools.py", "original_ys_exact_reuse.py", "original_ys_fraction_bridge.py","original_ys_artinian_shadow_consumer.py",
        "original_affine_fast_operations.py","original_section_ring_embedding.py",
        "original_ys_divisor_ideal_tools.py","original_ys_closed_point_tools.py",
        "original_ys_local_value_tools.py","original_shadow_relative_six_tools.py",
        "original_shadow_coefficient_tools.py","original_shadow_tate_trace_tools.py",
        "original_affine_multiplication.py","produce-original-y-affine-normalization.py",
        "produce-original-y-colon-apery.py","produce-original-y-global-section-and-ys.py",
        "produce-original-tuv-section-fractions.py",
        "produce-original-map-section-fractions.py","section_quotient_algebra.py",
        "read-original-shadow-pass-receipts.py","original_shadow_receipt_tools.py",
        "produce-original-shadow-local-input.py","original_good_prime_germ_tools.py",
        "check-r873-original-cm-petersson-degree.py","original_low_weight_cm_tools.py",
        "produce-r917-original-global-rr-q-lattice.py","original_pari_m2_basis.py",
        "original_shadow_coordinate_tools.py"]
    receipt={
        "kind":"rank2_original_complete_artinian_shadow_pipeline",
        "status":"all_requested_original_acceptance_gates_completed",
        "completed_phase":args.phase,"prime":args.prime,
        "requested_trace_method":args.trace_method,
        "completed_trace_method":args.trace_method if shadow is not None else None,
        "q_precision":args.q_precision,"batch_size":args.batch_size,
        "kernel_method":args.kernel_method,"level":3468,
        "same_original_cubes_result_sha256":digest(cube_receipt),
        "same_original_compact_cubes_result_sha256":digest(compact_receipt),
        "same_original_normalization_result_sha256":digest(normalization_receipt),
        "complete_fast_operations_initial_receipt":fast_receipt,
        "complete_coefficient_operation_summary":affine["coefficient_contraction_summary"](),
        "complete_phase_receipt_sha256":phase_receipts,
        "all_objects_retained_in_same_offline_process":True,
        "same_original_compact_RF_R2_and_RP_R3_certified":True,
        "complete_original_maps_computed":True,
        "complete_original_geometry_computed":geometry is not None,
        "complete_large_divisor_ideals_computed":intersections is not None,
        "all_intersection_closed_points_computed":False,
        "all_original_intersection_support_and_thickness_accounted":all_intersection_support_accounted,
        "same_original_two_chart_artinian_preflight_sha256":digest(preflight_receipt),
        "all_original_thick_Artin_values_and_complete_traces_computed":shadow is not None,
        "original_shadow_computed":shadow is not None,
        "original_rational_AJ_detected_nonzero":(
            shadow_receipt["original_rational_AJ_detected_nonzero"] if shadow is not None else None),
        "ordinary_nonvanishing_or_infinitely_many_p_claimed":False,
        "public_pass_envelope_sha256":envelope["envelope_sha256"],
        "authenticated_public_jobs":envelope["authentication"],
        "source":os.environ.get("RANK2_SOURCE_SHA"),
        "run_id":os.environ.get("RANK2_RUN_ID"),
        "run_attempt":os.environ.get("RANK2_RUN_ATTEMPT"),
        "image":os.environ.get("RANK2_IMAGE"),"sage_version":SAGE_VERSION,
        "readme_blobs":{"root":os.environ.get("RANK2_ROOT_README_SHA"),
                        "topic":os.environ.get("RANK2_TOPIC_README_SHA")},
        "script_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "dependency_sha256":{name:hashlib.sha256((HERE/name).read_bytes()).hexdigest()
                             for name in dependencies},
        "elapsed_seconds":time.monotonic()-STARTED,
    }
    retained["certificate"]=receipt
    globals()["ORIGINAL_COMPLETE_ARTINIAN_SHADOW_CONTEXT"]=retained
    emit("RANK2_ARTINIAN_CONSUMER",receipt)


if __name__=="__main__":
    try:
        main()
    except Exception as exc:
        failed=CURRENT_STAGE
        progress("failed",failed_stage=failed,
                 exception_type=type(exc).__name__,message=str(exc))
        raise
