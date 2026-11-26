"""NH uses the complete fixed public engine for twelve new scalar targets.

Only task identities, four small readonly native inputs and output handlers
change. Capacity, periodic README diffs, prefix preservation and successful
push-after-rebase semantics remain inherited from the original engine.
"""
from __future__ import annotations
import argparse, ast, hashlib, importlib.util
from pathlib import Path

TOPIC = "topics/visible-flex-exact-nearby"
PARENT = TOPIC+"/scripts/fourfold_codazzi_strict_nu_particular_public_worker.py"
PARENT_SHA = "0f4d3b932a5632019bf9581c2ae2fa057cc63323d8699e7f45e4f44b9dc93aba"
REPLACEMENTS = {
    "R147_true_selected_strict_nu_particular_inputs_v1":"R147_complete_true_strict_nu_high_forcing_inputs_v1",
    "true_selected_strict_nu_particular":"complete_true_strict_nu_high_forcing",
    "actual-strict-nu-particular.json":"actual-strict-nu-high-forcing.json",
    "actual-strict-nu-particular-":"actual-strict-nu-high-forcing-",
    "R147_true_selected_strict_nu_particular_execution_v1":"R147_complete_true_strict_nu_high_forcing_execution_v1",
    "consumed_R147_true_selected_strict_nu_particular_v1":"consumed_R147_complete_true_strict_nu_high_forcing_v1",
    "one complete strict true-nu particular manifest":"one complete true-nu high forcing scalar manifest",
    "visible-exact: reserve strict true nu ":"visible-exact: reserve strict nu high forcing ",
    "visible-exact: preserve strict true nu ":"visible-exact: preserve strict nu high forcing ",
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
    for spec in manifest["historical_inputs"]:
        role = spec["role"]
        if role not in snapshots:
            fetch_commit(spec["commit"])
            raw = checked_bytes(spec,spec["commit"],small=False)
            destination = source_dir/("input_"+role+".json.gz")
            atomic(destination,raw)
            snapshots[role] = destination
    require(len(snapshots) == len(specs)+4,"whole current results and all four original saved native definitions")
    require(sha(Path(__file__).read_bytes()) == by_role["worker"]["sha256"],"entire pinned actual worker")
    require(sha(git("show",head+":"+str(mpath.relative_to(root)),binary=True).stdout)
            == args.manifest_sha,"whole manifest unchanged after pull")
    state["current_input_receipts"] = specs
    state["historical_restoration"] = {"original_small_definition_files_restored":4,
        "full_definition_list_sha256":sha(encode(manifest["historical_inputs"])),
        "NP_trial_or_PDE_carriers_restored":0,"original_norms_rows_or_pairings_recomputed":0}
'''

VALIDATOR = '''
def validate_output(raw):
    require(0 < len(raw) <= op["maximum_scientific_bytes"],"whole complete scalar result")
    doc = parse(raw)
    identity = doc["identity"]
    require(identity["kind"] == manifest["scientific_kind"] and identity["scalar_stage"] == manifest["stage"]
            and identity["source_sha256"] == by_role["science"]["sha256"]
            and identity["manifest_sha256"] == args.manifest_sha
            and identity["run_id"] == run and identity["run_attempt"] == attempt
            and identity["arithmetic_bits"] == manifest["parameters"]["arithmetic_bits"],
            "the exact actual scalar identity")
    count = doc["saved_record_count"]
    require(type(count) is int and 0 <= count <= 12
            and doc["completed_targets"] == manifest["target_order"][:count]
            and set(doc["new_records"]) == set(doc["completed_targets"])
            and doc["parameters"] == manifest["parameters"]
            and sorted(doc) == manifest["allowed_scientific_fields"]
            and all(doc[key] == 0 for key in ("old_scientific_target_calls","new_arrays_published",
                                             "new_artifacts","new_Releases")),
            "one whole actual prefix and no replayed old target")
    for index,name in enumerate(doc["completed_targets"]):
        record = doc["new_records"][name]
        require(set(record) == {"ball","bound"} and isinstance(record["ball"],str)
                and record["bound"] == ("lower" if index in (1,5,6) else "upper"),
                "the complete saved bound and its correct direction")
    if doc["complete"]:
        result = doc["result"]
        require(count == 12 and doc["proved"] is True and doc["failure"] is None
                and doc["actual_returncode"] == 0 and doc["current_target"] is doc["candidate_record"] is None
                and doc["stage"] == "complete_"+manifest["stage"]+"_scalar_branch"
                and result["kind"] == manifest["scientific_kind"]
                and result["complete_new_record_count"] == 12
                and result["complete_new_record_order"] == doc["completed_targets"],
                "all twelve genuinely completed new scalar targets")
        for name in ("whole_true_paired_high97_forcing_proved","all_high_modes_and_two_means_retained",
                     "mean_leakage_uses_original_full_Wiener_derivative",
                     "Jacobian_lower_includes_same_true_H_endpoint",
                     "only_true_paid_cosine_head_energy_lower_subtracted",
                     "unobserved_low_sine_energy_not_subtracted",
                     "rotation_used_only_for_commuting_high_projection_norm",
                     "every_dependent_scalar_uses_whole_formal_readback"):
            require(result[name] is True,"complete mathematical qualification: "+name)
        for name in ("old_pairings_or_trials_recomputed","actual_rotated_signed_entries_proved",
                     "complete_high_inverse_or_full_nu_Schur_proved","topic_completion_proved"):
            require(result[name] is False,"retained full problem scope: "+name)
    return doc
'''

REPORT = '''
def final_files():
    body = encode(state)
    require(len(body) <= op["maximum_execution_bytes"],"complete execution receipt budget")
    report = ("# Actual complete high parameter forcing\\n\\nRun "+run+"/"+attempt
        +"; complete: "+str(state["complete"])+".\\n\\n"
        "The child consumes the whole actually completed NP/JC results and the original W "
        "derivative Wiener data. It combines twelve new directed mean-leakage, energy and "
        "paired high-source bounds. All high modes and both density means remain. No PDE "
        "trial, carrier, DFT row, old pairing or old norm runs again. The complete high "
        "incoming inverse and the true parameter Schur remain separate obligations.\\n").encode()
    return {**staged,output_dir+"/execution.json":body,output_dir+"/report.md":report}
'''


def require(ok,message):
    if not ok:
        raise ValueError(message)


def build_adapter(root):
    raw = (root/PARENT).read_bytes()
    require(hashlib.sha256(raw).hexdigest() == PARENT_SHA,"the entire frozen public parent")
    spec = importlib.util.spec_from_file_location("_NH_complete_public_parent",root/PARENT)
    parent = importlib.util.module_from_spec(spec);spec.loader.exec_module(parent)
    tree = parent.build_adapter(root)
    strings = dict.fromkeys(REPLACEMENTS,0)
    functions = {"materialize":MATERIALIZE,"validate_output":VALIDATOR,"final_files":REPORT}
    counts = dict.fromkeys(functions,0)
    comparisons = {"counts":0,"historical":0}
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
            pairs = {
                'manifest["complete_record_counts"] == [2]':('counts','manifest["complete_record_counts"] == [12]'),
                'len(manifest["historical_inputs"]) == 51':('historical','len(manifest["historical_inputs"]) == 4'),
            }
            for original,(label,replacement) in pairs.items():
                if ast.dump(node) == ast.dump(ast.parse(original,mode="eval").body):
                    comparisons[label] += 1
                    return ast.copy_location(ast.parse(replacement,mode="eval").body,node)
            return self.generic_visit(node)
    tree = Adapter().visit(tree)
    require(all(value == 1 for group in (strings,counts,comparisons) for value in group.values()),
            "only the declared new identities, small inputs and result handlers changed")
    tree.body[0].value = ast.Constant(__doc__);ast.fix_missing_locations(tree);return tree


def main():
    parser = argparse.ArgumentParser(add_help=False);parser.add_argument("--repo",required=True)
    args,_ = parser.parse_known_args();root = Path(args.repo).resolve()
    namespace = {"__name__":"_NH_complete_public_worker","__file__":__file__}
    exec(compile(build_adapter(root),"<NH complete public worker>","exec"),namespace)
    namespace["main"]()


if __name__ == "__main__":
    main()
