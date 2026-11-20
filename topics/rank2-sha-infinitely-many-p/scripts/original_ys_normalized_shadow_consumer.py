"""The complete ORIGINAL R883 shadow, using R925's actual normalization.

The old relative-six loop is retained: the same four pairs, cyclic choice
from the ACTUAL first pole degree, ramified/common/extra multiplicities,
whole residue degrees, actual local cancellation, complete [6] traces, and
the original 18-by-9/two-axis readout.  No ordinary or infinitely-many-prime
conclusion is inferred from this one finite shadow.
"""
import os
if (os.environ.get("GITHUB_ACTIONS") != "true" or
        os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public"):
    raise SystemExit("Run this mathematical helper only in the public research Actions.")

import hashlib
import time
from pathlib import Path
from sage.all import ZZ, EllipticCurve
from section_quotient_algebra import canonical, digest
from original_ys_closed_point_tools import decompose_complete_ideal
from original_ys_local_value_tools import OriginalAffineLocalReader
from original_ys_fraction_bridge import ORIGINAL_FOUR_PAIRS
from original_ys_exact_reuse import validate_shared_original_intersection
import original_shadow_relative_six_tools as legacy


def default_progress(stage, **data):
    print("RANK2_NORMALIZED_SHADOW_STAGE " + canonical(dict(stage=stage, **data)), flush=True)


def _complete_pair_points(context, item, progress):
    """Read every finite point and exactly the missing s=0 boundary."""
    shared = item.get("exact_shared_intersection")
    shared_record = None
    if shared is not None:
        shared_record = validate_shared_original_intersection(context,item,shared)
        if shared["closed_points"] is not None:
            points = shared["closed_points"]
            assert sum(int(p["full_local_k_length"]) for p in points) == item["complete_degree"]
            assert sum(int(p["point"]["degree_over_original_constants"])*
                       int(p["intersection_multiplicity"]) for p in points) == item["complete_degree"]
            item["closed_points"] = points
            record = dict(shared["closed_point_decomposition_receipt"])
            record["exact_complete_ideal_reuse"] = shared_record
            item["closed_point_decomposition_receipt"] = record
            progress("same complete original closed-point decomposition reused",
                     endpoint_pair=list(item["endpoint_pair"]),
                     first_endpoint_pair=list(shared["first_pair"]),
                     complete_degree=int(item["complete_degree"]),
                     all_current_pair_outputs_and_traces_still_to_read=True)
            return points,record
    if "closed_points" in item:
        points = item["closed_points"]
        assert sum(int(p["full_local_k_length"]) for p in points) == item["complete_degree"]
        return points, {"source":"already complete original intersection decomposition",
                        "whole_projective_degree":int(item["complete_degree"])}
    a,b = item["endpoint_pair"]
    finite,finite_record = decompose_complete_ideal(
        context["engines"][False],item["finite_ideal"],context["registry"],
        label="same original E_%d%d finite closed points" % (a,b),progress=progress)
    infinite,infinite_record = decompose_complete_ideal(
        context["engines"][True],item["full_infinity_chart_ideal"],context["registry"],
        label="same original E_%d%d entire infinity fiber" % (a,b),
        only_infinity_boundary=True,progress=progress)
    points = finite+infinite
    assert sum(int(p["full_local_k_length"]) for p in points) == item["complete_degree"]
    assert sum(int(p["point"]["degree_over_original_constants"])*
               int(p["intersection_multiplicity"]) for p in points) == item["complete_degree"]
    item["closed_points"] = points
    record = {"finite":finite_record,"entire_infinity_boundary":infinite_record,
              "whole_projective_degree":int(item["complete_degree"]),
              "every_thick_local_length_included":True}
    item["closed_point_decomposition_receipt"] = record
    if shared is not None:
        assert shared["closed_points"] is None
        shared["closed_points"] = points
        shared["closed_point_decomposition_receipt"] = record
        record["first_endpoint_pair"] = list(shared["first_pair"])
    return points,record


def complete_original_pair_shadow(context, item, torsion, local_readers,
                                  trace_method="tate", tate_reader=None, progress=None):
    """R883(46)--(50), term for term, on actual complete original closed points."""
    progress = progress or default_progress
    assert trace_method in ("tate","scalar","compare")
    assert (tate_reader is not None) == (trace_method in ("tate","compare"))
    six = context["six"]
    field, r = six["constants"], int(six["prime"])
    ell, E0 = int(torsion["ell"]), torsion["curve"]
    assert (r,ell) in ((29,5),(41,7))
    a,b = item["endpoint_pair"]
    first_degree = int(context["first_map_degree"])
    expected = 2256+r*first_degree if first_degree < 2256 else 2256*(r+1)
    assert int(item["complete_degree"]) == expected
    points,decomposition_receipt = _complete_pair_points(context,item,progress)
    progress("whole original intersection ready for local trace",
             endpoint_pair=[a,b],closed_points=len(points),complete_degree=expected,
             cyclic_presentation=item["cyclic_presentation"])
    total = E0(0)
    record_hash = hashlib.sha256()
    counts = {
        "closed_places":0,"ramified_degree":0,"common_degree":0,
        "extra_degree":0,"extra_closed_places":0,"extra_output_infinity_degree":0,
        "nonzero_six_trace_places":0,"maximum_residue_degree":0,
        "cuspidal_intersection_degree":0,
    }
    valuation_cache = {}

    def valuation(point, function):
        key = (id(point),id(function))
        if key not in valuation_cache:
            flag = bool(point["infinity_chart"])
            value = local_readers[flag].fraction_valuation(point,function.chart_pair(flag))
            assert value in ZZ, "Every original coordinate used here is a nonzero global function."
            valuation_cache[key] = int(value)
        return valuation_cache[key]

    for index,entry in enumerate(points):
        point = entry["point"]
        multiplicity = int(entry["intersection_multiplicity"])
        degree = int(point["degree_over_original_constants"])
        assert multiplicity > 0 and degree > 0
        assert int(entry["full_local_k_length"]) == multiplicity*degree
        flag = bool(point["infinity_chart"])
        reader = local_readers[flag]
        counts["closed_places"] += 1
        counts["maximum_residue_degree"] = max(counts["maximum_residue_degree"],degree)
        # Registry identity was established by equality of the WHOLE maximal
        # ideal and original chart/basis, not merely by a hash collision.
        if id(point) in context["original_cusp_points"]:
            assert context["original_cusp_points"][id(point)][0] is point
            counts["cuspidal_intersection_degree"] += multiplicity*degree
        vv = valuation(point,six["vs"])
        record = {
            "place_sha256":point["fingerprint"],"infinity_chart":flag,
            "residue_degree":degree,"intersection_multiplicity":multiplicity,
            "full_local_k_length":int(entry["full_local_k_length"]),
            "vs_valuation":vv,
        }
        if vv % 3:
            counts["ramified_degree"] += multiplicity*degree
            record["boundary"] = "original ramified contribution is exact 3-torsion, killed by 6"
        else:
            s = vv//3
            ax = s+valuation(point,item["a0"])
            c_order = ((r-2)//3)*vv+r*valuation(point,item["xp"])
            cx = 2*s+c_order
            # The y2 and c0 orders are the exact orders of genuine r-th
            # POWERS.  This is neither coefficient conjugation nor Artin.
            py1 = max(-valuation(point,item["y1"]),0)
            pyp = max(-valuation(point,item["yp"]),0)
            py2 = r*pyp
            assert (py1 > 0) == (py2 > 0), (
                "A single pole cannot be in the whole effective intersection.")
            if py1 and py2:
                assert py1 % 3 == py2 % 3 == 0
                common = min(py1//3,py2//3)
            elif ax > 0 and cx > 0:
                common = min(ax,cx)
            else:
                common = 0
            extra = multiplicity-3*common
            assert extra >= 0
            counts["common_degree"] += 3*common*degree
            counts["extra_degree"] += extra*degree
            record.update({"xA_valuation":ax,"xB_valuation":cx,
                           "common_multiplicity":common,"extra_multiplicity":extra,
                           "original_y1_pole_order":py1,"original_y2_pole_order":py2})
            if extra:
                assert ax == cx
                counts["extra_closed_places"] += 1
                if valuation(point,item["output_y"]) < 0:
                    counts["extra_output_infinity_degree"] += extra*degree
                    record["output"] = "O by the actual original projective extension"
                else:
                    assert valuation(point,item["xout"]) >= 0
                    residue_field = point["native_residue_field"]
                    embed_base = point["original_constant_embedding"]
                    assert residue_field.cardinality() == ZZ(r)**(2*degree)
                    assert int(residue_field.absolute_degree()) == 2*degree
                    assert embed_base(field.one()) == residue_field.one()
                    omega_residue = embed_base(six["omega"])
                    assert omega_residue**2+omega_residue+1 == 0
                    assert omega_residue != 1
                    xx = reader.reduce_fraction(point,item["xout"].chart_pair(flag))
                    yy = reader.reduce_fraction(point,item["output_y"].chart_pair(flag))
                    assert xx.parent() is residue_field and yy.parent() is residue_field
                    assert yy**2 == xx**3+1
                    EQ = EllipticCurve(residue_field,[0,0,0,0,1])
                    P = EQ([xx,yy])
                    trace_record = {"trace_method":trace_method,
                                    "actual_original_constant_embedding_preserved":True,
                                    "full_residue_degree_used":degree}
                    Tate_point = scalar_point = None
                    if trace_method in ("tate","compare"):
                        Tate_point,pairing_record = tate_reader.six_trace(
                            P,residue_field,embed_base,degree)
                        trace_record["reduced_Tate"] = pairing_record
                    if trace_method in ("scalar","compare"):
                        numerator = ZZ.one()-ZZ(-r)**degree
                        assert numerator % ell == 0
                        scalar = numerator//ell
                        S = scalar*P
                        assert ell*S == EQ(0)
                        if not S.is_zero():
                            assert S[0]**(r*r) == S[0] and S[1]**(r*r) == S[1]
                        scalar_point = legacy.read_fixed_field_point(
                            S,residue_field,omega_residue,six["omega"],field,E0,r,degree)
                        trace_record["scalar_bits"] = int(abs(scalar).nbits())
                    if trace_method == "compare":
                        assert Tate_point == scalar_point
                        trace_record["same_original_basis_full_trace_comparison"] = True
                    Sbase = scalar_point if trace_method == "scalar" else Tate_point
                    assert ell*Sbase == E0(0)
                    if not Sbase.is_zero():
                        counts["nonzero_six_trace_places"] += 1
                    # Only the complete [6]trace is now ell torsion.  Keep
                    # the TRUE intersection multiplicity until this step.
                    total += extra*Sbase
                    record.update({"trace_audit":trace_record,
                                   "six_trace":legacy.point_coordinates(Sbase),
                                   "weighted_trace":legacy.point_coordinates(extra*Sbase)})
            else:
                record["boundary"] = "three equal lift contributions sum to zero"
        record_hash.update(canonical(record).encode())
        record_hash.update(b"\n")
        if index % 20 == 19 or index+1 == len(points):
            progress("whole original closed-point trace",
                     endpoint_pair=[a,b],processed=index+1,total_places=len(points),
                     residue_degree_max=counts["maximum_residue_degree"])
    assert counts["ramified_degree"]+counts["common_degree"]+counts["extra_degree"] == expected
    assert counts["closed_places"] == len(points)
    assert ell*total == E0(0)
    coordinates = torsion["coordinates"][total]
    result = {
        "endpoint_pair":[a,b],"trace_method":trace_method,
        "full_intersection_degree":expected,"first_map_degree":first_degree,
        "cyclic_presentation":item["cyclic_presentation"],
        "six_times_trace":legacy.point_coordinates(total),
        "torsion_coordinates":list(coordinates),
        "complete_closed_records_sha256":record_hash.hexdigest(),
        "complete_original_closed_point_decomposition":decomposition_receipt,
        "all_actual_common_zero_values_in_original_residue_fields":True,
        "all_whole_residue_degrees_and_true_multiplicities_retained":True,
        **counts,
    }
    progress("same original pair complete",endpoint_pair=[a,b],
             full_intersection_degree=expected,torsion_coordinates=list(coordinates))
    return total,result


def consume_original_normalized_shadow(intersection_context, trace_method="tate", progress=None):
    """Finish the original nine-point/18-row/two-axis consumer from complete E's."""
    started = time.monotonic()
    progress = progress or default_progress
    context = intersection_context
    assert context["kind"] == "rank2_original_Y_four_intersection_context"
    assert trace_method in ("tate","scalar","compare")
    six = context["six"]
    assert set(context["intersections"]) == set(ORIGINAL_FOUR_PAIRS)
    torsion = legacy.verified_torsion_basis(six["constants"],six["omega"],six["prime"])
    tate_reader = None
    if trace_method in ("tate","compare"):
        from original_shadow_tate_trace_tools import OriginalTateTraceReader
        tate_reader = OriginalTateTraceReader(torsion,six["prime"])
        progress("original reduced Tate reader calibrated",trace_method=trace_method,
                 **tate_reader.calibration)
    local_readers = {
        flag:OriginalAffineLocalReader(engine,context["original_basis_identity"],progress=progress)
        for flag,engine in context["engines"].items()}
    points = [[None]*3 for _ in range(3)]
    pair_records = []
    for a,b in ORIGINAL_FOUR_PAIRS:
        point,record = complete_original_pair_shadow(
            context,context["intersections"][a,b],torsion,local_readers,
            trace_method=trace_method,tate_reader=tate_reader,progress=progress)
        points[a][b] = points[b][a] = point
        pair_records.append(record)
    cm,frobenius = torsion["cm"],torsion["frobenius"]
    # These relations are applied ONLY to fully computed whole [6] traces.
    points[0][2] = points[2][0] = -cm(frobenius(points[0][1]))
    points[2][2] = -cm(cm(frobenius(points[1][1])))
    assert frobenius(points[0][0]) == -points[0][0]
    assert frobenius(points[1][2]) == -cm(points[1][2])
    assert all(torsion["ell"]*point == torsion["curve"](0)
               for row in points for point in row)
    readout = legacy.read_full_artin(six,torsion,points)
    Atest = points[0][0]-cm(cm(points[1][2]))
    Ctest = points[1][1]+cm(frobenius(points[0][1]))
    assert frobenius(Atest) == -Atest
    detector = not Atest.is_zero() or not Ctest.is_zero()
    assert bool(readout["nonzero_original_pairs"]) == detector
    assert len(readout["nonzero_original_pairs"]) in (0,3)
    point_test = {
        "A":legacy.point_coordinates(Atest),"C":legacy.point_coordinates(Ctest),
        "A_coordinates":list(torsion["coordinates"][Atest]),
        "C_coordinates":list(torsion["coordinates"][Ctest]),
        "equivalent_to_all_three_original_nonzero_readouts":True,
        "detected_nonzero":detector,
    }
    local_records = {str(flag):reader.receipt_summary() for flag,reader in local_readers.items()}
    receipt = {
        "kind":"rank2_same_original_normalized_relative_six_frobenius_shadow",
        "status":"complete_original_shadow",
        "prime":int(six["prime"]),"ell":int(torsion["ell"]),
        "trace_method":trace_method,
        "divisor_method":"same original R925 full polynomial ideals and complete local modules",
        "RR_method":"same original M2 lattice, full colon/Apery basis and certified multiplication",
        "original_source_level":10404,"relative_six_level":3468,"RR_base_level":867,
        "source_genus":1729,"relative_six_genus":559,
        "normalization_module_rank_over_ys":306,
        "computed_complete_divisors":[list(pair) for pair in ORIGINAL_FOUR_PAIRS],
        "all_nine_original_pairs_accounted":True,
        "remaining_pairs_via_proved_original_W_and_constant_reflection":True,
        "actual_r_Frobenius_matrix":[[int(z) for z in row]
                                     for row in torsion["Frobenius_matrix"].rows()],
        "two_exact_point_detector":point_test,
        "all_cusps_common_zeros_and_residue_degrees_retained":True,
        "first_factor_x_correction":"(v_s+4)/v_s",
        "pair_summaries":pair_records,
        "actual_local_value_readers":local_records,
        "Tate_trace_reader":tate_reader.summary() if tate_reader is not None else None,
        "every_contributing_point_compared_in_same_basis":trace_method == "compare",
        "original_artin_readout":readout,
        "original_rational_AJ_detected_nonzero":bool(readout["nonzero_original_pairs"]),
        "canonical_cycle_substituted":False,
        "ordinary_nonvanishing_or_infinitely_many_p_claimed":False,
        "original_complete_intersection_source":context["certificate"],
        "helper_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "unchanged_original_trace_and_artin_code_sha256":hashlib.sha256(Path(legacy.__file__).read_bytes()).hexdigest(),
        "elapsed_seconds":time.monotonic()-started,
    }
    result_context = {
        "original_intersection_context":context,"original_torsion_basis":torsion,
        "original_local_readers":local_readers,"original_tate_reader":tate_reader,
        "all_nine_original_trace_points":points,"original_point_detector":point_test,
        "certificate":receipt,
    }
    progress("complete same original normalized shadow finished",
             prime=int(six["prime"]),ell=int(torsion["ell"]),
             detected_original_finite_shadow_nonzero=detector,
             all_nine_points_and_all_eighteen_rows=True)
    return result_context,receipt
