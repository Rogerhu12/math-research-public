"""PO reuses the complete fixed public engine for one new96 inverse.

Only the task identities and complete-result handlers change.  Capacity,
periodic README diffs, prefix retention and rebase/push remain inherited.
"""
from __future__ import annotations
import argparse, ast, hashlib, importlib.util
from pathlib import Path

TOPIC = "topics/visible-flex-exact-nearby"
PARENT = TOPIC+"/scripts/fourfold_codazzi_strict_nu_high_forcing_public_worker.py"
PARENT_SHA = "4e69d9f73cbcb616983259367d3f38a077f626b0fcf8ee56e66627ed0e9482d1"
REPLACEMENTS = {
    "R147_complete_true_strict_nu_high_forcing_inputs_v1":"R147_complete_physical_nu_observation_inverse_inputs_v1",
    "complete_true_strict_nu_high_forcing":"complete_physical_nu_observation_inverse",
    "actual-strict-nu-high-forcing.json":"actual-physical-nu-observation-inverse.json",
    "actual-strict-nu-high-forcing-":"actual-physical-nu-observation-inverse-",
    "R147_complete_true_strict_nu_high_forcing_execution_v1":"R147_complete_physical_nu_observation_inverse_execution_v1",
    "consumed_R147_complete_true_strict_nu_high_forcing_v1":"consumed_R147_complete_physical_nu_observation_inverse_v1",
    "one complete true-nu high forcing scalar manifest":"one complete physical nu observation inverse manifest",
    "visible-exact: reserve strict nu high forcing ":"visible-exact: reserve physical nu observation inverse ",
    "visible-exact: preserve strict nu high forcing ":"visible-exact: preserve physical nu observation inverse ",
}

VALIDATOR = '''
def validate_output(raw):
    require(0 < len(raw) <= op["maximum_scientific_bytes"],"whole complete new inverse result")
    doc = parse(raw);identity = doc["identity"]
    require(identity["kind"] == manifest["scientific_kind"] and identity["scalar_stage"] == manifest["stage"]
        and identity["source_sha256"] == by_role["science"]["sha256"]
        and identity["manifest_sha256"] == args.manifest_sha
        and identity["run_id"] == run and identity["run_attempt"] == attempt
        and identity["arithmetic_bits"] == manifest["parameters"]["arithmetic_bits"],
        "the same actual public child identity")
    count = doc["saved_record_count"]
    require(type(count) is int and 0 <= count <= 12
        and doc["completed_targets"] == manifest["target_order"][:count]
        and set(doc["new_records"]) == set(doc["completed_targets"])
        and doc["parameters"] == manifest["parameters"] and sorted(doc) == manifest["allowed_scientific_fields"]
        and all(doc[key] == 0 for key in ("old_scientific_target_calls","new_arrays_published",
                                         "new_artifacts","new_Releases")),
        "one entire actual prefix and no old target replay")
    for name in doc["completed_targets"]:
        record = doc["new_records"][name]
        require(set(record) == {"ball","bound"} and isinstance(record["ball"],str)
                and record["bound"] == "upper","whole saved new upper ball")
    if doc["complete"]:
        result = doc["result"]
        require(count == 12 and doc["proved"] is True and doc["failure"] is None
            and doc["actual_returncode"] == 0 and doc["current_target"] is doc["candidate_record"] is None
            and doc["stage"] == "complete_"+manifest["stage"]+"_scalar_branch"
            and result["kind"] == manifest["scientific_kind"]
            and result["complete_new_record_count"] == 12
            and result["complete_new_record_order"] == doc["completed_targets"]
            and doc["necessary_old_carrier_receipts"]["complete_grid"] is True
            and doc["necessary_old_carrier_receipts"]["complete_rows"] == 96
            and doc["private_new_inverse_receipt"]["complete_readback"] is True
            and doc["private_new_inverse_receipt"]["arrays_published"] is False,
            "all twelve genuine new scalar conclusions and necessary complete private inputs")
        for name in ("complete_even96_observation_inverse_proved","original_uninflated_whole_NP_pairings_used",
                     "only_actual_even_nonmean_physical_trial_reconstructed",
                     "mean_translation_not_H_zero_value_removed","same_true_H_full_Wiener_and_Jacobian_used",
                     "complete_infinite_physical_tail_and_PDE_error_paid","both_independent_density_means_retained",
                     "same_sign_original_target_B_and_same_high_index_retained",
                     "every_dependent_scalar_uses_whole_formal_readback"):
            require(result[name] is True,"complete mathematical qualification: "+name)
        for name in ("old_pairings_or_trials_or_norm_targets_recomputed","unobserved_h2_sine_phase_or_amplitude_recovered",
                     "actual_rotated_signed_entries_proved","complete_high_inverse_or_full_nu_Schur_proved",
                     "topic_completion_proved"):
            require(result[name] is False,"retained full problem scope: "+name)
    return doc
'''

REPORT = '''
def final_files():
    body = encode(state)
    require(len(body) <= op["maximum_execution_bytes"],"whole execution receipt budget")
    report = ("# Actual physical parameter observation inverse\\n\\nRun "+run+"/"+attempt
        +"; complete: "+str(state["complete"])+".\\n\\n"
        "The child consumes the complete actual NP/NH/JC/RW/NW outcomes. It restores only "
        "necessary exact original RW carriers, computes the new full96 observation inverse, "
        "and bounds the physical parameter tail in the original target coordinates. "
        "All192 raw signed NP balls remain distinct from194 inflated true observations. "
        "Only the even mean-zero physical trial is recovered. Independent means, unobserved "
        "directions, the full PDE error and the true parameter Schur remain. No old trial, "
        "pairing, row-error or norm target runs again.\\n").encode()
    return {**staged,output_dir+"/execution.json":body,output_dir+"/report.md":report}
'''


def require(ok,message):
    if not ok:
        raise ValueError(message)


def build_adapter(root):
    raw = (root/PARENT).read_bytes()
    require(hashlib.sha256(raw).hexdigest() == PARENT_SHA,"the entire frozen public parent")
    spec = importlib.util.spec_from_file_location("_PO_complete_public_parent",root/PARENT)
    parent = importlib.util.module_from_spec(spec);spec.loader.exec_module(parent)
    tree = parent.build_adapter(root);strings = dict.fromkeys(REPLACEMENTS,0)
    functions = {"validate_output":VALIDATOR,"final_files":REPORT};counts = dict.fromkeys(functions,0)
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
    tree = Adapter().visit(tree)
    require(all(value == 1 for group in (strings,counts) for value in group.values()),
            "only new task identities and complete output handlers change")
    tree.body[0].value = ast.Constant(__doc__);ast.fix_missing_locations(tree);return tree


def main():
    parser = argparse.ArgumentParser(add_help=False);parser.add_argument("--repo",required=True)
    args,_ = parser.parse_known_args();root = Path(args.repo).resolve()
    namespace = {"__name__":"_PO_complete_public_worker","__file__":__file__}
    exec(compile(build_adapter(root),"<PO complete public worker>","exec"),namespace)
    namespace["main"]()


if __name__ == "__main__":
    main()

