"""NP uses the existing small public worker with complete original native inputs.

Only task identities, task output validation/reporting, and necessary readonly
input materialization change.  Original capacity, periodic README checks,
failed-prefix preservation, and pull/rebase/push loops remain unchanged.
Private Python snapshots have input_ prefixes, so no stdlib is shadowed.
"""
from __future__ import annotations
import argparse, ast, hashlib, importlib.util
from pathlib import Path

TOPIC = "topics/visible-flex-exact-nearby"
ADAPTER = TOPIC+"/scripts/fourfold_codazzi_support_localized_nu_public_worker.py"
ADAPTER_SHA = "65daf6f2fa7a5e3a09bb331e0087d4ffe563e5740fb972e46e61fb7d14187fa0"
REPLACEMENTS = {
    "R147_support_localized_selected_negative_nu_inputs_v1":"R147_true_selected_strict_nu_particular_inputs_v1",
    "support_localized_selected_negative_nu":"true_selected_strict_nu_particular",
    "actual-support-localized-nu.json":"actual-strict-nu-particular.json",
    "actual-support-localized-nu-":"actual-strict-nu-particular-",
    "R147_support_localized_selected_negative_nu_execution_v1":"R147_true_selected_strict_nu_particular_execution_v1",
    "consumed_R147_support_localized_selected_negative_nu_target_v1":"consumed_R147_true_selected_strict_nu_particular_v1",
    "one complete actual four-record support-localized negative nu manifest":"one complete strict true-nu particular manifest",
    "visible-exact: reserve support-localized negative nu ":"visible-exact: reserve strict true nu ",
    "visible-exact: preserve support-localized negative nu ":"visible-exact: preserve strict true nu ",
}

MATERIALIZE = '''
def materialize(head):
    for spec in specs:
        raw = checked_bytes(spec,head)
        if spec["path"].endswith(".py"):
            ast.parse(raw.decode(),filename=spec["path"])
        destination = source_dir/("input_"+spec["role"]+Path(spec["path"]).suffix)
        atomic(destination,raw)
        snapshots[spec["role"]] = destination
    for item in manifest["historical_inputs"]:
        role = item["role"]
        if role not in snapshots:
            fetch_commit(item["commit"])
            raw = checked_bytes(item,item["commit"],small=False)
            destination = source_dir/"original-native"/topic_path(item["path"])
            atomic(destination,raw)
            snapshots[role] = destination
    require(len(snapshots) == len(specs)+51,
            "every complete current object and all51 original native or definition files")
    require(sha(Path(__file__).read_bytes()) == by_role["worker"]["sha256"],
            "actual running worker is the entire pinned source")
    require(sha(git("show",head+":"+str(mpath.relative_to(root)),binary=True).stdout)
            == args.manifest_sha,"manifest unchanged after pull")
    state["current_input_receipts"] = specs
    state["historical_restoration"] = {
        "original_native_files_restored":47,"complete_saved_RW_definition_files":4,
        "complete_original_input_definitions_sha256":sha(encode(manifest["historical_inputs"])),
        "original_centre_parts":5,"original_native_row_parts":40,
        "original_direction_shards_reconstructed":0,
        "old_enclosure_integral_QR_or_direction_targets_executed":0,
        "all_original_bytes_retained_in_private_input_tree":True}
'''

VALIDATOR = '''
def validate_output(raw):
    require(0 < len(raw) <= op["maximum_scientific_bytes"],"whole small complete scientific result")
    doc = parse(raw)
    identity = doc["identity"]
    require(identity["kind"] == manifest["scientific_kind"]
            and identity["scalar_stage"] == manifest["stage"]
            and identity["source_sha256"] == by_role["science"]["sha256"]
            and identity["manifest_sha256"] == args.manifest_sha
            and identity["run_id"] == run and identity["run_attempt"] == attempt
            and identity["arithmetic_bits"] == manifest["parameters"]["arithmetic_bits"],
            "exact new true parameter-particular identity")
    count = doc["saved_record_count"]
    require(type(count) is int and 0 <= count <= 2
            and doc["completed_targets"] == manifest["target_order"][:count]
            and set(doc["new_records"]) == set(doc["completed_targets"])
            and doc["parameters"] == manifest["parameters"]
            and sorted(doc) == manifest["allowed_scientific_fields"]
            and all(doc[key] == 0 for key in ("old_scientific_target_calls",
                "new_arrays_published","new_artifacts","new_Releases")),
            "complete actual prefix, original scopes and schema")
    if doc["complete"]:
        result = doc["result"]
        require(count == 2 and manifest["complete_record_counts"] == [2]
                and doc["proved"] is True and doc["failure"] is None
                and doc["actual_returncode"] == 0
                and doc["candidate_record"] is doc["current_target"] is None
                and doc["stage"] == "complete_"+manifest["stage"]+"_scalar_branch"
                and result["kind"] == manifest["scientific_kind"]
                and result["complete_new_record_count"] == 2
                and result["complete_new_record_order"] == doc["completed_targets"]
                and result["whole_signed_waist_output_count"] == 194,
                "all two mathematical targets and194 signed output balls")
        for key in ("complete_selected_strict_nu_particular_certified",
                    "unknown_true_solution_remains_full_Fourier",
                    "both_physical_density_means_retained",
                    "all_trial_jumps_proved_zero_from_shared_exact_endpoint_data",
                    "direct_positive_and_root_state_exactly_zero"):
            require(result[key] is True,"complete mathematical qualification: "+key)
        for key in ("old_direction_array_or_QR_reconstructed","positive_inverse_used",
                    "complete_incoming_inverse_proved","full_parameter_boundary_column_proved",
                    "true_nu_or_phase_Schur_proved","topic_completion_proved"):
            require(result[key] is False,"retained original global obligation: "+key)
        outputs = doc["new_records"][manifest["target_order"][1]]["complete_signed_output_balls"]
        require(len(outputs["declared_incoming_cosine96"]) == 96
                and len(outputs["original_physical_primitive96"]) == 96
                and set(outputs["independent_density_means"]) == {"plus","minus"},
                "every declared signed row and both physical density means")
        second = doc["new_records"][manifest["target_order"][1]]
        trial = second["complete_signed_trial_pairings"]
        require(second["complete_signed_trial_pairing_count"] == 192
                and second["trial_pairings_exclude_PDE_and_RW_error_fees"] is True
                and set(trial) == {"declared_incoming_cosine96","original_physical_primitive96"}
                and all(set(group) == {"row_%03d"%j for j in range(1,97)} for group in trial.values()),
                "all192 same-run raw signed observations retained for a future joint error consumer")
    return doc
'''

REPORT = '''
def final_files():
    body = encode(state)
    require(len(body) <= op["maximum_execution_bytes"],"complete execution receipt budget")
    report = ("# Actual strict true-parameter particular and signed waist column\\n\\nRun "+run+"/"+attempt
        +"; complete: "+str(state["complete"])+".\\n\\n"
        "The new child selects a finite forced trial at the original continuous M32 centre, "
        "certifies its complete residual and transfers it to the same implicit selected member "
        "using whole saved D coefficient/source bounds and the original strict SP receiver. "
        "Both density means and all194 true signed output observations are retained, alongside "
        "the192 uninflated signed trial pairings from the same evaluations. "
        "No old direction reconstruction, QR, source integral, receiver norm or positive inverse runs. "
        "Full incoming matching, explicit parameter boundary rows, phase and the final nonlinear "
        "family remain separate obligations.\\n").encode()
    return {**staged,output_dir+"/execution.json":body,output_dir+"/report.md":report}
'''


def require(ok,message):
    if not ok:
        raise ValueError(message)


def build_adapter(root):
    raw = (root/ADAPTER).read_bytes()
    require(hashlib.sha256(raw).hexdigest() == ADAPTER_SHA,"the unchanged complete original small adapter")
    spec = importlib.util.spec_from_file_location("_NP_original_public_adapter",root/ADAPTER)
    source = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(source)
    tree = source.build_adapter(root)
    strings = dict.fromkeys(REPLACEMENTS,0)
    functions = {"materialize":MATERIALIZE,"validate_output":VALIDATOR,"final_files":REPORT}
    counts = dict.fromkeys(functions,0)
    comparisons = {"complete_record_counts":0,"historical_inputs":0}

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
            if (isinstance(node.left,ast.Subscript) and isinstance(node.left.value,ast.Name)
                    and node.left.value.id == "manifest" and isinstance(node.left.slice,ast.Constant)
                    and node.left.slice.value in comparisons):
                name = node.left.slice.value
                expected = ast.parse('manifest["'+name+'"] == '+('[4]' if name == "complete_record_counts" else '[]'),mode="eval").body
                require(ast.dump(node) == ast.dump(expected),"the exact inherited task-input comparison")
                comparisons[name] += 1
                replacement = ('manifest["complete_record_counts"] == [2]' if name == "complete_record_counts"
                               else 'len(manifest["historical_inputs"]) == 51')
                return ast.copy_location(ast.parse(replacement,mode="eval").body,node)
            return self.generic_visit(node)

    tree = Adapter().visit(tree)
    require(all(x == 1 for group in (strings,counts,comparisons) for x in group.values()),
            "only the declared task names, input handling and result handlers change")
    tree.body[0].value = ast.Constant(__doc__)
    ast.fix_missing_locations(tree)
    return tree


def main():
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument("--repo",required=True)
    args,_ = parser.parse_known_args()
    root = Path(args.repo).resolve()
    namespace = {"__name__":"_NP_reused_public_worker","__file__":__file__}
    exec(compile(build_adapter(root),"<NP complete existing public worker>","exec"),namespace)
    namespace["main"]()


if __name__ == "__main__":
    main()
