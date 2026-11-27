"""P96: public first phase row on the same whole original96 finite trials.

Reuse the complete PHI public engine. Only task names, complete input
materialization and the six new result handlers change. In particular the
README checks, capacity checks, one-child reservation, actual-failure
publication and immediate pull/rebase/push loop are inherited unchanged.
"""
from __future__ import annotations
import argparse, ast, hashlib, importlib.util
from pathlib import Path

TOPIC = 'topics/visible-flex-exact-nearby'
PARENT = TOPIC+'/scripts/fourfold_codazzi_strict_nu_phase_public_worker.py'
PARENT_SHA = '32569d72195ed7640bd47d2d6e1690d299e1636fb93365dea4855e28432f0eef'
REPLACEMENTS = {
    'R147_complete_strict_nu_nonlocal_phase_inputs_v1':'R149_complete_original_finite_trial_phase_row_inputs_v1',
    'complete_strict_nu_nonlocal_phase':'complete_original_finite_trial_phase_row',
    'actual-strict-nu-phase.json':'actual-finite-trial-phase.json',
    'actual-strict-nu-phase-':'actual-finite-trial-phase-',
    'R147_complete_strict_nu_nonlocal_phase_execution_v1':'R149_complete_original_finite_trial_phase_execution_v1',
    'consumed_R147_complete_strict_nu_nonlocal_phase_v1':'consumed_R149_complete_original_finite_trial_phase_v1',
    'one complete strict nonlocal phase manifest':'one complete original96 finite-trial phase manifest',
    'visible-exact: reserve strict nonlocal phase ':'visible-exact: reserve original96 trial phase ',
    'visible-exact: preserve strict nonlocal phase ':'visible-exact: preserve original96 trial phase ',
}

MATERIALIZE = '''
def materialize(head):
    import importlib.util
    def remember(item,destination,raw=None):
        role = item["role"]
        if role in snapshots:
            require(snapshots[role] == destination,"same exact original input path on repeated materialization")
            saved = destination.read_bytes()
            require(len(saved) == item["bytes"] and sha(saved) == item["sha256"],
                    "idempotent reuse requires the same whole original bytes and SHA")
            if raw is not None:require(saved == raw,"no different object silently replaces an admitted input")
        else:
            require(raw is not None,"first input restoration supplies all original bytes")
            atomic(destination,raw);snapshots[role] = destination
    for spec in specs:
        raw = checked_bytes(spec,head)
        if spec["path"].endswith(".py"):ast.parse(raw.decode(),filename=spec["path"])
        destination = source_dir/("input_"+spec["role"]+Path(spec["path"]).suffix)
        remember(spec,destination,raw)
    definition = importlib.util.spec_from_file_location("_P96_complete_input_expansion",snapshots["phase_carriers"])
    carrier = importlib.util.module_from_spec(definition);definition.loader.exec_module(carrier)
    original,unused = carrier.original(snapshots["original_phase_carriers"])
    originals = manifest["historical_inputs"]+carrier.expand(manifest["phase_input_plan"],original)
    require(len(originals) == 391 and len({x["role"] for x in originals}) == len(originals),
            "all original base/row inputs and complete169 phase/scalar objects")
    for item in originals:
        destination = source_dir/"original-native"/topic_path(item["path"])
        if item["role"] in snapshots:
            remember(item,destination)
        else:
            fetch_commit(item["commit"])
            remember(item,destination,checked_bytes(item,item["commit"],small=False))
    require(len(snapshots) == len(specs)+391,"every complete current and original object restored")
    require(sha(Path(__file__).read_bytes()) == by_role["worker"]["sha256"],"the entire actual P96 worker")
    require(sha(git("show",head+":"+str(mpath.relative_to(root)),binary=True).stdout)
            == args.manifest_sha,"whole P96 manifest unchanged after pull")
    state["current_input_receipts"] = specs
    state["historical_restoration"] = {"complete_original_files":391,
        "original_base_row_and_selected_family_files":51,"necessary_original_phase_germs":169,
        "necessary_original_scalar_germs":169,"complete_original_error_natives":2,
        "whole_original_descriptors_sha256":sha(encode(originals)),
        "all_original_bytes_retained_in_private_input_tree":True,
        "repeated_materialization_reuses_only_identical_whole_objects":True,
        "old_scientific_targets_evaluated":0}
'''

VALIDATOR = '''
def validate_output(raw):
    require(0 < len(raw) <= op["maximum_scientific_bytes"],"whole actual96-column phase conclusion")
    doc = parse(raw);identity = doc["identity"]
    require(identity["kind"] == manifest["scientific_kind"] and identity["scalar_stage"] == manifest["stage"]
        and identity["source_sha256"] == by_role["science"]["sha256"]
        and identity["manifest_sha256"] == args.manifest_sha and identity["run_id"] == run
        and identity["run_attempt"] == attempt and identity["arithmetic_bits"] == 320,
        "whole original-selected finite-trial phase identity")
    count = doc["saved_record_count"]
    require(type(count) is int and 0 <= count <= 6
        and doc["completed_targets"] == manifest["target_order"][:count]
        and set(doc["new_records"]) == set(doc["completed_targets"])
        and doc["parameters"] == manifest["parameters"] and sorted(doc) == manifest["allowed_scientific_fields"]
        and all(doc[key] == 0 for key in ("old_scientific_target_calls","new_arrays_published","new_artifacts","new_Releases")),
        "the entire real new prefix and no old target replay")
    def vector(record,bound,centres=False):
        keys = {"complete_count","bound","balls"}|({"exact_dyadic_centres"} if centres else set())
        require(set(record) == keys and record["complete_count"] == 96 and record["bound"] == bound
            and len(record["balls"]) == 96 and all(isinstance(x,str) for x in record["balls"]),
            "one complete96-entry signed or upper target")
        if centres:
            require(len(record["exact_dyadic_centres"]) == 96
                and all(isinstance(x,str) for x in record["exact_dyadic_centres"]),
                "all96 exact dyadic centres retained separately from the complete true balls")
    for i,name in enumerate(doc["completed_targets"]):
        record = doc["new_records"][name]
        if i == 5:
            require(set(record) == {"ball","bound"} and isinstance(record["ball"],str)
                and record["bound"] == "upper","complete joint row radius")
        else:vector(record,"signed_enclosure" if i in (0,4) else "upper",i == 4)
    carrier_calls = doc["necessary_original_carrier_calls"]
    require(set(carrier_calls) == {"TC_floating_factory","original_nodal_QR"}
        and carrier_calls["TC_floating_factory"] in (0,1) and carrier_calls["original_nodal_QR"] == 0,
        "necessary same TC factory rematerialization is explicit and old nodal QR is absent")
    prefix = doc["phase_integral_prefix"]
    if prefix is not None:
        require(prefix["kind"] == "P96_complete_new_phase_germ_prefix_v1"
            and prefix["exact_interval"][0] == "0"
            and type(prefix["last_complete_original_germ"]) is int
            and 0 <= prefix["last_complete_original_germ"] <= 168
            and 0 < prefix["complete_original_steps"] <= 3095
            and prefix["complete_new_intersections"] > 0
            and prefix["maximum_complete_row_degree"] <= 160
            and prefix["all96_columns_and_all_old_scalar_remainders_retained"] is True
            and prefix["all_eight_exact_radial_moments_retained"] is True,
            "one genuinely accepted complete original germ with all96 trial pairings")
        if "complete_accumulators_in_new_records" in prefix:
            require(count >= 3 and prefix["complete_accumulators_in_new_records"] == manifest["target_order"][:3]
                and len(prefix["whole_completed_integral_prefix_sha256"]) == 64,
                "completed accumulators moved whole into their natural target objects")
        else:
            for key,bound in (("signed_original_trial_row96","signed_enclosure"),
                ("complete_trial_L1_L2_upper96","upper"),("complete_field_L1_upper96","upper")):
                vector(prefix[key],bound)
    if doc["complete"]:
        result = doc["result"]
        require(count == 6 and doc["proved"] is True and doc["failure"] is None
            and doc["actual_returncode"] == 0 and doc["current_target"] is doc["candidate_record"] is None
            and doc["stage"] == "complete_"+manifest["stage"]+"_scalar_branch"
            and result["kind"] == manifest["scientific_kind"] and result["complete_new_target_count"] == 6
            and result["complete_new_target_order"] == manifest["target_order"]
            and result["complete_signed_phase_columns"] == 96
            and prefix["exact_interval"] == manifest["parameters"]["exact_phase_carrier_interval"]
            and prefix["last_complete_original_germ"] == 168 and prefix["complete_original_steps"] == 3095
            and carrier_calls["TC_floating_factory"] == 1
            and doc["necessary_original_trial_receipts"]["all_four_original_TC_arrays_verified"] is True
            and len(doc["necessary_original_trial_receipts"]["complete_original_arrays"]) == 4
            and doc["necessary_original_phase_receipts"]["whole_original_polynomial_sha256_checks"] == 3095
            and doc["necessary_original_phase_receipts"]["whole_original_two_leg_endpoint_checks"] == 169,
            "all six complete new objects with all original carrier identities")
        for key in ("same_original_selected_Q_delta","same_four_whole_original_TC_arrays",
            "all169_original_phase_germs","all3095_original_two_leg_polynomial_hashes",
            "complete_true_root_sliver_included","full_adjoint_row_formed_before_finite_pairing",
            "all_eight_exact_radial_moments_retained","complete_selected_label_and_background_errors_paid",
            "both_means_and_original_phase_constant_retained","same_original_orthonormal_trial_input_coordinates",
            "complete_final_balls_and_exact_dyadic_centres_saved","joint_radius_includes_all_final_ball_radii",
            "every_dependent_target_uses_whole_saved_readback"):
            require(result[key] is True,"complete finite-trial functional qualification: "+key)
        for key in ("old_scientific_targets_recomputed","new_trial_selected","true_PDE_corrected_columns_proved",
            "original_TC_negative_result_complete","full_regular_or_Theta_inverse_proved",
            "full_phase_Schur_or_topic_completion_proved"):
            require(result[key] is False,"the original unfinished PDE/inverse ports remain separate: "+key)
    return doc
'''

REPORT = '''
def final_files():
    state["necessary_original_carrier_calls"] = (result or {}).get("necessary_original_carrier_calls")
    body = encode(state)
    require(len(body) <= op["maximum_execution_bytes"],"whole P96 execution receipt budget")
    report = ("# Actual phase row on the original96 finite trials\\n\\nRun "+run+"/"+attempt
        +"; complete: "+str(state["complete"])+".\\n\\n"
        "The child necessarily rematerializes the same four complete original TC arrays and all169 "
        "original two-leg phase carriers, with their original whole hashes. It computes one complete "
        "adjoint phase row, eight exact radial moments and all96 pairings, paying the entire selected "
        "background, label and true-root-sliver errors. The saved true signed balls and their exact "
        "dyadic centres are separate objects; the joint radius includes every ball radius. "
        "Old residual, norm and trial-matrix targets are not evaluated. In particular the incomplete "
        "TC negative/positive PDE corrections and the full phase Schur are not asserted.\\n").encode()
    return {**staged,output_dir+"/execution.json":body,output_dir+"/report.md":report}
'''


def require(ok, message):
    if not ok:
        raise ValueError(message)


def build_adapter(root):
    raw = (root/PARENT).read_bytes()
    require(hashlib.sha256(raw).hexdigest() == PARENT_SHA, 'whole original PHI public engine')
    spec = importlib.util.spec_from_file_location('_P96_original_public_engine', root/PARENT)
    parent = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(parent)
    tree = parent.build_adapter(root)
    strings = dict.fromkeys(REPLACEMENTS, 0)
    functions = {'materialize':MATERIALIZE,'validate_output':VALIDATOR,'final_files':REPORT}
    counts = dict.fromkeys(functions, 0)
    class Adapter(ast.NodeTransformer):
        def visit_Constant(self, node):
            if isinstance(node.value,str) and node.value in REPLACEMENTS:
                strings[node.value] += 1
                return ast.copy_location(ast.Constant(REPLACEMENTS[node.value]),node)
            return node
        def visit_FunctionDef(self, node):
            if node.name in functions:
                counts[node.name] += 1
                return ast.copy_location(ast.parse(functions[node.name]).body[0],node)
            return self.generic_visit(node)
    tree = Adapter().visit(tree)
    require(all(x == 1 for group in (strings,counts) for x in group.values()),
            'only the declared names and complete input/result handlers change')
    tree.body[0].value = ast.Constant(__doc__)
    ast.fix_missing_locations(tree)
    return tree


def main():
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument('--repo',required=True)
    args,unused = parser.parse_known_args()
    namespace = {'__name__':'_P96_complete_public_worker','__file__':__file__}
    exec(compile(build_adapter(Path(args.repo).resolve()),'<P96 complete public worker>','exec'),namespace)
    namespace['main']()


if __name__ == '__main__':
    main()
