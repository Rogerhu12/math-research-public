"""H96 uses the frozen RHI public engine for seven new complete trial rows.

Only names, complete seven-target validation and the report differ.  The
entire51 native input restoration, README pulls, capacity gate, consumed
reservation, one child, actual failure publication and rebase loop remain.
"""
from __future__ import annotations
import argparse, ast, hashlib, importlib.util
from pathlib import Path

TOPIC = "topics/visible-flex-exact-nearby"
PARENT = TOPIC+"/scripts/fourfold_codazzi_relative_nu_carrier_public_worker.py"
PARENT_SHA = "20fc6576ae6be64896d089b4070ab03be328e6fc51db571413ed6cd36da18260"
REPLACEMENTS = {
    "R147_complete_relative_strict_nu_carriers_inputs_v1":"R149_complete_original_finite_trial_height_rows_inputs_v1",
    "complete_relative_strict_nu_carriers":"complete_original_finite_trial_height_rows",
    "actual-relative-nu-carriers.json":"actual-finite-trial-height.json",
    "actual-relative-nu-carriers-":"actual-finite-trial-height-",
    "R147_complete_relative_strict_nu_carriers_execution_v1":"R149_complete_original_finite_trial_height_rows_execution_v1",
    "consumed_R147_complete_relative_strict_nu_carriers_v1":"consumed_R149_complete_original_finite_trial_height_rows_v1",
    "one complete relative parameter carrier manifest":"one complete original96 finite-trial height manifest",
    "visible-exact: reserve relative parameter carriers ":"visible-exact: reserve complete finite-trial height rows ",
    "visible-exact: preserve relative parameter carriers ":"visible-exact: preserve complete finite-trial height rows ",
}
VALIDATOR = '''
def validate_output(raw):
    require(0<len(raw)<=op["maximum_scientific_bytes"],"whole actual complete H96 output")
    doc=parse(raw);identity=doc["identity"]
    require(identity["kind"]==manifest["scientific_kind"] and identity["scalar_stage"]==manifest["stage"]
        and identity["source_sha256"]==by_role["science"]["sha256"]
        and identity["manifest_sha256"]==args.manifest_sha and identity["run_id"]==run
        and identity["run_attempt"]==attempt and identity["arithmetic_bits"]==320,
        "whole actual first same-original-trial height identity")
    count=doc["saved_record_count"]
    require(type(count) is int and 0<=count<=7
        and doc["completed_targets"]==manifest["target_order"][:count]
        and set(doc["new_records"])==set(doc["completed_targets"])
        and doc["parameters"]==manifest["parameters"]
        and sorted(doc)==manifest["allowed_scientific_fields"]
        and all(doc[key]==0 for key in
            ("old_scientific_target_calls","new_arrays_published","new_artifacts","new_Releases")),
        "whole genuine new target prefix, with no old target replay")
    for index,name in enumerate(doc["completed_targets"]):
        value=doc["new_records"][name]
        keys={"complete_count","bound","balls"}|({"exact_dyadic_centres"} if index in (3,5) else set())
        require(set(value)==keys and value["complete_count"]==[96,96,96,96,1,96,1][index]
            and value["bound"]==("signed_enclosure" if index in (0,2,3,5) else "upper")
            and len(value["balls"])==value["complete_count"]
            and all(isinstance(x,str) for x in value["balls"]),
            "one entire original96 row or complete scalar joint radius")
        if index in (3,5):
            require(len(value["exact_dyadic_centres"])==96
                and all(isinstance(x,str) for x in value["exact_dyadic_centres"]),
                "the entire chosen96-vector of exact joint-radius centres")
    prefix=doc["height_integral_prefix"]
    if prefix is not None:
        require(prefix["kind"]=="H96_complete_new_height_integral_prefix_v1"
            and len(prefix["exact_interval"])==2 and prefix["exact_interval"][0]=="0"
            and type(prefix["complete_relative_cells"]) is int
            and 1<=prefix["complete_relative_cells"]<=2847
            and type(prefix["complete_intersections"]) is int
            and prefix["complete_intersections"]>=prefix["complete_relative_cells"]
            and len(prefix["all96_signed_polynomial_integrals"])==96
            and all(isinstance(x,str) for x in prefix["all96_signed_polynomial_integrals"])
            and isinstance(prefix["complete_uniform_adjoint_error_upper"],str)
            and 0<=prefix["maximum_complete_angular_degree"]<=3584
            and type(prefix["maximum_complete_radial_degree"]) is int
            and prefix["old_L1_or_phase_targets_recomputed"] is False,
            "all96 complete signed integrals on one accepted actual radial prefix")
    tc=doc["necessary_original_trial_receipts"]
    if tc is not None:
        require(tc["all_four_original_TC_arrays_verified"] is True
            and len(tc["complete_original_arrays"])==4
            and all(item["shape"]==[7671,193,96] and item["bytes"]==1137026304
                    and len(item["sha256"])==64 for item in tc["complete_original_arrays"])
            and tc["original_TC_floating_proposal_rematerializations"]==1
            and tc["old_completed_scientific_target_calls"]==0
            and tc["unused_direction_array_materializations"]==0
            and tc["new_trial_selected"] is False,
            "all four full original TC arrays and unchanged selected trial")
    restoration=doc["necessary_relative_carrier_receipt"]
    if restoration is not None:
        original=restoration["original_relative_carrier"]
        cache=restoration["complete_polynomial_cache"]
        adapter=restoration["passive_cache_adapter"]
        require(original["all18_original_components_retained"] is True
            and original["complete_private_readback"] is True
            and original["coefficient_construction_and_proposal_only"] is True
            and original["new_carrier_chosen"] is False
            and original["exact_interval"]==["0","9/50"]
            and original["complete_ordered_cells"]==2847
            and original["complete_original_endpoint"]["shape"]==[2048,18]
            and original["complete_original_endpoint"]["bytes"]==294912
            and len(original["complete_original_endpoint"]["sha256"])==64
            and len(original["whole_ordered_receipt_chain_sha256"])==64
            and all(original[key]==0 for key in
                ("old_RHI_residual_steps_evaluated","old_RHI_strip_or_mean_targets_evaluated",
                 "old_NP_targets_evaluated")),"the entire identical old RHI endpoint and all18 chain")
        require(cache["shape"]==[2847,7,2048,12] and cache["bytes"]==3918200832
            and cache["complete_cells"]==2847 and len(cache["sha256"])==64
            and len(cache["whole_reverse_construction_chain_sha256"])==64
            and cache["polynomial_variable"]=="u=(right-r)/(right-left)"
            and cache["component_order"]==["A_rowmajor9","x3"]
            and cache["entire_original18_state_used_and_checked"] is True
            and adapter["passive_polynomial_cache_tap_count"]==1
            and adapter["original_coefficient_or_proposal_arithmetic_changed"] is False
            and adapter["original_full18_endpoint_or_chain_check_changed"] is False
            and restoration["old_RHI_residual_strip_mean_or_phase_targets_called"]==0
            and restoration["new_carrier_selected"] is False
            and restoration["new_arrays_published"]==0,
            "all original2847 complete seven-coefficient polynomials cached privately once")
    if doc["complete"]:
        result=doc["result"]
        require(count==7 and doc["proved"] is True and doc["failure"] is None
            and doc["actual_returncode"]==0 and doc["current_target"] is doc["candidate_record"] is None
            and doc["stage"]=="complete_"+manifest["stage"]+"_scalar_branch"
            and doc["runtime"]=={**manifest["runtime"],"OPENBLAS_CORETYPE":"Haswell"}
            and result["kind"]==manifest["scientific_kind"]
            and result["complete_new_target_count"]==7
            and result["complete_new_target_order"]==manifest["target_order"]
            and restoration is not None and tc is not None and prefix is not None
            and prefix["exact_interval"]==["0","9/50"]
            and prefix["complete_relative_cells"]==result["complete_original_relative_cells"]==2847
            and doc["necessary_original_NP_receipts"]["all_four_complete_arrays_read_back"] is True,
            "all seven actual new targets, full radial cover and every necessary input")
        for key in ("same_original96_TC_trials","same_original_selected_member",
            "full_real_Nyquist_cosine_retained","whole_old_P96_L1_and_phase_vectors_reused",
            "full_physical_coordinate_term_g_f0_paid","one_fixed_height_constant_cancelled_by_Pi_g_zero",
            "independent_Yb_Kb_and_geometric_impulse_ports_retained",
            "raw_phase_chart_and_direct_parameter_terms_retained_separately",
            "all_four_whole_original_TC_arrays_verified","all_four_whole_original_NP_arrays_verified",
            "original_RHI_all18_endpoint_and_entire_chain_verified",
            "entire_original2847_degree6_polynomials_used","all_complete_target_records_saved_and_read_back"):
            require(result[key] is True,"complete H96 mathematical qualification: "+key)
        for key in ("true_PDE_corrected_columns","actual_cap_input_admissibility_or_full_Schur_proved",
            "topic_completion_proved","new_trial_selected","old_scientific_targets_recomputed",
            "unused_phase169_carriers_restored","full_regular_or_Theta_inverse_proved",
            "full_height_phase_Schur_or_topic_completion_proved"):
            require(result[key] is False,"independent unpaid original problem responsibility: "+key)
        require(result["unrestricted_C0_error_primitive_factor"]=="2/5"
            and result["old_completed_scientific_target_calls"]==0,
            "unrestricted angular errors retained without redoing the old phase or L1 target")
    return doc
'''
REPORT = '''
def final_files():
    body=encode(state)
    require(len(body)<=op["maximum_execution_bytes"],"whole finite-trial-height execution")
    report=("# Actual complete height rows on the original96 finite trials\\n\\nRun "+run+"/"+attempt
        +"; complete: "+str(state["complete"])+".\\n\\n"
        "The same four whole TC arrays, four whole NP arrays and original all18 RHI endpoint/chain "
        "are mandatory inputs. A passive cache keeps all2847 original seven-coefficient A9/x3 "
        "polynomials privately. The new8192-point directed contraction includes every96 trial column, "
        "both moving means, the complete physical-coordinate term and unrestricted C0 angular errors. "
        "The existing complete P96 phase/L1 vectors are consumed without phase-carrier or old-target replay. "
        "The seven complete targets are canonical height96, waist-Jacobian L2 uppers96, reference height96, "
        "actual-cap height96 and its joint radius, then height-reduced phase96 and its joint radius. "
        "These are rows on the unchanged finite trial. True PDE correction, full low/high and mean "
        "responses, independent Yb/Kb ports and the remaining Schur problem remain separate. "
        "Every genuine failure and its whole accepted radial/target prefix are preserved. "
        "Private arrays are never published.\\n").encode()
    return {**staged,output_dir+"/execution.json":body,output_dir+"/report.md":report}
'''


def require(ok, message):
    if not ok:
        raise ValueError(message)


def build_adapter(root):
    raw = (root/PARENT).read_bytes()
    require(hashlib.sha256(raw).hexdigest() == PARENT_SHA, "whole unchanged original RHI public engine")
    spec = importlib.util.spec_from_file_location("_H96_original_RHI_public_engine", root/PARENT)
    parent = importlib.util.module_from_spec(spec); spec.loader.exec_module(parent)
    tree = parent.build_adapter(root)
    strings = dict.fromkeys(REPLACEMENTS, 0)
    functions = {"validate_output":VALIDATOR, "final_files":REPORT}
    counts = dict.fromkeys(functions, 0); comparison = {"complete_record_counts":0}
    class Adapter(ast.NodeTransformer):
        def visit_Constant(self, node):
            if isinstance(node.value,str) and node.value in REPLACEMENTS:
                strings[node.value] += 1
                return ast.copy_location(ast.Constant(REPLACEMENTS[node.value]), node)
            return node
        def visit_FunctionDef(self, node):
            if node.name in functions:
                counts[node.name] += 1
                return ast.copy_location(ast.parse(functions[node.name]).body[0], node)
            return self.generic_visit(node)
        def visit_Compare(self, node):
            old = ast.parse('manifest["complete_record_counts"] == [4]', mode="eval").body
            if ast.dump(node) == ast.dump(old):
                comparison["complete_record_counts"] += 1
                return ast.copy_location(ast.parse('manifest["complete_record_counts"] == [7]',
                                                   mode="eval").body, node)
            return self.generic_visit(node)
    tree = Adapter().visit(tree)
    require(all(value == 1 for group in (strings,counts,comparison) for value in group.values()),
            "only exact new names, complete seven-target validator, report and target count change")
    tree.body[0].value = ast.Constant(__doc__)
    ast.fix_missing_locations(tree)
    return tree


def main():
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument("--repo", required=True)
    args, unused = parser.parse_known_args()
    namespace = {"__name__":"_H96_complete_public_worker", "__file__":__file__}
    exec(compile(build_adapter(Path(args.repo).resolve()), "<H96 complete public worker>", "exec"), namespace)
    namespace["main"]()


if __name__ == "__main__":
    main()
