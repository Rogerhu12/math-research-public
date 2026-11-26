#!/usr/bin/env sage-python
"""Same original seven maps: three full equations and four exact transports.

Only the repeated equation-expansion block changes.  All original root,
source, scale, W and reflection checks remain.  This independent builder
does not modify the shared bridge or any running workflow.
"""
import os
if (os.environ.get("GITHUB_ACTIONS") != "true" or
        os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public"):
    raise SystemExit("Run mathematical computations only in the public research Actions.")

import hashlib
from pathlib import Path
from sage.all import ZZ, QQ, PolynomialRing
import original_ys_fraction_bridge as original_bridge
from original_ys_fraction_bridge import (
    OriginalFractionModel, build_original_section_ring_embedding,
    finite_coordinates, legacy, _progress)
from section_quotient_algebra import canonical, digest

BASE_BRIDGE_SHA256 = "788949117cba32c3ce347257ab71681bfe4a6940f935e017efef852c6ea4d9b8"
SOURCE_DEPENDENCIES = (
    "original_ys_equation_transport.py",
    "original_ys_fraction_bridge.py",
    "original_section_ring_embedding.py",
    "original_affine_fast_operations.py",
    "original_shadow_relative_six_tools.py",
)


def equation_transport_formal_preflight():
    """Exact universal identities; no original geometric input is generated."""
    P = PolynomialRing(ZZ, names=("X","Y","A","B","V","v","c","lam"))
    X,Y,A,B,V,v,c,lam = P.gens()
    target = Y**2-v*X**3-1
    original_W = B**2-V*A**3-1
    W_error = ((Y-B)*(Y+B)-v*(X-c*A)*(X**2+c*X*A+c**2*A**2)
               +(V-v*c**3)*A**3)
    assert target-original_W == W_error
    reflected = B**2-v*A**3-1
    reflection_error = (
        (B-Y)*(B+Y)-v*(A-lam*X)*(A**2+lam*A*X+lam**2*X**2)
        -v*(lam**3-1)*X**3)
    assert reflected-target == reflection_error
    R = PolynomialRing(QQ, "original_scalar_xi")
    xi = R.fraction_field()(R.gen())
    h, c0 = xi-1, 2/(xi-1)
    wxi = (xi+3)/(xi-1)
    assert wxi-1 == 4/h
    assert (wxi+3)/(wxi-1) == xi
    assert wxi**2-1 == c0**3*(xi**2-1)
    return dict(
        kind="exact_universal_original_elliptic_equation_transport",
        status="two_universal_polynomial_identities_and_W_scalars_verified",
        universal_polynomial_coefficient_ring="ZZ",
        universal_W_identity_verified=True,
        universal_reflection_identity_verified=True,
        W_scalar_involution_and_complete_cubic_correction_verified=True,
        all_original_geometric_automorphism_inputs_still_required=True,
        original_normalization_maps_or_shadow_computed=False,
        helper_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())


def build_original_ys_fraction_maps_with_equation_transport(affine_context, cube_context,
                                   embedding_context=None, progress=None,
                                   compact_context=None):
    """Same original seven maps, with complete equation-transport certificates."""
    assert hashlib.sha256(Path(original_bridge.__file__).read_bytes()).hexdigest() == BASE_BRIDGE_SHA256
    formal_transport = equation_transport_formal_preflight()
    cube = cube_context
    assert cube["kind"] == "rank2_original_cube_section_fractions_context"
    assert cube["RF"]["complete_global_identity"]["original_global_identity_certified"] is True
    assert all(cube["RP"][i]["complete_global_identity"]["original_global_identity_certified"] is True
               for i in (0,1,2))
    root_source = cube
    compaction_records = None
    if compact_context is not None:
        compact = compact_context
        assert compact["kind"] == "rank2_original_compact_cube_sections_context"
        assert compact["cube_context"] is cube
        assert compact["complete_product_recipes"] is cube["complete_product_recipes"]
        compaction_records = {}
        for tag,old,new,expected_power in (
                [("RF",cube["RF"],compact["RF"],2)]+
                [("RP%d" % i,cube["RP"][i],compact["RP"][i],3)
                 for i in (0,1,2)]):
            assert new["same_original_function_certified"] is True
            record = new["same_original_function_certificate"]
            assert record["same_original_function_certified"] is True
            source_power,compact_power = int(old["section_power"]),int(new["section_power"])
            assert compact_power == expected_power
            assert int(record["source_section_power"]) == source_power
            assert int(record["compact_section_power"]) == compact_power
            zero_bound = 204*(source_power+compact_power)
            assert int(record["complete_global_zero_degree_bound"]) == zero_bound
            assert int(record["full_checked_coefficients"]) == zero_bound+1
            compaction_records[tag] = record
        root_source = compact
    maps = cube["map_context"]
    if embedding_context is None:
        embedding, embedding_receipt = build_original_section_ring_embedding(
            affine_context, maps, progress=progress, with_map_fractions=True)
    else:
        embedding = embedding_context
        assert embedding["original_map_sections_context"] is maps
        assert embedding["original_affine_context"] is affine_context
        assert embedding["certificate"]["F_and_P_fractions_built"] is True
        embedding_receipt = embedding["certificate"]
    assert embedding["constants"] is cube["constants"]
    model = OriginalFractionModel(embedding, affine_context)
    k, r, ys = model.k, model.prime, model.ys
    # Reuse the ORIGINAL constant routine, including its specified finite
    # field root ordering.  theta17 is a constant here, not a missing Y map.
    constant_input = {
        "constants":k, "prime":r, "omega":cube["original_omega"],
        "original_a_roots":maps["local_context"]["a_roots"],
        "sigma_a_index":maps["sigma_a_index"], "P":maps["P"],
    }
    constants = legacy.fixed_artin_constants(constant_input)
    assert tuple(maps["sigma_a_index"]) == (2,0,1)
    theta, omega = constants["theta17"], constants["omega"]
    section = embedding["section_coordinates"]
    fraction = embedding["same_degree_fraction"]
    recipes = root_source["complete_product_recipes"]
    RF = root_source["RF"]
    RF_power = int(RF["section_power"])
    RF_data = fraction(section(RF_power, recipes[RF_power], RF["numerator_coordinates"], 2),
                       section(RF_power, recipes[RF_power], RF["denominator_coordinates"], 2),
                       RF_power, "same original RF on pi2")
    central_RF = model.same_degree_section_fraction(RF_data)
    central_vF = model.same_degree_section_fraction(embedding["F"][2])
    _progress(progress,"same original central root embedded",
              common_root_bound=central_RF.pole_weight_bound,
              common_y_bound=central_vF.pole_weight_bound)
    endpoint_Y, endpoint_R = {}, {}
    root_embedding_records = [RF_data["certificate"]]
    for index in (0,1,2):
        for exponent in (1,4):
            endpoint_Y[index,exponent] = model.same_degree_section_fraction(
                embedding["P"][index][exponent])
            root = root_source["RP"][index]
            root_power = int(root["section_power"])
            data = fraction(section(root_power, recipes[root_power], root["numerator_coordinates"], exponent),
                            section(root_power, recipes[root_power], root["denominator_coordinates"], exponent),
                            root_power, "same original RP_%d on pi%d" % (index,exponent))
            endpoint_R[index,exponent] = model.same_degree_section_fraction(data)
            root_embedding_records.append(data["certificate"])
            _progress(progress,"same original endpoint root embedded",
                      original_embedding=index,degeneracy=exponent,
                      common_root_bound=endpoint_R[index,exponent].pole_weight_bound,
                      common_y_bound=endpoint_Y[index,exponent].pole_weight_bound)

    def formulas(parameter, swapped=False):
        v = parameter**2-1
        central_T = parameter**2*(parameter**2-9)**2/v**2
        N0 = 5*v+8-parameter*(v-8)
        T0, T2 = N0**3/v**4-27, (v-2)**3/v-27
        epsilon = -central_T*parameter*(v-8)*v**3/(v+4)**6
        f0 = (v+4)/v*central_RF/theta**2
        yF = central_vF/(epsilon*theta**3)
        rows = []
        j0, j2 = (4,1) if swapped else (1,4)
        for constant in constants["rows"]:
            index = int(constant["embedding"])
            dnew, vnew = constant["dnew"], constant["vnew"]
            x0 = N0**2/v**3*endpoint_R[index,j0]/dnew**2
            x2 = (v-2)**2/v*endpoint_R[index,j2]/dnew**2
            y0 = endpoint_Y[index,j0]*2/vnew+1
            y2 = endpoint_Y[index,j2]*2/vnew+1
            rows.append({"x0":x0,"y0":y0,"x2":x2,"y2":y2,
                         "artin_index":int(constant["artin_index"]),
                         "original_embedding":index})
        return {"ys":parameter,"vs":v,"T":central_T,"N0":N0,
                "T0":T0,"T2":T2,"epsilon":epsilon,
                "F_x_over_xs":f0,"F_y":yF,"A":rows}

    actual = formulas(ys)
    v = actual["vs"]
    _progress(progress,"checking original first elliptic equation",
              x_bound=actual["F_x_over_xs"].pole_weight_bound,
              y_bound=actual["F_y"].pole_weight_bound)
    assert actual["F_y"]**2 == v*actual["F_x_over_xs"]**3+1
    for index in (0,1):
        row = actual["A"][index]
        _progress(progress,"checking original representative endpoint equation",
                  artin_index=index,x0_bound=row["x0"].pole_weight_bound,
                  y0_bound=row["y0"].pole_weight_bound)
        assert row["y0"]**2 == v*row["x0"]**3+1
    _progress(progress,"three original representative equations passed by full ring identity")
    _progress(progress,"checking actual original W through proved degeneracy identities")
    W = formulas((ys+3)/(ys-1), swapped=True)
    assert W["T"] == actual["T"]
    assert W["T0"] == actual["T2"] and W["T2"] == actual["T0"]
    correction = 2/(ys-1)
    assert W["vs"] == correction**3*v
    assert correction*W["F_x_over_xs"] == actual["F_x_over_xs"]
    assert W["F_y"] == -actual["F_y"]
    for original_row, Wrow in zip(actual["A"],W["A"]):
        assert Wrow["y0"] == original_row["y2"]
        assert Wrow["y2"] == original_row["y0"]
        assert correction*Wrow["x0"] == original_row["x2"]
        assert correction*Wrow["x2"] == original_row["x0"]
    _progress(progress,"all original W and endpoint identities passed")
    _progress(progress,"checking original coefficient reflection and CM phases")
    assert actual["F_x_over_xs"].constant_conjugate() == actual["F_x_over_xs"]
    assert actual["F_y"].constant_conjugate() == -actual["F_y"]
    for index, row in enumerate(actual["A"]):
        star, phase = (-index)%3, k.one() if index == 0 else omega**-1
        for tag in ("x0","x2"):
            assert row[tag].constant_conjugate() == actual["A"][star][tag]*phase
        for tag in ("y0","y2"):
            assert row[tag].constant_conjugate() == actual["A"][star][tag]
    # The COMPLETE original multiplication tables are defined over F_r.
    # Thus coefficient reflection, fixing the entire original basis, is
    # an algebra automorphism on all source vectors, not a pointwise test.
    fp = affine_context["constants"]
    tables = affine_context["product_blocks"]
    assert int(fp.cardinality()) == r
    assert all(table.base_ring() == fp for table in tables.values())
    assert sum(table.nrows() for table in tables.values()) == 306*307//2
    assert len(affine_context["product_pair_positions"]) == 306*307//2
    assert affine_context["certificate"]["every_product_full_global_zero_bound_checked"] is True
    assert all(c**r == c for f in model.unit for c in f.list())
    assert omega**3 == 1 and omega != 1
    assert (omega**-1)**3 == 1
    original_functions = [actual["vs"], actual["F_x_over_xs"], actual["F_y"]]
    for row in actual["A"]:
        original_functions.extend(row[tag] for tag in ("x0","y0","x2","y2"))
    W_functions = [W["vs"], W["F_x_over_xs"], W["F_y"]]
    for row in W["A"]:
        W_functions.extend(row[tag] for tag in ("x0","y0","x2","y2"))
    assert all(f.model is model and len(f.denominator) == 306 and not f.denominator.is_zero()
               for f in original_functions+W_functions)
    equation_transport = dict(
        formal_certificate=formal_transport,
        direct_complete_equation_labels=["F","A0q0","A1q0"],
        transported_complete_equation_labels=["A2q0","A0q2","A1q2","A2q2"],
        reflection_source="A1q0",
        reflection_target="A2q0",
        reflection_x_phase=finite_coordinates(omega**-1,k),
        reflection_phase_cubed_equals_one=True,
        W_source_target_labels=[["A0q0","A0q2"],["A1q0","A1q2"],["A2q0","A2q2"]],
        original_complete_prime_field_product_table_count=306*307//2,
        coefficient_reflection_is_full_original_algebra_automorphism=True,
        W_comes_from_original_full_curve_and_identified_degeneracy_pullbacks=True,
        W_v_equals_cubed_x_correction_times_v_by_full_fraction_identity=True,
        all_original_W_forward_reverse_and_reflection_cross_products_retained=True,
        full_filtered_source_integral_return="T_n(a)=(xi-1)^n W(a); T_n^2=4^n",
        all_actual_fraction_denominators_nonzero_in_original_integral_domain=True,
        global_cleared_equations_precede_reduction_to_any_thick_quotient=True,
        denominator_cancellation_inside_nonreduced_quotient_used=False,
        whole_quotient_curve_and_unit_gates_unchanged=True,
        all_seven_equations_are_global_ring_identities=True,
        all_seven_equations_individually_reexpanded=False,
        unchanged_base_bridge_sha256=BASE_BRIDGE_SHA256)
    _progress(progress,"all seven original elliptic equations certified by complete transport",
              direct_labels=equation_transport["direct_complete_equation_labels"],
              transported_labels=equation_transport["transported_complete_equation_labels"],
              transport_certificate_sha256=digest(equation_transport))
    records = {tag:actual[tag].receipt() for tag in (
        "ys","vs","T","N0","T0","T2","epsilon","F_x_over_xs","F_y")}
    endpoint_records = [{tag:row[tag].receipt() for tag in ("x0","y0","x2","y2")}
                        for row in actual["A"]]
    receipt = {
        "kind":"rank2_original_Y_fraction_consumer_maps",
        "status":"same_original_maps_and_all_endpoint_CM_reflection_identities",
        "prime":r,"level":3468,"normalization_module_rank":306,
        "same_original_constant_routine_reused":True,
        "original_sigma_a_index":[2,0,1],
        "ordered_packet_embeddings":[int(c["embedding"]) for c in constants["rows"]],
        "theta17_in_original_local_constants":finite_coordinates(theta,k),
        "theta17_is_constant_not_a_missing_function":True,
        "all_original_lambda_h_dnew_scales_retained":True,
        "original_v_and_epsilon_retained":True,
        "first_factor_x_correction":"(v+4)/v",
        "actual_degeneracies":"pi1=q0, pi2=fixed central base, pi4=q2",
        "all_j_to_power_m_differential_factors_retained":True,
        "all_seven_original_elliptic_equations_checked_by_full_ring_identity":True,
        "complete_original_equation_transport":equation_transport,
        "all_original_W_and_constant_reflection_identities_checked":True,
        "W_implemented_on_proved_original_expression_generators":True,
        "whole_arbitrary_M2_W_matrix_claimed":False,
        "coefficient_Frobenius_distinct_from_function_power_and_Artin":True,
        "embedding_source":embedding_receipt,
        "actual_original_root_embeddings":root_embedding_records,
        "compact_original_roots_used":compact_context is not None,
        "complete_compact_to_original_cross_identity_receipts":compaction_records,
        "actual_RF_section_power":RF_power,
        "actual_RP_section_powers":[int(root_source["RP"][i]["section_power"])
                                    for i in (0,1,2)],
        "old_cube_self_identity_receipts_not_reused_for_new_coordinates":True,
        "actual_scalar_fractions":records,"actual_endpoint_fractions":endpoint_records,
        "exact_shared_base_polynomial_cancellations":model.scalar_cancellations,
        "complete_intersections_computed":False,"original_shadow_computed":False,
        "helper_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "original_constant_consumer_sha256":hashlib.sha256(Path(legacy.__file__).read_bytes()).hexdigest(),
    }
    actual.update({
        "kind":"rank2_original_Y_fraction_consumer_context",
        "prime":r,"constants":k,"omega":omega,"model":model,
        "artin_constants":constants,"cube_context":cube,
        "compact_context":compact_context,
        "embedding_context":embedding,"original_affine_context":affine_context,
        "first_certificate":maps["first_certificate"],
        "packet_certificate":maps["packet_certificate"],
        "certificate":receipt,
    })
    _progress(progress,"same original two-endpoint maps certified in normalization",
              prime=r,all_original_equations=True,original_Artin_order=[2,0,1])
    return actual, receipt

