#!/usr/bin/env sage-python
"""Fixed small full-graph checks of the streamed same-MD source return.

This exercises actual selected-label bindings only in the software process.
It compares complete original X/Y graphs and both full ideal lengths, keeps
the actual F_y attached-HNF route, and tests the existing scalar-primary
binding.  It is neither a rank-306 run nor permission to change production.
"""
import os
if (os.environ.get("GITHUB_ACTIONS") != "true" or
        os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public"):
    raise SystemExit("Use only the named public research Actions.")

from copy import copy
import hashlib
import importlib.util
from pathlib import Path
import time
from sage.all import GF, QQ, PolynomialRing, identity_matrix, matrix

import original_streamed_denominator_return as candidate
import original_function_field_denominator_return as same_md
import original_cyclic_denominator_return as cyclic
import original_complete_quadratic_returns as complete_returns
import original_scalar_primary_return as scalar_primary
import original_scalar_base_divisor_support as scalar_support

values = candidate.values
ideal_tools = candidate.ideal_tools
norm_tools = candidate.norm_tools
HERE = Path(__file__).resolve().parent
STARTED = time.monotonic()
TOTAL_SECONDS = 420
PINNED = {
    "check-original-function-field-denominator-return.py": "07b8e39757e998a91b64c2114253ec6072ebdb19ab53aeed58b3dea625c090eb",
    "check-original-scalar-base-divisor-support.py": "3dd124a953a0a5dc160dd35a3a6ef6a04af11cf0231a947b32053cec40af297c",
    "original_affine_fast_operations.py": "1e0ffc3533022e17ca3da39e6cdd85997425f1150f6bb943d8e9a500e632c67b",
    "original_affine_multiplication.py": "ff55083ab0e25d6b44991b64fa9cdc63d397842add1c474459e42986437e65a2",
    "original_complete_quadratic_polynomials.pyx": "7742254770d03bbdab649902e4a9faf92dc7e82c0fb360d279b496b7eb7ed917",
    "original_complete_quadratic_returns.py": "7da06cd12f35f7f2b98bf0c2c247c2732c838924c5497d3b8755b34932ce6d09",
    "original_degree_bounded_row_reduction.py": "41be1b362e024ba847240c7bd928ae4e991b3c160d1c3556f7d8837d9b1788fa",
    "original_full_w_basis_transport.py": "85cc92c3536fc0a326d3d51f6fb553f823fb1d63f70622ba4caa9ebd33680af8",
    "original_function_field_denominator_return.py": "0a1b6232348067cf9deb49498d97f9d32a0213dc3ef12d882d83ae35f00df5c4",
    "original_polynomial_row_reduction.py": "9e3413176d9cce5fa00836ee05ea450483c60a786407b40fcef2ae226f009936",
    "original_projector_hermite.py": "545b330c4b7fb0c876e15f0ea6b94c9e35d29fdaf94b87707b3853dd33c32545",
    "original_scalar_base_divisor_support.py": "c84656c73bb062958c233de20fbed4fb889779985d154058548305e02d73e39a",
    "original_scalar_primary_return.py": "d8d4f90b667d2d66346636e69d764207c84de1ebb5d82c4cfa55d4ca7a87c7d3",
    "original_section_ring_embedding.py": "d43d5c31bf6b0ac69bbc80a532efbb458349299f6229c2dfa70f4b2952274687",
    "original_triangular_artinian_values.py": "9327760e26f1666dcd04a22b964b3b15a67b3e7d66e4f66bee84dd350b73db5d",
    "original_triangular_preimage_tools.py": "f1f3f7925bfdc32e771111c4a512a81470229473fd25f9193cd3a6f38a22d9fd",
    "original_w_ideal_transport.py": "f6c87d36f4ded0e7e14e6e025cbbcc169bef30422b60d791a394a853aa536c58",
    "original_ys_artinian_norm_tools.py": "f604ae5f862519f5ccdce609a78ef05866fd85ae81ea699fb1de06f47b550714",
    "original_ys_closed_point_tools.py": "7428cadb6b2179aebd547c749ec11ae46305476947aa443f7266e64d03ccc7bb",
    "original_ys_divisor_ideal_tools.py": "661075eecb9c7ba67da615c89fd3b7dbf2834b08ca8e1534c1713894dc1226d7",
    "original_ys_fraction_bridge.py": "788949117cba32c3ce347257ab71681bfe4a6940f935e017efef852c6ea4d9b8",
    "original_ys_geometry_transport.py": "cb39ebfb3b7adfa63c5d0ec2483354621938eb52381e957977f5e8f1544cd371",
    "original_ys_integral_image_tools.py": "268ae368f0aea343b1490d2245d19475e82c193a3dd4f2e0cc747aec49ff86c0",
    "original_ys_local_value_tools.py": "566f231e614f4b961cbd695318a159ee92b08a99de2da6f4c8786474e832b5a1",
    "original_ys_scalar_colon_tools.py": "b643b02deb3948d352a3fc252008f9fb939bef5083184f7c9cc85653ef3a8436",
    "section_quotient_algebra.py": "4c66da67ab76a61c075367a9a23801b726ebaa6ed098226dd943a708020a0536",
    "original_pair_reset_row_reduction.py": "ffa85755931dfb3b52e68a50981ad4db6b49714287efe92e0403922a8eef802f",
    "original_native_pair_reset.py": "a270a003fbbe80d3cced1856fb19707ab83cb250bc57d2152da5583978fd7e28",
    "original_native_polynomial_rows.pyx": "c940f1759238103c85bf01bf22427394c87524eaf7ebe3f08488457447246922",
    "original_row_operation_right_return.py": "ce7675e8b57fee62a2b5c7907a5cd5887759e4d72bc1e4117f04c4032e4dc225",
    "original_cyclic_denominator_return.py": "4ebbe8018347d9bf6269d6e0d83960224bb399fa5ae1998b7d91e3c1ba96fbf1",
    "original_streamed_denominator_return.py": "e315b6a330df38d370657d1db68a4b3a6ebe161509d92d9b239e6da8c89b542f"
}
ORIGINAL_GRAPH_REFERENCE = candidate.ORIGINAL_GRAPH
ORIGINAL_DIVIDE_METHOD = same_md.SameDenominatorImageSession.divide
ORIGINAL_RELEASE_METHOD = same_md.SameDenominatorImageSession.release
ORIGINAL_WRAPPER = same_md.paired_graph_with_same_denominator_image


def deadline():
    if time.monotonic()-STARTED >= TOTAL_SECONDS:
        raise TimeoutError("The fixed complete same-MD software-check budget was exhausted.")


def progress(stage, **data):
    deadline()
    print("RANK2_STREAMED_SAME_MD_STAGE "+
          ideal_tools.canonical(dict(stage=stage, **data)), flush=True)


def verify_pins():
    for name, expected in PINNED.items():
        assert hashlib.sha256((HERE/name).read_bytes()).hexdigest() == expected
    candidate.verify_source_pins()
    assert same_md.SameDenominatorImageSession.divide is ORIGINAL_DIVIDE_METHOD
    assert same_md.SameDenominatorImageSession.release is ORIGINAL_RELEASE_METHOD
    assert same_md.paired_graph_with_same_denominator_image is ORIGINAL_WRAPPER
    assert candidate.ORIGINAL_GRAPH is ORIGINAL_GRAPH_REFERENCE
    return dict(PINNED)


def monic_determinant(H):
    assert H.is_hermite() and H.nrows() == H.ncols()
    answer = H.base_ring().one()
    for i in range(H.nrows()):
        assert H[i,i] and H[i,i].leading_coefficient() == 1
        answer *= H[i,i]
    return answer


def known_cyclic_H(R,n,q):
    H = copy(identity_matrix(R,n))
    t = R.gen()
    H[n-1,n-1] = q
    for i in range(n-1):
        H[i,n-1] = (t**(i+1)+(i+2)*t+i+1) % q
    assert H.is_hermite()
    return H


def change_rows(H):
    M = copy(H)
    t,n = M.base_ring().gen(),M.nrows()
    if n > 1:
        M.swap_rows(0,n-1)
        M.rescale_row(0,2)
        M.add_multiple_of_row(1,0,t**2+1)
        M.add_multiple_of_row(0,n-1,t+3)
    return M


def verify_image_receipt(image,M,H):
    assert image["method"] == (
        "whole cyclic/content image or unchanged full fallback, streamed H-row certificates")
    assert image["implementation"] == candidate.IMPLEMENTATION
    assert image["original_rows_sha256"] == ideal_tools.polynomial_matrix_digest(M)
    assert image["complete_hermite_basis_sha256"] == ideal_tools.polynomial_matrix_digest(H)
    determinant = monic_determinant(H)
    assert image["full_monic_determinant_sha256"] == ideal_tools.polynomial_digest(determinant)
    assert image["determinant_degree"] == image["full_quotient_length"] == determinant.degree()
    cert = image["complete_image_certificate"]
    assert cert["both_polynomial_row_module_inclusions_verified"] is True
    assert cert["every_H_row_divided_completely_in_original_P"] is True
    assert cert["each_H_coordinate_row_discarded_before_the_next"] is True
    assert cert["every_original_MD_row_has_zero_full_Hermite_remainder"] is True
    assert cert["current_dynamic_original_remainder_used"] is True
    assert len(cert["complete_H_row_coordinate_sha256"]) == M.nrows()
    assert cert["full_coordinate_matrix_materialized"] is False
    assert cert["universal_full_transform_materialized"] is False
    forward = image["full_transcript_forward_return"]
    assert forward["complete_P_equals_E_M"] is True
    assert forward["E_or_any_universal_transform_materialized"] is False
    assert forward["complete_transcript"]["actual_coefficients_retained_in_this_invocation"] is True
    assert image["attached_block"] is False
    assert image["old_transposed_attached_hermite_reduction_executed"] is False
    assert image["official_function_field_hnf_executed_for_this_image"] is False
    assert image["universal_full_transform_materialized"] is False
    assert image["whole_coordinate_matrix_materialized"] is False
    assert image["all_original_rows_columns_and_nilpotents_retained"] is True
    assert image["old_tail_reset_algorithm_executed_for_this_image"] is bool(
        image["actual_old_tail_reset_phase_count"])
    if image["old_complete_reducer_executed_for_this_image"]:
        full = image["fallback_full_reducer_receipt"]
        phases = [p for p in full["phases"] if
                  p["phase"] == "whole unshifted tail reset after certified gcd pair"]
        assert len(phases) == image["actual_old_tail_reset_phase_count"]
        assert image["fallback_uses_exact_original_undivided_MD"] is True
        assert image["actual_content_restoration_used"] is False
    else:
        assert image["fallback_full_reducer_receipt"] is None
        assert image["actual_content_restoration_used"] is True
        assert image["cyclic_attempt"]["original_complete_popov_receipt"][
            "prefix_stopped_only_after_all_original_column_reductions"] is True
    return image


def verify_division(division,image,X,Y,N,D):
    assert division["method"] == (
        "same complete P=E*MD, factored actual W_i=(Y*MN)_i, C_i*P=W_i, X_i=C_i*E")
    for key in ("every_source_row_returned_against_original_denominator",
                "full_actual_coefficient_transcript_verified_at_both_ends",
                "same_actual_MD_P_H_and_transcript_used_for_every_source",
                "unique_X_from_original_nonsingular_MD",
                "original_complete_nonreduced_graph_retained"):
        assert division[key] is True
    for key in ("full_Y_times_MN_materialized","universal_full_transform_materialized",
                "whole_coordinate_matrix_materialized",
                "old_transposed_attached_hermite_reduction_executed",
                "cross_call_solved_image_or_transform_reused"):
        assert division[key] is False
    assert division["reduction"] is None
    assert division["same_complete_denominator_image_receipt_sha256"] == ideal_tools.digest(image)
    assert division["actual_source_Y_sha256"] == ideal_tools.polynomial_matrix_digest(Y)
    assert division["actual_source_MN_sha256"] == ideal_tools.polynomial_matrix_digest(N)
    assert division["complete_returned_X_sha256"] == ideal_tools.polynomial_matrix_digest(X)
    assert division["original_source_row_count"] == D.nrows()
    assert len(division["all_actual_source_row_returns"]) == D.nrows()
    for i,item in enumerate(division["all_actual_source_row_returns"]):
        assert item["original_source_row"] == i
        assert item["complete_C_W_P_equals_W"] is True
        assert item["complete_X_MD_equals_W"] is True
        reverse = item["reverse_right_return"]
        assert reverse["actual_source_rows"] == 1
        assert reverse["universal_transform_materialized"] is False
        assert reverse["every_original_operation_replayed"] is True
        assert reverse["simultaneous_two_column_Bezout_return"] is True
    executed = sum(item["reverse_right_return"]["actual_scalar_column_updates"]
                   for item in division["all_actual_source_row_returns"])
    assert executed == division["planned_complete_graph_reverse_scalar_updates"]
    assert executed == division["actual_complete_graph_reverse_scalar_updates"]
    assert executed <= division["complete_graph_reverse_scalar_update_budget"]
    component_peak = division["maximum_actual_prime_component_coordinate_work_cells"]
    if image["complete_cyclic_route_succeeded"]:
        assert component_peak is not None and component_peak >= 0
    else:
        assert component_peak is None
    assert division["combined_quadratic_coordinate_or_total_process_peak_claimed"] is False
    assert candidate.verify_factored_identity(X,D,Y,N) is True


def compare_graph(name,N,D,wanted_route,zero_numerator=False):
    deadline()
    snapshots = copy(N),copy(D)
    mutability = bool(N.is_mutable()),bool(D.is_mutable())
    original_X,original_Y,original = ORIGINAL_GRAPH_REFERENCE(
        N,D,progress=progress,label="software original "+name)
    official_H,official_U = copy(D).hermite_form(
        transformation=True,include_zero_rows=False)
    assert official_U*D == official_H
    before = len(candidate.denominator_return_audit())
    old_audit_before = len(same_md.denominator_return_audit())
    X,Y,returned = candidate.paired_graph_with_streamed_sources(
        N,D,progress=progress,label="software streamed same-MD "+name)
    assert len(candidate.denominator_return_audit()) == before+1
    assert len(same_md.denominator_return_audit()) == old_audit_before
    assert X == original_X and Y == original_Y
    assert X*D == Y*N and Y.is_hermite()
    assert (N,D) == snapshots
    assert (bool(N.is_mutable()),bool(D.is_mutable())) == mutability
    image = returned["complete_denominator_image"]
    verify_image_receipt(image,D,official_H)
    assert image["complete_cyclic_route_succeeded"] is (wanted_route == "cyclic")
    division = returned["full_paired_numerator_division"]
    verify_division(division,image,X,Y,N,D)
    assert returned["complete_denominator_preimage"]["entire_result_basis_sha256"] == (
        ideal_tools.polynomial_matrix_digest(Y))
    assert original["full_paired_numerator_division"]["reduction"]["attached_block"] is True
    assert returned["full_global_paired_identity_returned"] is True
    assert returned["all_original_denominator_source_vectors_retained"] is True
    probe = matrix(D.base_ring(),[
        [D.base_ring().gen()**((i+2*j)%4)+i+j+1 for j in range(D.ncols())]
        for i in range(2)])
    assert ideal_tools._hermite_remainder_rows(probe,Y) == (
        ideal_tools._hermite_remainder_rows(probe,original_Y))
    positive = None
    if zero_numerator:
        assert N.is_zero() and X.is_zero() and Y == identity_matrix(D.base_ring(),D.nrows())
    else:
        positive = copy(X).hermite_form(include_zero_rows=False)
        assert positive == copy(original_X).hermite_form(include_zero_rows=False)
        assert positive.nrows() == D.nrows()
    audit = candidate.denominator_return_audit()[-1]
    assert audit["original_denominator_sha256"] == image["original_rows_sha256"]
    assert audit["complete_denominator_image_receipt_sha256"] == ideal_tools.digest(image)
    assert audit["actual_old_tail_reset_phase_count"] == image["actual_old_tail_reset_phase_count"]
    assert audit["full_Y_MN_or_universal_U_materialized"] is False
    return dict(
        name=name,rank=int(D.nrows()),wanted_and_actual_route=wanted_route,
        entire_X_and_Y_equal_to_original=True,
        same_full_saturated_graph_by_complete_canonical_Y_and_unique_X=True,
        complete_denominator_image=image,complete_same_MD_division=division,
        complete_original_graph_sha256=ideal_tools.digest(original),
        complete_returned_graph_sha256=ideal_tools.digest(returned),
        full_pole_length=int(monic_determinant(Y).degree()),
        full_zero_length=None if positive is None else int(monic_determinant(positive).degree()),
        original_inputs_and_mutability_retained=True,
        original_same_MD_official_audit_not_reused=True)


def check_budget_session(N,D):
    old_X,old_Y,old = ORIGINAL_GRAPH_REFERENCE(
        N,D,progress=progress,label="software direct-budget original graph")
    session = candidate.StreamedDenominatorSession(candidate.StreamBudget(
        cyclic.CyclicBudget(max_native_cells=1,max_seconds=120)))
    try:
        H,attached,image = session.image(
            D,progress=progress,label="software direct-budget complete image")
        assert attached is None
        assert image["old_complete_reducer_executed_for_this_image"] is True
        assert image["actual_old_tail_reset_phase_count"] > 0
        verify_image_receipt(image,D,H)
        Y,preimage = values.complete_triangular_preimage(
            H,N,progress=progress,label="software direct-budget complete preimage")
        X,division = session.divide_factored(
            D,Y,N,progress=progress,label="software direct-budget all numerators")
        assert X == old_X and Y == old_Y and X*D == Y*N
        verify_division(division,image,X,Y,N,D)
        assert session.image_calls == session.division_calls == 1
        result = dict(
            name="actual allocation-budget fallback with actual reset and all streamed sources",
            complete_denominator_image=image,complete_same_MD_division=division,
            same_entire_X_Y_and_nonreduced_graph_as_original=True,
            original_reference_graph_sha256=ideal_tools.digest(old))
    finally:
        session.release()
    assert session.input_object is session.input_snapshot is session.P is session.H is None
    assert session.stream is session.tape is session.native_rows is None
    result["all_same_call_MD_P_H_and_actual_operation_objects_released"] = True
    return result


def refuse(label,call):
    before = len(candidate.denominator_return_audit())
    try:
        call()
    except (AssertionError,ArithmeticError,ValueError,TypeError,RuntimeError,AttributeError,MemoryError) as exc:
        assert len(candidate.denominator_return_audit()) == before
        return dict(name=label,rejected=True,exception=type(exc).__name__,message=str(exc))
    raise AssertionError("A deliberately invalid complete same-MD return was accepted: "+label)



def refuse_actual_output_budget(N,D):
    snapshots = copy(N),copy(D)
    mutability = bool(N.is_mutable()),bool(D.is_mutable())
    before_graph = len(candidate.denominator_return_audit())
    before_outer = len(candidate.outer_identity_audit())
    result = refuse("actual nonsingular full X exceeds one-coefficient output budget",
        lambda:candidate.paired_graph_with_streamed_sources(
            N,D,progress=progress,label="software exact actual-X budget refusal",
            budget=candidate.StreamBudget(max_returned_coefficients=1)))
    assert result["exception"] == "MemoryError"
    assert result["message"] == "The actual final canonical X exceeds its explicit output budget."
    assert (N,D) == snapshots
    assert (bool(N.is_mutable()),bool(D.is_mutable())) == mutability
    assert len(candidate.denominator_return_audit()) == before_graph
    assert len(candidate.outer_identity_audit()) == before_outer
    result.update(actual_nonsingular_two_by_two_fixture=True,
        actual_returned_coefficient_limit=1,
        both_original_inputs_and_mutability_unchanged=True,
        no_graph_or_outer_success_audit_appended=True)
    return result


def selected_and_F_bindings(N,D):
    old_hnf = values.complete_row_hermite
    old_division = values.full_polynomial_left_division
    old_preimage = values.complete_triangular_preimage
    old_binding = same_md.bind_original_denominator_return()
    preparation = candidate.prepare_source_bindings()
    binding = candidate.bind_original_streamed_denominator_return()
    assert candidate.bind_original_streamed_denominator_return()["already_bound"] is True
    assert values.complete_paired_fraction_graph is candidate._selected_endpoint_graph
    assert values.OriginalTriangularIdealEngine.zero_pole_ideals is candidate._selected_zero_pole_ideals
    fixture = old_sameMD_fixture().load_old_fixture()
    before = len(candidate.denominator_return_audit())
    before_outer = len(candidate.outer_identity_audit())
    selected = []
    for label in ("original A0 y0","original A1 y0"):
        for software_chart in (False,True):
            engine = fixture.SoftwareFiniteFreeEngine(infinity_chart=software_chart)
            t = engine.R.gen()
            num,den = (t+2)*engine.unit,(t-engine.fixture_eta)**2*engine.unit
            refpos,refneg,reference = candidate.ORIGINAL_ZERO_POLES(
                engine,num,den,label="software untouched reference "+label)
            forbidden = []
            def forbidden_old(*args,**kwargs):
                forbidden.append(True)
                raise AssertionError("The selected graph reached a replaced general callsite.")
            values.complete_row_hermite = forbidden_old
            values.full_polynomial_left_division = forbidden_old
            try:
                pos,neg,receipt = values.OriginalTriangularIdealEngine.zero_pole_ideals(
                    engine,num,den,label=label)
            finally:
                values.complete_row_hermite = old_hnf
                values.full_polynomial_left_division = old_division
            assert not forbidden
            assert pos.basis == refpos.basis and neg.basis == refneg.basis
            assert pos.length == refpos.length and neg.length == refneg.length
            assert pos.determinant == refpos.determinant and neg.determinant == refneg.determinant
            assert receipt["kernel"]["full_paired_numerator_division"]["reduction"] is None
            last = candidate.outer_identity_audit()[-1]
            assert last["actual_engine_object_id"] == id(engine)
            assert last["actual_infinity_chart"] is software_chart
            assert last["complete_identity_rechecked_after_both_original_ideals"] is True
            selected.append(dict(label=label,software_chart=software_chart,
                complete_original_graph_sha256=ideal_tools.digest(reference),
                complete_selected_graph_sha256=ideal_tools.digest(receipt),
                actual_original_positive_and_negative_ideals_equal=True,
                actual_third_complete_identity_after_both_ideals_executed=True))
    assert len(candidate.denominator_return_audit()) == before+4
    assert len(candidate.outer_identity_audit()) == before_outer+4
    assert values.complete_triangular_preimage is old_preimage
    calls = dict(image=0,division=0)
    def actual_old_image(*args,**kwargs):
        calls["image"] += 1
        return old_hnf(*args,**kwargs)
    def actual_old_division(*args,**kwargs):
        calls["division"] += 1
        return old_division(*args,**kwargs)
    before_F = len(candidate.denominator_return_audit())
    before_F_outer = len(candidate.outer_identity_audit())
    F_records = []
    for software_chart in (False,True):
        engine = fixture.SoftwareFiniteFreeEngine(infinity_chart=software_chart)
        t = engine.R.gen()
        num,den = (t+2)*engine.unit,(t-engine.fixture_eta)**2*engine.unit
        refpos,refneg,reference = candidate.ORIGINAL_ZERO_POLES(
            engine,num,den,label="software untouched F reference")
        values.complete_row_hermite = actual_old_image
        values.full_polynomial_left_division = actual_old_division
        try:
            pos,neg,receipt = values.OriginalTriangularIdealEngine.zero_pole_ideals(
                engine,num,den,label="original first factor yF")
        finally:
            values.complete_row_hermite = old_hnf
            values.full_polynomial_left_division = old_division
        assert pos.basis == refpos.basis and neg.basis == refneg.basis
        assert pos.length == refpos.length and neg.length == refneg.length
        division = receipt["kernel"]["full_paired_numerator_division"]
        assert division["method"] == "same full attached-column Hermite reduction and exact back substitution"
        assert division["reduction"]["attached_block"] is True
        F_records.append(dict(software_chart=software_chart,
            old_complete_graph_sha256=ideal_tools.digest(receipt)))
    assert calls == dict(image=2,division=2)
    assert len(candidate.denominator_return_audit()) == before_F
    assert len(candidate.outer_identity_audit()) == before_F_outer
    assert values.complete_triangular_preimage is old_preimage
    verify_pins()
    return dict(existing_official_session_binding=old_binding,new_optional_binding=binding,
        preparation=preparation,four_actual_selected_software_calls=selected,
        four_actual_third_outer_identities=candidate.outer_identity_audit()[before_outer:],
        both_original_F_label_software_calls=F_records,actual_old_F_calls=calls,
        four_software_calls_are_not_original_rank306_geometry=True,
        all_general_aliases_restored_and_only_two_labels_select_new_outer_method=True)


def old_sameMD_fixture():
    name = "check-original-function-field-denominator-return.py"
    spec = importlib.util.spec_from_file_location("_actual_sameMD_original_fixture",HERE/name)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def old_scalar_compatibility():
    module = old_sameMD_fixture()
    result = module.scalar_primary_compatibility_check()
    assert result["same_complete_original_and_new_scalar_primary"] is True
    return result


def main():
    verify_pins()
    preparation = candidate.prepare_source_bindings()
    native_binding = complete_returns.bind_original_returns()
    assert ideal_tools._hermite_remainder_rows is complete_returns.complete_remainder_rows
    assert norm_tools._whole_hermite_coordinates is complete_returns.complete_hermite_coordinates
    fp = GF(29)
    modulus = PolynomialRing(fp,"sameMD_modulus")
    k = GF(29**2,"sameMD_a",modulus=modulus.gen()**2-2)
    a = k.gen()
    R = PolynomialRing(k,"sameMD_t")
    t = R.gen()
    first = matrix(R,[[t,1],[1,t]])
    Nfirst = matrix(R,[[t+1,1],[0,t-2]])
    checks = [compare_graph("whole Popov not HNF",Nfirst,first,"cyclic")]
    H = known_cyclic_H(R,3,t**7*(t-1)**2)
    D = change_rows(H)
    D.set_immutable()
    N = matrix(R,[[t+1,1,a],[0,t-1,1],[0,0,t+2]])
    checks.append(compare_graph("immutable complete nilpotent input",N,D,"cyclic"))
    h = (t-a)**2*(t+1)**3
    checks.append(compare_graph("quadratic content with PRIME quotient retained in original ring",
                               N,h*D,"cyclic"))
    checks.append(compare_graph("scalar thick image over a unit quotient",N,
                               (t-a)**3*change_rows(identity_matrix(R,3)),"cyclic"))
    noncyclic = matrix(R,[[t**2,0],[0,(t-1)**2]])
    checks.append(compare_graph("noncyclic last vector uses unchanged complete input",
                               Nfirst,noncyclic,"fallback"))
    nonprime = matrix(R,[[(t-a)**2,t+a],[0,(t-a-1)**3]])
    checks.append(compare_graph("nonprime actual quotient uses unchanged complete input",
                               Nfirst,change_rows(nonprime),"fallback"))
    checks.append(compare_graph("zero numerator still returns whole graph",
                               matrix(R,2,2),first,"cyclic",zero_numerator=True))
    R41 = PolynomialRing(GF(41),"sameMD_s")
    s = R41.gen()
    D41 = change_rows(known_cyclic_H(R41,2,(s-1)**5*(s+2)**2))
    N41 = matrix(R41,[[s+1,1],[0,s-3]])
    checks.append(compare_graph("second original prime full graph",N41,D41,"cyclic"))
    checks.append(check_budget_session(Nfirst,first))
    assert len(checks) == 9

    session = candidate.StreamedDenominatorSession()
    returned_H,unused,image = session.image(first,progress=progress,label="software refusal fixture")
    assert unused is None
    fake_H = copy(returned_H)
    fake_H[0,1] += 1
    assert fake_H.is_hermite() and fake_H.det() == returned_H.det() and fake_H != returned_H
    wrong_ring = PolynomialRing(k,"different_sameMD_t")
    Qring = PolynomialRing(QQ,"rational_sameMD_t")
    def false_H():
        old = session.H
        session.H = fake_H
        try:
            session.certify_image()
        finally:
            session.H = old
    refusals = [
        refuse("wrong explicit budget object",lambda:candidate.StreamedDenominatorSession(budget={})),
        refuse("nonfinite constants",lambda:candidate.StreamedDenominatorSession().image(
               identity_matrix(Qring,2),progress=progress)),
        refuse("singular complete denominator",lambda:candidate.StreamedDenominatorSession().image(
               matrix(R,[[t,1],[t,1]]),progress=progress)),
        refuse("attached block outside exact image scope",
               lambda:candidate.StreamedDenominatorSession().image(
                   first,attached=identity_matrix(R,2),progress=progress)),
        refuse("rectangular original input",lambda:candidate.StreamedDenominatorSession().image(
               matrix(R,2,3),progress=progress)),
        refuse("same determinant wrong complete H",false_H),
        refuse("wrong actual forward transcript return",
               lambda:candidate.verify_forward_transcript(session.M0,
                   session.P0+identity_matrix(R,2),session.stream,session.budget,progress=progress)),
        refuse("different equal MD object",lambda:session.divide_factored(
               copy(first),returned_H,identity_matrix(R,2),progress=progress)),
        refuse("nonintegral entire factored source",lambda:session.divide_factored(
               first,identity_matrix(R,2),identity_matrix(R,2),progress=progress)),
        refuse("wrong full source ring",lambda:session.divide_factored(
               first,identity_matrix(wrong_ring,2),identity_matrix(wrong_ring,2),progress=progress)),
        refuse("second image in same session",lambda:session.image(first,progress=progress)),
    ]
    mutated_D = copy(first)
    changed = candidate.StreamedDenominatorSession()
    changed.image(mutated_D,progress=progress,label="software changed-object fixture")
    mutated_D[0,0] += 1
    refusals.append(refuse("same MD object changed after image",
                          lambda:changed.divide_factored(mutated_D,returned_H,
                              identity_matrix(R,2),progress=progress)))
    current_binding = values.complete_paired_fraction_graph
    values.complete_paired_fraction_graph = lambda *args,**kwargs: None
    try:
        refusals.append(refuse("foreign graph binding",
                              lambda:candidate.bind_original_streamed_denominator_return()))
    finally:
        values.complete_paired_fraction_graph = current_binding
    session.release()
    changed.release()
    refusals.append(refuse("released session cannot be reused",
                          lambda:session.divide_factored(first,returned_H,
                              identity_matrix(R,2),progress=progress)))
    refusals.append(refuse_actual_output_budget(Nfirst,first))
    assert len(refusals) == 15

    binding = selected_and_F_bindings(Nfirst,first)
    scalar_compatibility = old_scalar_compatibility()
    assert scalar_support.ScalarBaseSupportSession is scalar_primary.ScalarPrimaryReturnSession
    assert values.complete_paired_fraction_graph is candidate._selected_endpoint_graph
    assert ideal_tools._hermite_remainder_rows is complete_returns.complete_remainder_rows
    assert norm_tools._whole_hermite_coordinates is complete_returns.complete_hermite_coordinates
    verify_pins()
    deadline()
    files = tuple(dict.fromkeys(
        ("check-original-complete-quadratic-api.py",Path(__file__).name)+tuple(PINNED)+
        candidate.SOURCE_DEPENDENCIES+scalar_primary.SOURCE_DEPENDENCIES))
    assert set(files)-{"check-original-complete-quadratic-api.py",Path(__file__).name} == set(PINNED)
    report = dict(
        kind="original-streamed-same-denominator-return-software-check",status="PASS",
        source=os.environ["RANK2_SOURCE_SHA"],run_id=os.environ["RANK2_RUN_ID"],
        run_attempt=os.environ["RANK2_RUN_ATTEMPT"],
        root_readme_blob=os.environ["RANK2_ROOT_README_SHA"],
        topic_readme_blob=os.environ["RANK2_TOPIC_README_SHA"],
        source_file_sha256={name:hashlib.sha256((HERE/name).read_bytes()).hexdigest() for name in files},
        preparation=preparation,current_native_complete_return_binding=native_binding,
        checks=checks,complete_graph_comparison_count=len(checks),
        refusals=refusals,rejection_count=len(refusals),
        selected_and_untouched_F_binding_checks=binding,
        unchanged_actual_scalar_primary_compatibility=scalar_compatibility,
        actual_optional_graph_return_count=len(candidate.denominator_return_audit()),
        actual_optional_graph_return_audit=candidate.denominator_return_audit(),
        actual_selected_outer_identity_audit=candidate.outer_identity_audit(),
        separate_existing_official_graph_return_count=len(same_md.denominator_return_audit()),
        original_general_division_and_integral_multiple_unchanged=True,
        only_selected_outer_identity_source_is_explicitly_replaced=True,
        actual_original_rank306_geometric_input_executed=False,
        running_production_sources_or_requests_changed=False,
        software_process_only_selected_binding_exercised=True,
        performance_improvement_claimed=False,
        data_artifact_written=False,
        software_time_budget_seconds=TOTAL_SECONDS,
        elapsed_seconds=time.monotonic()-STARTED)
    payload = ideal_tools.canonical(report)
    print("RANK2_STREAMED_SAME_MD_API_RESULT "+payload,flush=True)
    print("RANK2_STREAMED_SAME_MD_API_SHA256 "+hashlib.sha256(payload.encode()).hexdigest(),flush=True)


if __name__ == "__main__":
    main()
