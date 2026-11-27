"""WMR inherits the completed RHI public engine for one new height kernel.

Only immutable names, complete3-target validation and the report differ.
The RHI engine preserves identical input reuse, whole failed output,
README pulls, capacity checks and immediate non-fast-forward rebase.
"""
from __future__ import annotations
import argparse,ast,hashlib,importlib.util
from pathlib import Path

TOPIC="topics/visible-flex-exact-nearby"
PARENT=TOPIC+"/scripts/fourfold_codazzi_relative_nu_carrier_public_worker.py"
PARENT_SHA="20fc6576ae6be64896d089b4070ab03be328e6fc51db571413ed6cd36da18260"
REPLACEMENTS={
    "R147_complete_relative_strict_nu_carriers_inputs_v1":"R147_complete_physical_mean_height_nu_kernel_inputs_v1",
    "complete_relative_strict_nu_carriers":"complete_physical_mean_height_nu_kernel",
    "actual-relative-nu-carriers.json":"actual-world-mean-height.json",
    "actual-relative-nu-carriers-":"actual-world-mean-height-",
    "R147_complete_relative_strict_nu_carriers_execution_v1":"R147_complete_physical_mean_height_nu_kernel_execution_v1",
    "consumed_R147_complete_relative_strict_nu_carriers_v1":"consumed_R147_complete_physical_mean_height_nu_kernel_v1",
    "one complete relative parameter carrier manifest":"one complete physical mean-height kernel manifest",
    "visible-exact: reserve relative parameter carriers ":"visible-exact: reserve complete physical mean height ",
    "visible-exact: preserve relative parameter carriers ":"visible-exact: preserve complete physical mean height ",
}
VALIDATOR='''
def validate_output(raw):
    require(0<len(raw)<=op["maximum_scientific_bytes"],"whole actual physical mean-height kernel")
    doc=parse(raw);identity=doc["identity"]
    require(identity["kind"]==manifest["scientific_kind"] and identity["scalar_stage"]==manifest["stage"]
        and identity["source_sha256"]==by_role["science"]["sha256"]
        and identity["manifest_sha256"]==args.manifest_sha and identity["run_id"]==run
        and identity["run_attempt"]==attempt and identity["arithmetic_bits"]==320,
        "whole actual first mean-height identity")
    count=doc["saved_record_count"]
    require(type(count) is int and 0<=count<=3
        and doc["completed_targets"]==manifest["target_order"][:count]
        and set(doc["new_records"])==set(doc["completed_targets"])
        and doc["parameters"]==manifest["parameters"]
        and sorted(doc)==manifest["allowed_scientific_fields"]
        and all(doc[key]==0 for key in
            ("old_scientific_target_calls","new_arrays_published","new_artifacts","new_Releases")),
        "whole genuine saved target prefix, with no old scientific replay")
    for index,name in enumerate(doc["completed_targets"]):
        value=doc["new_records"][name];signed=index in (0,2)
        keys={"complete_count","bound","balls"}|({"exact_dyadic_centres"} if index==0 else set())
        require(set(value)==keys and value["complete_count"]==[3,1,1][index]
            and value["bound"]==("signed_enclosure" if signed else "upper")
            and len(value["balls"])==value["complete_count"]
            and all(isinstance(x,str) for x in value["balls"]),
            "one whole signed kernel vector or complete scalar")
        if index==0:
            require(len(value["exact_dyadic_centres"])==3
                and all(isinstance(x,str) for x in value["exact_dyadic_centres"])
                and value["balls"][1]=="0" and value["exact_dyadic_centres"][1]=="0",
                "all exact chosen centres and the sole proved zero mean")
    restoration=doc["necessary_relative_carrier_receipt"]
    if restoration is not None:
        require(restoration["all18_original_components_retained"] is True
            and restoration["complete_private_readback"] is True
            and restoration["coefficient_construction_and_proposal_only"] is True
            and restoration["new_carrier_chosen"] is False
            and restoration["exact_interval"]==["0","9/50"]
            and 2472<=restoration["complete_ordered_cells"]<3948
            and restoration["complete_original_endpoint"]["shape"]==[2048,18]
            and restoration["complete_original_endpoint"]["bytes"]==294912
            and len(restoration["complete_original_endpoint"]["sha256"])==64
            and len(restoration["whole_ordered_receipt_chain_sha256"])==64
            and all(restoration[key]==0 for key in
                ("old_RHI_residual_steps_evaluated","old_RHI_strip_or_mean_targets_evaluated",
                 "old_NP_targets_evaluated")),"complete necessary original relative carrier")
    details=doc["complete_kernel_details"]
    if details is not None:
        grid=details["complete_grid"]
        require(grid["original_grid"]==2048 and grid["contraction_grid"]==8192
            and grid["complete_interpolant_degree"]==1024
            and grid["maximum_complete_kernel_degree"]==2144
            and grid["exact_real_Nyquist_cosine_retained"] is True
            and grid["complete_polynomial_products_unaliased"] is True
            and details["physical_coordinate_term_gx_included"] is True
            and details["both_means_and_full_h2_preserved"] is True
            and details["exact_zero_kernel_mean_indices"]==[1]
            and details["world_reference_orientation"]==-1
            and details["actual_world_anchor_error_or_outer_ports_not_evaluated"] is True,
            "whole physical coordinate/mean kernel in the original world convention")
        require(len(details["whole_raw_kernel_mean_balls"])==3
            and len(details["exact_dyadic_joint_mean_centres"])==3
            and isinstance(details["complete_raw_mean_joint_radius_upper"],str)
            and isinstance(details["complete_true_mean_joint_radius_upper"],str)
            and set(details["new_kernel_norm_uppers"])=={"X2","Y2","g0_L2","B2","h2_trial_L2"}
            and set(details["whole_reused_error_uppers"])=={"EA","EX","EY_true","EH_true_uniform"}
            and set(details["new_complete_error_assembly"])=={"EJ","EG","EB","EK","UK"},
            "all complete new norm terms and whole error assembly")
    if doc["complete"]:
        result=doc["result"]
        require(count==3 and doc["proved"] is True and doc["failure"] is None
            and doc["actual_returncode"]==0 and doc["current_target"] is doc["candidate_record"] is None
            and doc["stage"]=="complete_"+manifest["stage"]+"_scalar_branch"
            and result["kind"]==manifest["scientific_kind"]
            and result["complete_new_record_count"]==3
            and result["complete_new_record_order"]==manifest["target_order"]
            and restoration is not None and details is not None
            and doc["necessary_original_trial_receipts"]["all_four_complete_arrays_read_back"] is True,
            "all three actually completed new targets and their entire necessary inputs")
        for key in ("same_original_implicit_selected_Q_delta","original_det_minus_one_world_frame_retained",
            "no_long_original_geometry_ODE_repeated","actual_world_frame_position_and_rigid_ports_independent",
            "all_true_PDE_and_coordinate_mean_errors_included","full_physical_coordinate_term_retained",
            "whole_original_RHI_profiles_used","whole_original_NP_waist_and_both_means_used",
            "fixed_world_translation_cancels_by_Pi_dotJ_zero","independent_varying_vertical_translation_retained"):
            require(result[key] is True,"complete mathematical qualification: "+key)
        for key in ("original_RHI_targets_recomputed","original_NP_targets_recomputed",
            "new_trial_selected","full_nu_phase_height_Schur_or_topic_complete",
            "actual_full_world_height_or_Schur_proved"):
            require(result[key] is False,"remaining independent full problem responsibility: "+key)
        require(result["reference_covector_error"]=="108627/1000000000"
            and isinstance(result["independent_actual_anchor_error_coefficient"],str)
            and result["independent_outer_port_formula"]=="Pi[J ez^T(Y_b+K_b Q_b x)+dotJ ez^T F_b]",
            "actual world anchor and full outer ports remain explicit")
    return doc
'''
REPORT='''
def final_files():
    body=encode(state)
    require(len(body)<=op["maximum_execution_bytes"],"whole height-kernel execution")
    report=("# Actual complete physical mean-height parameter kernel\\n\\nRun "+run+"/"+attempt
        +"; complete: "+str(state["complete"])+".\\n\\n"
        "The same whole NP and relative RHI carriers are necessary inputs. Only the new complete "
        "physical mean-height kernel is contracted. The8192-point directed product includes "
        "all2144 possible modes, the original two means and the complete dotJ*x coordinate term. "
        "The old world orientation remains determinant-1. The original-reference body interval "
        "retains its paid covector fee; actual frame/position/rigid ports remain independent. "
        "No original geometry, RHI or NP target is repeated and no full world-height Schur is asserted. "
        "Every genuine failure and its complete saved target prefix are preserved.\\n").encode()
    return {**staged,output_dir+"/execution.json":body,output_dir+"/report.md":report}
'''


def require(ok,message):
    if not ok:
        raise ValueError(message)


def build_adapter(root):
    raw=(root/PARENT).read_bytes()
    require(hashlib.sha256(raw).hexdigest()==PARENT_SHA,"whole unchanged original RHI public engine")
    spec=importlib.util.spec_from_file_location("_WMR_original_RHI_public_engine",root/PARENT)
    parent=importlib.util.module_from_spec(spec);spec.loader.exec_module(parent)
    tree=parent.build_adapter(root)
    strings=dict.fromkeys(REPLACEMENTS,0)
    functions={"validate_output":VALIDATOR,"final_files":REPORT}
    counts=dict.fromkeys(functions,0);comparison={"complete_record_counts":0}
    class Adapter(ast.NodeTransformer):
        def visit_Constant(self,node):
            if isinstance(node.value,str) and node.value in REPLACEMENTS:
                strings[node.value]+=1
                return ast.copy_location(ast.Constant(REPLACEMENTS[node.value]),node)
            return node
        def visit_FunctionDef(self,node):
            if node.name in functions:
                counts[node.name]+=1
                return ast.copy_location(ast.parse(functions[node.name]).body[0],node)
            return self.generic_visit(node)
        def visit_Compare(self,node):
            old=ast.parse('manifest["complete_record_counts"] == [4]',mode="eval").body
            if ast.dump(node)==ast.dump(old):
                comparison["complete_record_counts"]+=1
                return ast.copy_location(
                    ast.parse('manifest["complete_record_counts"] == [3]',mode="eval").body,node)
            return self.generic_visit(node)
    tree=Adapter().visit(tree)
    require(all(value==1 for group in (strings,counts,comparison) for value in group.values()),
        "only exact new names, result validation, report and target count change")
    tree.body[0].value=ast.Constant(__doc__)
    ast.fix_missing_locations(tree)
    return tree


def main():
    parser=argparse.ArgumentParser(add_help=False)
    parser.add_argument("--repo",required=True)
    args,unused=parser.parse_known_args()
    namespace={"__name__":"_WMR_complete_public_worker","__file__":__file__}
    exec(compile(build_adapter(Path(args.repo).resolve()),"<WMR complete public worker>","exec"),namespace)
    namespace["main"]()


if __name__=="__main__":
    main()
