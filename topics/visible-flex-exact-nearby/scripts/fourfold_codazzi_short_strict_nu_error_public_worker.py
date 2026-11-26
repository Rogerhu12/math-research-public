"""SB uses the original public small-scalar engine and forty readonly row inputs.

Capacity, README checks, preservation and pull/rebase/push remain unchanged.
No old target is retried; only the new short radial target is consumed once.
"""
from __future__ import annotations
import argparse, ast, hashlib
from pathlib import Path

TEMPLATE = "topics/visible-flex-exact-nearby/scripts/fourfold_codazzi_negative_nu_waist_public_worker.py"
TEMPLATE_SHA = "17cb1a5c838cba72571880d871df533aad18577b08e28a8b92d9f681f78aff39"
REPLACEMENTS = {
    "R147_selected_negative_nu_ordinary_to_waist_inputs_v1":"R147_complete_short_strict_nu_error_inputs_v1",
    "selected_negative_nu_ordinary":"complete_short_strict_nu_error",
    "actual-negative-nu-waist.json":"actual-short-strict-nu-error.json",
    "actual-negative-nu-waist-":"actual-short-strict-nu-error-",
    "R147_complete_selected_negative_nu_ordinary_to_waist_execution_v1":"R147_complete_short_strict_nu_error_execution_v1",
    "consumed_R147_selected_negative_nu_ordinary_to_waist_target_v1":"consumed_R147_complete_short_strict_nu_error_v1",
    "one complete actual four-record same-window negative nu manifest":"one complete eleven-record short strict nu error manifest",
    "visible-exact: reserve negative nu waist ":"visible-exact: reserve short strict nu error ",
    "visible-exact: preserve negative nu waist ":"visible-exact: preserve short strict nu error ",
}

MATERIALIZE = '''
def materialize(head):
    for spec in specs:
        raw = checked_bytes(spec,head)
        if spec["path"].endswith(".py"):
            ast.parse(raw.decode(),filename=spec["path"])
        destination = source_dir/("input_"+spec["role"]+Path(spec["path"]).suffix)
        atomic(destination,raw);snapshots[spec["role"]] = destination
    for item in manifest["historical_inputs"]:
        role = item["role"]
        if role not in snapshots:
            fetch_commit(item["commit"]);raw = checked_bytes(item,item["commit"],small=False)
            destination = source_dir/"original-native"/topic_path(item["path"])
            atomic(destination,raw);snapshots[role] = destination
    require(len(snapshots) == len(specs)+40,"all whole current inputs and all40 original body parts")
    require(sha(Path(__file__).read_bytes()) == by_role["worker"]["sha256"],"entire actual pinned worker")
    require(sha(git("show",head+":"+str(mpath.relative_to(root)),binary=True).stdout) == args.manifest_sha,
            "whole manifest unchanged after pull")
    state["current_input_receipts"] = specs
    state["historical_restoration"] = {"original_native_files_restored":40,
        "all_original_body_rows":7721,"original_definition_descriptors_sha256":sha(encode(manifest["historical_inputs"])),
        "old_intrinsic_residual_trial_pairing_matrix_targets_executed":0,
        "all_original_bytes_retained_in_private_input_tree":True}
'''

VALIDATOR = '''
def validate_output(raw):
    require(0 < len(raw) <= op["maximum_scientific_bytes"],"whole actual short-interval conclusion")
    doc = parse(raw);identity = doc["identity"]
    require(identity["kind"] == manifest["scientific_kind"] and identity["scalar_stage"] == manifest["stage"]
        and identity["source_sha256"] == by_role["science"]["sha256"]
        and identity["manifest_sha256"] == args.manifest_sha and identity["run_id"] == run
        and identity["run_attempt"] == attempt
        and identity["arithmetic_bits"] == manifest["parameters"]["arithmetic_bits"],"same entire new scientific object")
    count = doc["saved_record_count"]
    require(type(count) is int and 0 <= count <= 11
        and doc["completed_targets"] == manifest["target_order"][:count]
        and set(doc["new_records"]) == set(doc["completed_targets"])
        and doc["parameters"] == manifest["parameters"] and sorted(doc) == manifest["allowed_scientific_fields"]
        and all(doc[key] == 0 for key in ("old_scientific_target_calls","new_arrays_published","new_artifacts","new_Releases")),
        "entire genuine saved prefix, exact scope, and no old target replay")
    for record in doc["new_records"].values():
        require(set(record) == {"ball","bound"} and isinstance(record["ball"],str) and record["bound"] == "upper",
                "whole outward scalar enclosure")
    if doc["complete"]:
        result = doc["result"]
        require(count == 11 and doc["proved"] is True and doc["failure"] is None and doc["actual_returncode"] == 0
            and doc["candidate_record"] is doc["current_target"] is None
            and doc["stage"] == "complete_"+manifest["stage"]+"_scalar_branch"
            and result["kind"] == manifest["scientific_kind"] and result["complete_new_record_count"] == 11
            and result["complete_new_record_order"] == doc["completed_targets"]
            and doc["whole_completed_inputs"]["all7721_original_rows_admitted"] is True
            and doc["short_radial_receipts"]["exact_short_interval"] == ["0","9/50"],
            "all eleven mathematical records and every original body row")
        for name in ("same_original_selected_full_frequency_particular","whole_original_SP_nonradial_matrix_retained",
            "all_shorter_source_insertion_intervals_retained","both_physical_means_retained",
            "full_NP_error_sources_reused_without_subtracting_uppers","true_short_waist_error_uses_min_with_complete_old_D",
            "uniform_interior_primitive_plus_mean_error_proved","whole_formal_readback_for_each_dependency",
            "uniform_interior_and_radial_L2_error_proved","degree160_factor_applies_only_to_original_centre_residual",
            "all_selected_operator_and_parameter_difference_terms_keep_full_L2_units"):
            require(result[name] is True,"complete original-scope qualification: "+name)
        for name in ("old_trial_residual_pairings_or_nonradial_matrix_recomputed","new_trial_chosen",
            "nonlocal_phase_or_height_signed_column_proved","full_incoming_inverse_or_Schur_proved","topic_completion_proved"):
            require(result[name] is False,"retained uncompleted global obligation: "+name)
    return doc
'''

REPORT = '''
def final_files():
    body = encode(state);require(len(body) <= op["maximum_execution_bytes"],"whole execution budget")
    report = ("# Actual short strict parameter error receiver\\n\\nRun "+run+"/"+attempt
        +"; complete: "+str(state["complete"])+".\\n\\n"
        "This child consumes the whole completed original NP and SP outcomes and restores "
        "all forty complete original body parts. It integrates only the previously missing "
        "radial cost on [0,9/50], retaining the whole completed SP nonradial matrix, all source "
        "insertion times and both means. Eleven new complete scalar records provide the "
        "true waist-density error, uniform interior primitive-plus-mean error, and "
        "uniform and radial raw L2 errors. The degree160 factor acts only on the "
        "original centre residual; every selected difference keeps its full L2 units. "
        "No old intrinsic, trial, residual, signed pairing or matrix target runs. "
        "Nonlocal phase/height signed columns and the full incoming Schur remain.\\n").encode()
    return {**staged,output_dir+"/execution.json":body,output_dir+"/report.md":report}
'''


def require(ok,message):
    if not ok:raise ValueError(message)


def build_adapter(root):
    raw = (root/TEMPLATE).read_bytes()
    require(hashlib.sha256(raw).hexdigest() == TEMPLATE_SHA,"unchanged entire original scalar engine")
    tree = ast.parse(raw.decode(),filename=TEMPLATE)
    strings = dict.fromkeys(REPLACEMENTS,0)
    functions = {"materialize":MATERIALIZE,"validate_output":VALIDATOR,"final_files":REPORT}
    counts = dict.fromkeys(functions,0);comparisons = {"complete_record_counts":0,"historical_inputs":0}
    class Adapter(ast.NodeTransformer):
        def visit_Constant(self,node):
            if isinstance(node.value,str) and node.value in REPLACEMENTS:
                strings[node.value] += 1
                return ast.copy_location(ast.Constant(REPLACEMENTS[node.value]),node)
            return node
        def visit_FunctionDef(self,node):
            if node.name in functions:
                counts[node.name] += 1
                return ast.copy_location(ast.parse(functions[node.name]).body[0],node)
            return self.generic_visit(node)
        def visit_Compare(self,node):
            for name,new in (("complete_record_counts",'manifest["complete_record_counts"] == [11]'),
                             ("historical_inputs",'len(manifest["historical_inputs"]) == 40')):
                old = 'manifest["'+name+'"] == '+('[4]' if name == "complete_record_counts" else '[]')
                if ast.dump(node) == ast.dump(ast.parse(old,mode="eval").body):
                    comparisons[name] += 1
                    return ast.copy_location(ast.parse(new,mode="eval").body,node)
            return self.generic_visit(node)
    tree = Adapter().visit(tree)
    require(all(value == 1 for group in (strings,counts,comparisons) for value in group.values()),
        "only declared identities, whole result handlers and necessary readonly inputs change")
    tree.body[0].value = ast.Constant(__doc__);ast.fix_missing_locations(tree);return tree


def main():
    parser = argparse.ArgumentParser(add_help=False);parser.add_argument("--repo",required=True)
    args,_ = parser.parse_known_args();root = Path(args.repo).resolve()
    namespace = {"__name__":"_SB_existing_public_engine","__file__":__file__}
    exec(compile(build_adapter(root),"<SB existing public engine>","exec"),namespace);namespace["main"]()


if __name__ == "__main__":
    main()
