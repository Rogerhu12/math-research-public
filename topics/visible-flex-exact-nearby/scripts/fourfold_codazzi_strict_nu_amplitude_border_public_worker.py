"""PA uses the original complete NP public engine for a new amplitude row.

Necessary readonly native restoration, capacity, README checks, actual
prefix preservation and rebase/push loops remain inherited unchanged.
"""
from __future__ import annotations
import argparse, ast, hashlib, importlib.util
from pathlib import Path

TOPIC = "topics/visible-flex-exact-nearby"
PARENT = TOPIC+"/scripts/fourfold_codazzi_strict_nu_particular_public_worker.py"
PARENT_SHA = "0f4d3b932a5632019bf9581c2ae2fa057cc63323d8699e7f45e4f44b9dc93aba"
REPLACEMENTS = {
    "R147_true_selected_strict_nu_particular_inputs_v1":"R147_complete_strict_nu_amplitude_border_inputs_v1",
    "true_selected_strict_nu_particular":"complete_strict_nu_amplitude_border",
    "actual-strict-nu-particular.json":"actual-strict-nu-amplitude-border.json",
    "actual-strict-nu-particular-":"actual-strict-nu-amplitude-border-",
    "R147_true_selected_strict_nu_particular_execution_v1":"R147_complete_strict_nu_amplitude_border_execution_v1",
    "consumed_R147_true_selected_strict_nu_particular_v1":"consumed_R147_complete_strict_nu_amplitude_border_v1",
    "one complete strict true-nu particular manifest":"one complete strict nu amplitude border manifest",
    "visible-exact: reserve strict true nu ":"visible-exact: reserve strict nu amplitude border ",
    "visible-exact: preserve strict true nu ":"visible-exact: preserve strict nu amplitude border ",
}

VALIDATOR = '''
def validate_output(raw):
    require(0 < len(raw) <= op["maximum_scientific_bytes"],"one whole actual amplitude conclusion")
    doc = parse(raw);identity = doc["identity"]
    require(identity["kind"] == manifest["scientific_kind"] and identity["scalar_stage"] == manifest["stage"]
        and identity["source_sha256"] == by_role["science"]["sha256"]
        and identity["manifest_sha256"] == args.manifest_sha and identity["run_id"] == run
        and identity["run_attempt"] == attempt
        and identity["arithmetic_bits"] == manifest["parameters"]["arithmetic_bits"],
        "whole actual public amplitude identity")
    count = doc["saved_record_count"]
    require(type(count) is int and 0 <= count <= 8
        and doc["completed_targets"] == manifest["target_order"][:count]
        and set(doc["new_records"]) == set(doc["completed_targets"])
        and doc["parameters"] == manifest["parameters"] and sorted(doc) == manifest["allowed_scientific_fields"]
        and all(doc[key] == 0 for key in ("old_scientific_target_calls","new_arrays_published",
                                         "new_artifacts","new_Releases")),
        "entire genuine prefix and no old scientific target replay")
    for index,name in enumerate(doc["completed_targets"]):
        record = doc["new_records"][name]
        require(set(record) == {"ball","bound"} and isinstance(record["ball"],str)
            and record["bound"] == ("signed_enclosure" if index in (3,6,7) else "upper"),
            "all complete new signed balls and upper fees in proper order")
    if doc["complete"]:
        result = doc["result"]
        require(count == 8 and doc["proved"] is True and doc["failure"] is None
            and doc["actual_returncode"] == 0 and doc["current_target"] is doc["candidate_record"] is None
            and doc["stage"] == "complete_"+manifest["stage"]+"_scalar_branch"
            and result["kind"] == manifest["scientific_kind"] and result["complete_new_record_count"] == 8
            and result["complete_new_record_order"] == doc["completed_targets"]
            and doc["necessary_original_trial_receipts"]["all_four_complete_arrays_read_back"] is True
            and doc["necessary_original_trial_receipts"]["new_trial_selected"] is False,
            "all eight truly completed new scalar targets and same original carrier input")
        for name in ("same_original_NP_complete_trial_carriers_restored","same_selected_Q_delta_amplitude_row_paid",
                     "whole_original97_amplitude_entries_and_their_signs_retained",
                     "full_infinite_error_paid_in_primitive_plus_mean_dual","both_physical_density_means_retained",
                     "physical_and_original_alpha_normalized_signed_balls_separate",
                     "every_dependent_scalar_uses_whole_formal_readback"):
            require(result[name] is True,"complete mathematical qualification: "+name)
        for name in ("new_trial_selected","old_residual_or_signed_pairings_recomputed",
                     "old_amplitude_Bessel_or_row_targets_recomputed","nonlocal_phase_column_proved",
                     "true_nu_or_phase_Schur_nonzero_proved","topic_completion_proved"):
            require(result[name] is False,"retained actual whole problem scope: "+name)
    return doc
'''

REPORT = '''
def final_files():
    body = encode(state)
    require(len(body) <= op["maximum_execution_bytes"],"whole execution receipt budget")
    report = ("# Actual strict parameter amplitude border\\n\\nRun "+run+"/"+attempt
        +"; complete: "+str(state["complete"])+".\\n\\n"
        "The child restores NP's necessary exact original four complete trial carriers, "
        "preserving their full original hashes, then evaluates one new signed physical "
        "amplitude pairing against all97 original rational row entries. It pays the "
        "complete selected-background row change and the full infinite NP error in "
        "primitive plus mean norm. The physical and exact-alpha-normalized signed "
        "balls remain separate. No old residual, signed observation, Bessel or row "
        "target runs again. Phase, full incoming matching and the true Schur remain.\\n").encode()
    return {**staged,output_dir+"/execution.json":body,output_dir+"/report.md":report}
'''


def require(ok,message):
    if not ok:
        raise ValueError(message)


def build_adapter(root):
    raw = (root/PARENT).read_bytes()
    require(hashlib.sha256(raw).hexdigest() == PARENT_SHA,"the whole frozen original NP engine")
    spec = importlib.util.spec_from_file_location("_PA_complete_public_parent",root/PARENT)
    parent = importlib.util.module_from_spec(spec);spec.loader.exec_module(parent)
    tree = parent.build_adapter(root);strings = dict.fromkeys(REPLACEMENTS,0)
    functions = {"validate_output":VALIDATOR,"final_files":REPORT};counts = dict.fromkeys(functions,0)
    comparisons = {"counts":0}
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
            original = ast.parse('manifest["complete_record_counts"] == [2]',mode="eval").body
            if ast.dump(node) == ast.dump(original):
                comparisons["counts"] += 1
                return ast.copy_location(ast.parse('manifest["complete_record_counts"] == [8]',mode="eval").body,node)
            return self.generic_visit(node)
    tree = Adapter().visit(tree)
    require(all(value == 1 for group in (strings,counts,comparisons) for value in group.values()),
            "only the declared new identities, target count and whole-result handlers change")
    tree.body[0].value = ast.Constant(__doc__);ast.fix_missing_locations(tree);return tree


def main():
    parser = argparse.ArgumentParser(add_help=False);parser.add_argument("--repo",required=True)
    args,_ = parser.parse_known_args();root = Path(args.repo).resolve()
    namespace = {"__name__":"_PA_complete_public_worker","__file__":__file__}
    exec(compile(build_adapter(root),"<PA complete public worker>","exec"),namespace)
    namespace["main"]()


if __name__ == "__main__":
    main()

