"""PHI uses the unchanged public NP engine for the first nonlocal phase target.

Only complete input materialization, names and result handlers change.
Capacity, README pull checks, prefix publication and immediate rebase/push
loops remain inherited. No automatic old or new scientific retry is added.
"""
from __future__ import annotations
import argparse, ast, hashlib, importlib.util
from pathlib import Path

TOPIC = 'topics/visible-flex-exact-nearby'
PARENT = TOPIC+'/scripts/fourfold_codazzi_strict_nu_particular_public_worker.py'
PARENT_SHA = '0f4d3b932a5632019bf9581c2ae2fa057cc63323d8699e7f45e4f44b9dc93aba'
REPLACEMENTS = {
    'R147_true_selected_strict_nu_particular_inputs_v1':'R147_complete_strict_nu_nonlocal_phase_inputs_v1',
    'true_selected_strict_nu_particular':'complete_strict_nu_nonlocal_phase',
    'actual-strict-nu-particular.json':'actual-strict-nu-phase.json',
    'actual-strict-nu-particular-':'actual-strict-nu-phase-',
    'R147_true_selected_strict_nu_particular_execution_v1':'R147_complete_strict_nu_nonlocal_phase_execution_v1',
    'consumed_R147_true_selected_strict_nu_particular_v1':'consumed_R147_complete_strict_nu_nonlocal_phase_v1',
    'one complete strict true-nu particular manifest':'one complete strict nonlocal phase manifest',
    'visible-exact: reserve strict true nu ':'visible-exact: reserve strict nonlocal phase ',
    'visible-exact: preserve strict true nu ':'visible-exact: preserve strict nonlocal phase ',
}

MATERIALIZE = '''
def materialize(head):
    import importlib.util
    for spec in specs:
        raw = checked_bytes(spec,head)
        if spec["path"].endswith(".py"):ast.parse(raw.decode(),filename=spec["path"])
        destination = source_dir/("input_"+spec["role"]+Path(spec["path"]).suffix)
        atomic(destination,raw);snapshots[spec["role"]] = destination
    definition = importlib.util.spec_from_file_location("_PHI_complete_input_expansion",snapshots["phase_carriers"])
    carrier = importlib.util.module_from_spec(definition);definition.loader.exec_module(carrier)
    originals = manifest["historical_inputs"]+carrier.expand(manifest["phase_input_plan"])
    require(len(originals) == 315 and len({x["role"] for x in originals}) == len(originals),
            "all original NP and whole phase scalar/native objects")
    for item in originals:
        role = item["role"]
        require(role not in snapshots,"no original input silently replaced")
        fetch_commit(item["commit"])
        raw = checked_bytes(item,item["commit"],small=False)
        destination = source_dir/"original-native"/topic_path(item["path"])
        atomic(destination,raw);snapshots[role] = destination
    require(len(snapshots) == len(specs)+315,"every whole original file restored")
    require(sha(Path(__file__).read_bytes()) == by_role["worker"]["sha256"],"entire actual frozen worker")
    require(sha(git("show",head+":"+str(mpath.relative_to(root)),binary=True).stdout)
            == args.manifest_sha,"whole input manifest unchanged after pull")
    state["current_input_receipts"] = specs
    state["historical_restoration"] = {"complete_original_files":315,
        "original_NP_input_files":51,"necessary_original_phase_germs":131,
        "necessary_original_scalar_germs":131,"complete_original_error_natives":2,
        "whole_original_descriptors_sha256":sha(encode(originals)),
        "all_original_bytes_retained_in_private_input_tree":True,"old_scientific_targets_evaluated":0}
'''

VALIDATOR = '''
def validate_output(raw):
    require(0 < len(raw) <= op["maximum_scientific_bytes"],"whole actual nonlocal phase conclusion")
    doc = parse(raw);identity = doc["identity"]
    require(identity["kind"] == manifest["scientific_kind"] and identity["scalar_stage"] == manifest["stage"]
        and identity["source_sha256"] == by_role["science"]["sha256"]
        and identity["manifest_sha256"] == args.manifest_sha and identity["run_id"] == run
        and identity["run_attempt"] == attempt and identity["arithmetic_bits"] == 320,
        "whole actual original-selected phase identity")
    count = doc["saved_record_count"]
    require(type(count) is int and 0 <= count <= 6
        and doc["completed_targets"] == manifest["target_order"][:count]
        and set(doc["new_records"]) == set(doc["completed_targets"])
        and doc["parameters"] == manifest["parameters"] and sorted(doc) == manifest["allowed_scientific_fields"]
        and all(doc[key] == 0 for key in ("old_scientific_target_calls","new_arrays_published","new_artifacts","new_Releases")),
        "whole real prefix and no old scientific target replay")
    for i,name in enumerate(doc["completed_targets"]):
        record = doc["new_records"][name]
        require(set(record) == {"ball","bound"} and isinstance(record["ball"],str)
            and record["bound"] == ("signed_enclosure" if i in (0,5) else "upper"),
            "complete signed or upper new scalar")
    prefix = doc["phase_integral_prefix"]
    if prefix is not None:
        require(prefix["kind"] == "PHI_complete_new_phase_integral_prefix_v1"
            and prefix["exact_interval"][0] == "0"
            and type(prefix["last_complete_original_germ"]) is int
            and 0 <= prefix["last_complete_original_germ"] <= 130
            and 0 < prefix["complete_original_steps"] <= 1572
            and prefix["complete_new_intersections"] > 0
            and prefix["maximum_complete_output_degree"] <= 256
            and prefix["all_new_cells_and_scalar_remainders_retained"] is True
            and prefix["signed_trial_integral"]["bound"] == "signed_enclosure"
            and prefix["whole_forcing_L1_upper"]["bound"] == "upper"
            and prefix["whole_direct_selected_field_difference_L1_upper"]["bound"] == "upper",
            "a genuinely complete accepted new radial prefix")
    if doc["complete"]:
        result = doc["result"]
        require(count == 6 and doc["proved"] is True and doc["failure"] is None
            and doc["actual_returncode"] == 0 and doc["current_target"] is doc["candidate_record"] is None
            and doc["stage"] == "complete_"+manifest["stage"]+"_scalar_branch"
            and result["kind"] == manifest["scientific_kind"] and result["complete_new_record_count"] == 6
            and result["complete_new_record_order"] == manifest["target_order"]
            and prefix["exact_interval"] == ["0","9/50"]
            and prefix["last_complete_original_germ"] == 130 and prefix["complete_original_steps"] == 1572
            and doc["necessary_original_trial_receipts"]["all_four_complete_arrays_read_back"] is True
            and doc["necessary_original_phase_receipts"]["whole_original_polynomial_sha256_checks"] == 1572
            and doc["necessary_original_phase_receipts"]["whole_original_two_leg_endpoint_checks"] == 131,
            "all six actual targets and complete original carrier identities")
        for key in ("same_original_selected_Q_delta","whole_original_NP_arrays_restored",
            "whole_original_two_leg_phase_polynomials_restored","original_phase_constant_preserved",
            "true_squared_label_weight_used","full_direct_metric_and_state_mean_retained",
            "complete_selected_background_change_paid","complete_infinite_PDE_response_error_paid",
            "all_accepted_new_integral_prefixes_preserved","every_dependent_scalar_uses_whole_readback","strict_particular_only"):
            require(result[key] is True,"complete phase qualification: "+key)
        for key in ("old_phase_residual_or_norm_targets_recomputed","old_NP_scientific_targets_recomputed",
            "new_trial_selected","full_regular_response_phase_column_proved","physical_height_or_rigid_ports_proved",
            "true_nu_or_phase_Schur_proved","topic_completion_proved"):
            require(result[key] is False,"retained original full-problem scope: "+key)
        require(type(result["strict_phase_enclosure_excludes_zero"]) is bool,
                "actual nonzero status is reported separately from enclosure completion")
    return doc
'''

REPORT = '''
def final_files():
    body = encode(state)
    require(len(body) <= op["maximum_execution_bytes"],"whole execution receipt budget")
    report = ("# Actual strict parameter nonlocal phase pairing\\n\\nRun "+run+"/"+attempt
        +"; complete: "+str(state["complete"])+".\\n\\n"
        "The child restores the necessary original NP carriers and original two-leg phase polynomials, "
        "then computes the first signed nonlocal phase pairing with the true squared-label weight. "
        "It pays the full selected-background change, direct metric source, mean term and infinite PDE error. "
        "Every completed new radial prefix is retained; old residual, norm, pairing and KAM targets remain read-only. "
        "The full regular response, physical height, rigid ports and final phase Schur remain separate.\\n").encode()
    return {**staged,output_dir+"/execution.json":body,output_dir+"/report.md":report}
'''


def require(ok,message):
    if not ok:raise ValueError(message)


def build_adapter(root):
    raw = (root/PARENT).read_bytes();require(hashlib.sha256(raw).hexdigest() == PARENT_SHA,'whole original NP public engine')
    spec = importlib.util.spec_from_file_location('_PHI_original_public_engine',root/PARENT)
    parent = importlib.util.module_from_spec(spec);spec.loader.exec_module(parent)
    tree = parent.build_adapter(root);strings = dict.fromkeys(REPLACEMENTS,0)
    functions = {'materialize':MATERIALIZE,'validate_output':VALIDATOR,'final_files':REPORT}
    counts = dict.fromkeys(functions,0);comparisons = {'complete_record_counts':0}
    class Adapter(ast.NodeTransformer):
        def visit_Constant(self,node):
            if isinstance(node.value,str) and node.value in REPLACEMENTS:
                strings[node.value] += 1;return ast.copy_location(ast.Constant(REPLACEMENTS[node.value]),node)
            return node
        def visit_FunctionDef(self,node):
            if node.name in functions:
                counts[node.name] += 1;return ast.copy_location(ast.parse(functions[node.name]).body[0],node)
            return self.generic_visit(node)
        def visit_Compare(self,node):
            expected = ast.parse('manifest["complete_record_counts"] == [2]',mode='eval').body
            if ast.dump(node) == ast.dump(expected):
                comparisons['complete_record_counts'] += 1
                return ast.copy_location(ast.parse('manifest["complete_record_counts"] == [6]',mode='eval').body,node)
            return self.generic_visit(node)
    tree = Adapter().visit(tree)
    require(all(x == 1 for group in (strings,counts,comparisons) for x in group.values()),
        'only declared task names, input materialization, count and result handlers change')
    tree.body[0].value = ast.Constant(__doc__);ast.fix_missing_locations(tree);return tree


def main():
    parser = argparse.ArgumentParser(add_help=False);parser.add_argument('--repo',required=True)
    args,_ = parser.parse_known_args();root = Path(args.repo).resolve()
    namespace = {'__name__':'_PHI_complete_public_worker','__file__':__file__}
    exec(compile(build_adapter(root),'<PHI complete public worker>','exec'),namespace)
    namespace['main']()


if __name__ == '__main__':main()
