"""RHI uses the existing complete PHI public engine for new relative carriers.

Only names, the complete51 original input materialization, four-target
validation and report change. Capacity checks, README pulls, one-child
reservation, failure publication and non-fast-forward rebase are inherited.
"""
from __future__ import annotations
import argparse,ast,hashlib,importlib.util
from pathlib import Path

TOPIC='topics/visible-flex-exact-nearby'
PARENT=TOPIC+'/scripts/fourfold_codazzi_strict_nu_phase_public_worker.py'
PARENT_SHA='32569d72195ed7640bd47d2d6e1690d299e1636fb93365dea4855e28432f0eef'
REPLACEMENTS={
    'R147_complete_strict_nu_nonlocal_phase_inputs_v1':'R147_complete_relative_strict_nu_carriers_inputs_v1',
    'complete_strict_nu_nonlocal_phase':'complete_relative_strict_nu_carriers',
    'actual-strict-nu-phase.json':'actual-relative-nu-carriers.json',
    'actual-strict-nu-phase-':'actual-relative-nu-carriers-',
    'R147_complete_strict_nu_nonlocal_phase_execution_v1':'R147_complete_relative_strict_nu_carriers_execution_v1',
    'consumed_R147_complete_strict_nu_nonlocal_phase_v1':'consumed_R147_complete_relative_strict_nu_carriers_v1',
    'one complete strict nonlocal phase manifest':'one complete relative parameter carrier manifest',
    'visible-exact: reserve strict nonlocal phase ':'visible-exact: reserve relative parameter carriers ',
    'visible-exact: preserve strict nonlocal phase ':'visible-exact: preserve relative parameter carriers ',
}
MATERIALIZE='''
def materialize(head):
    def remember(item,destination,raw=None):
        role=item["role"]
        if role in snapshots:
            require(snapshots[role]==destination,"same exact original input path on repeated materialization")
            saved=destination.read_bytes()
            require(len(saved)==item["bytes"] and sha(saved)==item["sha256"],
                    "same whole original bytes and SHA on idempotent reuse")
            if raw is not None:require(saved==raw,"no different object silently replaces an input")
        else:
            require(raw is not None,"first restoration has all original bytes")
            atomic(destination,raw);snapshots[role]=destination
    for spec in specs:
        raw=checked_bytes(spec,head)
        if spec["path"].endswith(".py"):ast.parse(raw.decode(),filename=spec["path"])
        destination=source_dir/("input_"+spec["role"]+Path(spec["path"]).suffix)
        remember(spec,destination,raw)
    originals=manifest["historical_inputs"]
    require(len(originals)==51 and len({x["role"] for x in originals})==51,"the entire original NP native closure")
    for item in originals:
        destination=source_dir/"original-native"/topic_path(item["path"])
        if item["role"] in snapshots:remember(item,destination)
        else:
            fetch_commit(item["commit"])
            remember(item,destination,checked_bytes(item,item["commit"],small=False))
    require(len(snapshots)==len(specs)+51,"all complete current and historical objects")
    require(sha(Path(__file__).read_bytes())==by_role["worker"]["sha256"],"whole actual relative worker")
    require(sha(git("show",head+":"+str(mpath.relative_to(root)),binary=True).stdout)==args.manifest_sha,
            "whole relative carrier manifest unchanged after pull")
    state["current_input_receipts"]=specs
    state["historical_restoration"]={"complete_original_files":51,
        "whole_original_descriptors_sha256":sha(encode(originals)),
        "all_original_bytes_retained_in_private_input_tree":True,
        "repeated_materialization_reuses_only_identical_whole_objects":True,
        "old_scientific_targets_evaluated":0}
'''
VALIDATOR='''
def validate_output(raw):
    require(0<len(raw)<=op["maximum_scientific_bytes"],"whole actual relative carrier conclusion")
    doc=parse(raw);identity=doc["identity"]
    require(identity["kind"]==manifest["scientific_kind"] and identity["scalar_stage"]==manifest["stage"]
        and identity["source_sha256"]==by_role["science"]["sha256"]
        and identity["manifest_sha256"]==args.manifest_sha and identity["run_id"]==run
        and identity["run_attempt"]==attempt and identity["arithmetic_bits"]==320,
        "whole same-selected actual relative identity")
    count=doc["saved_record_count"]
    require(type(count) is int and 0<=count<=4 and doc["completed_targets"]==manifest["target_order"][:count]
        and set(doc["new_records"])==set(doc["completed_targets"]) and doc["parameters"]==manifest["parameters"]
        and sorted(doc)==manifest["allowed_scientific_fields"]
        and all(doc[key]==0 for key in ("old_scientific_target_calls","new_arrays_published","new_artifacts","new_Releases")),
        "whole real prefix with no old target replay")
    for i,name in enumerate(doc["completed_targets"]):
        record=doc["new_records"][name];signed=i in (0,2)
        keys={"complete_count","bound","balls"}|({"exact_dyadic_grid_means"} if signed else set())
        require(set(record)==keys and record["complete_count"]==[6,4,6,2][i]
            and record["bound"]==("signed_enclosure" if signed else "upper")
            and len(record["balls"])==record["complete_count"] and all(isinstance(x,str) for x in record["balls"]),
            "one entire signed vector or joint profile-error vector")
        if signed:
            require(len(record["exact_dyadic_grid_means"])==6
                and all(isinstance(x,str) for x in record["exact_dyadic_grid_means"])
                and all(record["balls"][j]=="0" for j in (0,2,4)),
                "all exact chosen grid means distinct from true enclosures and proved three zero means")
    prefix=doc["relative_carrier_prefix"]
    if prefix is not None:
        require(prefix["kind"]=="RHI_complete_relative_ordered_cell_prefix_v1"
            and len(prefix["exact_interval"])==2 and prefix["exact_interval"][1]=="9/50"
            and type(prefix["complete_cells"]) is int and type(prefix["total_cells"]) is int
            and 0<prefix["complete_cells"]<=prefix["total_cells"]<3948
            and prefix["total_cells"]>=2472 and prefix["grid"]==2048
            and prefix["component_order"]==manifest["parameters"]["component_order"]
            and prefix["complete_endpoint_impulse_count"]==prefix["complete_cells"]
            and 0<=prefix["maximum_complete_source_support"]<=288
            and prefix["whole_private_endpoint"]["shape"]==[2048,18]
            and prefix["whole_private_endpoint"]["bytes"]==294912
            and len(prefix["whole_private_endpoint"]["sha256"])==64,
            "one whole genuinely accepted ordered cell prefix and all18 carrier components")
        require(len(prefix["complete_uniform_grid_errors"])==len(prefix["complete_endpoint_impulse_sums"])==4
            and len(prefix["complete_strip_integrals"])==3
            and all(len(x)==4 for x in prefix["complete_strip_integrals"]),
            "every joint grid error, impulse and strip integral")
        records=prefix["complete_uniform_grid_errors"]+prefix["complete_endpoint_impulse_sums"]+[
            x for row in prefix["complete_strip_integrals"] for x in row]
        require(all(set(x)=={"ball","bound"} and isinstance(x["ball"],str) and x["bound"]=="upper" for x in records)
            and prefix["all_original_seams_and_both_means_retained"] is True
            and prefix["all_source_and_residual_monomials_retained"] is True
            and prefix["relative_initial_identity_is_not_world_anchor"] is True
            and prefix["old_scientific_targets_evaluated"]==0,"complete whole prefix scope")
    if doc["complete"]:
        result=doc["result"];carrier=doc["whole_private_carrier_receipt"]
        require(count==4 and doc["proved"] is True and doc["failure"] is None and doc["actual_returncode"]==0
            and doc["current_target"] is doc["candidate_record"] is None
            and doc["stage"]=="complete_"+manifest["stage"]+"_scalar_branch"
            and result["kind"]==manifest["scientific_kind"] and result["complete_new_record_count"]==4
            and result["complete_new_record_order"]==manifest["target_order"]
            and prefix["exact_interval"]==["0","9/50"] and prefix["complete_cells"]==prefix["total_cells"]
            and carrier["complete_readback"] is True and carrier["shape"]==[2048,18]
            and carrier["bytes"]==294912 and carrier["sha256"]==prefix["whole_private_endpoint"]["sha256"]
            and carrier["all18_components_retained"] is True
            and doc["necessary_original_trial_receipts"]["all_four_complete_arrays_read_back"] is True,
            "four actual targets and complete original/final carrier identities")
        for key in ("same_original_selected_Q_delta","whole_four_original_NP_arrays_restored",
            "all_original2472_cells_and_every_true_join_retained","complete_relative18_component_carrier",
            "all2048_grid_labels_and_complete_angular_interpolation_errors",
            "real_orthogonal_residual_propagation_and_all_rounding_impulses",
            "complete_selected_background_direct_metric_and_both_means","full_infinite_PDE_response_error_paid",
            "complete_signed_vectors_and_exact_dyadic_means_distinct",
            "world_anchors_rigid_ports_and_physical_coordinate_term_independent",
            "every_dependent_target_uses_whole_saved_readback","strict_particular_only"):
            require(result[key] is True,"complete relative qualification: "+key)
        for key in ("old_NP_or_phase_scientific_targets_recomputed","original_Z14_materialized",
            "new_NP_trial_selected","full_regular_response_proved","actual_world_anchor_carrier_computed",
            "full_world_height_signed_value_proved","true_phase_height_Schur_or_topic_completion_proved"):
            require(result[key] is False,"independent original full problem port: "+key)
    return doc
'''
REPORT='''
def final_files():
    body=encode(state)
    require(len(body)<=op["maximum_execution_bytes"],"whole relative execution receipt")
    report=("# Actual relative strict parameter carriers\\n\\nRun "+run+"/"+attempt
        +"; complete: "+str(state["complete"])+".\\n\\n"
        "The child restores the same four complete original NP arrays, then computes the first "
        "relative frame/position profiles with all18 components, full radial residuals, numerical "
        "endpoint impulses and complete angular interpolation errors. It retains both means and "
        "the direct metric source and pays the full true PDE response error through RH. "
        "The exact chosen grid means remain distinct from the signed true enclosures. "
        "World anchors, rigid ports and the physical-coordinate term remain independent; "
        "no full world height or Schur is asserted. Every genuine failure prefix is preserved.\\n").encode()
    return {**staged,output_dir+"/execution.json":body,output_dir+"/report.md":report}
'''


def require(ok,message):
    if not ok:raise ValueError(message)


def build_adapter(root):
    raw=(root/PARENT).read_bytes()
    require(hashlib.sha256(raw).hexdigest()==PARENT_SHA,'whole unchanged PHI public engine')
    spec=importlib.util.spec_from_file_location('_RHI_original_public_engine',root/PARENT)
    parent=importlib.util.module_from_spec(spec);spec.loader.exec_module(parent)
    tree=parent.build_adapter(root);strings=dict.fromkeys(REPLACEMENTS,0)
    functions={'materialize':MATERIALIZE,'validate_output':VALIDATOR,'final_files':REPORT}
    counts=dict.fromkeys(functions,0);comparison={'complete_record_counts':0}
    class Adapter(ast.NodeTransformer):
        def visit_Constant(self,node):
            if isinstance(node.value,str) and node.value in REPLACEMENTS:
                strings[node.value]+=1;return ast.copy_location(ast.Constant(REPLACEMENTS[node.value]),node)
            return node
        def visit_FunctionDef(self,node):
            if node.name in functions:
                counts[node.name]+=1;return ast.copy_location(ast.parse(functions[node.name]).body[0],node)
            return self.generic_visit(node)
        def visit_Compare(self,node):
            old=ast.parse('manifest["complete_record_counts"] == [6]',mode='eval').body
            if ast.dump(node)==ast.dump(old):
                comparison['complete_record_counts']+=1
                return ast.copy_location(ast.parse('manifest["complete_record_counts"] == [4]',mode='eval').body,node)
            return self.generic_visit(node)
    tree=Adapter().visit(tree)
    require(all(x==1 for group in (strings,counts,comparison) for x in group.values()),
            'only exact names, complete materialization/count/result handlers change')
    tree.body[0].value=ast.Constant(__doc__);ast.fix_missing_locations(tree);return tree


def main():
    parser=argparse.ArgumentParser(add_help=False);parser.add_argument('--repo',required=True)
    args,unused=parser.parse_known_args()
    namespace={'__name__':'_RHI_complete_public_worker','__file__':__file__}
    exec(compile(build_adapter(Path(args.repo).resolve()),'<RHI complete public worker>','exec'),namespace)
    namespace['main']()


if __name__=='__main__':main()
