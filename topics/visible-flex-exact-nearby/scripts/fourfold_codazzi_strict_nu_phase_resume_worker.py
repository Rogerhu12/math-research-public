"""Explicit PHI continuation after the actual zero-child materialization failure.

The first worker restores all 315 original objects successfully, reserves its
marker, and invokes materialize again.  Reuse an already restored role only
after checking its exact destination, whole byte length and SHA256.  The
scientific owner, formulas, original carrier recipe and first failure remain
unchanged.  This is one explicit continuation, never an automatic retry.
"""
from __future__ import annotations
import argparse, ast, hashlib, importlib.util, json
from pathlib import Path

TOPIC = 'topics/visible-flex-exact-nearby'
ADAPTER = TOPIC+'/scripts/fourfold_codazzi_strict_nu_phase_public_worker.py'
ADAPTER_SHA = '32569d72195ed7640bd47d2d6e1690d299e1636fb93365dea4855e28432f0eef'
FAILED = TOPIC+'/notes/strict_nu_phase_ci/run-45913335399-1/execution.json'
FAILED_SHA = '808570ee6c7e365894552cdf70e1053d613d68c0406fb570084092fd1c80cd7c'
OLD_MANIFEST = TOPIC+'/notes/2026-11-27-strict-nu-phase-complete-inputs.json'
OLD_MANIFEST_SHA = 'bb9b080191f018f9b615d89a78bcd7e00e5e728c5df02a90c505dc7376542100'


def require(ok,message):
    if not ok:raise ValueError(message)


def admitted_failure(root):
    raw,original = (root/FAILED).read_bytes(),(root/OLD_MANIFEST).read_bytes()
    require(len(raw) == 29505 and hashlib.sha256(raw).hexdigest() == FAILED_SHA
        and hashlib.sha256(original).hexdigest() == OLD_MANIFEST_SHA,
        'whole actual first failure and whole original PHI manifest')
    old,manifest = json.loads(raw),json.loads(original)
    require(old['kind'] == 'R147_complete_strict_nu_nonlocal_phase_execution_v1'
        and old['run_id'] == '45913335399' and old['run_attempt'] == '1'
        and old['manifest_sha256'] == OLD_MANIFEST_SHA
        and old['entry_checkout'] == old['event_commit'] == '69a4744bf72716b0f35a35852fd2a6880cb335ce'
        and old['complete'] is old['complete_new_response_target_set'] is False
        and old['actual_child_returncode'] is old['original_scientific_complete']
            is old['original_scientific_failure'] is None
        and old['scientific_children'] == old['completed_new_scalar_targets'] == 0
        and old['scientific_files'] == [] and old['current_input_receipts'] == manifest['files']
        and old['failure']['type'] == 'ValueError'
        and old['failure']['message'] == 'no original input silently replaced'
        and old['old_completed_targets_recomputed'] == old['old_numerical_producers_called'] == 0,
        'the complete actual failure started no scientific child and completed no phase target')
    restoration = old['historical_restoration']
    require(restoration['complete_original_files'] == 315
        and restoration['original_NP_input_files'] == 51
        and restoration['necessary_original_phase_germs'] == restoration['necessary_original_scalar_germs'] == 131
        and restoration['complete_original_error_natives'] == 2
        and restoration['whole_original_descriptors_sha256']
            == 'f85bab2f8913268a9c092659b29a7513e72f3a9ecf6989e29bfd4790e6e804f3'
        and restoration['all_original_bytes_retained_in_private_input_tree'] is True
        and restoration['old_scientific_targets_evaluated'] == 0,
        'the first complete restoration is retained as the actual historical fact')
    return old,manifest


def build_adapter(root):
    raw = (root/ADAPTER).read_bytes()
    require(hashlib.sha256(raw).hexdigest() == ADAPTER_SHA,'unchanged first whole PHI public worker')
    spec = importlib.util.spec_from_file_location('_PHI_first_public_adapter',root/ADAPTER)
    module = importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
    tree = module.build_adapter(root);replacements = 0
    expected = ast.parse('require(role not in snapshots,"no original input silently replaced")').body[0]
    reuse = ast.parse('''
if role in snapshots:
    destination = source_dir/"original-native"/topic_path(item["path"])
    require(role not in by_role and snapshots[role] == destination,
            "only the same already restored original role and path may be reused")
    retained = destination.read_bytes()
    require(len(retained) == item["bytes"] and sha(retained) == item["sha256"],
            "the complete original bytes and SHA must agree before reuse")
    continue
''').body[0]

    class SameWholeOriginal(ast.NodeTransformer):
        def visit_Expr(self,node):
            nonlocal replacements
            if ast.dump(node) == ast.dump(expected):
                replacements += 1;return ast.copy_location(reuse,node)
            return self.generic_visit(node)

    tree = SameWholeOriginal().visit(tree)
    require(replacements == 1,'only the one historical snapshot lifecycle condition changes')
    ast.fix_missing_locations(tree);return tree


def main():
    parser = argparse.ArgumentParser(add_help=False);parser.add_argument('--repo',required=True)
    args,_ = parser.parse_known_args();root = Path(args.repo).resolve()
    admitted_failure(root)
    namespace = {'__name__':'_PHI_explicit_zero_child_continuation','__file__':__file__}
    exec(compile(build_adapter(root),str(Path(__file__).resolve()),'exec'),namespace)
    namespace['main']()


if __name__ == '__main__':main()
