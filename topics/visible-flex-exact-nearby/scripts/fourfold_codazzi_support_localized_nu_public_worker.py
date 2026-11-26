"""Run the four new support-localized R147 scalars with the existing small worker.

The fixed predecessor supplies its public input, capacity, README, prefix,
and push/rebase machinery unchanged.  This explicit AST adapter changes
only task names, the output validator, and the human-readable task report.
It never imports a numerical producer or computes an old target.
"""
from __future__ import annotations
import argparse, ast, hashlib
from pathlib import Path

TEMPLATE = "topics/visible-flex-exact-nearby/scripts/fourfold_codazzi_negative_nu_waist_public_worker.py"
TEMPLATE_SHA256 = "17cb1a5c838cba72571880d871df533aad18577b08e28a8b92d9f681f78aff39"
REPLACEMENTS = {
    "R147_selected_negative_nu_ordinary_to_waist_inputs_v1":
        "R147_support_localized_selected_negative_nu_inputs_v1",
    "selected_negative_nu_ordinary": "support_localized_selected_negative_nu",
    "actual-negative-nu-waist.json": "actual-support-localized-nu.json",
    "actual-negative-nu-waist-": "actual-support-localized-nu-",
    "R147_complete_selected_negative_nu_ordinary_to_waist_execution_v1":
        "R147_support_localized_selected_negative_nu_execution_v1",
    "consumed_R147_selected_negative_nu_ordinary_to_waist_target_v1":
        "consumed_R147_support_localized_selected_negative_nu_target_v1",
    "one complete actual four-record same-window negative nu manifest":
        "one complete actual four-record support-localized negative nu manifest",
    "visible-exact: reserve negative nu waist ":
        "visible-exact: reserve support-localized negative nu ",
    "visible-exact: preserve negative nu waist ":
        "visible-exact: preserve support-localized negative nu ",
    "# Actual selected negative nu ordinary contribution to the waist\n\nRun ":
        "# Actual support-localized selected negative nu reception\n\nRun ",
    ".\n\nThis child reads whole S0/D/SP/PW scientific and execution files and their manifests. "
    "It evaluates only the four new selected-source and full negative-receiver records, "
    "with every candidate saved and checked before entering the completed prefix. "
    "The full same-fixed-window source includes both moving rows and the independent mean. "
    "The output is the original waist primitive pair plus both physical density means. "
    "Positive/root/interface/exterior/phase inputs, the full incoming inverse and the "
    "nonlinear closed-surface family remain separate obligations. No old producer runs.\n":
        ".\n\nThis child reads the whole completed original R147 and D files. "
        "It computes only four new scalar combinations after splitting the actual source "
        "into its base, state-change, and compact parameter-change summands. "
        "The compact summand uses the original strict L1 receiver and its exact support length; "
        "the other two summands use the already saved complete negative L2 receiver. "
        "The output retains the waist primitive pair and both physical density means. "
        "No previous source, Green, Cauchy, or receiver target is repeated. "
        "The full response, incoming inverse, parameter/phase Schur, and nonlinear family "
        "remain separate obligations.\n",
}

VALIDATOR = '''
def validate_output(raw):
    require(0 < len(raw) <= op["maximum_scientific_bytes"], "whole small scalar stage")
    doc = parse(raw)
    identity = doc["identity"]
    require(identity["kind"] == manifest["scientific_kind"]
            and identity["scalar_stage"] == manifest["stage"]
            and identity["source_sha256"] == by_role["science"]["sha256"]
            and identity["manifest_sha256"] == args.manifest_sha
            and identity["run_id"] == run and identity["run_attempt"] == attempt
            and identity["arithmetic_bits"] == manifest["parameters"]["arithmetic_bits"],
            "exact new scalar-stage identity")
    count = doc["saved_record_count"]
    require(type(count) is int and 0 <= count <= len(manifest["target_order"])
            and doc["completed_targets"] == manifest["target_order"][:count]
            and set(doc["new_records"]) == set(doc["completed_targets"])
            and doc["old_scientific_target_calls"] == 0 and doc["new_arrays_published"] == 0
            and doc["new_artifacts"] == 0 and doc["new_Releases"] == 0
            and doc["parameters"] == manifest["parameters"]
            and sorted(doc) == manifest["allowed_scientific_fields"],
            "whole saved ordered scalar prefix and exact schema without old target replay")
    if doc["complete"]:
        result = doc["result"]
        require(count == 4 and manifest["complete_record_counts"] == [4]
                and doc["proved"] is True and doc["failure"] is None
                and doc["actual_returncode"] == 0
                and doc["candidate_record"] is None and doc["current_target"] is None
                and doc["stage"] == "complete_"+manifest["stage"]+"_scalar_branch"
                and result["kind"] == manifest["scientific_kind"]
                and result["complete_new_record_count"] == 4
                and result["complete_new_record_order"] == doc["completed_targets"],
                "complete declared mathematical branch")
        for key in ("same_selected_original_source_and_receiver",
                    "source_split_made_before_receiver_norms",
                    "only_parameter_difference_is_compact",
                    "both_physical_density_means_in_output",
                    "complete_second_nonmean_source_admitted_by_SC2",
                    "complete_negative_ordinary_to_waist_density_contribution_proved",
                    "whole_saved_dependency_uppers_used",
                    "strict_improvement_of_previous_complete_record_proved",
                    "strict_upper_187_over_1000000_proved"):
            require(result[key] is True, "complete support-localized qualification: "+key)
        for key in ("old_Cauchy_source_or_strict_computation_repeated",
                    "positive_root_interface_exterior_phase_inputs_included",
                    "complete_nu_response_error_proved", "complete_incoming_inverse_proved",
                    "true_nu_or_phase_Schur_proved", "topic_completion_proved"):
            require(result[key] is False, "retained mathematical scope: "+key)
    return doc
'''


def build_adapter(root):
    """Standard-library-only source adaptation; usable by metadata generation."""
    raw = (root/TEMPLATE).read_bytes()
    if hashlib.sha256(raw).hexdigest() != TEMPLATE_SHA256:
        raise ValueError("the complete unchanged public worker template is required")
    tree = ast.parse(raw.decode(), filename=TEMPLATE)
    counts = dict.fromkeys(REPLACEMENTS, 0)
    validator_count = 0

    class Adapter(ast.NodeTransformer):
        def visit_Constant(self, node):
            if isinstance(node.value, str) and node.value in REPLACEMENTS:
                counts[node.value] += 1
                return ast.copy_location(ast.Constant(REPLACEMENTS[node.value]), node)
            return node

        def visit_FunctionDef(self, node):
            nonlocal validator_count
            if node.name == "validate_output":
                validator_count += 1
                return ast.copy_location(ast.parse(VALIDATOR).body[0], node)
            return self.generic_visit(node)

    tree = Adapter().visit(tree)
    if validator_count != 1 or any(value != 1 for value in counts.values()):
        raise ValueError("only the declared task validator and single literal occurrences may change")
    tree.body[0].value = ast.Constant(__doc__)
    ast.fix_missing_locations(tree)
    return tree


def main():
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument("--repo", required=True)
    args, _ = parser.parse_known_args()
    root = Path(args.repo).resolve()
    namespace = {"__name__": "_R147_support_localized_public_worker", "__file__": __file__}
    exec(compile(build_adapter(root), str(Path(__file__).resolve()), "exec"), namespace)
    namespace["main"]()


if __name__ == "__main__":
    main()
