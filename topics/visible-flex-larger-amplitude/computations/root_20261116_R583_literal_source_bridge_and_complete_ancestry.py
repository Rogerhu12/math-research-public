#!/usr/bin/env python3
"""R616: literal-repaired R583 preparation and explicit old-source relation scopes.

The R583 adapter has exactly the missing closing quote repaired (R616).
The same six prepare_sources arguments, actual HERE and every source predicate
remain in that explicitly named full source. No original compiler installer or scientific callable is run.
The complete actual binding is written once to the caller's job-local file;
a private source child does not impose a second stdout 90000-byte transport.
Final complete source/science necessary objects retain their original limit/70.

The metadata relation accepts only the declared R584/R604 current source scope
and its exact R593 -> R589 necessary ancestry. It unwraps only the original
R588 relations at those explicit scopes, retaining the entire old reports,
wrapper key order and all existing marker addresses for an exact reverse.
No arbitrary scientific tree or raw is encoded or recovered by hash.
"""
from __future__ import annotations
import argparse
import copy
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import sys
import traceback

HERE = Path(__file__).resolve().parent
SELF = Path(__file__).resolve()
REPOSITORY = "Rogerhu12/math-research-public"
RUN_KEYS = ("GITHUB_REPOSITORY", "GITHUB_RUN_ID", "GITHUB_RUN_ATTEMPT", "GITHUB_SHA")
BRIDGE_SCHEMA = "R616-direct-literal-repaired-R583-six-argument-source-bridge-v1"
RELATION_SCHEMA = "R616-explicit-R593-R589-complete-source-relations-v1"
CURRENT_SCHEMAS = frozenset((
    "R616-literal-repaired-R583-original248-complete-source-preparation-v1-necessary-v1",
    "R584-loop-rounding-observation-complete-source-preparation-v1-necessary-v1",
    "R604-direct-R583-original248-complete-source-preparation-v1-necessary-v1",
))
PARENT_SCHEMA = "R593-live128-extended-owner-budget-complete-source-preparation-v1-necessary-v1"
OLDER_SCHEMA = "R589-complete-current-owner-named-necessary-source-preparation-v1-necessary-v1"
OLD_RELATION_SCHEMA = "R588-complete-named-source-and-root-statistics-relations-v1"
MARKER = "R588_named_metadata_row"
R583_BINDING = "R583-loop-rounding-observation-source-binding-v1"
ADAPTER = dict(file="root_20261116_loop_rounding_observation_source_literal.py", bytes=22649,
    sha256="8067ed32b24b98e5aeedeac8390d4c0356eef3a0676423fc14384a91c4533d4d")
SIX_LAYER = dict(file="root_20261116_complete_six_layer_R583_source_relations.py",
    bytes=17338,
    sha256="2a7c44446089d2136c096ffca73b8870a5b062f49f725515f5bafcb3fd40a77f")
OLD_LAYER = dict(file="root_20261116_complete_named_source_and_root_statistics_relations.py",
    bytes=19120,
    sha256="6f7cb8049e8b77b26964deb675e5868d6b374ac2e07c49b6517c8e51d7db0dad")
PARENT_PATH = ("original_parent_complete_necessary", "value")
OLDER_PATH = PARENT_PATH + ("original_parent_complete_necessary", "value")
OLDER_REPORT = "R588_complete_nested_relation"
OLDER_INVERSE = "R588_inverse_order"
CURRENT_REPORT = "R588_current_source_relation"
CURRENT_INVERSE = "R588_current_source_inverse"
CURRENT_SCOPE = ("current_source_record",)
MODULES = {}


def require(ok, message):
    if not ok:
        raise ValueError(message)


def canonical(value):
    return (json.dumps(value, sort_keys=True, ensure_ascii=True,
        separators=(",", ":"), allow_nan=False) + "\n").encode("ascii")


def identity(path):
    path = Path(path)
    require(path.is_file() and not path.is_symlink(), "Ordinary actual metadata/source file")
    path = path.resolve(strict=True)
    raw = path.read_bytes()
    return dict(file=str(path), bytes=len(raw), sha256=hashlib.sha256(raw).hexdigest())


def run_identity():
    return {name: os.environ.get(name) for name in RUN_KEYS}


def require_actions():
    require(os.environ.get("GITHUB_ACTIONS") == "true"
        and os.environ.get("GITHUB_REPOSITORY") == REPOSITORY
        and all(os.environ.get(key) for key in RUN_KEYS),
        "This is the actual public repository Actions source/metadata invocation")
    workspace = Path(os.environ["GITHUB_WORKSPACE"]).resolve(strict=True)
    require(HERE == workspace / "topics/visible-flex-larger-amplitude/computations",
        "The bridge and declared adapters use the actual checkout computations")
    return workspace


def fixed_module(desc, label):
    if label in MODULES:
        return MODULES[label]
    path = HERE / desc["file"]
    require(Path(desc["file"]).name == desc["file"]
        and path.is_file() and not path.is_symlink(),
        "Ordinary same-directory fixed metadata dependency")
    raw = path.read_bytes()
    require(len(raw) == desc["bytes"]
        and hashlib.sha256(raw).hexdigest() == desc["sha256"],
        "Complete actual fixed metadata dependency: " + desc["file"])
    name = "_R616_" + label
    spec = importlib.util.spec_from_file_location(name, path)
    require(spec is not None and spec.loader is not None, "Fixed metadata import specification")
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    require(Path(module.__file__).resolve() == path.resolve(),
        "Imported fixed metadata module has its actual source path")
    MODULES[label] = module
    return module


def prepare_to_binding(source_plan, synthesis_source_plan, product_source_plan,
        average_source_plan, reuse_source_plan, word_source_plan, binding_out):
    """One direct original source-only call, one full binding, no internal cap.

    Errors from original preparation retain their actual type, complete message,
    traceback and the original partial_source_state. Final necessary readers
    must read this complete file and must keep their original whole-body limit.
    """
    require_actions()
    original = fixed_module(ADAPTER, "original_R583")
    require(original.HERE == HERE and original.BINDING_SCHEMA == R583_BINDING,
        "The exact literal-repaired R583 source-only producer and actual HERE")
    output = Path(binding_out)
    require(not output.exists() and not output.is_symlink(),
        "One fresh actual full source binding")
    parent = output.parent.resolve(strict=True)
    runner = Path(os.environ["RUNNER_TEMP"]).resolve(strict=True)
    require(parent.is_relative_to(runner) and parent != runner,
        "The binding is inside this job's actual temporary source directory")
    arguments = tuple(Path(value) for value in (
        source_plan, synthesis_source_plan, product_source_plan,
        average_source_plan, reuse_source_plan, word_source_plan))
    # The original function itself reads/checks every plan. Do not pre-read a
    # missing plan here and thereby replace its original error/partial binding.
    code = 0
    try:
        binding = original.prepare_sources(*arguments)
    except Exception as error:
        code = 2
        original_error = dict(type=type(error).__name__, message=str(error),
            traceback=traceback.format_exc())
        binding = dict(schema=original.BINDING_SCHEMA, run=original.run_identity(),
            actual_source_root=str(original.HERE), actual_adapter=original.identity(original.SELF),
            source_preparation_complete=False, compiler_completed=False,
            scientific_evaluation_performed_by_preparation=False,
            error=original_error,
            partial_sources=original.partial_source_state(
                arguments[0], arguments[1], arguments[2], arguments[3], arguments[4]))
    # These are receipt observations after the original call, not new input
    # gates. A missing/unreadable plan keeps its full actual source error here
    # and cannot erase the binding already returned or caught from R583.
    actual_plans = []
    for path in arguments:
        try:
            actual_plans.append(dict(argument=str(path), actual_file=identity(path)))
        except Exception as error:
            actual_plans.append(dict(argument=str(path), actual_file=None,
                read_error=dict(type=type(error).__name__, message=str(error),
                    traceback=traceback.format_exc())))
    raw = canonical(binding)
    with output.open("xb") as stream:
        stream.write(raw)
    receipt = dict(schema=BRIDGE_SCHEMA, run=run_identity(), source=identity(SELF),
        actual_original_adapter=identity(HERE / ADAPTER["file"]),
        original_callable="prepare_sources",
        original_argument_names=[
            "source_plan", "synthesis_source_plan", "product_source_plan",
            "average_source_plan", "reuse_source_plan", "word_source_plan"],
        actual_six_plan_arguments=actual_plans,
        actual_binding=identity(output), actual_exit=code,
        original_preparation_returned=(code == 0),
        source_preparation_complete=binding.get("source_preparation_complete") is True,
        compiler_completed=binding.get("compiler_completed"),
        scientific_evaluation_performed_by_preparation=
            binding.get("scientific_evaluation_performed_by_preparation"),
        original_source_binding_schema_retained=True,
        complete_binding_members_not_selected_or_relabelled=True,
        original_preparation_exception_and_partial_sources_retained=True,
        source_preparation_called_exactly_once=True,
        no_ancestor_compiler_installer_called=True,
        source_only_child_has_no_full_binding_stdout_size_gate=True,
        original_final_complete_source_and_science90000_limit_and_overflow70_unchanged=True,
        no_scientific_clock_created_or_restarted=True,
        original244_internal_error_not_claimed_resolved=True)
    return binding, code, receipt


def path_get(value, path):
    node = value
    for part in path:
        if type(part) is int:
            require(isinstance(node, list) and 0 <= part < len(node),
                "Existing complete metadata list position")
        else:
            require(isinstance(part, str) and isinstance(node, dict) and part in node,
                "Existing complete metadata member")
        node = node[part]
    return node


def path_present(value, path):
    node = value
    for part in path:
        if isinstance(part, str) and isinstance(node, dict) and part in node:
            node = node[part]
        elif type(part) is int and isinstance(node, list) and 0 <= part < len(node):
            node = node[part]
        else:
            return False
    return True


def path_set(value, path, replacement):
    require(isinstance(path, (list, tuple)) and path,
        "A declared non-root source-scope location")
    parent = path_get(value, path[:-1])
    final = path[-1]
    if type(final) is int:
        require(isinstance(parent, list) and 0 <= final < len(parent),
            "Existing original metadata list position")
    else:
        require(isinstance(final, str) and isinstance(parent, dict) and final in parent,
            "Existing original metadata member")
    parent[final] = replacement


def reference_slots(value, original):
    """Record only references already created by the actual old R588 relation."""
    rows = []

    def walk(node, path):
        if isinstance(node, list):
            for index, item in enumerate(node):
                walk(item, path + [index])
        elif isinstance(node, dict):
            if MARKER in node:
                require(set(node) == {MARKER}, "An actual old marker is an exact reference")
                ref = node[MARKER]
                require(isinstance(ref, list) and len(ref) == 2
                    and isinstance(ref[0], str) and ref[0] in original.FAMILIES
                    and type(ref[1]) is int and ref[1] >= 0,
                    "An explicit original named reference, never arbitrary data coding")
                rows.append(dict(path=path, reference=copy.deepcopy(ref)))
                return
            for key, item in node.items():
                require(isinstance(key, str), "Original parsed JSON metadata keys")
                walk(item, path + [key])
    walk(value, [])
    return rows


def old_relation_eligible(container, report_key, original):
    if report_key not in container:
        return False
    report = container[report_key]
    if not isinstance(report, dict) or report.get("schema") != OLD_RELATION_SCHEMA:
        return False
    if report.get("applied") is not True or report.get("reference_member") != MARKER:
        return False
    tables = report.get("complete_named_tables")
    return isinstance(tables, dict) and all(name in original.FAMILIES for name in tables)


def unwrap_whole_R589(value, original):
    """One actual schema chain, never recursive schema guessing."""
    if not path_present(value, OLDER_PATH):
        return None
    parent = path_get(value, PARENT_PATH)
    older = path_get(value, OLDER_PATH)
    if not isinstance(parent, dict) or parent.get("schema") != PARENT_SCHEMA:
        return None
    if not isinstance(older, dict) or older.get("schema") != OLDER_SCHEMA:
        return None
    if not old_relation_eligible(older, OLDER_REPORT, original):
        return None
    wrapper_names = [key for key in (OLDER_REPORT, OLDER_INVERSE) if key in older]
    selected = {key: item for key, item in older.items() if key not in wrapper_names}
    slots = reference_slots(selected, original)
    decoded = original.restore_relation(selected, older[OLDER_REPORT])
    require(isinstance(decoded, dict) and decoded.get("schema") == OLDER_SCHEMA,
        "The old whole-scope inverse restores the same actual R589 selection")
    bundle = dict(kind="original-R589-whole-source-necessary-R588",
        container_path=list(OLDER_PATH), selected_scope_path=[],
        original_container_key_order=list(older),
        wrapper_members={key: copy.deepcopy(older[key]) for key in wrapper_names},
        original_reference_slots=slots,
        original_report_and_inverse_members_preserved=True)
    path_set(value, OLDER_PATH, decoded)
    return bundle


def unwrap_current_R584(value, original):
    """Only the original R584 current_source_record relation, not its old parent."""
    if value.get("schema") != (
            "R584-loop-rounding-observation-complete-source-preparation-v1-necessary-v1"):
        return None
    if not old_relation_eligible(value, CURRENT_REPORT, original):
        return None
    if not path_present(value, CURRENT_SCOPE):
        return None
    selected = path_get(value, CURRENT_SCOPE)
    slots = reference_slots(selected, original)
    decoded = original.restore_relation(selected, value[CURRENT_REPORT])
    wrapper_names = [key for key in (CURRENT_REPORT, CURRENT_INVERSE) if key in value]
    bundle = dict(kind="original-R584-current-source-record-R588",
        container_path=[], selected_scope_path=list(CURRENT_SCOPE),
        original_container_key_order=list(value),
        wrapper_members={key: copy.deepcopy(value[key]) for key in wrapper_names},
        original_reference_slots=slots,
        original_report_and_inverse_members_preserved=True)
    path_set(value, CURRENT_SCOPE, decoded)
    for key in wrapper_names:
        del value[key]
    return bundle


def complete_source_relation(value, source_hashes, computations):
    """Represent the exact original complete source selection plus old inverses.

    No old source/readback operation is repeated. All original reports are
    carried in the same new relation; only the declared selected scopes are
    expanded for common R600 source facts. The caller compares the entire body.
    """
    require_actions()
    require(isinstance(value, dict) and value.get("schema") in CURRENT_SCHEMAS,
        "One explicitly declared current source necessary schema")
    six = fixed_module(SIX_LAYER, "six_layer_relations")
    original = fixed_module(OLD_LAYER, "original_R588")
    require(six.MARKER == MARKER and original.MARKER == MARKER,
        "Actual unchanged reference marker contracts")
    normalized = copy.deepcopy(value)
    bundles = []
    try:
        older = unwrap_whole_R589(normalized, original)
        if older is not None:
            bundles.append(older)
        current = unwrap_current_R584(normalized, original)
        if current is not None:
            bundles.append(current)
        selected, relation = six.source_necessary_relation(
            normalized, source_hashes, computations)
        report = dict(schema=RELATION_SCHEMA, applied=True,
            source=identity(SELF), original_R588_source=copy.deepcopy(OLD_LAYER),
            actual_R600_source=copy.deepcopy(SIX_LAYER),
            complete_R600_relation=relation,
            complete_original_parent_relation_scopes=bundles,
            original_root_schema=value["schema"],
            old_relation_scopes_are_exact_declared_fields_not_generic_tree_rules=True,
            old_reports_errors_returncodes_complete_and_unknown_members_retained=True,
            original_source_generation_and_readback_not_repeated=True,
            original_reference_slots_are_existing_metadata_references_only=True,
            no_scientific_raw_or_hash_recovery=True,
            entire_candidate_body_including_this_report_must_be_strictly_smaller=True,
            original_final90000_limit_and_actual_overflow70_unchanged=True,
            inverse=(
                "Apply R616.restore_complete_source to the selected full source "
                "scope and this same-body report. It first applies the complete "
                "R600 inverse, then reverses these exact old-scope bundles, "
                "restoring every original R588 reference at its actual recorded "
                "address and every old wrapper member in original key order. "
                "The restored object is the original selected metadata, including "
                "its old relation reports, not a reinterpreted raw or inferred success."))
        return selected, report
    except Exception as error:
        # The caller keeps this complete new metadata error if it records the
        # attempt; no partial normalization replaces the complete original scope.
        return value, dict(schema=RELATION_SCHEMA, applied=False,
            source=identity(SELF), original_root_schema=value["schema"],
            original_complete_scope_retained=True,
            no_partial_inverse_or_scope_replacement=True,
            error=dict(type=type(error).__name__, message=str(error),
                traceback=traceback.format_exc()),
            scientific_success_and_size_fit_not_inferred=True)


def restore_reference_slots(decoded, slots):
    """Restore the old spelling at existing old reference positions only."""
    result = copy.deepcopy(decoded)
    seen = []
    for row in slots:
        require(isinstance(row, dict) and set(row) == {"path", "reference"},
            "One complete original reference-slot record")
        path, reference = row["path"], row["reference"]
        require(isinstance(path, list)
            and all(isinstance(p, str) or type(p) is int for p in path),
            "Original typed source metadata address")
        require(isinstance(reference, list) and len(reference) == 2
            and isinstance(reference[0], str) and type(reference[1]) is int,
            "Original reference family and row")
        require(all(path != earlier and not (
            len(path) <= len(earlier) and earlier[:len(path)] == path) and not (
            len(earlier) <= len(path) and path[:len(earlier)] == earlier)
            for earlier in seen), "Original reference positions are distinct leaves")
        seen.append(path)
        replacement = {MARKER: copy.deepcopy(reference)}
        if path:
            path_set(result, path, replacement)
        else:
            result = replacement
    return result


def restore_container_order(container, bundle):
    wrappers = bundle["wrapper_members"]
    keys = bundle["original_container_key_order"]
    require(isinstance(container, dict) and isinstance(wrappers, dict)
        and isinstance(keys, list) and all(isinstance(k, str) for k in keys)
        and len(keys) == len(set(keys)), "Complete original container and key order")
    require(not set(container).intersection(wrappers)
        and set(keys) == set(container).union(wrappers),
        "Exactly all original values and original wrapper members")
    return {key: copy.deepcopy(wrappers[key]) if key in wrappers else container[key]
            for key in keys}


def restore_complete_source(selected, report):
    """Exact original selected object, including its old relation spellings.

    The only loaded files are these fixed metadata implementation modules.
    No source fact, raw array or missing output is loaded or recovered by hash.
    """
    require(isinstance(report, dict) and report.get("schema") == RELATION_SCHEMA,
        "Actual complete R616 relation")
    if report.get("applied") is False:
        return selected
    require(report.get("applied") is True, "Explicit applied R604 representation")
    six = fixed_module(SIX_LAYER, "six_layer_relations")
    result = six.restore_relation(selected, report["complete_R600_relation"])
    result = copy.deepcopy(result)
    for bundle in reversed(report["complete_original_parent_relation_scopes"]):
        kind = bundle["kind"]
        require(bundle.get("original_report_and_inverse_members_preserved") is True,
            "Original complete report wrapper retained")
        if kind == "original-R589-whole-source-necessary-R588":
            require(bundle["container_path"] == list(OLDER_PATH)
                and bundle["selected_scope_path"] == [],
                "Exact original R593-to-R589 whole-scope address")
            container = path_get(result, OLDER_PATH)
            container = restore_reference_slots(container, bundle["original_reference_slots"])
            container = restore_container_order(container, bundle)
            path_set(result, OLDER_PATH, container)
        elif kind == "original-R584-current-source-record-R588":
            require(bundle["container_path"] == []
                and bundle["selected_scope_path"] == list(CURRENT_SCOPE),
                "Exact original R584 current-source scope")
            container = restore_reference_slots(
                path_get(result, CURRENT_SCOPE), bundle["original_reference_slots"])
            path_set(result, CURRENT_SCOPE, container)
            result = restore_container_order(result, bundle)
        else:
            raise ValueError("An undeclared old source scope cannot be reconstructed")
    require(isinstance(result, dict)
        and result.get("schema") == report["original_root_schema"],
        "The same original selected source schema is restored")
    return result


def choose_complete_body(original_body, candidate_body, serialize):
    """Delegate the original strict entire-body choice, never a local size guess."""
    return fixed_module(SIX_LAYER, "six_layer_relations").choose_complete_body(
        original_body, candidate_body, serialize)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-plan", type=Path, required=True)
    parser.add_argument("--synthesis-source-plan", type=Path, required=True)
    parser.add_argument("--product-source-plan", type=Path, required=True)
    parser.add_argument("--average-source-plan", type=Path, required=True)
    parser.add_argument("--reuse-source-plan", type=Path, required=True)
    parser.add_argument("--word-source-plan", type=Path, required=True)
    parser.add_argument("--binding-out", type=Path, required=True)
    parser.add_argument("--bridge-receipt-out", type=Path, required=True)
    args = parser.parse_args()
    try:
        binding, code, receipt = prepare_to_binding(
            args.source_plan, args.synthesis_source_plan, args.product_source_plan,
            args.average_source_plan, args.reuse_source_plan, args.word_source_plan,
            args.binding_out)
        target = args.bridge_receipt_out
        require(not target.exists() and not target.is_symlink(),
            "One fresh complete source bridge receipt")
        require(target.parent.resolve(strict=True) == args.binding_out.parent.resolve(strict=True),
            "Bridge and full binding belong to the same temporary source directory")
        with target.open("xb") as stream:
            stream.write(canonical(receipt))
        # Internal stdout is an actual source-return receipt, not a second
        # public necessary body or a successful substitute for the full binding.
        print(json.dumps(dict(event="R616_literal_repaired_source_bridge_return",
            schema=BRIDGE_SCHEMA, actual_exit=code,
            source_preparation_complete=receipt["source_preparation_complete"],
            actual_binding=receipt["actual_binding"], actual_bridge_receipt=identity(target),
            original_error=binding.get("error"),
            final_complete_necessary_scope_still_unpaid=True), ensure_ascii=True), flush=True)
        return code
    except Exception as error:
        print(json.dumps(dict(event="R616_source_bridge_unreturned",
            schema=BRIDGE_SCHEMA, actual_exit=2,
            error=dict(type=type(error).__name__, message=str(error),
                traceback=traceback.format_exc()),
            complete_source_binding_or_scientific_success_not_invented=True,
            cleanup_permitted=False), ensure_ascii=True), flush=True)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
