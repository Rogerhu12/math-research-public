#!/usr/bin/env python3
"""Request183: true completed-ten resume through sixteen frozen eight-direction blocks.

The actual178r3 nonzero-xi Decimal50 point is the explicit initial input.
One persistent full-ten owner, one global2400second science deadline,
and the frozen complete-three 6b55 search implement at most128 directions.
Every block after the first freshly forms all ten response columns.
Only the exact original eight-direction budget stop permits another block;
full20 rejection, original tolerance stop, exception or resource stop ends
the continuation. Original initial/final120 FD and scalar/453 consumers
remain actual evaluations. No old-nine zero-extension claim is made at
this genuinely nonzero ten-coordinate point.
"""
from __future__ import annotations
import argparse
import hashlib
import importlib.util
import json
import math
import os
from pathlib import Path
import signal
import sys
import time
import traceback

HERE=Path(__file__).resolve().parent
ENTRY='geometry_20261115_completed_ten_joint_newton_resume.py'
SCHEMA='R259-completed-ten-persistent-scaled-Newton-continuation-v1'
STATUS_NAME='completed-ten-joint-newton-resume-status.json'
RECIPE_SCHEMA='R259-completed-ten-persistent-Newton-resume-recipe-v1'
BASELINE_PRODUCER='geometry_20261115_fixed_power_ten_joint_newton_recipe.py'
BASELINE_PRODUCER_SHA='3e5c8a34f5043fac35addf09627e16e59dcfc7287bb7ec087805be5dcac1474e'
R3_ORIGIN=json.loads(r'''{"request_number":178,"engineering_revision":"r3","run_id":"43753070697","source_commit":"195cd2d42fe7f73b112022c1f06d50c7e7d9c154","producer_schema":"R259-fixed-power-ten-scaled-minimum-norm-Newton-full3-v1","producer_sha256":"3e5c8a34f5043fac35addf09627e16e59dcfc7287bb7ec087805be5dcac1474e","status_bytes":970477,"status_sha256":"d32b951ea9bdb1aaa1ade19f0844ca4eb96a89bb8fc0943c3cf453d6c22b4d8e","summary_bytes":80163,"summary_sha256":"d816bef85711aea3dcdc6ef29ed4fcb4aa0ee5a24ca24e9b7ef4a87c2f38fbef","compute_job_id":"132931097320","report_job_id":"132931551767","summary_parameter_path":"final.parameters","diagnostic_completed":true,"accepted_point_count":8,"parent_stop_reason":"Explicit eight full-ten direction budget completed","scientific_result":"R389-actual178r3-complete-ten-eight-acceptances-and-actual-restart.md","is_accepted_nonlinear_native_or_fullDN_field":false}''')
R3_WORDS=json.loads(r'''["0.30551471382432198523814373041712069362455716637942","0.21644607672744466942679076187410625232938633963972","0.34269525160550151302162044735633622663563341715322","-0.063225067257510646371192296956363431839929322140043","-0.017473501272827210698563735286418405241143848036754","0.93760846540451112661569039143271631681250959842143","1.0751298569617059521200106239875679541638261594461","0.68868739059146809583253612991050148797660361205307","0.93853260668276076994469929930064914787519663500352","0.00093743918442139073375164637457095209406810504324798"]''')
EXPECTED_TEN_BINDING='065b11752c4b72422df2d9564748f2418f0a277401877c00c359d72171eefcbd'
CONTINUATION_CONTRACT=json.loads(r'''{"maximum_eight_direction_blocks":16,"maximum_complete_ten_directions":128,"original_direction_budget_per_block":8,"original_real_backtracks_per_direction":20,"producer_total_wall_seconds":2400,"wall_deadline_restarted_between_blocks":false,"same_persistent_Decimal50_owner_across_blocks":true,"fresh_complete_ten_response_at_each_block_start":true,"continue_only_after_explicit_eight_direction_budget_stop":true,"no_retry_after_all_twenty_trials_rejected":true,"fixed_original_actual157_coordinate_scales_preserved":true,"initial_and_final_complete_120_FD_checks_not_per_block":true,"original_complete_final_consumers_preserved":true,"no_new_scientific_acceptance_gate":true}''')
OLD_PRODUCER='geometry_20261115_small_core_nine_control_decimal_residual_quadratic_recipe.py'
OLD_PRODUCER_SHA='54167dff0ce67e9f8fe0fa5d2899c35f0f99534077f2530d90b296eee7537100'
FAMILY='geometry_20261115_adjoint_selected_ten_control_family.py'
FAMILY_SHA='09240b33b82be3f595e82df05d93b309baefd6eeb74f1c34ba3a095cb2548016'
MODEL='geometry_20261115_adjoint_selected_ten_decimal_model.py'
MODEL_SHA='8cb8352b76be0770ab565de3b24907faa302a86a75660b9f5ffaa9a23cc6a9b7'
SEARCH='geometry_20261115_fixed_power_ten_scaled_newton.py'
SEARCH_SHA='6b55a6d223f0103bb0396a578d89cfd06c6b4888d38dbb4d518eaa3ecb6f2861'
PARENT_SOURCES=json.loads(r'''{"geometry_20261114_constrained_collocation.py":"70ad9123d414d2e46851812105759ff26f62946bf7c865b17b3386915c3a86f8","geometry_20261114_constrained_trust_warm.py":"5378b7d732dc768f154849a1138ea59a2571f1128cc507932d38d4f8bfb115f2","geometry_20261114_direct_operator_cell.py":"1774f8da00ccd8ced6199e85d1fda6f455a224eed7d20d1a92ac04df3801e2ce","geometry_20261114_full_dn_augmented.py":"f76b9c37b8549bc670ad5fe95ccc2da6c1da1a967256f21d23eba4973495d87e","geometry_20261114_full_dn_boundary.py":"4517274cc4e79a7264d5980e79bbd209d73761f86ae7b015a2fa5671cca35ca2","geometry_20261114_full_prefix_operator.py":"a9a25d96eeb286d9f2214f997c992e50e42f6e6ec2bc59c136a183febe2a0703","geometry_20261114_full_scalar_profile.py":"8ff23e31a58d0f8b087929d69ac8d6f9b6f2777615e50eef5ebe40ed7b6bed6b","geometry_20261114_lifted_modes_profile.py":"13cd479d91590a6ce7a82e6461d6cd2c1561d7303264680621e9cbe438b7cee5","geometry_20261114_physical_test_boundary.py":"3975eb0daf8941516962a46d33efef614aa1f9759a979165e7cc0f83a2838681","geometry_20261114_prefix_controls_profile.py":"f019e6b33c8e1776d5cca87c22efadd0f999766b894be855efb53ad10b4d6a24","geometry_20261114_small_core_resonance.py":"3b9c45abed425a92be662c3547d088a3074ebcc5923c23ac2ef7aaf003124bd5","geometry_20261115_nine_control_direct_normal_full_merit_candidate.py":"485e5fd8b71bce6365084cca518a2b42e2e58d302933bd868c38995b59ad6a55","geometry_20261115_nine_control_directional_complex_response.py":"50044473f14b34c9451360debaa1ec9189f0a7924957098cafc37df3f849643f","geometry_20261115_nine_control_same_trace_full_merit_candidate.py":"d4c9cd448b81e3c506984a273cb0e050cf806ebc109ad4d2b140cec9fa8d2cbf","geometry_20261115_small_core_damped_resume.py":"ec9a56fd184ff7d68fd1caadc9d350312b075172d20dabdee5203ce5b491ad1a","geometry_20261115_small_core_damped_search.py":"1691c7d9aad782f9f1a6308ca16fa9630a44988a1b99decdca594a412cdb1728","geometry_20261115_small_core_four_control_curved_recipe.py":"3ca1bdf723e7c44f808ed786ccda854775c262d28ce92804fde2c8ca86cad160","geometry_20261115_small_core_four_control_family.py":"9222390b73abbd2e8bc4a1f8e9d8b861cd66b4a927b21629deb2e6b70073dd11","geometry_20261115_small_core_full3_curved_normal_recipe.py":"be37ce213ddfd87972b5edc241a0b220fe0f424c553f5836b5df337ff1dd980e","geometry_20261115_small_core_full3_retry_trust_recipe.py":"b9fff58becdfdcfdb4877cd789a3160510c7c2895005239d8989bb7673c2ea20","geometry_20261115_small_core_full3_trust_recipe.py":"5d3540150390f0e820200ba4a210eb2bc8d06bc025a0a677160df97d72e6f4c1","geometry_20261115_small_core_inexact_p3_eta_0p01.py":"f43c20ea6b8a5616b4330870897a1d0b6bd2c157435544366af1fe70dcdff7bd","geometry_20261115_small_core_inexact_p3_eta_0p01_recipe.py":"3169b2d3ea821a244d9f27611cd6c5cb3b239cf0e7f9bbbd7f49ac9d5f1dc9ee","geometry_20261115_small_core_inexact_p3_restoration.py":"ce93a364f8423c89e9e696e1e2c96662b61c6daaf225bd51c44fcd572e05654e","geometry_20261115_small_core_nine_control_carried_radius_recipe.py":"ed78684f93c76cf1695a3a54f04d28528b5505fccf115b6fd6afddc7a657cd50","geometry_20261115_small_core_nine_control_curved_recipe.py":"824c0967e5de5cc9079a80018b66b1232c78ce406a6de4e0d7ab4cdee876bdaf","geometry_20261115_small_core_nine_control_direct_normal_response_recipe.py":"c717bafb95854bef7b60048a8194b9949a30fbff29bc5e1eee8a0dbb25cf233b","geometry_20261115_small_core_nine_control_directional_response_recipe.py":"5acf5b029a756a356a3de3d598211eaa89df4a7670fc703f2d3567488e09bae4","geometry_20261115_small_core_nine_control_family.py":"086572f9a9fc172d671f050e9b343b66c4a57c5c88867537a1e8a3daa5ab9629","geometry_20261115_small_core_nine_control_same_trace_merit_recipe.py":"e8704af6daa13eac4d0301a6ef1debdca4c9cb0b10a806544644a2e1d162329a","geometry_20261115_small_core_p3_inner_root_search.py":"3b48efd71eb696fef66acbe7fbd163bb8dc8ca63287bfa8c4e873a2600fbf9d9","geometry_20261115_small_core_six_control_curved_recipe.py":"e154afe28c588ce0c2ae936d4304b67ec84e2b46c96b03e48ce4113e2401a761","geometry_20261115_small_core_six_control_family.py":"79464f9c6af8863d3c65254701a858f067881b22ca80dba24bacf2bfea484acf","geometry_20261115_nine_control_decimal_literal_model.py":"2422be0c2e30d10c38b56ff7b68412c5397d37ed36451676bb16acbdc142ef75","geometry_20261115_nine_control_decimal_curved_search.py":"433d5ddd2587efa581fb28ea151ddf3cec5b6a63eb5017340375d1f19b6d98d0","geometry_20261115_small_core_nine_control_decimal_recipe.py":"66906f121c52f6dc57894efa368299990eea45f2f1d4fc5e6ce4af2fc5b9536e","geometry_20261115_nine_control_decimal_second_variation.py":"ad568abc8bf35003375d80e303c44df6dcb2f1c75fd41163cf5c0f423ba321a1","geometry_20261115_nine_control_decimal_ambient_trust.py":"bb603fc6c32f146552262b38648ddc2e777e5968a1473259ad6d1e6ce2a86115","geometry_20261115_small_core_nine_control_decimal_curvature_recipe.py":"3d59811078d82110449216a8ab5dadf905c435e1e45085b96f6d1c8fa04eb0c4","geometry_20261115_nine_control_decimal_residual_quadratic_trust.py":"ef61c5f19370a302b198901a7691fda31ed0a6619d9f9dcafc147f6b1bdc3180","geometry_20261115_small_core_nine_control_decimal_residual_quadratic_recipe.py":"54167dff0ce67e9f8fe0fa5d2899c35f0f99534077f2530d90b296eee7537100"}''')
ACTUAL_PARENT=json.loads(r'''{"origin":{"repository":"Rogerhu12/math-research-public","run_id":"43729310294","source_commit":"c71cbeac7fd13c65cf50c7eb39842e9949737b25","producer_file":"geometry_20261115_small_core_nine_control_decimal_residual_quadratic_recipe.py","producer_sha256":"54167dff0ce67e9f8fe0fa5d2899c35f0f99534077f2530d90b296eee7537100","producer_schema":"R259-nine-control-persistent-decimal50-residual-quadratic-square-trust-v1","status_bytes":51842612,"status_sha256":"931b013b6cfaba4215065e0734c129ba2089662273427f7ebecc5df4f35ee2b0","log_summary_bytes":89063,"log_summary_sha256":"7411fd01db054215e5d22293f6a4c239aa482302bf75b4da123f35d500d0cad2","chain_bytes":29684,"chain_sha256":"9d8bf161d9b88c0c411d326b1717fd2d32332a49534041ebd495b673a35652bd","parameter_field":"final.parameters","radius_field":"final_relative_trust_radius"},"literal_parameters":["0.30552142546786087419329326763885317892313777930545","0.21644987290946319325196797861927627381324526334114","0.34270150727769461288268268825412573632054712673319","-0.063223623342288894213621979760433326917938764055697","-0.017474541697462463794792191406211542045739295377083","0.93761104499027068067117010211647732552611947830979","1.0751309729055790270477681013298138652831191583353","0.68868893897292614021176494008067699691013641552647","0.93853282406083699927458787857662556746972349511891"],"parent_relative_trust_radius":"0.0000390625","literal_binding":{"actual_binary64_input_table_words_still_only_lifted":true,"arrays":{"base":{"dtype":"float64","exact_Decimal_from_float_lift":true,"raw_C_order_sha256":"5a26da19688c7d77b9c20bc3d90f39b4b84038788ed4bc696b724c512ccd96dd","shape":[699,2]},"base_mid":{"dtype":"float64","exact_Decimal_from_float_lift":true,"raw_C_order_sha256":"0c375941ce46d907c4b8b4532a97a8721f88e582473dce891f41922191173703","shape":[698,2]},"controls":{"dtype":"float64","exact_Decimal_from_float_lift":true,"raw_C_order_sha256":"6523f85bd59aeb25c1e9f3d791d9ac79ef1408b007731a3c91d060466c265f2a","shape":[699,2,9]},"controls_mid":{"dtype":"float64","exact_Decimal_from_float_lift":true,"raw_C_order_sha256":"532a6ddb558dab6dce208ebc8e2f79aa52a2ac6c3739a5c7aa727818ba7cc8e6","shape":[698,2,9]},"frequency":{"dtype":"float64","exact_Decimal_from_float_lift":true,"raw_C_order_sha256":"51c16f13beb17c892ed884b329f39d62a6d4318ec7f3d0004f24dcb18872c76f","shape":[3]},"h":{"dtype":"float64","exact_Decimal_from_float_lift":true,"raw_C_order_sha256":"ee6981d6d293a1d067fd7fb53e4ea4ea93b1a4e7406364a3dc503c83162266e7","shape":[698]},"mesh":{"dtype":"float64","exact_Decimal_from_float_lift":true,"raw_C_order_sha256":"3b837d4580a1dff2575208ef6fc76bc19021e744eb6b37277040a2fbc9eb350e","shape":[699]},"mid":{"dtype":"float64","exact_Decimal_from_float_lift":true,"raw_C_order_sha256":"f06f265bd25b0d1d499f94b984caca930f00e357348a8d58372f2875430d263f","shape":[698]},"native_slope_J":{"dtype":"float64","exact_Decimal_from_float_lift":true,"raw_C_order_sha256":"44039f96cb20b0edca76a843a44f40235fbfbf72c19093a12a212c1cf6eb655d","shape":[112,112]},"target":{"dtype":"float64","exact_Decimal_from_float_lift":true,"raw_C_order_sha256":"8ca034c42495150b10a778e9cad2a338837e06c275b36490301f0b656c181585","shape":[3]}},"canonical_binding_sha256":"cc10a080eafa19e282ca22cefa62af57dadaf0ab19e54b0a4e6f7e7188ec32d3","complete_original_tail_J_consumed":true,"continuous_metric_or_interval_roundoff_certificate_claimed":false,"cut_scale_exact_binary64_lift":"0.99681527853612494904922414207248948514461517333984375","decimal_digits":50,"exactly_diagonal_as_original_record":true,"field_and_tail_modes":112,"forward_is_real_expression_variation_not_discrete_rounding_derivative":true,"height_sign_exact_binary64_lift":"-1","input_table_formation_recomputed_in_higher_precision":false,"original149_literal_model_binding_sha256":"c201e4b709df8f6cf1be61b0d71b19732b4a3cb78b1e56d799f10db1c7760368","original149_primal_body_reused_without_replacement":true,"original149_primal_source_sha256":"2422be0c2e30d10c38b56ff7b68412c5397d37ed36451676bb16acbdc142ef75","original_mesh_nodes":699,"original_three_frequencies":[2,4,6],"parameter_dimension":9,"rounding":"ROUND_HALF_EVEN","schema":"nine-control-persistent-decimal50-literal-circle-model-v1","second_variation_all9_axes_and45_pairs":true,"second_variation_schema":"nine-control-decimal50-complete-second-forward-v1","solve2_is_same_real_linear_system_not_the_old_LAPACK_rounding_path":true}}''')
INPUTS=json.loads(r'''{"accepted":"b4d2b98abc1da2dd149ca28e83ea17963a0d2a50b3c454baabc92f6229b412ff","prepared":"0f94dd88b4ad43a58694e25c8dded46cddcf96939abae1dc21416adb50042714","tail_anchor":"e788a28deca2720f1b530c0f60a9301578cc83398b8fbf8aa451df25f320ba51","tail_config":"01930f3bcb365d77f7e7959b021b95e7c38a3f5c8d05671747ec6359349454c5"}''')
POLICY=json.loads(r'''{"complete_parameter_dimension":10,"complete_residual_dimension":3,"selected_support_index":1,"selected_power":4,"selected_catalogue_index":3,"original_nine_relative_scale":"0.01","new_xi_absolute_scale":"0.01","fixed_scales_use_actual157_nine_input_words":true,"scales_recomputed_after_acceptance":false,"scaled_trust_radius":"1","original_parent_radius_is_provenance_only":true,"full_ten_direction_budget":8,"original_real_backtrack_budget":20,"proposal":"column-pivoted QR of complete transpose(J*S), minimum-norm solve then radial clip","fallback":"complete scaled Cauchy direction after recorded Newton arithmetic failure or nonnegative formed slope","scalar_residual_rows_reweighted":false,"normal_matrix_formed":false,"singular_value_cutoff_or_rank_acceptance_gate":false,"normal_curved_path_used":false,"post_rejection_same_point_retry":false,"original_full3_strict_slope_and_exact_binary64_lift_Armijo":true}''')
FIXED_SHAPE=json.loads(r'''{"catalogue_index":3,"support_index":1,"power":4,"family":"geometry_20261115_adjoint_selected_ten_control_family.py","family_sha256":"09240b33b82be3f595e82df05d93b309baefd6eeb74f1c34ba3a095cb2548016","selection_origin":{"request_number":164,"engineering_revision":"r3","run_id":"43743904448","source_commit":"257b227a49034faaf1979bfe093122e7d06e1785","status_bytes":565694,"status_sha256":"0f9c86d1f8e1ad94bcf83dc32ea4774534cf3f0854c696b9806905cc6397cb53","summary_bytes":89762,"summary_sha256":"33ca4bc6d9dc545d75ccb625d16d588d7298f259c0b1896df3a1351b65f0716b","scientific_result":"R373-actual164-r3-six-shapes-and-twenty-full-merit-rejections.md"},"same_original_family_function_not_same_direction_or_algorithm":true,"selection_not_recomputed_at_current_or_perturbed_points":true,"actual157_nine_words_remain_the_initial_numerical_parent":false,"actual157_words_only_fixed_scale_basis_for_this_nonzero_ten_resume":true}''')


class ResourceStopped(RuntimeError):
    pass


def require_actions():
    if (os.environ.get('GITHUB_ACTIONS')!='true'
            or os.environ.get('GITHUB_REPOSITORY')!='Rogerhu12/math-research-public'):
        raise RuntimeError('Scientific execution is public repository Actions only')


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def source_module(name,wanted):
    if Path(name).name!=name or sha(HERE/name)!=wanted:
        raise ValueError('The source identity differs: '+name)
    spec=importlib.util.spec_from_file_location(name[:-3],HERE/name)
    module=importlib.util.module_from_spec(spec);sys.modules[spec.name]=module
    spec.loader.exec_module(module)
    return module


def recipe(path,wanted):
    raw=Path(path).read_bytes()
    if len(raw)>32768 or hashlib.sha256(raw).hexdigest()!=wanted:
        raise ValueError('The complete explicit completed-ten recipe differs')
    data=json.loads(raw)
    origin=data.get('origin',{})
    words=data.get('initial_ten_parameter_words')
    if (data.get('schema')!=RECIPE_SCHEMA
            or data.get('fixed_scale_original_actual157_words')!=ACTUAL_PARENT['literal_parameters']
            or data.get('fixed_scale_origin')!=ACTUAL_PARENT['origin']
            or data.get('original_parent_radius_provenance')!=ACTUAL_PARENT['parent_relative_trust_radius']
            or data.get('expected_original_literal_binding')!=ACTUAL_PARENT['literal_binding']
            or data.get('expected_ten_literal_binding_sha256')!=EXPECTED_TEN_BINDING
            or data.get('input_sha256')!=INPUTS or data.get('policy')!=POLICY
            or data.get('continuation_contract')!=CONTINUATION_CONTRACT
            or data.get('fixed_shape')!=FIXED_SHAPE
            or not isinstance(words,list) or len(words)!=10
            or any(not isinstance(x,str) or not x for x in words)):
        raise ValueError('Keep the explicit actual ten-state, original literal tables, fixed shape and unchanged scales')
    if origin.get('producer_schema')==R3_ORIGIN['producer_schema']:
        if origin!=R3_ORIGIN or words!=R3_WORDS:
            raise ValueError('The first resumed point is the actual178r3 original ten-word state')
    elif origin.get('producer_schema')==SCHEMA:
        if (origin.get('producer_sha256')!=sha(__file__)
                or origin.get('diagnostic_completed') is not True
                or not isinstance(origin.get('accepted_point_count'),int)
                or origin['accepted_point_count']<1):
            raise ValueError('Own-schema resumption requires an explicitly recorded completed accepted ten point')
        for key,size in (('status_sha256',64),('summary_sha256',64),('source_commit',40)):
            value=origin.get(key)
            if (not isinstance(value,str) or len(value)!=size
                    or any(c not in '0123456789abcdef' for c in value)):
                raise ValueError('The actual completed parent byte identity is absent: '+key)
        if (not str(origin.get('run_id','')).isdigit()
                or any(not isinstance(origin.get(key),int) or origin[key]<=0
                       for key in ('status_bytes','summary_bytes'))):
            raise ValueError('The actual completed parent run/size identity is absent')
    else:
        raise ValueError('Do not relabel any nine-state, projection or unrelated producer as a completed ten parent')
    return raw,data


def continue_original_blocks(search_module,model,state,initial_J,scales,status,
                             checkpoint,event_sink,check_budget,k):
    """Only orchestration and provenance; the frozen8-by20 numerical function is unchanged."""
    maximum=CONTINUATION_CONTRACT['maximum_eight_direction_blocks']
    all_records=[]
    blocks=[]
    status.update(continuation_blocks=blocks,outer_steps=all_records,
        complete_outer_direction_budget=128,complete_real_trial_budget_per_direction=20,
        unvisited_outer_indices=list(range(128)),unvisited_block_indices=list(range(maximum)),
        accepted_point_count=0,attempted_outer_directions=0,original_trial_records=0,
        scaled_trust_radius=k.ONE,stop_reason=None)
    J=initial_J
    for block_index in range(maximum):
        check_budget()
        if blocks:
            blocks[-1]['continued']=True
        offset=8*block_index
        block=dict(index=block_index,global_direction_offset=offset,started=True,
            phase='starting',initial_ten_parameter_words=list(state['parameters']),
            original_search_source_sha256=SEARCH_SHA,original_eight_search_completed=False,
            accepted_point_count=0,attempted_outer_directions=0,original_trial_records=0,
            stop_reason=None,continued=False)
        blocks.append(block)
        status['unvisited_block_indices']=list(range(block_index+1,maximum))
        status['current_block_index']=block_index
        checkpoint()
        if block_index:
            with model.context('resume-block-'+str(block_index)+'-fresh-complete-ten-response'):
                J,response,forward_state=model.response(list(state['parameters']),
                    label='all-ten-current-resume-block-axes')
            block.update(first_J_source='fresh-complete-ten-response-at-owned-current-point',
                first_forward_report=response,
                first_forward_equation_words_equal_owned_primal=(
                    forward_state['equation']==state['equation']))
        else:
            block['first_J_source']='global-initial-description-complete-ten-forward'
        block_status={}

        def synchronized_checkpoint():
            current=block_status.get('outer_steps',[])
            for row in current:
                row['block_index']=block_index
                row['global_direction']=offset+row['direction']
                if (block_index and row.get('direction')==0
                        and row.get('initial_complete_ten_J_from_initial_description') is True):
                    # Correct the frozen block API's generic label; no numerical value changes.
                    row['initial_complete_ten_J_from_initial_description']=False
                    row['initial_block_J_from_fresh_complete_current_response']=True
            status['outer_steps']=all_records+current
            status['accepted_point_count']=sum(row.get('accepted') is True
                for row in status['outer_steps'])
            status['attempted_outer_directions']=len(status['outer_steps'])
            status['original_trial_records']=sum(len(row.get('trials',[]))
                for row in status['outer_steps'])
            status['unvisited_outer_indices']=list(range(len(status['outer_steps']),128))
            status['current_accepted_ten_parameter_words']=block_status.get(
                'current_accepted_ten_parameter_words',list(state['parameters']))
            status['stop_reason']=block_status.get('stop_reason')
            block.update(phase='original-eight-direction-search',
                accepted_point_count=block_status.get('accepted_point_count',0),
                attempted_outer_directions=len(current),
                original_trial_records=sum(len(row.get('trials',[])) for row in current),
                stop_reason=block_status.get('stop_reason'),
                unvisited_local_direction_indices=block_status.get('unvisited_outer_indices',list(range(8))))
            status['complete_planned_outer_rows']=[
                dict(index=i,started=i<len(status['outer_steps']),
                    stop_reason=(status['outer_steps'][i].get('stop_reason')
                        if i<len(status['outer_steps']) else status.get('stop_reason')))
                for i in range(128)]
            checkpoint()

        state=search_module.search(model,state,J,scales,block_status,
            synchronized_checkpoint,event_sink,check_budget)
        synchronized_checkpoint()
        block.update(phase='original-eight-search-returned',
            original_eight_search_completed=True,
            final_ten_parameter_words=list(state['parameters']),
            stop_reason=block_status['stop_reason'],
            original_eight_status_identity=dict(
                bytes=len(k.encoded(block_status)),
                sha256=hashlib.sha256(k.encoded(block_status)).hexdigest()))
        all_records.extend(block_status.get('outer_steps',[]))
        status['outer_steps']=list(all_records)
        status['current_accepted_ten_parameter_words']=list(state['parameters'])
        if block_status['stop_reason']!='Explicit eight full-ten direction budget completed':
            status['stop_reason']=block_status['stop_reason']
            checkpoint()
            break
        if block_index+1<maximum:
            block['eligible_for_next_block_after_actual_budget_stop']=True
        checkpoint()
    else:
        status['stop_reason']='Explicit128 directions in16 original eight-direction blocks completed'
    status['complete_planned_block_rows']=[
        dict(index=i,started=i<len(blocks),
            original_stop_reason=blocks[i].get('stop_reason') if i<len(blocks) else status['stop_reason'])
        for i in range(maximum)]
    status['complete_planned_outer_rows']=[
        dict(index=i,started=i<len(status['outer_steps']),
            stop_reason=status['outer_steps'][i].get('stop_reason')
                if i<len(status['outer_steps']) else status['stop_reason'])
        for i in range(128)]
    checkpoint()
    return state


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    for key in ('accepted','prepared','tail-anchor','tail-config','parameter-recipe','out'):
        parser.add_argument('--'+key,type=Path,required=True)
    parser.add_argument('--parameter-recipe-sha256',required=True)
    parser.add_argument('--directions',type=int,default=128)
    parser.add_argument('--backtracks',type=int,default=20)
    parser.add_argument('--decimal-digits',type=int,default=50)
    parser.add_argument('--interval-bits',type=int,default=160)
    parser.add_argument('--interval-depth',type=int,default=14)
    parser.add_argument('--wall-seconds',type=int,default=2400)
    args=parser.parse_args()
    require_actions()
    if Path(__file__).name!=ENTRY:
        raise ValueError('Retain this independent new-family producer identity')
    if (args.directions,args.backtracks,args.decimal_digits,args.interval_bits,args.interval_depth)!=(128,20,50,160,14):
        raise ValueError('Retain128 total directions in original8-by20 blocks, Decimal50 and fresh160/14 final consumer')
    if args.wall_seconds!=2400:
        raise ValueError('The independent experiment wall budget is explicit2400seconds')
    for name in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
        os.environ[name]='1'
    for name,wanted in PARENT_SOURCES.items():
        if sha(HERE/name)!=wanted:
            raise ValueError('Preserve the complete actual157 source ancestry: '+name)
    prior=source_module(OLD_PRODUCER,OLD_PRODUCER_SHA)
    parent=prior.source_module(prior.PARENT,prior.PARENT_SHA)
    baseline,baseline_sources,parent_sources=parent.load_baseline()
    if prior.INPUTS!=INPUTS or any(PARENT_SOURCES.get(n)!=v for n,v in parent_sources.items()):
        raise ValueError('Keep the complete original setup and four inputs')
    family=source_module(FAMILY,FAMILY_SHA)
    k=source_module(MODEL,MODEL_SHA)
    search_module=source_module(SEARCH,SEARCH_SHA)
    if search_module.POLICY!=POLICY:
        raise ValueError('The complete scientific direction policy differs')
    old_model_module=prior.source_module(prior.MODEL,prior.MODEL_SHA)
    if sha(HERE/BASELINE_PRODUCER)!=BASELINE_PRODUCER_SHA:
        raise ValueError('Preserve the exact original178 producer as an identity-only source baseline')
    sources={**PARENT_SOURCES,FAMILY:FAMILY_SHA,MODEL:MODEL_SHA,SEARCH:SEARCH_SHA,
        BASELINE_PRODUCER:BASELINE_PRODUCER_SHA,ENTRY:sha(__file__)}
    if len(PARENT_SOURCES)!=41 or len(sources)!=46:
        raise ValueError('The explicitly bound41 original-nine plus5 current sources differs')
    for key,wanted in INPUTS.items():
        if sha(getattr(args,key))!=wanted:
            raise ValueError('The original complete mathematical input differs: '+key)
    recipe_raw,parameters_recipe=recipe(args.parameter_recipe,args.parameter_recipe_sha256)
    if args.out.exists() and any(args.out.iterdir()):
        raise ValueError('Use a fresh experiment-owned output directory')
    args.out.mkdir(parents=True,exist_ok=True)
    (args.out/'parameter-recipe.json').write_bytes(recipe_raw)
    started=time.monotonic();deadline=started+args.wall_seconds
    status=dict(schema=SCHEMA,phase='starting',source_sha256=sources[ENTRY],
        consumed_source_sha256=sources,input_sha256=INPUTS,
        actual_origin=parameters_recipe['origin'],
        parameter_recipe=dict(bytes=len(recipe_raw),sha256=args.parameter_recipe_sha256),
        policy=POLICY,continuation_contract=CONTINUATION_CONTRACT,
        run_id=os.environ.get('GITHUB_RUN_ID'),source_commit=os.environ.get('GITHUB_SHA'),
        initial_ten_parameter_words=parameters_recipe['initial_ten_parameter_words'],
        fixed_scale_original_actual157_words=parameters_recipe['fixed_scale_original_actual157_words'],
        fixed_scale_origin=parameters_recipe['fixed_scale_origin'],
        original_parent_radius=parameters_recipe['original_parent_radius_provenance'],
        parent_radius_not_used_as_new_shape_scale=True,decimal_digits=50,rounding='ROUND_HALF_EVEN',
        fixed_shape_evidence=FIXED_SHAPE,selected_catalogue_index=3,
        catalogue_reselection_performed=False,all_ten_parameters_can_change=True,
        outer_steps=[],unvisited_outer_indices=list(range(128)),accepted_point_count=0,
        continuation_blocks=[],unvisited_block_indices=list(range(16)),
        no_previous_parent_state_J_merit_or_FD_used_as_current=True,
        zero_extension_not_evaluated_in_nonzero_ten_resume=True,
        old_nine_parameters_relabelled_as_new=False,new_shape_parameter_index=9,
        input_tables_not_reformed_in_high_precision=True,
        source_bound_original112_terminal_and699_chain_retained=True,
        full_ten_QR_or_Cauchy_is_a_proposal_not_an_accuracy_or_rank_gate=True,
        high_mode_Schur_elimination_or_current_nonlinear_native_performed=False,
        native_nonlinear_solver_called=False,nonzero_field_completed=False,success=False,
        diagnostic_completed=False,resource_partial=False)
    status_path=args.out/STATUS_NAME
    ledger_path=args.out/'actual-joint-ten-evaluation-events.jsonl'
    ledger=ledger_path.open('wb');ledger_hash=hashlib.sha256();events=0
    trace=None;model=None;old_model=None

    def checkpoint():
        raw=k.encoded(status)+b'\n'
        temporary=status_path.with_suffix('.pending')
        temporary.write_bytes(raw);os.replace(temporary,status_path)

    def event_sink(event):
        nonlocal events
        raw=k.encoded(event)+b'\n'
        ledger.write(raw);ledger.flush();ledger_hash.update(raw);events+=1

    def check_budget():
        if time.monotonic()>=deadline:
            raise ResourceStopped('Explicit independent2400second wall budget reached')

    def stop_signal(signum,frame):
        raise ResourceStopped('Received signal '+str(signum)+'; do not infer a mathematical failure')
    old_signals={sig:signal.signal(sig,stop_signal) for sig in (signal.SIGTERM,signal.SIGINT)}
    checkpoint()
    try:
        prepared,accepted,anchor=[family.original.read(path)
            for path in (args.prepared,args.accepted,args.tail_anchor)]
        original_profile,flow,boundary=family.old.setup(accepted,prepared,anchor,4096,1)
        np=family.np
        true_J=np.asarray(anchor['heightJetJacobian']).reshape(3*flow.M+2,flow.M)[:flow.M]
        target=np.asarray(accepted['core']['coefficients'])[:3]
        trace=baseline.EvaluationTrace(args.out/'actual-projection-calls')
        original_class=family.old.observed_model_class(trace,baseline)
        original_model=original_class(original_profile,prepared['mesh'],true_J,target,boundary.eh,boundary.cut_scale)
        if not original_model.exactly_diagonal or np.any(target==0):
            raise ValueError('Retain original diagonal-unit choice, all112 entries and nonzero three targets')
        status.update(original_mesh_nodes=len(original_model.x),field_and_tail_modes=flow.M,
            original_nine_profile=original_profile.description(),
            source_bound_family_views=family.SOURCE_DERIVATIONS,
            source_bound_decimal_views=k.SOURCE_DERIVATIONS)

        with k.precision_context():
            p10=[k.dec(word) for word in parameters_recipe['initial_ten_parameter_words']]
            if any(not x.is_finite() for x in p10):
                raise ValueError('Every explicit initial ten word must be finite')
            p9=p10[:9]
            old_model=old_model_module.LiteralCircleModel(original_model,event_sink)
            status['original_nine_literal_binding']=old_model.binding
            if k.encoded(old_model.binding)!=k.encoded(parameters_recipe['expected_original_literal_binding']):
                raise ValueError('The actual reconstructed original literal coefficient identity differs')
            status['old_nine_model_role']='Rebuild original literal tables only; no zero-xi state is adopted or required at this nonzero ten point'
            if family.CATALOGUE[3]!=(1,4):
                raise ValueError('The frozen source catalogue index does not identify support1/power4')
            profile=family.TenControlProfile(original_profile,3)
            status['selected_shape']=profile.description()
            status['fixed_shape_definition']=profile.extra.definition()
            status['shape_frozen_for_all_ten_forward_FD_trials_and_final_consumers']=True
            status['phase']='independent-fixed-power-ten-model';checkpoint()
            extended_class=family.observed_model_class(trace,baseline)
            extended_original_model=extended_class(profile,prepared['mesh'],true_J,target,boundary.eh,boundary.cut_scale)
            model=k.LiteralTenModel(old_model,extended_original_model,profile.description(),event_sink)
            status['new_ten_literal_binding']=model.binding
            if model.binding.get('canonical_binding_sha256')!=parameters_recipe['expected_ten_literal_binding_sha256']:
                raise ValueError('The actual reconstructed ten-table literal binding differs from the real parent')
            with model.context('fresh-independent-ten-initial'):
                state=model.evaluate(p10)
            status['fresh_initial_parent_word_comparison']=dict(
                parent_unit_equations=parameters_recipe.get('parent_saved_unit_equations'),
                parent_merit=parameters_recipe.get('parent_saved_merit'),
                fresh_unit_equations=state['equation'],fresh_merit=k.merit(state),
                same_equation_words=[str(x) for x in state['equation']]==parameters_recipe.get('parent_saved_unit_equations'),
                same_merit_word=str(k.merit(state))==parameters_recipe.get('parent_saved_merit'),
                comparison_is_readback_not_an_acceptance_gate=True)
            status['phase']='initial-complete-ten-forward-and-three-step-FD';checkpoint()
            check_budget()
            status['initial']=model.description(state)
            initial_J=status['initial']['complete_three_by_ten_forward_response']
            scales=search_module.fixed_physical_scales(parameters_recipe['fixed_scale_original_actual157_words'])
            status['fixed_physical_scales']=scales
            status['fixed_scales_computed_once_from_actual157_words']=True
            status['initial_complete_ten_response_not_replaced_by_old_nine_response']=True
            fp0=np.asarray([float(x) for x in p10],float)
            with trace.context('initial-binary64-ten-projection'):
                projected_initial=extended_original_model.evaluate(fp0)
                status['initial_binary64_projection']=extended_original_model.description(projected_initial)
            status['initial_projection_contract']=dict(persistent_parameters=p10,
                binary64_parameters=fp0.tolist(),binary64_hex=[float(x).hex() for x in fp0],
                projection_is_not_adopted_by_Decimal_owner=True)
            before=k.merit(state)
            status['actual_initial_merit']=before
            status['original_Armijo_coefficient_exact_binary64_lift']=k.ARM
            status['phase']='complete-ten-joint-Newton-sixteen-original8-by20-blocks';checkpoint()
            state=continue_original_blocks(search_module,model,state,initial_J,scales,status,
                checkpoint,event_sink,check_budget,k)
            status['phase']='final-full-ten-forward-FD-and-original-projection-final-consumers';checkpoint()
            check_budget()
            status['final']=model.description(state)
            p10=list(state['parameters'])
            fp=np.asarray([float(x) for x in p10],float)
            with trace.context('final-binary64-ten-projection'):
                projected=extended_original_model.evaluate(fp)
                status['final_binary64_projection']=extended_original_model.description(projected)
            status['final_projection_contract']=dict(persistent_parameters=p10,
                binary64_parameters=fp.tolist(),binary64_hex=[float(x).hex() for x in fp],
                persistent_minus_binary64_exact_lift=[x-k.dec(float(y)) for x,y in zip(p10,fp)],
                projected_consumers_do_not_certify_the_distinct_persistent_point=True,
                projection_is_not_adopted_by_Decimal_owner=True)
            specification=family.scalar_spec(profile,prepared['complete_scalar_profile']['complete_original_port'],
                fp,INPUTS['accepted'])
            status['fresh_extended_scalar_family']=specification
            status['complete_scalar_domain_at_binary64_projection']=family.scalar_domain(
                profile,specification,args.out,args.interval_bits,args.interval_depth)
            status['original_complete_circle_check_at_binary64_projection']=family.complete_reference_check(
                extended_original_model,projected,profile,flow,boundary,args.out,prepared,INPUTS['prepared'])
            status.update(phase='diagnostic-completed',diagnostic_completed=True,
                final_ten_parameter_words=p10,final_selected_shape_coefficient=p10[9],
                final_original_three_merit=k.merit(state),
                high_precision_original_unit_stopping_tolerance_met=k.maxabs(state['equation'])<=k.TOL,
                high_precision_full112_linear_right_tolerance_met=k.maxabs(state['full_right'])<=k.TOL,
                binary64_projection_original_unit_stopping_tolerance_met=bool(np.max(abs(projected['equation']))<=1e-8),
                binary64_projection_full112_linear_right_tolerance_met=bool(np.max(abs(projected['full_right']))<=1e-8),
                initial_final_complete_ten_axis_three_step_Decimal_and_binary64_FD_attempted=True,
                final_continuous_scalar_and453_circle_consumers_at_explicit_projection_only=True,
                high_precision_complete_interval_domain_or_exact_derivative_accuracy_certified=False,
                native_nonlinear_solver_called=False,nonzero_field_completed=False,success=False)
            checkpoint()
        return 0
    except ResourceStopped as error:
        status.update(phase='resource-partial',resource_partial=True,exception=repr(error),
            traceback=traceback.format_exc(),scientific_failure_not_inferred=True)
        return 75
    except Exception as error:
        status.update(phase='exception',exception=repr(error),traceback=traceback.format_exc(),
            diagnostic_completed=False,scientific_completion_not_claimed=True)
        raise
    finally:
        if trace is not None:
            trace.close();status['original_projection_call_trace']=trace.report()
        if model is not None:
            status['independent_ten_model_call_counts']=dict(model.counts)
        if old_model is not None:
            status['fresh_original_nine_model_call_counts']=dict(old_model.counts)
        ledger.close()
        status['complete_original_event_ledger']=dict(file=ledger_path.name,
            bytes=ledger_path.stat().st_size,sha256=ledger_hash.hexdigest(),events=events,
            raw_not_retained_after_compact_readback=True)
        status['elapsed_wall_seconds']=format(time.monotonic()-started,'.9f')
        checkpoint()
        for sig,handler in old_signals.items():
            signal.signal(sig,handler)
        print(k.encoded(dict(event='request183-producer-completed-or-partial',
            phase=status['phase'],diagnostic_completed=status['diagnostic_completed'],
            resource_partial=status['resource_partial'],status_file=STATUS_NAME,
            status_bytes=status_path.stat().st_size,status_sha256=sha(status_path),
            accepted_point_count=status['accepted_point_count'],selected_catalogue_index=status['selected_catalogue_index'],
            attempted_outer_directions=len(status.get('outer_steps',[])),
            scientific_nonzero_field_acceptance_claimed=False)).decode('ascii'),flush=True)


if __name__=='__main__':
    raise SystemExit(main())
