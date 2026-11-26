#!/usr/bin/env sage-python
"""The original complete geometry with exact W and reflection reuse.

The complete original cusp and branch calculations, seven actual function
objects, all pole degrees, both charts and infinity boundaries are retained.
Three map representatives are computed directly; the four other original
principal divisors use complete source transport AND their own actual
zero/pole image and unit-sum gates.
"""
import os
if (os.environ.get("GITHUB_ACTIONS") != "true" or
        os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public"):
    raise SystemExit("Run mathematical computations only in the public research Actions.")

import hashlib
from pathlib import Path
import original_ys_fraction_bridge as original_bridge
from original_ys_fraction_bridge import (
    OriginalClosedPointRegistry, decompose_complete_ideal, _progress)
from original_triangular_artinian_values import (
    OriginalTriangularIdealEngine as OriginalAffineIdealEngine,
    SOURCE_DEPENDENCIES as VALUE_DEPENDENCIES)
from original_full_w_basis_transport import (
    build_original_w_basis_transport, SOURCE_DEPENDENCIES as W_DEPENDENCIES)
from original_w_ideal_transport import (
    OriginalWholeWIdealTransport, SOURCE_DEPENDENCIES as IDEAL_DEPENDENCIES)

BASE_BRIDGE_SHA256 = "788949117cba32c3ce347257ab71681bfe4a6940f935e017efef852c6ea4d9b8"
SOURCE_DEPENDENCIES = tuple(dict.fromkeys((
    "original_ys_geometry_transport.py",
    "original_ys_fraction_bridge.py",
) + VALUE_DEPENDENCIES + W_DEPENDENCIES + IDEAL_DEPENDENCIES))


def prepare_original_ys_geometry_with_complete_transports(six, progress=None, kernel_method="minimal"):
    """Actual complete cusp/branch support and all seven original pole degrees."""
    assert hashlib.sha256(Path(original_bridge.__file__).read_bytes()).hexdigest() == BASE_BRIDGE_SHA256
    assert six["kind"] == "rank2_original_Y_fraction_consumer_context"
    model, affine, prime = six["model"], six["original_affine_context"], int(six["prime"])
    operations = model.operations
    engines = {flag:OriginalAffineIdealEngine(
        operations["chart"](infinity=flag),progress=progress,kernel_method=kernel_method)
        for flag in (False,True)}
    basis_identity = {
        "original_curve":"X0(3468)",
        "original_complete_normalization_signature":affine["certificate"]["exact_multiplication_signature_sha256"],
        "original_Y_M2_basis":six["embedding_context"]["coordinate_basis_id"],
    }
    registry = OriginalClosedPointRegistry(basis_identity)
    cache = {}

    transporter, W_receipt = None, None
    # These are the SAME original function objects. The actual target
    # fractions will independently pass both whole primitive-divisor gates.
    transport_sources = {
        id(six["A"][2]["y0"]):(six["A"][1]["y0"], "constant_reflection", "original A1 y0"),
    }
    for index, row in enumerate(six["A"]):
        transport_sources[id(row["y2"])] = (row["y0"], "W", "original A%d y0" % index)
    assert len(transport_sources) == 4
    direct_map_labels = {
        id(six["A"][0]["y0"]):"original A0 y0",
        id(six["A"][1]["y0"]):"original A1 y0",
        id(six["F_y"]):"original first factor yF",
    }
    actual_direct_map_labels = []

    def whole_transporter():
        nonlocal transporter, W_receipt
        if transporter is None:
            W_context, W_receipt = build_original_w_basis_transport(
                six["embedding_context"], progress=progress)
            transporter = OriginalWholeWIdealTransport(six, W_context, engines, progress)
        return transporter

    def direct_complete_divisor(function, label):
        key = id(function)
        if key in cache:
            assert cache[key]["function"] is function
            return cache[key]
        charts, records = {}, {}
        for flag in (False,True):
            N,D = function.chart_pair(flag)
            positive,negative,record = engines[flag].zero_pole_ideals(N,D,label)
            charts[flag] = {"positive":positive,"negative":negative}
            records[str(flag)] = record
        for sign in ("positive","negative"):
            boundary,record = engines[True].infinity_boundary(charts[True][sign])
            charts[True][sign+"_boundary"] = boundary
            records[sign+"_infinity_boundary"] = record
        positive_degree = charts[False]["positive"].length+charts[True]["positive_boundary"].length
        negative_degree = charts[False]["negative"].length+charts[True]["negative_boundary"].length
        assert positive_degree == negative_degree
        result = {"function":function,"charts":charts,"positive_degree":positive_degree,
                  "negative_degree":negative_degree,"records":records}
        cache[key] = result
        if key in direct_map_labels:
            actual_direct_map_labels.append(direct_map_labels[key])
        _progress(progress,"same original complete principal divisor certified",
                  label=label,zero_degree=positive_degree,pole_degree=negative_degree)
        return result

    def complete_divisor(function, label):
        key = id(function)
        if key in cache:
            assert cache[key]["function"] is function
            return cache[key]
        if key not in transport_sources:
            return direct_complete_divisor(function, label)
        source_function, operation, source_label = transport_sources[key]
        assert source_function is not function
        source_divisor = complete_divisor(source_function, source_label)
        result = whole_transporter().transported_principal_parts(
            source_divisor["charts"], function, operation=operation, label=label)
        assert result["function"] is function
        cache[key] = result
        _progress(progress,"same original complete principal divisor certified",
                  label=label,zero_degree=result["positive_degree"],
                  pole_degree=result["negative_degree"],
                  exact_whole_source_transport=operation,
                  both_actual_target_fraction_primitive_gates=True)
        return result

    def whole_signed_support(divisor,label):
        entries, records = {}, []
        for flag in (False,True):
            for sign, direction in (("positive",1),("negative",-1)):
                ideal = divisor["charts"][flag][sign]
                points,record = decompose_complete_ideal(
                    engines[flag],ideal,registry,label=label+":"+sign,
                    only_infinity_boundary=flag,progress=progress)
                records.append(record)
                for item in points:
                    point = item["point"]
                    key = id(point)
                    assert key not in entries, "Zero and pole divisors must have disjoint original support."
                    entries[key] = (point,direction*int(item["intersection_multiplicity"]))
        return entries,records

    T_divisor = complete_divisor(six["T"],"same central T")
    v_divisor = complete_divisor(six["vs"],"same v=ys^2-1")
    cusps,T_records = whole_signed_support(T_divisor,"all original cusps")
    v_support,v_records = whole_signed_support(v_divisor,"all original cubic branching")
    assert sum(point["degree_over_original_constants"] for point,m in cusps.values()) == 108
    assert set(v_support).issubset(set(cusps))
    ramified = [(point,m) for point,m in v_support.values() if m % 3]
    assert all(cusps[id(point)][1] < 0 for point,m in ramified)
    assert sum(point["degree_over_original_constants"] for point,m in ramified) == 54
    endpoint_poles = []
    for index,row in enumerate(six["A"]):
        endpoint_poles.append({})
        for tag in ("y0","y2"):
            divisor = complete_divisor(row[tag],"original A%d %s" % (index,tag))
            assert divisor["negative_degree"] == 2256
            endpoint_poles[index][tag] = divisor
    F_poles = complete_divisor(six["F_y"],"original first factor yF")
    first_degree = int(F_poles["negative_degree"])
    assert first_degree > 0
    assert sorted(actual_direct_map_labels) == sorted(direct_map_labels.values())
    assert transporter is not None and W_receipt is not None
    for key in transport_sources:
        assert key in cache
        record = cache[key]["records"]["whole_target_fraction_gates"]
        for chart_name in ("finite", "infinity"):
            assert record[chart_name]["whole_positive_plus_negative_is_unit_ideal"]
            assert record[chart_name]["whole_ZD_and_PN_images_equal_by_complete_HNF"]
    transport_receipt = transporter.receipt()
    receipt = {
        "kind":"rank2_original_Y_complete_boundary_and_pole_geometry",
        "status":"same_original_cusps_branching_and_seven_actual_map_pole_divisors",
        "prime":prime,"first_map_degree_from_actual_complete_poles":first_degree,
        "original_geometric_cusp_count":108,"original_cubic_ramified_geometric_count":54,
        "actual_whole_boundary_divisors":[T_records,v_records],
        "all_six_original_endpoint_pole_degrees":2256,
        "actual_endpoint_pole_records":[{tag:value["records"] for tag,value in item.items()}
                                        for item in endpoint_poles],
        "actual_first_factor_pole_records":F_poles["records"],
        "complete_original_W_basis_transport":W_receipt,
        "complete_two_chart_original_ideal_transports":transport_receipt,
        "actual_direct_original_map_divisors":actual_direct_map_labels,
        "all_four_transported_actual_fractions_passed_full_ZD_PN_and_unit_sum":True,
        "complete_intersection_divisors_computed":False,
        "original_shadow_computed":False,
        "helper_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    }
    return {
        "kind":"rank2_original_Y_complete_pole_geometry_context",
        "six":six,"engines":engines,"registry":registry,
        "original_basis_identity":basis_identity,
        "complete_principal_divisor_cache":cache,
        "complete_divisor":complete_divisor,
        "original_cusp_points":cusps,"original_v_signed_support":v_support,
        "endpoint_poles":endpoint_poles,"F_poles":F_poles,
        "first_map_degree":first_degree,"certificate":receipt,
    },receipt
